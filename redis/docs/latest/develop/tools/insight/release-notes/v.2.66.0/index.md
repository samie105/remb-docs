---
title: "Redis Insight v2.66.0, January 2025"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.66.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.66.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:58.891Z"
content_hash: "f0ca0c6555ed6952caef2ae07f35187905d3f00e5099112c3f80e75bcea03817"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.66.0, January 2025","→","Redis Insight v2.66.0, January 2025"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.66.0, January 2025","→","Redis Insight v2.66.0, January 2025"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.64.1/index.md", "title": "Redis Insight v2.64.1, December 2024"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.68.0/index.md", "title": "Redis Insight v2.68.0, April 2025"}
---

# Redis Insight v2.66.0, January 2025

Redis Insight v2.66

## 2.66 (January 2025)

This is the General Availability (GA) release of Redis Insight 2.66.

### Highlights

*   Switch between Redis databases and [Redis Data Integration](https://redis.io/data-integration/?utm_source=redisinsight&utm_medium=repository&utm_campaign=release_notes) (RDI) instances without returning to the database or RDI endpoint list.
*   Improved performance in Browser when handling nested JSON data, along with the option to hide key size and TTL for a more efficient navigation.

### Details

**Features and improvements**

*   [#4258](https://github.com/RedisInsight/RedisInsight/pull/4258) Improved navigation allows seamless switching between Redis databases and [Redis Data Integration](https://redis.io/data-integration/?utm_source=redisinsight&utm_medium=repository&utm_campaign=release_notes) (RDI) instances without returning to the database or endpoint list.
*   [#4315](https://github.com/RedisInsight/RedisInsight/pull/4315) Improved performance when working with nested JSON data types in Browser.
*   [#4290](https://github.com/RedisInsight/RedisInsight/pull/4290) Added an option to hide key size and TTL in Browser to optimize space. Hiding key size can also help avoid performance issues when working with large keys.
*   [#4268](https://github.com/RedisInsight/RedisInsight/pull/4268) Enhanced UX for adding Redis databases, now displaying information in multiple tabs.
*   [#4228](https://github.com/RedisInsight/RedisInsight/pull/4228) Added the ability to customize the refresh interval or stop refreshing database overview metrics, allowing to change the frequency or avoid seeing the `INFO` command in Profiler.
*   [#4255](https://github.com/RedisInsight/RedisInsight/pull/4255) Updated Brotli decompression to use brotli-wasm.

**Bugs**

*   [#4304](https://github.com/RedisInsight/RedisInsight/pull/4304) Resolved the [application startup error](https://github.com/RedisInsight/RedisInsight/issues/3871) on Ubuntu 24.04 caused by a space in the application name.

**SHA-256 Checksums**

Package

SHA-256

Windows

Bjxu9UFPpWhz29prFqRsKDNlF4LZaTUJgAvBBI/FNQ9rBncFGGOb5m59wY3dXIYAG6+VB6F9U9ylffv31IDszw==

Linux AppImage

T6y4xd4BVs1skNAOWkFpWkcov0288qIh2dXHo7gofDw99ow6phV3LzcaasHLT5F+TdlbfcjB8aGVJMx1qEIaBw==

Linux Debian

WaMsSd6qKvw5x6ALLLPTnFoWMX/qVZafVJ3SJAUr8IYoGksnNlU1huUr9q/ftlwP00y2zYac7EZBbl2Z/bOppQ==

MacOS Intel

4x7vG7nTt3s4+kQ6WSuhrtigRa2XZ9Q6UiR1WCb/vROAL/X5GjmFvv4jBPIxZC1w6Z46pNzS+IhLcI4oHVSyAw==

MacOS Apple silicon

x8wlgNy4dadKV3tcn8uJh/ksvEMnBYaCPvlxlfwcMjNwXNoSBQ+tK6kgJSONGgLVUqtQe1pfTbzqBsqkEAxquw==

## On this page
