---
title: "PostgreSQL: Documentation: 18: WHENEVER"
source: "https://www.postgresql.org/docs/current/ecpg-sql-whenever.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-whenever.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:47.939Z"
content_hash: "26d70a7e84b4efc41e0fb7753d3202875d8ec3e951ce055feceb7d9e8eb9f1c1"
menu_path: ["PostgreSQL: Documentation: 18: WHENEVER"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ecpg-sql-var.html/index.md", "title": "PostgreSQL: Documentation: 18: VAR"}
nav_next: {"path": "postgres/docs/current/ecpg-variables.html/index.md", "title": "PostgreSQL: Documentation: 18: 34.4.\u00a0Using Host Variables"}
---

WHENEVER — specify the action to be taken when an SQL statement causes a specific class condition to be raised

## Synopsis

WHENEVER { NOT FOUND | SQLERROR | SQLWARNING } _`action`_

## Description

Define a behavior which is called on the special cases (Rows not found, SQL warnings or errors) in the result of SQL execution.

## Examples

EXEC SQL WHENEVER NOT FOUND CONTINUE;
EXEC SQL WHENEVER NOT FOUND DO BREAK;
EXEC SQL WHENEVER NOT FOUND DO CONTINUE;
EXEC SQL WHENEVER SQLWARNING SQLPRINT;
EXEC SQL WHENEVER SQLWARNING DO warn();
EXEC SQL WHENEVER SQLERROR sqlprint;
EXEC SQL WHENEVER SQLERROR CALL print2();
EXEC SQL WHENEVER SQLERROR DO handle\_error("select");
EXEC SQL WHENEVER SQLERROR DO sqlnotice(NULL, NONO);
EXEC SQL WHENEVER SQLERROR DO sqlprint();
EXEC SQL WHENEVER SQLERROR GOTO error\_label;
EXEC SQL WHENEVER SQLERROR STOP;

A typical application is the use of `WHENEVER NOT FOUND BREAK` to handle looping through result sets:

int
main(void)
{
    EXEC SQL CONNECT TO testdb AS con1;
    EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL COMMIT;
    EXEC SQL ALLOCATE DESCRIPTOR d;
    EXEC SQL DECLARE cur CURSOR FOR SELECT current\_database(), 'hoge', 256;
    EXEC SQL OPEN cur;

    /\* when end of result set reached, break out of while loop \*/
    EXEC SQL WHENEVER NOT FOUND DO BREAK;

    while (1)
    {
        EXEC SQL FETCH NEXT FROM cur INTO SQL DESCRIPTOR d;
        ...
    }

    EXEC SQL CLOSE cur;
    EXEC SQL COMMIT;

    EXEC SQL DEALLOCATE DESCRIPTOR d;
    EXEC SQL DISCONNECT ALL;

    return 0;
}

## Compatibility

`WHENEVER` is specified in the SQL standard, but most of the actions are PostgreSQL extensions.
