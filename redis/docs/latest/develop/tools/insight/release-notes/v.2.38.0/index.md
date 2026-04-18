---
title: "RedisInsight v2.38.0, November 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.38.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.38.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:37.418Z"
content_hash: "5345c7beec69f5e89fda68c6a2dd25f8e5ad3c8fdd6fa6bc3e3c3eef67817465"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.38.0, November 2023","→","RedisInsight v2.38.0, November 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.38.0, November 2023","→","RedisInsight v2.38.0, November 2023"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.36.0/index.md", "title": "RedisInsight v2.36.0, October 2023"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.4.0/index.md", "title": "RedisInsight v2.4.0, June 2022"}
---

# RedisInsight v2.38.0, November 2023

RedisInsight v2.38

## 2.38 (November 2023)

This is the General Availability (GA) release of RedisInsight 2.38.

### Highlights

*   Major UX improvements and space optimization for a cleaner and more organized Tree view, ensuring easier namespace navigation and faster key browsing. Additionally, in Tree view, you can now sort your Redis key names alphabetically.
*   Renamed the application from RedisInsight v2 to simply RedisInsight

### Details

**Features and improvements**

*   [#2706](https://github.com/RedisInsight/RedisInsight/pull/2706), [#2783](https://github.com/RedisInsight/RedisInsight/pull/2783) Major UX improvements and space optimization for a cleaner and more organized Tree view. This includes consolidating the display of namespaces and keys in a dedicated section and omitting namespace information from key names in the list of keys. In addition, the Tree view introduces a new option to alphabetically sort Redis key names.
*   [#2751](https://github.com/RedisInsight/RedisInsight/pull/2751) Renamed the application from RedisInsight v2 to simply RedisInsight
*   [#2799](https://github.com/RedisInsight/RedisInsight/pull/2799) Automatically make three retries to establish or re-establish a database connection if an error occurs

**Bugs**

*   [#2793](https://github.com/RedisInsight/RedisInsight/pull/2793) [Do not require](https://github.com/RedisInsight/RedisInsight/issues/2765) an SSH password or passphrase
*   [#2794](https://github.com/RedisInsight/RedisInsight/pull/2794) Prevent [potential crashes](https://github.com/RedisInsight/RedisInsight/issues/2763) caused by using parentheses in usernames on the Windows operating system
*   [#2797](https://github.com/RedisInsight/RedisInsight/pull/2797) Avoid initiating a bulk deletion or Profiler after the operating system resumes from sleep mode

## On this page
