---
title: "Drizzle HTTP proxy"
source: "https://orm.drizzle.team/docs/connect-drizzle-proxy"
canonical_url: "https://orm.drizzle.team/docs/connect-drizzle-proxy"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T18:28:34.464Z"
content_hash: "596140daad9b2c49a65f017f8762a9a33f378e036dd4ebb8bd239af0f7ee3018"
menu_path: ["Drizzle HTTP proxy"]
section_path: []
content_language: "en"
---
How an HTTP Proxy works and why you might need it

Drizzle Proxy is used when you need to implement your own driver communication with the database. It can be used in several cases, such as adding custom logic at the query stage with existing drivers. The most common use is with an HTTP driver, which sends queries to your server with the database, executes the query on your database, and responds with raw data that Drizzle ORM can then map to results

How it works under the hood?

```plaintext
┌───────────────────────────┐                 ┌─────────────────────────────┐              
│       Drizzle ORM         │                 │  HTTP Server with Database  │             
└─┬─────────────────────────┘                 └─────────────────────────┬───┘             
  │                                                ^                    │
  │-- 1. Build query         2. Send built query --│                    │
  │                                                │                    │
  │              ┌───────────────────────────┐     │                    │
  └─────────────>│                           │─────┘                    │ 
                 │      HTTP Proxy Driver    │                          │
  ┌──────────────│                           │<─────────────┬───────────┘
  │              └───────────────────────────┘              │
  │                                                  3. Execute a query + send raw results back
  │-- 4. Map data and return        
  │                   
  v
```

Drizzle ORM also supports simply using asynchronous callback function for executing SQL.

-   `sql` is a query string with placeholders.
-   `params` is an array of parameters.
-   One of the following values will set for `method` depending on the SQL statement - `run`, `all`, `values` or `get`.

Drizzle always waits for `{rows: string[][]}` or `{rows: string[]}` for the return value.

-   When the `method` is `get`, you should return a value as `{rows: string[]}`.
-   Otherwise, you should return `{rows: string[][]}`.

  

```typescript
// Example of driver implementation
import { drizzle } from 'drizzle-orm/pg-proxy';

const db = drizzle(async (sql, params, method) => {
  try {
    const rows = await axios.post('http://localhost:3000/query', { sql, params, method });

    return { rows: rows.data };
  } catch (e: any) {
    console.error('Error from pg proxy server: ', e.response.data)
    return { rows: [] };
  }
});
```

```ts
// Example of server implementation
import { Client } from 'pg';
import express from 'express';

const app = express();

app.use(express.json());
const port = 3000;

const client = new Client('postgres://postgres:postgres@localhost:5432/postgres');

app.post('/query', async (req, res) => {
  const { sql, params, method } = req.body;

  // prevent multiple queries
  const sqlBody = sql.replace(/;/g, '');

  try {
    const result = await client.query({
      text: sqlBody,
      values: params,
      rowMode: method === 'all' ? 'array': undefined,
    });
    res.send(result.rows);
  } catch (e: any) {
    res.status(500).json({ error: e });
  }

  res.status(500).json({ error: 'Unknown method value' });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
```
