---
title: "postgres_fdw"
source: "https://supabase.com/docs/guides/database/extensions/postgres_fdw"
canonical_url: "https://supabase.com/docs/guides/database/extensions/postgres_fdw"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:17.282Z"
content_hash: "0a6fdbaa5614be5801738d1c0a8be530daca5563d9b68301178310e7ba055162"
menu_path: ["Database","Database","Extensions","Extensions","postgres_fdw: query data from an external Postgres server","postgres_fdw: query data from an external Postgres server"]
section_path: ["Database","Database","Extensions","Extensions","postgres_fdw: query data from an external Postgres server","postgres_fdw: query data from an external Postgres server"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/postgis/index.md", "title": "PostGIS: Geo queries"}
nav_next: {"path": "supabase/docs/guides/database/extensions/rum/index.md", "title": "RUM: improved inverted index for full-text search based on GIN index"}
---

# 

postgres\_fdw

* * *

The extension enables Postgres to query tables and views on a remote Postgres server.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "postgres\_fdw" and enable the extension.

## Create a connection to another database[#](#create-a-connection-to-another-database)

1

### Create a foreign server

Define the remote database address

```
1create server "<foreign_server_name>"2    foreign data wrapper postgres_fdw3    options (4        host '<host>',5        port '<port>',6        dbname '<dbname>'7    );
```

2

### Create a server mapping

Set the user credentials for the remote server

```
1create user mapping for "<dbname>"2server "<foreign_server_name>"3options (4    user '<db_user>',5    password '<password>'6);
```

3

### Import tables

Import tables from the foreign database

Example: Import all tables from a schema

```
1import foreign schema "<foreign_schema>"2from server "<foreign_server>"3into "<host_schema>";
```

Example: Import specific tables

```
1import foreign schema "<foreign_schema>"2limit to (3    "<table_name1>",4    "<table_name2>"5)6from server "<foreign_server>"7into "<host_schema>";
```

4

### Query foreign table

```
1select * from "<foreign_table>"
```

### Configuring execution options[#](#configuring-execution-options)

#### Fetch\_size[#](#fetchsize)

Maximum rows fetched per operation. For example, fetching 200 rows with `fetch_size` set to 100 requires 2 requests.

```
1alter server "<foreign_server_name>"2options (fetch_size '10000');
```

#### Batch\_size[#](#batchsize)

Maximum rows inserted per cycle. For example, inserting 200 rows with `batch_size` set to 100 requires 2 requests.

```
1alter server "<foreign_server_name>"2options (batch_size '1000');
```

#### Extensions[#](#extensions)

Lists shared extensions. Without them, queries involving unlisted extension functions or operators may fail or omit references.

```
1alter server "<foreign_server_name>"2options (extensions 'vector, postgis');
```

For more server options, check the extension's [official documentation](https://www.postgresql.org/docs/current/postgres-fdw.html#POSTGRES-FDW)

## Resources[#](#resources)

*   Official [`postgres_fdw` documentation](https://www.postgresql.org/docs/current/postgres-fdw.html#POSTGRES-FDW)


