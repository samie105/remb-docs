---
title: "Full-text search"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/full-text/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/full-text/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:45.273Z"
content_hash: "401c0d2835a37409565c804dcfb7a3fb4f211c405890cdabee6d9ca3b79b8880"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Full-text search","→","Full-text search"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Full-text search","→","Full-text search"]
---
# Full-text search

Perform a full-text search

A full-text search finds words or phrases within larger texts. You can search within a specific text field or across all text fields.

This article provides a good overview of the most relevant full-text search capabilities. Please find further details about all the full-text search features in the [reference documentation](/docs/latest/develop/ai/search-and-query/advanced-concepts/).

The examples in this article use a schema with the following fields:

Field name

Field type

`brand`

`TEXT`

`model`

`TEXT`

`description`

`TEXT`

## Single word

To search for a word (or word stem) across all text fields, you can construct the following simple query:

```
FT.SEARCH index "word"
```

Instead of searching across all text fields, you might want to limit the search to a specific text field.

```
FT.SEARCH index "@field: word"
```

Words that occur very often in natural language, such as `the` or `a` for the English language, aren't indexed and will not return a search result. You can find further details in the [stop words article](/docs/latest/develop/ai/search-and-query/advanced-concepts/stopwords/).

The following example searches for all bicycles that have the word 'kids' in the description:

```plaintext
FT.SEARCH idx:bicycle "@description: kids"
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.brand", as_name="brand"),
    TextField("$.model", as_name="model"),
    TextField("$.description", as_name="description"),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_em.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

res = index.search(Query("@description: kids"))
print(res.total)
# >>> 2

res = index.search(Query("@model: ka*"))
print(res.total)
# >>> 1

res = index.search(Query("@brand: *bikes"))
print(res.total)
# >>> 2

res = index.search(Query("%optamized%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

res = index.search(Query("%%optamised%%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.model': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'model'
  },
  '$.brand': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'brand'
  },
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
})

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_em.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', '@description: kids');
console.log(res1.total); // >>> 2

const res2 = await client.ft.search('idx:bicycle', '@model: ka*');
console.log(res2.total); // >>> 1

const res3 = await client.ft.search('idx:bicycle', '@brand: *bikes');
console.log(res3.total); // >>> 2

const res4 = await client.ft.search('idx:bicycle', '%optamized%');
console.log(res4); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

const res5 = await client.ft.search('idx:bicycle', '%%optamised%%');
console.log(res5); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

```

```java
import java.util.List;
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryFtExample {
    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition")
        };

        jedis.ftCreate("idx:bicycle",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("bicycle:"),
            schema
        );

        String[] bicycleJsons = new String[] {
            "  {"
            + "	  \"pickup_zone\": \"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, "
            + "-74.0610 40.6678, -74.0610 40.7578))\","
            + "	  \"store_location\": \"-74.0060,40.7128\","
            + "	  \"brand\": \"Velorim\","
            + "	  \"model\": \"Jigger\","
            + "	  \"price\": 270,"
            + "	  \"description\": \"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
            + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
            + "is the vehicle of choice for the rare tenacious little rider raring to go.\","
            + "	  \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, "
            + "-118.2887 33.9872, -118.2887 34.0972))\","
            + "	  \"store_location\": \"-118.2437,34.0522\","
            + "	  \"brand\": \"Bicyk\","
            + "	  \"model\": \"Hillcraft\","
            + "	  \"price\": 1200,"
            + "	  \"description\": \"Kids want to ride with as little weight as possible. Especially "
            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\","
            + "	  \"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, "
            + "-87.6848 41.8231, -87.6848 41.9331))\","
            + "	  \"store_location\": \"-87.6298,41.8781\","
            + "  	\"brand\": \"Nord\","
            + "  	\"model\": \"Chook air 5\","
            + "  	\"price\": 815,"
            + "  	\"description\": \"The Chook Air 5  gives kids aged six years and older a durable "
            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
            + "situation, giving your kids greater safety on the trails.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, "
            + "-80.2433 25.6967, -80.2433 25.8067))\","
            + "  	\"store_location\": \"-80.1918,25.7617\","
            + "  	\"brand\": \"Eva\","
            + "  	\"model\": \"Eva 291\","
            + "  	\"price\": 3400,"
            + "  	\"description\": \"The sister company to Nord, Eva launched in 2005 as the first "
            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
            + "are optimized for the feminine physique using analytics from a body metrics database. "
            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
            + "29-inch wheels. Yippee!\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, "
            + "-122.4644 37.7099, -122.4644 37.8199))\","
            + "  	\"store_location\": \"-122.4194,37.7749\","
            + "  	\"brand\": \"Noka Bikes\","
            + "  	\"model\": \"Kahuna\","
            + "  	\"price\": 3200,"
            + "  	\"description\": \"Whether you want to try your hand at XC racing or are looking "
            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
            + "frames and components have been tweaked to include a women’s saddle, different bars "
            + "and unique colourway.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, "
            + "-0.1778 51.4024, -0.1778 51.5524))\","
            + "    \"store_location\": \"-0.1278,51.5074\","
            + "    \"brand\": \"Breakout\","
            + "    \"model\": \"XBN 2.1 Alloy\","
            + "    \"price\": 810,"
            + "    \"description\": \"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
            + "doesn’t break the bank and delivers craved performance.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, "
            + "2.1767 48.5516, 2.1767 48.9016))\","
            + "    \"store_location\": \"2.3522,48.8566\","
            + "    \"brand\": \"ScramBikes\","
            + "    \"model\": \"WattBike\","
            + "    \"price\": 2300,"
            + "    \"description\": \"The WattBike is the best e-bike for people who still "
            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
            + "leisurely ride. With three working modes, you can choose between E-bike, "
            + "assisted bicycle, and normal bike modes.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, "
            + "13.3260 52.2700, 13.3260 52.5700))\","
            + "    \"store_location\": \"13.4050,52.5200\","
            + "    \"brand\": \"Peaknetic\","
            + "    \"model\": \"Secto\","
            + "    \"price\": 430,"
            + "    \"description\": \"If you struggle with stiff fingers or a kinked neck or "
            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
            + "on the ground to balance at a stop, and the low step-over frame makes it "
            + "accessible for all ability and mobility levels. The saddle is very soft, with "
            + "a wide back to support your hip joints and a cutout in the center to redistribute "
            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, "
            + "1.9450 41.1987, 1.9450 41.4301))\","
            + "    \"store_location\": \"2.1734, 41.3851\","
            + "    \"brand\": \"nHill\","
            + "    \"model\": \"Summit\","
            + "    \"price\": 1200,"
            + "    \"description\": \"This budget mountain bike from nHill performs well both "
            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
            + "Whether you want an affordable bike that you can take to work, but also take "
            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
            + "ride for the bike path, the Summit gives a good value for money.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((12.4464 42.1028, 12.5464 42.1028, "
            + "12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\","
            + "    \"store_location\": \"12.4964,41.9028\","
            + "    \"model\": \"ThrillCycle\","
            + "    \"brand\": \"BikeShind\","
            + "    \"price\": 815,"
            + "    \"description\": \"An artsy,  retro-inspired bicycle that’s as "
            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
            + "with a limited lifetime warranty, so this little guy will last you long "
            + "past graduation.\","
            + "    \"condition\": \"refurbished\""
            + "  }"
        };

        for (int i = 0; i < bicycleJsons.length; i++) {
            jedis.jsonSet("bicycle:" + i, Path2.ROOT_PATH, bicycleJsons[i]);
        }

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@description: kids");
        System.out.println(res1.getTotalResults()); // >>> 2

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:2
        // >>> bicycle:1

        // Tests for 'ft1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle", "@model: ka*");
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:4

        // Tests for 'ft2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@brand: *bikes");
        System.out.println(res3.getTotalResults()); // >>> 2

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:6
        // >>> bicycle:4

        // Tests for 'ft3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle", "%optamized%");
        System.out.println(res4.getTotalResults()); // >>> 1

        List<Document> docs4 = res4.getDocuments();

        for (int i = 0; i < docs4.size(); i++) {
            System.out.println(docs4.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft4' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle", "%%optamised%%");
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft5' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            asyncCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).toCompletableFuture().join();

            JsonParser parser = asyncCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<?>[] bikeFutures = new CompletableFuture[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = asyncCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i))
                        .toCompletableFuture();
            }

            CompletableFuture.allOf(bikeFutures).join();

            CompletableFuture<SearchReply<String, String>> descriptionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description: kids").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:1
                        // >>> ID: bicycle:2
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> startsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@model: ka*").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> endsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@brand: *bikes").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        // >>> ID: bicycle:6
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzyResults = asyncCommands.ftSearch("idx:bicycle", "%optamized%")
                    .thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzierResults = asyncCommands
                    .ftSearch("idx:bicycle", "%%optamised%%").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults)
                    .join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.reactive.RedisReactiveCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            reactiveCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).block();

            JsonParser parser = reactiveCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<?>[] bikeFutures = new Mono<?>[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = reactiveCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i));
            }

            Mono.when(bikeFutures).block();

            Mono<SearchReply<String, String>> descriptionResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description: kids").doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:1
                            // >>> ID: bicycle:2
                        });
                    });

            Mono<SearchReply<String, String>> startsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@model: ka*")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                        });
                    });

            Mono<SearchReply<String, String>> endsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@brand: *bikes")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                            // >>> ID: bicycle:6
                        });
                    });

            Mono<SearchReply<String, String>> fuzzyResults = reactiveCommands.ftSearch("idx:bicycle", "%optamized%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono<SearchReply<String, String>> fuzzierResults = reactiveCommands.ftSearch("idx:bicycle", "%%optamised%%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono.when(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults).block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"sort"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_ft() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	_, err := rdb.FTCreate(ctx, "idx:bicycle",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"bicycle:"},
		},
		&redis.FieldSchema{
			FieldName: "$.brand",
			As:        "brand",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.model",
			As:        "model",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.description",
			As:        "description",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.price",
			As:        "price",
			FieldType: redis.SearchFieldTypeNumeric,
		},
		&redis.FieldSchema{
			FieldName: "$.condition",
			As:        "condition",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	exampleJsons := []map[string]interface{}{
		{
			"pickup_zone": "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, " +
				"-74.0610 40.6678, -74.0610 40.7578))",
			"store_location": "-74.0060,40.7128",
			"brand":          "Velorim",
			"model":          "Jigger",
			"price":          270,
			"description": "Small and powerful, the Jigger is the best ride for the smallest of tikes! " +
				"This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger " +
				"is the vehicle of choice for the rare tenacious little rider raring to go.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, " +
				"-118.2887 33.9872, -118.2887 34.0972))",
			"store_location": "-118.2437,34.0522",
			"brand":          "Bicyk",
			"model":          "Hillcraft",
			"price":          1200,
			"description": "Kids want to ride with as little weight as possible. Especially " +
				"on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming " +
				"off a 24'' bike. The Hillcraft 26 is just the solution they need!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, " +
				"-87.6848 41.8231, -87.6848 41.9331))",
			"store_location": "-87.6298,41.8781",
			"brand":          "Nord",
			"model":          "Chook air 5",
			"price":          815,
			"description": "The Chook Air 5  gives kids aged six years and older a durable " +
				"and uberlight mountain bike for their first experience on tracks and easy cruising through " +
				"forests and fields. The lower  top tube makes it easy to mount and dismount in any " +
				"situation, giving your kids greater safety on the trails.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, " +
				"-80.2433 25.6967, -80.2433 25.8067))",
			"store_location": "-80.1918,25.7617",
			"brand":          "Eva",
			"model":          "Eva 291",
			"price":          3400,
			"description": "The sister company to Nord, Eva launched in 2005 as the first " +
				"and only women-dedicated bicycle brand. Designed by women for women, allEva bikes " +
				"are optimized for the feminine physique using analytics from a body metrics database. " +
				"If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This " +
				"full-suspension, cross-country ride has been designed for velocity. The 291 has " +
				"100mm of front and rear travel, a superlight aluminum frame and fast-rolling " +
				"29-inch wheels. Yippee!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, " +
				"-122.4644 37.7099, -122.4644 37.8199))",
			"store_location": "-122.4194,37.7749",
			"brand":          "Noka Bikes",
			"model":          "Kahuna",
			"price":          3200,
			"description": "Whether you want to try your hand at XC racing or are looking " +
				"for a lively trail bike that's just as inspiring on the climbs as it is over rougher " +
				"ground, the Wilder is one heck of a bike built specifically for short women. Both the " +
				"frames and components have been tweaked to include a women’s saddle, different bars " +
				"and unique colourway.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, " +
				"-0.1778 51.4024, -0.1778 51.5524))",
			"store_location": "-0.1278,51.5074",
			"brand":          "Breakout",
			"model":          "XBN 2.1 Alloy",
			"price":          810,
			"description": "The XBN 2.1 Alloy is our entry-level road bike – but that’s " +
				"not to say that it’s a basic machine. With an internal weld aluminium frame, a full " +
				"carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which " +
				"doesn’t break the bank and delivers craved performance.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, " +
				"2.1767 48.5516, 2.1767 48.9016))",
			"store_location": "2.3522,48.8566",
			"brand":          "ScramBikes",
			"model":          "WattBike",
			"price":          2300,
			"description": "The WattBike is the best e-bike for people who still " +
				"feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH " +
				"Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one " +
				"charge. It’s great for tackling hilly terrain or if you just fancy a more " +
				"leisurely ride. With three working modes, you can choose between E-bike, " +
				"assisted bicycle, and normal bike modes.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, " +
				"13.3260 52.2700, 13.3260 52.5700))",
			"store_location": "13.4050,52.5200",
			"brand":          "Peaknetic",
			"model":          "Secto",
			"price":          430,
			"description": "If you struggle with stiff fingers or a kinked neck or " +
				"back after a few minutes on the road, this lightweight, aluminum bike alleviates " +
				"those issues and allows you to enjoy the ride. From the ergonomic grips to the " +
				"lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. " +
				"The rear-inclined seat tube facilitates stability by allowing you to put a foot " +
				"on the ground to balance at a stop, and the low step-over frame makes it " +
				"accessible for all ability and mobility levels. The saddle is very soft, with " +
				"a wide back to support your hip joints and a cutout in the center to redistribute " +
				"that pressure. Rim brakes deliver satisfactory braking control, and the wide tires " +
				"provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts " +
				"facilitate setting up the Roll Low-Entry as your preferred commuter, and the " +
				"BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, " +
				"1.9450 41.1987, 1.9450 41.4301))",
			"store_location": "2.1734, 41.3851",
			"brand":          "nHill",
			"model":          "Summit",
			"price":          1200,
			"description": "This budget mountain bike from nHill performs well both " +
				"on bike paths and on the trail. The fork with 100mm of travel absorbs rough " +
				"terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. " +
				"The Shimano Tourney drivetrain offered enough gears for finding a comfortable " +
				"pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. " +
				"Whether you want an affordable bike that you can take to work, but also take " +
				"trail in mountains on the weekends or you’re just after a stable, comfortable " +
				"ride for the bike path, the Summit gives a good value for money.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((12.4464 42.1028, 12.5464 42.1028, " +
				"12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
			"store_location": "12.4964,41.9028",
			"model":          "ThrillCycle",
			"brand":          "BikeShind",
			"price":          815,
			"description": "An artsy,  retro-inspired bicycle that’s as " +
				"functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. " +
				"A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t " +
				"suggest taking it to the mountains. Fenders protect you from mud, and a rear " +
				"basket lets you transport groceries, flowers and books. The ThrillCycle comes " +
				"with a limited lifetime warranty, so this little guy will last you long " +
				"past graduation.",
			"condition": "refurbished",
		},
	}

	for i, json := range exampleJsons {
		_, err := rdb.JSONSet(ctx, fmt.Sprintf("bicycle:%v", i), "$", json).Result()

		if err != nil {
			panic(err)
		}
	}

	res1, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description: kids",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 2

	sort.Slice(res1.Docs, func(i, j int) bool {
		return res1.Docs[i].ID < res1.Docs[j].ID
	})

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:1
	// >>> bicycle:2

	res2, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@model: ka*",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@brand: *bikes",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 2

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})
	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4
	// >>> bicycle:6

	res4, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%optamized%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 1

	for _, doc := range res4.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

	res5, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%%optamised%%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5.Total) // >>> 1

	for _, doc := range res5.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryFtExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.brand", "brand"))
            .AddTextField(new FieldName("$.model", "model"))
            .AddTextField(new FieldName("$.description", "description"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[]
        {
            new
            {
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride " +
                                "for the smallest of tikes! This is the tiniest " +
                                "kids’ pedal bike on the market available without" +
                                " a coaster brake, the Jigger is the vehicle of " +
                                "choice for the rare tenacious little rider " +
                                "raring to go.",
                condition = "used"
            },
            new
            {
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible." +
                    " Especially on an incline! They may be at the age " +
                    "when a 27.5 inch wheel bike is just too clumsy coming " +
                    "off a 24 inch bike. The Hillcraft 26 is just the solution" +
                    " they need!",
                condition = "used",
            },
            new
            {
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older " +
                    "a durable and uberlight mountain bike for their first" +
                    " experience on tracks and easy cruising through forests" +
                    " and fields. The lower  top tube makes it easy to mount" +
                    " and dismount in any situation, giving your kids greater" +
                    " safety on the trails.",
                condition = "used",
            },
            new
            {
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the" +
                    " first and only women-dedicated bicycle brand. Designed" +
                    " by women for women, allEva bikes are optimized for the" +
                    " feminine physique using analytics from a body metrics" +
                    " database. If you like 29ers, try the Eva 291. It’s a " +
                    "brand new bike for 2022.. This full-suspension, " +
                    "cross-country ride has been designed for velocity. The" +
                    " 291 has 100mm of front and rear travel, a superlight " +
                    "aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used",
            },
            new
            {
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are " +
                    "looking for a lively trail bike that's just as inspiring" +
                    " on the climbs as it is over rougher ground, the Wilder" +
                    " is one heck of a bike built specifically for short women." +
                    " Both the frames and components have been tweaked to " +
                    "include a women’s saddle, different bars and unique " +
                    "colourway.",
                condition = "used",
            },
            new
            {
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
                    " not to say that it’s a basic machine. With an internal " +
                    "weld aluminium frame, a full carbon fork, and the slick-shifting" +
                    " Claris gears from Shimano’s, this is a bike which doesn’t" +
                    " break the bank and delivers craved performance.",
                condition = "new",
            },
            new
            {
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young" +
                    " at heart. It has a Bafang 1000W mid-drive system and a 48V" +
                    " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
                    " more than 60 miles on one charge. It’s great for tackling hilly" +
                    " terrain or if you just fancy a more leisurely ride. With three" +
                    " working modes, you can choose between E-bike, assisted bicycle," +
                    " and normal bike modes.",
                condition = "new",
            },
            new
            {
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after" +
                    " a few minutes on the road, this lightweight, aluminum bike" +
                    " alleviates those issues and allows you to enjoy the ride. From" +
                    " the ergonomic grips to the lumbar-supporting seat position, the" +
                    " Roll Low-Entry offers incredible comfort. The rear-inclined seat" +
                    " tube facilitates stability by allowing you to put a foot on the" +
                    " ground to balance at a stop, and the low step-over frame makes it" +
                    " accessible for all ability and mobility levels. The saddle is" +
                    " very soft, with a wide back to support your hip joints and a" +
                    " cutout in the center to redistribute that pressure. Rim brakes" +
                    " deliver satisfactory braking control, and the wide tires provide" +
                    " a smooth, stable ride on paved roads and gravel. Rack and fender" +
                    " mounts facilitate setting up the Roll Low-Entry as your preferred" +
                    " commuter, and the BMX-like handlebar offers space for mounting a" +
                    " flashlight, bell, or phone holder.",
                condition = "new",
            },
            new
            {
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike" +
                    " paths and on the trail. The fork with 100mm of travel absorbs" +
                    " rough terrain. Fat Kenda Booster tires give you grip in corners" +
                    " and on wet trails. The Shimano Tourney drivetrain offered enough" +
                    " gears for finding a comfortable pace to ride uphill, and the" +
                    " Tektro hydraulic disc brakes break smoothly. Whether you want an" +
                    " affordable bike that you can take to work, but also take trail in" +
                    " mountains on the weekends or you’re just after a stable," +
                    " comfortable ride for the bike path, the Summit gives a good value" +
                    " for money.",
                condition = "new",
            },
            new
            {
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is" +
                    " pretty: The ThrillCycle steel frame offers a smooth ride. A" +
                    " 9-speed drivetrain has enough gears for coasting in the city, but" +
                    " we wouldn’t suggest taking it to the mountains. Fenders protect" +
                    " you from mud, and a rear basket lets you transport groceries," +
                    " flowers and books. The ThrillCycle comes with a limited lifetime" +
                    " warranty, so this little guy will last you long past graduation.",
                condition = "refurbished",
            },
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        SearchResult res1 = db.FT().Search(
           "idx:bicycle",
           new("@description: kids")
       );
        Console.WriteLine(res1);    // >>> 2

        // Tests for 'ft1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new("@model: ka*")
        );
        Console.WriteLine(res2.TotalResults);   // >>> 1

        // Tests for 'ft2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@brand: *bikes")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 2

        // Tests for 'ft3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new("%optamized%")
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'ft4' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("%%optamised%%")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'ft5' step.

    }
}

```

