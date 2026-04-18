---
title: "Manage Monthly Active Users usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:10.810Z"
content_hash: "0dc594528a12f010be551cd0bb10c03c69dc12fe065ef0125c1424e8209d36d6"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Monthly Active Users","Monthly Active Users"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Monthly Active Users","Monthly Active Users"]
---
# 

Manage Monthly Active Users usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

You are charged for the number of distinct users who log in or refresh their token during the billing cycle (including Social Login with e.g. Google, Facebook, GitHub). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "MAUs".

### Example[#](#example)

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single MAU for this billing cycle.

1

### Sign User-1 in on January 3

The MAU count increases from 0 to 1.

```
1const {data, error} = await supabase.auth.signInWithPassword({2email: 'user-1@email.com',3password: 'example-password-1',4})
```

2

### Sign User-1 out on January 4

`javascript const {error} = await supabase.auth.signOut()`

3

### Sign User-1 in again on January 17

The MAU count remains 1.

```
1const {data, error} = await supabase.auth.signInWithPassword({2email: 'user-1@email.com',3password: 'example-password-1',4})
```

## How charges are calculated[#](#how-charges-are-calculated)

You are charged by MAU.

### Usage on your invoice[#](#usage-on-your-invoice)

Usage is shown as "Monthly Active Users" on your invoice.

## Pricing[#](#pricing)

$0.00325 per MAU. You are only charged for usage exceeding your subscription plan's quota.

The count resets at the start of each billing cycle.

Plan

Quota

Over-Usage

Free

50,000

\-

Pro

100,000

$0.00325 per MAU

Team

100,000

$0.00325 per MAU

Enterprise

Custom

Custom

## Billing examples[#](#billing-examples)

### Within quota[#](#within-quota)

The organization's MAU usage for the billing cycle is within the quota, so no charges apply.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Monthly Active Users

23,000 MAU

$0

**Subtotal**

**$35**

Compute Credits

\-$10

**Total**

**$25**

### Exceeding quota[#](#exceeding-quota)

The organization's MAU usage for the billing cycle exceeds the quota by 60,000, incurring charges for this additional usage.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Monthly Active Users

160,000 MAU

$195

**Subtotal**

**$230**

Compute Credits

\-$10

**Total**

**$220**

## View usage[#](#view-usage)

You can view Monthly Active Users usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

![Usage page navigation bar](/docs/img/guides/platform/usage-navbar--light.png)

In the Monthly Active Users section, you can see the usage for the selected time period.

![Usage page Monthly Active Users section](/docs/img/guides/platform/usage-mau--light.png)

## Exceeding Quotas[#](#exceeding-quotas)

If you are on a paid plan and have [Spend Cap](/docs/guides/platform/cost-control#spend-cap) disabled or your organization is on Team Plan or above, you will pay for any overages.

When you are exceeding your quotas while being on a Free Plan or having [Spend Cap](/docs/guides/platform/cost-control#spend-cap) enabled, you will get a notification to your billing email address and put under a grace period. For more details, refer to our [Fair Use Policy](/docs/guides/platform/billing-faq#fair-use-policy).
