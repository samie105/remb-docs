---
title: "Rolling sensor graph demo with Redis"
source: "https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/"
canonical_url: "https://redis.io/docs/latest/develop/use-cases/time-series-dashboard/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:09.469Z"
content_hash: "4271f75c9d6e1b480cc84a129c26cdfab708275557f7e963d0c2b29acbe823e7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Rolling sensor graph demo with Redis","→","Rolling sensor graph demo with Redis"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Rolling sensor graph demo with Redis","→","Rolling sensor graph demo with Redis"]
nav_prev: {"path": "redis/docs/latest/develop/use-cases/session-store/rust/index.md", "title": "Redis session store with Rust"}
nav_next: {"path": "redis/docs/latest/develop/use-cases/time-series-dashboard/dotnet/index.md", "title": "Rolling sensor graph demo with Redis and .NET"}
---

# Rolling sensor graph demo with Redis

Build a rolling sensor graph demo with Redis time series data

This guide family shows how to build a compact rolling sensor graph demo backed by Redis time series.

## Overview

This use case simulates three sensors that continuously send readings to Redis. A small web dashboard then queries Redis to show:

*   A rolling graph of raw readings for each sensor
*   Bucket summaries drawn directly under the same time axis
*   Bucketed minimum, maximum, and average values
*   A short retention window where old samples visibly expire

This makes it a good fit for demonstrating how Redis time series support:

*   High-ingest telemetry workloads
*   Time-window queries
*   Aggregation over fixed buckets
*   Short retention periods that bound data size

## Available implementations

*   [redis-py](redis-py/index.md) - Build a local Python demo with three rolling sensor graphs, aligned bucket summaries, and visible sample expiration
*   [Node.js](nodejs/index.md) - Build the same rolling sensor graph demo with `node-redis` and a local Node.js server
*   [Java](java-jedis/index.md) - Build the same rolling sensor graph demo with Jedis and a local Java server
*   [Java (Lettuce)](java-lettuce/index.md) - Build the same rolling sensor graph demo with async and reactive Lettuce APIs
*   [Go](go/index.md) - Build the same rolling sensor graph demo with `go-redis` and a local Go server
*   [Rust](rust/index.md) - Build the same rolling sensor graph demo with `redis-rs` and a local Axum server
*   [.NET](dotnet/index.md) - Build the same rolling sensor graph demo with StackExchange.Redis and a local ASP.NET Core server
*   [PHP](php/index.md) - Build the same rolling sensor graph demo with Predis and PHP's built-in development server
*   [Ruby](ruby/index.md) - Build the same rolling sensor graph demo with `redis-rb` and a local WEBrick server

## On this page
