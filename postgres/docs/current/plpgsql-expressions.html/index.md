---
title: "PostgreSQL: Documentation: 18: 41.4. Expressions"
source: "https://www.postgresql.org/docs/current/plpgsql-expressions.html"
canonical_url: "https://www.postgresql.org/docs/current/plpgsql-expressions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:32.382Z"
content_hash: "654c8bb551ff9267cc238e2c371e2ca70bafcabf88b89c5cfe0fe8dff38d8791"
menu_path: ["PostgreSQL: Documentation: 18: 41.4. Expressions"]
section_path: []
nav_prev: {"path": "../plpgsql-errors-and-messages.html/index.md", "title": "PostgreSQL: Documentation: 18: 41.9.\u00a0Errors and Messages"}
nav_next: {"path": "../plpgsql-statements.html/index.md", "title": "PostgreSQL: Documentation: 18: 41.5.\u00a0Basic Statements"}
---

All expressions used in PL/pgSQL statements are processed using the server's main SQL executor. For example, when you write a PL/pgSQL statement like

IF _`expression`_ THEN ...

PL/pgSQL will evaluate the expression by feeding a query like

SELECT _`expression`_

to the main SQL engine. While forming the `SELECT` command, any occurrences of PL/pgSQL variable names are replaced by query parameters, as discussed in detail in [Section 41.11.1](https://www.postgresql.org/docs/current/plpgsql-implementation.html#PLPGSQL-VAR-SUBST "41.11.1. Variable Substitution"). This allows the query plan for the `SELECT` to be prepared just once and then reused for subsequent evaluations with different values of the variables. Thus, what really happens on first use of an expression is essentially a `PREPARE` command. For example, if we have declared two integer variables `x` and `y`, and we write

IF x < y THEN ...

what happens behind the scenes is equivalent to

PREPARE _`statement_name`_(integer, integer) AS SELECT $1 < $2;

and then this prepared statement is `EXECUTE`d for each execution of the `IF` statement, with the current values of the PL/pgSQL variables supplied as parameter values. Normally these details are not important to a PL/pgSQL user, but they are useful to know when trying to diagnose a problem. More information appears in [Section 41.11.2](https://www.postgresql.org/docs/current/plpgsql-implementation.html#PLPGSQL-PLAN-CACHING "41.11.2. Plan Caching").

Since an _`expression`_ is converted to a `SELECT` command, it can contain the same clauses that an ordinary `SELECT` would, except that it cannot include a top-level `UNION`, `INTERSECT`, or `EXCEPT` clause. Thus for example one could test whether a table is non-empty with

IF count(\*) > 0 FROM my\_table THEN ...

since the _`expression`_ between `IF` and `THEN` is parsed as though it were `SELECT count(*) > 0 FROM my_table`. The `SELECT` must produce a single column, and not more than one row. (If it produces no rows, the result is taken as NULL.)
