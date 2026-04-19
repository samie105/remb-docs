---
title: "Known limitations"
source: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/known_limitations/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/known_limitations/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:12:29.088Z"
content_hash: "0b301387344e5ce74eda77e7a2f8265c9394b2d53011491d47f4fc0959d28f70"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Known limitations","→","Known limitations"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Redis Open Source and Redis Software","→","Redis Open Source and Redis Software","→\n      \n        Deprecated Redis Open Source features and modules","→","Deprecated Redis Open Source features and modules","→\n      \n        Triggers and functions","→","Triggers and functions","→\n      \n        Known limitations","→","Known limitations"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/examples/index.md", "title": "Triggers and functions examples"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/quick_start_cli/index.md", "title": "Quick start using redis-cli"}
---

# Known limitations

Overview of the known limitations

Redis Open Source

Redis Software

Redis Cloud

Redis Open Source

Redis Enterprise for Kubernetes

clients

## Limited write options

JavaScript remote functions are limited to **read operations** only. Any attempt to perform a write operation of the following functions on a shard different than the one executing the function will result in an error.

*   `async_client.runOnShards` runs the remote function on all the shards
*   `async_client.runOnKey` runs the remote function on the shard responsible for a given key

In addition, keyspace modification performed by JavaScript functions that are registered using any of the methods available should perform write operations locally:

*   If the function is registered with `registerFunction` or `registerAsyncFunction`, it can insert, modify or delete keys that are in the same shard where the function is executed.
*   If the function is registered with `registerKeySpaceTrigger` or `registerStreamTrigger`, keyspace modification must be local to the shard that originated the events.

It is also recommended to co-locate the keys to be modified in the same hash slot as the key or Stream that originated the event. As an example, if the user profile stored in the Hash `myserv:user:1234` is subject to changes and we'd like to count them in an external counter, we would name the counter using hash tags: `{myserv:user:1234}:cnt`.

## Exclusive access to the keyspace

By design, asynchronous functions guarantee exclusive single-threaded access to the keyspace, the distinctive feature of Redis. In asynchronous programming with JavaScript functions, access to the keyspace in read or write mode must be blocking, while if not accessing the keyspace, the execution may be non-blocking. This implementation maintains the same level of data consistency as Redis standard commands or Lua scripts and functions but takes advantage of asynchronous execution, a feature of the JavaScript engine.

## JavaScript variables

Not all the JavaScript global variables are made available by the JavaScript engine loaded by Redis (e.g. `console`, `document`). The `redis` global variable can be used to manage functions registration, logging etc.

## Sandboxed

This feature is sandboxed, meaning, from within a function, it’s not possible to make calls to external services, including other Redis databases, or APIs.

## On this page
