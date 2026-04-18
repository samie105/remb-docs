---
title: "Index and query documents"
source: "https://redis.io/docs/latest/develop/clients/lettuce/queryjson/"
canonical_url: "https://redis.io/docs/latest/develop/clients/lettuce/queryjson/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:36.019Z"
content_hash: "fed9f8c6a3a3dd6d9f6c4bd5d481476c3fafc4fd5eb64a8349e92c960a5fd38b"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Lettuce guide (Java)","→","Lettuce guide (Java)","→\n      \n        Index and query documents","→","Index and query documents"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Lettuce guide (Java)","→","Lettuce guide (Java)","→\n      \n        Index and query documents","→","Index and query documents"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/administration/gc/index.md", "title": "Garbage collection"}
nav_next: {"path": "redis/docs/latest/develop/data-types/json/indexing_json/index.md", "title": "Index/Search JSON documents"}
---

# Index and query documents

Learn how to use Redis Search with JSON and hash documents.

This example shows how to create a [search index](/docs/latest/develop/ai/search-and-query/indexing/) for [JSON](/docs/latest/develop/data-types/json/) documents and run queries against the index. It then goes on to show the slight differences in the equivalent code for [hash](/docs/latest/develop/data-types/hashes/) documents.

## Initialize

Make sure that you have [Redis Open Source](/docs/latest/operate/oss_and_stack/) or another Redis server available. Also install the [Lettuce](/docs/latest/develop/clients/lettuce/) client library if you haven't already done so.

Add the following dependencies. All of them are applicable to both JSON and hash, except for the `JsonParser`, `JsonPath`, and `JsonObject` classes.

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

## Create data

Create some test data to add to the database:

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

## Add the index

Connect to your Redis database. The code below shows the most basic connection but see [Connect to the server](/docs/latest/develop/clients/lettuce/connect/) to learn more about the available connection options.

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](/docs/latest/develop/ai/search-and-query/query/).

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

## Add the data

Add the three sets of user data to the database as [JSON](/docs/latest/develop/data-types/json/) objects. If you use keys with the `user:` prefix then Redis will index the objects automatically as you add them:

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

## Query the data

You can now use the index to search the JSON objects. The [query](/docs/latest/develop/ai/search-and-query/query/) below searches for objects that have the text "Paul" in any field and have an `age` value in the range 30 to 40:

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

Specify query options to return only the `city` field:

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

Use an [aggregation query](/docs/latest/develop/ai/search-and-query/query/aggregation/) to count all users in each city.

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you need to specify some slightly different options.

When you create the schema for a hash index, you don't need to add aliases for the fields, since you use the basic names to access the fields. Also, you must use `CreateArgs.TargetType.HASH` for the `On()` option of `CreateArgs` when you create the index. The code below shows these changes with a new index called `hash-idx:users`, which is otherwise the same as the `idx:users` index used for JSON documents in the previous examples.

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

Use [`hset()`](/docs/latest/commands/hset/) to add the hash documents instead of [`jsonSet()`](/docs/latest/commands/json.set/).

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

The query commands work the same here for hash as they do for JSON (but the name of the hash index is different). The results are returned in a `List` of `SearchReply.SearchResult<String, String>` objects, as with JSON:

