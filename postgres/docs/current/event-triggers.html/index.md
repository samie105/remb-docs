---
title: "PostgreSQL: Documentation: 18: Chapter 38. Event Triggers"
source: "https://www.postgresql.org/docs/current/event-triggers.html"
canonical_url: "https://www.postgresql.org/docs/current/event-triggers.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:48.154Z"
content_hash: "c30eef06f12da7f7b63abdde92852803327cac6c60c4226df0cb3273fb07cf19"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 38. Event Triggers"]
section_path: []
nav_prev: {"path": "postgres/docs/current/server-programming.html/index.md", "title": "Part\u00a0V.\u00a0Server Programming"}
nav_next: {"path": "postgres/docs/current/plpgsql.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a041.\u00a0PL/pgSQL \u2014 SQL Procedural Language"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/event-triggers.html "PostgreSQL devel - Chapter 38. Event Triggers")

Chapter 38. Event Triggers

[Prev](https://www.postgresql.org/docs/current/trigger-example.html "37.4. A Complete Trigger Example") 

[Up](https://www.postgresql.org/docs/current/server-programming.html "Part V. Server Programming")

Part V. Server Programming

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/event-trigger-definition.html "38.1. Overview of Event Trigger Behavior")

* * *

To supplement the trigger mechanism discussed in [Chapter 37](https://www.postgresql.org/docs/current/triggers.html "Chapter 37. Triggers"), PostgreSQL also provides event triggers. Unlike regular triggers, which are attached to a single table and capture only DML events, event triggers are global to a particular database and are capable of capturing DDL events.

Like regular triggers, event triggers can be written in any procedural language that includes event trigger support, or in C, but not in plain SQL.

* * *

[Prev](https://www.postgresql.org/docs/current/trigger-example.html "37.4. A Complete Trigger Example") 

[Up](https://www.postgresql.org/docs/current/server-programming.html "Part V. Server Programming")

 [Next](https://www.postgresql.org/docs/current/event-trigger-definition.html "38.1. Overview of Event Trigger Behavior")

37.4. A Complete Trigger Example 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 38.1. Overview of Event Trigger Behavior

