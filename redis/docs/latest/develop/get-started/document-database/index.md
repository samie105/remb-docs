---
title: "Redis as a document database quick start guide"
source: "https://redis.io/docs/latest/develop/get-started/document-database/"
canonical_url: "https://redis.io/docs/latest/develop/get-started/document-database/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:50.797Z"
content_hash: "393c81bb5a7e5d0065bf76f67a206fd122cd41e43a503738ed338744c5207bdf"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Quick starts","→","Quick starts","→\n      \n        Redis as a document database quick start guide","→","Redis as a document database quick start guide"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Quick starts","→","Quick starts","→\n      \n        Redis as a document database quick start guide","→","Redis as a document database quick start guide"]
nav_prev: {"path": "redis/docs/latest/develop/get-started/data-store/index.md", "title": "Redis as an in-memory data structure store quick start guide"}
nav_next: {"path": "redis/docs/latest/develop/get-started/rag/index.md", "title": "RAG with Redis"}
---

# Redis as a document database quick start guide

Understand how to use Redis as a document database

This quick start guide shows you how to:

1.  Create a secondary index
2.  Add [JSON](/docs/latest/develop/data-types/json/) documents
3.  Search and query your data

The examples in this article refer to a simple bicycle inventory that contains JSON documents with the following structure:

```json
{
  "brand": "brand name",
  "condition": "new | used | refurbished",
  "description": "description",
  "model": "model",
  "price": 0
}
```

## Setup

The easiest way to get started with [Redis](/docs/latest/operate/oss_and_stack/) is to use Redis Cloud:

