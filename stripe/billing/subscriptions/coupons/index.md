---
title: "Coupons and promotion codes"
source: "https://docs.stripe.com/billing/subscriptions/coupons"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:19:05.715Z"
content_hash: "c79db5654f6511d9a193bab4af4c004dc67397f433463bcda1eb8c51af11d22e"
---

Redeem coupons to apply discounts to the subscriptions you offer. You can also use coupons to create promotion codes to share with your customers. Customers can redeem these promotion codes to apply discounts to their subscriptions.

*   [Coupons](#coupons): You create and manage coupons to define discounts, such as a percentage or amount off from the subscription price.
*   [Promotion codes](#promotion-codes): You create customer-facing codes that map to your coupons. For example, FALLPROMO and SPRINGPROMO can both map to a single 25% off coupon. You can share promotion codes directly with your customers, who can enter and redeem the codes at checkout.

You can use coupons and promotion codes to:

*   Apply one or more discounts to an invoice, subscription, or subscription item
*   Apply one or more discounts for a certain duration of time
*   Reduce invoice amounts by a percentage or a flat amount

You can also define a coupon that a customer must redeem by a certain date, or that’s limited to a set number of redemptions across all of your customers.

To use discounts for one-time payments, see [Add discounts for one-time payments](https://docs.stripe.com/payments/checkout/discounts).

## Coupons

To apply discounts to a customer or a customer’s charges, redeem coupons into discounts. Learn how to create and manage coupons in the following sections.

### Create a coupon

Create coupons in the Dashboard or with the [API](https://docs.stripe.com/api/coupons/create):

1.  In the Dashboard, open the [Products](https://dashboard.stripe.com/test/products?active=true) page.
2.  Click **Coupons**.
3.  Click **+New**.
4.  In the **Create a coupon** dialog, enter the coupon’s parameters.
5.  Click **Create coupon**.

The following are all the settings for coupons. The name is the only setting you can edit after you create the coupon.

Setting

Description

**Name**

The name of the coupon that appears on receipts and invoices.

**ID** optional

A unique identifier for the coupon in the API. If you leave this field blank, Stripe generates an ID for you.

**Type**

Determines whether a coupon discounts a subscription by a fixed amount or by a percentage.

**Percentage off** or **Discount amount**

Indicates how much the coupon actually discounts.

If you sell in multiple currencies, a single coupon can define different discount amounts for different currencies. Multi-currency coupons follow the same rules as [multi-currency prices](https://docs.stripe.com/products-prices/how-products-and-prices-work#multiple-currencies).

**Apply to specific products** optional

Limits the type of items that the coupon can apply to.

**Duration**

Indicates how long the coupon is valid for.

**Redemption limits** optional

Allows you to limit when a customer can redeem the coupon and the number of times a coupon can be redeemed.

**Codes** optional

Allows you to create [promotion codes](#promotion-codes--promotion-codes) for the coupon.

### Set eligible products

To set the products that are eligible for discounts, add the relevant product in the **Apply to specific product** field. Any promotion codes that are associated with the coupon are also restricted to this list of eligible products.

If you configure a coupon to apply to specific products and a subscription doesn’t have any applicable products, no discount is applied when you add the coupon to the subscription.

When you [make changes](https://docs.stripe.com/billing/subscriptions/change) to a subscription, Stripe calculates the proration and applies any existing discounts. You can’t discount proration line items further on the invoice that’s generated.

### Apply coupons to subscriptions

After you’ve created coupons, create a discount by applying them to a subscription. You can apply the coupon when you create the subscription or by [updating a customer’s existing subscription](https://docs.stripe.com/api#update_subscription).

1.  In the Dashboard, open the [Subscriptions](https://dashboard.stripe.com/test/subscriptions?status=active) page.
2.  Click the relevant subscription.
3.  Click **Actions**.
4.  Click **Update subscription**.
5.  Click **Add coupon**.
6.  Select one or more coupons from the dropdown menus and click **Submit**.

You can still create a subscription when a customer doesn’t have a stored payment method if [no immediate payment](https://docs.stripe.com/billing/subscriptions/deferred-payment) is required after you apply coupons to it.

### Apply coupons to Checkout

Apply coupons to subscriptions in a Checkout Session by setting the `discounts` parameter in the [API](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-discounts). To create a session with an applied discount, pass the coupon ID in the `coupon` parameter of the `discounts` array.

`curl https://api.stripe.com/v1/checkout/sessions \   -u` 

`sk_test_REDACTED`

`: \   -d "payment_method_types[]"=card \   -d "line_items[][price]"=  "{{PRICE_ID}}"   \   -d "line_items[][quantity]"=1 \   -d mode=subscription \   -d "discounts[][coupon]"="{{COUPON_ID}}" \   -d success_url="https://example.com/success"`

### Delete coupons

You can delete coupons with the Dashboard or the [API](https://docs.stripe.com/api/coupons/delete).

Deleting a coupon prevents it from being applied to future subscriptions or invoices, but it doesn’t remove the discount from any subscription or invoice that already has it.

1.  In the Dashboard, open the [Products](https://dashboard.stripe.com/test/products?active=true) page.
2.  Click **Coupons**
3.  Click the relevant coupon.
4.  Click the overflow menu ().
5.  Click **Delete coupon**.

### Coupon duration

A coupon’s duration indicates how long the redeemed [discount](https://docs.stripe.com/api/#discounts) is valid for. For example, a coupon for 50% off with a duration of 4 months applies to all invoices in the 4 month period starting when the coupon is first applied. If a customer applies this coupon to a yearly subscription during the coupon’s 4 month period, the 50% discount applies to the entire yearly subscription. In a monthly subscription, the coupon applies to the first 4 months. For a weekly subscription, a 4 month coupon applies to every invoice in the first 4 months.

If you’re configuring a coupon’s duration in the API, when you use the value `repeating` you must specify `duration_in_months` as the number of months that the coupon repeatedly applies to. If you set the duration to `once`, the coupon applies only to the first invoice. If you set the duration to `forever`, the coupon applies to all invoices indefinitely.

#### Note

When a subscription uses a coupon with `duration=once`, the coupon applies only to the next invoice and is considered used after the invoice finalizes. After the coupon has been applied, the subscription’s `discounts` array no longer includes that discount. Specifically:

*   Before a coupon is applied to any invoice, the subscription’s `discounts` includes the discount object.
*   After the invoice that used the coupon is finalized or paid, the subscription’s `discounts` stops showing that discount.
*   The invoice that consumed the coupon still shows the applied discount on the invoice resource and line items.

This behavior can lead to two commonly observed states: a subscription response that doesn’t show any discount (because a `duration=once` coupon was already consumed), or a subscription response that shows the discount in `discounts` only if the coupon hasn’t been applied.

#### Caution

If you apply a coupon to a [backdated subscription](https://docs.stripe.com/billing/subscriptions/backdating), the coupon’s duration starts counting from the backdated start date, not from when you make the API call. For `repeating` coupons, this means the backdated period consumes part of the coupon’s duration. The coupon’s `duration_in_months` must be longer than the backdated period if you want the discount to apply to invoices after the backdated period. See [Backdating and discounts](https://docs.stripe.com/billing/subscriptions/backdating#backdating-discounts) for more details.

### Redemption limits

Redemption limits apply to the coupon across every customer. For example, if you limit the number of times a coupon can be redeemed to 50, you can apply it to your customers only 50 times. This can be one time each for 50 different customers, one customer 50 times, or multiple customers multiple times until the max of 50 times.

If you set a coupon to last forever when a customer uses it but the coupon has an expiration date, any customer given that coupon will have that coupon’s discount forever. No new customers can apply the coupon after the expiration date.

Promotion codes are customer-facing codes that you create for coupons. For example, FALLPROMO and SPRINGPROMO can both point to a single 25% off coupon. You can share promotion codes directly with your customers to use at checkout.

If you’ve implemented the [customer portal](https://docs.stripe.com/billing/subscriptions/customer-portal) and turned on promotion codes, customers can apply a discount when upgrading or downgrading their existing subscriptions in the portal.

#### Caution

Subscriptions apply promotion code and price updates separately, which might cause unexpected updates. For example, a payment failure can cause a price upgrade to fail, but the promotion code included with the price upgrade succeeds.

#### Caution

The customer portal displays promotion codes that have been applied to a subscription. If you don’t want to allow customers to apply the promotion code themselves or potentially share it with others, you should either [set limits on the promotion code](#promo-code-config) or [apply a coupon](#discount-subscriptions) directly.

Customize controls and limits on promotion codes by specifying eligible customers, first time orders, minimum order values, expiration dates, and redemption limits.

### Restrictions

There are some restrictions to promotion codes.

*   You can’t apply a promotion code with amount restrictions on:
    *   [Subscription Item objects](https://docs.stripe.com/api/subscription_items/object)
    *   [Invoice Item objects](https://docs.stripe.com/api/invoiceitems/object)
    *   [Subscriptions objects](https://docs.stripe.com/api/subscriptions/object) when you make an update
    *   Future phases on [Subscription Schedule objects](https://docs.stripe.com/api/subscription_schedules/object)

### Create promotion codes

You can create a promotion code in the Dashboard when you [create a coupon](#create-a-coupon).

The **Code** is case-insensitive and unique across active promotion codes for any customer. For example:

*   You can create multiple customer-restricted promotion codes with the same **Code**, but you can’t reuse that **Code** for a promotion code that any customer can redeem.
*   If you create a promotion code that is redeemable by any customer, you can’t create another active promotion code with the same **code**.
*   You can create a promotion code with one **Code**, [inactivate](#deactivate) it, and then create a new promotion code with the same **Code**.

1.  In the Dashboard on the [Create a coupon](https://dashboard.stripe.com/test/coupons/create) page, click the **Use customer-facing coupon codes** button.
2.  Enter a code. This is the code that a customer enters at checkout to redeem the discount. If you don’t set a code, Stripe generates one for you.
3.  Select requirements for the promotion code. For example, you can restrict the coupon to only being valid on first-time orders.

When you create a promotion code, it inherits the configuration of the associated coupon.

### Promotion code configurations

By configuring the promotion code settings, you can customize the following:

*   Which customers are eligible to use a promotion code
*   How many times a customer can redeem a promotion code
*   When a promotion code expires
*   Set a minimum amount a promotion code can apply to

### Limit by customer

To limit a promotion code to a particular customer, complete these steps:

1.  On the [Create a coupon](https://dashboard.stripe.com/test/coupons/create) page, select **Limit to a specific customer**.
2.  Select the relevant customer. If you don’t specify a customer, any customer can redeem the promotion code.

### Limit by first time order

Restricts the coupon to customers who have no prior transaction history on your platform. This setting prevents customers from using the coupon if they:

*   Initiated a PaymentIntent, even if the payment never completed.
*   Subscribed to a trial period, even if it subsequently canceled.

To limit a promotion code to first-time customers, on the [Create a coupon](https://dashboard.stripe.com/test/coupons/create) page, select **Eligible for first-time order only**.

### Set a minimum amount

To set an minimum amount that is eligible for a promotion code, on the [Create a coupon](https://dashboard.stripe.com/test/coupons/create) page, select **Require minimum order value** and enter the minimum value.

Because promotion code restrictions are checked at redemption time, the minimum transaction amount only applies to the initial payment for a subscription.

If the coupon supports multiple currencies, the minimum amount can be different per-currency.

### Customize expirations

To set an expiration date for a promotion code, on the [Create a coupon](https://dashboard.stripe.com/test/coupons/create) page, select **Add an expiration date** and the date and time at which the promotion code expires.

If the underlying coupon already has an expiration date set, then the promotion code’s expiration date can’t be later than the coupon’s.

For example, you might have plans to support a coupon for a year, but you only want it to be redeemable for one week after a customer receives it. To do this, set the coupon’s expiration date to one year from now, and set each the promotion code’s expiration date to one week after it’s created.

### Limit redemptions

To set the total number of times the promotion code can be redeemed by your customers, select **Limit the number of times this code can be redeemed** on the [Create a coupon](https://dashboard.stripe.com/test/coupons/create) page and enter the number. See [Redemption limits](#redemption-limits) for details.

If the underlying coupon already has a maximum number of times set, then the promotion code’s maximum redemptions can’t be greater than the coupon’s.

### Deactivate promotion codes

To deactivate a promotion code, doing the following steps:

1.  In the Dashboard, open the [Products](https://dashboard.stripe.com/test/products?active=true) page.
2.  Click **Coupons**.
3.  Click the coupon whose promotion code you want to deactivate.
4.  In the relevant promotion code row, click the overflow menu ().
5.  Click **Archive promotion code**.

However, if the underlying coupon for a promotion code becomes invalid, all of its promotion codes become permanently inactive. Similarly, if a promotion code reaches its maximum redemption limit or its expiration date, it becomes permanently inactive. These promotion codes can’t be reactivated.

### Apply promotion codes to subscriptions

After you create a promotion code, redeem a discount by applying the promotion code to a subscription. You can apply promotion codes two ways:

*   When you [create a subscription](https://docs.stripe.com/api#create_subscription)
*   When you [update a customer’s existing subscription](https://docs.stripe.com/api#update_subscription)

1.  In the Dashboard, go to **Billing** > **Subscriptions**.
2.  Click the relevant subscription.
3.  Click **Actions** > **Update subscription** > **Add coupon**.
4.  Click a promotion code from the dropdown menu and click **Submit**.

### Add promotion codes to Checkout

Enable promotion codes with the API by setting the [allow\_promotion\_codes](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes) parameter in Checkout Sessions. When `allow_promotion_codes` is enabled on a Checkout Session, Checkout includes a promotion code redemption box for your customers to use.

![Promotion code field at checkout](https://b.stripecdn.com/docs-statics-srv/assets/promo_code_checkout.c07ef6d4f0b1b3f9a8a7e4bbba83d56f.png)

Promotion code field at checkout

## Stackable coupons and promotion codes

You can add multiple coupons, promotion codes, or redeemed [discounts](https://docs.stripe.com/api/#discounts) to a customer’s list of charges. You can do this when [creating a subscription](https://docs.stripe.com/api#create_subscription) or by [updating a customer’s existing subscription](https://docs.stripe.com/api#update_subscription).

We support multiple discounts on both subscriptions and subscription items.

When you create a subscription with stackable discounts, each discount applies to all items on the subscription. The order of the discounts is important if you use both `amount_off` and `percent_off`. For example, the following stacked discounts apply differently:

*   20% off _then_ 5 USD off
*   5 USD off _then_ 20% off

1.  In the Dashboard, go to **Billing** > **Subscriptions**.
2.  Click the relevant subscription.
3.  Click **Actions** > **Update subscription** > **Add coupon**.
4.  Click coupons from the dropdown menus and click **Submit**.
5.  Click the relevant product.
6.  Click **Add coupons**.
7.  Click coupons from the dropdown menus and click **Submit**.

### Restrictions

There are some restrictions to using multiple discounts.

*   You can set up to 20 entries in the `discounts` parameter.
*   Each entry in `discounts` has to be unique.
*   You can’t pass in a coupon and a promotion code created from the same coupon.
*   You can’t pass in a coupon and a discount that is generated from the same coupon.
*   Redeemed discounts must already be attached to the customer or subscription that you’re updating.

### Update a subscription

You don’t need to set `discounts` if you don’t intend to make changes to existing discounts.

When updating `discounts`, you need to pass in any previously set `coupon`, `promotion_code` or `discount` you want to keep on the subscription.

Pass `discounts = ""` to clear all discounts from the subscription. When a subscription has no discounts, the customer-level discount, if any, applies to invoices.

If you’ve already set more than one discount on a subscription with the new `discounts` parameter, you can’t update the subscription with the deprecated `coupon` or `promotion_code` parameter. Similarly, you can’t update a schedule’s phases with the deprecated `coupon` or `promotion_code` parameter if you’ve set more than one discount on a prior phase.

Updating `discounts` doesn’t incur prorations or generate an invoice on its own. The new discounts are applied the next time the subscription creates an invoice.

#### Note

Updating subscription-level promotion codes, coupons, or discounts by themselves doesn’t create proration invoice items. Only changes that affect billable amounts for the current billing cycle create prorations—for example, changing a subscription item’s `price` or `quantity`, adding or removing subscription items, or changing billing cycle anchors.

However, when you combine a discount change with a proration-triggering update (such as changing an item quantity and modifying a discount in the same API call), Stripe computes proration amounts using the subscription’s updated pricing and discounting state. The proration debit or credit reflects the modified discounts.

## Alternative discount methods

Although coupons are the most common way to discount a subscription, you can also do the following:

*   Add a negative [customer balance](https://docs.stripe.com/api#customer_object-balance) to the customer.
*   Add negative [invoice items](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items).
*   Add a [second price](https://docs.stripe.com/products-prices/manage-prices#create-price) that is a cheaper version of a product’s usual price.

Of these methods, negative invoice items provide more detailed information as to what discount was created, when, and why.

## See also

*   [Changing subscriptions](https://docs.stripe.com/billing/subscriptions/change)
*   [Prorations](https://docs.stripe.com/billing/subscriptions/prorations)
*   [Working with invoices](https://docs.stripe.com/billing/invoices/subscription)
*   [Coupons API](https://docs.stripe.com/api#coupons)
*   [Promotion codes API](https://docs.stripe.com/api#promotion_codes)
