---
title: "PostgreSQL: Documentation: 18: DO"
source: "https://www.postgresql.org/docs/current/sql-do.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-do.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:12.567Z"
content_hash: "6afe7c4657478945e846a78b5955478f3a23644f002204b7e4dd35088cac8f31"
menu_path: ["PostgreSQL: Documentation: 18: DO"]
section_path: []
nav_prev: {"path": "../sql-delete.html/index.md", "title": "PostgreSQL: Documentation: 18: DELETE"}
nav_next: {"path": "../sql-drop-access-method.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP ACCESS METHOD"}
---

DO — execute an anonymous code block

## Synopsis

DO \[ LANGUAGE _`lang_name`_ \] _`code`_

## Description

`DO` executes an anonymous code block, or in other words a transient anonymous function in a procedural language.

The code block is treated as though it were the body of a function with no parameters, returning `void`. It is parsed and executed a single time.

The optional `LANGUAGE` clause can be written either before or after the code block.

## Parameters

_`code`_

The procedural language code to be executed. This must be specified as a string literal, just as in `CREATE FUNCTION`. Use of a dollar-quoted literal is recommended.

_`lang_name`_

The name of the procedural language the code is written in. If omitted, the default is `plpgsql`.

## Notes

The procedural language to be used must already have been installed into the current database by means of `CREATE EXTENSION`. `plpgsql` is installed by default, but other languages are not.

The user must have `USAGE` privilege for the procedural language, or must be a superuser if the language is untrusted. This is the same privilege requirement as for creating a function in the language.

If `DO` is executed in a transaction block, then the procedure code cannot execute transaction control statements. Transaction control statements are only allowed if `DO` is executed in its own transaction.

## Examples

Grant all privileges on all views in schema `public` to role `webuser`:

DO $$DECLARE r record;
BEGIN
    FOR r IN SELECT table\_schema, table\_name FROM information\_schema.tables
             WHERE table\_type = 'VIEW' AND table\_schema = 'public'
    LOOP
        EXECUTE 'GRANT ALL ON ' || quote\_ident(r.table\_schema) || '.' || quote\_ident(r.table\_name) || ' TO webuser';
    END LOOP;
END$$;

## Compatibility

There is no `DO` statement in the SQL standard.
