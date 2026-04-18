---
title: "PostgreSQL: Documentation: 18: 68.4. BKI Commands"
source: "https://www.postgresql.org/docs/current/bki-commands.html"
canonical_url: "https://www.postgresql.org/docs/current/bki-commands.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:15.989Z"
content_hash: "97fa5d6b9687b0a31e14e3996ddcd916750691c5af55be1bc16280b59f1e78e9"
menu_path: ["PostgreSQL: Documentation: 18: 68.4. BKI Commands"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-merge.html/index.md", "title": "PostgreSQL: Documentation: 18: MERGE"}
nav_next: {"path": "postgres/docs/current/runtime-config-short.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.18.\u00a0Short Options"}
---

Create a table named _`tablename`_, and having the OID _`tableoid`_, with the columns given in parentheses.

The following column types are supported directly by `bootstrap.c`: `bool`, `bytea`, `char` (1 byte), `name`, `int2`, `int4`, `regproc`, `regclass`, `regtype`, `text`, `oid`, `tid`, `xid`, `cid`, `int2vector`, `oidvector`, `_int4` (array), `_text` (array), `_oid` (array), `_char` (array), `_aclitem` (array). Although it is possible to create tables containing columns of other types, this cannot be done until after `pg_type` has been created and filled with appropriate entries. (That effectively means that only these column types can be used in bootstrap catalogs, but non-bootstrap catalogs can contain any built-in type.)

When `bootstrap` is specified, the table will only be created on disk; nothing is entered into `pg_class`, `pg_attribute`, etc., for it. Thus the table will not be accessible by ordinary SQL operations until such entries are made the hard way (with `insert` commands). This option is used for creating `pg_class` etc. themselves.

The table is created as shared if `shared_relation` is specified. The table's row type OID (`pg_type` OID) can optionally be specified via the `rowtype_oid` clause; if not specified, an OID is automatically generated for it. (The `rowtype_oid` clause is useless if `bootstrap` is specified, but it can be provided anyway for documentation.)

Create an index named _`indexname`_, having OID _`indexoid`_, on the table named _`tablename`_, using the _`amname`_ access method. The fields to index are called _`name1`_, _`name2`_ etc., and the operator classes to use are _`opclass1`_, _`opclass2`_ etc., respectively. The index file is created and appropriate catalog entries are made for it, but the index contents are not initialized by this command.
