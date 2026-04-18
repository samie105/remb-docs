---
title: "RedisInsight v2.26.0, May 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.26.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.26.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:19.663Z"
content_hash: "5bbc2b85203aebb5ba6029cbfb7071718aba146e4717a03072143470395243ac"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.26.0, May 2023","→","RedisInsight v2.26.0, May 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.26.0, May 2023","→","RedisInsight v2.26.0, May 2023"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.30.0/index.md", "title": "RedisInsight v2.30.0, July 2023"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v2.28.0/index.md", "title": "RedisInsight v2.28.0, June 2023"}
---

# RedisInsight v2.26.0, May 2023

RedisInsight v2.26

## 2.26 (May 2023)

This is the General Availability (GA) release of RedisInsight 2.26.

### Highlights

*   Introducing Insights (Beta): a new right-side panel that displays contextualised database recommendations for optimizing performance and memory usage. The list of recommendations gets updated as you interact with your database. Check out the paired-up tutorials to learn about the recommended feature and vote to provide feedback. This functionality is being rolled out gradually to the user base.
*   Support for bulk data upload in custom tutorials: quickly upload sample datasets from your custom RedisInsight tutorials to share your Redis expertise with your team and the wider community.

### Details

**Features and improvements**

*   [#1847](https://github.com/RedisInsight/RedisInsight/pull/1847), [#1901](https://github.com/RedisInsight/RedisInsight/pull/1901), [#1957](https://github.com/RedisInsight/RedisInsight/pull/1957), [#1972](https://github.com/RedisInsight/RedisInsight/pull/1972) Launching Insights (Beta): a new right-side panel that displays contextualised database recommendations for optimizing performance and memory usage. The list of recommendations gets updated in real-time as you interact with your database taking into account database configuration, user actions and accessed data. Consult the paired-up tutorials to learn more about the recommended feature. This functionality is being rolled out gradually to the user base in order to allow the RedisInsight team to learn and adjust the recommendations. Provide feedback directly in the app or the [GitHub repository](https://github.com/RedisInsight/RedisInsight/issues).
*   [#2019](https://github.com/RedisInsight/RedisInsight/pull/2019) Quickly upload sample data sets in bulk from your custom RedisInsight tutorials to share your Redis expertise with your team and the wider community. Use a text file with the list of Redis commands and follow our simple [instructions](https://github.com/RedisInsight/Tutorials) to include example data sets in your custom RedisInsight tutorials
*   [#2010](https://github.com/RedisInsight/RedisInsight/pull/2010), [#2012](https://github.com/RedisInsight/RedisInsight/pull/2012), [#2013](https://github.com/RedisInsight/RedisInsight/pull/2013) Optimized the logic when filtering per data type in Browser to avoid unnecessary [TYPE](https://redis.io/commands/type/) commands

**Bugs**

*   [#2014](https://github.com/RedisInsight/RedisInsight/pull/2014) Display the actual command processing time in Workbench when results are grouped

## On this page
