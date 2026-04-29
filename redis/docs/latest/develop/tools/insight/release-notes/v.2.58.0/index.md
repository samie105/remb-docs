---
title: "Redis Insight v2.58.0, October 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.58.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.58.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:23.965Z"
content_hash: "d66288ecdda1abacca6cf25a53ddc635cfe44c9a3fa28656742d2e260f3f0a5f"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.58.0, October 2024","→","Redis Insight v2.58.0, October 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.58.0, October 2024","→","Redis Insight v2.58.0, October 2024"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.56.0/index.md", "title": "Redis Insight v2.56.0, September 2024"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.6.0/index.md", "title": "RedisInsight v2.6.0, July 2022"}
---

# Redis Insight v2.58.0, October 2024

Redis Insight v2.58

## 2.58 (October 2024)

This is the General Availability (GA) release of Redis Insight 2.58.

### Highlights

*   Added functionality to start, stop, and reset [Redis Data Integration](https://redis.io/data-integration/?utm_source=redisinsight&utm_medium=repository&utm_campaign=release_notes) pipelines directly in the app, simplifying management and enhancing control
*   Introduced support for subscribing to specific Pub/Sub channel - a [highly requested feature](https://github.com/RedisInsight/RedisInsight/issues/1671)
*   Ability to delete previously added CA and Client certificates to keep them updated

### Details

**Features and improvements**

*   [#3843](https://github.com/RedisInsight/RedisInsight/pull/3843) Redis Insight now supports starting, stopping, and resetting [Redis Data Integration](https://redis.io/data-integration/?utm_source=redisinsight&utm_medium=repository&utm_campaign=release_notes) (RDI) pipelines. Use RDI version 1.2.9 or later to seamlessly stop or resume processing new data. You can also reset an RDI pipeline to take a new snapshot of the data, process it, and continue tracking changes. To get started, navigate to the "Redis Data Integration" tab on the database list page and add or connect to your RDI endpoint.
*   [#3832](https://github.com/RedisInsight/RedisInsight/pull/3832) Added support for a [highly requested feature](https://github.com/RedisInsight/RedisInsight/issues/1671) to subscribe to specific Pub/Sub channels. On the Pub/Sub page, you can now subscribe to multiple channels or patterns by entering them as a space delimited list.
*   [#3796](https://github.com/RedisInsight/RedisInsight/pull/3796) Ability to delete previously added CA and Client certificates to keep them up-to-date.

**Bugs**

*   [#3840](https://github.com/RedisInsight/RedisInsight/pull/3840) [Saved](https://github.com/RedisInsight/RedisInsight/issues/3833) SNI and SSH connection information for newly added database connections.
*   [#3828](https://github.com/RedisInsight/RedisInsight/pull/3828) Fixed an issue to [display multiple hash fields](https://github.com/RedisInsight/RedisInsight/issues/3826) when expanding a hash value.

## On this page
