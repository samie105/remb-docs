---
title: "PostgreSQL: Documentation: 18: 52.48. pg_shdepend"
source: "https://www.postgresql.org/docs/current/catalog-pg-shdepend.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-shdepend.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:43:06.251Z"
content_hash: "cc228ccca2b156b780534fb6983de8500ce786e761310d59c64472ddf5c39dc9"
menu_path: ["PostgreSQL: Documentation: 18: 52.48. pg_shdepend"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-shdepend.html "PostgreSQL devel - 52.48. pg_shdepend")

The catalog `pg_shdepend` records the dependency relationships between database objects and shared objects, such as roles. This information allows PostgreSQL to ensure that those objects are unreferenced before attempting to delete them.

See also [`pg_depend`](https://www.postgresql.org/docs/current/catalog-pg-depend.html "52.18. pg_depend"), which performs a similar function for dependencies involving objects within a single database.

Unlike most system catalogs, `pg_shdepend` is shared across all databases of a cluster: there is only one copy of `pg_shdepend` per cluster, not one per database.

**Table 52.48. `pg_shdepend` Columns**

| 
Column Type

Description

 |
| --- |
| 

`dbid` `oid` (references [`pg_database`](https://www.postgresql.org/docs/current/catalog-pg-database.html "52.15. pg_database").`oid`)

The OID of the database the dependent object is in, or zero for a shared object

 |
| 

`classid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

The OID of the system catalog the dependent object is in

 |
| 

`objid` `oid` (references any OID column)

The OID of the specific dependent object

 |
| 

`objsubid` `int4`

For a table column, this is the column number (the `objid` and `classid` refer to the table itself). For all other object types, this column is zero.

 |
| 

`refclassid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

The OID of the system catalog the referenced object is in (must be a shared catalog)

 |
| 

`refobjid` `oid` (references any OID column)

The OID of the specific referenced object

 |
| 

`deptype` `char`

A code defining the specific semantics of this dependency relationship; see text

 |

In all cases, a `pg_shdepend` entry indicates that the referenced object cannot be dropped without also dropping the dependent object. However, there are several subflavors identified by `deptype`:

`SHARED_DEPENDENCY_OWNER` (`o`)

The referenced object (which must be a role) is the owner of the dependent object.

`SHARED_DEPENDENCY_ACL` (`a`)

The referenced object (which must be a role) is mentioned in the ACL of the dependent object. (A `SHARED_DEPENDENCY_ACL` entry is not made for the owner of the object, since the owner will have a `SHARED_DEPENDENCY_OWNER` entry anyway.)

`SHARED_DEPENDENCY_INITACL` (`i`)

The referenced object (which must be a role) is mentioned in a [`pg_init_privs`](https://www.postgresql.org/docs/current/catalog-pg-init-privs.html "52.28. pg_init_privs") entry for the dependent object.

`SHARED_DEPENDENCY_POLICY` (`r`)

The referenced object (which must be a role) is mentioned as the target of a dependent policy object.

`SHARED_DEPENDENCY_TABLESPACE` (`t`)

The referenced object (which must be a tablespace) is mentioned as the tablespace for a relation that doesn't have storage.

Other dependency flavors might be needed in future. Note in particular that the current definition only supports roles and tablespaces as referenced objects.

As in the `pg_depend` catalog, most objects created during initdb are considered “pinned”. No entries are made in `pg_shdepend` that would have a pinned object as either referenced or dependent object.
