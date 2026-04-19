---
title: "PostgreSQL: Documentation: 18: SPI_scroll_cursor_move"
source: "https://www.postgresql.org/docs/current/spi-spi-scroll-cursor-move.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-scroll-cursor-move.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:16.797Z"
content_hash: "ef335c3f47f09f5c49e9153e1972c5ff94d8ce5af3dfec86e008b5e73eaa5b7d"
menu_path: ["PostgreSQL: Documentation: 18: SPI_scroll_cursor_move"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-spi-register-relation.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_register_relation"}
nav_next: {"path": "postgres/docs/current/spi-spi-start-transaction.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_start_transaction"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-spi-scroll-cursor-move.html "PostgreSQL 18 - SPI_scroll_cursor_move") ([18](/docs/18/spi-spi-scroll-cursor-move.html "PostgreSQL 18 - SPI_scroll_cursor_move")) / [17](/docs/17/spi-spi-scroll-cursor-move.html "PostgreSQL 17 - SPI_scroll_cursor_move") / [16](/docs/16/spi-spi-scroll-cursor-move.html "PostgreSQL 16 - SPI_scroll_cursor_move") / [15](/docs/15/spi-spi-scroll-cursor-move.html "PostgreSQL 15 - SPI_scroll_cursor_move") / [14](/docs/14/spi-spi-scroll-cursor-move.html "PostgreSQL 14 - SPI_scroll_cursor_move")

Development Versions: [devel](/docs/devel/spi-spi-scroll-cursor-move.html "PostgreSQL devel - SPI_scroll_cursor_move")

Unsupported versions: [13](/docs/13/spi-spi-scroll-cursor-move.html "PostgreSQL 13 - SPI_scroll_cursor_move") / [12](/docs/12/spi-spi-scroll-cursor-move.html "PostgreSQL 12 - SPI_scroll_cursor_move") / [11](/docs/11/spi-spi-scroll-cursor-move.html "PostgreSQL 11 - SPI_scroll_cursor_move") / [10](/docs/10/spi-spi-scroll-cursor-move.html "PostgreSQL 10 - SPI_scroll_cursor_move") / [9.6](/docs/9.6/spi-spi-scroll-cursor-move.html "PostgreSQL 9.6 - SPI_scroll_cursor_move") / [9.5](/docs/9.5/spi-spi-scroll-cursor-move.html "PostgreSQL 9.5 - SPI_scroll_cursor_move") / [9.4](/docs/9.4/spi-spi-scroll-cursor-move.html "PostgreSQL 9.4 - SPI_scroll_cursor_move") / [9.3](/docs/9.3/spi-spi-scroll-cursor-move.html "PostgreSQL 9.3 - SPI_scroll_cursor_move") / [9.2](/docs/9.2/spi-spi-scroll-cursor-move.html "PostgreSQL 9.2 - SPI_scroll_cursor_move") / [9.1](/docs/9.1/spi-spi-scroll-cursor-move.html "PostgreSQL 9.1 - SPI_scroll_cursor_move") / [9.0](/docs/9.0/spi-spi-scroll-cursor-move.html "PostgreSQL 9.0 - SPI_scroll_cursor_move") / [8.4](/docs/8.4/spi-spi-scroll-cursor-move.html "PostgreSQL 8.4 - SPI_scroll_cursor_move") / [8.3](/docs/8.3/spi-spi-scroll-cursor-move.html "PostgreSQL 8.3 - SPI_scroll_cursor_move")

## SPI\_scroll\_cursor\_move

SPI\_scroll\_cursor\_move — move a cursor

## Synopsis

void SPI\_scroll\_cursor\_move(Portal _`portal`_, FetchDirection _`direction`_,
                            long _`count`_)

## Description

`SPI_scroll_cursor_move` skips over some number of rows in a cursor. This is equivalent to the SQL command `MOVE`.

## Arguments

``Portal _`portal`_``

portal containing the cursor

``FetchDirection _`direction`_``

one of `FETCH_FORWARD`, `FETCH_BACKWARD`, `FETCH_ABSOLUTE` or `FETCH_RELATIVE`

``long _`count`_``

number of rows to move for `FETCH_FORWARD` or `FETCH_BACKWARD`; absolute row number to move to for `FETCH_ABSOLUTE`; or relative row number to move to for `FETCH_RELATIVE`

## Return Value

`SPI_processed` is set as in `SPI_execute` if successful. `SPI_tuptable` is set to `NULL`, since no rows are returned by this function.

## Notes

See the SQL [FETCH](sql-fetch.html "FETCH") command for details of the interpretation of the _`direction`_ and _`count`_ parameters.

Direction values other than `FETCH_FORWARD` may fail if the cursor's plan was not created with the `CURSOR_OPT_SCROLL` option.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-spi-scroll-cursor-move.html/) to report a documentation issue.
