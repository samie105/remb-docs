---
title: "Combined queries"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/combined/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/combined/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:13:58.025Z"
content_hash: "8b4d2fe31a9a95d40b632dd53d7e3b9bb47a91b5da046543d23c978b3e359943"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Combined queries","→","Combined queries"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data","→\n      \n        Combined queries","→","Combined queries"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/query/aggregation/index.md", "title": "Aggregation queries"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/query/exact-match/index.md", "title": "Exact match queries"}
---

# Combined queries

Combine query expressions

A combined query is a combination of several query types, such as:

*   [Exact match](/docs/latest/develop/ai/search-and-query/query/exact-match/)
*   [Range](/docs/latest/develop/ai/search-and-query/query/range/)
*   [Full-text](/docs/latest/develop/ai/search-and-query/query/full-text/)
*   [Geospatial](/docs/latest/develop/ai/search-and-query/query/geo-spatial/)
*   [Vector search](/docs/latest/develop/ai/search-and-query/query/vector-search/)

You can use logical query operators to combine query expressions for numeric, tag, and text fields. For vector fields, you can combine a KNN query with a pre-filter.

Note:

The operators are interpreted slightly differently depending on the query dialect used. The default dialect is `DIALECT 1`; see [this article](/docs/latest/develop/ai/search-and-query/administration/configuration/#search-default-dialect) for information on how to change the dialect version. This article uses the second version of the query dialect, `DIALECT 2`, and uses additional brackets (`(...)`) to help clarify the examples. Further details can be found in the [query syntax documentation](/docs/latest/develop/ai/search-and-query/advanced-concepts/query_syntax/).

The examples in this article use the following schema:

Field name

Field type

`description`

`TEXT`

`condition`

`TAG`

`price`

`NUMERIC`

`vector`

`VECTOR`

## AND

The binary operator (space) is used to intersect the results of two or more expressions.

```
FT.SEARCH index "(expr1) (expr2)"
```

If you want to perform an intersection based on multiple values within a specific text field, then you should use the following simplified notion:

```
FT.SEARCH index "@text_field:( value1 value2 ... )"
```

The following example shows you a query that finds bicycles in new condition and in a price range from 500 USD to 1000 USD:

```plaintext
FT.SEARCH idx:bicycle "@price:[500 1000] @condition:{new}"
```

```python
import json
import numpy as np
import redis
import warnings
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import  SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query = "Bike for small kids"
query_vector = embed_text(model, query)

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", no_stem=True, as_name="model"),
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

q = Query("@price:[500 1000] @condition:{new}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("kids @price:[500 1000] @condition:{used}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("@description:(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@description:(kids | small) @condition:{new | used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@price:[500 1000] -@condition:{new}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]").dialect(2)
# put query string here
res = index.search(q,{ 'query_vector': query_vector })
print(res.total) # >>> 2

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

  if (vectorOutput == null) {
    throw new Error('vectorOutput is undefined');
  }

  const embedding = Object.values(vectorOutput.data);

  return embedding;
}

let vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.condition': {
      type: SCHEMA_FIELD_TYPE.TAG,
      AS: 'condition'
    },
    '$.price': {
      type: SCHEMA_FIELD_TYPE.NUMERIC,
      AS: 'price'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector',
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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000] @condition:{new}');
console.log(res1.total); // >>> 1
console.log(res1); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]
//}

const res2 = await client.ft.search('idx:bicycle', 'kids @price:[500 1000] @condition:{used}');
console.log(res2.total); // >>> 1
console.log(res2); // >>>
// {
//   total: 1,
//   documents: [ { id: 'bicycle:2', value: [Object: null prototype] } ]
// }

const res3 = await client.ft.search('idx:bicycle', '(kids | small) @condition:{used}');
console.log(res3.total); // >>> 2
console.log(res3); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res4 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{used}');
console.log(res4.total); // >>> 2
console.log(res4); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res5 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{new | used}');
console.log(res5.total); // >>> 3
console.log(res5); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:1', value: [Object: null prototype] },
//    { id: 'bicycle:0', value: [Object: null prototype] },
//    { id: 'bicycle:2', value: [Object: null prototype] }
//  ]
//}

const res6 = await client.ft.search('idx:bicycle', '@price:[500 1000] -@condition:{new}');
console.log(res6.total); // >>> 2
console.log(res6); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

const res7 = await client.ft.search('idx:bicycle', 
  '(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]', {
    PARAMS: { query_vector: vector_query },
    DIALECT: 2
  }
);
console.log(res7.total); // >>> 2
console.log(res7); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

```

You might also be interested in bicycles for kids. The query below shows you how to combine a full-text search with the criteria from the previous query:

```plaintext
FT.SEARCH idx:bicycle "kids (@price:[500 1000] @condition:{used})"
```

```python
import json
import numpy as np
import redis
import warnings
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import  SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query = "Bike for small kids"
query_vector = embed_text(model, query)

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", no_stem=True, as_name="model"),
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

q = Query("@price:[500 1000] @condition:{new}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("kids @price:[500 1000] @condition:{used}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("@description:(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@description:(kids | small) @condition:{new | used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@price:[500 1000] -@condition:{new}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]").dialect(2)
# put query string here
res = index.search(q,{ 'query_vector': query_vector })
print(res.total) # >>> 2

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

  if (vectorOutput == null) {
    throw new Error('vectorOutput is undefined');
  }

  const embedding = Object.values(vectorOutput.data);

  return embedding;
}

let vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.condition': {
      type: SCHEMA_FIELD_TYPE.TAG,
      AS: 'condition'
    },
    '$.price': {
      type: SCHEMA_FIELD_TYPE.NUMERIC,
      AS: 'price'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector',
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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000] @condition:{new}');
console.log(res1.total); // >>> 1
console.log(res1); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]
//}

const res2 = await client.ft.search('idx:bicycle', 'kids @price:[500 1000] @condition:{used}');
console.log(res2.total); // >>> 1
console.log(res2); // >>>
// {
//   total: 1,
//   documents: [ { id: 'bicycle:2', value: [Object: null prototype] } ]
// }

const res3 = await client.ft.search('idx:bicycle', '(kids | small) @condition:{used}');
console.log(res3.total); // >>> 2
console.log(res3); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res4 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{used}');
console.log(res4.total); // >>> 2
console.log(res4); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res5 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{new | used}');
console.log(res5.total); // >>> 3
console.log(res5); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:1', value: [Object: null prototype] },
//    { id: 'bicycle:0', value: [Object: null prototype] },
//    { id: 'bicycle:2', value: [Object: null prototype] }
//  ]
//}

const res6 = await client.ft.search('idx:bicycle', '@price:[500 1000] -@condition:{new}');
console.log(res6.total); // >>> 2
console.log(res6); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

const res7 = await client.ft.search('idx:bicycle', 
  '(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]', {
    PARAMS: { query_vector: vector_query },
    DIALECT: 2
  }
);
console.log(res7.total); // >>> 2
console.log(res7); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

```

## OR

You can use the binary operator `|` (vertical bar) to perform a union.

```
FT.SEARCH index "(expr1) | (expr2)"
```

Note:

The logical `AND` takes precedence over `OR` when using dialect version two. The expression `expr1 expr2 | expr3 expr4` means `(expr1 expr2) | (expr3 expr4)`. Version one of the query dialect behaves differently. Using parentheses in query strings is advised to ensure the order is clear.

If you want to perform the union based on multiple values within a single tag or text field, then you should use the following simplified notion:

```
FT.SEARCH index "@text_field:( value1 | value2 | ... )"
```

```
FT.SEARCH index "@tag_field:{ value1 | value2 | ... }"
```

The following query shows you how to find used bicycles that contain either the word 'kids' or 'small':

```plaintext
FT.SEARCH idx:bicycle "(kids | small) @condition:{used}"
```

```python
import json
import numpy as np
import redis
import warnings
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import  SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query = "Bike for small kids"
query_vector = embed_text(model, query)

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", no_stem=True, as_name="model"),
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

q = Query("@price:[500 1000] @condition:{new}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("kids @price:[500 1000] @condition:{used}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("@description:(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@description:(kids | small) @condition:{new | used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@price:[500 1000] -@condition:{new}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]").dialect(2)
# put query string here
res = index.search(q,{ 'query_vector': query_vector })
print(res.total) # >>> 2

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

  if (vectorOutput == null) {
    throw new Error('vectorOutput is undefined');
  }

  const embedding = Object.values(vectorOutput.data);

  return embedding;
}

let vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.condition': {
      type: SCHEMA_FIELD_TYPE.TAG,
      AS: 'condition'
    },
    '$.price': {
      type: SCHEMA_FIELD_TYPE.NUMERIC,
      AS: 'price'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector',
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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000] @condition:{new}');
console.log(res1.total); // >>> 1
console.log(res1); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]
//}

const res2 = await client.ft.search('idx:bicycle', 'kids @price:[500 1000] @condition:{used}');
console.log(res2.total); // >>> 1
console.log(res2); // >>>
// {
//   total: 1,
//   documents: [ { id: 'bicycle:2', value: [Object: null prototype] } ]
// }

const res3 = await client.ft.search('idx:bicycle', '(kids | small) @condition:{used}');
console.log(res3.total); // >>> 2
console.log(res3); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res4 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{used}');
console.log(res4.total); // >>> 2
console.log(res4); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res5 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{new | used}');
console.log(res5.total); // >>> 3
console.log(res5); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:1', value: [Object: null prototype] },
//    { id: 'bicycle:0', value: [Object: null prototype] },
//    { id: 'bicycle:2', value: [Object: null prototype] }
//  ]
//}

const res6 = await client.ft.search('idx:bicycle', '@price:[500 1000] -@condition:{new}');
console.log(res6.total); // >>> 2
console.log(res6); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

const res7 = await client.ft.search('idx:bicycle', 
  '(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]', {
    PARAMS: { query_vector: vector_query },
    DIALECT: 2
  }
);
console.log(res7.total); // >>> 2
console.log(res7); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

```

The previous query searches across all text fields. The following example shows you how to limit the search to the description field:

```plaintext
FT.SEARCH idx:bicycle "@description:(kids | small) @condition:{used}"
```

```python
import json
import numpy as np
import redis
import warnings
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import  SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query = "Bike for small kids"
query_vector = embed_text(model, query)

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", no_stem=True, as_name="model"),
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

q = Query("@price:[500 1000] @condition:{new}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("kids @price:[500 1000] @condition:{used}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("@description:(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@description:(kids | small) @condition:{new | used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@price:[500 1000] -@condition:{new}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]").dialect(2)
# put query string here
res = index.search(q,{ 'query_vector': query_vector })
print(res.total) # >>> 2

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

  if (vectorOutput == null) {
    throw new Error('vectorOutput is undefined');
  }

  const embedding = Object.values(vectorOutput.data);

  return embedding;
}

let vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.condition': {
      type: SCHEMA_FIELD_TYPE.TAG,
      AS: 'condition'
    },
    '$.price': {
      type: SCHEMA_FIELD_TYPE.NUMERIC,
      AS: 'price'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector',
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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000] @condition:{new}');
console.log(res1.total); // >>> 1
console.log(res1); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]
//}

const res2 = await client.ft.search('idx:bicycle', 'kids @price:[500 1000] @condition:{used}');
console.log(res2.total); // >>> 1
console.log(res2); // >>>
// {
//   total: 1,
//   documents: [ { id: 'bicycle:2', value: [Object: null prototype] } ]
// }

const res3 = await client.ft.search('idx:bicycle', '(kids | small) @condition:{used}');
console.log(res3.total); // >>> 2
console.log(res3); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res4 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{used}');
console.log(res4.total); // >>> 2
console.log(res4); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res5 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{new | used}');
console.log(res5.total); // >>> 3
console.log(res5); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:1', value: [Object: null prototype] },
//    { id: 'bicycle:0', value: [Object: null prototype] },
//    { id: 'bicycle:2', value: [Object: null prototype] }
//  ]
//}

const res6 = await client.ft.search('idx:bicycle', '@price:[500 1000] -@condition:{new}');
console.log(res6.total); // >>> 2
console.log(res6); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

const res7 = await client.ft.search('idx:bicycle', 
  '(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]', {
    PARAMS: { query_vector: vector_query },
    DIALECT: 2
  }
);
console.log(res7.total); // >>> 2
console.log(res7); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

```

If you want to extend the search to new bicycles, then the below example shows you how to do that:

```plaintext
FT.SEARCH idx:bicycle "@description:(kids | small) @condition:{new | used}"
```

```python
import json
import numpy as np
import redis
import warnings
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import  SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query = "Bike for small kids"
query_vector = embed_text(model, query)

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", no_stem=True, as_name="model"),
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

q = Query("@price:[500 1000] @condition:{new}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("kids @price:[500 1000] @condition:{used}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("@description:(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@description:(kids | small) @condition:{new | used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@price:[500 1000] -@condition:{new}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]").dialect(2)
# put query string here
res = index.search(q,{ 'query_vector': query_vector })
print(res.total) # >>> 2

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

  if (vectorOutput == null) {
    throw new Error('vectorOutput is undefined');
  }

  const embedding = Object.values(vectorOutput.data);

  return embedding;
}

let vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.condition': {
      type: SCHEMA_FIELD_TYPE.TAG,
      AS: 'condition'
    },
    '$.price': {
      type: SCHEMA_FIELD_TYPE.NUMERIC,
      AS: 'price'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector',
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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000] @condition:{new}');
console.log(res1.total); // >>> 1
console.log(res1); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]
//}

const res2 = await client.ft.search('idx:bicycle', 'kids @price:[500 1000] @condition:{used}');
console.log(res2.total); // >>> 1
console.log(res2); // >>>
// {
//   total: 1,
//   documents: [ { id: 'bicycle:2', value: [Object: null prototype] } ]
// }

const res3 = await client.ft.search('idx:bicycle', '(kids | small) @condition:{used}');
console.log(res3.total); // >>> 2
console.log(res3); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res4 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{used}');
console.log(res4.total); // >>> 2
console.log(res4); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res5 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{new | used}');
console.log(res5.total); // >>> 3
console.log(res5); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:1', value: [Object: null prototype] },
//    { id: 'bicycle:0', value: [Object: null prototype] },
//    { id: 'bicycle:2', value: [Object: null prototype] }
//  ]
//}

const res6 = await client.ft.search('idx:bicycle', '@price:[500 1000] -@condition:{new}');
console.log(res6.total); // >>> 2
console.log(res6); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

const res7 = await client.ft.search('idx:bicycle', 
  '(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]', {
    PARAMS: { query_vector: vector_query },
    DIALECT: 2
  }
);
console.log(res7.total); // >>> 2
console.log(res7); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

```

## NOT

A minus (`-`) in front of a query expression negates the expression.

```
FT.SEARCH index "-(expr)"
```

If you want to exclude new bicycles from the search within the previous price range, you can use this query:

```plaintext
FT.SEARCH idx:bicycle "@price:[500 1000] -@condition:{new}"
```

```python
import json
import numpy as np
import redis
import warnings
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import  SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query = "Bike for small kids"
query_vector = embed_text(model, query)

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", no_stem=True, as_name="model"),
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

q = Query("@price:[500 1000] @condition:{new}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("kids @price:[500 1000] @condition:{used}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("@description:(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@description:(kids | small) @condition:{new | used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@price:[500 1000] -@condition:{new}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]").dialect(2)
# put query string here
res = index.search(q,{ 'query_vector': query_vector })
print(res.total) # >>> 2

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

  if (vectorOutput == null) {
    throw new Error('vectorOutput is undefined');
  }

  const embedding = Object.values(vectorOutput.data);

  return embedding;
}

let vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.condition': {
      type: SCHEMA_FIELD_TYPE.TAG,
      AS: 'condition'
    },
    '$.price': {
      type: SCHEMA_FIELD_TYPE.NUMERIC,
      AS: 'price'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector',
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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000] @condition:{new}');
console.log(res1.total); // >>> 1
console.log(res1); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]
//}

const res2 = await client.ft.search('idx:bicycle', 'kids @price:[500 1000] @condition:{used}');
console.log(res2.total); // >>> 1
console.log(res2); // >>>
// {
//   total: 1,
//   documents: [ { id: 'bicycle:2', value: [Object: null prototype] } ]
// }

const res3 = await client.ft.search('idx:bicycle', '(kids | small) @condition:{used}');
console.log(res3.total); // >>> 2
console.log(res3); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res4 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{used}');
console.log(res4.total); // >>> 2
console.log(res4); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res5 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{new | used}');
console.log(res5.total); // >>> 3
console.log(res5); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:1', value: [Object: null prototype] },
//    { id: 'bicycle:0', value: [Object: null prototype] },
//    { id: 'bicycle:2', value: [Object: null prototype] }
//  ]
//}

const res6 = await client.ft.search('idx:bicycle', '@price:[500 1000] -@condition:{new}');
console.log(res6.total); // >>> 2
console.log(res6); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

const res7 = await client.ft.search('idx:bicycle', 
  '(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]', {
    PARAMS: { query_vector: vector_query },
    DIALECT: 2
  }
);
console.log(res7.total); // >>> 2
console.log(res7); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

```

## Numeric filter

The [FT.SEARCH](/docs/latest/commands/ft.search/) command allows you to combine any query expression with a numeric filter.

```
FT.SEARCH index "expr" FILTER numeric_field start end
```

Please see the [range query article](/docs/latest/develop/ai/search-and-query/query/range/) to learn more about numeric range queries and such filters.

## Pre-filter for a KNN vector query

You can use a simple or more complex query expression with logical operators as a pre-filter in a KNN vector query.

```
FT.SEARCH index "(filter_expr)=>[KNN num_neighbours @field $vector]" PARAMS 2 vector "binary_data" DIALECT 2
```

Here is an example:

```plaintext
FT.SEARCH idx:bikes_vss "(@price:[500 1000] @condition:{new})=>[KNN 3 @vector $query_vector]" PARAMS 2 "query_vector" "Z\xf8\x15:\xf23\xa1\xbfZ\x1dI>\r\xca9..." DIALECT 2
```

```python
import json
import numpy as np
import redis
import warnings
from redis.commands.json.path import Path
from redis.commands.search.field import NumericField, TagField, TextField, VectorField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from sentence_transformers import  SentenceTransformer

def embed_text(model, text):
    return np.array(model.encode(text)).astype(np.float32).tobytes()

warnings.filterwarnings("ignore", category=FutureWarning, message=r".*clean_up_tokenization_spaces.*")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
query = "Bike for small kids"
query_vector = embed_text(model, query)

r = redis.Redis(decode_responses=True)

# create index
schema = (
    TextField("$.description", no_stem=True, as_name="model"),
    TagField("$.condition", as_name="condition"),
    NumericField("$.price", as_name="price"),
    VectorField(
        "$.description_embeddings",
        "FLAT",
        {
            "TYPE": "FLOAT32",
            "DIM": 384,
            "DISTANCE_METRIC": "COSINE",
        },
        as_name="vector",
    ),
)

index = r.ft("idx:bicycle")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["bicycle:"], index_type=IndexType.JSON),
)

# load data
with open("data/query_vector.json") as f:
    bicycles = json.load(f)

pipeline = r.pipeline(transaction=False)
for bid, bicycle in enumerate(bicycles):
    pipeline.json().set(f'bicycle:{bid}', Path.root_path(), bicycle)
pipeline.execute()

q = Query("@price:[500 1000] @condition:{new}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("kids @price:[500 1000] @condition:{used}")
res = index.search(q)
print(res.total) # >>> 1

q = Query("(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("@description:(kids | small) @condition:{used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@description:(kids | small) @condition:{new | used}")
res = index.search(q)
print(res.total) # >>> 0

q = Query("@price:[500 1000] -@condition:{new}")
res = index.search(q)
print(res.total) # >>> 2

q = Query("(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]").dialect(2)
# put query string here
res = index.search(q,{ 'query_vector': query_vector })
print(res.total) # >>> 2

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

  if (vectorOutput == null) {
    throw new Error('vectorOutput is undefined');
  }

  const embedding = Object.values(vectorOutput.data);

  return embedding;
}

let vector_query = float32Buffer(await embedText('That is a very happy person'));

const client = createClient();
await client.connect().catch(console.error);

// create index
await client.ft.create('idx:bicycle', {
    '$.description': {
      type: SCHEMA_FIELD_TYPE.TEXT,
      AS: 'description'
    },
    '$.condition': {
      type: SCHEMA_FIELD_TYPE.TAG,
      AS: 'condition'
    },
    '$.price': {
      type: SCHEMA_FIELD_TYPE.NUMERIC,
      AS: 'price'
    },
    '$.description_embeddings': {
        type: SCHEMA_FIELD_TYPE.VECTOR,
        TYPE: 'FLOAT32',
        ALGORITHM: SCHEMA_VECTOR_FIELD_ALGORITHM.FLAT,
        DIM: 384,
        DISTANCE_METRIC: 'COSINE',
        AS: 'vector',
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

const res1 = await client.ft.search('idx:bicycle', '@price:[500 1000] @condition:{new}');
console.log(res1.total); // >>> 1
console.log(res1); // >>>
//{
//  total: 1,
//  documents: [ { id: 'bicycle:5', value: [Object: null prototype] } ]
//}

const res2 = await client.ft.search('idx:bicycle', 'kids @price:[500 1000] @condition:{used}');
console.log(res2.total); // >>> 1
console.log(res2); // >>>
// {
//   total: 1,
//   documents: [ { id: 'bicycle:2', value: [Object: null prototype] } ]
// }

const res3 = await client.ft.search('idx:bicycle', '(kids | small) @condition:{used}');
console.log(res3.total); // >>> 2
console.log(res3); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res4 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{used}');
console.log(res4.total); // >>> 2
console.log(res4); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:1', value: [Object: null prototype] }
//  ]
//}

const res5 = await client.ft.search('idx:bicycle', '@description:(kids | small) @condition:{new | used}');
console.log(res5.total); // >>> 3
console.log(res5); // >>>
//{
//  total: 3,
//  documents: [
//    { id: 'bicycle:1', value: [Object: null prototype] },
//    { id: 'bicycle:0', value: [Object: null prototype] },
//    { id: 'bicycle:2', value: [Object: null prototype] }
//  ]
//}

const res6 = await client.ft.search('idx:bicycle', '@price:[500 1000] -@condition:{new}');
console.log(res6.total); // >>> 2
console.log(res6); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

const res7 = await client.ft.search('idx:bicycle', 
  '(@price:[500 1000] -@condition:{new})=>[KNN 3 @vector $query_vector]', {
    PARAMS: { query_vector: vector_query },
    DIALECT: 2
  }
);
console.log(res7.total); // >>> 2
console.log(res7); // >>>
//{
//  total: 2,
//  documents: [
//    { id: 'bicycle:2', value: [Object: null prototype] },
//    { id: 'bicycle:9', value: [Object: null prototype] }
//  ]
//}

```

The [vector search article](/docs/latest/develop/ai/search-and-query/query/vector-search/) provides further details about vector queries in general.

## On this page
