---
title: "Manage IPv4 usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/ipv4"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/ipv4"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:05.879Z"
content_hash: "8d4b430208b80d1c52628c7eff85552aa1c17b558d35c166154d670f4bfb3daf"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","IPv4","IPv4"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","IPv4","IPv4"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/log-drains/index.md", "title": "Manage Log Drain usage"}
nav_next: {"path": "supabase/docs/guides/platform/manage-your-usage/monthly-active-users-sso/index.md", "title": "Manage Monthly Active SSO Users usage"}
---

# 

Manage IPv4 usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

You can assign a dedicated [IPv4 address](/docs/guides/platform/ipv4-address) to a database by enabling the [IPv4 add-on](/dashboard/project/_/settings/addons?panel=ipv4). You are charged for all IPv4 addresses configured across your databases.

IPv4 Hours are **not** covered by the [Spend Cap](/docs/guides/platform/cost-control#spend-cap).

If the primary database has a dedicated IPv4 address configured, its Read Replicas are also assigned one, with charges for each.

## How charges are calculated[#](#how-charges-are-calculated)

IPv4 addresses are charged by the hour, meaning you are charged for the exact number of hours that an IPv4 address is assigned to a database. If an address is assigned for part of an hour, you are still charged for the full hour.

### Example[#](#example)

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you enable the IPv4 add-on for your project. At the end of the billing cycle you are billed for 512 hours.

Time Window

IPv4 add-on

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

Usage is shown as "IPv4 Hours" on your invoice.

## Pricing[#](#pricing)

$0.0055 per hour ($4 per month).

## Billing examples[#](#billing-examples)

### One project[#](#one-project)

The project has the IPv4 add-on enabled throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

IPv4 Hours

744

$4

**Subtotal**

**$39**

Compute Credits

\-$10

**Total**

**$29**

### Multiple projects[#](#multiple-projects)

All projects have the IPv4 add-on enabled throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

IPv4 Hours Project 1

744

$4

Compute Hours Micro Project 2

744

$10

IPv4 Hours Project 2

744

$4

Compute Hours Micro Project 3

744

$10

IPv4 Hours Project 3

744

$4

**Subtotal**

**$67**

Compute Credits

\-$10

**Total**

**$57**

### One project with Read Replicas[#](#one-project-with-read-replicas)

The project has two Read Replicas and the IPv4 add-on enabled throughout the entire billing cycle.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Small Project 1

744

$15

IPv4 Hours Project 1

744

$4

Compute Hours Small Replica 1

744

$15

IPv4 Hours Replica 1

744

$4

Compute Hours Small Replica 2

744

$15

IPv4 Hours Replica 2

744

$4

**Subtotal**

**$82**

Compute Credits

\-$10

**Total**

**$72**

### Add-on disabled after a day[#](#add-on-disabled-after-a-day)

Project add-ons are billed in arrears based on how many hours you used them. If you remove the IPv4 add-on, you are no longer billed from the time of removal onward.

Line Item

Hours

Costs

Pro Plan

\-

$25

Compute Hours Micro Project 1

744

$10

IPv4 Hours Project 1

24

$0.13

**Subtotal**

**$35.13**

Compute Credits

\-$10

**Total**

**$25.13**

## Optimize usage[#](#optimize-usage)

To see whether your database actually needs a dedicated IPv4 address, refer to [When you need the IPv4 add-on](/docs/guides/platform/ipv4-address#when-you-need-the-ipv4-add-on).

