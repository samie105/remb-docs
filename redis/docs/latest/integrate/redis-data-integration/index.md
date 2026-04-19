---
title: "Redis Data Integration"
source: "https://redis.io/docs/latest/integrate/redis-data-integration/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-data-integration/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:15.326Z"
content_hash: "499bbd314f4c6f6b6d1b7de53b9d4cc9caed073faea5470e2dd22429b9936421"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis Data Integration","→","Redis Data Integration"]
nav_prev: {"path": "redis/docs/latest/integrate/redis-ai-libraries/index.md", "title": "Redis for AI"}
nav_next: {"path": "redis/docs/latest/integrate/redis-data-integration/data-pipelines/pipeline-config/index.md", "title": "Pipeline configuration file"}
---

# Redis Data Integration

This is the first General Availability version of Redis Data Integration (RDI).

RDI's purpose is to help Redis customers sync Redis Enterprise with live data from their slow disk based databases in order to:

*   Meet the required speed and scale of read queries and provide an excellent and predictable user experience.
*   Save resources and time when building pipelines and coding data transformations.
*   Reduce the total cost of ownership by saving money on expensive database read replicas.

If you use a relational database as the system of record for your app, you may eventually find that its performance doesn't scale well as your userbase grows. It may be acceptable for a few thousand users but for a few million, it can become a major problem. If you don't have the option of abandoning the relational database, you should consider using a fast database, such as Redis, to cache data from read queries. Since read queries are typically many times more common than writes, the cache will greatly improve performance and let your app scale without a major redesign.

RDI keeps a Redis cache up to date with changes in the primary database, using a [_Change Data Capture (CDC)_](https://en.wikipedia.org/wiki/Change_data_capture) mechanism. It also lets you _transform_ the data from relational tables into convenient and fast data structures that match your app's requirements. You specify the transformations using a configuration system, so no coding is necessary.

Note:

RDI is supported with Redis databases or [CRDB](https://redis.io/active-active/) (Active Active Replication) targets, and is also available on [Redis Cloud](/docs/latest/operate/rc/databases/rdi/).

## Features

RDI provides enterprise-grade streaming data pipelines with the following features:

*   **Near realtime pipeline** - The CDC system captures changes in very short time intervals, then ships and processes them in _micro-batches_ to provide near real time updates to Redis.
*   **At least once guarantee** - RDI will deliver any change to the selected data set at least once to the target Redis database.
*   **Data integrity** - RDI keeps the data change order per source table or unique key.
*   **High availability** - All stateless components have hot failover or quick automatic recovery. RDI state is always highly available using Redis Enterprise replication.
*   **Easy to install and operate** - Use a self-documenting command line interface (CLI) for all installation and day-two operations.
*   **No coding needed** - Create and test your pipelines using Redis Insight.
*   **Data-in-transit encryption** - RDI never persists data to disk. All data in-flight is protected using TLS or mTLS connections.
*   **Observability - Metrics** - RDI collects data processing counters at source table granularity along with data processing performance metrics. These are available via GUI, CLI and [Prometheus](https://prometheus.io/) endpoints.
*   **Observability - logs** - RDI saves rotating logs to a single folder. They are in a JSON format, so you can collect and process them with your favorite observability tool.
*   **Backpressure mechanism** - RDI is designed to backoff writing data when the cache gets disconnected, which prevents cascading failure. Since the change data is persisted in the source database and Redis is very fast, RDI can easily catch up with missed changes after a short period of disconnection. See [Backpressure mechanism](/docs/latest/integrate/redis-data-integration/architecture/#backpressure-mechanism) for more information.
*   **Recovering from full failure** - If the cache fails or gets disconnected for a long time, RDI can reconstruct the cache data in Redis using a full snapshot of the defined dataset.
*   **High throughput** - Because RDI uses Redis for staging and writes to Redis as a target, it has very high throughput. With a single processor core and records of about 1KB in size, RDI processes around 10,000 records per second. While taking the initial full _snapshot_ of the source database, RDI automatically scales to a configurable number of processing units, to fill the cache as fast as possible.

## When to use RDI

RDI is highly configurable but it is not intended to be a general solution for all data integration tasks. See [When to use RDI](/docs/latest/integrate/redis-data-integration/when-to-use/) to find out if your use case is a good fit for RDI's features.

## Supported source databases

RDI can capture data from any of the following sources:

Database

Versions

AWS RDS Versions

GCP SQL Versions

Oracle

19c, 21c, 23ai (LogMiner only)

19c, 21c

\-

MariaDB

10.5, 11.4.x, 11.7.x

10.4 to 10.11, 11.4.3

\-

MongoDB

6.0, 7.0, 8.0

\-

\-

MySQL

5.7, 8.0.x, 8.4.x, 9.0, 9.1

8.0.x

8.0

PostgreSQL

10, 11, 12, 13, 14, 15, 16, 17

11, 12, 13, 14, 15, 16

15

Supabase (uses PostgreSQL)

10, 11, 12, 13, 14, 15, 16, 17

\-

\-

SQL Server

2017, 2019, 2022

2016, 2017, 2019, 2022

2019

Spanner

\-

\-

All versions

AlloyDB for PostgreSQL

14.2, 15.7

\-

14.2, 15.7

AWS Aurora/PostgreSQL

15

15

\-

Neon

14, 15, 16, 17

\-

\-

## Continue learning with Redis University

*   [Redis Data Integration Lab](https://university.redis.io/course/2qa1u1ss21vsy5?tab=details)

## Documentation

Learn more about RDI from the other pages in this section:

## On this page
