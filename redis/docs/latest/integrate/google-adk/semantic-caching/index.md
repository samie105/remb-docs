---
title: "Semantic caching"
source: "https://redis.io/docs/latest/integrate/google-adk/semantic-caching/"
canonical_url: "https://redis.io/docs/latest/integrate/google-adk/semantic-caching/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:28.089Z"
content_hash: "b9dcb2d2ab39d2cdcbb79599b2b6b0bca622c008556cdde8338b0e01d6309f2a"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        Semantic caching","→","Semantic caching"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        Semantic caching","→","Semantic caching"]
nav_prev: {"path": "redis/docs/latest/integrate/google-adk/search-tools/index.md", "title": "Redis search tools"}
nav_next: {"path": "redis/docs/latest/integrate/hiredis/index.md", "title": "C client for Redis"}
---

# Semantic caching

Cache LLM responses and tool results using semantic similarity with Redis.

adk-redis provides semantic caching at two levels: LLM response caching and tool result caching, both backed by Redis. Caching uses ADK's callback system, so enabling it requires no changes to your agent's core logic.

## How it works

Before each LLM call (or tool execution), the cache checks whether a semantically similar prompt already exists in Redis. If so, the cached response is returned immediately. If not, the call proceeds and the response is stored for future lookups.

## Cache providers

Two backends are available:

Provider

Embeddings

Setup

Best for

`RedisVLCacheProvider`

Local (you provide vectorizer)

Self-managed Redis

Full control

`LangCacheProvider`

Server-side (managed)

API key from Redis Cloud

Zero embedding overhead

### RedisVL provider (local embeddings)

```python
from redisvl.utils.vectorize import HFTextVectorizer
from adk_redis.cache import RedisVLCacheProvider, RedisVLCacheProviderConfig

provider = RedisVLCacheProvider(
    config=RedisVLCacheProviderConfig(
        redis_url="redis://localhost:6379",
        name="my_cache",
        ttl=3600,
        distance_threshold=0.1,
    ),
    vectorizer=HFTextVectorizer(model="redis/langcache-embed-v1"),
)
```

### LangCache provider (managed)

No local vectorizer needed. Embeddings are generated server-side.

```python
from adk_redis.cache import LangCacheProvider, LangCacheProviderConfig

provider = LangCacheProvider(
    config=LangCacheProviderConfig(
        cache_id="your-cache-id",
        api_key="your-api-key",
        ttl=3600,
    )
)
```

## LLM response cache

Intercepts model calls through ADK's `before_model_callback` and `after_model_callback`.

```python
from adk_redis.cache import (
    LLMResponseCache,
    LLMResponseCacheConfig,
    create_llm_cache_callbacks,
)

llm_cache = LLMResponseCache(
    provider=provider,
    config=LLMResponseCacheConfig(
        first_message_only=True,
        include_app_name=True,
        include_user_id=True,
    ),
)

before_cb, after_cb = create_llm_cache_callbacks(llm_cache)

agent = Agent(
    name="cached_agent",
    model="gemini-2.0-flash",
    instruction="You are a helpful assistant.",
    before_model_callback=before_cb,
    after_model_callback=after_cb,
)
```

### Configuration notes

*   **`first_message_only=True`** caches only the first message in a session. Later messages depend on conversation context, making cache hits unreliable.
*   Function call responses and errors are automatically excluded from caching.
*   **`distance_threshold`** (set on the provider) controls how similar two prompts need to be for a cache hit. `0.0` = exact match only. `0.1` = small phrasing variations. Higher values risk returning wrong cached responses.

## Tool result cache

Caches tool executions using `before_tool_callback` and `after_tool_callback`.

```python
from adk_redis.cache import (
    ToolCache,
    ToolCacheConfig,
    create_tool_cache_callbacks,
)

tool_cache = ToolCache(
    provider=provider,
    config=ToolCacheConfig(
        tool_names={"web_search", "get_weather"},
    ),
)

before_tool_cb, after_tool_cb = create_tool_cache_callbacks(tool_cache)
```

The `tool_names` set specifies which tools to cache. Not all tools are idempotent: cache `get_weather` but not `send_email`.

## More info

*   [semantic\_cache example](https://github.com/redis-developer/adk-redis/tree/main/examples/semantic_cache): Local caching with RedisVL
*   [langcache\_cache example](https://github.com/redis-developer/adk-redis/tree/main/examples/langcache_cache): Managed caching with LangCache

## On this page
