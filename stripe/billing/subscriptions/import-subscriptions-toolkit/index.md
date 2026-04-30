---
title: "Migrate subscriptions to Stripe Billing using toolkit"
source: "https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:21:03.522Z"
content_hash: "f9c0df010eaea29e9f0000c044a06a94312799a31e92e2a3aa84535bfaf47549"
---

## Learn how to migrate your existing subscriptions to Stripe using the toolkit.

Use the [Billing migration toolkit](https://dashboard.stripe.com/billing/migrations) in the Stripe Dashboard to migrate your existing subscriptions from a third-party system, a home-grown system, or an existing Stripe account to Stripe Billing.

## Before you begin

1.  If you haven’t already, review the [migration stages](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions#migration-stages).
2.  [Set up a Stripe Billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions) before you begin migration. This is a one-time setup that you don’t need to repeat for future migrations.
3.  [Request a PAN data import](https://docs.stripe.com/get-started/data-migrations/pan-import) from your current processor. This step is only required if you’re migrating to Stripe from another processor. If you’re migrating from Stripe to Stripe, you can skip this prerequisite.
4.  If you’re migrating from a third-party or home-grown system, carefully time the cancellation of your existing subscriptions and the creation of new ones in Stripe. To avoid missing a billing period, create the new subscriptions in Stripe first, before canceling the old subscriptions. To avoid double billing, cancel subscriptions in your old system before the subscriptions are set to charge. For subscriptions with upcoming billing dates close to migration, schedule them to start after the cycle so the final bill is in the old system.

[](#download-csv)

First, export your existing subscriptions by matching the exported data to a migration-compatible CSV file. You can create your own CSV file, or download any of the following CSV templates provided by Stripe ([Basic](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#basic), [Multi-price items](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#multi-price), and [Ad-hoc pricing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#ad-hoc)). You can also find examples of CSV files for common migration [use cases](#migration-use-cases).

1.  Click **Download CSV template**.
    
2.  Choose a CSV template (basic, multi-price items, or ad-hoc pricing) based on your billing use case.
    
    ### Basic CSV
    
    This example shows a migration for common subscription use cases like quantity, taxes, billing anchor, discounts, trials, and backdating.
    
    ### Specify the following fields for a Basic CSV file:
    
    ### Multi-price items CSV
    
    This example shows a migration that has multiple products per subscription.
    
    ### Specify the following fields for a Multi-price items CSV file:
    
    ### Ad-hoc prices CSV
    
    This example shows handling a subscription migration using [ad-hoc pricing](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data) for existing products.
    
    ### Specify the following fields for an Ad-hoc pricing CSV file:
    
3.  In the CSV file, specify the details of the subscriptions you want to export.
    
    #### For Stripe-to-Stripe migrations
    
    If you’re migrating subscriptions within Stripe accounts, refer to the [CSV example](#within-Stripe-accounts) before you specify and upload a CSV file.
    

[](#upload-csv)

Click **Upload CSV**. The CSV file size limit is 120 MB.

Stripe validates the file to verify that the uploaded subscriptions are in the required CSV format. This process might take up to a few hours, depending on the size of the file. If the file is valid, you can proceed to the next step in the migration. If there are any validation errors, you must [resolve the errors](#resolve-validation-errors) to proceed.

[](#review-subscriptions)

After Stripe validates your CSV file, review the summary of your uploaded subscriptions for any discrepancies:

1.  Cross-check the summary for the correct:
    
    *   Date of upload
    *   Uploaded file name
    *   Number of subscriptions
    *   Number of customers
    *   First subscription go-live date
2.  If everything is valid, click **Start migration**.
    
    If you see errors, click **Cancel migration** and restart the migration from [Download a CSV file](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#download-csv).
    

[](#track-migration)

After you review your uploaded subscriptions, track the progress of your migration:

Migration progress

Description

Migration in progress

Your subscriptions are queued to schedule on the specified start date. This process can take a few minutes to a few hours, depending on the size of the file. For example, the validation and migration for 100,000 subscriptions takes approximately 30 minutes to complete.

The Billing migration toolkit uses the [Subscription schedule](https://docs.stripe.com/api/subscription_schedules) to migrate your subscriptions. This allows your subscriptions to remain in a scheduled state for 24 hours before going live. In a sandbox, the buffer time is reduced to 1 hour for faster evaluation and testing.

Scheduled subscriptions

After migration, your subscriptions remain in a scheduled state for 24 hours before going live. You have 10 hours to [cancel these scheduled subscriptions](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#cancel-migration) using the toolkit.

You can’t update scheduled subscriptions using the migration toolkit. If you want to update your scheduled subscriptions, you can either call the [update](https://docs.stripe.com/api/subscription_schedules/update) endpoint, or update each subscription individually in the [Subscriptions](https://dashboard.stripe.com/subscriptions) page of the Dashboard.

Customers can’t cancel scheduled subscriptions from their customer portal. They can only cancel live subscriptions.

Go live with subscriptions

After 24 hours, your scheduled subscriptions go live and charge customers on their applicable start dates. You can view all your live subscriptions in the [Subscriptions](https://dashboard.stripe.com/subscriptions) page of the Dashboard.

After the migration goes live, we recommend you monitor your subscriptions starting from the first payment. Make sure the charge dates and amounts for the migrated subscriptions match the specified [start\_date](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-start_date).

Customers can cancel live subscriptions from their customer portal.

Monitor subscriptions

After the migration goes live, monitor your subscriptions for problems related to payment methods. For example, check transactions for unrecoverable issuer [decline codes](https://docs.stripe.com/declines/codes) such as `incorrect_number` and [take action](https://docs.stripe.com/get-started/data-migrations/pan-import#remap-customer-ids) to make sure invoices get paid. Consider notifying customers that have invalid payment methods through channels other than email, such as text messages or in-app notifications.

When using automatic collection, check [open or past due invoices](https://docs.stripe.com/billing/collection-method#failed-incomplete-subscriptions) to make sure customers aren’t missing [default payment methods](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method), which might cause the invoice to be unable to attempt collection.

[](#view-migrations)

To view all of your migrations:

1.  Select the migration you want to review in [**Migrations**](https://dashboard.stripe.com/billing/migrations).
    
2.  To open a migration, click **View** in the dropdown menu.
    
    You can track the following fields:
    
    *   Upload date
    *   File name
    *   Stripe billing migration id
    *   Number of subscriptions
    *   Migration status

[](#cancel-migration)

If you identify any problems with the scheduled subscriptions, you can roll back the migration and revert the scheduled subscriptions. The Dashboard displays a timestamp to indicate if you can still cancel the migration using the toolkit. You have 10 hours from when you scheduled the subscriptions to cancel them. After 10 hours, the cancel option is disabled in the toolkit. To cancel the migration after 10 hours, you can either call the [cancel](https://docs.stripe.com/api/subscription_schedules/cancel) endpoint, or individually cancel each subscription in the [Subscriptions](https://dashboard.stripe.com/subscriptions) page of the Dashboard.

1.  Find the migration you want to cancel in your [Migrations](https://dashboard.stripe.com/billing/migrations).
2.  Click **Cancel migration** in the dropdown menu.

[](#run-multiple-migrations)

You can run as many simultaneous subscription migrations as you want. For large migrations, divide the subscriptions into batches and start with a small batch. This can help you quickly identify any validation issues and save validation time.

To start a new migration:

1.  Click **Start new migration**.
2.  Restart the migration process from [Download a CSV file](#download-csv).

You can also find examples of CSV files for common migration [use cases](#migration-use-cases).

## Migration use cases

You can apply the migration use cases in this section to your own migration, if applicable. Timestamps in these examples are in Unix EPOCH format. The examples also include test customer and price IDs that you can use in a sandbox.

You can combine any Stripe-provided CSV template ([Basic](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#basic), [Multi-price items](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#multi-price), [Ad-hoc pricing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#ad-hoc)) with any of these examples as needed.

### Migrate subscriptions with various pricing models

### Migrate subscriptions with different types of payment collection methods

### Migrate subscriptions at different stages of subscription service period

### Migrate subscriptions with taxes

### Migrate subscriptions with discounts

### Migrate subscriptions within Stripe accounts

### Migrate subscriptions with multiple phases

## CSV reference

The migration tookit requires you to upload a CSV that has specific information in the correct fields.

### CSV prerequisites

Before you create or download a CSV file, make sure you have access to the following information:

**Customer object**

All customers must have a default [payment method attached to them](https://docs.stripe.com/api/payment_methods/attach). Without a default payment method, future subscription payments will fail. If you don’t have a default payment method set for your customers after migrating their data, you have two options:

*   Obtain the user’s consent or rely on their past payment behavior to determine the default payment method on a per-customer basis.
*   Use this [provided script](https://gist.github.com/bsears90/c3f36bfe379dfd13cae749824c5b45ae) to attach the latest payment method to your customers and make it the default method.

**Automatic tax**

If you use Stripe Tax (where you set automatic tax to true), all customers must have either [addresses or postal codes](https://docs.stripe.com/tax/customer-locations) (or both) per country. Stripe needs this information to calculate taxes for the given subscriptions.

[collection\_method](https://docs.stripe.com/api/subscriptions/create#create_subscription-collection_method)

If you’re using the `send_invoice` payment method for your subscriptions:

*   Add email addresses to the required customers.
*   Add the [days\_until\_due](https://docs.stripe.com/api/subscriptions/create#create_subscription-days_until_due) parameter in the migration CSV file to state the validity of [invoices](https://docs.stripe.com/api/invoices) for each customer.

**Dates**

*   To ensure accurate timing, pay special attention to timezones when you create epoch date-time formats for your migration CSV file.
*   For the toolkit, set the [start\_date](https://docs.stripe.com/api/subscriptions/object#subscription_object-start_date) with a buffer of at least 24 hours in advance from the CSV upload time. We create a [subscription schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules) so that you get this buffer time to confirm and verify accuracy. When the start date begins, the subscription changes from scheduled start to live state.

**Coupons**

*   If the subscription schedule or subscription has [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle) in the future and `proration_behavior` [set to](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations) `none`, updating these objects unsets the coupon. Re-apply the coupon if you make any updates to the subscription schedule or subscription.
*   To migrate a subscription with ongoing `discount_behavior`:
    *   Set a future phase that removes the coupon at the correct date instead of waiting for an expiration.
    *   Create a coupon for each subscription, with the duration being different on each one so they all expire correctly.

**Stripe to Stripe migration**

Users can migrate subscriptions within Stripe accounts. You must input Customer IDs and Price IDs (and both Coupon IDs and Tax IDs, if using them) into the template associated with your destination Stripe account, and not your source Stripe account. The migration tool generates an error if you input IDs associated with your source account.

### Full CSV specification

Attribute

Type

Description

`customer` **(required)**

Stripe Customer ID

The identifier of the customer to create the subscription for.

`start_date` **(required)**

Timestamp in epoch UNIX format

Determines when to create the subscription. You must provide a value that’s 24 hours (or greater) into the future. In a sandbox, you can set this to 1 hour in the future.

`price` **(required)**

Stripe Price ID

Must be a recurring price. If migrating multiple items, use `items.x.{price, quantity}` format instead. Ad-hoc prices are also supported with `adhoc_items.x.{amount, interval, product, currency}`.

`quantity`

Number

Determines quantity of a subscription. By default, each subscription is for one product, but Stripe allows you to subscribe a customer to multiple quantities of an item.

`items.x.price` **(required)**

Stripe Price ID

The ID of the price object. Must be a recurring price.

`items.x.quantity`

Number

Determines quantity of a subscription. By default, each subscription is for one product, but Stripe allows you to subscribe a customer to multiple quantities of an item.

`adhoc_items.x.amount` **(required)**

Number

A positive number. Use full units with decimals (such as 21.50).

`adhoc_items.x.product` **(required)**

Stripe Product ID

The identifier of the product that belongs with the ad-hoc price.

`adhoc_items.x.interval` **(required)**

`day`, `week`, `month` or `year`

The billing frequency.

`adhoc_items.x.currency` **(required)**

String

A three-letter ISO currency code, in lowercase, for a [supported currency](https://docs.stripe.com/currencies).

`adhoc_items.x.quantity`

Number

Determines quantity of a subscription. By default, each subscription is for one product, but Stripe allows you to subscribe a customer to multiple quantities of an item.

`metadata_source`

String

If you’re doing a Stripe-to-Stripe migration, enter `internal:Stripe`.

`metadata_*`

String

Attach these key-value pairs to an object. This is useful for storing additional information about the object in a structured format.

`automatic_tax`

Boolean

Specify `true` to use automatic tax settings by Stripe Tax.

`coupon`

Stripe Coupon ID

The identifier of the coupon to apply to this subscription.

`currency`

String

Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies). Used for currency selection with multi-currency prices.

`trial_end`

Timestamp

Sets the phase to trialing from the start date to the `trial_end` date. You must specify a value that’s before the cycle/phase end date, and you can’t combine it with the trial.

`proration_behavior`

`create_prorations` or `none`

Determines if the subscription creates prorations after migration. The default value is `create_prorations`.

`collection_method`

`charge_automatically` or `send_invoice`

When charging automatically, Stripe attempts to pay the underlying subscription at the end of each billing period using the default source attached to the customer. The default value is `charge_automatically`. When sending an invoice, Stripe emails your customer an invoice with payment instructions, and marks the subscription as active. If using `send_invoice`, you must set `days_until_due`.

`default_tax_rate`

Stripe Tax ID

Sets the subscription’s `default_tax_rates`. This also determines the invoice’s `default_tax_rates` for any invoices issued by the subscription during this phase. This value is incompatible with `automatic_tax`.

`backdate_start_date`

Timestamp in epoch UNIX format

Determines the `start_date` of the created subscription, which must occur in the past. If set, you must specify `none` for the `proration_behavior`. Doing so prevents the creation of a prorated invoice for the time between `backdate_start_date` and actual `start_date`. For more details, see [backdating no charge](https://docs.stripe.com/billing/subscriptions/backdating#backdating-no-charge).

`billing_cycle_anchor`

Timestamp

Determines the future dates of when to bill the subscription to the customer.

`days_until_due`

Integer

The number of days from when the invoice is created until it’s due. This is required and valid only for invoices with `collection_method` set to `send_invoice`.

`cancel_at_period_end`

Boolean

Specify `true` to cancel a subscription at the end of the period.
