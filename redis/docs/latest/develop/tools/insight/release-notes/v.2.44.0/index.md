---
title: "RedisInsight v2.44.0, February 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.44.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.44.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:15.686Z"
content_hash: "a7152f2cfd5f48c047a903d5ccf97bd209eb9feaef07f76d593bee055c3f9cf7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.44.0, February 2024","→","RedisInsight v2.44.0, February 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.44.0, February 2024","→","RedisInsight v2.44.0, February 2024"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.48.0/index.md", "title": "Redis Insight v2.48.0, April 2024"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.42.0/index.md", "title": "RedisInsight v2.42.0, January 2024"}
---

# RedisInsight v2.44.0, February 2024

RedisInsight v2.44

## 2.44 (February 2024)

This is the General Availability (GA) release of RedisInsight 2.44.

### Highlights

*   Added support for SSH tunneling for clustered databases, unblocking some users who want to migrate from RESP.app to RedisInsight.
*   UX optimizations in the Browser layout to make it easier to leverage [search and query](https://redis.io/docs/interact/search-and-query/?utm_source=redisinsight&utm_medium=main&utm_campaign=redisinsight_release_notes) indexes.

### Details

**Features and improvements**

*   [#2711](https://github.com/RedisInsight/RedisInsight/pull/2711), [#3040](https://github.com/RedisInsight/RedisInsight/pull/3040) Connect to your clustered Redis database via SSH tunnel using a password or private key in PEM format.
*   [#3030](https://github.com/RedisInsight/RedisInsight/pull/3030), [#3070](https://github.com/RedisInsight/RedisInsight/pull/3070) UX optimizations in the Browser layout to enlarge the "Filter by Key" input field in the Browser and optimize the display of long [search and query](https://redis.io/docs/interact/search-and-query/?utm_source=redisinsight&utm_medium=main&utm_campaign=redisinsight_release_notes) indexes.
*   [#3033](https://github.com/RedisInsight/RedisInsight/pull/3033), [#3036](https://github.com/RedisInsight/RedisInsight/pull/3036) Various improvements for custom [tutorials](https://github.com/RedisInsight/Tutorials), including visual highlighting of Redis code blocks and strengthening security measures for bulk data uploads by providing an option to download and preview the list of commands for upload.
*   [#3010](https://github.com/RedisInsight/RedisInsight/pull/3010) Enhancements to prevent authentication errors caused by [certain special characters](https://github.com/RedisInsight/RedisInsight/issues/3019) in database passwords.

**Bugs**

*   [#3029](https://github.com/RedisInsight/RedisInsight/pull/3029) A fix for cases when autofill [prevents](https://github.com/RedisInsight/RedisInsight/issues/3026) the form to auto-discover Redis Software Cluster database from being submitted.

## On this page


