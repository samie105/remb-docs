---
title: "Geospatial queries"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/geo-spatial/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/geo-spatial/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:24.222Z"
content_hash: "a334fe9e81682b5163a5246b87a9b2a704588b86474bd6f9d1e48db62fb33e28"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Geospatial queries","→","Geospatial queries"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Geospatial queries","→","Geospatial queries"]
nav_prev: {"path": "redis/docs/latest/integrate/riot/docs/index.md", "title": "Documentation"}
nav_next: {"path": "redis/docs/latest/develop/use-cases/time-series-dashboard/go/index.md", "title": "Rolling sensor graph demo with Go"}
---

# Geospatial queries

Query based on geographic data

The geospatial feature in Redis Open Source allows you to query for data associated with geographic locations. You can either query for locations within a specific radius or based on geometric shapes, such as polygons. A polygon shape could, for instance, represent a lake or the layout of a building.

The examples in this article use the following schema:

Field name

Field type

`store_location`

`GEO`

`pickup_zone`

`GEOSHAPE`

Note:

Redis version 7.2.0 or higher is required to use the `GEOSHAPE` field type.

## Radius

You can construct a radius query by passing the center coordinates (longitude, latitude), the radius, and the distance unit to the [FT.SEARCH](/docs/latest/commands/ft.search/) command.

```
FT.SEARCH index "@geo_field:[lon lat radius unit]"
```

Allowed units are `m`, `km`, `mi`, and `ft`.

The following query finds all bicycle stores within a radius of 20 miles around London:

```plaintext
FT.SEARCH idx:bicycle "@store_location:[-0.1778 51.5524 20 mi]"
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import GeoField, GeoShapeField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    GeoField("$.store_location", as_name="store_location"),
    GeoShapeField("$.pickup_zone", coord_system=GeoShapeField.FLAT, as_name="pickup_zone")
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

params_dict = {"lon": -0.1778, "lat": 51.5524, "radius": 20, "units": "mi"}
q = Query("@store_location:[$lon $lat $radius $units]").dialect(2)
res = index.search(q, query_params=params_dict)
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:5', ...

params_dict = {"bike": "POINT(-0.1278 51.5074)"}
q = Query("@pickup_zone:[CONTAINS $bike]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 1

params_dict = {"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))"}
q = Query("@pickup_zone:[WITHIN $europe]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 5

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE } from '@redis/search';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.store_location': {
    type: SCHEMA_FIELD_TYPE.GEO,
    AS: 'store_location'
  },
   '$.pickup_zone': {
    type: SCHEMA_FIELD_TYPE.GEOSHAPE,
    AS: 'pickup_zone'
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

const res1= await client.ft.search('idx:bicycle', '@store_location:[-0.1778 51.5524 20 mi]');
console.log(res1.total); // >>> 1
console.log(res1); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}

const params_dict_geo2 = { bike: 'POINT(-0.1278 51.5074)' };
const q_geo2 = '@pickup_zone:[CONTAINS $bike]';
const res2 = await client.ft.search('idx:bicycle', q_geo2, { PARAMS: params_dict_geo2, DIALECT: 3 });
console.log(res2.total); // >>> 1
console.log(res2); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}

const params_dict_geo3 = { europe: 'POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))' };
const q_geo3 = '@pickup_zone:[WITHIN $europe]';
const res3 = await client.ft.search('idx:bicycle', q_geo3, { PARAMS: params_dict_geo3, DIALECT: 3 });
console.log(res3.total); // >>> 5
console.log(res3); // >>>
// {
//   total: 5,
//   documents: [
//     { id: 'bicycle:5', value: [Object: null prototype] },
//     { id: 'bicycle:6', value: [Object: null prototype] },
//     { id: 'bicycle:7', value: [Object: null prototype] },
//     { id: 'bicycle:8', value: [Object: null prototype] },
//     { id: 'bicycle:9', value: [Object: null prototype] }
//   ]
// }

```

