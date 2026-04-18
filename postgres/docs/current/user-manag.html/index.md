---
title: "PostgreSQL: Documentation: 18: Chapter 21. Database Roles"
source: "https://www.postgresql.org/docs/current/user-manag.html"
canonical_url: "https://www.postgresql.org/docs/current/user-manag.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:03.906Z"
content_hash: "16dc44660ba20f8064055a9cdb5cc159b68544e6985c973eaa82b8da6e3a5c8c"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 21. Database Roles"]
section_path: []
nav_prev: {"path": "postgres/docs/current/runtime.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a018.\u00a0Server Setup and Operation"}
nav_next: {"path": "postgres/docs/current/wal.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a028.\u00a0Reliability and the Write-Ahead Log"}
---

PostgreSQL manages database access permissions using the concept of _roles_. A role can be thought of as either a database user, or a group of database users, depending on how the role is set up. Roles can own database objects (for example, tables and functions) and can assign privileges on those objects to other roles to control who has access to which objects. Furthermore, it is possible to grant _membership_ in a role to another role, thus allowing the member role to use privileges assigned to another role.

The concept of roles subsumes the concepts of “users” and “groups”. In PostgreSQL versions before 8.1, users and groups were distinct kinds of entities, but now there are only roles. Any role can act as a user, a group, or both.

This chapter describes how to create and manage roles. More information about the effects of role privileges on various database objects can be found in [Section 5.8](https://www.postgresql.org/docs/current/ddl-priv.html "5.8. Privileges").

