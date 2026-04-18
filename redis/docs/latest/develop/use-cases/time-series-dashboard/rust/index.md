---
title: "Rolling sensor graph demo with Rust"
source: "https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/rust/"
canonical_url: "https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/rust/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:19.960Z"
content_hash: "c8f07442a147204315ef07046e1a5b3d3491a4987ff84020e662c3ec701912aa"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Rolling sensor graph demo with Redis","→","Rolling sensor graph demo with Redis","→\n      \n        Rolling sensor graph demo with Rust","→","Rolling sensor graph demo with Rust"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Rolling sensor graph demo with Redis","→","Rolling sensor graph demo with Redis","→\n      \n        Rolling sensor graph demo with Rust","→","Rolling sensor graph demo with Rust"]
nav_prev: {"path": "redis/docs/latest/integrate/redis-data-integration/installation/reqsummary/index.md", "title": "Requirements summary"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-from-source/index.md", "title": "Install Redis from Source"}
---

# Rolling sensor graph demo with Rust

Build a Redis-backed rolling sensor graph demo in Rust with redis-rs

This guide shows you how to build a compact rolling sensor graph demo in Rust with [`redis-rs`](/docs/latest/develop/clients/rust/) and Redis time series support. The example simulates three power sensors, ingests readings into Redis, and serves a local browser dashboard that updates in real time.

## Overview

Time series are a natural fit for telemetry, monitoring, and IoT-style workloads. In this example, Redis stores a stream of timestamped readings from three simulated power sensors.

The demo is designed to make a few ideas easy to see:

*   Raw readings arrive every 500ms
*   Each graph shows only the most recent 12 seconds
*   Older samples disappear because the time series retention is short
*   3-second buckets summarize the same readings with minimum, maximum, and average values
*   The bucket summaries are drawn under the same moving time scale as the graph

## How it works

The example has three main parts:

1.  A `SensorSimulator` generates realistic-looking power readings with drift and occasional spikes
2.  A `RedisTimeSeriesStore` creates the time series keys and issues Redis TimeSeries queries through `redis::cmd(...)`
3.  A small local HTTP server built with `axum` renders three stacked combined graph-and-bucket views and polls a JSON snapshot endpoint

Each sensor is stored in its own time series with labels such as `sensor_type`, `sensor_id`, `zone`, and `unit`. The dashboard uses [`TS.MADD`](/docs/latest/commands/ts.madd/) to ingest new readings and [`TS.RANGE`](/docs/latest/commands/ts.range/) to query both raw samples and aggregated bucket summaries. The aggregate queries use aligned buckets so the bucket boundaries stay stable as the visible window moves.

## The Rust files

The implementation is split across three files:

*   [`sensor_simulator.rs`](sensor_simulator.rs) - Sensor definitions and sample generation
*   [`timeseries_store.rs`](timeseries_store.rs) - Redis TimeSeries command helpers
*   [`demo_server.rs`](demo_server.rs) - Local HTTP server and inline dashboard UI

The Redis helper issues time series commands with `redis::cmd(...)`, which keeps the example small while still making the Redis command flow explicit.

## Data model

Series keys use this pattern:

```text
ts:sensor:power_consumption:{sensor_id}
```

For example:

```text
ts:sensor:power_consumption:power-1
ts:sensor:power_consumption:power-2
ts:sensor:power_consumption:power-3
```

Each time series has labels similar to:

```text
site = demo
sensor_type = power_consumption
sensor_id = power-1
zone = north
unit = watts
```

The demo uses a 12-second retention period so the graphs visibly slide forward as old samples expire. The setup is also idempotent, so you can stop and restart the demo without first cleaning up the time series keys.

## Redis commands used

The implementation uses these time series commands directly through `redis-rs`:

*   [`TS.CREATE`](/docs/latest/commands/ts.create/) - Create one time series per sensor with retention and labels
*   [`TS.MADD`](/docs/latest/commands/ts.madd/) - Batch-ingest readings from all three sensors every 500ms
*   [`TS.GET`](/docs/latest/commands/ts.get/) - Fetch the latest reading for a sensor
*   [`TS.RANGE`](/docs/latest/commands/ts.range/) - Read raw recent samples and aggregated 3-second buckets
*   `ALIGN 0` with `TS.RANGE ... AGGREGATION` - Keep bucket boundaries stable as the visible window moves

## Prerequisites

Before running the demo, make sure that:

*   Redis is running and accessible. By default, the demo connects to `localhost:6379`.
*   Your Redis deployment includes time series support.
*   The required Rust crates are available:

```bash
cargo build
```

## Running the demo

Build and run the demo:

```bash
cargo run --bin demo_server
```

The server accepts optional flags if your Redis instance is not on the default host and port:

```bash
cargo run --bin demo_server -- --redis-host 127.0.0.1 --redis-port 6379 --port 8080
```

You can also override the full Redis URL with `REDIS_URL`.

After starting the server, visit `http://localhost:8080`.

The dashboard polls a JSON snapshot endpoint several times per second to show:

*   Three stacked rolling graphs of raw sensor readings
*   A bucket summary strip aligned to the same time axis as each graph
*   Minimum, maximum, and average values for each visible bucket
*   A moving 12-second window where old samples disappear as retention expires them

Because the graph and the bucket summary share the same moving time scale, you can see how raw samples relate to their aggregate bucket without switching views or interpreting a separate table.

## What to look for

As you watch the dashboard, pay attention to how the Redis query patterns map to the UI:

*   New points arrive every 500ms through `TS.MADD`
*   The graphs show raw values returned by `TS.RANGE`
*   The bucket summaries use `TS.RANGE ... ALIGN 0 AGGREGATION min|max|avg 3000`
*   The left edge of the graph keeps advancing because the time series retention is short
*   The bucket boundaries stay fixed even while the visible window moves
*   The dashboard remains safe to rerun because series creation is idempotent

## Why this shape works well

This demo intentionally uses only three sensors and a very short time horizon. That keeps the visualization small enough to understand at a glance while still demonstrating:

*   Repeated high-frequency ingest
*   Querying recent raw history
*   Aggregating into fixed time buckets
*   Short retention and visible expiration

For a first time series example, this is often easier to understand than a larger dashboard with many metrics, filters, or tables.

## Production considerations

This example intentionally keeps the server and UI small so the Redis behavior is easy to follow. In production, you would usually want to add:

*   Authentication and authorization
*   Separate static assets instead of inline HTML
*   Better error reporting and health checks
*   Deployment-specific retention, window sizes, and aggregation intervals
*   Stronger key namespacing if multiple applications share the same Redis deployment

## Learn more

*   [Rust client guide](/docs/latest/develop/clients/rust/) - Install and use the Rust client
*   [Time series overview](/docs/latest/develop/data-types/timeseries/) - Time series concepts and commands
*   [TS.RANGE command](/docs/latest/commands/ts.range/) - Query raw and aggregated ranges from a time series
*   [TS.MADD command](/docs/latest/commands/ts.madd/) - Add multiple samples in one call
*   [TS.CREATE command](/docs/latest/commands/ts.create/) - Create a time series with labels and retention

## On this page


