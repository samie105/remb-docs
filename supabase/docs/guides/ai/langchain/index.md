---
title: "LangChain"
source: "https://supabase.com/docs/guides/ai/langchain"
canonical_url: "https://supabase.com/docs/guides/ai/langchain"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:10.723Z"
content_hash: "1e8bb173b7fc788e5e74b5d7b8cc7515232d59ebe6f7e33aa4746daf692f3b80"
menu_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","LangChain","LangChain"]
section_path: ["AI & Vectors","AI & Vectors","Third-Party Tools","Third-Party Tools","LangChain","LangChain"]
nav_prev: {"path": "supabase/docs/guides/ai/keyword-search/index.md", "title": "Keyword search"}
nav_next: {"path": "supabase/docs/guides/ai/rag-with-permissions/index.md", "title": "RAG with Permissions"}
---

# 

LangChain

* * *

[LangChain](https://langchain.com/) is a popular framework for working with AI, Vectors, and embeddings. LangChain supports using Supabase as a [vector store](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase), using the `pgvector` extension.

## Initializing your database[#](#initializing-your-database)

Prepare you database with the relevant tables:

1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
2.  Click **LangChain** in the Quick start section.
3.  Click **Run**.

## Usage[#](#usage)

You can now search your documents using any Node.js application. This is intended to be run on a secure server route.

```
1import { SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'2import { OpenAIEmbeddings } from '@langchain/openai'3import { createClient } from '@supabase/supabase-js'45const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY6if (!supabaseKey) throw new Error(`Expected SUPABASE_SERVICE_ROLE_KEY`)78const url = process.env.SUPABASE_URL9if (!url) throw new Error(`Expected env var SUPABASE_URL`)1011export const run = async () => {12  const client = createClient(url, supabaseKey)1314  const vectorStore = await SupabaseVectorStore.fromTexts(15    ['Hello world', 'Bye bye', "What's this?"],16    [{ id: 2 }, { id: 1 }, { id: 3 }],17    new OpenAIEmbeddings(),18    {19      client,20      tableName: 'documents',21      queryName: 'match_documents',22    }23  )2425  const resultOne = await vectorStore.similaritySearch('Hello world', 1)2627  console.log(resultOne)28}
```

### Simple metadata filtering[#](#simple-metadata-filtering)

Given the above `match_documents` Postgres function, you can also pass a filter parameter to only return documents with a specific metadata field value. This filter parameter is a JSON object, and the `match_documents` function will use the Postgres JSONB Containment operator `@>` to filter documents by the metadata field values you specify. See details on the [Postgres JSONB Containment operator](https://www.postgresql.org/docs/current/datatype-json.html#JSON-CONTAINMENT) for more information.

```
1import { SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'2import { OpenAIEmbeddings } from '@langchain/openai'3import { createClient } from '@supabase/supabase-js'45// First, follow set-up instructions above67const privateKey = process.env.SUPABASE_SERVICE_ROLE_KEY8if (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)910const url = process.env.SUPABASE_URL11if (!url) throw new Error(`Expected env var SUPABASE_URL`)1213export const run = async () => {14  const client = createClient(url, privateKey)1516  const vectorStore = await SupabaseVectorStore.fromTexts(17    ['Hello world', 'Hello world', 'Hello world'],18    [{ user_id: 2 }, { user_id: 1 }, { user_id: 3 }],19    new OpenAIEmbeddings(),20    {21      client,22      tableName: 'documents',23      queryName: 'match_documents',24    }25  )2627  const result = await vectorStore.similaritySearch('Hello world', 1, {28    user_id: 3,29  })3031  console.log(result)32}
```

### Advanced metadata filtering[#](#advanced-metadata-filtering)

You can also use query builder-style filtering ([similar to how the Supabase JavaScript library works](/docs/reference/javascript/using-filters)) instead of passing an object. Note that since the filter properties will be in the metadata column, you need to use arrow operators (`->` for integer or `->>` for text) as defined in [PostgREST API documentation](https://postgrest.org/en/stable/references/api/tables_views.html?highlight=operators#json-columns) and specify the data type of the property (e.g. the column should look something like `metadata->some_int_value::int`).

```
1import { SupabaseFilterRPCCall, SupabaseVectorStore } from '@langchain/community/vectorstores/supabase'2import { OpenAIEmbeddings } from '@langchain/openai'3import { createClient } from '@supabase/supabase-js'45// First, follow set-up instructions above67const privateKey = process.env.SUPABASE_SERVICE_ROLE_KEY8if (!privateKey) throw new Error(`Expected env var SUPABASE_SERVICE_ROLE_KEY`)910const url = process.env.SUPABASE_URL11if (!url) throw new Error(`Expected env var SUPABASE_URL`)1213export const run = async () => {14  const client = createClient(url, privateKey)1516  const embeddings = new OpenAIEmbeddings()1718  const store = new SupabaseVectorStore(embeddings, {19    client,20    tableName: 'documents',21  })2223  const docs = [24    {25      pageContent:26        'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to expand upon the notion of quantum fluff, a theoretical concept where subatomic particles coalesce to form transient multidimensional spaces. Yet, this abstraction holds no real-world application or comprehensible meaning, reflecting a cosmic puzzle.',27      metadata: { b: 1, c: 10, stuff: 'right' },28    },29    {30      pageContent:31        'This is a long text, but it actually means something because vector database does not understand Lorem Ipsum. So I would need to proceed by discussing the echo of virtual tweets in the binary corridors of the digital universe. Each tweet, like a pixelated canary, hums in an unseen frequency, a fascinatingly perplexing phenomenon that, while conjuring vivid imagery, lacks any concrete implication or real-world relevance, portraying a paradox of multidimensional spaces in the age of cyber folklore.',32      metadata: { b: 2, c: 9, stuff: 'right' },33    },34    { pageContent: 'hello', metadata: { b: 1, c: 9, stuff: 'right' } },35    { pageContent: 'hello', metadata: { b: 1, c: 9, stuff: 'wrong' } },36    { pageContent: 'hi', metadata: { b: 2, c: 8, stuff: 'right' } },37    { pageContent: 'bye', metadata: { b: 3, c: 7, stuff: 'right' } },38    { pageContent: "what's this", metadata: { b: 4, c: 6, stuff: 'right' } },39  ]4041  await store.addDocuments(docs)4243  const funcFilterA: SupabaseFilterRPCCall = (rpc) =>44    rpc45      .filter('metadata->b::int', 'lt', 3)46      .filter('metadata->c::int', 'gt', 7)47      .textSearch('content', `'multidimensional' & 'spaces'`, {48        config: 'english',49      })5051  const resultA = await store.similaritySearch('quantum', 4, funcFilterA)5253  const funcFilterB: SupabaseFilterRPCCall = (rpc) =>54    rpc55      .filter('metadata->b::int', 'lt', 3)56      .filter('metadata->c::int', 'gt', 7)57      .filter('metadata->>stuff', 'eq', 'right')5859  const resultB = await store.similaritySearch('hello', 2, funcFilterB)6061  console.log(resultA, resultB)62}
```

## Hybrid search[#](#hybrid-search)

LangChain supports the concept of a hybrid search, which combines Similarity Search with Full Text Search. Read the official docs to get started: [Supabase Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid).

You can install the LangChain Hybrid Search function though our [database.dev package manager](https://database.dev/langchain/hybrid_search).

## Resources[#](#resources)

*   Official [LangChain site](https://langchain.com/).
*   Official [LangChain docs](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase).
*   Supabase [Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid).


