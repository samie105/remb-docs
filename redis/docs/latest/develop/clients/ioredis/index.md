---
title: "ioredis guide (JavaScript)"
source: "https://redis.io/docs/latest/develop/clients/ioredis/"
canonical_url: "https://redis.io/docs/latest/develop/clients/ioredis/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:42.069Z"
content_hash: "816da457726edf84251e1d4448185fbe1f7b4faeed0db6ab8fc089e0cf88aa9d"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        ioredis guide (JavaScript)","→","ioredis guide (JavaScript)"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        ioredis guide (JavaScript)","→","ioredis guide (JavaScript)"]
nav_prev: {"path": "redis/docs/latest/develop/clients/hiredis/issue-commands/index.md", "title": "Issue commands"}
nav_next: {"path": "redis/docs/latest/develop/clients/jedis/index.md", "title": "Jedis guide (Java)"}
---

# ioredis guide (JavaScript)

Connect your Node.js/JavaScript application to a Redis database

[`ioredis`](https://github.com/redis/ioredis) is a Redis client for Node.js/JavaScript. The sections below explain how to install `ioredis` and connect your application to a Redis database.

Note:

Redis actively maintains and supports `ioredis` since it is in widespread use, but for new projects, we recommend using our newer Node.js client [`node-redis`](/docs/latest/develop/clients/nodejs/). See [Migrate from ioredis](/docs/latest/develop/clients/nodejs/migration/) if you are interested in converting an existing `ioredis` project to `node-redis`.

`ioredis` requires a running Redis server. See [here](/docs/latest/operate/oss_and_stack/install/) for Redis Open Source installation instructions.

## Install

To install `ioredis`, run:

```bash
npm install ioredis
```

## Connect and test

Connect to localhost on port 6379.

```node.js
import { Redis } from 'ioredis';

const redis = new Redis();

await redis.set('key', 'value');
const value = await redis.get('key');
console.log(value); // >>> value

await redis.hset('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
});

const userSession = await redis.hgetall('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

redis.disconnect();
```

Store and retrieve a simple string.

```node.js
import { Redis } from 'ioredis';

const redis = new Redis();

await redis.set('key', 'value');
const value = await redis.get('key');
console.log(value); // >>> value

await redis.hset('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
});

const userSession = await redis.hgetall('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

redis.disconnect();
```

Store and retrieve a map.

```node.js
import { Redis } from 'ioredis';

const redis = new Redis();

await redis.set('key', 'value');
const value = await redis.get('key');
console.log(value); // >>> value

await redis.hset('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
});

const userSession = await redis.hgetall('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

redis.disconnect();
```

When you have finished using a connection, close it with `client.quit()`.

```node.js
import { Redis } from 'ioredis';

const redis = new Redis();

await redis.set('key', 'value');
const value = await redis.get('key');
console.log(value); // >>> value

await redis.hset('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
});

const userSession = await redis.hgetall('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

redis.disconnect();
```

## More information

The [Github repository](https://github.com/redis/ioredis) has useful information, including [API docs](https://redis.github.io/ioredis/index.html) and a set of [code examples](https://github.com/redis/ioredis/tree/main/examples).

## On this page
