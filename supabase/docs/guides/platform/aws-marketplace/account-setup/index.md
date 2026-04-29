---
title: "Account Setup"
source: "https://supabase.com/docs/guides/platform/aws-marketplace/account-setup"
canonical_url: "https://supabase.com/docs/guides/platform/aws-marketplace/account-setup"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:38.562Z"
content_hash: "3e5deef22970536b134dc57118a68c5d0014928f2606aca6d4801e7808f5763e"
menu_path: ["Platform","Platform","More","More","More","AWS Marketplace","AWS Marketplace","Account Setup","Account Setup"]
section_path: ["Platform","Platform","More","More","More","AWS Marketplace","AWS Marketplace","Account Setup","Account Setup"]
nav_prev: {"path": "supabase/docs/guides/platform/aws-marketplace/index.md", "title": "AWS Marketplace"}
nav_next: {"path": "supabase/docs/guides/platform/aws-marketplace/faq/index.md", "title": "AWS Marketplace FAQ"}
---

# 

Account Setup

* * *

After purchasing a Supabase subscription on the AWS Marketplace, the next and final step is to link the newly purchased subscription to a Supabase organization. This can either be an existing organization or a newly created one.

An AWS Marketplace subscription is linked to exactly one Supabase organization. If you want to manage multiple organizations through the AWS Marketplace, you must purchase a separate marketplace subscription for each organization.

![Supabase product subscribe](/docs/img/guides/platform/aws-marketplace-onboarding-page-extended--light.png)

## Implications of linking a Supabase organization to a marketplace subscription[#](#implications-of-linking-a-supabase-organization-to-a-marketplace-subscription)

*   The billing details from your AWS account, such as the billing address and tax ID, are used. These details are managed through the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing).
*   The subscription plan is managed through the AWS Marketplace. You can read more about this in the [Manage your subscription](./manage-your-subscription#manage-your-subscription-plan) guide.
*   Charges will come from AWS rather than Supabase, using the default payment method set in your AWS account.
*   The [Spend Cap](../../cost-control/index.md#spend-cap) for the organization is disabled. The Spend Cap is not available for organizations managed through AWS.
*   When you downgrade your plan to the Free Plan, all projects within the organization will be paused if you exceed the [free projects limit](../../billing-on-supabase/index.md#free-plan).

### Linking an existing Supabase organization[#](#linking-an-existing-supabase-organization)

Linking an existing organization will result in the following:

*   The organization will be upgraded or downgraded to the plan purchased on the AWS Marketplace.
*   The organization’s billing cycle will be adjusted. The start date will be set to the date your marketplace subscription became active.
*   The credit card you have on file with Supabase may receive a closing charge. This charge covers usage costs incurred up until the point when the marketplace subscription became active.

## Prerequisites for linking a Supabase organization to a marketplace subscription[#](#prerequisites-for-linking-a-supabase-organization-to-a-marketplace-subscription)

*   The Supabase user must have the Owner or Admin role
*   There must be no overdue invoices within the organization
*   The organization must not already be managed through another marketplace (e.g. Vercel Marketplace)
