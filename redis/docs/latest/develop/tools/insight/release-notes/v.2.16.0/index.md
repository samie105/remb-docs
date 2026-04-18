---
title: "RedisInsight v2.16.0, December 2022"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.16.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.16.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:09.266Z"
content_hash: "1b8b23cbcac62c3dfa0fec1aeafba46e5a9b0ae1b578e2eadf27da250f9e34d4"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.16.0, December 2022","→","RedisInsight v2.16.0, December 2022"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.16.0, December 2022","→","RedisInsight v2.16.0, December 2022"]
nav_prev: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-16-august2025/index.md", "title": "Redis Enterprise for Kubernetes 7.22.0-16 (August 2025) release notes"}
nav_next: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-8-4-releases/7-8-4-8-feb25/index.md", "title": "Redis Enterprise for Kubernetes 7.8.4-8 (Feb 2025) release notes"}
---

# RedisInsight v2.16.0, December 2022

RedisInsight v2.16.0

## 2.16.0 (December 2022)

This is the General Availability (GA) release of RedisInsight 2.16.

### Highlights

*   Bulk import database connections from a file
*   Navigation enhancements for the Tree view
*   Pre-populated host, port, and database alias in the form when adding a new Redis database

### Details

**Features and improvements**

*   [#1492](https://github.com/RedisInsight/RedisInsight/pull/1492), [#1497](https://github.com/RedisInsight/RedisInsight/pull/1497), [#1500](https://github.com/RedisInsight/RedisInsight/pull/1500), [#1502](https://github.com/RedisInsight/RedisInsight/pull/1502) Migrate your database connections from other Redis GUIs, including RESP.app, with the new feature to bulk import database connections from a file.
*   [#1506](https://github.com/RedisInsight/RedisInsight/pull/1506) Pre-populated host (127.0.0.1), port (6379, or 26379 for [Sentinel](https://redis.io/docs/management/sentinel/) connection type), and database alias in the form when adding a new Redis database
*   [#1473](https://github.com/RedisInsight/RedisInsight/pull/1473) **Browser** view is renamed **List** view to avoid confusion with the Browser tool
*   [#1464](https://github.com/RedisInsight/RedisInsight/pull/1464) Navigation enhancements for the Tree view, covering cases when filters are applied, the list of keys is refreshed or the view is switched to the Tree view
*   [#1481](https://github.com/RedisInsight/RedisInsight/pull/1481), [#1482](https://github.com/RedisInsight/RedisInsight/pull/1482), [#1489](https://github.com/RedisInsight/RedisInsight/pull/1489) Indication of new database connections that have been manually added, auto-discovered or imported, but not opened yet
*   [#1499](https://github.com/RedisInsight/RedisInsight/pull/1499) Display values of [JSON](https://redis.io/docs/stack/json/) keys when [JSON.DEBUG MEMORY](https://redis.io/commands/json.debug-memory/) is not available

**Bugs**

*   [#1514](https://github.com/RedisInsight/RedisInsight/pull/1514) Scan the database even when the [DBSIZE](https://redis.io/commands/dbsize/) returns 0

## On this page

