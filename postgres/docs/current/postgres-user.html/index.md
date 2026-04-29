---
title: "PostgreSQL: Documentation: 18: 18.1. The PostgreSQL User Account"
source: "https://www.postgresql.org/docs/current/postgres-user.html"
canonical_url: "https://www.postgresql.org/docs/current/postgres-user.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:59.645Z"
content_hash: "9a45fd65cd8e160e28c13cb887c1d97379c45e3270afb7910ed1b9e52e49152b"
menu_path: ["PostgreSQL: Documentation: 18: 18.1. The PostgreSQL User Account"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pltcl-global.html/index.md", "title": "PostgreSQL: Documentation: 18: 42.4.\u00a0Global Data in PL/Tcl"}
nav_next: {"path": "postgres/docs/current/predefined-roles.html/index.md", "title": "PostgreSQL: Documentation: 18: 21.5.\u00a0Predefined Roles"}
---

As with any server daemon that is accessible to the outside world, it is advisable to run PostgreSQL under a separate user account. This user account should only own the data that is managed by the server, and should not be shared with other daemons. (For example, using the user `nobody` is a bad idea.) In particular, it is advisable that this user account not own the PostgreSQL executable files, to ensure that a compromised server process could not modify those executables.

Pre-packaged versions of PostgreSQL will typically create a suitable user account automatically during package installation.

To add a Unix user account to your system, look for a command `useradd` or `adduser`. The user name postgres is often used, and is assumed throughout this book, but you can use another name if you like.
