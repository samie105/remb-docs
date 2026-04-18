---
title: "Aggregation queries"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/aggregation/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:15:50.568Z"
content_hash: "99a4146ebf22feaad10077f7cf26bd8252b74c4048a9c745fcbbe665160429a1"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Aggregation queries","→","Aggregation queries"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Aggregation queries","→","Aggregation queries"]
nav_prev: {"path": "redis/docs/latest/integrate/write-behind/reference/data-transformation-block-types/add_field/index.md", "title": "add_field"}
---

# Aggregation queries

Group and aggregate query results

An aggregation query allows you to perform the following actions:

*   Apply simple mapping functions.
*   Group data based on field values.
*   Apply aggregation functions on the grouped data.

This article explains the basic usage of the [FT.AGGREGATE](/docs/latest/commands/ft.aggregate/) command. For further details, see the [command specification](/docs/latest/commands/ft.aggregate/) and the [aggregations reference documentation](/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations/).

The examples in this article use a schema with the following fields:

Field name

Field type

`condition`

`TAG`

`price`

`NUMERIC`

## Simple mapping

The `APPLY` clause allows you to apply a simple mapping function to a result set that is returned based on the query expression.

```
FT.AGGREGATE index "query_expr" LOAD n "field_1" .. "field_n" APPLY "function_expr" AS "result_field"
```

Here is a more detailed explanation of the query syntax:

1.  **Query expression**: you can use the same query expressions as you would use with the [`FT.SEARCH`](/docs/latest/commands/ft.search/) command. You can substitute `query_expr` with any of the expressions explained in the articles of this [query topic](/docs/latest/develop/ai/search-and-query/query/). Vector search queries are an exception. You can't combine a vector search with an aggregation query.
2.  **Loaded fields**: if field values weren't already loaded into the aggregation pipeline, you can force their presence via the `LOAD` clause. This clause takes the number of fields (`n`), followed by the field names (`"field_1" .. "field_n"`).
3.  **Mapping function**: this mapping function operates on the field values. A specific field is referenced as `@field_name` within the function expression. The result is returned as `result_field`.

The following example shows you how to calculate a discounted price for new bicycles:

```plaintext
FT.AGGREGATE idx:bicycle "@condition:{new}" LOAD 2 "__key" "price" APPLY "@price - (@price * 0.1)" AS "discounted"
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search import Search
from redis.commands.search.aggregation import AggregateRequest
from redis.commands.search.field import NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
import redis.commands.search.reducers as reducers

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
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

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='@condition:{new}') \
    .load('__key', 'price') \
    .apply(discounted='@price - (@price * 0.1)')
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 5
print(res.rows) # >>> [['__key', 'bicycle:0', ...
#[['__key', 'bicycle:0', 'price', '270', 'discounted', '243'],
# ['__key', 'bicycle:5', 'price', '810', 'discounted', '729'],
# ['__key', 'bicycle:6', 'price', '2300', 'discounted', '2070'],
# ['__key', 'bicycle:7', 'price', '430', 'discounted', '387'],
# ['__key', 'bicycle:8', 'price', '1200', 'discounted', '1080']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('price') \
    .apply(price_category='@price<1000') \
    .group_by('@condition', reducers.sum('@price_category').alias('num_affordable'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'num_affordable', '1'],
# ['condition', 'used', 'num_affordable', '1'],
# ['condition', 'new', 'num_affordable', '3']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .apply(type="'bicycle'") \
    .group_by('@type', reducers.count().alias('num_total'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 1
print(res.rows) # >>> [['type', 'bicycle', 'num_total', '10']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('__key') \
    .group_by('@condition', reducers.tolist('__key').alias('bicycles'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'bicycles', ['bicycle:9']],
# ['condition', 'used', 'bicycles', ['bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4']],
# ['condition', 'new', 'bicycles', ['bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8']]]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, FT_AGGREGATE_STEPS, FT_AGGREGATE_GROUP_BY_REDUCERS } from '@redis/search';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
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

const res1 = await client.ft.aggregate('idx:bicycle', '@condition:{new}', {
  LOAD: ['__key', 'price'],
  APPLY: {
    expression: '@price - (@price * 0.1)',
    AS: 'discounted'
  }
});

console.log(res1.results.length); // >>> 5
console.log(res1.results); // >>>
//[
//  [Object: null prototype] { __key: 'bicycle:0', price: '270' },
//  [Object: null prototype] { __key: 'bicycle:5', price: '810' },
//  [Object: null prototype] { __key: 'bicycle:6', price: '2300' },
//  [Object: null prototype] { __key: 'bicycle:7', price: '430' },
//  [Object: null prototype] { __key: 'bicycle:8', price: '1200' }
//]

const res2 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['@price'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: '@price<1000',
      AS: 'price_category'
    },{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE:[{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.SUM,
        property: '@price_category',
        AS: 'num_affordable'
      }]
    }]
});
console.log(res2.results.length); // >>> 3
console.log(res2.results); // >>>
//[[Object: null prototype] { condition: 'refurbished', num_affordable: '1' },
//  [Object: null prototype] { condition: 'used', num_affordable: '1' },
//  [Object: null prototype] { condition: 'new', num_affordable: '3' }
//]

const res3 = await client.ft.aggregate('idx:bicycle', '*', {
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: "'bicycle'",
      AS: 'type'
    }, {
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@type',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
        property: null,
        AS: 'num_total'
      }]
    }]
});
console.log(res3.results.length); // >>> 1
console.log(res3.results); // >>>
//[ [Object: null prototype] { type: 'bicycle', num_total: '10' } ]

const res4 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['__key'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.TOLIST,
        property: '__key',
        AS: 'bicycles'
      }]
    }]
});
console.log(res4.results.length); // >>> 3
console.log(res4.results); // >>>
//[[Object: null prototype] {condition: 'refurbished', bicycles: [ 'bicycle:9' ]},
//  [Object: null prototype] {condition: 'used', bicycles: [ 'bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4' ]},
//  [Object: null prototype] {condition: 'new', bicycles: [ 'bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8' ]}]

```

