---
title: "Redis leaderboard"
source: "https://redis.io/docs/latest/develop/use-cases/leaderboard/"
canonical_url: "https://redis.io/docs/latest/develop/use-cases/leaderboard/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:17.438Z"
content_hash: "dd0baf28d1d2879a31ff40b878e38cc98929031fedce1a89ca53f2822fdd6fb7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Redis leaderboard","→","Redis leaderboard"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis use cases","→","Redis use cases","→\n      \n        Redis leaderboard","→","Redis leaderboard"]
nav_prev: {"path": "redis/docs/latest/develop/programmability/lua-api/index.md", "title": "Redis Lua API reference"}
nav_next: {"path": "redis/docs/latest/develop/ai/redisvl/user_guide/llmcache/index.md", "title": "LLM Caching"}
---

# Redis leaderboard

Build ranked leaderboards with Redis sorted sets and user metadata

This guide family shows how to build a leaderboard with Redis sorted sets and per-user metadata.

## Overview

Leaderboards are a natural fit for Redis because sorted sets keep members ordered by score while still allowing fast updates and range queries.

This pattern works well when you need to:

*   Track scores for players, users, teams, or other ranked entities
*   Fetch the top `n` entries quickly
*   Show entries around a specific rank position
*   Keep only the highest-ranked entries, such as the top 100
*   Store richer user details separately from the ranking score

## Available implementations

*   [redis-py](/docs/latest/develop/use-cases/leaderboard/redis-py/) - Build a Python leaderboard with sorted sets, user metadata hashes, and a local interactive demo
*   [node-redis](/docs/latest/develop/use-cases/leaderboard/nodejs/) - Build a JavaScript leaderboard with sorted sets, user metadata hashes, and a local interactive demo
*   [go-redis](/docs/latest/develop/use-cases/leaderboard/go/) - Build a Go leaderboard with sorted sets, user metadata hashes, and a local interactive demo
*   [Jedis](/docs/latest/develop/use-cases/leaderboard/java-jedis/) - Build a Java leaderboard with sorted sets, user metadata hashes, and a local interactive demo
*   [Lettuce](/docs/latest/develop/use-cases/leaderboard/java-lettuce/) - Build async and reactive Java leaderboards with sorted sets, user metadata hashes, and a local interactive demo
*   [.NET](/docs/latest/develop/use-cases/leaderboard/dotnet/) - Build a C# leaderboard with sorted sets, user metadata hashes, and a local interactive demo
*   [Rust](/docs/latest/develop/use-cases/leaderboard/rust/) - Build sync and async Rust leaderboards with sorted sets, user metadata hashes, and a local interactive demo
*   [PHP](/docs/latest/develop/use-cases/leaderboard/php/) - Build a PHP leaderboard with sorted sets, user metadata hashes, and a local interactive demo
*   [Ruby](/docs/latest/develop/use-cases/leaderboard/ruby/) - Build a Ruby leaderboard with sorted sets, user metadata hashes, and a local interactive demo

## On this page
