---
title: "PostgreSQL: Documentation: 18: CREATE TEXT SEARCH PARSER"
source: "https://www.postgresql.org/docs/current/sql-createtsparser.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-createtsparser.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:35.885Z"
content_hash: "422654c58301df9056f63a5f1676f1498958df4ba74914fe159f61450b511330"
menu_path: ["PostgreSQL: Documentation: 18: CREATE TEXT SEARCH PARSER"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-createtableas.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TABLE AS"}
nav_next: {"path": "postgres/docs/current/sql-createtstemplate.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TEXT SEARCH TEMPLATE"}
---

CREATE TEXT SEARCH PARSER — define a new text search parser

## Synopsis

CREATE TEXT SEARCH PARSER _`name`_ (
    START = _`start_function`_ ,
    GETTOKEN = _`gettoken_function`_ ,
    END = _`end_function`_ ,
    LEXTYPES = _`lextypes_function`_
    \[, HEADLINE = _`headline_function`_ \]
)

## Description

`CREATE TEXT SEARCH PARSER` creates a new text search parser. A text search parser defines a method for splitting a text string into tokens and assigning types (categories) to the tokens. A parser is not particularly useful by itself, but must be bound into a text search configuration along with some text search dictionaries to be used for searching.

If a schema name is given then the text search parser is created in the specified schema. Otherwise it is created in the current schema.

You must be a superuser to use `CREATE TEXT SEARCH PARSER`. (This restriction is made because an erroneous text search parser definition could confuse or even crash the server.)

Refer to [Chapter 12](https://www.postgresql.org/docs/current/textsearch.html "Chapter 12. Full Text Search") for further information.

## Parameters

_`name`_

The name of the text search parser to be created. The name can be schema-qualified.

_`start_function`_

The name of the start function for the parser.

_`gettoken_function`_

The name of the get-next-token function for the parser.

_`end_function`_

The name of the end function for the parser.

_`lextypes_function`_

The name of the lextypes function for the parser (a function that returns information about the set of token types it produces).

_`headline_function`_

The name of the headline function for the parser (a function that summarizes a set of tokens).

The function names can be schema-qualified if necessary. Argument types are not given, since the argument list for each type of function is predetermined. All except the headline function are required.

The arguments can appear in any order, not only the one shown above.

## Compatibility

There is no `CREATE TEXT SEARCH PARSER` statement in the SQL standard.
