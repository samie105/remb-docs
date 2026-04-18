---
title: "Platform Audit Logs"
source: "https://supabase.com/docs/guides/security/platform-audit-logs"
canonical_url: "https://supabase.com/docs/guides/security/platform-audit-logs"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:01.407Z"
content_hash: "1f471519fd7248daea522201184ebf75fc0d12040bff70cb1fc8f4f194ed174e"
menu_path: ["Security","Security","Product security","Product security","Platform Audit Logs","Platform Audit Logs"]
section_path: ["Security","Security","Product security","Product security","Platform Audit Logs","Platform Audit Logs"]
nav_prev: {"path": "supabase/docs/guides/realtime/subscribing-to-database-changes/index.md", "title": "Subscribing to Database Changes"}
nav_next: {"path": "supabase/docs/guides/security/platform-security/index.md", "title": "Secure configuration of Supabase platform"}
---

# 

Platform Audit Logs

* * *

Any [Platform API](/docs/reference/api/introduction) or [dashboard](/dashboard) actions performed by organization members are logged automatically for auditing and security purposes. This includes actions such as creating a new project, inviting members, modifying an edge function or changing project settings.

Besides Platform Audit Logs, Supabase Auth also provides [Auth Audit Logs](/docs/guides/auth/audit-logs) to monitor authentication-related activities within your projects.

Platform Audit Logs are only available on the [Team and Enterprise plans](/pricing).

## Accessing audit logs[#](#accessing-audit-logs)

Platform Audit Logs can be found under your [organization's audit logs](/dashboard/org/_/audit).

![Platform audit logs](/docs/img/guides/security/platform-audit-logs--light.png)

For each audit log, you can see additional details by clicking on the log entry:

*   Timestamp of action
*   Actor who performed the action
    *   IP address
    *   Email
    *   Token Type
*   Action performed
    *   Name
    *   Metadata such as route and response status
*   Action Target (Project, organization, Edge Function, ...)

## Limitations[#](#limitations)

*   There is currently no way to export the logs via dashboard
*   There is currently no way to set up a log drain of platform audit logs
*   Retention periods depend on your plan
