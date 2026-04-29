---
title: "Manage Custom Domain usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/custom-domains"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/custom-domains"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:54.879Z"
content_hash: "e99bc456a50ffec6e45c65e9dbf410c0c0310b4c59c42a8ece7a063d3f399dcf"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Custom Domains","Custom Domains"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Custom Domains","Custom Domains"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/compute/index.md", "title": "Manage Compute usage"}
nav_next: {"path": "supabase/docs/guides/platform/manage-your-usage/disk-iops/index.md", "title": "Manage Disk IOPS usage"}
---

# 

Manage Custom Domain usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

You can configure a [custom domain](../../custom-domains/index.md) for a project by enabling the [Custom Domain add-on](/dashboard/project/_/settings/addons?panel=customDomain). You are charged for all custom domains configured across your projects.

Custom Domains are **not** covered by the [Spend Cap](../../cost-control/index.md#spend-cap).

## How charges are calculated[#](#how-charges-are-calculated)

Custom domains are charged by the hour, meaning you are charged for the exact number of hours that a custom domain is active. If a custom domain is active for part of an hour, you are still charged for the full hour.

### Example[#](#example)

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you activate a custom domain for your project. At the end of the billing cycle you are billed for 512 hours.

Time Window

Custom Domain Activated

Hours Billed

Description

January 1, 00:00 AM - January 10, 4:00 PM

No

0

January 10, 04:00 PM - January 10, 4:30 PM

No

0

January 10, 04:30 PM - January 10, 5:00 PM

Yes

1

full hour is billed

January 10, 05:00 PM - January 31, 23:59 PM

Yes

511

### Usage on your invoice[#](#usage-on-your-invoice)

Usage is shown as "Custom Domain Hours" on your invoice.

## Pricing[#](#pricing)

$0.0137 per hour ($10 per month).

## Billing examples[#](#billing-examples)

### One project[#](#one-project)

The project has a custom domain activated throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

Custom Domain Hours

744

$10

**Subtotal**

**$45**

Compute Credits

\-$10

**Total**

**$35**

### Multiple projects[#](#multiple-projects)

All projects have a custom domain activated throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

Custom Domain Hours Project 1

744

$10

Compute Hours Micro Project 2

744

$10

Custom Domain Hours Project 2

744

$10

**Subtotal**

**$65**

Compute Credits

\-$10

**Total**

**$55**

### Add-on disabled after a day[#](#add-on-disabled-after-a-day)

Project add-ons are billed in arrears based on how many hours you used them. If you remove the custom domain add-on, you are no longer billed from the time of removal onward.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

Custom Domain Hours Project 1

24

$0.33

**Subtotal**

**$35.33**

Compute Credits

\-$10

**Total**

**$25.33**

## Optimize usage[#](#optimize-usage)

*   Regularly check your projects and remove custom domains that are no longer needed
*   Use free [Vanity subdomains](../../custom-domains/index.md#vanity-subdomains) where applicable
