---
title: "Vector search"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:41.586Z"
content_hash: "b0ec8d73e19031a243aed8bd355817fc3c9faf73e25ec872c950c638adecfb41"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Vector search","→","Vector search"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Vector search","→","Vector search"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/query/range/index.md", "title": "Range queries"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/vectors/index.md", "title": "Vector search concepts"}
---

# Vector search

Query for data based on vector embeddings

This article gives you a good overview of how to perform vector search queries with Redis Search, which is part of Redis Open Source. See the [Redis as a vector database quick start guide](../../../../get-started/vector-database/index.md) for more information about Redis as a vector database. You can also find more detailed information about all the parameters in the [vector reference documentation](../../vectors/index.md).

A vector search query on a vector field allows you to find all vectors in a vector space that are close to a given vector. You can query for the k-nearest neighbors or vectors within a given radius.

The examples in this article use a schema with the following fields:

JSON field

Field alias

Field type

Description

`$.description`

`description`

`TEXT`

The description of a bicycle as unstructured text

`$.description_embeddings`

`vector`

`VECTOR`

The vector that a machine learning model derived from the description text

## K-neareast neighbours (KNN)

The Redis command [FT.SEARCH](/docs/latest/commands/ft.search/) takes the index name, the query string, and additional query parameters as arguments. You need to pass the number of nearest neighbors, the vector field name, and the vector's binary representation in the following way:

```
FT.SEARCH index "(*)=>[KNN num_neighbours @field $vector]" PARAMS 2 vector "binary_data" DIALECT 2
```

Here is a more detailed explanation of this query:

1.  **Pre-filter**: The first expression within the round brackets is a filter. It allows you to decide which vectors should be taken into account before the vector search is performed. The expression `(*)` means that all vectors are considered.
2.  **Next step**: The `=>` arrow indicates that the pre-filtering happens before the vector search.
3.  **KNN query**: The expression `[KNN num_neighbours @field $vector]` is a parameterized query expression. A parameter name is indicated by the `$` prefix within the query string.
4.  **Vector binary data**: You need to use the `PARAMS` argument to substitute `$vector` with the binary representation of the vector. The value `2` indicates that `PARAMS` is followed by two arguments, the parameter name `vector` and the parameter value.
5.  **Dialect**: The vector search feature has been available since version two of the query dialect.

You can read more about the `PARAMS` argument in the [FT.SEARCH](/docs/latest/commands/ft.search/) command reference.

The following example shows you how to query for three bikes based on their description embeddings, and by using the field alias `vector`. The result is returned in ascending order based on the distance. You can see that the query only returns the fields `__vector_score` and `description`. The field `__vector_score` is present by default. Because you can have multiple vector fields in your schema, the vector score field name depends on the name of the vector field. If you change the field name `@vector` to `@foo`, the score field name changes to `__foo_score`.

```plaintext
FT.SEARCH idx:bikes_vss "(*)=>[KNN 3 @vector $query_vector]" PARAMS 2 "query_vector" "Z\xf8\x15:\xf23\xa1\xbfZ\x1dI>\r\xca9..." SORTBY "__vector_score" ASC RETURN 2 "__vector_score" "description" DIALECT 2
```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, SCHEMA_VECTOR_FIELD_ALGORITHM } from '@redis/search';
import { pipeline } from '@xenova/transformers';

function float32Buffer(arr) {
  const floatArray = new Float32Array(arr);
  const float32Buffer = Buffer.from(floatArray.buffer);
  return float32Buffer;
}

async function embedText(sentence) {
  let modelName = 'Xenova/all-MiniLM-L6-v2';
  let pipe = await pipeline('feature-extraction', modelName);

  let vectorOutput = await pipe(sentence, {
      pooling: 'mean',
      normalize: true,
  });

  const embedding = Object.values(vectorOutput?.data);

  return embedding;
}

const vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector'
    }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
});

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_vector.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', 
  '*=>[KNN 3 @vector $query_vector AS score]', {
    PARAMS: { query_vector: vector_query },
    RETURN: ['description'],
    DIALECT: 2
  }
);
console.log(res1.total); // >>> 3
console.log(res1); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:0', value: [Object: null prototype] {} },
//    { id: 'bicycle:2', value: [Object: null prototype] {} },
//    { id: 'bicycle:9', value: [Object: null prototype] {} }
//  ]
//}

