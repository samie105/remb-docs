---
title: "RedisInsight v2.46.0, March 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.46.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.46.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:12.996Z"
content_hash: "c691223bb13152fa98a5158b87a02fb73b55abf9733c6bdbc189e25ecd5e1b24"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.46.0, March 2024","→","RedisInsight v2.46.0, March 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.46.0, March 2024","→","RedisInsight v2.46.0, March 2024"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.50.0/index.md", "title": "Redis Insight v2.50.0, May 2024"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.48.0/index.md", "title": "Redis Insight v2.48.0, April 2024"}
---

# RedisInsight v2.46.0, March 2024

RedisInsight v2.46

## 2.46 (March 2024)

This is the General Availability (GA) release of RedisInsight 2.46.

### Highlights

*   New formatters for 32-bit and 64-bit vector embeddings for a more human-readable representation in the Browser
*   Cleaner layout on the main page with quick access to JSON and search & query tutorials and Redis Cloud in-app sign-up

### Details

**Features and improvements**

*   [#2843](https://github.com/RedisInsight/RedisInsight/pull/2843), [#3185](https://github.com/RedisInsight/RedisInsight/pull/3185) Adding new formatters for 32-bit and 64-bit vector embeddings to visualize them as arrays in Browser for a simpler and more intuitive representation.
*   [#3069](https://github.com/RedisInsight/RedisInsight/pull/3069) UX enhancements in the database list page for an improved user experience, leading to a cleaner layout and easier navigation.
*   [#3151](https://github.com/RedisInsight/RedisInsight/pull/3151) Launch RedisInsight with the previously used window size.

**Bugs**

*   [#3152](https://github.com/RedisInsight/RedisInsight/pull/3152), [#3156](https://github.com/RedisInsight/RedisInsight/pull/3156) A fix to [support the \* wildcard](https://github.com/RedisInsight/RedisInsight/issues/3146) in Stream IDs.
*   [#3174](https://github.com/RedisInsight/RedisInsight/pull/3174) Display invalid JSONs as unformatted values when a JSON view is set in Workbench results.

## On this page

