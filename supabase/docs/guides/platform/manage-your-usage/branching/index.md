---
title: "Manage Branching usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/branching"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/branching"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:50.035Z"
content_hash: "8b571f8f717bd8b87cd4ef3fc06fd6982d70177bc4bd122730ed1b11c7b961e0"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Branching","Branching"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Branching","Branching"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/advanced-mfa-phone/index.md", "title": "Manage Advanced MFA Phone usage"}
nav_next: {"path": "supabase/docs/guides/platform/manage-your-usage/compute/index.md", "title": "Manage Compute usage"}
---

# 

Manage Branching usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

Each [Preview branch](../../../deployment/branching/index.md) is a separate environment with all Supabase services (Database, Auth, Storage, etc.). You're charged for usage within that environment—such as [Compute](../compute/index.md), [Disk Size](../disk-size/index.md), [Egress](../egress/index.md), and [Storage](../storage-size/index.md)—just like the project you branched from.

Usage by Preview branches counts toward your subscription plan's quota. Branches are **not** covered by the [Spend Cap](../../cost-control/index.md#spend-cap).

## How charges are calculated[#](#how-charges-are-calculated)

Refer to individual [usage items](../index.md) for details on how charges are calculated. Branching charges are the sum of all these items.

### Usage on your invoice[#](#usage-on-your-invoice)

Compute incurred by Preview branches is shown as "Branching Compute Hours" on your invoice. Other usage items are not shown separately for branches and are rolled up into the project.

## Pricing[#](#pricing)

There is no fixed fee for a Preview branch. You only pay for the usage it incurs. A branch running on the default Micro Compute size starts at $0.01344 per hour.

## Billing examples[#](#billing-examples)

The project has a Preview branch "XYZ", that runs for 30 hours, incurring Compute and Egress costs. Disk Size usage remains within the 8 GB included in the subscription plan, so no additional charges apply.

Line Item

Costs

Pro Plan

$25

Compute Hours Small Project 1

$15

Egress Project 1

$7

Disk Size Project 1

$3

Compute Hours Micro Branch XYZ

$0.4

Egress Branch XYZ

$1

Disk Size Branch XYZ

$0

**Subtotal**

**$51.4**

Compute Credits

\-$10

**Total**

**$41.4**

## View usage[#](#view-usage)

You can view Branching usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

![Usage page navigation bar](/docs/img/guides/platform/usage-navbar--light.png)

In the Usage Summary section, you can see how many hours your Preview branches existed during the selected time period. Hover over "Branching Compute Hours" for a detailed breakdown.

![Usage summary Branching Compute Hours](/docs/img/guides/platform/usage-summary-branch-hours--light.png)

## Optimize usage[#](#optimize-usage)

*   Merge Preview branches as soon as they are ready
*   Delete Preview branches that are no longer in use
*   Check whether your [persistent branches](../../../deployment/branching/index.md#persistent-branches) need to be defined as persistent, or if they can be ephemeral instead. Persistent branches will remain active even after the underlying PR is closed.

## FAQ[#](#faq)

### Do Compute Credits apply to Branching Compute?[#](#do-compute-credits-apply-to-branching-compute)

No, Compute Credits do not apply to Branching Compute.