const res2 = await client.ft.search('idx:bicycle', 
  '@vector:[VECTOR_RANGE 0.9 $query_vector]=>{$YIELD_DISTANCE_AS: vector_dist}', {
    PARAMS: { query_vector: vector_query },
    SORTBY: 'vector_dist',
    RETURN: ['vector_dist', 'description'],
    DIALECT: 2
  }
);
console.log(res2.total); // >>> 1
console.log(res2); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:0', value: [Object: null prototype] } ]
//}

```

```python
import json
import warnings
import redis
import numpy as np
from redisvl.index import SearchIndex
from redisvl.query import RangeQuery, VectorQuery
from redisvl.schema import IndexSchema
from sentence_transformers import SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

r = redis.Redis(decode_responses=True)

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# create index
schema = IndexSchema.from_yaml('data/query_vector_idx.yaml')
index = SearchIndex(schema, r)
index.create(overwrite=True, drop=True)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)
index.load(bicycles)

query = "Bike for small kids"
query_vector = embed_text(model, query)
print(query_vector[:10]) # >>> b'\x02=c=\x93\x0e\xe0=aC'

vquery = VectorQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    num_results=3,
    return_score=True,
    return_fields=["description"]
)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6b702e8b...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

vquery = RangeQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    distance_threshold=0.5,
    return_score=True
).return_fields("description").dialect(2)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6bcb1bb4...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

```

Note:

The binary value of the query vector is significantly shortened in the CLI example above.

## Radius

Instead of the number of nearest neighbors, you need to pass the radius along with the index name, the vector field name, and the vector's binary value:

```
FT.SEARCH index "@field:[VECTOR_RANGE radius $vector]" PARAMS 2 vector "binary_data" DIALECT 2
```

If you want to sort by distance, then you must yield the distance via the range query parameter `$YIELD_DISTANCE_AS`:

```
FT.SEARCH index "@field:[VECTOR_RANGE radius $vector]=>{$YIELD_DISTANCE_AS: dist_field}" PARAMS 2 vector "binary_data" SORTBY dist_field DIALECT 2
```

Here is a more detailed explanation of this query:

1.  **Range query**: the syntax of a radius query is very similar to the regular range query, except for the keyword `VECTOR_RANGE`. You can also combine a vector radius query with other queries in the same way as regular range queries. See [combined queries article](../combined/index.md) for more details.
2.  **Additional step**: the `=>` arrow means that the range query is followed by evaluating additional parameters.
3.  **Range query parameters**: parameters such as `$YIELD_DISTANCE_AS` can be found in the [vectors reference documentation](../../vectors/index.md).
4.  **Vector binary data**: you need to use `PARAMS` to pass the binary representation of the vector.
5.  **Dialect**: vector search has been available since version two of the query dialect.

Note:

By default, [`FT.SEARCH`](/docs/latest/commands/ft.search/) returns only the first ten results. The [range query article](../range/index.md) explains to you how to scroll through the result set.

The example below shows a radius query that returns the description and the distance within a radius of `0.5`. The result is sorted by the distance.

```plaintext
FT.SEARCH idx:bikes_vss "@vector:[VECTOR_RANGE 0.5 $query_vector]=>{$YIELD_DISTANCE_AS: vector_dist}" PARAMS 2 "query_vector" "Z\xf8\x15:\xf23\xa1\xbfZ\x1dI>\r\xca9..." SORTBY vector_dist ASC RETURN 2 vector_dist description DIALECT 2
```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, SCHEMA_VECTOR_FIELD_ALGORITHM } from '@redis/search';
import { pipeline } from '@xenova/transformers';

function float32Buffer(arr) {
  const floatArray = new Float32Array(arr);
  const float32Buffer = Buffer.from(floatArray.buffer);
  return float32Buffer;
}

async function embedText(sentence) {
  let modelName = 'Xenova/all-MiniLM-L6-v2';
  let pipe = await pipeline('feature-extraction', modelName);

  let vectorOutput = await pipe(sentence, {
      pooling: 'mean',
      normalize: true,
  });

  const embedding = Object.values(vectorOutput?.data);

  return embedding;
}

const vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector'
    }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
});

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_vector.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', 
  '*=>[KNN 3 @vector $query_vector AS score]', {
    PARAMS: { query_vector: vector_query },
    RETURN: ['description'],
    DIALECT: 2
  }
);
console.log(res1.total); // >>> 3
console.log(res1); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:0', value: [Object: null prototype] {} },
//    { id: 'bicycle:2', value: [Object: null prototype] {} },
//    { id: 'bicycle:9', value: [Object: null prototype] {} }
//  ]
//}

const res2 = await client.ft.search('idx:bicycle', 
  '@vector:[VECTOR_RANGE 0.9 $query_vector]=>{$YIELD_DISTANCE_AS: vector_dist}', {
    PARAMS: { query_vector: vector_query },
    SORTBY: 'vector_dist',
    RETURN: ['vector_dist', 'description'],
    DIALECT: 2
  }
);
console.log(res2.total); // >>> 1
console.log(res2); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:0', value: [Object: null prototype] } ]
//}

```

