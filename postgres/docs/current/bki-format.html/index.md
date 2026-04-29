---
title: "PostgreSQL: Documentation: 18: 68.3. BKI File Format"
source: "https://www.postgresql.org/docs/current/bki-format.html"
canonical_url: "https://www.postgresql.org/docs/current/bki-format.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:09.251Z"
content_hash: "56d8c8daf15fb425b003c00d8fa249f2493f9f5ce00fa1da9a8e60ec96d9debb"
menu_path: ["PostgreSQL: Documentation: 18: 68.3. BKI File Format"]
section_path: []
nav_prev: {"path": "../bki-example.html/index.md", "title": "PostgreSQL: Documentation: 18: 68.6.\u00a0BKI Example"}
nav_next: {"path": "../bki-structure.html/index.md", "title": "PostgreSQL: Documentation: 18: 68.5.\u00a0Structure of the Bootstrap BKI File"}
---

This section describes how the PostgreSQL backend interprets BKI files. This description will be easier to understand if the `postgres.bki` file is at hand as an example.

BKI input consists of a sequence of commands. Commands are made up of a number of tokens, depending on the syntax of the command. Tokens are usually separated by whitespace, but need not be if there is no ambiguity. There is no special command separator; the next token that syntactically cannot belong to the preceding command starts a new one. (Usually you would put a new command on a new line, for clarity.) Tokens can be certain key words, special characters (parentheses, commas, etc.), identifiers, numbers, or single-quoted strings. Everything is case sensitive.

Lines starting with `#` are ignored.
