---
title: "pgTAP: Unit Testing"
source: "https://supabase.com/docs/guides/database/extensions/pgtap"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pgtap"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:06.199Z"
content_hash: "ed65f62f07e31e28f813cea895b0be38ba88fb78578cd759c677ef4722fd665f"
menu_path: ["Database","Database","Extensions","Extensions","pgTAP: Unit Testing","pgTAP: Unit Testing"]
section_path: ["Database","Database","Extensions","Extensions","pgTAP: Unit Testing","pgTAP: Unit Testing"]
---
# 

pgTAP: Unit Testing

* * *

`pgTAP` is a unit testing extension for Postgres.

## Overview[#](#overview)

Let's cover some basic concepts:

*   Unit tests: allow you to test small parts of a system (like a database table!).
*   TAP: stands for [Test Anything Protocol](http://testanything.org/). It is an framework which aims to simplify the error reporting during testing.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for `pgtap` and enable the extension.

## Testing tables[#](#testing-tables)

```
1begin;2select plan( 1 );34select has_table( 'profiles' );56select * from finish();7rollback;
```

API:

*   [`has_table()`](https://pgtap.org/documentation.html#has_table): Tests whether or not a table exists in the database
*   [`has_index()`](https://pgtap.org/documentation.html#has_index): Checks for the existence of a named index associated with the named table.
*   [`has_relation()`](https://pgtap.org/documentation.html#has_relation): Tests whether or not a relation exists in the database.

## Testing columns[#](#testing-columns)

```
1begin;2select plan( 2 );34select has_column( 'profiles', 'id' ); -- test that the "id" column exists in the "profiles" table5select col_is_pk( 'profiles', 'id' ); -- test that the "id" column is a primary key67select * from finish();8rollback;
```

API:

*   [`has_column()`](https://pgtap.org/documentation.html#has_column): Tests whether or not a column exists in a given table, view, materialized view or composite type.
*   [`col_is_pk()`](https://pgtap.org/documentation.html#col_is_pk): Tests whether the specified column or columns in a table is/are the primary key for that table.

## Testing RLS policies[#](#testing-rls-policies)

```
1begin;2select plan( 1 );34select policies_are(5  'public',6  'profiles',7  ARRAY [8    'Profiles are public', -- Test that there is a policy called  "Profiles are public" on the "profiles" table.9    'Profiles can only be updated by the owner'  -- Test that there is a policy called  "Profiles can only be updated by the owner" on the "profiles" table.10  ]11);1213select * from finish();14rollback;
```

API:

*   [`policies_are()`](https://pgtap.org/documentation.html#policies_are): Tests that all of the policies on the named table are only the policies that should be on that table.
*   [`policy_roles_are()`](https://pgtap.org/documentation.html#policy_roles_are): Tests whether the roles to which policy applies are only the roles that should be on that policy.
*   [`policy_cmd_is()`](https://pgtap.org/documentation.html#policy_cmd_is): Tests whether the command to which policy applies is same as command that is given in function arguments.

You can also use the `results_eq()` method to test that a Policy returns the correct data:

```
1begin;2select plan( 1 );34select results_eq(5    'select * from profiles()',6    $$VALUES ( 1, 'Anna'), (2, 'Bruce'), (3, 'Caryn')$$,7    'profiles() should return all users'8);91011select * from finish();12rollback;
```

API:

*   [`results_eq()`](https://pgtap.org/documentation.html#results_eq)
*   [`results_ne()`](https://pgtap.org/documentation.html#results_ne)

## Testing functions[#](#testing-functions)

```
1prepare hello_expr as select 'hello'23begin;4select plan(3);5-- You'll need to create a hello_world and is_even function6select function_returns( 'hello_world', 'text' );                   -- test if the function "hello_world" returns text7select function_returns( 'is_even', ARRAY['integer'], 'boolean' );  -- test if the function "is_even" returns a boolean8select results_eq('select * from hello_world()', 'hello_expr');          -- test if the function "hello_world" returns "hello"910select * from finish();11rollback;
```

API:

*   [`function_returns()`](https://pgtap.org/documentation.html#function_returns): Tests that a particular function returns a particular data type
*   [`is_definer()`](https://pgtap.org/documentation.html#is_definer): Tests that a function is a security definer (that is, a `setuid` function).

## Resources[#](#resources)

*   Official [`pgTAP` documentation](https://pgtap.org/)
