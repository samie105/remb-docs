---
title: "RedisInsight v2.28.0, June 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v2.28.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v2.28.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:20.333Z"
content_hash: "c91108b87b0af422f73c441d7c50e91b12dd4018354e770d5824a2801cda7f36"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.28.0, June 2023","→","RedisInsight v2.28.0, June 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.28.0, June 2023","→","RedisInsight v2.28.0, June 2023"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v2.2.0/index.md", "title": "RedisInsight v2.2.0, May 2022"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v2.8.0/index.md", "title": "RedisInsight v2.8.0, August 2022"}
---

# RedisInsight v2.28.0, June 2023

RedisInsight v2.28

## 2.28 (June 2023)

This is the General Availability (GA) release of RedisInsight 2.28.

### Highlights

*   Quickly and conveniently add [Redis Cloud](https://redis.com/redis-enterprise-cloud/overview/) databases that belong to fixed subscriptions using the auto-discovery tool
*   UX optimizations in Browser for an improved experience when performing [full-text search and queries](https://redis.io/docs/stack/search/), filtering, and bulk actions.
*   Support for a monospaced font in [JSON](https://redis.io/docs/stack/json/) key types

### Details

**Features and improvements**

*   [#2198](https://github.com/RedisInsight/RedisInsight/pull/2198), [#2207](https://github.com/RedisInsight/RedisInsight/pull/2207) Automatically discover and add [Redis Cloud](https://redis.com/redis-enterprise-cloud/overview/) databases that belong to fixed subscriptions using the `Redis Cloud` option on the form to auto-discover databases.
*   [#2146](https://github.com/RedisInsight/RedisInsight/pull/2146),[#2161](https://github.com/RedisInsight/RedisInsight/pull/2161) Added UX optimizations in the Browser layout to improve the experience when performing [full-text search and queries](https://redis.io/docs/stack/search/), filtering, and bulk actions.
*   [#2200](https://github.com/RedisInsight/RedisInsight/pull/2200) Changed to a monospaced font in [JSON](https://redis.io/docs/stack/json/) key types, and JSON formatters in Browser and Workbench.
*   [#2204](https://github.com/RedisInsight/RedisInsight/pull/2204) Re-bind default RedisInsight port from 5001 to 5530 to avoid conflicts with other applications
*   [#2120](https://github.com/RedisInsight/RedisInsight/pull/2120) Added the ability to investigate the commands processed by Redis or Redis Stack server without the need to stop Profiler when a new record appears.
*   [#2186](https://github.com/RedisInsight/RedisInsight/pull/2186) Unified the RedisInsight icon with other macOS applications.

**Bugs**

*   [#2154](https://github.com/RedisInsight/RedisInsight/pull/2154) Display `(integer) 0` instead of `nil` in [ZRANK](https://redis.io/commands/zrank/) results in Workbench

## On this page
