---
title: "PostgreSQL: Documentation: 18: 19.15. Preset Options"
source: "https://www.postgresql.org/docs/current/runtime-config-preset.html"
canonical_url: "https://www.postgresql.org/docs/current/runtime-config-preset.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:04.993Z"
content_hash: "17282963ce587cf3b5d95dd9b9aa04cf510268281264118bedb31394aff364cd"
menu_path: ["PostgreSQL: Documentation: 18: 19.15. Preset Options"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-spi-register-relation.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_register_relation"}
nav_next: {"path": "postgres/docs/current/pgtesttiming.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_test_timing"}
---

The following “parameters” are read-only. As such, they have been excluded from the sample `postgresql.conf` file. These options report various aspects of PostgreSQL behavior that might be of interest to certain applications, particularly administrative front-ends. Most of them are determined when PostgreSQL is compiled or when it is installed.

`block_size` (`integer`) [#](#GUC-BLOCK-SIZE)

Reports the size of a disk block. It is determined by the value of `BLCKSZ` when building the server. The default value is 8192 bytes. The meaning of some configuration variables (such as [shared\_buffers](postgres/docs/current/runtime-config-resource.html/index.md#GUC-SHARED-BUFFERS)) is influenced by `block_size`. See [Section 19.4](https://www.postgresql.org/docs/current/runtime-config-resource.html "19.4. Resource Consumption") for information.

`data_checksums` (`boolean`) [#](#GUC-DATA-CHECKSUMS)

Reports whether data checksums are enabled for this cluster. See [`-k`](https://www.postgresql.org/docs/current/app-initdb.html#APP-INITDB-DATA-CHECKSUMS) for more information.

`data_directory_mode` (`integer`) [#](#GUC-DATA-DIRECTORY-MODE)

On Unix systems this parameter reports the permissions the data directory (defined by [data\_directory](https://www.postgresql.org/docs/current/runtime-config-file-locations.html#GUC-DATA-DIRECTORY)) had at server startup. (On Microsoft Windows this parameter will always display `0700`.) See [the initdb `-g` option](https://www.postgresql.org/docs/current/app-initdb.html#APP-INITDB-ALLOW-GROUP-ACCESS) for more information.

`debug_assertions` (`boolean`) [#](#GUC-DEBUG-ASSERTIONS)

Reports whether PostgreSQL has been built with assertions enabled. That is the case if the macro `USE_ASSERT_CHECKING` is defined when PostgreSQL is built (accomplished e.g., by the `configure` option `--enable-cassert`). By default PostgreSQL is built without assertions.

`huge_pages_status` (`enum`) [#](#GUC-HUGE-PAGES-STATUS)

Reports the state of huge pages in the current instance: `on`, `off`, or `unknown` (if displayed with `postgres -C`). This parameter is useful to determine whether allocation of huge pages was successful under `huge_pages=try`. See [huge\_pages](postgres/docs/current/runtime-config-resource.html/index.md#GUC-HUGE-PAGES) for more information.

`integer_datetimes` (`boolean`) [#](#GUC-INTEGER-DATETIMES)

Reports whether PostgreSQL was built with support for 64-bit-integer dates and times. As of PostgreSQL 10, this is always `on`.

`in_hot_standby` (`boolean`) [#](#GUC-IN-HOT-STANDBY)

Reports whether the server is currently in hot standby mode. When this is `on`, all transactions are forced to be read-only. Within a session, this can change only if the server is promoted to be primary. See [Section 26.4](https://www.postgresql.org/docs/current/hot-standby.html "26.4. Hot Standby") for more information.

`max_function_args` (`integer`) [#](#GUC-MAX-FUNCTION-ARGS)

Reports the maximum number of function arguments. It is determined by the value of `FUNC_MAX_ARGS` when building the server. The default value is 100 arguments.

`max_identifier_length` (`integer`) [#](#GUC-MAX-IDENTIFIER-LENGTH)

Reports the maximum identifier length. It is determined as one less than the value of `NAMEDATALEN` when building the server. The default value of `NAMEDATALEN` is 64; therefore the default `max_identifier_length` is 63 bytes, which can be less than 63 characters when using multibyte encodings.

`max_index_keys` (`integer`) [#](#GUC-MAX-INDEX-KEYS)

Reports the maximum number of index keys. It is determined by the value of `INDEX_MAX_KEYS` when building the server. The default value is 32 keys.

`num_os_semaphores` (`integer`) [#](#GUC-NUM-OS-SEMAPHORES)

Reports the number of semaphores that are needed for the server based on the configured number of allowed connections ([max\_connections](postgres/docs/current/runtime-config-connection.html/index.md#GUC-MAX-CONNECTIONS)), allowed autovacuum worker processes ([autovacuum\_max\_workers](postgres/docs/current/runtime-config-vacuum.html/index.md#GUC-AUTOVACUUM-MAX-WORKERS)), allowed WAL sender processes ([max\_wal\_senders](postgres/docs/current/runtime-config-replication.html/index.md#GUC-MAX-WAL-SENDERS)), allowed background processes ([max\_worker\_processes](postgres/docs/current/runtime-config-resource.html/index.md#GUC-MAX-WORKER-PROCESSES)), etc.

`segment_size` (`integer`) [#](#GUC-SEGMENT-SIZE)

Reports the number of blocks (pages) that can be stored within a file segment. It is determined by the value of `RELSEG_SIZE` when building the server. The maximum size of a segment file in bytes is equal to `segment_size` multiplied by `block_size`; by default this is 1GB.

`server_encoding` (`string`) [#](#GUC-SERVER-ENCODING)

Reports the database encoding (character set). It is determined when the database is created. Ordinarily, clients need only be concerned with the value of [client\_encoding](postgres/docs/current/runtime-config-client.html/index.md#GUC-CLIENT-ENCODING).

`server_version` (`string`) [#](#GUC-SERVER-VERSION)

Reports the version number of the server. It is determined by the value of `PG_VERSION` when building the server.

`server_version_num` (`integer`) [#](#GUC-SERVER-VERSION-NUM)

Reports the version number of the server as an integer. It is determined by the value of `PG_VERSION_NUM` when building the server.

`shared_memory_size` (`integer`) [#](#GUC-SHARED-MEMORY-SIZE)

Reports the size of the main shared memory area, rounded up to the nearest megabyte.

`shared_memory_size_in_huge_pages` (`integer`) [#](#GUC-SHARED-MEMORY-SIZE-IN-HUGE-PAGES)

Reports the number of huge pages that are needed for the main shared memory area based on the specified [huge\_page\_size](postgres/docs/current/runtime-config-resource.html/index.md#GUC-HUGE-PAGE-SIZE). If huge pages are not supported, this will be `-1`.

This setting is supported only on Linux. It is always set to `-1` on other platforms. For more details about using huge pages on Linux, see [Section 18.4.5](https://www.postgresql.org/docs/current/kernel-resources.html#LINUX-HUGE-PAGES "18.4.5. Linux Huge Pages").

`ssl_library` (`string`) [#](#GUC-SSL-LIBRARY)

Reports the name of the SSL library that this PostgreSQL server was built with (even if SSL is not currently configured or in use on this instance), for example `OpenSSL`, or an empty string if none.

`wal_block_size` (`integer`) [#](#GUC-WAL-BLOCK-SIZE)

Reports the size of a WAL disk block. It is determined by the value of `XLOG_BLCKSZ` when building the server. The default value is 8192 bytes.

`wal_segment_size` (`integer`) [#](#GUC-WAL-SEGMENT-SIZE)

Reports the size of write ahead log segments. The default value is 16MB. See [Section 28.5](https://www.postgresql.org/docs/current/wal-configuration.html "28.5. WAL Configuration") for more information.

