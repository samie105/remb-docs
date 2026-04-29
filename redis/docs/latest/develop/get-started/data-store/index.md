---
title: "Redis as an in-memory data structure store quick start guide"
source: "https://redis.io/docs/latest/develop/get-started/data-store/"
canonical_url: "https://redis.io/docs/latest/develop/get-started/data-store/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:40.599Z"
content_hash: "aac67aacbda765b65ef6133d77f017ba334a6635f8534d8251c6756fe7a9fbc2"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Quick starts","→","Quick starts","→\n      \n        Redis as an in-memory data structure store quick start guide","→","Redis as an in-memory data structure store quick start guide"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Quick starts","→","Quick starts","→\n      \n        Redis as an in-memory data structure store quick start guide","→","Redis as an in-memory data structure store quick start guide"]
nav_prev: {"path": "redis/docs/latest/develop/data-types/timeseries/use_cases/index.md", "title": "Use cases"}
nav_next: {"path": "redis/docs/latest/develop/get-started/document-database/index.md", "title": "Redis as a document database quick start guide"}
---

# Redis as an in-memory data structure store quick start guide

Understand how to use basic Redis data types

This quick start guide shows you how to:

1.  Get started with Redis
2.  Store data under a key in Redis
3.  Retrieve data with a key from Redis
4.  Scan the keyspace for keys that match a specific pattern

The examples in this article refer to a simple bicycle inventory.

## Setup

The easiest way to get started with Redis is to use Redis Cloud:

