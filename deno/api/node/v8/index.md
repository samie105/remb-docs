---
title: "v8 - Node documentation"
source: "https://docs.deno.com/api/node/v8/"
canonical_url: "https://docs.deno.com/api/node/v8/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:16:12.823Z"
content_hash: "4927cf6e568f9d8280593b5408e882a28ffa543f7d8e9883db7dac54ba56ea4d"
menu_path: ["v8 - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/util/types/index.md", "title": "util/types - Node documentation"}
nav_next: {"path": "deno/api/node/vm/index.md", "title": "vm - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:v8";
```

Deno compatibility

`cachedDataVersionTag` and `getHeapStatistics`, `serialize` and `deserialize` are supported. `setFlagsFromStrings` is a noop. Other APIs are not supported and will throw and error.

The `node:v8` module exposes APIs that are specific to the version of [V8](https://developers.google.com/v8/) built into the Node.js binary. It can be accessed using:

```js
import v8 from 'node:v8';
```

c

[DefaultDeserializer](.././v8/~/DefaultDeserializer "DefaultDeserializer")

A subclass of `Deserializer` corresponding to the format written by `DefaultSerializer`.

c

[DefaultSerializer](.././v8/~/DefaultSerializer "DefaultSerializer")

A subclass of `Serializer` that serializes `TypedArray`(in particular `Buffer`) and `DataView` objects as host objects, and only stores the part of their underlying `ArrayBuffer`s that they are referring to.

c

[Deserializer](.././v8/~/Deserializer "Deserializer")

No documentation available

-   [getWireFormatVersion](.././v8/~/Deserializer#method_getwireformatversion_0)
-   [readDouble](.././v8/~/Deserializer#method_readdouble_0)
-   [readHeader](.././v8/~/Deserializer#method_readheader_0)
-   [readRawBytes](.././v8/~/Deserializer#method_readrawbytes_0)
-   [readUint32](.././v8/~/Deserializer#method_readuint32_0)
-   [readUint64](.././v8/~/Deserializer#method_readuint64_0)
-   [readValue](.././v8/~/Deserializer#method_readvalue_0)
-   [transferArrayBuffer](.././v8/~/Deserializer#method_transferarraybuffer_0)

c

[GCProfiler](.././v8/~/GCProfiler "GCProfiler")

This API collects GC data in current thread.

-   [start](.././v8/~/GCProfiler#method_start_0)
-   [stop](.././v8/~/GCProfiler#method_stop_0)

c

[Serializer](.././v8/~/Serializer "Serializer")

No documentation available

-   [releaseBuffer](.././v8/~/Serializer#method_releasebuffer_0)
-   [transferArrayBuffer](.././v8/~/Serializer#method_transferarraybuffer_0)
-   [writeDouble](.././v8/~/Serializer#method_writedouble_0)
-   [writeHeader](.././v8/~/Serializer#method_writeheader_0)
-   [writeRawBytes](.././v8/~/Serializer#method_writerawbytes_0)
-   [writeUint32](.././v8/~/Serializer#method_writeuint32_0)
-   [writeUint64](.././v8/~/Serializer#method_writeuint64_0)
-   [writeValue](.././v8/~/Serializer#method_writevalue_0)

f

[cachedDataVersionTag](.././v8/~/cachedDataVersionTag "cachedDataVersionTag")

Returns an integer representing a version tag derived from the V8 version, command-line flags, and detected CPU features. This is useful for determining whether a `vm.Script` `cachedData` buffer is compatible with this instance of V8.

f

[deserialize](.././v8/~/deserialize "deserialize")

Uses a `DefaultDeserializer` with default options to read a JS value from a buffer.

f

[getHeapCodeStatistics](.././v8/~/getHeapCodeStatistics "getHeapCodeStatistics")

Get statistics about code and its metadata in the heap, see V8 [`GetHeapCodeAndMetadataStatistics`](https://v8docs.nodesource.com/node-13.2/d5/dda/classv8_1_1_isolate.html#a6079122af17612ef54ef3348ce170866) API. Returns an object with the following properties:

f

[getHeapSnapshot](.././v8/~/getHeapSnapshot "getHeapSnapshot")

Generates a snapshot of the current V8 heap and returns a Readable Stream that may be used to read the JSON serialized representation. This JSON stream format is intended to be used with tools such as Chrome DevTools. The JSON schema is undocumented and specific to the V8 engine. Therefore, the schema may change from one version of V8 to the next.

f

[getHeapSpaceStatistics](.././v8/~/getHeapSpaceStatistics "getHeapSpaceStatistics")

Returns statistics about the V8 heap spaces, i.e. the segments which make up the V8 heap. Neither the ordering of heap spaces, nor the availability of a heap space can be guaranteed as the statistics are provided via the V8 [`GetHeapSpaceStatistics`](https://v8docs.nodesource.com/node-13.2/d5/dda/classv8_1_1_isolate.html#ac673576f24fdc7a33378f8f57e1d13a4) function and may change from one V8 version to the next.

f

[getHeapStatistics](.././v8/~/getHeapStatistics "getHeapStatistics")

Returns an object with the following properties:

f

[queryObjects](.././v8/~/queryObjects "queryObjects")

This is similar to the [`queryObjects()` console API](https://developer.chrome.com/docs/devtools/console/utilities#queryObjects-function) provided by the Chromium DevTools console. It can be used to search for objects that have the matching constructor on its prototype chain in the heap after a full garbage collection, which can be useful for memory leak regression tests. To avoid surprising results, users should avoid using this API on constructors whose implementation they don't control, or on constructors that can be invoked by other parties in the application.

f

[serialize](.././v8/~/serialize "serialize")

Uses a `DefaultSerializer` to serialize `value` into a buffer.

f

[setFlagsFromString](.././v8/~/setFlagsFromString "setFlagsFromString")

The `v8.setFlagsFromString()` method can be used to programmatically set V8 command-line flags. This method should be used with care. Changing settings after the VM has started may result in unpredictable behavior, including crashes and data loss; or it may simply do nothing.

f

[setHeapSnapshotNearHeapLimit](.././v8/~/setHeapSnapshotNearHeapLimit "setHeapSnapshotNearHeapLimit")

The API is a no-op if `--heapsnapshot-near-heap-limit` is already set from the command line or the API is called more than once. `limit` must be a positive integer. See [`--heapsnapshot-near-heap-limit`](https://nodejs.org/docs/latest-v22.x/api/cli.html#--heapsnapshot-near-heap-limitmax_count) for more information.

f

[stopCoverage](.././v8/~/stopCoverage "stopCoverage")

The `v8.stopCoverage()` method allows the user to stop the coverage collection started by `NODE_V8_COVERAGE`, so that V8 can release the execution count records and optimize code. This can be used in conjunction with [takeCoverage](.././v8/~/takeCoverage) if the user wants to collect the coverage on demand.

f

[takeCoverage](.././v8/~/takeCoverage "takeCoverage")

The `v8.takeCoverage()` method allows the user to write the coverage started by `NODE_V8_COVERAGE` to disk on demand. This method can be invoked multiple times during the lifetime of the process. Each time the execution counter will be reset and a new coverage report will be written to the directory specified by `NODE_V8_COVERAGE`.

f

[writeHeapSnapshot](.././v8/~/writeHeapSnapshot "writeHeapSnapshot")

Generates a snapshot of the current V8 heap and writes it to a JSON file. This file is intended to be used with tools such as Chrome DevTools. The JSON schema is undocumented and specific to the V8 engine, and may change from one version of V8 to the next.

I

[After](.././v8/~/After "After")

Called immediately after a promise continuation executes. This may be after a `then()`, `catch()`, or `finally()` handler or before an await after another await.

I

[Before](.././v8/~/Before "Before")

Called before a promise continuation executes. This can be in the form of `then()`, `catch()`, or `finally()` handlers or an await resuming.

I

[GCProfilerResult](.././v8/~/GCProfilerResult "GCProfilerResult")

No documentation available

-   [endTime](.././v8/~/GCProfilerResult#property_endtime)
-   [startTime](.././v8/~/GCProfilerResult#property_starttime)
-   [statistics](.././v8/~/GCProfilerResult#property_statistics)
-   [version](.././v8/~/GCProfilerResult#property_version)

I

[HeapCodeStatistics](.././v8/~/HeapCodeStatistics "HeapCodeStatistics")

No documentation available

-   [bytecode\_and\_metadata\_size](.././v8/~/HeapCodeStatistics#property_bytecode_and_metadata_size)
-   [code\_and\_metadata\_size](.././v8/~/HeapCodeStatistics#property_code_and_metadata_size)
-   [external\_script\_source\_size](.././v8/~/HeapCodeStatistics#property_external_script_source_size)

I

[HeapInfo](.././v8/~/HeapInfo "HeapInfo")

No documentation available

-   [does\_zap\_garbage](.././v8/~/HeapInfo#property_does_zap_garbage)
-   [external\_memory](.././v8/~/HeapInfo#property_external_memory)
-   [heap\_size\_limit](.././v8/~/HeapInfo#property_heap_size_limit)
-   [malloced\_memory](.././v8/~/HeapInfo#property_malloced_memory)
-   [number\_of\_detached\_contexts](.././v8/~/HeapInfo#property_number_of_detached_contexts)
-   [number\_of\_native\_contexts](.././v8/~/HeapInfo#property_number_of_native_contexts)
-   [peak\_malloced\_memory](.././v8/~/HeapInfo#property_peak_malloced_memory)
-   [total\_available\_size](.././v8/~/HeapInfo#property_total_available_size)
-   [total\_global\_handles\_size](.././v8/~/HeapInfo#property_total_global_handles_size)
-   [total\_heap\_size](.././v8/~/HeapInfo#property_total_heap_size)
-   [total\_heap\_size\_executable](.././v8/~/HeapInfo#property_total_heap_size_executable)
-   [total\_physical\_size](.././v8/~/HeapInfo#property_total_physical_size)
-   [used\_global\_handles\_size](.././v8/~/HeapInfo#property_used_global_handles_size)
-   [used\_heap\_size](.././v8/~/HeapInfo#property_used_heap_size)

I

[HeapSnapshotOptions](.././v8/~/HeapSnapshotOptions "HeapSnapshotOptions")

No documentation available

-   [exposeInternals](.././v8/~/HeapSnapshotOptions#property_exposeinternals)
-   [exposeNumericValues](.././v8/~/HeapSnapshotOptions#property_exposenumericvalues)

I

[HeapSpaceInfo](.././v8/~/HeapSpaceInfo "HeapSpaceInfo")

No documentation available

-   [physical\_space\_size](.././v8/~/HeapSpaceInfo#property_physical_space_size)
-   [space\_available\_size](.././v8/~/HeapSpaceInfo#property_space_available_size)
-   [space\_name](.././v8/~/HeapSpaceInfo#property_space_name)
-   [space\_size](.././v8/~/HeapSpaceInfo#property_space_size)
-   [space\_used\_size](.././v8/~/HeapSpaceInfo#property_space_used_size)

I

[HeapSpaceStatistics](.././v8/~/HeapSpaceStatistics "HeapSpaceStatistics")

No documentation available

-   [physicalSpaceSize](.././v8/~/HeapSpaceStatistics#property_physicalspacesize)
-   [spaceAvailableSize](.././v8/~/HeapSpaceStatistics#property_spaceavailablesize)
-   [spaceName](.././v8/~/HeapSpaceStatistics#property_spacename)
-   [spaceSize](.././v8/~/HeapSpaceStatistics#property_spacesize)
-   [spaceUsedSize](.././v8/~/HeapSpaceStatistics#property_spaceusedsize)

I

[HeapStatistics](.././v8/~/HeapStatistics "HeapStatistics")

No documentation available

-   [externalMemory](.././v8/~/HeapStatistics#property_externalmemory)
-   [heapSizeLimit](.././v8/~/HeapStatistics#property_heapsizelimit)
-   [mallocedMemory](.././v8/~/HeapStatistics#property_mallocedmemory)
-   [peakMallocedMemory](.././v8/~/HeapStatistics#property_peakmallocedmemory)
-   [totalAvailableSize](.././v8/~/HeapStatistics#property_totalavailablesize)
-   [totalGlobalHandlesSize](.././v8/~/HeapStatistics#property_totalglobalhandlessize)
-   [totalHeapSize](.././v8/~/HeapStatistics#property_totalheapsize)
-   [totalHeapSizeExecutable](.././v8/~/HeapStatistics#property_totalheapsizeexecutable)
-   [totalPhysicalSize](.././v8/~/HeapStatistics#property_totalphysicalsize)
-   [usedGlobalHandlesSize](.././v8/~/HeapStatistics#property_usedglobalhandlessize)
-   [usedHeapSize](.././v8/~/HeapStatistics#property_usedheapsize)

I

[HookCallbacks](.././v8/~/HookCallbacks "HookCallbacks")

Key events in the lifetime of a promise have been categorized into four areas: creation of a promise, before/after a continuation handler is called or around an await, and when the promise resolves or rejects.

-   [after](.././v8/~/HookCallbacks#property_after)
-   [before](.././v8/~/HookCallbacks#property_before)
-   [init](.././v8/~/HookCallbacks#property_init)
-   [settled](.././v8/~/HookCallbacks#property_settled)

I

[Init](.././v8/~/Init "Init")

Called when a promise is constructed. This does not mean that corresponding before/after events will occur, only that the possibility exists. This will happen if a promise is created without ever getting a continuation.

I

[PromiseHooks](.././v8/~/PromiseHooks "PromiseHooks")

No documentation available

-   [createHook](.././v8/~/PromiseHooks#property_createhook)
-   [onAfter](.././v8/~/PromiseHooks#property_onafter)
-   [onBefore](.././v8/~/PromiseHooks#property_onbefore)
-   [onInit](.././v8/~/PromiseHooks#property_oninit)
-   [onSettled](.././v8/~/PromiseHooks#property_onsettled)

I

[Settled](.././v8/~/Settled "Settled")

Called when the promise receives a resolution or rejection value. This may occur synchronously in the case of Promise.resolve() or Promise.reject().

I

[StartupSnapshot](.././v8/~/StartupSnapshot "StartupSnapshot")

No documentation available

-   [addDeserializeCallback](.././v8/~/StartupSnapshot#method_adddeserializecallback_0)
-   [addSerializeCallback](.././v8/~/StartupSnapshot#method_addserializecallback_0)
-   [isBuildingSnapshot](.././v8/~/StartupSnapshot#method_isbuildingsnapshot_0)
-   [setDeserializeMainFunction](.././v8/~/StartupSnapshot#method_setdeserializemainfunction_0)

T

[DoesZapCodeSpaceFlag](.././v8/~/DoesZapCodeSpaceFlag "DoesZapCodeSpaceFlag")

No documentation available

T

[StartupSnapshotCallbackFn](.././v8/~/StartupSnapshotCallbackFn "StartupSnapshotCallbackFn")

No documentation available

v

[promiseHooks](.././v8/~/promiseHooks "promiseHooks")

The `promiseHooks` interface can be used to track promise lifecycle events.

v

[startupSnapshot](.././v8/~/startupSnapshot "startupSnapshot")

The `v8.startupSnapshot` interface can be used to add serialization and deserialization hooks for custom startup snapshots.