## Phrase

A phrase is a sentence, sentence fragment, or small group of words. You can find further details about how to find exact phrases in the [exact match article](/docs/latest/develop/ai/search-and-query/query/exact-match/).

## Word prefix

You can also search for words that match a given prefix.

```
FT.SEARCH index "prefix*"
```

```
FT.SEARCH index "@field: prefix*"
```

Important:

The prefix needs to be at least two characters long.

Here is an example that shows you how to search for bicycles with a brand that starts with 'ka':

```plaintext
FT.SEARCH idx:bicycle "@model: ka*"
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.brand", as_name="brand"),
    TextField("$.model", as_name="model"),
    TextField("$.description", as_name="description"),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_em.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

res = index.search(Query("@description: kids"))
print(res.total)
# >>> 2

res = index.search(Query("@model: ka*"))
print(res.total)
# >>> 1

res = index.search(Query("@brand: *bikes"))
print(res.total)
# >>> 2

res = index.search(Query("%optamized%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

res = index.search(Query("%%optamised%%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.model': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'model'
  },
  '$.brand': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'brand'
  },
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
})

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_em.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', '@description: kids');
console.log(res1.total); // >>> 2

const res2 = await client.ft.search('idx:bicycle', '@model: ka*');
console.log(res2.total); // >>> 1

const res3 = await client.ft.search('idx:bicycle', '@brand: *bikes');
console.log(res3.total); // >>> 2

const res4 = await client.ft.search('idx:bicycle', '%optamized%');
console.log(res4); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

const res5 = await client.ft.search('idx:bicycle', '%%optamised%%');
console.log(res5); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

```

