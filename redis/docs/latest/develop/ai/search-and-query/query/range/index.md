---
title: "Range queries"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/range/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/range/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:49.915Z"
content_hash: "80ce26536d86835e7f0fcda459a7f7f66bdbd795f15130daf298d59e20771379"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Range queries","→","Range queries"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Range queries","→","Range queries"]
---
# Range queries

Perform numeric range queries

A range query on a numeric field returns the values that are in between a given start and end value:

```
FT.SEARCH index "@field:[start end]"
```

You can also use the `FILTER` argument, but you need to know that the query execution plan is different because the filter is applied after the query string (e.g., `*`) is evaluated:

```
FT.SEARCH index "*" FILTER field start end
```

## Start and end values

Start and end values are by default inclusive, but you can prepend `(` to a value to exclude it from the range.

The values `-inf`, `inf`, and `+inf` are valid values that allow you to define open ranges.

## Result set

An open-range query can lead to a large result set.

By default, [`FT.SEARCH`](/docs/latest/commands/ft.search/) returns only the first ten results. The `LIMIT` argument helps you to scroll through the result set. The `SORTBY` argument ensures that the documents in the result set are returned in the specified order.

```
FT.SEARCH index "@field:[start end]" SORTBY field LIMIT page_start page_end
```

You can find further details about using the `LIMIT` and `SORTBY` in the \[[`FT.SEARCH`](/docs/latest/commands/ft.search/) command reference\](/commands/ft.search/).

## Examples

The examples in this section use a schema with the following fields:

Field name

Field type

`price`

`NUMERIC`

The following query finds bicycles within a price range greater than or equal to 500 USD and smaller than or equal to 1000 USD (`500 <= price <= 1000`):

