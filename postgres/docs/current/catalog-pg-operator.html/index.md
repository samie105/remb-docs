---
title: "PostgreSQL: Documentation: 18: 52.34. pg_operator"
source: "https://www.postgresql.org/docs/current/catalog-pg-operator.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-operator.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:36.355Z"
content_hash: "5a0c2111180d8d3ccef9e71c8137f7544e645edc2e53067a500d041c1d42fc59"
menu_path: ["PostgreSQL: Documentation: 18: 52.34. pg_operator"]
section_path: []
nav_prev: {"path": "postgres/docs/current/amcheck.html/index.md", "title": "PostgreSQL: Documentation: 18: F.1.\u00a0amcheck \u2014 tools to verify table and index consistency"}
nav_next: {"path": "postgres/docs/current/functions-uuid.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.14.\u00a0UUID Functions"}
---

The catalog `pg_operator` stores information about operators. See [CREATE OPERATOR](https://www.postgresql.org/docs/current/sql-createoperator.html "CREATE OPERATOR") and [Section 36.14](https://www.postgresql.org/docs/current/xoper.html "36.14. User-Defined Operators") for more information.

**Table 52.34. `pg_operator` Columns**

Column Type

Description

`oid` `oid`

Row identifier

`oprname` `name`

Name of the operator

`oprnamespace` `oid` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`oid`)

The OID of the namespace that contains this operator

`oprowner` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

Owner of the operator

`oprkind` `char`

`b` = infix operator (“both”), or `l` = prefix operator (“left”)

`oprcanmerge` `bool`

This operator supports merge joins

`oprcanhash` `bool`

This operator supports hash joins

`oprleft` `oid` (references [`pg_type`](https://www.postgresql.org/docs/current/catalog-pg-type.html "52.64. pg_type").`oid`)

Type of the left operand (zero for a prefix operator)

`oprright` `oid` (references [`pg_type`](https://www.postgresql.org/docs/current/catalog-pg-type.html "52.64. pg_type").`oid`)

Type of the right operand

`oprresult` `oid` (references [`pg_type`](https://www.postgresql.org/docs/current/catalog-pg-type.html "52.64. pg_type").`oid`)

Type of the result (zero for a not-yet-defined “shell” operator)

`oprcom` `oid` (references [`pg_operator`](https://www.postgresql.org/docs/current/catalog-pg-operator.html "52.34. pg_operator").`oid`)

Commutator of this operator (zero if none)

`oprnegate` `oid` (references [`pg_operator`](https://www.postgresql.org/docs/current/catalog-pg-operator.html "52.34. pg_operator").`oid`)

Negator of this operator (zero if none)

`oprcode` `regproc` (references [`pg_proc`](https://www.postgresql.org/docs/current/catalog-pg-proc.html "52.39. pg_proc").`oid`)

Function that implements this operator (zero for a not-yet-defined “shell” operator)

`oprrest` `regproc` (references [`pg_proc`](https://www.postgresql.org/docs/current/catalog-pg-proc.html "52.39. pg_proc").`oid`)

Restriction selectivity estimation function for this operator (zero if none)

`oprjoin` `regproc` (references [`pg_proc`](https://www.postgresql.org/docs/current/catalog-pg-proc.html "52.39. pg_proc").`oid`)

Join selectivity estimation function for this operator (zero if none)

