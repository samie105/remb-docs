---
title: "Redis Insight v2.54.0, August 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.54.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.54.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:46.126Z"
content_hash: "d8da6d12297ad643758dc9bb34b9533076fcba041f4e39dd0788b968ecd7c4ea"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.54.0, August 2024","→","Redis Insight v2.54.0, August 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.54.0, August 2024","→","Redis Insight v2.54.0, August 2024"]
---
# Redis Insight v2.54.0, August 2024

Redis Insight v2.54

## 2.54 (August 2024)

This is the General Availability (GA) release of Redis Insight 2.54.

### Highlights

Support for [Redis Data Integration (RDI)](https://redis.io/data-integration/?utm_source=redisinsight&utm_medium=repository&utm_campaign=release_notes) - a powerful tool designed to seamlessly synchronize data from your existing database to Redis in near real-time. RDI establishes a data streaming pipeline that mirrors data from your existing database to Redis Software, so if a record is added or updated, those changes automatically flow into Redis. This no-code solution enables seamless data integration and faster data access so you can build real-time apps at any scale. And now you can seamlessly create, validate, deploy, and monitor your data pipelines directly from Redis Insight.

### Details

**Features and improvements**

*   [#2839](https://github.com/RedisInsight/RedisInsight/pull/2839), [#2853](https://github.com/RedisInsight/RedisInsight/pull/2853), [#3101](https://github.com/RedisInsight/RedisInsight/pull/3101) Redis Insight now comes with the support for [Redis Data Integration (RDI)](https://redis.io/data-integration/?utm_source=redisinsight&utm_medium=repository&utm_campaign=release_notes) - a powerful tool designed to seamlessly synchronize data from your existing database to Redis in near real-time. RDI establishes a data streaming pipeline that mirrors data from your existing database to Redis Software, so if a record is added or updated, those changes automatically flow into Redis. This no-code solution enables seamless data integration and faster data access so you can build real-time apps at any scale. Use RDI version 1.2.7 or later to seamlessly create, validate, deploy, and monitor your data pipelines within Redis Insight. To get started, switch to the "Redis Data Integration" tab on the page with the list of Redis databases and add your RDI endpoint to Redis Insight.

**Bugs**

*   [#3577](https://github.com/RedisInsight/RedisInsight/pull/3577) Show [information about OSS cluster](https://github.com/RedisInsight/RedisInsight/issues/3157) when connected using TLS.
*   [#3575](https://github.com/RedisInsight/RedisInsight/pull/3575) Return [results instead of an empty list](https://github.com/RedisInsight/RedisInsight/issues/3465) for commands written in lowercase.
*   [#3613](https://github.com/RedisInsight/RedisInsight/pull/3613) Prevent repetitive buffer overflow by avoiding the resending of unfulfilled commands.

## On this page
