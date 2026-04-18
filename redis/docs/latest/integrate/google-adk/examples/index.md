---
title: "adk-redis examples"
source: "https://redis.io/docs/latest/integrate/google-adk/examples/"
canonical_url: "https://redis.io/docs/latest/integrate/google-adk/examples/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:03:05.745Z"
content_hash: "5959196a99fda1b94eb8260690d8e02d3c47fb5830bf15172620de19c16392f2"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        adk-redis examples","→","adk-redis examples"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        adk-redis examples","→","adk-redis examples"]
nav_prev: {"path": "redis/docs/latest/integrate/go-redis/index.md", "title": "Go client for Redis"}
nav_next: {"path": "redis/docs/latest/integrate/google-adk/integration-patterns/index.md", "title": "Memory integration patterns"}
---

# adk-redis examples

Complete examples for every adk-redis capability.

The [adk-redis repository](https://github.com/redis-developer/adk-redis/tree/main/examples) includes seven complete examples. Each focuses on a specific capability.

## Prerequisites

All examples require:

*   **Python 3.10+**
*   **Redis 8.4+**: `docker run -d --name redis -p 6379:6379 redis:8.4-alpine`
*   **Agent Memory Server** (for memory examples): See [setup instructions](https://github.com/redis/agent-memory-server)
*   **API keys**: Most examples need a `GOOGLE_API_KEY` for Gemini

## `simple_redis_memory`

**Capability:** Redis Agent Memory (framework-managed)

Minimal starting point. Wires up `RedisWorkingMemorySessionService` and `RedisLongTermMemoryService` with a basic conversational agent. No search tools, no caching: just memory.

[View on GitHub](https://github.com/redis-developer/adk-redis/tree/main/examples/simple_redis_memory)

## `travel_agent_memory_hybrid`

**Capability:** Redis Agent Memory + REST tools + web search + planning

The most complete example. Combines framework-managed memory services with LLM-controlled memory tools, web search, itinerary planning, and calendar export. Demonstrates the [hybrid integration pattern](/docs/latest/integrate/google-adk/integration-patterns/#hybrid-approach).

[View on GitHub](https://github.com/redis-developer/adk-redis/tree/main/examples/travel_agent_memory_hybrid)

## `travel_agent_memory_tools`

**Capability:** REST memory tools (LLM-controlled)

Uses REST-based memory tools exclusively, without framework-managed services. The LLM has full control over when to search, create, update, and delete memories.

[View on GitHub](https://github.com/redis-developer/adk-redis/tree/main/examples/travel_agent_memory_tools)

## `fitness_coach_mcp`

**Capability:** MCP memory tools

Demonstrates MCP-based memory integration. The agent connects to the Agent Memory Server via SSE and manages semantic and episodic memories for workout tracking.

[View on GitHub](https://github.com/redis-developer/adk-redis/tree/main/examples/fitness_coach_mcp)

## `redis_search_tools`

**Capability:** Vector, hybrid, text, and range search

All four RedisVL [search tools](/docs/latest/integrate/google-adk/search-tools/) plugged into a single agent with a product catalog dataset.

[View on GitHub](https://github.com/redis-developer/adk-redis/tree/main/examples/redis_search_tools)

## `semantic_cache`

**Capability:** Local semantic caching (RedisVL)

Demonstrates LLM response caching and tool result caching using the `RedisVLCacheProvider` with local embeddings and ADK callbacks.

[View on GitHub](https://github.com/redis-developer/adk-redis/tree/main/examples/semantic_cache)

## `langcache_cache`

**Capability:** Managed semantic caching (LangCache)

Uses the managed [LangCache](/docs/latest/integrate/google-adk/semantic-caching/) service for semantic caching with server-side embeddings. No local vectorizer required.

[View on GitHub](https://github.com/redis-developer/adk-redis/tree/main/examples/langcache_cache)

## Running an example

```bash
pip install adk-redis[all]
cd examples/simple_redis_memory
export GOOGLE_API_KEY=your-key
python main.py
```

## More info

*   [Car dealership tutorial](https://redis.io/tutorials/build-a-car-dealership-agent-with-google-adk-and-redis-agent-memory/): Full walkthrough building an agent from scratch
*   [adk-redis README](https://github.com/redis-developer/adk-redis): Installation and overview

## On this page