```java
import java.util.List;
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryFtExample {
    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition")
        };

        jedis.ftCreate("idx:bicycle",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("bicycle:"),
            schema
        );

        String[] bicycleJsons = new String[] {
            "  {"
            + "	  \"pickup_zone\": \"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, "
            + "-74.0610 40.6678, -74.0610 40.7578))\","
            + "	  \"store_location\": \"-74.0060,40.7128\","
            + "	  \"brand\": \"Velorim\","
            + "	  \"model\": \"Jigger\","
            + "	  \"price\": 270,"
            + "	  \"description\": \"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
            + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
            + "is the vehicle of choice for the rare tenacious little rider raring to go.\","
            + "	  \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, "
            + "-118.2887 33.9872, -118.2887 34.0972))\","
            + "	  \"store_location\": \"-118.2437,34.0522\","
            + "	  \"brand\": \"Bicyk\","
            + "	  \"model\": \"Hillcraft\","
            + "	  \"price\": 1200,"
            + "	  \"description\": \"Kids want to ride with as little weight as possible. Especially "
            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\","
            + "	  \"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, "
            + "-87.6848 41.8231, -87.6848 41.9331))\","
            + "	  \"store_location\": \"-87.6298,41.8781\","
            + "  	\"brand\": \"Nord\","
            + "  	\"model\": \"Chook air 5\","
            + "  	\"price\": 815,"
            + "  	\"description\": \"The Chook Air 5  gives kids aged six years and older a durable "
            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
            + "situation, giving your kids greater safety on the trails.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, "
            + "-80.2433 25.6967, -80.2433 25.8067))\","
            + "  	\"store_location\": \"-80.1918,25.7617\","
            + "  	\"brand\": \"Eva\","
            + "  	\"model\": \"Eva 291\","
            + "  	\"price\": 3400,"
            + "  	\"description\": \"The sister company to Nord, Eva launched in 2005 as the first "
            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
            + "are optimized for the feminine physique using analytics from a body metrics database. "
            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
            + "29-inch wheels. Yippee!\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, "
            + "-122.4644 37.7099, -122.4644 37.8199))\","
            + "  	\"store_location\": \"-122.4194,37.7749\","
            + "  	\"brand\": \"Noka Bikes\","
            + "  	\"model\": \"Kahuna\","
            + "  	\"price\": 3200,"
            + "  	\"description\": \"Whether you want to try your hand at XC racing or are looking "
            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
            + "frames and components have been tweaked to include a women’s saddle, different bars "
            + "and unique colourway.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, "
            + "-0.1778 51.4024, -0.1778 51.5524))\","
            + "    \"store_location\": \"-0.1278,51.5074\","
            + "    \"brand\": \"Breakout\","
            + "    \"model\": \"XBN 2.1 Alloy\","
            + "    \"price\": 810,"
            + "    \"description\": \"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
            + "doesn’t break the bank and delivers craved performance.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, "
            + "2.1767 48.5516, 2.1767 48.9016))\","
            + "    \"store_location\": \"2.3522,48.8566\","
            + "    \"brand\": \"ScramBikes\","
            + "    \"model\": \"WattBike\","
            + "    \"price\": 2300,"
            + "    \"description\": \"The WattBike is the best e-bike for people who still "
            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
            + "leisurely ride. With three working modes, you can choose between E-bike, "
            + "assisted bicycle, and normal bike modes.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, "
            + "13.3260 52.2700, 13.3260 52.5700))\","
            + "    \"store_location\": \"13.4050,52.5200\","
            + "    \"brand\": \"Peaknetic\","
            + "    \"model\": \"Secto\","
            + "    \"price\": 430,"
            + "    \"description\": \"If you struggle with stiff fingers or a kinked neck or "
            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
            + "on the ground to balance at a stop, and the low step-over frame makes it "
            + "accessible for all ability and mobility levels. The saddle is very soft, with "
            + "a wide back to support your hip joints and a cutout in the center to redistribute "
            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, "
            + "1.9450 41.1987, 1.9450 41.4301))\","
            + "    \"store_location\": \"2.1734, 41.3851\","
            + "    \"brand\": \"nHill\","
            + "    \"model\": \"Summit\","
            + "    \"price\": 1200,"
            + "    \"description\": \"This budget mountain bike from nHill performs well both "
            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
            + "Whether you want an affordable bike that you can take to work, but also take "
            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
            + "ride for the bike path, the Summit gives a good value for money.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((12.4464 42.1028, 12.5464 42.1028, "
            + "12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\","
            + "    \"store_location\": \"12.4964,41.9028\","
            + "    \"model\": \"ThrillCycle\","
            + "    \"brand\": \"BikeShind\","
            + "    \"price\": 815,"
            + "    \"description\": \"An artsy,  retro-inspired bicycle that’s as "
            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
            + "with a limited lifetime warranty, so this little guy will last you long "
            + "past graduation.\","
            + "    \"condition\": \"refurbished\""
            + "  }"
        };

        for (int i = 0; i < bicycleJsons.length; i++) {
            jedis.jsonSet("bicycle:" + i, Path2.ROOT_PATH, bicycleJsons[i]);
        }

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@description: kids");
        System.out.println(res1.getTotalResults()); // >>> 2

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:2
        // >>> bicycle:1

        // Tests for 'ft1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle", "@model: ka*");
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:4

        // Tests for 'ft2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@brand: *bikes");
        System.out.println(res3.getTotalResults()); // >>> 2

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:6
        // >>> bicycle:4

        // Tests for 'ft3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle", "%optamized%");
        System.out.println(res4.getTotalResults()); // >>> 1

        List<Document> docs4 = res4.getDocuments();

        for (int i = 0; i < docs4.size(); i++) {
            System.out.println(docs4.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft4' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle", "%%optamised%%");
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft5' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            asyncCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).toCompletableFuture().join();

            JsonParser parser = asyncCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<?>[] bikeFutures = new CompletableFuture[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = asyncCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i))
                        .toCompletableFuture();
            }

            CompletableFuture.allOf(bikeFutures).join();

            CompletableFuture<SearchReply<String, String>> descriptionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description: kids").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:1
                        // >>> ID: bicycle:2
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> startsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@model: ka*").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> endsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@brand: *bikes").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        // >>> ID: bicycle:6
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzyResults = asyncCommands.ftSearch("idx:bicycle", "%optamized%")
                    .thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzierResults = asyncCommands
                    .ftSearch("idx:bicycle", "%%optamised%%").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults)
                    .join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.reactive.RedisReactiveCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            reactiveCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).block();

            JsonParser parser = reactiveCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<?>[] bikeFutures = new Mono<?>[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = reactiveCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i));
            }

            Mono.when(bikeFutures).block();

            Mono<SearchReply<String, String>> descriptionResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description: kids").doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:1
                            // >>> ID: bicycle:2
                        });
                    });

            Mono<SearchReply<String, String>> startsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@model: ka*")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                        });
                    });

            Mono<SearchReply<String, String>> endsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@brand: *bikes")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                            // >>> ID: bicycle:6
                        });
                    });

            Mono<SearchReply<String, String>> fuzzyResults = reactiveCommands.ftSearch("idx:bicycle", "%optamized%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono<SearchReply<String, String>> fuzzierResults = reactiveCommands.ftSearch("idx:bicycle", "%%optamised%%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono.when(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults).block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"sort"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_ft() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	_, err := rdb.FTCreate(ctx, "idx:bicycle",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"bicycle:"},
		},
		&redis.FieldSchema{
			FieldName: "$.brand",
			As:        "brand",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.model",
			As:        "model",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.description",
			As:        "description",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.price",
			As:        "price",
			FieldType: redis.SearchFieldTypeNumeric,
		},
		&redis.FieldSchema{
			FieldName: "$.condition",
			As:        "condition",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	exampleJsons := []map[string]interface{}{
		{
			"pickup_zone": "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, " +
				"-74.0610 40.6678, -74.0610 40.7578))",
			"store_location": "-74.0060,40.7128",
			"brand":          "Velorim",
			"model":          "Jigger",
			"price":          270,
			"description": "Small and powerful, the Jigger is the best ride for the smallest of tikes! " +
				"This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger " +
				"is the vehicle of choice for the rare tenacious little rider raring to go.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, " +
				"-118.2887 33.9872, -118.2887 34.0972))",
			"store_location": "-118.2437,34.0522",
			"brand":          "Bicyk",
			"model":          "Hillcraft",
			"price":          1200,
			"description": "Kids want to ride with as little weight as possible. Especially " +
				"on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming " +
				"off a 24'' bike. The Hillcraft 26 is just the solution they need!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, " +
				"-87.6848 41.8231, -87.6848 41.9331))",
			"store_location": "-87.6298,41.8781",
			"brand":          "Nord",
			"model":          "Chook air 5",
			"price":          815,
			"description": "The Chook Air 5  gives kids aged six years and older a durable " +
				"and uberlight mountain bike for their first experience on tracks and easy cruising through " +
				"forests and fields. The lower  top tube makes it easy to mount and dismount in any " +
				"situation, giving your kids greater safety on the trails.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, " +
				"-80.2433 25.6967, -80.2433 25.8067))",
			"store_location": "-80.1918,25.7617",
			"brand":          "Eva",
			"model":          "Eva 291",
			"price":          3400,
			"description": "The sister company to Nord, Eva launched in 2005 as the first " +
				"and only women-dedicated bicycle brand. Designed by women for women, allEva bikes " +
				"are optimized for the feminine physique using analytics from a body metrics database. " +
				"If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This " +
				"full-suspension, cross-country ride has been designed for velocity. The 291 has " +
				"100mm of front and rear travel, a superlight aluminum frame and fast-rolling " +
				"29-inch wheels. Yippee!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, " +
				"-122.4644 37.7099, -122.4644 37.8199))",
			"store_location": "-122.4194,37.7749",
			"brand":          "Noka Bikes",
			"model":          "Kahuna",
			"price":          3200,
			"description": "Whether you want to try your hand at XC racing or are looking " +
				"for a lively trail bike that's just as inspiring on the climbs as it is over rougher " +
				"ground, the Wilder is one heck of a bike built specifically for short women. Both the " +
				"frames and components have been tweaked to include a women’s saddle, different bars " +
				"and unique colourway.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, " +
				"-0.1778 51.4024, -0.1778 51.5524))",
			"store_location": "-0.1278,51.5074",
			"brand":          "Breakout",
			"model":          "XBN 2.1 Alloy",
			"price":          810,
			"description": "The XBN 2.1 Alloy is our entry-level road bike – but that’s " +
				"not to say that it’s a basic machine. With an internal weld aluminium frame, a full " +
				"carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which " +
				"doesn’t break the bank and delivers craved performance.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, " +
				"2.1767 48.5516, 2.1767 48.9016))",
			"store_location": "2.3522,48.8566",
			"brand":          "ScramBikes",
			"model":          "WattBike",
			"price":          2300,
			"description": "The WattBike is the best e-bike for people who still " +
				"feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH " +
				"Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one " +
				"charge. It’s great for tackling hilly terrain or if you just fancy a more " +
				"leisurely ride. With three working modes, you can choose between E-bike, " +
				"assisted bicycle, and normal bike modes.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, " +
				"13.3260 52.2700, 13.3260 52.5700))",
			"store_location": "13.4050,52.5200",
			"brand":          "Peaknetic",
			"model":          "Secto",
			"price":          430,
			"description": "If you struggle with stiff fingers or a kinked neck or " +
				"back after a few minutes on the road, this lightweight, aluminum bike alleviates " +
				"those issues and allows you to enjoy the ride. From the ergonomic grips to the " +
				"lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. " +
				"The rear-inclined seat tube facilitates stability by allowing you to put a foot " +
				"on the ground to balance at a stop, and the low step-over frame makes it " +
				"accessible for all ability and mobility levels. The saddle is very soft, with " +
				"a wide back to support your hip joints and a cutout in the center to redistribute " +
				"that pressure. Rim brakes deliver satisfactory braking control, and the wide tires " +
				"provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts " +
				"facilitate setting up the Roll Low-Entry as your preferred commuter, and the " +
				"BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, " +
				"1.9450 41.1987, 1.9450 41.4301))",
			"store_location": "2.1734, 41.3851",
			"brand":          "nHill",
			"model":          "Summit",
			"price":          1200,
			"description": "This budget mountain bike from nHill performs well both " +
				"on bike paths and on the trail. The fork with 100mm of travel absorbs rough " +
				"terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. " +
				"The Shimano Tourney drivetrain offered enough gears for finding a comfortable " +
				"pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. " +
				"Whether you want an affordable bike that you can take to work, but also take " +
				"trail in mountains on the weekends or you’re just after a stable, comfortable " +
				"ride for the bike path, the Summit gives a good value for money.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((12.4464 42.1028, 12.5464 42.1028, " +
				"12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
			"store_location": "12.4964,41.9028",
			"model":          "ThrillCycle",
			"brand":          "BikeShind",
			"price":          815,
			"description": "An artsy,  retro-inspired bicycle that’s as " +
				"functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. " +
				"A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t " +
				"suggest taking it to the mountains. Fenders protect you from mud, and a rear " +
				"basket lets you transport groceries, flowers and books. The ThrillCycle comes " +
				"with a limited lifetime warranty, so this little guy will last you long " +
				"past graduation.",
			"condition": "refurbished",
		},
	}

	for i, json := range exampleJsons {
		_, err := rdb.JSONSet(ctx, fmt.Sprintf("bicycle:%v", i), "$", json).Result()

		if err != nil {
			panic(err)
		}
	}

	res1, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description: kids",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 2

	sort.Slice(res1.Docs, func(i, j int) bool {
		return res1.Docs[i].ID < res1.Docs[j].ID
	})

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:1
	// >>> bicycle:2

	res2, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@model: ka*",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@brand: *bikes",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 2

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})
	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4
	// >>> bicycle:6

	res4, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%optamized%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 1

	for _, doc := range res4.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

	res5, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%%optamised%%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5.Total) // >>> 1

	for _, doc := range res5.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryFtExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.brand", "brand"))
            .AddTextField(new FieldName("$.model", "model"))
            .AddTextField(new FieldName("$.description", "description"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[]
        {
            new
            {
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride " +
                                "for the smallest of tikes! This is the tiniest " +
                                "kids’ pedal bike on the market available without" +
                                " a coaster brake, the Jigger is the vehicle of " +
                                "choice for the rare tenacious little rider " +
                                "raring to go.",
                condition = "used"
            },
            new
            {
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible." +
                    " Especially on an incline! They may be at the age " +
                    "when a 27.5 inch wheel bike is just too clumsy coming " +
                    "off a 24 inch bike. The Hillcraft 26 is just the solution" +
                    " they need!",
                condition = "used",
            },
            new
            {
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older " +
                    "a durable and uberlight mountain bike for their first" +
                    " experience on tracks and easy cruising through forests" +
                    " and fields. The lower  top tube makes it easy to mount" +
                    " and dismount in any situation, giving your kids greater" +
                    " safety on the trails.",
                condition = "used",
            },
            new
            {
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the" +
                    " first and only women-dedicated bicycle brand. Designed" +
                    " by women for women, allEva bikes are optimized for the" +
                    " feminine physique using analytics from a body metrics" +
                    " database. If you like 29ers, try the Eva 291. It’s a " +
                    "brand new bike for 2022.. This full-suspension, " +
                    "cross-country ride has been designed for velocity. The" +
                    " 291 has 100mm of front and rear travel, a superlight " +
                    "aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used",
            },
            new
            {
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are " +
                    "looking for a lively trail bike that's just as inspiring" +
                    " on the climbs as it is over rougher ground, the Wilder" +
                    " is one heck of a bike built specifically for short women." +
                    " Both the frames and components have been tweaked to " +
                    "include a women’s saddle, different bars and unique " +
                    "colourway.",
                condition = "used",
            },
            new
            {
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
                    " not to say that it’s a basic machine. With an internal " +
                    "weld aluminium frame, a full carbon fork, and the slick-shifting" +
                    " Claris gears from Shimano’s, this is a bike which doesn’t" +
                    " break the bank and delivers craved performance.",
                condition = "new",
            },
            new
            {
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young" +
                    " at heart. It has a Bafang 1000W mid-drive system and a 48V" +
                    " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
                    " more than 60 miles on one charge. It’s great for tackling hilly" +
                    " terrain or if you just fancy a more leisurely ride. With three" +
                    " working modes, you can choose between E-bike, assisted bicycle," +
                    " and normal bike modes.",
                condition = "new",
            },
            new
            {
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after" +
                    " a few minutes on the road, this lightweight, aluminum bike" +
                    " alleviates those issues and allows you to enjoy the ride. From" +
                    " the ergonomic grips to the lumbar-supporting seat position, the" +
                    " Roll Low-Entry offers incredible comfort. The rear-inclined seat" +
                    " tube facilitates stability by allowing you to put a foot on the" +
                    " ground to balance at a stop, and the low step-over frame makes it" +
                    " accessible for all ability and mobility levels. The saddle is" +
                    " very soft, with a wide back to support your hip joints and a" +
                    " cutout in the center to redistribute that pressure. Rim brakes" +
                    " deliver satisfactory braking control, and the wide tires provide" +
                    " a smooth, stable ride on paved roads and gravel. Rack and fender" +
                    " mounts facilitate setting up the Roll Low-Entry as your preferred" +
                    " commuter, and the BMX-like handlebar offers space for mounting a" +
                    " flashlight, bell, or phone holder.",
                condition = "new",
            },
            new
            {
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike" +
                    " paths and on the trail. The fork with 100mm of travel absorbs" +
                    " rough terrain. Fat Kenda Booster tires give you grip in corners" +
                    " and on wet trails. The Shimano Tourney drivetrain offered enough" +
                    " gears for finding a comfortable pace to ride uphill, and the" +
                    " Tektro hydraulic disc brakes break smoothly. Whether you want an" +
                    " affordable bike that you can take to work, but also take trail in" +
                    " mountains on the weekends or you’re just after a stable," +
                    " comfortable ride for the bike path, the Summit gives a good value" +
                    " for money.",
                condition = "new",
            },
            new
            {
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is" +
                    " pretty: The ThrillCycle steel frame offers a smooth ride. A" +
                    " 9-speed drivetrain has enough gears for coasting in the city, but" +
                    " we wouldn’t suggest taking it to the mountains. Fenders protect" +
                    " you from mud, and a rear basket lets you transport groceries," +
                    " flowers and books. The ThrillCycle comes with a limited lifetime" +
                    " warranty, so this little guy will last you long past graduation.",
                condition = "refurbished",
            },
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        SearchResult res1 = db.FT().Search(
           "idx:bicycle",
           new("@description: kids")
       );
        Console.WriteLine(res1);    // >>> 2

        // Tests for 'ft1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new("@model: ka*")
        );
        Console.WriteLine(res2.TotalResults);   // >>> 1

        // Tests for 'ft2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@brand: *bikes")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 2

        // Tests for 'ft3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new("%optamized%")
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'ft4' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("%%optamised%%")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'ft5' step.

    }
}

```

