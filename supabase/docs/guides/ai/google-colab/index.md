---
title: "Google Colab"
source: "https://supabase.com/docs/guides/ai/google-colab"
canonical_url: "https://supabase.com/docs/guides/ai/google-colab"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:37.798Z"
content_hash: "0f95b0240c13e60078551b5d43f9938fbf4a40080c9c20823022ae670afa1341"
menu_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Google Colab","Google Colab"]
section_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","Google Colab","Google Colab"]
nav_prev: {"path": "supabase/docs/guides/ai/engineering-for-scale/index.md", "title": "Engineering for Scale"}
nav_next: {"path": "supabase/docs/guides/ai/going-to-prod/index.md", "title": "Going to Production"}
---

# 

Google Colab

## 

Use Google Colab to manage your Supabase Vector store.

* * *

[![](/docs/img/ai/colab-badge.svg)](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb)

Google Colab is a hosted Jupyter Notebook service. It provides free access to computing resources, including GPUs and TPUs, and is well-suited to machine learning, data science, and education. We can use Colab to manage collections using [Supabase Vecs](/docs/guides/ai/vecs-python-client).

In this tutorial we'll connect to a database running on the Supabase [platform](/dashboard/). If you don't already have a database, you can create one here: [database.new](https://database.new).

## Create a new notebook[#](#create-a-new-notebook)

Start by visiting [colab.research.google.com](https://colab.research.google.com/). There you can create a new notebook.

![Google Colab new notebook](/docs/img/ai/google-colab/colab-new.png)

## Install Vecs[#](#install-vecs)

We'll use the Supabase Vector client, [Vecs](/docs/guides/ai/vecs-python-client), to manage our collections.

At the top of the notebook add the notebook paste the following code and hit the "execute" button (`ctrl+enter`):

```
1pip install vecs
```

![Install vecs](/docs/img/ai/google-colab/install-vecs.png)

## Connect to your database[#](#connect-to-your-database)

On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true). The connection string should look like `postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:6543/postgres`

Create a new code block below the install block (`ctrl+m b`) and add the following code using the Postgres URI you copied above:

```
1import vecs23DB_CONNECTION = "postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:6543/postgres"45# create vector store client6vx = vecs.create_client(DB_CONNECTION)
```

Execute the code block (`ctrl+enter`). If no errors were returned then your connection was successful.

## Create a collection[#](#create-a-collection)

Now we're going to create a new collection and insert some documents.

Create a new code block below the install block (`ctrl+m b`). Add the following code to the code block and execute it (`ctrl+enter`):

```
1collection = vx.get_or_create_collection(name="colab_collection", dimension=3)23collection.upsert(4    vectors=[5        (6         "vec0",           # the vector's identifier7         [0.1, 0.2, 0.3],  # the vector. list or np.array8         {"year": 1973}    # associated  metadata9        ),10        (11         "vec1",12         [0.7, 0.8, 0.9],13         {"year": 2012}14        )15    ]16)
```

This will create a table inside your database within the `vecs` schema, called `colab_collection`. You can view the inserted items in the [Table Editor](/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.

![Colab documents](/docs/img/ai/google-colab/colab-documents.png)

## Query your documents[#](#query-your-documents)

Now we can search for documents based on their similarity. Create a new code block and execute the following code:

```
1collection.query(2    query_vector=[0.4,0.5,0.6],  # required3    limit=5,                     # number of records to return4    filters={},                  # metadata filters5    measure="cosine_distance",   # distance measure to use6    include_value=False,         # should distance measure values be returned?7    include_metadata=False,      # should record metadata be returned?8)
```

You will see that this returns two documents in an array `['vec1', 'vec0']`:

![Colab results](/docs/img/ai/google-colab/colab-results.png)

It also returns a warning:

```
1Query does not have a covering index for cosine_distance.
```

You can lean more about creating indexes in the [Vecs documentation](https://supabase.github.io/vecs/api/#create-an-index).

## Resources[#](#resources)

*   Vecs API: [supabase.github.io/vecs/api](https://supabase.github.io/vecs/api)


