---
title: "Manual Replication FAQ"
source: "https://supabase.com/docs/guides/database/replication/manual-replication-faq"
canonical_url: "https://supabase.com/docs/guides/database/replication/manual-replication-faq"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:52.842Z"
content_hash: "5fd6f9672c062f16494d59117b4f0be99c8b78ec584bfcf36f760368c4002f53"
menu_path: ["Database","Database","More","More","More","Manual replication","Manual replication","FAQ","FAQ"]
section_path: ["Database","Database","More","More","More","Manual replication","Manual replication","FAQ","FAQ"]
nav_prev: {"path": "supabase/docs/guides/database/replication/index.md", "title": "Database Replication"}
nav_next: {"path": "supabase/docs/guides/database/replication/manual-replication-monitoring/index.md", "title": "Manual Replication Monitoring"}
---

# 

Manual Replication FAQ

## 

Common questions and considerations when setting up manual replication.

* * *

## Which connection string should be used?[#](#which-connection-string-should-be-used)

Always use the direct connection string for logical replication.

Connections through a pooler, such as Supavisor, will not work.

## The tool in use does not support IPv6[#](#the-tool-in-use-does-not-support-ipv6)

You can enable the [IPv4 add-on](../../../platform/ipv4-address/index.md) for your project.

## What is XMIN and should it be used?[#](#what-is-xmin-and-should-it-be-used)

Xmin is a different form of replication from logical replication and should only be used if logical replication is not available for your database (i.e. older versions of Postgres).

Xmin performs replication by checking the [xmin system column](https://www.postgresql.org/docs/current/ddl-system-columns.html) and determining if that row has already been synchronized.

It does not capture deletion of data and is **not recommended**, particularly for larger databases.

## Can replication be configured in the Dashboard?[#](#can-replication-be-configured-in-the-dashboard)

You can view [publications](/dashboard/project/default/database/publications) in the Dashboard but all steps to configure replication must be done using the [SQL Editor](/dashboard/project/default/sql/new) or a CLI tool of your choice.

## How to configure database settings for replication?[#](#how-to-configure-database-settings-for-replication)

Using the Supabase CLI, you can [configure database settings](../../custom-postgres-config/index.md#cli-configurable-settings) to optimize them for your replication needs. These values can vary depending on your database size and activity.

## What are some important configuration options?[#](#what-are-some-important-configuration-options)

Some of the more important options to be aware of are:

*   `max_wal_size` - Maximum size the WAL can grow between automatic WAL checkpoints
*   `max_slot_wal_keep_size` - Maximum size of WAL files that replication slots are allowed to retain
*   `wal_keep_size` - Minimum number of past WAL files to keep for standby servers
*   `max_wal_senders` - Maximum number of concurrent connections from standby servers or streaming backup clients

These settings help ensure your replication slots don't run out of space and that replicas can reconnect without requiring a full re-sync.