```java

import java.util.List;
import java.util.ArrayList;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class QueryAggExample {

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
            jedis.jsonSet("bicycle:" + i, new Path2("$"), bicycleJsons[i]);
        }

        AggregationResult res1 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("@condition:{new}")
                    .load("__key", "price")
                    .apply("@price - (@price * 0.1)", "discounted")
        );
        
        List<Row> rows1 = res1.getRows();
        System.out.println(rows1.size());   // >>> 5

        for (int i = 0; i < rows1.size(); i++) {
            System.out.println(rows1.get(i));
        }
        // >>> {__key=bicycle:0, discounted=243, price=270}
        // >>> {__key=bicycle:5, discounted=729, price=810}
        // >>> {__key=bicycle:6, discounted=2070, price=2300}
        // >>> {__key=bicycle:7, discounted=387, price=430}
        // >>> {__key=bicycle:8, discounted=1080, price=1200}

        // Tests for 'agg1' step.

        AggregationResult res2 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("price")
                    .apply("@price<1000", "price_category")
                    .groupBy("@condition",
                        Reducers.sum("@price_category").as("num_affordable"))
        );

        List<Row> rows2 = res2.getRows();
        System.out.println(rows2.size());   // >>> 3

        for (int i = 0; i < rows2.size(); i++) {
            System.out.println(rows2.get(i));
        }
        // >>> {condition=refurbished, num_affordable=1}
        // >>> {condition=used, num_affordable=1}
        // >>> {condition=new, num_affordable=3}

        // Tests for 'agg2' step.

        AggregationResult res3 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .apply("'bicycle'", "type")
                    .groupBy("@type", Reducers.count().as("num_total"))
        );

        List<Row> rows3 = res3.getRows();
        System.out.println(rows3.size());   // >>> 1

        for (int i = 0; i < rows3.size(); i++) {
            System.out.println(rows3.get(i));
        }
        // >>> {type=bicycle, num_total=10}

        // Tests for 'agg3' step.

        AggregationResult res4 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("__key")
                    .groupBy("@condition",
                        Reducers.to_list("__key").as("bicycles"))
        );

        List<Row> rows4 = res4.getRows();
        System.out.println(rows4.size());   // >>> 3

        for (int i = 0; i < rows4.size(); i++) {
            System.out.println(rows4.get(i));
        }
        // >>> {condition=refurbished, bicycles=[bicycle:9]}
        // >>> {condition=used, bicycles=[bicycle:3, bicycle:4, bicycle:1, bicycle:2]}
        // >>> {condition=new, bicycles=[bicycle:7, bicycle:0, bicycle:5, bicycle:6, bicycle:8]}

        // Tests for 'agg4' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            JsonParser parser = asyncCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<Void> setup = asyncCommands.ftCreate("idx:bicycle", createArgs, schema).thenCompose(result -> {
                CompletableFuture<Void> loadData = CompletableFuture.completedFuture(null);
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadData = loadData.thenCompose(v -> asyncCommands
                            .jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)).thenApply(res -> null));
                }
                return loadData;
            }).toCompletableFuture();
            setup.join();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            CompletableFuture<AggregationReply<String, String>> agg1 = asyncCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg2 = asyncCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg3 = asyncCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                        return result;
                    }).toCompletableFuture();

            // The `TOLIST` reducer is not currently available in Lettuce.

            // Wait for all aggregations to complete
            CompletableFuture.allOf(agg1, agg2, agg3).join();

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
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import reactor.core.publisher.Mono;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            JsonParser parser = reactiveCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<String> setup = reactiveCommands.ftCreate("idx:bicycle", createArgs, schema).flatMap(result -> {
                // load data sequentially using reactive chains
                Mono<String> loadChain = Mono.just("OK");
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadChain = loadChain.flatMap(
                            v -> reactiveCommands.jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)));
                }
                return loadChain;
            });

            setup.block();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            Mono<AggregationReply<String, String>> agg1 = reactiveCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                    });

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            Mono<AggregationReply<String, String>> agg2 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                    });

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            Mono<AggregationReply<String, String>> agg3 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                    });

            // The `TOLIST` reducer is not currently available in Lettuce.

            Mono.when(agg1, agg2, agg3).block();
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

func ExampleClient_query_agg() {
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

	res1, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle",
		"@condition:{new}",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price - (@price * 0.1)",
					As:    "discounted",
				},
			},
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
				{Field: "price"},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res1.Rows)) // >>> 5

	sort.Slice(res1.Rows, func(i, j int) bool {
		return res1.Rows[i].Fields["__key"].(string) <
			res1.Rows[j].Fields["__key"].(string)
	})

	for _, row := range res1.Rows {
		fmt.Printf(
			"__key=%v, discounted=%v, price=%v\n",
			row.Fields["__key"],
			row.Fields["discounted"],
			row.Fields["price"],
		)
	}
	// >>> __key=bicycle:0, discounted=243, price=270
	// >>> __key=bicycle:5, discounted=729, price=810
	// >>> __key=bicycle:6, discounted=2070, price=2300
	// >>> __key=bicycle:7, discounted=387, price=430
	// >>> __key=bicycle:8, discounted=1080, price=1200

	res2, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "price"},
			},
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price<1000",
					As:    "price_category",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchSum,
							Args:    []interface{}{"@price_category"},
							As:      "num_affordable",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res2.Rows)) // >>> 3

	sort.Slice(res2.Rows, func(i, j int) bool {
		return res2.Rows[i].Fields["condition"].(string) <
			res2.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res2.Rows {
		fmt.Printf(
			"condition=%v, num_affordable=%v\n",
			row.Fields["condition"],
			row.Fields["num_affordable"],
		)
	}
	// >>> condition=new, num_affordable=3
	// >>> condition=refurbished, num_affordable=1
	// >>> condition=used, num_affordable=1

	res3, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "'bicycle'",
					As:    "type",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@type"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchCount,
							As:      "num_total",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res3.Rows)) // >>> 1

	for _, row := range res3.Rows {
		fmt.Printf(
			"type=%v, num_total=%v\n",
			row.Fields["type"],
			row.Fields["num_total"],
		)
	}
	// type=bicycle, num_total=10

	res4, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchToList,
							Args:    []interface{}{"__key"},
							As:      "bicycles",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res4.Rows)) // >>> 3

	sort.Slice(res4.Rows, func(i, j int) bool {
		return res4.Rows[i].Fields["condition"].(string) <
			res4.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res4.Rows {
		rowBikes := row.Fields["bicycles"].([]interface{})
		bikes := make([]string, len(rowBikes))

		for i, rowBike := range rowBikes {
			bikes[i] = rowBike.(string)
		}

		sort.Slice(bikes, func(i, j int) bool {
			return bikes[i] < bikes[j]
		})

		fmt.Printf(
			"condition=%v, bicycles=%v\n",
			row.Fields["condition"],
			bikes,
		)
	}
	// >>> condition=new, bicycles=[bicycle:0 bicycle:5 bicycle:6 bicycle:7 bicycle:8]
	// >>> condition=refurbished, bicycles=[bicycle:9]
	// >>> condition=used, bicycles=[bicycle:1 bicycle:2 bicycle:3 bicycle:4]

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Aggregation;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryAggExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTagField(new FieldName("$.condition", "condition"))
            .AddNumericField(new FieldName("$.price", "price"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[] {
            new
            {
                pickup_zone = "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))",
                store_location = "-74.0060,40.7128",
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))",
                store_location = "-118.2437,34.0522",
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\" wheel bike is just too clumsy coming off a 24\" bike. The Hillcraft 26 is just the solution they need!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))",
                store_location = "-87.6298,41.8781",
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))",
                store_location = "-80.1918,25.7617",
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))",
                store_location = "-122.4194,37.7749",
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women’s saddle, different bars and unique colourway.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))",
                store_location = "-0.1278,51.5074",
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s not to say that it’s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which doesn’t break the bank and delivers craved performance.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))",
                store_location = "2.3522,48.8566",
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It’s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))",
                store_location = "13.4050,52.5200",
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))",
                store_location = "2.1734, 41.3851",
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you’re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
                store_location = "12.4964,41.9028",
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.",
                condition = "refurbished"
            }
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        AggregationResult res1 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("@condition:{new}")
                .Load(new FieldName("__key"), new FieldName("price"))
                .Apply("@price - (@price * 0.1)", "discounted")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 5

        for (int i = 0; i < res1.TotalResults; i++)
        {
            Row res1Row = res1.GetRow(i);

            Console.WriteLine(
                $"Key: {res1Row["__key"]}, Price: {res1Row["price"]}, Discounted: {res1Row["discounted"]}"
            );
        }
        // >>> Key: bicycle:0, Price: 270, Discounted: 243
        // >>> Key: bicycle:5, Price: 810, Discounted: 729
        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
        // >>> Key: bicycle:7, Price: 430, Discounted: 387
        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080

        // Tests for 'agg1' step.

        AggregationResult res2 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Load(new FieldName("price"))
                .Apply("@price<1000", "price_category")
                .GroupBy(
                    "@condition",
                    Reducers.Sum("@price_category").As("num_affordable")
                )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        for (int i = 0; i < res2.TotalResults; i++)
        {
            Row res2Row = res2.GetRow(i);

            Console.WriteLine(
                $"Condition: {res2Row["condition"]}, Num affordable: {res2Row["num_affordable"]}"
            );
        }
        // >>> Condition: refurbished, Num affordable: 1
        // >>> Condition: used, Num affordable: 1
        // >>> Condition: new, Num affordable: 3

        // Tests for 'agg2' step.

        AggregationResult res3 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Apply("'bicycle'", "type")
                .GroupBy("@type", Reducers.Count().As("num_total"))
        );
        Console.WriteLine(res3.TotalResults);   // >>> 1

        Row res3Row = res3.GetRow(0);
        Console.WriteLine($"Type: {res3Row["type"]}, Num total: {res3Row["num_total"]}");
        // >>> Type: bicycle, Num total: 10

        // Tests for 'agg3' step.

        // Not supported in NRedisStack.

        // Tests for 'agg4' step.

    }
}

```

The field `__key` is a built-in field.

The output of this query is:

```
1) "1"
2) 1) "__key"
   1) "bicycle:0"
   2) "price"
   3) "270"
   4) "discounted"
   5) "243"
3) 1) "__key"
   1) "bicycle:5"
   2) "price"
   3) "810"
   4) "discounted"
   5) "729"
4) 1) "__key"
   1) "bicycle:6"
   2) "price"
   3) "2300"
   4) "discounted"
   5) "2070"
...
```

## Grouping with aggregation

The previous example did not group the data. You can group and aggregate data based on one or many criteria in the following way:

```
FT.AGGREGATE index "query_expr" ...  GROUPBY n "field_1" .. "field_n" REDUCE AGG_FUNC m "@field_param_1" .. "@field_param_m" AS "aggregated_result_field"
```

Here is an explanation of the additional constructs:

1.  **Grouping**: you can group by one or many fields. Each ordered sequence of field values then defines one group. It's also possible to group by values that resulted from a previous `APPLY ... AS`.
2.  **Aggregation**: you must replace `AGG_FUNC` with one of the supported aggregation functions (e.g., `SUM` or `COUNT`). A complete list of functions is available in the [aggregations reference documentation](/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations/). Replace `aggregated_result_field` with a value of your choice.

The following query shows you how to group by the field `condition` and apply a reduction based on the previously derived `price_category`. The expression `@price<1000` causes a bicycle to have the price category `1` if its price is lower than 1000 USD. Otherwise, it has the price category `0`. The output is the number of affordable bicycles grouped by price category.

