---
title: "PostgreSQL: Documentation: 18: 52.54. pg_subscription"
source: "https://www.postgresql.org/docs/current/catalog-pg-subscription.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-subscription.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:43.904Z"
content_hash: "abe3e07e84aa92d6a8abae48597e8cf50a3c950457a8584367e8ba16d1c0d902"
menu_path: ["PostgreSQL: Documentation: 18: 52.54. pg_subscription"]
section_path: []
content_language: "en"
---
The catalog `pg_subscription` contains all existing logical replication subscriptions. For more information about logical replication see [Chapter 29](https://www.postgresql.org/docs/current/logical-replication.html "Chapter 29. Logical Replication").

Unlike most system catalogs, `pg_subscription` is shared across all databases of a cluster: there is only one copy of `pg_subscription` per cluster, not one per database.

Access to the column `subconninfo` is revoked from normal users, because it could contain plain-text passwords.

**Table 52.54. `pg_subscription` Columns**

| 
Column Type

Description

 |
| --- |
| 

`oid` `oid`

Row identifier

 |
| 

`subdbid` `oid` (references [`pg_database`](https://www.postgresql.org/docs/current/catalog-pg-database.html "52.15. pg_database").`oid`)

OID of the database that the subscription resides in

 |
| 

`subskiplsn` `pg_lsn`

Finish LSN of the transaction whose changes are to be skipped, if a valid LSN; otherwise `0/0`.

 |
| 

`subname` `name`

Name of the subscription

 |
| 

`subowner` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

Owner of the subscription

 |
| 

`subenabled` `bool`

If true, the subscription is enabled and should be replicating

 |
| 

`subbinary` `bool`

If true, the subscription will request that the publisher send data in binary format

 |
| 

`substream` `char`

Controls how to handle the streaming of in-progress transactions: `f` = disallow streaming of in-progress transactions, `t` = spill the changes of in-progress transactions to disk and apply at once after the transaction is committed on the publisher and received by the subscriber, `p` = apply changes directly using a parallel apply worker if available (same as `t` if no worker is available)

 |
| 

`subtwophasestate` `char`

State codes for two-phase mode: `d` = disabled, `p` = pending enablement, `e` = enabled

 |
| 

`subdisableonerr` `bool`

If true, the subscription will be disabled if one of its workers detects an error

 |
| 

`subpasswordrequired` `bool`

If true, the subscription will be required to specify a password for authentication

 |
| 

`subrunasowner` `bool`

If true, the subscription will be run with the permissions of the subscription owner

 |
| 

`subfailover` `bool`

If true, the associated replication slots (i.e. the main slot and the table synchronization slots) in the upstream database are enabled to be synchronized to the standbys

 |
| 

`subconninfo` `text`

Connection string to the upstream database

 |
| 

`subslotname` `name`

Name of the replication slot in the upstream database (also used for the local replication origin name); null represents `NONE`

 |
| 

`subsynccommit` `text`

The `synchronous_commit` setting for the subscription's workers to use

 |
| 

`subpublications` `text[]`

Array of subscribed publication names. These reference publications defined in the upstream database. For more on publications see [Section 29.1](https://www.postgresql.org/docs/current/logical-replication-publication.html "29.1. Publication").

 |
| 

`suborigin` `text`

The origin value must be either `none` or `any`. The default is `any`. If `none`, the subscription will request the publisher to only send changes that don't have an origin. If `any`, the publisher sends changes regardless of their origin.

 |
