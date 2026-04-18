---
title: "Read Replicas"
source: "https://supabase.com/docs/guides/platform/read-replicas"
canonical_url: "https://supabase.com/docs/guides/platform/read-replicas"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:06.308Z"
content_hash: "86374aca24d3ba615a62d9da0b0443080217fb1d574e34ac7814a342249484b9"
menu_path: ["Platform","Platform","More","More","More","Read Replicas","Read Replicas","Overview","Overview"]
section_path: ["Platform","Platform","More","More","More","Read Replicas","Read Replicas","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/platform/privatelink/index.md", "title": "PrivateLink"}
nav_next: {"path": "supabase/docs/guides/platform/regions/index.md", "title": "Available regions"}
---

# 

Read Replicas

## 

Deploy read-only databases across multiple regions, for lower latency and better resource management.

* * *

Read Replicas are additional databases kept in sync with your Primary database. You can read your data from a Read Replica, which helps with:

*   **Load balancing:** Read Replicas reduce load on the Primary database. For example, you can use a Read Replica for complex analytical queries and reserve the Primary for user-facing create, update, and delete operations.
*   **Improved latency:** For projects with a global user base, additional databases can be deployed closer to users to reduce latency.
*   **Redundancy:** Read Replicas provide data redundancy.

![Map view of all project databases.](/docs/img/guides/platform/read-replicas/map-view.png?v=1)

## About Read Replicas[#](#about-read-replicas)

The database you start with when launching a Supabase project is your Primary database. A process called "replication" keeps Read Replicas in sync with the Primary. Replication is asynchronous to ensure that transactions on the Primary aren't blocked. There is a delay between an update on the Primary and the time that a Read Replica receives the change. This delay is called "replication lag."

You can only read data from a Read Replica. This is in contrast to a Primary database, where you can both read and write:

select

insert

update

delete

Primary

✅

✅

✅

✅

Read Replica

✅

\-

\-

\-

## Features[#](#features)

Read Replicas offer the following features:

### Dedicated endpoints[#](#dedicated-endpoints)

Each Read Replica has its own dedicated database and API endpoints.

*   Find the database endpoint on the project's [**Connect** panel](/dashboard/project/_?showConnect=true). Toggle between Primary and Read Replicas using the **Source** dropdown.
*   Find the API endpoint on the [API Settings page](/dashboard/project/_/settings/api) under **Project URL**. Toggle between Primary and Read Replicas using the **Source** dropdown.

If you use an [IPv4 add-on](/docs/guides/platform/ipv4-address#read-replicas), the database endpoints for your Read Replicas also use an IPv4 add-on.

Read Replicas only support `GET` requests from the [REST API](/docs/guides/api). If you are calling a read-only Postgres function through the REST API, make sure to set the `get: true` [option](/docs/reference/javascript/rpc?queryGroups=example&example=call-a-read-only-postgres-function).

Requests to other Supabase products, such as Auth, Storage, and Realtime, aren't able to use a Read Replica or its API endpoint. Support for more products will be added in the future.

### Dedicated connection pool[#](#dedicated-connection-pool)

A connection pool through Supavisor is also available for each Read Replica. Find the connection string on the [Database Settings page](/dashboard/project/_/database/settings) under **Connection String**.

### API load balancer[#](#api-load-balancer)

A load balancer automatically balances requests between your Primary database and Read Replicas. Find its endpoint on the [**API Settings page**](/dashboard/project/_/settings/api).

The load balancer enables geo-routing for Data API requests to automatically route `GET` requests to the database closest to your user ensuring the lowest latency. You can also send Non-`GET` requests through this endpoint, and they are routed to the Primary database automatically.

You can also interact with other Supabase services (Auth, Edge Functions, Realtime, and Storage) through this load balancer so there's no need to worry about which endpoint to use and in which situations. Geo-routing for Auth, Realtime, and Storage aren't yet available but are coming soon.

Due to the requirements of the Auth service, all Auth requests are handled by the Primary, even when sent over the load balancer endpoint. This is similar to how non-Read requests for the Data API (PostgREST) are exclusively handled by the Primary.

To call a read-only Postgres function on Read Replicas through the REST API, use the `get: true` [option](/docs/reference/javascript/rpc?queryGroups=example&example=call-a-read-only-postgres-function).

If you remove all Read Replicas from your project, the load balancer and its endpoint are removed as well. Make sure to redirect requests back to your Primary database before removal.

From April 4th, 2025, the routing behavior for eligible Data API requests changed:

*   **Old behavior**: Round-Robin distribution among all databases (all read replicas + primary) of your project, regardless of location
*   **New behavior**: Geo-routing, that directs requests to the closest available database (all read replicas + primary)

The new behavior delivers a better experience for your users by minimizing the latency to your project. You can take full advantage of this by placing Read Replicas close to your major customer bases.

If you use a [custom domain](/docs/guides/platform/custom-domains), requests will not be routed through the load balancer. You should instead use the dedicated endpoints provided in the dashboard.

### Querying through the SQL editor[#](#querying-through-the-sql-editor)

In the SQL editor, you can choose if you want to run the query on a particular Read Replica.

![SQL editor view.](/docs/img/guides/platform/read-replicas/sql-editor.png?v=1)

### Logging[#](#logging)

When a Read Replica is deployed, it emits logs from the following services:

*   [API](/dashboard/project/_/logs/edge-logs)
*   [Postgres](/dashboard/project/_/logs/postgres-logs)
*   [PostgREST](/dashboard/project/_/logs/postgrest-logs)
*   [Supavisor](/dashboard/project/_/logs/pooler-logs)

Views on [Log Explorer](/docs/guides/platform/logs) are automatically filtered by databases, with the logs of the Primary database displayed by default. Viewing logs from other databases can be toggled with the `Source` button found on the upper-right part section of the Logs Explorer page.

For API logs, logs can originate from the API Load Balancer as well. The upstream database or the one that eventually handles the request can be found under the `Redirect Identifier` field. This is equivalent to `metadata.load_balancer_redirect_identifier` when querying the underlying logs.

### Metrics[#](#metrics)

Observability and metrics for Read Replicas are available on the Supabase Dashboard. Resource utilization for a specific Read Replica can be viewed on the [Database Reports page](/dashboard/project/_/observability/database) by toggling for `Source`. Likewise, metrics on API requests going through either a Read Replica or Load Balancer API endpoint are also available on the dashboard through the [API Reports page](/dashboard/project/_/observability/api-overview)

We recommend ingesting your [project's metrics](/docs/guides/platform/metrics#accessing-the-metrics-endpoint) into your own environment. If you have an existing ingestion pipeline set up for your project, you can [update it](https://github.com/supabase/supabase-grafana?tab=readme-ov-file#read-replica-support) to additionally ingest metrics from your Read Replicas.

### Centralized configuration management[#](#centralized-configuration-management)

All settings configured through the dashboard will be propagated across all databases of a project. This ensures that no Read Replica get out of sync with the Primary database or with other Read Replicas.

## Pricing[#](#pricing)

For a detailed breakdown of how we calculate charges, read the [Manage Read Replica usage guide](/docs/guides/platform/manage-your-usage/read-replicas).


