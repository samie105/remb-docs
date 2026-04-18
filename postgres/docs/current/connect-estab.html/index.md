---
title: "PostgreSQL: Documentation: 18: 51.2. How Connections Are Established"
source: "https://www.postgresql.org/docs/current/connect-estab.html"
canonical_url: "https://www.postgresql.org/docs/current/connect-estab.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:47.513Z"
content_hash: "c6c760751a23fca20e10c30d7f14466f88f66b1992f022b66e616370c642ebe4"
menu_path: ["PostgreSQL: Documentation: 18: 51.2. How Connections Are Established"]
section_path: []
nav_prev: {"path": "postgres/docs/current/config-setting.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.1.\u00a0Setting Parameters"}
nav_next: {"path": "postgres/docs/current/continuous-archiving.html/index.md", "title": "PostgreSQL: Documentation: 18: 25.3.\u00a0Continuous Archiving and Point-in-Time Recovery (PITR)"}
---

PostgreSQL implements a “process per user” client/server model. In this model, every [](postgres/docs/current/glossary.html/index.md#GLOSSARY-CLIENT)[client process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-CLIENT "Client (process)") connects to exactly one [](postgres/docs/current/glossary.html/index.md#GLOSSARY-BACKEND)[backend process](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BACKEND "Backend (process)"). As we do not know ahead of time how many connections will be made, we have to use a “supervisor process” that spawns a new backend process every time a connection is requested. This supervisor process is called [](postgres/docs/current/glossary.html/index.md#GLOSSARY-POSTMASTER)[postmaster](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-POSTMASTER "Postmaster (process)") and listens at a specified TCP/IP port for incoming connections. Whenever it detects a request for a connection, it spawns a new backend process. Those backend processes communicate with each other and with other processes of the [](postgres/docs/current/glossary.html/index.md#GLOSSARY-INSTANCE)[instance](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-INSTANCE "Instance") using _semaphores_ and [](postgres/docs/current/glossary.html/index.md#GLOSSARY-SHARED-MEMORY)[shared memory](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory") to ensure data integrity throughout concurrent data access.

The client process can be any program that understands the PostgreSQL protocol described in [Chapter 54](https://www.postgresql.org/docs/current/protocol.html "Chapter 54. Frontend/Backend Protocol"). Many clients are based on the C-language library libpq, but several independent implementations of the protocol exist, such as the Java JDBC driver.

Once a connection is established, the client process can send a query to the backend process it's connected to. The query is transmitted using plain text, i.e., there is no parsing done in the client. The backend process parses the query, creates an _execution plan_, executes the plan, and returns the retrieved rows to the client by transmitting them over the established connection.