## Word suffix

Similar to the prefix, it is also possible to search for words that share the same suffix.

```
FT.SEARCH index "*suffix"
```

You can also combine prefix- and suffix-based searches within a query expression.

```
FT.SEARCH index "*infix*"
```

Here is an example that finds all brands that end with 'bikes':

```plaintext
FT.SEARCH idx:bicycle "@brand:*bikes"
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.brand", as_name="brand"),
    TextField("$.model", as_name="model"),
    TextField("$.description", as_name="description"),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_em.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

res = index.search(Query("@description: kids"))
print(res.total)
# >>> 2

res = index.search(Query("@model: ka*"))
print(res.total)
# >>> 1

res = index.search(Query("@brand: *bikes"))
print(res.total)
# >>> 2

res = index.search(Query("%optamized%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

res = index.search(Query("%%optamised%%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.model': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'model'
  },
  '$.brand': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'brand'
  },
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
})

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_em.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', '@description: kids');
console.log(res1.total); // >>> 2

const res2 = await client.ft.search('idx:bicycle', '@model: ka*');
console.log(res2.total); // >>> 1

const res3 = await client.ft.search('idx:bicycle', '@brand: *bikes');
console.log(res3.total); // >>> 2

const res4 = await client.ft.search('idx:bicycle', '%optamized%');
console.log(res4); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

const res5 = await client.ft.search('idx:bicycle', '%%optamised%%');
console.log(res5); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

```

```java
import java.util.List;
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryFtExample {
    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition")
        };

        jedis.ftCreate("idx:bicycle",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("bicycle:"),
            schema
        );

        String[] bicycleJsons = new String[] {
            "  {"
            + "	  \"pickup_zone\": \"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, "
            + "-74.0610 40.6678, -74.0610 40.7578))\","
            + "	  \"store_location\": \"-74.0060,40.7128\","
            + "	  \"brand\": \"Velorim\","
            + "	  \"model\": \"Jigger\","
            + "	  \"price\": 270,"
            + "	  \"description\": \"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
            + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
            + "is the vehicle of choice for the rare tenacious little rider raring to go.\","
            + "	  \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, "
            + "-118.2887 33.9872, -118.2887 34.0972))\","
            + "	  \"store_location\": \"-118.2437,34.0522\","
            + "	  \"brand\": \"Bicyk\","
            + "	  \"model\": \"Hillcraft\","
            + "	  \"price\": 1200,"
            + "	  \"description\": \"Kids want to ride with as little weight as possible. Especially "
            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\","
            + "	  \"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, "
            + "-87.6848 41.8231, -87.6848 41.9331))\","
            + "	  \"store_location\": \"-87.6298,41.8781\","
            + "  	\"brand\": \"Nord\","
            + "  	\"model\": \"Chook air 5\","
            + "  	\"price\": 815,"
            + "  	\"description\": \"The Chook Air 5  gives kids aged six years and older a durable "
            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
            + "situation, giving your kids greater safety on the trails.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, "
            + "-80.2433 25.6967, -80.2433 25.8067))\","
            + "  	\"store_location\": \"-80.1918,25.7617\","
            + "  	\"brand\": \"Eva\","
            + "  	\"model\": \"Eva 291\","
            + "  	\"price\": 3400,"
            + "  	\"description\": \"The sister company to Nord, Eva launched in 2005 as the first "
            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
            + "are optimized for the feminine physique using analytics from a body metrics database. "
            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
            + "29-inch wheels. Yippee!\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, "
            + "-122.4644 37.7099, -122.4644 37.8199))\","
            + "  	\"store_location\": \"-122.4194,37.7749\","
            + "  	\"brand\": \"Noka Bikes\","
            + "  	\"model\": \"Kahuna\","
            + "  	\"price\": 3200,"
            + "  	\"description\": \"Whether you want to try your hand at XC racing or are looking "
            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
            + "frames and components have been tweaked to include a women’s saddle, different bars "
            + "and unique colourway.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, "
            + "-0.1778 51.4024, -0.1778 51.5524))\","
            + "    \"store_location\": \"-0.1278,51.5074\","
            + "    \"brand\": \"Breakout\","
            + "    \"model\": \"XBN 2.1 Alloy\","
            + "    \"price\": 810,"
            + "    \"description\": \"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
            + "doesn’t break the bank and delivers craved performance.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, "
            + "2.1767 48.5516, 2.1767 48.9016))\","
            + "    \"store_location\": \"2.3522,48.8566\","
            + "    \"brand\": \"ScramBikes\","
            + "    \"model\": \"WattBike\","
            + "    \"price\": 2300,"
            + "    \"description\": \"The WattBike is the best e-bike for people who still "
            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
            + "leisurely ride. With three working modes, you can choose between E-bike, "
            + "assisted bicycle, and normal bike modes.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, "
            + "13.3260 52.2700, 13.3260 52.5700))\","
            + "    \"store_location\": \"13.4050,52.5200\","
            + "    \"brand\": \"Peaknetic\","
            + "    \"model\": \"Secto\","
            + "    \"price\": 430,"
            + "    \"description\": \"If you struggle with stiff fingers or a kinked neck or "
            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
            + "on the ground to balance at a stop, and the low step-over frame makes it "
            + "accessible for all ability and mobility levels. The saddle is very soft, with "
            + "a wide back to support your hip joints and a cutout in the center to redistribute "
            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, "
            + "1.9450 41.1987, 1.9450 41.4301))\","
            + "    \"store_location\": \"2.1734, 41.3851\","
            + "    \"brand\": \"nHill\","
            + "    \"model\": \"Summit\","
            + "    \"price\": 1200,"
            + "    \"description\": \"This budget mountain bike from nHill performs well both "
            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
            + "Whether you want an affordable bike that you can take to work, but also take "
            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
            + "ride for the bike path, the Summit gives a good value for money.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((12.4464 42.1028, 12.5464 42.1028, "
            + "12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\","
            + "    \"store_location\": \"12.4964,41.9028\","
            + "    \"model\": \"ThrillCycle\","
            + "    \"brand\": \"BikeShind\","
            + "    \"price\": 815,"
            + "    \"description\": \"An artsy,  retro-inspired bicycle that’s as "
            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
            + "with a limited lifetime warranty, so this little guy will last you long "
            + "past graduation.\","
            + "    \"condition\": \"refurbished\""
            + "  }"
        };

        for (int i = 0; i < bicycleJsons.length; i++) {
            jedis.jsonSet("bicycle:" + i, Path2.ROOT_PATH, bicycleJsons[i]);
        }

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@description: kids");
        System.out.println(res1.getTotalResults()); // >>> 2

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:2
        // >>> bicycle:1

        // Tests for 'ft1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle", "@model: ka*");
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:4

        // Tests for 'ft2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@brand: *bikes");
        System.out.println(res3.getTotalResults()); // >>> 2

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:6
        // >>> bicycle:4

        // Tests for 'ft3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle", "%optamized%");
        System.out.println(res4.getTotalResults()); // >>> 1

        List<Document> docs4 = res4.getDocuments();

        for (int i = 0; i < docs4.size(); i++) {
            System.out.println(docs4.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft4' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle", "%%optamised%%");
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft5' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            asyncCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).toCompletableFuture().join();

            JsonParser parser = asyncCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<?>[] bikeFutures = new CompletableFuture[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = asyncCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i))
                        .toCompletableFuture();
            }

            CompletableFuture.allOf(bikeFutures).join();

            CompletableFuture<SearchReply<String, String>> descriptionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description: kids").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:1
                        // >>> ID: bicycle:2
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> startsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@model: ka*").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> endsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@brand: *bikes").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        // >>> ID: bicycle:6
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzyResults = asyncCommands.ftSearch("idx:bicycle", "%optamized%")
                    .thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzierResults = asyncCommands
                    .ftSearch("idx:bicycle", "%%optamised%%").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults)
                    .join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.reactive.RedisReactiveCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            reactiveCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).block();

            JsonParser parser = reactiveCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<?>[] bikeFutures = new Mono<?>[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = reactiveCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i));
            }

            Mono.when(bikeFutures).block();

            Mono<SearchReply<String, String>> descriptionResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description: kids").doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:1
                            // >>> ID: bicycle:2
                        });
                    });

            Mono<SearchReply<String, String>> startsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@model: ka*")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                        });
                    });

            Mono<SearchReply<String, String>> endsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@brand: *bikes")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                            // >>> ID: bicycle:6
                        });
                    });

            Mono<SearchReply<String, String>> fuzzyResults = reactiveCommands.ftSearch("idx:bicycle", "%optamized%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono<SearchReply<String, String>> fuzzierResults = reactiveCommands.ftSearch("idx:bicycle", "%%optamised%%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono.when(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults).block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"sort"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_ft() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	_, err := rdb.FTCreate(ctx, "idx:bicycle",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"bicycle:"},
		},
		&redis.FieldSchema{
			FieldName: "$.brand",
			As:        "brand",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.model",
			As:        "model",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.description",
			As:        "description",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.price",
			As:        "price",
			FieldType: redis.SearchFieldTypeNumeric,
		},
		&redis.FieldSchema{
			FieldName: "$.condition",
			As:        "condition",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	exampleJsons := []map[string]interface{}{
		{
			"pickup_zone": "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, " +
				"-74.0610 40.6678, -74.0610 40.7578))",
			"store_location": "-74.0060,40.7128",
			"brand":          "Velorim",
			"model":          "Jigger",
			"price":          270,
			"description": "Small and powerful, the Jigger is the best ride for the smallest of tikes! " +
				"This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger " +
				"is the vehicle of choice for the rare tenacious little rider raring to go.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, " +
				"-118.2887 33.9872, -118.2887 34.0972))",
			"store_location": "-118.2437,34.0522",
			"brand":          "Bicyk",
			"model":          "Hillcraft",
			"price":          1200,
			"description": "Kids want to ride with as little weight as possible. Especially " +
				"on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming " +
				"off a 24'' bike. The Hillcraft 26 is just the solution they need!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, " +
				"-87.6848 41.8231, -87.6848 41.9331))",
			"store_location": "-87.6298,41.8781",
			"brand":          "Nord",
			"model":          "Chook air 5",
			"price":          815,
			"description": "The Chook Air 5  gives kids aged six years and older a durable " +
				"and uberlight mountain bike for their first experience on tracks and easy cruising through " +
				"forests and fields. The lower  top tube makes it easy to mount and dismount in any " +
				"situation, giving your kids greater safety on the trails.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, " +
				"-80.2433 25.6967, -80.2433 25.8067))",
			"store_location": "-80.1918,25.7617",
			"brand":          "Eva",
			"model":          "Eva 291",
			"price":          3400,
			"description": "The sister company to Nord, Eva launched in 2005 as the first " +
				"and only women-dedicated bicycle brand. Designed by women for women, allEva bikes " +
				"are optimized for the feminine physique using analytics from a body metrics database. " +
				"If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This " +
				"full-suspension, cross-country ride has been designed for velocity. The 291 has " +
				"100mm of front and rear travel, a superlight aluminum frame and fast-rolling " +
				"29-inch wheels. Yippee!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, " +
				"-122.4644 37.7099, -122.4644 37.8199))",
			"store_location": "-122.4194,37.7749",
			"brand":          "Noka Bikes",
			"model":          "Kahuna",
			"price":          3200,
			"description": "Whether you want to try your hand at XC racing or are looking " +
				"for a lively trail bike that's just as inspiring on the climbs as it is over rougher " +
				"ground, the Wilder is one heck of a bike built specifically for short women. Both the " +
				"frames and components have been tweaked to include a women’s saddle, different bars " +
				"and unique colourway.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, " +
				"-0.1778 51.4024, -0.1778 51.5524))",
			"store_location": "-0.1278,51.5074",
			"brand":          "Breakout",
			"model":          "XBN 2.1 Alloy",
			"price":          810,
			"description": "The XBN 2.1 Alloy is our entry-level road bike – but that’s " +
				"not to say that it’s a basic machine. With an internal weld aluminium frame, a full " +
				"carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which " +
				"doesn’t break the bank and delivers craved performance.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, " +
				"2.1767 48.5516, 2.1767 48.9016))",
			"store_location": "2.3522,48.8566",
			"brand":          "ScramBikes",
			"model":          "WattBike",
			"price":          2300,
			"description": "The WattBike is the best e-bike for people who still " +
				"feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH " +
				"Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one " +
				"charge. It’s great for tackling hilly terrain or if you just fancy a more " +
				"leisurely ride. With three working modes, you can choose between E-bike, " +
				"assisted bicycle, and normal bike modes.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, " +
				"13.3260 52.2700, 13.3260 52.5700))",
			"store_location": "13.4050,52.5200",
			"brand":          "Peaknetic",
			"model":          "Secto",
			"price":          430,
			"description": "If you struggle with stiff fingers or a kinked neck or " +
				"back after a few minutes on the road, this lightweight, aluminum bike alleviates " +
				"those issues and allows you to enjoy the ride. From the ergonomic grips to the " +
				"lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. " +
				"The rear-inclined seat tube facilitates stability by allowing you to put a foot " +
				"on the ground to balance at a stop, and the low step-over frame makes it " +
				"accessible for all ability and mobility levels. The saddle is very soft, with " +
				"a wide back to support your hip joints and a cutout in the center to redistribute " +
				"that pressure. Rim brakes deliver satisfactory braking control, and the wide tires " +
				"provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts " +
				"facilitate setting up the Roll Low-Entry as your preferred commuter, and the " +
				"BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, " +
				"1.9450 41.1987, 1.9450 41.4301))",
			"store_location": "2.1734, 41.3851",
			"brand":          "nHill",
			"model":          "Summit",
			"price":          1200,
			"description": "This budget mountain bike from nHill performs well both " +
				"on bike paths and on the trail. The fork with 100mm of travel absorbs rough " +
				"terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. " +
				"The Shimano Tourney drivetrain offered enough gears for finding a comfortable " +
				"pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. " +
				"Whether you want an affordable bike that you can take to work, but also take " +
				"trail in mountains on the weekends or you’re just after a stable, comfortable " +
				"ride for the bike path, the Summit gives a good value for money.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((12.4464 42.1028, 12.5464 42.1028, " +
				"12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
			"store_location": "12.4964,41.9028",
			"model":          "ThrillCycle",
			"brand":          "BikeShind",
			"price":          815,
			"description": "An artsy,  retro-inspired bicycle that’s as " +
				"functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. " +
				"A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t " +
				"suggest taking it to the mountains. Fenders protect you from mud, and a rear " +
				"basket lets you transport groceries, flowers and books. The ThrillCycle comes " +
				"with a limited lifetime warranty, so this little guy will last you long " +
				"past graduation.",
			"condition": "refurbished",
		},
	}

	for i, json := range exampleJsons {
		_, err := rdb.JSONSet(ctx, fmt.Sprintf("bicycle:%v", i), "$", json).Result()

		if err != nil {
			panic(err)
		}
	}

	res1, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description: kids",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 2

	sort.Slice(res1.Docs, func(i, j int) bool {
		return res1.Docs[i].ID < res1.Docs[j].ID
	})

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:1
	// >>> bicycle:2

	res2, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@model: ka*",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@brand: *bikes",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 2

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})
	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4
	// >>> bicycle:6

	res4, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%optamized%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 1

	for _, doc := range res4.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

	res5, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%%optamised%%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5.Total) // >>> 1

	for _, doc := range res5.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryFtExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.brand", "brand"))
            .AddTextField(new FieldName("$.model", "model"))
            .AddTextField(new FieldName("$.description", "description"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[]
        {
            new
            {
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride " +
                                "for the smallest of tikes! This is the tiniest " +
                                "kids’ pedal bike on the market available without" +
                                " a coaster brake, the Jigger is the vehicle of " +
                                "choice for the rare tenacious little rider " +
                                "raring to go.",
                condition = "used"
            },
            new
            {
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible." +
                    " Especially on an incline! They may be at the age " +
                    "when a 27.5 inch wheel bike is just too clumsy coming " +
                    "off a 24 inch bike. The Hillcraft 26 is just the solution" +
                    " they need!",
                condition = "used",
            },
            new
            {
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older " +
                    "a durable and uberlight mountain bike for their first" +
                    " experience on tracks and easy cruising through forests" +
                    " and fields. The lower  top tube makes it easy to mount" +
                    " and dismount in any situation, giving your kids greater" +
                    " safety on the trails.",
                condition = "used",
            },
            new
            {
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the" +
                    " first and only women-dedicated bicycle brand. Designed" +
                    " by women for women, allEva bikes are optimized for the" +
                    " feminine physique using analytics from a body metrics" +
                    " database. If you like 29ers, try the Eva 291. It’s a " +
                    "brand new bike for 2022.. This full-suspension, " +
                    "cross-country ride has been designed for velocity. The" +
                    " 291 has 100mm of front and rear travel, a superlight " +
                    "aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used",
            },
            new
            {
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are " +
                    "looking for a lively trail bike that's just as inspiring" +
                    " on the climbs as it is over rougher ground, the Wilder" +
                    " is one heck of a bike built specifically for short women." +
                    " Both the frames and components have been tweaked to " +
                    "include a women’s saddle, different bars and unique " +
                    "colourway.",
                condition = "used",
            },
            new
            {
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
                    " not to say that it’s a basic machine. With an internal " +
                    "weld aluminium frame, a full carbon fork, and the slick-shifting" +
                    " Claris gears from Shimano’s, this is a bike which doesn’t" +
                    " break the bank and delivers craved performance.",
                condition = "new",
            },
            new
            {
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young" +
                    " at heart. It has a Bafang 1000W mid-drive system and a 48V" +
                    " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
                    " more than 60 miles on one charge. It’s great for tackling hilly" +
                    " terrain or if you just fancy a more leisurely ride. With three" +
                    " working modes, you can choose between E-bike, assisted bicycle," +
                    " and normal bike modes.",
                condition = "new",
            },
            new
            {
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after" +
                    " a few minutes on the road, this lightweight, aluminum bike" +
                    " alleviates those issues and allows you to enjoy the ride. From" +
                    " the ergonomic grips to the lumbar-supporting seat position, the" +
                    " Roll Low-Entry offers incredible comfort. The rear-inclined seat" +
                    " tube facilitates stability by allowing you to put a foot on the" +
                    " ground to balance at a stop, and the low step-over frame makes it" +
                    " accessible for all ability and mobility levels. The saddle is" +
                    " very soft, with a wide back to support your hip joints and a" +
                    " cutout in the center to redistribute that pressure. Rim brakes" +
                    " deliver satisfactory braking control, and the wide tires provide" +
                    " a smooth, stable ride on paved roads and gravel. Rack and fender" +
                    " mounts facilitate setting up the Roll Low-Entry as your preferred" +
                    " commuter, and the BMX-like handlebar offers space for mounting a" +
                    " flashlight, bell, or phone holder.",
                condition = "new",
            },
            new
            {
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike" +
                    " paths and on the trail. The fork with 100mm of travel absorbs" +
                    " rough terrain. Fat Kenda Booster tires give you grip in corners" +
                    " and on wet trails. The Shimano Tourney drivetrain offered enough" +
                    " gears for finding a comfortable pace to ride uphill, and the" +
                    " Tektro hydraulic disc brakes break smoothly. Whether you want an" +
                    " affordable bike that you can take to work, but also take trail in" +
                    " mountains on the weekends or you’re just after a stable," +
                    " comfortable ride for the bike path, the Summit gives a good value" +
                    " for money.",
                condition = "new",
            },
            new
            {
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is" +
                    " pretty: The ThrillCycle steel frame offers a smooth ride. A" +
                    " 9-speed drivetrain has enough gears for coasting in the city, but" +
                    " we wouldn’t suggest taking it to the mountains. Fenders protect" +
                    " you from mud, and a rear basket lets you transport groceries," +
                    " flowers and books. The ThrillCycle comes with a limited lifetime" +
                    " warranty, so this little guy will last you long past graduation.",
                condition = "refurbished",
            },
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        SearchResult res1 = db.FT().Search(
           "idx:bicycle",
           new("@description: kids")
       );
        Console.WriteLine(res1);    // >>> 2

        // Tests for 'ft1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new("@model: ka*")
        );
        Console.WriteLine(res2.TotalResults);   // >>> 1

        // Tests for 'ft2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@brand: *bikes")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 2

        // Tests for 'ft3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new("%optamized%")
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'ft4' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("%%optamised%%")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'ft5' step.

    }
}

```

