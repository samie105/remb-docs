---
title: "RedisInsight v2.6.0, July 2022"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.6.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.6.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:45.985Z"
content_hash: "b81f124499231ddad427bbd20cecb20c05a7a3106d81f96e56d36bba8915a9e7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.6.0, July 2022","→","RedisInsight v2.6.0, July 2022"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        RedisInsight v2.6.0, July 2022","→","RedisInsight v2.6.0, July 2022"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/install/install-stack/windows/index.md", "title": "Run Redis Open Source on Windows using Docker"}
nav_next: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-4-2-releases/7-4-2-2/index.md", "title": "Redis Enterprise for Kubernetes 7.4.2-2 (Feb 2024) release notes"}
---

# RedisInsight v2.6.0, July 2022

RedisInsight v2.6.0

## 2.6.0 (July 2022)

This is the General Availability (GA) release of RedisInsight 2.6.0

### Headlines:

*   Bulk actions: Delete the keys in bulk based on the filters set in Browser or Tree view
*   Multiline support for key values in Browser and Tree View: Click the key value to see it in full
*   [Pipeline](https://redis.io/docs/manual/pipelining/) support in Workbench: Batch Redis commands in Workbench to optimize round-trip times
*   In-app notifications: Receive messages about important changes, updates, or announcements inside the application. Notifications are always available in the Notification center, and can be displayed with or without preview.

### Details

**Features and improvements:**

*   [#890](https://github.com/RedisInsight/RedisInsight/pull/890), [#883](https://github.com/RedisInsight/RedisInsight/pull/883), [#875](https://github.com/RedisInsight/RedisInsight/pull/875) Delete keys in bulk from your Redis database in Browser and Tree view based on filters you set by key name or data type.
*   [#878](https://github.com/RedisInsight/RedisInsight/pull/878) Multiline support for key values in Browser and Tree View: Select the truncated value to expand the row and see the full value, select again to collapse it.
*   [#837](https://github.com/RedisInsight/RedisInsight/pull/837), [#838](https://github.com/RedisInsight/RedisInsight/pull/838) Added [pipeline](https://redis.io/docs/manual/pipelining/) support for commands run in Workbench to optimize round-trip times. Default number of commands sent in a pipeline is 5, and is configurable in Settings > Advanced.
*   [#862](https://github.com/RedisInsight/RedisInsight/pull/862), [#840](https://github.com/RedisInsight/RedisInsight/pull/840) Added in-app notifications to inform you about any important changes, updates, or announcements. Notifications are always available in the Notification center, and can be displayed with or without preview.
*   [#830](https://github.com/RedisInsight/RedisInsight/pull/830) To more easily explore and work with stream data, always display stream entry ID and controls to remove the Stream entry regardless of the number of fields.
*   [#928](https://github.com/RedisInsight/RedisInsight/pull/928) Remember the sorting on the list of databases.

**Bugs fixed:**

*   [#932](https://github.com/RedisInsight/RedisInsight/pull/932) Refresh the JSON value in Browser/Tree view.

## On this page


