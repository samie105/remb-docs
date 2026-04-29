---
title: "Choosing a Client"
source: "https://supabase.com/docs/guides/ai/python-clients"
canonical_url: "https://supabase.com/docs/guides/ai/python-clients"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:17.941Z"
content_hash: "e67bda69c0d91d299f492697a2e8cbf65d3268aa30f9d170c87cae6fb88b01d3"
menu_path: ["AI & Vectors","AI & Vectors","Python Client","Python Client","Choosing a Client","Choosing a Client"]
section_path: ["AI & Vectors","AI & Vectors","Python Client","Python Client","Choosing a Client","Choosing a Client"]
nav_prev: {"path": "supabase/docs/guides/ai/langchain/index.md", "title": "LangChain"}
nav_next: {"path": "supabase/docs/guides/ai/quickstarts/face-similarity/index.md", "title": "Face similarity search"}
---

# 

Choosing a Client

* * *

As described in [Structured & Unstructured Embeddings](../structured-unstructured/index.md), AI workloads come in many forms.

For data science or ephemeral workloads, the [Supabase Vecs](https://supabase.github.io/vecs/) client gets you started quickly. All you need is a connection string and vecs handles setting up your database to store and query vectors with associated metadata.

Click [**Connect**](/dashboard/project/_/?showConnect=true) at the top of any project page to get your connection string.

Copy the URI from the **Shared pooler** option.

For production python applications with version controlled migrations, we recommend adding first class vector support to your toolchain by [registering the vector type with your ORM](https://github.com/pgvector/pgvector-python). pgvector provides bindings for the most commonly used SQL drivers/libraries including Django, SQLAlchemy, SQLModel, psycopg, asyncpg and Peewee.
