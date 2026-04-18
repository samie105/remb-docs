---
title: "Integrating with Supabase Database (Postgres)"
source: "https://supabase.com/docs/guides/functions/connect-to-postgres"
canonical_url: "https://supabase.com/docs/guides/functions/connect-to-postgres"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:55.676Z"
content_hash: "6a7085af25778f23a8ed0c78d8f3b4986f7ff58f2cb4d7dcdd9b71edda312f00"
menu_path: ["Edge Functions","Edge Functions","Integrations","Integrations","Supabase Database (Postgres)","Supabase Database (Postgres)"]
section_path: ["Edge Functions","Edge Functions","Integrations","Integrations","Supabase Database (Postgres)","Supabase Database (Postgres)"]
nav_prev: {"path": "supabase/docs/guides/functions/compression/index.md", "title": "Handling Compressed Requests"}
nav_next: {"path": "supabase/docs/guides/functions/cors/index.md", "title": "CORS (Cross-Origin Resource Sharing) support for Invoking from the browser"}
---

# 

Integrating with Supabase Database (Postgres)

## 

Connect to your Postgres database from Edge Functions.

* * *

Connect to your Postgres database from an Edge Function by using the `supabase-js` client. You can also use other Postgres clients like [Deno Postgres](https://deno.land/x/postgres)

* * *

## Using supabase-js[#](#using-supabase-js)

The `supabase-js` client handles authorization with Row Level Security and automatically formats responses as JSON. This is the recommended approach for most applications:

```
1import { createClient } from 'npm:@supabase/supabase-js@2'23Deno.serve(async (req) => {4  try {5    const supabase = createClient(6      Deno.env.get('SUPABASE_URL') ?? '',7      Deno.env.get('SUPABASE_PUBLISHABLE_KEY') ?? '',8      { global: { headers: { Authorization: req.headers.get('Authorization')! } } }9    )1011    const { data, error } = await supabase.from('countries').select('*')1213    if (error) {14      throw error15    }1617    return new Response(JSON.stringify({ data }), {18      headers: { 'Content-Type': 'application/json' },19      status: 200,20    })21  } catch (err) {22    return new Response(String(err?.message ?? err), { status: 500 })23  }24})
```

This enables:

*   Automatic Row Level Security enforcement
*   Built-in JSON serialization
*   Consistent error handling
*   TypeScript support for database schema

* * *

## Using a Postgres client[#](#using-a-postgres-client)

Because Edge Functions are a server-side technology, it's safe to connect directly to your database using any popular Postgres client. This means you can run raw SQL from your Edge Functions.

Here is how you can connect to the database using Deno Postgres driver and run raw SQL. Check out the [full example](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/postgres-on-the-edge).

```
1import { Pool } from 'https://deno.land/x/postgres@v0.17.0/mod.ts'23// Create a database pool with one connection.4const pool = new Pool(5  {6    tls: { enabled: false },7    database: 'postgres',8    hostname: Deno.env.get('DB_HOSTNAME'),9    user: Deno.env.get('DB_USER'),10    port: 6543,11    password: Deno.env.get('DB_PASSWORD'),12  },13  114)1516Deno.serve(async (_req) => {17  try {18    // Grab a connection from the pool19    const connection = await pool.connect()2021    try {22      // Run a query23      const result = await connection.queryObject`SELECT * FROM animals`24      const animals = result.rows // [{ id: 1, name: "Lion" }, ...]2526      // Encode the result as pretty printed JSON27      const body = JSON.stringify(28        animals,29        (_key, value) => (typeof value === 'bigint' ? value.toString() : value),30        231      )3233      // Return the response with the correct content type header34      return new Response(body, {35        status: 200,36        headers: {37          'Content-Type': 'application/json; charset=utf-8',38        },39      })40    } finally {41      // Release the connection back into the pool42      connection.release()43    }44  } catch (err) {45    console.error(err)46    return new Response(String(err?.message ?? err), { status: 500 })47  }48})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/postgres-on-the-edge/index.ts)

* * *

## Using Drizzle[#](#using-drizzle)

You can use Drizzle together with [Postgres.js](https://github.com/porsager/postgres). Both can be loaded directly from npm:

**Set up dependencies in `import_map.json`**:

```
1{2  "imports": {3    "drizzle-orm": "npm:drizzle-orm@0.29.1",4    "drizzle-orm/": "npm:/drizzle-orm@0.29.1/",5    "postgres": "npm:postgres@3.4.3"6  }7}
```

**Use in your function**:

```
1import { drizzle } from 'drizzle-orm/postgres-js'2import postgres from 'postgres'3import { countries } from '../_shared/schema.ts'45const connectionString = Deno.env.get('SUPABASE_DB_URL')!67Deno.serve(async (_req) => {8  // Disable prefetch as it is not supported for "Transaction" pool mode9  const client = postgres(connectionString, { prepare: false })10  const db = drizzle(client)11  const allCountries = await db.select().from(countries)1213  return Response.json(allCountries)14})
```

You can find the full example on [GitHub](https://github.com/thorwebdev/edgy-drizzle).

* * *

## SSL connections[#](#ssl-connections)

### Production[#](#production)

Deployed edge functions are pre-configured to use SSL for connections to the Supabase database. You don't need to add any extra configurations.

### Local development[#](#local-development)

If you want to use SSL connections during local development, follow these steps:

1.  Download the SSL certificate from [Database Settings](/dashboard/project/_/database/settings)
2.  Add to your [local .env file](/docs/guides/functions/secrets), add these two variables:

```
1SSL_CERT_FILE=/path/to/cert.crt # set the path to the downloaded cert2DENO_TLS_CA_STORE=mozilla,system
```

Then, restart your local development server:

```
1supabase functions serve your-function
```