## Fuzzy search

A fuzzy search allows you to find documents with words that approximately match your search term. To perform a fuzzy search, you wrap search terms with pairs of `%` characters. A single pair represents a (Levenshtein) distance of one, two pairs represent a distance of two, and three pairs, the maximum distance, represents a distance of three.

Here is the command that searches across all text fields with a distance of one:

```
FT.SEARCH index "%word%"
```

The following example finds all documents that contain a word that has a distance of one to the incorrectly spelled word 'optamized'. You can see that this matches the word 'optimized'.

```plaintext
FT.SEARCH idx:bicycle "%optamized%"
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.brand", as_name="brand"),
    TextField("$.model", as_name="model"),
    TextField("$.description", as_name="description"),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_em.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

res = index.search(Query("@description: kids"))
print(res.total)
# >>> 2

res = index.search(Query("@model: ka*"))
print(res.total)
# >>> 1

res = index.search(Query("@brand: *bikes"))
print(res.total)
# >>> 2

res = index.search(Query("%optamized%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

res = index.search(Query("%%optamised%%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.model': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'model'
  },
  '$.brand': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'brand'
  },
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
})

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_em.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', '@description: kids');
console.log(res1.total); // >>> 2

const res2 = await client.ft.search('idx:bicycle', '@model: ka*');
console.log(res2.total); // >>> 1

const res3 = await client.ft.search('idx:bicycle', '@brand: *bikes');
console.log(res3.total); // >>> 2

const res4 = await client.ft.search('idx:bicycle', '%optamized%');
console.log(res4); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

const res5 = await client.ft.search('idx:bicycle', '%%optamised%%');
console.log(res5); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

```

