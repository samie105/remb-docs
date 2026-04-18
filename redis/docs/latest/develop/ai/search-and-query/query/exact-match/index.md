---
title: "Exact match queries"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/exact-match/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/exact-match/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:36.761Z"
content_hash: "5c713711491f101f5ca6f9e8817e990848712323bb9ef822e342968a9c25f36d"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Exact match queries","→","Exact match queries"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Exact match queries","→","Exact match queries"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/query/combined/index.md", "title": "Combined queries"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/query/full-text/index.md", "title": "Full-text search"}
---

# Exact match queries

Perform simple exact match queries

An exact match query allows you to select all documents where a field matches a specific value.

You can use exact match queries on several field types. The query syntax varies depending on the type.

The examples in this article use a schema with the following fields:

Field name

Field type

`description`

`TEXT`

`condition`

`TAG`

`price`

`NUMERIC`

You can find more details about creating the index and loading the demo data in the [quick start guide](/docs/latest/develop/get-started/document-database/).

## Numeric field

To perform an exact match query on a numeric field, you need to construct a range query with the same start and end value:

```
FT.SEARCH index "@field:[value value]"

or

FT.SEARCH index "@field:[value]" DIALECT 2 # requires v2.10

or

FT.SEARCH index "@field==value" DIALECT 2 # requires v2.10
```

As described in the [article about range queries](/docs/latest/develop/ai/search-and-query/query/range/), you can also use the `FILTER` argument:

```
FT.SEARCH index "*" FILTER field start end
```

The following examples show you how to query for bicycles with a price of exactly 270 USD:

```plaintext
> FT.SEARCH idx:bicycle "@price:[270 270]"
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...

> FT.SEARCH idx:bicycle "@price:[270]" # requires v2.10
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...

> FT.SEARCH idx:bicycle "@price==270" # requires v2.10
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...

> FT.SEARCH idx:bicycle "*" FILTER price 270 270
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, ...
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", as_name="description"),
    NumericField("$.price", as_name="price"),
    TagField("$.condition", as_name="condition"),
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

res = index.search(Query("@price:[270 270]"))
print(res.total)
# >>> 1

try:
    res = index.search(Query("@price:[270]")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price:[270]' syntax not yet supported.")

try:
    res = index.search(Query("@price==270")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price==270' syntax not yet supported.")

query = Query("*").add_filter(NumericFilter("price", 270, 270))
res = index.search(query)
print(res.total)
# >>> 1

res = index.search(Query("@condition:{new}"))
print(res.total)
# >>> 5

schema = (
    TagField("$.email", as_name="email")
)

idx_email = r.ft("idx:email")
idx_email.create_index(
    schema,
    definition=IndexDefinition(prefix=["key:"], index_type=IndexType.JSON),
)
r.json().set('key:1', Path.root_path(), '{"email": "test@redis.com"}')

try:
    res = idx_email.search(Query("test@redis.com").dialect(2))
    print(res)
except Exception:
    print("'test@redis.com' syntax not yet supported.")

res = index.search(Query("@description:\"rough terrain\""))
print(res.total)
# >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
  },
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
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

const res1 = await client.ft.search('idx:bicycle', '@price:[270 270]');
console.log(res1.total); // >>> 1

try {
    const res2 = await client.ft.search('idx:bicycle', '@price:[270]');
    console.log(res2.total); // >>> 1
    assert.strictEqual(res2.total, 1);
} catch (err) {
    console.log("'@price:[270]' syntax not yet supported.");
}

try {
    const res3 = await client.ft.search('idx:bicycle', '@price==270');
    console.log(res3.total); // >>> 1
    assert.strictEqual(res3.total, 1);
} catch (err) {
    console.log("'@price==270' syntax not yet supported.");
}

// FILTER is not supported
// const res4 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//       field: 'price',
//       min: 270,
//       max: 270,
//   }
// });
// console.log(res4.total); // >>> 1

const res5 = await client.ft.search('idx:bicycle', '@condition:{new}');
console.log(res5.total); // >>> 5

await client.ft.create('idx:email', {
  '$.email': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'email'
  }
}, {
  ON: 'JSON',
  PREFIX: 'key:'
})

await client.json.set('key:1', '$', { email: 'test@redis.com' });

try {
    const res6 = await client.ft.search('idx:email', 'test@redis.com', { DIALECT: 2 });
    console.log(res6);
} catch (err) {
    console.log("'test@redis.com' syntax not yet supported.");
}

const res7 = await client.ft.search('idx:bicycle', '@description:"rough terrain"');
console.log(res7.total); // >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryEmExample {

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

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@price:[270 270]");
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:0

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                    .filter("price", 270, 270)
        );
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:0

        // Tests for 'em1' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@condition:{new}");
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:5
        // >>> bicycle:0
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8

        // Tests for 'em2' step.

        SchemaField[] emailSchema = {
            TextField.of("$.email").as("email")
        };

        jedis.ftCreate("idx:email", 
            new FTCreateParams()
                    .addPrefix("key:")
                    .on(IndexDataType.JSON),
            emailSchema
        );

        jedis.jsonSet("key:1", Path2.ROOT_PATH, "{\"email\": \"test@redis.com\"}");
        
        SearchResult res4 = jedis.ftSearch("idx:email",
            RediSearchUtil.escapeQuery("@email{test@redis.com}"),
            new FTSearchParams().dialect(2)
        );
        System.out.println(res4.getTotalResults());

        // Tests for 'em3' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle",
            "@description:\"rough terrain\""
        );
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:8

        // Tests for 'em4' step.

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

public class QueryEmExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands.ftSearch("idx:bicycle", "@price:[270]")

                    .thenApply(res -> {

                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0

                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> conditionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@condition:{new}").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());
            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            CompletableFuture<SearchReply<String, String>> emailResults = asyncCommands
                    .ftCreate("idx:email", emailCreateArgs, emailSchema).thenCompose(res -> {
                        System.out.println(res); // >>> OK
                        return asyncCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                                parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> OK
                        return asyncCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}");
                    }).thenApply(res3 -> {
                        System.out.println(res3.getResults().size()); // >>> 1
                        System.out.println(res3.getResults().get(0).getId());
                        // >>> key:1
                        return res3;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> textMatchResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").thenApply(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, conditionResults, emailResults, textMatchResults).join();
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

public class QueryEmExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[270]")
                    .doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                    });

            Mono<SearchReply<String, String>> conditionResults = reactiveCommands.ftSearch("idx:bicycle", "@condition:{new}")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8
                    });

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());

            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            Mono<Void> emailResults = reactiveCommands.ftCreate("idx:email", emailCreateArgs, emailSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).flatMap(res -> reactiveCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                    parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")))).doOnNext(res -> {
                        System.out.println(res); // >>> OK
                    }).flatMap(res -> reactiveCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}")).doOnNext(res -> {
                        System.out.println(res.getResults().size()); // >>> 1
                        System.out.println(res.getResults().get(0).getId());
                        // >>> key:1
                    }).then();

            Mono<SearchReply<String, String>> textMatchResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8
                    });
            Mono.when(priceResults, conditionResults, emailResults, textMatchResults).block();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"slices"
	"strings"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_em() {
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
				"This is the tiniest kids pedal bike on the market available without a coaster brake, the Jigger " +
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
		"idx:bicycle", "@price:[270 270]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       270,
					Max:       270,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@condition:{new}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	docs := res3.Docs
	slices.SortFunc(docs, func(a, b redis.Document) int {
		return strings.Compare(a.ID, b.ID)
	})

	for _, doc := range docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8

	res4, err := rdb.FTCreate(ctx,
		"idx:email",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"key:"},
		},
		&redis.FieldSchema{
			FieldName: "$.email",
			As:        "email",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> OK

	res5, err := rdb.JSONSet(ctx, "key:1", "$",
		map[string]interface{}{
			"email": "test@redis.com",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK

	res6, err := rdb.FTSearch(ctx, "idx:email",
		"@email:{test\\@redis\\.com}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6.Total) // >>> 1

	res7, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description:\"rough terrain\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7.Total) // >>> 1

	for _, doc := range res7.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:8

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryEmExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        FTCreateParams idxParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

        db.FT().Create("idx:bicycle", idxParams, bikeSchema);

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
            new("@price:[270 270]")
        );
        Console.WriteLine(res1.TotalResults); //    >>> 1

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 270, 270)
            )
        );
        Console.WriteLine(res2.TotalResults); //    >>> 1

        // Tests for 'em1' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@condition:{new}")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 4

        // Tests for 'em2' step.

        Schema emailSchema = new Schema()
            .AddTagField(new FieldName("$.email", "email"));

        FTCreateParams emailParams = new FTCreateParams()
            .AddPrefix("key:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:email", emailParams, emailSchema);

        db.JSON().Set("key:1", "$", "{\"email\": \"test@redis.com\"}");

        SearchResult res4 = db.FT().Search(
            "idx:email",
            new Query("@email:{test\\@redis\\.com}").Dialect(2)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'em3' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("@description:\"rough terrain\"")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'em4' step.

    }
}

```

## Tag field

A tag is a short sequence of text, for example, "new" or "Los Angeles".

Important:

If you need to query for short texts, use a tag query instead of a full-text query. Tag fields are more space-efficient for storing index entries and often lead to lower query complexity for exact match queries.

