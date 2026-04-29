---
title: "Manage Storage size usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/storage-size"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/storage-size"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:20.858Z"
content_hash: "af4018369260e0858d740220134539a273d2999592d6a8091edc2a87eaf7e944"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Storage Size","Storage Size"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Storage Size","Storage Size"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/realtime-peak-connections/index.md", "title": "Manage Realtime Peak Connections usage"}
nav_next: {"path": "supabase/docs/guides/platform/mfa/org-mfa-enforcement/index.md", "title": "Enforce MFA on Organization"}
---

# 

Manage Storage size usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

You are charged for the total size of all assets in your buckets.

## How charges are calculated[#](#how-charges-are-calculated)

Storage size is charged by Gigabyte-Hours (GB-Hrs). 1 GB-Hr represents the use of 1 GB of storage for 1 hour. For example, storing 10 GB of data for 5 hours results in 50 GB-Hrs (10 GB × 5 hours).

### Usage on your invoice[#](#usage-on-your-invoice)

Usage is shown as "Storage Size GB-Hrs" on your invoice.

## Pricing[#](#pricing)

$0.00002919 per GB-Hr ($0.021 per GB per month). You are only charged for usage exceeding your subscription plan's quota.

Plan

Quota in GB

Over-Usage per GB

Quota in GB-Hrs

Over-Usage per GB-Hr

Free

1

\-

744

\-

Pro

100

$0.021

74,400

$0.00002919

Team

100

$0.021

74,400

$0.00002919

Enterprise

Custom

Custom

Custom

Custom

## Billing examples[#](#billing-examples)

### Within quota[#](#within-quota)

The organization's Storage size usage is within the quota, so no charges for Storage size apply.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Storage Size

85 GB

$0

**Subtotal**

**$35**

Compute Credits

\-$10

**Total**

**$25**

### Exceeding quota[#](#exceeding-quota)

The organization's Storage size usage exceeds the quota by 257 GB, incurring charges for this additional usage.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Micro

744 hours

$10

Storage Size

357 GB

$5.4

**Subtotal**

**$40.4**

Compute Credits

\-$10

**Total**

**$30.4**

## View usage[#](#view-usage)

### Usage page[#](#usage-page)

You can view Storage size usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

![Usage page navigation bar](/docs/img/guides/platform/usage-navbar--light.png)

In the Storage size section, you can see how much storage your projects have used during the selected time period.

![Usage page Storage Size section](/docs/img/guides/platform/usage-storage-size--light.png)

### SQL Editor[#](#sql-editor)

Since we designed Storage to work as an integrated part of your Postgres database on Supabase, you can query information about your Storage objects in the `storage` schema.

List files larger than 5 MB:

```
1select2    name,3    bucket_id as bucket,4    case5        when (metadata->>'size')::int >= 1073741824 then6            ((metadata->>'size')::int / 1073741824.0)::numeric(10, 2) || ' GB'7        when (metadata->>'size')::int >= 1048576 then8            ((metadata->>'size')::int / 1048576.0)::numeric(10, 2) || ' MB'9        when (metadata->>'size')::int >= 1024 then10            ((metadata->>'size')::int / 1024.0)::numeric(10, 2) || ' KB'11        else12            (metadata->>'size')::int || ' bytes'13        end as size14from15    storage.objects16where17    (metadata->>'size')::int > 1048576 * 518order by (metadata->>'size')::int desc
```

List buckets with their total size:

```
1select2    bucket_id,3    (sum((metadata->>'size')::int) / 1048576.0)::numeric(10, 2) as total_size_megabyte4from5    storage.objects6group by7    bucket_id8order by9    total_size_megabyte desc;
```

## Optimize usage[#](#optimize-usage)

*   [Limit the upload size](../../../storage/production/scaling/index.md#limit-the-upload-size) for your buckets
*   [Delete assets](../../../storage/management/delete-objects/index.md) that are no longer in use

## Exceeding Quotas[#](#exceeding-quotas)

If you are on a paid plan and have [Spend Cap](../../cost-control/index.md#spend-cap) disabled or your organization is on Team Plan or above, you will pay for any overages.

When you are exceeding your quotas while being on a Free Plan or having [Spend Cap](../../cost-control/index.md#spend-cap) enabled, you will get a notification to your billing email address and put under a grace period. For more details, refer to our [Fair Use Policy](../../billing-faq/index.md#fair-use-policy).