```java
import java.util.List;
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryFtExample {
    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition")
        };

        jedis.ftCreate("idx:bicycle",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("bicycle:"),
            schema
        );

        String[] bicycleJsons = new String[] {
            "  {"
            + "	  \"pickup_zone\": \"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, "
            + "-74.0610 40.6678, -74.0610 40.7578))\","
            + "	  \"store_location\": \"-74.0060,40.7128\","
            + "	  \"brand\": \"Velorim\","
            + "	  \"model\": \"Jigger\","
            + "	  \"price\": 270,"
            + "	  \"description\": \"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
            + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
            + "is the vehicle of choice for the rare tenacious little rider raring to go.\","
            + "	  \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, "
            + "-118.2887 33.9872, -118.2887 34.0972))\","
            + "	  \"store_location\": \"-118.2437,34.0522\","
            + "	  \"brand\": \"Bicyk\","
            + "	  \"model\": \"Hillcraft\","
            + "	  \"price\": 1200,"
            + "	  \"description\": \"Kids want to ride with as little weight as possible. Especially "
            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\","
            + "	  \"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, "
            + "-87.6848 41.8231, -87.6848 41.9331))\","
            + "	  \"store_location\": \"-87.6298,41.8781\","
            + "  	\"brand\": \"Nord\","
            + "  	\"model\": \"Chook air 5\","
            + "  	\"price\": 815,"
            + "  	\"description\": \"The Chook Air 5  gives kids aged six years and older a durable "
            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
            + "situation, giving your kids greater safety on the trails.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, "
            + "-80.2433 25.6967, -80.2433 25.8067))\","
            + "  	\"store_location\": \"-80.1918,25.7617\","
            + "  	\"brand\": \"Eva\","
            + "  	\"model\": \"Eva 291\","
            + "  	\"price\": 3400,"
            + "  	\"description\": \"The sister company to Nord, Eva launched in 2005 as the first "
            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
            + "are optimized for the feminine physique using analytics from a body metrics database. "
            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
            + "29-inch wheels. Yippee!\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, "
            + "-122.4644 37.7099, -122.4644 37.8199))\","
            + "  	\"store_location\": \"-122.4194,37.7749\","
            + "  	\"brand\": \"Noka Bikes\","
            + "  	\"model\": \"Kahuna\","
            + "  	\"price\": 3200,"
            + "  	\"description\": \"Whether you want to try your hand at XC racing or are looking "
            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
            + "frames and components have been tweaked to include a women’s saddle, different bars "
            + "and unique colourway.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, "
            + "-0.1778 51.4024, -0.1778 51.5524))\","
            + "    \"store_location\": \"-0.1278,51.5074\","
            + "    \"brand\": \"Breakout\","
            + "    \"model\": \"XBN 2.1 Alloy\","
            + "    \"price\": 810,"
            + "    \"description\": \"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
            + "doesn’t break the bank and delivers craved performance.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, "
            + "2.1767 48.5516, 2.1767 48.9016))\","
            + "    \"store_location\": \"2.3522,48.8566\","
            + "    \"brand\": \"ScramBikes\","
            + "    \"model\": \"WattBike\","
            + "    \"price\": 2300,"
            + "    \"description\": \"The WattBike is the best e-bike for people who still "
            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
            + "leisurely ride. With three working modes, you can choose between E-bike, "
            + "assisted bicycle, and normal bike modes.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, "
            + "13.3260 52.2700, 13.3260 52.5700))\","
            + "    \"store_location\": \"13.4050,52.5200\","
            + "    \"brand\": \"Peaknetic\","
            + "    \"model\": \"Secto\","
            + "    \"price\": 430,"
            + "    \"description\": \"If you struggle with stiff fingers or a kinked neck or "
            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
            + "on the ground to balance at a stop, and the low step-over frame makes it "
            + "accessible for all ability and mobility levels. The saddle is very soft, with "
            + "a wide back to support your hip joints and a cutout in the center to redistribute "
            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, "
            + "1.9450 41.1987, 1.9450 41.4301))\","
            + "    \"store_location\": \"2.1734, 41.3851\","
            + "    \"brand\": \"nHill\","
            + "    \"model\": \"Summit\","
            + "    \"price\": 1200,"
            + "    \"description\": \"This budget mountain bike from nHill performs well both "
            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
            + "Whether you want an affordable bike that you can take to work, but also take "
            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
            + "ride for the bike path, the Summit gives a good value for money.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((12.4464 42.1028, 12.5464 42.1028, "
            + "12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\","
            + "    \"store_location\": \"12.4964,41.9028\","
            + "    \"model\": \"ThrillCycle\","
            + "    \"brand\": \"BikeShind\","
            + "    \"price\": 815,"
            + "    \"description\": \"An artsy,  retro-inspired bicycle that’s as "
            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
            + "with a limited lifetime warranty, so this little guy will last you long "
            + "past graduation.\","
            + "    \"condition\": \"refurbished\""
            + "  }"
        };

        for (int i = 0; i < bicycleJsons.length; i++) {
            jedis.jsonSet("bicycle:" + i, Path2.ROOT_PATH, bicycleJsons[i]);
        }

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@description: kids");
        System.out.println(res1.getTotalResults()); // >>> 2

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:2
        // >>> bicycle:1

        // Tests for 'ft1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle", "@model: ka*");
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:4

        // Tests for 'ft2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@brand: *bikes");
        System.out.println(res3.getTotalResults()); // >>> 2

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:6
        // >>> bicycle:4

        // Tests for 'ft3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle", "%optamized%");
        System.out.println(res4.getTotalResults()); // >>> 1

        List<Document> docs4 = res4.getDocuments();

        for (int i = 0; i < docs4.size(); i++) {
            System.out.println(docs4.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft4' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle", "%%optamised%%");
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft5' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            asyncCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).toCompletableFuture().join();

            JsonParser parser = asyncCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<?>[] bikeFutures = new CompletableFuture[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = asyncCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i))
                        .toCompletableFuture();
            }

            CompletableFuture.allOf(bikeFutures).join();

            CompletableFuture<SearchReply<String, String>> descriptionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description: kids").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:1
                        // >>> ID: bicycle:2
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> startsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@model: ka*").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> endsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@brand: *bikes").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        // >>> ID: bicycle:6
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzyResults = asyncCommands.ftSearch("idx:bicycle", "%optamized%")
                    .thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzierResults = asyncCommands
                    .ftSearch("idx:bicycle", "%%optamised%%").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults)
                    .join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.reactive.RedisReactiveCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            reactiveCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).block();

            JsonParser parser = reactiveCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<?>[] bikeFutures = new Mono<?>[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = reactiveCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i));
            }

            Mono.when(bikeFutures).block();

            Mono<SearchReply<String, String>> descriptionResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description: kids").doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:1
                            // >>> ID: bicycle:2
                        });
                    });

            Mono<SearchReply<String, String>> startsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@model: ka*")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                        });
                    });

            Mono<SearchReply<String, String>> endsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@brand: *bikes")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                            // >>> ID: bicycle:6
                        });
                    });

            Mono<SearchReply<String, String>> fuzzyResults = reactiveCommands.ftSearch("idx:bicycle", "%optamized%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono<SearchReply<String, String>> fuzzierResults = reactiveCommands.ftSearch("idx:bicycle", "%%optamised%%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono.when(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults).block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"sort"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_ft() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	_, err := rdb.FTCreate(ctx, "idx:bicycle",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"bicycle:"},
		},
		&redis.FieldSchema{
			FieldName: "$.brand",
			As:        "brand",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.model",
			As:        "model",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.description",
			As:        "description",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.price",
			As:        "price",
			FieldType: redis.SearchFieldTypeNumeric,
		},
		&redis.FieldSchema{
			FieldName: "$.condition",
			As:        "condition",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	exampleJsons := []map[string]interface{}{
		{
			"pickup_zone": "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, " +
				"-74.0610 40.6678, -74.0610 40.7578))",
			"store_location": "-74.0060,40.7128",
			"brand":          "Velorim",
			"model":          "Jigger",
			"price":          270,
			"description": "Small and powerful, the Jigger is the best ride for the smallest of tikes! " +
				"This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger " +
				"is the vehicle of choice for the rare tenacious little rider raring to go.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, " +
				"-118.2887 33.9872, -118.2887 34.0972))",
			"store_location": "-118.2437,34.0522",
			"brand":          "Bicyk",
			"model":          "Hillcraft",
			"price":          1200,
			"description": "Kids want to ride with as little weight as possible. Especially " +
				"on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming " +
				"off a 24'' bike. The Hillcraft 26 is just the solution they need!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, " +
				"-87.6848 41.8231, -87.6848 41.9331))",
			"store_location": "-87.6298,41.8781",
			"brand":          "Nord",
			"model":          "Chook air 5",
			"price":          815,
			"description": "The Chook Air 5  gives kids aged six years and older a durable " +
				"and uberlight mountain bike for their first experience on tracks and easy cruising through " +
				"forests and fields. The lower  top tube makes it easy to mount and dismount in any " +
				"situation, giving your kids greater safety on the trails.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, " +
				"-80.2433 25.6967, -80.2433 25.8067))",
			"store_location": "-80.1918,25.7617",
			"brand":          "Eva",
			"model":          "Eva 291",
			"price":          3400,
			"description": "The sister company to Nord, Eva launched in 2005 as the first " +
				"and only women-dedicated bicycle brand. Designed by women for women, allEva bikes " +
				"are optimized for the feminine physique using analytics from a body metrics database. " +
				"If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This " +
				"full-suspension, cross-country ride has been designed for velocity. The 291 has " +
				"100mm of front and rear travel, a superlight aluminum frame and fast-rolling " +
				"29-inch wheels. Yippee!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, " +
				"-122.4644 37.7099, -122.4644 37.8199))",
			"store_location": "-122.4194,37.7749",
			"brand":          "Noka Bikes",
			"model":          "Kahuna",
			"price":          3200,
			"description": "Whether you want to try your hand at XC racing or are looking " +
				"for a lively trail bike that's just as inspiring on the climbs as it is over rougher " +
				"ground, the Wilder is one heck of a bike built specifically for short women. Both the " +
				"frames and components have been tweaked to include a women’s saddle, different bars " +
				"and unique colourway.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, " +
				"-0.1778 51.4024, -0.1778 51.5524))",
			"store_location": "-0.1278,51.5074",
			"brand":          "Breakout",
			"model":          "XBN 2.1 Alloy",
			"price":          810,
			"description": "The XBN 2.1 Alloy is our entry-level road bike – but that’s " +
				"not to say that it’s a basic machine. With an internal weld aluminium frame, a full " +
				"carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which " +
				"doesn’t break the bank and delivers craved performance.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, " +
				"2.1767 48.5516, 2.1767 48.9016))",
			"store_location": "2.3522,48.8566",
			"brand":          "ScramBikes",
			"model":          "WattBike",
			"price":          2300,
			"description": "The WattBike is the best e-bike for people who still " +
				"feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH " +
				"Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one " +
				"charge. It’s great for tackling hilly terrain or if you just fancy a more " +
				"leisurely ride. With three working modes, you can choose between E-bike, " +
				"assisted bicycle, and normal bike modes.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, " +
				"13.3260 52.2700, 13.3260 52.5700))",
			"store_location": "13.4050,52.5200",
			"brand":          "Peaknetic",
			"model":          "Secto",
			"price":          430,
			"description": "If you struggle with stiff fingers or a kinked neck or " +
				"back after a few minutes on the road, this lightweight, aluminum bike alleviates " +
				"those issues and allows you to enjoy the ride. From the ergonomic grips to the " +
				"lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. " +
				"The rear-inclined seat tube facilitates stability by allowing you to put a foot " +
				"on the ground to balance at a stop, and the low step-over frame makes it " +
				"accessible for all ability and mobility levels. The saddle is very soft, with " +
				"a wide back to support your hip joints and a cutout in the center to redistribute " +
				"that pressure. Rim brakes deliver satisfactory braking control, and the wide tires " +
				"provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts " +
				"facilitate setting up the Roll Low-Entry as your preferred commuter, and the " +
				"BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, " +
				"1.9450 41.1987, 1.9450 41.4301))",
			"store_location": "2.1734, 41.3851",
			"brand":          "nHill",
			"model":          "Summit",
			"price":          1200,
			"description": "This budget mountain bike from nHill performs well both " +
				"on bike paths and on the trail. The fork with 100mm of travel absorbs rough " +
				"terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. " +
				"The Shimano Tourney drivetrain offered enough gears for finding a comfortable " +
				"pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. " +
				"Whether you want an affordable bike that you can take to work, but also take " +
				"trail in mountains on the weekends or you’re just after a stable, comfortable " +
				"ride for the bike path, the Summit gives a good value for money.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((12.4464 42.1028, 12.5464 42.1028, " +
				"12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
			"store_location": "12.4964,41.9028",
			"model":          "ThrillCycle",
			"brand":          "BikeShind",
			"price":          815,
			"description": "An artsy,  retro-inspired bicycle that’s as " +
				"functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. " +
				"A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t " +
				"suggest taking it to the mountains. Fenders protect you from mud, and a rear " +
				"basket lets you transport groceries, flowers and books. The ThrillCycle comes " +
				"with a limited lifetime warranty, so this little guy will last you long " +
				"past graduation.",
			"condition": "refurbished",
		},
	}

	for i, json := range exampleJsons {
		_, err := rdb.JSONSet(ctx, fmt.Sprintf("bicycle:%v", i), "$", json).Result()

		if err != nil {
			panic(err)
		}
	}

	res1, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description: kids",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 2

	sort.Slice(res1.Docs, func(i, j int) bool {
		return res1.Docs[i].ID < res1.Docs[j].ID
	})

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:1
	// >>> bicycle:2

	res2, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@model: ka*",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@brand: *bikes",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 2

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})
	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4
	// >>> bicycle:6

	res4, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%optamized%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 1

	for _, doc := range res4.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

	res5, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%%optamised%%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5.Total) // >>> 1

	for _, doc := range res5.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryFtExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.brand", "brand"))
            .AddTextField(new FieldName("$.model", "model"))
            .AddTextField(new FieldName("$.description", "description"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[]
        {
            new
            {
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride " +
                                "for the smallest of tikes! This is the tiniest " +
                                "kids’ pedal bike on the market available without" +
                                " a coaster brake, the Jigger is the vehicle of " +
                                "choice for the rare tenacious little rider " +
                                "raring to go.",
                condition = "used"
            },
            new
            {
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible." +
                    " Especially on an incline! They may be at the age " +
                    "when a 27.5 inch wheel bike is just too clumsy coming " +
                    "off a 24 inch bike. The Hillcraft 26 is just the solution" +
                    " they need!",
                condition = "used",
            },
            new
            {
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older " +
                    "a durable and uberlight mountain bike for their first" +
                    " experience on tracks and easy cruising through forests" +
                    " and fields. The lower  top tube makes it easy to mount" +
                    " and dismount in any situation, giving your kids greater" +
                    " safety on the trails.",
                condition = "used",
            },
            new
            {
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the" +
                    " first and only women-dedicated bicycle brand. Designed" +
                    " by women for women, allEva bikes are optimized for the" +
                    " feminine physique using analytics from a body metrics" +
                    " database. If you like 29ers, try the Eva 291. It’s a " +
                    "brand new bike for 2022.. This full-suspension, " +
                    "cross-country ride has been designed for velocity. The" +
                    " 291 has 100mm of front and rear travel, a superlight " +
                    "aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used",
            },
            new
            {
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are " +
                    "looking for a lively trail bike that's just as inspiring" +
                    " on the climbs as it is over rougher ground, the Wilder" +
                    " is one heck of a bike built specifically for short women." +
                    " Both the frames and components have been tweaked to " +
                    "include a women’s saddle, different bars and unique " +
                    "colourway.",
                condition = "used",
            },
            new
            {
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
                    " not to say that it’s a basic machine. With an internal " +
                    "weld aluminium frame, a full carbon fork, and the slick-shifting" +
                    " Claris gears from Shimano’s, this is a bike which doesn’t" +
                    " break the bank and delivers craved performance.",
                condition = "new",
            },
            new
            {
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young" +
                    " at heart. It has a Bafang 1000W mid-drive system and a 48V" +
                    " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
                    " more than 60 miles on one charge. It’s great for tackling hilly" +
                    " terrain or if you just fancy a more leisurely ride. With three" +
                    " working modes, you can choose between E-bike, assisted bicycle," +
                    " and normal bike modes.",
                condition = "new",
            },
            new
            {
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after" +
                    " a few minutes on the road, this lightweight, aluminum bike" +
                    " alleviates those issues and allows you to enjoy the ride. From" +
                    " the ergonomic grips to the lumbar-supporting seat position, the" +
                    " Roll Low-Entry offers incredible comfort. The rear-inclined seat" +
                    " tube facilitates stability by allowing you to put a foot on the" +
                    " ground to balance at a stop, and the low step-over frame makes it" +
                    " accessible for all ability and mobility levels. The saddle is" +
                    " very soft, with a wide back to support your hip joints and a" +
                    " cutout in the center to redistribute that pressure. Rim brakes" +
                    " deliver satisfactory braking control, and the wide tires provide" +
                    " a smooth, stable ride on paved roads and gravel. Rack and fender" +
                    " mounts facilitate setting up the Roll Low-Entry as your preferred" +
                    " commuter, and the BMX-like handlebar offers space for mounting a" +
                    " flashlight, bell, or phone holder.",
                condition = "new",
            },
            new
            {
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike" +
                    " paths and on the trail. The fork with 100mm of travel absorbs" +
                    " rough terrain. Fat Kenda Booster tires give you grip in corners" +
                    " and on wet trails. The Shimano Tourney drivetrain offered enough" +
                    " gears for finding a comfortable pace to ride uphill, and the" +
                    " Tektro hydraulic disc brakes break smoothly. Whether you want an" +
                    " affordable bike that you can take to work, but also take trail in" +
                    " mountains on the weekends or you’re just after a stable," +
                    " comfortable ride for the bike path, the Summit gives a good value" +
                    " for money.",
                condition = "new",
            },
            new
            {
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is" +
                    " pretty: The ThrillCycle steel frame offers a smooth ride. A" +
                    " 9-speed drivetrain has enough gears for coasting in the city, but" +
                    " we wouldn’t suggest taking it to the mountains. Fenders protect" +
                    " you from mud, and a rear basket lets you transport groceries," +
                    " flowers and books. The ThrillCycle comes with a limited lifetime" +
                    " warranty, so this little guy will last you long past graduation.",
                condition = "refurbished",
            },
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        SearchResult res1 = db.FT().Search(
           "idx:bicycle",
           new("@description: kids")
       );
        Console.WriteLine(res1);    // >>> 2

        // Tests for 'ft1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new("@model: ka*")
        );
        Console.WriteLine(res2.TotalResults);   // >>> 1

        // Tests for 'ft2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@brand: *bikes")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 2

        // Tests for 'ft3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new("%optamized%")
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'ft4' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("%%optamised%%")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'ft5' step.

    }
}

```

