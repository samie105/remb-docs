---
title: "Settings"
source: "https://supabase.com/docs/guides/realtime/settings"
canonical_url: "https://supabase.com/docs/guides/realtime/settings"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:49.910Z"
content_hash: "1ae72fe5633c80794a1132946583961c7878d557f3199523da2a80e68aab0605"
menu_path: ["Realtime","Realtime","Usage","Usage","Settings","Settings"]
section_path: ["Realtime","Realtime","Usage","Usage","Settings","Settings"]
nav_prev: {"path": "supabase/docs/guides/realtime/realtime-with-nextjs/index.md", "title": "Using Realtime with Next.js"}
nav_next: {"path": "supabase/docs/guides/realtime/reports/index.md", "title": "Realtime Reports"}
---

# 

Settings

## 

Realtime Settings that allow you to configure your Realtime usage.

* * *

## Settings[#](#settings)

All changes made in this screen will disconnect all your connected clients to ensure Realtime starts with the appropriate settings and all changes are stored in Supabase middleware.

![Usage page navigation bar](/docs/img/guides/platform/realtime/realtime-settings--light.png)

You can set the following settings using the Realtime Settings screen in your Dashboard:

*   Enable Realtime service: Determines if the Realtime service is enabled or disabled for your project.
*   Channel Restrictions: You can toggle this settings to set Realtime to allow public channels or set it to use only private channels with [Realtime Authorization](/docs/guides/realtime/authorization).
*   Database connection pool size: Determines the number of connections used for Realtime Authorization RLS checking
*   Max concurrent clients: Determines the maximum number of clients that can be connected
*   Max events per second: Determines the maximum number of events per second that can be sent
*   Max presence events per second: Determines the maximum number of presence events per second that can be sent
*   Max payload size in KB: Determines the maximum number of payload size in KB that can be sent
