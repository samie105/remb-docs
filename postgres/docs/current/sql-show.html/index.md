---
title: "PostgreSQL: Documentation: 18: SHOW"
source: "https://www.postgresql.org/docs/current/sql-show.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-show.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:55.568Z"
content_hash: "a151905786674c618021f66835e30469165e17db1fdd531e165c9225f2527cd4"
menu_path: ["PostgreSQL: Documentation: 18: SHOW"]
section_path: []
nav_prev: {"path": "../sql-set.html/index.md", "title": "PostgreSQL: Documentation: 18: SET"}
nav_next: {"path": "../sql-start-transaction.html/index.md", "title": "PostgreSQL: Documentation: 18: START TRANSACTION"}
---

SHOW — show the value of a run-time parameter

## Synopsis

SHOW _`name`_
SHOW ALL

## Description

`SHOW` will display the current setting of run-time parameters. These variables can be set using the `SET` statement, by editing the `postgresql.conf` configuration file, through the `PGOPTIONS` environmental variable (when using libpq or a libpq\-based application), or through command-line flags when starting the `postgres` server. See [Chapter 19](https://www.postgresql.org/docs/current/runtime-config.html "Chapter 19. Server Configuration") for details.

## Parameters

_`name`_

The name of a run-time parameter. Available parameters are documented in [Chapter 19](https://www.postgresql.org/docs/current/runtime-config.html "Chapter 19. Server Configuration") and on the [SET](https://www.postgresql.org/docs/current/sql-set.html "SET") reference page. In addition, there are a few parameters that can be shown but not set:

`SERVER_VERSION`

Shows the server's version number.

`SERVER_ENCODING`

Shows the server-side character set encoding. At present, this parameter can be shown but not set, because the encoding is determined at database creation time.

`IS_SUPERUSER`

True if the current role has superuser privileges.

`ALL`

Show the values of all configuration parameters, with descriptions.

## Notes

The function `current_setting` produces equivalent output; see [Section 9.28.1](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-SET "9.28.1. Configuration Settings Functions"). Also, the [`pg_settings`](https://www.postgresql.org/docs/current/view-pg-settings.html "53.25. pg_settings") system view produces the same information.

## Examples

Show the current setting of the parameter `DateStyle`:

SHOW DateStyle;
 DateStyle
-----------
 ISO, MDY
(1 row)

Show the current setting of the parameter `geqo`:

SHOW geqo;
 geqo
------
 on
(1 row)

Show all settings:

SHOW ALL;
            name         | setting |                description
-------------------------+---------+-------------------------------------------------
 allow\_system\_table\_mods | off     | Allows modifications of the structure of ...
    .
    .
    .
 xmloption               | content | Sets whether XML data in implicit parsing ...
 zero\_damaged\_pages      | off     | Continues processing past damaged page headers.
(196 rows)

## Compatibility

The `SHOW` command is a PostgreSQL extension.
