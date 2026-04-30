---
title: "Apple Pay"
source: "https://docs.stripe.com/apple-pay"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:57:39.813Z"
content_hash: "93b2aea26486aea3a3dd252f8f9df78e8cc44306c53e89bf687ee8a23af5639d"
---

Apple Pay is compatible with most Stripe products and features. Stripe users can accept [Apple Pay](https://stripe.com/apple-pay) in iOS applications in iOS 9 and above, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and [pricing](https://stripe.com/pricing/local-payment-methods#apple-pay) is the same as for other card transactions.

Apple Pay is available to cardholders at participating banks in supported countries. For more information, refer to Apple’s [participating banks](https://support.apple.com/en-us/ht204916) documentation.

This guide explains how to configure your app to accept Apple Pay directly for physical goods, services, and other eligible items. Stripe processes these payments, and you pay only Stripe’s [processing fees](https://stripe.com/pricing).

For digital products, content, and subscriptions sold in the United States or European Economic Area (EEA), your app can accept Apple Pay by redirecting to an external payment page. You can use the following payment UIs:

In other regions, your app can’t accept Apple Pay for digital products, content, or subscriptions.

Stripe offers a variety of methods to add Apple Pay as a payment method. For integration details, select the method you prefer:

#### Note

With the [Stripe iOS SDK](https://github.com/stripe/stripe-ios), you can accept both Apple Pay and traditional credit card payments. Before starting, you need to be enrolled in the [Apple Developer Program](https://developer.apple.com/programs/). Next, follow these steps:

1.  [Set up Stripe](#setup)
2.  [Register for an Apple Merchant ID](#merchantid)
3.  [Create a new Apple Pay certificate](#csr)
4.  [Integrate with Xcode](#xcode-pay)
5.  [Check if Apple Pay is supported](#check-if-apple-pay-supported)
6.  [Create the payment request](#create-payment-request)
7.  [Present the payment sheet](#present-payment-sheet)
8.  [Submit the payment to Stripe](#handle-payment)

[](#setup)

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

`# Available as a gem sudo gem install stripe`

`# If you use bundler, you can add this line to your Gemfile gem 'stripe'`

### Client-side

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

To install the SDK, follow these steps:

1.  In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
2.  Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
3.  Add the **StripeApplePay** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### Note

For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

`import UIKit import StripeApplePay  @main class AppDelegate: UIResponder, UIApplicationDelegate {      func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {         StripeAPI.defaultPublishableKey =` 

`"pk_test_REDACTED"`

        `// do any other necessary launch configuration         return true     } }`

#### Note

Use your [test keys](https://docs.stripe.com/keys#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys#test-live-modes) keys when you publish your app.

[](#merchantid)

Obtain an Apple Merchant ID by [registering for a new identifier](https://developer.apple.com/account/resources/identifiers/add/merchant) on the Apple Developer website.

Fill out the form with a description and identifier. Your description is for your own records and you can modify it in the future. Stripe recommends using the name of your app as the identifier (for example, `merchant.com.{{YOUR_APP_NAME}}`).

[](#csr)

Create a certificate for your app to encrypt payment data.

Go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard, click **Add new application**, and follow the guide.

Download a Certificate Signing Request (CSR) file to get a secure certificate from Apple that allows you to use Apple Pay.

One CSR file must be used to issue exactly one certificate. If you switch your Apple Merchant ID, you must go to the [iOS Certificate Settings](https://dashboard.stripe.com/settings/ios_certificates) in the Dashboard to obtain a new CSR and certificate.

[](#xcode-pay)

Add the Apple Pay capability to your app. In Xcode, open your project settings, click the **Signing & Capabilities** tab, and add the **Apple Pay** capability. You might be prompted to log in to your developer account at this point. Select the merchant ID you created earlier, and your app is ready to accept Apple Pay.

![](https://b.stripecdn.com/docs-statics-srv/assets/xcode.a701d4c1922d19985e9c614a6f105bf1.png)

Enable the Apple Pay capability in Xcode

[](#check-if-apple-pay-supported)

Before displaying Apple Pay as a payment option in your app, determine if the user’s device supports Apple Pay and that they have a card added to their wallet:

CheckoutViewController.swift

`import StripeApplePay import PassKit  class CheckoutViewController: UIViewController, ApplePayContextDelegate {     let applePayButton: PKPaymentButton = PKPaymentButton(paymentButtonType: .plain, paymentButtonStyle: .black)      override func viewDidLoad() {         super.viewDidLoad()         // Only offer Apple Pay if the customer can pay with it         applePayButton.isHidden = !StripeAPI.deviceSupportsApplePay()         applePayButton.addTarget(self, action: #selector(handleApplePayButtonTapped), for: .touchUpInside)     }      // ...continued in next step }`

[](#create-payment-request)

When the user taps the **Apple Pay** button, call [StripeAPI paymentRequestWithMerchantIdentifier:country:currency:](https://stripe.dev/stripe-ios/stripe-payments/Classes/StripeAPI.html#/c:@M@StripeCore@objc\(cs\)StripeAPI\(cm\)paymentRequestWithMerchantIdentifier:country:currency:) to create a [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest).

Then, configure the `PKPaymentRequest` to display your business name and the total. You can also collect information like billing details or shipping information.

See [Apple’s documentation](https://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/checkout-and-payment/#customize-the-payment-sheet) for full guidance on how to customize the payment request.

CheckoutViewController.swift

`func handleApplePayButtonTapped() {     let merchantIdentifier = "merchant.com.your_app_name"     let paymentRequest = StripeAPI.paymentRequest(withMerchantIdentifier: merchantIdentifier, country: "US", currency: "USD")      // Configure the line items on the payment request     paymentRequest.paymentSummaryItems = [         // The final line should represent your company;         // it'll be prepended with the word "Pay" (that is, "Pay iHats, Inc $50")         PKPaymentSummaryItem(label: "iHats, Inc", amount: 50.00),     ]     // ...continued in next step }`

[](#present-payment-sheet)

Create an [STPApplePayContext](https://stripe.dev/stripe-ios/stripe-applepay/Classes/STPApplePayContext.html) instance with the `PKPaymentRequest` and use it to present the Apple Pay sheet:

CheckoutViewController.swift

`func handleApplePayButtonTapped() {     // ...continued from previous step      // Initialize an STPApplePayContext instance     if let applePayContext = STPApplePayContext(paymentRequest: paymentRequest, delegate: self) {         // Present Apple Pay payment sheet         applePayContext.presentApplePay(on: self)     } else {         // There is a problem with your Apple Pay configuration     } }`

Apple requires that user gestures trigger the Apple Pay modal (for example, clicking a button or interacting with the form). Make sure your code adheres to the following:

*   Invoke the payment sheet directly with a user activation event.
*   Add the code for the payment sheet at or near the top of your user gesture event handler, before any asynchronous or long-running code.
*   Set a reasonable time limit to call `confirmPayment` after the user gesture.

[

## Submit the payment to Stripe



](#handle-payment)

### Server-side

Make an endpoint that creates a PaymentIntent with an [amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount) and [currency](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-currency). Always decide how much to charge on the server side, a trusted environment, as opposed to the client side. This prevents malicious customers from choosing their own prices.

`curl https://api.stripe.com/v1/payment_intents \   -u` 

`sk_test_REDACTED`

`: \   -d "amount"=1099 \   -d "currency"="usd"`

### Client-side

Implement `applePayContext(_:didCreatePaymentMethod:paymentInformation:)` to return the PaymentIntent client secret retrieved from the endpoint above, or throw an error if the request fails.

After you return the client secret, `STPApplePayContext` completes the payment, dismisses the Apple Pay sheet, and calls `applePayContext(_:didCompleteWithStatus:error:)` with the status of the payment. Implement this method to show a receipt to your customer.

CheckoutViewController.swift

`extension CheckoutViewController {     func applePayContext(_ context: STPApplePayContext, didCreatePaymentMethod paymentMethod: StripeAPI.PaymentMethod, paymentInformation: PKPayment) async throws -> String {         let clientSecret = try await ... // Retrieve the PaymentIntent client secret from your backend (see Server-side step above)         // Return the client secret or throw an error         return clientSecret     }      func applePayContext(_ context: STPApplePayContext, didCompleteWith status: STPApplePayContext.PaymentStatus, error: Error?) {           switch status {         case .success:             // Payment succeeded, show a receipt view             break         case .error:             // Payment failed, show the error             break         case .userCancellation:             // User canceled the payment             break         @unknown default:             fatalError()         }     } }`

Finally, [handle post-payment events](https://docs.stripe.com/payments/accept-a-payment?payment-ui=mobile&platform=ios#ios-post-payment) to do things like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

### Troubleshooting

If you’re seeing errors from the Stripe API when attempting to create tokens, you most likely have a problem with your Apple Pay Certificate. You’ll need to generate a new certificate and upload it to Stripe, as described on this page. Make sure you use a CSR obtained from your Dashboard and not one you generated yourself. Xcode often incorrectly caches old certificates, so in addition to generating a new certificate, Stripe recommends creating a new Apple Merchant ID as well.

If you receive the error:

> You haven’t added your Apple merchant account to Stripe

it’s likely your app is sending data encrypted with a previous (non-Stripe) CSR/Certificate. Make sure any certificates generated by non-Stripe CSRs are revoked under your Apple Merchant ID. If this doesn’t resolve the issue, delete the merchant ID in your Apple account and re-create it. Then, create a new certificate based on the same (Stripe-provided) CSR that was previously used. You don’t need to upload this new certificate to Stripe. When finished, toggle the Apple Pay Credentials off and on in your app to ensure they refresh properly.

## App Clips

The `StripeApplePay` module is a lightweight Stripe SDK optimized for use in an [App Clip](https://developer.apple.com/app-clips/). Follow [the above steps](https://docs.stripe.com/apple-pay?platform=ios#accept) to add the `StripeApplePay` module to your App Clip’s target.

#### Note

The `StripeApplePay` module is only supported in Swift. Objective-C users must import `STPApplePayContext` from the `Stripe` module.

### Migrating from STPApplePayContext

If you’re an existing user of `STPApplePayContext` and wish to switch to the lightweight Apple Pay SDK, follow these steps:

1.  In your App Clip target’s dependencies, replace the `Stripe` module with the `StripeApplePay` module.
2.  In your code, replace `import Stripe` with `import StripeApplePay`.
3.  Replace your usage of `STPApplePayContextDelegate` with the new `ApplePayContextDelegate` protocol.
4.  Change your implementation of `applePayContext(_:didCreatePaymentMethod:)` to accept a `StripeAPI.PaymentMethod`.
5.  Change your implementation of `applePayContext(_:didCompleteWith:error:)` to accept an `STPApplePayContext.PaymentStatus`.

`import Stripe  class CheckoutViewController: UIViewController, STPApplePayContextDelegate {     func applePayContext(_ context: STPApplePayContext,       didCreatePaymentMethod paymentMethod: STPPaymentMethod,       paymentInformation: PKPayment,     ) async throws -> String {         // ...     }      func applePayContext(_ context: STPApplePayContext,       didCompleteWith status: STPPaymentStatus,       error: Error?) {         // ...     } }`

`import StripeApplePay  class CheckoutViewController: UIViewController, ApplePayContextDelegate {     func applePayContext(_ context: STPApplePayContext,       didCreatePaymentMethod paymentMethod: StripeAPI.PaymentMethod,       paymentInformation: PKPayment         // ...     } async throws -> String {      func applePayContext(_ context: STPApplePayContext,       didCompleteWith status: STPApplePayContext.PaymentStatus,       error: Error?) {         // ...     } }`

## Recurring payments

In iOS 16 or later, you can adopt [merchant tokens](https://developer.apple.com/apple-pay/merchant-tokens/) by setting the `recurringPaymentRequest` or `automaticReloadPaymentRequest` properties on `PKPaymentRequest`.

Recurring payments can use saved payment methods for [off-session transactions](https://docs.stripe.com/apple-pay/apple-pay-recurring#set-up-off-session-payments) only.

CheckoutViewController.swift

`extension CheckoutViewController {   func handleApplePayButtonTapped() {     let request = StripeAPI.paymentRequest(withMerchantIdentifier: merchantIdentifier, country: "US", currency: "USD")      let billing = PKRecurringPaymentSummaryItem(label: "My Subscription", amount: NSDecimalNumber(string: "59.99"))     billing.startDate = Date()     billing.endDate = Date().addingTimeInterval(60 * 60 * 24 * 365)     billing.intervalUnit = .month      request.recurringPaymentRequest = PKRecurringPaymentRequest(paymentDescription: "Recurring",                                                                 regularBilling: billing,                                                                 managementURL: URL(string: "[https://my-backend.example.com/customer-portal](https://my-backend.example.com/customer-portal)")!)     request.recurringPaymentRequest?.billingAgreement = "You'll be billed $59.99 every month for the next 12 months. To cancel at any time, go to Account and click 'Cancel Membership.'"     request.paymentSummaryItems = [billing]   } }`

To learn more about how to use recurring payments with Apple Pay, see [Apple’s PassKit documentation](https://developer.apple.com/documentation/passkit/pkpaymentrequest).

## Order tracking

To adopt [order tracking](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/designing-order-tracking) in iOS 16 or later, implement the [applePayContext(context:willCompleteWithResult:handler:)](https://github.com/stripe/stripe-ios/blob/22.8.0/StripeApplePay/StripeApplePay/Source/ApplePayContext/STPApplePayContext.swift#L38) function in your `ApplePayContextDelegate`. Stripe calls your implementation after the payment is complete, but before iOS dismisses the Apple Pay sheet.

In your implementation:

1.  Fetch the order details from your server for the completed order.
2.  Add these details to the provided [PKPaymentAuthorizationResult](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationresult).
3.  Call the provided completion handler on the main queue.

To learn more about order tracking, see [Apple’s Wallet Orders documentation](https://developer.apple.com/documentation/walletorders).

CheckoutViewController.swift

`extension CheckoutViewController {     func applePayContext(_ context: STPApplePayContext, willCompleteWithResult authorizationResult: PKPaymentAuthorizationResult) async -> PKPaymentAuthorizationResult {         // Fetch the order details from your service         do {           let myOrderDetails = try await MyAPIClient.shared.fetchOrderDetails(orderID: myOrderID)           authorizationResult.orderDetails = PKPaymentOrderDetails(             orderTypeIdentifier: myOrderDetails.orderTypeIdentifier, // "com.myapp.order"             orderIdentifier: myOrderDetails.orderIdentifier, // "ABC123-AAAA-1111"             webServiceURL: myOrderDetails.webServiceURL, // "[https://my-backend.example.com/apple-order-tracking-backend](https://my-backend.example.com/apple-order-tracking-backend)"             authenticationToken: myOrderDetails.authenticationToken // "abc123"           )           // Return your modified PKPaymentAuthorizationResult           return authorizationResult         } catch {           return PKPaymentAuthorizationResult(status: .failure, errors: [error])         }     } }`

To test Apple Pay, you must use a real credit card number and your test [API keys](https://docs.stripe.com/keys). Stripe recognizes that you’re testing and returns a successful test card token for you to use, so you can make test payments on a live card without charging it.
