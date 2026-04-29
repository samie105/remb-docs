---
title: "Index and query documents"
source: "https://redis.io/docs/latest/develop/clients/jedis/queryjson/"
canonical_url: "https://redis.io/docs/latest/develop/clients/jedis/queryjson/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:17.010Z"
content_hash: "791bee5c42eec18e2720e5d69dfa7fa200d57efb870a57c9f1b48af45730c9c7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Jedis guide (Java)","→","Jedis guide (Java)","→\n      \n        Index and query documents","→","Index and query documents"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Connect with Redis client API libraries","→","Connect with Redis client API libraries","→\n      \n        Jedis guide (Java)","→","Jedis guide (Java)","→\n      \n        Index and query documents","→","Index and query documents"]
nav_prev: {"path": "../prob/index.md", "title": "Probabilistic data types"}
nav_next: {"path": "../transpipe/index.md", "title": "Pipelines and transactions"}
---

# Index and query documents

Learn how to use Redis Search with JSON and hash documents.

This example shows how to create a [search index](/docs/latest/develop/ai/search-and-query/indexing/) for [JSON](/docs/latest/develop/data-types/json/) documents and run queries against the index. It then goes on to show the slight differences in the equivalent code for [hash](/docs/latest/develop/data-types/hashes/) documents.

Note:

From [v6.0.0](https://github.com/redis/jedis/releases/tag/v6.0.0) onwards, `Jedis` uses query dialect 2 by default. Redis Search methods such as [`ftSearch()`](/docs/latest/commands/ft.search/) will explicitly request this dialect, overriding the default set for the server. See [Query dialects](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/) for more information.

## Initialize

Make sure that you have [Redis Open Source](/docs/latest/operate/oss_and_stack/) or another Redis server available. Also install the [Jedis](/docs/latest/develop/clients/jedis/) client library if you haven't already done so.

Add the following dependencies. All of them are applicable to both JSON and hash, except for the `Path` and `JSONObject` classes, which are specific to JSON (see [Path](/docs/latest/develop/data-types/json/path/) for a description of the JSON path syntax).

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

## Create data

Create some test data to add to the database:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

## Add the index

Connect to your Redis database. The code below shows the most basic connection but see [Connect to the server](/docs/latest/develop/clients/jedis/connect/) to learn more about the available connection options.

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

Delete any existing index called `idx:users` and any keys that start with `user:`.

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

Create an index. In this example, only JSON documents with the key prefix `user:` are indexed. For more information, see [Query syntax](/docs/latest/develop/ai/search-and-query/query/).

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

## Add the data

Add the three sets of user data to the database as [JSON](/docs/latest/develop/data-types/json/) objects. If you use keys with the `user:` prefix then Redis will index the objects automatically as you add them:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

## Query the data

You can now use the index to search the JSON objects. The [query](/docs/latest/develop/ai/search-and-query/query/) below searches for objects that have the text "Paul" in any field and have an `age` value in the range 30 to 40:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

Specify query options to return only the `city` field:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

Use an [aggregation query](/docs/latest/develop/ai/search-and-query/query/aggregation/) to count all users in each city.

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

## Differences with hash documents

Indexing for hash documents is very similar to JSON indexing but you need to specify some slightly different options.

When you create the schema for a hash index, you don't need to add aliases for the fields, since you use the basic names to access the fields anyway. Also, you must use `IndexDataType.HASH` for the `On()` option of `FTCreateParams` when you create the index. The code below shows these changes with a new index called `hash-idx:users`, which is otherwise the same as the `idx:users` index used for JSON documents in the previous examples.

First, delete any existing index called `hash-idx:users` and any keys that start with `huser:`.

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

Now create the new index:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

Use [`hset()`](/docs/latest/commands/hset/) to add the hash documents instead of [`jsonSet()`](/docs/latest/commands/json.set/).

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

The query commands work the same here for hash as they do for JSON (but the name of the hash index is different). The results are returned in a `List` of `Document` objects, as with JSON:

```java
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HomeJsonExample {

    public void run() {

        JSONObject user1 = new JSONObject()
                .put("name", "Paul John")
                .put("email", "paul.john@example.com")
                .put("age", 42)
                .put("city", "London");
        
        JSONObject user2 = new JSONObject()
                .put("name", "Eden Zamir")
                .put("email", "eden.zamir@example.com")
                .put("age", 29)
                .put("city", "Tel Aviv");
        
        JSONObject user3 = new JSONObject()
                .put("name", "Paul Zamir")
                .put("email", "paul.zamir@example.com")
                .put("age", 35)
                .put("city", "Tel Aviv");

        RedisClient jedis = new RedisClient("redis://localhost:6379");

        try {jedis.ftDropIndex("idx:users");} catch (JedisDataException j){}
        jedis.del("user:1", "user:2", "user:3");

        SchemaField[] schema = {
            TextField.of("$.name").as("name"),
            TextField.of("$.city").as("city"),
            NumericField.of("$.age").as("age")
        };

        String createResult = jedis.ftCreate("idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.JSON)
                .addPrefix("user:"),
                schema
        );

        System.out.println(createResult); // >>> OK

        String user1Set = jedis.jsonSet("user:1", new Path2("$"), user1);
        String user2Set = jedis.jsonSet("user:2", new Path2("$"), user2);
        String user3Set = jedis.jsonSet("user:3", new Path2("$"), user3);

        SearchResult findPaulResult = jedis.ftSearch("idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulResult.getTotalResults()); // >>> 1

        List<Document> paulDocs = findPaulResult.getDocuments();

        for (Document doc: paulDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        SearchResult citiesResult = jedis.ftSearch("idx:users",
            "Paul",
            FTSearchParams.searchParams()
                .returnFields("city")
        );

        System.out.println(citiesResult.getTotalResults()); // >>> 2

        for (Document doc: citiesResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> user:1
        // >>> user:3

        AggregationResult aggResult = jedis.ftAggregate("idx:users",
            new AggregationBuilder("*")
                .groupBy("@city", Reducers.count().as("count"))
        );

        System.out.println(aggResult.getTotalResults()); // >>> 2

        for (Row cityRow: aggResult.getRows()) {
            System.out.printf("%s - %d%n",
                cityRow.getString("city"), cityRow.getLong("count"));
        }
        // >>> London - 1
        // >>> Tel Aviv - 2

        try {jedis.ftDropIndex("hash-idx:users");} catch (JedisDataException j){}
        jedis.del("huser:1", "huser:2", "huser:3");

        SchemaField[] hashSchema = {
            TextField.of("name"),
            TextField.of("city"),
            NumericField.of("age")
        };

        String hashCreateResult = jedis.ftCreate("hash-idx:users",
            FTCreateParams.createParams()
                .on(IndexDataType.HASH)
                .addPrefix("huser:"),
                hashSchema
        );

        System.out.println(hashCreateResult); // >>> OK

        Map<String, String> user1Info = new HashMap<>();
        user1Info.put("name", "Paul John");
        user1Info.put("email", "paul.john@example.com");
        user1Info.put("age", "42");
        user1Info.put("city", "London");
        long huser1Set = jedis.hset("huser:1", user1Info);
        
        System.out.println(huser1Set); // >>> 4

        Map<String, String> user2Info = new HashMap<>();
        user2Info.put("name", "Eden Zamir");
        user2Info.put("email", "eden.zamir@example.com");
        user2Info.put("age", "29");
        user2Info.put("city", "Tel Aviv");
        long huser2Set = jedis.hset("huser:2", user2Info);
        
        System.out.println(huser2Set); // >>> 4

        Map<String, String> user3Info = new HashMap<>();
        user3Info.put("name", "Paul Zamir");
        user3Info.put("email", "paul.zamir@example.com");
        user3Info.put("age", "35");
        user3Info.put("city", "Tel Aviv");
        long huser3Set = jedis.hset("huser:3", user3Info);
        
        System.out.println(huser3Set); // >>> 4
        
        SearchResult findPaulHashResult = jedis.ftSearch("hash-idx:users",
             "Paul @age:[30 40]"
        );
        
        System.out.println(findPaulHashResult.getTotalResults()); // >>> 1

        List<Document> paulHashDocs = findPaulHashResult.getDocuments();

        for (Document doc: paulHashDocs) {
            System.out.println(doc.getId());
        }
        // >>> user:3

        jedis.close();
    }
}

```

## More information

See the [Redis Search](/docs/latest/develop/ai/search-and-query/) docs for a full description of all query features with examples.

## On this page
