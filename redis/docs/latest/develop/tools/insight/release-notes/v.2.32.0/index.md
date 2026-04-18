---
title: "RedisInsight v2.32.0, August 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.32.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.32.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:58.815Z"
content_hash: "9442e9e2ccf0eed9a00541be235610bc1f69790b8d86a47fe7c82a902767c6a4"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.32.0, August 2023","→","RedisInsight v2.32.0, August 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.32.0, August 2023","→","RedisInsight v2.32.0, August 2023"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.30.0/index.md", "title": "RedisInsight v2.30.0, July 2023"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.34.0/index.md", "title": "RedisInsight v2.34.0, September 2023"}
---

# RedisInsight v2.32.0, August 2023

RedisInsight v2.32

## 2.32 (August 2023)

This is the General Availability (GA) release of RedisInsight 2.32.

### Highlights

*   Easily provision a free database to use with the RedisInsight interactive tutorials to learn, among others, how to leverage Vector Similarity Search for your AI use cases or discover the power of the native JSON data structure supporting structured querying and full-text search. Take advantage of the in-app social sign-up to [Redis Cloud](https://redis.com/comparisons/oss-vs-enterprise/?utm_source=redisinsight&utm_medium=rel_notes&utm_campaign=2_32) to quickly provision a free database with [Redis Stack’s capabilities](https://redis.io/docs/about/about-stack/?utm_source=redisinsight&utm_medium=rel_notes&utm_campaign=2_32). Try the [latest 7.2](https://redis.com/blog/introducing-redis-7-2/?utm_source=redisinsight&utm_medium=rel_notes&utm_campaign=2_32) release which delivers the new [Triggers and Functions](https://redis.com/blog/introducing-triggers-and-functions/?utm_source=redisinsight&utm_medium=rel_notes&utm_campaign=2_32) feature, allowing you to execute server-side functions written in JavaScript that are either triggered by a keyspace change, by a stream entry arrival, or by explicitly calling them, empowering developers to build and maintain real-time applications by moving business logic closer to the data, ensuring a lower latency whilst delivering the best developer experience.
*   Select a custom installation directory on Windows OS for when multi-user access to the app is required.

### Details

**Features and improvements**

*   [#2270](https://github.com/RedisInsight/RedisInsight/pull/2270), [#2271](https://github.com/RedisInsight/RedisInsight/pull/2271), [#2437](https://github.com/RedisInsight/RedisInsight/pull/2437) Added the ability to quickly provision a free [Redis Cloud](https://redis.com/comparisons/oss-vs-enterprise/?utm_source=redisinsight&utm_medium=rel_notes&utm_campaign=2_32) database via in-app social signup (Google or GitHub). Use the database with the RedisInsight interactive tutorials or try the [latest 7.2](https://redis.com/blog/introducing-redis-7-2/?utm_source=redisinsight&utm_medium=rel_notes&utm_campaign=2_32) release which delivers the new [Triggers and Functions](https://redis.com/blog/introducing-triggers-and-functions/?utm_source=redisinsight&utm_medium=rel_notes&utm_campaign=2_32) feature. To quickly create and automatically add a free Redis Cloud database to RedisInsight, click the "Try Redis Cloud" banner in the list of database connections page and follow the steps.
*   [#2455](https://github.com/RedisInsight/RedisInsight/pull/2455) Select a custom installation directory on Windows OS
*   [#2373](https://github.com/RedisInsight/RedisInsight/pull/2373), [#2387](https://github.com/RedisInsight/RedisInsight/pull/2387) Delete all command results in Workbench at once
*   [#2458](https://github.com/RedisInsight/RedisInsight/pull/2458) Added in-app hints in Browser and Workbench to get started with RedisInsight interactive tutorials
*   [#2422](https://github.com/RedisInsight/RedisInsight/pull/2422) Ignore the empty lines in files when uploading data in bulk
*   [#2470](https://github.com/RedisInsight/RedisInsight/pull/2470) Preset the header containing the engine, the API version and the library name in the JavaScript file when creating a new library within the [Triggers and Functions](https://redis.com/blog/introducing-triggers-and-functions/?utm_source=redisinsight&utm_medium=main&utm_campaign=main) tool

## On this page
