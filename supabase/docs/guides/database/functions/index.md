---
title: "Database Functions"
source: "https://supabase.com/docs/guides/database/functions"
canonical_url: "https://supabase.com/docs/guides/database/functions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:11.020Z"
content_hash: "b5267f065f2daa62f252229c730d2ce914110733f47435cec60b082ef2a50a1d"
menu_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Managing database functions","Managing database functions"]
section_path: ["Database","Database","Working with your database (intermediate)","Working with your database (intermediate)","Managing database functions","Managing database functions"]
nav_prev: {"path": "supabase/docs/guides/database/inspect/index.md", "title": "Debugging and monitoring"}
nav_next: {"path": "supabase/docs/guides/database/joins-and-nesting/index.md", "title": "Querying Joins and Nested tables"}
---

# 

Database Functions

* * *

Postgres has built-in support for [SQL functions](https://www.postgresql.org/docs/current/sql-createfunction.html). These functions live inside your database, and they can be [used with the API](../../reference/javascript/rpc).

## Quick demo[#](#quick-demo)

## Getting started[#](#getting-started)

Supabase provides several options for creating database functions. You can use the Dashboard or create them directly using SQL. We provide a SQL editor within the Dashboard, or you can [connect](../../guides/database/connecting-to-postgres) to your database and run the SQL queries yourself.

1.  Go to the "SQL editor" section.
2.  Click "New Query".
3.  Enter the SQL to create or replace your Database function.
4.  Click "Run" or cmd+enter (ctrl+enter).

## Simple functions[#](#simple-functions)

Let's create a basic Database Function which returns a string "hello world".

```
1create or replace function hello_world() -- 12returns text -- 23language sql -- 34as $$  -- 45  select 'hello world';  -- 56$$; --6
```

Show/Hide Details

At it's most basic a function has the following parts:

1.  `create or replace function hello_world()`: The function declaration, where `hello_world` is the name of the function. You can use either `create` when creating a new function or `replace` when replacing an existing function. Or you can use `create or replace` together to handle either.
2.  `returns text`: The type of data that the function returns. If it returns nothing, you can `returns void`.
3.  `language sql`: The language used inside the function body. This can also be a procedural language: `plpgsql`, `plpython`, etc.
4.  `as $$`: The function wrapper. Anything enclosed inside the `$$` symbols will be part of the function body.
5.  `select 'hello world';`: A simple function body. The final `select` statement inside a function body will be returned if there are no statements following it.
6.  `$$;`: The closing symbols of the function wrapper.

  

When naming your functions, make the name of the function unique as overloaded functions are not supported.

After the Function is created, we have several ways of "executing" the function - either directly inside the database using SQL, or with one of the client libraries.

```
1select hello_world();
```

## Returning data sets[#](#returning-data-sets)

Database Functions can also return data sets from [Tables](../../guides/database/tables) or Views.

For example, if we had a database with some Star Wars data inside:

#### Planets

```
1| id  | name     |2| --- | -------- |3| 1   | Tatooine |4| 2   | Alderaan |5| 3   | Kashyyyk |
```

#### People

```
1| id  | name             | planet_id |2| --- | ---------------- | --------- |3| 1   | Anakin Skywalker | 1         |4| 2   | Luke Skywalker   | 1         |5| 3   | Princess Leia    | 2         |6| 4   | Chewbacca        | 3         |
```

We could create a function which returns all the planets:

```
1create or replace function get_planets()2returns setof planets3language sql4as $$5  select * from planets;6$$;
```

Because this function returns a table set, we can also apply filters and selectors. For example, if we only wanted the first planet:

```
1select *2from get_planets()3where id = 1;
```

## Passing parameters[#](#passing-parameters)

Let's create a Function to insert a new planet into the `planets` table and return the new ID. Note that this time we're using the `plpgsql` language.

```
1create or replace function add_planet(name text)2returns bigint3language plpgsql4as $$5declare6  new_row bigint;7begin8  insert into planets(name)9  values (add_planet.name)10  returning id into new_row;1112  return new_row;13end;14$$;
```

Once again, you can execute this function either inside your database using a `select` query, or with the client libraries:

```
1select * from add_planet('Jakku');
```

## Suggestions[#](#suggestions)

### Database Functions vs Edge Functions[#](#database-functions-vs-edge-functions)

For data-intensive operations, use Database Functions, which are executed within your database and can be called remotely using the [REST and GraphQL API](../api).

For use-cases which require low-latency, use [Edge Functions](../../guides/functions), which are globally-distributed and can be written in Typescript.

### Security `definer` vs `invoker`[#](#security-definer-vs-invoker)

Postgres allows you to specify whether you want the function to be executed as the user _calling_ the function (`invoker`), or as the _creator_ of the function (`definer`). For example:

```
1create function hello_world()2returns text3language plpgsql4security definer set search_path = ''5as $$6begin7  return 'hello world';8end;9$$;
```

It is best practice to use `security invoker` (which is also the default). If you ever use `security definer`, you _must_ set the `search_path`. If you use an empty search path (`search_path = ''`), you must explicitly state the schema for every relation in the function body (e.g. `from public.table`). This limits the potential damage if you allow access to schemas which the user executing the function should not have.

### Function privileges[#](#function-privileges)

By default, database functions can be executed by any role. There are two main ways to restrict this:

1.  On a case-by-case basis. Specifically revoke permissions for functions you want to protect. Execution needs to be revoked for both `public` and the role you're restricting:
    
    ```
    1revoke execute on function public.hello_world from public;2revoke execute on function public.hello_world from anon;
    ```
    
2.  Restrict function execution by default. Specifically _grant_ access when you want a function to be executable by a specific role.
    
    To restrict all existing functions, revoke execution permissions from both `public` _and_ the role you want to restrict:
    
    ```
    1revoke execute on all functions in schema public from public;2revoke execute on all functions in schema public from anon, authenticated;
    ```
    
    To restrict all new functions, change the default privileges for both `public` _and_ the role you want to restrict:
    
    ```
    1alter default privileges in schema public revoke execute on functions from public;2alter default privileges in schema public revoke execute on functions from anon, authenticated;
    ```
    
    You can then regrant permissions for a specific function to a specific role:
    
    ```
    1grant execute on function public.hello_world to authenticated;
    ```
    

### Debugging functions[#](#debugging-functions)

You can add logs to help you debug functions. This is especially recommended for complex functions.

Good targets to log include:

*   Values of (non-sensitive) variables
*   Returned results from queries

#### General logging[#](#general-logging)

To create custom logs in the [Dashboard's Postgres Logs](/dashboard/project/_/logs/postgres-logs), you can use the `raise` keyword. By default, there are 3 observed severity levels:

*   `log`
*   `warning`
*   `exception` (error level)

```
1create function logging_example(2  log_message text,3  warning_message text,4  error_message text5)6returns void7language plpgsql8as $$9begin10  raise log 'logging message: %', log_message;11  raise warning 'logging warning: %', warning_message;1213  -- immediately ends function and reverts transaction14  raise exception 'logging error: %', error_message;15end;16$$;1718select logging_example('LOGGED MESSAGE', 'WARNING MESSAGE', 'ERROR MESSAGE');
```

#### Error handling[#](#error-handling)

You can create custom errors with the `raise exception` keywords.

A common pattern is to throw an error when a variable doesn't meet a condition:

```
1create or replace function error_if_null(some_val text)2returns text3language plpgsql4as $$5begin6  -- error if some_val is null7  if some_val is null then8    raise exception 'some_val should not be NULL';9  end if;10  -- return some_val if it is not null11  return some_val;12end;13$$;1415select error_if_null(null);
```

Value checking is common, so Postgres provides a shorthand: the `assert` keyword. It uses the following format:

```
1-- throw error when condition is false2assert <some condition>, 'message';
```

Below is an example

```
1create function assert_example(name text)2returns uuid3language plpgsql4as $$5declare6  student_id uuid;7begin8  -- save a user's id into the user_id variable9  select10    id into student_id11  from attendance_table12  where student = name;1314  -- throw an error if the student_id is null15  assert student_id is not null, 'assert_example() ERROR: student not found';1617  -- otherwise, return the user's id18  return student_id;19end;20$$;2122select assert_example('Harry Potter');
```

Error messages can also be captured and modified with the `exception` keyword:

```
1create function error_example()2returns void3language plpgsql4as $$5begin6  -- fails: cannot read from nonexistent table7  select * from table_that_does_not_exist;89  exception10      when others then11          raise exception 'An error occurred in function <function name>: %', sqlerrm;12end;13$$;
```

#### Advanced logging[#](#advanced-logging)

For more complex functions or complicated debugging, try logging:

*   Formatted variables
*   Individual rows
*   Start and end of function calls

```
1create or replace function advanced_example(num int default 10)2returns text3language plpgsql4as $$5declare6    var1 int := 20;7    var2 text;8begin9    -- Logging start of function10    raise log 'logging start of function call: (%)', (select now());1112    -- Logging a variable from a SELECT query13    select14      col_1 into var115    from some_table16    limit 1;17    raise log 'logging a variable (%)', var1;1819    -- It is also possible to avoid using variables, by returning the values of your query to the log20    raise log 'logging a query with a single return value(%)', (select col_1 from some_table limit 1);2122    -- If necessary, you can even log an entire row as JSON23    raise log 'logging an entire row as JSON (%)', (select to_jsonb(some_table.*) from some_table limit 1);2425    -- When using INSERT or UPDATE, the new value(s) can be returned26    -- into a variable.27    -- When using DELETE, the deleted value(s) can be returned.28    -- All three operations use "RETURNING value(s) INTO variable(s)" syntax29    insert into some_table (col_2)30    values ('new val')31    returning col_2 into var2;3233    raise log 'logging a value from an INSERT (%)', var2;3435    return var1 || ',' || var2;36exception37    -- Handle exceptions here if needed38    when others then39        raise exception 'An error occurred in function <advanced_example>: %', sqlerrm;40end;41$$;4243select advanced_example();
```

## Resources[#](#resources)

*   Official Client libraries: [JavaScript](../../reference/javascript/rpc) and [Flutter](../../reference/dart/rpc)
*   Community client libraries: [github.com/supabase-community](https://github.com/supabase-community)
*   Postgres Official Docs: [Chapter 9. Functions and Operators](https://www.postgresql.org/docs/current/functions.html)
*   Postgres Reference: [CREATE FUNCTION](https://www.postgresql.org/docs/9.1/sql-createfunction.html)

## Deep dive[#](#deep-dive)

### Create Database Functions[#](#create-database-functions)

### Call Database Functions using JavaScript[#](#call-database-functions-using-javascript)

### Using Database Functions to call an external API[#](#using-database-functions-to-call-an-external-api)


