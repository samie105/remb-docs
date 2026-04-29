---
title: "Enforce MFA on Organization"
source: "https://supabase.com/docs/guides/platform/mfa/org-mfa-enforcement"
canonical_url: "https://supabase.com/docs/guides/platform/mfa/org-mfa-enforcement"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:19.382Z"
content_hash: "edb5b2a57f6a298bb371b2c1c486f9fdd2e588529f89435311650b6cf1118cb5"
menu_path: ["Platform","Platform","More","More","More","Multi-factor Authentication","Multi-factor Authentication","Enforce MFA on organization","Enforce MFA on organization"]
section_path: ["Platform","Platform","More","More","More","Multi-factor Authentication","Multi-factor Authentication","Enforce MFA on organization","Enforce MFA on organization"]
nav_prev: {"path": "../../manage-your-usage/storage-size/index.md", "title": "Manage Storage size usage"}
nav_next: {"path": "../../migrating-to-supabase/index.md", "title": "Migrating to Supabase"}
---

# 

Enforce MFA on Organization

* * *

Supabase provides multi-factor authentication (MFA) enforcement on the organization level. With MFA enforcement, you can ensure that all organization members use MFA. Members cannot interact with your organization or your organization's projects without a valid MFA-backed session.

MFA enforcement is only available on the [Pro, Team and Enterprise plans](/pricing).

## Manage MFA enforcement[#](#manage-mfa-enforcement)

To enable MFA on an organization, visit the [security settings](/dashboard/org/_/security) page and toggle `Require MFA to access organization` on.

*   Only organization **owners** can modify this setting
*   The owner must have [MFA on their own account](/docs/guides/platform/multi-factor-authentication)
*   Supabase recommends creating two distinct MFA apps on your user account

When MFA enforcement is enabled, users without MFA will immediately lose access all resources in the organization. The users will still be members of the organization and will regain their original permissions once they enable MFA on their account.

## Personal access tokens[#](#personal-access-tokens)

Personal access tokens are not affected by MFA enforcement. Personal access tokens are designed for programmatic access and issuing of these require a valid Supabase session backed by MFA, if enabled on the account.
