---
title: "PostgreSQL: Documentation: 18: 52.55. pg_subscription_rel"
source: "https://www.postgresql.org/docs/current/catalog-pg-subscription-rel.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-subscription-rel.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:05.951Z"
content_hash: "d91ec7ab3b45915b908214fe6797fa76c88338987a15c96721c78ceffa8c84f2"
menu_path: ["PostgreSQL: Documentation: 18: 52.55. pg_subscription_rel"]
section_path: []
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-subscription-rel.html "PostgreSQL devel - 52.55. pg_subscription_rel")

The catalog `pg_subscription_rel` contains the state for each replicated relation in each subscription. This is a many-to-many mapping.

This catalog only contains tables known to the subscription after running either [`CREATE SUBSCRIPTION`](https://www.postgresql.org/docs/current/sql-createsubscription.html "CREATE SUBSCRIPTION") or [`ALTER SUBSCRIPTION ... REFRESH PUBLICATION`](https://www.postgresql.org/docs/current/sql-altersubscription.html "ALTER SUBSCRIPTION").

**Table 52.55. `pg_subscription_rel` Columns**

Column Type

Description

`srsubid` `oid` (references [`pg_subscription`](https://www.postgresql.org/docs/current/catalog-pg-subscription.html "52.54. pg_subscription").`oid`)

Reference to subscription

`srrelid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

Reference to relation

`srsubstate` `char`

State code: `i` = initialize, `d` = data is being copied, `f` = finished table copy, `s` = synchronized, `r` = ready (normal replication)

`srsublsn` `pg_lsn`

Remote LSN of the state change used for synchronization coordination when in `s` or `r` states, otherwise null
