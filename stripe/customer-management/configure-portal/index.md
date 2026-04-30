---
title: "Configure the customer portal"
source: "https://docs.stripe.com/customer-management/configure-portal"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:08:47.588Z"
content_hash: "6c677e44c151997347c647c4f41bf6fbd783448739f50d58aa18b259fb010cb9"
---

After setting up your customer portal, configure its settings [in your Dashboard](https://dashboard.stripe.com/test/settings/billing/portal). If you haven’t set up your customer portal, see the [customer portal guide](https://docs.stripe.com/customer-management).

## Configure subscription management

Configure how to manage subscriptions in your customer portal integration.

Option

Description

Default

**Switch plan**

Let your customer switch their subscription. This option is best when you have a good-better-best pricing model.

Off

**Update quantities**

Let your customer increase or decrease the quantity of a subscription. This functionality is best when you have a seat-based pricing model.

Off

**Prorate subscription updates**

If customers can change their plan or quantity, optionally credit back customers for time remaining in the billing period. You can apply a [proration](https://docs.stripe.com/billing/subscriptions/prorations) immediately or at the end of the billing period.

Off

**Manage downgrades**

If customers can change their plan or quantity, optionally schedule the change to occur at the end of the billing period. If enabled, the customer portal automatically creates and attaches a subscription schedule to the subscription. You can only downgrade at the end of a billing period between prices that have the same product. When using this feature, be sure to follow [best practices](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-sub-updates) to prevent unexpected subscription overwrites.

Update immediately

**Use promotion codes**

If customers can change their plan or quantity, optionally allow customers to apply [promotion codes](https://docs.stripe.com/billing/subscriptions/coupons) when updating subscriptions.

Off

## Cancellation management

Configure your portal to allow cancellations, collect cancellation reasons, and offer retention coupons.

Option

Description

Default

**Cancel subscription**

Let your customer cancel their subscription. After canceling, customers can still renew subscriptions until the billing period ends.

On

**Cancellation reason**

Enable the **Cancel subscription** option to capture a cancellation reason when your customer cancels their subscription on the customer portal.

On

**Retention coupons**

Offer coupons to customers before they cancel their subscriptions. You can use coupons as part of your churn reduction strategy.

Off

## Customer billing configurations

Dictate what information your customers can manage.

Option

Description

Default

**Billing information**

Capture critical customer, shipping, and tax information from your customer for payment methods and to display on an invoice.

Name

Description

Default status

**Name**

Let the customer change their name.

On

**Email address**

Let the customer change their email address. _Note: This functionality isn’t available in the no-code customer portal_

On

**Billing address**

Let the customer update their billing address.

On

**Phone number**

Let the customer update their phone number

On

**Shipping address**

Let the customer update their shipping address

Off

**Tax ID**

Let the customer update their tax ID

Off

On

**Payment methods**

Let your customer update their payment method information.

On

**Promotion codes**

Let your customer enter promotion codes on your customer portal instance when upgrading their plan. Go to the [Coupons](https://docs.stripe.com/billing/subscriptions/coupons) documentation to learn more about coupons, promotion codes, and discounts.

Off

## Customize the portal

Use these configuration settings to customize your customer portal instance.

Name

Description

Required?

**Headline**

Enter an introductory text that the customer portal displays to your customers. You can only add one headline for each customer portal configuration. If you don’t enter anything, the customer portal displays this default text: “{{YOUR\_BUSINESS\_NAME}} partners with Stripe for simplified billing.”

Yes

**Terms of service link**

Enter a link to your terms of service. The customer portal shows this to your customers whenever they change a subscription or add a payment method. If you don’t enter anything, the customer portal uses the terms of service set in [public account details](https://dashboard.stripe.com/settings/public) instead.

No

**Default Redirect link**

Enter a link to redirect customers when they exit the customer portal. If you don’t enter anything, the customer portal doesn’t display “Return to {{YOUR\_BUSINESS\_NAME}}”.

No

**Custom domain**

Set a custom domain from which to serve the customer portal. To learn more, read the [Checkout guide](https://docs.stripe.com/payments/checkout/custom-domains) about custom domains. You can only set one custom domain per account.

No

**Business name**

Set the name of your business in the [**Public business information**](https://dashboard.stripe.com/settings/public) section of the Stripe Dashboard. The customer portal displays this name to your customer.

Yes

## Invoice history configurations

Name

Description

Default status

**Invoice history visible**

Determine whether invoice history is visible to customers using your customer portal.

On

## Email settings configurations

#### Caution

Email settings are applied to all emails sent from Stripe to your customers. Make sure that any changes you make are appropriate for all your Stripe use cases.

Configure which emails Stripe sends to your customers. You can also configure a custom domain to use for the emails. You can configure all of this in the [email settings](https://dashboard.stripe.com/settings/emails) of the Dashboard.

## Customize branding

To customize the look and feel of the customer portal, go to the [branding settings](https://dashboard.stripe.com/account/branding) of the Dashboard. You can customize the following items:

*   Your logo and icon
*   Background color
*   Button color
*   Font
*   Shapes

### Branding with Connect

If you maintain a platform with Connect, the customer portal uses the brand settings of the connected account under these circumstances:

*   The platform uses direct charges
*   The platform uses destination charges with `on_behalf_of`

For all other connected accounts, you can configure the brand settings with the [Accounts](https://docs.stripe.com/api/v2/core/accounts/create#v2_create_accounts-configuration-merchant-branding) API.

## Preview invoicing management

To preview invoicing management in the portal:

1.  Create a [sandbox](https://docs.stripe.com/sandboxes) in the Dashboard. Nothing you do in a sandbox affects your live setup.
2.  Go to the [Customers page](https://dashboard.stripe.com/customers) and select a customer.
3.  Create a new invoice for the customer.
4.  On the customer’s page, click the overflow menu . Under **Actions**, select **Open customer portal**.

For security reasons, the quick view option isn’t available for live mode customers.
