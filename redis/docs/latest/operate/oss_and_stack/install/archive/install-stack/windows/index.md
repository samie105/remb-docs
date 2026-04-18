---
title: "Install Redis Stack on Windows"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/windows/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/windows/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:26.680Z"
content_hash: "23083a4a943a0f799213aa4f65dff21378a9a101b04065613f47682a0fea3cd5"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Install Redis Stack on Windows","→","Install Redis Stack on Windows"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Install Redis Stack on Windows","→","Install Redis Stack on Windows"]
nav_prev: {"path": "redis/docs/latest/develop/whats-new/8-4/index.md", "title": "Redis 8.4"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v2.12.0/index.md", "title": "RedisInsight v2.12.0, October 2022"}
---

# Install Redis Stack on Windows

How to install Redis Stack on Windows

Redis Open Source

## Run Redis on Windows using Memurai

Redis is now natively supported on Windows through [Memurai](https://www.memurai.com/), the official Redis partner for Windows compatibility.

## Run Redis on Windows using Docker

To install Redis Stack on Windows, you will need to have Docker installed. When Docker is up and running, open Windows PowerShell and follow the instructions described in [Run Redis Stack on Docker](/docs/latest/operate/oss_and_stack/install/install-stack/docker/). Then, use Docker to connect with `redis-cli` as explained in that topic.

About using WSL and Ubuntu for Windows :

If you attempt to use Windows Subsystem for Linux (WSL) or Ubuntu for Windows to follow [Linux instructions](/docs/latest/operate/oss_and_stack/install/install-stack/apt/), you will get a `systemd` error telling you `System has not been booted with systemd as init system (PID 1). Can't operate.` Do not fret. Just use Docker.

_`systemd` is a suite of basic building blocks for a Linux system._ For more information about its function, see [System and Service Manager](https://systemd.io/). This becomes an issue due to the lack of support for Linux workflows on WSL. But, you can test the instructions listed in [Systemd support is now available in WSL!](https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/). Let us know how that worked for you.

## On this page

