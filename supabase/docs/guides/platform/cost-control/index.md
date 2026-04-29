---
title: "Control your costs"
source: "https://supabase.com/docs/guides/platform/cost-control"
canonical_url: "https://supabase.com/docs/guides/platform/cost-control"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:18.723Z"
content_hash: "55d2c25f23a13470fcef6bd198b7dc3796238977c04f552040246c005949de7b"
menu_path: ["Platform","Platform","Billing","Billing","Control your costs","Control your costs"]
section_path: ["Platform","Platform","Billing","Billing","Control your costs","Control your costs"]
nav_prev: {"path": "supabase/docs/guides/platform/compute-and-disk/index.md", "title": "Compute and Disk"}
nav_next: {"path": "supabase/docs/guides/platform/credits/index.md", "title": "Credits"}
---

# 

Control your costs

* * *

## Spend Cap[#](#spend-cap)

The Spend Cap determines whether your organization can exceed your subscription plan's quota for any usage item. Scenarios that could lead to high usage—and thus high costs—include system attacks or bugs in your software. The Spend Cap can protect you from these unexpected costs for certain usage items.

This feature is available only with the Pro Plan. However, you will not be charged while using the Free Plan.

### What happens when the Spend Cap is on?[#](#what-happens-when-the-spend-cap-is-on)

After exceeding the quota for a usage item, further usage of that item is disallowed until the next billing cycle. You don't get charged for over-usage but your services will be restricted according to our [Fair Use Policy](../billing-faq/index.md#fair-use-policy) if you consistently exceed the quota.

Note that only certain usage items are covered by the Spend Cap.

### What happens when the Spend Cap is off?[#](#what-happens-when-the-spend-cap-is-off)

Your projects will continue to operate after exceeding the quota for a usage item. Any additional usage will be charged based on the item's cost per unit, as outlined on the [pricing page](/pricing).

When the Spend Cap is off, we recommend monitoring your usage and costs on the [organization's usage page](/dashboard/org/_/usage).

### Usage items covered by the Spend Cap[#](#usage-items-covered-by-the-spend-cap)

*   [Disk Size](../manage-your-usage/disk-size/index.md)
*   [Egress](../manage-your-usage/egress/index.md)
*   [Edge Function Invocations](../manage-your-usage/edge-function-invocations/index.md)
*   [Monthly Active Users](../manage-your-usage/monthly-active-users/index.md)
*   [Monthly Active SSO Users](../manage-your-usage/monthly-active-users-sso/index.md)
*   [Monthly Active Third Party Users](/docs/guides/platform/manage-your-usage/monthly-active-users-third-party)
*   [Realtime Messages](../manage-your-usage/realtime-messages/index.md)
*   [Realtime Peak Connections](../manage-your-usage/realtime-peak-connections/index.md)
*   [Storage Image Transformations](/docs/guides/platform/manage-your-usage/storage-image-transformations)
*   [Storage Size](../manage-your-usage/storage-size/index.md)

### Usage items not covered by the Spend Cap[#](#usage-items-not-covered-by-the-spend-cap)

Usage items that are predictable and explicitly opted into by the user are excluded.

*   [Compute](../manage-your-usage/compute/index.md)
*   [Branching Compute](../manage-your-usage/branching/index.md)
*   [Read Replica Compute](../manage-your-usage/read-replicas/index.md)
*   [Custom Domain](../manage-your-usage/custom-domains/index.md)
*   Additionally provisioned [Disk IOPS](../manage-your-usage/disk-iops/index.md)
*   Additionally provisioned [Disk Throughput](../manage-your-usage/disk-throughput/index.md)
*   [IPv4 address](../manage-your-usage/ipv4/index.md)
*   [Log Drain Hours](../manage-your-usage/log-drains/index.md#log-drain-hours)
*   [Log Drain Events](../manage-your-usage/log-drains/index.md#log-drain-events)
*   [Multi-Factor Authentication Phone](../manage-your-usage/advanced-mfa-phone/index.md)
*   [Point-in-Time-Recovery](../manage-your-usage/point-in-time-recovery/index.md)

### What the Spend Cap is not[#](#what-the-spend-cap-is-not)

The Spend Cap doesn't allow for fine-grained cost control, such as setting budgets for specific usage item or receiving notifications when certain costs are reached. We plan to make cost control more flexible in the future.

### Configure the Spend Cap[#](#configure-the-spend-cap)

You can configure the Spend Cap when creating an organization on the Pro Plan or at any time in the Cost Control section of the [organization's billing page](/dashboard/org/_/billing).

## Keep track of your usage and costs[#](#keep-track-of-your-usage-and-costs)

You can monitor your usage on the [organization's usage page](/dashboard/org/_/usage). The Upcoming Invoice section of the [organization's billing page](/dashboard/org/_/billing) shows your current spending and provides an estimate of your total costs for the billing cycle based on your usage.