1.  Create a [free account](https://redis.com/try-free?utm_source=redisio&utm_medium=referral&utm_campaign=2023-09-try_free&utm_content=cu-redis_cloud_users).
    
    ![](../img/free-cloud-db.png)
2.  Follow the instructions to create a free database.
    

You can alternatively follow the [installation guides](../../../operate/oss_and_stack/install/install-stack/index.md) to install Redis on your local machine.

## Connect

The first step is to connect to Redis. You can find further details about the connection options in this documentation site's [Tools section](/docs/latest/develop/tools/). The following example shows how to connect to a Redis server that runs on localhost (`-h 127.0.0.1`) and listens on the default port (`-p 6379`):

```plaintext
> redis-cli -h 127.0.0.1 -p 6379
```

```python
"""
Code samples for document database quickstart pages:
    https://redis.io/docs/latest/develop/get-started/document-database/
"""

import redis
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
bicycle = {
    "brand": "Velorim",
    "model": "Jigger",
    "price": 270,
    "description": (
        "Small and powerful, the Jigger is the best ride "
        "for the smallest of tikes! This is the tiniest "
        "kids’ pedal bike on the market available without"
        " a coaster brake, the Jigger is the vehicle of "
        "choice for the rare tenacious little rider "
        "raring to go."
    ),
    "condition": "new",
}

bicycles = [
    bicycle,
    {
        "brand": "Bicyk",
        "model": "Hillcraft",
        "price": 1200,
        "description": (
            "Kids want to ride with as little weight as possible."
            " Especially on an incline! They may be at the age "
            'when a 27.5" wheel bike is just too clumsy coming '
            'off a 24" bike. The Hillcraft 26 is just the solution'
            " they need!"
        ),
        "condition": "used",
    },
    {
        "brand": "Nord",
        "model": "Chook air 5",
        "price": 815,
        "description": (
            "The Chook Air 5  gives kids aged six years and older "
            "a durable and uberlight mountain bike for their first"
            " experience on tracks and easy cruising through forests"
            " and fields. The lower  top tube makes it easy to mount"
            " and dismount in any situation, giving your kids greater"
            " safety on the trails."
        ),
        "condition": "used",
    },
    {
        "brand": "Eva",
        "model": "Eva 291",
        "price": 3400,
        "description": (
            "The sister company to Nord, Eva launched in 2005 as the"
            " first and only women-dedicated bicycle brand. Designed"
            " by women for women, allEva bikes are optimized for the"
            " feminine physique using analytics from a body metrics"
            " database. If you like 29ers, try the Eva 291. It’s a "
            "brand new bike for 2022.. This full-suspension, "
            "cross-country ride has been designed for velocity. The"
            " 291 has 100mm of front and rear travel, a superlight "
            "aluminum frame and fast-rolling 29-inch wheels. Yippee!"
        ),
        "condition": "used",
    },
    {
        "brand": "Noka Bikes",
        "model": "Kahuna",
        "price": 3200,
        "description": (
            "Whether you want to try your hand at XC racing or are "
            "looking for a lively trail bike that's just as inspiring"
            " on the climbs as it is over rougher ground, the Wilder"
            " is one heck of a bike built specifically for short women."
            " Both the frames and components have been tweaked to "
            "include a women’s saddle, different bars and unique "
            "colourway."
        ),
        "condition": "used",
    },
    {
        "brand": "Breakout",
        "model": "XBN 2.1 Alloy",
        "price": 810,
        "description": (
            "The XBN 2.1 Alloy is our entry-level road bike – but that’s"
            " not to say that it’s a basic machine. With an internal "
            "weld aluminium frame, a full carbon fork, and the slick-shifting"
            " Claris gears from Shimano’s, this is a bike which doesn’t"
            " break the bank and delivers craved performance."
        ),
        "condition": "new",
    },
    {
        "brand": "ScramBikes",
        "model": "WattBike",
        "price": 2300,
        "description": (
            "The WattBike is the best e-bike for people who still feel young"
            " at heart. It has a Bafang 1000W mid-drive system and a 48V"
            " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for"
            " more than 60 miles on one charge. It’s great for tackling hilly"
            " terrain or if you just fancy a more leisurely ride. With three"
            " working modes, you can choose between E-bike, assisted bicycle,"
            " and normal bike modes."
        ),
        "condition": "new",
    },
    {
        "brand": "Peaknetic",
        "model": "Secto",
        "price": 430,
        "description": (
            "If you struggle with stiff fingers or a kinked neck or back after"
            " a few minutes on the road, this lightweight, aluminum bike"
            " alleviates those issues and allows you to enjoy the ride. From"
            " the ergonomic grips to the lumbar-supporting seat position, the"
            " Roll Low-Entry offers incredible comfort. The rear-inclined seat"
            " tube facilitates stability by allowing you to put a foot on the"
            " ground to balance at a stop, and the low step-over frame makes it"
            " accessible for all ability and mobility levels. The saddle is"
            " very soft, with a wide back to support your hip joints and a"
            " cutout in the center to redistribute that pressure. Rim brakes"
            " deliver satisfactory braking control, and the wide tires provide"
            " a smooth, stable ride on paved roads and gravel. Rack and fender"
            " mounts facilitate setting up the Roll Low-Entry as your preferred"
            " commuter, and the BMX-like handlebar offers space for mounting a"
            " flashlight, bell, or phone holder."
        ),
        "condition": "new",
    },
    {
        "brand": "nHill",
        "model": "Summit",
        "price": 1200,
        "description": (
            "This budget mountain bike from nHill performs well both on bike"
            " paths and on the trail. The fork with 100mm of travel absorbs"
            " rough terrain. Fat Kenda Booster tires give you grip in corners"
            " and on wet trails. The Shimano Tourney drivetrain offered enough"
            " gears for finding a comfortable pace to ride uphill, and the"
            " Tektro hydraulic disc brakes break smoothly. Whether you want an"
            " affordable bike that you can take to work, but also take trail in"
            " mountains on the weekends or you’re just after a stable,"
            " comfortable ride for the bike path, the Summit gives a good value"
            " for money."
        ),
        "condition": "new",
    },
    {
        "model": "ThrillCycle",
        "brand": "BikeShind",
        "price": 815,
        "description": (
            "An artsy,  retro-inspired bicycle that’s as functional as it is"
            " pretty: The ThrillCycle steel frame offers a smooth ride. A"
            " 9-speed drivetrain has enough gears for coasting in the city, but"
            " we wouldn’t suggest taking it to the mountains. Fenders protect"
            " you from mud, and a rear basket lets you transport groceries,"
            " flowers and books. The ThrillCycle comes with a limited lifetime"
            " warranty, so this little guy will last you long past graduation."
        ),
        "condition": "refurbished",
    },
]

schema = (
    TextField("$.brand", as_name="brand"),
    TextField("$.model", as_name="model"),
    TextField("$.description", as_name="description"),
    NumericField("$.price", as_name="price"),
    TagField("$.condition", as_name="condition"),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)
for bid, bicycle in enumerate(bicycles):
    r.json().set(f"bicycle:{bid}", Path.root_path(), bicycle)

res = index.search(Query("*"))
print("Documents found:", res.total)
# >>> Documents found: 10

res = index.search(Query("@model:Jigger"))
print(res)
# >>> Result{1 total, docs: [
# Document {
#   'id': 'bicycle:0',
#   'payload': None,
#   'json': '{
#       "brand":"Velorim",
#       "model":"Jigger",
#       "price":270,
#       ...
#       "condition":"new"
#    }'
# }]}

res = index.search(Query("@model:Jigger").return_field("$.price", as_field="price"))
print(res)
# >>> [Document {'id': 'bicycle:0', 'payload': None, 'price': '270'}]

res = index.search(Query("basic @price:[500 1000]"))
print(res)
# >>> Result{1 total, docs: [
# Document {
#   'id': 'bicycle:5',
#   'payload': None,
#   'json': '{
#       "brand":"Breakout",
#       "model":"XBN 2.1 Alloy",
#       "price":810,
#       ...
#       "condition":"new"
#    }'
# }]}

res = index.search(Query('@brand:"Noka Bikes"'))
print(res)
# >>> Result{1 total, docs: [
# Document {
#   'id': 'bicycle:4',
#   'payload': None,
#   'json': '{
#       "brand":"Noka Bikes",
#       "model":"Kahuna",
#       "price":3200,
#       ...
#       "condition":"used"
#    }'
# }]}

res = index.search(
    Query("@description:%analitics%").dialect(  # Note the typo in the word "analytics"
        2
    )
)
print(res)
# >>> Result{1 total, docs: [
# Document {
#   'id': 'bicycle:3',
#   'payload': None,
#   'json': '{
#       "brand":"Eva",
#       "model":"Eva 291",
#       "price":3400,
#       "description":"...using analytics from a body metrics database...",
#       "condition":"used"
#    }'
# }]}

res = index.search(
    Query("@description:%%analitycs%%").dialect(  # Note 2 typos in the word "analytics"
        2
    )
)
print(res)
# >>> Result{1 total, docs: [
# Document {
#   'id': 'bicycle:3',
#   'payload': None,
#   'json': '{
#       "brand":"Eva",
#       "model":"Eva 291",
#       "price":3400,
#       "description":"...using analytics from a body metrics database...",
#       "condition":"used"
#    }'
# }]}

res = index.search(Query("@model:hill*"))
print(res)
# >>> Result{1 total, docs: [
# Document {
#   'id': 'bicycle:1',
#   'payload': None,
#   'json': '{
#       "brand":"Bicyk",
#       "model":"Hillcraft",
#       "price":1200,
#       ...
#       "condition":"used"
#    }'
# }]}

res = index.search(Query("@model:*bike"))
print(res)
# >>> Result{1 total, docs: [
# Document {
#   'id': 'bicycle:6',
#   'payload': None,
#   'json': '{
#       "brand":"ScramBikes",
#       "model":"WattBike",
#       "price":2300,
#       ...
#       "condition":"new"
#   }'
# }]}

res = index.search(Query("w'H?*craft'").dialect(2))
print(res.docs[0].json)
# >>> {
#   "brand":"Bicyk",
#   "model":"Hillcraft",
#   "price":1200,
#   ...
#   "condition":"used"
# }

res = index.search(Query("mountain").with_scores())
for sr in res.docs:
    print(f"{sr.id}: score={sr.score}")

res = index.search(Query("mountain").with_scores().scorer("BM25"))
for sr in res.docs:
    print(f"{sr.id}: score={sr.score}")

req = aggregations.AggregateRequest("*").group_by(
    "@condition", reducers.count().alias("count")
)
res = index.aggregate(req).rows
print(res)
# >>> [['condition', 'refurbished', 'count', '1'],
#      ['condition', 'used', 'count', '4'],
#      ['condition', 'new', 'count', '5']]
```

```node.js
import { createClient, SCHEMA_FIELD_TYPE } from 'redis';
const client = createClient();
client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

const bicycle1 = {
  brand: 'Velorim',
  model: 'Jigger',
  price: 270,
  description:
    'Small and powerful, the Jigger is the best ' +
    'ride for the smallest of tikes! This is the tiniest kids\u2019 ' +
    'pedal bike on the market available without a coaster brake, the ' +
    'Jigger is the vehicle of choice for the rare tenacious little' +
    'rider raring to go.',
  condition: 'new'
};
const bicycles = [
  bicycle1,
  {
    brand: 'Bicyk',
    model: 'Hillcraft',
    price: 1200,
    description: 'Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\" wheel bike is just too clumsy coming off a 24\" bike. The Hillcraft 26 is just the solution they need!',
    condition: 'used'
  },
  {
    brand: 'Nord',
    model: 'Chook air 5',
    price: 815,
    description: 'The Chook Air 5 gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.',
    condition: 'used'
  },
  {
    brand: 'Eva',
    model: 'Eva 291',
    price: 3400,
    description: 'The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It\u2019s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!',
    condition: 'used'
  },
  {
    brand: 'Noka Bikes',
    model: 'Kahuna',
    price: 3200,
    description: 'Whether you want to try your hand at XC racing or are looking for a lively trail bike that\'s just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women\u2019s saddle, different bars and unique colourway.',
    condition: 'used'
  },
  {
    brand: 'Breakout',
    model: 'XBN 2.1 Alloy',
    price: 810,
    description: 'The XBN 2.1 Alloy is our entry-level road bike \u2013 but that\u2019s not to say that it\u2019s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano\u2019s, this is a bike which doesn\u2019t break the bank and delivers craved performance.',
    condition: 'new'
  },
  {
    brand: 'ScramBikes',
    model: 'WattBike',
    price: 2300,
    description: 'The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It\u2019s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.',
    condition: 'new'
  },
  {
    brand: 'Peaknetic',
    model: 'Secto',
    price: 430,
    description: 'If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.',
    condition: 'new'
  },
  {
    brand: 'nHill',
    model: 'Summit',
    price: 1200,
    description: 'This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\u2019re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.',
    condition: 'new'
  },
  {
    model: 'ThrillCycle',
    brand: 'BikeShind',
    price: 815,
    description: 'An artsy, retro-inspired bicycle that\u2019s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn\u2019t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.',
    condition: 'refurbished'
  }
];
const schema = {
  '$.brand': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    SORTABLE: true,
    AS: 'brand'
  },
  '$.model': {
    type: SCHEMA_FIELD_TYPE.TEXT,
    AS: 'model'
  },
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
};

try {
  await client.ft.create('idx:bicycle', schema, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
  });
} catch (e) {
  if (e.message === 'Index already exists') {
    console.log('Index exists already, skipped creation.');
  } else {
    // Something went wrong, perhaps RediSearch isn't installed...
    console.error(e);
    process.exit(1);
  }
}

await Promise.all(
  bicycles.map((bicycle, i) => client.json.set(`bicycle:${i}`, '$', bicycle))
);

let result = await client.ft.search('idx:bicycle', '*', {
  LIMIT: {
    from: 0,
    size: 10
  }
});

console.log(JSON.stringify(result, null, 2));

/*
{
  "total": 10,
  "documents": ...
}
*/

result = await client.ft.search(
  'idx:bicycle',
  '@model:Jigger',
  {
    LIMIT: {
    from: 0,
    size: 10
  }
});

console.log(JSON.stringify(result, null, 2));
/*
{
  "total": 1,
  "documents": [{
    "id": "bicycle:0",
    "value": {
      "brand": "Velorim",
      "model": "Jigger",
      "price": 270,
      "description": "Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.",
      "condition": "new"
    }
  }]
}
 */

result = await client.ft.search(
  'idx:bicycle',
  '@brand:"Noka Bikes"',
  {
    LIMIT: {
      from: 0,
      size: 10
    }
  }
);

console.log(JSON.stringify(result, null, 2));

/*
{
  "total": 1,
  "documents": [{
    "id": "bicycle:4",
    "value": {
      "brand": "Noka Bikes",
      "model": "Kahuna",
      "price": 3200,
      "description": "Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women’s saddle, different bars and unique colourway.",
      "condition": "used"
    }
  }]
}
*/

```

```java
package io.redis.examples;

import java.math.BigDecimal;
import java.util.*;

import redis.clients.jedis.*;
import redis.clients.jedis.exceptions.*;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.aggr.*;
import redis.clients.jedis.search.schemafields.*;

class Bicycle {
  public String brand;
  public String model;
  public BigDecimal price;
  public String description;
  public String condition;

  public Bicycle(String brand, String model, BigDecimal price, String condition, String description) {
    this.brand = brand;
    this.model = model;
    this.price = price;
    this.condition = condition;
    this.description = description;
  }
}

public class SearchQuickstartExample {

  public void run() {
    RedisClient jedis = RedisClient.create("localhost", 6379);

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

    Bicycle[] bicycles = {
        new Bicycle(
            "Velorim",
            "Jigger",
            new BigDecimal(270),
            "new",
            "Small and powerful, the Jigger is the best ride " +
            "for the smallest of tikes! This is the tiniest " +
            "kids’ pedal bike on the market available without" +
            " a coaster brake, the Jigger is the vehicle of " +
            "choice for the rare tenacious little rider " +
            "raring to go."
        ),
        new Bicycle(
            "Bicyk",
            "Hillcraft",
            new BigDecimal(1200),
            "used",
            "Kids want to ride with as little weight as possible." +
            " Especially on an incline! They may be at the age " +
            "when a 27.5 inch wheel bike is just too clumsy coming " +
            "off a 24 inch bike. The Hillcraft 26 is just the solution" +
            " they need!"
        ),
        new Bicycle(
            "Nord",
            "Chook air 5",
            new BigDecimal(815),
            "used",
            "The Chook Air 5  gives kids aged six years and older " +
            "a durable and uberlight mountain bike for their first" +
            " experience on tracks and easy cruising through forests" +
            " and fields. The lower  top tube makes it easy to mount" +
            " and dismount in any situation, giving your kids greater" +
            " safety on the trails."
        ),
        new Bicycle(
            "Eva",
            "Eva 291",
            new BigDecimal(3400),
            "used",
            "The sister company to Nord, Eva launched in 2005 as the" +
            " first and only women-dedicated bicycle brand. Designed" +
            " by women for women, allEva bikes are optimized for the" +
            " feminine physique using analytics from a body metrics" +
            " database. If you like 29ers, try the Eva 291. It's a " +
            "brand new bike for 2022.. This full-suspension, " +
            "cross-country ride has been designed for velocity. The" +
            " 291 has 100mm of front and rear travel, a superlight " +
            "aluminum frame and fast-rolling 29-inch wheels. Yippee!"
        ),
        new Bicycle(
            "Noka Bikes",
            "Kahuna",
            new BigDecimal(3200),
            "used",
            "Whether you want to try your hand at XC racing or are " +
            "looking for a lively trail bike that's just as inspiring" +
            " on the climbs as it is over rougher ground, the Wilder" +
            " is one heck of a bike built specifically for short women." +
            " Both the frames and components have been tweaked to " +
            "include a women’s saddle, different bars and unique " +
            "colourway."
        ),
        new Bicycle(
            "Breakout",
            "XBN 2.1 Alloy",
            new BigDecimal(810),
            "new",
            "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
            " not to say that it’s a basic machine. With an internal " +
            "weld aluminium frame, a full carbon fork, and the slick-shifting" +
            " Claris gears from Shimano’s, this is a bike which doesn’t" +
            " break the bank and delivers craved performance."
        ),
        new Bicycle(
            "ScramBikes",
            "WattBike",
            new BigDecimal(2300),
            "new",
            "The WattBike is the best e-bike for people who still feel young" +
            " at heart. It has a Bafang 1000W mid-drive system and a 48V" +
            " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
            " more than 60 miles on one charge. It’s great for tackling hilly" +
            " terrain or if you just fancy a more leisurely ride. With three" +
            " working modes, you can choose between E-bike, assisted bicycle," +
            " and normal bike modes."
        ),
        new Bicycle(
            "Peaknetic",
            "Secto",
            new BigDecimal(430),
            "new",
            "If you struggle with stiff fingers or a kinked neck or back after" +
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
            " flashlight, bell, or phone holder."
        ),
        new Bicycle(
            "nHill",
            "Summit",
            new BigDecimal(1200),
            "new",
            "This budget mountain bike from nHill performs well both on bike" +
            " paths and on the trail. The fork with 100mm of travel absorbs" +
            " rough terrain. Fat Kenda Booster tires give you grip in corners" +
            " and on wet trails. The Shimano Tourney drivetrain offered enough" +
            " gears for finding a comfortable pace to ride uphill, and the" +
            " Tektro hydraulic disc brakes break smoothly. Whether you want an" +
            " affordable bike that you can take to work, but also take trail in" +
            " mountains on the weekends or you’re just after a stable," +
            " comfortable ride for the bike path, the Summit gives a good value" +
            " for money."
        ),
        new Bicycle(
            "ThrillCycle",
            "BikeShind",
            new BigDecimal(815),
            "refurbished",
            "An artsy,  retro-inspired bicycle that’s as functional as it is" +
            " pretty: The ThrillCycle steel frame offers a smooth ride. A" +
            " 9-speed drivetrain has enough gears for coasting in the city, but" +
            " we wouldn’t suggest taking it to the mountains. Fenders protect" +
            " you from mud, and a rear basket lets you transport groceries," +
            " flowers and books. The ThrillCycle comes with a limited lifetime" +
            " warranty, so this little guy will last you long past graduation."
        ),
    };

    for (int i = 0; i < bicycles.length; i++) {
      jedis.jsonSetWithEscape(String.format("bicycle:%d", i), bicycles[i]);
    }

    Query query1 = new Query("*");
    List<Document> result1 = jedis.ftSearch("idx:bicycle", query1).getDocuments();
    System.out.println("Documents found:" + result1.size());
    // Prints: Documents found: 10

    Query query2 = new Query("@model:Jigger");
    List<Document> result2 = jedis.ftSearch("idx:bicycle", query2).getDocuments();
    System.out.println(result2);
    // Prints: [id:bicycle:0, score: 1.0, payload:null,
    // properties:[$={"brand":"Velorim","model":"Jigger","price":270,"description":"Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids’ pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.","condition":"new"}]]

    Query query3 = new Query("@model:Jigger").returnFields("price");
    List<Document> result3 = jedis.ftSearch("idx:bicycle", query3).getDocuments();
    System.out.println(result3);
    // Prints: [id:bicycle:0, score: 1.0, payload:null, properties:[price=270]]

    Query query4 = new Query("basic @price:[500 1000]");
    List<Document> result4 = jedis.ftSearch("idx:bicycle", query4).getDocuments();
    System.out.println(result4);
    // Prints: [id:bicycle:5, score: 1.0, payload:null,
    // properties:[$={"brand":"Breakout","model":"XBN 2.1 Alloy","price":810,"description":"The XBN 2.1 Alloy is our entry-level road bike – but that’s not to say that it’s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano’s, this is a bike which doesn’t break the bank and delivers craved performance.","condition":"new"}]]

    Query query5 = new Query("@brand:\"Noka Bikes\"");
    List<Document> result5 = jedis.ftSearch("idx:bicycle", query5).getDocuments();
    System.out.println(result5);
    // Prints: [id:bicycle:4, score: 1.0, payload:null,
    // properties:[$={"brand":"Noka Bikes","model":"Kahuna","price":3200,"description":"Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women’s saddle, different bars and unique colourway.","condition":"used"}]]

    AggregationBuilder ab = new AggregationBuilder("*").groupBy("@condition",
      Reducers.count().as("count"));
    AggregationResult ar = jedis.ftAggregate("idx:bicycle", ab);
    for (int i = 0; i < ar.getTotalResults(); i++) {
      System.out.println(ar.getRow(i).getString("condition") + " - "
          + ar.getRow(i).getString("count"));
    }
    // Prints:
    // refurbished - 1
    // used - 5
    // new - 4
    assertEquals(3, ar.getTotalResults(), "Validate aggregation results");

    jedis.close();
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

var bicycles = []interface{}{
	map[string]interface{}{
		"brand": "Velorim",
		"model": "Jigger",
		"price": 270,
		"description": "Small and powerful, the Jigger is the best ride " +
			"for the smallest of tikes! This is the tiniest " +
			"kids’ pedal bike on the market available without" +
			" a coaster brake, the Jigger is the vehicle of " +
			"choice for the rare tenacious little rider " +
			"raring to go.",
		"condition": "new",
	},
	map[string]interface{}{
		"brand": "Bicyk",
		"model": "Hillcraft",
		"price": 1200,
		"description": "Kids want to ride with as little weight as possible." +
			" Especially on an incline! They may be at the age " +
			"when a 27.5\" wheel bike is just too clumsy coming " +
			"off a 24\" bike. The Hillcraft 26 is just the solution" +
			" they need!",
		"condition": "used",
	},
	map[string]interface{}{
		"brand": "Nord",
		"model": "Chook air 5",
		"price": 815,
		"description": "The Chook Air 5  gives kids aged six years and older " +
			"a durable and uberlight mountain bike for their first" +
			" experience on tracks and easy cruising through forests" +
			" and fields. The lower  top tube makes it easy to mount" +
			" and dismount in any situation, giving your kids greater" +
			" safety on the trails.",
		"condition": "used",
	},
	map[string]interface{}{
		"brand": "Eva",
		"model": "Eva 291",
		"price": 3400,
		"description": "The sister company to Nord, Eva launched in 2005 as the" +
			" first and only women-dedicated bicycle brand. Designed" +
			" by women for women, allEva bikes are optimized for the" +
			" feminine physique using analytics from a body metrics" +
			" database. If you like 29ers, try the Eva 291. It’s a " +
			"brand new bike for 2022.. This full-suspension, " +
			"cross-country ride has been designed for velocity. The" +
			" 291 has 100mm of front and rear travel, a superlight " +
			"aluminum frame and fast-rolling 29-inch wheels. Yippee!",
		"condition": "used",
	},
	map[string]interface{}{
		"brand": "Noka Bikes",
		"model": "Kahuna",
		"price": 3200,
		"description": "Whether you want to try your hand at XC racing or are " +
			"looking for a lively trail bike that's just as inspiring" +
			" on the climbs as it is over rougher ground, the Wilder" +
			" is one heck of a bike built specifically for short women." +
			" Both the frames and components have been tweaked to " +
			"include a women’s saddle, different bars and unique " +
			"colourway.",
		"condition": "used",
	},
	map[string]interface{}{
		"brand": "Breakout",
		"model": "XBN 2.1 Alloy",
		"price": 810,
		"description": "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
			" not to say that it’s a basic machine. With an internal " +
			"weld aluminium frame, a full carbon fork, and the slick-shifting" +
			" Claris gears from Shimano’s, this is a bike which doesn’t" +
			" break the bank and delivers craved performance.",
		"condition": "new",
	},
	map[string]interface{}{
		"brand": "ScramBikes",
		"model": "WattBike",
		"price": 2300,
		"description": "The WattBike is the best e-bike for people who still feel young" +
			" at heart. It has a Bafang 1000W mid-drive system and a 48V" +
			" 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
			" more than 60 miles on one charge. It’s great for tackling hilly" +
			" terrain or if you just fancy a more leisurely ride. With three" +
			" working modes, you can choose between E-bike, assisted bicycle," +
			" and normal bike modes.",
		"condition": "new",
	},
	map[string]interface{}{
		"brand": "Peaknetic",
		"model": "Secto",
		"price": 430,
		"description": "If you struggle with stiff fingers or a kinked neck or back after" +
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
		"condition": "new",
	},
	map[string]interface{}{
		"brand": "nHill",
		"model": "Summit",
		"price": 1200,
		"description": "This budget mountain bike from nHill performs well both on bike" +
			" paths and on the trail. The fork with 100mm of travel absorbs" +
			" rough terrain. Fat Kenda Booster tires give you grip in corners" +
			" and on wet trails. The Shimano Tourney drivetrain offered enough" +
			" gears for finding a comfortable pace to ride uphill, and the" +
			" Tektro hydraulic disc brakes break smoothly. Whether you want an" +
			" affordable bike that you can take to work, but also take trail in" +
			" mountains on the weekends or you’re just after a stable," +
			" comfortable ride for the bike path, the Summit gives a good value" +
			" for money.",
		"condition": "new",
	},
	map[string]interface{}{
		"model": "ThrillCycle",
		"brand": "BikeShind",
		"price": 815,
		"description": "An artsy,  retro-inspired bicycle that’s as functional as it is" +
			" pretty: The ThrillCycle steel frame offers a smooth ride. A" +
			" 9-speed drivetrain has enough gears for coasting in the city, but" +
			" we wouldn’t suggest taking it to the mountains. Fenders protect" +
			" you from mud, and a rear basket lets you transport groceries," +
			" flowers and books. The ThrillCycle comes with a limited lifetime" +
			" warranty, so this little guy will last you long past graduation.",
		"condition": "refurbished",
	},
}

func ExampleClient_search_qs() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	schema := []*redis.FieldSchema{
		{
			FieldName: "$.brand",
			As:        "brand",
			FieldType: redis.SearchFieldTypeText,
		},
		{
			FieldName: "$.model",
			As:        "model",
			FieldType: redis.SearchFieldTypeText,
		},
		{
			FieldName: "$.description",
			As:        "description",
			FieldType: redis.SearchFieldTypeText,
		},
	}

	_, err := rdb.FTCreate(ctx, "idx:bicycle",
		&redis.FTCreateOptions{
			Prefix: []interface{}{"bicycle:"},
			OnJSON: true,
		},
		schema...,
	).Result()

	if err != nil {
		panic(err)
	}

	for i, bicycle := range bicycles {
		_, err := rdb.JSONSet(
			ctx,
			fmt.Sprintf("bicycle:%v", i),
			"$",
			bicycle,
		).Result()

		if err != nil {
			panic(err)
		}
	}

	wCardResult, err := rdb.FTSearch(ctx, "idx:bicycle", "*").Result()

	if err != nil {
		panic(err)
	}

	fmt.Printf("Documents found: %v\n", wCardResult.Total)
	// >>> Documents found: 10

	stResult, err := rdb.FTSearch(
		ctx,
		"idx:bicycle",
		"@model:Jigger",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(stResult)
	// >>> {1 [{bicycle:0 <nil> <nil> <nil> map[$:{"brand":"Velorim", ...

	exactMatchResult, err := rdb.FTSearch(
		ctx,
		"idx:bicycle",
		"@brand:\"Noka Bikes\"",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(exactMatchResult)
	// >>> {1 [{bicycle:4 <nil> <nil> <nil> map[$:{"brand":"Noka Bikes"...

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Aggregation;
using NRedisStack.Search.Literals.Enums;
using NRedisStack.Tests;
using StackExchange.Redis;

public class SearchQuickstartExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();
        var ft = db.FT();
        var json = db.JSON();

        var bike1 = new
        {
            Brand = "Velorim",
            Model = "Jigger",
            Price = 270M,
            Description = "Small and powerful, the Jigger is the best ride " +
                            "for the smallest of tikes! This is the tiniest " +
                            "kids’ pedal bike on the market available without" +
                            " a coaster brake, the Jigger is the vehicle of " +
                            "choice for the rare tenacious little rider " +
                            "raring to go.",
            Condition = "used"
        };

        var bicycles = new object[]
            {
                bike1,
                new
                {
                    Brand = "Bicyk",
                    Model = "Hillcraft",
                    Price = 1200M,
                    Description = "Kids want to ride with as little weight as possible." +
                        " Especially on an incline! They may be at the age " +
                        "when a 27.5 inch wheel bike is just too clumsy coming " +
                        "off a 24 inch bike. The Hillcraft 26 is just the solution" +
                        " they need!",
                    Condition = "used",
                },
                new
                {
                    Brand = "Nord",
                    Model = "Chook air 5",
                    Price = 815M,
                    Description = "The Chook Air 5  gives kids aged six years and older " +
                        "a durable and uberlight mountain bike for their first" +
                        " experience on tracks and easy cruising through forests" +
                        " and fields. The lower  top tube makes it easy to mount" +
                        " and dismount in any situation, giving your kids greater" +
                        " safety on the trails.",
                    Condition = "used",
                },
                new
                {
                    Brand = "Eva",
                    Model = "Eva 291",
                    Price = 3400M,
                    Description = "The sister company to Nord, Eva launched in 2005 as the" +
                        " first and only women-dedicated bicycle brand. Designed" +
                        " by women for women, allEva bikes are optimized for the" +
                        " feminine physique using analytics from a body metrics" +
                        " database. If you like 29ers, try the Eva 291. It’s a " +
                        "brand new bike for 2022.. This full-suspension, " +
                        "cross-country ride has been designed for velocity. The" +
                        " 291 has 100mm of front and rear travel, a superlight " +
                        "aluminum frame and fast-rolling 29-inch wheels. Yippee!",
                    Condition = "used",
                },
                new
                {
                    Brand = "Noka Bikes",
                    Model = "Kahuna",
                    Price = 3200M,
                    Description = "Whether you want to try your hand at XC racing or are " +
                        "looking for a lively trail bike that's just as inspiring" +
                        " on the climbs as it is over rougher ground, the Wilder" +
                        " is one heck of a bike built specifically for short women." +
                        " Both the frames and components have been tweaked to " +
                        "include a women’s saddle, different bars and unique " +
                        "colourway.",
                    Condition = "used",
                },
                new
                {
                    Brand = "Breakout",
                    Model = "XBN 2.1 Alloy",
                    Price = 810M,
                    Description = "The XBN 2.1 Alloy is our entry-level road bike – but that’s" +
                        " not to say that it’s a basic machine. With an internal " +
                        "weld aluminium frame, a full carbon fork, and the slick-shifting" +
                        " Claris gears from Shimano’s, this is a bike which doesn’t" +
                        " break the bank and delivers craved performance.",
                    Condition = "new",
                },
                new
                {
                    Brand = "ScramBikes",
                    Model = "WattBike",
                    Price = 2300M,
                    Description = "The WattBike is the best e-bike for people who still feel young" +
                        " at heart. It has a Bafang 1000W mid-drive system and a 48V" +
                        " 17.5AH Samsung Lithium-Ion battery, allowing you to ride for" +
                        " more than 60 miles on one charge. It’s great for tackling hilly" +
                        " terrain or if you just fancy a more leisurely ride. With three" +
                        " working modes, you can choose between E-bike, assisted bicycle," +
                        " and normal bike modes.",
                    Condition = "new",
                },
                new
                {
                    Brand = "Peaknetic",
                    Model = "Secto",
                    Price = 430M,
                    Description = "If you struggle with stiff fingers or a kinked neck or back after" +
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
                    Condition = "new",
                },
                new
                {
                    Brand = "nHill",
                    Model = "Summit",
                    Price = 1200M,
                    Description = "This budget mountain bike from nHill performs well both on bike" +
                        " paths and on the trail. The fork with 100mm of travel absorbs" +
                        " rough terrain. Fat Kenda Booster tires give you grip in corners" +
                        " and on wet trails. The Shimano Tourney drivetrain offered enough" +
                        " gears for finding a comfortable pace to ride uphill, and the" +
                        " Tektro hydraulic disc brakes break smoothly. Whether you want an" +
                        " affordable bike that you can take to work, but also take trail in" +
                        " mountains on the weekends or you’re just after a stable," +
                        " comfortable ride for the bike path, the Summit gives a good value" +
                        " for money.",
                    Condition = "new",
                },
                new
                {
                    Model = "ThrillCycle",
                    Brand = "BikeShind",
                    Price = 815M,
                    Description = "An artsy,  retro-inspired bicycle that’s as functional as it is" +
                        " pretty: The ThrillCycle steel frame offers a smooth ride. A" +
                        " 9-speed drivetrain has enough gears for coasting in the city, but" +
                        " we wouldn’t suggest taking it to the mountains. Fenders protect" +
                        " you from mud, and a rear basket lets you transport groceries," +
                        " flowers and books. The ThrillCycle comes with a limited lifetime" +
                        " warranty, so this little guy will last you long past graduation.",
                    Condition = "refurbished",
                },
            };

        var schema = new Schema()
            .AddTextField(new FieldName("$.Brand", "Brand"))
            .AddTextField(new FieldName("$.Model", "Model"))
            .AddTextField(new FieldName("$.Description", "Description"))
            .AddNumericField(new FieldName("$.Price", "Price"))
            .AddTagField(new FieldName("$.Condition", "Condition"));

        ft.Create(
            "idx:bicycle",
            new FTCreateParams().On(IndexDataType.JSON).Prefix("bicycle:"),
            schema);

        for (int i = 0; i < bicycles.Length; i++)
        {
            json.Set($"bicycle:{i}", "$", bicycles[i]);
        }

        var query1 = new Query("*");
        var res1 = ft.Search("idx:bicycle", query1).Documents;
        Console.WriteLine(string.Join("\n", res1.Count()));
        // Prints: Documents found: 10

        var query2 = new Query("@Model:Jigger");
        var res2 = ft.Search("idx:bicycle", query2).Documents;
        Console.WriteLine(string.Join("\n", res2.Select(x => x["json"])));
        // Prints: {"Brand":"Moore PLC","Model":"Award Race","Price":3790.76,
        //          "Description":"This olive folding bike features a carbon frame
        //          and 27.5 inch wheels. This folding bike is perfect for compact
        //          storage and transportation.","Condition":"new"}

        var query3 = new Query("basic @Price:[500 1000]");
        var res3 = ft.Search("idx:bicycle", query3).Documents;
        Console.WriteLine(string.Join("\n", res3.Select(x => x["json"])));
        // Prints: {"Brand":"Moore PLC","Model":"Award Race","Price":3790.76,
        //          "Description":"This olive folding bike features a carbon frame
        //          and 27.5 inch wheels. This folding bike is perfect for compact
        //          storage and transportation.","Condition":"new"}

        var query4 = new Query("@Brand:\"Noka Bikes\"");
        var res4 = ft.Search("idx:bicycle", query4).Documents;
        Console.WriteLine(string.Join("\n", res4.Select(x => x["json"])));
        // Prints: {"Brand":"Moore PLC","Model":"Award Race","Price":3790.76,
        //          "Description":"This olive folding bike features a carbon frame
        //          and 27.5 inch wheels. This folding bike is perfect for compact
        //          storage and transportation.","Condition":"new"}

        var query5 = new Query("@Model:Jigger").ReturnFields("Price");
        var res5 = ft.Search("idx:bicycle", query5).Documents;
        Console.WriteLine(res5.First()["Price"]);
        // Prints: 270

        var request = new AggregationRequest("*").GroupBy(
            "@Condition", Reducers.Count().As("Count"));
        var result = ft.Aggregate("idx:bicycle", request);

        for (var i = 0; i < result.TotalResults; i++)
        {
            var row = result.GetRow(i);
            Console.WriteLine($"{row["Condition"]} - {row["Count"]}");
        }

        // Prints:
        // refurbished - 1
        // used - 5
        // new - 4
    }
}
```

  

Tip:

You can copy and paste the connection details from the Redis Cloud database configuration page. Here is an example connection string of a Cloud database that is hosted in the AWS region `us-east-1` and listens on port 16379: `redis-16379.c283.us-east-1-4.ec2.cloud.redislabs.com:16379`. The connection string has the format `host:port`. You must also copy and paste the username and password of your Cloud database and then either pass the credentials to your client or use the [AUTH command](/docs/latest/commands/auth/) after the connection is established.

## Store and retrieve data

Redis stands for Remote Dictionary Server. You can use the same data types as in your local programming environment but on the server side within Redis.

Similar to byte arrays, Redis strings store sequences of bytes, including text, serialized objects, counter values, and binary arrays. The following example shows you how to set and get a string value:

```plaintext
SET bike:1 "Process 134"
GET bike:1
```

```python
"""
Code samples for data structure store quickstart pages:
    https://redis.io/docs/latest/develop/get-started/data-store/
"""

import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

res = r.set("bike:1", "Process 134")
print(res)
# >>> True

res = r.get("bike:1")
print(res)
# >>> "Process 134"
```

```node.js

import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis Client Error', err));

await client.connect().catch(console.error);

await client.set('bike:1', 'Process 134');
const value = await client.get('bike:1');
console.log(value);
// returns 'Process 134'

await client.close();
```

```java
package io.redis.examples;

import redis.clients.jedis.RedisClient;

public class SetGetExample {

  public void run() {

    RedisClient jedis = RedisClient.create("redis://localhost:6379");

    String status = jedis.set("bike:1", "Process 134");

    if ("OK".equals(status)) System.out.println("Successfully added a bike.");

    String value = jedis.get("bike:1");

    if (value != null) System.out.println("The name of the bike is: " + value + ".");

    jedis.close();
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

func ExampleClient_Set_and_get() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
	})

	err := rdb.Set(ctx, "bike:1", "Process 134", 0).Err()
	if err != nil {
		panic(err)
	}

	fmt.Println("OK")

	value, err := rdb.Get(ctx, "bike:1").Result()
	if err != nil {
		panic(err)
	}
	fmt.Printf("The name of the bike is %s", value)

}

```

```c#

using NRedisStack.Tests;
using StackExchange.Redis;

public class SetGetExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        bool status = db.StringSet("bike:1", "Process 134");

        if (status)
            Console.WriteLine("Successfully added a bike.");

        var value = db.StringGet("bike:1");

        if (value.HasValue)
            Console.WriteLine("The name of the bike is: " + value + ".");

    }
}
```

Hashes are the equivalent of dictionaries (dicts or hash maps). Among other things, you can use hashes to represent plain objects and to store groupings of counters. The following example explains how to set and access field values of an object:

```plaintext
> HSET bike:1 model Deimos brand Ergonom type 'Enduro bikes' price 4972
(integer) 4
> HGET bike:1 model
"Deimos"
> HGET bike:1 price
"4972"
> HGETALL bike:1
1) "model"
2) "Deimos"
3) "brand"
4) "Ergonom"
5) "type"
6) "Enduro bikes"
7) "price"
8) "4972"
```

```python
"""
Code samples for Hash doc pages:
    https://redis.io/docs/latest/develop/data-types/hashes/
"""
import redis

r = redis.Redis(decode_responses=True)
res1 = r.hset(
    "bike:1",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)
print(res1)
# >>> 4

res2 = r.hget("bike:1", "model")
print(res2)
# >>> 'Deimos'

res3 = r.hget("bike:1", "price")
print(res3)
# >>> '4972'

res4 = r.hgetall("bike:1")
print(res4)
# >>> {'model': 'Deimos', 'brand': 'Ergonom', 'type': 'Enduro bikes', 'price': '4972'}

res5 = r.hmget("bike:1", ["model", "price"])
print(res5)
# >>> ['Deimos', '4972']

res6 = r.hincrby("bike:1", "price", 100)
print(res6)
# >>> 5072
res7 = r.hincrby("bike:1", "price", -100)
print(res7)
# >>> 4972

res11 = r.hincrby("bike:1:stats", "rides", 1)
print(res11)
# >>> 1
res12 = r.hincrby("bike:1:stats", "rides", 1)
print(res12)
# >>> 2
res13 = r.hincrby("bike:1:stats", "rides", 1)
print(res13)
# >>> 3
res14 = r.hincrby("bike:1:stats", "crashes", 1)
print(res14)
# >>> 1
res15 = r.hincrby("bike:1:stats", "owners", 1)
print(res15)
# >>> 1
res16 = r.hget("bike:1:stats", "rides")
print(res16)
# >>> 3
res17 = r.hmget("bike:1:stats", ["crashes", "owners"])
print(res17)
# >>> ['1', '1']

```

```node.js
import assert from 'assert';
import { createClient } from 'redis';

const client = createClient();
await client.connect();
const res1 = await client.hSet(
  'bike:1',
  {
    'model': 'Deimos',
    'brand': 'Ergonom',
    'type': 'Enduro bikes',
    'price': 4972,
  }
)
console.log(res1) // 4

const res2 = await client.hGet('bike:1', 'model')
console.log(res2)  // 'Deimos'

const res3 = await client.hGet('bike:1', 'price')
console.log(res3)  // '4972'

const res4 = await client.hGetAll('bike:1')
console.log(res4)  
/*
{
  brand: 'Ergonom',
  model: 'Deimos',
  price: '4972',
  type: 'Enduro bikes'
}
*/

const res5 = await client.hmGet('bike:1', ['model', 'price'])
console.log(res5)  // ['Deimos', '4972']

const res6 = await client.hIncrBy('bike:1', 'price', 100)
console.log(res6)  // 5072
const res7 = await client.hIncrBy('bike:1', 'price', -100)
console.log(res7)  // 4972

const res11 = await client.hIncrBy('bike:1:stats', 'rides', 1)
console.log(res11)  // 1
const res12 = await client.hIncrBy('bike:1:stats', 'rides', 1)
console.log(res12)  // 2
const res13 = await client.hIncrBy('bike:1:stats', 'rides', 1)
console.log(res13)  // 3
const res14 = await client.hIncrBy('bike:1:stats', 'crashes', 1)
console.log(res14)  // 1
const res15 = await client.hIncrBy('bike:1:stats', 'owners', 1)
console.log(res15)  // 1
const res16 = await client.hGet('bike:1:stats', 'rides')
console.log(res16)  // 3
const res17 = await client.hmGet('bike:1:stats', ['crashes', 'owners'])
console.log(res17)  // ['1', '1']

```

```java
package io.redis.examples;

import redis.clients.jedis.UnifiedJedis;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HashExample {

  public void run() {
    try (UnifiedJedis jedis = new UnifiedJedis("redis://localhost:6379")) {

      Map<String, String> bike1 = new HashMap<>();
      bike1.put("model", "Deimos");
      bike1.put("brand", "Ergonom");
      bike1.put("type", "Enduro bikes");
      bike1.put("price", "4972");

      Long res1 = jedis.hset("bike:1", bike1);
      System.out.println(res1); // 4

      String res2 = jedis.hget("bike:1", "model");
      System.out.println(res2); // Deimos

      String res3 = jedis.hget("bike:1", "price");
      System.out.println(res3); // 4972

      Map<String, String> res4 = jedis.hgetAll("bike:1");
      System.out.println(res4); // {type=Enduro bikes, brand=Ergonom, price=4972, model=Deimos}

      List<String> res5 = jedis.hmget("bike:1", "model", "price");
      System.out.println(res5); // [Deimos, 4972]

      Long res6 = jedis.hincrBy("bike:1", "price", 100);
      System.out.println(res6); // 5072
      Long res7 = jedis.hincrBy("bike:1", "price", -100);
      System.out.println(res7); // 4972

      Long res8 = jedis.hincrBy("bike:1:stats", "rides", 1);
      System.out.println(res8); // 1
      Long res9 = jedis.hincrBy("bike:1:stats", "rides", 1);
      System.out.println(res9); // 2
      Long res10 = jedis.hincrBy("bike:1:stats", "rides", 1);
      System.out.println(res10); // 3
      Long res11 = jedis.hincrBy("bike:1:stats", "crashes", 1);
      System.out.println(res11); // 1
      Long res12 = jedis.hincrBy("bike:1:stats", "owners", 1);
      System.out.println(res12); // 1
      String res13 = jedis.hget("bike:1:stats", "rides");
      System.out.println(res13); // 3
      List<String> res14 = jedis.hmget("bike:1:stats", "crashes", "owners");
      System.out.println(res14); // [1, 1]

    }
  }
}
```

```java
package io.redis.examples.async;

import io.lettuce.core.*;
import io.lettuce.core.api.async.RedisAsyncCommands;
import io.lettuce.core.api.StatefulRedisConnection;

import java.util.*;
import java.util.concurrent.CompletableFuture;

public class HashExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisAsyncCommands<String, String> asyncCommands = connection.async();

            Map<String, String> bike1 = new HashMap<>();
            bike1.put("model", "Deimos");
            bike1.put("brand", "Ergonom");
            bike1.put("type", "Enduro bikes");
            bike1.put("price", "4972");

            CompletableFuture<Void> setGetAll = asyncCommands.hset("bike:1", bike1).thenCompose(res1 -> {
                System.out.println(res1); // >>> 4
                return asyncCommands.hget("bike:1", "model");
            }).thenCompose(res2 -> {
                System.out.println(res2); // >>> Deimos
                return asyncCommands.hget("bike:1", "price");
            }).thenCompose(res3 -> {
                System.out.println(res3); // >>> 4972
                return asyncCommands.hgetall("bike:1");
            })
                    .thenAccept(System.out::println)
                    // >>> {type=Enduro bikes, brand=Ergonom, price=4972, model=Deimos}
                    .toCompletableFuture();

            CompletableFuture<Void> hmGet = setGetAll.thenCompose(res4 -> {
                return asyncCommands.hmget("bike:1", "model", "price");
            })
                    .thenAccept(System.out::println)
                    // [KeyValue[model, Deimos], KeyValue[price, 4972]]
                    .toCompletableFuture();

            CompletableFuture<Void> hIncrBy = hmGet.thenCompose(r -> {
                return asyncCommands.hincrby("bike:1", "price", 100);
            }).thenCompose(res6 -> {
                System.out.println(res6); // >>> 5072
                return asyncCommands.hincrby("bike:1", "price", -100);
            })
                    .thenAccept(System.out::println)
                    // >>> 4972
                    .toCompletableFuture();

            CompletableFuture<Void> incrByGetMget = asyncCommands.hincrby("bike:1:stats", "rides", 1).thenCompose(res7 -> {
                System.out.println(res7); // >>> 1
                return asyncCommands.hincrby("bike:1:stats", "rides", 1);
            }).thenCompose(res8 -> {
                System.out.println(res8); // >>> 2
                return asyncCommands.hincrby("bike:1:stats", "rides", 1);
            }).thenCompose(res9 -> {
                System.out.println(res9); // >>> 3
                return asyncCommands.hincrby("bike:1:stats", "crashes", 1);
            }).thenCompose(res10 -> {
                System.out.println(res10); // >>> 1
                return asyncCommands.hincrby("bike:1:stats", "owners", 1);
            }).thenCompose(res11 -> {
                System.out.println(res11); // >>> 1
                return asyncCommands.hget("bike:1:stats", "rides");
            }).thenCompose(res12 -> {
                System.out.println(res12); // >>> 3
                return asyncCommands.hmget("bike:1:stats", "crashes", "owners");
            })
                    .thenAccept(System.out::println)
                    // >>> [KeyValue[crashes, 1], KeyValue[owners, 1]]
                    .toCompletableFuture();

            CompletableFuture.allOf(
                    hIncrBy, incrByGetMget).join();
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

import reactor.core.publisher.Mono;

import java.util.*;

public class HashExample {

    public void run() {
        RedisClient redisClient = RedisClient.create("redis://localhost:6379");

        try (StatefulRedisConnection<String, String> connection = redisClient.connect()) {
            RedisReactiveCommands<String, String> reactiveCommands = connection.reactive();

            Map<String, String> bike1 = new HashMap<>();
            bike1.put("model", "Deimos");
            bike1.put("brand", "Ergonom");
            bike1.put("type", "Enduro bikes");
            bike1.put("price", "4972");

            Mono<Long> setGetAll = reactiveCommands.hset("bike:1", bike1).doOnNext(result -> {
                System.out.println(result); // >>> 4
            });

            setGetAll.block();

            Mono<String> getModel = reactiveCommands.hget("bike:1", "model").doOnNext(result -> {
                System.out.println(result); // >>> Deimos
            });

            Mono<String> getPrice = reactiveCommands.hget("bike:1", "price").doOnNext(result -> {
                System.out.println(result); // >>> 4972
            });

            Mono<List<KeyValue<String, String>>> getAll = reactiveCommands.hgetall("bike:1").collectList().doOnNext(result -> {
                System.out.println(result);
                // >>> [KeyValue[type, Enduro bikes], KeyValue[brand, Ergonom],
                // KeyValue[price, 4972], KeyValue[model, Deimos]]
            });

            Mono<List<KeyValue<String, String>>> hmGet = reactiveCommands.hmget("bike:1", "model", "price").collectList()
                    .doOnNext(result -> {
                        System.out.println(result);
                        // >>> [KeyValue[model, Deimos], KeyValue[price, 4972]]
                    });

            Mono.when(getModel, getPrice, getAll, hmGet).block();

            Mono<Void> hIncrBy = reactiveCommands.hincrby("bike:1", "price", 100).doOnNext(result -> {
                System.out.println(result); // >>> 5072
            }).flatMap(v -> reactiveCommands.hincrby("bike:1", "price", -100)).doOnNext(result -> {
                System.out.println(result); // >>> 4972
            }).then();
            hIncrBy.block();

            Mono<Void> incrByGetMget = reactiveCommands.hincrby("bike:1:stats", "rides", 1).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "rides", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 2
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "rides", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 3
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "crashes", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).flatMap(v -> reactiveCommands.hincrby("bike:1:stats", "owners", 1)).doOnNext(result -> {
                System.out.println(result); // >>> 1
            }).then();

            incrByGetMget.block();

            Mono<String> getRides = reactiveCommands.hget("bike:1:stats", "rides").doOnNext(result -> {
                System.out.println(result); // >>> 3
            });

            Mono<List<KeyValue<String, String>>> getCrashesOwners = reactiveCommands.hmget("bike:1:stats", "crashes", "owners")
                    .collectList().doOnNext(result -> {
                        System.out.println(result);
                        // >>> [KeyValue[crashes, 1], KeyValue[owners, 1]]
                    });

            Mono.when(getRides, getCrashesOwners).block();
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

func ExampleClient_set_get_all() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
	})

	hashFields := []string{
		"model", "Deimos",
		"brand", "Ergonom",
		"type", "Enduro bikes",
		"price", "4972",
	}

	res1, err := rdb.HSet(ctx, "bike:1", hashFields).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1) // >>> 4

	res2, err := rdb.HGet(ctx, "bike:1", "model").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2) // >>> Deimos

	res3, err := rdb.HGet(ctx, "bike:1", "price").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3) // >>> 4972

	cmdReturn := rdb.HGetAll(ctx, "bike:1")
	res4, err := cmdReturn.Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4)
	// >>> map[brand:Ergonom model:Deimos price:4972 type:Enduro bikes]

	type BikeInfo struct {
		Model string `redis:"model"`
		Brand string `redis:"brand"`
		Type  string `redis:"type"`
		Price int    `redis:"price"`
	}

	var res4a BikeInfo

	if err := cmdReturn.Scan(&res4a); err != nil {
		panic(err)
	}

	fmt.Printf("Model: %v, Brand: %v, Type: %v, Price: $%v\n",
		res4a.Model, res4a.Brand, res4a.Type, res4a.Price)
	// >>> Model: Deimos, Brand: Ergonom, Type: Enduro bikes, Price: $4972

}

func ExampleClient_hmget() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
	})

	hashFields := []string{
		"model", "Deimos",
		"brand", "Ergonom",
		"type", "Enduro bikes",
		"price", "4972",
	}

	_, err := rdb.HSet(ctx, "bike:1", hashFields).Result()

	if err != nil {
		panic(err)
	}

	cmdReturn := rdb.HMGet(ctx, "bike:1", "model", "price")
	res5, err := cmdReturn.Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5) // >>> [Deimos 4972]

	type BikeInfo struct {
		Model string `redis:"model"`
		Brand string `redis:"-"`
		Type  string `redis:"-"`
		Price int    `redis:"price"`
	}

	var res5a BikeInfo

	if err := cmdReturn.Scan(&res5a); err != nil {
		panic(err)
	}

	fmt.Printf("Model: %v, Price: $%v\n", res5a.Model, res5a.Price)
	// >>> Model: Deimos, Price: $4972

}

func ExampleClient_hincrby() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
	})

	hashFields := []string{
		"model", "Deimos",
		"brand", "Ergonom",
		"type", "Enduro bikes",
		"price", "4972",
	}

	_, err := rdb.HSet(ctx, "bike:1", hashFields).Result()

	if err != nil {
		panic(err)
	}

	res6, err := rdb.HIncrBy(ctx, "bike:1", "price", 100).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res6) // >>> 5072

	res7, err := rdb.HIncrBy(ctx, "bike:1", "price", -100).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> 4972

}

func ExampleClient_incrby_get_mget() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
	})

	res8, err := rdb.HIncrBy(ctx, "bike:1:stats", "rides", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> 1

	res9, err := rdb.HIncrBy(ctx, "bike:1:stats", "rides", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 2

	res10, err := rdb.HIncrBy(ctx, "bike:1:stats", "rides", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res10) // >>> 3

	res11, err := rdb.HIncrBy(ctx, "bike:1:stats", "crashes", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> 1

	res12, err := rdb.HIncrBy(ctx, "bike:1:stats", "owners", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12) // >>> 1

	res13, err := rdb.HGet(ctx, "bike:1:stats", "rides").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13) // >>> 3

	res14, err := rdb.HMGet(ctx, "bike:1:stats", "crashes", "owners").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14) // >>> [1 1]

}
```

```c#

using NRedisStack.Tests;
using StackExchange.Redis;

public class HashExample
{
    public void Run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();
        db.KeyDelete("bike:1");
        db.HashSet("bike:1", [
            new("model", "Deimos"),
            new("brand", "Ergonom"),
            new("type", "Enduro bikes"),
            new("price", 4972)
        ]);

        Console.WriteLine("Hash Created");
        // Hash Created

        var model = db.HashGet("bike:1", "model");
        Console.WriteLine($"Model: {model}");
        // Model: Deimos

        var price = db.HashGet("bike:1", "price");
        Console.WriteLine($"Price: {price}");
        // Price: 4972

        var bike = db.HashGetAll("bike:1");
        Console.WriteLine("bike:1");
        Console.WriteLine(string.Join("\n", bike.Select(b => $"{b.Name}: {b.Value}")));
        // Bike:1:
        // model: Deimos
        // brand: Ergonom
        // type: Enduro bikes
        // price: 4972

        var values = db.HashGet("bike:1", ["model", "price"]);
        Console.WriteLine(string.Join(" ", values));
        // Deimos 4972

        var newPrice = db.HashIncrement("bike:1", "price", 100);
        Console.WriteLine($"New price: {newPrice}");
        // New price: 5072

        newPrice = db.HashIncrement("bike:1", "price", -100);
        Console.WriteLine($"New price: {newPrice}");
        // New price: 4972

        var rides = db.HashIncrement("bike:1", "rides");
        Console.WriteLine($"Rides: {rides}");
        // Rides: 1

        rides = db.HashIncrement("bike:1", "rides");
        Console.WriteLine($"Rides: {rides}");
        // Rides: 2

        rides = db.HashIncrement("bike:1", "rides");
        Console.WriteLine($"Rides: {rides}");
        // Rides: 3

        var crashes = db.HashIncrement("bike:1", "crashes");
        Console.WriteLine($"Crashes: {crashes}");
        // Crashes: 1

        var owners = db.HashIncrement("bike:1", "owners");
        Console.WriteLine($"Owners: {owners}");
        // Owners: 1

        var stats = db.HashGet("bike:1", ["crashes", "owners"]);
        Console.WriteLine($"Bike stats: crashes={stats[0]}, owners={stats[1]}");
        // Bike stats: crashes=1, owners=1
    }
}
```

```php
<?php

require 'vendor/autoload.php';

use Predis\Client as PredisClient;

class DtHashTest
{
    public function testDtHash() {
        $r = new PredisClient([
            'scheme'   => 'tcp',
            'host'     => '127.0.0.1',
            'port'     => 6379,
            'password' => '',
            'database' => 0,
        ]);

        $res1 = $r->hmset('bike:1', [
            'model' => 'Deimos',
            'brand' => 'Ergonom',
            'type' => 'Enduro bikes',
            'price' => 4972,
        ]);

        echo $res1 . PHP_EOL;
        // >>> 4

        $res2 = $r->hget('bike:1', 'model');
        echo $res2 . PHP_EOL;
        // >>> Deimos

        $res3 = $r->hget('bike:1', 'price');
        echo $res3 . PHP_EOL;
        // >>> 4972

        $res4 = $r->hgetall('bike:1');
        echo json_encode($res3) . PHP_EOL;
        // >>> {"name":"Deimos","brand":"Ergonom","type":"Enduro bikes","price":"4972"}

        $res5 = $r->hmget('bike:1', ['model', 'price']);
        echo json_encode($res5) . PHP_EOL;
        // >>> ["Deimos","4972"]

        $res6 = $r->hincrby('bike:1', 'price', 100);
        echo $res6 . PHP_EOL;
        // >>> 5072

        $res7 = $r->hincrby('bike:1', 'price', -100);
        echo $res7 . PHP_EOL;
        // >>> 4972

        $res8 = $r->hincrby('bike:1:stats', 'rides', 1);
        echo $res8 . PHP_EOL;
        // >>> 1

        $res9 = $r->hincrby('bike:1:stats', 'rides', 1);
        echo $res9 . PHP_EOL;
        // >>> 2

        $res10 = $r->hincrby('bike:1:stats', 'rides', 1);
        echo $res10 . PHP_EOL;
        // >>> 3

        $res11 = $r->hincrby('bike:1:stats', 'crashes', 1);
        echo $res11 . PHP_EOL;
        // >>> 1

        $res12 = $r->hincrby('bike:1:stats', 'owners', 1);
        echo $res12 . PHP_EOL;
        // >>> 1

        $res13 = $r->hget('bike:1:stats', 'rides');
        echo $res13 . PHP_EOL;
        // >>> 3

        $res14 = $r->hmget('bike:1:stats', ['crashes', 'owners']);
        echo json_encode($res14) . PHP_EOL;
        // >>> ["1","1"]
    }
}
```

```rust
mod hash_tests {
    use redis::Commands;

    fn run() {
        let mut r = match redis::Client::open("redis://127.0.0.1") {
            Ok(client) => {
                match client.get_connection() {
                    Ok(conn) => conn,
                    Err(e) => {
                        println!("Failed to connect to Redis: {e}");
                        return;
                    }
                }
            },
            Err(e) => {
                println!("Failed to create Redis client: {e}");
                return;
            }
        };

        let hash_fields = [
            ("model", "Deimos"),
            ("brand", "Ergonom"),
            ("type", "Enduro bikes"),
            ("price", "4972"),
        ];

        if let Ok(res) = r.hset_multiple("bike:1", &hash_fields) {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.hget("bike:1", "model") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1 model: {e}");
                return;
            }
        };

        match r.hget("bike:1", "price") {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> 4972
            },
            Err(e) => {
                println!("Error getting bike:1 price: {e}");
                return;
            }
        };

        match r.hgetall("bike:1") {
            Ok(res) => {
                let res: Vec<(String, String)> = res;
                println!("{res:?}");
                // >>> [("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };

        match r.hmget("bike:1", &["model", "price"]) {
            Ok(res) => {
                let res: Vec<String> = res;
                println!("{res:?}");   // >>> ["Deimos", "4972"]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };

        if let Ok(res) = r.hincr("bike:1", "price", 100) {
            let res: i32 = res;
            println!("{res}");    // >>> 5072
        }

        if let Ok(res) = r.hincr("bike:1", "price", -100) {
            let res: i32 = res;
            println!("{res}");    // >>> 4972
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 2
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 3
        }

        if let Ok(res) = r.hincr("bike:1:stats", "crashes", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "owners", 1) {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        match r.hget("bike:1:stats", "rides") {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");   // >>> 3
            },
            Err(e) => {
                println!("Error getting bike:1:stats rides: {e}");
                return;
            }
        };

        match r.hmget("bike:1:stats", &["crashes", "owners"]) {
            Ok(res) => {
                let res: Vec<i32> = res;
                println!("{res:?}");   // >>> [1, 1]
            },
            Err(e) => {
                println!("Error getting bike:1:stats crashes and owners: {e}");
                return;
            }
        };
    }
}
```

```rust
mod tests {
    use redis::AsyncCommands;

    async fn run() {
        let mut r = match redis::Client::open("redis://127.0.0.1") {
            Ok(client) => {
                match client.get_multiplexed_async_connection().await {
                    Ok(conn) => conn,
                    Err(e) => {
                        println!("Failed to connect to Redis: {e}");
                        return;
                    }
                }
            },
            Err(e) => {
                println!("Failed to create Redis client: {e}");
                return;
            }
        };

        let hash_fields = [
            ("model", "Deimos"),
            ("brand", "Ergonom"),
            ("type", "Enduro bikes"),
            ("price", "4972"),
        ];

        if let Ok(res) = r.hset_multiple("bike:1", &hash_fields).await {
            let res: String = res;
            println!("{res}");    // >>> OK
        }

        match r.hget("bike:1", "model").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> Deimos
            },
            Err(e) => {
                println!("Error getting bike:1 model: {e}");
                return;
            }
        };

        match r.hget("bike:1", "price").await {
            Ok(res) => {
                let res: String = res;
                println!("{res}");   // >>> 4972
            },
            Err(e) => {
                println!("Error getting bike:1 price: {e}");
                return;
            }
        };

        match r.hgetall("bike:1").await {
            Ok(res) => {
                let res: Vec<(String, String)> = res;
                println!("{res:?}");
                // >>> [("model", "Deimos"), ("brand", "Ergonom"), ("type", "Enduro bikes"), ("price", "4972")]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };

        match r.hmget("bike:1", &["model", "price"]).await {
            Ok(res) => {
                let res: Vec<String> = res;
                println!("{res:?}");   // >>> ["Deimos", "4972"]
            },
            Err(e) => {
                println!("Error getting bike:1: {e}");
                return;
            }
        };

        if let Ok(res) = r.hincr("bike:1", "price", 100).await {
            let res: i32 = res;
            println!("{res}");    // >>> 5072
        }

        if let Ok(res) = r.hincr("bike:1", "price", -100).await {
            let res: i32 = res;
            println!("{res}");    // >>> 4972
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 2
        }

        if let Ok(res) = r.hincr("bike:1:stats", "rides", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 3
        }

        if let Ok(res) = r.hincr("bike:1:stats", "crashes", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        if let Ok(res) = r.hincr("bike:1:stats", "owners", 1).await {
            let res: i32 = res;
            println!("{res}");    // >>> 1
        }

        match r.hget("bike:1:stats", "rides").await {
            Ok(res) => {
                let res: i32 = res;
                println!("{res}");   // >>> 3
            },
            Err(e) => {
                println!("Error getting bike:1:stats rides: {e}");
                return;
            }
        };

        match r.hmget("bike:1:stats", &["crashes", "owners"]).await {
            Ok(res) => {
                let res: Vec<i32> = res;
                println!("{res:?}");   // >>> [1, 1]
            },
            Err(e) => {
                println!("Error getting bike:1:stats crashes and owners: {e}");
                return;
            }
        };
    }
}
```

You can get a complete overview of available data types in this documentation site's [data types section](/docs/latest/develop/data-types/). Each data type has commands allowing you to manipulate or retrieve data. The [commands reference](/docs/latest/commands/) provides a sophisticated explanation.

## Scan the keyspace

Each item within Redis has a unique key. All items live within the Redis [keyspace](/docs/latest/develop/using-commands/keyspace/). You can scan the Redis keyspace via the [SCAN command](/docs/latest/commands/scan/). Here is an example that scans for the first 100 keys that have the prefix `bike:`:

```
SCAN 0 MATCH "bike:*" COUNT 100
```

[SCAN](/docs/latest/commands/scan/) returns a cursor position, allowing you to scan iteratively for the next batch of keys until you reach the cursor value 0.

## Next steps

You can address more use cases with Redis by reading these additional quick start guides:

*   [Redis as a document database](../document-database/index.md)
*   [Redis as a vector database](../vector-database/index.md)

## Continue learning with Redis University

See the [Get Started with Redis learning path](https://university.redis.io/learningpath/14q8m6gilfwltm) for courses.

## On this page