```python
import json
import warnings
import redis
import numpy as np
from redisvl.index import SearchIndex
from redisvl.query import RangeQuery, VectorQuery
from redisvl.schema import IndexSchema
from sentence_transformers import SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

r = redis.Redis(decode_responses=True)

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# create index
schema = IndexSchema.from_yaml('data/query_vector_idx.yaml')
index = SearchIndex(schema, r)
index.create(overwrite=True, drop=True)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)
index.load(bicycles)

query = "Bike for small kids"
query_vector = embed_text(model, query)
print(query_vector[:10]) # >>> b'\x02=c=\x93\x0e\xe0=aC'

vquery = VectorQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    num_results=3,
    return_score=True,
    return_fields=["description"]
)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6b702e8b...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

vquery = RangeQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    distance_threshold=0.5,
    return_score=True
).return_fields("description").dialect(2)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6bcb1bb4...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

```

## Cluster optimization

In Redis cluster environments, you can optimize vector search performance using the `$SHARD_K_RATIO` query attribute. This parameter controls how many results each shard retrieves relative to the requested `top_k`, creating a tunable trade-off between accuracy and performance.

### Basic cluster optimization

Retrieve 100 nearest neighbors with each shard providing 60% of the requested results:

```plaintext
FT.SEARCH idx:bikes_vss "(*)=>[KNN 100 @vector $query_vector]=>{$SHARD_K_RATIO: 0.6; $YIELD_DISTANCE_AS: vector_distance}" PARAMS 2 "query_vector" "Z\xf8\x15:\xf23\xa1\xbfZ\x1dI>\r\xca9..." SORTBY vector_distance ASC RETURN 2 "vector_distance" "description" DIALECT 2
```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, SCHEMA_VECTOR_FIELD_ALGORITHM } from '@redis/search';
import { pipeline } from '@xenova/transformers';

function float32Buffer(arr) {
  const floatArray = new Float32Array(arr);
  const float32Buffer = Buffer.from(floatArray.buffer);
  return float32Buffer;
}

async function embedText(sentence) {
  let modelName = 'Xenova/all-MiniLM-L6-v2';
  let pipe = await pipeline('feature-extraction', modelName);

  let vectorOutput = await pipe(sentence, {
      pooling: 'mean',
      normalize: true,
  });

  const embedding = Object.values(vectorOutput?.data);

  return embedding;
}

const vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector'
    }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
});

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_vector.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', 
  '*=>[KNN 3 @vector $query_vector AS score]', {
    PARAMS: { query_vector: vector_query },
    RETURN: ['description'],
    DIALECT: 2
  }
);
console.log(res1.total); // >>> 3
console.log(res1); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:0', value: [Object: null prototype] {} },
//    { id: 'bicycle:2', value: [Object: null prototype] {} },
//    { id: 'bicycle:9', value: [Object: null prototype] {} }
//  ]
//}

const res2 = await client.ft.search('idx:bicycle', 
  '@vector:[VECTOR_RANGE 0.9 $query_vector]=>{$YIELD_DISTANCE_AS: vector_dist}', {
    PARAMS: { query_vector: vector_query },
    SORTBY: 'vector_dist',
    RETURN: ['vector_dist', 'description'],
    DIALECT: 2
  }
);
console.log(res2.total); // >>> 1
console.log(res2); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:0', value: [Object: null prototype] } ]
//}

```

```python
import json
import warnings
import redis
import numpy as np
from redisvl.index import SearchIndex
from redisvl.query import RangeQuery, VectorQuery
from redisvl.schema import IndexSchema
from sentence_transformers import SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

r = redis.Redis(decode_responses=True)

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# create index
schema = IndexSchema.from_yaml('data/query_vector_idx.yaml')
index = SearchIndex(schema, r)
index.create(overwrite=True, drop=True)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)
index.load(bicycles)

