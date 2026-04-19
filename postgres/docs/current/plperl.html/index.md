---
title: "PostgreSQL: Documentation: 18: Chapter 43. PL/Perl — Perl Procedural Language"
source: "https://www.postgresql.org/docs/current/plperl.html"
canonical_url: "https://www.postgresql.org/docs/current/plperl.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:49.832Z"
content_hash: "a400839a78b6317fcd0c1c5f629afe459bba462792d6913c8233d65e6380f809"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 43. PL/Perl — Perl Procedural Language"]
section_path: []
nav_prev: {"path": "postgres/docs/current/plpgsql.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a041.\u00a0PL/pgSQL \u2014 SQL Procedural Language"}
nav_next: {"path": "postgres/docs/current/plpython.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a044.\u00a0PL/Python \u2014 Python Procedural Language"}
---

PL/Perl is a loadable procedural language that enables you to write PostgreSQL functions and procedures in the [Perl programming language](https://www.perl.org/).

The main advantage to using PL/Perl is that this allows use, within stored functions and procedures, of the manyfold “string munging” operators and functions available for Perl. Parsing complex strings might be easier using Perl than it is with the string functions and control structures provided in PL/pgSQL.

To install PL/Perl in a particular database, use `CREATE EXTENSION plperl`.

### Tip

If a language is installed into `template1`, all subsequently created databases will have the language installed automatically.

### Note

Users of source packages must specially enable the build of PL/Perl during the installation process. (Refer to [Chapter 17](https://www.postgresql.org/docs/current/installation.html "Chapter 17. Installation from Source Code") for more information.) Users of binary packages might find PL/Perl in a separate subpackage.