```plaintext
FT.AGGREGATE idx:bicycle "*" LOAD 1 price APPLY "@price<1000" AS price_category GROUPBY 1 @condition REDUCE SUM 1 "@price_category" AS "num_affordable"
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search import Search
from redis.commands.search.aggregation import AggregateRequest
from redis.commands.search.field import NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
import redis.commands.search.reducers as reducers

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
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

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='@condition:{new}') \
    .load('__key', 'price') \
    .apply(discounted='@price - (@price * 0.1)')
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 5
print(res.rows) # >>> [['__key', 'bicycle:0', ...
#[['__key', 'bicycle:0', 'price', '270', 'discounted', '243'],
# ['__key', 'bicycle:5', 'price', '810', 'discounted', '729'],
# ['__key', 'bicycle:6', 'price', '2300', 'discounted', '2070'],
# ['__key', 'bicycle:7', 'price', '430', 'discounted', '387'],
# ['__key', 'bicycle:8', 'price', '1200', 'discounted', '1080']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('price') \
    .apply(price_category='@price<1000') \
    .group_by('@condition', reducers.sum('@price_category').alias('num_affordable'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'num_affordable', '1'],
# ['condition', 'used', 'num_affordable', '1'],
# ['condition', 'new', 'num_affordable', '3']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .apply(type="'bicycle'") \
    .group_by('@type', reducers.count().alias('num_total'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 1
print(res.rows) # >>> [['type', 'bicycle', 'num_total', '10']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('__key') \
    .group_by('@condition', reducers.tolist('__key').alias('bicycles'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'bicycles', ['bicycle:9']],
# ['condition', 'used', 'bicycles', ['bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4']],
# ['condition', 'new', 'bicycles', ['bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8']]]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, FT_AGGREGATE_STEPS, FT_AGGREGATE_GROUP_BY_REDUCERS } from '@redis/search';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
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

const res1 = await client.ft.aggregate('idx:bicycle', '@condition:{new}', {
  LOAD: ['__key', 'price'],
  APPLY: {
    expression: '@price - (@price * 0.1)',
    AS: 'discounted'
  }
});

console.log(res1.results.length); // >>> 5
console.log(res1.results); // >>>
//[
//  [Object: null prototype] { __key: 'bicycle:0', price: '270' },
//  [Object: null prototype] { __key: 'bicycle:5', price: '810' },
//  [Object: null prototype] { __key: 'bicycle:6', price: '2300' },
//  [Object: null prototype] { __key: 'bicycle:7', price: '430' },
//  [Object: null prototype] { __key: 'bicycle:8', price: '1200' }
//]

const res2 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['@price'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: '@price<1000',
      AS: 'price_category'
    },{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE:[{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.SUM,
        property: '@price_category',
        AS: 'num_affordable'
      }]
    }]
});
console.log(res2.results.length); // >>> 3
console.log(res2.results); // >>>
//[[Object: null prototype] { condition: 'refurbished', num_affordable: '1' },
//  [Object: null prototype] { condition: 'used', num_affordable: '1' },
//  [Object: null prototype] { condition: 'new', num_affordable: '3' }
//]

const res3 = await client.ft.aggregate('idx:bicycle', '*', {
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: "'bicycle'",
      AS: 'type'
    }, {
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@type',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
        property: null,
        AS: 'num_total'
      }]
    }]
});
console.log(res3.results.length); // >>> 1
console.log(res3.results); // >>>
//[ [Object: null prototype] { type: 'bicycle', num_total: '10' } ]

const res4 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['__key'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.TOLIST,
        property: '__key',
        AS: 'bicycles'
      }]
    }]
});
console.log(res4.results.length); // >>> 3
console.log(res4.results); // >>>
//[[Object: null prototype] {condition: 'refurbished', bicycles: [ 'bicycle:9' ]},
//  [Object: null prototype] {condition: 'used', bicycles: [ 'bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4' ]},
//  [Object: null prototype] {condition: 'new', bicycles: [ 'bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8' ]}]

```

```java

import java.util.List;
import java.util.ArrayList;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class QueryAggExample {

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
            jedis.jsonSet("bicycle:" + i, new Path2("$"), bicycleJsons[i]);
        }

        AggregationResult res1 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("@condition:{new}")
                    .load("__key", "price")
                    .apply("@price - (@price * 0.1)", "discounted")
        );
        
        List<Row> rows1 = res1.getRows();
        System.out.println(rows1.size());   // >>> 5

        for (int i = 0; i < rows1.size(); i++) {
            System.out.println(rows1.get(i));
        }
        // >>> {__key=bicycle:0, discounted=243, price=270}
        // >>> {__key=bicycle:5, discounted=729, price=810}
        // >>> {__key=bicycle:6, discounted=2070, price=2300}
        // >>> {__key=bicycle:7, discounted=387, price=430}
        // >>> {__key=bicycle:8, discounted=1080, price=1200}

        // Tests for 'agg1' step.

        AggregationResult res2 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("price")
                    .apply("@price<1000", "price_category")
                    .groupBy("@condition",
                        Reducers.sum("@price_category").as("num_affordable"))
        );

        List<Row> rows2 = res2.getRows();
        System.out.println(rows2.size());   // >>> 3

        for (int i = 0; i < rows2.size(); i++) {
            System.out.println(rows2.get(i));
        }
        // >>> {condition=refurbished, num_affordable=1}
        // >>> {condition=used, num_affordable=1}
        // >>> {condition=new, num_affordable=3}

        // Tests for 'agg2' step.

        AggregationResult res3 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .apply("'bicycle'", "type")
                    .groupBy("@type", Reducers.count().as("num_total"))
        );

        List<Row> rows3 = res3.getRows();
        System.out.println(rows3.size());   // >>> 1

        for (int i = 0; i < rows3.size(); i++) {
            System.out.println(rows3.get(i));
        }
        // >>> {type=bicycle, num_total=10}

        // Tests for 'agg3' step.

        AggregationResult res4 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("__key")
                    .groupBy("@condition",
                        Reducers.to_list("__key").as("bicycles"))
        );

        List<Row> rows4 = res4.getRows();
        System.out.println(rows4.size());   // >>> 3

        for (int i = 0; i < rows4.size(); i++) {
            System.out.println(rows4.get(i));
        }
        // >>> {condition=refurbished, bicycles=[bicycle:9]}
        // >>> {condition=used, bicycles=[bicycle:3, bicycle:4, bicycle:1, bicycle:2]}
        // >>> {condition=new, bicycles=[bicycle:7, bicycle:0, bicycle:5, bicycle:6, bicycle:8]}

        // Tests for 'agg4' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            JsonParser parser = asyncCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<Void> setup = asyncCommands.ftCreate("idx:bicycle", createArgs, schema).thenCompose(result -> {
                CompletableFuture<Void> loadData = CompletableFuture.completedFuture(null);
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadData = loadData.thenCompose(v -> asyncCommands
                            .jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)).thenApply(res -> null));
                }
                return loadData;
            }).toCompletableFuture();
            setup.join();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            CompletableFuture<AggregationReply<String, String>> agg1 = asyncCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg2 = asyncCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg3 = asyncCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                        return result;
                    }).toCompletableFuture();

            // The `TOLIST` reducer is not currently available in Lettuce.

            // Wait for all aggregations to complete
            CompletableFuture.allOf(agg1, agg2, agg3).join();

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
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import reactor.core.publisher.Mono;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            JsonParser parser = reactiveCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<String> setup = reactiveCommands.ftCreate("idx:bicycle", createArgs, schema).flatMap(result -> {
                // load data sequentially using reactive chains
                Mono<String> loadChain = Mono.just("OK");
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadChain = loadChain.flatMap(
                            v -> reactiveCommands.jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)));
                }
                return loadChain;
            });

            setup.block();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            Mono<AggregationReply<String, String>> agg1 = reactiveCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                    });

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            Mono<AggregationReply<String, String>> agg2 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                    });

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            Mono<AggregationReply<String, String>> agg3 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                    });

            // The `TOLIST` reducer is not currently available in Lettuce.

            Mono.when(agg1, agg2, agg3).block();
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

func ExampleClient_query_agg() {
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

	res1, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle",
		"@condition:{new}",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price - (@price * 0.1)",
					As:    "discounted",
				},
			},
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
				{Field: "price"},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res1.Rows)) // >>> 5

	sort.Slice(res1.Rows, func(i, j int) bool {
		return res1.Rows[i].Fields["__key"].(string) <
			res1.Rows[j].Fields["__key"].(string)
	})

	for _, row := range res1.Rows {
		fmt.Printf(
			"__key=%v, discounted=%v, price=%v\n",
			row.Fields["__key"],
			row.Fields["discounted"],
			row.Fields["price"],
		)
	}
	// >>> __key=bicycle:0, discounted=243, price=270
	// >>> __key=bicycle:5, discounted=729, price=810
	// >>> __key=bicycle:6, discounted=2070, price=2300
	// >>> __key=bicycle:7, discounted=387, price=430
	// >>> __key=bicycle:8, discounted=1080, price=1200

	res2, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "price"},
			},
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price<1000",
					As:    "price_category",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchSum,
							Args:    []interface{}{"@price_category"},
							As:      "num_affordable",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res2.Rows)) // >>> 3

	sort.Slice(res2.Rows, func(i, j int) bool {
		return res2.Rows[i].Fields["condition"].(string) <
			res2.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res2.Rows {
		fmt.Printf(
			"condition=%v, num_affordable=%v\n",
			row.Fields["condition"],
			row.Fields["num_affordable"],
		)
	}
	// >>> condition=new, num_affordable=3
	// >>> condition=refurbished, num_affordable=1
	// >>> condition=used, num_affordable=1

	res3, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "'bicycle'",
					As:    "type",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@type"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchCount,
							As:      "num_total",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res3.Rows)) // >>> 1

	for _, row := range res3.Rows {
		fmt.Printf(
			"type=%v, num_total=%v\n",
			row.Fields["type"],
			row.Fields["num_total"],
		)
	}
	// type=bicycle, num_total=10

	res4, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchToList,
							Args:    []interface{}{"__key"},
							As:      "bicycles",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res4.Rows)) // >>> 3

	sort.Slice(res4.Rows, func(i, j int) bool {
		return res4.Rows[i].Fields["condition"].(string) <
			res4.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res4.Rows {
		rowBikes := row.Fields["bicycles"].([]interface{})
		bikes := make([]string, len(rowBikes))

		for i, rowBike := range rowBikes {
			bikes[i] = rowBike.(string)
		}

		sort.Slice(bikes, func(i, j int) bool {
			return bikes[i] < bikes[j]
		})

		fmt.Printf(
			"condition=%v, bicycles=%v\n",
			row.Fields["condition"],
			bikes,
		)
	}
	// >>> condition=new, bicycles=[bicycle:0 bicycle:5 bicycle:6 bicycle:7 bicycle:8]
	// >>> condition=refurbished, bicycles=[bicycle:9]
	// >>> condition=used, bicycles=[bicycle:1 bicycle:2 bicycle:3 bicycle:4]

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Aggregation;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryAggExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTagField(new FieldName("$.condition", "condition"))
            .AddNumericField(new FieldName("$.price", "price"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[] {
            new
            {
                pickup_zone = "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))",
                store_location = "-74.0060,40.7128",
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))",
                store_location = "-118.2437,34.0522",
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\" wheel bike is just too clumsy coming off a 24\" bike. The Hillcraft 26 is just the solution they need!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))",
                store_location = "-87.6298,41.8781",
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))",
                store_location = "-80.1918,25.7617",
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))",
                store_location = "-122.4194,37.7749",
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women’s saddle, different bars and unique colourway.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))",
                store_location = "-0.1278,51.5074",
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s not to say that it’s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which doesn’t break the bank and delivers craved performance.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))",
                store_location = "2.3522,48.8566",
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It’s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))",
                store_location = "13.4050,52.5200",
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))",
                store_location = "2.1734, 41.3851",
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you’re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
                store_location = "12.4964,41.9028",
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.",
                condition = "refurbished"
            }
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        AggregationResult res1 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("@condition:{new}")
                .Load(new FieldName("__key"), new FieldName("price"))
                .Apply("@price - (@price * 0.1)", "discounted")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 5

        for (int i = 0; i < res1.TotalResults; i++)
        {
            Row res1Row = res1.GetRow(i);

            Console.WriteLine(
                $"Key: {res1Row["__key"]}, Price: {res1Row["price"]}, Discounted: {res1Row["discounted"]}"
            );
        }
        // >>> Key: bicycle:0, Price: 270, Discounted: 243
        // >>> Key: bicycle:5, Price: 810, Discounted: 729
        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
        // >>> Key: bicycle:7, Price: 430, Discounted: 387
        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080

        // Tests for 'agg1' step.

        AggregationResult res2 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Load(new FieldName("price"))
                .Apply("@price<1000", "price_category")
                .GroupBy(
                    "@condition",
                    Reducers.Sum("@price_category").As("num_affordable")
                )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        for (int i = 0; i < res2.TotalResults; i++)
        {
            Row res2Row = res2.GetRow(i);

            Console.WriteLine(
                $"Condition: {res2Row["condition"]}, Num affordable: {res2Row["num_affordable"]}"
            );
        }
        // >>> Condition: refurbished, Num affordable: 1
        // >>> Condition: used, Num affordable: 1
        // >>> Condition: new, Num affordable: 3

        // Tests for 'agg2' step.

        AggregationResult res3 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Apply("'bicycle'", "type")
                .GroupBy("@type", Reducers.Count().As("num_total"))
        );
        Console.WriteLine(res3.TotalResults);   // >>> 1

        Row res3Row = res3.GetRow(0);
        Console.WriteLine($"Type: {res3Row["type"]}, Num total: {res3Row["num_total"]}");
        // >>> Type: bicycle, Num total: 10

        // Tests for 'agg3' step.

        // Not supported in NRedisStack.

        // Tests for 'agg4' step.

    }
}

```

