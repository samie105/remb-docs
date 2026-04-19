---
title: "Manage Advanced MFA Phone usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/advanced-mfa-phone"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/advanced-mfa-phone"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:49.864Z"
content_hash: "49a5e9e10a29099138cd5130186f12a5c8a5cdb3fffde21780696a35de7831a7"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","MFA Phone","MFA Phone"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","MFA Phone","MFA Phone"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/index.md", "title": "Manage your usage"}
nav_next: {"path": "supabase/docs/guides/platform/manage-your-usage/branching/index.md", "title": "Manage Branching usage"}
---

# 

Manage Advanced MFA Phone usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

You are charged for having the feature [Advanced Multi-Factor Authentication Phone](/docs/guides/auth/auth-mfa/phone) enabled for your project.

The Advanced MFA Phone add-on is **not** covered by the [Spend Cap](/docs/guides/platform/cost-control#spend-cap).

Additional charges apply for each SMS or WhatsApp message sent, depending on your third-party messaging provider (such as Twilio or MessageBird).

## How charges are calculated[#](#how-charges-are-calculated)

MFA Phone is charged by the hour, meaning you are charged for the exact number of hours that the feature is enabled for a project. If the feature is enabled for part of an hour, you are still charged for the full hour.

### Example[#](#example)

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you enable the MFA Phone feature for your project. At the end of the billing cycle you are billed for 512 hours.

Time Window

MFA Phone

Hours Billed

Description

January 1, 00:00 AM - January 10, 4:00 PM

Disabled

0

January 10, 04:00 PM - January 10, 4:30 PM

Disabled

0

January 10, 04:30 PM - January 10, 5:00 PM

Enabled

1

full hour is billed

January 10, 05:00 PM - January 31, 23:59 PM

Enabled

511

### Usage on your invoice[#](#usage-on-your-invoice)

Usage is shown as "Auth MFA Phone Hours" on your invoice.

## Pricing[#](#pricing)

## Pricing[#](#pricing)

$0.1027 per hour ($75 per month) for the first project. $0.0137 per hour ($10 per month) for every additional project.

Plan

Project 1 per month

Project 2 per month

Project 3 per month

Pro

$75

$10

$10

Team

$75

$10

$10

Enterprise

Custom

Custom

Custom

For a detailed breakdown of how charges are calculated, refer to [Manage Advanced MFA Phone usage](/docs/guides/platform/manage-your-usage/advanced-mfa-phone).

## Billing examples[#](#billing-examples)

### One project[#](#one-project)

The project has MFA Phone activated throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

MFA Phone Hours

744

$75

**Subtotal**

**$110**

Compute Credits

\-$10

**Total**

**$100**

### Multiple projects[#](#multiple-projects)

All projects have MFA Phone activated throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

MFA Phone Hours Project 1

744

$75

Compute Hours Micro Project 2

744

$10

MFA Phone Hours Project 2

744

$10

Compute Hours Micro Project 3

744

$10

MFA Phone Hours Project 3

744

$10

**Subtotal**

**$150**

Compute Credits

\-$10

**Total**

**$140**

### Add-on disabled after a day[#](#add-on-disabled-after-a-day)

Project add-ons are billed in arrears based on how many hours you used them. If you remove the MFA Phone add-on, you are no longer billed from the time of removal onward.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

MFA Phone Hours Project 1

24

$2.46

**Subtotal**

**$37.46**

Compute Credits

\-$10

**Total**

**$27.46**