```plaintext
> FT.SEARCH idx:bicycle "@price:[500 1000]"
1) (integer) 3
2) "bicycle:2"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\",\"store_location\":\"-87.6298,41.8781\",\"brand\":\"Nord\",\"model\":\"Chook air 5\",\"price\":815,\"description\":\"The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.\",\"condition\":\"used\"}"
4) "bicycle:5"
5) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\",\"store_location\":\"-0.1278,51.5074\",\"brand\":\"Breakout\",\"model\":\"XBN 2.1 Alloy\",\"price\":810,\"description\":\"The XBN 2.1 Alloy is our entry-level road bike \xe2\x80\x93 but that\xe2\x80\x99s not to say that it\xe2\x80\x99s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano\xe2\x80\x99s, this is a bike which doesn\xe2\x80\x99t break the bank and delivers craved performance.\",\"condition\":\"new\"}"
6) "bicycle:9"
7) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\",\"store_location\":\"12.4964,41.9028\",\"model\":\"ThrillCycle\",\"brand\":\"BikeShind\",\"price\":815,\"description\":\"An artsy,  retro-inspired bicycle that\xe2\x80\x99s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn\xe2\x80\x99t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.\",\"condition\":\"refurbished\"}"
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

res = index.search(Query("@price:[500 1000]"))
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", 500, 1000))
res = index.search(query)
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", "(1000", "+inf"))
res = index.search(query)
print(res.total)
# >>> 5

query = Query('@price:[-inf 2000]').sort_by('price').paging(0, 5)
res = index.search(query)
print(res.total)
print(res)
# >>> Result{7 total, docs: [Document {'id': 'bicycle:0', ... }, Document {'id': 'bicycle:7', ... }, Document {'id': 'bicycle:5', ... }, ...]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE,} from 'redis';

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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000]');
console.log(res1.total); // >>> 3

// FILTER is not supported
// const res2 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: 500,
//     max: 1000,
//   }
// });
// console.log(res2.total); // >>> 3

// FILTER is not supported
// const res3 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: '(1000',
//     max: '+inf,
//   }
// });
// console.log(res3.total); // >>> 5

const res4 = await client.ft.search(
  'idx:bicycle',
  '@price:[-inf 2000]',
  {
    SORTBY: 'price',
    LIMIT: { from: 0, size: 5 }
  }
);
console.log(res4.total); // >>> 7
console.log(res4); // >>> { total: 7, documents: [ { id: 'bicycle:0', value: [Object: null prototype] }, { id: 'bicycle:7', value: [Object: null prototype] }, { id: 'bicycle:5', value: [Object: null prototype] }, { id: 'bicycle:2', value: [Object: null prototype] }, { id: 'bicycle:9', value: [Object: null prototype] } ] }

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.args.SortingOrder;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryRangeExample {

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

        SearchResult res1 = jedis.ftSearch(
            "idx:bicycle", "@price:[500 1000]",
            FTSearchParams.searchParams().returnFields("price"));
        System.out.println(res1.getTotalResults()); // >>> 3

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 500, 1000)
        );
        System.out.println(res2.getTotalResults()); // >>> 3

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 1000, true, Double.POSITIVE_INFINITY, false)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:1 : price 1200
        // >>> bicycle:4 : price 3200
        // >>> bicycle:6 : price 2300
        // >>> bicycle:3 : price 3400
        // >>> bicycle:8 : price 1200

        // Tests for 'range3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle",
            "@price:[-inf 2000]",
            FTSearchParams.searchParams()
                    .returnFields("price")
                    .sortBy("price", SortingOrder.ASC)
                    .limit(0, 5) 
        );
        System.out.println(res4.getTotalResults()); // >>> 7

        List<Document> docs4 = res4.getDocuments();

        for (Document document : docs4) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:0 : price 270
        // >>> bicycle:7 : price 430
        // >>> bicycle:5 : price 810
        // >>> bicycle:2 : price 815
        // >>> bicycle:9 : price 815

        // Tests for 'range4' step.

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

public class QueryRangeExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[500 1000]").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                        return res;
                    }).toCompletableFuture();

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            CompletableFuture<SearchReply<String, String>> priceResults2 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            CompletableFuture<SearchReply<String, String>> priceResults3 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, priceResults2, priceResults3).join();

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

public class QueryRangeExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[500 1000]")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                    });

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            Mono<SearchReply<String, String>> priceResults2 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                    });

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            Mono<SearchReply<String, String>> priceResults3 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                    });

            Mono.when(priceResults, priceResults2, priceResults3).block();

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

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_range() {
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

	res1, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "@price:[500 1000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 3

	for _, doc := range res1.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       500,
					Max:       1000,
				},
			},
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 3

	for _, doc := range res2.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       "(1000",
					Max:       "+inf",
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	for _, doc := range res3.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:1 : price 1200
	// >>> bicycle:4 : price 3200
	// >>> bicycle:6 : price 2300
	// >>> bicycle:3 : price 3400
	// >>> bicycle:8 : price 1200

	res4, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@price:[-inf 2000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			LimitOffset: 0,
			Limit:       5,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 7

	for _, doc := range res4.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:0 : price 270
	// >>> bicycle:7 : price 430
	// >>> bicycle:5 : price 810
	// >>> bicycle:2 : price 815
	// >>> bicycle:9 : price 815

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryRangeExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

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
            new("@price:[500 1000]")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 3

        // Tests for 'range1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 500, 1000)
            )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        // Tests for 'range2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new Query("*").AddFilter(new Query.NumericFilter(
                    "price", 1000, true, Double.PositiveInfinity, false
                )
            )
        );
        Console.WriteLine(res3.TotalResults);   // >>> 5

        // Tests for 'range3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new Query("@price:[-inf 2000]")
                .SetSortBy("price")
                .Limit(0, 5)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 7
        Console.WriteLine($"Prices: {string.Join(", ", res4.Documents.Select(d => d["price"]))}");
        // >>> Prices: 270, 430, 810, 815, 815

        // Tests for 'range4' step.

    }
}

```

This is semantically equivalent to:

