---
title: "Redis session store"
source: "https://redis.io/docs/latest/develop/use-cases/session-store/"
canonical_url: "https://redis.io/docs/latest/develop/use-cases/session-store/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:27.860Z"
content_hash: "3295b6487201792c6330a560b9e42537fcb9f34c8e9bcac0e0d6468a1b2c0e0c"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Redis session store","→","Redis session store"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Redis session store","→","Redis session store"]
nav_prev: {"path": "redis/docs/latest/develop/use-cases/rate-limiter/rust/index.md", "title": "Token bucket rate limiter with Redis and Rust"}
nav_next: {"path": "redis/docs/latest/develop/use-cases/session-store/dotnet/index.md", "title": "Redis session store with .NET"}
---

# Redis session store

Store web sessions in Redis with cookie-based session IDs and TTL expiration

This guide family shows how to store web sessions in Redis so multiple application servers can share session state.

## Overview

A Redis-backed session store is a good fit when you need:

*   Shared session state across multiple web servers
*   Fast reads and writes for authenticated user state
*   Automatic session expiration after inactivity
*   A simple way to store lightweight user-specific data

The typical pattern is:

1.  Generate an opaque session ID
2.  Store the session data in Redis under a key such as `session:{id}`
3.  Send the session ID to the browser in a cookie
4.  Load the session from Redis on each request
5.  Refresh the TTL while the session stays active

## Available implementations

*   [redis-py](/docs/latest/develop/use-cases/session-store/redis-py/) - Build a Python session store and a local demo server using the standard library HTTP server
*   [Node.js](/docs/latest/develop/use-cases/session-store/nodejs/) - Build a Redis-backed session store with `node-redis` and a local Node.js demo server
*   [Go](/docs/latest/develop/use-cases/session-store/go/) - Build a Redis-backed session store with `go-redis` and a local Go demo server
*   [Java](/docs/latest/develop/use-cases/session-store/java-jedis/) - Build a Redis-backed session store with Jedis and a local Java demo server
*   [Java (Lettuce)](/docs/latest/develop/use-cases/session-store/java-lettuce/) - Build a Redis-backed session store with Lettuce using async and reactive APIs
*   [.NET](/docs/latest/develop/use-cases/session-store/dotnet/) - Build a Redis-backed session store with `StackExchange.Redis` and a local ASP.NET Core demo server
*   [PHP](/docs/latest/develop/use-cases/session-store/php/) - Build a Redis-backed session store with Predis and a local PHP demo server
*   [Ruby](/docs/latest/develop/use-cases/session-store/ruby/) - Build a Redis-backed session store with `redis-rb` and a local Ruby demo server
*   [Rust](/docs/latest/develop/use-cases/session-store/rust/) - Build a Redis-backed session store with `redis-rs`, including both sync and async APIs

## On this page
