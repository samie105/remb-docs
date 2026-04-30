---
title: "Build a subscriptions integration"
source: "https://docs.stripe.com/billing/subscriptions/build-subscriptions?payment-ui=mobile&platform=react-native"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:17:06.729Z"
content_hash: "0053ded186ce5a2a2d480cc06cf100c6c55cbf34ba4919d847ec321624501c76"
---

Learn how to sell fixed-price [subscriptions](https://docs.stripe.com/billing/subscriptions/creating). You’ll use the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment) to create a custom payment form that you embed in your app.

![Fixed-price subscription page with Mobile Payment Element](https://b.stripecdn.com/docs-statics-srv/assets/fixed-price-collect-payment-details-mobile.b11cdc8fa8952d753238df4df3375fa6.png)

#### Note

If you’re selling digital products or services that are consumed within your app (for example, subscriptions, in-game currencies, game levels, access to premium content, or unlocking a full version), you must use Apple’s in-app purchase APIs. This rule has some exceptions, including one-to-one personal services and [apps based in specific regions](https://support.stripe.com/questions/changes-to-mobile-app-store-rules). See the [App Store review guidelines](https://developer.apple.com/app-store/review/guidelines/#payments) for more information.

## Build your subscription

This guide shows you how to:

*   Model your business by building a product catalog.
*   Create a registration process to add customers.
*   Create subscriptions and collect payment information.
*   Test and monitor the status of payments and subscriptions.
*   Let customers change their plan or cancel the subscription.
*   Learn how to use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode) to access enhanced billing behavior and additional features.

## How to model it on Stripe

[Subscriptions](https://docs.stripe.com/api/subscriptions) simplify your billing by automatically creating [Invoices](https://docs.stripe.com/api/invoices) and [PaymentIntents](https://docs.stripe.com/api/payment_intents) for you. To create and activate a subscription, you need to first create a [Product](https://docs.stripe.com/api/products) to model what’s being sold, and a [Price](https://docs.stripe.com/api/prices) which determines the interval and amount to charge. You also need either a customer-configured `Account` object or a `Customer` object to store [PaymentMethods](https://docs.stripe.com/api/payment_methods) used to make each recurring payment.

default\_payment\_method

`pm_1234`

customer\_account

`acct_1234`

items.data.price

`price_1234`

contact\_email

`jennyrosen@example.com`

customer\_account

`acct_1234`

A diagram illustrating common billing objects and their relationships

### API object definitions

[](#install-setup)

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

`yarn add @stripe/stripe-react-native`

Next, install some other necessary dependencies:

*   For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
*   For Android, there are no more dependencies to install.

#### Note

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

`import { useState, useEffect } from 'react'; import { StripeProvider } from '@stripe/stripe-react-native';  function App() {   const [publishableKey, setPublishableKey] = useState('');    const fetchPublishableKey = async () => {     const key = await fetchKey(); // fetch key from your server here     setPublishableKey(key);   };    useEffect(() => {     fetchPublishableKey();   }, []);    return (     <StripeProvider       publishableKey={publishableKey}       merchantIdentifier="merchant.identifier" // required for Apple Pay       urlScheme="your-url-scheme" // required for 3D Secure and bank redirects     >       {/* Your app code here */}     </StripeProvider>   ); }`

#### Note

Use your API [test keys](https://docs.stripe.com/keys#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys#test-live-modes) keys when you publish your app.

And then install the Stripe CLI. The CLI provides webhook testing and you can run it to make API calls to Stripe. This guide shows how to use the CLI to set up a pricing model in a later section.

For additional install options, see [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli).

[](#create-pricing-model)

[Recurring pricing models](https://docs.stripe.com/products-prices/pricing-models) represent the products or services you sell, how much they cost, what currency you accept for payments, and the service period for subscriptions. To build the pricing model, create [products](https://docs.stripe.com/api/products) (what you sell) and [prices](https://docs.stripe.com/api/prices) (how much and how often to charge for your products).

This example uses flat-rate pricing with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. To add a one-time charge for something like a setup fee, create a third product with a one-time price.

Each product bills at monthly intervals. The price for the Basic product is 5 USD. The price for the Premium product is 15 USD. See the [flat rate pricing](https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing) guide for an example with three tiers.

Go to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create two products. Add one price for each product, each with a monthly recurring billing period:

*   Premium product: Premium service with extra features
    
    *   Price: Flat rate | 15 USD
*   Basic product: Basic service with minimum features
    
    *   Price: Flat rate | 5 USD

After you create the prices, record the price IDs so you can use them in other steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the **Copy to live mode** button at the top right of the page to clone your product from [a sandbox to live mode](https://docs.stripe.com/keys#test-live-modes).

[](#create-customer)

Stripe needs a customer for each subscription. In your application front end, collect any necessary information from your users and pass it to the backend.

If you need to collect address details, the Address Element enables you to collect a shipping or billing address for your customers. For more information on the Address Element, visit the [Address Element](https://docs.stripe.com/elements/address-element) page.

``import React from 'react'; import {View, TextInput, StyleSheet, Button, Platform} from 'react-native';  function RegisterView() {   const [email, setEmail] = React.useState('');    const createCustomer = async () => {     const apiEndpoint =       Platform.OS === 'ios' ? '[http://localhost:4242](http://localhost:4242/)' : '[http://10.0.2.2:4567](http://10.0.2.2:4567/)';     const response = await fetch(`${apiEndpoint}/create-customer`, {       method: 'POST',       headers: {         'Content-Type': 'application/json',       },       body: JSON.stringify({         email: email,       }),     });     if (response.status === 200) {       const customer = await response.json();       console.log(customer);     }   };    return (     <View>       <TextInput         style={styles.input}         placeholder="Email"         value={email}         onChangeText={setEmail}       />       <Button         title="Register"         onPress={async () => {           await createCustomer();         }}       />     </View>   ); }  const styles = StyleSheet.create({   input: {     height: 40,     margin: 12,     borderWidth: 1,     padding: 10,   }, });  export default RegisterView;``

On the server, create the Stripe customer object.

#### Use the Accounts v2 API to represent customers

`curl -X POST https://api.stripe.com/v2/core/accounts \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: 2026-04-22.preview" \   --json '{     "contact_email": "jenny.rosen@example.com",     "display_name": "Jenny Rosen",     "identity": {         "individual": {             "given_name": "Jenny Rosen",             "address": {                 "city": "San Francisco",                 "country": "US",                 "line1": "123 Main Street",                 "postal_code": "94605",                 "state": "CA"             }         }     },     "configuration": {         "customer": {             "capabilities": {                 "automatic_indirect_tax": {                     "requested": true                 }             },             "shipping": {                 "address": {                     "city": "San Francisco",                     "country": "US",                     "line1": "123 Main Street",                     "postal_code": "94605",                     "state": "CA"                 }             }         }     },     "include": [         "configuration.customer",         "identity"     ]   }'`

[](#create-subscription)

#### Note

Let your new customer choose a plan and then create the subscription—in this guide, they choose between Basic and Premium.

In your app, pass the selected price ID and the ID of the customer record to the backend.

``const createSubscription = async (priceId, customerAccountId) => {   const apiEndpoint =     Platform.OS === 'ios' ? '[http://localhost:4242](http://localhost:4242/)' : '[http://10.0.2.2:4567](http://10.0.2.2:4567/)';   const response = await fetch(`${apiEndpoint}/create-subscription`, {     method: 'POST',     headers: {       'Content-Type': 'application/json',     },     body: JSON.stringify({       priceId: priceId,       customerAccountId: customerAccountId,     }),   });   if (response.status === 200) {     const subscription = await response.json();     return subscription;   } };``

On the backend, create the subscription with status `incomplete` using `payment_behavior=default_incomplete`. Then return the `client_secret` from the subscription’s first [payment intent](https://docs.stripe.com/payments/payment-intents) to the frontend to complete payment by expanding the[`confirmation_secret`](https://docs.stripe.com/api/invoices/object#invoice_object-confirmation_secret) on the latest invoice of the subscription.

To enable [improved subscription behavior](https://docs.stripe.com/billing/subscriptions/billing-mode), set `billing_mode[type]` to `flexible`. You must use Stripe API version [2025-06-30.basil](https://docs.stripe.com/changelog/basil#2025-06-30.basil) or later.

Set [save\_default\_payment\_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method) to `on_subscription` to save the payment method as the default for a subscription when a payment succeeds. Saving a default payment method increases the success rate of future subscription payments.

The following example creates a `Subscription` and expands the `confirmation_secret` from its latest invoice in the response. That lets you pass the secret to the front end to confirm the payment.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer_account=  {{CUSTOMER_ACCOUNT_ID}}  " \   -d "items[0][price]=  {{PRICE_ID}}  " \   -d payment_behavior=default_incomplete \  -d "payment_settings[save_default_payment_method]=on_subscription" \   -d "billing_mode[type]=flexible" \   -d "expand[0]=latest_invoice.confirmation_secret"`

#### Note

If you’re using a [multi-currency Price](https://docs.stripe.com/products-prices/pricing-models#multicurrency), use the [currency](https://docs.stripe.com/api/subscriptions/create#create_subscription-currency) parameter to tell the Subscription which of the Price’s currencies to use. (If you omit the `currency` parameter, then the Subscription uses the Price’s default currency.)

The Subscription is now `inactive` and awaiting payment. The following example response highlights the minimum fields to store, but you can store whatever your application frequently accesses.

`{   "id": "sub_JgRjFjhKbtD2qz",   "object": "subscription",   "application_fee_percent": null,   "automatic_tax": {     "disabled_reason": null,     "enabled": false,     "liability": "null"   },   "billing_cycle_anchor": 1623873347,`

### Update your server endpoint

Add ephemeral key creation to the subscription endpoint and return it in the response:

`ephemeral_key = Stripe::EphemeralKey.create(   {customer_account: customer_account_id},   {stripe_version: '2026-03-25.dahlia'} )  {   subscriptionId: subscription.id,   clientSecret: subscription.latest_invoice.confirmation_secret.client_secret,   ephemeralKey: ephemeral_key.secret,   customerAccountId: customer_account_id, }.to_json`

### Update your response model

`interface SubscriptionsResponse {   subscriptionId: string;   clientSecret: string;   ephemeralKey: string;   customerAccountId: string; }`

### Pass the customer configuration to PaymentSheet

Add the following parameters when initializing PaymentSheet:

`await initPaymentSheet({   paymentIntentClientSecret: clientSecret,   customerAccountId: customerAccountId,   customerEphemeralKeySecret: ephemeralKey,   // ... other parameters });`

[](#collect-payment)

Use the [Payment Sheet](https://docs.stripe.com/payments/mobile/payment-sheet) to collect payment details and activate the subscription. You can customize Elements to match the look and feel of your application.

The Payment Sheet securely collects all necessary payment details for a wide variety of payments methods. Learn about the [supported payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support) for Payment Sheet and Subscriptions.

### Add the Payment Element to your app

#### Note

Initialize and present the Mobile Payment Element using the PaymentSheet class.

``import React from 'react'; import {useStripe, PaymentSheetError} from '@stripe/stripe-react-native'; import {View, Button} from 'react-native';  function SubscribeView({clientSecret}) {   const {initPaymentSheet, presentPaymentSheet} = useStripe();    React.useEffect(() => {     const initializePaymentSheet = async () => {       const {error} = await initPaymentSheet({         paymentIntentClientSecret: clientSecret,         returnURL: 'stripe-example://payment-sheet',         // Set `allowsDelayedPaymentMethods` to true if your business handles         // delayed notification payment methods like US bank accounts.         allowsDelayedPaymentMethods: true,       });       if (error) {         // Handle error       }     };      initializePaymentSheet();   }, [clientSecret, initPaymentSheet]);    return (     <View>       <Button         title="Subscribe"         onPress={async () => {           const {error} = await presentPaymentSheet();           if (error) {             if (error.code === PaymentSheetError.Failed) {               // Handle failed             } else if (error.code === PaymentSheetError.Canceled) {               // Handle canceled             }           } else {             // Payment succeeded           }         }}       />     </View>   ); }  export default SubscribeView;``

The Mobile Payment Element renders a sheet that allows your customer to select a payment method. The form automatically collects all necessary payments details for the payment method that they select.

Setting `allowsDelayedPaymentMethods` to true allows [delayed notification](https://docs.stripe.com/payments/payment-methods#payment-notification) payment methods like US bank accounts. For these payment methods, the final payment status isn’t known when the `PaymentSheet` completes, and instead succeeds or fails later. If you support these types of payment methods, inform the customer their order is confirmed and only fulfill their order (for example, ship their product) when the payment is successful.

You can customize the Payment Element to match the design of your app by using the [`appearance` property](https://docs.stripe.com/elements/appearance-api/mobile?platform=ios) your `PaymentSheet.Configuration` object.

### Confirm payment

The Mobile Payment Element creates a PaymentMethod and confirms the incomplete Subscription’s first PaymentIntent, causing a charge to be made. If [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication) (SCA) is required for the payment, the Payment Element handles the authentication process before confirming the PaymentIntent.

[](#react-native-set-up-return-url)

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types _require_ a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

To provide a return URL:

1.  [Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme) a custom URL. Universal links aren’t supported.
2.  [Configure](https://reactnative.dev/docs/linking) your custom URL.
3.  Set up your root component to forward the URL to the Stripe SDK as shown below.

#### Note

`import { useEffect, useCallback } from 'react'; import { Linking } from 'react-native'; import { useStripe } from '@stripe/stripe-react-native';  export default function MyApp() {   const { handleURLCallback } = useStripe();    const handleDeepLink = useCallback(     async (url: string | null) => {       if (url) {         const stripeHandled = await handleURLCallback(url);         if (stripeHandled) {           // This was a Stripe URL - you can return or add extra handling here as you see fit         } else {           // This was NOT a Stripe URL – handle as you normally would         }       }     },     [handleURLCallback]   );    useEffect(() => {     const getUrlAsync = async () => {       const initialUrl = await Linking.getInitialURL();       handleDeepLink(initialUrl);     };      getUrlAsync();      const deepLinkListener = Linking.addEventListener(       'url',       (event: { url: string }) => {         handleDeepLink(event.url);       }     );      return () => deepLinkListener.remove();   }, [handleDeepLink]);    return (     <View>       <AwesomeAppComponent />     </View>   ); }`

Additionally, set the `returnURL` when you call the `initPaymentSheet` method:

`await initPaymentSheet({   ...   returnURL: 'your-app://stripe-redirect',   ... });`

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

[](#webhooks)

To complete the integration, you need to process [webhooks](https://docs.stripe.com/webhooks) sent by Stripe. These are events triggered whenever state inside of Stripe changes, such as subscriptions creating new invoices. In your application, set up an HTTP handler to accept a POST request containing the webhook event, and verify the signature of the event:

During development, use the Stripe CLI to [observe webhooks and forward them to your application](https://docs.stripe.com/webhooks#test-webhook). Run the following in a new terminal while your development app is running:

`stripe listen --forward-to localhost:4242/webhook`

For production, set up a webhook endpoint URL in the Dashboard, or use the [Webhook Endpoints API](https://docs.stripe.com/api/webhook_endpoints).

You need to listen to a few events to complete the remaining steps in this guide. See [Subscription events](https://docs.stripe.com/billing/subscriptions/webhooks#events) for more details about subscription-specific webhooks.

[](#provision-access)

Now that the subscription is active, give your user access to your service. To do this, listen to the `customer.subscription.created`, `customer.subscription.updated`, and `customer.subscription.deleted` events. These events pass a subscription object which contains a `status` field indicating whether the subscription is active, past due, or canceled. See [the subscription lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle) for a complete list of statuses.

In your webhook handler:

1.  Verify the subscription status. If it’s `active` then your user has paid for your product.
2.  Check the product the customer subscribed to and grant access to your service. Checking the product instead of the price gives you more flexibility if you need to change the pricing or billing interval.
3.  Store the `product.id`, `subscription.id` and `subscription.status` in your database along with the `customer.id` you already saved. Check this record when determining which features to enable for the user in your application.

The state of a subscription might change at any point during its lifetime, even if your application doesn’t directly make any calls to Stripe. For example, a renewal might fail due to an expired credit card, which puts the subscription into a past due state. Or, if you implement the [customer portal](https://docs.stripe.com/customer-management), a user might cancel their subscription without directly visiting your application. Implementing your handler correctly keeps your application state in sync with Stripe.

[](#cancel-subscription)

It’s common to allow customers to cancel their subscriptions. This example adds a cancellation option to the account settings page.

The example collects the subscription ID on the frontend, but your application can get this information from your database for your logged in user.

![Sample subscription cancelation interface.](https://b.stripecdn.com/docs-statics-srv/assets/fixed-price-subscriptions-guide-account-settings.6559626ba4b434826a67abfea165e097.png)

Account settings with the ability to cancel the subscription

``const cancelSubscription = async subscriptionId => {   const apiEndpoint =     Platform.OS === 'ios' ? '[http://localhost:4242](http://localhost:4242/)' : '[http://10.0.2.2:4567](http://10.0.2.2:4567/)';   const response = await fetch(`${apiEndpoint}/cancel-subscription`, {     method: 'POST',     headers: {       'Content-Type': 'application/json',     },     body: JSON.stringify({       subscriptionId: subscriptionId,     }),   });   if (response.status === 200) {     const subscription = await response.json();     return subscription;   } };``

On the backend, define the endpoint for your app to call.

`# Don't put any keys in code. See [https://docs.stripe.com/keys-best-practices.](https://docs.stripe.com/keys-best-practices) # Find your keys at [https://dashboard.stripe.com/apikeys.](https://dashboard.stripe.com/apikeys) client = Stripe::StripeClient.new(`

`'sk_test_REDACTED'`

`)  post '/cancel-subscription' do   content_type 'application/json'   data = JSON.parse request.body.read    deleted_subscription = client.v1.subscriptions.  cancel  (data['subscriptionId'])    deleted_subscription.to_json end`

Your backend receives a `customer.subscription.deleted` event.

After the subscription is canceled, update your database to remove the Stripe subscription ID you previously stored, and limit access to your service.

When a subscription is canceled, it can’t be reactivated. Instead, collect updated billing information from your customer, update their default payment method, and create a new subscription with their existing customer record.

[](#test)

### Test payment methods

Use the following table to test different payment methods and scenarios.

Payment method

Scenario

How to test

BECS Direct Debit

Your customer successfully pays with BECS Direct Debit.

Fill out the form using the account number `900123456` and BSB `000000`. The confirmed PaymentIntent initially transitions to `processing`, then transitions to the `succeeded` status three minutes later.

BECS Direct Debit

Your customer’s payment fails with an `account_closed` error code.

Fill out the form using the account number `111111113` and BSB `000000`.

Credit card

The card payment succeeds and doesn’t require authentication.

Fill out the credit card form using the credit card number `4242 4242 4242 4242` with any expiration, CVC, and postal code.

Credit card

The card payment requires [authentication](https://docs.stripe.com/strong-customer-authentication).

Fill out the credit card form using the credit card number `4000 0025 0000 3155` with any expiration, CVC, and postal code.

Credit card

The card is declined with a decline code like `insufficient_funds`.

Fill out the credit card form using the credit card number `4000 0000 0000 9995` with any expiration, CVC, and postal code.

SEPA Direct Debit

Your customer successfully pays with SEPA Direct Debit.

Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later.

SEPA Direct Debit

Your customer’s PaymentIntent status transitions from `processing` to `requires_payment_method`.

Fill out the form using the account number `AT861904300235473202`.

### Monitor events

Set up webhooks to listen to subscription change events, such as upgrades and cancellations. Learn more about [subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks). You can view events in the [Dashboard](https://dashboard.stripe.com/test/events) or with the [Stripe CLI](https://docs.stripe.com/webhooks#test-webhook).

For more details, see [testing your Billing integration](https://docs.stripe.com/billing/testing).

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide services to you, prevent fraud, and improve its services. This includes using cookies and IP addresses to identify which Elements a customer saw during a single checkout session. You’re responsible for disclosing and obtaining all rights and consents necessary for Stripe to use data in these ways. For more information, visit our [privacy center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).
