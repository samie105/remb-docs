---
title: "PostgreSQL: Documentation: 18: 53.2. pg_aios"
source: "https://www.postgresql.org/docs/current/view-pg-aios.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-aios.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:58.052Z"
content_hash: "cf8b2679d92a2795da7b9e45f9abee3b1e62c1646ba8ce0ed000ed1f493ccb65"
menu_path: ["PostgreSQL: Documentation: 18: 53.2. pg_aios"]
section_path: []
nav_prev: {"path": "postgres/docs/current/vacuumlo.html/index.md", "title": "PostgreSQL: Documentation: 18: vacuumlo"}
nav_next: {"path": "postgres/docs/current/view-pg-available-extension-versions.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.4.\u00a0pg_available_extension_versions"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-aios.html "PostgreSQL devel - 53.2. pg_aios")

The `pg_aios` view lists all [Asynchronous I/O](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-AIO "Asynchronous I/O") handles that are currently in-use. An I/O handle is used to reference an I/O operation that is being prepared, executed or is in the process of completing. `pg_aios` contains one row for each I/O handle.

This view is mainly useful for developers of PostgreSQL, but may also be useful when tuning PostgreSQL.

**Table 53.2. `pg_aios` Columns**

Column Type

Description

`pid` `int4`

Process ID of the server process that is issuing this I/O.

`io_id` `int4`

Identifier of the I/O handle. Handles are reused once the I/O completed (or if the handle is released before I/O is started). On reuse [`pg_aios`.`io_generation`](postgres/docs/current/view-pg-aios.html/index.md#VIEW-PG-AIOS-IO-GENERATION) is incremented.

`io_generation` `int8`

Generation of the I/O handle.

`state` `text`

State of the I/O handle:

*   `HANDED_OUT`, referenced by code but not yet used
    
*   `DEFINED`, information necessary for execution is known
    
*   `STAGED`, ready for execution
    
*   `SUBMITTED`, submitted for execution
    
*   `COMPLETED_IO`, finished, but result has not yet been processed
    
*   `COMPLETED_SHARED`, shared completion processing completed
    
*   `COMPLETED_LOCAL`, backend local completion processing completed
    

`operation` `text`

Operation performed using the I/O handle:

*   `invalid`, not yet known
    
*   `readv`, a vectored read
    
*   `writev`, a vectored write
    

`off` `int8`

Offset of the I/O operation.

`length` `int8`

Length of the I/O operation.

`target` `text`

What kind of object is the I/O targeting:

*   `smgr`, I/O on relations
    

`handle_data_len` `int2`

Length of the data associated with the I/O operation. For I/O to/from [shared\_buffers](postgres/docs/current/runtime-config-resource.html/index.md#GUC-SHARED-BUFFERS) and [temp\_buffers](postgres/docs/current/runtime-config-resource.html/index.md#GUC-TEMP-BUFFERS), this indicates the number of buffers the I/O is operating on.

`raw_result` `int4`

Low-level result of the I/O operation, or NULL if the operation has not yet completed.

`result` `text`

High-level result of the I/O operation:

*   `UNKNOWN` means that the result of the operation is not yet known.
    
*   `OK` means the I/O completed successfully.
    
*   `PARTIAL` means that the I/O completed without error, but did not process all data. Commonly callers will need to retry and perform the remainder of the work in a separate I/O.
    
*   `WARNING` means that the I/O completed without error, but that execution of the IO triggered a warning. E.g. when encountering a corrupted buffer with [zero\_damaged\_pages](https://www.postgresql.org/docs/current/runtime-config-developer.html#GUC-ZERO-DAMAGED-PAGES) enabled.
    
*   `ERROR` means the I/O failed with an error.
    

`target_desc` `text`

Description of what the I/O operation is targeting.

`f_sync` `bool`

Flag indicating whether the I/O is executed synchronously.

`f_localmem` `bool`

Flag indicating whether the I/O references process local memory.

`f_buffered` `bool`

Flag indicating whether the I/O is buffered I/O.

The `pg_aios` view is read-only.

By default, the `pg_aios` view can be read only by superusers or roles with privileges of the `pg_read_all_stats` role.