You can construct a tag query for a single tag in the following way:

```
FT.SEARCH index "@field:{tag}"
```

Note:

The curly brackets are mandatory for tag queries.

This short example shows you how to query for new bicycles:

```plaintext
> FT.SEARCH idx:bicycle "@condition:{new}"
 1) (integer) 5
 2) "bicycle:0"
 3) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\",\"store_location\":\"-74.0060,40.7128\",\"brand\":\"Velorim\",\"model\":\"Jigger\",\"price\":270,\"description\":\"Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids\xe2\x80\x99 pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.\",\"condition\":\"new\"}"
 4) "bicycle:5"
 5) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\",\"store_location\":\"-0.1278,51.5074\",\"brand\":\"Breakout\",\"model\":\"XBN 2.1 Alloy\",\"price\":810,\"description\":\"The XBN 2.1 Alloy is our entry-level road bike \xe2\x80\x93 but that\xe2\x80\x99s not to say that it\xe2\x80\x99s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano\xe2\x80\x99s, this is a bike which doesn\xe2\x80\x99t break the bank and delivers craved performance.\",\"condition\":\"new\"}"
 6) "bicycle:6"
 7) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\",\"store_location\":\"2.3522,48.8566\",\"brand\":\"ScramBikes\",\"model\":\"WattBike\",\"price\":2300,\"description\":\"The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It\xe2\x80\x99s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.\",\"condition\":\"new\"}"
 8) "bicycle:7"
 9) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\",\"store_location\":\"13.4050,52.5200\",\"brand\":\"Peaknetic\",\"model\":\"Secto\",\"price\":430,\"description\":\"If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\",\"condition\":\"new\"}"
10) "bicycle:8"
11) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\",\"store_location\":\"2.1734, 41.3851\",\"brand\":\"nHill\",\"model\":\"Summit\",\"price\":1200,\"description\":\"This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\xe2\x80\x99re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.\",\"condition\":\"new\"}"
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", as_name="description"),
    NumericField("$.price", as_name="price"),
    TagField("$.condition", as_name="condition"),
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

res = index.search(Query("@price:[270 270]"))
print(res.total)
# >>> 1

try:
    res = index.search(Query("@price:[270]")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price:[270]' syntax not yet supported.")

try:
    res = index.search(Query("@price==270")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price==270' syntax not yet supported.")

query = Query("*").add_filter(NumericFilter("price", 270, 270))
res = index.search(query)
print(res.total)
# >>> 1

res = index.search(Query("@condition:{new}"))
print(res.total)
# >>> 5

schema = (
    TagField("$.email", as_name="email")
)

idx_email = r.ft("idx:email")
idx_email.create_index(
    schema,
    definition=IndexDefinition(prefix=["key:"], index_type=IndexType.JSON),
)
r.json().set('key:1', Path.root_path(), '{"email": "test@redis.com"}')

try:
    res = idx_email.search(Query("test@redis.com").dialect(2))
    print(res)
except Exception:
    print("'test@redis.com' syntax not yet supported.")

res = index.search(Query("@description:\"rough terrain\""))
print(res.total)
# >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
  },
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
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

const res1 = await client.ft.search('idx:bicycle', '@price:[270 270]');
console.log(res1.total); // >>> 1

try {
    const res2 = await client.ft.search('idx:bicycle', '@price:[270]');
    console.log(res2.total); // >>> 1
    assert.strictEqual(res2.total, 1);
} catch (err) {
    console.log("'@price:[270]' syntax not yet supported.");
}

try {
    const res3 = await client.ft.search('idx:bicycle', '@price==270');
    console.log(res3.total); // >>> 1
    assert.strictEqual(res3.total, 1);
} catch (err) {
    console.log("'@price==270' syntax not yet supported.");
}

// FILTER is not supported
// const res4 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//       field: 'price',
//       min: 270,
//       max: 270,
//   }
// });
// console.log(res4.total); // >>> 1

const res5 = await client.ft.search('idx:bicycle', '@condition:{new}');
console.log(res5.total); // >>> 5

await client.ft.create('idx:email', {
  '$.email': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'email'
  }
}, {
  ON: 'JSON',
  PREFIX: 'key:'
})

await client.json.set('key:1', '$', { email: 'test@redis.com' });

try {
    const res6 = await client.ft.search('idx:email', 'test@redis.com', { DIALECT: 2 });
    console.log(res6);
} catch (err) {
    console.log("'test@redis.com' syntax not yet supported.");
}

const res7 = await client.ft.search('idx:bicycle', '@description:"rough terrain"');
console.log(res7.total); // >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryEmExample {

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

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@price:[270 270]");
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:0

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                    .filter("price", 270, 270)
        );
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:0

        // Tests for 'em1' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@condition:{new}");
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:5
        // >>> bicycle:0
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8

        // Tests for 'em2' step.

        SchemaField[] emailSchema = {
            TextField.of("$.email").as("email")
        };

        jedis.ftCreate("idx:email", 
            new FTCreateParams()
                    .addPrefix("key:")
                    .on(IndexDataType.JSON),
            emailSchema
        );

        jedis.jsonSet("key:1", Path2.ROOT_PATH, "{\"email\": \"test@redis.com\"}");
        
        SearchResult res4 = jedis.ftSearch("idx:email",
            RediSearchUtil.escapeQuery("@email{test@redis.com}"),
            new FTSearchParams().dialect(2)
        );
        System.out.println(res4.getTotalResults());

        // Tests for 'em3' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle",
            "@description:\"rough terrain\""
        );
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:8

        // Tests for 'em4' step.

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

public class QueryEmExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands.ftSearch("idx:bicycle", "@price:[270]")

                    .thenApply(res -> {

                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0

                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> conditionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@condition:{new}").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());
            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            CompletableFuture<SearchReply<String, String>> emailResults = asyncCommands
                    .ftCreate("idx:email", emailCreateArgs, emailSchema).thenCompose(res -> {
                        System.out.println(res); // >>> OK
                        return asyncCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                                parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> OK
                        return asyncCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}");
                    }).thenApply(res3 -> {
                        System.out.println(res3.getResults().size()); // >>> 1
                        System.out.println(res3.getResults().get(0).getId());
                        // >>> key:1
                        return res3;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> textMatchResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").thenApply(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, conditionResults, emailResults, textMatchResults).join();
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

public class QueryEmExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[270]")
                    .doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                    });

            Mono<SearchReply<String, String>> conditionResults = reactiveCommands.ftSearch("idx:bicycle", "@condition:{new}")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8
                    });

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());

            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            Mono<Void> emailResults = reactiveCommands.ftCreate("idx:email", emailCreateArgs, emailSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).flatMap(res -> reactiveCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                    parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")))).doOnNext(res -> {
                        System.out.println(res); // >>> OK
                    }).flatMap(res -> reactiveCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}")).doOnNext(res -> {
                        System.out.println(res.getResults().size()); // >>> 1
                        System.out.println(res.getResults().get(0).getId());
                        // >>> key:1
                    }).then();

            Mono<SearchReply<String, String>> textMatchResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8
                    });
            Mono.when(priceResults, conditionResults, emailResults, textMatchResults).block();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"slices"
	"strings"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_em() {
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
				"This is the tiniest kids pedal bike on the market available without a coaster brake, the Jigger " +
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
		"idx:bicycle", "@price:[270 270]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       270,
					Max:       270,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@condition:{new}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	docs := res3.Docs
	slices.SortFunc(docs, func(a, b redis.Document) int {
		return strings.Compare(a.ID, b.ID)
	})

	for _, doc := range docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8

	res4, err := rdb.FTCreate(ctx,
		"idx:email",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"key:"},
		},
		&redis.FieldSchema{
			FieldName: "$.email",
			As:        "email",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> OK

	res5, err := rdb.JSONSet(ctx, "key:1", "$",
		map[string]interface{}{
			"email": "test@redis.com",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK

	res6, err := rdb.FTSearch(ctx, "idx:email",
		"@email:{test\\@redis\\.com}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6.Total) // >>> 1

	res7, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description:\"rough terrain\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7.Total) // >>> 1

	for _, doc := range res7.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:8

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryEmExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        FTCreateParams idxParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

        db.FT().Create("idx:bicycle", idxParams, bikeSchema);

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
            new("@price:[270 270]")
        );
        Console.WriteLine(res1.TotalResults); //    >>> 1

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 270, 270)
            )
        );
        Console.WriteLine(res2.TotalResults); //    >>> 1

        // Tests for 'em1' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@condition:{new}")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 4

        // Tests for 'em2' step.

        Schema emailSchema = new Schema()
            .AddTagField(new FieldName("$.email", "email"));

        FTCreateParams emailParams = new FTCreateParams()
            .AddPrefix("key:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:email", emailParams, emailSchema);

        db.JSON().Set("key:1", "$", "{\"email\": \"test@redis.com\"}");

        SearchResult res4 = db.FT().Search(
            "idx:email",
            new Query("@email:{test\\@redis\\.com}").Dialect(2)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'em3' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("@description:\"rough terrain\"")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'em4' step.

    }
}

```

