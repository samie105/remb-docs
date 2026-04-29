---
title: "Redis 8.0 release notes and breaking changes"
source: "https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-0/"
canonical_url: "https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:44.814Z"
content_hash: "e3a4afe227cef9fd131d7d99d6f5e133c27141e994812fdcb8b26bad1decde3c"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Redis Cloud changelog","→","Redis Cloud changelog","→\n      \n        Redis version release notes and breaking changes","→","Redis version release notes and breaking changes","→\n      \n        Redis 8.0 release notes and breaking changes","→","Redis 8.0 release notes and breaking changes"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Redis Cloud changelog","→","Redis Cloud changelog","→\n      \n        Redis version release notes and breaking changes","→","Redis version release notes and breaking changes","→\n      \n        Redis 8.0 release notes and breaking changes","→","Redis 8.0 release notes and breaking changes"]
nav_prev: {"path": "../index.md", "title": "Redis version release notes and breaking changes"}
nav_next: {"path": "../8-2/index.md", "title": "Redis 8.2 release notes and breaking changes"}
---

# Redis 8.0 release notes and breaking changes

Release notes and breaking changes for Redis 8.0 on Redis Cloud.

Redis Cloud

Redis 8.0 introduces powerful new capabilities, including the beta release of the Vector Set data structure, designed for AI use cases such as semantic search and recommendation systems. Redis 8 also merges Redis Stack and Redis Community Edition into a single unified distribution: Redis Open Source. For more information on the changes in Redis 8.0, see [What's new in Redis 8.0](/docs/latest/develop/whats-new/8-0/).

## Breaking changes

When new versions of Redis Open Source change existing commands, upgrading your database to a new version can potentially break some functionality. Before you upgrade, read the provided list of breaking changes that affect Redis Cloud and update any applications that connect to your database to handle these changes.

Make sure to review all breaking changes between your current version of Redis and the version you are upgrading to.

### Potentially breaking changes to ACLs

Note:

The following content is relevant to all Redis distributions (RS, RC, and ROS).

Redis 8 includes Redis Search, as well as JSON, time series, Bloom filter, cuckoo filter, top-k, count-min sketch, and t-digest data types. The integration of these features into Redis also comes with improvements to Redis [ACL](/docs/latest/operate/oss_and_stack/management/security/acl/) rules.

Warning:

These ACL changes may introduce breaking changes for some users, which must be analyzed carefully.

#### Extension to the existing ACL categories

Before Redis 8, the existing ACL categories @read, @write, @dangerous, @admin, @slow, and @fast did not include commands for Redis Search and the JSON, time series, and probabilistic data structures.

Starting with Redis 8, Redis includes all Redis Search, JSON, time series, Bloom filter, cuckoo filter, top-k, count-min sketch, and t-digest commands in these existing ACL categories.

As a result:

*   Existing ACL rules such as `+@read +@write` will allow access to more commands than in previous versions of Redis. Here are some examples:
    
    *   A user with `+@read` access will be able to execute `FT.SEARCH`.
    *   A user with `+@write` access will be able to execute `JSON.SET`.
*   ACL rules such as `+@all -@write` will allow access to fewer commands than previous versions of Redis. For example:
    
    *   A user with `+@all -@write` will not be able to execute `JSON.SET`.

Note that the `@all` category did not change, as it always included all the commands.

Additionally, ACL rules such as `+@read +JSON.GET` can now be simplified as `+@read` because `JSON.GET` is included in the `@read` category.

#### Who is affected by this change?

Users who currently use Redis Search and/or the JSON, time series, or probabilistic data structures, and use custom ACL rules.

You should reanalyze your ACL rules to make sure they are aligned with your security and access control requirements.

### Redis Search

The following changes affect behavior and validation in Redis Search:

*   Enforces validation for `LIMIT` arguments (offset must be 0 if limit is 0).
*   Enforces parsing rules for `FT.CURSOR READ` and `FT.ALIASADD`.
*   Parentheses are now required for exponentiation precedence in `APPLY` expressions.
*   Invalid input now returns errors instead of empty results.
*   Default values revisited for reducers like `AVG`, `COUNT`, `SUM`, `STDDEV`, `QUANTILE`, and others.
*   Updates to scoring (`BM25` is now the default instead of `TF-IDF`).
*   Improved handling of expired records, memory constraints, and malformed fields.

For a full list of Redis Search-related changes, see the [release notes](https://github.com/redis/redis/releases).

## On this page
