---
title: "Redis search tools"
source: "https://redis.io/docs/latest/integrate/google-adk/search-tools/"
canonical_url: "https://redis.io/docs/latest/integrate/google-adk/search-tools/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:59.885Z"
content_hash: "3f7b1884980a2f7a7745b0ef80a02de5d3ec0f8821a24b96b3b982162da8efcf"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        Redis search tools","→","Redis search tools"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis with Google Agent Development Kit (ADK)","→","Redis with Google Agent Development Kit (ADK)","→\n      \n        Redis search tools","→","Redis search tools"]
---
# Redis search tools

Vector, hybrid, text, and range search tools for Google ADK agents.

adk-redis provides four search tools that wrap [RedisVL](/docs/latest/develop/ai/redisvl/) query types into ADK-compatible tools. The LLM sees each tool as a callable function with a `query` parameter and gets back structured results.

## Overview

Tool

Query type

Use case

`RedisVectorSearchTool`

KNN vector similarity

Conceptual/semantic queries

`RedisHybridSearchTool`

Vector + BM25

Queries with specific terms + concepts

`RedisTextSearchTool`

BM25 keyword

Exact terms, error messages, IDs

`RedisRangeSearchTool`

Distance threshold

Exhaustive retrieval within a radius

## Vector search

Embeds the query using a vectorizer and performs K-nearest-neighbor search.

```python
from redisvl.index import SearchIndex
from redisvl.utils.vectorize import HFTextVectorizer
from adk_redis import RedisVectorSearchTool, RedisVectorQueryConfig

vectorizer = HFTextVectorizer(model="redis/langcache-embed-v2")
index = SearchIndex.from_existing("products", redis_url="redis://localhost:6379")

vector_tool = RedisVectorSearchTool(
    index=index,
    vectorizer=vectorizer,
    config=RedisVectorQueryConfig(num_results=5),
    return_fields=["name", "description", "price"],
    name="search_products",
    description="Find products by semantic similarity.",
)
```

## Hybrid search

Combines vector similarity with BM25 keyword matching. Auto-detects whether your Redis server supports native hybrid search (Redis 8.4+ with RedisVL 0.13+). Falls back to client-side aggregation if not.

```python
from adk_redis import RedisHybridSearchTool, RedisHybridQueryConfig

hybrid_tool = RedisHybridSearchTool(
    index=index,
    vectorizer=vectorizer,
    config=RedisHybridQueryConfig(
        text_field_name="content",
        combination_method="LINEAR",
        linear_alpha=0.7,
    ),
    name="search_docs",
    description="Search documents using semantic and keyword matching.",
)
```

## Text search

Pure BM25 keyword search. No embeddings or vectorizer needed.

```python
from adk_redis import RedisTextSearchTool, RedisTextQueryConfig

text_tool = RedisTextSearchTool(
    index=index,
    config=RedisTextQueryConfig(
        text_field_name="content",
        text_scorer="BM25STD",
    ),
    return_fields=["title", "content"],
    name="keyword_search",
    description="Search for exact terms and phrases.",
)
```

## Range search

Returns all documents within a distance threshold instead of top-K. Useful for exhaustive retrieval.

```python
from adk_redis import RedisRangeSearchTool, RedisRangeQueryConfig

range_tool = RedisRangeSearchTool(
    index=index,
    vectorizer=vectorizer,
    config=RedisRangeQueryConfig(distance_threshold=0.5),
    return_fields=["title", "content"],
    name="range_search",
    description="Find all documents within a semantic distance threshold.",
)
```

## Multi-tool agent

Wire multiple search tools into a single agent and let the LLM choose the right one:

```python
from google.adk import Agent

agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    instruction=(
        "You have three search tools. Use search_products for conceptual "
        "queries, keyword_search for exact terms, range_search for "
        "exhaustive retrieval."
    ),
    tools=[vector_tool, text_tool, range_tool],
)
```

The `name` and `description` on each tool matter: the LLM reads them to decide which tool to call and when. Specific descriptions like "Find products by semantic similarity" work better than generic ones like "search documents".

## More info

*   [redis\_search\_tools example](https://github.com/redis-developer/adk-redis/tree/main/examples/redis_search_tools): All four search tools with a product catalog
*   [RedisVL documentation](/docs/latest/develop/ai/redisvl/)

## On this page
