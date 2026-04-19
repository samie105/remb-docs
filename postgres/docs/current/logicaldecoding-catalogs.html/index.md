---
title: "PostgreSQL: Documentation: 18: 47.5. System Catalogs Related to Logical Decoding"
source: "https://www.postgresql.org/docs/current/logicaldecoding-catalogs.html"
canonical_url: "https://www.postgresql.org/docs/current/logicaldecoding-catalogs.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:05.323Z"
content_hash: "69ef91ffa72497b4a345b5febc038cd0b9829ce3cd9341469da9e4e7a94fc531"
menu_path: ["PostgreSQL: Documentation: 18: 47.5. System Catalogs Related to Logical Decoding"]
section_path: []
nav_prev: {"path": "postgres/docs/current/logical-replication-upgrade.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.13.\u00a0Upgrade"}
nav_next: {"path": "postgres/docs/current/logicaldecoding-two-phase-commits.html/index.md", "title": "PostgreSQL: Documentation: 18: 47.10.\u00a0Two-phase Commit Support for Logical Decoding"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/logicaldecoding-catalogs.html "PostgreSQL devel - 47.5. System Catalogs Related to Logical Decoding")

47.5. System Catalogs Related to Logical Decoding

[Prev](https://www.postgresql.org/docs/current/logicaldecoding-sql.html "47.4. Logical Decoding SQL Interface") 

[Up](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding")

Chapter 47. Logical Decoding

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html "47.6. Logical Decoding Output Plugins")

* * *

The [`pg_replication_slots`](https://www.postgresql.org/docs/current/view-pg-replication-slots.html "53.20. pg_replication_slots") view and the [`pg_stat_replication`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW "27.2.4. pg_stat_replication") view provide information about the current state of replication slots and streaming replication connections respectively. These views apply to both physical and logical replication. The [`pg_stat_replication_slots`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-SLOTS-VIEW "27.2.5. pg_stat_replication_slots") view provides statistics information about the logical replication slots.

* * *

[Prev](https://www.postgresql.org/docs/current/logicaldecoding-sql.html "47.4. Logical Decoding SQL Interface") 

[Up](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding")

 [Next](https://www.postgresql.org/docs/current/logicaldecoding-output-plugin.html "47.6. Logical Decoding Output Plugins")

47.4. Logical Decoding SQL Interface 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 47.6. Logical Decoding Output Plugins
