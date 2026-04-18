---
title: "Redis 8.2 release notes and breaking changes"
source: "https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-2/"
canonical_url: "https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-2/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:14.154Z"
content_hash: "6531b80e0fe4d5fa9bd2d06316bda471c361816be6b1edc126527f42c2ed16fa"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Redis Cloud changelog","→","Redis Cloud changelog","→\n      \n        Redis version release notes and breaking changes","→","Redis version release notes and breaking changes","→\n      \n        Redis 8.2 release notes and breaking changes","→","Redis 8.2 release notes and breaking changes"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Cloud","→","Redis Cloud","→\n      \n        Redis Cloud changelog","→","Redis Cloud changelog","→\n      \n        Redis version release notes and breaking changes","→","Redis version release notes and breaking changes","→\n      \n        Redis 8.2 release notes and breaking changes","→","Redis 8.2 release notes and breaking changes"]
---
# Redis 8.2 release notes and breaking changes

Release notes and breaking changes for Redis 8.2 on Redis Cloud.

Redis Cloud

Redis 8.2 builds on the foundation of Redis 8.0 with significant performance and memory optimizations, enhanced streaming capabilities, and improved cluster management tools. For more information on the changes in Redis 8.2, see [What's new in Redis 8.2](/docs/latest/develop/whats-new/8-2/) and review the Redis Open Source [8.2 release notes](/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.2-release-notes/).

## Breaking changes

When new versions of Redis Open Source change existing commands, upgrading your database to a new version can potentially break some functionality. Before you upgrade, read the provided list of breaking changes that affect Redis Cloud and update any applications that connect to your database to handle these changes.

If you are upgrading from Redis 7.4, review the [Redis 8.0 breaking changes](/docs/latest/operate/rc/changelog/version-release-notes/8-0/#breaking-changes) before upgrading.

### Terraform compatibility limitation

If you use the [Redis Cloud Terraform provider](/docs/latest/integrate/terraform-provider-for-redis-cloud/) versions 2.1.2 through 2.4.5 with Redis 8.2 databases, database creation will fail. This issue only affects the Terraform provider and does not impact existing databases or data.

To resolve this issue, upgrade to the [latest supported version](https://registry.terraform.io/providers/RedisLabs/rediscloud/latest) and run `terraform init -upgrade`.

## On this page
