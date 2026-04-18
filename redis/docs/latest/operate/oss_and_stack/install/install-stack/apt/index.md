---
title: "Install Redis Open Source on Linux"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/apt/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/apt/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:28.986Z"
content_hash: "b2a70af63f51e6a4e6762515acab13a19209448640eb56ff0107fd36cdaacffb"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source on Linux","→","Install Redis Open Source on Linux"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source on Linux","→","Install Redis Open Source on Linux"]
nav_prev: {"path": "redis/docs/latest/develop/reference/client-side-caching/index.md", "title": "Client-side caching reference"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/management/config/index.md", "title": "Redis configuration"}
---

# Install Redis Open Source on Linux

How to install Redis Open Source using APT

Redis Open Source

## Install Redis Open Source on Ubuntu or Debian Linux using APT

Add the repository to the APT index, update it, and install Redis Open Source:

```bash
sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis
```

The most recent version of Redis Open Source will be installed, along with the redis-tools package (redis-cli, etc.). If you need to install an earlier version, run the following command to list the available versions:

```bash
apt policy redis

redis:
  Installed: (none)
  Candidate: 6:8.6.1-1rl1~noble1
  Version table:
     6:8.6.1-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages
     6:8.6.0-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages
     ...
     6:8.0.0-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages
     6:7.4.8-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages
```

For example, to install Redis Open Source v7.4.8 on Ubuntu LTS 24.04 (Noble Numbat), run the following command:

```bash
sudo apt-get install \
redis=6:7.4.8-1rl1~noble1 \
redis-server=6:7.4.8-1rl1~noble1 \
redis-sentinel=6:7.4.8-1rl1~noble1 \
redis-tools=6:7.4.8-1rl1~noble1
```

Alternatively, you can also set up a preferences file to pin a particular release:

```bash
Package: redis redis-server redis-sentinel redis-tools
Pin: version 6:7.4.*
Pin-Priority: 1001
```

See [this document](https://manpages.debian.org/buster/apt/apt_preferences.5.en.html#How_APT_Interprets_Priorities) for more information on `Pin-Priority`.

With the example preferences file give above, `6:7.4.8-1rl1~noble1` is the latest version that matches the pinned version and it will be installed when you run this command:

```bash
sudo apt-get install redis-server redis-sentinel redis-tools
```

Redis should start automatically after the initial installation and also at boot time. Should that not be the case on your system, run the following commands:

```bash
sudo systemctl enable redis-server
sudo systemctl start redis-server
```

## On this page


