---
title: "Postgres.js"
source: "https://supabase.com/docs/guides/database/postgres-js"
canonical_url: "https://supabase.com/docs/guides/database/postgres-js"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:51.972Z"
content_hash: "fd884cc657ac4fec93e6091869c505519b0cc749ee3e3742b75d5e2434fc3c2c"
menu_path: ["Database","Database","ORM Quickstarts","ORM Quickstarts","Postgres.js","Postgres.js"]
section_path: ["Database","Database","ORM Quickstarts","ORM Quickstarts","Postgres.js","Postgres.js"]
nav_prev: {"path": "supabase/docs/guides/database/pgadmin/index.md", "title": "Connecting with pgAdmin"}
nav_next: {"path": "supabase/docs/guides/database/psql/index.md", "title": "Connecting with PSQL"}
---

# 

Postgres.js

* * *

### Connecting with Postgres.js[#](#connecting-with-postgresjs)

[Postgres.js](https://github.com/porsager/postgres) is a full-featured Postgres client for Node.js and Deno.

1

### Install

Install Postgres.js and related dependencies.

```
1npm i postgres
```

2

### Connect

Create a `db.js` file with the connection details.

To get your connection details, go to the [**Connect** panel](/dashboard/project/_?showConnect=true). Choose [**Transaction pooler**](/dashboard/project/_?showConnect=true&method=transaction) if you're on a platform with transient connections, such as a serverless function, and [**Session pooler**](/dashboard/project/_?showConnect=true&method=session) if you have a long-lived connection. Copy the URI and save it as the environment variable `DATABASE_URL`.

```
1// db.js2import postgres from 'postgres'34const connectionString = process.env.DATABASE_URL5const sql = postgres(connectionString)67export default sql
```

3

### Execute commands

Use the connection to execute commands.

```
1import sql from './db.js'23async function getUsersOver(age) {4  const users = await sql`5    select name, age6    from users7    where age > ${ age }8  `9  // users = Result [{ name: "Walter", age: 80 }, { name: 'Murray', age: 68 }, ...]10  return users11}
```
