---
title: "PostgreSQL: Documentation: 18: 19.18. Short Options"
source: "https://www.postgresql.org/docs/current/runtime-config-short.html"
canonical_url: "https://www.postgresql.org/docs/current/runtime-config-short.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:20.548Z"
content_hash: "58a46078daf8c2cfb44299b442d844c6502571681c7108a8014c7c4829da3213"
menu_path: ["PostgreSQL: Documentation: 18: 19.18. Short Options"]
section_path: []
nav_prev: {"path": "postgres/docs/current/runtime-config-resource.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.4.\u00a0Resource Consumption"}
nav_next: {"path": "postgres/docs/current/runtime-config-statistics.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.9.\u00a0Run-time Statistics"}
---

Short Option

Equivalent

``-B _`x`_``

``shared_buffers = _`x`_``

``-d _`x`_``

``log_min_messages = DEBUG_`x`_``

`-e`

`datestyle = euro`

`-fb`, `-fh`, `-fi`, `-fm`, `-fn`, `-fo`, `-fs`, `-ft`

`enable_bitmapscan = off`, `enable_hashjoin = off`, `enable_indexscan = off`, `enable_mergejoin = off`, `enable_nestloop = off`, `enable_indexonlyscan = off`, `enable_seqscan = off`, `enable_tidscan = off`

`-F`

`fsync = off`

``-h _`x`_``

``listen_addresses = _`x`_``

`-i`

`listen_addresses = '*'`

``-k _`x`_``

``unix_socket_directories = _`x`_``

`-l`

`ssl = on`

``-N _`x`_``

``max_connections = _`x`_``

`-O`

`allow_system_table_mods = on`

``-p _`x`_``

``port = _`x`_``

`-P`

`ignore_system_indexes = on`

`-s`

`log_statement_stats = on`

``-S _`x`_``

``work_mem = _`x`_``

`-tpa`, `-tpl`, `-te`

`log_parser_stats = on`, `log_planner_stats = on`, `log_executor_stats = on`

``-W _`x`_``

``post_auth_delay = _`x`_``