Use double quotes and [DIALECT 2](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/#dialect-2) for exact match queries involving tags that contain special characters. As of v2.10, the only character that needs escaping in queries involving double-quoted tags is the double-quote character. Here's an example of using double-quoted tags that contain special characters:

```plaintext
> FT.CREATE idx:email ON JSON PREFIX 1 key: SCHEMA $.email AS email TAG
OK
> JSON.SET key:1 $ '{"email": "test@redis.com"}'
OK
> FT.SEARCH idx:email '@email:{"test@redis.com"}' DIALECT 2
1) (integer) 1
2) "key:1"
3) 1) "$"
   2) "{\"email\":\"test@redis.com\"}"
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", as_name="description"),
    NumericField("$.price", as_name="price"),
    TagField("$.condition", as_name="condition"),
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

res = index.search(Query("@price:[270 270]"))
print(res.total)
# >>> 1

try:
    res = index.search(Query("@price:[270]")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price:[270]' syntax not yet supported.")

try:
    res = index.search(Query("@price==270")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price==270' syntax not yet supported.")

query = Query("*").add_filter(NumericFilter("price", 270, 270))
res = index.search(query)
print(res.total)
# >>> 1

res = index.search(Query("@condition:{new}"))
print(res.total)
# >>> 5

schema = (
    TagField("$.email", as_name="email")
)

idx_email = r.ft("idx:email")
idx_email.create_index(
    schema,
    definition=IndexDefinition(prefix=["key:"], index_type=IndexType.JSON),
)
r.json().set('key:1', Path.root_path(), '{"email": "test@redis.com"}')

try:
    res = idx_email.search(Query("test@redis.com").dialect(2))
    print(res)
except Exception:
    print("'test@redis.com' syntax not yet supported.")

res = index.search(Query("@description:\"rough terrain\""))
print(res.total)
# >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
  },
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
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

const res1 = await client.ft.search('idx:bicycle', '@price:[270 270]');
console.log(res1.total); // >>> 1

try {
    const res2 = await client.ft.search('idx:bicycle', '@price:[270]');
    console.log(res2.total); // >>> 1
    assert.strictEqual(res2.total, 1);
} catch (err) {
    console.log("'@price:[270]' syntax not yet supported.");
}

try {
    const res3 = await client.ft.search('idx:bicycle', '@price==270');
    console.log(res3.total); // >>> 1
    assert.strictEqual(res3.total, 1);
} catch (err) {
    console.log("'@price==270' syntax not yet supported.");
}

// FILTER is not supported
// const res4 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//       field: 'price',
//       min: 270,
//       max: 270,
//   }
// });
// console.log(res4.total); // >>> 1

const res5 = await client.ft.search('idx:bicycle', '@condition:{new}');
console.log(res5.total); // >>> 5

await client.ft.create('idx:email', {
  '$.email': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'email'
  }
}, {
  ON: 'JSON',
  PREFIX: 'key:'
})

await client.json.set('key:1', '$', { email: 'test@redis.com' });

try {
    const res6 = await client.ft.search('idx:email', 'test@redis.com', { DIALECT: 2 });
    console.log(res6);
} catch (err) {
    console.log("'test@redis.com' syntax not yet supported.");
}

const res7 = await client.ft.search('idx:bicycle', '@description:"rough terrain"');
console.log(res7.total); // >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryEmExample {

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

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@price:[270 270]");
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:0

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                    .filter("price", 270, 270)
        );
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:0

        // Tests for 'em1' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@condition:{new}");
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:5
        // >>> bicycle:0
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8

        // Tests for 'em2' step.

        SchemaField[] emailSchema = {
            TextField.of("$.email").as("email")
        };

        jedis.ftCreate("idx:email", 
            new FTCreateParams()
                    .addPrefix("key:")
                    .on(IndexDataType.JSON),
            emailSchema
        );

        jedis.jsonSet("key:1", Path2.ROOT_PATH, "{\"email\": \"test@redis.com\"}");
        
        SearchResult res4 = jedis.ftSearch("idx:email",
            RediSearchUtil.escapeQuery("@email{test@redis.com}"),
            new FTSearchParams().dialect(2)
        );
        System.out.println(res4.getTotalResults());

        // Tests for 'em3' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle",
            "@description:\"rough terrain\""
        );
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:8

        // Tests for 'em4' step.

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

public class QueryEmExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands.ftSearch("idx:bicycle", "@price:[270]")

                    .thenApply(res -> {

                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0

                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> conditionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@condition:{new}").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());
            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            CompletableFuture<SearchReply<String, String>> emailResults = asyncCommands
                    .ftCreate("idx:email", emailCreateArgs, emailSchema).thenCompose(res -> {
                        System.out.println(res); // >>> OK
                        return asyncCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                                parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> OK
                        return asyncCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}");
                    }).thenApply(res3 -> {
                        System.out.println(res3.getResults().size()); // >>> 1
                        System.out.println(res3.getResults().get(0).getId());
                        // >>> key:1
                        return res3;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> textMatchResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").thenApply(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, conditionResults, emailResults, textMatchResults).join();
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

public class QueryEmExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[270]")
                    .doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                    });

            Mono<SearchReply<String, String>> conditionResults = reactiveCommands.ftSearch("idx:bicycle", "@condition:{new}")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8
                    });

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());

            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            Mono<Void> emailResults = reactiveCommands.ftCreate("idx:email", emailCreateArgs, emailSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).flatMap(res -> reactiveCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                    parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")))).doOnNext(res -> {
                        System.out.println(res); // >>> OK
                    }).flatMap(res -> reactiveCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}")).doOnNext(res -> {
                        System.out.println(res.getResults().size()); // >>> 1
                        System.out.println(res.getResults().get(0).getId());
                        // >>> key:1
                    }).then();

            Mono<SearchReply<String, String>> textMatchResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8
                    });
            Mono.when(priceResults, conditionResults, emailResults, textMatchResults).block();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"slices"
	"strings"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_em() {
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
				"This is the tiniest kids pedal bike on the market available without a coaster brake, the Jigger " +
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
		"idx:bicycle", "@price:[270 270]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       270,
					Max:       270,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@condition:{new}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	docs := res3.Docs
	slices.SortFunc(docs, func(a, b redis.Document) int {
		return strings.Compare(a.ID, b.ID)
	})

	for _, doc := range docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8

	res4, err := rdb.FTCreate(ctx,
		"idx:email",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"key:"},
		},
		&redis.FieldSchema{
			FieldName: "$.email",
			As:        "email",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> OK

	res5, err := rdb.JSONSet(ctx, "key:1", "$",
		map[string]interface{}{
			"email": "test@redis.com",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK

	res6, err := rdb.FTSearch(ctx, "idx:email",
		"@email:{test\\@redis\\.com}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6.Total) // >>> 1

	res7, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description:\"rough terrain\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7.Total) // >>> 1

	for _, doc := range res7.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:8

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryEmExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        FTCreateParams idxParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

        db.FT().Create("idx:bicycle", idxParams, bikeSchema);

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
            new("@price:[270 270]")
        );
        Console.WriteLine(res1.TotalResults); //    >>> 1

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 270, 270)
            )
        );
        Console.WriteLine(res2.TotalResults); //    >>> 1

        // Tests for 'em1' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@condition:{new}")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 4

        // Tests for 'em2' step.

        Schema emailSchema = new Schema()
            .AddTagField(new FieldName("$.email", "email"));

        FTCreateParams emailParams = new FTCreateParams()
            .AddPrefix("key:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:email", emailParams, emailSchema);

        db.JSON().Set("key:1", "$", "{\"email\": \"test@redis.com\"}");

        SearchResult res4 = db.FT().Search(
            "idx:email",
            new Query("@email:{test\\@redis\\.com}").Dialect(2)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'em3' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("@description:\"rough terrain\"")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'em4' step.

    }
}

```

## Full-text field

A detailed explanation of full-text queries is available in the [full-text queries documentation](/docs/latest/develop/ai/search-and-query/query/full-text/). You can also query for an exact match of a phrase within a text field:

```
FT.SEARCH index "@field:\"phrase\""
```

Important:

The phrase must be wrapped by escaped double quotes for an exact match query.

You can't use a phrase that starts with a [stop word](/docs/latest/develop/ai/search-and-query/advanced-concepts/stopwords/).

Here is an example for finding all bicycles that have a description containing the exact text 'rough terrain':

```plaintext
FT.SEARCH idx:bicycle "@description:\"rough terrain\""
1) (integer) 1
2) "bicycle:8"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\",\"store_location\":\"2.1734, 41.3851\",\"brand\":\"nHill\",\"model\":\"Summit\",\"price\":1200,\"description\":\"This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\xe2\x80\x99re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.\",\"condition\":\"new\"}"
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", as_name="description"),
    NumericField("$.price", as_name="price"),
    TagField("$.condition", as_name="condition"),
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

res = index.search(Query("@price:[270 270]"))
print(res.total)
# >>> 1

try:
    res = index.search(Query("@price:[270]")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price:[270]' syntax not yet supported.")

try:
    res = index.search(Query("@price==270")) # not yet supported in redis-py
    print(res.total)
    # >>> 1
    assert res.total == 1
except Exception:
    print("'@price==270' syntax not yet supported.")

query = Query("*").add_filter(NumericFilter("price", 270, 270))
res = index.search(query)
print(res.total)
# >>> 1

res = index.search(Query("@condition:{new}"))
print(res.total)
# >>> 5

schema = (
    TagField("$.email", as_name="email")
)

idx_email = r.ft("idx:email")
idx_email.create_index(
    schema,
    definition=IndexDefinition(prefix=["key:"], index_type=IndexType.JSON),
)
r.json().set('key:1', Path.root_path(), '{"email": "test@redis.com"}')

try:
    res = idx_email.search(Query("test@redis.com").dialect(2))
    print(res)
except Exception:
    print("'test@redis.com' syntax not yet supported.")

res = index.search(Query("@description:\"rough terrain\""))
print(res.total)
# >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.description': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'description'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
  },
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
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

const res1 = await client.ft.search('idx:bicycle', '@price:[270 270]');
console.log(res1.total); // >>> 1

try {
    const res2 = await client.ft.search('idx:bicycle', '@price:[270]');
    console.log(res2.total); // >>> 1
    assert.strictEqual(res2.total, 1);
} catch (err) {
    console.log("'@price:[270]' syntax not yet supported.");
}

try {
    const res3 = await client.ft.search('idx:bicycle', '@price==270');
    console.log(res3.total); // >>> 1
    assert.strictEqual(res3.total, 1);
} catch (err) {
    console.log("'@price==270' syntax not yet supported.");
}

// FILTER is not supported
// const res4 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//       field: 'price',
//       min: 270,
//       max: 270,
//   }
// });
// console.log(res4.total); // >>> 1

const res5 = await client.ft.search('idx:bicycle', '@condition:{new}');
console.log(res5.total); // >>> 5

await client.ft.create('idx:email', {
  '$.email': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'email'
  }
}, {
  ON: 'JSON',
  PREFIX: 'key:'
})

await client.json.set('key:1', '$', { email: 'test@redis.com' });

try {
    const res6 = await client.ft.search('idx:email', 'test@redis.com', { DIALECT: 2 });
    console.log(res6);
} catch (err) {
    console.log("'test@redis.com' syntax not yet supported.");
}

const res7 = await client.ft.search('idx:bicycle', '@description:"rough terrain"');
console.log(res7.total); // >>> 1 (Result{1 total, docs: [Document {'id': 'bicycle:8'...)

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryEmExample {

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

        SearchResult res1 = jedis.ftSearch("idx:bicycle", "@price:[270 270]");
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (int i = 0; i < docs1.size(); i++) {
            System.out.println(docs1.get(i).getId());
        }
        // >>> bicycle:0

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                    .filter("price", 270, 270)
        );
        System.out.println(res2.getTotalResults()); // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (int i = 0; i < docs2.size(); i++) {
            System.out.println(docs2.get(i).getId());
        }
        // >>> bicycle:0

        // Tests for 'em1' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle", "@condition:{new}");
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (int i = 0; i < docs3.size(); i++) {
            System.out.println(docs3.get(i).getId());
        }
        // >>> bicycle:5
        // >>> bicycle:0
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8

        // Tests for 'em2' step.

        SchemaField[] emailSchema = {
            TextField.of("$.email").as("email")
        };

        jedis.ftCreate("idx:email", 
            new FTCreateParams()
                    .addPrefix("key:")
                    .on(IndexDataType.JSON),
            emailSchema
        );

        jedis.jsonSet("key:1", Path2.ROOT_PATH, "{\"email\": \"test@redis.com\"}");
        
        SearchResult res4 = jedis.ftSearch("idx:email",
            RediSearchUtil.escapeQuery("@email{test@redis.com}"),
            new FTSearchParams().dialect(2)
        );
        System.out.println(res4.getTotalResults());

        // Tests for 'em3' step.

        SearchResult res5 = jedis.ftSearch("idx:bicycle",
            "@description:\"rough terrain\""
        );
        System.out.println(res5.getTotalResults()); // >>> 1

        List<Document> docs5 = res5.getDocuments();

        for (int i = 0; i < docs5.size(); i++) {
            System.out.println(docs5.get(i).getId());
        }
        // >>> bicycle:8

        // Tests for 'em4' step.

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

public class QueryEmExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands.ftSearch("idx:bicycle", "@price:[270]")

                    .thenApply(res -> {

                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0

                        return res;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> conditionResults = asyncCommands
                    .ftSearch("idx:bicycle", "@condition:{new}").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());
            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            CompletableFuture<SearchReply<String, String>> emailResults = asyncCommands
                    .ftCreate("idx:email", emailCreateArgs, emailSchema).thenCompose(res -> {
                        System.out.println(res); // >>> OK
                        return asyncCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                                parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")));
                    }).thenCompose(res2 -> {
                        System.out.println(res2); // >>> OK
                        return asyncCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}");
                    }).thenApply(res3 -> {
                        System.out.println(res3.getResults().size()); // >>> 1
                        System.out.println(res3.getResults().get(0).getId());
                        // >>> key:1
                        return res3;
                    }).toCompletableFuture();

            CompletableFuture<SearchReply<String, String>> textMatchResults = asyncCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").thenApply(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8

                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, conditionResults, emailResults, textMatchResults).join();
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

public class QueryEmExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[270]")
                    .doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                    });

            Mono<SearchReply<String, String>> conditionResults = reactiveCommands.ftSearch("idx:bicycle", "@condition:{new}")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:0
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:6
                        // >>> ID: bicycle:7
                        // >>> ID: bicycle:8
                    });

            List<FieldArgs<String>> emailSchema = Arrays
                    .asList(TagFieldArgs.<String> builder().name("$.email").as("email").build());

            CreateArgs<String, String> emailCreateArgs = CreateArgs.<String, String> builder().on(CreateArgs.TargetType.JSON)
                    .withPrefix("key:").build();

            Mono<Void> emailResults = reactiveCommands.ftCreate("idx:email", emailCreateArgs, emailSchema).doOnNext(res -> {
                System.out.println(res); // >>> OK
            }).flatMap(res -> reactiveCommands.jsonSet("key:1", JsonPath.ROOT_PATH,
                    parser.createJsonObject().put("email", parser.createJsonValue("\"test@redis.com\"")))).doOnNext(res -> {
                        System.out.println(res); // >>> OK
                    }).flatMap(res -> reactiveCommands.ftSearch("idx:email", "@email:{test\\@redis\\.com}")).doOnNext(res -> {
                        System.out.println(res.getResults().size()); // >>> 1
                        System.out.println(res.getResults().get(0).getId());
                        // >>> key:1
                    }).then();

            Mono<SearchReply<String, String>> textMatchResults = reactiveCommands
                    .ftSearch("idx:bicycle", "@description:\"rough terrain\"").doOnNext(res -> {
                        res.getResults().forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:8
                    });
            Mono.when(priceResults, conditionResults, emailResults, textMatchResults).block();
        }
    }

}
```

```go
package example_commands_test

import (
	"context"
	"fmt"
	"slices"
	"strings"

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_em() {
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
				"This is the tiniest kids pedal bike on the market available without a coaster brake, the Jigger " +
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
		"idx:bicycle", "@price:[270 270]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       270,
					Max:       270,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0

	res3, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@condition:{new}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	docs := res3.Docs
	slices.SortFunc(docs, func(a, b redis.Document) int {
		return strings.Compare(a.ID, b.ID)
	})

	for _, doc := range docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:0
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8

	res4, err := rdb.FTCreate(ctx,
		"idx:email",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"key:"},
		},
		&redis.FieldSchema{
			FieldName: "$.email",
			As:        "email",
			FieldType: redis.SearchFieldTypeTag,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4) // >>> OK

	res5, err := rdb.JSONSet(ctx, "key:1", "$",
		map[string]interface{}{
			"email": "test@redis.com",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> OK

	res6, err := rdb.FTSearch(ctx, "idx:email",
		"@email:{test\\@redis\\.com}",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6.Total) // >>> 1

	res7, err := rdb.FTSearch(ctx,
		"idx:bicycle", "@description:\"rough terrain\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7.Total) // >>> 1

	for _, doc := range res7.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:8

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryEmExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        FTCreateParams idxParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

        db.FT().Create("idx:bicycle", idxParams, bikeSchema);

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
            new("@price:[270 270]")
        );
        Console.WriteLine(res1.TotalResults); //    >>> 1

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 270, 270)
            )
        );
        Console.WriteLine(res2.TotalResults); //    >>> 1

        // Tests for 'em1' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new("@condition:{new}")
        );
        Console.WriteLine(res3.TotalResults);   // >>> 4

        // Tests for 'em2' step.

        Schema emailSchema = new Schema()
            .AddTagField(new FieldName("$.email", "email"));

        FTCreateParams emailParams = new FTCreateParams()
            .AddPrefix("key:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:email", emailParams, emailSchema);

        db.JSON().Set("key:1", "$", "{\"email\": \"test@redis.com\"}");

        SearchResult res4 = db.FT().Search(
            "idx:email",
            new Query("@email:{test\\@redis\\.com}").Dialect(2)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 1

        // Tests for 'em3' step.

        SearchResult res5 = db.FT().Search(
            "idx:bicycle",
            new("@description:\"rough terrain\"")
        );
        Console.WriteLine(res5.TotalResults);   // >>> 1

        // Tests for 'em4' step.

    }
}

```

## On this page
