---
title: "RedisInsight v2.18.0, January 2023"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.18.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.18.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:46.861Z"
content_hash: "c8481ad0fe0142788ee1b04d35fd591bfce9118db6281c09306d3b193b58afe3"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.18.0, January 2023","→","RedisInsight v2.18.0, January 2023"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.18.0, January 2023","→","RedisInsight v2.18.0, January 2023"]
---
# RedisInsight v2.18.0, January 2023

RedisInsight v2.18.0

## 2.18.0 (January 2023)

This is the General Availability (GA) release of RedisInsight 2.18.

### Highlights

*   Support for SSH tunnel to connect to your Redis database
*   Ability to switch between database indexes while connected to your database
*   Recommendations on how to optimize the usage of your database

### Details

**Features and improvements**

*   [#1567](https://github.com/RedisInsight/RedisInsight/pull/1567), [#1576](https://github.com/RedisInsight/RedisInsight/pull/1576), [#1577](https://github.com/RedisInsight/RedisInsight/pull/1577) Connect to your Redis database via SSH tunnel using a password or private key in PEM format.
*   [#1540](https://github.com/RedisInsight/RedisInsight/pull/1540), [#1608](https://github.com/RedisInsight/RedisInsight/pull/1608) Switch between database indexes while connected to your database in Browser, Workbench, and Database Analysis.
*   [#1457](https://github.com/RedisInsight/RedisInsight/pull/1457), [#1465](https://github.com/RedisInsight/RedisInsight/pull/1465), [#1590](https://github.com/RedisInsight/RedisInsight/pull/1590) Run Database Analysis to generate recommendations on how to save memory and optimize the usage of your database. These recommendations are based on industry standards and Redis best practices. Upvote or downvote recommendations in terms of their usefulness.
*   [#1598](https://github.com/RedisInsight/RedisInsight/pull/1598) Check and highlight the [JSON](https://redis.io/docs/stack/json/) syntax using new [Monaco Editor](https://microsoft.github.io/monaco-editor/).
*   [#1583](https://github.com/RedisInsight/RedisInsight/pull/1583) Click a pencil icon to make changes to database aliases.
*   [#1579](https://github.com/RedisInsight/RedisInsight/pull/1579) Increase the database password length limitation to 10,000.

## On this page
