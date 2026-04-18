---
title: "PostgreSQL: Documentation: 18: DROP DATABASE"
source: "https://www.postgresql.org/docs/current/sql-dropdatabase.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropdatabase.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:53.434Z"
content_hash: "62d6a80a98d7d19ecb324b0620cb0cc03da7b8ef0f104b3437c6bdaf825a8cf1"
menu_path: ["PostgreSQL: Documentation: 18: DROP DATABASE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/plpython-funcs.html/index.md", "title": "PostgreSQL: Documentation: 18: 44.1.\u00a0PL/Python Functions"}
nav_next: {"path": "postgres/docs/current/release-18-2.html/index.md", "title": "PostgreSQL: Documentation: 18: E.2.\u00a0Release 18.2"}
---

DROP DATABASE — remove a database

## Synopsis

DROP DATABASE \[ IF EXISTS \] _`name`_ \[ \[ WITH \] ( _`option`_ \[, ...\] ) \]

where _`option`_ can be:

    FORCE

## Description

`DROP DATABASE` drops a database. It removes the catalog entries for the database and deletes the directory containing the data. It can only be executed by the database owner. It cannot be executed while you are connected to the target database. (Connect to `postgres` or any other database to issue this command.) Also, if anyone else is connected to the target database, this command will fail unless you use the `FORCE` option described below.

`DROP DATABASE` cannot be undone. Use it with care!

## Parameters

`IF EXISTS`

Do not throw an error if the database does not exist. A notice is issued in this case.

_`name`_

The name of the database to remove.

`FORCE`

Attempt to terminate all existing connections to the target database. It doesn't terminate if prepared transactions, active logical replication slots or subscriptions are present in the target database.

This terminates background worker connections and connections that the current user has permission to terminate with `pg_terminate_backend`, described in [Section 9.28.2](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-SIGNAL "9.28.2. Server Signaling Functions"). If connections would remain, this command will fail.

## Notes

`DROP DATABASE` cannot be executed inside a transaction block.

This command cannot be executed while connected to the target database. Thus, it might be more convenient to use the program [dropdb](https://www.postgresql.org/docs/current/app-dropdb.html "dropdb") instead, which is a wrapper around this command.

## Compatibility

There is no `DROP DATABASE` statement in the SQL standard.


