---
title: "Postgres Extensions Overview"
source: "https://supabase.com/docs/guides/database/extensions/pg_partman"
canonical_url: "https://supabase.com/docs/guides/database/extensions"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:45.552Z"
content_hash: "6a03c55fdb78ce2ddd4f88b54d83404225e641ac154f29084482f6d5f5ff6a68"
menu_path: ["Database","Database","Extensions","Extensions","Overview","Overview"]
section_path: ["Database","Database","Extensions","Extensions","Overview","Overview"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pg_net/index.md", "title": "pg_net: Async Networking"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pg_plan_filter/index.md", "title": "pg_plan_filter: Restrict Total Cost"}
---

# 

Postgres Extensions Overview

* * *

Extensions are exactly as they sound - they "extend" the database with functionality which isn't part of the Postgres core. Supabase has pre-installed some of the most useful open source extensions.

### Enable and disable extensions[#](#enable-and-disable-extensions)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click **Extensions** in the sidebar.
3.  Enable or disable an extension.

Most extensions are installed under the `extensions` schema, which is accessible to public by default. To avoid namespace pollution, we do not recommend creating other entities in the `extensions` schema.

If you need to restrict user access to tables managed by extensions, we recommend creating a separate schema for installing that specific extension.

Some extensions can only be created under a specific schema, for example, `postgis_tiger_geocoder` extension creates a schema named `tiger`. Before enabling such extensions, make sure you have not created a conflicting schema with the same name.

In addition to the pre-configured extensions, you can also install your own SQL extensions directly in the database using Supabase's SQL editor. The SQL code for the extensions, including plpgsql extensions, can be added through the SQL editor.

### Upgrade extensions[#](#upgrade-extensions)

If a new version of an extension becomes available on Supabase, you need to initiate a software upgrade in the [Infrastructure Settings](/dashboard/project/_/settings/infrastructure) to access it. Software upgrades can also be initiated by restarting your server in the [General Settings](/dashboard/project/_/settings/general).

### Full list of extensions[#](#full-list-of-extensions)

