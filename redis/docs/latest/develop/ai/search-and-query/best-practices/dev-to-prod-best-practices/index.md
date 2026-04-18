---
title: "Move from Development to Production with Redis Search"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/best-practices/dev-to-prod-best-practices/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/best-practices/dev-to-prod-best-practices/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:08.988Z"
content_hash: "d4c51ad7335e4a3b2741d5d24393defcc60ebfc38aa782c884c3cc52531170de"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Best practices","→","Best practices","→\n      \n        Move from Development to Production with Redis Search","→","Move from Development to Production with Redis Search"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Best practices","→","Best practices","→\n      \n        Move from Development to Production with Redis Search","→","Move from Development to Production with Redis Search"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/best-practices/index.md", "title": "Best practices"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/best-practices/index-mgmt-best-practices/index.md", "title": "Index management best practices for Redis Search"}
---

# Move from Development to Production with Redis Search

Transitioning a Redis Open Source with Redis Search environment from development to production requires thoughtful consideration of configuration, performance tuning, and resource allocation. This guide outlines key practices to ensure your Redis deployment operates optimally under production workloads.

## Configuration parameter considerations

Redis Search offers several configurable parameters that influence query results and performance. While a full list of these parameters and their functions can be found [here](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/), this section highlights the most commonly adjusted parameters for production environments.

### 1\. `TIMEOUT`

*   Purpose: limits the duration a query is allowed to execute.
*   Default: 500 milliseconds.
*   Behavior:
    *   Ensures that queries do not monopolize the main Redis thread.
    *   If a query exceeds the `TIMEOUT` value, its outcome is determined by the `ON_TIMEOUT` setting:
        *   `FAIL`: the query will return an error.
        *   `PARTIAL`: this setting will return the top results accumulated by the query until it timed out.
*   Recommendations:
    *   Caution: be mindful when increasing `TIMEOUT`, as long-running queries can degrade overall system performance.

### 2\. `MINPREFIX`

*   Purpose: sets the minimum number of characters required for wildcard searches.
*   Default: 2 characters.
*   Behavior:
    *   Queries like `he*` are valid, while `h*` would not meet the threshold.
*   Recommendations:
    *   Lowering this value to 1 can significantly increase result sets, which may lead to degraded performance.
    *   Keep the default unless there is a strong use case for single-character wildcards.

### 3\. `MAXPREFIXEXPANSIONS`

*   Purpose: Defines the maximum number of expansions for a wildcard query term.
*   Default: 200 expansions.
*   Behavior:
    *   Expansions: when a wildcard query term is processed, Redis generates a list of all possible matches from the index that satisfy the wildcard. For example, the query he\* might expand to terms like hello, hero, and heat. Each of these matches is an "expansion."
    *   This parameter limits how many of these expansions Redis will generate and process. If the number of possible matches exceeds the limit, the query may return incomplete results or fail, depending on the query context.
*   Recommendations:
    *   Avoid increasing this parameter excessively, as it can lead to performance bottlenecks during query execution.
    *   If wildcard searches are common, consider optimizing your index to reduce the reliance on large wildcard expansions.

### 4\. `DEFAULT_DIALECT`

*   Purpose: specifies the default query dialect used by [`FT.SEARCH`](/docs/latest/commands/ft.search/) and [`FT.AGGREGATE`](/docs/latest/commands/ft.aggregate/) commands.
*   Default: [Dialect 1](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/).
*   Recommendations:
    *   Update the default to [**Dialect 4**](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/#dialect-4) for better performance and access to advanced features.
    *   Individual commands can override this parameter if necessary, but setting a higher default ensures consistent performance across queries.

## Testing

### 1\. Correctness

*   Run a few test queries and check the results are what you expect.
*   Use the following tools to validate and debug:
    *   Redis CLI: use the [`MONITOR`](/docs/latest/commands/monitor/) command or [profiling features](/docs/latest/develop/tools/insight/#profiler) in Redis Insight to analyze commands.
    *   [`FT.PROFILE`](/docs/latest/commands/ft.profile/): Provides detailed insights into individual query execution paths, helping identify bottlenecks and inefficiencies.

### 2\. Performance

*   Test query performance in a controlled test environment that mirrors production as closely as possible.
*   Use tools like `memtier_benchmark` or custom test applications to simulate load.
*   Network Considerations:
    *   Minimize latency during testing by locating test clients in the same network as the Redis instance.
    *   For Redis Cloud, ensure test machines are in a **VPC-peered environment** with the target Redis database.

## Sizing requirements

Redis Search has resource requirements distinct from general caching use cases. Proper sizing ensures that the system can handle production workloads efficiently.

### Key considerations:

1.  CPU:
    *   Adequate CPU resources are critical.
    *   Ensure CPUs are not over-subscribed with search threads and shard processes.
2.  RAM:
    *   Plan for sufficient memory to store the dataset and indexes, plus overhead for operations.
3.  Network:
    *   High throughput and low latency are essential, particularly for applications with demanding query patterns.

### Tools:

*   Use [Redis Search Sizing Calculator](https://redis.io/redisearch-sizing-calculator/) to estimate resource requirements based on your dataset and workload.

## Demand spikes

Production environments must be sized for peak load scenarios to ensure performance remains acceptable under maximum stress.

### Recommendations:

1.  Plan for Spikes:
    *   If query workloads are expected to vary significantly, ensure the infrastructure can handle peak loads.
    *   Monitor real-world usage patterns and adjust capacity as needed.
2.  Autoscaling:
    *   Consider using autoscaling strategies in cloud environments to dynamically adjust resources based on load.

By following these best practices, you can ensure a smooth and efficient transition from development to production with Redis Open Source and Redis Search. Proper configuration, rigorous testing, and careful resource planning are critical to delivering a reliable and high-performance Redis deployment.

## On this page
