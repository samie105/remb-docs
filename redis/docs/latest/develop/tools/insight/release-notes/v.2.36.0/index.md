---
title: "RedisInsight v2.36.0, October 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.36.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.36.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:55.564Z"
content_hash: "c24ffd733f6a1ec05f4c48a9443fdf58f40c2b81e369c4aa0055a064d182e1ac"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.36.0, October 2023","→","RedisInsight v2.36.0, October 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.36.0, October 2023","→","RedisInsight v2.36.0, October 2023"]
---
# RedisInsight v2.36.0, October 2023

RedisInsight v2.36

## 2.36 (October 2023)

This is the General Availability (GA) release of RedisInsight 2.36.

### Highlights

*   Optimizations for efficient handling of big [Redis strings](https://redis.io/docs/data-types/strings/): choose to either view the string value for up to a maximum of 5,000 characters or download the data fully as a file if it exceeds the limit
*   Improved security measurement to no longer display in plain text existing database passwords, SSH passwords, passphrases, and private keys

### Details

**Features and improvements**

*   [#2685](https://github.com/RedisInsight/RedisInsight/pull/2685), [#2686](https://github.com/RedisInsight/RedisInsight/pull/2686) Added optimizations for working with big [Redis strings](https://redis.io/docs/data-types/strings/). Users can now choose to either view the data up to a maximum of 5,000 characters or download it in a file fully if it exceeds the limit.
*   [#2647](https://github.com/RedisInsight/RedisInsight/pull/2647) Improved security measurement to no longer expose the existing database passwords, SSH passwords, passphrases, and private keys in plain text
*   [#2631](https://github.com/RedisInsight/RedisInsight/pull/2631) Added proactive notification to restart the application when a new version becomes available
*   [#2705](https://github.com/RedisInsight/RedisInsight/pull/2705) Basic support in the [search index](https://redis.io/docs/interact/search-and-query/) creation form (in Browser) to enable [geo polygon](https://redis.io/commands/ft.create/#:~:text=Vector%20Fields.-,GEOSHAPE,-%2D%20Allows%20polygon%20queries) search
*   [#2681](https://github.com/RedisInsight/RedisInsight/pull/2681) Updated the Pickle formatter to [support](https://github.com/RedisInsight/RedisInsight/issues/2260) Pickle protocol 5

**Bugs**

*   [#2675](https://github.com/RedisInsight/RedisInsight/pull/2675) Show the "Scan more" control until the cursor returned by the server is 0 to fix [cases](https://github.com/RedisInsight/RedisInsight/issues/2618) when not all keys are displayed.

## On this page