```plaintext
> FT.SEARCH idx:bicycle "*" FILTER price 500 1000
1) (integer) 3
2) "bicycle:2"
3) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\",\"store_location\":\"-87.6298,41.8781\",\"brand\":\"Nord\",\"model\":\"Chook air 5\",\"price\":815,\"description\":\"The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.\",\"condition\":\"used\"}"
4) "bicycle:5"
5) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\",\"store_location\":\"-0.1278,51.5074\",\"brand\":\"Breakout\",\"model\":\"XBN 2.1 Alloy\",\"price\":810,\"description\":\"The XBN 2.1 Alloy is our entry-level road bike \xe2\x80\x93 but that\xe2\x80\x99s not to say that it\xe2\x80\x99s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano\xe2\x80\x99s, this is a bike which doesn\xe2\x80\x99t break the bank and delivers craved performance.\",\"condition\":\"new\"}"
6) "bicycle:9"
7) 1) "$"
   2) "{\"pickup_zone\":\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\",\"store_location\":\"12.4964,41.9028\",\"model\":\"ThrillCycle\",\"brand\":\"BikeShind\",\"price\":815,\"description\":\"An artsy,  retro-inspired bicycle that\xe2\x80\x99s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn\xe2\x80\x99t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.\",\"condition\":\"refurbished\"}"
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

res = index.search(Query("@price:[500 1000]"))
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", 500, 1000))
res = index.search(query)
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", "(1000", "+inf"))
res = index.search(query)
print(res.total)
# >>> 5

query = Query('@price:[-inf 2000]').sort_by('price').paging(0, 5)
res = index.search(query)
print(res.total)
print(res)
# >>> Result{7 total, docs: [Document {'id': 'bicycle:0', ... }, Document {'id': 'bicycle:7', ... }, Document {'id': 'bicycle:5', ... }, ...]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE,} from 'redis';

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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000]');
console.log(res1.total); // >>> 3

// FILTER is not supported
// const res2 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: 500,
//     max: 1000,
//   }
// });
// console.log(res2.total); // >>> 3

// FILTER is not supported
// const res3 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: '(1000',
//     max: '+inf,
//   }
// });
// console.log(res3.total); // >>> 5

const res4 = await client.ft.search(
  'idx:bicycle',
  '@price:[-inf 2000]',
  {
    SORTBY: 'price',
    LIMIT: { from: 0, size: 5 }
  }
);
console.log(res4.total); // >>> 7
console.log(res4); // >>> { total: 7, documents: [ { id: 'bicycle:0', value: [Object: null prototype] }, { id: 'bicycle:7', value: [Object: null prototype] }, { id: 'bicycle:5', value: [Object: null prototype] }, { id: 'bicycle:2', value: [Object: null prototype] }, { id: 'bicycle:9', value: [Object: null prototype] } ] }

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.args.SortingOrder;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryRangeExample {

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

        SearchResult res1 = jedis.ftSearch(
            "idx:bicycle", "@price:[500 1000]",
            FTSearchParams.searchParams().returnFields("price"));
        System.out.println(res1.getTotalResults()); // >>> 3

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 500, 1000)
        );
        System.out.println(res2.getTotalResults()); // >>> 3

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 1000, true, Double.POSITIVE_INFINITY, false)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:1 : price 1200
        // >>> bicycle:4 : price 3200
        // >>> bicycle:6 : price 2300
        // >>> bicycle:3 : price 3400
        // >>> bicycle:8 : price 1200

        // Tests for 'range3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle",
            "@price:[-inf 2000]",
            FTSearchParams.searchParams()
                    .returnFields("price")
                    .sortBy("price", SortingOrder.ASC)
                    .limit(0, 5) 
        );
        System.out.println(res4.getTotalResults()); // >>> 7

        List<Document> docs4 = res4.getDocuments();

        for (Document document : docs4) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:0 : price 270
        // >>> bicycle:7 : price 430
        // >>> bicycle:5 : price 810
        // >>> bicycle:2 : price 815
        // >>> bicycle:9 : price 815

        // Tests for 'range4' step.

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

public class QueryRangeExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[500 1000]").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                        return res;
                    }).toCompletableFuture();

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            CompletableFuture<SearchReply<String, String>> priceResults2 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            CompletableFuture<SearchReply<String, String>> priceResults3 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, priceResults2, priceResults3).join();

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

public class QueryRangeExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[500 1000]")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                    });

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            Mono<SearchReply<String, String>> priceResults2 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                    });

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            Mono<SearchReply<String, String>> priceResults3 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                    });

            Mono.when(priceResults, priceResults2, priceResults3).block();

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

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_range() {
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

	res1, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "@price:[500 1000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 3

	for _, doc := range res1.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       500,
					Max:       1000,
				},
			},
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 3

	for _, doc := range res2.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       "(1000",
					Max:       "+inf",
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	for _, doc := range res3.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:1 : price 1200
	// >>> bicycle:4 : price 3200
	// >>> bicycle:6 : price 2300
	// >>> bicycle:3 : price 3400
	// >>> bicycle:8 : price 1200

	res4, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@price:[-inf 2000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			LimitOffset: 0,
			Limit:       5,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 7

	for _, doc := range res4.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:0 : price 270
	// >>> bicycle:7 : price 430
	// >>> bicycle:5 : price 810
	// >>> bicycle:2 : price 815
	// >>> bicycle:9 : price 815

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryRangeExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

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
            new("@price:[500 1000]")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 3

        // Tests for 'range1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 500, 1000)
            )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        // Tests for 'range2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new Query("*").AddFilter(new Query.NumericFilter(
                    "price", 1000, true, Double.PositiveInfinity, false
                )
            )
        );
        Console.WriteLine(res3.TotalResults);   // >>> 5

        // Tests for 'range3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new Query("@price:[-inf 2000]")
                .SetSortBy("price")
                .Limit(0, 5)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 7
        Console.WriteLine($"Prices: {string.Join(", ", res4.Documents.Select(d => d["price"]))}");
        // >>> Prices: 270, 430, 810, 815, 815

        // Tests for 'range4' step.

    }
}

```

