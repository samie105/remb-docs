# Redis Documentation SKILL.md

## Overview

Redis is an in-memory data store widely used as a database, cache, message broker, and search engine. It delivers performance, flexibility, and a broad set of features for storing, querying, and processing data with sub-millisecond latency at scale.

---

## Key Concepts

- **Data Structures:** Redis natively supports strings, hashes, lists, sets, sorted sets, streams, bitmaps, hyperloglogs, and geospatial indexes.
- **Persistence:** Data is preserved through snapshotting (RDB) and command appending (AOF).
- **Pub/Sub & Streams:** Enables event-driven and real-time architectures via publish/subscribe and log-like stream features.
- **Clustering & Replication:** Built-in capabilities for high-availability and horizontal scaling.
- **Modules & Extensions:** Extensible system for AI/search (e.g., RedisVL), triggers, time series, and more.
- **Security:** Includes access control lists, TLS, and authentication.
- **Client Libraries & Tools:** Broad language support and GUI/admin tooling (e.g., Redis Insight).
- **Command Reference:** Versioned, detailed documentation of every Redis command per release.

---

## Documentation Navigation Guide

### If you need…
- **Quickstarts / Installation:**  
  Start in the "Quick starts" or "Redis products" sections for setup on your OS or cloud.
- **Command syntax or behavior:**  
  Go directly to the versioned "Commands" pages matching your Redis deployment.
- **Developing applications or using client libraries:**  
  See "Develop with Redis" for language guides, best practices, and use case patterns.
- **Using Redis for AI, Search, or advanced features:**  
  Explore "Develop with Redis" → "Redis for AI and search" (including RedisVL).
- **Integrating with frameworks/tools:**  
  Check "Libraries and tools" for plugins, integrations, and third-party clients.
- **Operations, Monitoring, Security:**  
  "Redis products" sub-sections—installation, monitoring, and security pages.
- **Gotchas or deprecated features:**  
  Some deprecated and special features are nested deep under "Redis products" (e.g., triggers).

**Tip:** Some features (especially AI/Search/Triggers) are documented under "Develop with Redis" (for code) and "Redis products" (for deployment/management)—if you can't find a concept under one, check the other.

---

## Top 15 Most Important Pages

1. **[Install Redis Open Source on Linux](redis/docs/latest/operate/oss_and_stack/install/install-stack/apt/index.md)**  
   How to install Redis on Linux systems via APT.

2. **[Docker quickstart for Redis Software](redis/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart/index.md)**  
   Instructions for running Redis using Docker—fastest way to experiment locally.

3. **[Redis Software quickstart](redis/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart/index.md)**  
   Get started with Redis Software Enterprise quickly on any platform.

4. **[Redis 8.6 Commands Reference](redis/docs/latest/commands/redis-8-6-commands/index.md)**  
   Most current, full command reference for Redis 8.6.

5. **[Redis 8.4 Commands Reference](redis/docs/latest/commands/redis-8-4-commands/index.md)**  
   Access command documentation for Redis 8.4 (or reference [other versions](#versioned-command-references) below).

6. **[Access control](redis/docs/latest/operate/rs/security/access-control/index.md)**  
   Securing your Redis instance: authentication, users, and permissions.

7. **[Get started with monitoring Redis Software](redis/docs/latest/operate/rs/monitoring/get-started/index.md)**  
   Setting up and using Redis monitoring, metrics, and alerts.

8. **[redis-rs guide (Rust)](redis/docs/latest/develop/clients/rust/index.md)**  
   Official guide to using Redis from Rust.

9. **[Rust client for Redis](redis/docs/latest/integrate/rust-redis/index.md)**  
   High-level integration steps for Rust clients beyond basic usage.

10. **[Manage streams and consumer groups in Redis Insight](redis/docs/latest/develop/tools/insight/insight-stream-consumer/index.md)**  
    Using Redis Insight's GUI for advanced stream/consumer group management.

11. **[RedisVL (Vectors & AI)](redis/docs/latest/develop/ai/redisvl/index.md)**  
    Core documentation for Redis Vector Library (VL) for similarity search and AI/ML integration.

12. **[Overview (RedisVL)](redis/docs/latest/develop/ai/redisvl/overview/index.md)**  
    Quick conceptual overview of how RedisVL fits into the Redis ecosystem.

13. **[Install RedisVL](redis/docs/latest/develop/ai/redisvl/install/index.md)**  
    Step-by-step install guide for vector search.

14. **[RedisVL API](redis/docs/latest/develop/ai/redisvl/api/index.md)**  
    Programmatic reference for vector operations in RedisVL.

15. **[Range queries (AI & Search)](redis/docs/latest/develop/ai/search-and-query/query/range/index.md)**  
    How to perform advanced range queries in Redis-based search/AI modules.

---

#### Versioned Command References (Pick the version matching your deployment)

- [Redis 6.2 Commands Reference](redis/docs/latest/commands/redis-6-2-commands/index.md)
- [Redis 7.2 Commands Reference](redis/docs/latest/commands/redis-7-2-commands/index.md)
- [Redis 7.4 Commands Reference](redis/docs/latest/commands/redis-7-4-commands/index.md)
- [Redis 8.0 Commands Reference](redis/docs/latest/commands/redis-8-0-commands/index.md)
- [Redis 8.2 Commands Reference](redis/docs/latest/commands/redis-8-2-commands/index.md)
- [Redis 8.4 Commands Reference](redis/docs/latest/commands/redis-8-4-commands/index.md)
- [Redis 8.6 Commands Reference](redis/docs/latest/commands/redis-8-6-commands/index.md)

---

## Notable Gotchas & Doc Structure Quirks

- **Versioned Command Docs:** Redis commands are documented per version. Always use the reference that matches your runtime for complete and accurate command/parameter information.
- **Module/Feature Overlap:** Features like AI, Search, or Triggers may have docs both under "Develop with Redis" (for APIs, code, patterns) and "Redis products" (for deployment, configuration, and management).
- **Some features deprecated:** Docs for deprecated or legacy features (like triggers) can be deeply nested, e.g., under `...deprecated-features...`.
- **Language Clients:** For client libraries, there are sometimes two guides: one in "Develop with Redis" (for in-depth usage) and "Integrate" (for quick setup/reference).
- **Tooling/GUI:** Management and GUI tools (like Redis Insight) have their own sub-sections under both "Develop with Redis" and "Libraries and tools".
- **Use Cases:** Practical patterns (like session storage) are under "Develop with Redis" → "Redis use cases".

---

## See Also

- **[New Relic with Redis Software](redis/docs/latest/integrate/new-relic-with-redis-enterprise/index.md):**  
  Integration guide for using Redis with New Relic for advanced monitoring.
- **[Keyspace triggers (deprecated)](redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/triggers/keyspace_triggers/index.md):**  
  For advanced or migration use cases involving legacy triggers.
- **[Redis session store with Rust](redis/docs/latest/develop/use-cases/session-store/rust/index.md):**  
  Example-driven resource for using Redis as a session store in Rust applications.

---

For deeper dives, always use the section most closely related to your goal (setup, client development, deployment, or feature/module), and select the right Redis version when referencing commands or APIs.