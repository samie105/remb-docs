---
title: "Install Redis Stack from binaries"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/binaries/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-stack/binaries/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:15.516Z"
content_hash: "827910a6c39855f6064000267fccfd2f9c08140cca87ae5f17b531b4d201ecc1"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Install Redis Stack from binaries","→","Install Redis Stack from binaries"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Community Edition or Redis Stack","→","Install Redis Community Edition or Redis Stack","→\n      \n        Install Redis Stack","→","Install Redis Stack","→\n      \n        Install Redis Stack from binaries","→","Install Redis Stack from binaries"]
nav_prev: {"path": "redis/docs/latest/operate/rc/security/access-control/access-management/index.md", "title": "Access management"}
nav_next: {"path": "redis/docs/latest/develop/reference/clients/index.md", "title": "Redis client handling"}
---

# Install Redis Stack from binaries

How to install Redis Stack using tarballs

Redis Open Source

## Start Redis Stack Server

Install the openssl libraries for your platform. For example, on a Debian or Ubuntu instance run:

```bash
sudo apt install libssl-dev
```

After untarring or unzipping your redis-stack-server download, you can start Redis Stack Server as follows:

```bash
/path/to/redis-stack-server/bin/redis-stack-server
```

### Add the binaries to your PATH

You can add the redis-stack-server binaries to your `$PATH` as follows:

Open the file `~/.bashrc` or `~/zshrc` (depending on your shell), and add the following lines.

```bash
export PATH=/path/to/redis-stack-server/bin:$PATH
```

If you have an existing Redis installation on your system, then you can choose override those override those PATH variables as before, or you can choose to only add redis-stack-server binary as follows:

```bash
export PATH=/path/to/redis-stack-server/bin/redis-stack-server:$PATH
```

If you're running redis-stack-server on a mac, please ensure you have openssl installed, via [homebrew](https://brew.sh/).

Now you can start Redis Stack Server as follows:

```bash
redis-stack-server
```

## On this page


