---
title: "Automatic embeddings"
source: "https://supabase.com/docs/guides/ai/automatic-embeddings"
canonical_url: "https://supabase.com/docs/guides/ai/automatic-embeddings"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:18.928Z"
content_hash: "175eb48f10c6d695004028795df0f64eccf43b99a0b95b10d2625dea3fc2f9c7"
menu_path: ["AI & Vectors","AI & Vectors","Learn","Learn","Automatic embeddings","Automatic embeddings"]
section_path: ["AI & Vectors","AI & Vectors","Learn","Learn","Automatic embeddings","Automatic embeddings"]
nav_prev: {"path": "supabase/docs/guides/ai/index.md", "title": "AI & Vectors"}
nav_next: {"path": "supabase/docs/guides/ai/choosing-compute-addon/index.md", "title": "Choosing your Compute Add-on"}
---

# 

Automatic embeddings

* * *

Vector embeddings enable powerful [semantic search](/docs/guides/ai/semantic-search) capabilities in Postgres, but managing them alongside your content has traditionally been complex. This guide demonstrates how to automate embedding generation and updates using Supabase [Edge Functions](/docs/guides/functions), [pgmq](/docs/guides/database/extensions/pgmq), [pg\_net](/docs/guides/database/extensions/pg_net), and [pg\_cron](/docs/guides/cron).

## Understanding the challenge[#](#understanding-the-challenge)

When implementing semantic search with pgvector, developers typically need to:

1.  Generate embeddings via an external API (like OpenAI)
2.  Store these embeddings alongside the content
3.  Keep embeddings in sync when content changes
4.  Handle failures and retries in the embedding generation process