```java

import java.util.List;
import java.util.stream.Stream;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryGeoExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition"),
            GeoField.of("$.store_location").as("store_location"),
            GeoShapeField.of("$.pickup_zone", CoordinateSystem.FLAT).as("pickup_zone")
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

        SearchResult res1 = jedis.ftSearch("idx:bicycle",
            "@store_location:[$lon $lat $radius $units]",
            FTSearchParams.searchParams()
                    .addParam("lon", -0.1778)
                    .addParam("lat", 51.5524)
                    .addParam("radius", 20)
                    .addParam("units", "mi")
                    .dialect(2)
        );
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5

        // Tests for 'geo1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[CONTAINS $bike]",
            FTSearchParams.searchParams()
                    .addParam("bike", "POINT(-0.1278 51.5074)")
                    .dialect(3)
        );
        System.out.println(res2.getTotalResults());   // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5

        // Tests for 'geo2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[WITHIN $europe]",
            FTSearchParams.searchParams()
                    .addParam("europe", "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))")
                    .dialect(3)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8
        // >>> bicycle:9

        // Tests for 'geo3' step.

        jedis.close();
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

func ExampleClient_query_geo() {
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
		&redis.FieldSchema{
			FieldName: "$.store_location",
			As:        "store_location",
			FieldType: redis.SearchFieldTypeGeo,
		},
		&redis.FieldSchema{
			FieldName:         "$.pickup_zone",
			As:                "pickup_zone",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
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
		"idx:bicycle", "@store_location:[$lon $lat $radius $units]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"lon":    -0.1778,
				"lat":    51.5524,
				"radius": 20,
				"units":  "mi",
			},
			DialectVersion: 2,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[CONTAINS $bike]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"bike": "POINT(-0.1278 51.5074)",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5

	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[WITHIN $europe]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})

	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8
	// >>> bicycle:9

}
```

## Shape

The only supported shapes are points and polygons. You can query for polygons or points that either contain or are within a given geometric shape.

```
FT.SEARCH index "@geo_shape_field:[{WITHIN|CONTAINS|INTERSECTS|DISJOINT} $shape] PARAMS 2 shape "shape_as_wkt" DIALECT 3
```

Here is a more detailed explanation of this query:

1.  **Field name**: you need to replace `geo_shape_field` with the `GEOSHAPE` field's name on which you want to query.
2.  **Spatial operator**: spatial operators define the relationship between the shapes in the database and the shape you are searching for. You can either use `WITHIN`, `CONTAINS`, `INTERSECTS`, or `DISJOINT`. `WITHIN` finds any shape in the database that is inside the given shape. `CONTAINS` queries for any shape that surrounds the given shape. `INTERSECTS` finds any shape that has coordinates in common with the provided shape. `DISJOINT` finds any shapes that have nothing in common with the provided shape. `INTERSECTS` and `DISJOINT` were introduced in v2.10.
3.  **Parameter**: the query refers to a parameter named `shape`. You can use any parameter name here. You need to use the `PARAMS` clause to set the parameter value. The value follows the [well-known text representation of a geometry](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry). Supported types are `POINT(x y)` and `POLYGON((x1 y1, x2 y2, ...))`.
4.  **Dialect**: Shape-based queries are not supported in `DIALECT 1`.

The following example query verifies if a bicycle is within a pickup zone:

```plaintext
FT.SEARCH idx:bicycle "@pickup_zone:[CONTAINS $bike]" PARAMS 2 bike "POINT(-0.1278 51.5074)" DIALECT 2
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import GeoField, GeoShapeField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    GeoField("$.store_location", as_name="store_location"),
    GeoShapeField("$.pickup_zone", coord_system=GeoShapeField.FLAT, as_name="pickup_zone")
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

params_dict = {"lon": -0.1778, "lat": 51.5524, "radius": 20, "units": "mi"}
q = Query("@store_location:[$lon $lat $radius $units]").dialect(2)
res = index.search(q, query_params=params_dict)
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:5', ...

params_dict = {"bike": "POINT(-0.1278 51.5074)"}
q = Query("@pickup_zone:[CONTAINS $bike]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 1

params_dict = {"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))"}
q = Query("@pickup_zone:[WITHIN $europe]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 5

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE } from '@redis/search';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.store_location': {
    type: SCHEMA_FIELD_TYPE.GEO,
    AS: 'store_location'
  },
   '$.pickup_zone': {
    type: SCHEMA_FIELD_TYPE.GEOSHAPE,
    AS: 'pickup_zone'
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

const res1= await client.ft.search('idx:bicycle', '@store_location:[-0.1778 51.5524 20 mi]');
console.log(res1.total); // >>> 1
console.log(res1); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}

const params_dict_geo2 = { bike: 'POINT(-0.1278 51.5074)' };
const q_geo2 = '@pickup_zone:[CONTAINS $bike]';
const res2 = await client.ft.search('idx:bicycle', q_geo2, { PARAMS: params_dict_geo2, DIALECT: 3 });
console.log(res2.total); // >>> 1
console.log(res2); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}

const params_dict_geo3 = { europe: 'POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))' };
const q_geo3 = '@pickup_zone:[WITHIN $europe]';
const res3 = await client.ft.search('idx:bicycle', q_geo3, { PARAMS: params_dict_geo3, DIALECT: 3 });
console.log(res3.total); // >>> 5
console.log(res3); // >>>
// {
//   total: 5,
//   documents: [
//     { id: 'bicycle:5', value: [Object: null prototype] },
//     { id: 'bicycle:6', value: [Object: null prototype] },
//     { id: 'bicycle:7', value: [Object: null prototype] },
//     { id: 'bicycle:8', value: [Object: null prototype] },
//     { id: 'bicycle:9', value: [Object: null prototype] }
//   ]
// }

```

