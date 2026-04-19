# SKILL.md — PostgreSQL Developer Documentation

## Overview

PostgreSQL is an advanced, open-source relational database system emphasizing extensibility, reliability, and standards compliance. It solves problems related to structured data storage, complex querying, concurrency, and data integrity for applications ranging from small prototypes to enterprise-scale systems.

---

## Key Concepts

- **SQL Language Support:** PostgreSQL implements most of the SQL standard, including advanced querying, data definition, manipulation, and transaction semantics.
- **Extensibility:** Rich support for user-defined functions, data types, operators, languages, and extensions.
- **Concurrency & Reliability:** MVCC (Multi-Version Concurrency Control), robust transaction processing, Write-Ahead Logging (WAL), and high availability features.
- **Server Programming:** Support for procedural languages (PL/pgSQL, PL/Python, etc.), triggers, event triggers, and background workers.
- **Performance & Indexing:** Deep indexing options, full-text search, parallel query processing, and advanced optimizer techniques.
- **Client & Server Interfaces:** Libpq C API, client tools, frontend/backend protocol details.
- **Administration:** Installation, configuration, authentication, roles, monitoring, backup/restore, replication, and routine maintenance.

---

## Navigation Guide

- **Getting Started / Tutorials:** Introductory material and step-by-step guides under the Tutorial section.
- **SQL Reference:** For syntax and command details, see the SQL Language section, including Data Definition, Data Manipulation, Queries, Functions, and Operators.
- **Performance & Indexing:** Performance tips, indexing strategies, and parallel query under SQL Language and Performance Tips sections.
- **Server Admin:** Installation, configuration, authentication, roles, backup, replication, and monitoring are in Server Administration.
- **Programming & Extensions:** Procedures, triggers, procedural languages, background workers, and extensibility live in Server Programming.
- **Client APIs & Tools:** Reference information for client libraries and utilities in Client Interfaces and Reference.
- **Internals:** Architecture, physical storage, catalogs, protocol, and extension interfaces are under Internals.

### Common Task Mapping:
- **Define tables/users/config:** Data Definition, Database Roles, Server Setup & Configuration
- **Query/write data:** SQL Syntax, Functions and Operators, Queries, Data Manipulation
- **Optimize/scale:** Performance Tips, Indexes, Parallel Query, High Availability
- **Integrate/extend:** Server Programming, Procedural Languages, Event Triggers, Background Workers

---

## Top Important Pages

1. [PostgreSQL 18.3 Documentation](postgres/docs/current/index.html/index.md)  
   Entry point with overview and structure.
2. [Legal Notice](postgres/docs/current/legalnotice.html/index.md)  
   Licensing and legal considerations.
3. [Further Information](postgres/docs/current/resources.html/index.md)  
   Where to find more on PostgreSQL.
4. [Bug Reporting Guidelines](postgres/docs/current/bug-reporting.html/index.md)  
   How to report issues or get help.
5. [Advanced Features (Tutorial)](postgres/docs/current/tutorial-advanced.html/index.md)  
   Introduction to advanced PostgreSQL capabilities.
6. [SQL Syntax](postgres/docs/current/sql-syntax.html/index.md)  
   In-depth syntax reference for writing SQL in PostgreSQL.
7. [Data Definition](postgres/docs/current/ddl.html/index.md)  
   Table and schema creation/modification.
8. [Functions and Operators](postgres/docs/current/functions.html/index.md)  
   Built-in and custom functions/operators documentation.
9. [Full Text Search](postgres/docs/current/textsearch.html/index.md)  
   Guidance on implementing and using PostgreSQL's full-text search.
10. [Performance Tips](postgres/docs/current/performance-tips.html/index.md)  
    Practical optimization strategies for queries and schema.
11. [Parallel Query](postgres/docs/current/parallel-query.html/index.md)  
    Parallel execution and scaling query workloads.
12. [Database Roles](postgres/docs/current/user-manag.html/index.md)  
    User/role management and permissions.
13. [Write-Ahead Log](postgres/docs/current/wal.html/index.md)  
    Reliability and crash recovery mechanisms.
14. [Just-in-Time Compilation (JIT)](postgres/docs/current/jit.html/index.md)  
    Speeding up query execution through JIT compilation.
15. [ECPG — Embedded SQL in C](postgres/docs/current/ecpg.html/index.md)  
    Guide to using embedded SQL in C programs.
16. [Event Triggers](postgres/docs/current/event-triggers.html/index.md)  
    Triggering actions on schema changes.
17. [PL/Perl — Perl Procedural Language](postgres/docs/current/plperl.html/index.md)  
    Perl as a server-side programming language.
18. [Background Worker Processes](postgres/docs/current/bgworker.html/index.md)  
    Extending PostgreSQL with custom background tasks.
19. [PostgreSQL Client Applications](postgres/docs/current/reference-client.html/index.md)  
    Reference for command-line client tools.
20. [Frontend/Backend Protocol](postgres/docs/current/protocol.html/index.md)  
    Internal protocol details for advanced integrations.

---

## Notable Gotchas & Doc Structure Quirks

- **Chapters vs. Parts vs. Appendixes:** Some key features are under "Chapters" within Parts, but interfaces and advanced programming topics may be in separate Parts (e.g., VI. Reference, VII. Internals).
- **API/Command Reference Separation:** Client applications and server commands are referenced separately in the Reference section, rather than grouped under tutorials.
- **Procedural Languages:** Each PL (e.g., PL/pgSQL, PL/Perl, PL/Python) has a dedicated chapter; general server programming concepts are under "Server Programming."
- **Internals:** Deep technical material (catalogs, optimizer, protocol, extension interfaces) are in the Internals section—crucial for extension writers and performance tuning.
- **Advanced Features:** While introductory tutorials exist, some advanced usage patterns (text search, parallel queries, JIT, worker processes) reside in specific chapters, not in the main tutorial path.

---

**For all developer queries, cross-check the task type with the navigation guide above, use the local file path links for page lookups, and note structural quirks for rapid, accurate answers.**