---
title: "plv8: JavaScript Language"
source: "https://supabase.com/docs/guides/database/extensions/plv8"
canonical_url: "https://supabase.com/docs/guides/database/extensions/plv8"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:12.781Z"
content_hash: "0f918fcbd11178b4df90552fc7795157b862e00b161c4dcdec945998b4e1e5ef"
menu_path: ["Database","Database","Extensions","Extensions","plv8 (deprecated)","plv8 (deprecated)"]
section_path: ["Database","Database","Extensions","Extensions","plv8 (deprecated)","plv8 (deprecated)"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/plpgsql_check/index.md", "title": "plpgsql_check: PL/pgSQL Linter"}
nav_next: {"path": "supabase/docs/guides/database/extensions/postgis/index.md", "title": "PostGIS: Geo queries"}
---

# 

plv8: JavaScript Language

* * *

The `plv8` extension is deprecated in projects using Postgres 17. It continues to be supported in projects using Postgres 15, but will need to dropped before those projects are upgraded to Postgres 17. See the [Upgrading to Postgres 17 notes](/docs/guides/platform/upgrading#upgrading-to-postgres-17) for more information.

The `plv8` extension allows you use JavaScript within Postgres.

## Overview[#](#overview)

While Postgres natively runs SQL, it can also run other procedural languages. `plv8` allows you to run JavaScript code - specifically any code that runs on the [V8 JavaScript engine](https://v8.dev).

It can be used for database functions, triggers, queries and more.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "plv8" and enable the extension.

## Create `plv8` functions[#](#create-plv8-functions)

Functions written in `plv8` are written just like any other Postgres functions, only with the `language` identifier set to `plv8`.

```
1create or replace function function_name()2returns void as $$3    // V8 JavaScript4    // code5    // here6$$ language plv8;
```

You can call `plv8` functions like any other Postgres function:

```
1select function_name();
```

## Examples[#](#examples)

### Scalar functions[#](#scalar-functions)

A [scalar function](https://plv8.github.io/#scalar-function-calls) is anything that takes in some user input and returns a single result.

```
1create or replace function hello_world(name text)2returns text as $$34    let output = `Hello, ${name}!`;5    return output;67$$ language plv8;
```

### Executing SQL[#](#executing-sql)

You can execute SQL within `plv8` code using the [`plv8.execute` function](https://plv8.github.io/#plv8-execute).

```
1create or replace function update_user(id bigint, first_name text)2returns smallint as $$34    var num_affected = plv8.execute(5        'update profiles set first_name = $1 where id = $2',6        [first_name, id]7    );89    return num_affected;10$$ language plv8;
```

### Set-returning functions[#](#set-returning-functions)

A [set-returning function](https://plv8.github.io/#set-returning-function-calls) is anything that returns a full set of results - for example, rows in a table.

```
1create or replace function get_messages()2returns setof messages as $$34    var json_result = plv8.execute(5        'select * from messages'6    );78    return json_result;9$$ language plv8;1011select * from get_messages();
```

## Resources[#](#resources)

*   Official [`plv8` documentation](https://plv8.github.io/)
*   [plv8 GitHub Repository](https://github.com/plv8/plv8)
