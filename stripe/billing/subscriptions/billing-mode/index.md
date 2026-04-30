---
title: "Enable increased flexibility for subscriptions"
source: "https://docs.stripe.com/billing/subscriptions/billing-mode"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:25:24.448Z"
content_hash: "b8d23e8ed0b3914ab7dffbd7d0475e491b57c9940d6fbe21cc25c4304286dcb9"
---

You can set your preferred [billing mode](https://docs.stripe.com/api/subscriptions/create#create_subscription-billing_mode) to orchestrate your invoices and subscriptions to meet your business requirements. You can configure each subscription to use one of two billing modes:

*   **Flexible** Recommended: Provides accurate and predictable billing behavior and new capabilities. To access these improvements, which are only available in flexible billing mode, you must create new subscriptions with flexible billing mode or migrate your existing subscriptions.
*   **Classic**: Uses the existing Stripe subscription behavior. This setting is maintained for backward compatibility with older integrations.

You can [learn more](https://docs.stripe.com/billing/subscriptions/billing-mode/compare) about the detailed differences between classic and flexible billing mode and how to choose the billing mode that works best for you.

#### Warning

You can’t migrate a subscription from flexible billing mode to classic billing mode.

## Why flexible billing mode

Flexible billing mode provides more accurate billing for prorations, usage-based pricing, flexible invoicing, and trial settings. It also unlocks new capabilities such as [mixed intervals on the same subscription](https://docs.stripe.com/billing/subscriptions/mixed-interval). These improvements are only available in flexible billing mode, which is why we recommend creating new subscriptions with flexible billing mode and [migrating](https://docs.stripe.com/billing/subscriptions/billing-mode#migrate-existing-subscriptions-to-flexible-billing-mode) your existing ones.

We recommend that new Billing users use flexible billing mode for subscriptions and invoices, although we don’t require it.

For existing users, your default billing mode is preserved as classic to maintain backward compatibility with your current integration. However, we recommend migrating to flexible billing mode to take advantage of the latest billing features and improvements. Learn more about the [differences between classic and flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode/compare).

## Get started with flexible billing mode

You can set or update the billing mode through the API or Dashboard when you create or migrate subscriptions. We apply a default billing mode if you don’t specify one.

*   If you create or update a subscription through the API, the default billing mode depends on your [API integration version](https://docs.stripe.com/changelog). For API version `2025-09-30.clover` and later, the default is `flexible`. For earlier versions, the default is `classic`. If you [upgrade your API version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api), the default billing mode for new subscriptions changes accordingly.
*   If you create or update subscriptions through the Dashboard (including [Payment Links](https://docs.stripe.com/payment-links) and [Pricing Tables](https://docs.stripe.com/payments/checkout/pricing-table)), the default value depends on the [billing mode default setting](https://dashboard.stripe.com/settings/billing/subscriptions) you configure in **Settings** > **Billing** > **Subscriptions and emails**.

To use flexible billing mode, your integration must be on Stripe API version [2025-06-30.basil](https://docs.stripe.com/changelog/basil#2025-06-30.basil) or later. Learn how to [upgrade your API version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api).

### Create a new subscription with flexible billing mode

You can create a flexible billing mode subscription or update a classic billing mode subscription to be flexible through the Dashboard, regardless of your integration’s API version. To fully modify these subscriptions in the Stripe API, your integration must be on [2025-06-30.basil](https://docs.stripe.com/changelog/basil#2025-06-30.basil) or later. To see what version you’re on, go to the [Workbench overview](https://dashboard.stripe.com/workbench/overview) and look at the API versions section. From there, click **Upgrade** to upgrade to a newer version.

Follow the steps below to create a flexible billing mode subscription through the subscription editor:

1.  Go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard.
2.  Click **+Create Subscription**.
3.  Scroll down to the **Advanced settings** section.
4.  Set **Billing mode** to **Flexible**.

The default billing mode value depends on your account settings. You can customize both the available billing mode options and the default selection in the Subscription editor. To configure this, go to **Settings** > **Billing** > **Subscriptions and emails** > [Default billing mode](https://dashboard.stripe.com/settings/billing/subscriptions). In the subscription editor, you can choose to display billing mode options from the following:

*   **Classic:** Both flexible and classic billing modes are displayed, with classic selected by default. This option is recommended if your integration depends on classic billing mode and you can’t migrate to flexible billing yet.
*   **Flexible:** Both flexible and classic billing modes are displayed, with flexible selected by default. This option is recommended if you’re actively migrating to flexible billing mode.
*   **Flexible and hide classic:** Only flexible billing mode is displayed in the subscription editor. This option is recommended for new Stripe Billing users and for existing users who exclusively use flexible billing mode.

The billing mode default setting also determines the billing mode for subscriptions created through Dashboard-generated Payment Links and Pricing Tables. For example, if you set the billing mode default to flexible and then create a Payment Link in the Dashboard, any subscription generated from that Payment Link uses flexible billing mode.

The billing mode default setting only applies to new subscriptions created in the Dashboard. It doesn’t affect subscriptions created using the API or subscriptions migrated to flexible mode.

### Migrate existing subscriptions to flexible billing mode

You can migrate your existing subscriptions to flexible billing mode. The flexible behaviors take effect for all new activity on the subscription after migration. However, Stripe doesn’t recalculate any resources created before migration, including pending proration `Invoice Items`.

To use flexible billing mode, your integration must be on Stripe API version [2025-06-30.basil](https://docs.stripe.com/changelog/basil#2025-06-30.basil) or later. To see what version you’re on, go to the Workbench overview and look at the **API versions** section. From there, click **Upgrade** to upgrade to a newer version.

1.  On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard, select the subscription that you want to migrate.
2.  Click **Update subscription**.
3.  Expand the **Billing and payment collection** section.
4.  Set **Billing mode** to **Flexible**, and click **Update subscription**.

### Billing mode and subscription schedules

When you create a subscription schedule from an existing subscription, don’t set `billing_mode` if the subscription already has one. The schedule automatically inherits the `billing_mode` from the original subscription. If you set `billing_mode` when using `from_subscription`, Stripe returns an error. If you need a different `billing_mode`, create a new subscription.

### Itemize proration discounts

If you use flexible subscriptions, you can set your preferred behavior for [proration discounts](https://docs.stripe.com/api/subscriptions/create#create_subscription-billing_mode-flexible-proration_discounts) on invoices and invoice items:

*   **Itemized** Recommended: Enables invoices and invoice items to show prorations with gross amounts and accurate discount amounts, consistent with non-prorations.
*   **Included**: Uses the existing Stripe proration display behavior, with net amount and zero monetary discount amounts. This setting is maintained for backward compatibility with older integrations.

Learn more about the [differences between itemized and included](https://docs.stripe.com/billing/subscriptions/billing-mode/compare).

To enable itemized proration discounts, you must [upgrade your API version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api) to [2025-06-30.basil](https://docs.stripe.com/changelog/basil#2025-06-30.basil) or later.

[Create](https://docs.stripe.com/api/subscriptions/create) or [migrate](https://docs.stripe.com/api/subscriptions/migrate) a subscription in order to set `proration_discounts` to `itemized`.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2025-06-30.basil" \  -d "items[0][price]=  {{PRICE_ID}}  " \   -d "customer=  {{CUSTOMER_ID}}  " \   -d "billing_mode[type]=flexible" \   -d "billing_mode[flexible][proration_discounts]=itemized" \   -d payment_behavior=default_incomplete \  -d "payment_settings[save_default_payment_method]=on_subscription"`

The code example above returns the following response:

`{   "id": "sub_JgRjFjhKbtD2qz",   "object": "subscription",   "billing_mode": {     "flexible": {       "proration_discounts": "itemized"     },     "type": "flexible",     "updated_at": 1751071020   },`
