---
title: "Geospatial indexing"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/indexing/geoindex/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/indexing/geoindex/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:54.005Z"
content_hash: "ccc7084dff598c8fa4bdcd7218e4ae7d514f361cf74fb6b3dc4a37fff81ee23e"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Indexing","→","Indexing","→\n      \n        Geospatial indexing","→","Geospatial indexing"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Indexing","→","Indexing","→\n      \n        Geospatial indexing","→","Geospatial indexing"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/indexing/field-and-type-options/index.md", "title": "Field and type options"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/indexing/schema-definition/index.md", "title": "Schema definition"}
---

# Geospatial indexing

Options for indexing geospatial data

Redis supports two different [schema types](/docs/latest/develop/ai/search-and-query/indexing/field-and-type-options/) for geospatial data:

*   [`GEO`](#geo): This uses a simple format where individual geospatial points are specified as numeric longitude-latitude pairs.
*   [`GEOSHAPE`](#geoshape): This uses a subset of the [Well-Known Text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format to specify both points and polygons using either geographical coordinates or Cartesian coordinates.

The sections below explain how to index these schema types. See the [Geospatial](/docs/latest/develop/ai/search-and-query/advanced-concepts/geo/) reference page for a full description of both types.

## `GEO`

The following command creates a `GEO` index for JSON objects that contain the geospatial data in a field called `location`:

```plaintext
> FT.CREATE productidx ON JSON PREFIX 1 product: SCHEMA $.location AS location GEO
OK
```

```python
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, GeoField, GeoShapeField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis()

geo_schema = (
    GeoField("$.location", as_name="location")
)

geo_index_create_result = r.ft("productidx").create_index(
    geo_schema,
    definition=IndexDefinition(
        prefix=["product:"], index_type=IndexType.JSON
    )
)
print(geo_index_create_result)  # >>> True

prd46885 = {
    "description": "Navy Blue Slippers",
    "price": 45.99,
    "city": "Denver",
    "location": "-104.991531, 39.742043"
}

json_add_result_1 = r.json().set("product:46885", Path.root_path(), prd46885)
print(json_add_result_1)  # >>> True

prd46886 = {
    "description": "Bright Green Socks",
    "price": 25.50,
    "city": "Fort Collins",
    "location": "-105.0618814,40.5150098"
}

json_add_result_2 = r.json().set("product:46886", Path.root_path(), prd46886)
print(json_add_result_2)  # >>> True

geo_result = r.ft("productidx").search(
    "@location:[-104.800644 38.846127 100 mi]"
)
print(geo_result)
# >>> Result{1 total, docs: [Document {'id': 'product:46885'...

geom_schema = (
    TextField("$.name", as_name="name"),
    GeoShapeField(
        "$.geom", as_name="geom", coord_system=GeoShapeField.FLAT
    )
)

geom_index_create_result = r.ft("geomidx").create_index(
    geom_schema,
    definition=IndexDefinition(
        prefix=["shape:"], index_type=IndexType.JSON
    )
)
print(geom_index_create_result)  # True

shape1 = {
    "name": "Green Square",
    "geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
}

gm_json_res_1 = r.json().set("shape:1", Path.root_path(), shape1)
print(gm_json_res_1)  # >>> True

shape2 = {
    "name": "Red Rectangle",
    "geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
}

gm_json_res_2 = r.json().set("shape:2", Path.root_path(), shape2)
print(gm_json_res_2)  # >>> True

shape3 = {
    "name": "Blue Triangle",
    "geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
}

gm_json_res_3 = r.json().set("shape:3", Path.root_path(), shape3)
print(gm_json_res_3)  # >>> True

shape4 = {
    "name": "Purple Point",
    "geom": "POINT (2 2)"
}

gm_json_res_4 = r.json().set("shape:4", Path.root_path(), shape4)
print(gm_json_res_4)  # >>> True

geom_result = r.ft("geomidx").search(
    Query(
        "(-@name:(Green Square) @geom:[WITHIN $qshape])"
    ).dialect(4).paging(0, 1),
    query_params={
        "qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
    }
)
print(geom_result)
# >>> Result{1 total, docs: [Document {'id': 'shape:4'...
```

```java

import org.json.JSONObject;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.Document;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.FTSearchParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.search.SearchResult;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GeoIndexExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] geoSchema = {
            GeoField.of("$.location").as("location")
        };

        String geoIdxCreateResult = jedis.ftCreate("productidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("product:"),
            geoSchema
        );
        
        JSONObject prd46885 = new JSONObject()
                .put("description", "Navy Blue Slippers")
                .put("price", 45.99)
                .put("city", "Denver")
                .put("location", "-104.991531, 39.742043");
        
        String jsonAddResult1 = jedis.jsonSet("product:46885", new Path2("$"), prd46885);
        System.out.println(jsonAddResult1); // >>> OK

        JSONObject prd46886 = new JSONObject()
                .put("description", "Bright Green Socks")
                .put("price", 25.50)
                .put("city", "Fort Collins")
                .put("location", "-105.0618814,40.5150098");
        
        String jsonAddResult2 = jedis.jsonSet("product:46886", new Path2("$"), prd46886);
        System.out.println(jsonAddResult2); // >>> OK

        SearchResult geoResult = jedis.ftSearch("productidx",
            "@location:[-104.800644 38.846127 100 mi]"
        );

        System.out.println(geoResult.getTotalResults()); // >>> 1

        for (Document doc: geoResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> product:46885

        SchemaField[] geomSchema = {
            TextField.of("$.name").as("name"),
            GeoShapeField.of("$.geom", CoordinateSystem.FLAT).as("geom")
        };

        String geomIndexCreateResult = jedis.ftCreate("geomidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("shape"),
            geomSchema
        );
        System.out.println(geomIndexCreateResult); // >>> OK

        JSONObject shape1 = new JSONObject()
                .put("name", "Green Square")
                .put("geom", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))");
        
        String gmJsonRes1 = jedis.jsonSet("shape:1", new Path2("$"), shape1);
        System.out.println(gmJsonRes1); // >>> OK

        JSONObject shape2 = new JSONObject()
                .put("name", "Red Rectangle")
                .put("geom", "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))");
        
        String gmJsonRes2 = jedis.jsonSet("shape:2", new Path2("$"), shape2);
        System.out.println(gmJsonRes2); // >>> OK

        JSONObject shape3 = new JSONObject()
                .put("name", "Blue Triangle")
                .put("geom", "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))");
        
        String gmJsonRes3 = jedis.jsonSet("shape:3", new Path2("$"), shape3);
        System.out.println(gmJsonRes3); // >>> OK

        JSONObject shape4 = new JSONObject()
                .put("name", "Purple Point")
                .put("geom", "POINT (2 2)");
        
        String gmJsonRes4 = jedis.jsonSet("shape:4", new Path2("$"), shape4);
        System.out.println(gmJsonRes4); // >>> OK

        SearchResult geomResult = jedis.ftSearch("geomidx",
            "(-@name:(Green Square) @geom:[WITHIN $qshape])",
            FTSearchParams.searchParams()
                    .addParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .dialect(4)
                    .limit(0, 1)
        );
        System.out.println(geomResult.getTotalResults()); // >>> 1

        for (Document doc: geomResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // shape:4

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

func ExampleClient_geoindex() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	geoCreateResult, err := rdb.FTCreate(ctx,
		"productidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"product:"},
		},
		&redis.FieldSchema{
			FieldName: "$.location",
			As:        "location",
			FieldType: redis.SearchFieldTypeGeo,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoCreateResult) // >>> OK

	prd46885 := map[string]interface{}{
		"description": "Navy Blue Slippers",
		"price":       45.99,
		"city":        "Denver",
		"location":    "-104.991531, 39.742043",
	}

	gjResult1, err := rdb.JSONSet(ctx, "product:46885", "$", prd46885).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult1) // >>> OK

	prd46886 := map[string]interface{}{
		"description": "Bright Green Socks",
		"price":       25.50,
		"city":        "Fort Collins",
		"location":    "-105.0618814,40.5150098",
	}

	gjResult2, err := rdb.JSONSet(ctx, "product:46886", "$", prd46886).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult2) // >>> OK

	geoQueryResult, err := rdb.FTSearch(ctx, "productidx",
		"@location:[-104.800644 38.846127 100 mi]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoQueryResult)
	// >>> {1 [{product:46885...

	geomCreateResult, err := rdb.FTCreate(ctx, "geomidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"shape:"},
		},
		&redis.FieldSchema{
			FieldName: "$.name",
			As:        "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName:         "$.geom",
			As:                "geom",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomCreateResult) // >>> OK

	shape1 := map[string]interface{}{
		"name": "Green Square",
		"geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
	}

	gmjResult1, err := rdb.JSONSet(ctx, "shape:1", "$", shape1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult1) // >>> OK

	shape2 := map[string]interface{}{
		"name": "Red Rectangle",
		"geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))",
	}

	gmjResult2, err := rdb.JSONSet(ctx, "shape:2", "$", shape2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult2) // >>> OK

	shape3 := map[string]interface{}{
		"name": "Blue Triangle",
		"geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))",
	}

	gmjResult3, err := rdb.JSONSet(ctx, "shape:3", "$", shape3).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult3) // >>> OK

	shape4 := map[string]interface{}{
		"name": "Purple Point",
		"geom": "POINT (2 2)",
	}

	gmjResult4, err := rdb.JSONSet(ctx, "shape:4", "$", shape4).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult4) // >>> OK

	geomQueryResult, err := rdb.FTSearchWithArgs(ctx, "geomidx",
		"(-@name:(Green Square) @geom:[WITHIN $qshape])",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
			},
			DialectVersion: 4,
			Limit:          1,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomQueryResult)
	// >>> {1 [{shape:4...

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using StackExchange.Redis;

public class GeoIndexExample
{
    public void run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema geoSchema = new Schema()
            .AddGeoField(new FieldName("$.location", "location"));

        bool geoCreateResult = db.FT().Create(
            "productidx",
            new FTCreateParams()
                .On(IndexDataType.JSON)
                .Prefix("product:"),
            geoSchema
        );
        Console.WriteLine(geoCreateResult); // >>> True

        var product46885 = new
        {
            description = "Navy Blue Slippers",
            price = 45.99,
            city = "Denver",
            location = "-104.991531, 39.742043"
        };

        bool gjAddResult1 = db.JSON().Set("product:46885", "$", product46885);
        Console.WriteLine(gjAddResult1); // >>> True

        var product46886 = new
        {
            description = "Bright Green Socks",
            price = 25.50,
            city = "Fort Collins",
            location = "-105.0618814,40.5150098"
        };

        bool gjAddResult2 = db.JSON().Set("product:46886", "$", product46886);
        Console.WriteLine(gjAddResult2); // >>> True

        SearchResult geoQueryResult = db.FT().Search(
            "productidx",
            new Query("@location:[-104.800644 38.846127 100 mi]")
        );
        Console.WriteLine(geoQueryResult.Documents.Count); // >>> 1

        Console.WriteLine(
            string.Join(", ", geoQueryResult.Documents.Select(x => x["json"]))
        );
        // >>> {"description":"Navy Blue Slippers","price":45.99,"city":"Denver"...

        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            Schema geomSchema = new Schema()
                .AddGeoShapeField(
                    new FieldName("$.geom", "geom"),
                    Schema.GeoShapeField.CoordinateSystem.FLAT
                )
                .AddTextField(new FieldName("$.name", "name"));

            bool geomCreateResult = db.FT().Create(
                "geomidx",
                new FTCreateParams()
                    .On(IndexDataType.JSON)
                    .Prefix("shape:"),
                    geomSchema
            );
            Console.WriteLine(geomCreateResult); // >>> True
        }

        var shape1 = new
        {
            name = "Green Square",
            geom = "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
        };

        bool gmJsonRes1 = db.JSON().Set("shape:1", "$", shape1);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape2 = new
        {
            name = "Red Rectangle",
            geom = "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
        };

        bool gmJsonRes2 = db.JSON().Set("shape:2", "$", shape2);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape3 = new
        {
            name = "Blue Triangle",
            geom = "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
        };

        bool gmJsonRes3 = db.JSON().Set("shape:3", "$", shape3);
        Console.WriteLine(gmJsonRes3); // >>> True

        var shape4 = new
        {
            name = "Purple Point",
            geom = "POINT (2 2)"
        };

        bool gmJsonRes4 = db.JSON().Set("shape:4", "$", shape4);
        Console.WriteLine(gmJsonRes3); // >>> True

        if (version.Major >= 7)
        {
            SearchResult geomQueryResult = db.FT().Search(
                "geomidx",
                new Query("(-@name:(Green Square) @geom:[WITHIN $qshape])")
                    .AddParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .Limit(0, 1)
            );

            Console.WriteLine(geomQueryResult.Documents.Count); // >>> 1
            var res = string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]));

            Console.WriteLine(
                string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]))
            );
            // >>> {"name":"Purple Point","geom":"POINT (2 2)"}
        }
    }
}
```

If you now add JSON objects with the `product:` prefix and a `location` field, they will be added to the index automatically:

```plaintext
> JSON.SET product:46885 $ '{"description": "Navy Blue Slippers","price": 45.99,"city": "Denver","location": "-104.991531, 39.742043"}'
OK
> JSON.SET product:46886 $ '{"description": "Bright Green Socks","price": 25.50,"city": "Fort Collins","location": "-105.0618814,40.5150098"}'
OK
```

```python
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, GeoField, GeoShapeField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis()

geo_schema = (
    GeoField("$.location", as_name="location")
)

geo_index_create_result = r.ft("productidx").create_index(
    geo_schema,
    definition=IndexDefinition(
        prefix=["product:"], index_type=IndexType.JSON
    )
)
print(geo_index_create_result)  # >>> True

prd46885 = {
    "description": "Navy Blue Slippers",
    "price": 45.99,
    "city": "Denver",
    "location": "-104.991531, 39.742043"
}

json_add_result_1 = r.json().set("product:46885", Path.root_path(), prd46885)
print(json_add_result_1)  # >>> True

prd46886 = {
    "description": "Bright Green Socks",
    "price": 25.50,
    "city": "Fort Collins",
    "location": "-105.0618814,40.5150098"
}

json_add_result_2 = r.json().set("product:46886", Path.root_path(), prd46886)
print(json_add_result_2)  # >>> True

geo_result = r.ft("productidx").search(
    "@location:[-104.800644 38.846127 100 mi]"
)
print(geo_result)
# >>> Result{1 total, docs: [Document {'id': 'product:46885'...

geom_schema = (
    TextField("$.name", as_name="name"),
    GeoShapeField(
        "$.geom", as_name="geom", coord_system=GeoShapeField.FLAT
    )
)

geom_index_create_result = r.ft("geomidx").create_index(
    geom_schema,
    definition=IndexDefinition(
        prefix=["shape:"], index_type=IndexType.JSON
    )
)
print(geom_index_create_result)  # True

shape1 = {
    "name": "Green Square",
    "geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
}

gm_json_res_1 = r.json().set("shape:1", Path.root_path(), shape1)
print(gm_json_res_1)  # >>> True

shape2 = {
    "name": "Red Rectangle",
    "geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
}

gm_json_res_2 = r.json().set("shape:2", Path.root_path(), shape2)
print(gm_json_res_2)  # >>> True

shape3 = {
    "name": "Blue Triangle",
    "geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
}

gm_json_res_3 = r.json().set("shape:3", Path.root_path(), shape3)
print(gm_json_res_3)  # >>> True

shape4 = {
    "name": "Purple Point",
    "geom": "POINT (2 2)"
}

gm_json_res_4 = r.json().set("shape:4", Path.root_path(), shape4)
print(gm_json_res_4)  # >>> True

geom_result = r.ft("geomidx").search(
    Query(
        "(-@name:(Green Square) @geom:[WITHIN $qshape])"
    ).dialect(4).paging(0, 1),
    query_params={
        "qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
    }
)
print(geom_result)
# >>> Result{1 total, docs: [Document {'id': 'shape:4'...
```

```java

import org.json.JSONObject;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.Document;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.FTSearchParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.search.SearchResult;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GeoIndexExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] geoSchema = {
            GeoField.of("$.location").as("location")
        };

        String geoIdxCreateResult = jedis.ftCreate("productidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("product:"),
            geoSchema
        );
        
        JSONObject prd46885 = new JSONObject()
                .put("description", "Navy Blue Slippers")
                .put("price", 45.99)
                .put("city", "Denver")
                .put("location", "-104.991531, 39.742043");
        
        String jsonAddResult1 = jedis.jsonSet("product:46885", new Path2("$"), prd46885);
        System.out.println(jsonAddResult1); // >>> OK

        JSONObject prd46886 = new JSONObject()
                .put("description", "Bright Green Socks")
                .put("price", 25.50)
                .put("city", "Fort Collins")
                .put("location", "-105.0618814,40.5150098");
        
        String jsonAddResult2 = jedis.jsonSet("product:46886", new Path2("$"), prd46886);
        System.out.println(jsonAddResult2); // >>> OK

        SearchResult geoResult = jedis.ftSearch("productidx",
            "@location:[-104.800644 38.846127 100 mi]"
        );

        System.out.println(geoResult.getTotalResults()); // >>> 1

        for (Document doc: geoResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> product:46885

        SchemaField[] geomSchema = {
            TextField.of("$.name").as("name"),
            GeoShapeField.of("$.geom", CoordinateSystem.FLAT).as("geom")
        };

        String geomIndexCreateResult = jedis.ftCreate("geomidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("shape"),
            geomSchema
        );
        System.out.println(geomIndexCreateResult); // >>> OK

        JSONObject shape1 = new JSONObject()
                .put("name", "Green Square")
                .put("geom", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))");
        
        String gmJsonRes1 = jedis.jsonSet("shape:1", new Path2("$"), shape1);
        System.out.println(gmJsonRes1); // >>> OK

        JSONObject shape2 = new JSONObject()
                .put("name", "Red Rectangle")
                .put("geom", "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))");
        
        String gmJsonRes2 = jedis.jsonSet("shape:2", new Path2("$"), shape2);
        System.out.println(gmJsonRes2); // >>> OK

        JSONObject shape3 = new JSONObject()
                .put("name", "Blue Triangle")
                .put("geom", "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))");
        
        String gmJsonRes3 = jedis.jsonSet("shape:3", new Path2("$"), shape3);
        System.out.println(gmJsonRes3); // >>> OK

        JSONObject shape4 = new JSONObject()
                .put("name", "Purple Point")
                .put("geom", "POINT (2 2)");
        
        String gmJsonRes4 = jedis.jsonSet("shape:4", new Path2("$"), shape4);
        System.out.println(gmJsonRes4); // >>> OK

        SearchResult geomResult = jedis.ftSearch("geomidx",
            "(-@name:(Green Square) @geom:[WITHIN $qshape])",
            FTSearchParams.searchParams()
                    .addParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .dialect(4)
                    .limit(0, 1)
        );
        System.out.println(geomResult.getTotalResults()); // >>> 1

        for (Document doc: geomResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // shape:4

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

func ExampleClient_geoindex() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	geoCreateResult, err := rdb.FTCreate(ctx,
		"productidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"product:"},
		},
		&redis.FieldSchema{
			FieldName: "$.location",
			As:        "location",
			FieldType: redis.SearchFieldTypeGeo,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoCreateResult) // >>> OK

	prd46885 := map[string]interface{}{
		"description": "Navy Blue Slippers",
		"price":       45.99,
		"city":        "Denver",
		"location":    "-104.991531, 39.742043",
	}

	gjResult1, err := rdb.JSONSet(ctx, "product:46885", "$", prd46885).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult1) // >>> OK

	prd46886 := map[string]interface{}{
		"description": "Bright Green Socks",
		"price":       25.50,
		"city":        "Fort Collins",
		"location":    "-105.0618814,40.5150098",
	}

	gjResult2, err := rdb.JSONSet(ctx, "product:46886", "$", prd46886).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult2) // >>> OK

	geoQueryResult, err := rdb.FTSearch(ctx, "productidx",
		"@location:[-104.800644 38.846127 100 mi]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoQueryResult)
	// >>> {1 [{product:46885...

	geomCreateResult, err := rdb.FTCreate(ctx, "geomidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"shape:"},
		},
		&redis.FieldSchema{
			FieldName: "$.name",
			As:        "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName:         "$.geom",
			As:                "geom",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomCreateResult) // >>> OK

	shape1 := map[string]interface{}{
		"name": "Green Square",
		"geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
	}

	gmjResult1, err := rdb.JSONSet(ctx, "shape:1", "$", shape1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult1) // >>> OK

	shape2 := map[string]interface{}{
		"name": "Red Rectangle",
		"geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))",
	}

	gmjResult2, err := rdb.JSONSet(ctx, "shape:2", "$", shape2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult2) // >>> OK

	shape3 := map[string]interface{}{
		"name": "Blue Triangle",
		"geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))",
	}

	gmjResult3, err := rdb.JSONSet(ctx, "shape:3", "$", shape3).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult3) // >>> OK

	shape4 := map[string]interface{}{
		"name": "Purple Point",
		"geom": "POINT (2 2)",
	}

	gmjResult4, err := rdb.JSONSet(ctx, "shape:4", "$", shape4).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult4) // >>> OK

	geomQueryResult, err := rdb.FTSearchWithArgs(ctx, "geomidx",
		"(-@name:(Green Square) @geom:[WITHIN $qshape])",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
			},
			DialectVersion: 4,
			Limit:          1,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomQueryResult)
	// >>> {1 [{shape:4...

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using StackExchange.Redis;

public class GeoIndexExample
{
    public void run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema geoSchema = new Schema()
            .AddGeoField(new FieldName("$.location", "location"));

        bool geoCreateResult = db.FT().Create(
            "productidx",
            new FTCreateParams()
                .On(IndexDataType.JSON)
                .Prefix("product:"),
            geoSchema
        );
        Console.WriteLine(geoCreateResult); // >>> True

        var product46885 = new
        {
            description = "Navy Blue Slippers",
            price = 45.99,
            city = "Denver",
            location = "-104.991531, 39.742043"
        };

        bool gjAddResult1 = db.JSON().Set("product:46885", "$", product46885);
        Console.WriteLine(gjAddResult1); // >>> True

        var product46886 = new
        {
            description = "Bright Green Socks",
            price = 25.50,
            city = "Fort Collins",
            location = "-105.0618814,40.5150098"
        };

        bool gjAddResult2 = db.JSON().Set("product:46886", "$", product46886);
        Console.WriteLine(gjAddResult2); // >>> True

        SearchResult geoQueryResult = db.FT().Search(
            "productidx",
            new Query("@location:[-104.800644 38.846127 100 mi]")
        );
        Console.WriteLine(geoQueryResult.Documents.Count); // >>> 1

        Console.WriteLine(
            string.Join(", ", geoQueryResult.Documents.Select(x => x["json"]))
        );
        // >>> {"description":"Navy Blue Slippers","price":45.99,"city":"Denver"...

        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            Schema geomSchema = new Schema()
                .AddGeoShapeField(
                    new FieldName("$.geom", "geom"),
                    Schema.GeoShapeField.CoordinateSystem.FLAT
                )
                .AddTextField(new FieldName("$.name", "name"));

            bool geomCreateResult = db.FT().Create(
                "geomidx",
                new FTCreateParams()
                    .On(IndexDataType.JSON)
                    .Prefix("shape:"),
                    geomSchema
            );
            Console.WriteLine(geomCreateResult); // >>> True
        }

        var shape1 = new
        {
            name = "Green Square",
            geom = "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
        };

        bool gmJsonRes1 = db.JSON().Set("shape:1", "$", shape1);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape2 = new
        {
            name = "Red Rectangle",
            geom = "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
        };

        bool gmJsonRes2 = db.JSON().Set("shape:2", "$", shape2);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape3 = new
        {
            name = "Blue Triangle",
            geom = "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
        };

        bool gmJsonRes3 = db.JSON().Set("shape:3", "$", shape3);
        Console.WriteLine(gmJsonRes3); // >>> True

        var shape4 = new
        {
            name = "Purple Point",
            geom = "POINT (2 2)"
        };

        bool gmJsonRes4 = db.JSON().Set("shape:4", "$", shape4);
        Console.WriteLine(gmJsonRes3); // >>> True

        if (version.Major >= 7)
        {
            SearchResult geomQueryResult = db.FT().Search(
                "geomidx",
                new Query("(-@name:(Green Square) @geom:[WITHIN $qshape])")
                    .AddParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .Limit(0, 1)
            );

            Console.WriteLine(geomQueryResult.Documents.Count); // >>> 1
            var res = string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]));

            Console.WriteLine(
                string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]))
            );
            // >>> {"name":"Purple Point","geom":"POINT (2 2)"}
        }
    }
}
```

The query below finds products within a 100 mile radius of Colorado Springs (Longitude=-104.800644, Latitude=38.846127). This returns only the location in Denver, but a radius of 200 miles would also include the location in Fort Collins:

```plaintext
> FT.SEARCH productidx '@location:[-104.800644 38.846127 100 mi]'
1) "1"
2) "product:46885"
3) 1) "$"
   2) "{\"description\":\"Navy Blue Slippers\",\"price\":45.99,\"city\":\"Denver\",\"location\":\"-104.991531, 39.742043\"}"
```

```python
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, GeoField, GeoShapeField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis()

geo_schema = (
    GeoField("$.location", as_name="location")
)

geo_index_create_result = r.ft("productidx").create_index(
    geo_schema,
    definition=IndexDefinition(
        prefix=["product:"], index_type=IndexType.JSON
    )
)
print(geo_index_create_result)  # >>> True

prd46885 = {
    "description": "Navy Blue Slippers",
    "price": 45.99,
    "city": "Denver",
    "location": "-104.991531, 39.742043"
}

json_add_result_1 = r.json().set("product:46885", Path.root_path(), prd46885)
print(json_add_result_1)  # >>> True

prd46886 = {
    "description": "Bright Green Socks",
    "price": 25.50,
    "city": "Fort Collins",
    "location": "-105.0618814,40.5150098"
}

json_add_result_2 = r.json().set("product:46886", Path.root_path(), prd46886)
print(json_add_result_2)  # >>> True

geo_result = r.ft("productidx").search(
    "@location:[-104.800644 38.846127 100 mi]"
)
print(geo_result)
# >>> Result{1 total, docs: [Document {'id': 'product:46885'...

geom_schema = (
    TextField("$.name", as_name="name"),
    GeoShapeField(
        "$.geom", as_name="geom", coord_system=GeoShapeField.FLAT
    )
)

geom_index_create_result = r.ft("geomidx").create_index(
    geom_schema,
    definition=IndexDefinition(
        prefix=["shape:"], index_type=IndexType.JSON
    )
)
print(geom_index_create_result)  # True

shape1 = {
    "name": "Green Square",
    "geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
}

gm_json_res_1 = r.json().set("shape:1", Path.root_path(), shape1)
print(gm_json_res_1)  # >>> True

shape2 = {
    "name": "Red Rectangle",
    "geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
}

gm_json_res_2 = r.json().set("shape:2", Path.root_path(), shape2)
print(gm_json_res_2)  # >>> True

shape3 = {
    "name": "Blue Triangle",
    "geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
}

gm_json_res_3 = r.json().set("shape:3", Path.root_path(), shape3)
print(gm_json_res_3)  # >>> True

shape4 = {
    "name": "Purple Point",
    "geom": "POINT (2 2)"
}

gm_json_res_4 = r.json().set("shape:4", Path.root_path(), shape4)
print(gm_json_res_4)  # >>> True

geom_result = r.ft("geomidx").search(
    Query(
        "(-@name:(Green Square) @geom:[WITHIN $qshape])"
    ).dialect(4).paging(0, 1),
    query_params={
        "qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
    }
)
print(geom_result)
# >>> Result{1 total, docs: [Document {'id': 'shape:4'...
```

```java

import org.json.JSONObject;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.Document;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.FTSearchParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.search.SearchResult;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GeoIndexExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] geoSchema = {
            GeoField.of("$.location").as("location")
        };

        String geoIdxCreateResult = jedis.ftCreate("productidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("product:"),
            geoSchema
        );
        
        JSONObject prd46885 = new JSONObject()
                .put("description", "Navy Blue Slippers")
                .put("price", 45.99)
                .put("city", "Denver")
                .put("location", "-104.991531, 39.742043");
        
        String jsonAddResult1 = jedis.jsonSet("product:46885", new Path2("$"), prd46885);
        System.out.println(jsonAddResult1); // >>> OK

        JSONObject prd46886 = new JSONObject()
                .put("description", "Bright Green Socks")
                .put("price", 25.50)
                .put("city", "Fort Collins")
                .put("location", "-105.0618814,40.5150098");
        
        String jsonAddResult2 = jedis.jsonSet("product:46886", new Path2("$"), prd46886);
        System.out.println(jsonAddResult2); // >>> OK

        SearchResult geoResult = jedis.ftSearch("productidx",
            "@location:[-104.800644 38.846127 100 mi]"
        );

        System.out.println(geoResult.getTotalResults()); // >>> 1

        for (Document doc: geoResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> product:46885

        SchemaField[] geomSchema = {
            TextField.of("$.name").as("name"),
            GeoShapeField.of("$.geom", CoordinateSystem.FLAT).as("geom")
        };

        String geomIndexCreateResult = jedis.ftCreate("geomidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("shape"),
            geomSchema
        );
        System.out.println(geomIndexCreateResult); // >>> OK

        JSONObject shape1 = new JSONObject()
                .put("name", "Green Square")
                .put("geom", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))");
        
        String gmJsonRes1 = jedis.jsonSet("shape:1", new Path2("$"), shape1);
        System.out.println(gmJsonRes1); // >>> OK

        JSONObject shape2 = new JSONObject()
                .put("name", "Red Rectangle")
                .put("geom", "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))");
        
        String gmJsonRes2 = jedis.jsonSet("shape:2", new Path2("$"), shape2);
        System.out.println(gmJsonRes2); // >>> OK

        JSONObject shape3 = new JSONObject()
                .put("name", "Blue Triangle")
                .put("geom", "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))");
        
        String gmJsonRes3 = jedis.jsonSet("shape:3", new Path2("$"), shape3);
        System.out.println(gmJsonRes3); // >>> OK

        JSONObject shape4 = new JSONObject()
                .put("name", "Purple Point")
                .put("geom", "POINT (2 2)");
        
        String gmJsonRes4 = jedis.jsonSet("shape:4", new Path2("$"), shape4);
        System.out.println(gmJsonRes4); // >>> OK

        SearchResult geomResult = jedis.ftSearch("geomidx",
            "(-@name:(Green Square) @geom:[WITHIN $qshape])",
            FTSearchParams.searchParams()
                    .addParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .dialect(4)
                    .limit(0, 1)
        );
        System.out.println(geomResult.getTotalResults()); // >>> 1

        for (Document doc: geomResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // shape:4

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

func ExampleClient_geoindex() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	geoCreateResult, err := rdb.FTCreate(ctx,
		"productidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"product:"},
		},
		&redis.FieldSchema{
			FieldName: "$.location",
			As:        "location",
			FieldType: redis.SearchFieldTypeGeo,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoCreateResult) // >>> OK

	prd46885 := map[string]interface{}{
		"description": "Navy Blue Slippers",
		"price":       45.99,
		"city":        "Denver",
		"location":    "-104.991531, 39.742043",
	}

	gjResult1, err := rdb.JSONSet(ctx, "product:46885", "$", prd46885).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult1) // >>> OK

	prd46886 := map[string]interface{}{
		"description": "Bright Green Socks",
		"price":       25.50,
		"city":        "Fort Collins",
		"location":    "-105.0618814,40.5150098",
	}

	gjResult2, err := rdb.JSONSet(ctx, "product:46886", "$", prd46886).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult2) // >>> OK

	geoQueryResult, err := rdb.FTSearch(ctx, "productidx",
		"@location:[-104.800644 38.846127 100 mi]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoQueryResult)
	// >>> {1 [{product:46885...

	geomCreateResult, err := rdb.FTCreate(ctx, "geomidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"shape:"},
		},
		&redis.FieldSchema{
			FieldName: "$.name",
			As:        "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName:         "$.geom",
			As:                "geom",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomCreateResult) // >>> OK

	shape1 := map[string]interface{}{
		"name": "Green Square",
		"geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
	}

	gmjResult1, err := rdb.JSONSet(ctx, "shape:1", "$", shape1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult1) // >>> OK

	shape2 := map[string]interface{}{
		"name": "Red Rectangle",
		"geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))",
	}

	gmjResult2, err := rdb.JSONSet(ctx, "shape:2", "$", shape2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult2) // >>> OK

	shape3 := map[string]interface{}{
		"name": "Blue Triangle",
		"geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))",
	}

	gmjResult3, err := rdb.JSONSet(ctx, "shape:3", "$", shape3).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult3) // >>> OK

	shape4 := map[string]interface{}{
		"name": "Purple Point",
		"geom": "POINT (2 2)",
	}

	gmjResult4, err := rdb.JSONSet(ctx, "shape:4", "$", shape4).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult4) // >>> OK

	geomQueryResult, err := rdb.FTSearchWithArgs(ctx, "geomidx",
		"(-@name:(Green Square) @geom:[WITHIN $qshape])",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
			},
			DialectVersion: 4,
			Limit:          1,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomQueryResult)
	// >>> {1 [{shape:4...

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using StackExchange.Redis;

public class GeoIndexExample
{
    public void run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema geoSchema = new Schema()
            .AddGeoField(new FieldName("$.location", "location"));

        bool geoCreateResult = db.FT().Create(
            "productidx",
            new FTCreateParams()
                .On(IndexDataType.JSON)
                .Prefix("product:"),
            geoSchema
        );
        Console.WriteLine(geoCreateResult); // >>> True

        var product46885 = new
        {
            description = "Navy Blue Slippers",
            price = 45.99,
            city = "Denver",
            location = "-104.991531, 39.742043"
        };

        bool gjAddResult1 = db.JSON().Set("product:46885", "$", product46885);
        Console.WriteLine(gjAddResult1); // >>> True

        var product46886 = new
        {
            description = "Bright Green Socks",
            price = 25.50,
            city = "Fort Collins",
            location = "-105.0618814,40.5150098"
        };

        bool gjAddResult2 = db.JSON().Set("product:46886", "$", product46886);
        Console.WriteLine(gjAddResult2); // >>> True

        SearchResult geoQueryResult = db.FT().Search(
            "productidx",
            new Query("@location:[-104.800644 38.846127 100 mi]")
        );
        Console.WriteLine(geoQueryResult.Documents.Count); // >>> 1

        Console.WriteLine(
            string.Join(", ", geoQueryResult.Documents.Select(x => x["json"]))
        );
        // >>> {"description":"Navy Blue Slippers","price":45.99,"city":"Denver"...

        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            Schema geomSchema = new Schema()
                .AddGeoShapeField(
                    new FieldName("$.geom", "geom"),
                    Schema.GeoShapeField.CoordinateSystem.FLAT
                )
                .AddTextField(new FieldName("$.name", "name"));

            bool geomCreateResult = db.FT().Create(
                "geomidx",
                new FTCreateParams()
                    .On(IndexDataType.JSON)
                    .Prefix("shape:"),
                    geomSchema
            );
            Console.WriteLine(geomCreateResult); // >>> True
        }

        var shape1 = new
        {
            name = "Green Square",
            geom = "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
        };

        bool gmJsonRes1 = db.JSON().Set("shape:1", "$", shape1);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape2 = new
        {
            name = "Red Rectangle",
            geom = "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
        };

        bool gmJsonRes2 = db.JSON().Set("shape:2", "$", shape2);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape3 = new
        {
            name = "Blue Triangle",
            geom = "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
        };

        bool gmJsonRes3 = db.JSON().Set("shape:3", "$", shape3);
        Console.WriteLine(gmJsonRes3); // >>> True

        var shape4 = new
        {
            name = "Purple Point",
            geom = "POINT (2 2)"
        };

        bool gmJsonRes4 = db.JSON().Set("shape:4", "$", shape4);
        Console.WriteLine(gmJsonRes3); // >>> True

        if (version.Major >= 7)
        {
            SearchResult geomQueryResult = db.FT().Search(
                "geomidx",
                new Query("(-@name:(Green Square) @geom:[WITHIN $qshape])")
                    .AddParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .Limit(0, 1)
            );

            Console.WriteLine(geomQueryResult.Documents.Count); // >>> 1
            var res = string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]));

            Console.WriteLine(
                string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]))
            );
            // >>> {"name":"Purple Point","geom":"POINT (2 2)"}
        }
    }
}
```

See [Geospatial queries](/docs/latest/develop/ai/search-and-query/query/geo-spatial/) for more information about the available options.

## `GEOSHAPE`

The following command creates an index for JSON objects that include geospatial data in a field called `geom`. The `FLAT` option at the end of the field definition specifies Cartesian coordinates instead of the default spherical geographical coordinates. Use `SPHERICAL` in place of `FLAT` to choose the coordinate space explicitly.

```plaintext
> FT.CREATE geomidx ON JSON PREFIX 1 shape: SCHEMA $.name AS name TEXT $.geom AS geom GEOSHAPE FLAT
OK
```

```python
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, GeoField, GeoShapeField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis()

geo_schema = (
    GeoField("$.location", as_name="location")
)

geo_index_create_result = r.ft("productidx").create_index(
    geo_schema,
    definition=IndexDefinition(
        prefix=["product:"], index_type=IndexType.JSON
    )
)
print(geo_index_create_result)  # >>> True

prd46885 = {
    "description": "Navy Blue Slippers",
    "price": 45.99,
    "city": "Denver",
    "location": "-104.991531, 39.742043"
}

json_add_result_1 = r.json().set("product:46885", Path.root_path(), prd46885)
print(json_add_result_1)  # >>> True

prd46886 = {
    "description": "Bright Green Socks",
    "price": 25.50,
    "city": "Fort Collins",
    "location": "-105.0618814,40.5150098"
}

json_add_result_2 = r.json().set("product:46886", Path.root_path(), prd46886)
print(json_add_result_2)  # >>> True

geo_result = r.ft("productidx").search(
    "@location:[-104.800644 38.846127 100 mi]"
)
print(geo_result)
# >>> Result{1 total, docs: [Document {'id': 'product:46885'...

geom_schema = (
    TextField("$.name", as_name="name"),
    GeoShapeField(
        "$.geom", as_name="geom", coord_system=GeoShapeField.FLAT
    )
)

geom_index_create_result = r.ft("geomidx").create_index(
    geom_schema,
    definition=IndexDefinition(
        prefix=["shape:"], index_type=IndexType.JSON
    )
)
print(geom_index_create_result)  # True

shape1 = {
    "name": "Green Square",
    "geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
}

gm_json_res_1 = r.json().set("shape:1", Path.root_path(), shape1)
print(gm_json_res_1)  # >>> True

shape2 = {
    "name": "Red Rectangle",
    "geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
}

gm_json_res_2 = r.json().set("shape:2", Path.root_path(), shape2)
print(gm_json_res_2)  # >>> True

shape3 = {
    "name": "Blue Triangle",
    "geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
}

gm_json_res_3 = r.json().set("shape:3", Path.root_path(), shape3)
print(gm_json_res_3)  # >>> True

shape4 = {
    "name": "Purple Point",
    "geom": "POINT (2 2)"
}

gm_json_res_4 = r.json().set("shape:4", Path.root_path(), shape4)
print(gm_json_res_4)  # >>> True

geom_result = r.ft("geomidx").search(
    Query(
        "(-@name:(Green Square) @geom:[WITHIN $qshape])"
    ).dialect(4).paging(0, 1),
    query_params={
        "qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
    }
)
print(geom_result)
# >>> Result{1 total, docs: [Document {'id': 'shape:4'...
```

```java

import org.json.JSONObject;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.Document;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.FTSearchParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.search.SearchResult;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GeoIndexExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] geoSchema = {
            GeoField.of("$.location").as("location")
        };

        String geoIdxCreateResult = jedis.ftCreate("productidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("product:"),
            geoSchema
        );
        
        JSONObject prd46885 = new JSONObject()
                .put("description", "Navy Blue Slippers")
                .put("price", 45.99)
                .put("city", "Denver")
                .put("location", "-104.991531, 39.742043");
        
        String jsonAddResult1 = jedis.jsonSet("product:46885", new Path2("$"), prd46885);
        System.out.println(jsonAddResult1); // >>> OK

        JSONObject prd46886 = new JSONObject()
                .put("description", "Bright Green Socks")
                .put("price", 25.50)
                .put("city", "Fort Collins")
                .put("location", "-105.0618814,40.5150098");
        
        String jsonAddResult2 = jedis.jsonSet("product:46886", new Path2("$"), prd46886);
        System.out.println(jsonAddResult2); // >>> OK

        SearchResult geoResult = jedis.ftSearch("productidx",
            "@location:[-104.800644 38.846127 100 mi]"
        );

        System.out.println(geoResult.getTotalResults()); // >>> 1

        for (Document doc: geoResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> product:46885

        SchemaField[] geomSchema = {
            TextField.of("$.name").as("name"),
            GeoShapeField.of("$.geom", CoordinateSystem.FLAT).as("geom")
        };

        String geomIndexCreateResult = jedis.ftCreate("geomidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("shape"),
            geomSchema
        );
        System.out.println(geomIndexCreateResult); // >>> OK

        JSONObject shape1 = new JSONObject()
                .put("name", "Green Square")
                .put("geom", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))");
        
        String gmJsonRes1 = jedis.jsonSet("shape:1", new Path2("$"), shape1);
        System.out.println(gmJsonRes1); // >>> OK

        JSONObject shape2 = new JSONObject()
                .put("name", "Red Rectangle")
                .put("geom", "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))");
        
        String gmJsonRes2 = jedis.jsonSet("shape:2", new Path2("$"), shape2);
        System.out.println(gmJsonRes2); // >>> OK

        JSONObject shape3 = new JSONObject()
                .put("name", "Blue Triangle")
                .put("geom", "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))");
        
        String gmJsonRes3 = jedis.jsonSet("shape:3", new Path2("$"), shape3);
        System.out.println(gmJsonRes3); // >>> OK

        JSONObject shape4 = new JSONObject()
                .put("name", "Purple Point")
                .put("geom", "POINT (2 2)");
        
        String gmJsonRes4 = jedis.jsonSet("shape:4", new Path2("$"), shape4);
        System.out.println(gmJsonRes4); // >>> OK

        SearchResult geomResult = jedis.ftSearch("geomidx",
            "(-@name:(Green Square) @geom:[WITHIN $qshape])",
            FTSearchParams.searchParams()
                    .addParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .dialect(4)
                    .limit(0, 1)
        );
        System.out.println(geomResult.getTotalResults()); // >>> 1

        for (Document doc: geomResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // shape:4

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

func ExampleClient_geoindex() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	geoCreateResult, err := rdb.FTCreate(ctx,
		"productidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"product:"},
		},
		&redis.FieldSchema{
			FieldName: "$.location",
			As:        "location",
			FieldType: redis.SearchFieldTypeGeo,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoCreateResult) // >>> OK

	prd46885 := map[string]interface{}{
		"description": "Navy Blue Slippers",
		"price":       45.99,
		"city":        "Denver",
		"location":    "-104.991531, 39.742043",
	}

	gjResult1, err := rdb.JSONSet(ctx, "product:46885", "$", prd46885).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult1) // >>> OK

	prd46886 := map[string]interface{}{
		"description": "Bright Green Socks",
		"price":       25.50,
		"city":        "Fort Collins",
		"location":    "-105.0618814,40.5150098",
	}

	gjResult2, err := rdb.JSONSet(ctx, "product:46886", "$", prd46886).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult2) // >>> OK

	geoQueryResult, err := rdb.FTSearch(ctx, "productidx",
		"@location:[-104.800644 38.846127 100 mi]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoQueryResult)
	// >>> {1 [{product:46885...

	geomCreateResult, err := rdb.FTCreate(ctx, "geomidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"shape:"},
		},
		&redis.FieldSchema{
			FieldName: "$.name",
			As:        "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName:         "$.geom",
			As:                "geom",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomCreateResult) // >>> OK

	shape1 := map[string]interface{}{
		"name": "Green Square",
		"geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
	}

	gmjResult1, err := rdb.JSONSet(ctx, "shape:1", "$", shape1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult1) // >>> OK

	shape2 := map[string]interface{}{
		"name": "Red Rectangle",
		"geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))",
	}

	gmjResult2, err := rdb.JSONSet(ctx, "shape:2", "$", shape2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult2) // >>> OK

	shape3 := map[string]interface{}{
		"name": "Blue Triangle",
		"geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))",
	}

	gmjResult3, err := rdb.JSONSet(ctx, "shape:3", "$", shape3).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult3) // >>> OK

	shape4 := map[string]interface{}{
		"name": "Purple Point",
		"geom": "POINT (2 2)",
	}

	gmjResult4, err := rdb.JSONSet(ctx, "shape:4", "$", shape4).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult4) // >>> OK

	geomQueryResult, err := rdb.FTSearchWithArgs(ctx, "geomidx",
		"(-@name:(Green Square) @geom:[WITHIN $qshape])",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
			},
			DialectVersion: 4,
			Limit:          1,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomQueryResult)
	// >>> {1 [{shape:4...

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using StackExchange.Redis;

public class GeoIndexExample
{
    public void run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema geoSchema = new Schema()
            .AddGeoField(new FieldName("$.location", "location"));

        bool geoCreateResult = db.FT().Create(
            "productidx",
            new FTCreateParams()
                .On(IndexDataType.JSON)
                .Prefix("product:"),
            geoSchema
        );
        Console.WriteLine(geoCreateResult); // >>> True

        var product46885 = new
        {
            description = "Navy Blue Slippers",
            price = 45.99,
            city = "Denver",
            location = "-104.991531, 39.742043"
        };

        bool gjAddResult1 = db.JSON().Set("product:46885", "$", product46885);
        Console.WriteLine(gjAddResult1); // >>> True

        var product46886 = new
        {
            description = "Bright Green Socks",
            price = 25.50,
            city = "Fort Collins",
            location = "-105.0618814,40.5150098"
        };

        bool gjAddResult2 = db.JSON().Set("product:46886", "$", product46886);
        Console.WriteLine(gjAddResult2); // >>> True

        SearchResult geoQueryResult = db.FT().Search(
            "productidx",
            new Query("@location:[-104.800644 38.846127 100 mi]")
        );
        Console.WriteLine(geoQueryResult.Documents.Count); // >>> 1

        Console.WriteLine(
            string.Join(", ", geoQueryResult.Documents.Select(x => x["json"]))
        );
        // >>> {"description":"Navy Blue Slippers","price":45.99,"city":"Denver"...

        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            Schema geomSchema = new Schema()
                .AddGeoShapeField(
                    new FieldName("$.geom", "geom"),
                    Schema.GeoShapeField.CoordinateSystem.FLAT
                )
                .AddTextField(new FieldName("$.name", "name"));

            bool geomCreateResult = db.FT().Create(
                "geomidx",
                new FTCreateParams()
                    .On(IndexDataType.JSON)
                    .Prefix("shape:"),
                    geomSchema
            );
            Console.WriteLine(geomCreateResult); // >>> True
        }

        var shape1 = new
        {
            name = "Green Square",
            geom = "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
        };

        bool gmJsonRes1 = db.JSON().Set("shape:1", "$", shape1);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape2 = new
        {
            name = "Red Rectangle",
            geom = "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
        };

        bool gmJsonRes2 = db.JSON().Set("shape:2", "$", shape2);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape3 = new
        {
            name = "Blue Triangle",
            geom = "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
        };

        bool gmJsonRes3 = db.JSON().Set("shape:3", "$", shape3);
        Console.WriteLine(gmJsonRes3); // >>> True

        var shape4 = new
        {
            name = "Purple Point",
            geom = "POINT (2 2)"
        };

        bool gmJsonRes4 = db.JSON().Set("shape:4", "$", shape4);
        Console.WriteLine(gmJsonRes3); // >>> True

        if (version.Major >= 7)
        {
            SearchResult geomQueryResult = db.FT().Search(
                "geomidx",
                new Query("(-@name:(Green Square) @geom:[WITHIN $qshape])")
                    .AddParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .Limit(0, 1)
            );

            Console.WriteLine(geomQueryResult.Documents.Count); // >>> 1
            var res = string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]));

            Console.WriteLine(
                string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]))
            );
            // >>> {"name":"Purple Point","geom":"POINT (2 2)"}
        }
    }
}
```

Use the `shape:` prefix for the JSON objects to add them to the index:

```plaintext
> JSON.SET shape:1 $ '{"name": "Green Square", "geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"}'
OK
> JSON.SET shape:2 $ '{"name": "Red Rectangle", "geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"}'
OK
> JSON.SET shape:3 $ '{"name": "Blue Triangle", "geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"}'
OK
> JSON.SET shape:4 $ '{"name": "Purple Point", "geom": "POINT (2 2)"}'
OK
```

```python
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, GeoField, GeoShapeField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis()

geo_schema = (
    GeoField("$.location", as_name="location")
)

geo_index_create_result = r.ft("productidx").create_index(
    geo_schema,
    definition=IndexDefinition(
        prefix=["product:"], index_type=IndexType.JSON
    )
)
print(geo_index_create_result)  # >>> True

prd46885 = {
    "description": "Navy Blue Slippers",
    "price": 45.99,
    "city": "Denver",
    "location": "-104.991531, 39.742043"
}

json_add_result_1 = r.json().set("product:46885", Path.root_path(), prd46885)
print(json_add_result_1)  # >>> True

prd46886 = {
    "description": "Bright Green Socks",
    "price": 25.50,
    "city": "Fort Collins",
    "location": "-105.0618814,40.5150098"
}

json_add_result_2 = r.json().set("product:46886", Path.root_path(), prd46886)
print(json_add_result_2)  # >>> True

geo_result = r.ft("productidx").search(
    "@location:[-104.800644 38.846127 100 mi]"
)
print(geo_result)
# >>> Result{1 total, docs: [Document {'id': 'product:46885'...

geom_schema = (
    TextField("$.name", as_name="name"),
    GeoShapeField(
        "$.geom", as_name="geom", coord_system=GeoShapeField.FLAT
    )
)

geom_index_create_result = r.ft("geomidx").create_index(
    geom_schema,
    definition=IndexDefinition(
        prefix=["shape:"], index_type=IndexType.JSON
    )
)
print(geom_index_create_result)  # True

shape1 = {
    "name": "Green Square",
    "geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
}

gm_json_res_1 = r.json().set("shape:1", Path.root_path(), shape1)
print(gm_json_res_1)  # >>> True

shape2 = {
    "name": "Red Rectangle",
    "geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
}

gm_json_res_2 = r.json().set("shape:2", Path.root_path(), shape2)
print(gm_json_res_2)  # >>> True

shape3 = {
    "name": "Blue Triangle",
    "geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
}

gm_json_res_3 = r.json().set("shape:3", Path.root_path(), shape3)
print(gm_json_res_3)  # >>> True

shape4 = {
    "name": "Purple Point",
    "geom": "POINT (2 2)"
}

gm_json_res_4 = r.json().set("shape:4", Path.root_path(), shape4)
print(gm_json_res_4)  # >>> True

geom_result = r.ft("geomidx").search(
    Query(
        "(-@name:(Green Square) @geom:[WITHIN $qshape])"
    ).dialect(4).paging(0, 1),
    query_params={
        "qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
    }
)
print(geom_result)
# >>> Result{1 total, docs: [Document {'id': 'shape:4'...
```

```java

import org.json.JSONObject;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.Document;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.FTSearchParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.search.SearchResult;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GeoIndexExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] geoSchema = {
            GeoField.of("$.location").as("location")
        };

        String geoIdxCreateResult = jedis.ftCreate("productidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("product:"),
            geoSchema
        );
        
        JSONObject prd46885 = new JSONObject()
                .put("description", "Navy Blue Slippers")
                .put("price", 45.99)
                .put("city", "Denver")
                .put("location", "-104.991531, 39.742043");
        
        String jsonAddResult1 = jedis.jsonSet("product:46885", new Path2("$"), prd46885);
        System.out.println(jsonAddResult1); // >>> OK

        JSONObject prd46886 = new JSONObject()
                .put("description", "Bright Green Socks")
                .put("price", 25.50)
                .put("city", "Fort Collins")
                .put("location", "-105.0618814,40.5150098");
        
        String jsonAddResult2 = jedis.jsonSet("product:46886", new Path2("$"), prd46886);
        System.out.println(jsonAddResult2); // >>> OK

        SearchResult geoResult = jedis.ftSearch("productidx",
            "@location:[-104.800644 38.846127 100 mi]"
        );

        System.out.println(geoResult.getTotalResults()); // >>> 1

        for (Document doc: geoResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> product:46885

        SchemaField[] geomSchema = {
            TextField.of("$.name").as("name"),
            GeoShapeField.of("$.geom", CoordinateSystem.FLAT).as("geom")
        };

        String geomIndexCreateResult = jedis.ftCreate("geomidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("shape"),
            geomSchema
        );
        System.out.println(geomIndexCreateResult); // >>> OK

        JSONObject shape1 = new JSONObject()
                .put("name", "Green Square")
                .put("geom", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))");
        
        String gmJsonRes1 = jedis.jsonSet("shape:1", new Path2("$"), shape1);
        System.out.println(gmJsonRes1); // >>> OK

        JSONObject shape2 = new JSONObject()
                .put("name", "Red Rectangle")
                .put("geom", "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))");
        
        String gmJsonRes2 = jedis.jsonSet("shape:2", new Path2("$"), shape2);
        System.out.println(gmJsonRes2); // >>> OK

        JSONObject shape3 = new JSONObject()
                .put("name", "Blue Triangle")
                .put("geom", "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))");
        
        String gmJsonRes3 = jedis.jsonSet("shape:3", new Path2("$"), shape3);
        System.out.println(gmJsonRes3); // >>> OK

        JSONObject shape4 = new JSONObject()
                .put("name", "Purple Point")
                .put("geom", "POINT (2 2)");
        
        String gmJsonRes4 = jedis.jsonSet("shape:4", new Path2("$"), shape4);
        System.out.println(gmJsonRes4); // >>> OK

        SearchResult geomResult = jedis.ftSearch("geomidx",
            "(-@name:(Green Square) @geom:[WITHIN $qshape])",
            FTSearchParams.searchParams()
                    .addParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .dialect(4)
                    .limit(0, 1)
        );
        System.out.println(geomResult.getTotalResults()); // >>> 1

        for (Document doc: geomResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // shape:4

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

func ExampleClient_geoindex() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	geoCreateResult, err := rdb.FTCreate(ctx,
		"productidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"product:"},
		},
		&redis.FieldSchema{
			FieldName: "$.location",
			As:        "location",
			FieldType: redis.SearchFieldTypeGeo,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoCreateResult) // >>> OK

	prd46885 := map[string]interface{}{
		"description": "Navy Blue Slippers",
		"price":       45.99,
		"city":        "Denver",
		"location":    "-104.991531, 39.742043",
	}

	gjResult1, err := rdb.JSONSet(ctx, "product:46885", "$", prd46885).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult1) // >>> OK

	prd46886 := map[string]interface{}{
		"description": "Bright Green Socks",
		"price":       25.50,
		"city":        "Fort Collins",
		"location":    "-105.0618814,40.5150098",
	}

	gjResult2, err := rdb.JSONSet(ctx, "product:46886", "$", prd46886).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult2) // >>> OK

	geoQueryResult, err := rdb.FTSearch(ctx, "productidx",
		"@location:[-104.800644 38.846127 100 mi]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoQueryResult)
	// >>> {1 [{product:46885...

	geomCreateResult, err := rdb.FTCreate(ctx, "geomidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"shape:"},
		},
		&redis.FieldSchema{
			FieldName: "$.name",
			As:        "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName:         "$.geom",
			As:                "geom",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomCreateResult) // >>> OK

	shape1 := map[string]interface{}{
		"name": "Green Square",
		"geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
	}

	gmjResult1, err := rdb.JSONSet(ctx, "shape:1", "$", shape1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult1) // >>> OK

	shape2 := map[string]interface{}{
		"name": "Red Rectangle",
		"geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))",
	}

	gmjResult2, err := rdb.JSONSet(ctx, "shape:2", "$", shape2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult2) // >>> OK

	shape3 := map[string]interface{}{
		"name": "Blue Triangle",
		"geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))",
	}

	gmjResult3, err := rdb.JSONSet(ctx, "shape:3", "$", shape3).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult3) // >>> OK

	shape4 := map[string]interface{}{
		"name": "Purple Point",
		"geom": "POINT (2 2)",
	}

	gmjResult4, err := rdb.JSONSet(ctx, "shape:4", "$", shape4).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult4) // >>> OK

	geomQueryResult, err := rdb.FTSearchWithArgs(ctx, "geomidx",
		"(-@name:(Green Square) @geom:[WITHIN $qshape])",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
			},
			DialectVersion: 4,
			Limit:          1,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomQueryResult)
	// >>> {1 [{shape:4...

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using StackExchange.Redis;

public class GeoIndexExample
{
    public void run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema geoSchema = new Schema()
            .AddGeoField(new FieldName("$.location", "location"));

        bool geoCreateResult = db.FT().Create(
            "productidx",
            new FTCreateParams()
                .On(IndexDataType.JSON)
                .Prefix("product:"),
            geoSchema
        );
        Console.WriteLine(geoCreateResult); // >>> True

        var product46885 = new
        {
            description = "Navy Blue Slippers",
            price = 45.99,
            city = "Denver",
            location = "-104.991531, 39.742043"
        };

        bool gjAddResult1 = db.JSON().Set("product:46885", "$", product46885);
        Console.WriteLine(gjAddResult1); // >>> True

        var product46886 = new
        {
            description = "Bright Green Socks",
            price = 25.50,
            city = "Fort Collins",
            location = "-105.0618814,40.5150098"
        };

        bool gjAddResult2 = db.JSON().Set("product:46886", "$", product46886);
        Console.WriteLine(gjAddResult2); // >>> True

        SearchResult geoQueryResult = db.FT().Search(
            "productidx",
            new Query("@location:[-104.800644 38.846127 100 mi]")
        );
        Console.WriteLine(geoQueryResult.Documents.Count); // >>> 1

        Console.WriteLine(
            string.Join(", ", geoQueryResult.Documents.Select(x => x["json"]))
        );
        // >>> {"description":"Navy Blue Slippers","price":45.99,"city":"Denver"...

        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            Schema geomSchema = new Schema()
                .AddGeoShapeField(
                    new FieldName("$.geom", "geom"),
                    Schema.GeoShapeField.CoordinateSystem.FLAT
                )
                .AddTextField(new FieldName("$.name", "name"));

            bool geomCreateResult = db.FT().Create(
                "geomidx",
                new FTCreateParams()
                    .On(IndexDataType.JSON)
                    .Prefix("shape:"),
                    geomSchema
            );
            Console.WriteLine(geomCreateResult); // >>> True
        }

        var shape1 = new
        {
            name = "Green Square",
            geom = "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
        };

        bool gmJsonRes1 = db.JSON().Set("shape:1", "$", shape1);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape2 = new
        {
            name = "Red Rectangle",
            geom = "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
        };

        bool gmJsonRes2 = db.JSON().Set("shape:2", "$", shape2);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape3 = new
        {
            name = "Blue Triangle",
            geom = "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
        };

        bool gmJsonRes3 = db.JSON().Set("shape:3", "$", shape3);
        Console.WriteLine(gmJsonRes3); // >>> True

        var shape4 = new
        {
            name = "Purple Point",
            geom = "POINT (2 2)"
        };

        bool gmJsonRes4 = db.JSON().Set("shape:4", "$", shape4);
        Console.WriteLine(gmJsonRes3); // >>> True

        if (version.Major >= 7)
        {
            SearchResult geomQueryResult = db.FT().Search(
                "geomidx",
                new Query("(-@name:(Green Square) @geom:[WITHIN $qshape])")
                    .AddParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .Limit(0, 1)
            );

            Console.WriteLine(geomQueryResult.Documents.Count); // >>> 1
            var res = string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]));

            Console.WriteLine(
                string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]))
            );
            // >>> {"name":"Purple Point","geom":"POINT (2 2)"}
        }
    }
}
```

You can now run various geospatial queries against the index. For example, the query below returns any shapes within the boundary of the green square but omits the green square itself:

```plaintext
> FT.SEARCH geomidx "(-@name:(Green Square) @geom:[WITHIN $qshape])" PARAMS 2 qshape "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))" RETURN 1 name DIALECT 2

1) (integer) 1
2) "shape:4"
3) 1) "name"
   2) "[\"Purple Point\"]"
```

```python
import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, GeoField, GeoShapeField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

r = redis.Redis()

geo_schema = (
    GeoField("$.location", as_name="location")
)

geo_index_create_result = r.ft("productidx").create_index(
    geo_schema,
    definition=IndexDefinition(
        prefix=["product:"], index_type=IndexType.JSON
    )
)
print(geo_index_create_result)  # >>> True

prd46885 = {
    "description": "Navy Blue Slippers",
    "price": 45.99,
    "city": "Denver",
    "location": "-104.991531, 39.742043"
}

json_add_result_1 = r.json().set("product:46885", Path.root_path(), prd46885)
print(json_add_result_1)  # >>> True

prd46886 = {
    "description": "Bright Green Socks",
    "price": 25.50,
    "city": "Fort Collins",
    "location": "-105.0618814,40.5150098"
}

json_add_result_2 = r.json().set("product:46886", Path.root_path(), prd46886)
print(json_add_result_2)  # >>> True

geo_result = r.ft("productidx").search(
    "@location:[-104.800644 38.846127 100 mi]"
)
print(geo_result)
# >>> Result{1 total, docs: [Document {'id': 'product:46885'...

geom_schema = (
    TextField("$.name", as_name="name"),
    GeoShapeField(
        "$.geom", as_name="geom", coord_system=GeoShapeField.FLAT
    )
)

geom_index_create_result = r.ft("geomidx").create_index(
    geom_schema,
    definition=IndexDefinition(
        prefix=["shape:"], index_type=IndexType.JSON
    )
)
print(geom_index_create_result)  # True

shape1 = {
    "name": "Green Square",
    "geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
}

gm_json_res_1 = r.json().set("shape:1", Path.root_path(), shape1)
print(gm_json_res_1)  # >>> True

shape2 = {
    "name": "Red Rectangle",
    "geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
}

gm_json_res_2 = r.json().set("shape:2", Path.root_path(), shape2)
print(gm_json_res_2)  # >>> True

shape3 = {
    "name": "Blue Triangle",
    "geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
}

gm_json_res_3 = r.json().set("shape:3", Path.root_path(), shape3)
print(gm_json_res_3)  # >>> True

shape4 = {
    "name": "Purple Point",
    "geom": "POINT (2 2)"
}

gm_json_res_4 = r.json().set("shape:4", Path.root_path(), shape4)
print(gm_json_res_4)  # >>> True

geom_result = r.ft("geomidx").search(
    Query(
        "(-@name:(Green Square) @geom:[WITHIN $qshape])"
    ).dialect(4).paging(0, 1),
    query_params={
        "qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
    }
)
print(geom_result)
# >>> Result{1 total, docs: [Document {'id': 'shape:4'...
```

```java

import org.json.JSONObject;

import redis.clients.jedis.RedisClient;
import redis.clients.jedis.json.Path2;
import redis.clients.jedis.search.Document;
import redis.clients.jedis.search.FTCreateParams;
import redis.clients.jedis.search.FTSearchParams;
import redis.clients.jedis.search.IndexDataType;
import redis.clients.jedis.search.schemafields.*;
import redis.clients.jedis.search.schemafields.GeoShapeField.CoordinateSystem;
import redis.clients.jedis.search.SearchResult;
import redis.clients.jedis.exceptions.JedisDataException;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GeoIndexExample {

    public void run() {
        RedisClient jedis = RedisClient.create("redis://localhost:6379");

        SchemaField[] geoSchema = {
            GeoField.of("$.location").as("location")
        };

        String geoIdxCreateResult = jedis.ftCreate("productidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("product:"),
            geoSchema
        );
        
        JSONObject prd46885 = new JSONObject()
                .put("description", "Navy Blue Slippers")
                .put("price", 45.99)
                .put("city", "Denver")
                .put("location", "-104.991531, 39.742043");
        
        String jsonAddResult1 = jedis.jsonSet("product:46885", new Path2("$"), prd46885);
        System.out.println(jsonAddResult1); // >>> OK

        JSONObject prd46886 = new JSONObject()
                .put("description", "Bright Green Socks")
                .put("price", 25.50)
                .put("city", "Fort Collins")
                .put("location", "-105.0618814,40.5150098");
        
        String jsonAddResult2 = jedis.jsonSet("product:46886", new Path2("$"), prd46886);
        System.out.println(jsonAddResult2); // >>> OK

        SearchResult geoResult = jedis.ftSearch("productidx",
            "@location:[-104.800644 38.846127 100 mi]"
        );

        System.out.println(geoResult.getTotalResults()); // >>> 1

        for (Document doc: geoResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // >>> product:46885

        SchemaField[] geomSchema = {
            TextField.of("$.name").as("name"),
            GeoShapeField.of("$.geom", CoordinateSystem.FLAT).as("geom")
        };

        String geomIndexCreateResult = jedis.ftCreate("geomidx",
            FTCreateParams.createParams()
                    .on(IndexDataType.JSON)
                    .addPrefix("shape"),
            geomSchema
        );
        System.out.println(geomIndexCreateResult); // >>> OK

        JSONObject shape1 = new JSONObject()
                .put("name", "Green Square")
                .put("geom", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))");
        
        String gmJsonRes1 = jedis.jsonSet("shape:1", new Path2("$"), shape1);
        System.out.println(gmJsonRes1); // >>> OK

        JSONObject shape2 = new JSONObject()
                .put("name", "Red Rectangle")
                .put("geom", "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))");
        
        String gmJsonRes2 = jedis.jsonSet("shape:2", new Path2("$"), shape2);
        System.out.println(gmJsonRes2); // >>> OK

        JSONObject shape3 = new JSONObject()
                .put("name", "Blue Triangle")
                .put("geom", "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))");
        
        String gmJsonRes3 = jedis.jsonSet("shape:3", new Path2("$"), shape3);
        System.out.println(gmJsonRes3); // >>> OK

        JSONObject shape4 = new JSONObject()
                .put("name", "Purple Point")
                .put("geom", "POINT (2 2)");
        
        String gmJsonRes4 = jedis.jsonSet("shape:4", new Path2("$"), shape4);
        System.out.println(gmJsonRes4); // >>> OK

        SearchResult geomResult = jedis.ftSearch("geomidx",
            "(-@name:(Green Square) @geom:[WITHIN $qshape])",
            FTSearchParams.searchParams()
                    .addParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .dialect(4)
                    .limit(0, 1)
        );
        System.out.println(geomResult.getTotalResults()); // >>> 1

        for (Document doc: geomResult.getDocuments()) {
            System.out.println(doc.getId());
        }
        // shape:4

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

func ExampleClient_geoindex() {
	ctx := context.Background()

	rdb := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password docs
		DB:       0,  // use default DB
		Protocol: 2,
	})

	geoCreateResult, err := rdb.FTCreate(ctx,
		"productidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"product:"},
		},
		&redis.FieldSchema{
			FieldName: "$.location",
			As:        "location",
			FieldType: redis.SearchFieldTypeGeo,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoCreateResult) // >>> OK

	prd46885 := map[string]interface{}{
		"description": "Navy Blue Slippers",
		"price":       45.99,
		"city":        "Denver",
		"location":    "-104.991531, 39.742043",
	}

	gjResult1, err := rdb.JSONSet(ctx, "product:46885", "$", prd46885).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult1) // >>> OK

	prd46886 := map[string]interface{}{
		"description": "Bright Green Socks",
		"price":       25.50,
		"city":        "Fort Collins",
		"location":    "-105.0618814,40.5150098",
	}

	gjResult2, err := rdb.JSONSet(ctx, "product:46886", "$", prd46886).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gjResult2) // >>> OK

	geoQueryResult, err := rdb.FTSearch(ctx, "productidx",
		"@location:[-104.800644 38.846127 100 mi]",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geoQueryResult)
	// >>> {1 [{product:46885...

	geomCreateResult, err := rdb.FTCreate(ctx, "geomidx",
		&redis.FTCreateOptions{
			OnJSON: true,
			Prefix: []interface{}{"shape:"},
		},
		&redis.FieldSchema{
			FieldName: "$.name",
			As:        "name",
			FieldType: redis.SearchFieldTypeText,
		},
		&redis.FieldSchema{
			FieldName:         "$.geom",
			As:                "geom",
			FieldType:         redis.SearchFieldTypeGeoShape,
			GeoShapeFieldType: "FLAT",
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomCreateResult) // >>> OK

	shape1 := map[string]interface{}{
		"name": "Green Square",
		"geom": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
	}

	gmjResult1, err := rdb.JSONSet(ctx, "shape:1", "$", shape1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult1) // >>> OK

	shape2 := map[string]interface{}{
		"name": "Red Rectangle",
		"geom": "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))",
	}

	gmjResult2, err := rdb.JSONSet(ctx, "shape:2", "$", shape2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult2) // >>> OK

	shape3 := map[string]interface{}{
		"name": "Blue Triangle",
		"geom": "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))",
	}

	gmjResult3, err := rdb.JSONSet(ctx, "shape:3", "$", shape3).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult3) // >>> OK

	shape4 := map[string]interface{}{
		"name": "Purple Point",
		"geom": "POINT (2 2)",
	}

	gmjResult4, err := rdb.JSONSet(ctx, "shape:4", "$", shape4).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(gmjResult4) // >>> OK

	geomQueryResult, err := rdb.FTSearchWithArgs(ctx, "geomidx",
		"(-@name:(Green Square) @geom:[WITHIN $qshape])",
		&redis.FTSearchOptions{
			Params: map[string]interface{}{
				"qshape": "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))",
			},
			DialectVersion: 4,
			Limit:          1,
		},
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(geomQueryResult)
	// >>> {1 [{shape:4...

}
```

```c#

using NRedisStack.RedisStackCommands;
using NRedisStack.Search;
using NRedisStack.Search.Literals.Enums;
using StackExchange.Redis;

public class GeoIndexExample
{
    public void run()
    {
        var muxer = ConnectionMultiplexer.Connect("localhost:6379");
        var db = muxer.GetDatabase();

        Schema geoSchema = new Schema()
            .AddGeoField(new FieldName("$.location", "location"));

        bool geoCreateResult = db.FT().Create(
            "productidx",
            new FTCreateParams()
                .On(IndexDataType.JSON)
                .Prefix("product:"),
            geoSchema
        );
        Console.WriteLine(geoCreateResult); // >>> True

        var product46885 = new
        {
            description = "Navy Blue Slippers",
            price = 45.99,
            city = "Denver",
            location = "-104.991531, 39.742043"
        };

        bool gjAddResult1 = db.JSON().Set("product:46885", "$", product46885);
        Console.WriteLine(gjAddResult1); // >>> True

        var product46886 = new
        {
            description = "Bright Green Socks",
            price = 25.50,
            city = "Fort Collins",
            location = "-105.0618814,40.5150098"
        };

        bool gjAddResult2 = db.JSON().Set("product:46886", "$", product46886);
        Console.WriteLine(gjAddResult2); // >>> True

        SearchResult geoQueryResult = db.FT().Search(
            "productidx",
            new Query("@location:[-104.800644 38.846127 100 mi]")
        );
        Console.WriteLine(geoQueryResult.Documents.Count); // >>> 1

        Console.WriteLine(
            string.Join(", ", geoQueryResult.Documents.Select(x => x["json"]))
        );
        // >>> {"description":"Navy Blue Slippers","price":45.99,"city":"Denver"...

        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            Schema geomSchema = new Schema()
                .AddGeoShapeField(
                    new FieldName("$.geom", "geom"),
                    Schema.GeoShapeField.CoordinateSystem.FLAT
                )
                .AddTextField(new FieldName("$.name", "name"));

            bool geomCreateResult = db.FT().Create(
                "geomidx",
                new FTCreateParams()
                    .On(IndexDataType.JSON)
                    .Prefix("shape:"),
                    geomSchema
            );
            Console.WriteLine(geomCreateResult); // >>> True
        }

        var shape1 = new
        {
            name = "Green Square",
            geom = "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))"
        };

        bool gmJsonRes1 = db.JSON().Set("shape:1", "$", shape1);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape2 = new
        {
            name = "Red Rectangle",
            geom = "POLYGON ((2 2.5, 2 3.5, 3.5 3.5, 3.5 2.5, 2 2.5))"
        };

        bool gmJsonRes2 = db.JSON().Set("shape:2", "$", shape2);
        Console.WriteLine(gmJsonRes1); // >>> True

        var shape3 = new
        {
            name = "Blue Triangle",
            geom = "POLYGON ((3.5 1, 3.75 2, 4 1, 3.5 1))"
        };

        bool gmJsonRes3 = db.JSON().Set("shape:3", "$", shape3);
        Console.WriteLine(gmJsonRes3); // >>> True

        var shape4 = new
        {
            name = "Purple Point",
            geom = "POINT (2 2)"
        };

        bool gmJsonRes4 = db.JSON().Set("shape:4", "$", shape4);
        Console.WriteLine(gmJsonRes3); // >>> True

        if (version.Major >= 7)
        {
            SearchResult geomQueryResult = db.FT().Search(
                "geomidx",
                new Query("(-@name:(Green Square) @geom:[WITHIN $qshape])")
                    .AddParam("qshape", "POLYGON ((1 1, 1 3, 3 3, 3 1, 1 1))")
                    .Limit(0, 1)
            );

            Console.WriteLine(geomQueryResult.Documents.Count); // >>> 1
            var res = string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]));

            Console.WriteLine(
                string.Join(", ", geomQueryResult.Documents.Select(x => x["json"]))
            );
            // >>> {"name":"Purple Point","geom":"POINT (2 2)"}
        }
    }
}
```

You can also run queries to find whether shapes in the index completely contain or overlap each other. See [Geospatial queries](/docs/latest/develop/ai/search-and-query/query/geo-spatial/) for more information.

## On this page
