---
title: "Permissions"
source: "https://supabase.com/docs/guides/platform/permissions"
canonical_url: "https://supabase.com/docs/guides/platform/permissions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:53.426Z"
content_hash: "85197f70dde21382b26f782e3296c1c9307387f9eacacbd7c536f1fc0c3717f5"
menu_path: ["Platform","Platform","Platform Configuration","Platform Configuration","Default Platform Permissions","Default Platform Permissions"]
section_path: ["Platform","Platform","Platform Configuration","Platform Configuration","Default Platform Permissions","Default Platform Permissions"]
nav_prev: {"path": "supabase/docs/guides/platform/performance/index.md", "title": "Performance Tuning"}
nav_next: {"path": "supabase/docs/guides/platform/privatelink/index.md", "title": "PrivateLink"}
---

# 

Permissions

* * *

The Supabase platform offers additional services (e.g. Storage) on top of the Postgres database that comes with each project. These services default to storing their operational data within your database, to ensure that you retain complete control over it.

However, these services assume a base level of access to their data, in order to e.g. be able to run migrations over it. Breaking these assumptions runs the risk of rendering these services inoperational for your project:

*   all entities under the `storage` schema are owned by `supabase_storage_admin`
*   all entities under the `auth` schema are owned by `supabase_auth_admin`

It is possible for violations of these assumptions to not cause an immediate outage, but take effect at a later time when a newer migration becomes available.
