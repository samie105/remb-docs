---
title: "Manage your subscription"
source: "https://supabase.com/docs/guides/platform/aws-marketplace/manage-your-subscription"
canonical_url: "https://supabase.com/docs/guides/platform/aws-marketplace/manage-your-subscription"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:47.080Z"
content_hash: "2d4c6d1028cda0595e04096a2057f563dceaaa3adc9ae9db1c34ef65740cfb01"
menu_path: ["Platform","Platform","More","More","More","AWS Marketplace","AWS Marketplace","Manage your subscription","Manage your subscription"]
section_path: ["Platform","Platform","More","More","More","AWS Marketplace","AWS Marketplace","Manage your subscription","Manage your subscription"]
nav_prev: {"path": "supabase/docs/guides/platform/aws-marketplace/invoices/index.md", "title": "Invoices"}
nav_next: {"path": "supabase/docs/guides/platform/backups/index.md", "title": "Database Backups"}
---

# 

Manage your subscription

* * *

## Manage your subscription plan[#](#manage-your-subscription-plan)

Plan changes are not made on the Supabase dashboard, but instead through the AWS Marketplace. The easiest way to navigate to the corresponding page on the marketplace is through the Supabase dashboard.

1.  On the [organization's billing page](/dashboard/org/_/billing), go to section **Subscription Plan**
2.  Click **Change subscription plan**
3.  On the side panel, follow the link to the AWS Marketplace

### Upgrade[#](#upgrade)

You can upgrade your plan at any time. The new plan will be active immediately, and you will be charged a prorated amount for the remainder of the current billing cycle. The charge for the upgrade also factors in the upfront payment you have already made for your existing plan.

![AWS Marketplace modify contract page](/docs/img/guides/platform/aws-marketplace-change-plan.png)

### Downgrade[#](#downgrade)

Downgrades are only possible at the end of the billing cycle, not in the middle of a billing cycle.

#### Downgrade to the Free Plan[#](#downgrade-to-the-free-plan)

If you want your subscription to be downgraded to the Free Plan at the end of the current billing cycle, you need to disable auto-renewal for the marketplace subscription.

If the downgrade causes you to exceed the [free projects limit](../../billing-on-supabase/index.md#free-plan), **all** projects within the organization will be paused. We do not make the decision about which projects continue to run and which are paused. You must then decide which projects you want to keep active and manually reactivate them through the Supabase dashboard.

![AWS Marketplace modify contract page](/docs/img/guides/platform/aws-marketplace-configure-auto-renewal.png)

#### Downgrade to a paid plan[#](#downgrade-to-a-paid-plan)

A downgrade to a paid plan (Pro Plan / Team Plan) involves two steps.

**Step 1:** Let the current subscription on the higher plan expire, meaning turn off auto-renewal **Step 2:** Start a new subscription on the lower plan

## Manage your payment methods[#](#manage-your-payment-methods)

You can manage your payment methods through the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing).

## Manage your billing details[#](#manage-your-billing-details)

You can manage billing details, such as the billing address or tax ID, through the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing).
