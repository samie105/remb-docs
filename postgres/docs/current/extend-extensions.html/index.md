---
title: "PostgreSQL: Documentation: 18: 36.17. Packaging Related Objects into an Extension"
source: "https://www.postgresql.org/docs/current/extend-extensions.html"
canonical_url: "https://www.postgresql.org/docs/current/extend-extensions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:51:50.091Z"
content_hash: "af5d98736fa86b89e34591c22702c01fd2d16baa4b24266337701eaeb75f3a81"
menu_path: ["PostgreSQL: Documentation: 18: 36.17. Packaging Related Objects into an Extension"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/explicit-locking.html/index.md", "title": "PostgreSQL: Documentation: 18: 13.3.\u00a0Explicit Locking"}
nav_next: {"path": "postgres/docs/current/extend-type-system.html/index.md", "title": "PostgreSQL: Documentation: 18: 36.2.\u00a0The PostgreSQL Type System"}
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
