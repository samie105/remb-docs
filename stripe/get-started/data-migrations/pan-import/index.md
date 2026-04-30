---
title: "Request a payment data import"
source: "https://docs.stripe.com/get-started/data-migrations/pan-import"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:40:00.173Z"
content_hash: "468033ef00c9181d561fc69b1a89b7e4e95fc2d0c7715d08253995d2b2c4cfe6"
---

## Securely import sensitive payment data.

Stripe enables you to retain your existing customer and payment data when you migrate to Stripe. We work with your team and current payment provider, as needed, to securely migrate your information.

This process allows you to accept and charge new customers on Stripe and continue charging your existing customers with your current processor until the migration is complete. Your customers incur no downtime. After the migration process completes, you can process all payments on Stripe.

This guide describes how to migrate to Stripe from another payment processor or a custom payment solution. You’ll also build a Stripe integration that you can test in a sandbox before you accept real payments. If you have any questions about the migration process or integrating with Stripe, see [support](https://support.stripe.com/topics/migration). If you haven’t already, [review Stripe pricing](https://stripe.com/pricing).

If you have to transfer sensitive payment information, you must complete a [Data migration request](https://support.stripe.com/questions/request-a-data-migration) before you migrate. We can help you do so in a secure and [PCI-compliant](https://docs.stripe.com/security/guide#validating-pci-compliance) way.

[](#review-integration)

Stripe simplifies your security requirements so that your customers don’t have to leave your site to complete a payment. We do this through a combination of client-side and server-side steps:

1.  From your website running in the customer’s browser, Stripe securely collects their payment details.
2.  Stripe responds with a representative token.
3.  The browser submits the token to your server, along with any other form data.
4.  Your server-side code uses that token in an API request (for example, when [creating a charge](https://docs.stripe.com/payments/charges-api)).

This approach simplifies your website’s checkout flow, while sensitive payment information never touches your server. This allows you to operate in accordance with [PCI-compliance](https://docs.stripe.com/security/guide#validating-pci-compliance) regulations, which can save you time and provide financial benefits.

![Stripe payment process flow](https://b.stripecdn.com/docs-statics-srv/assets/charge-workflow.6d5c025c1b1e62a53803f1908104e0a8.png)

The Stripe payment process flow

Compared to other payment processors, a Stripe integration can differ in the following ways:

*   Your customer never leaves your website.
*   Token creation isn’t tied to a specific product or amount.
*   It doesn’t require you to create of a client-side key on-demand. You use a set, publishable [API key](https://docs.stripe.com/keys) instead.

[](#create-account)

Before integrating with Stripe, you must create a Stripe account.

1.  [Create an account](https://dashboard.stripe.com/register) by entering your email address, full name, country, and creating a password.
2.  Fill out your business profile.
3.  In the Dashboard, click **Verify your email**. Stripe sends a verification email to your email address.
4.  Verify your email address.

[](#build-integration)

For all new customer tokens (not imported), implement the following:

1.  Use [Customer](https://docs.stripe.com/api#create_customer) objects to save the card information.
    
2.  Collect and tokenize customer card information with one of our recommended [payments integrations](https://docs.stripe.com/payments/online-payments#compare-features-and-availability). Build your Stripe integration before you ask your payment processor to transfer data to Stripe. For most startups, we recommend building an [Embedded Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works) integration, a payment form you embed in your website.
    
    To set up this integration, see the [Embedded Checkout Quickstart](https://docs.stripe.com/checkout/embedded/quickstart) and accept payments for one-time and subscription payments (if applicable).
    
3.  [Create charges](https://docs.stripe.com/api#create_charge-customer) for these new customers.
    

Using this approach, you can accept payments from your new customers on Stripe without impacting your current customers in your existing processor during the migration process.

### Integration considerations

Designing your integration before you ask your payment processor to transfer data to Stripe is the most efficient way to handle imported data. Some actions you can take before requesting an import include:

*   [Remap customer records](#remap-customer-ids)
*   [Protect updates to saved payment methods during the migration](#handle-card-updates).
*   Enable all [optimizations](https://docs.stripe.com/payments/analytics/optimization), such as Adaptive Acceptance, card account updater (CAU), and network tokens.

[](#remap-customer-ids)

If you prefer, you can configure your integration to [import the payment method data from prior records into existing Stripe Customer objects](https://docs.stripe.com/get-started/data-migrations/map-payment-data). Doing so prevents the migration from creating a new (possibly duplicate) customer in your Stripe account for each unique customer ID in the files we receive from your prior processor.

After migrating, you might still have to update some records to correspond with the new Stripe [Customer](https://docs.stripe.com/api/customers) identifier, if:

*   You created the Stripe `Customer` before migration, then we imported the payment information to update this customer record.
*   We imported the payment information as a new customer record.

For example, customer jenny.rosen@example.com might have ID `42` in your database, corresponding to ID `1893` in your previous processor’s system, but is ID `cus_12345` in your Stripe account. In this case, you must now map your ID `42` to the Stripe ID `cus_12345` in your database. Stripe provides a post-import [mapping file](#update-integration) to help you identify required remapping.

[

## OptionalProtect updates to saved payment methods



](#handle-card-updates)

If customers update their payment information with your previous processor in the window between transferring the data and completing the import, those changes are lost.

Update your site’s process for handling updates to saved payments to prevent errors or billing issues for your customers. This includes preparations to perform a self-migration for any customer without a stored Stripe `Customer` ID:

1.  Create a new [Customer object](https://docs.stripe.com/api/customers/object) in Stripe for your customer.
2.  Attach the payment method to the `Customer` object.
3.  If necessary, [migrate subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit).

After migration completes, Stripe [automatically handles card-triggered updates](https://stripe.com/blog/smarter-saved-cards), such as expiration date changes.

[](#test)

To test your embedded payment form integration:

1.  Create an embedded Checkout Session and mount the payment form on your page.
2.  Fill out the payment details with a method from the table below.
    *   Enter any future date for card expiry.
    *   Enter any 3-digit number for CVC.
    *   Enter any billing postal code.
3.  Click **Pay**. You’re redirected to your `return_url`.
4.  Go to the Dashboard and look for the payment on the [Transactions page](https://dashboard.stripe.com/test/payments?status%5B0%5D=successful). If your payment succeeded, you’ll see it in that list.
5.  Click your payment to see more details, like a Checkout summary with billing information and the list of purchased items. You can use this information to fulfill the order.

Learn more about [testing your integration](https://docs.stripe.com/testing).

Card number

Scenario

How to test

The card payment succeeds and doesn’t require authentication.

Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.

The card payment requires [authentication](https://docs.stripe.com/strong-customer-authentication).

Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.

The card is declined with a decline code like `insufficient_funds`.

Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.

The UnionPay card has a variable length of 13-19 digits.

Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.

See [Testing](https://docs.stripe.com/testing) for additional information to test your integration.

[](#request-migration)

1.  After you complete your integration and are ready to process payments on Stripe, [request your payment data from your previous processor](https://support.stripe.com/questions/request-data-from-a-current-processor-for-a-data-import-to-stripe). Many processors require the account owner to request a data transfer.
2.  Log in to your Stripe account to submit the [migration request form](https://support.stripe.com/questions/request-a-data-migration) to request your import migration.
3.  Engage with Stripe through the authenticated email thread we create upon receipt of your migration request.

#### Warning

Never send sensitive credit card details or customer information directly to Stripe. If you have this data, let us know in your migration request form so we can help you securely transfer your data.

Stripe can import your customer billing address information and payment details. You can also:

*   [Migrate specific payment types](https://docs.stripe.com/get-started/data-migrations/payment-method-imports)
*   [Migrate subscriptions](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions) or import them using the [Billing Migration Toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit).

Your previous processor might take a few days or several weeks to transfer the final data to Stripe. Allow for this transition time in your migration plan. After your previous processor transfers your data, Stripe reviews the data and identifies any problems with the import. We work with you and your previous processor to correct any issues. We then share a summary of the import for your final review and approval.

After your approval, Stripe imports the data into your account. We create a [Customer](https://docs.stripe.com/api#customer_object) for each unique customer in the transferred data file, and create and attach the customer’s cards as [Card](https://docs.stripe.com/api#card_object) or [Payment Method](https://docs.stripe.com/api/payment_methods/object) objects. If the transferred data specifies the customer’s default card, we set that as the customer’s [default payment method](https://docs.stripe.com/api#customer_object-default_source) for charges and [subscription](https://docs.stripe.com/api/subscriptions/create) payments.

If your Stripe account has accumulated significant customer records by the time you migrate, consider [mapping import data into existing Stripe Customer objects](https://docs.stripe.com/get-started/data-migrations/map-payment-data) instead of creating new `Customer` objects.

Stripe typically imports data within 10 business days of receiving the correct data from your previous processor, along with any supplementary data files you want to share with our team.

[](#update-integration)

After completing the import, Stripe sends you a choice of a CSV or JSON file that shows the mapped relationship between your current processor’s IDs and the imported Stripe object IDs. Parse this mapping file and update your database accordingly. Make sure your integration [handled any card updates](#handle-card-updates) that took place during the transition.

### Post import mapping file

After you update your integration with this mapping file, you can begin charging all of your customers on Stripe.

`{   "1893": {     "cards": {       "2600": {         "id": "card_2222222222",         "fingerprint": "x9yW1WE4nLvl6zjg",         "last4": "4242",         "exp_month": 1,         "exp_year": 2020,         "brand": "Visa"       },       "3520": {         "id": "card_3333333333",         "fingerprint": "nZnMWbJBurX3VHIN",         "last4": "0341",         "exp_month": 6,         "exp_year": 2021,         "brand": "Mastercard"       }     },     "id": "cus_abc123def456"   } }`

The example JSON mapping above shows:

*   Imported customer ID 1893 as a new Stripe `Customer` with ID `cus_abc123def456`.
*   Imported customer card ID 2600 as a new Stripe `Card` with ID `card_2222222222`.
*   Imported customer card ID 3520 as a new Stripe `Card` with ID `card_3333333333`.

Stripe can import card data as [PaymentMethods](https://docs.stripe.com/api#payment_method_object) instead of `Card` objects if you specify it in your migration request. The following examples show the mapping files for different types of payment information imports.

`old_customer_id,customer_id,old_card_id,card_id,card_fingerprint,card_last4,card_exp_month,card_exp_year,card_brand old_cus_100,cus_abc123def456,old_src_100,card_2222222222,x9yW1WE4nLvl6zjg,4242,09,2024,Visa`

[](#undefined)

After migrating, monitor your payments performance to make sure the acceptance rate for imported payment data matches your expectations.

Payment acceptance (or issuer authorization rate) is the percentage of transactions that issuers successfully authorize out of all transactions submitted for payment. This metric excludes blocked transactions (for example due to Radar rules) because those are never submitted for authorization.

In both your general approach and post migration, align your [payment authorization optimization](https://stripe.com/guides/optimizing-authorization-rates) goals with your business objectives. For example, a digital goods business with low unit cost might set their risk level to block fewer payments. Consider the potential effects:

*   Increased conversion rates due to less friction.
*   Increased exposure to fraud due to riskier payments getting through.
*   Lower raw issuer authorization rates due to fraud model blocks by the issuer.

Make sure you provide accurate data (such as cardholder name, billing address, and email). Reflecting the cardholder’s intent maximizes successful authorization potential.

### Identify cards on file

Payment data migrations involve _cards on file_ (cards saved for a future [merchant-initiated or off session](https://support.stripe.com/questions/what-is-the-difference-between-on-session-and-off-session-and-why-is-it-important) payment for the same customer). Make sure you store imported payment data and label payments using those cards on file with the correct `off_session` parameter. If you improperly identify cards on file:

*   Issuers who can’t confirm a cardholder’s consent to future or recurring payments might [decline](https://docs.stripe.com/declines#issuer-declines) them.
*   The payment data might be ineligible for certain Stripe optimization products such as Card account updater (CAU) and Network tokens (NT).

### Monitor decline reasons for optimization opportunities

Following your migration, your [issuer decline reasons](https://docs.stripe.com/declines/codes) can help you identify whether migrated payment data is transacting as expected. Spikes in certain types of declines might benefit from the following optimization products:

*   Card account updater: Stripe partnerships with card networks allow us to automatically obtain updates for expired or replaced cards in both real time and the background.
*   **Automatic retries** (Dunning): Use caution because retrying numerous cards (such as after a migration) can appear suspicious to issuers. If you use Stripe [Smart retries](https://stripe.com/guides/optimizing-authorization-rates#smart-retries) for your billing payments, our AI model analyzes decline code, payment method updates, and bank risk threshold activity to retry recurring revenue payments more strategically.
*   [Network tokens](https://stripe.com/guides/optimizing-authorization-rates#network-tokens): Replace a specific payment account number (PAN) with a secure token from the card network to make sure PAN updates (like renewal or replacement) automatically reflect in the token.
*   [Adaptive acceptance](https://stripe.com/guides/optimizing-authorization-rates#adaptive-acceptance): Stripe uses AI to assess the effect of minor adjustments (such as formatting) to an authorization request in real time, then refines the payment retry before returning the original decline to the customer.
*   **Customer outreach**: Asking your customer to log in and re-enter or re-verify their payment details often re-establishes your business’s trustworthiness with the customer and the payment providers. Consider notifying customers through channels other than email, such as text messages or in-app notifications.

The following table shows which optimization products offer improvement for a variety of decline reasons.

Decline codes might include

Migration effect

Do

Don’t

`incorrect_number`

`invalid_number`

`expired_card`

Updates to card data during the natural migration lag can cause saved card data to be out of date.

*   Card account updater
*   Network tokens
*   Adaptive acceptance
*   Contact customer

Retry

`generic_decline`

`do_not_honor`

Changes to your statement descriptor or other identification markers might trigger issuer risk models or confuse your customer.

*   Retry
*   Network tokens
*   Adaptive acceptance
*   Contact customer

Card account updater

`transaction_not_allowed`

`try_again_later`

`authentication_required`

`incorrect_cvc`

Some migrated payment data might be missing initial card validation details, such as the network token or original transaction ID.

*   Card account updater
*   Retry
*   Adaptive acceptance
*   Contact customer

Network tokens

`lost_card`

`stolen_card`

`invalid_account`

`pickup_card`

`card_not_supported`

Customers might report lost or stolen cards during a migration lag. Look out for a special CONTAC event in conjunction with these declines.

*   Network tokens
*   Contact customer

*   CAU
*   Retry1
*   Adaptive acceptance

1 Retrying lost or stolen payment data can appear suspicious to card issuers.

[](#migration-pgp-key)

If you’re unfamiliar with PGP, see [GPG](http://gnupg.org/) and start by [importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84). After you familiarize yourself with the basics of PGP, use the following PGP key to encrypt sensitive data (such as credit card information) for PCI-compliant migration.

### PGP migration key

This creates **FILENAME.gpg** with the following information:

*   Key ID: `9C78B7620C1E99AD`
*   Key type: `RSA`
*   Key size: `4096 bits`
*   Fingerprint: `AEBF 7C48 38C4 4D2F DC99 A3F9 9C78 B762 0C1E 99AD`
*   User ID: `Stripe Import Key (PCI) <support-migrations@stripe.com>`

After you import our key, you can encrypt files to send by running this command in your command line prompt:

`gpg --encrypt --recipient 9C78B7620C1E99AD FILENAME`

For more details on providing encrypted data to Stripe, see [Upload supplementary data](https://docs.stripe.com/get-started/data-migrations/supplementary-data).

## See also

*   [Payments optimizations](https://docs.stripe.com/payments/analytics/optimization)
*   [Multiple accounts](https://docs.stripe.com/get-started/account/multiple-accounts)
*   [Account checklist](https://docs.stripe.com/get-started/account/checklist)
