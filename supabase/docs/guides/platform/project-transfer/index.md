---
title: "Project Transfers"
source: "https://supabase.com/docs/guides/platform/project-transfer"
canonical_url: "https://supabase.com/docs/guides/platform/project-transfer"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:01.685Z"
content_hash: "58983443d4be47c204504577b8a07f5e2c006e29b279fed11684d09f7dad2433"
menu_path: ["Platform","Platform","Project & Account Management","Project & Account Management","Transfer Project","Transfer Project"]
section_path: ["Platform","Platform","Project & Account Management","Project & Account Management","Transfer Project","Transfer Project"]
nav_prev: {"path": "../privatelink/index.md", "title": "PrivateLink"}
nav_next: {"path": "../read-replicas/index.md", "title": "Read Replicas"}
---

# 

Project Transfers

* * *

You can freely transfer projects between different organizations. Head to your [projects' general settings](/dashboard/project/_/settings/general) to initiate a project transfer.

![Project Transfer: General Settings](/docs/img/guides/platform/project-transfer-overview--light.png)

![Project Transfer: Confirmation Modal](/docs/img/guides/platform/project-transfer-modal--light.png)

Source organization - the organization the project currently belongs to Target organization - the organization you want to move the project to

## Pre-Requirements[#](#pre-requirements)

*   You need to be the owner of the source organization.
*   You need to be at least a member of the target organization you want to move the project to.
*   No active GitHub integration connection
*   No project-scoped roles pointing to the project (Team/Enterprise plan)
*   No log drains configured

## Usage-billing and project add-ons[#](#usage-billing-and-project-add-ons)

For usage metrics such as disk size, egress or image transformations and project add-ons such as [Compute Add-On](/docs/guides/platform/compute-add-ons), [Point-In-Time-Recovery](/docs/guides/platform/backups#point-in-time-recovery), [IPv4](/docs/guides/platform/ipv4-address), [Log Drains](/docs/guides/platform/log-drains), [Advanced MFA](/docs/guides/auth/auth-mfa/phone) or a [Custom Domain](/docs/guides/platform/custom-domains), the source organization will still be charged for the usage up until the transfer. The charges will be added to the invoice when the billing cycle resets.

The target organization will be charged at the end of the billing cycle for usage after the project transfer.

## Things to watch out for[#](#things-to-watch-out-for)

*   Transferring a project might come with a short 1-2 minute downtime if you're moving a project from a paid to a Free Plan.
*   You could lose access to certain project features depending on the plan of the target organization, i.e. moving a project from a Pro Plan to a Free Plan.
*   When moving your project to a Free Plan, we also ensure you’re not exceeding your two free project limit. In these cases, it is best to upgrade your target organization to Pro Plan first.
*   You could have less rights on the project depending on your role in the target organization, i.e. you were an Owner in the previous organization and only have a Read-Only role in the target organization.

## Transfer to a different region[#](#transfer-to-a-different-region)

Note that project transfers are only transferring your projects across an organization and cannot be used to transfer between different regions. To move your project to a different region, see [migrating your project](/docs/guides/platform/migrating-within-supabase).