```
1) "3"
2) 1) "condition"
   1) "refurbished"
   2) "num_affordable"
   3) "1"
3) 1) "condition"
   1) "used"
   2) "num_affordable"
   3) "1"
4) 1) "condition"
   1) "new"
   2) "num_affordable"
   3) "3"
```

Note:

You can also create more complex aggregation pipelines with [FT.AGGREGATE](/docs/latest/commands/ft.aggregate/). Applying multiple reduction functions under one `GROUPBY` clause is possible. In addition, you can also chain groupings and mix in additional mapping steps (e.g., `GROUPBY ... REDUCE ... APPLY ... GROUPBY ... REDUCE`)

## Aggregating without grouping

You can't use an aggregation function outside of a `GROUPBY` clause, but you can construct your pipeline in a way that the aggregation happens on a single group that spans all documents. If your documents don't share a common attribute, you can add it via an extra `APPLY` step.

Here is an example that adds a type attribute `bicycle` to each document before counting all documents with that type:

```plaintext
FT.AGGREGATE idx:bicycle "*" APPLY "'bicycle'" AS type GROUPBY 1 @type REDUCE COUNT 0 AS num_total
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search import Search
from redis.commands.search.aggregation import AggregateRequest
from redis.commands.search.field import NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
import redis.commands.search.reducers as reducers

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
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

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='@condition:{new}') \
    .load('__key', 'price') \
    .apply(discounted='@price - (@price * 0.1)')
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 5
print(res.rows) # >>> [['__key', 'bicycle:0', ...
#[['__key', 'bicycle:0', 'price', '270', 'discounted', '243'],
# ['__key', 'bicycle:5', 'price', '810', 'discounted', '729'],
# ['__key', 'bicycle:6', 'price', '2300', 'discounted', '2070'],
# ['__key', 'bicycle:7', 'price', '430', 'discounted', '387'],
# ['__key', 'bicycle:8', 'price', '1200', 'discounted', '1080']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('price') \
    .apply(price_category='@price<1000') \
    .group_by('@condition', reducers.sum('@price_category').alias('num_affordable'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'num_affordable', '1'],
# ['condition', 'used', 'num_affordable', '1'],
# ['condition', 'new', 'num_affordable', '3']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .apply(type="'bicycle'") \
    .group_by('@type', reducers.count().alias('num_total'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 1
print(res.rows) # >>> [['type', 'bicycle', 'num_total', '10']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('__key') \
    .group_by('@condition', reducers.tolist('__key').alias('bicycles'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'bicycles', ['bicycle:9']],
# ['condition', 'used', 'bicycles', ['bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4']],
# ['condition', 'new', 'bicycles', ['bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8']]]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, FT_AGGREGATE_STEPS, FT_AGGREGATE_GROUP_BY_REDUCERS } from '@redis/search';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
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

const res1 = await client.ft.aggregate('idx:bicycle', '@condition:{new}', {
  LOAD: ['__key', 'price'],
  APPLY: {
    expression: '@price - (@price * 0.1)',
    AS: 'discounted'
  }
});

console.log(res1.results.length); // >>> 5
console.log(res1.results); // >>>
//[
//  [Object: null prototype] { __key: 'bicycle:0', price: '270' },
//  [Object: null prototype] { __key: 'bicycle:5', price: '810' },
//  [Object: null prototype] { __key: 'bicycle:6', price: '2300' },
//  [Object: null prototype] { __key: 'bicycle:7', price: '430' },
//  [Object: null prototype] { __key: 'bicycle:8', price: '1200' }
//]

const res2 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['@price'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: '@price<1000',
      AS: 'price_category'
    },{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE:[{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.SUM,
        property: '@price_category',
        AS: 'num_affordable'
      }]
    }]
});
console.log(res2.results.length); // >>> 3
console.log(res2.results); // >>>
//[[Object: null prototype] { condition: 'refurbished', num_affordable: '1' },
//  [Object: null prototype] { condition: 'used', num_affordable: '1' },
//  [Object: null prototype] { condition: 'new', num_affordable: '3' }
//]

const res3 = await client.ft.aggregate('idx:bicycle', '*', {
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: "'bicycle'",
      AS: 'type'
    }, {
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@type',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
        property: null,
        AS: 'num_total'
      }]
    }]
});
console.log(res3.results.length); // >>> 1
console.log(res3.results); // >>>
//[ [Object: null prototype] { type: 'bicycle', num_total: '10' } ]

const res4 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['__key'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.TOLIST,
        property: '__key',
        AS: 'bicycles'
      }]
    }]
});
console.log(res4.results.length); // >>> 3
console.log(res4.results); // >>>
//[[Object: null prototype] {condition: 'refurbished', bicycles: [ 'bicycle:9' ]},
//  [Object: null prototype] {condition: 'used', bicycles: [ 'bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4' ]},
//  [Object: null prototype] {condition: 'new', bicycles: [ 'bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8' ]}]

```

