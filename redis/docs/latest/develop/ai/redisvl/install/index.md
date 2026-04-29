---
title: "Install RedisVL"
source: "https://redis.io/docs/latest/develop/ai/redisvl/install/"
canonical_url: "https://redis.io/docs/latest/develop/ai/redisvl/install/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:07.818Z"
content_hash: "3c5f780262368f224ac3d5e99ce00b00a3fca7e007a70563d25e6650a6985291"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        RedisVL","→","RedisVL","→\n      \n        Install RedisVL","→","Install RedisVL"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        RedisVL","→","RedisVL","→\n      \n        Install RedisVL","→","Install RedisVL"]
nav_prev: {"path": "../api/index.md", "title": "RedisVL API"}
nav_next: {"path": "../overview/index.md", "title": "Overview"}
---

# Install RedisVL

## Installation

Install the `redisvl` package into your Python (>=3.8) environment using the `pip` command:

```shell
pip install redisvl
```

Then make sure to have a Redis instance with the Redis Query Engine features enabled on Redis Cloud or locally in docker with Redis Stack:

```shell
docker run -d --name redis -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

After running the previous command, the Redis Insight GUI will be available at http://localhost:8001.

## On this page
