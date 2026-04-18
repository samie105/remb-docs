---
title: "Redis 8.4 release notes and breaking changes"
source: "https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-4/"
canonical_url: "https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-4/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:44.383Z"
content_hash: "558959e34cb001430e5b8e06457227a59977cc971e78c12c652ed865b2cf77c9"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Redis Cloud changelog","→","Redis Cloud changelog","→\n      \n        Redis version release notes and breaking changes","→","Redis version release notes and breaking changes","→\n      \n        Redis 8.4 release notes and breaking changes","→","Redis 8.4 release notes and breaking changes"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Redis Cloud changelog","→","Redis Cloud changelog","→\n      \n        Redis version release notes and breaking changes","→","Redis version release notes and breaking changes","→\n      \n        Redis 8.4 release notes and breaking changes","→","Redis 8.4 release notes and breaking changes"]
---
# Redis 8.4 release notes and breaking changes

Release notes and breaking changes for Redis 8.4 on Redis Cloud.

Redis Cloud

Redis 8.4 builds on the foundation of Redis 8.2 with significant enhancements to cluster operations, string manipulation, and stream processing capabilities.. For more information on the changes in Redis 8.4, see [What's new in Redis 8.4](/docs/latest/develop/whats-new/8-4/) and review the Redis Open Source [8.4 release notes](/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.4-release-notes/).

## Known limitations

When using Redis 8.4, be aware of these current limitations:

*   Search commands (`FT.SEARCH`, `FT.AGGREGATE`, `FT.CURSOR`, `FT.HYBRID`) and time series commands (`TS.MGET`, `TS.MRANGE`, `TS.MREVRANGE`, `TS.QUERYINDEX`) may return partial results or duplicates during atomic slot migration.
*   `FT.PROFILE`, `FT.EXPLAIN`, and `FT.EXPLAINCLI` don't include `FT.HYBRID` options.
*   `FT.HYBRID` metrics aren't displayed in `FT.INFO` and `INFO` commands.
*   Several `FT.HYBRID` options (`EXPLAINSCORE`, `SHARD_K_RATIO`, `YIELD_DISTANCE_AS`, `WITHCURSOR`) are not yet available.
*   Post-filtering after the `COMBINE` step using `FILTER` is not currently supported.

## On this page