```java

import java.util.List;
import java.util.ArrayList;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class QueryAggExample {

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
            jedis.jsonSet("bicycle:" + i, new Path2("$"), bicycleJsons[i]);
        }

        AggregationResult res1 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("@condition:{new}")
                    .load("__key", "price")
                    .apply("@price - (@price * 0.1)", "discounted")
        );
        
        List<Row> rows1 = res1.getRows();
        System.out.println(rows1.size());   // >>> 5

        for (int i = 0; i < rows1.size(); i++) {
            System.out.println(rows1.get(i));
        }
        // >>> {__key=bicycle:0, discounted=243, price=270}
        // >>> {__key=bicycle:5, discounted=729, price=810}
        // >>> {__key=bicycle:6, discounted=2070, price=2300}
        // >>> {__key=bicycle:7, discounted=387, price=430}
        // >>> {__key=bicycle:8, discounted=1080, price=1200}

        // Tests for 'agg1' step.

        AggregationResult res2 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("price")
                    .apply("@price<1000", "price_category")
                    .groupBy("@condition",
                        Reducers.sum("@price_category").as("num_affordable"))
        );

        List<Row> rows2 = res2.getRows();
        System.out.println(rows2.size());   // >>> 3

        for (int i = 0; i < rows2.size(); i++) {
            System.out.println(rows2.get(i));
        }
        // >>> {condition=refurbished, num_affordable=1}
        // >>> {condition=used, num_affordable=1}
        // >>> {condition=new, num_affordable=3}

        // Tests for 'agg2' step.

        AggregationResult res3 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .apply("'bicycle'", "type")
                    .groupBy("@type", Reducers.count().as("num_total"))
        );

        List<Row> rows3 = res3.getRows();
        System.out.println(rows3.size());   // >>> 1

        for (int i = 0; i < rows3.size(); i++) {
            System.out.println(rows3.get(i));
        }
        // >>> {type=bicycle, num_total=10}

        // Tests for 'agg3' step.

        AggregationResult res4 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("__key")
                    .groupBy("@condition",
                        Reducers.to_list("__key").as("bicycles"))
        );

        List<Row> rows4 = res4.getRows();
        System.out.println(rows4.size());   // >>> 3

        for (int i = 0; i < rows4.size(); i++) {
            System.out.println(rows4.get(i));
        }
        // >>> {condition=refurbished, bicycles=[bicycle:9]}
        // >>> {condition=used, bicycles=[bicycle:3, bicycle:4, bicycle:1, bicycle:2]}
        // >>> {condition=new, bicycles=[bicycle:7, bicycle:0, bicycle:5, bicycle:6, bicycle:8]}

        // Tests for 'agg4' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            JsonParser parser = asyncCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<Void> setup = asyncCommands.ftCreate("idx:bicycle", createArgs, schema).thenCompose(result -> {
                CompletableFuture<Void> loadData = CompletableFuture.completedFuture(null);
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadData = loadData.thenCompose(v -> asyncCommands
                            .jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)).thenApply(res -> null));
                }
                return loadData;
            }).toCompletableFuture();
            setup.join();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            CompletableFuture<AggregationReply<String, String>> agg1 = asyncCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg2 = asyncCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg3 = asyncCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                        return result;
                    }).toCompletableFuture();

            // The `TOLIST` reducer is not currently available in Lettuce.

            // Wait for all aggregations to complete
            CompletableFuture.allOf(agg1, agg2, agg3).join();

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
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import reactor.core.publisher.Mono;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            JsonParser parser = reactiveCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<String> setup = reactiveCommands.ftCreate("idx:bicycle", createArgs, schema).flatMap(result -> {
                // load data sequentially using reactive chains
                Mono<String> loadChain = Mono.just("OK");
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadChain = loadChain.flatMap(
                            v -> reactiveCommands.jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)));
                }
                return loadChain;
            });

            setup.block();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            Mono<AggregationReply<String, String>> agg1 = reactiveCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                    });

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            Mono<AggregationReply<String, String>> agg2 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                    });

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            Mono<AggregationReply<String, String>> agg3 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                    });

            // The `TOLIST` reducer is not currently available in Lettuce.

            Mono.when(agg1, agg2, agg3).block();
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

func ExampleClient_query_agg() {
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

	res1, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle",
		"@condition:{new}",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price - (@price * 0.1)",
					As:    "discounted",
				},
			},
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
				{Field: "price"},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res1.Rows)) // >>> 5

	sort.Slice(res1.Rows, func(i, j int) bool {
		return res1.Rows[i].Fields["__key"].(string) <
			res1.Rows[j].Fields["__key"].(string)
	})

	for _, row := range res1.Rows {
		fmt.Printf(
			"__key=%v, discounted=%v, price=%v\n",
			row.Fields["__key"],
			row.Fields["discounted"],
			row.Fields["price"],
		)
	}
	// >>> __key=bicycle:0, discounted=243, price=270
	// >>> __key=bicycle:5, discounted=729, price=810
	// >>> __key=bicycle:6, discounted=2070, price=2300
	// >>> __key=bicycle:7, discounted=387, price=430
	// >>> __key=bicycle:8, discounted=1080, price=1200

	res2, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "price"},
			},
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price<1000",
					As:    "price_category",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchSum,
							Args:    []interface{}{"@price_category"},
							As:      "num_affordable",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res2.Rows)) // >>> 3

	sort.Slice(res2.Rows, func(i, j int) bool {
		return res2.Rows[i].Fields["condition"].(string) <
			res2.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res2.Rows {
		fmt.Printf(
			"condition=%v, num_affordable=%v\n",
			row.Fields["condition"],
			row.Fields["num_affordable"],
		)
	}
	// >>> condition=new, num_affordable=3
	// >>> condition=refurbished, num_affordable=1
	// >>> condition=used, num_affordable=1

	res3, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "'bicycle'",
					As:    "type",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@type"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchCount,
							As:      "num_total",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res3.Rows)) // >>> 1

	for _, row := range res3.Rows {
		fmt.Printf(
			"type=%v, num_total=%v\n",
			row.Fields["type"],
			row.Fields["num_total"],
		)
	}
	// type=bicycle, num_total=10

	res4, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchToList,
							Args:    []interface{}{"__key"},
							As:      "bicycles",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res4.Rows)) // >>> 3

	sort.Slice(res4.Rows, func(i, j int) bool {
		return res4.Rows[i].Fields["condition"].(string) <
			res4.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res4.Rows {
		rowBikes := row.Fields["bicycles"].([]interface{})
		bikes := make([]string, len(rowBikes))

		for i, rowBike := range rowBikes {
			bikes[i] = rowBike.(string)
		}

		sort.Slice(bikes, func(i, j int) bool {
			return bikes[i] < bikes[j]
		})

		fmt.Printf(
			"condition=%v, bicycles=%v\n",
			row.Fields["condition"],
			bikes,
		)
	}
	// >>> condition=new, bicycles=[bicycle:0 bicycle:5 bicycle:6 bicycle:7 bicycle:8]
	// >>> condition=refurbished, bicycles=[bicycle:9]
	// >>> condition=used, bicycles=[bicycle:1 bicycle:2 bicycle:3 bicycle:4]

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Aggregation;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryAggExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTagField(new FieldName("$.condition", "condition"))
            .AddNumericField(new FieldName("$.price", "price"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[] {
            new
            {
                pickup_zone = "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))",
                store_location = "-74.0060,40.7128",
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))",
                store_location = "-118.2437,34.0522",
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\" wheel bike is just too clumsy coming off a 24\" bike. The Hillcraft 26 is just the solution they need!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))",
                store_location = "-87.6298,41.8781",
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))",
                store_location = "-80.1918,25.7617",
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))",
                store_location = "-122.4194,37.7749",
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women’s saddle, different bars and unique colourway.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))",
                store_location = "-0.1278,51.5074",
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s not to say that it’s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which doesn’t break the bank and delivers craved performance.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))",
                store_location = "2.3522,48.8566",
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It’s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))",
                store_location = "13.4050,52.5200",
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))",
                store_location = "2.1734, 41.3851",
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you’re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
                store_location = "12.4964,41.9028",
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.",
                condition = "refurbished"
            }
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        AggregationResult res1 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("@condition:{new}")
                .Load(new FieldName("__key"), new FieldName("price"))
                .Apply("@price - (@price * 0.1)", "discounted")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 5

        for (int i = 0; i < res1.TotalResults; i++)
        {
            Row res1Row = res1.GetRow(i);

            Console.WriteLine(
                $"Key: {res1Row["__key"]}, Price: {res1Row["price"]}, Discounted: {res1Row["discounted"]}"
            );
        }
        // >>> Key: bicycle:0, Price: 270, Discounted: 243
        // >>> Key: bicycle:5, Price: 810, Discounted: 729
        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
        // >>> Key: bicycle:7, Price: 430, Discounted: 387
        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080

        // Tests for 'agg1' step.

        AggregationResult res2 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Load(new FieldName("price"))
                .Apply("@price<1000", "price_category")
                .GroupBy(
                    "@condition",
                    Reducers.Sum("@price_category").As("num_affordable")
                )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        for (int i = 0; i < res2.TotalResults; i++)
        {
            Row res2Row = res2.GetRow(i);

            Console.WriteLine(
                $"Condition: {res2Row["condition"]}, Num affordable: {res2Row["num_affordable"]}"
            );
        }
        // >>> Condition: refurbished, Num affordable: 1
        // >>> Condition: used, Num affordable: 1
        // >>> Condition: new, Num affordable: 3

        // Tests for 'agg2' step.

        AggregationResult res3 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Apply("'bicycle'", "type")
                .GroupBy("@type", Reducers.Count().As("num_total"))
        );
        Console.WriteLine(res3.TotalResults);   // >>> 1

        Row res3Row = res3.GetRow(0);
        Console.WriteLine($"Type: {res3Row["type"]}, Num total: {res3Row["num_total"]}");
        // >>> Type: bicycle, Num total: 10

        // Tests for 'agg3' step.

        // Not supported in NRedisStack.

        // Tests for 'agg4' step.

    }
}

```

The result is:

```
1) "1"
2) 1) "type"
   1) "bicycle"
   2) "num_total"
   3) "10"
```

## Grouping without aggregation

It's sometimes necessary to group your data without applying a mathematical aggregation function. If you need a grouped list of values, then the `TOLIST` function is helpful.

The following example shows how to group all bicycles by `condition`:

```plaintext
FT.AGGREGATE idx:bicycle "*" LOAD 1 "__key" GROUPBY 1 "@condition" REDUCE TOLIST 1 "__key" AS bicycles
```