For bicycles with a price greater than 1000 USD (`price > 1000`), you can use:

```plaintext
> FT.SEARCH idx:bicycle "@price:[(1000 +inf]"
 1) (integer) 5
 2) "bicycle:1"
 3) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\",\"store_location\":\"-118.2437,34.0522\",\"brand\":\"Bicyk\",\"model\":\"Hillcraft\",\"price\":1200,\"description\":\"Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\\\" wheel bike is just too clumsy coming off a 24\\\" bike. The Hillcraft 26 is just the solution they need!\",\"condition\":\"used\"}"
 4) "bicycle:4"
 5) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\",\"store_location\":\"-122.4194,37.7749\",\"brand\":\"Noka Bikes\",\"model\":\"Kahuna\",\"price\":3200,\"description\":\"Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women\xe2\x80\x99s saddle, different bars and unique colourway.\",\"condition\":\"used\"}"
 6) "bicycle:3"
 7) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\",\"store_location\":\"-80.1918,25.7617\",\"brand\":\"Eva\",\"model\":\"Eva 291\",\"price\":3400,\"description\":\"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It\xe2\x80\x99s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!\",\"condition\":\"used\"}"
 8) "bicycle:6"
 9) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\",\"store_location\":\"2.3522,48.8566\",\"brand\":\"ScramBikes\",\"model\":\"WattBike\",\"price\":2300,\"description\":\"The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It\xe2\x80\x99s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.\",\"condition\":\"new\"}"
10) "bicycle:8"
11) 1) "$"
    2) "{\"pickup_zone\":\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\",\"store_location\":\"2.1734, 41.3851\",\"brand\":\"nHill\",\"model\":\"Summit\",\"price\":1200,\"description\":\"This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\xe2\x80\x99re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.\",\"condition\":\"new\"}"
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

res = index.search(Query("@price:[500 1000]"))
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", 500, 1000))
res = index.search(query)
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", "(1000", "+inf"))
res = index.search(query)
print(res.total)
# >>> 5

query = Query('@price:[-inf 2000]').sort_by('price').paging(0, 5)
res = index.search(query)
print(res.total)
print(res)
# >>> Result{7 total, docs: [Document {'id': 'bicycle:0', ... }, Document {'id': 'bicycle:7', ... }, Document {'id': 'bicycle:5', ... }, ...]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE,} from 'redis';

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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000]');
console.log(res1.total); // >>> 3

// FILTER is not supported
// const res2 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: 500,
//     max: 1000,
//   }
// });
// console.log(res2.total); // >>> 3

// FILTER is not supported
// const res3 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: '(1000',
//     max: '+inf,
//   }
// });
// console.log(res3.total); // >>> 5

const res4 = await client.ft.search(
  'idx:bicycle',
  '@price:[-inf 2000]',
  {
    SORTBY: 'price',
    LIMIT: { from: 0, size: 5 }
  }
);
console.log(res4.total); // >>> 7
console.log(res4); // >>> { total: 7, documents: [ { id: 'bicycle:0', value: [Object: null prototype] }, { id: 'bicycle:7', value: [Object: null prototype] }, { id: 'bicycle:5', value: [Object: null prototype] }, { id: 'bicycle:2', value: [Object: null prototype] }, { id: 'bicycle:9', value: [Object: null prototype] } ] }

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.args.SortingOrder;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryRangeExample {

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

        SearchResult res1 = jedis.ftSearch(
            "idx:bicycle", "@price:[500 1000]",
            FTSearchParams.searchParams().returnFields("price"));
        System.out.println(res1.getTotalResults()); // >>> 3

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 500, 1000)
        );
        System.out.println(res2.getTotalResults()); // >>> 3

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 1000, true, Double.POSITIVE_INFINITY, false)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:1 : price 1200
        // >>> bicycle:4 : price 3200
        // >>> bicycle:6 : price 2300
        // >>> bicycle:3 : price 3400
        // >>> bicycle:8 : price 1200

        // Tests for 'range3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle",
            "@price:[-inf 2000]",
            FTSearchParams.searchParams()
                    .returnFields("price")
                    .sortBy("price", SortingOrder.ASC)
                    .limit(0, 5) 
        );
        System.out.println(res4.getTotalResults()); // >>> 7

        List<Document> docs4 = res4.getDocuments();

        for (Document document : docs4) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:0 : price 270
        // >>> bicycle:7 : price 430
        // >>> bicycle:5 : price 810
        // >>> bicycle:2 : price 815
        // >>> bicycle:9 : price 815

        // Tests for 'range4' step.

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

public class QueryRangeExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[500 1000]").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                        return res;
                    }).toCompletableFuture();

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            CompletableFuture<SearchReply<String, String>> priceResults2 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            CompletableFuture<SearchReply<String, String>> priceResults3 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, priceResults2, priceResults3).join();

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

public class QueryRangeExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[500 1000]")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                    });

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            Mono<SearchReply<String, String>> priceResults2 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                    });

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            Mono<SearchReply<String, String>> priceResults3 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                    });

            Mono.when(priceResults, priceResults2, priceResults3).block();

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

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_range() {
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

	res1, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "@price:[500 1000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 3

	for _, doc := range res1.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       500,
					Max:       1000,
				},
			},
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 3

	for _, doc := range res2.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       "(1000",
					Max:       "+inf",
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	for _, doc := range res3.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:1 : price 1200
	// >>> bicycle:4 : price 3200
	// >>> bicycle:6 : price 2300
	// >>> bicycle:3 : price 3400
	// >>> bicycle:8 : price 1200

	res4, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@price:[-inf 2000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			LimitOffset: 0,
			Limit:       5,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 7

	for _, doc := range res4.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:0 : price 270
	// >>> bicycle:7 : price 430
	// >>> bicycle:5 : price 810
	// >>> bicycle:2 : price 815
	// >>> bicycle:9 : price 815

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryRangeExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

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
            new("@price:[500 1000]")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 3

        // Tests for 'range1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 500, 1000)
            )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        // Tests for 'range2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new Query("*").AddFilter(new Query.NumericFilter(
                    "price", 1000, true, Double.PositiveInfinity, false
                )
            )
        );
        Console.WriteLine(res3.TotalResults);   // >>> 5

        // Tests for 'range3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new Query("@price:[-inf 2000]")
                .SetSortBy("price")
                .Limit(0, 5)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 7
        Console.WriteLine($"Prices: {string.Join(", ", res4.Documents.Select(d => d["price"]))}");
        // >>> Prices: 270, 430, 810, 815, 815

        // Tests for 'range4' step.

    }
}

```

