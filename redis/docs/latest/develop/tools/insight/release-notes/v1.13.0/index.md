---
title: "RedisInsight v1.13, Aug 2022"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v1.13.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v1.13.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:57.849Z"
content_hash: "ddd3b59c5e0c094cb11220aa5a417db0de7ab37123511eeb4ec2316985829c11"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v1.13, Aug 2022","→","RedisInsight v1.13, Aug 2022"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v1.13, Aug 2022","→","RedisInsight v1.13, Aug 2022"]
nav_prev: {"path": "redis/docs/latest/develop/data-types/json/resp3/index.md", "title": "Guide for migrating from RESP2 to RESP3 replies"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/management/scaling/index.md", "title": "Scale with Redis Cluster"}
---

# RedisInsight v1.13, Aug 2022

RedisInsight v1.13.0

## 1.13.1 (November 2022)

This is the maintenance release of RedisInsight 1.13 (v1.13.1).

### Fixes:

*   Core:
    *   Fixed container vulnerabilities.
    *   Prevented healthcheck API from overloading RedisInsight DB. Earlier, a separate session was created for each healthcheck hit, which overloaded the database with too many session tokens. Now, healtcheck API doesn't create any session tokens.
    *   Get Sentinel host using IP field.
*   Memory Analysis:
    *   Added support for `hashlistpack`, `zsetlistpack`, `quicklist2` and `streamlistpack2`, encoding types.

## 1.13.0 (August 2022)

This is the General Availability Release of RedisInsight 1.13 (v1.13.0).

## Headlines

*   Subpath Proxy Support

## Details

### Core

*   Subpath Proxy support: RedisInsight can now be proxied behind a subpath
*   Added trusted origins environment variable to set trusted origins
*   Fixed major container vulnerabilities
*   Added proxy notification that displays when such an environment is found

### RediSearch

*   Fixed index information

### Profiler

*   Added support for IPv6 clients

### Memory Analyzer

*   Fixed Lua recommendation

## On this page