```python
import json
import redis
from redis.commands.json.path import Path
from redis.commands.search import Search
from redis.commands.search.aggregation import AggregateRequest
from redis.commands.search.field import NumericField, TagField
from redis.commands.search.index_definition import IndexDefinition, IndexType
import redis.commands.search.reducers as reducers

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
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

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='@condition:{new}') \
    .load('__key', 'price') \
    .apply(discounted='@price - (@price * 0.1)')
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 5
print(res.rows) # >>> [['__key', 'bicycle:0', ...
#[['__key', 'bicycle:0', 'price', '270', 'discounted', '243'],
# ['__key', 'bicycle:5', 'price', '810', 'discounted', '729'],
# ['__key', 'bicycle:6', 'price', '2300', 'discounted', '2070'],
# ['__key', 'bicycle:7', 'price', '430', 'discounted', '387'],
# ['__key', 'bicycle:8', 'price', '1200', 'discounted', '1080']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('price') \
    .apply(price_category='@price<1000') \
    .group_by('@condition', reducers.sum('@price_category').alias('num_affordable'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'num_affordable', '1'],
# ['condition', 'used', 'num_affordable', '1'],
# ['condition', 'new', 'num_affordable', '3']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .apply(type="'bicycle'") \
    .group_by('@type', reducers.count().alias('num_total'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 1
print(res.rows) # >>> [['type', 'bicycle', 'num_total', '10']]

search = Search(r, index_name="idx:bicycle")
aggregate_request = AggregateRequest(query='*') \
    .load('__key') \
    .group_by('@condition', reducers.tolist('__key').alias('bicycles'))
res = search.aggregate(aggregate_request)
print(len(res.rows)) # >>> 3
print(res.rows) # >>>
#[['condition', 'refurbished', 'bicycles', ['bicycle:9']],
# ['condition', 'used', 'bicycles', ['bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4']],
# ['condition', 'new', 'bicycles', ['bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8']]]

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, FT_AGGREGATE_STEPS, FT_AGGREGATE_GROUP_BY_REDUCERS } from '@redis/search';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.condition': {
    type: SCHEMA_FIELD_TYPE.TAG,
    AS: 'condition'
  },
  '$.price': {
    type: SCHEMA_FIELD_TYPE.NUMERIC,
    AS: 'price'
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

const res1 = await client.ft.aggregate('idx:bicycle', '@condition:{new}', {
  LOAD: ['__key', 'price'],
  APPLY: {
    expression: '@price - (@price * 0.1)',
    AS: 'discounted'
  }
});

console.log(res1.results.length); // >>> 5
console.log(res1.results); // >>>
//[
//  [Object: null prototype] { __key: 'bicycle:0', price: '270' },
//  [Object: null prototype] { __key: 'bicycle:5', price: '810' },
//  [Object: null prototype] { __key: 'bicycle:6', price: '2300' },
//  [Object: null prototype] { __key: 'bicycle:7', price: '430' },
//  [Object: null prototype] { __key: 'bicycle:8', price: '1200' }
//]

const res2 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['@price'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: '@price<1000',
      AS: 'price_category'
    },{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE:[{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.SUM,
        property: '@price_category',
        AS: 'num_affordable'
      }]
    }]
});
console.log(res2.results.length); // >>> 3
console.log(res2.results); // >>>
//[[Object: null prototype] { condition: 'refurbished', num_affordable: '1' },
//  [Object: null prototype] { condition: 'used', num_affordable: '1' },
//  [Object: null prototype] { condition: 'new', num_affordable: '3' }
//]

const res3 = await client.ft.aggregate('idx:bicycle', '*', {
  STEPS: [{
      type: FT_AGGREGATE_STEPS.APPLY,
      expression: "'bicycle'",
      AS: 'type'
    }, {
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@type',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.COUNT,
        property: null,
        AS: 'num_total'
      }]
    }]
});
console.log(res3.results.length); // >>> 1
console.log(res3.results); // >>>
//[ [Object: null prototype] { type: 'bicycle', num_total: '10' } ]

const res4 = await client.ft.aggregate('idx:bicycle', '*', {
  LOAD: ['__key'],
  STEPS: [{
      type: FT_AGGREGATE_STEPS.GROUPBY,
      properties: '@condition',
      REDUCE: [{
        type: FT_AGGREGATE_GROUP_BY_REDUCERS.TOLIST,
        property: '__key',
        AS: 'bicycles'
      }]
    }]
});
console.log(res4.results.length); // >>> 3
console.log(res4.results); // >>>
//[[Object: null prototype] {condition: 'refurbished', bicycles: [ 'bicycle:9' ]},
//  [Object: null prototype] {condition: 'used', bicycles: [ 'bicycle:1', 'bicycle:2', 'bicycle:3', 'bicycle:4' ]},
//  [Object: null prototype] {condition: 'new', bicycles: [ 'bicycle:5', 'bicycle:6', 'bicycle:7', 'bicycle:0', 'bicycle:8' ]}]

```

```java

import java.util.List;
import java.util.ArrayList;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class QueryAggExample {

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
            jedis.jsonSet("bicycle:" + i, new Path2("$"), bicycleJsons[i]);
        }

        AggregationResult res1 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("@condition:{new}")
                    .load("__key", "price")
                    .apply("@price - (@price * 0.1)", "discounted")
        );
        
        List<Row> rows1 = res1.getRows();
        System.out.println(rows1.size());   // >>> 5

        for (int i = 0; i < rows1.size(); i++) {
            System.out.println(rows1.get(i));
        }
        // >>> {__key=bicycle:0, discounted=243, price=270}
        // >>> {__key=bicycle:5, discounted=729, price=810}
        // >>> {__key=bicycle:6, discounted=2070, price=2300}
        // >>> {__key=bicycle:7, discounted=387, price=430}
        // >>> {__key=bicycle:8, discounted=1080, price=1200}

        // Tests for 'agg1' step.

        AggregationResult res2 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("price")
                    .apply("@price<1000", "price_category")
                    .groupBy("@condition",
                        Reducers.sum("@price_category").as("num_affordable"))
        );

        List<Row> rows2 = res2.getRows();
        System.out.println(rows2.size());   // >>> 3

        for (int i = 0; i < rows2.size(); i++) {
            System.out.println(rows2.get(i));
        }
        // >>> {condition=refurbished, num_affordable=1}
        // >>> {condition=used, num_affordable=1}
        // >>> {condition=new, num_affordable=3}

        // Tests for 'agg2' step.

        AggregationResult res3 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .apply("'bicycle'", "type")
                    .groupBy("@type", Reducers.count().as("num_total"))
        );

        List<Row> rows3 = res3.getRows();
        System.out.println(rows3.size());   // >>> 1

        for (int i = 0; i < rows3.size(); i++) {
            System.out.println(rows3.get(i));
        }
        // >>> {type=bicycle, num_total=10}

        // Tests for 'agg3' step.

        AggregationResult res4 = jedis.ftAggregate("idx:bicycle",
            new AggregationBuilder("*")
                    .load("__key")
                    .groupBy("@condition",
                        Reducers.to_list("__key").as("bicycles"))
        );

        List<Row> rows4 = res4.getRows();
        System.out.println(rows4.size());   // >>> 3

        for (int i = 0; i < rows4.size(); i++) {
            System.out.println(rows4.get(i));
        }
        // >>> {condition=refurbished, bicycles=[bicycle:9]}
        // >>> {condition=used, bicycles=[bicycle:3, bicycle:4, bicycle:1, bicycle:2]}
        // >>> {condition=new, bicycles=[bicycle:7, bicycle:0, bicycle:5, bicycle:6, bicycle:8]}

        // Tests for 'agg4' step.

        jedis.close();
    }
}

```

