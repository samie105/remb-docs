---
title: "Use cases"
source: "https://redis.io/docs/latest/develop/data-types/json/use_cases/"
canonical_url: "https://redis.io/docs/latest/develop/data-types/json/use_cases/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:45.275Z"
content_hash: "8b671ff3850fdd24ed066c77c460f189ddb341890665c1b79a7d60211299e1c7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis data types","→","Redis data types","→\n      \n        JSON","→","JSON","→\n      \n        Use cases","→","Use cases"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis data types","→","Redis data types","→\n      \n        JSON","→","JSON","→\n      \n        Use cases","→","Use cases"]
nav_prev: {"path": "redis/docs/latest/develop/data-types/json/resp3/index.md", "title": "Guide for migrating from RESP2 to RESP3 replies"}
nav_next: {"path": "redis/docs/latest/develop/data-types/probabilistic/hyperloglogs/index.md", "title": "HyperLogLog"}
---

# Use cases

JSON use cases

You can of course use Redis native data structures to store JSON objects, and that's a common practice. For example, you can serialize JSON and save it in a Redis String.

However, Redis JSON provides several benefits over this approach.

**Access and retrieval of subvalues**

With JSON, you can get nested values without having to transmit the entire object over the network. Being able to access sub-objects can lead to greater efficiencies when you're storing large JSON objects in Redis.

**Atomic partial updates**

JSON allows you to atomically run operations like incrementing a value, adding, or removing elements from an array, append strings, and so on. To do the same with a serialized object, you have to retrieve and then reserialize the entire object, which can be expensive and also lack atomicity.

**Indexing and querying**

When you store JSON objects as Redis strings, there's no good way to query those objects. On the other hand, storing these objects as JSON using Redis Open Source lets you index and query them. This capability is provided by Redis Search.
