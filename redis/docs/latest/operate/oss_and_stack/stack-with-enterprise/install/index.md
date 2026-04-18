---
title: "Install and upgrade modules"
source: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/install/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/install/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:42.522Z"
content_hash: "ebcb1b94be026209a71a5dece43af46abced0d252ea7dc13372569c33d04744b"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Install and upgrade modules","→","Install and upgrade modules"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Install and upgrade modules","→","Install and upgrade modules"]
---
# Install and upgrade modules

Several modules that provide additional Redis capabilities, such as search and query, JSON, time series, and probabilistic data structures, come packaged with [Redis Software](/docs/latest/operate/rs/). As of version 8.0, Redis Software includes multiple feature sets, compatible with different Redis database versions.

However, if you want to use additional modules or upgrade a module to a more recent version, you need to:

1.  [Install a module package](/docs/latest/operate/oss_and_stack/stack-with-enterprise/install/add-module-to-cluster/) on the cluster.
2.  [Enable a module](/docs/latest/operate/oss_and_stack/stack-with-enterprise/install/add-module-to-database/) for a new database or [upgrade a module](/docs/latest/operate/oss_and_stack/stack-with-enterprise/install/upgrade-module/) in an existing database.

## Automatically enabled capabilities in Redis 8

Databases created with or upgraded to Redis version 8 or later automatically enable the capabilities (modules) bundled with Redis Software as follows:

Database type

Automatically enabled capabilities

RAM-only

[Search and query](/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/)  
[JSON](/docs/latest/operate/oss_and_stack/stack-with-enterprise/json/)  
[Time series](/docs/latest/operate/oss_and_stack/stack-with-enterprise/timeseries/)  
[Probabilistic](/docs/latest/operate/oss_and_stack/stack-with-enterprise/bloom/)

Flash-enabled ([Redis Flex](/docs/latest/operate/rs/databases/flash/))

[JSON](/docs/latest/operate/oss_and_stack/stack-with-enterprise/json/)  
[Probabilistic](/docs/latest/operate/oss_and_stack/stack-with-enterprise/bloom/)

[Active-Active](/docs/latest/operate/rs/databases/active-active/)[1](#enabled-modules-table-note-1)

[Search and query](/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/search-active-active/)  
[JSON](/docs/latest/operate/oss_and_stack/stack-with-enterprise/json/)

1.  Upgrading existing Active-Active databases to Redis version 8 does not automatically enable these capabilities. Only new Active-Active databases created with Redis version 8 enable these capabilities by default.

## On this page
