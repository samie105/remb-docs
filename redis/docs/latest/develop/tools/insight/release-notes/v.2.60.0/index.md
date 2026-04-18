---
title: "Redis Insight v2.60.0, October 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.60.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.60.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:20.693Z"
content_hash: "4c68d4ac25e9f68cadb745dbfb00240d2ea159643cefeceaffab58f4f461b34a"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.60.0, October 2024","→","Redis Insight v2.60.0, October 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.60.0, October 2024","→","Redis Insight v2.60.0, October 2024"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.62.0/index.md", "title": "Redis Insight v2.62.0, November 2024"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.58.0/index.md", "title": "Redis Insight v2.58.0, October 2024"}
---

# Redis Insight v2.60.0, October 2024

Redis Insight v2.60

## 2.60 (October 2024)

This is the General Availability (GA) release of Redis Insight 2.60.

### Highlights

*   Advanced and schema-aware command auto-complete for [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query/?utm_source=redisinsight&utm_medium=main&utm_campaign=release_notes) is now available in Workbench, enabling faster and more accurate query building with smart suggestions for indexes, schemas, and expressions.
*   Support for adding multiple elements to the head or tail of lists, for both new or existing keys.
*   Multiple UI enhancements for clarity and ease of use when editing Redis Data Integration (RDI) jobs.

### Details

**Features and improvements**

*   [#3553](https://github.com/RedisInsight/RedisInsight/pull/3553), [#3647](https://github.com/RedisInsight/RedisInsight/pull/3647), [#3669](https://github.com/RedisInsight/RedisInsight/pull/3669) Advanced, schema-aware auto-complete for [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query/?utm_source=redisinsight&utm_medium=main&utm_campaign=release_notes) in Workbench. Enjoy faster query building with context-sensitive suggestions that recognize indexes, schemas, and fields based on your current query. Start typing any [Redis Search](https://redis.io/docs/latest/commands/?group=search) command in Workbench to try this feature.
*   [#3891](https://github.com/RedisInsight/RedisInsight/pull/3891) Allows to easily push multiple elements to the head or tail of list data types, whether creating new or updating existing lists.
*   [#3891](https://github.com/RedisInsight/RedisInsight/pull/3891) UX/UI enhancements to provide more details about Redis Data Integration (RDI) job transformation and output results in the dry-run section.
*   [#3981](https://github.com/RedisInsight/RedisInsight/pull/3981) Removes confirmation prompts for template insertions in Redis Data Integration jobs, simplifying a workflow.
*   [#3827](https://github.com/RedisInsight/RedisInsight/pull/3827) Provides easy-to-understand metrics of network input/output by automatically converting units in Browser Overview.
*   [#3982](https://github.com/RedisInsight/RedisInsight/pull/3982), [#3975](https://github.com/RedisInsight/RedisInsight/pull/3975), [#3941](https://github.com/RedisInsight/RedisInsight/pull/3941) Various vulnerabilities have been fixed.

## On this page