If you want to increase the maximum word distance to two, you can use the following query:

```plaintext
FT.SEARCH idx:bicycle "%%optamised%%"
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.brand", as_name="brand"),
    TextField("$.model", as_name="model"),
    TextField("$.description", as_name="description"),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_em.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

res = index.search(Query("@description: kids"))
print(res.total)
# >>> 2

res = index.search(Query("@model: ka*"))
print(res.total)
# >>> 1

res = index.search(Query("@brand: *bikes"))
print(res.total)
# >>> 2

res = index.search(Query("%optamized%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

res = index.search(Query("%%optamised%%"))
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:3', 'payload': None, 'json': '{"pickup_zone":"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))","store_location":"-80.1918,25.7617","brand":"Eva","model":"Eva 291","price":3400,"description":"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!","condition":"used"}'}]}

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.model': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'model'
  },
  '$.brand': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'brand'
  },
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
})

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_em.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', '@description: kids');
console.log(res1.total); // >>> 2

const res2 = await client.ft.search('idx:bicycle', '@model: ka*');
console.log(res2.total); // >>> 1

const res3 = await client.ft.search('idx:bicycle', '@brand: *bikes');
console.log(res3.total); // >>> 2

const res4 = await client.ft.search('idx:bicycle', '%optamized%');
console.log(res4); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

const res5 = await client.ft.search('idx:bicycle', '%%optamised%%');
console.log(res5); // >>> { total: 1, documents: [ { id: 'bicycle:3', value: [Object: null prototype] } ]}

```

