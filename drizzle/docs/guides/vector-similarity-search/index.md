---
title: "Drizzle ORM - Vector similarity search with pgvector extension"
source: "https://orm.drizzle.team/docs/guides/vector-similarity-search"
canonical_url: "https://orm.drizzle.team/docs/guides/vector-similarity-search"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:03.363Z"
content_hash: "69ed385338400d02264b00fac7c24b8b65e0dfba4ba0e003f17d27096c6e17f4"
menu_path: ["Drizzle ORM - Vector similarity search with pgvector extension"]
section_path: []
---
Drizzle | Vector similarity search with pgvector extension

To implement vector similarity search in PostgreSQL with Drizzle ORM, you can use the `pgvector` extension. This extension provides a set of functions to work with vectors and perform similarity search.

As for now, Drizzle doesn’t create extension automatically, so you need to create it manually. Create an empty migration file and add SQL query:

```
npx drizzle-kit generate --custom
```

```
CREATE EXTENSION vector;
```

To perform similarity search, you need to create a table with a vector column and an `HNSW` or `IVFFlat` index on this column for better performance:

schema.ts

migration.sql

```
import { index, pgTable, serial, text, vector } from 'drizzle-orm/pg-core';

export const guides = pgTable(
  'guides',
  {
    id: serial('id').primaryKey(),
    title: text('title').notNull(),
    description: text('description').notNull(),
    url: text('url').notNull(),
    embedding: vector('embedding', { dimensions: 1536 }),
  },
  (table) => [
    index('embeddingIndex').using('hnsw', table.embedding.op('vector_cosine_ops')),
  ]
);
```

```
CREATE TABLE IF NOT EXISTS "guides" (
  "id" serial PRIMARY KEY NOT NULL,
  "title" text NOT NULL,
  "description" text NOT NULL,
  "url" text NOT NULL,
  "embedding" vector(1536)
);
--> statement-breakpoint
CREATE INDEX IF NOT EXISTS "embeddingIndex" ON "guides" USING hnsw (embedding vector_cosine_ops);
```

The `embedding` column is used to store vector embeddings of the guide descriptions. Vector embedding is just a representation of some data. It converts different types of data into a common format (vectors) that language models can process. This allows us to perform mathematical operations, such as measuring the distance between two vectors, to determine how similar or different two data items are.

In this example we will use `OpenAI` model to generate [embeddings](https://platform.openai.com/docs/guides/embeddings) for the description:

```
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'],
});

export const generateEmbedding = async (value: string): Promise<number[]> => {
  const input = value.replaceAll('\n', ' ');

  const { data } = await openai.embeddings.create({
    model: 'text-embedding-ada-002',
    input,
  });

  return data[0].embedding;
};
```

To search for similar guides by embedding, you can use `gt` and `sql` operators with `cosineDistance` function to calculate the similarity between the `embedding` column and the generated embedding:

```
import { cosineDistance, desc, gt, sql } from 'drizzle-orm';
import { generateEmbedding } from './embedding';
import { guides } from './schema';

const db = drizzle(...);

const findSimilarGuides = async (description: string) => {
  const embedding = await generateEmbedding(description);

  const similarity = sql<number>`1 - (${cosineDistance(guides.embedding, embedding)})`;

  const similarGuides = await db
    .select({ name: guides.title, url: guides.url, similarity })
    .from(guides)
    .where(gt(similarity, 0.5))
    .orderBy((t) => desc(t.similarity))
    .limit(4);

  return similarGuides;
};
```

```
const description = 'Guides on using Drizzle ORM with different platforms';

const similarGuides = await findSimilarGuides(description);
```

```
[
  {
    name: 'Drizzle with Turso',
    url: '/docs/tutorials/drizzle-with-turso',
    similarity: 0.8642314333984994
  },
  {
    name: 'Drizzle with Supabase Database',
    url: '/docs/tutorials/drizzle-with-supabase',
    similarity: 0.8593631126014918
  },
  {
    name: 'Drizzle with Neon Postgres',
    url: '/docs/tutorials/drizzle-with-neon',
    similarity: 0.8541051184461372
  },
  {
    name: 'Drizzle with Vercel Edge Functions',
    url: '/docs/tutorials/drizzle-with-vercel-edge-functions',
    similarity: 0.8481551084241092
  }
]
```
