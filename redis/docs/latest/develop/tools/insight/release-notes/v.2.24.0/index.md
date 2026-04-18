---
title: "RedisInsight v2.24.0, April 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.24.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.24.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:29.559Z"
content_hash: "71ed529d3090b48cda2861cdeda24ed4ce0742113ae45ec748eb6c4577039cdd"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.24.0, April 2023","→","RedisInsight v2.24.0, April 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.24.0, April 2023","→","RedisInsight v2.24.0, April 2023"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v2.28.0/index.md", "title": "RedisInsight v2.28.0, June 2023"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.22.1/index.md", "title": "RedisInsight v2.22.1, March 2023"}
---

# RedisInsight v2.24.0, April 2023

RedisInsight v2.24

## 2.24 (April 2023)

This is the General Availability (GA) release of RedisInsight 2.24.

### Highlights

*   Bulk data upload: Upload the list of Redis commands from a text file using the new bulk action in the Browser tool. Use the bulk data upload with custom RedisInsight tutorials to quickly load your sample dataset.
*   Support for images in custom tutorials: showcase your Redis expertise with your team and the wider community by building shareable RedisInsight tutorials.
*   JSON formatter support for the [JSON.GET](https://redis.io/commands/json.get/), [JSON.MGET](https://redis.io/commands/json.mget/), and [GET](https://redis.io/commands/get/) command output in Workbench.
*   Added Brotli and PHP GZcompress to the list of supported decompression formats to view your data in a human-readable format.

### Details

**Features and improvements**

*   [#1930](https://github.com/RedisInsight/RedisInsight/pull/1930), [#1961](https://github.com/RedisInsight/RedisInsight/pull/1961) Upload the list of Redis commands from a text file using the new bulk action in the Browser tool. Use the bulk data upload with custom RedisInsight tutorials to quickly load your sample dataset.
*   [#1936](https://github.com/RedisInsight/RedisInsight/pull/1936), [#1939](https://github.com/RedisInsight/RedisInsight/pull/1939) Added support for images in custom tutorials, available in Workbench. Showcase your Redis expertise with your team and the wider community by building shareable tutorials. Use markdown syntax described in our [instructions](https://github.com/RedisInsight/Tutorials) to build tutorials.
*   [#1946](https://github.com/RedisInsight/RedisInsight/pull/1946) See the output of [JSON.GET](https://redis.io/commands/json.get/), [JSON.MGET](https://redis.io/commands/json.mget/), and [GET](https://redis.io/commands/get/) formatted as JSON in Workbench.
*   [#1876](https://github.com/RedisInsight/RedisInsight/pull/1876) Ability to directly delete a key in the Browser list of keys without having to view its values.
*   [#1889](https://github.com/RedisInsight/RedisInsight/pull/1889), [#1900](https://github.com/RedisInsight/RedisInsight/pull/1900) Added Brotli and PHP GZcompress to the list of supported decompression formats to view your data in a human-readable format. Decompression format is configurable when adding a database connection.
*   [#1886](https://github.com/RedisInsight/RedisInsight/pull/1886) Enhanced command syntax in CLI, Workbench, and Command Helper to align with [command documentation](https://redis.io/commands/).
*   [#1975](https://github.com/RedisInsight/RedisInsight/pull/1975) [Renamed](https://github.com/RedisInsight/RedisInsight/issues/1902) the "Display On System Tray" to "Show in Menu Bar" on macOS.

**Bugs**

*   [#1990](https://github.com/RedisInsight/RedisInsight/pull/1990) Keep the previously specified SNI parameters when a database connection is edited.
*   [#1999](https://github.com/RedisInsight/RedisInsight/pull/1999) Keep the previously set database index when a database connection is edited.

## On this page
