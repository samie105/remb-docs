---
title: "Manual Replication Setup"
source: "https://supabase.com/docs/guides/database/replication/manual-replication-setup"
canonical_url: "https://supabase.com/docs/guides/database/replication/manual-replication-setup"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:57.480Z"
content_hash: "d8c79034a4ab8553473a57a1f6bc2b063e9111882bc042628cd01db86dcc2a2c"
menu_path: ["Database","Database","More","More","More","Manual replication","Manual replication","Setting up","Setting up"]
section_path: ["Database","Database","More","More","More","Manual replication","Manual replication","Setting up","Setting up"]
nav_prev: {"path": "supabase/docs/guides/database/replication/manual-replication-monitoring/index.md", "title": "Manual Replication Monitoring"}
nav_next: {"path": "supabase/docs/guides/database/replication/replication-faq/index.md", "title": "Replication FAQ"}
---

# 

Manual Replication Setup

## 

Set up replication with Airbyte, Estuary, Fivetran, and other tools.

* * *

This guide covers setting up **manual logical replication** using external tools. If you prefer a simpler, managed solution, read [the Replication setup docs](/docs/guides/database/replication/replication-setup) instead.

This guide is for replicating data to external systems using your own tools. For deploying read-only databases across multiple regions, see [Read Replicas](/docs/guides/platform/read-replicas) instead.

### Prerequisites[#](#prerequisites)

To set up replication, the following is recommended:

*   Instance size of XL or greater
*   [IPv4 add-on](/docs/guides/platform/ipv4-address) enabled

To create a replication slot, you will need to use the `postgres` user and follow the instructions in the [external replication setup guide](/docs/guides/database/postgres/setup-replication-external).

If you are running Postgres 17 or higher, you can create a new user and grant them replication permissions with the `postgres` user. For versions below 17, you will need to use the `postgres` user.

If you are replicating to an external system and using any of the tools below, check their documentation first. Additional information is provided where the setup with Supabase can vary.

Estuary has the following [documentation](https://docs.estuary.dev/reference/Connectors/capture-connectors/PostgreSQL/Supabase/) for setting up Postgres as a source.
