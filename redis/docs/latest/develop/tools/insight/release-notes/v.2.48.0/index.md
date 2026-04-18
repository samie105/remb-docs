---
title: "Redis Insight v2.48.0, April 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.48.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.48.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:13.251Z"
content_hash: "37690bdfcabc60351d7bf3d302ab68b516c830abad61c2ffcaf7aee67271e240"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.48.0, April 2024","→","Redis Insight v2.48.0, April 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.48.0, April 2024","→","Redis Insight v2.48.0, April 2024"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.46.0/index.md", "title": "RedisInsight v2.46.0, March 2024"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.44.0/index.md", "title": "RedisInsight v2.44.0, February 2024"}
---

# Redis Insight v2.48.0, April 2024

Redis Insight v2.48

## 2.48 (April 2024)

This is the General Availability (GA) release of Redis Insight 2.48.

### Highlights

*   New look, equally fast.
*   Learn Redis faster by uploading sample data and a concise tutorial for empty databases.
*   Enhance the security and scalability when running Redis Insight on Docker behind a proxy by adding support for the static proxy subpath.

### Details

**Features and improvements**

*   [#3233](https://github.com/RedisInsight/RedisInsight/pull/3233) New look, equally fast. We've refreshed our Redis Insight app to align with our new brand look.
*   [#3224](https://github.com/RedisInsight/RedisInsight/pull/3224) Jumpstart your Redis journey by uploading sample data with JSON and basic data structures for empty databases. To upload the sample data, navigate to the Browser screen for your empty database and initiate the upload process with just a click.
*   [#2711](https://github.com/RedisInsight/RedisInsight/pull/2711) Enhance the security and scalability by running Redis Insight on Docker [behind a proxy](https://github.com/RedisInsight/RedisInsight-reverse-proxy) using the newly added support for the static proxy subpath. Use the `RIPROXYPATH` environment variable to configure the subpath proxy path.

## On this page
