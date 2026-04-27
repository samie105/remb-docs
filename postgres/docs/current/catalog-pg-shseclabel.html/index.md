---
title: "PostgreSQL: Documentation: 18: 52.50. pg_shseclabel"
source: "https://www.postgresql.org/docs/current/catalog-pg-shseclabel.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-shseclabel.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:45:43.601Z"
content_hash: "76cd1b4137a63a632847ad4ab103ef324589f3e71d88fc58d8625cbbb09b9bac"
menu_path: ["PostgreSQL: Documentation: 18: 52.50. pg_shseclabel"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-shseclabel.html "PostgreSQL devel - 52.50. pg_shseclabel")

The catalog `pg_shseclabel` stores security labels on shared database objects. Security labels can be manipulated with the [`SECURITY LABEL`](https://www.postgresql.org/docs/current/sql-security-label.html "SECURITY LABEL") command. For an easier way to view security labels, see [Section 53.23](https://www.postgresql.org/docs/current/view-pg-seclabels.html "53.23. pg_seclabels").

See also [`pg_seclabel`](https://www.postgresql.org/docs/current/catalog-pg-seclabel.html "52.46. pg_seclabel"), which performs a similar function for security labels involving objects within a single database.

Unlike most system catalogs, `pg_shseclabel` is shared across all databases of a cluster: there is only one copy of `pg_shseclabel` per cluster, not one per database.

**Table 52.50. `pg_shseclabel` Columns**

| 
Column Type

Description

 |
| --- |
| 

`objoid` `oid` (references any OID column)

The OID of the object this security label pertains to

 |
| 

`classoid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

The OID of the system catalog this object appears in

 |
| 

`provider` `text`

The label provider associated with this label.

 |
| 

`label` `text`

The security label applied to this object.

 |
