---
title: "plpgsql_check: PL/pgSQL Linter"
source: "https://supabase.com/docs/guides/database/extensions/plpgsql_check"
canonical_url: "https://supabase.com/docs/guides/database/extensions/plpgsql_check"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:10.274Z"
content_hash: "ad85db2459ef8712732d77127a94a3f70260acab1f132cac7c0b40861477b1f3"
menu_path: ["Database","Database","Extensions","Extensions","plpgsql_check: PL/pgSQL Linter","plpgsql_check: PL/pgSQL Linter"]
section_path: ["Database","Database","Extensions","Extensions","plpgsql_check: PL/pgSQL Linter","plpgsql_check: PL/pgSQL Linter"]
---
# 

plpgsql\_check: PL/pgSQL Linter

* * *

[plpgsql\_check](https://github.com/okbob/plpgsql_check) is a Postgres extension that lints plpgsql for syntax, semantic and other related issues. The tool helps developers to identify and correct errors before executing the code. plpgsql\_check is most useful for developers who are working with large or complex SQL codebases, as it can help identify and resolve issues early in the development cycle.

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "plpgsql\_check" and enable the extension.

## API[#](#api)

*   [`plpgsql_check_function( ... )`](https://github.com/okbob/plpgsql_check#active-mode): Scans a function for errors.

`plpgsql_check_function` is highly customizable. For a complete list of available arguments see [the docs](https://github.com/okbob/plpgsql_check#arguments)

## Usage[#](#usage)

To demonstrate `plpgsql_check` we can create a function with a known error. In this case we create a function `some_func`, that references a non-existent column `place.created_at`.

```
1create table place(2  x float,3  y float4);56create or replace function public.some_func()7  returns void8  language plpgsql9as $$10declare11  rec record;12begin13  for rec in select * from place14  loop15    -- Bug: There is no column `created_at` on table `place`16    raise notice '%', rec.created_at;17  end loop;18end;19$$;
```

Note that executing the function would not catch the invalid reference error because the `loop` does not execute if no rows are present in the table.

```
1select public.some_func();2  some_func3 ───────────45 (1 row)
```

Now we can use plpgsql\_check's `plpgsql_check_function` function to identify the known error.

```
1select plpgsql_check_function('public.some_func()');23                   plpgsql_check_function4------------------------------------------------------------5 error:42703:8:RAISE:record "rec" has no field "created_at"6 Context: SQL expression "rec.created_at"
```

## Resources[#](#resources)

*   Official [`plpgsql_check` documentation](https://github.com/okbob/plpgsql_check)
