---
title: "Manage Monthly Active SSO Users usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users-sso"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/monthly-active-users-sso"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:10.201Z"
content_hash: "0e22e4a5d910e284ca0d95eccca86dc68911b806ef2265fb67378923f4dd32b2"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Monthly Active SSO Users","Monthly Active SSO Users"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Monthly Active SSO Users","Monthly Active SSO Users"]
nav_prev: {"path": "../monthly-active-users/index.md", "title": "Manage Monthly Active Users usage"}
nav_next: {"path": "../point-in-time-recovery/index.md", "title": "Manage Point-in-Time Recovery usage"}
---

# 

Manage Monthly Active SSO Users usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

You are charged for the number of distinct users who log in or refresh their token during the billing cycle using a SAML 2.0 compatible identity provider (e.g. Google Workspace, Microsoft Active Directory). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "SSO MAUs".

### Example[#](#example)

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single SSO MAU for this billing cycle.

1

### Sign User-1 in on January 3

The SSO MAU count increases from 0 to 1.

```
1const { data, error } = await supabase.auth.signInWithSSO({2domain: 'company.com'3})45if (data?.url) {6// redirect User-1 to the identity provider's authentication flow7window.location.href = data.url8}
```

2

### Sign User-1 out on January 4

```
1const { error } = await supabase.auth.signOut()
```

3

### Sign User-1 in again on January 17

The SSO MAU count remains 1.

```
1const { data, error } = await supabase.auth.signInWithSSO({2domain: 'company.com'3})45if (data?.url) {6// redirect User-1 to the identity provider's authentication flow7window.location.href = data.url8}
```

## How charges are calculated[#](#how-charges-are-calculated)

You are charged by SSO MAU.

### Usage on your invoice[#](#usage-on-your-invoice)

Usage is shown as "Monthly Active SSO Users" on your invoice.

## Pricing[#](#pricing)

## Pricing[#](#pricing)

$0.015 per SSO MAU. You are only charged for usage exceeding your subscription plan's quota.

For a detailed breakdown of how charges are calculated, refer to [Manage Monthly Active SSO Users usage](/docs/guides/platform/manage-your-usage/monthly-active-users-sso).

The count resets at the start of each billing cycle.

Plan

Quota

Over-Usage

Pro

50

$0.015 per SSO MAU

Team

50

$0.015 per SSO MAU

Enterprise

Custom

Custom

## Billing examples[#](#billing-examples)

### Within quota[#](#within-quota)

The organization's SSO MAU usage for the billing cycle is within the quota, so no charges apply.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Monthly Active SSO Users

37 SSO MAU

$0

**Subtotal**

**$35**

Compute Credits

\-$10

**Total**

**$25**

### Exceeding quota[#](#exceeding-quota)

The organization's SSO MAU usage for the billing cycle exceeds the quota by 10, incurring charges for this additional usage.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Monthly Active SSO Users

60 SSO MAU

$0.15

**Subtotal**

**$35.15**

Compute Credits

\-$10

**Total**

**$25.15**

## View usage[#](#view-usage)

You can view Monthly Active SSO Users usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

![Usage page navigation bar](/docs/img/guides/platform/usage-navbar--light.png)

In the Monthly Active SSO Users section, you can see the usage for the selected time period.

![Usage page Monthly Active SSO Users section](/docs/img/guides/platform/usage-mau-sso--light.png)

## Exceeding Quotas[#](#exceeding-quotas)

If you are on a paid plan and have [Spend Cap](/docs/guides/platform/cost-control#spend-cap) disabled or your organization is on Team Plan or above, you will pay for any overages.

When you are exceeding your quotas while being on a Free Plan or having [Spend Cap](/docs/guides/platform/cost-control#spend-cap) enabled, you will get a notification to your billing email address and put under a grace period. For more details, refer to our [Fair Use Policy](/docs/guides/platform/billing-faq#fair-use-policy).
