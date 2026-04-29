---
title: "RedisInsight v2.12.0, October 2022"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v2.12.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v2.12.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:41.909Z"
content_hash: "25b7edb1998f38aa3e8f6e29226e24fbf0564fc5fe8dda51c93fa8de9c5cb9cd"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.12.0, October 2022","→","RedisInsight v2.12.0, October 2022"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.12.0, October 2022","→","RedisInsight v2.12.0, October 2022"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v2.10.0/index.md", "title": "RedisInsight v2.10.0, September 2022"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v2.2.0/index.md", "title": "RedisInsight v2.2.0, May 2022"}
---

# RedisInsight v2.12.0, October 2022

RedisInsight v2.12.0

## 2.12.0 (October 2022)

This is the General Availability (GA) release of RedisInsight 2.12.

### Highlights

*   Database Analysis: Get insights and optimize the usage and performance of your Redis or Redis Stack based on the overview of the memory and data type distribution, big or complicated keys, and namespaces used
*   Faster initial loading of the list of keys in Browser and Tree views
*   Performance optimizations for large results in Workbench

### Details

**Features and improvements**

*   [#1207](https://github.com/RedisInsight/RedisInsight/pull/1207), [#1222](https://github.com/RedisInsight/RedisInsight/pull/1222), [#1295](https://github.com/RedisInsight/RedisInsight/pull/1295), [#1159](https://github.com/RedisInsight/RedisInsight/pull/1159), [#1231](https://github.com/RedisInsight/RedisInsight/pull/1231), [#1155](https://github.com/RedisInsight/RedisInsight/pull/1155) Get insights and optimize the usage and performance of your Redis or Redis Stack with Database Analysis. Navigate to Analysis Tools and scan up to 10,000 keys in the database to see the summary of memory allocation and the number of keys per Redis data type, memory likely to be freed over time, top 15 key namespaces, and the biggest keys found. You can extrapolate results based on the total number of keys or see the exact results for the number of keys scanned.
*   [#1280](https://github.com/RedisInsight/RedisInsight/pull/1280) Speed up the initial load of the key list in Browser and Tree views
*   [#1285](https://github.com/RedisInsight/RedisInsight/pull/1285) Support for infinite floating point numbers in sorted sets
*   [#1290](https://github.com/RedisInsight/RedisInsight/pull/1290) Performance optimizations to process large results of Redis commands in Workbench

**Bugs**

*   [#1293](https://github.com/RedisInsight/RedisInsight/pull/1293) Fixed Workbench visualizations in Redis Stack

## On this page
