---
title: "Spring Data Redis"
source: "https://redis.io/docs/latest/integrate/spring-framework-cache/"
canonical_url: "https://redis.io/docs/latest/integrate/spring-framework-cache/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:13:21.312Z"
content_hash: "d6a845f8df46139061dbefded9f81a4c9e51d6b1282ef420992b8279e10dbd29"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Spring Data Redis","→","Spring Data Redis"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        Spring Data Redis","→","Spring Data Redis"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/reference/signals/index.md", "title": "Redis signal handling"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/vectors/index.md", "title": "Vector search concepts"}
---

# Spring Data Redis

Plug Redis into your Spring application with minimal effort

Spring Data Redis implements the Spring framework's cache abstraction for Redis, which allows you to plug Redis into your Spring application with minimal effort.

Spring's cache abstraction applies cache-aside to methods, reducing executions by storing and reusing results. When a method is invoked, the abstraction checks if it's been called with the same arguments before. If so, it returns the cached result. If not, it invokes the method, caches the result, and returns it. This way, costly methods are invoked less often. Further details are in the [Spring cache abstraction documentation](https://docs.spring.io/spring-framework/reference/integration/cache.html).

## Get started

In a nutshell, you need to perform the following steps to use Redis as your cache storage:

1.  [Configure the cache storage](https://docs.spring.io/spring-framework/reference/integration/cache/store-configuration.html) by using the [Redis cache manager](https://docs.spring.io/spring-data/redis/reference/redis/redis-cache.html) that is part of Spring Data.
2.  Annotate a repository with your `@CacheConfig`.
3.  Use the `@Cachable` annotation on a repository method to cache the results of that method.

Here is an example:

```
@CacheConfig("books")
public class BookRepositoryImpl implements BookRepository {

    @Cacheable
    public Book findBook(ISBN isbn) {...}
}
```

## Further readings

Please read the Spring framework's documentation to learn more about how to use the Redis cache abstraction for Spring:

*   [Spring cache abstraction](https://docs.spring.io/spring-framework/reference/integration/cache.html)
*   [Spring cache store configuration](https://docs.spring.io/spring-framework/reference/integration/cache/store-configuration.html)
*   [Spring Data Redis Cache](https://docs.spring.io/spring-data/redis/reference/redis/redis-cache.html)

## On this page

