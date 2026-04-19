---
title: "Configuration parameters"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/administration/configuration/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/administration/configuration/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:35.741Z"
content_hash: "75f2805a557cec6223dd0a911f2b5266022b8afb0855e28c7822aed83fae0f95"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Administration","→","Administration","→\n      \n        Configuration parameters","→","Configuration parameters"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Administration","→","Administration","→\n      \n        Configuration parameters","→","Configuration parameters"]
nav_prev: {"path": "redis/docs/latest/develop/ai/search-and-query/administration/index.md", "title": "Administration"}
nav_next: {"path": "redis/docs/latest/develop/ai/search-and-query/administration/design/index.md", "title": "Internal design"}
---

# Configuration parameters

Redis Search can be tuned through multiple configuration parameters. Some of these parameters can only be set at load-time, while other parameters can be set either at load-time or at run-time.

Note:

As of Redis 8 in Redis Open Source (Redis 8), configuration parameters for Redis Search are now set in the following ways:

*   At load time via your `redis.conf` file.
*   At run time (where applicable) using the [`CONFIG SET`](/docs/latest/commands/config-set/) command.

Also, Redis 8 persists Redis Search configuration parameters just like any other configuration parameters (e.g., using the [`CONFIG REWRITE`](/docs/latest/commands/config-rewrite/) command).

## Redis Search configuration parameters

The following table summarizes which configuration parameters can be set at run-time, and compatibility with Redis Software and Redis Cloud.

Parameter name  
(version < 8.0)

Parameter name  
(version ≥ 8.0)

Run-time

Redis  
Software

Redis  
Cloud

BG\_INDEX\_SLEEP\_GAP