```java
import java.util.List;
import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryFtExample {
    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition")
        };

        jedis.ftCreate("idx:bicycle",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("bicycle:"),
            schema
        );

        String[] bicycleJsons = new String[] {
            "  {"
            + "	  \"pickup_zone\": \"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, "
            + "-74.0610 40.6678, -74.0610 40.7578))\","
            + "	  \"store_location\": \"-74.0060,40.7128\","
            + "	  \"brand\": \"Velorim\","
            + "	  \"model\": \"Jigger\","
            + "	  \"price\": 270,"
            + "	  \"description\": \"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
            + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
            + "is the vehicle of choice for the rare tenacious little rider raring to go.\","
            + "	  \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, "
            + "-118.2887 33.9872, -118.2887 34.0972))\","
            + "	  \"store_location\": \"-118.2437,34.0522\","
            + "	  \"brand\": \"Bicyk\","
            + "	  \"model\": \"Hillcraft\","
            + "	  \"price\": 1200,"
            + "	  \"description\": \"Kids want to ride with as little weight as possible. Especially "
            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\","
            + "	  \"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, "
            + "-87.6848 41.8231, -87.6848 41.9331))\","
            + "	  \"store_location\": \"-87.6298,41.8781\","
            + "  	\"brand\": \"Nord\","
            + "  	\"model\": \"Chook air 5\","
            + "  	\"price\": 815,"
            + "  	\"description\": \"The Chook Air 5  gives kids aged six years and older a durable "
            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
            + "situation, giving your kids greater safety on the trails.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, "
            + "-80.2433 25.6967, -80.2433 25.8067))\","
            + "  	\"store_location\": \"-80.1918,25.7617\","
            + "  	\"brand\": \"Eva\","
            + "  	\"model\": \"Eva 291\","
            + "  	\"price\": 3400,"
            + "  	\"description\": \"The sister company to Nord, Eva launched in 2005 as the first "
            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
            + "are optimized for the feminine physique using analytics from a body metrics database. "
            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
            + "29-inch wheels. Yippee!\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, "
            + "-122.4644 37.7099, -122.4644 37.8199))\","
            + "  	\"store_location\": \"-122.4194,37.7749\","
            + "  	\"brand\": \"Noka Bikes\","
            + "  	\"model\": \"Kahuna\","
            + "  	\"price\": 3200,"
            + "  	\"description\": \"Whether you want to try your hand at XC racing or are looking "
            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
            + "frames and components have been tweaked to include a women’s saddle, different bars "
            + "and unique colourway.\","
            + "  	\"condition\": \"used\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, "
            + "-0.1778 51.4024, -0.1778 51.5524))\","
            + "    \"store_location\": \"-0.1278,51.5074\","
            + "    \"brand\": \"Breakout\","
            + "    \"model\": \"XBN 2.1 Alloy\","
            + "    \"price\": 810,"
            + "    \"description\": \"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
            + "doesn’t break the bank and delivers craved performance.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, "
            + "2.1767 48.5516, 2.1767 48.9016))\","
            + "    \"store_location\": \"2.3522,48.8566\","
            + "    \"brand\": \"ScramBikes\","
            + "    \"model\": \"WattBike\","
            + "    \"price\": 2300,"
            + "    \"description\": \"The WattBike is the best e-bike for people who still "
            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
            + "leisurely ride. With three working modes, you can choose between E-bike, "
            + "assisted bicycle, and normal bike modes.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, "
            + "13.3260 52.2700, 13.3260 52.5700))\","
            + "    \"store_location\": \"13.4050,52.5200\","
            + "    \"brand\": \"Peaknetic\","
            + "    \"model\": \"Secto\","
            + "    \"price\": 430,"
            + "    \"description\": \"If you struggle with stiff fingers or a kinked neck or "
            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
            + "on the ground to balance at a stop, and the low step-over frame makes it "
            + "accessible for all ability and mobility levels. The saddle is very soft, with "
            + "a wide back to support your hip joints and a cutout in the center to redistribute "
            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, "
            + "1.9450 41.1987, 1.9450 41.4301))\","
            + "    \"store_location\": \"2.1734, 41.3851\","
            + "    \"brand\": \"nHill\","
            + "    \"model\": \"Summit\","
            + "    \"price\": 1200,"
            + "    \"description\": \"This budget mountain bike from nHill performs well both "
            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
            + "Whether you want an affordable bike that you can take to work, but also take "
            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
            + "ride for the bike path, the Summit gives a good value for money.\","
            + "    \"condition\": \"new\""
            + "  }",

            "  {"
            + "    \"pickup_zone\": \"POLYGON((12.4464 42.1028, 12.5464 42.1028, "
            + "12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\","
            + "    \"store_location\": \"12.4964,41.9028\","
            + "    \"model\": \"ThrillCycle\","
            + "    \"brand\": \"BikeShind\","
            + "    \"price\": 815,"
            + "    \"description\": \"An artsy,  retro-inspired bicycle that’s as "
            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
            + "with a limited lifetime warranty, so this little guy will last you long "
            + "past graduation.\","
            + "    \"condition\": \"refurbished\""
            + "  }"
        };

        for (int i = 0; i < bicycleJsons.length; i++) {
            jedis.jsonSet("bicycle:" + i, Path2.ROOT_PATH, bicycleJsons[i]);
        }

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@description: kids");
        System.out.println(res1.getTotalResults()); // >>> 2

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:2
        // >>> bicycle:1

        // Tests for 'ft1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle", "@model: ka*");
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:4

        // Tests for 'ft2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@brand: *bikes");
        System.out.println(res3.getTotalResults()); // >>> 2

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:6
        // >>> bicycle:4

        // Tests for 'ft3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle", "%optamized%");
        System.out.println(res4.getTotalResults()); // >>> 1

        List<Document> docs4 = res4.getDocuments();

        for (int i = 0; i < docs4.size(); i++) {
            System.out.println(docs4.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft4' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle", "%%optamised%%");
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:3

        // Tests for 'ft5' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            asyncCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).toCompletableFuture().join();

            JsonParser parser = asyncCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<?>[] bikeFutures = new CompletableFuture[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = asyncCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i))
                        .toCompletableFuture();
            }

            CompletableFuture.allOf(bikeFutures).join();

            CompletableFuture<SearchReply<String, String>> descriptionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description: kids").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:1
                        // >>> ID: bicycle:2
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> startsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@model: ka*").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> endsWithResults = asyncCommands
                    .ftSearch("idx:bicycle", "@brand: *bikes").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:4
                        // >>> ID: bicycle:6
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzyResults = asyncCommands.ftSearch("idx:bicycle", "%optamized%")
                    .thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> fuzzierResults = asyncCommands
                    .ftSearch("idx:bicycle", "%%optamised%%").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:3
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults)
                    .join();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.reactive.RedisReactiveCommands;

import io.lettuce.core.search.arguments.*;
import io.lettuce.core.search.SearchReply;

import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import reactor.core.publisher.Mono;

public class QueryFtExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();

            List<FieldArgs<String>> bicycleSchema = Arrays.asList(
                    TextFieldArgs.<String> builder().name("$.brand").as("brand").build(),
                    TextFieldArgs.<String> builder().name("$.model").as("model").build(),
                    TextFieldArgs.<String> builder().name("$.description").as("description").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build(),
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build());

            CreateArgs<String, String> bicycleCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("bicycle:").build();

            reactiveCommands.ftCreate("idx:bicycle", bicycleCreateArgs, bicycleSchema).block();

            JsonParser parser = reactiveCommands.getJsonParser();

            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject()
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("price", parser.createJsonValue("270")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\""))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\""))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("price", parser.createJsonValue("815")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Eva\""))
                            .put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("price", parser.createJsonValue("3400")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\""))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women’s saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("price", parser.createJsonValue("3200")).put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that’s "
                                            + "not to say that it’s a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which "
                                            + "doesn’t break the bank and delivers craved performance.\""))
                            .put("price", parser.createJsonValue("810")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\""))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It’s great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("price", parser.createJsonValue("2300")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\""))
                            .put("description",
                                    parser.createJsonValue("\"If you struggle with stiff fingers or a kinked neck or "
                                            + "back after a few minutes on the road, this lightweight, aluminum bike alleviates "
                                            + "those issues and allows you to enjoy the ride. From the ergonomic grips to the "
                                            + "lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. "
                                            + "The rear-inclined seat tube facilitates stability by allowing you to put a foot "
                                            + "on the ground to balance at a stop, and the low step-over frame makes it "
                                            + "accessible for all ability and mobility levels. The saddle is very soft, with "
                                            + "a wide back to support your hip joints and a cutout in the center to redistribute "
                                            + "that pressure. Rim brakes deliver satisfactory braking control, and the wide tires "
                                            + "provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts "
                                            + "facilitate setting up the Roll Low-Entry as your preferred commuter, and the "
                                            + "BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\""))
                            .put("price", parser.createJsonValue("430")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\""))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you’re just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("price", parser.createJsonValue("1200")).put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("brand", parser.createJsonValue("\"ThrillCycle\""))
                            .put("model", parser.createJsonValue("\"BikeShind\""))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that’s as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("price", parser.createJsonValue("815"))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<?>[] bikeFutures = new Mono<?>[bicycleJsons.size()];

            for (int i = 0; i < bicycleJsons.size(); i++) {
                bikeFutures[i] = reactiveCommands.jsonSet("bicycle:" + i, JsonPath.ROOT_PATH, bicycleJsons.get(i));
            }

            Mono.when(bikeFutures).block();

            Mono<SearchReply<String, String>> descriptionResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description: kids").doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:1
                            // >>> ID: bicycle:2
                        });
                    });

            Mono<SearchReply<String, String>> startsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@model: ka*")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                        });
                    });

            Mono<SearchReply<String, String>> endsWithResults = reactiveCommands.ftSearch("idx:bicycle", "@brand: *bikes")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:4
                            // >>> ID: bicycle:6
                        });
                    });

            Mono<SearchReply<String, String>> fuzzyResults = reactiveCommands.ftSearch("idx:bicycle", "%optamized%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono<SearchReply<String, String>> fuzzierResults = reactiveCommands.ftSearch("idx:bicycle", "%%optamised%%")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                            // >>> ID: bicycle:3
                        });
                    });

            Mono.when(descriptionResults, startsWithResults, endsWithResults, fuzzyResults, fuzzierResults).block();
        } finally {
            redisClient.shutdown();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"sort"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_ft() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	_, err := rdb.FTCreate(ctx, "idx:bicycle",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"bicycle:"},
		},
		&redis.FieldSchema{
			FieldName: "$.brand",
			As:        "brand",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.model",
			As:        "model",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.description",
			As:        "description",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName: "$.price",
			As:        "price",
			FieldType: redis.SearchFieldTypeNumeric,
		},
		&redis.FieldSchema{
			FieldName: "$.condition",
			As:        "condition",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	exampleJsons := []map[string]interface{}{
		{
			"pickup_zone": "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, " +
				"-74.0610 40.6678, -74.0610 40.7578))",
			"store_location": "-74.0060,40.7128",
			"brand":          "Velorim",
			"model":          "Jigger",
			"price":          270,
			"description": "Small and powerful, the Jigger is the best ride for the smallest of tikes! " +
				"This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger " +
				"is the vehicle of choice for the rare tenacious little rider raring to go.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, " +
				"-118.2887 33.9872, -118.2887 34.0972))",
			"store_location": "-118.2437,34.0522",
			"brand":          "Bicyk",
			"model":          "Hillcraft",
			"price":          1200,
			"description": "Kids want to ride with as little weight as possible. Especially " +
				"on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming " +
				"off a 24'' bike. The Hillcraft 26 is just the solution they need!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, " +
				"-87.6848 41.8231, -87.6848 41.9331))",
			"store_location": "-87.6298,41.8781",
			"brand":          "Nord",
			"model":          "Chook air 5",
			"price":          815,
			"description": "The Chook Air 5  gives kids aged six years and older a durable " +
				"and uberlight mountain bike for their first experience on tracks and easy cruising through " +
				"forests and fields. The lower  top tube makes it easy to mount and dismount in any " +
				"situation, giving your kids greater safety on the trails.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, " +
				"-80.2433 25.6967, -80.2433 25.8067))",
			"store_location": "-80.1918,25.7617",
			"brand":          "Eva",
			"model":          "Eva 291",
			"price":          3400,
			"description": "The sister company to Nord, Eva launched in 2005 as the first " +
				"and only women-dedicated bicycle brand. Designed by women for women, allEva bikes " +
				"are optimized for the feminine physique using analytics from a body metrics database. " +
				"If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This " +
				"full-suspension, cross-country ride has been designed for velocity. The 291 has " +
				"100mm of front and rear travel, a superlight aluminum frame and fast-rolling " +
				"29-inch wheels. Yippee!",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, " +
				"-122.4644 37.7099, -122.4644 37.8199))",
			"store_location": "-122.4194,37.7749",
			"brand":          "Noka Bikes",
			"model":          "Kahuna",
			"price":          3200,
			"description": "Whether you want to try your hand at XC racing or are looking " +
				"for a lively trail bike that's just as inspiring on the climbs as it is over rougher " +
				"ground, the Wilder is one heck of a bike built specifically for short women. Both the " +
				"frames and components have been tweaked to include a women’s saddle, different bars " +
				"and unique colourway.",
			"condition": "used",
		},
		{
			"pickup_zone": "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, " +
				"-0.1778 51.4024, -0.1778 51.5524))",
			"store_location": "-0.1278,51.5074",
			"brand":          "Breakout",
			"model":          "XBN 2.1 Alloy",
			"price":          810,
			"description": "The XBN 2.1 Alloy is our entry-level road bike – but that’s " +
				"not to say that it’s a basic machine. With an internal weld aluminium frame, a full " +
				"carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which " +
				"doesn’t break the bank and delivers craved performance.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, " +
				"2.1767 48.5516, 2.1767 48.9016))",
			"store_location": "2.3522,48.8566",
			"brand":          "ScramBikes",
			"model":          "WattBike",
			"price":          2300,
			"description": "The WattBike is the best e-bike for people who still " +
				"feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH " +
				"Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one " +
				"charge. It’s great for tackling hilly terrain or if you just fancy a more " +
				"leisurely ride. With three working modes, you can choose between E-bike, " +
				"assisted bicycle, and normal bike modes.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, " +
				"13.3260 52.2700, 13.3260 52.5700))",
			"store_location": "13.4050,52.5200",
			"brand":          "Peaknetic",
			"model":          "Secto",
			"price":          430,
			"description": "If you struggle with stiff fingers or a kinked neck or " +
				"back after a few minutes on the road, this lightweight, aluminum bike alleviates " +
				"those issues and allows you to enjoy the ride. From the ergonomic grips to the " +
				"lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. " +
				"The rear-inclined seat tube facilitates stability by allowing you to put a foot " +
				"on the ground to balance at a stop, and the low step-over frame makes it " +
				"accessible for all ability and mobility levels. The saddle is very soft, with " +
				"a wide back to support your hip joints and a cutout in the center to redistribute " +
				"that pressure. Rim brakes deliver satisfactory braking control, and the wide tires " +
				"provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts " +
				"facilitate setting up the Roll Low-Entry as your preferred commuter, and the " +
				"BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, " +
				"1.9450 41.1987, 1.9450 41.4301))",
			"store_location": "2.1734, 41.3851",
			"brand":          "nHill",
			"model":          "Summit",
			"price":          1200,
			"description": "This budget mountain bike from nHill performs well both " +
				"on bike paths and on the trail. The fork with 100mm of travel absorbs rough " +
				"terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. " +
				"The Shimano Tourney drivetrain offered enough gears for finding a comfortable " +
				"pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. " +
				"Whether you want an affordable bike that you can take to work, but also take " +
				"trail in mountains on the weekends or you’re just after a stable, comfortable " +
				"ride for the bike path, the Summit gives a good value for money.",
			"condition": "new",
		},
		{
			"pickup_zone": "POLYGON((12.4464 42.1028, 12.5464 42.1028, " +
				"12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
			"store_location": "12.4964,41.9028",
			"model":          "ThrillCycle",
			"brand":          "BikeShind",
			"price":          815,
			"description": "An artsy,  retro-inspired bicycle that’s as " +
				"functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. " +
				"A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t " +
				"suggest taking it to the mountains. Fenders protect you from mud, and a rear " +
				"basket lets you transport groceries, flowers and books. The ThrillCycle comes " +
				"with a limited lifetime warranty, so this little guy will last you long " +
				"past graduation.",
			"condition": "refurbished",
		},
	}

	for i, json := range exampleJsons {
		_, err := rdb.JSONSet(ctx, fmt.Sprintf("bicycle:%v", i), "$", json).Result()

		if err != nil {
			panic(err)
		}
	}

	res1, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description: kids",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 2

	sort.Slice(res1.Docs, func(i, j int) bool {
		return res1.Docs[i].ID < res1.Docs[j].ID
	})

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:1
	// >>> bicycle:2

	res2, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@model: ka*",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@brand: *bikes",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 2

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})
	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:4
	// >>> bicycle:6

	res4, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%optamized%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 1

	for _, doc := range res4.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

	res5, err := rdb.FTSearch(ctx,
		"idx:bicycle", "%%optamised%%",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5.Total) // >>> 1

	for _, doc := range res5.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:3

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryFtExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.brand", "brand"))
            .AddTextField(new FieldName("$.model", "model"))
            .AddTextField(new FieldName("$.description", "description"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[]
        {
            new
            {
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride " +
                                "for the smallest of tikes! This is the tiniest " +
                                "kids’ pedal bike on the market available without" +
                                " a coaster brake, the Jigger is the vehicle of " +
                                "choice for the rare tenacious little rider " +
                                "raring to go.",
                condition = "used"
            },
            new
            {
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible." +
                    " Especially on an incline! They may be at the age " +
                    "when a 27.5 inch wheel bike is just too clumsy coming " +
                    "off a 24 inch bike. The Hillcraft 26 is just the solution" +
                    " they need!",
                condition = "used",
            },
            new
            {
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older " +
                    "a durable and uberlight mountain bike for their first" +
                    " experience on tracks and easy cruising through forests" +
                    " and fields. The lower  top tube makes it easy to mount" +
                    " and dismount in any situation, giving your kids greater" +
                    " safety on the trails.",
                condition = "used",
            },
            new
            {
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the" +
                    " first and only women-dedicated bicycle brand. Designed" +
                    " by women for women, allEva bikes are optimized for the" +
                    " feminine physique using analytics from a body metrics" +
                    " database. If you like 29ers, try the Eva 291. It’s a " +
                    "brand new bike for 2022.. This full-suspension, " +
                    "cross-country ride has been designed for velocity. The" +
                    " 291 has 100mm of front and rear travel, a superlight " +
                    "aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used",
            },
            new
            {
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are " +
                    "looking for a lively trail bike that's just as inspiring" +
                    " on the climbs as it is over rougher ground, the Wilder" +
                    " is one heck of a bike built specifically for short women." +
                    " Both the frames and components have been tweaked to " +
                    "include a women’s saddle, different bars and unique " +
                    "colourway.",
                condition = "used",
            },
            new
            {
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
                    " not to say that it’s a basic machine. With an internal " +
                    "weld aluminium frame, a full carbon fork, and the slick-shifting" +
                    " Claris gears from Shimano’s, this is a bike which doesn’t" +
                    " break the bank and delivers craved performance.",
                condition = "new",
            },
            new
            {
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young" +
                    " at heart. It has a Bafang 1000W mid-drive system and a 48V" +
                    " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
                    " more than 60 miles on one charge. It’s great for tackling hilly" +
                    " terrain or if you just fancy a more leisurely ride. With three" +
                    " working modes, you can choose between E-bike, assisted bicycle," +
                    " and normal bike modes.",
                condition = "new",
            },
            new
            {
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after" +
                    " a few minutes on the road, this lightweight, aluminum bike" +
                    " alleviates those issues and allows you to enjoy the ride. From" +
                    " the ergonomic grips to the lumbar-supporting seat position, the" +
                    " Roll Low-Entry offers incredible comfort. The rear-inclined seat" +
                    " tube facilitates stability by allowing you to put a foot on the" +
                    " ground to balance at a stop, and the low step-over frame makes it" +
                    " accessible for all ability and mobility levels. The saddle is" +
                    " very soft, with a wide back to support your hip joints and a" +
                    " cutout in the center to redistribute that pressure. Rim brakes" +
                    " deliver satisfactory braking control, and the wide tires provide" +
                    " a smooth, stable ride on paved roads and gravel. Rack and fender" +
                    " mounts facilitate setting up the Roll Low-Entry as your preferred" +
                    " commuter, and the BMX-like handlebar offers space for mounting a" +
                    " flashlight, bell, or phone holder.",
                condition = "new",
            },
            new
            {
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike" +
                    " paths and on the trail. The fork with 100mm of travel absorbs" +
                    " rough terrain. Fat Kenda Booster tires give you grip in corners" +
                    " and on wet trails. The Shimano Tourney drivetrain offered enough" +
                    " gears for finding a comfortable pace to ride uphill, and the" +
                    " Tektro hydraulic disc brakes break smoothly. Whether you want an" +
                    " affordable bike that you can take to work, but also take trail in" +
                    " mountains on the weekends or you’re just after a stable," +
                    " comfortable ride for the bike path, the Summit gives a good value" +
                    " for money.",
                condition = "new",
            },
            new
            {
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is" +
                    " pretty: The ThrillCycle steel frame offers a smooth ride. A" +
                    " 9-speed drivetrain has enough gears for coasting in the city, but" +
                    " we wouldn’t suggest taking it to the mountains. Fenders protect" +
                    " you from mud, and a rear basket lets you transport groceries," +
                    " flowers and books. The ThrillCycle comes with a limited lifetime" +
                    " warranty, so this little guy will last you long past graduation.",
                condition = "refurbished",
            },
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        SearchResult res1 = db.FT().Search(
           "idx:bicycle",
           new("@description: kids")
       );
        Console.WriteLine(res1);    // >>> 2

        // Tests for 'ft1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new("@model: ka*")
        );
        Console.WriteLine(res2.TotalResults);   // >>> 1

        // Tests for 'ft2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@brand: *bikes")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 2

        // Tests for 'ft3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new("%optamized%")
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'ft4' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("%%optamised%%")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'ft5' step.

    }
}

```

### Fuzzy search on a specific attribute

To perform a fuzzy search on a specific text field, use the `@field:(...)` syntax with the fuzzy term inside parentheses.

```
FT.SEARCH index "@field:(%word%)"
```

Important:

Do not use quotes around the fuzzy term when targeting a specific field. Wrapping the term in quotes (for example, `@field:("%word%")`) converts the query into an exact match search, and the `%` characters are treated as literal characters rather than fuzzy operators.

The following example shows the correct way to perform a fuzzy search with distance one on the `description` field:

```
FT.SEARCH idx:bicycle "@description:(%optamized%)"
```

For a fuzzy search with distance two on a specific field:

```
FT.SEARCH idx:bicycle "@description:(%%optamised%%)"
```

You can also combine fuzzy searches on multiple fields using boolean operators:

```
FT.SEARCH idx:bicycle "@description:(%optamized%) | @model:(%jigar%)"
```

## Unicode considerations

Redis Search only supports Unicode characters in the [basic multilingual plane](https://en.wikipedia.org/wiki/Plane_\(Unicode\)#Basic_Multilingual_Plane); U+0000 to U+FFFF. Unicode characters beyond U+FFFF, such as Emojis, are not supported and would not be retrieved by queries including such characters in the following use cases:

*   Querying TEXT fields with Prefix/Suffix/Infix
*   Querying TEXT fields with fuzzy

Examples:

```
redis> FT.CREATE idx SCHEMA tag TAG text TEXT
OK
redis> HSET doc:1 tag '😀😁🙂' text '😀😁🙂'
(integer) 2
redis> HSET doc:2 tag '😀😁🙂abc' text '😀😁🙂abc'
(integer) 2
redis> FT.SEARCH idx '@text:(*😀😁🙂)' NOCONTENT
1) (integer) 0
redis> FT.SEARCH idx '@text:(*😀😁🙂*)' NOCONTENT
1) (integer) 0
redis> FT.SEARCH idx '@text:(😀😁🙂*)' NOCONTENT
1) (integer) 0

redis> FT.SEARCH idx '@text:(%😀😁🙃%)' NOCONTENT
1) (integer) 0
```

## On this page
