---
title: "RedisInsight v2.30.0, July 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.30.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.30.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:06.996Z"
content_hash: "91fc0ee4bee4b5bc7086dc38827dacb178ee355dffd75b58972706fad363179f"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.30.0, July 2023","→","RedisInsight v2.30.0, July 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.30.0, July 2023","→","RedisInsight v2.30.0, July 2023"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.26.0/index.md", "title": "RedisInsight v2.26.0, May 2023"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.32.0/index.md", "title": "RedisInsight v2.32.0, August 2023"}
---

# RedisInsight v2.30.0, July 2023

RedisInsight v2.30

## 2.30 (July 2023)

This is the General Availability (GA) release of RedisInsight 2.30.

### Highlights

Introducing support for [triggers and functions](https://github.com/RedisGears/RedisGears/) that bring application logic closer to your data and give Redis powerful features for event-driven data processing

### Details

**Features and improvements**

[#2247](https://github.com/RedisInsight/RedisInsight/pull/2247), [#2249](https://github.com/RedisInsight/RedisInsight/pull/2249), [#2273](https://github.com/RedisInsight/RedisInsight/pull/2273), [#2279](https://github.com/RedisInsight/RedisInsight/pull/2279) Support for [triggers and functions](https://github.com/RedisGears/RedisGears/) that add the capability to execute server-side functions triggered by events or data operations to:

*   Speed up applications by running the application logic where the data lives
*   Eliminate the need to maintain the same code across different applications by moving application functionality inside the Redis database
*   Maintain consistent data when applications react to any keyspace change
*   Improve code resiliency by backing up and replicating triggers and functions along with the database

Triggers and functions work with a JavaScript engine, which lets you take advantage of JavaScript’s vast ecosystem of libraries and frameworks and modern, expressive syntax.

## On this page