Supabase is pre-configured with over 50 extensions and you can install additional extensions through the [database.dev](https://database.dev/) package manager.

You can install pure SQL extensions directly in the database using the SQL editor or any Postgres client.

If you would like to request an extension, add (or upvote) it in the [GitHub Discussion](https://github.com/orgs/supabase/discussions/33754).

Search extensions

### Filter

*   AI
*   Admin
*   Audit
*   Cryptography
*   Data Type
*   Dataset
*   Geo
*   Index
*   Language
*   Notifications
*   Search
*   Testing
*   Time Series
*   Utility

[

address\_standardizer

Used to parse an address into constituent elements. Generally used to support geocoding address normalization step.

](https://postgis.net/docs/manual-2.5/Address_Standardizer.html)[

address\_standardizer\_data\_us

Address Standardizer US dataset example

](https://postgis.net/docs/manual-2.5/Address_Standardizer.html)[

amcheck

Functions for verifying relation integrity

](https://www.postgresql.org/docs/current/amcheck.html)[

autoinc

Functions for autoincrementing fields

](https://www.postgresql.org/docs/current/contrib-spi.html#id-1.11.7.50.6)[

bloom

Bloom access method - signature file based index

](https://www.postgresql.org/docs/current/bloom.html)[

btree\_gin

Support for indexing common datatypes in GIN

](https://www.postgresql.org/docs/current/btree-gin.html)[

btree\_gist

Support for indexing common datatypes in GiST

](https://www.postgresql.org/docs/current/btree-gist.html)[

citext

Data type for case-insensitive character strings

](https://www.postgresql.org/docs/current/citext.html)[

cube

Data type for multidimensional cubes

](https://www.postgresql.org/docs/current/cube.html)[

dblink

Connect to other PostgreSQL databases from within a database

](https://www.postgresql.org/docs/current/contrib-dblink-function.html)[

dict\_int

Text search dictionary template for integers

](https://www.postgresql.org/docs/current/dict-int.html)[

dict\_xsyn

Text search dictionary template for extended synonym processing

](https://www.postgresql.org/docs/current/dict-xsyn.html)[

earthdistance

Calculate great-circle distances on the surface of the Earth

](https://www.postgresql.org/docs/current/earthdistance.html)[

fuzzystrmatch

Determine similarities and distance between strings

](https://www.postgresql.org/docs/current/fuzzystrmatch.html)[

hstore

Data type for storing sets of (key, value) pairs

](https://www.postgresql.org/docs/current/hstore.html)[

hypopg

Hypothetical indexes for PostgreSQL

](../hypopg/index.md)[

http

HTTP client for PostgreSQL, allows web page retrieval inside the database.

](../http/index.md)[

insert\_username

Functions for tracking who changed a table

](https://www.postgresql.org/docs/current/contrib-spi.html#id-1.11.7.50.7)[

old\_snapshot

Utilities in support of old\_snapshot\_threshold

](https://www.postgresql.org/docs/current/oldsnapshot.html)[

index\_advisor

Optimize query performance with automatic index recommendation

](../index_advisor/index.md)[

intarray

Functions, operators, and index support for 1-D arrays of integers

](https://www.postgresql.org/docs/current/intarray.html)[

isn

Data types for international product numbering standards

](https://www.postgresql.org/docs/current/isn.html)[

lo

Large Object maintenance

](https://www.postgresql.org/docs/current/lo.html)[

ltree

Data type for hierarchical tree-like structures

](https://www.postgresql.org/docs/current/ltree.html)[

moddatetime

Functions for tracking last modification time

](https://www.postgresql.org/docs/current/contrib-spi.html#id-1.11.7.50.8)[

pg\_cron

Job scheduler for PostgreSQL

](../pg_cron/index.md)[

pg\_freespacemap

Examine the free space map (FSM)

](https://www.postgresql.org/docs/current/pgfreespacemap.html)[

pg\_graphql

Pg\_graphql: GraphQL support

](../pg_graphql/index.md)[

pg\_hashids

Pg\_hashids

](../pg_hashids/index.md)[

pg\_jsonschema

Pg\_jsonschema

](../pg_jsonschema/index.md)[

pg\_net

Async HTTP

](../pg_net/index.md)[

pg\_partman

Automated partition management

](https://github.com/pgpartman/pg_partman)[

pg\_prewarm

Prewarm relation data

](https://www.postgresql.org/docs/current/pgprewarm.html)[

pg\_stat\_statements

Track execution statistics of all SQL statements executed

](../pg_stat_statements/index.md)[

pg\_surgery

Extension to perform surgery on a damaged relation

](https://www.postgresql.org/docs/current/pgsurgery.html)[

pg\_trgm

Text similarity measurement and index searching based on trigrams

](https://www.postgresql.org/docs/current/pgtrgm.html)[

pgaudit

Provides auditing functionality

](../pgaudit/index.md)[

pg\_walinspect

Functions to inspect contents of PostgreSQL Write-Ahead Log

](https://www.postgresql.org/docs/current/pgwalinspect.html)[

pgcrypto

Cryptographic functions

](https://www.postgresql.org/docs/current/pgcrypto.html)[

pgjwt

JSON Web Token API for Postgresql

Deprecated in Postgres 17

](../pgjwt/index.md)[

pgroonga

Super fast and all languages supported full text search index based on Groonga

](../pgroonga/index.md)[

pgroonga\_database

PGroonga database management module

](https://pgroonga.github.io/reference/modules/pgroonga-database.html)[

pgrouting

PgRouting Extension

](../pgrouting/index.md)[

pgrowlocks

Show row-level locking information

](https://www.postgresql.org/docs/current/pgrowlocks.html)[

pgsodium

Postgres extension for libsodium functions

](../pgsodium/index.md)[

pgstattuple

Show tuple-level statistics

](https://www.postgresql.org/docs/current/pgstattuple.html)[

pgtap

Unit testing for PostgreSQL

](../pgtap/index.md)[

plcoffee

PL/CoffeeScript (v8) trusted procedural language

Deprecated in Postgres 17

](https://github.com/plv8/plv8/blob/master/doc/plv8.md#coffeescript-extension)[

pljava

PL/Java procedural language (https://tada.github.io/pljava/)

](https://tada.github.io/pljava/)[

plls

PL/LiveScript (v8) trusted procedural language

Deprecated in Postgres 17

](https://github.com/plv8/plv8/blob/master/doc/plv8.md#livescript-extension)[

plpgsql

PL/pgSQL procedural language

](https://www.postgresql.org/docs/current/plpgsql.html)[

plpgsql\_check

Extended check for plpgsql functions

](../plpgsql_check/index.md)[

plv8

PL/JavaScript (v8) trusted procedural language

Deprecated in Postgres 17

](../plv8/index.md)[

postgis

PostGIS geometry and geography spatial types and functions

](../postgis/index.md)[

postgres\_fdw

Foreign-data wrapper for remote PostgreSQL servers

](../postgres_fdw/index.md)[

refint

Functions for implementing referential integrity (obsolete)

](https://www.postgresql.org/docs/current/contrib-spi.html#id-1.11.7.50.5)[

rum

GIN-like index for text search

](../rum/index.md)[

seg

Data type for representing line segments or floating-point intervals

](https://www.postgresql.org/docs/current/seg.html)[

sslinfo

Information about SSL certificates

](https://www.postgresql.org/docs/current/sslinfo.html)[

tablefunc

Functions that manipulate whole tables, including crosstab

](https://www.postgresql.org/docs/current/tablefunc.html)[

tcn

Triggered change notifications

](https://www.postgresql.org/docs/current/tcn.html)[

timescaledb

Enables scalable inserts and complex queries for time-series data

Deprecated in Postgres 17

](../timescaledb/index.md)[

tsm\_system\_rows

TABLESAMPLE method which accepts number of rows as a limit

](https://www.postgresql.org/docs/current/tsm-system-rows.html)[

tsm\_system\_time

TABLESAMPLE method which accepts time in milliseconds as a limit

](https://www.postgresql.org/docs/current/tsm-system-time.html)[

unaccent

Text search dictionary that removes accents

](https://www.postgresql.org/docs/current/unaccent.html)[

uuid-ossp

Generate universally unique identifiers (UUIDs)

](../uuid-ossp/index.md)[

vector

Vector data type with similarity search

](../pgvector/index.md)[

pg\_repack

Optimize physical storage and remove bloat from tables and indexes

](../pg_repack/index.md)[

wrappers

Foreign data wrappers developed by Supabase

](/docs/guides/database/extensions/wrappers/overview)
