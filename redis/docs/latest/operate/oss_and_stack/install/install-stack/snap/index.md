---
title: "Install Redis Open Source on Linux"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/snap/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/snap/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:31.018Z"
content_hash: "ecc753e1a57b0d3d6fee02a69b6816cd6315977a27510a2a21419bba661eb065"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source on Linux","→","Install Redis Open Source on Linux"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source on Linux","→","Install Redis Open Source on Linux"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/install/install-stack/rpm/index.md", "title": "Install Redis Open Source on Linux"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/install/install-stack/windows/index.md", "title": "Run Redis Open Source on Windows using Docker"}
---

# Install Redis Open Source on Linux

How to install Redis Open Source using Snap

Redis Open Source

## Install Redis Open Source on Ubuntu Linux using Snap

To install Redis via snap, run the following commands:

```bash
sudo apt update
sudo apt install redis-tools # this will install `redis-cli`
sudo snap install redis
```

Redis will start automatically after installation and also at boot time.

## Connect to Redis

Once Redis is running, you can test it by running `redis-cli`:

```bash
redis-cli
```

Test the connection with the `ping` command:

```bash
127.0.0.1:6379> PING
PONG
```

## On this page
