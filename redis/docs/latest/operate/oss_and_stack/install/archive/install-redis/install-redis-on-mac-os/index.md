---
title: "Install Redis on macOS"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-mac-os/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-mac-os/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:48.379Z"
content_hash: "42d41f869859427c03d17caa2be9b1204b4dd8c08be30c6d4179f6cd8f1b7381"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis","→","Install Redis","→\n      \n        Install Redis on macOS","→","Install Redis on macOS"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis","→","Install Redis","→\n      \n        Install Redis on macOS","→","Install Redis on macOS"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux/index.md", "title": "Install Redis on Linux"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-windows/index.md", "title": "Install Redis on Windows"}
---

# Install Redis on macOS

Use Homebrew to install and start Redis on macOS

Redis Open Source

This guide shows you how to install Redis on macOS using Homebrew. Homebrew is the easiest way to install Redis on macOS. If you'd prefer to build Redis from the source files on macOS, see [Installing Redis from Source](../install-redis-from-source/index.md).

Note:

The Homebrew distribution of Redis Open Source is only supported on macOS.

## Prerequisites

First, make sure you have Homebrew installed. From the terminal, run:

```bash
brew --version
```

If this command fails, you'll need to [follow the Homebrew installation instructions](https://brew.sh/).

## Installation

From the terminal, run:

```bash
brew install redis
```

This will install Redis on your system.

## Starting and stopping Redis in the foreground

To test your Redis installation, you can run the `redis-server` executable from the command line:

```bash
redis-server
```

If successful, you'll see the startup logs for Redis, and Redis will be running in the foreground.

To stop Redis, enter `Ctrl-C`.

### Starting and stopping Redis using launchd

As an alternative to running Redis in the foreground, you can also use `launchd` to start the process in the background:

```bash
brew services start redis
```

This launches Redis and restarts it at login. You can check the status of a `launchd` managed Redis by running the following:

```bash
brew services info redis
```

If the service is running, you'll see output like the following:

```bash
redis (homebrew.mxcl.redis)
Running: ✔
Loaded: ✔
User: miranda
PID: 67975
```

To stop the service, run:

```bash
brew services stop redis
```

## Connect to Redis

Once Redis is running, you can test it by running `redis-cli`:

```bash
redis-cli
```

Test the connection with the `ping` command:

```bash
127.0.0.1:6379> ping
PONG
```

You can also test that your Redis server is running using [Redis Insight](../../../../../../develop/tools/insight/index.md).

## Next steps

Once you have a running Redis instance, you may want to:

*   Try the [Redis CLI tutorial](../../../../../../develop/tools/cli/index.md)
*   Connect using one of the [Redis clients](/docs/latest/develop/clients/)
*   [Install Redis "properly"](../index.md#install-redis-properly) for production use.

## On this page