query = "Bike for small kids"
query_vector = embed_text(model, query)
print(query_vector[:10]) # >>> b'\x02=c=\x93\x0e\xe0=aC'

vquery = VectorQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    num_results=3,
    return_score=True,
    return_fields=["description"]
)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6b702e8b...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

vquery = RangeQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    distance_threshold=0.5,
    return_score=True
).return_fields("description").dialect(2)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6bcb1bb4...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

```

### Combined with filtering

You can combine `$SHARD_K_RATIO` with pre-filtering to optimize searches on specific subsets of data:

```plaintext
FT.SEARCH idx:bikes_vss "(@brand:trek)=>[KNN 50 @vector $query_vector]=>{$SHARD_K_RATIO: 0.4; $YIELD_DISTANCE_AS: similarity}" PARAMS 2 "query_vector" "Z\xf8\x15:\xf23\xa1\xbfZ\x1dI>\r\xca9..." SORTBY similarity ASC RETURN 2 "similarity" "description" DIALECT 2
```

```node.js
import assert from 'node:assert';
import fs from 'node:fs';
import { createClient } from 'redis';
import { SCHEMA_FIELD_TYPE, SCHEMA_VECTOR_FIELD_ALGORITHM } from '@redis/search';
import { pipeline } from '@xenova/transformers';

function float32Buffer(arr) {
  const floatArray = new Float32Array(arr);
  const float32Buffer = Buffer.from(floatArray.buffer);
  return float32Buffer;
}

async function embedText(sentence) {
  let modelName = 'Xenova/all-MiniLM-L6-v2';
  let pipe = await pipeline('feature-extraction', modelName);

  let vectorOutput = await pipe(sentence, {
      pooling: 'mean',
      normalize: true,
  });

  const embedding = Object.values(vectorOutput?.data);

  return embedding;
}

const vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector'
    }
}, {
    ON: 'JSON',
    PREFIX: 'bicycle:'
});

// load data
const bicycles = JSON.parse(fs.readFileSync('data/query_vector.json', 'utf8'));

await Promise.all(
  bicycles.map((bicycle, bid) => {
      return client.json.set(`bicycle:${bid}`, '$', bicycle);
  })
);

const res1 = await client.ft.search('idx:bicycle', 
  '*=>[KNN 3 @vector $query_vector AS score]', {
    PARAMS: { query_vector: vector_query },
    RETURN: ['description'],
    DIALECT: 2
  }
);
console.log(res1.total); // >>> 3
console.log(res1); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:0', value: [Object: null prototype] {} },
//    { id: 'bicycle:2', value: [Object: null prototype] {} },
//    { id: 'bicycle:9', value: [Object: null prototype] {} }
//  ]
//}

const res2 = await client.ft.search('idx:bicycle', 
  '@vector:[VECTOR_RANGE 0.9 $query_vector]=>{$YIELD_DISTANCE_AS: vector_dist}', {
    PARAMS: { query_vector: vector_query },
    SORTBY: 'vector_dist',
    RETURN: ['vector_dist', 'description'],
    DIALECT: 2
  }
);
console.log(res2.total); // >>> 1
console.log(res2); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:0', value: [Object: null prototype] } ]
//}

```

```python
import json
import warnings
import redis
import numpy as np
from redisvl.index import SearchIndex
from redisvl.query import RangeQuery, VectorQuery
from redisvl.schema import IndexSchema
from sentence_transformers import SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

r = redis.Redis(decode_responses=True)

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# create index
schema = IndexSchema.from_yaml('data/query_vector_idx.yaml')
index = SearchIndex(schema, r)
index.create(overwrite=True, drop=True)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)
index.load(bicycles)

query = "Bike for small kids"
query_vector = embed_text(model, query)
print(query_vector[:10]) # >>> b'\x02=c=\x93\x0e\xe0=aC'

vquery = VectorQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    num_results=3,
    return_score=True,
    return_fields=["description"]
)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6b702e8b...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

vquery = RangeQuery(
    vector=query_vector,
    vector_field_name="description_embeddings",
    distance_threshold=0.5,
    return_score=True
).return_fields("description").dialect(2)
res = index.query(vquery)
print(res) # >>> [{'id': 'bicycle:6bcb1bb4...', 'vector_distance': '0.399111807346', 'description': 'Kids want...

```

Note:

The `$SHARD_K_RATIO` parameter is only applicable in Redis cluster environments and has no effect in standalone Redis instances.

## On this page