While Postgres [full-text search](/docs/guides/database/full-text-search) can handle this internally through synchronous calls to `to_tsvector` and [triggers](https://www.postgresql.org/docs/current/textsearch-features.html#TEXTSEARCH-UPDATE-TRIGGERS), semantic search requires asynchronous API calls to a provider like OpenAI to generate vector embeddings. This guide demonstrates how to use triggers, queues, and Supabase Edge Functions to bridge this gap.

## Understanding the architecture[#](#understanding-the-architecture)

We'll leverage the following Postgres and Supabase features to create the automated embedding system:

1.  [pgvector](/docs/guides/database/extensions/pgvector): Stores and queries vector embeddings
2.  [pgmq](/docs/guides/queues): Queues embedding generation requests for processing and retries
3.  [pg\_net](/docs/guides/database/extensions/pg_net): Handles asynchronous HTTP requests to Edge Functions directly from Postgres
4.  [pg\_cron](/docs/guides/cron): Automatically processes and retries embedding generations
5.  [Triggers](/docs/guides/database/postgres/triggers): Detects content changes and enqueues embedding generation requests
6.  [Edge Functions](/docs/guides/functions): Generates embeddings via an API like OpenAI (customizable)

We'll design the system to:

1.  Be generic, so that it can be used with any table and content. This allows you to configure embeddings in multiple places, each with the ability to customize the input used for embedding generation. These will all use the same queue infrastructure and Edge Function to generate the embeddings.
    
2.  Handle failures gracefully, by retrying failed jobs and providing detailed information about the status of each job.
    

## Implementation[#](#implementation)

We'll start by setting up the infrastructure needed to queue and process embedding generation requests. Then we'll create an example table with triggers to enqueue these embedding requests whenever content is inserted or updated.

### Step 1: Enable extensions[#](#step-1-enable-extensions)

First, let's enable the required extensions:

```
1-- For vector operations2create extension if not exists vector3with4  schema extensions;56-- For queueing and processing jobs7-- (pgmq will create its own schema)8create extension if not exists pgmq;910-- For async HTTP requests11create extension if not exists pg_net12with13  schema extensions;1415-- For scheduled processing and retries16-- (pg_cron will create its own schema)17create extension if not exists pg_cron;1819-- For clearing embeddings during updates20create extension if not exists hstore21with22  schema extensions;
```

Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension". To disable an extension, call `drop extension`.

### Step 2: Create utility functions[#](#step-2-create-utility-functions)

Before we set up our embedding logic, we need to create some utility functions:

```
1-- Schema for utility functions2create schema util;34-- Utility function to get the Supabase project URL (required for Edge Functions)5create function util.project_url()6returns text7language plpgsql8security definer9as $$10declare11  secret_value text;12begin13  -- Retrieve the project URL from Vault14  select decrypted_secret into secret_value from vault.decrypted_secrets where name = 'project_url';15  return secret_value;16end;17$$;1819-- Generic function to invoke any Edge Function20create or replace function util.invoke_edge_function(21  name text,22  body jsonb,23  timeout_milliseconds int = 5 * 60 * 1000  -- default 5 minute timeout24)25returns void26language plpgsql27as $$28declare29  headers_raw text;30  auth_header text;31begin32  -- If we're in a PostgREST session, reuse the request headers for authorization33  headers_raw := current_setting('request.headers', true);3435  -- Only try to parse if headers are present36  auth_header := case37    when headers_raw is not null then38      (headers_raw::json->>'authorization')39    else40      null41  end;4243  -- Perform async HTTP request to the edge function44  perform net.http_post(45    url => util.project_url() || '/functions/v1/' || name,46    headers => jsonb_build_object(47      'Content-Type', 'application/json',48      'Authorization', auth_header49    ),50    body => body,51    timeout_milliseconds => timeout_milliseconds52  );53end;54$$;5556-- Generic trigger function to clear a column on update57create or replace function util.clear_column()58returns trigger59language plpgsql as $$60declare61    clear_column text := TG_ARGV[0];62begin63    NEW := NEW #= hstore(clear_column, NULL);64    return NEW;65end;66$$;
```

Here we create:

*   A schema `util` to store utility functions.
*   A function to retrieve the Supabase project URL from [Vault](/docs/guides/database/vault). We'll add this secret next.
*   A generic function to invoke any Edge Function with a given name and request body.
*   A generic trigger function to clear a column on update. This function accepts the column name as an argument and sets it to `NULL` in the `NEW` record. We'll explain how to use this function later.

Every project has a unique API URL that is required to invoke Edge Functions. Let's go ahead and add the project URL secret to Vault depending on your environment.

When working with a local Supabase stack, add the following to your `supabase/seed.sql` file:

```
1select2  vault.create_secret('http://api.supabase.internal:8000', 'project_url');
```

When deploying to the cloud platform, open the [SQL editor](/dashboard/project/_/sql/new) and run the following, replacing `<project-url>` with your [project's API URL](/dashboard/project/_/settings/api):

```
1select2  vault.create_secret('<project-url>', 'project_url');
```

### Step 3: Create queue and triggers[#](#step-3-create-queue-and-triggers)

Our goal is to automatically generate embeddings whenever content is inserted or updated within a table. We can use triggers and queues to achieve this. Our approach is to automatically queue embedding jobs whenever records are inserted or updated in a table, then process them asynchronously using a cron job. If a job fails, it will remain in the queue and be retried in the next scheduled task.

First we create a `pgmq` queue for processing embedding requests:

```
1-- Queue for processing embedding jobs2select pgmq.create('embedding_jobs');
```

Next we create a trigger function to queue embedding jobs. We'll use this function to handle both insert and update events:

```
1-- Generic trigger function to queue embedding jobs2create or replace function util.queue_embeddings()3returns trigger4language plpgsql5security definer6set search_path = ''7as $$8declare9  content_function text = TG_ARGV[0];10  embedding_column text = TG_ARGV[1];11begin12  perform pgmq.send(13    queue_name => 'embedding_jobs',14    msg => jsonb_build_object(15      'id', NEW.id,16      'schema', TG_TABLE_SCHEMA,17      'table', TG_TABLE_NAME,18      'contentFunction', content_function,19      'embeddingColumn', embedding_column20    )21  );22  return NEW;23end;24$$;
```

Our `util.queue_embeddings` trigger function is generic and can be used with any table and content function. It accepts two arguments:

1.  `content_function`: The name of a function that returns the text content to be embedded. The function should accept a single row as input and return text (see the `embedding_input` example).
    
    This allows you to customize the text input passed to the embedding model - for example, you could concatenate multiple columns together like `title` and `content` and use the result as input.
    
2.  `embedding_column`: The name of the destination column where the embedding will be stored.
    

Note that the `util.queue_embeddings` trigger function requires a `for each row` clause to work correctly. See [Usage](#usage) for an example of how to use this trigger function with your table.

Next we'll create a function to process the embedding jobs. This function will read jobs from the queue, group them into batches, and invoke the Edge Function to generate embeddings. We'll use `pg_cron` to schedule this function to run every 10 seconds.

```
1-- Function to process embedding jobs from the queue2create or replace function util.process_embeddings(3  batch_size int = 10,4  max_requests int = 10,5  timeout_milliseconds int = 5 * 60 * 1000 -- default 5 minute timeout6)7returns void8language plpgsql9as $$10declare11  job_batches jsonb[];12  batch jsonb;13begin14  with15    -- First get jobs and assign batch numbers16    numbered_jobs as (17      select18        message || jsonb_build_object('jobId', msg_id) as job_info,19        (row_number() over (order by 1) - 1) / batch_size as batch_num20      from pgmq.read(21        queue_name => 'embedding_jobs',22        vt => timeout_milliseconds / 1000,23        qty => max_requests * batch_size24      )25    ),26    -- Then group jobs into batches27    batched_jobs as (28      select29        jsonb_agg(job_info) as batch_array,30        batch_num31      from numbered_jobs32      group by batch_num33    )34  -- Finally aggregate all batches into array35  select array_agg(batch_array)36  from batched_jobs37  into job_batches;3839  -- Invoke the embed edge function for each batch40  foreach batch in array job_batches loop41    perform util.invoke_edge_function(42      name => 'embed',43      body => batch,44      timeout_milliseconds => timeout_milliseconds45    );46  end loop;47end;48$$;4950-- Schedule the embedding processing51select52  cron.schedule(53    'process-embeddings',54    '10 seconds',55    $$56    select util.process_embeddings();57    $$58  );
```

Let's discuss some common questions about this approach:

#### Why not generate all embeddings in a single Edge Function request?[#](#why-not-generate-all-embeddings-in-a-single-edge-function-request)

While this is possible, it can lead to long processing times and potential timeouts. Batching allows us to process multiple embeddings concurrently and handle failures more effectively.

#### Why not one request per row?[#](#why-not-one-request-per-row)

This approach can lead to API rate limiting and performance issues. Batching provides a balance between efficiency and reliability.

#### Why queue requests instead of processing them immediately?[#](#why-queue-requests-instead-of-processing-them-immediately)

Queuing allows us to handle failures gracefully, retry requests, and manage concurrency more effectively. Specifically we are using `pgmq`'s visibility timeouts to ensure that failed requests are retried.

#### How do visibility timeouts work?[#](#how-do-visibility-timeouts-work)

Every time we read a message from the queue, we set a visibility timeout which tells `pgmq` to hide the message from other readers for a certain period. If the Edge Function fails to process the message within this period, the message becomes visible again and will be retried by the next scheduled task.

#### How do we handle retries?[#](#how-do-we-handle-retries)

We use `pg_cron` to schedule a task that reads messages from the queue and processes them. If the Edge Function fails to process a message, it becomes visible again after a timeout and can be retried by the next scheduled task.

#### Is 10 seconds a good interval for processing?[#](#is-10-seconds-a-good-interval-for-processing)

This interval is a good starting point, but you may need to adjust it based on your workload and the time it takes to generate embeddings. You can adjust the `batch_size`, `max_requests`, and `timeout_milliseconds` parameters to optimize performance.

### Step 4: Create the Edge Function[#](#step-4-create-the-edge-function)

Finally we'll create the Edge Function to generate embeddings. We'll use OpenAI's API in this example, but you can replace it with any other embedding generation service.

Use the Supabase CLI to create a new Edge Function:

```
1supabase functions new embed
```

This will create a new directory `supabase/functions/embed` with an `index.ts` file. Replace the contents of this file with the following:

_supabase/functions/embed/index.ts_:

```
1// Setup type definitions for built-in Supabase Runtime APIs2import 'jsr:@supabase/functions-js/edge-runtime.d.ts'34// We'll use the OpenAI API to generate embeddings5import OpenAI from 'jsr:@openai/openai'67import { z } from 'npm:zod'89// We'll make a direct Postgres connection to update the document10import postgres from 'https://deno.land/x/postgresjs@v3.4.5/mod.js'1112// Initialize OpenAI client13const openai = new OpenAI({14  // We'll need to manually set the `OPENAI_API_KEY` environment variable15  apiKey: Deno.env.get('OPENAI_API_KEY'),16})1718// Initialize Postgres client19const sql = postgres(20  // `SUPABASE_DB_URL` is a built-in environment variable21  Deno.env.get('SUPABASE_DB_URL')!22)2324const jobSchema = z.object({25  jobId: z.number(),26  id: z.number(),27  schema: z.string(),28  table: z.string(),29  contentFunction: z.string(),30  embeddingColumn: z.string(),31})3233const failedJobSchema = jobSchema.extend({34  error: z.string(),35})3637type Job = z.infer<typeof jobSchema>38type FailedJob = z.infer<typeof failedJobSchema>3940type Row = {41  id: string42  content: unknown43}4445const QUEUE_NAME = 'embedding_jobs'4647// Listen for HTTP requests48Deno.serve(async (req) => {49  if (req.method !== 'POST') {50    return new Response('expected POST request', { status: 405 })51  }5253  if (req.headers.get('content-type') !== 'application/json') {54    return new Response('expected json body', { status: 400 })55  }5657  // Use Zod to parse and validate the request body58  const parseResult = z.array(jobSchema).safeParse(await req.json())5960  if (parseResult.error) {61    return new Response(`invalid request body: ${parseResult.error.message}`, {62      status: 400,63    })64  }6566  const pendingJobs = parseResult.data6768  // Track jobs that completed successfully69  const completedJobs: Job[] = []7071  // Track jobs that failed due to an error72  const failedJobs: FailedJob[] = []7374  async function processJobs() {75    let currentJob: Job | undefined7677    while ((currentJob = pendingJobs.shift()) !== undefined) {78      try {79        await processJob(currentJob)80        completedJobs.push(currentJob)81      } catch (error) {82        failedJobs.push({83          ...currentJob,84          error: error instanceof Error ? error.message : JSON.stringify(error),85        })86      }87    }88  }8990  try {91    // Process jobs while listening for worker termination92    await Promise.race([processJobs(), catchUnload()])93  } catch (error) {94    // If the worker is terminating (e.g. wall clock limit reached),95    // add pending jobs to fail list with termination reason96    failedJobs.push(97      ...pendingJobs.map((job) => ({98        ...job,99        error: error instanceof Error ? error.message : JSON.stringify(error),100      }))101    )102  }103104  // Log completed and failed jobs for traceability105  console.log('finished processing jobs:', {106    completedJobs: completedJobs.length,107    failedJobs: failedJobs.length,108  })109110  return new Response(111    JSON.stringify({112      completedJobs,113      failedJobs,114    }),115    {116      // 200 OK response117      status: 200,118119      // Custom headers to report job status120      headers: {121        'content-type': 'application/json',122        'x-completed-jobs': completedJobs.length.toString(),123        'x-failed-jobs': failedJobs.length.toString(),124      },125    }126  )127})128129/**130 * Generates an embedding for the given text.131 */132async function generateEmbedding(text: string) {133  const response = await openai.embeddings.create({134    model: 'text-embedding-3-small',135    input: text,136  })137  const [data] = response.data138139  if (!data) {140    throw new Error('failed to generate embedding')141  }142143  return data.embedding144}145146/**147 * Processes an embedding job.148 */149async function processJob(job: Job) {150  const { jobId, id, schema, table, contentFunction, embeddingColumn } = job151152  // Fetch content for the schema/table/row combination153  const [row]: [Row] = await sql`154    select155      id,156      ${sql(contentFunction)}(t) as content157    from158      ${sql(schema)}.${sql(table)} t159    where160      id = ${id}161  `162163  if (!row) {164    throw new Error(`row not found: ${schema}.${table}/${id}`)165  }166167  if (typeof row.content !== 'string') {168    throw new Error(`invalid content - expected string: ${schema}.${table}/${id}`)169  }170171  const embedding = await generateEmbedding(row.content)172173  await sql`174    update175      ${sql(schema)}.${sql(table)}176    set177      ${sql(embeddingColumn)} = ${JSON.stringify(embedding)}178    where179      id = ${id}180  `181182  await sql`183    select pgmq.delete(${QUEUE_NAME}, ${jobId}::bigint)184  `185}186187/**188 * Returns a promise that rejects if the worker is terminating.189 */190function catchUnload() {191  return new Promise((reject) => {192    addEventListener('beforeunload', (ev: any) => {193      reject(new Error(ev.detail?.reason))194    })195  })196}
```

The Edge Function listens for incoming HTTP requests from `pg_net` and processes each embedding job. It is a generic worker that can handle embedding jobs for any table and column. It uses OpenAI's API to generate embeddings and updates the corresponding row in the database. It also deletes the job from the queue once it has been processed.

The function is designed to process multiple jobs independently. If one job fails, it will not affect the processing of other jobs. The function returns a `200 OK` response with a list of completed and failed jobs. We can use this information to diagnose failed jobs. See [Troubleshooting](#troubleshooting) for more details.

You will need to set the `OPENAI_API_KEY` environment variable to authenticate with OpenAI. When running the Edge Function locally, you can add it to a `.env` file:

_.env_:

```
1OPENAI_API_KEY=your-api-key
```

When you're ready to deploy the Edge Function, set can set the environment variable using the Supabase CLI:

```
1supabase secrets set --env-file .env
```

or

```
1supabase secrets set OPENAI_API_KEY=<your-api-key>
```

Alternatively, you can replace the `generateEmbedding` function with your own embedding generation logic.

See [Deploy to Production](/docs/guides/functions/deploy) for more information on how to deploy the Edge Function.

## Usage[#](#usage)

Now that the infrastructure is in place, let's go through an example of how to use this system to automatically generate embeddings for a table of documents. You can use this approach with multiple tables and customize the input for each embedding generation as needed.

### 1\. Create table to store documents with embeddings[#](#1-create-table-to-store-documents-with-embeddings)

We'll set up a new `documents` table that will store our content and embeddings:

```
1-- Table to store documents with embeddings2create table documents (3  id integer primary key generated always as identity,4  title text not null,5  content text not null,6  embedding halfvec(1536),7  created_at timestamp with time zone default now()8);910-- Index for vector search over document embeddings11create index on documents using hnsw (embedding halfvec_cosine_ops);
```

Our `documents` table stores the title and content of each document along with its vector embedding. We use a `halfvec(1536)` column to store the embeddings.

`halfvec` is a `pgvector` data type that stores float values in half precision (16 bits) to save space. Our Edge Function used OpenAI's `text-embedding-3-small` model which generates 1536-dimensional embeddings, so we use the same dimensionality here. Adjust this based on the number of dimensions your embedding model generates.

We use an [HNSW index](/docs/guides/ai/vector-indexes/hnsw-indexes) on the vector column. Note that we are choosing `halfvec_cosine_ops` as the index method, which means our future queries will need to use cosine distance (`<=>`) to find similar embeddings. Also note that HNSW indexes support a maximum of 4000 dimensions for `halfvec` vectors, so keep this in mind when choosing an embedding model. If your model generates embeddings with more than 4000 dimensions, you will need to reduce the dimensionality before indexing them. See [Matryoshka embeddings](/blog/matryoshka-embeddings) for a potential solution to shortening dimensions.

Also note that the table must have a primary key column named `id` for our triggers to work correctly with the `util.queue_embeddings` function and for our Edge Function to update the correct row.

### 2\. Create triggers to enqueue embedding jobs[#](#2-create-triggers-to-enqueue-embedding-jobs)

Now we'll set up the triggers to enqueue embedding jobs whenever content is inserted or updated:

```
1-- Customize the input for embedding generation2-- e.g. Concatenate title and content with a markdown header3create or replace function embedding_input(doc documents)4returns text5language plpgsql6immutable7as $$8begin9  return '# ' || doc.title || E'\n\n' || doc.content;10end;11$$;1213-- Trigger for insert events14create trigger embed_documents_on_insert15  after insert16  on documents17  for each row18  execute function util.queue_embeddings('embedding_input', 'embedding');1920-- Trigger for update events21create trigger embed_documents_on_update22  after update of title, content -- must match the columns in embedding_input()23  on documents24  for each row25  execute function util.queue_embeddings('embedding_input', 'embedding');
```

We create 2 triggers:

1.  `embed_documents_on_insert`: Enqueues embedding jobs whenever new rows are inserted into the `documents` table.
    
2.  `embed_documents_on_update`: Enqueues embedding jobs whenever the `title` or `content` columns are updated in the `documents` table.
    

Both of these triggers use the same `util.queue_embeddings` function that will queue the embedding jobs for processing. They accept 2 arguments:

1.  `embedding_input`: The name of the function that generates the input for embedding generation. This function allows you to customize the text input passed to the embedding model (e.g. concatenating the title and content). The function should accept a single row as input and return text.
    
2.  `embedding`: The name of the destination column where the embedding will be stored.
    

Note that the update trigger only fires when the `title` or `content` columns are updated. This is to avoid unnecessary updates to the embedding column when other columns are updated. Make sure that these columns match the columns used in the `embedding_input` function.

#### (Optional) Clearing embeddings on update[#](#optional-clearing-embeddings-on-update)

Note that our trigger will enqueue new embedding jobs when content is updated, but it will not clear any existing embeddings. This means that an embedding can be temporarily out of sync with the content until the new embedding is generated and updated.

If it is more important to have _accurate_ embeddings than _any_ embedding, you can add another trigger to clear the existing embedding until the new one is generated:

```
1-- Trigger to clear the embedding column on update2create trigger clear_document_embedding_on_update3  before update of title, content -- must match the columns in embedding_input()4  on documents5  for each row6  execute function util.clear_column('embedding');
```

`util.clear_column` is a generic trigger function we created earlier that can be used to clear any column in a table.

*   It accepts the column name as an argument. This column must be nullable.
*   It requires a `before` trigger with a `for each row` clause.
*   It requires the `hstore` extension we created earlier.

This example will clear the `embedding` column whenever the `title` or `content` columns are updated (note the `of title, content` clause). This ensures that the embedding is always in sync with the title and content, but it will result in temporary gaps in search results until the new embedding is generated.

We intentionally use a `before` trigger because it allows us to modify the record before it's written to disk, avoiding an extra `update` statement that would be needed with an `after` trigger.

### 3\. Insert and update documents[#](#3-insert-and-update-documents)

Let's insert a new document and update its content to see the embedding generation in action:

```
1-- Insert a new document2insert into documents (title, content)3values4  ('Understanding Vector Databases', 'Vector databases are specialized...');56-- Immediately check the embedding column7select id, embedding8from documents9where title = 'Understanding Vector Databases';
```

You should observe that the `embedding` column is initially `null` after inserting the document. This is because the embedding generation is asynchronous and will be processed by the Edge Function in the next scheduled task.

Wait up to 10 seconds for the next task to run, then check the `embedding` column again:

```
1select id, embedding2from documents3where title = 'Understanding Vector Databases';
```

You should see the generated embedding for the document.

Next let's update the content of the document:

```
1-- Update the content of the document2update documents3set content = 'Vector databases allow you to query...'4where title = 'Understanding Vector Databases';56-- Immediately check the embedding column7select id, embedding8from documents9where title = 'Understanding Vector Databases';
```

You should observe that the `embedding` column is reset to `null` after updating the content. This is because of the trigger we added to clear existing embeddings whenever the content is updated. The embedding will be regenerated by the Edge Function in the next scheduled task.

Wait up to 10 seconds for the next task to run, then check the `embedding` column again:

```
1select id, embedding2from documents3where title = 'Understanding Vector Databases';
```

You should see the updated embedding for the document.

Finally we'll update the title of the document:

```
1-- Update the title of the document2update documents3set title = 'Understanding Vector Databases with Supabase'4where title = 'Understanding Vector Databases';
```

You should observe that the `embedding` column is once again reset to `null` after updating the title. This is because the trigger we added to clear existing embeddings fires when either the `content` or `title` columns are updated. The embedding will be regenerated by the Edge Function in the next scheduled task.

Wait up to 10 seconds for the next task to run, then check the `embedding` column again:

```
1select id, embedding2from documents3where title = 'Understanding Vector Databases with Supabase';
```

You should see the updated embedding for the document.

## Troubleshooting[#](#troubleshooting)

The `embed` Edge Function processes a batch of embedding jobs and returns a `200 OK` response with a list of completed and failed jobs in the body. For example:

```
1{2  "completedJobs": [3    {4      "jobId": "1",5      "id": "1",6      "schema": "public",7      "table": "documents",8      "contentFunction": "embedding_input",9      "embeddingColumn": "embedding"10    }11  ],12  "failedJobs": [13    {14      "jobId": "2",15      "id": "2",16      "schema": "public",17      "table": "documents",18      "contentFunction": "embedding_input",19      "embeddingColumn": "embedding",20      "error": "error connecting to openai api"21    }22  ]23}
```

It also returns the number of completed and failed jobs in the response headers. For example:

```
1x-completed-jobs: 12x-failed-jobs: 1
```

You can also use the `x-deno-execution-id` header to trace the execution of the Edge Function within the [dashboard](/dashboard/project/_/functions) logs.

Each failed job includes an `error` field with a description of the failure. Reasons for a job failing could include:

*   An error generating the embedding via external API
*   An error connecting to the database
*   The edge function being terminated (e.g. due to a wall clock limit)
*   Any other error thrown during processing

`pg_net` stores HTTP responses in the `net._http_response` table, which can be queried to diagnose issues with the embedding generation process.

```
1select2  *3from4  net._http_response5where6  (headers->>'x-failed-jobs')::int > 0;
```

## Conclusion[#](#conclusion)

Automating embedding generation and updates in Postgres allow you to build powerful semantic search capabilities without the complexity of managing embeddings manually.

By combining Postgres features like triggers, queues, and other extensions with Supabase Edge Functions, we can create a robust system that handles embedding generation asynchronously and retries failed jobs automatically.

This system can be customized to work with any content and embedding generation service, providing a flexible and scalable solution for semantic search in Postgres.

## See also[#](#see-also)

*   [What are embeddings?](/docs/guides/ai/concepts)
*   [Semantic search](/docs/guides/ai/semantic-search)
*   [Vector indexes](/docs/guides/ai/vector-indexes)
*   [Supabase Edge Functions](/docs/guides/functions)
