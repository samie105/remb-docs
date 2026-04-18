---
title: "Metrics API"
source: "https://supabase.com/docs/guides/telemetry/metrics"
canonical_url: "https://supabase.com/docs/guides/telemetry/metrics"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:12.528Z"
content_hash: "777413b87ff919e79362ae5092414e2ca6e3cba2fcf95a719c3661c7472f95cb"
menu_path: ["Telemetry","Telemetry","More","More","More","Metrics","Metrics","Overview","Overview"]
section_path: ["Telemetry","Telemetry","More","More","More","Metrics","Metrics","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/telemetry/advanced-log-filtering/index.md", "title": "Advanced Log Filtering"}
nav_next: {"path": "supabase/docs/guides/telemetry/logs/index.md", "title": "Logging"}
---

# 

Metrics API

* * *

Every Supabase project exposes a [Prometheus](https://prometheus.io/)\-compatible **Metrics API** endpoint that surfaces ~200 Postgres performance and health series. You can scrape it into any observability stack to power custom dashboards, alerting rules, or long-term retention that goes beyond what Supabase Studio provides out of the box.

The Metrics API is currently in beta. Metric names and labels might evolve as we expand the dataset, and the feature is not available in self-hosted Supabase instances.

## What you can do with the Metrics API[#](#what-you-can-do-with-the-metrics-api)

*   Stream database CPU, IO, WAL, connection, and query stats into Prometheus-compatible systems.
*   Combine Supabase metrics with application signals in Grafana, Datadog, or any other observability vendor.
*   Reuse our [supabase-grafana dashboard JSON](https://github.com/supabase/supabase-grafana) to bootstrap over 200 ready-made charts.
*   Build your own alerting policies (right-sizing, saturation detection, index regression, and more).

## Choose your monitoring stack[#](#choose-your-monitoring-stack)

Pick the workflow that best matches your tooling. Cards link to Supabase-authored guides or vendor integration docs, and some include a “Community” pill when there’s an accompanying vendor reference.

[

Grafana Cloud (SaaS)

Use Grafana Cloud’s managed Prometheus (works on Free + Pro tiers) and import the Supabase dashboard without running any infrastructure.

Supabase guideCommunity

](/docs/guides/telemetry/metrics/grafana-cloud)[

Grafana + self-hosted Prometheus

Run Prometheus yourself following the official installation guidance and pair it with Grafana plus our dashboard JSON and alert pack.

Supabase guide

](/docs/guides/telemetry/metrics/grafana-self-hosted)[

Datadog

Scrape the Metrics API with the Datadog Agent or Prometheus remote write and monitor Supabase alongside your app telemetry.

Community

](https://docs.datadoghq.com/integrations/supabase/)[

Vendor-agnostic / BYO Prometheus

Connect AWS AMP, Grafana Mimir, VictoriaMetrics, or any Prometheus-compatible SaaS with the same scrape job pattern.

Supabase guide

](/docs/guides/telemetry/metrics/vendor-agnostic)

![Supabase Grafana dashboard showcasing database metrics](/docs/img/guides/platform/supabase-grafana-prometheus.png)

## Additional resources[#](#additional-resources)

*   [Supabase Grafana repository](https://github.com/supabase/supabase-grafana) for dashboard JSON and alert examples.
*   [Grafana Cloud’s Supabase integration doc](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-supabase/) (community-maintained, built on this Metrics API).
*   [Datadog’s Supabase integration doc](https://docs.datadoghq.com/integrations/supabase/) (community-maintained, built on this Metrics API).
*   [Log Drains](/docs/guides/telemetry/log-drains) for exporting event-based telemetry alongside metrics.
*   [Query Performance report](/dashboard/project/_/observability/query-performance) for built-in visualizations based on the same underlying metrics.


