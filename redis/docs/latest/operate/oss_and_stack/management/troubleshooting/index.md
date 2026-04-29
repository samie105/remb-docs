---
title: "Troubleshooting Redis"
source: "https://redis.io/docs/latest/operate/oss_and_stack/management/troubleshooting/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/management/troubleshooting/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:15:11.683Z"
content_hash: "642faff6f5f8dc122ed669404bf24d2eb28741d59f300967d6ff157ee81b78cb"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Manage Redis","→","Manage Redis","→\n      \n        Troubleshooting Redis","→","Troubleshooting Redis"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Manage Redis","→","Manage Redis","→\n      \n        Troubleshooting Redis","→","Troubleshooting Redis"]
nav_prev: {"path": "../sentinel/index.md", "title": "High availability with Redis Sentinel"}
nav_next: {"path": "../../reference/cluster-spec/index.md", "title": "Redis cluster specification"}
---

# Troubleshooting Redis

Problems with Redis? Start here.

Redis Open Source

This page tries to help you with what to do if you have issues with Redis. Part of the Redis project is helping people that are experiencing problems because we don't like to leave people alone with their issues.

*   If you have **latency problems** with Redis, that in some way appears to be idle for some time, read our [Redis latency troubleshooting guide](/docs/latest/operate/oss_and_stack/management/optimization/latency/).
*   Redis stable releases are usually very reliable, however in the rare event you are **experiencing crashes** the developers can help a lot more if you provide debugging information. Please read our [Debugging Redis guide](/docs/latest/operate/oss_and_stack/management/debugging/).
*   We have a long history of users experiencing crashes with Redis that actually turned out to be servers with **broken RAM**. Please test your RAM using **redis-server --test-memory** in case Redis is not stable in your system. Redis built-in memory test is fast and reasonably reliable, but if you can you should reboot your server and use [memtest86](http://memtest86.com).

For every other problem please drop a message to the [Redis Google Group](http://groups.google.com/group/redis-db). We will be glad to help.

You can also find assistance on the [Redis Discord server](https://discord.gg/redis).

### List of known critical bugs in Redis 3.0.x, 2.8.x and 2.6.x

To find a list of critical bugs please refer to the changelogs:

*   [Redis 3.0 Changelog](https://raw.githubusercontent.com/redis/redis/3.0/00-RELEASENOTES).
*   [Redis 2.8 Changelog](https://raw.githubusercontent.com/redis/redis/2.8/00-RELEASENOTES).
*   [Redis 2.6 Changelog](https://raw.githubusercontent.com/redis/redis/2.6/00-RELEASENOTES).

Check the _upgrade urgency_ level in each patch release to more easily spot releases that included important fixes.

### List of known Linux related bugs affecting Redis.

*   Ubuntu 10.04 and 10.10 contain [bugs](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/666211) that can cause performance issues. The default kernels shipped with these distributions are not recommended. Bugs were reported as having affected EC2 instances, but some users also cited server impact.
*   Certain versions of the Xen hypervisor report poor fork() performance. See [the latency page](/docs/latest/operate/oss_and_stack/management/optimization/latency/) for more information.

## On this page
