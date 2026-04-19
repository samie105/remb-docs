---
title: "PostgreSQL: Documentation: 18: 19.4. Resource Consumption"
source: "https://www.postgresql.org/docs/current/runtime-config-resource.html"
canonical_url: "https://www.postgresql.org/docs/current/runtime-config-resource.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:25.673Z"
content_hash: "4081d9e169fb1045d63d2c91434881dc38bc26c169cb67120f16b66d9a8573e2"
menu_path: ["PostgreSQL: Documentation: 18: 19.4. Resource Consumption"]
section_path: []
nav_prev: {"path": "postgres/docs/current/runtime-config-replication.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.6.\u00a0Replication"}
nav_next: {"path": "postgres/docs/current/runtime-config-short.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.18.\u00a0Short Options"}
---

`shared_buffers` (`integer`) [#](#GUC-SHARED-BUFFERS)

Sets the amount of memory the database server uses for shared memory buffers. The default is typically 128 megabytes (`128MB`), but might be less if your kernel settings will not support it (as determined during initdb). This setting must be at least 128 kilobytes. However, settings significantly higher than the minimum are usually needed for good performance. If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. (Non-default values of `BLCKSZ` change the minimum value.) This parameter can only be set at server start.

If you have a dedicated database server with 1GB or more of RAM, a reasonable starting value for `shared_buffers` is 25% of the memory in your system. There are some workloads where even larger settings for `shared_buffers` are effective, but because PostgreSQL also relies on the operating system cache, it is unlikely that an allocation of more than 40% of RAM to `shared_buffers` will work better than a smaller amount. Larger settings for `shared_buffers` usually require a corresponding increase in `max_wal_size`, in order to spread out the process of writing large quantities of new or changed data over a longer period of time.

On systems with less than 1GB of RAM, a smaller percentage of RAM is appropriate, so as to leave adequate space for the operating system.

`huge_pages` (`enum`) [#](#GUC-HUGE-PAGES)

Controls whether huge pages are requested for the main shared memory area. Valid values are `try` (the default), `on`, and `off`. This parameter can only be set at server start. With `huge_pages` set to `try`, the server will try to request huge pages, but fall back to the default if that fails. With `on`, failure to request huge pages will prevent the server from starting up. With `off`, huge pages will not be requested. The actual state of huge pages is indicated by the server variable [huge\_pages\_status](postgres/docs/current/runtime-config-preset.html/index.md#GUC-HUGE-PAGES-STATUS).

At present, this setting is supported only on Linux and Windows. The setting is ignored on other systems when set to `try`. On Linux, it is only supported when `shared_memory_type` is set to `mmap` (the default).

The use of huge pages results in smaller page tables and less CPU time spent on memory management, increasing performance. For more details about using huge pages on Linux, see [Section 18.4.5](https://www.postgresql.org/docs/current/kernel-resources.html#LINUX-HUGE-PAGES "18.4.5. Linux Huge Pages").

Huge pages are known as large pages on Windows. To use them, you need to assign the user right “Lock pages in memory” to the Windows user account that runs PostgreSQL. You can use Windows Group Policy tool (gpedit.msc) to assign the user right “Lock pages in memory”. To start the database server on the command prompt as a standalone process, not as a Windows service, the command prompt must be run as an administrator or User Access Control (UAC) must be disabled. When the UAC is enabled, the normal command prompt revokes the user right “Lock pages in memory” when started.

Note that this setting only affects the main shared memory area. Operating systems such as Linux, FreeBSD, and Illumos can also use huge pages (also known as “super” pages or “large” pages) automatically for normal memory allocation, without an explicit request from PostgreSQL. On Linux, this is called “transparent huge pages” (THP). That feature has been known to cause performance degradation with PostgreSQL for some users on some Linux versions, so its use is currently discouraged (unlike explicit use of `huge_pages`).

`huge_page_size` (`integer`) [#](#GUC-HUGE-PAGE-SIZE)

Controls the size of huge pages, when they are enabled with [huge\_pages](postgres/docs/current/runtime-config-resource.html/index.md#GUC-HUGE-PAGES). The default is zero (`0`). When set to `0`, the default huge page size on the system will be used. This parameter can only be set at server start.

Some commonly available page sizes on modern 64 bit server architectures include: `2MB` and `1GB` (Intel and AMD), `16MB` and `16GB` (IBM POWER), and `64kB`, `2MB`, `32MB` and `1GB` (ARM). For more information about usage and support, see [Section 18.4.5](https://www.postgresql.org/docs/current/kernel-resources.html#LINUX-HUGE-PAGES "18.4.5. Linux Huge Pages").

Non-default settings are currently supported only on Linux.

`temp_buffers` (`integer`) [#](#GUC-TEMP-BUFFERS)

Sets the maximum amount of memory used for temporary buffers within each database session. These are session-local buffers used only for access to temporary tables. If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default is eight megabytes (`8MB`). (If `BLCKSZ` is not 8kB, the default value scales proportionally to it.) This setting can be changed within individual sessions, but only before the first use of temporary tables within the session; subsequent attempts to change the value will have no effect on that session.

A session will allocate temporary buffers as needed up to the limit given by `temp_buffers`. The cost of setting a large value in sessions that do not actually need many temporary buffers is only a buffer descriptor, or about 64 bytes, per increment in `temp_buffers`. However if a buffer is actually used an additional 8192 bytes will be consumed for it (or in general, `BLCKSZ` bytes).

`max_prepared_transactions` (`integer`) [#](#GUC-MAX-PREPARED-TRANSACTIONS)

Sets the maximum number of transactions that can be in the “prepared” state simultaneously (see [PREPARE TRANSACTION](https://www.postgresql.org/docs/current/sql-prepare-transaction.html "PREPARE TRANSACTION")). Setting this parameter to zero (which is the default) disables the prepared-transaction feature. This parameter can only be set at server start.

If you are not planning to use prepared transactions, this parameter should be set to zero to prevent accidental creation of prepared transactions. If you are using prepared transactions, you will probably want `max_prepared_transactions` to be at least as large as [max\_connections](postgres/docs/current/runtime-config-connection.html/index.md#GUC-MAX-CONNECTIONS), so that every session can have a prepared transaction pending.

When running a standby server, you must set this parameter to the same or higher value than on the primary server. Otherwise, queries will not be allowed in the standby server.

`work_mem` (`integer`) [#](#GUC-WORK-MEM)

Sets the base maximum amount of memory to be used by a query operation (such as a sort or hash table) before writing to temporary disk files. If this value is specified without units, it is taken as kilobytes. The default value is four megabytes (`4MB`). Note that a complex query might perform several sort and hash operations at the same time, with each operation generally being allowed to use as much memory as this value specifies before it starts to write data into temporary files. Also, several running sessions could be doing such operations concurrently. Therefore, the total memory used could be many times the value of `work_mem`; it is necessary to keep this fact in mind when choosing the value. Sort operations are used for `ORDER BY`, `DISTINCT`, and merge joins. Hash tables are used in hash joins, hash-based aggregation, memoize nodes and hash-based processing of `IN` subqueries.

Hash-based operations are generally more sensitive to memory availability than equivalent sort-based operations. The memory limit for a hash table is computed by multiplying `work_mem` by `hash_mem_multiplier`. This makes it possible for hash-based operations to use an amount of memory that exceeds the usual `work_mem` base amount.

`hash_mem_multiplier` (`floating point`) [#](#GUC-HASH-MEM-MULTIPLIER)

Used to compute the maximum amount of memory that hash-based operations can use. The final limit is determined by multiplying `work_mem` by `hash_mem_multiplier`. The default value is 2.0, which makes hash-based operations use twice the usual `work_mem` base amount.

Consider increasing `hash_mem_multiplier` in environments where spilling by query operations is a regular occurrence, especially when simply increasing `work_mem` results in memory pressure (memory pressure typically takes the form of intermittent out of memory errors). The default setting of 2.0 is often effective with mixed workloads. Higher settings in the range of 2.0 - 8.0 or more may be effective in environments where `work_mem` has already been increased to 40MB or more.

`maintenance_work_mem` (`integer`) [#](#GUC-MAINTENANCE-WORK-MEM)

Specifies the maximum amount of memory to be used by maintenance operations, such as `VACUUM`, `CREATE INDEX`, and `ALTER TABLE ADD FOREIGN KEY`. If this value is specified without units, it is taken as kilobytes. It defaults to 64 megabytes (`64MB`). Since only one of these operations can be executed at a time by a database session, and an installation normally doesn't have many of them running concurrently, it's safe to set this value significantly larger than `work_mem`. Larger settings might improve performance for vacuuming and for restoring database dumps.

Note that when autovacuum runs, up to [autovacuum\_max\_workers](postgres/docs/current/runtime-config-vacuum.html/index.md#GUC-AUTOVACUUM-MAX-WORKERS) times this memory may be allocated, so be careful not to set the default value too high. It may be useful to control for this by separately setting [autovacuum\_work\_mem](postgres/docs/current/runtime-config-resource.html/index.md#GUC-AUTOVACUUM-WORK-MEM).

`autovacuum_work_mem` (`integer`) [#](#GUC-AUTOVACUUM-WORK-MEM)

Specifies the maximum amount of memory to be used by each autovacuum worker process. If this value is specified without units, it is taken as kilobytes. It defaults to -1, indicating that the value of [maintenance\_work\_mem](postgres/docs/current/runtime-config-resource.html/index.md#GUC-MAINTENANCE-WORK-MEM) should be used instead. The setting has no effect on the behavior of `VACUUM` when run in other contexts. This parameter can only be set in the `postgresql.conf` file or on the server command line.

`vacuum_buffer_usage_limit` (`integer`) [#](#GUC-VACUUM-BUFFER-USAGE-LIMIT)

Specifies the size of the [](postgres/docs/current/glossary.html/index.md#GLOSSARY-BUFFER-ACCESS-STRATEGY)[Buffer Access Strategy](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BUFFER-ACCESS-STRATEGY "Buffer Access Strategy") used by the `VACUUM` and `ANALYZE` commands. A setting of `0` will allow the operation to use any number of `shared_buffers`. Otherwise valid sizes range from `128 kB` to `16 GB`. If the specified size would exceed 1/8 the size of `shared_buffers`, the size is silently capped to that value. The default value is `2MB`. If this value is specified without units, it is taken as kilobytes. This parameter can be set at any time. It can be overridden for [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM") and [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE") when passing the `BUFFER_USAGE_LIMIT` option. Higher settings can allow `VACUUM` and `ANALYZE` to run more quickly, but having too large a setting may cause too many other useful pages to be evicted from shared buffers.

`logical_decoding_work_mem` (`integer`) [#](#GUC-LOGICAL-DECODING-WORK-MEM)

Specifies the maximum amount of memory to be used by logical decoding, before some of the decoded changes are written to local disk. This limits the amount of memory used by logical streaming replication connections. It defaults to 64 megabytes (`64MB`). Since each replication connection only uses a single buffer of this size, and an installation normally doesn't have many such connections concurrently (as limited by `max_wal_senders`), it's safe to set this value significantly higher than `work_mem`, reducing the amount of decoded changes written to disk.

`commit_timestamp_buffers` (`integer`) [#](#GUC-COMMIT-TIMESTAMP-BUFFERS)

Specifies the amount of memory to use to cache the contents of `pg_commit_ts` (see [Table 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html#PGDATA-CONTENTS-TABLE "Table 66.1. Contents of PGDATA")). If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default value is `0`, which requests `shared_buffers`/512 up to 1024 blocks, but not fewer than 16 blocks. This parameter can only be set at server start.

`multixact_member_buffers` (`integer`) [#](#GUC-MULTIXACT-MEMBER-BUFFERS)

Specifies the amount of shared memory to use to cache the contents of `pg_multixact/members` (see [Table 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html#PGDATA-CONTENTS-TABLE "Table 66.1. Contents of PGDATA")). If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default value is `32`. This parameter can only be set at server start.

`multixact_offset_buffers` (`integer`) [#](#GUC-MULTIXACT-OFFSET-BUFFERS)

Specifies the amount of shared memory to use to cache the contents of `pg_multixact/offsets` (see [Table 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html#PGDATA-CONTENTS-TABLE "Table 66.1. Contents of PGDATA")). If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default value is `16`. This parameter can only be set at server start.

`notify_buffers` (`integer`) [#](#GUC-NOTIFY-BUFFERS)

Specifies the amount of shared memory to use to cache the contents of `pg_notify` (see [Table 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html#PGDATA-CONTENTS-TABLE "Table 66.1. Contents of PGDATA")). If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default value is `16`. This parameter can only be set at server start.

`serializable_buffers` (`integer`) [#](#GUC-SERIALIZABLE-BUFFERS)

Specifies the amount of shared memory to use to cache the contents of `pg_serial` (see [Table 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html#PGDATA-CONTENTS-TABLE "Table 66.1. Contents of PGDATA")). If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default value is `32`. This parameter can only be set at server start.

`subtransaction_buffers` (`integer`) [#](#GUC-SUBTRANSACTION-BUFFERS)

Specifies the amount of shared memory to use to cache the contents of `pg_subtrans` (see [Table 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html#PGDATA-CONTENTS-TABLE "Table 66.1. Contents of PGDATA")). If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default value is `0`, which requests `shared_buffers`/512 up to 1024 blocks, but not fewer than 16 blocks. This parameter can only be set at server start.

`transaction_buffers` (`integer`) [#](#GUC-TRANSACTION-BUFFERS)

Specifies the amount of shared memory to use to cache the contents of `pg_xact` (see [Table 66.1](https://www.postgresql.org/docs/current/storage-file-layout.html#PGDATA-CONTENTS-TABLE "Table 66.1. Contents of PGDATA")). If this value is specified without units, it is taken as blocks, that is `BLCKSZ` bytes, typically 8kB. The default value is `0`, which requests `shared_buffers`/512 up to 1024 blocks, but not fewer than 16 blocks. This parameter can only be set at server start.

`max_stack_depth` (`integer`) [#](#GUC-MAX-STACK-DEPTH)

Specifies the maximum safe depth of the server's execution stack. The ideal setting for this parameter is the actual stack size limit enforced by the kernel (as set by `ulimit -s` or local equivalent), less a safety margin of a megabyte or so. The safety margin is needed because the stack depth is not checked in every routine in the server, but only in key potentially-recursive routines. If this value is specified without units, it is taken as kilobytes. The default setting is two megabytes (`2MB`), which is conservatively small and unlikely to risk crashes. However, it might be too small to allow execution of complex functions. Only superusers and users with the appropriate `SET` privilege can change this setting.

Setting `max_stack_depth` higher than the actual kernel limit will mean that a runaway recursive function can crash an individual backend process. On platforms where PostgreSQL can determine the kernel limit, the server will not allow this variable to be set to an unsafe value. However, not all platforms provide the information, so caution is recommended in selecting a value.

`shared_memory_type` (`enum`) [#](#GUC-SHARED-MEMORY-TYPE)

Specifies the shared memory implementation that the server should use for the main shared memory region that holds PostgreSQL's shared buffers and other shared data. Possible values are `mmap` (for anonymous shared memory allocated using `mmap`), `sysv` (for System V shared memory allocated via `shmget`) and `windows` (for Windows shared memory). Not all values are supported on all platforms; the first supported option is the default for that platform. The use of the `sysv` option, which is not the default on any platform, is generally discouraged because it typically requires non-default kernel settings to allow for large allocations (see [Section 18.4.1](https://www.postgresql.org/docs/current/kernel-resources.html#SYSVIPC "18.4.1. Shared Memory and Semaphores")). This parameter can only be set at server start.

`dynamic_shared_memory_type` (`enum`) [#](#GUC-DYNAMIC-SHARED-MEMORY-TYPE)

Specifies the dynamic shared memory implementation that the server should use. Possible values are `posix` (for POSIX shared memory allocated using `shm_open`), `sysv` (for System V shared memory allocated via `shmget`), `windows` (for Windows shared memory), and `mmap` (to simulate shared memory using memory-mapped files stored in the data directory). Not all values are supported on all platforms; the first supported option is usually the default for that platform. The use of the `mmap` option, which is not the default on any platform, is generally discouraged because the operating system may write modified pages back to disk repeatedly, increasing system I/O load; however, it may be useful for debugging, when the `pg_dynshmem` directory is stored on a RAM disk, or when other shared memory facilities are not available. This parameter can only be set at server start.

`min_dynamic_shared_memory` (`integer`) [#](#GUC-MIN-DYNAMIC-SHARED-MEMORY)

Specifies the amount of memory that should be allocated at server startup for use by parallel queries. When this memory region is insufficient or exhausted by concurrent queries, new parallel queries try to allocate extra shared memory temporarily from the operating system using the method configured with `dynamic_shared_memory_type`, which may be slower due to memory management overheads. Memory that is allocated at startup with `min_dynamic_shared_memory` is affected by the `huge_pages` setting on operating systems where that is supported, and may be more likely to benefit from larger pages on operating systems where that is managed automatically. The default value is `0` (none). This parameter can only be set at server start.
