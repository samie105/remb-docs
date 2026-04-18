---
title: "PostgreSQL: Documentation: 18: 41.12. Tips for Developing in PL/pgSQL"
source: "https://www.postgresql.org/docs/current/plpgsql-development-tips.html"
canonical_url: "https://www.postgresql.org/docs/current/plpgsql-development-tips.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:03.633Z"
content_hash: "a303cfc182c86325a1ec42b9cfb7bc44ea09847799b9b8e749698f546d490192"
menu_path: ["PostgreSQL: Documentation: 18: 41.12. Tips for Developing in PL/pgSQL"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ecpg-sql-describe.html/index.md", "title": "PostgreSQL: Documentation: 18: DESCRIBE"}
nav_next: {"path": "postgres/docs/current/sql-declare.html/index.md", "title": "PostgreSQL: Documentation: 18: DECLARE"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/plpgsql-development-tips.html "PostgreSQL devel - 41.12. Tips for Developing in PL/pgSQL")

One good way to develop in PL/pgSQL is to use the text editor of your choice to create your functions, and in another window, use psql to load and test those functions. If you are doing it this way, it is a good idea to write the function using `CREATE OR REPLACE FUNCTION`. That way you can just reload the file to update the function definition. For example:

CREATE OR REPLACE FUNCTION testfunc(integer) RETURNS integer AS $$
          ....
$$ LANGUAGE plpgsql;

While running psql, you can load or reload such a function definition file with:

\\i filename.sql

and then immediately issue SQL commands to test the function.

Another good way to develop in PL/pgSQL is with a GUI database access tool that facilitates development in a procedural language. One example of such a tool is pgAdmin, although others exist. These tools often provide convenient features such as escaping single quotes and making it easier to recreate and debug functions.

### 41.12.1. Handling of Quotation Marks [#](#PLPGSQL-QUOTE-TIPS)

The code of a PL/pgSQL function is specified in `CREATE FUNCTION` as a string literal. If you write the string literal in the ordinary way with surrounding single quotes, then any single quotes inside the function body must be doubled; likewise any backslashes must be doubled (assuming escape string syntax is used). Doubling quotes is at best tedious, and in more complicated cases the code can become downright incomprehensible, because you can easily find yourself needing half a dozen or more adjacent quote marks. It's recommended that you instead write the function body as a “dollar-quoted” string literal (see [Section 4.1.2.4](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-DOLLAR-QUOTING "4.1.2.4. Dollar-Quoted String Constants")). In the dollar-quoting approach, you never double any quote marks, but instead take care to choose a different dollar-quoting delimiter for each level of nesting you need. For example, you might write the `CREATE FUNCTION` command as:

CREATE OR REPLACE FUNCTION testfunc(integer) RETURNS integer AS $PROC$
          ....
$PROC$ LANGUAGE plpgsql;

Within this, you might use quote marks for simple literal strings in SQL commands and `$$` to delimit fragments of SQL commands that you are assembling as strings. If you need to quote text that includes `$$`, you could use `$Q$`, and so on.

The following chart shows what you have to do when writing quote marks without dollar quoting. It might be useful when translating pre-dollar quoting code into something more comprehensible.

1 quotation mark [#](#PLPGSQL-QUOTE-TIPS-1-QUOT)

To begin and end the function body, for example:

CREATE FUNCTION foo() RETURNS integer AS '
          ....
' LANGUAGE plpgsql;

Anywhere within a single-quoted function body, quote marks _must_ appear in pairs.

2 quotation marks [#](#PLPGSQL-QUOTE-TIPS-2-QUOT)

For string literals inside the function body, for example:

a\_output := ''Blah'';
SELECT \* FROM users WHERE f\_name=''foobar'';

In the dollar-quoting approach, you'd just write:

a\_output := 'Blah';
SELECT \* FROM users WHERE f\_name='foobar';

which is exactly what the PL/pgSQL parser would see in either case.

4 quotation marks [#](#PLPGSQL-QUOTE-TIPS-4-QUOT)

When you need a single quotation mark in a string constant inside the function body, for example:

a\_output := a\_output || '' AND name LIKE ''''foobar'''' AND xyz''

The value actually appended to `a_output` would be: `AND name LIKE 'foobar' AND xyz`.

In the dollar-quoting approach, you'd write:

a\_output := a\_output || $$ AND name LIKE 'foobar' AND xyz$$

being careful that any dollar-quote delimiters around this are not just `$$`.

6 quotation marks [#](#PLPGSQL-QUOTE-TIPS-6-QUOT)

When a single quotation mark in a string inside the function body is adjacent to the end of that string constant, for example:

a\_output := a\_output || '' AND name LIKE ''''foobar''''''

The value appended to `a_output` would then be: `AND name LIKE 'foobar'`.

In the dollar-quoting approach, this becomes:

a\_output := a\_output || $$ AND name LIKE 'foobar'$$

10 quotation marks [#](#PLPGSQL-QUOTE-TIPS-10-QUOT)

When you want two single quotation marks in a string constant (which accounts for 8 quotation marks) and this is adjacent to the end of that string constant (2 more). You will probably only need that if you are writing a function that generates other functions, as in [Example 41.10](https://www.postgresql.org/docs/current/plpgsql-porting.html#PLPGSQL-PORTING-EX2 "Example 41.10. Porting a Function that Creates Another Function from PL/SQL to PL/pgSQL"). For example:

a\_output := a\_output || '' if v\_'' ||
    referrer\_keys.kind || '' like ''''''''''
    || referrer\_keys.key\_string || ''''''''''
    then return ''''''  || referrer\_keys.referrer\_type
    || ''''''; end if;'';

The value of `a_output` would then be:

if v\_... like ''...'' then return ''...''; end if;

In the dollar-quoting approach, this becomes:

a\_output := a\_output || $$ if v\_$$ || referrer\_keys.kind || $$ like '$$
    || referrer\_keys.key\_string || $$'
    then return '$$  || referrer\_keys.referrer\_type
    || $$'; end if;$$;

where we assume we only need to put single quote marks into `a_output`, because it will be re-quoted before use.


