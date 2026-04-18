---
title: "RedisInsight v2.2.0, May 2022"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v2.2.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v2.2.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:15:24.066Z"
content_hash: "b9ed730d84cca842e9904f95da8dcc1acffaf0305a6deed7d24b803424f11979"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.2.0, May 2022","→","RedisInsight v2.2.0, May 2022"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.2.0, May 2022","→","RedisInsight v2.2.0, May 2022"]
---
# RedisInsight v2.2.0, May 2022

RedisInsight v2.2.0

## 2.2.0 (May 2022)

This is the General Availability (GA) release of RedisInsight 2.2.0

### Headlines:

*   SlowLog: New tool based on results of the [Slowlog](https://redis.io/commands/slowlog/) command to analyze slow operations in Redis instances
*   Streams: Added support for [Redis Streams](https://redis.io/docs/manual/data-types/streams/)
*   Open the list of keys or key details in full screen
*   Automatically refresh the list of keys and key values with a timer

### Details

**Features and improvements:**

*   [#621](https://github.com/RedisInsight/RedisInsight/pull/621) , [#645](https://github.com/RedisInsight/RedisInsight/pull/645) , [#649](https://github.com/RedisInsight/RedisInsight/pull/649) Added SlowLog, a tool that displays the list of logs captured by the [Slowlog](https://redis.io/commands/slowlog/) command to analyze all commands that exceed a specified runtime, which helps in troubleshooting performance issues. Specify both the runtime and the maximum length of SlowLog (which are server configurations) to configure the list of commands logged and set the auto-refresh interval to automatically update the list of commands displayed.
*   [#597](https://github.com/RedisInsight/RedisInsight/pull/597) , [#598](https://github.com/RedisInsight/RedisInsight/pull/598), [#601](https://github.com/RedisInsight/RedisInsight/pull/601) , [#603](https://github.com/RedisInsight/RedisInsight/pull/603) , [#608](https://github.com/RedisInsight/RedisInsight/pull/608) , [#613](https://github.com/RedisInsight/RedisInsight/pull/613) , [#614](https://github.com/RedisInsight/RedisInsight/pull/614) , [#632](https://github.com/RedisInsight/RedisInsight/pull/632) Support for [Redis Streams](https://redis.io/docs/manual/data-types/streams/), including creation and deletion of Streams, addition and deletion of entries, and filtration of entries per timestamp. [Consumer groups](https://redis.io/docs/manual/data-types/streams/#consumer-groups) will be added in a future release.
*   [#643](https://github.com/RedisInsight/RedisInsight/pull/643) List of keys or key details are supported in full screen mode. To open the key list in full screen, close the key details. To open key details in full screen, use the new **Full Screen** control in key details section.
*   [#633](https://github.com/RedisInsight/RedisInsight/pull/633) Automatically refresh the list of keys and key values with a timer. To do so, enable the **Auto Refresh** mode by clicking the control next to the **Refresh** button and set the refresh rate.
*   [#634](https://github.com/RedisInsight/RedisInsight/pull/634) Removed the max value limitation in the **Database Index** field of the form for adding a new database.

**Bugs Fixed:**

*   [#656](https://github.com/RedisInsight/RedisInsight/pull/656) Binary key names will not trigger errors in databases with enabled OSS Cluster API. Data type, TTL, and size of such keys are displayed in the list of keys in all Redis instances. Key details are currently not available.

## On this page
