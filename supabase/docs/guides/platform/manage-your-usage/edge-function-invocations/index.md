---
title: "Manage Edge Function Invocations usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/edge-function-invocations"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/edge-function-invocations"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:00.622Z"
content_hash: "d3868e7194b1b81e09f9f0ff1bfbbc8077f44b3f18574599a2dbd35286bfc19e"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Edge Function Invocations","Edge Function Invocations"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Edge Function Invocations","Edge Function Invocations"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/disk-throughput/index.md", "title": "Manage Disk Throughput usage"}
nav_next: {"path": "supabase/docs/guides/platform/manage-your-usage/egress/index.md", "title": "Manage Egress usage"}
---

# 

Manage Edge Function Invocations usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

You are charged for the number of times your functions get invoked, regardless of the response status code. Preflight (OPTIONS) requests are not billed.

## How charges are calculated[#](#how-charges-are-calculated)

Edge Function Invocations are billed using Package pricing, with each package representing 1 million invocations. If your usage falls between two packages, you are billed for the next whole package.

### Example[#](#example)

For simplicity, let's assume a package size of 1 million and a charge of $2 per package without a free quota.

Invocations

Packages Billed

Costs

999,999

1

$2

1,000,000

1

$2

1,000,001

2

$4

1,500,000

2

$4

### Usage on your invoice[#](#usage-on-your-invoice)

Usage is shown as "Function Invocations" on your invoice.

## Pricing[#](#pricing)

$2 per 1 million invocations. You are only charged for usage exceeding your subscription plan's quota.

Plan

Quota

Over-Usage

Free

500,000

\-

Pro

2 million

$2 per 1 million invocations

Team

2 million

$2 per 1 million invocations

Enterprise

Custom

Custom

## Billing examples[#](#billing-examples)

### Within quota[#](#within-quota)

The organization's function invocations are within the quota, so no charges apply.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Function Invocations

1,800,000 invocations

$0

**Subtotal**

**$35**

Compute Credits

\-$10

**Total**

**$25**

### Exceeding quota[#](#exceeding-quota)

The organization's function invocations exceed the quota by 1.4 million, incurring charges for this additional usage.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Function Invocations

3,400,000 invocations

$4

**Subtotal**

**$39**

Compute Credits

\-$10

**Total**

**$29**

## View usage[#](#view-usage)

You can view Edge Function Invocations usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

![Usage page navigation bar](/docs/img/guides/platform/usage-navbar--light.png)

In the Edge Function Invocations section, you can see how many invocations your projects have had during the selected time period.

![Usage page Edge Function Invocations section](/docs/img/guides/platform/usage-function-invocations--light.png)

## Exceeding Quotas[#](#exceeding-quotas)

If you are on a paid plan and have [Spend Cap](/docs/guides/platform/cost-control#spend-cap) disabled or your organization is on Team Plan or above, you will pay for any overages.

When you are exceeding your quotas while being on a Free Plan or having [Spend Cap](/docs/guides/platform/cost-control#spend-cap) enabled, you will get a notification to your billing email address and put under a grace period. For more details, refer to our [Fair Use Policy](/docs/guides/platform/billing-faq#fair-use-policy).