The example below returns bicycles with a price lower than or equal to 2000 USD (`price <= 2000`) by returning the five cheapest bikes:

```plaintext
> FT.SEARCH idx:bicycle "@price:[-inf 2000]" SORTBY price LIMIT 0 5
 1) (integer) 7
 2) "bicycle:0"
 3) 1) "price"
    2) "270"
    3) "$"
    4) "{\"pickup_zone\":\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\",\"store_location\":\"-74.0060,40.7128\",\"brand\":\"Velorim\",\"model\":\"Jigger\",\"price\":270,\"description\":\"Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids\xe2\x80\x99 pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.\",\"condition\":\"new\"}"
 4) "bicycle:7"
 5) 1) "price"
    2) "430"
    3) "$"
    4) "{\"pickup_zone\":\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\",\"store_location\":\"13.4050,52.5200\",\"brand\":\"Peaknetic\",\"model\":\"Secto\",\"price\":430,\"description\":\"If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\",\"condition\":\"new\"}"
 6) "bicycle:5"
 7) 1) "price"
    2) "810"
    3) "$"
    4) "{\"pickup_zone\":\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\",\"store_location\":\"-0.1278,51.5074\",\"brand\":\"Breakout\",\"model\":\"XBN 2.1 Alloy\",\"price\":810,\"description\":\"The XBN 2.1 Alloy is our entry-level road bike \xe2\x80\x93 but that\xe2\x80\x99s not to say that it\xe2\x80\x99s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano\xe2\x80\x99s, this is a bike which doesn\xe2\x80\x99t break the bank and delivers craved performance.\",\"condition\":\"new\"}"
 8) "bicycle:2"
 9) 1) "price"
    2) "815"
    3) "$"
    4) "{\"pickup_zone\":\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\",\"store_location\":\"-87.6298,41.8781\",\"brand\":\"Nord\",\"model\":\"Chook air 5\",\"price\":815,\"description\":\"The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.\",\"condition\":\"used\"}"
10) "bicycle:9"
11) 1) "price"
    2) "815"
    3) "$"
    4) "{\"pickup_zone\":\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\",\"store_location\":\"12.4964,41.9028\",\"model\":\"ThrillCycle\",\"brand\":\"BikeShind\",\"price\":815,\"description\":\"An artsy,  retro-inspired bicycle that\xe2\x80\x99s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn\xe2\x80\x99t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.\",\"condition\":\"refurbished\"}"
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

res = index.search(Query("@price:[500 1000]"))
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", 500, 1000))
res = index.search(query)
print(res.total)
# >>> 3

query = Query("*").add_filter(NumericFilter("price", "(1000", "+inf"))
res = index.search(query)
print(res.total)
# >>> 5

query = Query('@price:[-inf 2000]').sort_by('price').paging(0, 5)
res = index.search(query)
print(res.total)
print(res)
# >>> Result{7 total, docs: [Document {'id': 'bicycle:0', ... }, Document {'id': 'bicycle:7', ... }, Document {'id': 'bicycle:5', ... }, ...]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient, SCHEMA_FIELD_TYPE,} from 'redis';

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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000]');
console.log(res1.total); // >>> 3

// FILTER is not supported
// const res2 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: 500,
//     max: 1000,
//   }
// });
// console.log(res2.total); // >>> 3

// FILTER is not supported
// const res3 = await client.ft.search('idx:bicycle', '*', {
//   FILTER: {
//     field: 'price',
//     min: '(1000',
//     max: '+inf,
//   }
// });
// console.log(res3.total); // >>> 5

const res4 = await client.ft.search(
  'idx:bicycle',
  '@price:[-inf 2000]',
  {
    SORTBY: 'price',
    LIMIT: { from: 0, size: 5 }
  }
);
console.log(res4.total); // >>> 7
console.log(res4); // >>> { total: 7, documents: [ { id: 'bicycle:0', value: [Object: null prototype] }, { id: 'bicycle:7', value: [Object: null prototype] }, { id: 'bicycle:5', value: [Object: null prototype] }, { id: 'bicycle:2', value: [Object: null prototype] }, { id: 'bicycle:9', value: [Object: null prototype] } ] }

```