[search-bg-index-sleep-gap](#search-bg-index-sleep-gap)

⬜

✅ Supported  
  

❌ Flexible & Annual  
❌ Free & Fixed

BG\_INDEX\_SLEEP\_DURATION\_US

[search-bg-index-sleep-duration-us](#search-bg-index-sleep-duration-us)

⬜

CONCURRENT\_WRITE\_MODE

[search-concurrent-write-mode](#search-concurrent-write-mode)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

CONN\_PER\_SHARD

[search-conn-per-shard](#search-conn-per-shard)

✅

CURSOR\_MAX\_IDLE

[search-cursor-max-idle](#search-cursor-max-idle)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

CURSOR\_READ\_SIZE

[search-cursor-read-size](#search-cursor-read-size)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

CURSOR\_REPLY\_THRESHOLD

[search-cursor-reply-threshold](#search-cursor-reply-threshold)

✅

DEFAULT\_DIALECT

[search-default-dialect](#search-default-dialect)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

EXTLOAD

[search-ext-load](#search-ext-load)

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

FORK\_GC\_CLEAN\_THRESHOLD

[search-fork-gc-clean-threshold](#search-fork-gc-clean-threshold)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

FORK\_GC\_RETRY\_INTERVAL

[search-fork-gc-retry-interval](#search-fork-gc-retry-interval)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

FORK\_GC\_RUN\_INTERVAL

[search-fork-gc-run-interval](#search-fork-gc-run-interval)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

FORKGC\_SLEEP\_BEFORE\_EXIT

[search-fork-gc-sleep-before-exit](#search-fork-gc-sleep-before-exit)

✅

FRISOINI

[search-friso-ini](#search-friso-ini)

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

[GC\_POLICY](#gc_policy)

There is no matching `CONFIG` parameter.

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

GCSCANSIZE

[search-gc-scan-size](#search-gc-scan-size)

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

INDEX\_CURSOR\_LIMIT

[search-index-cursor-limit](#search-index-cursor-limit)

⬜

INDEX\_THREADS

search-index-threads

⬜

MAXAGGREGATERESULTS

[search-max-aggregate-results](#search-max-aggregate-results)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

MAXDOCTABLESIZE

[search-max-doctablesize](#search-max-doctablesize)

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

MAXEXPANSIONS

[search-max-expansions](#search-max-expansions)

✅

MAXPREFIXEXPANSIONS

[search-max-prefix-expansions](#search-max-prefix-expansions)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

MAXSEARCHRESULTS

[search-max-search-results](#search-max-search-results)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

MIN\_OPERATION\_WORKERS

[search-min-operation-workers](#search-min-operation-workers)

✅

MIN\_PHONETIC\_TERM\_LEN

[search-min-phonetic-term-len](#search-min-phonetic-term-len)

✅

MINPREFIX

[search-min-prefix](#search-min-prefix)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

MINSTEMLEN

[search-min-stem-len](#search-min-stem-len)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

MULTI\_TEXT\_SLOP

[search-multi-text-slop](#search-multi-text-slop)

⬜

NO\_MEM\_POOLS

[search-no-mem-pools](#search-no-mem-pools)

⬜

NOGC

[search-no-gc](#search-no-gc)

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

ON\_TIMEOUT

[search-on-timeout](#search-on-timeout)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

PARTIAL\_INDEXED\_DOCS

[search-partial-indexed-docs](#search-partial-indexed-docs)

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

RAW\_DOCID\_ENCODING

[search-raw-docid-encoding](#search-raw-docid-encoding)

⬜

SEARCH\_THREADS

[search-threads](#search-threads)

⬜

SEARCH\_IO\_THREADS

[search-io-threads](#search-io-threads)

⬜

TIERED\_HNSW\_BUFFER\_LIMIT

[search-tiered-hnsw-buffer-limit](#search-tiered-hnsw-buffer-limit)

⬜

TIMEOUT

[search-timeout](#search-timeout)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

TOPOLOGY\_VALIDATION\_TIMEOUT

[search-topology-validation-timeout](#search-topology-validation-timeout)

✅

UNION\_ITERATOR\_HEAP

[search-union-iterator-heap](#search-union-iterator-heap)

✅

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

UPGRADE\_INDEX

[search-upgrade-index](#search-upgrade-index)

⬜

✅ Supported  
  

✅ Flexible & Annual  
❌ Free & Fixed

VSS\_MAX\_RESIZE

[search-vss-max-resize](#search-vss-max-resize)

✅

WORKERS\_PRIORITY\_BIAS\_THRESHOLD

[search-workers-priority-bias-threshold](#search-workers-priority-bias-threshold)

⬜

WORKERS

[search-workers](#search-workers)

✅

OSS\_GLOBAL\_PASSWORD

Deprecated in v8.0.0. Replace with the `masterauth` password.

⬜

✅ Supported  
  

❌ Flexible & Annual  
❌ Free & Fixed

MT\_MODE

Deprecated in v8.0.0. Use search-workers.

⬜

PRIVILEGED\_THREADS\_NUM

Deprecated in v8.0.0. Use search-workers-priority-bias-threshold.

⬜

WORKER\_THREADS

Deprecated in v8.0.0. Use search-min-operation-workers.

⬜

SAFEMODE

Deprecated in v1.6.0. This is now the default setting.

⬜

FORK\_GC\_CLEAN\_NUMERIC\_EMPTY\_NODES

Deprecated in v8.0.0.

⬜

Note:

Parameter names for Redis Open Source versions < 8.0, while deprecated, will still be supported in Redis 8.

* * *

### search-bg-index-sleep-gap

The number of iterations to run while performing background indexing before `usleep(1)` (sleep for 1 microsecond) is called, ensuring that Redis can process other commands.

Type: integer

Valid range: `[1 .. 4294967295]`

Default: `100`

### search-bg-index-sleep-duration-us

Added in v8.2.

The sleep duration (in microseconds) used during background indexing. During background indexing (triggered by `FT.CREATE` on existing keys), Redis periodically sleeps to allow the main thread to process commands. This parameter controls how long each sleep lasts. Works in conjunction with [`search-bg-index-sleep-gap`](#search-bg-index-sleep-gap), which controls how many iterations occur between sleeps.

Type: integer

Valid range: `[1 .. 999999]`

Default: `1`

### search-concurrent-write-mode

If enabled, the tokenization of write queries will be performed concurrently.

Type: boolean

Default: `FALSE`

### search-conn-per-shard

The number of connections to each shard in a cluster. If `0`, the number of connections is set to `search-workers` + 1.

Type: integer

Valid range: `[0 .. 9,223,372,036,854,775,807]`

Default: `0`

### search-cursor-max-idle

The maximum idle time (in ms) that can be set to the [cursor api](/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations/#cursor-api).

Type: integer

Valid range: `[0 .. 9,223,372,036,854,775,807]`

Default: `300000`

### search-cursor-read-size

Type: integer

Default: `1000`

### search-cursor-reply-threshold

The maximum number of replies to accumulate before triggering `_FT.CURSOR READ` on the shards.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `1`

### search-default-dialect

The default [DIALECT](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/) to be used by [`FT.CREATE`](/docs/latest/commands/ft.create/), [`FT.AGGREGATE`](/docs/latest/commands/ft.aggregate/), [`FT.EXPLAIN`](/docs/latest/commands/ft.explain/), [`FT.EXPLAINCLI`](/docs/latest/commands/ft.explaincli/), and [`FT.SPELLCHECK`](/docs/latest/commands/ft.spellcheck/). See [Query dialects](/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects/) for more information.

Default: `1`

### search-ext-load

If present, Redis will try to load an extension dynamic library from the specified file path. See [Extensions](/docs/latest/develop/ai/search-and-query/administration/extensions/) for details.

Type: string

Default: not set

### search-fork-gc-clean-numeric-empty-nodes

Clean empty nodes from numeric tree.

Type: boolean

Default: `TRUE`

### search-fork-gc-clean-threshold

The fork GC will only start to clean when the number of uncleaned documents exceeds this threshold, otherwise it will skip this run.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `100`

### search-fork-gc-retry-interval

Interval (in seconds) in which Redis will retry to run fork GC in case of a failure. This setting can only be combined with the [`search-gc-policy`](#search-gc-policy) `FORK` setting.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `5`

### search-fork-gc-run-interval

Interval (in seconds) between two consecutive fork GC runs. This setting can only be combined with the [`search-gc-policy`](#search-gc-policy) `FORK` setting.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `30`

### search-fork-gc-sleep-before-exit

The number of seconds for the fork GC to sleep before exit. This value should always be set to 0 except when testing.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `0`

### search-friso-ini

If present, load the custom Chinese dictionary from the specified path. See [Using custom dictionaries](/docs/latest/develop/ai/search-and-query/advanced-concepts/chinese/#using-custom-dictionaries) for more details.

Type: string

Default: not set

### GC\_POLICY

The garbage collection policy. The two supported policies are:

*   FORK: uses a forked thread for garbage collection (v1.4.1 and above). This is the default GC policy since v1.6.1 and is ideal for general purpose workloads.
*   LEGACY: uses a synchronous, in-process fork. This is ideal for read-heavy and append-heavy workloads with very few updates/deletes. Deprecated in v2.6.0.

Note: When `GC_POLICY` is set to `FORK`, it can be combined with the `search-fork-gc-run-interval` and `search-fork-gc-retry-interval` settings.

Type: string

Valid values: `FORK` or `DEFAULT`

Default: `FORK`

### search-gc-scan-size

The bulk size of the internal GC used for cleaning up indexes.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `100`

Redis Software default: `-1` (unlimited)

Redis Cloud defaults:

*   Flexible & Annual: `-1` (unlimited)
*   Free & Fixed: `10000`

### search-index-cursor-limit

Added in v2.10.8.

The maximum number of cursors that can be opened, per shard, at any given time. Cursors can be opened by the user via [`FT.AGGREGATE WITHCURSOR`](/docs/latest/commands/ft.aggregate/). Cursors are also opened internally by Redis Search for long-running queries. Once `INDEX_CURSOR_LIMIT` is reached, any further attempts to open a cursor will result in an error.

Notes:

*   Caution should be used in modifying this parameter. Every open cursor results in additional memory usage.
*   Cursor usage should be regulated first by use of [`FT.CURSOR DEL`](/docs/latest/commands/ft.cursor-del/) and/or [`MAXIDLE`](/docs/latest/commands/ft.aggregate/) prior to modifying `INDEX_CURSOR_LIMIT`
*   See [Cursor API](/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations/#cursor-api) for more details.

Type: integer

Default: `128`

### search-max-aggregate-results

The maximum number of results to be returned by the `FT.AGGREGATE` command if `LIMIT` is used.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `-1` (unlimited)

Redis Software default: `-1` (unlimited)

Redis Cloud defaults:

*   Flexible & Annual: `-1` (unlimited)
*   Free & Fixed: `10000`

### search-max-doctablesize

The maximum size of the internal hash table used for storing documents. Note: this configuration option doesn't limit the number of documents that can be stored. It only affects the hash table internal array maximum size. Decreasing this property can decrease the memory overhead in cases where the index holds a small number of documents that are constantly updated.

Type: integer

Valid range: `[1 .. 18,446,744,073,709,551,615]`

Default: `1000000`

### search-max-expansions

This parameter is an alias for [search-max-prefix-expansions](#search-max-prefix-expansions).

### search-max-prefix-expansions

The maximum number of expansions allowed for query prefixes. The maximum number of expansions allowed for query prefixes. Setting it too high can cause performance issues. If `search-max-prefix-expansions` is reached, the query will continue with the first acquired results. The configuration is applicable for all affix queries including prefix, suffix, and infix (contains) queries.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `200`

### search-max-search-results

The maximum number of results to be returned by the `FT.SEARCH` command if `LIMIT` is used. Set it to `-1` to remove the limit.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `1000000`

Redis Software default: `1000000`

Redis Cloud defaults:

*   Flexible & Annual: `1000000`
*   Free & Fixed: `10000`

### search-min-operation-workers

The number of worker threads to use for background tasks when the server is in an operation event.

Type: integer

Valid range: `[0 .. 8192]`

Default: `4`

### search-min-phonetic-term-len

The minimum length of term to be considered for phonetic matching.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `3`

### search-min-prefix

The minimum number of characters allowed for prefix queries (for example, hel\*). Setting it to `1` can reduce performance.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `2`

### search-min-stem-len

The minimum word length to stem. Setting it lower than `4` can reduce performance.

Type: integer

Valid range: `[2 .. 4,294,967,295]`

Redis Open Source default: `4`

Redis Software and Redis Cloud default: `2`

### search-multi-text-slop

Set the delta that is used to increase positional offsets between array slots for multi text values. This will allow you to control the level of separation between phrases in different array slots; related to the `SLOP` parameter of `FT.SEARCH` command.

Type: integer

Valid range: `[0 .. 4,294,967,295]`

Default: `100`

### search-no-mem-pools

Set Redis Search to run without memory pools.

Type: boolean

Default: `FALSE`

### search-no-gc

If set to `TRUE`, garbage collection is disabled for all indexes.

Type: boolean

Default: `FALSE`

### search-on-timeout

The response policy for queries that exceed the [`search-timeout`](#search-timeout) setting can be one of the following:

*   `RETURN`: this policy will return the top results accumulated by the query until it timed out.
*   `FAIL`: will return an error when the query exceeds the timeout value.

Type: string

Valid values: `RETURN`, `FAIL`

Default: `RETURN`

### search-partial-indexed-docs

Added in v2.0.0.

Enable/disable the Redis command filter. The filter optimizes partial updates of hashes and may avoid re-indexing the hash if changed fields are not part of the schema.

The Redis command filter will be executed upon each Redis command. Though the filter is optimized, this will introduce a small increase in latency on all commands.  
This configuration is best used with partially indexed documents where the non-indexed fields are updated frequently.

Type: integer

Valid values: `0` (false), `1` (true)

Default: `0`

### search-raw-docid-encoding

Disable compression for DocID inverted indexes to boost CPU performance.

Type: boolean

Default: `FALSE`

### search-threads

Sets the number of search threads in the coordinator thread pool.

Type: integer

### search-io-threads

Sets the number of threads used in the coordinator to run I/O tasks with other shards.

Type: integer

Valid range: `[1 .. 256]`

Default: 1

### search-tiered-hnsw-buffer-limit

Used for setting the buffer limit threshold for vector tiered HNSW indexes. If Redis is using `WORKERS` for indexing, and the number of vectors waiting in the buffer to be indexed exceeds this limit, new vectors are inserted directly into HNSW.

Type: integer

Valid range: `[0 .. 9,223,372,036,854,775,807]`

Default: `1024`

### search-timeout

The maximum amount of time in milliseconds that a search query is allowed to run. If this time is exceeded, Redis returns the top results accumulated so far, or an error depending on the policy set with [`search-on-timeout`](#search-on-timeout). The timeout can be disabled by setting it to `0`.

Notes:

*   `search-timeout` refers to query time only.
*   Parsing the query is not counted towards `search-timeout`.
*   If `search-timeout` was not reached during the search, finalizing operations such as loading document content or reducers continue.

Type: integer

Value range: `[1 .. 9,223,372,036,854,775,807]`

Redis Open Source default: `500`

Redis Software default: `500`

Redis Cloud defaults:

*   Flexible & Annual: `500`
*   Free & Fixed: `100`

### search-topology-validation-timeout

Sets the timeout in milliseconds for topology validation. After this timeout, any pending requests will be processed, even if the topology is not fully connected. A value of `0` means no timeout.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `30000`

### search-union-iterator-heap

The minimum number of iterators in a union at which the iterator will switch to a heap based implementation.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `20`

### search-upgrade-index

Relevant only when loading an v1.x RDB file. Specify the argument for upgrading the index. This configuration setting is a special configuration option introduced to upgrade indexes from v1.x Redis Search versions, otherwise known as legacy indexes. This configuration option needs to be given for each legacy index, followed by the index name and all valid options for the index description (also referred to as the `ON` arguments for following hashes) as described on [FT.CREATE](/docs/latest/commands/ft.create/) command page.

Type: string

Default: there is no default for index name, and the other arguments have the same defaults as with the [`FT.CREATE`](/docs/latest/commands/ft.create/) command.

**Example**

```
search-upgrade-index idx PREFIX 1 tt LANGUAGE french LANGUAGE_FIELD MyLang SCORE 0.5 SCORE_FIELD MyScore
    PAYLOAD_FIELD MyPayload UPGRADE_INDEX idx1
```

Notes:

*   If the RDB file does not contain a legacy index that's specified in the configuration, a warning message will be added to the log file, and loading will continue.
*   If the RDB file contains a legacy index that wasn't specified in the configuration, loading will fail and the server won't start.

### search-vss-max-resize

Added in v2.4.8.

The maximum memory resize (in bytes) for vector indexes. The maximum memory resize (in bytes) for vector indexes. This value will override default memory limits if you need to allow for a large [`BLOCK_SIZE`](/docs/latest/develop/ai/search-and-query/vectors/#creation-attributes-per-algorithm).

Type: integer

Valid range: `[0 .. 4,294,967,295]`

Default: `0`

### search-workers-priority-bias-threshold

The number of high priority tasks to be executed at any given time by the worker thread pool before executing low priority tasks. After this number of high priority tasks are being executed, the worker thread pool will execute high and low priority tasks alternately.

Type: integer

Valid range: `[1 .. 9,223,372,036,854,775,807]`

Default: `1`

### search-workers

The number of worker threads to use for query processing and background tasks.

Type: integer

Valid range: `[0 .. 8192]`

Default: `0`

### search-on-oom

Specifies the response policy for queries when the server's current memory usage exceeds the configured [maxmemory](redis/docs/latest/develop/reference/eviction/index.md#maxmem) limit.

*   `IGNORE`: Execute the query regardless of current memory usage.
*   `RETURN`: In cluster mode, the query returns partial results from shards that did not exceed the memory limit. Shards that exceed the limit will not contribute results.
*   `FAIL`: Will return an error if memory usage exceeds the memory limit.

Type: string

Valid values: `IGNORE`, `RETURN`, `FAIL`

Default: `IGNORE`

Notes:

To prevent potential out-of-memory conditions, it is recommended that you set this parameter to FAIL or RETURN rather than IGNORE.

## Set configuration parameters at module load-time (deprecated)

These methods are deprecated beginning with Redis 8.

Setting configuration parameters at load-time is done by appending arguments after the `--loadmodule` argument when starting a server from the command line, or after the `loadmodule` directive in a Redis config file. For example:

In [redis.conf](/docs/latest/operate/oss_and_stack/management/config/):

```
loadmodule ./redisearch.so [OPT VAL]...
```

From the [Redis CLI](/docs/latest/develop/tools/cli/), using the [MODULE LOAD](/docs/latest/commands/module-load/) command:

```
127.0.0.6379> MODULE LOAD redisearch.so [OPT VAL]...
```

From the command line:

```
$ redis-server --loadmodule ./redisearch.so [OPT VAL]...
```

## Set configuration parameters at run-time (for supported parameters, deprecated)

These methods are deprecated beginning with Redis 8.

Redis Search exposes the `FT.CONFIG` endpoint to allow for the setting and retrieval of configuration parameters at run-time.

To set the value of a configuration parameter at run-time (for supported parameters), simply run:

```sh
FT.CONFIG SET OPT1 VAL1
```

Similarly, you can retrieve current configuration parameter values using:

```sh
FT.CONFIG GET OPT1
FT.CONFIG GET *
```

Values set using [`FT.CONFIG SET`](/docs/latest/commands/ft.config-set/) are not persisted after server restart.

## On this page
