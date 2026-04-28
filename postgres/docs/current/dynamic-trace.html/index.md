---
title: "PostgreSQL: Documentation: 18: 27.5. Dynamic Tracing"
source: "https://www.postgresql.org/docs/current/dynamic-trace.html"
canonical_url: "https://www.postgresql.org/docs/current/dynamic-trace.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:19.566Z"
content_hash: "b597a25a7d2db0ab866fa01c01010bcdeb7f1dbccd410b63689dc7e3e571c073"
menu_path: ["PostgreSQL: Documentation: 18: 27.5. Dynamic Tracing"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/domains.html/index.md", "title": "PostgreSQL: Documentation: 18: 8.18.\u00a0Domain Types"}
nav_next: {"path": "postgres/docs/current/earthdistance.html/index.md", "title": "PostgreSQL: Documentation: 18: F.14.\u00a0earthdistance \u2014 calculate great-circle distances"}
---

| Name | Parameters | Description |
| --- | --- | --- |
| `transaction-start` | `(LocalTransactionId)` | Probe that fires at the start of a new transaction. arg0 is the transaction ID. |
| `transaction-commit` | `(LocalTransactionId)` | Probe that fires when a transaction completes successfully. arg0 is the transaction ID. |
| `transaction-abort` | `(LocalTransactionId)` | Probe that fires when a transaction completes unsuccessfully. arg0 is the transaction ID. |
| `query-start` | `(const char *)` | Probe that fires when the processing of a query is started. arg0 is the query string. |
| `query-done` | `(const char *)` | Probe that fires when the processing of a query is complete. arg0 is the query string. |
| `query-parse-start` | `(const char *)` | Probe that fires when the parsing of a query is started. arg0 is the query string. |
| `query-parse-done` | `(const char *)` | Probe that fires when the parsing of a query is complete. arg0 is the query string. |
| `query-rewrite-start` | `(const char *)` | Probe that fires when the rewriting of a query is started. arg0 is the query string. |
| `query-rewrite-done` | `(const char *)` | Probe that fires when the rewriting of a query is complete. arg0 is the query string. |
| `query-plan-start` | `()` | Probe that fires when the planning of a query is started. |
| `query-plan-done` | `()` | Probe that fires when the planning of a query is complete. |
| `query-execute-start` | `()` | Probe that fires when the execution of a query is started. |
| `query-execute-done` | `()` | Probe that fires when the execution of a query is complete. |
| `statement-status` | `(const char *)` | Probe that fires anytime the server process updates its `pg_stat_activity`.`status`. arg0 is the new status string. |
| `checkpoint-start` | `(int)` | Probe that fires when a checkpoint is started. arg0 holds the bitwise flags used to distinguish different checkpoint types, such as shutdown, immediate or force. |
| `checkpoint-done` | `(int, int, int, int, int)` | Probe that fires when a checkpoint is complete. (The probes listed next fire in sequence during checkpoint processing.) arg0 is the number of buffers written. arg1 is the total number of buffers. arg2, arg3 and arg4 contain the number of WAL files added, removed and recycled respectively. |
| `clog-checkpoint-start` | `(bool)` | Probe that fires when the CLOG portion of a checkpoint is started. arg0 is true for normal checkpoint, false for shutdown checkpoint. |
| `clog-checkpoint-done` | `(bool)` | Probe that fires when the CLOG portion of a checkpoint is complete. arg0 has the same meaning as for `clog-checkpoint-start`. |
| `subtrans-checkpoint-start` | `(bool)` | Probe that fires when the SUBTRANS portion of a checkpoint is started. arg0 is true for normal checkpoint, false for shutdown checkpoint. |
| `subtrans-checkpoint-done` | `(bool)` | Probe that fires when the SUBTRANS portion of a checkpoint is complete. arg0 has the same meaning as for `subtrans-checkpoint-start`. |
| `multixact-checkpoint-start` | `(bool)` | Probe that fires when the MultiXact portion of a checkpoint is started. arg0 is true for normal checkpoint, false for shutdown checkpoint. |
| `multixact-checkpoint-done` | `(bool)` | Probe that fires when the MultiXact portion of a checkpoint is complete. arg0 has the same meaning as for `multixact-checkpoint-start`. |
| `buffer-checkpoint-start` | `(int)` | Probe that fires when the buffer-writing portion of a checkpoint is started. arg0 holds the bitwise flags used to distinguish different checkpoint types, such as shutdown, immediate or force. |
| `buffer-sync-start` | `(int, int)` | Probe that fires when we begin to write dirty buffers during checkpoint (after identifying which buffers must be written). arg0 is the total number of buffers. arg1 is the number that are currently dirty and need to be written. |
| `buffer-sync-written` | `(int)` | Probe that fires after each buffer is written during checkpoint. arg0 is the ID number of the buffer. |
| `buffer-sync-done` | `(int, int, int)` | Probe that fires when all dirty buffers have been written. arg0 is the total number of buffers. arg1 is the number of buffers actually written by the checkpoint process. arg2 is the number that were expected to be written (arg1 of `buffer-sync-start`); any difference reflects other processes flushing buffers during the checkpoint. |
| `buffer-checkpoint-sync-start` | `()` | Probe that fires after dirty buffers have been written to the kernel, and before starting to issue fsync requests. |
| `buffer-checkpoint-done` | `()` | Probe that fires when syncing of buffers to disk is complete. |
| `twophase-checkpoint-start` | `()` | Probe that fires when the two-phase portion of a checkpoint is started. |
| `twophase-checkpoint-done` | `()` | Probe that fires when the two-phase portion of a checkpoint is complete. |
| `buffer-extend-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, unsigned int)` | Probe that fires when a relation extension starts. arg0 contains the fork to be extended. arg1, arg2, and arg3 contain the tablespace, database, and relation OIDs identifying the relation. arg4 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg5 is the number of blocks the caller would like to extend by. |
| `buffer-extend-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, unsigned int, BlockNumber)` | Probe that fires when a relation extension is complete. arg0 contains the fork to be extended. arg1, arg2, and arg3 contain the tablespace, database, and relation OIDs identifying the relation. arg4 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg5 is the number of blocks the relation was extended by, this can be less than the number in the `buffer-extend-start` due to resource constraints. arg6 contains the BlockNumber of the first new block. |
| `buffer-read-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int)` | Probe that fires when a buffer read is started. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. |
| `buffer-read-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, bool)` | Probe that fires when a buffer read is complete. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg6 is true if the buffer was found in the pool, false if not. |
| `buffer-flush-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid)` | Probe that fires before issuing any write request for a shared buffer. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. |
| `buffer-flush-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid)` | Probe that fires when a write request is complete. (Note that this just reflects the time to pass the data to the kernel; it's typically not actually been written to disk yet.) The arguments are the same as for `buffer-flush-start`. |
| `wal-buffer-write-dirty-start` | `()` | Probe that fires when a server process begins to write a dirty WAL buffer because no more WAL buffer space is available. (If this happens often, it implies that [wal\_buffers](postgres/docs/current/runtime-config-wal.html/index.md#GUC-WAL-BUFFERS) is too small.) |
| `wal-buffer-write-dirty-done` | `()` | Probe that fires when a dirty WAL buffer write is complete. |
| `wal-insert` | `(unsigned char, unsigned char)` | Probe that fires when a WAL record is inserted. arg0 is the resource manager (rmid) for the record. arg1 contains the info flags. |
| `wal-switch` | `()` | Probe that fires when a WAL segment switch is requested. |
| `smgr-md-read-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int)` | Probe that fires when beginning to read a block from a relation. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. |
| `smgr-md-read-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, int, int)` | Probe that fires when a block read is complete. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg6 is the number of bytes actually read, while arg7 is the number requested (if these are different it indicates a short read). |
| `smgr-md-write-start` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int)` | Probe that fires when beginning to write a block to a relation. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. |
| `smgr-md-write-done` | `(ForkNumber, BlockNumber, Oid, Oid, Oid, int, int, int)` | Probe that fires when a block write is complete. arg0 and arg1 contain the fork and block numbers of the page. arg2, arg3, and arg4 contain the tablespace, database, and relation OIDs identifying the relation. arg5 is the ID of the backend which created the temporary relation for a local buffer, or `INVALID_PROC_NUMBER` (-1) for a shared buffer. arg6 is the number of bytes actually written, while arg7 is the number requested (if these are different it indicates a short write). |
| `sort-start` | `(int, bool, int, int, bool, int)` | Probe that fires when a sort operation is started. arg0 indicates heap, index or datum sort. arg1 is true for unique-value enforcement. arg2 is the number of key columns. arg3 is the number of kilobytes of work memory allowed. arg4 is true if random access to the sort result is required. arg5 indicates serial when `0`, parallel worker when `1`, or parallel leader when `2`. |
| `sort-done` | `(bool, long)` | Probe that fires when a sort is complete. arg0 is true for external sort, false for internal sort. arg1 is the number of disk blocks used for an external sort, or kilobytes of memory used for an internal sort. |
| `lwlock-acquire` | `(char *, LWLockMode)` | Probe that fires when an LWLock has been acquired. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-release` | `(char *)` | Probe that fires when an LWLock has been released (but note that any released waiters have not yet been awakened). arg0 is the LWLock's tranche. |
| `lwlock-wait-start` | `(char *, LWLockMode)` | Probe that fires when an LWLock was not immediately available and a server process has begun to wait for the lock to become available. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-wait-done` | `(char *, LWLockMode)` | Probe that fires when a server process has been released from its wait for an LWLock (it does not actually have the lock yet). arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-condacquire` | `(char *, LWLockMode)` | Probe that fires when an LWLock was successfully acquired when the caller specified no waiting. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lwlock-condacquire-fail` | `(char *, LWLockMode)` | Probe that fires when an LWLock was not successfully acquired when the caller specified no waiting. arg0 is the LWLock's tranche. arg1 is the requested lock mode, either exclusive or shared. |
| `lock-wait-start` | `(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, LOCKMODE)` | Probe that fires when a request for a heavyweight lock (lmgr lock) has begun to wait because the lock is not available. arg0 through arg3 are the tag fields identifying the object being locked. arg4 indicates the type of object being locked. arg5 indicates the lock type being requested. |
| `lock-wait-done` | `(unsigned int, unsigned int, unsigned int, unsigned int, unsigned int, LOCKMODE)` | Probe that fires when a request for a heavyweight lock (lmgr lock) has finished waiting (i.e., has acquired the lock). The arguments are the same as for `lock-wait-start`. |
| `deadlock-found` | `()` | Probe that fires when a deadlock is found by the deadlock detector. |