```java

import java.util.List;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.args.SortingOrder;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryRangeExample {

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

        SearchResult res1 = jedis.ftSearch(
            "idx:bicycle", "@price:[500 1000]",
            FTSearchParams.searchParams().returnFields("price"));
        System.out.println(res1.getTotalResults()); // >>> 3

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 500, 1000)
        );
        System.out.println(res2.getTotalResults()); // >>> 3

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:2 : price 815
        // >>> bicycle:5 : price 810
        // >>> bicycle:9 : price 815

        // Tests for 'range2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "*",
            FTSearchParams.searchParams()
                .returnFields("price")
                .filter("price", 1000, true, Double.POSITIVE_INFINITY, false)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:1 : price 1200
        // >>> bicycle:4 : price 3200
        // >>> bicycle:6 : price 2300
        // >>> bicycle:3 : price 3400
        // >>> bicycle:8 : price 1200

        // Tests for 'range3' step.

        SearchResult res4 = jedis.ftSearch("idx:bicycle",
            "@price:[-inf 2000]",
            FTSearchParams.searchParams()
                    .returnFields("price")
                    .sortBy("price", SortingOrder.ASC)
                    .limit(0, 5) 
        );
        System.out.println(res4.getTotalResults()); // >>> 7

        List<Document> docs4 = res4.getDocuments();

        for (Document document : docs4) {
            System.out.println(document.getId() + " : price " + document.getString("price"));
        }
        // >>> bicycle:0 : price 270
        // >>> bicycle:7 : price 430
        // >>> bicycle:5 : price 810
        // >>> bicycle:2 : price 815
        // >>> bicycle:9 : price 815

        // Tests for 'range4' step.

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

public class QueryRangeExample {

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

            CompletableFuture<SearchReply<String, String>> priceResults = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[500 1000]").thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                        return res;
                    }).toCompletableFuture();

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            CompletableFuture<SearchReply<String, String>> priceResults2 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                        return res;
                    }).toCompletableFuture();

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            CompletableFuture<SearchReply<String, String>> priceResults3 = asyncCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).thenApply(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                        return res;
                    }).toCompletableFuture();

            CompletableFuture.allOf(priceResults, priceResults2, priceResults3).join();

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

public class QueryRangeExample {

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

            Mono<SearchReply<String, String>> priceResults = reactiveCommands.ftSearch("idx:bicycle", "@price:[500 1000]")
                    .doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s\n", doc.getId());
                        });
                        // >>> ID: bicycle:2
                        // >>> ID: bicycle:5
                        // >>> ID: bicycle:9
                    });

            // `Filter` is not supported.

            SearchArgs<String, String> priceSearchArgs2 = SearchArgs.<String, String> builder().returnField("price").build();

            Mono<SearchReply<String, String>> priceResults2 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[(1000 +inf]", priceSearchArgs2).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:1, price: 1200
                        // >>> ID: bicycle:3, price: 3400
                        // >>> ID: bicycle:4, price: 3200
                        // >>> ID: bicycle:6, price: 2300
                        // >>> ID: bicycle:8, price: 1200
                    });

            SearchArgs<String, String> priceSearchArgs3 = SearchArgs.<String, String> builder().returnField("price")
                    .sortBy(SortByArgs.<String> builder().attribute("price").build()).limit(0, 5).build();

            Mono<SearchReply<String, String>> priceResults3 = reactiveCommands
                    .ftSearch("idx:bicycle", "@price:[-inf 2000]", priceSearchArgs3).doOnNext(res -> {
                        res.getResults().stream().sorted((doc1, doc2) -> doc1.getId().compareTo(doc2.getId())).forEach(doc -> {
                            System.out.printf("ID: %s, price: %s\n", doc.getId(), doc.getFields().get("price"));
                        });
                        // >>> ID: bicycle:0, price: 270
                        // >>> ID: bicycle:2, price: 815
                        // >>> ID: bicycle:5, price: 810
                        // >>> ID: bicycle:7, price: 430
                        // >>> ID: bicycle:9, price: 815
                    });

            Mono.when(priceResults, priceResults2, priceResults3).block();

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

	"github.com/redis/go-redis/v9"
)

func ExampleClient_query_range() {
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

	res1, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "@price:[500 1000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 3

	for _, doc := range res1.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       500,
					Max:       1000,
				},
			},
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 3

	for _, doc := range res2.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:2 : price 815
	// >>> bicycle:5 : price 810
	// >>> bicycle:9 : price 815

	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			Filters: []redis.FTSearchFilter{
				{
					FieldName: "price",
					Min:       "(1000",
					Max:       "+inf",
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	for _, doc := range res3.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:1 : price 1200
	// >>> bicycle:4 : price 3200
	// >>> bicycle:6 : price 2300
	// >>> bicycle:3 : price 3400
	// >>> bicycle:8 : price 1200

	res4, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@price:[-inf 2000]",
		&redis.FTSearchOptions{
			Return: []redis.FTSearchReturn{
				{
					FieldName: "price",
				},
			},
			SortBy: []redis.FTSearchSortBy{
				{
					FieldName: "price",
					Asc:       true,
				},
			},
			LimitOffset: 0,
			Limit:       5,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4.Total) // >>> 7

	for _, doc := range res4.Docs {
		fmt.Printf("%v : price %v\n", doc.ID, doc.Fields["price"])
	}
	// >>> bicycle:0 : price 270
	// >>> bicycle:7 : price 430
	// >>> bicycle:5 : price 810
	// >>> bicycle:2 : price 815
	// >>> bicycle:9 : price 815

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryRangeExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTextField(new FieldName("$.description", "description"))
            .AddNumericField(new FieldName("$.price", "price"))
            .AddTagField(new FieldName("$.condition", "condition"));

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
            new("@price:[500 1000]")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 3

        // Tests for 'range1' step.

        SearchResult res2 = db.FT().Search(
            "idx:bicycle",
            new Query().AddFilter(
                new Query.NumericFilter("price", 500, 1000)
            )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        // Tests for 'range2' step.

        SearchResult res3 = db.FT().Search(
            "idx:bicycle",
            new Query("*").AddFilter(new Query.NumericFilter(
                    "price", 1000, true, Double.PositiveInfinity, false
                )
            )
        );
        Console.WriteLine(res3.TotalResults);   // >>> 5

        // Tests for 'range3' step.

        SearchResult res4 = db.FT().Search(
            "idx:bicycle",
            new Query("@price:[-inf 2000]")
                .SetSortBy("price")
                .Limit(0, 5)
        );
        Console.WriteLine(res4.TotalResults);   // >>> 7
        Console.WriteLine($"Prices: {string.Join(", ", res4.Documents.Select(d => d["price"]))}");
        // >>> Prices: 270, 430, 810, 815, 815

        // Tests for 'range4' step.

    }
}

```

## Non-numeric range queries

You can learn more about non-numeric range queries, such as [geospatial](/docs/latest/develop/ai/search-and-query/query/geo-spatial/) or [vector search](/docs/latest/develop/ai/search-and-query/query/vector-search/) queries, in their dedicated articles.

## On this page
