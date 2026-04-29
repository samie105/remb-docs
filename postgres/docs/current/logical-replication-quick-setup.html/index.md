---
title: "PostgreSQL: Documentation: 18: 29.14. Quick Setup"
source: "https://www.postgresql.org/docs/current/logical-replication-quick-setup.html"
canonical_url: "https://www.postgresql.org/docs/current/logical-replication-quick-setup.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:07.228Z"
content_hash: "59b985344102ad23603a4d38ea4881cb98f1a67bc34558d7e31d7168824055bf"
menu_path: ["PostgreSQL: Documentation: 18: 29.14. Quick Setup"]
section_path: []
nav_prev: {"path": "../logical-replication-publication.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.1.\u00a0Publication"}
nav_next: {"path": "../logical-replication-restrictions.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.8.\u00a0Restrictions"}
---

First set the configuration options in `postgresql.conf`:

wal\_level = logical

The other required settings have default values that are sufficient for a basic setup.

`pg_hba.conf` needs to be adjusted to allow replication (the values here depend on your actual network configuration and user you want to use for connecting):

host     all     repuser     0.0.0.0/0     scram-sha-256

Then on the publisher database:

CREATE PUBLICATION mypub FOR TABLE users, departments;

And on the subscriber database:

CREATE SUBSCRIPTION mysub CONNECTION 'dbname=foo host=bar user=repuser' PUBLICATION mypub;

The above will start the replication process, which synchronizes the initial table contents of the tables `users` and `departments` and then starts replicating incremental changes to those tables.
