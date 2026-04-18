---
title: "PostgreSQL: Documentation: 18: 9.28. System Administration Functions"
source: "https://www.postgresql.org/docs/current/functions-admin.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-admin.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:54.903Z"
content_hash: "fb6edf808df4bd9e75c619109bf2bd2ad03964337c71b1f5e177252e414392b7"
menu_path: ["PostgreSQL: Documentation: 18: 9.28. System Administration Functions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-replication-slots.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.20.\u00a0pg_replication_slots"}
nav_next: {"path": "postgres/docs/current/infoschema-element-types.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.24.\u00a0element_types"}
---

Function

Description

`pg_create_physical_replication_slot` ( _`slot_name`_ `name` \[, _`immediately_reserve`_ `boolean`, _`temporary`_ `boolean` \] ) → `record` ( _`slot_name`_ `name`, _`lsn`_ `pg_lsn` )

Creates a new physical replication slot named _`slot_name`_. The optional second parameter, when `true`, specifies that the LSN for this replication slot be reserved immediately; otherwise the LSN is reserved on first connection from a streaming replication client. Streaming changes from a physical slot is only possible with the streaming-replication protocol — see [Section 54.4](https://www.postgresql.org/docs/current/protocol-replication.html "54.4. Streaming Replication Protocol"). The optional third parameter, _`temporary`_, when set to true, specifies that the slot should not be permanently stored to disk and is only meant for use by the current session. Temporary slots are also released upon any error. This function corresponds to the replication protocol command `CREATE_REPLICATION_SLOT ... PHYSICAL`.

`pg_drop_replication_slot` ( _`slot_name`_ `name` ) → `void`

Drops the physical or logical replication slot named _`slot_name`_. Same as replication protocol command `DROP_REPLICATION_SLOT`.

`pg_create_logical_replication_slot` ( _`slot_name`_ `name`, _`plugin`_ `name` \[, _`temporary`_ `boolean`, _`twophase`_ `boolean`, _`failover`_ `boolean` \] ) → `record` ( _`slot_name`_ `name`, _`lsn`_ `pg_lsn` )

Creates a new logical (decoding) replication slot named _`slot_name`_ using the output plugin _`plugin`_. The optional third parameter, _`temporary`_, when set to true, specifies that the slot should not be permanently stored to disk and is only meant for use by the current session. Temporary slots are also released upon any error. The optional fourth parameter, _`twophase`_, when set to true, specifies that the decoding of prepared transactions is enabled for this slot. The optional fifth parameter, _`failover`_, when set to true, specifies that this slot is enabled to be synced to the standbys so that logical replication can be resumed after failover. A call to this function has the same effect as the replication protocol command `CREATE_REPLICATION_SLOT ... LOGICAL`.

`pg_copy_physical_replication_slot` ( _`src_slot_name`_ `name`, _`dst_slot_name`_ `name` \[, _`temporary`_ `boolean` \] ) → `record` ( _`slot_name`_ `name`, _`lsn`_ `pg_lsn` )

Copies an existing physical replication slot named _`src_slot_name`_ to a physical replication slot named _`dst_slot_name`_. The copied physical slot starts to reserve WAL from the same LSN as the source slot. _`temporary`_ is optional. If _`temporary`_ is omitted, the same value as the source slot is used. Copy of an invalidated slot is not allowed.

`pg_copy_logical_replication_slot` ( _`src_slot_name`_ `name`, _`dst_slot_name`_ `name` \[, _`temporary`_ `boolean` \[, _`plugin`_ `name` \]\] ) → `record` ( _`slot_name`_ `name`, _`lsn`_ `pg_lsn` )

Copies an existing logical replication slot named _`src_slot_name`_ to a logical replication slot named _`dst_slot_name`_, optionally changing the output plugin and persistence. The copied logical slot starts from the same LSN as the source logical slot. Both _`temporary`_ and _`plugin`_ are optional; if they are omitted, the values of the source slot are used. The `failover` option of the source logical slot is not copied and is set to `false` by default. This is to avoid the risk of being unable to continue logical replication after failover to standby where the slot is being synchronized. Copy of an invalidated slot is not allowed.

`pg_logical_slot_get_changes` ( _`slot_name`_ `name`, _`upto_lsn`_ `pg_lsn`, _`upto_nchanges`_ `integer`, `VARIADIC` _`options`_ `text[]` ) → `setof record` ( _`lsn`_ `pg_lsn`, _`xid`_ `xid`, _`data`_ `text` )

Returns changes in the slot _`slot_name`_, starting from the point from which changes have been consumed last. If _`upto_lsn`_ and _`upto_nchanges`_ are NULL, logical decoding will continue until end of WAL. If _`upto_lsn`_ is non-NULL, decoding will include only those transactions which commit prior to the specified LSN. If _`upto_nchanges`_ is non-NULL, decoding will stop when the number of rows produced by decoding exceeds the specified value. Note, however, that the actual number of rows returned may be larger, since this limit is only checked after adding the rows produced when decoding each new transaction commit. If the specified slot is a logical failover slot then the function will not return until all physical slots specified in [`synchronized_standby_slots`](postgres/docs/current/runtime-config-replication.html/index.md#GUC-SYNCHRONIZED-STANDBY-SLOTS) have confirmed WAL receipt.

`pg_logical_slot_peek_changes` ( _`slot_name`_ `name`, _`upto_lsn`_ `pg_lsn`, _`upto_nchanges`_ `integer`, `VARIADIC` _`options`_ `text[]` ) → `setof record` ( _`lsn`_ `pg_lsn`, _`xid`_ `xid`, _`data`_ `text` )

Behaves just like the `pg_logical_slot_get_changes()` function, except that changes are not consumed; that is, they will be returned again on future calls.

`pg_logical_slot_get_binary_changes` ( _`slot_name`_ `name`, _`upto_lsn`_ `pg_lsn`, _`upto_nchanges`_ `integer`, `VARIADIC` _`options`_ `text[]` ) → `setof record` ( _`lsn`_ `pg_lsn`, _`xid`_ `xid`, _`data`_ `bytea` )

Behaves just like the `pg_logical_slot_get_changes()` function, except that changes are returned as `bytea`.

`pg_logical_slot_peek_binary_changes` ( _`slot_name`_ `name`, _`upto_lsn`_ `pg_lsn`, _`upto_nchanges`_ `integer`, `VARIADIC` _`options`_ `text[]` ) → `setof record` ( _`lsn`_ `pg_lsn`, _`xid`_ `xid`, _`data`_ `bytea` )

Behaves just like the `pg_logical_slot_peek_changes()` function, except that changes are returned as `bytea`.

`pg_replication_slot_advance` ( _`slot_name`_ `name`, _`upto_lsn`_ `pg_lsn` ) → `record` ( _`slot_name`_ `name`, _`end_lsn`_ `pg_lsn` )

Advances the current confirmed position of a replication slot named _`slot_name`_. The slot will not be moved backwards, and it will not be moved beyond the current insert location. Returns the name of the slot and the actual position that it was advanced to. The updated slot position information is written out at the next checkpoint if any advancing is done. So in the event of a crash, the slot may return to an earlier position. If the specified slot is a logical failover slot then the function will not return until all physical slots specified in [`synchronized_standby_slots`](postgres/docs/current/runtime-config-replication.html/index.md#GUC-SYNCHRONIZED-STANDBY-SLOTS) have confirmed WAL receipt.

`pg_replication_origin_create` ( _`node_name`_ `text` ) → `oid`

Creates a replication origin with the given external name, and returns the internal ID assigned to it. The name must be no longer than 512 bytes.

`pg_replication_origin_drop` ( _`node_name`_ `text` ) → `void`

Deletes a previously-created replication origin, including any associated replay progress.

`pg_replication_origin_oid` ( _`node_name`_ `text` ) → `oid`

Looks up a replication origin by name and returns the internal ID. If no such replication origin is found, `NULL` is returned.

`pg_replication_origin_session_setup` ( _`node_name`_ `text` ) → `void`

Marks the current session as replaying from the given origin, allowing replay progress to be tracked. Can only be used if no origin is currently selected. Use `pg_replication_origin_session_reset` to undo.

`pg_replication_origin_session_reset` () → `void`

Cancels the effects of `pg_replication_origin_session_setup()`.

`pg_replication_origin_session_is_setup` () → `boolean`

Returns true if a replication origin has been selected in the current session.

`pg_replication_origin_session_progress` ( _`flush`_ `boolean` ) → `pg_lsn`

Returns the replay location for the replication origin selected in the current session. The parameter _`flush`_ determines whether the corresponding local transaction will be guaranteed to have been flushed to disk or not.

`pg_replication_origin_xact_setup` ( _`origin_lsn`_ `pg_lsn`, _`origin_timestamp`_ `timestamp with time zone` ) → `void`

Marks the current transaction as replaying a transaction that has committed at the given LSN and timestamp. Can only be called when a replication origin has been selected using `pg_replication_origin_session_setup`.

`pg_replication_origin_xact_reset` () → `void`

Cancels the effects of `pg_replication_origin_xact_setup()`.

`pg_replication_origin_advance` ( _`node_name`_ `text`, _`lsn`_ `pg_lsn` ) → `void`

Sets replication progress for the given node to the given location. This is primarily useful for setting up the initial location, or setting a new location after configuration changes and similar. Be aware that careless use of this function can lead to inconsistently replicated data.

`pg_replication_origin_progress` ( _`node_name`_ `text`, _`flush`_ `boolean` ) → `pg_lsn`

Returns the replay location for the given replication origin. The parameter _`flush`_ determines whether the corresponding local transaction will be guaranteed to have been flushed to disk or not.

`pg_logical_emit_message` ( _`transactional`_ `boolean`, _`prefix`_ `text`, _`content`_ `text` \[, _`flush`_ `boolean` `DEFAULT` `false`\] ) → `pg_lsn`

`pg_logical_emit_message` ( _`transactional`_ `boolean`, _`prefix`_ `text`, _`content`_ `bytea` \[, _`flush`_ `boolean` `DEFAULT` `false`\] ) → `pg_lsn`

Emits a logical decoding message. This can be used to pass generic messages to logical decoding plugins through WAL. The _`transactional`_ parameter specifies if the message should be part of the current transaction, or if it should be written immediately and decoded as soon as the logical decoder reads the record. The _`prefix`_ parameter is a textual prefix that can be used by logical decoding plugins to easily recognize messages that are interesting for them. The _`content`_ parameter is the content of the message, given either in text or binary form. The _`flush`_ parameter (default set to `false`) controls if the message is immediately flushed to WAL or not. _`flush`_ has no effect with _`transactional`_, as the message's WAL record is flushed along with its transaction.

`pg_sync_replication_slots` () → `void`

Synchronize the logical failover replication slots from the primary server to the standby server. This function can only be executed on the standby server. Temporary synced slots, if any, cannot be used for logical decoding and must be dropped after promotion. See [Section 47.2.3](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html#LOGICALDECODING-REPLICATION-SLOTS-SYNCHRONIZATION "47.2.3. Replication Slot Synchronization") for details. Note that this function is primarily intended for testing and debugging purposes and should be used with caution. Additionally, this function cannot be executed if [`sync_replication_slots`](postgres/docs/current/runtime-config-replication.html/index.md#GUC-SYNC-REPLICATION-SLOTS) is enabled and the slotsync worker is already running to perform the synchronization of slots.

### Caution

If, after executing the function, [`hot_standby_feedback`](postgres/docs/current/runtime-config-replication.html/index.md#GUC-HOT-STANDBY-FEEDBACK) is disabled on the standby or the physical slot configured in [`primary_slot_name`](postgres/docs/current/runtime-config-replication.html/index.md#GUC-PRIMARY-SLOT-NAME) is removed, then it is possible that the necessary rows of the synchronized slot will be removed by the VACUUM process on the primary server, resulting in the synchronized slot becoming invalidated.


