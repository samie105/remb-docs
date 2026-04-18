---
title: "Install"
source: "https://supabase.com/docs/guides/cron/install"
canonical_url: "https://supabase.com/docs/guides/cron/install"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:32.527Z"
content_hash: "c51707b0bebbc1b7ea5dd83ce0701fef719fc7a7ac1ea736cbafa4f3b2c25dd2"
menu_path: ["Cron","Cron","Getting Started","Getting Started","Install","Install"]
section_path: ["Cron","Cron","Getting Started","Getting Started","Install","Install"]
nav_prev: {"path": "supabase/docs/guides/auth/users/index.md", "title": "Users"}
nav_next: {"path": "supabase/docs/guides/cron/quickstart/index.md", "title": "Quickstart"}
---

# 

Install

* * *

Install the Supabase Cron Postgres Module to begin scheduling recurring Jobs.

1.  Go to the [Cron Postgres Module](/dashboard/project/_/integrations/cron/overview) under Integrations in the Dashboard.
2.  Enable the `pg_cron` extension.

## Uninstall[#](#uninstall)

Uninstall Supabase Cron by disabling the `pg_cron` extension:

```
1drop extension if exists pg_cron;
```

Disabling the `pg_cron` extension will permanently delete all Jobs.

