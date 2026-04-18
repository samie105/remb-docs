---
title: "Performance Tuning"
source: "https://supabase.com/docs/guides/platform/performance"
canonical_url: "https://supabase.com/docs/guides/platform/performance"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:57.452Z"
content_hash: "ef66f91e4575b472a898291a5ee24c18e4bea34fdf148119039633915b115418"
menu_path: ["Platform","Platform","Platform Configuration","Platform Configuration","Performance Tuning","Performance Tuning"]
section_path: ["Platform","Platform","Platform Configuration","Platform Configuration","Performance Tuning","Performance Tuning"]
nav_prev: {"path": "supabase/docs/guides/platform/network-restrictions/index.md", "title": "Network Restrictions"}
nav_next: {"path": "supabase/docs/guides/platform/project-transfer/index.md", "title": "Project Transfers"}
---

# 

Performance Tuning

* * *

The Supabase platform automatically optimizes your Postgres database to take advantage of the compute resources of the plan your project is on. However, these optimizations are based on assumptions about the type of workflow the project is being utilized for, and it is likely that better results can be obtained by tuning the database for your particular workflow.

## Examining query performance[#](#examining-query-performance)

Unoptimized queries are a major cause of poor database performance. To analyze the performance of your queries, see the [Debugging and monitoring guide](/docs/guides/database/inspect).

## Optimizing the number of connections[#](#optimizing-the-number-of-connections)

The default connection limits for Postgres and Supavisor is based on your compute size. See the default connection numbers in the [Compute Add-ons](/docs/guides/platform/compute-add-ons) section.

If the number of connections is insufficient, you will receive the following error upon connecting to the DB:

```
1$ psql -U postgres -h ...2FATAL: remaining connection slots are reserved for non-replication superuser connections
```

In such a scenario, you can consider:

*   [upgrading to a larger compute add-on](/dashboard/project/_/settings/compute-and-disk)
*   configuring your clients to use fewer connections
*   manually configuring the database for a higher number of connections

### Configuring clients to use fewer connections[#](#configuring-clients-to-use-fewer-connections)

You can use the [pg\_stat\_activity](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW) view to debug which clients are holding open connections on your DB. `pg_stat_activity` only exposes information on direct connections to the database. Information on the number of connections to Supavisor is available [via the metrics endpoint](../platform/metrics).

Depending on the clients involved, you might be able to configure them to work with fewer connections (e.g. by imposing a limit on the maximum number of connections they're allowed to use), or shift specific workloads to connect via [Supavisor](/docs/guides/database/connecting-to-postgres#connection-pooler) instead. Transient workflows, which can quickly scale up and down in response to traffic (e.g. serverless functions), can especially benefit from using a connection pooler rather than connecting to the DB directly.

### Allowing higher number of connections[#](#allowing-higher-number-of-connections)

You can configure Postgres connection limit among other parameters by using [Custom Postgres Config](/docs/guides/platform/custom-postgres-config#custom-postgres-config).

### Enterprise[#](#enterprise)

[Contact us](https://forms.supabase.com/enterprise) if you need help tuning your database for your specific workflow.


