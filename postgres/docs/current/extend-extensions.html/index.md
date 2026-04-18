---
title: "PostgreSQL: Documentation: 18: 36.17. Packaging Related Objects into an Extension"
source: "https://www.postgresql.org/docs/current/extend-extensions.html"
canonical_url: "https://www.postgresql.org/docs/current/extend-extensions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:27.761Z"
content_hash: "84f4529917bbd30f6903d5303c2136d97597ab592cc4e95b98d8cd821062f549"
menu_path: ["PostgreSQL: Documentation: 18: 36.17. Packaging Related Objects into an Extension"]
section_path: []
nav_prev: {"path": "postgres/docs/current/geqo-intro.html/index.md", "title": "PostgreSQL: Documentation: 18: 61.1.\u00a0Query Handling as a Complex Optimization Problem"}
nav_next: {"path": "postgres/docs/current/infoschema-sql-features.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.48.\u00a0sql_features"}
---

# cannot be relocatable because of use of @extschema@
relocatable = false

While you hardly need a makefile to install these two files into the correct directory, you could use a `Makefile` containing this:

EXTENSION = pair
DATA = pair--1.0.sql

PG\_CONFIG = pg\_config
PGXS := $(shell $(PG\_CONFIG) --pgxs)
include $(PGXS)

This makefile relies on PGXS, which is described in [Section 36.18](https://www.postgresql.org/docs/current/extend-pgxs.html "36.18. Extension Building Infrastructure"). The command `make install` will install the control and script files into the correct directory as reported by pg\_config.

Once the files are installed, use the `CREATE EXTENSION` command to load the objects into any particular database.
