---
title: "Redis Software and Redis Open Source feature compatibility"
source: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/enterprise-capabilities/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/enterprise-capabilities/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:12:16.483Z"
content_hash: "abf114d04170e8b3a92ee12e7ced89c7038788c2d3eaba51363e8b354ed94642"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Redis Software and Redis Open Source feature compatibility","→","Redis Software and Redis Open Source feature compatibility"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Redis Software and Redis Open Source feature compatibility","→","Redis Software and Redis Open Source feature compatibility"]
nav_prev: {"path": "redis/docs/latest/operate/rc/databases/create-database/create-flex-database/index.md", "title": "Create a Flex database"}
nav_next: {"path": "redis/docs/latest/integrate/write-behind/installation/index.md", "title": "Installation"}
---

# Redis Software and Redis Open Source feature compatibility

Describes the Redis Software features supported by each Redis Open Source feature.

This article describes compatibility between Redis Software features and Redis Open Source features. Version numbers indicate the minimum module version required for feature support.

## Supported Redis Open Source features

The following table shows which Redis Open Source features are supported by Redis Software and Redis Cloud.

Feature

Redis  
Software

Redis  
Cloud

[Search and query](/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/)

✅ Supported

✅ Supported

[JSON](/docs/latest/operate/oss_and_stack/stack-with-enterprise/json/)

✅ Supported

✅ Supported

[Time series](/docs/latest/operate/oss_and_stack/stack-with-enterprise/timeseries/)

✅ Supported

✅ Supported

[Probabilistic](/docs/latest/operate/oss_and_stack/stack-with-enterprise/bloom/)

✅ Supported

✅ Supported

[Gears](/docs/latest/operate/oss_and_stack/stack-with-enterprise/gears-v1/)

✅ Supported

❌ Not supported

[Triggers and functions](/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/)

⚠️ Deprecated

⚠️ Deprecated

[Graph](/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/graph/)

⚠️ Deprecated

⚠️ Deprecated

## Feature compatibility

The following tables show Redis Software feature support for each Redis Open Source feature.

Version numbers indicate when the feature was first supported. If you're using an earlier version than what's shown in the table, the feature is not supported.

For details about individual features, see the corresponding documentation.

Feature name/capability

[Search and query](/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/)

[JSON](/docs/latest/operate/oss_and_stack/stack-with-enterprise/json/)

Active-Active (CRDB)[1](#fn:1)

Yes (v2.0)

Yes (v2.2)

Backup/Restore

Yes (v1.4)

Yes (v1.0)

Clustering

Yes (v1.6)[2](#fn:2)

Yes (v1.0)

Custom hashing policy

Yes (v2.0)

Yes (v1.0)

Eviction expiration

Yes (v2.0)

Yes (v1.0)

Failover/migration

Yes (v1.4)

Yes (v1.0)

Internode encryption

Yes (v2.0.11)

Yes (v1.0.8)

Module data types

Yes

Yes

Persistence (AOF)

Yes (v1.4)

Yes (v1.0)

Persistence (snapshot)

Yes (v1.6)

Yes (v1.0)

Auto Tiering [3](#fn:3)

Yes (v2.0)

Yes (v1.0)

Redis Flex

No

Yes (v8.0)

Replica Of

Yes (v1.6)[4](#fn:4)

Yes (v1.0)

Reshard/rebalance

Yes (v2.0)

Yes (v1.0)

Feature name/capability

[Time series](/docs/latest/operate/oss_and_stack/stack-with-enterprise/timeseries/)

[Probabilistic](/docs/latest/operate/oss_and_stack/stack-with-enterprise/bloom/)

[Gears](/docs/latest/operate/oss_and_stack/stack-with-enterprise/gears-v1/)

Active-Active (CRDB)[1](#fn:1)

No

No

Yes (v1.0)

Backup/Restore

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

Clustering

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

Custom hashing policy

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

Eviction expiration

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

Failover/migration

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

Internode encryption

Yes (v1.4.9)

Yes (v2.2.6)

Yes (v1.2)

Module data types

Yes

Yes

Yes

Persistence (AOF)

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

Persistence (snapshot)

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

Auto Tiering [3](#fn:3)

Yes (v1.6)[5](#fn:5)

Yes (vTBD)

Yes (vTBD)

Redis Flex

No

Yes (v8.0)

No

Replica Of

Yes (v1.2)

Yes (v2.0)

No

Reshard/rebalance

Yes (v1.2)

Yes (v2.0)

Yes (v1.0)

## Feature descriptions

The following table briefly describes each feature shown in the earlier tables.

Feature name/capability

Description

Active-Active (CRDB)

Compatible with Active-Active (CRDB) databases

Backup/Restore

Supports import and export features

Clustering

Compatible with sharded databases and shard migration

Custom hashing policy

Compatible with databases using custom hashing policies

Eviction expiration

Allows data to be evicted when the database reaches memory limits

Failover/migration

Compatible with primary/replica failover and the migration of shards between nodes within the cluster

Internode encryption

Compatible with encryption on the data plane

Persistence (AOF)

Compatible with databases using AoF persistence

Persistence (snapshot)

Compatible with databases using snapshot persistence

Auto Tiering

Compatible with Auto Tiering

Redis Flex

Compatible with Redis Flex

Replica Of

Compatible with Active-Passive replication

Reshard/rebalance

Compatible with database scaling for clustered databases, which redistributes data between the new shards.

## Footnotes

* * *

1.  With the exception of JSON, you currently cannot combine Active-Active with Redis Open Source features in Redis Cloud. [↩︎](#fnref:1) [↩︎](#fnref1:1)
    
2.  You cannot use search and query with the [OSS Cluster API](/docs/latest/operate/rs/databases/configure/oss-cluster-api/). This limitation was fixed in Redis Software version 8.0. [↩︎](#fnref:2)
    
3.  You currently cannot combine Auto Tiering with Redis Open Source features in Redis Cloud. [↩︎](#fnref:3) [↩︎](#fnref1:3)
    
4.  RediSearch version 1.6 supported Replica Of only between databases with the same number of shards. This limitation was fixed in v2.0. [↩︎](#fnref:4)
    
5.  Although time series are compatible with Auto Tiering, the entire series either lives in RAM or on flash. [↩︎](#fnref:5)
    

## On this page

