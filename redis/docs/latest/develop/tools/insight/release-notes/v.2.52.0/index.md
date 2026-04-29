---
title: "Redis Insight v2.52.0, June 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.52.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.52.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:46.077Z"
content_hash: "053a74317a4bc5c74464989c28dbd344fe1ea0bd2104db44d649036439b1a265"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.52.0, June 2024","→","Redis Insight v2.52.0, June 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.52.0, June 2024","→","Redis Insight v2.52.0, June 2024"]
nav_prev: {"path": "../v.2.50.0/index.md", "title": "Redis Insight v2.50.0, May 2024"}
nav_next: {"path": "../v.2.54.0/index.md", "title": "Redis Insight v2.54.0, August 2024"}
---

# Redis Insight v2.52.0, June 2024

Redis Insight v2.52

## 2.52 (June 2024)

This is the General Availability (GA) release of Redis Insight 2.52.

### Highlights

*   Redis Insight now supports [setting expiration for individual hash fields](https://redis.io/docs/latest/develop/data-types/hashes/?utm_source=redisinsight&utm_medium=release_notes&utm_campaign=2.52#field-expiration), a highly requested feature available in the [first release candidate of Redis 7.4](https://github.com/redis-stack/redis-stack/releases/tag/v7.4.0-rc1)
*   Learn how to leverage Redis for Retrieval Augmented Generation (RAG) use cases via a new built-in Redis Insight tutorial

### Details

**Features and improvements**

*   [#3470](https://github.com/RedisInsight/RedisInsight/pull/3470) Redis Insight now supports [setting expiration for individual hash fields](https://redis.io/docs/latest/develop/data-types/hashes/?utm_source=redisinsight&utm_medium=release_notes&utm_campaign=2.52#field-expiration) through intuitive Browser controls. The hash field expiration is a highly requested feature available in the [first release candidate of Redis 7.4](https://github.com/redis-stack/redis-stack/releases/tag/v7.4.0-rc1).
*   [#60](https://github.com/RedisInsight/Tutorials/pull/60) Redis, with its high performance and versatile data structures, is an excellent choice for implementing Retrieval Augmented Generation (RAG). Our new built-in tutorial provides an overview of how Redis can be leveraged in a RAG use case. To get started, open the "Insights" panel in the top right corner and try the new tutorial.
*   [#3447](https://github.com/RedisInsight/RedisInsight/pull/3447), [#3483](https://github.com/RedisInsight/RedisInsight/pull/3483) UX optimizations for displaying the values of keys in the Browser. The new layout includes controls for editing key values that appear only when you hover over them, optimizing the use of space and providing a cleaner interface.
*   [#3231](https://github.com/RedisInsight/RedisInsight/pull/3231) Support for applying the JSON formatting in Browser for values of keys with float numbers that contain 10 or more decimal places.
*   [#3492](https://github.com/RedisInsight/RedisInsight/pull/3492) Increased the slot refresh timeout to 5000 milliseconds to enhance connection stability for clustered databases. This adjustment helps avoid scenarios where a connection is terminated before the acknowledgment of a successful connection establishment is received.

**Bugs**

*   [#3490](https://github.com/RedisInsight/RedisInsight/pull/3490) Fix for an issue related to adding a JSON field to a key that already contains many fields.

## On this page
