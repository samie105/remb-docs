---
title: "Manage Compute usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/compute"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/compute"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:52.664Z"
content_hash: "cd02372b2e9659df4a6f84e9d991b2598cca93e180ade5c3f0fb53f71e0bd78e"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Compute","Compute"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Compute","Compute"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/branching/index.md", "title": "Manage Branching usage"}
nav_next: {"path": "supabase/docs/guides/platform/manage-your-usage/custom-domains/index.md", "title": "Manage Custom Domain usage"}
---

# 

Manage Compute usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

Each project on the Supabase platform includes a dedicated Postgres instance running on its own server. You are charged for the [Compute](/docs/guides/platform/compute-and-disk#compute) resources of that server, independent of your database usage.

Paused projects do not count towards Compute usage. Compute Hours are **not** covered by the [Spend Cap](/docs/guides/platform/cost-control#spend-cap).

## How charges are calculated[#](#how-charges-are-calculated)

Compute is charged by the hour, meaning you are charged for the exact number of hours that a project is running and, therefore, incurring Compute usage. If a project runs for part of an hour, you are still charged for the full hour.

Each project you launch increases your monthly Compute costs.

### Example[#](#example)

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you switch your project from the Micro Compute size to the Small Compute size. At the end of the billing cycle you are billed for 233 hours of Micro Compute size and 511 hours of Small Compute size.

Time Window

Compute Size

Hours Billed

Description

January 1, 00:00 AM - January 10, 4:00 PM

Micro

232

January 10, 04:00 PM - January 10, 4:30 PM

Micro

1

full hour is billed

January 10, 04:30 PM - January 10, 5:00 PM

Small

1

full hour is billed

January 10, 05:00 PM - January 31, 23:59 PM

Small

511

### Usage on your invoice[#](#usage-on-your-invoice)

Usage is shown as "Compute Hours" on your invoice.

## Compute Credits[#](#compute-credits)

Paid plans include $10 in Compute Credits, which cover one project running on the Micro/Nano Compute size or portions of other Compute sizes. Compute Credits are applied to your Compute costs and are provided to an organization each month. They reset monthly and do not accumulate.

## Pricing[#](#pricing)

Compute Size

Hourly Price USD

Monthly Price USD

Nano[1](#user-content-fn-1)

$0

$0

Micro

$0.01344

~$10

Small

$0.0206

~$15

Medium

$0.0822

~$60

Large

$0.1517

~$110

XL

$0.2877

~$210

2XL

$0.562

~$410

4XL

$1.32

~$960

8XL

$2.562

~$1,870

12XL

$3.836

~$2,800

16XL

$5.12

~$3,730

\>16XL

\-

[Contact Us](/dashboard/support/new?category=sales&subject=Enquiry%20about%20larger%20instance%20sizes)

##### Nano Compute size in paid plan organizations

In paid organizations, Nano Compute are billed at the same price as Micro Compute. It is recommended to upgrade your Project from Nano Compute to Micro Compute when it's convenient for you. Compute sizes are not auto-upgraded because of the downtime incurred. See [Supabase Pricing](/pricing) for more information. You cannot launch Nano instances on paid plans, only Micro and above - but you might have Nano instances after upgrading from Free Plan.

## Billing examples[#](#billing-examples)

### One project[#](#one-project)

The project runs on the same Compute size throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

**Subtotal**

**$35**

Compute Credits

\-$10

**Total**

**$25**

### Multiple projects[#](#multiple-projects)

All projects run on the same Compute size throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

Compute Hours Micro Project 2

744

$10

Compute Hours Micro Project 3

744

$10

**Subtotal**

**$55**

Compute Credits

\-$10

**Total**

**$45**

### One project on different Compute sizes[#](#one-project-on-different-compute-sizes)

The project's Compute size changes throughout the billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

233

$3

Compute Hours Small Project 1

511

$11

**Subtotal**

**$39**

Compute Credits

\-$10

**Total**

**$29**

### Projects not running for full month[#](#projects-not-running-for-full-month)

One project is running for the entire month, two other projects were launched and deleted within a few days. We only bill for the hours while the project was running and billing stops once a project is deleted. Compute is always billed in arrears when your billing cycle resets.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

Compute Hours Micro Project 2

20

$0.27

Compute Hours Micro Project 3

70

$0.94

**Subtotal**

**$36.21**

Compute Credits

\-$10

**Total**

**$26.21**

## View usage[#](#view-usage)

You can view Compute usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

![Usage page navigation bar](/docs/img/guides/platform/usage-navbar--light.png)

In the Compute Hours section, you can see how many hours of a specific Compute size your projects have used during the selected time period. Hover over a specific date for a daily breakdown.

![Usage page Compute Hours section](/docs/img/guides/platform/usage-compute--light.png)

## Optimize usage[#](#optimize-usage)

*   Start out on a smaller Compute size, [create a report](/dashboard/project/_/observability) on the Dashboard to monitor your CPU and memory utilization, and upgrade the Compute size as needed
*   Load test your application in staging to understand your Compute requirements
*   [Transfer projects](/docs/guides/platform/project-transfer) to a Free Plan organization to reduce Compute usage
*   Delete unused projects

## FAQ[#](#faq)

### Do Compute Credits apply to line items other than Compute?[#](#do-compute-credits-apply-to-line-items-other-than-compute)

No, Compute Credits apply only to Compute and do not cover other line items, including Read Replica Compute and Branching Compute.

## Footnotes[#](#footnote-label)

1.  Compute resources on the Free Plan are subject to change. [↩](#user-content-fnref-1)


