## Overview

Redis is an in-memory data store used as a database, cache, message broker, and streaming engine. An agent needs to know it because it underpins real-time applications, vector search, and modern AI pipelines like RAG. Mastering Redis means understanding its commands, data types, modules, and operational tooling.

## Mental Model

Redis centers on a single-threaded event loop executing atomic commands against in-memory data structures, extended by modules and client libraries for vectors, streams, and JSON. All operations are key-based and command-driven, with persistence, replication, and clustering layered on top. Start with the command references (`redis/docs/latest/commands/redis-7-4-commands/index.md`), core data types (`redis/docs/latest/develop/data-types/json/path/index.md`), and the modules API (`redis/docs/latest/develop/reference/modules/index.md`) to internalize the architecture.

## Learning Paths

**Getting Started**
1. `redis/docs/latest/develop/get-started/rag/index.md`
2. `redis/docs/latest/integrate/redisvl/index.md`
3. `redis/docs/latest/develop/clients/nodejs/transpipe/index.md`

**Production Ready**
1. `redis/docs/latest/operate/redisinsight/configuration/index.md`
2. `redis/docs/latest/develop/clients/nodejs/amr/index.md`
3. `redis/docs/latest/integrate/redis-data-integration/index.md`

**Reference Deep-Dive**
1. `redis/docs/latest/commands/redis-7-4-commands/index.md`
2. `redis/docs/latest/develop/reference/command-tips/index.md`
3. `redis/docs/latest/develop/reference/modules/index.md`
4. `redis/docs/latest/develop/reference/modules/modules-native-types/index.md`
5. `redis/docs/latest/develop/reference/modules/modules-blocking-ops/index.md`

## Concept Map

- Commands & Reference
  - redis commands used
    - `redis/docs/latest/commands/redis-7-4-commands/index.md`
    - `redis/docs/latest/commands/redis-8-2-commands/index.md`
    - `redis/docs/latest/develop/reference/command-tips/index.md`
  - why atomicity matters
    - `redis/docs/latest/develop/clients/nodejs/transpipe/index.md`
- Data & Model
  - data model
    - `redis/docs/latest/develop/data-types/json/path/index.md`
  - create index
    - `redis/docs/latest/develop/get-started/rag/index.md`
  - load data
    - `redis/docs/latest/integrate/redis-data-integration/index.md`
- Getting Started
  - overview
    - `redis/docs/latest/integrate/redisvl/index.md`
  - getting started
    - `redis/docs/latest/develop/get-started/rag/index.md`
  - key features
    - `redis/docs/latest/integrate/redis-data-integration/index.md`
  - why use redis
    - `redis/docs/latest/develop/get-started/rag/index.md`
- Clients & Connectivity
  - installation / install
    - `redis/docs/latest/develop/clients/nodejs/amr/index.md`
  - how it works
    - `redis/docs/latest/develop/clients/nodejs/transpipe/index.md`
    - `redis/docs/latest/develop/clients/nodejs/amr/index.md`
  - prerequisites
    - `redis/docs/latest/develop/clients/nodejs/amr/index.md`
- Modules & Scripting
  - the lua script / script breakdown
    - `redis/docs/latest/develop/reference/modules/index.md`
  - modules api reference
    - `redis/docs/latest/develop/reference/modules/modules-api-ref/index.md`
    - `redis/docs/latest/develop/reference/modules/modules-native-types/index.md`
    - `redis/docs/latest/develop/reference/modules/modules-blocking-ops/index.md`
- Operations & Tooling
  - highlights / details
    - `redis/docs/latest/develop/tools/insight/release-notes/v.2.68.0/index.md`
  - configuration
    - `redis/docs/latest/operate/redisinsight/configuration/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Look up core commands | `redis/docs/latest/commands/redis-7-4-commands/index.md` |
| Build a RAG/vector application | `redis/docs/latest/develop/get-started/rag/index.md` |
| Run pipelines or transactions | `redis/docs/latest/develop/clients/nodejs/transpipe/index.md` |
| Query JSON with JSONPath | `redis/docs/latest/develop/data-types/json/path/index.md` |
| Connect to Azure Managed Redis | `redis/docs/latest/develop/clients/nodejs/amr/index.md` |
| Write a custom module | `redis/docs/latest/develop/reference/modules/index.md` |
| Handle blocking module commands | `redis/docs/latest/develop/reference/modules/modules-blocking-ops/index.md` |
| Register native module types | `redis/docs/latest/develop/reference/modules/modules-native-types/index.md` |
| Configure Redis Insight | `redis/docs/latest/operate/redisinsight/configuration/index.md` |
| Replicate data from external sources | `redis/docs/latest/integrate/redis-data-integration/index.md` |
| Use vector search clients | `redis/docs/latest/integrate/redisvl/index.md` |
| Review command routing policies | `redis/docs/latest/develop/reference/command-tips/index.md` |

## Top Must-Know Pages

1. `redis/docs/latest/commands/redis-7-4-commands/index.md` — Canonical reference for Redis commands including strings, hashes, lists, and sets.
2. `redis/docs/latest/develop/get-started/rag/index.md` — Describes Redis as a vector database for Retrieval Augmented Generation and AI workloads.
3. `redis/docs/latest/develop/clients/nodejs/transpipe/index.md` — Demonstrates pipeline execution, transactions, and key watching for optimistic concurrency.
4. `redis/docs/latest/develop/data-types/json/path/index.md` — Defines JSONPath syntax and query patterns for the Redis JSON data type.
5. `redis/docs/latest/develop/reference/modules/index.md` — Covers module loading, initialization, cleanup, and writing the simplest custom module.
6. `redis/docs/latest/integrate/redisvl/index.md` — Overview of RedisVL features and getting started with vector search in Redis.
7. `redis/docs/latest/integrate/redis-data-integration/index.md` — Explains supported source databases, features, and when to use Redis Data Integration.
8. `redis/docs/latest/develop/clients/nodejs/amr/index.md` — Walks through installing the Node.js client and authenticating with Azure Managed Redis.
9. `redis/docs/latest/operate/redisinsight/configuration/index.md` — Reference for Redis Insight environment variables and preconfigured database connections.
10. `redis/docs/latest/develop/reference/command-tips/index.md` — Catalogs command metadata flags such as nondeterministic_output and request_policy.