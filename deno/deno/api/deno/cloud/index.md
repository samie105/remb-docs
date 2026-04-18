---
title: "Cloud - Deno documentation"
source: "https://docs.deno.com/api/deno/cloud"
canonical_url: "https://docs.deno.com/api/deno/cloud"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:38.841Z"
content_hash: "451c9c31bcbd761baaa3fdb81cbcfa66b0ea23ff77efcd2352256c261869ecfc"
menu_path: ["Cloud - Deno documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/deno/all_symbols/index.md", "title": "All Symbols - Deno documentation"}
nav_next: {"path": "deno/deno/api/deno/errors/index.md", "title": "Errors - Deno documentation"}
---

### Classes [#](#Classes)

c

[Deno.AtomicOperation](./././~/Deno.AtomicOperation "Deno.AtomicOperation")

An operation on a [`Deno.Kv`](./././~/Deno.Kv) that can be performed atomically. Atomic operations do not auto-commit, and must be committed explicitly by calling the `commit` method.

*   [check](./././~/Deno.AtomicOperation#method_check_0)
*   [commit](./././~/Deno.AtomicOperation#method_commit_0)
*   [delete](./././~/Deno.AtomicOperation#method_delete_0)
*   [enqueue](./././~/Deno.AtomicOperation#method_enqueue_0)
*   [max](./././~/Deno.AtomicOperation#method_max_0)
*   [min](./././~/Deno.AtomicOperation#method_min_0)
*   [mutate](./././~/Deno.AtomicOperation#method_mutate_0)
*   [set](./././~/Deno.AtomicOperation#method_set_0)
*   [sum](./././~/Deno.AtomicOperation#method_sum_0)

c

[Deno.Kv](./././~/Deno.Kv "Deno.Kv")

A key-value database that can be used to store and retrieve data.

*   [atomic](./././~/Deno.Kv#method_atomic_0)
*   [close](./././~/Deno.Kv#method_close_0)
*   [commitVersionstamp](./././~/Deno.Kv#method_commitversionstamp_0)
*   [delete](./././~/Deno.Kv#method_delete_0)
*   [enqueue](./././~/Deno.Kv#method_enqueue_0)
*   [get](./././~/Deno.Kv#method_get_0)
*   [getMany](./././~/Deno.Kv#method_getmany_0)
*   [list](./././~/Deno.Kv#method_list_0)
*   [listenQueue](./././~/Deno.Kv#method_listenqueue_0)
*   [set](./././~/Deno.Kv#method_set_0)
*   [watch](./././~/Deno.Kv#method_watch_0)

c

[Deno.KvListIterator](./././~/Deno.KvListIterator "Deno.KvListIterator")

An iterator over a range of data entries in a [`Deno.Kv`](./././~/Deno.Kv).

*   [cursor](./././~/Deno.KvListIterator#accessor_cursor)
*   [next](./././~/Deno.KvListIterator#method_next_0)

c

[Deno.KvU64](./././~/Deno.KvU64 "Deno.KvU64")

Wrapper type for 64-bit unsigned integers for use as values in a [`Deno.Kv`](./././~/Deno.Kv).

*   [value](./././~/Deno.KvU64#property_value)

### Functions [#](#Functions)

f

[Deno.cron](./././~/Deno.cron "Deno.cron")

Create a cron job that will periodically execute the provided handler callback based on the specified schedule.

f

[Deno.openKv](./././~/Deno.openKv "Deno.openKv")

Open a new [`Deno.Kv`](./././~/Deno.Kv) connection to persist data.

### Interfaces [#](#Interfaces)

I

[Deno.AtomicCheck](./././~/Deno.AtomicCheck "Deno.AtomicCheck")

A check to perform as part of a [`Deno.AtomicOperation`](./././~/Deno.AtomicOperation). The check will fail if the versionstamp for the key-value pair in the KV store does not match the given versionstamp. A check with a `null` versionstamp checks that the key-value pair does not currently exist in the KV store.

*   [key](./././~/Deno.AtomicCheck#property_key)
*   [versionstamp](./././~/Deno.AtomicCheck#property_versionstamp)

I

[Deno.CronSchedule](./././~/Deno.CronSchedule "Deno.CronSchedule")

CronSchedule is the interface used for JSON format cron `schedule`.

*   [dayOfMonth](./././~/Deno.CronSchedule#property_dayofmonth)
*   [dayOfWeek](./././~/Deno.CronSchedule#property_dayofweek)
*   [hour](./././~/Deno.CronSchedule#property_hour)
*   [minute](./././~/Deno.CronSchedule#property_minute)
*   [month](./././~/Deno.CronSchedule#property_month)

I

[Deno.KvCommitError](./././~/Deno.KvCommitError "Deno.KvCommitError")

No documentation available

*   [ok](./././~/Deno.KvCommitError#property_ok)

I

[Deno.KvCommitResult](./././~/Deno.KvCommitResult "Deno.KvCommitResult")

No documentation available

*   [ok](./././~/Deno.KvCommitResult#property_ok)
*   [versionstamp](./././~/Deno.KvCommitResult#property_versionstamp)

I

[Deno.KvEntry](./././~/Deno.KvEntry "Deno.KvEntry")

A versioned pair of key and value in a [`Deno.Kv`](./././~/Deno.Kv).

*   [key](./././~/Deno.KvEntry#property_key)
*   [value](./././~/Deno.KvEntry#property_value)
*   [versionstamp](./././~/Deno.KvEntry#property_versionstamp)

I

[Deno.KvListOptions](./././~/Deno.KvListOptions "Deno.KvListOptions")

Options for listing key-value pairs in a [`Deno.Kv`](./././~/Deno.Kv).

*   [batchSize](./././~/Deno.KvListOptions#property_batchsize)
*   [consistency](./././~/Deno.KvListOptions#property_consistency)
*   [cursor](./././~/Deno.KvListOptions#property_cursor)
*   [limit](./././~/Deno.KvListOptions#property_limit)
*   [reverse](./././~/Deno.KvListOptions#property_reverse)

### Type Aliases [#](<#Type Aliases>)

T

[Deno.CronScheduleExpression](./././~/Deno.CronScheduleExpression "Deno.CronScheduleExpression")

CronScheduleExpression is used as the type of `minute`, `hour`, `dayOfMonth`, `month`, and `dayOfWeek` in `CronSchedule`.

T

[Deno.KvConsistencyLevel](./././~/Deno.KvConsistencyLevel "Deno.KvConsistencyLevel")

Consistency level of a KV operation.

T

[Deno.KvEntryMaybe](./././~/Deno.KvEntryMaybe "Deno.KvEntryMaybe")

An optional versioned pair of key and value in a [`Deno.Kv`](./././~/Deno.Kv).

T

[Deno.KvKey](./././~/Deno.KvKey "Deno.KvKey")

A key to be persisted in a [`Deno.Kv`](./././~/Deno.Kv). A key is a sequence of [`Deno.KvKeyPart`](./././~/Deno.KvKeyPart)s.

T

[Deno.KvKeyPart](./././~/Deno.KvKeyPart "Deno.KvKeyPart")

A single part of a [`Deno.KvKey`](./././~/Deno.KvKey). Parts are ordered lexicographically, first by their type, and within a given type by their value.

T

[Deno.KvListSelector](./././~/Deno.KvListSelector "Deno.KvListSelector")

A selector that selects the range of data returned by a list operation on a [`Deno.Kv`](./././~/Deno.Kv).

T

[Deno.KvMutation](./././~/Deno.KvMutation "Deno.KvMutation")

A mutation to a key in a [`Deno.Kv`](./././~/Deno.Kv). A mutation is a combination of a key, a value, and a type. The type determines how the mutation is applied to the key.
