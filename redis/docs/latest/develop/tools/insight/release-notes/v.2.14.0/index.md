---
title: "RedisInsight v2.14.0, November 2022"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.14.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.14.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:46.175Z"
content_hash: "7f100fbcbb4f7fab4bb70d2841ad3cb35ec8507827dc33c0fb49779ef81aca99"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.14.0, November 2022","→","RedisInsight v2.14.0, November 2022"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.14.0, November 2022","→","RedisInsight v2.14.0, November 2022"]
nav_prev: {"path": "redis/docs/latest/develop/whats-new/8-6/index.md", "title": "Redis 8.6"}
nav_next: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-15-july2025/index.md", "title": "Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes"}
---

# RedisInsight v2.14.0, November 2022

RedisInsight v2.14.0

## 2.14.0 (November 2022)

This is the General Availability (GA) release of RedisInsight 2.14.

### Highlights

*   Support for [search capabilities](https://redis.io/docs/stack/search/) in Browser: Create secondary index via dedicated form, run queries and full-text search in Browser or Tree views
*   Ability to resize the column width of key values when displaying hashes, lists, and sorted sets
*   Command processing time displayed as part of the result in Workbench

### Details

**Features and improvements**

*   [#1345](https://github.com/RedisInsight/RedisInsight/pull/1345), [#1346](https://github.com/RedisInsight/RedisInsight/pull/1346), [#1376](https://github.com/RedisInsight/RedisInsight/pull/1376) Added support for [search capabilities](https://redis.io/docs/stack/search/) in Browser tool. Create secondary index of your data using a dedicated form. Conveniently run your queries and full-text search against the preselected index and display results in Browser or Tree views.
*   [#1385](https://github.com/RedisInsight/RedisInsight/pull/1385) Resize the column width of key values when displaying hashes, lists, and sorted sets
*   [#1354](https://github.com/RedisInsight/RedisInsight/pull/1407) Do not scroll to the end of results when double-clicking a command output in CLI
*   [#1347](https://github.com/RedisInsight/RedisInsight/pull/1347) Display command processing time as part of the result in Workbench (time taken to process the command by both RedisInsight backend and Redis)
*   [#1351](https://github.com/RedisInsight/RedisInsight/pull/1351) Display the namespaces section in the Database analysis report when no namespaces were found

## On this page
