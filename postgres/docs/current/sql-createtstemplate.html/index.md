---
title: "PostgreSQL: Documentation: 18: CREATE TEXT SEARCH TEMPLATE"
source: "https://www.postgresql.org/docs/current/sql-createtstemplate.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-createtstemplate.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:31.846Z"
content_hash: "040d5828571dc9648ae42607319f96057a9aec044315b7fc56e9858bd12341c2"
menu_path: ["PostgreSQL: Documentation: 18: CREATE TEXT SEARCH TEMPLATE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-createtsparser.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TEXT SEARCH PARSER"}
nav_next: {"path": "postgres/docs/current/sql-createtype.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TYPE"}
---

CREATE TEXT SEARCH TEMPLATE — define a new text search template

## Synopsis

CREATE TEXT SEARCH TEMPLATE _`name`_ (
    \[ INIT = _`init_function`_ , \]
    LEXIZE = _`lexize_function`_
)

## Description

`CREATE TEXT SEARCH TEMPLATE` creates a new text search template. Text search templates define the functions that implement text search dictionaries. A template is not useful by itself, but must be instantiated as a dictionary to be used. The dictionary typically specifies parameters to be given to the template functions.

If a schema name is given then the text search template is created in the specified schema. Otherwise it is created in the current schema.

You must be a superuser to use `CREATE TEXT SEARCH TEMPLATE`. This restriction is made because an erroneous text search template definition could confuse or even crash the server. The reason for separating templates from dictionaries is that a template encapsulates the “unsafe” aspects of defining a dictionary. The parameters that can be set when defining a dictionary are safe for unprivileged users to set, and so creating a dictionary need not be a privileged operation.

Refer to [Chapter 12](https://www.postgresql.org/docs/current/textsearch.html "Chapter 12. Full Text Search") for further information.

## Parameters

_`name`_

The name of the text search template to be created. The name can be schema-qualified.

_`init_function`_

The name of the init function for the template.

_`lexize_function`_

The name of the lexize function for the template.

The function names can be schema-qualified if necessary. Argument types are not given, since the argument list for each type of function is predetermined. The lexize function is required, but the init function is optional.

The arguments can appear in any order, not only the one shown above.

## Compatibility

There is no `CREATE TEXT SEARCH TEMPLATE` statement in the SQL standard.
