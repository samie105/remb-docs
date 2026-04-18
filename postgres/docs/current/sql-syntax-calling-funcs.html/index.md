---
title: "PostgreSQL: Documentation: 18: 4.3. Calling Functions"
source: "https://www.postgresql.org/docs/current/sql-syntax-calling-funcs.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-syntax-calling-funcs.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:16.284Z"
content_hash: "f3fabd356676e0488634296f9dd01b80a1abb7b8a5af1f0bc33a35ae37f9d591"
menu_path: ["PostgreSQL: Documentation: 18: 4.3. Calling Functions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/contrib-dblink-function.html/index.md", "title": "PostgreSQL: Documentation: 18: dblink"}
nav_next: {"path": "postgres/docs/current/catalog-pg-shseclabel.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.50.\u00a0pg_shseclabel"}
---

PostgreSQL allows functions that have named parameters to be called using either _positional_ or _named_ notation. Named notation is especially useful for functions that have a large number of parameters, since it makes the associations between parameters and actual arguments more explicit and reliable. In positional notation, a function call is written with its argument values in the same order as they are defined in the function declaration. In named notation, the arguments are matched to the function parameters by name and can be written in any order. For each notation, also consider the effect of function argument types, documented in [Section 10.3](https://www.postgresql.org/docs/current/typeconv-func.html "10.3. Functions").

In either notation, parameters that have default values given in the function declaration need not be written in the call at all. But this is particularly useful in named notation, since any combination of parameters can be omitted; while in positional notation parameters can only be omitted from right to left.

PostgreSQL also supports _mixed_ notation, which combines positional and named notation. In this case, positional parameters are written first and named parameters appear after them.

The following examples will illustrate the usage of all three notations, using the following function definition:

CREATE FUNCTION concat\_lower\_or\_upper(a text, b text, uppercase boolean DEFAULT false)
RETURNS text
AS
$$
 SELECT CASE
        WHEN $3 THEN UPPER($1 || ' ' || $2)
        ELSE LOWER($1 || ' ' || $2)
        END;
$$
LANGUAGE SQL IMMUTABLE STRICT;

Function `concat_lower_or_upper` has two mandatory parameters, `a` and `b`. Additionally there is one optional parameter `uppercase` which defaults to `false`. The `a` and `b` inputs will be concatenated, and forced to either upper or lower case depending on the `uppercase` parameter. The remaining details of this function definition are not important here (see [Chapter 36](https://www.postgresql.org/docs/current/extend.html "Chapter 36. Extending SQL") for more information).

### 4.3.1. Using Positional Notation [#](#SQL-SYNTAX-CALLING-FUNCS-POSITIONAL)

Positional notation is the traditional mechanism for passing arguments to functions in PostgreSQL. An example is:

SELECT concat\_lower\_or\_upper('Hello', 'World', true);
 concat\_lower\_or\_upper
-----------------------
 HELLO WORLD
(1 row)

All arguments are specified in order. The result is upper case since `uppercase` is specified as `true`. Another example is:

SELECT concat\_lower\_or\_upper('Hello', 'World');
 concat\_lower\_or\_upper
-----------------------
 hello world
(1 row)

Here, the `uppercase` parameter is omitted, so it receives its default value of `false`, resulting in lower case output. In positional notation, arguments can be omitted from right to left so long as they have defaults.

### 4.3.2. Using Named Notation [#](#SQL-SYNTAX-CALLING-FUNCS-NAMED)

In named notation, each argument's name is specified using `=>` to separate it from the argument expression. For example:

SELECT concat\_lower\_or\_upper(a => 'Hello', b => 'World');
 concat\_lower\_or\_upper
-----------------------
 hello world
(1 row)

Again, the argument `uppercase` was omitted so it is set to `false` implicitly. One advantage of using named notation is that the arguments may be specified in any order, for example:

SELECT concat\_lower\_or\_upper(a => 'Hello', b => 'World', uppercase => true);
 concat\_lower\_or\_upper
-----------------------
 HELLO WORLD
(1 row)

SELECT concat\_lower\_or\_upper(a => 'Hello', uppercase => true, b => 'World');
 concat\_lower\_or\_upper
-----------------------
 HELLO WORLD
(1 row)

An older syntax based on ":=" is supported for backward compatibility:

SELECT concat\_lower\_or\_upper(a := 'Hello', uppercase := true, b := 'World');
 concat\_lower\_or\_upper
-----------------------
 HELLO WORLD
(1 row)

### 4.3.3. Using Mixed Notation [#](#SQL-SYNTAX-CALLING-FUNCS-MIXED)

The mixed notation combines positional and named notation. However, as already mentioned, named arguments cannot precede positional arguments. For example:

SELECT concat\_lower\_or\_upper('Hello', 'World', uppercase => true);
 concat\_lower\_or\_upper
-----------------------
 HELLO WORLD
(1 row)

In the above query, the arguments `a` and `b` are specified positionally, while `uppercase` is specified by name. In this example, that adds little except documentation. With a more complex function having numerous parameters that have default values, named or mixed notation can save a great deal of writing and reduce chances for error.

### Note

Named and mixed call notations currently cannot be used when calling an aggregate function (but they do work when an aggregate function is used as a window function).

