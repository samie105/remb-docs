---
title: "Install Redis on Windows"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-windows/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-windows/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:50.163Z"
content_hash: "fc00c19bb3456dd5473445908821cf7b7769e1d5b38f6ee824a853ecdaceb68c"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis","→","Install Redis","→\n      \n        Install Redis on Windows","→","Install Redis on Windows"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis","→","Install Redis","→\n      \n        Install Redis on Windows","→","Install Redis on Windows"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/management/security/encryption/index.md", "title": "TLS"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/triggers/user_functions/index.md", "title": "User functions"}
---

# Install Redis on Windows

Use Redis on Windows through Memurai, official Redis partner for Windows compatibility

Redis Open Source

## Run Redis on Windows using Memurai

Redis is now natively supported on Windows through [Memurai](https://www.memurai.com/), the official Redis partner for Windows compatibility.

## Run Redis on Windows using WSL (Windows Subsystem for Linux)

To install Redis on Windows using WSL, you'll first need to enable [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux). WSL2 lets you run Linux binaries natively on Windows. For this method to work, you'll need to be running Windows 10 version 2004 and higher or Windows 11.

### Install or enable WSL2

Microsoft provides [detailed instructions for installing WSL](https://docs.microsoft.com/en-us/windows/wsl/install). Follow these instructions, and take note of the default Linux distribution it installs. This guide assumes Ubuntu.

### Install Redis

Once you're running Ubuntu on Windows, you can follow the steps detailed at [Install on Ubuntu/Debian](/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux/#install-on-ubuntu-debian) to install recent stable versions of Redis from the official `packages.redis.io` APT repository. Add the repository to the `apt` index, update it, and then install:

```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

Lastly, start the Redis server like so:

```bash
redis-server --daemonize yes
```

### Connect to Redis

Once Redis is running, you can test it by running `redis-cli`:

```bash
redis-cli
```

Test the connection with the `ping` command:

```bash
127.0.0.1:6379> ping
PONG
```

You can also test that your Redis server is running using [Redis Insight](/docs/latest/develop/tools/insight/).

## Next steps

Once you have a running Redis instance, you may want to:

*   Try the [Redis CLI tutorial](/docs/latest/develop/tools/cli/)
*   Connect using one of the [Redis clients](/docs/latest/develop/clients/)
*   [Install Redis "properly"](/docs/latest/operate/oss_and_stack/install/archive/install-redis/#install-redis-properly) for production use.

## On this page
