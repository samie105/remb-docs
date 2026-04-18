---
title: "node-redis guide (JavaScript)"
source: "https://redis.io/docs/latest/develop/clients/nodejs/"
canonical_url: "https://redis.io/docs/latest/develop/clients/nodejs/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:30.254Z"
content_hash: "f2a983bd73d6bd7e6890fcddf9f0967e516450bb028a431d0a8b49b82b3ab7e5"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        node-redis guide (JavaScript)","→","node-redis guide (JavaScript)"]
nav_prev: {"path": "redis/docs/latest/develop/use-cases/session-store/java-jedis/index.md", "title": "Redis session store with Java and Jedis"}
nav_next: {"path": "redis/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/index.md", "title": "Plan Redis Software deployment"}
---

# node-redis guide (JavaScript)

Connect your Node.js/JavaScript application to a Redis database

[`node-redis`](https://github.com/redis/node-redis) is the Redis client for Node.js/JavaScript. The sections below explain how to install `node-redis` and connect your application to a Redis database.

Note:

node-redis is the recommended client library for Node.js/JavaScript, but we also support and document our older JavaScript client [`ioredis`](/docs/latest/develop/clients/ioredis/). See [Migrate from ioredis](/docs/latest/develop/clients/nodejs/migration/) if you are interested in converting an existing `ioredis` project to `node-redis`.

`node-redis` requires a running Redis server. See [here](/docs/latest/operate/oss_and_stack/install/) for Redis Open Source installation instructions.

You can also access Redis with an object-mapping client interface. See [RedisOM for Node.js](/docs/latest/integrate/redisom-for-node-js/) for more information.

## Install

To install node-redis, run:

```bash
npm install redis
```

## Connect and test

Connect to localhost on port 6379.

```node.js
import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
console.log(value); // >>> value

await client.hSet('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
})

let userSession = await client.hGetAll('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

await client.quit();
```

Store and retrieve a simple string.

```node.js
import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
console.log(value); // >>> value

await client.hSet('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
})

let userSession = await client.hGetAll('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

await client.quit();
```

Store and retrieve a map.

```node.js
import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
console.log(value); // >>> value

await client.hSet('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
})

let userSession = await client.hGetAll('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

await client.quit();
```

To connect to a different host or port, use a connection string in the format `redis[s]://[[username][:password]@][host][:port][/db-number]`:

```js
createClient({
  url: 'redis://alice:foobared@awesome.redis.server:6380'
});
```

To check if the client is connected and ready to send commands, use `client.isReady`, which returns a Boolean. `client.isOpen` is also available. This returns `true` when the client's underlying socket is open, and `false` when it isn't (for example, when the client is still connecting or reconnecting after a network error).

When you have finished using a connection, close it with `client.quit()`.

```node.js
import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
console.log(value); // >>> value

await client.hSet('user-session:123', {
    name: 'John',
    surname: 'Smith',
    company: 'Redis',
    age: 29
})

let userSession = await client.hGetAll('user-session:123');
console.log(JSON.stringify(userSession, null, 2));
/* >>>
{
  "surname": "Smith",
  "name": "John",
  "company": "Redis",
  "age": "29"
}
 */

await client.quit();
```

## More information

The [`node-redis` website](https://redis.js.org/) has more examples. The [Github repository](https://github.com/redis/node-redis) also has useful information, including a guide to the [connection configuration options](https://github.com/redis/node-redis/blob/master/docs/client-configuration.md) you can use.

See also the other pages in this section for more information and examples:

## On this page