```java

import java.util.List;
import java.util.stream.Stream;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryGeoExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition"),
            GeoField.of("$.store_location").as("store_location"),
            GeoShapeField.of("$.pickup_zone", CoordinateSystem.FLAT).as("pickup_zone")
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

        SearchResult res1 = jedis.ftSearch("idx:bicycle",
            "@store_location:[$lon $lat $radius $units]",
            FTSearchParams.searchParams()
                    .addParam("lon", -0.1778)
                    .addParam("lat", 51.5524)
                    .addParam("radius", 20)
                    .addParam("units", "mi")
                    .dialect(2)
        );
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5

        // Tests for 'geo1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[CONTAINS $bike]",
            FTSearchParams.searchParams()
                    .addParam("bike", "POINT(-0.1278 51.5074)")
                    .dialect(3)
        );
        System.out.println(res2.getTotalResults());   // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5

        // Tests for 'geo2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[WITHIN $europe]",
            FTSearchParams.searchParams()
                    .addParam("europe", "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))")
                    .dialect(3)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8
        // >>> bicycle:9

        // Tests for 'geo3' step.

        jedis.close();
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

func ExampleClient_query_geo() {
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
		&redis.FieldSchema{
			FieldName: "$.store_location",
			As:        "store_location",
			FieldType: redis.SearchFieldTypeGeo,
		},
		&redis.FieldSchema{
			FieldName:         "$.pickup_zone",
			As:                "pickup_zone",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
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
		"idx:bicycle", "@store_location:[$lon $lat $radius $units]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"lon":    -0.1778,
				"lat":    51.5524,
				"radius": 20,
				"units":  "mi",
			},
			DialectVersion: 2,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[CONTAINS $bike]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"bike": "POINT(-0.1278 51.5074)",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5

	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[WITHIN $europe]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})

	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8
	// >>> bicycle:9

}
```

If you want to find all pickup zones that are approximately within Europe, then you can use the following query:

```plaintext
FT.SEARCH idx:bicycle "@pickup_zone:[WITHIN $europe]" PARAMS 2 europe "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))" DIALECT 2
```

```python
import json
import sys
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import GeoField, GeoShapeField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis(decode_responses=True)

# create index
schema = (
    GeoField("$.store_location", as_name="store_location"),
    GeoShapeField("$.pickup_zone", coord_system=GeoShapeField.FLAT, as_name="pickup_zone")
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

params_dict = {"lon": -0.1778, "lat": 51.5524, "radius": 20, "units": "mi"}
q = Query("@store_location:[$lon $lat $radius $units]").dialect(2)
res = index.search(q, query_params=params_dict)
print(res)
# >>> Result{1 total, docs: [Document {'id': 'bicycle:5', ...

params_dict = {"bike": "POINT(-0.1278 51.5074)"}
q = Query("@pickup_zone:[CONTAINS $bike]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 1

params_dict = {"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))"}
q = Query("@pickup_zone:[WITHIN $europe]").dialect(3)
res = index.search(q, query_params=params_dict)
print(res.total) # >>> 5

```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE } from '@redis/search';

const client = createClient();

await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
  '$.store_location': {
    type: SCHEMA_FIELD_TYPE.GEO,
    AS: 'store_location'
  },
   '$.pickup_zone': {
    type: SCHEMA_FIELD_TYPE.GEOSHAPE,
    AS: 'pickup_zone'
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

const res1= await client.ft.search('idx:bicycle', '@store_location:[-0.1778 51.5524 20 mi]');
console.log(res1.total); // >>> 1
console.log(res1); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}

const params_dict_geo2 = { bike: 'POINT(-0.1278 51.5074)' };
const q_geo2 = '@pickup_zone:[CONTAINS $bike]';
const res2 = await client.ft.search('idx:bicycle', q_geo2, { PARAMS: params_dict_geo2, DIALECT: 3 });
console.log(res2.total); // >>> 1
console.log(res2); // >>> {total: 1, documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]}

