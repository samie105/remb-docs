---
title: "Redis for AI"
source: "https://redis.io/docs/latest/integrate/redis-ai-libraries/"
canonical_url: "https://redis.io/docs/latest/integrate/redis-ai-libraries/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:47.841Z"
content_hash: "4f989c2521f2b947fed87c57e38e2980192ff543ee51b47f2024a83c68375054"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis for AI","→","Redis for AI"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Redis for AI","→","Redis for AI"]
nav_prev: {"path": "redis/docs/latest/integrate/railway-redis/index.md", "title": "Redis on Railway"}
nav_next: {"path": "redis/docs/latest/integrate/redis-data-integration/index.md", "title": "Redis Data Integration"}
---

# Redis for AI

Build AI applications with Redis vector database and semantic caching

Build powerful AI applications using Redis as your vector database with specialized libraries for Python, JavaScript, and Java.

## Overview

Redis provides comprehensive AI libraries and tools to help you build intelligent applications with vector search, retrieval-augmented generation (RAG), semantic caching, and more. Whether you're working with LangChain, LlamaIndex, or building custom AI solutions, Redis has the tools you need.

[Explore the complete Redis for AI documentation](/docs/latest/develop/ai/)

## Key Features

*   **Vector Search**: Store and query vector embeddings with HNSW and FLAT index types
*   **Semantic Caching**: Cache LLM responses to reduce costs and improve performance
*   **RAG Support**: Build retrieval-augmented generation applications with popular frameworks
*   **Multi-language Support**: Libraries available for Python, JavaScript, and Java
*   **Real-time Performance**: Sub-millisecond query latency for production AI applications

## AI Libraries

### RedisVL (Python)

The Redis Vector Library (RedisVL) is a Python client library for building AI applications with Redis.

*   **Vector Search**: Create and query vector indexes with ease
*   **Semantic Caching**: Built-in LLM cache for faster responses
*   **RAG Utilities**: Tools for building retrieval-augmented generation apps
*   **Framework Integration**: Works with LangChain, LlamaIndex, and more

[Learn more about RedisVL](../../develop/ai/redisvl/index.md)

### LangChain Integration

Use Redis with LangChain for vector stores, semantic caching, and chat message history.

*   **Vector Store**: Store and retrieve embeddings for RAG applications
*   **Semantic Cache**: Cache LLM responses based on semantic similarity
*   **Chat History**: Persist conversation history for AI agents

[Learn more about LangChain integration](/docs/latest/integrate/langchain-redis/)

### Client Libraries with Vector Search

All major Redis client libraries support vector search operations:

*   **redis-py (Python)**: [Vector search guide](/docs/latest/develop/clients/redis-py/vecsearch/)
*   **node-redis (JavaScript)**: [Vector search guide](../../develop/clients/nodejs/vecsearch/index.md)
*   **Jedis (Java)**: [Vector search guide](../../develop/clients/jedis/vecsearch/index.md)
*   **NRedisStack (C#/.NET)**: [Vector search guide](/docs/latest/develop/clients/dotnet/vecsearch/)
*   **go-redis (Go)**: [Vector search guide](/docs/latest/develop/clients/go/vecsearch/)

## Getting Started

### Quick Start Guides

*   [Redis vector database quick start](../../develop/get-started/vector-database/index.md)
*   [RAG quick start guide](../../develop/get-started/rag/index.md)

### Tutorials and Examples

Explore our [AI notebooks collection](/docs/latest/develop/ai/notebook-collection/) with examples for:

*   RAG implementations with RedisVL, LangChain, and LlamaIndex
*   Advanced RAG techniques and optimizations
*   Integration with cloud platforms like Azure and Vertex AI

### Video Tutorials

Watch our [AI video collection](/docs/latest/develop/ai/ai-videos/) for practical demonstrations.

## Use Cases

*   **Retrieval-Augmented Generation (RAG)**: Enhance LLM responses with relevant context
*   **Semantic Search**: Find similar documents, images, or products
*   **Recommendation Systems**: Build real-time personalized recommendations
*   **AI Agents**: Create autonomous agents with memory and tool use
*   **Chatbots**: Build conversational AI with context and history

## Additional Resources

*   [Complete AI documentation](/docs/latest/develop/ai/)
*   [Ecosystem integrations](/docs/latest/develop/ai/ecosystem-integrations/)
*   [Vector search benchmarks](https://redis.io/blog/benchmarking-results-for-vector-databases/)
*   [RAG best practices](https://redis.io/blog/get-better-rag-responses-with-ragas/)

## On this page
