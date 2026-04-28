---
title: "PostgreSQL: Documentation: 18: 53.1. Overview"
source: "https://www.postgresql.org/docs/current/views-overview.html"
canonical_url: "https://www.postgresql.org/docs/current/views-overview.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:46:54.655Z"
content_hash: "5faeffebf71c738710055bc9857df17b957fcb5c4377aeb9a90e956d6247b762"
menu_path: ["PostgreSQL: Documentation: 18: 53.1. Overview"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/view-pg-wait-events.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.38.\u00a0pg_wait_events"}
nav_next: {"path": "postgres/docs/current/wal-async-commit.html/index.md", "title": "PostgreSQL: Documentation: 18: 28.4.\u00a0Asynchronous Commit"}
---

| View Name | Purpose |
| --- | --- |
| [`pg_aios`](https://www.postgresql.org/docs/current/view-pg-aios.html "53.2. pg_aios") | In-use asynchronous IO handles |
| [`pg_available_extensions`](https://www.postgresql.org/docs/current/view-pg-available-extensions.html "53.3. pg_available_extensions") | available extensions |
| [`pg_available_extension_versions`](https://www.postgresql.org/docs/current/view-pg-available-extension-versions.html "53.4. pg_available_extension_versions") | available versions of extensions |
| [`pg_backend_memory_contexts`](https://www.postgresql.org/docs/current/view-pg-backend-memory-contexts.html "53.5. pg_backend_memory_contexts") | backend memory contexts |
| [`pg_config`](https://www.postgresql.org/docs/current/view-pg-config.html "53.6. pg_config") | compile-time configuration parameters |
| [`pg_cursors`](https://www.postgresql.org/docs/current/view-pg-cursors.html "53.7. pg_cursors") | open cursors |
| [`pg_file_settings`](https://www.postgresql.org/docs/current/view-pg-file-settings.html "53.8. pg_file_settings") | summary of configuration file contents |
| [`pg_group`](https://www.postgresql.org/docs/current/view-pg-group.html "53.9. pg_group") | groups of database users |
| [`pg_hba_file_rules`](https://www.postgresql.org/docs/current/view-pg-hba-file-rules.html "53.10. pg_hba_file_rules") | summary of client authentication configuration file contents |
| [`pg_ident_file_mappings`](https://www.postgresql.org/docs/current/view-pg-ident-file-mappings.html "53.11. pg_ident_file_mappings") | summary of client user name mapping configuration file contents |
| [`pg_indexes`](https://www.postgresql.org/docs/current/view-pg-indexes.html "53.12. pg_indexes") | indexes |
| [`pg_locks`](https://www.postgresql.org/docs/current/view-pg-locks.html "53.13. pg_locks") | locks currently held or awaited |
| [`pg_matviews`](https://www.postgresql.org/docs/current/view-pg-matviews.html "53.14. pg_matviews") | materialized views |
| [`pg_policies`](https://www.postgresql.org/docs/current/view-pg-policies.html "53.15. pg_policies") | policies |
| [`pg_prepared_statements`](https://www.postgresql.org/docs/current/view-pg-prepared-statements.html "53.16. pg_prepared_statements") | prepared statements |
| [`pg_prepared_xacts`](https://www.postgresql.org/docs/current/view-pg-prepared-xacts.html "53.17. pg_prepared_xacts") | prepared transactions |
| [`pg_publication_tables`](https://www.postgresql.org/docs/current/view-pg-publication-tables.html "53.18. pg_publication_tables") | publications and information of their associated tables |
| [`pg_replication_origin_status`](https://www.postgresql.org/docs/current/view-pg-replication-origin-status.html "53.19. pg_replication_origin_status") | information about replication origins, including replication progress |
| [`pg_replication_slots`](https://www.postgresql.org/docs/current/view-pg-replication-slots.html "53.20. pg_replication_slots") | replication slot information |
| [`pg_roles`](https://www.postgresql.org/docs/current/view-pg-roles.html "53.21. pg_roles") | database roles |
| [`pg_rules`](https://www.postgresql.org/docs/current/view-pg-rules.html "53.22. pg_rules") | rules |
| [`pg_seclabels`](https://www.postgresql.org/docs/current/view-pg-seclabels.html "53.23. pg_seclabels") | security labels |
| [`pg_sequences`](https://www.postgresql.org/docs/current/view-pg-sequences.html "53.24. pg_sequences") | sequences |
| [`pg_settings`](https://www.postgresql.org/docs/current/view-pg-settings.html "53.25. pg_settings") | parameter settings |
| [`pg_shadow`](https://www.postgresql.org/docs/current/view-pg-shadow.html "53.26. pg_shadow") | database users |
| [`pg_shmem_allocations`](https://www.postgresql.org/docs/current/view-pg-shmem-allocations.html "53.27. pg_shmem_allocations") | shared memory allocations |
| [`pg_shmem_allocations_numa`](https://www.postgresql.org/docs/current/view-pg-shmem-allocations-numa.html "53.28. pg_shmem_allocations_numa") | NUMA node mappings for shared memory allocations |
| [`pg_stats`](https://www.postgresql.org/docs/current/view-pg-stats.html "53.29. pg_stats") | planner statistics |
| [`pg_stats_ext`](https://www.postgresql.org/docs/current/view-pg-stats-ext.html "53.30. pg_stats_ext") | extended planner statistics |
| [`pg_stats_ext_exprs`](https://www.postgresql.org/docs/current/view-pg-stats-ext-exprs.html "53.31. pg_stats_ext_exprs") | extended planner statistics for expressions |
| [`pg_tables`](https://www.postgresql.org/docs/current/view-pg-tables.html "53.32. pg_tables") | tables |
| [`pg_timezone_abbrevs`](https://www.postgresql.org/docs/current/view-pg-timezone-abbrevs.html "53.33. pg_timezone_abbrevs") | time zone abbreviations |
| [`pg_timezone_names`](https://www.postgresql.org/docs/current/view-pg-timezone-names.html "53.34. pg_timezone_names") | time zone names |
| [`pg_user`](https://www.postgresql.org/docs/current/view-pg-user.html "53.35. pg_user") | database users |
| [`pg_user_mappings`](https://www.postgresql.org/docs/current/view-pg-user-mappings.html "53.36. pg_user_mappings") | user mappings |
| [`pg_views`](https://www.postgresql.org/docs/current/view-pg-views.html "53.37. pg_views") | views |
| [`pg_wait_events`](https://www.postgresql.org/docs/current/view-pg-wait-events.html "53.38. pg_wait_events") | wait events |