const params_dict_geo3 = { europe: 'POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))' };
const q_geo3 = '@pickup_zone:[WITHIN $europe]';
const res3 = await client.ft.search('idx:bicycle', q_geo3, { PARAMS: params_dict_geo3, DIALECT: 3 });
console.log(res3.total); // >>> 5
console.log(res3); // >>>
// {
//   total: 5,
//   documents: [
//     { id: 'bicycle:5', value: [Object: null prototype] },
//     { id: 'bicycle:6', value: [Object: null prototype] },
//     { id: 'bicycle:7', value: [Object: null prototype] },
//     { id: 'bicycle:8', value: [Object: null prototype] },
//     { id: 'bicycle:9', value: [Object: null prototype] }
//   ]
// }

```

```java

import java.util.List;
import java.util.stream.Stream;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.search.*;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.exceptions.JedisDataException;
import redis.clients.jedis.json.Path2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class QueryGeoExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] schema = {
            TextField.of("$.brand").as("brand"),
            TextField.of("$.model").as("model"),
            TextField.of("$.description").as("description"),
            NumericField.of("$.price").as("price"),
            TagField.of("$.condition").as("condition"),
            GeoField.of("$.store_location").as("store_location"),
            GeoShapeField.of("$.pickup_zone", CoordinateSystem.FLAT).as("pickup_zone")
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

        SearchResult res1 = jedis.ftSearch("idx:bicycle",
            "@store_location:[$lon $lat $radius $units]",
            FTSearchParams.searchParams()
                    .addParam("lon", -0.1778)
                    .addParam("lat", 51.5524)
                    .addParam("radius", 20)
                    .addParam("units", "mi")
                    .dialect(2)
        );
        System.out.println(res1.getTotalResults()); // >>> 1

        List<Document> docs1 = res1.getDocuments();

        for (Document document : docs1) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5

        // Tests for 'geo1' step.

        SearchResult res2 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[CONTAINS $bike]",
            FTSearchParams.searchParams()
                    .addParam("bike", "POINT(-0.1278 51.5074)")
                    .dialect(3)
        );
        System.out.println(res2.getTotalResults());   // >>> 1

        List<Document> docs2 = res2.getDocuments();

        for (Document document : docs2) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5

        // Tests for 'geo2' step.

        SearchResult res3 = jedis.ftSearch("idx:bicycle",
            "@pickup_zone:[WITHIN $europe]",
            FTSearchParams.searchParams()
                    .addParam("europe", "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))")
                    .dialect(3)
        );
        System.out.println(res3.getTotalResults()); // >>> 5

        List<Document> docs3 = res3.getDocuments();

        for (Document document : docs3) {
            System.out.println(document.getId());
        }
        // >>> bicycle:5
        // >>> bicycle:6
        // >>> bicycle:7
        // >>> bicycle:8
        // >>> bicycle:9

        // Tests for 'geo3' step.

        jedis.close();
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

func ExampleClient_query_geo() {
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
		&redis.FieldSchema{
			FieldName: "$.store_location",
			As:        "store_location",
			FieldType: redis.SearchFieldTypeGeo,
		},
		&redis.FieldSchema{
			FieldName:         "$.pickup_zone",
			As:                "pickup_zone",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
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
		"idx:bicycle", "@store_location:[$lon $lat $radius $units]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"lon":    -0.1778,
				"lat":    51.5524,
				"radius": 20,
				"units":  "mi",
			},
			DialectVersion: 2,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res1.Total) // >>> 1

	for _, doc := range res1.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5

	res2, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[CONTAINS $bike]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"bike": "POINT(-0.1278 51.5074)",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res2.Total) // >>> 1

	for _, doc := range res2.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5

	res3, err := rdb.FTSearchWithArgs(ctx,
		"idx:bicycle",
		"@pickup_zone:[WITHIN $europe]",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"europe": "POLYGON((-25 35, 40 35, 40 70, -25 70, -25 35))",
			},
			DialectVersion: 3,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res3.Total) // >>> 5

	sort.Slice(res3.Docs, func(i, j int) bool {
		return res3.Docs[i].ID < res3.Docs[j].ID
	})

	for _, doc := range res3.Docs {
		fmt.Println(doc.ID)
	}
	// >>> bicycle:5
	// >>> bicycle:6
	// >>> bicycle:7
	// >>> bicycle:8
	// >>> bicycle:9

}
```

## On this page
