---
title: "NRedisStack guide (C#/.NET)"
source: "https://redis.io/docs/latest/develop/clients/dotnet/"
canonical_url: "https://redis.io/docs/latest/develop/clients/dotnet/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:25.380Z"
content_hash: "520da75a4efc5f53c6be5ce7acbfaaa8798d67a43d9c406b99e09e6539530afe"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        NRedisStack guide (C#/.NET)","→","NRedisStack guide (C#/.NET)"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        NRedisStack guide (C#/.NET)","→","NRedisStack guide (C#/.NET)"]
nav_prev: {"path": "redis/docs/latest/develop/ai/redisvl/user_guide/llmcache/index.md", "title": "LLM Caching"}
nav_next: {"path": "redis/docs/latest/develop/ai/redisvl/overview/index.md", "title": "Overview"}
---

# NRedisStack guide (C#/.NET)

Connect your .NET application to a Redis database

[NRedisStack](https://github.com/redis/NRedisStack) is the .NET client for Redis. The sections below explain how to install `NRedisStack` and connect your application to a Redis database.

`NRedisStack` requires a running Redis server. See [here](/docs/latest/operate/oss_and_stack/install/) for Redis Open Source installation instructions.

You can also access Redis with an object-mapping client interface. See [Redis OM for .NET](/docs/latest/integrate/redisom-for-net/) for more information.

## Install

Using the `dotnet` CLI, run:

```bash
dotnet add package NRedisStack
```

## Connect and test

Add the following imports to your source file:

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class SyncLandingExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        db.StringSet("foo", "bar");
        Console.WriteLine(db.StringGet("foo")); // >>> bar

        var hash = new HashEntry[] {
            new HashEntry("name", "John"),
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
        };
        db.HashSet("user-session:123", hash);

        var hashFields = db.HashGetAll("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class AsyncLandingExample
{
    public async Task Run()
    {
        var muxer = await ConnectionMultiplexer.ConnectAsync("localhost:6379");
        var db = muxer.GetDatabase();

        await db.StringSetAsync("foo", "bar");
        string? fooResult = await db.StringGetAsync("foo");
        Console.WriteLine(fooResult); // >>> bar

        var hash = new HashEntry[] { 
            new HashEntry("name", "John"), 
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
            };
        await db.HashSetAsync("user-session:123", hash);

        var hashFields = await db.HashGetAllAsync("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

Connect to localhost on port 6379. The client supports both synchronous and asynchronous commands.

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class SyncLandingExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        db.StringSet("foo", "bar");
        Console.WriteLine(db.StringGet("foo")); // >>> bar

        var hash = new HashEntry[] {
            new HashEntry("name", "John"),
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
        };
        db.HashSet("user-session:123", hash);

        var hashFields = db.HashGetAll("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class AsyncLandingExample
{
    public async Task Run()
    {
        var muxer = await ConnectionMultiplexer.ConnectAsync("localhost:6379");
        var db = muxer.GetDatabase();

        await db.StringSetAsync("foo", "bar");
        string? fooResult = await db.StringGetAsync("foo");
        Console.WriteLine(fooResult); // >>> bar

        var hash = new HashEntry[] { 
            new HashEntry("name", "John"), 
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
            };
        await db.HashSetAsync("user-session:123", hash);

        var hashFields = await db.HashGetAllAsync("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

You can test the connection by storing and retrieving a simple string.

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class SyncLandingExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        db.StringSet("foo", "bar");
        Console.WriteLine(db.StringGet("foo")); // >>> bar

        var hash = new HashEntry[] {
            new HashEntry("name", "John"),
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
        };
        db.HashSet("user-session:123", hash);

        var hashFields = db.HashGetAll("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class AsyncLandingExample
{
    public async Task Run()
    {
        var muxer = await ConnectionMultiplexer.ConnectAsync("localhost:6379");
        var db = muxer.GetDatabase();

        await db.StringSetAsync("foo", "bar");
        string? fooResult = await db.StringGetAsync("foo");
        Console.WriteLine(fooResult); // >>> bar

        var hash = new HashEntry[] { 
            new HashEntry("name", "John"), 
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
            };
        await db.HashSetAsync("user-session:123", hash);

        var hashFields = await db.HashGetAllAsync("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

Store and retrieve a HashMap.

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class SyncLandingExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        db.StringSet("foo", "bar");
        Console.WriteLine(db.StringGet("foo")); // >>> bar

        var hash = new HashEntry[] {
            new HashEntry("name", "John"),
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
        };
        db.HashSet("user-session:123", hash);

        var hashFields = db.HashGetAll("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

```c#
using NRedisStack;
using NRedisStack.RedisStackCommands;
using StackExchange.Redis;

public class AsyncLandingExample
{
    public async Task Run()
    {
        var muxer = await ConnectionMultiplexer.ConnectAsync("localhost:6379");
        var db = muxer.GetDatabase();

        await db.StringSetAsync("foo", "bar");
        string? fooResult = await db.StringGetAsync("foo");
        Console.WriteLine(fooResult); // >>> bar

        var hash = new HashEntry[] { 
            new HashEntry("name", "John"), 
            new HashEntry("surname", "Smith"),
            new HashEntry("company", "Redis"),
            new HashEntry("age", "29"),
            };
        await db.HashSetAsync("user-session:123", hash);

        var hashFields = await db.HashGetAllAsync("user-session:123");
        Console.WriteLine(String.Join("; ", hashFields));
        // >>> name: John; surname: Smith; company: Redis; age: 29
    }
}

```

## Redis Open Source modules

To access Redis Open Source capabilities, use the appropriate interface like this:

```cs
IBloomCommands bf = db.BF();
ICuckooCommands cf = db.CF();
ICmsCommands cms = db.CMS();
IGraphCommands graph = db.GRAPH();
ITopKCommands topk = db.TOPK();
ITdigestCommands tdigest = db.TDIGEST();
ISearchCommands ft = db.FT();
IJsonCommands json = db.JSON();
ITimeSeriesCommands ts = db.TS();
```

## More information

See the other pages in this section for more information and examples.

## On this page

