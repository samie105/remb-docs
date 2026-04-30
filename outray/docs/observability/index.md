---
title: "Observability"
source: "https://outray.dev/docs/observability"
canonical_url: "https://outray.dev/docs/observability"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:26:09.119Z"
content_hash: "a9024ac0e128ac643448a61d0cbbf6815077eec409a9b5d79fcaf71e83671bc0"
menu_path: ["Observability"]
section_path: []
nav_prev: {"path": "outray/docs/ci-cd/index.md", "title": "CI/CD Integration"}
nav_next: {"path": "outray/docs/vite-plugin/index.md", "title": "Vite Plugin"}
---

## Observability

Monitor your tunnel traffic and debug requests in real-time.

OutRay provides comprehensive observability tools to help you monitor your tunnels and debug issues with your local services.

When you open a tunnel, OutRay captures detailed information about every HTTP request that passes through it. You can view these logs in real-time on your dashboard.

The logs include:

-   **HTTP Method & Path**: See exactly what resource was requested.
-   **Status Code**: Quickly identify failed requests (4xx, 5xx).
-   **Duration**: Monitor the latency of your local service.
-   **Response Size**: Track data transfer usage.
-   **Client IP**: See where your traffic is coming from.

The dashboard provides an overview of your tunnel's performance over time:

-   **Total Requests**: Track the volume of traffic hitting your tunnels.
-   **Bandwidth Usage**: Monitor your data transfer consumption (both ingress and egress).
-   **Success Rate**: Visualize the ratio of successful vs. failed requests.

OutRay stores your request history so you can analyze past traffic patterns. The retention period depends on your subscription plan:

-   **Free Plan**: 3 days retention
-   **Ray Plan**: 14 days retention
-   **Beam Plan**: 30 days retention
-   **Pulse Plan**: 90 days retention