```java
import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();
            JsonParser parser = asyncCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            CompletableFuture<Void> setup = asyncCommands.ftCreate("idx:bicycle", createArgs, schema).thenCompose(result -> {
                CompletableFuture<Void> loadData = CompletableFuture.completedFuture(null);
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadData = loadData.thenCompose(v -> asyncCommands
                            .jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)).thenApply(res -> null));
                }
                return loadData;
            }).toCompletableFuture();
            setup.join();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            CompletableFuture<AggregationReply<String, String>> agg1 = asyncCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg2 = asyncCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                        return result;
                    }).toCompletableFuture();

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            CompletableFuture<AggregationReply<String, String>> agg3 = asyncCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .thenApply(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                        return result;
                    }).toCompletableFuture();

            // The `TOLIST` reducer is not currently available in Lettuce.

            // Wait for all aggregations to complete
            CompletableFuture.allOf(agg1, agg2, agg3).join();

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
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.json.JsonPath;
import io.lettuce.core.json.JsonParser;
import io.lettuce.core.json.JsonObject;
import io.lettuce.core.search.arguments.AggregateArgs;
import io.lettuce.core.search.arguments.AggregateArgs.GroupBy;
import io.lettuce.core.search.arguments.AggregateArgs.Reducer;
import io.lettuce.core.search.AggregationReply;

import io.lettuce.core.search.arguments.CreateArgs;
import io.lettuce.core.search.arguments.FieldArgs;
import io.lettuce.core.search.arguments.NumericFieldArgs;
import io.lettuce.core.search.arguments.TagFieldArgs;

import java.util.Arrays;
import java.util.List;
import reactor.core.publisher.Mono;

public class QueryAggregationExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();
            JsonParser parser = reactiveCommands.getJsonParser();

            // create index
            List<FieldArgs<String>> schema = Arrays.asList(
                    TagFieldArgs.<String> builder().name("$.condition").as("condition").build(),
                    NumericFieldArgs.<String> builder().name("$.price").as("price").build());

            CreateArgs<String, String> createArgs = CreateArgs.<String, String> builder().withPrefix("bicycle:")
                    .on(CreateArgs.TargetType.JSON).build();

            // load data using JsonParser
            List<JsonObject> bicycleJsons = Arrays.asList(parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                    "\"POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))\""))
                    .put("store_location", parser.createJsonValue("\"-74.0060,40.7128\""))
                    .put("brand", parser.createJsonValue("\"Velorim\"")).put("model", parser.createJsonValue("\"Jigger\""))
                    .put("price", parser.createJsonValue("270"))
                    .put("description", parser
                            .createJsonValue("\"Small and powerful, the Jigger is the best ride for the smallest of tikes! "
                                    + "This is the tiniest kids' pedal bike on the market available without a coaster brake, the Jigger "
                                    + "is the vehicle of choice for the rare tenacious little rider raring to go.\""))
                    .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))\""))
                            .put("store_location", parser.createJsonValue("\"-118.2437,34.0522\""))
                            .put("brand", parser.createJsonValue("\"Bicyk\""))
                            .put("model", parser.createJsonValue("\"Hillcraft\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"Kids want to ride with as little weight as possible. Especially "
                                            + "on an incline! They may be at the age when a 27.5'' wheel bike is just too clumsy coming "
                                            + "off a 24'' bike. The Hillcraft 26 is just the solution they need!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))\""))
                            .put("store_location", parser.createJsonValue("\"-87.6298,41.8781\""))
                            .put("brand", parser.createJsonValue("\"Nord\""))
                            .put("model", parser.createJsonValue("\"Chook air 5\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"The Chook Air 5  gives kids aged six years and older a durable "
                                            + "and uberlight mountain bike for their first experience on tracks and easy cruising through "
                                            + "forests and fields. The lower  top tube makes it easy to mount and dismount in any "
                                            + "situation, giving your kids greater safety on the trails.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))\""))
                            .put("store_location", parser.createJsonValue("\"-80.1918,25.7617\""))
                            .put("brand", parser.createJsonValue("\"Eva\"")).put("model", parser.createJsonValue("\"Eva 291\""))
                            .put("price", parser.createJsonValue("3400"))
                            .put("description",
                                    parser.createJsonValue("\"The sister company to Nord, Eva launched in 2005 as the first "
                                            + "and only women-dedicated bicycle brand. Designed by women for women, allEva bikes "
                                            + "are optimized for the feminine physique using analytics from a body metrics database. "
                                            + "If you like 29ers, try the Eva 291. It's a brand new bike for 2022.. This "
                                            + "full-suspension, cross-country ride has been designed for velocity. The 291 has "
                                            + "100mm of front and rear travel, a superlight aluminum frame and fast-rolling "
                                            + "29-inch wheels. Yippee!\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))\""))
                            .put("store_location", parser.createJsonValue("\"-122.4194,37.7749\""))
                            .put("brand", parser.createJsonValue("\"Noka Bikes\""))
                            .put("model", parser.createJsonValue("\"Kahuna\"")).put("price", parser.createJsonValue("3200"))
                            .put("description",
                                    parser.createJsonValue("\"Whether you want to try your hand at XC racing or are looking "
                                            + "for a lively trail bike that's just as inspiring on the climbs as it is over rougher "
                                            + "ground, the Wilder is one heck of a bike built specifically for short women. Both the "
                                            + "frames and components have been tweaked to include a women's saddle, different bars "
                                            + "and unique colourway.\""))
                            .put("condition", parser.createJsonValue("\"used\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))\""))
                            .put("store_location", parser.createJsonValue("\"-0.1278,51.5074\""))
                            .put("brand", parser.createJsonValue("\"Breakout\""))
                            .put("model", parser.createJsonValue("\"XBN 2.1 Alloy\""))
                            .put("price", parser.createJsonValue("810"))
                            .put("description",
                                    parser.createJsonValue("\"The XBN 2.1 Alloy is our entry-level road bike – but that's "
                                            + "not to say that it's a basic machine. With an internal weld aluminium frame, a full "
                                            + "carbon fork, and the slick-shifting Claris gears from Shimano's, this is a bike which "
                                            + "doesn't break the bank and delivers craved performance.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))\""))
                            .put("store_location", parser.createJsonValue("\"2.3522,48.8566\""))
                            .put("brand", parser.createJsonValue("\"ScramBikes\""))
                            .put("model", parser.createJsonValue("\"WattBike\"")).put("price", parser.createJsonValue("2300"))
                            .put("description",
                                    parser.createJsonValue("\"The WattBike is the best e-bike for people who still "
                                            + "feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH "
                                            + "Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one "
                                            + "charge. It's great for tackling hilly terrain or if you just fancy a more "
                                            + "leisurely ride. With three working modes, you can choose between E-bike, "
                                            + "assisted bicycle, and normal bike modes.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))\""))
                            .put("store_location", parser.createJsonValue("\"13.4050,52.5200\""))
                            .put("brand", parser.createJsonValue("\"Peaknetic\""))
                            .put("model", parser.createJsonValue("\"Secto\"")).put("price", parser.createJsonValue("430"))
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
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))\""))
                            .put("store_location", parser.createJsonValue("\"2.1734, 41.3851\""))
                            .put("brand", parser.createJsonValue("\"nHill\""))
                            .put("model", parser.createJsonValue("\"Summit\"")).put("price", parser.createJsonValue("1200"))
                            .put("description",
                                    parser.createJsonValue("\"This budget mountain bike from nHill performs well both "
                                            + "on bike paths and on the trail. The fork with 100mm of travel absorbs rough "
                                            + "terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. "
                                            + "The Shimano Tourney drivetrain offered enough gears for finding a comfortable "
                                            + "pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. "
                                            + "Whether you want an affordable bike that you can take to work, but also take "
                                            + "trail in mountains on the weekends or you're just after a stable, comfortable "
                                            + "ride for the bike path, the Summit gives a good value for money.\""))
                            .put("condition", parser.createJsonValue("\"new\"")),
                    parser.createJsonObject().put("pickup_zone", parser.createJsonValue(
                            "\"POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))\""))
                            .put("store_location", parser.createJsonValue("\"12.4964,41.9028\""))
                            .put("brand", parser.createJsonValue("\"BikeShind\""))
                            .put("model", parser.createJsonValue("\"ThrillCycle\"")).put("price", parser.createJsonValue("815"))
                            .put("description",
                                    parser.createJsonValue("\"An artsy,  retro-inspired bicycle that's as "
                                            + "functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. "
                                            + "A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn't "
                                            + "suggest taking it to the mountains. Fenders protect you from mud, and a rear "
                                            + "basket lets you transport groceries, flowers and books. The ThrillCycle comes "
                                            + "with a limited lifetime warranty, so this little guy will last you long "
                                            + "past graduation.\""))
                            .put("condition", parser.createJsonValue("\"refurbished\"")));

            Mono<String> setup = reactiveCommands.ftCreate("idx:bicycle", createArgs, schema).flatMap(result -> {
                // load data sequentially using reactive chains
                Mono<String> loadChain = Mono.just("OK");
                for (int i = 0; i < bicycleJsons.size(); i++) {
                    final int index = i;
                    loadChain = loadChain.flatMap(
                            v -> reactiveCommands.jsonSet("bicycle:" + index, JsonPath.ROOT_PATH, bicycleJsons.get(index)));
                }
                return loadChain;
            });

            setup.block();

            AggregateArgs<String, String> agg1Args = AggregateArgs.<String, String> builder().load("__key").load("price")
                    .apply("@price - (@price * 0.1)", "discounted").build();

            Mono<AggregationReply<String, String>> agg1 = reactiveCommands
                    .ftAggregate("idx:bicycle", "@condition:{new}", agg1Args).doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("__key").compareTo(doc2.getFields().get("__key")))
                                .forEach(doc -> {
                                    System.out.printf("Key: %s, Price: %s, Discounted: %s\n", doc.getFields().get("__key"),
                                            doc.getFields().get("price"), doc.getFields().get("discounted"));
                                });
                        // >>> Key: bicycle:0, Price: 270, Discounted: 243
                        // >>> Key: bicycle:5, Price: 810, Discounted: 729
                        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
                        // >>> Key: bicycle:7, Price: 430, Discounted: 387
                        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080
                    });

            AggregateArgs<String, String> agg2Args = AggregateArgs.<String, String> builder().load("price")
                    .apply("@price<1000", "price_category").groupBy(GroupBy.<String, String> of("condition")
                            .reduce(Reducer.<String, String> sum("@price_category").as("num_affordable")))
                    .build();

            Mono<AggregationReply<String, String>> agg2 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg2Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream().sorted(
                                (doc1, doc2) -> doc1.getFields().get("condition").compareTo(doc2.getFields().get("condition")))
                                .forEach(doc -> {
                                    System.out.printf("Condition: %s, Num Affordable: %s\n", doc.getFields().get("condition"),
                                            doc.getFields().get("num_affordable"));
                                });
                        // >>> Condition: new, Num Affordable: 3
                        // >>> Condition: refurbished, Num Affordable: 1
                        // >>> Condition: used, Num Affordable: 1
                    });

            AggregateArgs<String, String> agg3Args = AggregateArgs.<String, String> builder().apply("'bicycle'", "type")
                    .groupBy(GroupBy.<String, String> of("type").reduce(Reducer.<String, String> count().as("num_total")))
                    .build();

            Mono<AggregationReply<String, String>> agg3 = reactiveCommands.ftAggregate("idx:bicycle", "*", agg3Args)
                    .doOnNext(result -> {
                        result.getReplies().get(0).getResults().stream()
                                .sorted((doc1, doc2) -> doc1.getFields().get("type").compareTo(doc2.getFields().get("type")))
                                .forEach(doc -> {
                                    System.out.printf("Type: %s, Total Count: %s\n", doc.getFields().get("type"),
                                            doc.getFields().get("num_total"));
                                });
                        // >>> Type: bicycle, Total Count: 10
                    });

            // The `TOLIST` reducer is not currently available in Lettuce.

            Mono.when(agg1, agg2, agg3).block();
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

func ExampleClient_query_agg() {
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

	res1, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle",
		"@condition:{new}",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price - (@price * 0.1)",
					As:    "discounted",
				},
			},
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
				{Field: "price"},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res1.Rows)) // >>> 5

	sort.Slice(res1.Rows, func(i, j int) bool {
		return res1.Rows[i].Fields["__key"].(string) <
			res1.Rows[j].Fields["__key"].(string)
	})

	for _, row := range res1.Rows {
		fmt.Printf(
			"__key=%v, discounted=%v, price=%v\n",
			row.Fields["__key"],
			row.Fields["discounted"],
			row.Fields["price"],
		)
	}
	// >>> __key=bicycle:0, discounted=243, price=270
	// >>> __key=bicycle:5, discounted=729, price=810
	// >>> __key=bicycle:6, discounted=2070, price=2300
	// >>> __key=bicycle:7, discounted=387, price=430
	// >>> __key=bicycle:8, discounted=1080, price=1200

	res2, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "price"},
			},
			Apply: []redis.FTAggregateApply{
				{
					Field: "@price<1000",
					As:    "price_category",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchSum,
							Args:    []interface{}{"@price_category"},
							As:      "num_affordable",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res2.Rows)) // >>> 3

	sort.Slice(res2.Rows, func(i, j int) bool {
		return res2.Rows[i].Fields["condition"].(string) <
			res2.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res2.Rows {
		fmt.Printf(
			"condition=%v, num_affordable=%v\n",
			row.Fields["condition"],
			row.Fields["num_affordable"],
		)
	}
	// >>> condition=new, num_affordable=3
	// >>> condition=refurbished, num_affordable=1
	// >>> condition=used, num_affordable=1

	res3, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Apply: []redis.FTAggregateApply{
				{
					Field: "'bicycle'",
					As:    "type",
				},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@type"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchCount,
							As:      "num_total",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res3.Rows)) // >>> 1

	for _, row := range res3.Rows {
		fmt.Printf(
			"type=%v, num_total=%v\n",
			row.Fields["type"],
			row.Fields["num_total"],
		)
	}
	// type=bicycle, num_total=10

	res4, err := rdb.FTAggregateWithArgs(ctx,
		"idx:bicycle", "*",
		&redis.FTAggregateOptions{
			Load: []redis.FTAggregateLoad{
				{Field: "__key"},
			},
			GroupBy: []redis.FTAggregateGroupBy{
				{
					Fields: []interface{}{"@condition"},
					Reduce: []redis.FTAggregateReducer{
						{
							Reducer: redis.SearchToList,
							Args:    []interface{}{"__key"},
							As:      "bicycles",
						},
					},
				},
			},
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(len(res4.Rows)) // >>> 3

	sort.Slice(res4.Rows, func(i, j int) bool {
		return res4.Rows[i].Fields["condition"].(string) <
			res4.Rows[j].Fields["condition"].(string)
	})

	for _, row := range res4.Rows {
		rowBikes := row.Fields["bicycles"].([]interface{})
		bikes := make([]string, len(rowBikes))

		for i, rowBike := range rowBikes {
			bikes[i] = rowBike.(string)
		}

		sort.Slice(bikes, func(i, j int) bool {
			return bikes[i] < bikes[j]
		})

		fmt.Printf(
			"condition=%v, bicycles=%v\n",
			row.Fields["condition"],
			bikes,
		)
	}
	// >>> condition=new, bicycles=[bicycle:0 bicycle:5 bicycle:6 bicycle:7 bicycle:8]
	// >>> condition=refurbished, bicycles=[bicycle:9]
	// >>> condition=used, bicycles=[bicycle:1 bicycle:2 bicycle:3 bicycle:4]

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Aggregation;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class QueryAggExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema bikeSchema = new Schema()
            .AddTagField(new FieldName("$.condition", "condition"))
            .AddNumericField(new FieldName("$.price", "price"));

        FTCreateParams bikeParams = new FTCreateParams()
            .AddPrefix("bicycle:")
            .On(IndexDataType.JSON);

        db.FT().Create("idx:bicycle", bikeParams, bikeSchema);

        var bicycles = new object[] {
            new
            {
                pickup_zone = "POLYGON((-74.0610 40.7578, -73.9510 40.7578, -73.9510 40.6678, -74.0610 40.6678, -74.0610 40.7578))",
                store_location = "-74.0060,40.7128",
                brand = "Velorim",
                model = "Jigger",
                price = 270,
                description = "Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((-118.2887 34.0972, -118.1987 34.0972, -118.1987 33.9872, -118.2887 33.9872, -118.2887 34.0972))",
                store_location = "-118.2437,34.0522",
                brand = "Bicyk",
                model = "Hillcraft",
                price = 1200,
                description = "Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\" wheel bike is just too clumsy coming off a 24\" bike. The Hillcraft 26 is just the solution they need!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-87.6848 41.9331, -87.5748 41.9331, -87.5748 41.8231, -87.6848 41.8231, -87.6848 41.9331))",
                store_location = "-87.6298,41.8781",
                brand = "Nord",
                model = "Chook air 5",
                price = 815,
                description = "The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-80.2433 25.8067, -80.1333 25.8067, -80.1333 25.6967, -80.2433 25.6967, -80.2433 25.8067))",
                store_location = "-80.1918,25.7617",
                brand = "Eva",
                model = "Eva 291",
                price = 3400,
                description = "The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It’s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-122.4644 37.8199, -122.3544 37.8199, -122.3544 37.7099, -122.4644 37.7099, -122.4644 37.8199))",
                store_location = "-122.4194,37.7749",
                brand = "Noka Bikes",
                model = "Kahuna",
                price = 3200,
                description = "Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women’s saddle, different bars and unique colourway.",
                condition = "used"
            },
            new
            {
                pickup_zone = "POLYGON((-0.1778 51.5524, 0.0822 51.5524, 0.0822 51.4024, -0.1778 51.4024, -0.1778 51.5524))",
                store_location = "-0.1278,51.5074",
                brand = "Breakout",
                model = "XBN 2.1 Alloy",
                price = 810,
                description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s not to say that it’s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which doesn’t break the bank and delivers craved performance.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((2.1767 48.9016, 2.5267 48.9016, 2.5267 48.5516, 2.1767 48.5516, 2.1767 48.9016))",
                store_location = "2.3522,48.8566",
                brand = "ScramBikes",
                model = "WattBike",
                price = 2300,
                description = "The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It’s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((13.3260 52.5700, 13.6550 52.5700, 13.6550 52.2700, 13.3260 52.2700, 13.3260 52.5700))",
                store_location = "13.4050,52.5200",
                brand = "Peaknetic",
                model = "Secto",
                price = 430,
                description = "If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((1.9450 41.4301, 2.4018 41.4301, 2.4018 41.1987, 1.9450 41.1987, 1.9450 41.4301))",
                store_location = "2.1734, 41.3851",
                brand = "nHill",
                model = "Summit",
                price = 1200,
                description = "This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you’re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.",
                condition = "new"
            },
            new
            {
                pickup_zone = "POLYGON((12.4464 42.1028, 12.5464 42.1028, 12.5464 41.7028, 12.4464 41.7028, 12.4464 42.1028))",
                store_location = "12.4964,41.9028",
                model = "ThrillCycle",
                brand = "BikeShind",
                price = 815,
                description = "An artsy,  retro-inspired bicycle that’s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn’t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.",
                condition = "refurbished"
            }
        };

        for (var i = 0; i < bicycles.Length; i++)
        {
            db.JSON().Set($"bicycle:{i}", "$", bicycles[i]);
        }

        AggregationResult res1 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("@condition:{new}")
                .Load(new FieldName("__key"), new FieldName("price"))
                .Apply("@price - (@price * 0.1)", "discounted")
        );
        Console.WriteLine(res1.TotalResults);   // >>> 5

        for (int i = 0; i < res1.TotalResults; i++)
        {
            Row res1Row = res1.GetRow(i);

            Console.WriteLine(
                $"Key: {res1Row["__key"]}, Price: {res1Row["price"]}, Discounted: {res1Row["discounted"]}"
            );
        }
        // >>> Key: bicycle:0, Price: 270, Discounted: 243
        // >>> Key: bicycle:5, Price: 810, Discounted: 729
        // >>> Key: bicycle:6, Price: 2300, Discounted: 2070
        // >>> Key: bicycle:7, Price: 430, Discounted: 387
        // >>> Key: bicycle:8, Price: 1200, Discounted: 1080

        // Tests for 'agg1' step.

        AggregationResult res2 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Load(new FieldName("price"))
                .Apply("@price<1000", "price_category")
                .GroupBy(
                    "@condition",
                    Reducers.Sum("@price_category").As("num_affordable")
                )
        );
        Console.WriteLine(res2.TotalResults);   // >>> 3

        for (int i = 0; i < res2.TotalResults; i++)
        {
            Row res2Row = res2.GetRow(i);

            Console.WriteLine(
                $"Condition: {res2Row["condition"]}, Num affordable: {res2Row["num_affordable"]}"
            );
        }
        // >>> Condition: refurbished, Num affordable: 1
        // >>> Condition: used, Num affordable: 1
        // >>> Condition: new, Num affordable: 3

        // Tests for 'agg2' step.

        AggregationResult res3 = db.FT().Aggregate(
            "idx:bicycle",
            new AggregationRequest("*")
                .Apply("'bicycle'", "type")
                .GroupBy("@type", Reducers.Count().As("num_total"))
        );
        Console.WriteLine(res3.TotalResults);   // >>> 1

        Row res3Row = res3.GetRow(0);
        Console.WriteLine($"Type: {res3Row["type"]}, Num total: {res3Row["num_total"]}");
        // >>> Type: bicycle, Num total: 10

        // Tests for 'agg3' step.

        // Not supported in NRedisStack.

        // Tests for 'agg4' step.

    }
}

```

The output of this query is:

```
1) "3"
2) 1) "condition"
   1) "refurbished"
   2) "bicycles"
   3) 1) "bicycle:9"
3) 1) "condition"
   1) "used"
   2) "bicycles"
   3) 1) "bicycle:1"
      1) "bicycle:2"
      2) "bicycle:3"
      3) "bicycle:4"
4) 1) "condition"
   1) "new"
   2) "bicycles"
   3) 1) "bicycle:0"
      1) "bicycle:5"
      2) "bicycle:6"
      3) "bicycle:8"
      4) "bicycle:7"
```

## On this page

