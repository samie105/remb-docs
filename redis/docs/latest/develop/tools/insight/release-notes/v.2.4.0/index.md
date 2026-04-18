---
title: "RedisInsight v2.4.0, June 2022"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.4.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.4.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:13:31.558Z"
content_hash: "6eb863d223939eb3b3ce7bcda0bc2e30cc0aa50f7f1f40c2079e1071b80ec814"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.4.0, June 2022","→","RedisInsight v2.4.0, June 2022"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.4.0, June 2022","→","RedisInsight v2.4.0, June 2022"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/vectors/index.md", "title": "Vector search concepts"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/administration/index.md", "title": "Administration"}
---

# RedisInsight v2.4.0, June 2022

RedisInsight v2.4.0

## 2.4.0 (June 2022)

This is the General Availability (GA) release of RedisInsight 2.4.0

### Headlines:

*   Pub/Sub: Added support for [Redis pub/sub](https://redis.io/docs/manual/pubsub/) enabling subscription to channels and posting messages to channels.
*   Consumer groups: Added support for [streams consumer groups](https://redis.io/docs/manual/data-types/streams/#consumer-groups) enabling provision of different subsets of messages from the same stream to many clients for inspection and processing.
*   Database search: Search the list of databases added to RedisInsight to quickly find the required database.

### Details

**Features and improvements:**

*   [#760](https://github.com/RedisInsight/RedisInsight/pull/760), [#737](https://github.com/RedisInsight/RedisInsight/pull/737), [#773](https://github.com/RedisInsight/RedisInsight/pull/773) Added support for [Redis pub/sub](https://redis.io/docs/manual/pubsub/) enabling subscription to channels and posting messages to channels. Currently does not support sharded channels.
*   [#717](https://github.com/RedisInsight/RedisInsight/pull/717), [#683](https://github.com/RedisInsight/RedisInsight/pull/683), [#684](https://github.com/RedisInsight/RedisInsight/pull/684), [#688](https://github.com/RedisInsight/RedisInsight/pull/688), [#720](https://github.com/RedisInsight/RedisInsight/pull/720), Added support for [streams consumer groups](https://redis.io/docs/manual/data-types/streams/#consumer-groups) to manage different groups and consumers for the same stream, explicit acknowledgment of processed items, ability to inspect the pending items, claiming of unprocessed messages, and coherent history visibility for each single client.
*   [#754](https://github.com/RedisInsight/RedisInsight/pull/754) New **All Relationship** toggle for RedisGraph visualizations in **Workbench**. Enable it to see all relationships between your nodes.
*   [#788](https://github.com/RedisInsight/RedisInsight/pull/788) Quickly search the list of databases added to RedisInsight per database alias, host:port, or the last connection to find the database needed.
*   [#788](https://github.com/RedisInsight/RedisInsight/pull/788) Overview displays the number of keys per the logical database connected if this number is not equal to the total number in the database.

**Bugs Fixed:**

*   [#774](https://github.com/RedisInsight/RedisInsight/pull/774) Fixed cases when not all parameters are received in Overview.
*   [#810](https://github.com/RedisInsight/RedisInsight/pull/810) Display several streams values with the same timestamp.

## On this page

