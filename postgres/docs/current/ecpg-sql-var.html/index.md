---
title: "PostgreSQL: Documentation: 18: VAR"
source: "https://www.postgresql.org/docs/current/ecpg-sql-var.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-var.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:08.385Z"
content_hash: "1f301732913b5a37a5469db6ad57c4bb6068d076e768915db138b7052215edf3"
menu_path: ["PostgreSQL: Documentation: 18: VAR"]
section_path: []
nav_prev: {"path": "../ecpg-sql-type.html/index.md", "title": "PostgreSQL: Documentation: 18: TYPE"}
nav_next: {"path": "../ecpg-sql-whenever.html/index.md", "title": "PostgreSQL: Documentation: 18: WHENEVER"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/ecpg-sql-var.html "PostgreSQL 18 - VAR") ([18](/docs/18/ecpg-sql-var.html "PostgreSQL 18 - VAR")) / [17](/docs/17/ecpg-sql-var.html "PostgreSQL 17 - VAR") / [16](/docs/16/ecpg-sql-var.html "PostgreSQL 16 - VAR") / [15](/docs/15/ecpg-sql-var.html "PostgreSQL 15 - VAR") / [14](/docs/14/ecpg-sql-var.html "PostgreSQL 14 - VAR")

Development Versions: [devel](/docs/devel/ecpg-sql-var.html "PostgreSQL devel - VAR")

Unsupported versions: [13](/docs/13/ecpg-sql-var.html "PostgreSQL 13 - VAR") / [12](/docs/12/ecpg-sql-var.html "PostgreSQL 12 - VAR") / [11](/docs/11/ecpg-sql-var.html "PostgreSQL 11 - VAR") / [10](/docs/10/ecpg-sql-var.html "PostgreSQL 10 - VAR") / [9.6](/docs/9.6/ecpg-sql-var.html "PostgreSQL 9.6 - VAR") / [9.5](/docs/9.5/ecpg-sql-var.html "PostgreSQL 9.5 - VAR") / [9.4](/docs/9.4/ecpg-sql-var.html "PostgreSQL 9.4 - VAR") / [9.3](/docs/9.3/ecpg-sql-var.html "PostgreSQL 9.3 - VAR") / [9.2](/docs/9.2/ecpg-sql-var.html "PostgreSQL 9.2 - VAR") / [9.1](/docs/9.1/ecpg-sql-var.html "PostgreSQL 9.1 - VAR")

## VAR

VAR — define a variable

## Synopsis

VAR _`varname`_ IS _`ctype`_

## Description

The `VAR` command assigns a new C data type to a host variable. The host variable must be previously declared in a declare section.

## Parameters

_`varname`_ [#](#ECPG-SQL-VAR-VARNAME)

A C variable name.

_`ctype`_ [#](#ECPG-SQL-VAR-CTYPE)

A C type specification.

## Examples

Exec sql begin declare section;
short a;
exec sql end declare section;
EXEC SQL VAR a IS int;

## Compatibility

The `VAR` command is a PostgreSQL extension.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/ecpg-sql-var.html/) to report a documentation issue.