```java
package io.redis.examples.async;

import io.lettuce.core.*;

import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.async.RediSearchAsyncCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            RediSearchAsyncCommands<String, String> searchCommands = connection.async();
            // ...

            JsonParser parser = asyncCommands.getJsonParser();

            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            CompletableFuture<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            make_index.join();

            CompletableFuture<String> addUser1 = asyncCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser2 = asyncCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<String> addUser3 = asyncCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addUser1, addUser2, addUser3).join();

            CompletableFuture<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();
            CompletableFuture<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                        return res;
                    }).toCompletableFuture();

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();
            CompletableFuture<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .thenApply(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(query1, query2, query3).join();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            CompletableFuture<Void> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema)
                    .thenAccept(System.out::println) // >>> OK
                    .toCompletableFuture();
            makeHashIndex.join();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            CompletableFuture<Long> addHashUser1 = asyncCommands.hset("huser:1", huser1).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser2 = asyncCommands.hset("huser:2", huser2).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();

            CompletableFuture<Long> addHashUser3 = asyncCommands.hset("huser:3", huser3).thenApply(r -> {
                System.out.println(r); // >>> OK
                return r;
            }).toCompletableFuture();
            CompletableFuture.allOf(addHashUser1, addHashUser2, addHashUser3).join();

            CompletableFuture<SearchReply<String, String>> query1Hash = searchCommands
                    .ftSearch("hash-idx:users", "Paul @age:[30 40]").thenApply(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                        return res;
                    }).toCompletableFuture();
            query1Hash.join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
package io.redis.examples.reactive;

import io.lettuce.core.*;

import io.lettuce.core.api.reactive.RedisReactiveCommands;
import io.lettuce.core.api.reactive.RediSearchReactiveCommands;
import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.arguments.AggregateArgs.*;
import io.lettuce.core.search.SearchReply;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.json.JsonPath;

import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class HomeJsonExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            RediSearchReactiveCommands<String, String> searchCommands = connection.reactive();
            // ...

            JsonParser parser = reactiveCommands.getJsonParser();
            JsonObject user1 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul John\""))
                    .put("email", parser.createJsonValue("\"paul.john@example.com\"")).put("age", parser.createJsonValue("42"))
                    .put("city", parser.createJsonValue("\"London\""));

            JsonObject user2 = parser.createJsonObject().put("name", parser.createJsonValue("\"Eden Zamir\""))
                    .put("email", parser.createJsonValue("\"eden.zamir@example.com\"")).put("age", parser.createJsonValue("29"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            JsonObject user3 = parser.createJsonObject().put("name", parser.createJsonValue("\"Paul Zamir\""))
                    .put("email", parser.createJsonValue("\"paul.zamir@example.com\"")).put("age", parser.createJsonValue("35"))
                    .put("city", parser.createJsonValue("\"Tel Aviv\""));

            List<FieldArgs<String>> schema = Arrays.asList(TextFieldArgs.<String> builder().name("$.name").as("name").build(),
                    NumericFieldArgs.<String> builder().name("$.age").as("age").build(),
                    TagFieldArgs.<String> builder().name("$.city").as("city").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("user:").build();

            Mono<Void> make_index = searchCommands.ftCreate("idx:users", createArgs, schema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).then();
            make_index.block();

            Mono<String> addUser1 = reactiveCommands.jsonSet("user:1", JsonPath.ROOT_PATH, user1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser2 = reactiveCommands.jsonSet("user:2", JsonPath.ROOT_PATH, user2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<String> addUser3 = reactiveCommands.jsonSet("user:3", JsonPath.ROOT_PATH, user3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addUser1, addUser2, addUser3).block();

            Mono<SearchReply<String, String>> query1 = searchCommands.ftSearch("idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> user:3
                    });

            SearchArgs<String, String> query2Args = SearchArgs.<String, String> builder().returnField("city").build();

            Mono<SearchReply<String, String>> query2 = searchCommands.ftSearch("idx:users", "Paul", query2Args)
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.printf("ID: %s, City: %s\n", result.getId(), result.getFields().get("city"));
                        });
                        // >>> ID: user:1, City: London
                        // >>> ID: user:3, City: Tel Aviv
                    });

            AggregateArgs<String, String> aggArgs = AggregateArgs.<String, String> builder()
                    .groupBy(GroupBy.<String, String> of("@city").reduce(Reducer.<String, String> count().as("count"))).build();

            Mono<AggregationReply<String, String>> query3 = searchCommands.ftAggregate("idx:users", "*", aggArgs)
                    .doOnNext(res -> {
                        List<SearchReply<String, String>> replies = res.getReplies();
                        replies.forEach(reply -> {
                            reply.getResults().forEach(result -> {
                                System.out.printf("City: %s, Count: %s\n", result.getFields().get("city"),
                                        result.getFields().get("count"));
                            });
                            // >>> City: London, Count: 1
                            // >>> City: Tel Aviv, Count: 2
                        });
                    });

            Mono.when(query1, query2, query3).block();

            List<FieldArgs<String>> hashSchema = Arrays.asList(TextFieldArgs.<String> builder().name("name").build(),
                    NumericFieldArgs.<String> builder().name("age").build(),
                    TagFieldArgs.<String> builder().name("city").build());

            CreateArgs<String, String> hashCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.HASH)
                    .withPrefix("huser:").build();

            Mono<String> makeHashIndex = searchCommands.ftCreate("hash-idx:users", hashCreateArgs, hashSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            });
            makeHashIndex.block();

            Map<String, String> huser1 = new HashMap<>();
            huser1.put("name", "Paul John");
            huser1.put("email", "paul.john@example.com");
            huser1.put("age", "42");
            huser1.put("city", "London");

            Map<String, String> huser2 = new HashMap<>();
            huser2.put("name", "Eden Zamir");
            huser2.put("email", "eden.zamir@example.com");
            huser2.put("age", "29");
            huser2.put("city", "Tel Aviv");

            Map<String, String> huser3 = new HashMap<>();
            huser3.put("name", "Paul Zamir");
            huser3.put("email", "paul.zamir@example.com");
            huser3.put("age", "35");
            huser3.put("city", "Tel Aviv");

            Mono<Long> addHashUser1 = reactiveCommands.hset("huser:1", huser1).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser2 = reactiveCommands.hset("huser:2", huser2).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });

            Mono<Long> addHashUser3 = reactiveCommands.hset("huser:3", huser3).doOnNext(r -> {
                System.out.println(r); // >>> OK
            });
            Mono.when(addHashUser1, addHashUser2, addHashUser3).block();

            Mono<SearchReply<String, String>> query1Hash = searchCommands.ftSearch("hash-idx:users", "Paul @age:[30 40]")
                    .doOnNext(res -> {
                        List<SearchReply.SearchResult<String, String>> results = res.getResults();

                        results.forEach(result -> {
                            System.out.println(result.getId());
                        });
                        // >>> huser:3
                    });
            query1Hash.block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

## More information

See the [Redis Search](/docs/latest/develop/ai/search-and-query/) docs for a full description of all query features with examples.

## On this page

