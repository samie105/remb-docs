---
title: "About billing on Supabase"
source: "https://supabase.com/docs/guides/platform/billing-on-supabase"
canonical_url: "https://supabase.com/docs/guides/platform/billing-on-supabase"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:04.344Z"
content_hash: "223aee1d026d9b6335a3d2065228639e62fd671831cf003ab84148351a22ecf9"
menu_path: ["Platform","Platform","Billing","Billing","About billing on Supabase","About billing on Supabase"]
section_path: ["Platform","Platform","Billing","Billing","About billing on Supabase","About billing on Supabase"]
nav_prev: {"path": "supabase/docs/guides/platform/billing-faq/index.md", "title": "Billing FAQ"}
nav_next: {"path": "supabase/docs/guides/platform/clone-project/index.md", "title": "Restore to a new project"}
---

# 

About billing on Supabase

* * *

## Subscription plans[#](#subscription-plans)

Supabase offers different subscription plans—Free, Pro, Team, and Enterprise. For a closer look at each plan's features and pricing, visit our [pricing page](/pricing).

### Free Plan[#](#free-plan)

The Free Plan helps you get started and explore the platform. You are granted two free projects. The project limit applies across all organizations where you are an Owner or Administrator. This means you could have two Free Plan organizations with one project each, or one Free Plan organization with two projects. Paused projects do not count towards your free project limit.

### Paid plans[#](#paid-plans)

Upgrading your organization to a paid plan provides additional features, and you receive a higher [usage quota](index.md#variable-usage-fees-and-quotas). You unlock the benefits of the paid plan for all projects within your organization - for example, no projects in your Pro Plan organization will be paused.

## Organization-based billing[#](#organization-based-billing)

Supabase bills separately for each organization. Each organization has its own subscription, including a unique subscription plan (Free, Pro, Team, or Enterprise), payment method, billing cycle, and invoices.

Different plans cannot be mixed within a single organization. For example, you cannot have both a Pro Plan project and a Free Plan project in the same organization. To have projects on different plans, you must create separate organizations. See [Project Transfers](../project-transfer/index.md) if you need to move a project to a different organization.

![Organization-based billing](/docs/img/guides/platform/billing-overview--light.png)

## Costs[#](#costs)

Monthly costs for paid plans include a fixed subscription fee based on your chosen plan and variable usage fees. To learn more about billing and cost management, refer to the following resources.

*   [Your monthly invoice](../your-monthly-invoice/index.md) - For a detailed breakdown of what a monthly invoice includes
*   [Manage your usage](../manage-your-usage/index.md) - For details on how the different usage items are billed, and how to optimize usage and reduce costs
*   [Control your costs](../cost-control/index.md) - For details on how you can control your costs in case unexpected high usage occurs

### Compute costs for projects[#](#compute-costs-for-projects)

An organization can have multiple projects. Each project includes a dedicated Postgres instance running on its own server. You are charged for the Compute resources of that server, independent of your database usage.

Each project you launch increases your monthly Compute costs.

Read more about [Compute costs](../manage-your-usage/compute/index.md).

## Variable Usage Fees and Quotas[#](#variable-usage-fees-and-quotas)

Each subscription plan includes a built-in quota for some selected usage items, such as [Egress](../manage-your-usage/egress/index.md), [Storage Size](../manage-your-usage/storage-size/index.md), or [Edge Function Invocations](../manage-your-usage/edge-function-invocations/index.md). This quota represents your free usage allowance. If you stay within it, you incur no extra charges for these items. Only usage beyond the quota is billed as overage.

For usage items without a quota, such as [Compute](../manage-your-usage/compute/index.md) or [Custom Domains](../manage-your-usage/custom-domains/index.md), you are charged for your entire usage.

The quota is applied to your entire organization, independent of how many projects you launch within that organization. For billing purposes, we sum the usage across all projects in a monthly invoice.

Usage Item

Free

Pro/Team

Enterprise

Egress

5 GB

250 GB included, then $0.09 per GB

Custom

Database Size

500 MB per project

8 GB disk per project included, then $0.125 per GB

Custom

Monthly Active Users

50,000 MAU

100,000 MAU included, then $0.00325 per MAU

Custom

Monthly Active Third-Party Users

50,000 MAU

100,000 MAU included, then $0.00325 per MAU

Custom

Monthly Active SSO Users

Unavailable on Free Plan

50 MAU included, then $0.015 per MAU

Custom

Storage Size

1 GB

100 GB included, then $0.021 per GB

Custom

Storage Images Transformed

Unavailable on Free Plan

100 included, then $5 per 1000

Custom

Edge Function Invocations

500,000

2 million included, then $2 per million

Custom

Realtime Message Count

2 million

5 million included, then $2.5 per million

Custom

Realtime Peak Connections

200

500 included, then $10 per 1000

Custom

You can find a detailed breakdown of all usage items and how they are billed on the [Manage your usage](../manage-your-usage/index.md) page.

## Project add-ons[#](#project-add-ons)

While your subscription plan applies to your entire organization and is charged only once, you can enhance individual projects by opting into various add-ons.

*   [Compute](../compute-and-disk/index.md#compute) to scale your database up to 64 cores and 256 GB RAM
*   [Read Replicas](../read-replicas/index.md) to scale read operations and provide resiliency
*   [Disk](../compute-and-disk/index.md#disk) to provision extra IOPS/throughput or use a high-performance SSD
*   [Log Drains](../../telemetry/log-drains/index.md) to sync Supabase logs to a logging system of your choice
*   [Custom Domains](../custom-domains/index.md) to provide a branded experience
*   [PITR](../backups/index.md#point-in-time-recovery) to roll back to any specific point in time, down to the minute
*   [IPv4](../ipv4-address/index.md) for a dedicated IPv4 address
*   [Advanced MFA](../../auth/auth-mfa/phone/index.md) to provide other options than TOTP
