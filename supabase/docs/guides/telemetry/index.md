---
title: "Telemetry"
source: "https://supabase.com/docs/guides/telemetry"
canonical_url: "https://supabase.com/docs/guides/telemetry"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:50.068Z"
content_hash: "fd6bf1e913588346bde6e664cef1b7b234788c9726a3e31751c1a50beb2fa16e"
menu_path: ["Telemetry","Telemetry","Overview","Overview"]
section_path: ["Telemetry","Telemetry","Overview","Overview"]
nav_prev: {"path": "../storage/security/ownership/index.md", "title": "Ownership"}
nav_next: {"path": "advanced-log-filtering/index.md", "title": "Advanced Log Filtering"}
---

# 

Telemetry

* * *

Telemetry helps you understand what’s happening inside your app by collecting logs, metrics, and traces.

*   **Logs** capture individual events, such as errors or warnings, providing details about what happened at a specific moment.
*   **Metrics** track numerical data over time, like request latency or database query performance, helping you spot trends.
*   **Traces** show the flow of a request through different services, helping you debug slow or failing operations.

Supabase is working towards full support for the [OpenTelemetry](https://opentelemetry.io/) standard, making it easier to integrate with observability tools.

This section provides guidance on telemetry in Supabase, including how to work with Supabase Logs.