1.  Create a [free account](https://redis.com/try-free?utm_source=redisio&utm_medium=referral&utm_campaign=2023-09-try_free&utm_content=cu-redis_cloud_users).
    
    ![](../img/free-cloud-db.png)
2.  Follow the instructions to create a free database.
    

This free Redis Cloud database comes out of the box with all the Redis Open Source features.

You can alternatively use the [installation guides](/docs/latest/operate/oss_and_stack/install/install-stack/) to install Redis Open Source on your local machine.

## Connect

The first step is to connect to your Redis Open Source database. You can find further details about the connection options in this documentation site's [Tools section](/docs/latest/develop/tools/). The following example shows how to connect to a Redis Open Source server that runs on localhost (`-h 127.0.0.1`) and listens on the default port (`-p 6379`):

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

You can copy and paste the connection details from the Redis Cloud database configuration page. Here is an example connection string of a Cloud database that is hosted in the AWS region `us-east-1` and listens on port 16379: `redis-16379.c283.us-east-1-4.ec2.cloud.redislabs.com:16379`. The connection string has the format `host:port`. You must also copy and paste your Cloud database's username and password and then pass the credentials to your client or use the [AUTH command](/docs/latest/commands/auth/) after the connection is established.

## Create an index

As explained in the [in-memory data store](/docs/latest/develop/get-started/data-store/) quick start guide, Redis allows you to access an item directly via its key. You also learned how to scan the keyspace. Whereby you can use other data structures (e.g., hashes and sorted sets) as secondary indexes, your application would need to maintain those indexes manually. Redis is a document database that allows you to declare which fields are auto-indexed. Redis currently supports secondary index creation on the [hashes](/docs/latest/develop/data-types/hashes/) and [JSON](/docs/latest/develop/data-types/json/) documents.

The following example shows an [FT.CREATE](/docs/latest/commands/ft.create/) command that creates an index with some text fields, a numeric field (price), and a tag field (condition). The text fields have a weight of 1.0, meaning they have the same relevancy in the context of full-text searches. The field names follow the [JSONPath](/docs/latest/develop/data-types/json/path/) notion. Each such index field maps to a property within the JSON document.

```plaintext
> FT.CREATE idx:bicycle ON JSON PREFIX 1 bicycle: SCORE 1.0 SCHEMA $.brand AS brand TEXT WEIGHT 1.0 $.model AS model TEXT WEIGHT 1.0 $.description AS description TEXT WEIGHT 1.0 $.price AS price NUMERIC $.condition AS condition TAG SEPARATOR ,
OK
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

Any pre-existing JSON documents with a key prefix `bicycle:` are automatically added to the index. Additionally, any JSON documents with that prefix created or modified after index creation are added or re-added to the index.

## Add JSON documents

The example below shows you how to use the [JSON.SET](/docs/latest/commands/json.set/) command to create new JSON documents:

```plaintext
> JSON.SET "bicycle:0" "." "{\"brand\": \"Velorim\", \"model\": \"Jigger\", \"price\": 270, \"description\": \"Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids\\u2019 pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.\", \"condition\": \"new\"}"
OK
> JSON.SET "bicycle:1" "." "{\"brand\": \"Bicyk\", \"model\": \"Hillcraft\", \"price\": 1200, \"description\": \"Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\\\" wheel bike is just too clumsy coming off a 24\\\" bike. The Hillcraft 26 is just the solution they need!\", \"condition\": \"used\"}"
OK
> JSON.SET "bicycle:2" "." "{\"brand\": \"Nord\", \"model\": \"Chook air 5\", \"price\": 815, \"description\": \"The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.\", \"condition\": \"used\"}"
OK
> JSON.SET "bicycle:3" "." "{\"brand\": \"Eva\", \"model\": \"Eva 291\", \"price\": 3400, \"description\": \"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It\\u2019s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!\", \"condition\": \"used\"}"
OK
> JSON.SET "bicycle:4" "." "{\"brand\": \"Noka Bikes\", \"model\": \"Kahuna\", \"price\": 3200, \"description\": \"Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women\\u2019s saddle, different bars and unique colourway.\", \"condition\": \"used\"}"
OK
> JSON.SET "bicycle:5" "." "{\"brand\": \"Breakout\", \"model\": \"XBN 2.1 Alloy\", \"price\": 810, \"description\": \"The XBN 2.1 Alloy is our entry-level road bike \\u2013 but that\\u2019s not to say that it\\u2019s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano\\u2019s, this is a bike which doesn\\u2019t break the bank and delivers craved performance.\", \"condition\": \"new\"}"
OK
> JSON.SET "bicycle:6" "." "{\"brand\": \"ScramBikes\", \"model\": \"WattBike\", \"price\": 2300, \"description\": \"The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It\\u2019s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.\", \"condition\": \"new\"}"
OK
> JSON.SET "bicycle:7" "." "{\"brand\": \"Peaknetic\", \"model\": \"Secto\", \"price\": 430, \"description\": \"If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\", \"condition\": \"new\"}"
OK
> JSON.SET "bicycle:8" "." "{\"brand\": \"nHill\", \"model\": \"Summit\", \"price\": 1200, \"description\": \"This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\\u2019re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.\", \"condition\": \"new\"}"
OK
> JSON.SET "bicycle:9" "." "{\"model\": \"ThrillCycle\", \"brand\": \"BikeShind\", \"price\": 815, \"description\": \"An artsy,  retro-inspired bicycle that\\u2019s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn\\u2019t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.\", \"condition\": \"refurbished\"}"
OK
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

## Search and query using Redis Search

### Wildcard query

You can retrieve all indexed documents using the [FT.SEARCH](/docs/latest/commands/ft.search/) command. Note the `LIMIT` clause below, which allows result pagination.

```plaintext
> FT.SEARCH "idx:bicycle" "*" LIMIT 0 10
1) (integer) 10
 2) "bicycle:1"
 3) 1) "$"
    2) "{\"brand\":\"Bicyk\",\"model\":\"Hillcraft\",\"price\":1200,\"description\":\"Kids want to ride with as little weight as possible. Especially on an incline! They may be at the age when a 27.5\\\" wheel bike is just too clumsy coming off a 24\\\" bike. The Hillcraft 26 is just the solution they need!\",\"condition\":\"used\"}"
 4) "bicycle:2"
 5) 1) "$"
    2) "{\"brand\":\"Nord\",\"model\":\"Chook air 5\",\"price\":815,\"description\":\"The Chook Air 5  gives kids aged six years and older a durable and uberlight mountain bike for their first experience on tracks and easy cruising through forests and fields. The lower  top tube makes it easy to mount and dismount in any situation, giving your kids greater safety on the trails.\",\"condition\":\"used\"}"
 6) "bicycle:4"
 7) 1) "$"
    2) "{\"brand\":\"Noka Bikes\",\"model\":\"Kahuna\",\"price\":3200,\"description\":\"Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women\xe2\x80\x99s saddle, different bars and unique colourway.\",\"condition\":\"used\"}"
 8) "bicycle:5"
 9) 1) "$"
    2) "{\"brand\":\"Breakout\",\"model\":\"XBN 2.1 Alloy\",\"price\":810,\"description\":\"The XBN 2.1 Alloy is our entry-level road bike \xe2\x80\x93 but that\xe2\x80\x99s not to say that it\xe2\x80\x99s a basic machine. With an internal weld aluminium frame, a full carbon fork, and the slick-shifting Claris gears from Shimano\xe2\x80\x99s, this is a bike which doesn\xe2\x80\x99t break the bank and delivers craved performance.\",\"condition\":\"new\"}"
10) "bicycle:0"
11) 1) "$"
    2) "{\"brand\":\"Velorim\",\"model\":\"Jigger\",\"price\":270,\"description\":\"Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids\xe2\x80\x99 pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.\",\"condition\":\"new\"}"
12) "bicycle:6"
13) 1) "$"
    2) "{\"brand\":\"ScramBikes\",\"model\":\"WattBike\",\"price\":2300,\"description\":\"The WattBike is the best e-bike for people who still feel young at heart. It has a Bafang 1000W mid-drive system and a 48V 17.5AH Samsung Lithium-Ion battery, allowing you to ride for more than 60 miles on one charge. It\xe2\x80\x99s great for tackling hilly terrain or if you just fancy a more leisurely ride. With three working modes, you can choose between E-bike, assisted bicycle, and normal bike modes.\",\"condition\":\"new\"}"
14) "bicycle:7"
15) 1) "$"
    2) "{\"brand\":\"Peaknetic\",\"model\":\"Secto\",\"price\":430,\"description\":\"If you struggle with stiff fingers or a kinked neck or back after a few minutes on the road, this lightweight, aluminum bike alleviates those issues and allows you to enjoy the ride. From the ergonomic grips to the lumbar-supporting seat position, the Roll Low-Entry offers incredible comfort. The rear-inclined seat tube facilitates stability by allowing you to put a foot on the ground to balance at a stop, and the low step-over frame makes it accessible for all ability and mobility levels. The saddle is very soft, with a wide back to support your hip joints and a cutout in the center to redistribute that pressure. Rim brakes deliver satisfactory braking control, and the wide tires provide a smooth, stable ride on paved roads and gravel. Rack and fender mounts facilitate setting up the Roll Low-Entry as your preferred commuter, and the BMX-like handlebar offers space for mounting a flashlight, bell, or phone holder.\",\"condition\":\"new\"}"
16) "bicycle:9"
17) 1) "$"
    2) "{\"model\":\"ThrillCycle\",\"brand\":\"BikeShind\",\"price\":815,\"description\":\"An artsy,  retro-inspired bicycle that\xe2\x80\x99s as functional as it is pretty: The ThrillCycle steel frame offers a smooth ride. A 9-speed drivetrain has enough gears for coasting in the city, but we wouldn\xe2\x80\x99t suggest taking it to the mountains. Fenders protect you from mud, and a rear basket lets you transport groceries, flowers and books. The ThrillCycle comes with a limited lifetime warranty, so this little guy will last you long past graduation.\",\"condition\":\"refurbished\"}"
18) "bicycle:3"
19) 1) "$"
    2) "{\"brand\":\"Eva\",\"model\":\"Eva 291\",\"price\":3400,\"description\":\"The sister company to Nord, Eva launched in 2005 as the first and only women-dedicated bicycle brand. Designed by women for women, allEva bikes are optimized for the feminine physique using analytics from a body metrics database. If you like 29ers, try the Eva 291. It\xe2\x80\x99s a brand new bike for 2022.. This full-suspension, cross-country ride has been designed for velocity. The 291 has 100mm of front and rear travel, a superlight aluminum frame and fast-rolling 29-inch wheels. Yippee!\",\"condition\":\"used\"}"
20) "bicycle:8"
21) 1) "$"
    2) "{\"brand\":\"nHill\",\"model\":\"Summit\",\"price\":1200,\"description\":\"This budget mountain bike from nHill performs well both on bike paths and on the trail. The fork with 100mm of travel absorbs rough terrain. Fat Kenda Booster tires give you grip in corners and on wet trails. The Shimano Tourney drivetrain offered enough gears for finding a comfortable pace to ride uphill, and the Tektro hydraulic disc brakes break smoothly. Whether you want an affordable bike that you can take to work, but also take trail in mountains on the weekends or you\xe2\x80\x99re just after a stable, comfortable ride for the bike path, the Summit gives a good value for money.\",\"condition\":\"new\"}"
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

### Single-term full-text query

The following command shows a simple single-term query for finding all bicycles with a specific model:

```plaintext
> FT.SEARCH "idx:bicycle" "@model:Jigger" LIMIT 0 10
1) (integer) 1
2) "bicycle:0"
3) 1) "$"
   2) "{\"brand\":\"Velorim\",\"model\":\"Jigger\",\"price\":270,\"description\":\"Small and powerful, the Jigger is the best ride for the smallest of tikes! This is the tiniest kids\xe2\x80\x99 pedal bike on the market available without a coaster brake, the Jigger is the vehicle of choice for the rare tenacious little rider raring to go.\",\"condition\":\"new\"}"
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

### Exact match query

Below is a command to perform an exact match query that finds all bicycles with the brand name `Noka Bikes`. You must use double quotes around the search term when constructing an exact match query on a text field.

```plaintext
> FT.SEARCH "idx:bicycle" "@brand:\"Noka Bikes\"" LIMIT 0 10
1) (integer) 1
2) "bicycle:4"
3) 1) "$"
   2) "{\"brand\":\"Noka Bikes\",\"model\":\"Kahuna\",\"price\":3200,\"description\":\"Whether you want to try your hand at XC racing or are looking for a lively trail bike that's just as inspiring on the climbs as it is over rougher ground, the Wilder is one heck of a bike built specifically for short women. Both the frames and components have been tweaked to include a women\xe2\x80\x99s saddle, different bars and unique colourway.\",\"condition\":\"used\"}"
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

Please see the [query documentation](/docs/latest/develop/ai/search-and-query/query/) to learn how to make more advanced queries.

## Next steps

You can learn more about how to use Redis Open Source as a vector database in the following quick start guide:

*   [Redis as a vector database](/docs/latest/develop/get-started/vector-database/)

## Continue learning with Redis University

See the [Get Started with Redis learning path](https://university.redis.io/learningpath/14q8m6gilfwltm) for courses.

## On this page
