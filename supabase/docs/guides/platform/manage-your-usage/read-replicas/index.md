---
title: "Manage Read Replica usage"
source: "https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas"
canonical_url: "https://supabase.com/docs/guides/platform/manage-your-usage/read-replicas"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:14.451Z"
content_hash: "6587054d5cc0a3b2ec4d2d03167fe692b1f7bcfe0c496a79bcc64099a0559798"
menu_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Read Replicas","Read Replicas"]
section_path: ["Platform","Platform","More","More","More","Manage your usage","Manage your usage","Read Replicas","Read Replicas"]
nav_prev: {"path": "supabase/docs/guides/platform/manage-your-usage/point-in-time-recovery/index.md", "title": "Manage Point-in-Time Recovery usage"}
nav_next: {"path": "supabase/docs/guides/platform/manage-your-usage/realtime-messages/index.md", "title": "Manage Realtime Messages usage"}
---

# 

Manage Read Replica usage

* * *

## What you are charged for[#](#what-you-are-charged-for)

Each [Read Replica](/docs/guides/platform/read-replicas) is a dedicated database. You are charged for its resources, which are the following, and mirrored from the primary database:

*   [Compute](/docs/guides/platform/compute-and-disk#compute)
*   [Disk Size](/docs/guides/platform/database-size#disk-size)
*   Provisioned [Disk IOPS](/docs/guides/platform/compute-and-disk#provisioned-disk-throughput-and-iops)
*   Provisioned [Disk Throughput](/docs/guides/platform/compute-and-disk#provisioned-disk-throughput-and-iops)
*   [IPv4](/docs/guides/platform/ipv4-address).

Read Replicas are **not** covered by the [Spend Cap](/docs/guides/platform/cost-control#spend-cap).

## How we calculate charges[#](#how-we-calculate-charges)

Read Replica charges are the total of the charges listed below.

### Compute[#](#compute)

Compute is charged by the hour, meaning you are charged for the exact number of hours that a Read Replica is running and, therefore, incurring Compute usage. If a Read Replica runs for part of an hour, you are still charged for the full hour.

Read Replicas run on the same Compute size as the primary database.

### Disk size[#](#disk-size)

Read [the Manage Disk Size usage guide](/docs/guides/platform/manage-your-usage/disk-size) for details on how we calculate charges. The disk size of a Read Replica is 1.25x the size of the primary disk to account for WAL archives. With a Read Replica you go beyond your subscription plan's quota for Disk Size.

### Provisioned Disk IOPS (optional)[#](#provisioned-disk-iops-optional)

Read Replicas inherit any additional provisioned Disk IOPS from the primary database. Read the [Manage Disk IOPS usage guide](/docs/guides/platform/manage-your-usage/disk-iops) for details on how we calculate charges.

### Provisioned Disk Throughput (optional)[#](#provisioned-disk-throughput-optional)

Read Replicas inherit any additional provisioned Disk Throughput from the primary database. Read the [Manage Disk Throughput usage guide](/docs/guides/platform/manage-your-usage/disk-throughput) for details on how we calculate charges.

### IPv4 (optional)[#](#ipv4-optional)

If the primary database has configured an IPv4 address add-on, its Read Replicas are also assigned one, with charges for each. Read the [Manage IPv4 usage guide](/docs/guides/platform/manage-your-usage/ipv4) for details on how we calculate charges.

### Usage on your invoice[#](#usage-on-your-invoice)

Compute incurred by Read Replicas is shown as "Replica Compute Hours" on your invoice. Disk Size, Disk IOPS, Disk Throughput and IPv4 are not shown separately for Read Replicas and are rolled up into the project.

## Billing examples[#](#billing-examples)

### No additional resources configured[#](#no-additional-resources-configured)

The project has one Read Replica, no IPv4, and no additional Disk IOPS and Disk Throughput configured.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Small Project 1

744 hours

$15

Disk Size Project 1

8 GB

$0

Compute Hours Small Replica

744 hours

$15

Disk Size Replica

10 GB

$1.25

**Subtotal**

**$56.25**

Compute Credits

\-$10

**Total**

**$46.25**

### Additional resources configured[#](#additional-resources-configured)

The project has two Read Replicas, IPv4, and additional Disk IOPS and Disk Throughput configured.

Line Item

Units

Costs

Pro Plan

1

$25

Compute Hours Large Project 1

744 hours

$110

Disk Size Project 1

8 GB

$0

Disk IOPS Project 1

3600

$14.40

Disk Throughput Project 1

200 MB/s

$7.13

IPv4 Hours Project 1

744 hours

$4

Compute Hours Large Replica 1

744 hours

$110

Disk Size Replica 1

10 GB

$1.25

Disk IOPS Replica 1

3600

$14.40

Disk Throughput Replica 1

200 MB/s

$7.13

IPv4 Hours Replica 1

744 hours

$4

Compute Hours Large Replica 2

744 hours

$110

Disk Size Replica 2

10 GB

$1.25

Disk IOPS Replica 2

3600

$14.40

Disk Throughput Replica 2

200 MB/s

$7.13

IPv4 Hours Replica 2

744 hours

$4

**Subtotal**

**$434.09**

Compute Credits

\-$10

**Total**

**$424.09**

## FAQ[#](#faq)

### Do Compute Credits apply to Read Replica Compute?[#](#do-compute-credits-apply-to-read-replica-compute)

No, Compute Credits do not apply to Read Replica Compute.
