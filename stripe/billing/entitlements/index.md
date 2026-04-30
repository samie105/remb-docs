---
title: "Entitlements"
source: "https://docs.stripe.com/billing/entitlements"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:09:46.997Z"
content_hash: "23b4e556da20682cccd62178b2b6b37c61358a3136b0abc4da217a4678195cf9"
---

Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access (according to your customer’s subscription status), and to what features, based on your mapping choices.

This guide assumes that you’re already using Stripe [Subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions) and [Customer](https://docs.stripe.com/invoicing/customer) resources.

## Get started

To get started with Entitlements:

*   **Set up your features**: Create each feature in Stripe Billing from the Dashboard. Here are some examples of features you can include:
    *   API access
    *   AI assistant
    *   Premium support
    *   Advanced reporting
    *   Extended data retention
*   **Add your features to products**: Attach features to corresponding Stripe Products. You can add a single feature to multiple products.
*   **Manage your features**: Edit or archive each feature from the Dashboard.

[](#setup)

To create a feature in the Dashboard, do the following:

1.  In the Dashboard, go to the [Product catalog](https://dashboard.stripe.com/products) and click **Features**.
2.  Click **\+ Create feature** and enter a Name and a Lookup Key for the feature. You can optionally also add Metadata.
3.  Because the Lookup Key is unique to each feature, you can’t reuse it across different features unless you archive the feature associated with the Lookup Key.
4.  Click **Create feature**.

[](#assign)

To add a feature to a product in the Dashboard, do the following:

1.  In the Dashboard, from the [Features](https://dashboard.stripe.com/features) tab, click the feature that you want to add.
2.  Click **Attach to product** and select a product from the menu.
3.  Click **Confirm**.

When a customer subscribes to the product, you can view what features they’re entitled to. To do this, go to the [Customers](https://dashboard.stripe.com/customers) page, select the customer, and review the Entitlements section.

#### Note

Existing subscriptions will create active entitlements for any product feature changes at the start of the next billing period.

[](#manage)

You can manage features from the Dashboard.

### Edit a feature

To edit a feature’s Name or add Metadata, go to the [Features](https://dashboard.stripe.com/features) tab, click the overflow menu (), and click **Edit feature**. You can’t edit a feature’s Lookup Key after the feature is created.

### Remove a feature from a product

To remove a feature from a product, go to the [Features](https://dashboard.stripe.com/features) tab and select the feature. Then click the overflow menu () next to the product name and click **Remove product**.

### Archive a feature

To archive a feature, go to the [Features](https://dashboard.stripe.com/features) tab, click the overflow menu (), and click **Archive feature**.

Before you archive a feature, keep in mind the following:

*   Archived features can’t be edited or added to any new products.
*   Archived features still create entitlements if attached to existing products.
*   An archived feature’s lookup key can be used again.
*   You can’t unarchive a feature.
