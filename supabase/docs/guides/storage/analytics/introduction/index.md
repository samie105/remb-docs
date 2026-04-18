---
title: "Analytics Buckets"
source: "https://supabase.com/docs/guides/storage/analytics/introduction"
canonical_url: "https://supabase.com/docs/guides/storage/analytics/introduction"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:01.715Z"
content_hash: "30e7692e8f6827fd5982ae176858163c13c90fe78f923b7f44ded9abb8b31653"
menu_path: ["Storage","Storage","Analytics Buckets","Analytics Buckets","Introduction","Introduction"]
section_path: ["Storage","Storage","Analytics Buckets","Analytics Buckets","Introduction","Introduction"]
nav_prev: {"path": "supabase/docs/guides/storage/analytics/creating-analytics-buckets/index.md", "title": "Creating Analytics Buckets"}
nav_next: {"path": "supabase/docs/guides/storage/analytics/limits/index.md", "title": "Analytics Buckets Limits"}
---

# 

Analytics Buckets

## 

Store large datasets for analytics and reporting.

* * *

##### This feature is in alpha

Expect rapid changes, limited features, and possible breaking updates. [share feedback](https://github.com/orgs/supabase/discussions/40116) as we refine the experience and expand access.

Analytics buckets enable analytical workflows on large-scale datasets while keeping your primary database optimized for transactional operations.

## Why Analytics buckets?[#](#why-analytics-buckets)

Postgres tables are purpose-built for transactional workloads with frequent inserts, updates, deletes, and low-latency queries. Analytical workloads have fundamentally different requirements:

*   Processing large volumes of historical data
*   Running complex queries and aggregations
*   Minimizing storage costs
*   Preventing analytical queries from impacting production traffic

Analytics buckets address these requirements using [Apache Iceberg](https://iceberg.apache.org/), an open-table format specifically designed for efficient management of large analytical datasets.

## Ideal use cases[#](#ideal-use-cases)

Analytics buckets are perfect for:

*   **Data warehousing and business intelligence** - Build scalable data warehouses for BI tools
*   **Historical data archiving** - Retain large volumes of historical data cost-effectively
*   **Periodically refreshed analytics** - Maintain near real-time analytical views
*   **Complex analytical queries** - Execute sophisticated aggregations and joins over large datasets

By separating transactional and analytical workloads, Supabase lets you build scalable analytics pipelines without compromising your primary Postgres performance.

