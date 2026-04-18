---
title: "Creating and managing collections"
source: "https://supabase.com/docs/guides/ai/quickstarts/hello-world"
canonical_url: "https://supabase.com/docs/guides/ai/quickstarts/hello-world"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:11.008Z"
content_hash: "fe367b87b7926997f472b103f62f7299280082912a2d375c26a43605d60d6e34"
menu_path: ["AI & Vectors","AI & Vectors","Python Examples","Python Examples","Creating and managing collections","Creating and managing collections"]
section_path: ["AI & Vectors","AI & Vectors","Python Examples","Python Examples","Creating and managing collections","Creating and managing collections"]
---
# 

Creating and managing collections

## 

Connecting to your database with Colab.

* * *

This guide will walk you through a basic ["Hello World"](https://github.com/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb) example using Colab and Supabase Vecs. You'll learn how to:

1.  Launch a Postgres database that uses pgvector to store embeddings
2.  Launch a notebook that connects to your database
3.  Create a vector collection
4.  Add data to the collection
5.  Query the collection

## Project setup[#](#project-setup)

Let's create a new Postgres database. This is as simple as starting a new Project in Supabase:

1.  [Create a new project](https://database.new/) in the Supabase dashboard.
2.  Enter your project details. Remember to store your password somewhere safe.

Your database will be available in less than a minute.

**Finding your credentials:**

You can find your project credentials on the dashboard:

*   [Database connection strings](/dashboard/project/_/settings/api?showConnect=true): Direct and Pooler connection details including the connection string and parameters.
*   [Database password](/dashboard/project/_/database/settings): Reset database password here if you do not have it.
*   [API credentials](/dashboard/project/_/settings/api): your serverless API URL and publishable keys.

## Launching a notebook[#](#launching-a-notebook)

Launch our [`vector_hello_world`](https://github.com/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb) notebook in Colab:

[![](/docs/img/ai/colab-badge.svg)](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/vector_hello_world.ipynb)

At the top of the notebook, you'll see a button `Copy to Drive`. Click this button to copy the notebook to your Google Drive.

## Connecting to your database[#](#connecting-to-your-database)

Inside the Notebook, find the cell which specifies the `DB_CONNECTION`. It will contain some code like this:

```
1import vecs23DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"45# create vector store client6vx = vecs.create_client(DB_CONNECTION)
```

Replace the `DB_CONNECTION` with your Session pooler connection string. You can find the connection string on your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true).

SQLAlchemy requires the connection string to start with `postgresql://` (instead of `postgres://`). Don't forget to rename this after copying the string from the dashboard.

You must use the Session pooler connection string with Google Colab since Colab does not support IPv6.

## Stepping through the notebook[#](#stepping-through-the-notebook)

Now all that's left is to step through the notebook. You can do this by clicking the "execute" button (`ctrl+enter`) at the top left of each code cell. The notebook guides you through the process of creating a collection, adding data to it, and querying it.

You can view the inserted items in the [Table Editor](/dashboard/project/_/editor/), by selecting the `vecs` schema from the schema dropdown.

![Colab documents](/docs/img/ai/google-colab/colab-documents.png)

## Next steps[#](#next-steps)

You can now start building your own applications with Vecs. Check our [examples](/docs/guides/ai#examples) for ideas.
