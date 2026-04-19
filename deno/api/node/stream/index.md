---
title: "stream - Node documentation"
source: "https://docs.deno.com/api/node/stream/"
canonical_url: "https://docs.deno.com/api/node/stream/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:24.343Z"
content_hash: "2b41da08559152d5a4f47d6f3958b44bd83bf1e0e3e5239fd61e9586ba98fab0"
menu_path: ["stream - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:stream";
```

A stream is an abstract interface for working with streaming data in Node.js. The `node:stream` module provides an API for implementing the stream interface.

There are many stream objects provided by Node.js. For instance, a [request to an HTTP server](https://nodejs.org/docs/latest-v22.x/api/http.html#class-httpincomingmessage) and [`process.stdout`](https://nodejs.org/docs/latest-v22.x/api/process.html#processstdout) are both stream instances.

Streams can be readable, writable, or both. All streams are instances of [`EventEmitter`](https://nodejs.org/docs/latest-v22.x/api/events.html#class-eventemitter).

To access the `node:stream` module:

```js
import stream from 'node:stream';
```

The `node:stream` module is useful for creating new types of stream instances. It is usually not necessary to use the `node:stream` module to consume streams.

### Classes [#](#Classes)

c

N

[default](.././stream/~/default "default")

No documentation available

*   [compose](.././stream/~/default#method_compose_0)
*   [pipe](.././stream/~/default#method_pipe_0)

c

I

[default.Duplex](.././stream/~/default.Duplex "default.Duplex")

Duplex streams are streams that implement both the `Readable` and `Writable` interfaces.

*   [addListener](.././stream/~/default.Duplex#method_addlistener_0)
*   [allowHalfOpen](.././stream/~/default.Duplex#property_allowhalfopen)
*   [emit](.././stream/~/default.Duplex#method_emit_0)
*   [from](.././stream/~/default.Duplex#method_from_0)
*   [fromWeb](.././stream/~/default.Duplex#method_fromweb_0)
*   [on](.././stream/~/default.Duplex#method_on_0)
*   [once](.././stream/~/default.Duplex#method_once_0)
*   [prependListener](.././stream/~/default.Duplex#method_prependlistener_0)
*   [prependOnceListener](.././stream/~/default.Duplex#method_prependoncelistener_0)
*   [removeListener](.././stream/~/default.Duplex#method_removelistener_0)
*   [toWeb](.././stream/~/default.Duplex#method_toweb_0)

c

[default.PassThrough](.././stream/~/default.PassThrough "default.PassThrough")

The `stream.PassThrough` class is a trivial implementation of a `Transform` stream that simply passes the input bytes across to the output. Its purpose is primarily for examples and testing, but there are some use cases where `stream.PassThrough` is useful as a building block for novel sorts of streams.

c

[default.Readable](.././stream/~/default.Readable "default.Readable")

No documentation available

*   [\_construct](.././stream/~/default.Readable#method__construct_0)
*   [\_destroy](.././stream/~/default.Readable#method__destroy_0)
*   [\_read](.././stream/~/default.Readable#method__read_0)
*   [addListener](.././stream/~/default.Readable#method_addlistener_0)
*   [asIndexedPairs](.././stream/~/default.Readable#method_asindexedpairs_0)
*   [closed](.././stream/~/default.Readable#property_closed)
*   [destroy](.././stream/~/default.Readable#method_destroy_0)
*   [destroyed](.././stream/~/default.Readable#property_destroyed)
*   [drop](.././stream/~/default.Readable#method_drop_0)
*   [emit](.././stream/~/default.Readable#method_emit_0)
*   [errored](.././stream/~/default.Readable#property_errored)
*   [every](.././stream/~/default.Readable#method_every_0)
*   [filter](.././stream/~/default.Readable#method_filter_0)
*   [find](.././stream/~/default.Readable#method_find_0)
*   [flatMap](.././stream/~/default.Readable#method_flatmap_0)
*   [forEach](.././stream/~/default.Readable#method_foreach_0)
*   [from](.././stream/~/default.Readable#method_from_0)
*   [fromWeb](.././stream/~/default.Readable#method_fromweb_0)
*   [isDisturbed](.././stream/~/default.Readable#method_isdisturbed_0)
*   [isPaused](.././stream/~/default.Readable#method_ispaused_0)
*   [iterator](.././stream/~/default.Readable#method_iterator_0)
*   [map](.././stream/~/default.Readable#method_map_0)
*   [on](.././stream/~/default.Readable#method_on_0)
*   [once](.././stream/~/default.Readable#method_once_0)
*   [pause](.././stream/~/default.Readable#method_pause_0)
*   [prependListener](.././stream/~/default.Readable#method_prependlistener_0)
*   [prependOnceListener](.././stream/~/default.Readable#method_prependoncelistener_0)
*   [push](.././stream/~/default.Readable#method_push_0)
*   [read](.././stream/~/default.Readable#method_read_0)
*   [readable](.././stream/~/default.Readable#property_readable)
*   [readableAborted](.././stream/~/default.Readable#property_readableaborted)
*   [readableDidRead](.././stream/~/default.Readable#property_readabledidread)
*   [readableEncoding](.././stream/~/default.Readable#property_readableencoding)
*   [readableEnded](.././stream/~/default.Readable#property_readableended)
*   [readableFlowing](.././stream/~/default.Readable#property_readableflowing)
*   [readableHighWaterMark](.././stream/~/default.Readable#property_readablehighwatermark)
*   [readableLength](.././stream/~/default.Readable#property_readablelength)
*   [readableObjectMode](.././stream/~/default.Readable#property_readableobjectmode)
*   [reduce](.././stream/~/default.Readable#method_reduce_0)
*   [removeListener](.././stream/~/default.Readable#method_removelistener_0)
*   [resume](.././stream/~/default.Readable#method_resume_0)
*   [setEncoding](.././stream/~/default.Readable#method_setencoding_0)
*   [some](.././stream/~/default.Readable#method_some_0)
*   [take](.././stream/~/default.Readable#method_take_0)
*   [toArray](.././stream/~/default.Readable#method_toarray_0)
*   [toWeb](.././stream/~/default.Readable#method_toweb_0)
*   [unpipe](.././stream/~/default.Readable#method_unpipe_0)
*   [unshift](.././stream/~/default.Readable#method_unshift_0)
*   [wrap](.././stream/~/default.Readable#method_wrap_0)

c

[default.Transform](.././stream/~/default.Transform "default.Transform")

Transform streams are `Duplex` streams where the output is in some way related to the input. Like all `Duplex` streams, `Transform` streams implement both the `Readable` and `Writable` interfaces.

*   [\_flush](.././stream/~/default.Transform#method__flush_0)
*   [\_transform](.././stream/~/default.Transform#method__transform_0)

c

[default.Writable](.././stream/~/default.Writable "default.Writable")

No documentation available

*   [\_construct](.././stream/~/default.Writable#method__construct_0)
*   [\_destroy](.././stream/~/default.Writable#method__destroy_0)
*   [\_final](.././stream/~/default.Writable#method__final_0)
*   [\_write](.././stream/~/default.Writable#method__write_0)
*   [\_writev](.././stream/~/default.Writable#method__writev_0)
*   [addListener](.././stream/~/default.Writable#method_addlistener_0)
*   [closed](.././stream/~/default.Writable#property_closed)
*   [cork](.././stream/~/default.Writable#method_cork_0)
*   [destroy](.././stream/~/default.Writable#method_destroy_0)
*   [destroyed](.././stream/~/default.Writable#property_destroyed)
*   [emit](.././stream/~/default.Writable#method_emit_0)
*   [end](.././stream/~/default.Writable#method_end_0)
*   [errored](.././stream/~/default.Writable#property_errored)
*   [fromWeb](.././stream/~/default.Writable#method_fromweb_0)
*   [on](.././stream/~/default.Writable#method_on_0)
*   [once](.././stream/~/default.Writable#method_once_0)
*   [prependListener](.././stream/~/default.Writable#method_prependlistener_0)
*   [prependOnceListener](.././stream/~/default.Writable#method_prependoncelistener_0)
*   [removeListener](.././stream/~/default.Writable#method_removelistener_0)
*   [setDefaultEncoding](.././stream/~/default.Writable#method_setdefaultencoding_0)
*   [toWeb](.././stream/~/default.Writable#method_toweb_0)
*   [uncork](.././stream/~/default.Writable#method_uncork_0)
*   [writable](.././stream/~/default.Writable#property_writable)
*   [writableCorked](.././stream/~/default.Writable#property_writablecorked)
*   [writableEnded](.././stream/~/default.Writable#property_writableended)
*   [writableFinished](.././stream/~/default.Writable#property_writablefinished)
*   [writableHighWaterMark](.././stream/~/default.Writable#property_writablehighwatermark)
*   [writableLength](.././stream/~/default.Writable#property_writablelength)
*   [writableNeedDrain](.././stream/~/default.Writable#property_writableneeddrain)
*   [writableObjectMode](.././stream/~/default.Writable#property_writableobjectmode)
*   [write](.././stream/~/default.Writable#method_write_0)

c

N

[Stream](.././stream/~/Stream "Stream")

No documentation available

*   [compose](.././stream/~/Stream#method_compose_0)
*   [pipe](.././stream/~/Stream#method_pipe_0)

c

I

[Stream.Duplex](.././stream/~/Stream.Duplex "Stream.Duplex")

Duplex streams are streams that implement both the `Readable` and `Writable` interfaces.

*   [addListener](.././stream/~/Stream.Duplex#method_addlistener_0)
*   [allowHalfOpen](.././stream/~/Stream.Duplex#property_allowhalfopen)
*   [emit](.././stream/~/Stream.Duplex#method_emit_0)
*   [from](.././stream/~/Stream.Duplex#method_from_0)
*   [fromWeb](.././stream/~/Stream.Duplex#method_fromweb_0)
*   [on](.././stream/~/Stream.Duplex#method_on_0)
*   [once](.././stream/~/Stream.Duplex#method_once_0)
*   [prependListener](.././stream/~/Stream.Duplex#method_prependlistener_0)
*   [prependOnceListener](.././stream/~/Stream.Duplex#method_prependoncelistener_0)
*   [removeListener](.././stream/~/Stream.Duplex#method_removelistener_0)
*   [toWeb](.././stream/~/Stream.Duplex#method_toweb_0)

c

[Stream.PassThrough](.././stream/~/Stream.PassThrough "Stream.PassThrough")

The `stream.PassThrough` class is a trivial implementation of a `Transform` stream that simply passes the input bytes across to the output. Its purpose is primarily for examples and testing, but there are some use cases where `stream.PassThrough` is useful as a building block for novel sorts of streams.

c

[Stream.Readable](.././stream/~/Stream.Readable "Stream.Readable")

No documentation available

*   [\_construct](.././stream/~/Stream.Readable#method__construct_0)
*   [\_destroy](.././stream/~/Stream.Readable#method__destroy_0)
*   [\_read](.././stream/~/Stream.Readable#method__read_0)
*   [addListener](.././stream/~/Stream.Readable#method_addlistener_0)
*   [asIndexedPairs](.././stream/~/Stream.Readable#method_asindexedpairs_0)
*   [closed](.././stream/~/Stream.Readable#property_closed)
*   [destroy](.././stream/~/Stream.Readable#method_destroy_0)
*   [destroyed](.././stream/~/Stream.Readable#property_destroyed)
*   [drop](.././stream/~/Stream.Readable#method_drop_0)
*   [emit](.././stream/~/Stream.Readable#method_emit_0)
*   [errored](.././stream/~/Stream.Readable#property_errored)
*   [every](.././stream/~/Stream.Readable#method_every_0)
*   [filter](.././stream/~/Stream.Readable#method_filter_0)
*   [find](.././stream/~/Stream.Readable#method_find_0)
*   [flatMap](.././stream/~/Stream.Readable#method_flatmap_0)
*   [forEach](.././stream/~/Stream.Readable#method_foreach_0)
*   [from](.././stream/~/Stream.Readable#method_from_0)
*   [fromWeb](.././stream/~/Stream.Readable#method_fromweb_0)
*   [isDisturbed](.././stream/~/Stream.Readable#method_isdisturbed_0)
*   [isPaused](.././stream/~/Stream.Readable#method_ispaused_0)
*   [iterator](.././stream/~/Stream.Readable#method_iterator_0)
*   [map](.././stream/~/Stream.Readable#method_map_0)
*   [on](.././stream/~/Stream.Readable#method_on_0)
*   [once](.././stream/~/Stream.Readable#method_once_0)
*   [pause](.././stream/~/Stream.Readable#method_pause_0)
*   [prependListener](.././stream/~/Stream.Readable#method_prependlistener_0)
*   [prependOnceListener](.././stream/~/Stream.Readable#method_prependoncelistener_0)
*   [push](.././stream/~/Stream.Readable#method_push_0)
*   [read](.././stream/~/Stream.Readable#method_read_0)
*   [readable](.././stream/~/Stream.Readable#property_readable)
*   [readableAborted](.././stream/~/Stream.Readable#property_readableaborted)
*   [readableDidRead](.././stream/~/Stream.Readable#property_readabledidread)
*   [readableEncoding](.././stream/~/Stream.Readable#property_readableencoding)
*   [readableEnded](.././stream/~/Stream.Readable#property_readableended)
*   [readableFlowing](.././stream/~/Stream.Readable#property_readableflowing)
*   [readableHighWaterMark](.././stream/~/Stream.Readable#property_readablehighwatermark)
*   [readableLength](.././stream/~/Stream.Readable#property_readablelength)
*   [readableObjectMode](.././stream/~/Stream.Readable#property_readableobjectmode)
*   [reduce](.././stream/~/Stream.Readable#method_reduce_0)
*   [removeListener](.././stream/~/Stream.Readable#method_removelistener_0)
*   [resume](.././stream/~/Stream.Readable#method_resume_0)
*   [setEncoding](.././stream/~/Stream.Readable#method_setencoding_0)
*   [some](.././stream/~/Stream.Readable#method_some_0)
*   [take](.././stream/~/Stream.Readable#method_take_0)
*   [toArray](.././stream/~/Stream.Readable#method_toarray_0)
*   [toWeb](.././stream/~/Stream.Readable#method_toweb_0)
*   [unpipe](.././stream/~/Stream.Readable#method_unpipe_0)
*   [unshift](.././stream/~/Stream.Readable#method_unshift_0)
*   [wrap](.././stream/~/Stream.Readable#method_wrap_0)

c

[Stream.Transform](.././stream/~/Stream.Transform "Stream.Transform")

Transform streams are `Duplex` streams where the output is in some way related to the input. Like all `Duplex` streams, `Transform` streams implement both the `Readable` and `Writable` interfaces.

*   [\_flush](.././stream/~/Stream.Transform#method__flush_0)
*   [\_transform](.././stream/~/Stream.Transform#method__transform_0)

c

[Stream.Writable](.././stream/~/Stream.Writable "Stream.Writable")

No documentation available

*   [\_construct](.././stream/~/Stream.Writable#method__construct_0)
*   [\_destroy](.././stream/~/Stream.Writable#method__destroy_0)
*   [\_final](.././stream/~/Stream.Writable#method__final_0)
*   [\_write](.././stream/~/Stream.Writable#method__write_0)
*   [\_writev](.././stream/~/Stream.Writable#method__writev_0)
*   [addListener](.././stream/~/Stream.Writable#method_addlistener_0)
*   [closed](.././stream/~/Stream.Writable#property_closed)
*   [cork](.././stream/~/Stream.Writable#method_cork_0)
*   [destroy](.././stream/~/Stream.Writable#method_destroy_0)
*   [destroyed](.././stream/~/Stream.Writable#property_destroyed)
*   [emit](.././stream/~/Stream.Writable#method_emit_0)
*   [end](.././stream/~/Stream.Writable#method_end_0)
*   [errored](.././stream/~/Stream.Writable#property_errored)
*   [fromWeb](.././stream/~/Stream.Writable#method_fromweb_0)
*   [on](.././stream/~/Stream.Writable#method_on_0)
*   [once](.././stream/~/Stream.Writable#method_once_0)
*   [prependListener](.././stream/~/Stream.Writable#method_prependlistener_0)
*   [prependOnceListener](.././stream/~/Stream.Writable#method_prependoncelistener_0)
*   [removeListener](.././stream/~/Stream.Writable#method_removelistener_0)
*   [setDefaultEncoding](.././stream/~/Stream.Writable#method_setdefaultencoding_0)
*   [toWeb](.././stream/~/Stream.Writable#method_toweb_0)
*   [uncork](.././stream/~/Stream.Writable#method_uncork_0)
*   [writable](.././stream/~/Stream.Writable#property_writable)
*   [writableCorked](.././stream/~/Stream.Writable#property_writablecorked)
*   [writableEnded](.././stream/~/Stream.Writable#property_writableended)
*   [writableFinished](.././stream/~/Stream.Writable#property_writablefinished)
*   [writableHighWaterMark](.././stream/~/Stream.Writable#property_writablehighwatermark)
*   [writableLength](.././stream/~/Stream.Writable#property_writablelength)
*   [writableNeedDrain](.././stream/~/Stream.Writable#property_writableneeddrain)
*   [writableObjectMode](.././stream/~/Stream.Writable#property_writableobjectmode)
*   [write](.././stream/~/Stream.Writable#method_write_0)

### Functions [#](#Functions)

f

[default.addAbortSignal](.././stream/~/default.addAbortSignal "default.addAbortSignal")

A stream to attach a signal to.

f

[default.duplexPair](.././stream/~/default.duplexPair "default.duplexPair")

The utility function `duplexPair` returns an Array with two items, each being a `Duplex` stream connected to the other side:

f

N

[default.finished](.././stream/~/default.finished "default.finished")

A readable and/or writable stream/webstream.

f

[default.finished.\_\_promisify\_\_](.././stream/~/default.finished.__promisify__ "default.finished.__promisify__")

No documentation available

f

[default.getDefaultHighWaterMark](.././stream/~/default.getDefaultHighWaterMark "default.getDefaultHighWaterMark")

Returns the default highWaterMark used by streams. Defaults to `65536` (64 KiB), or `16` for `objectMode`.

f

[default.isErrored](.././stream/~/default.isErrored "default.isErrored")

Returns whether the stream has encountered an error.

f

[default.isReadable](.././stream/~/default.isReadable "default.isReadable")

Returns whether the stream is readable.

f

N

[default.pipeline](.././stream/~/default.pipeline "default.pipeline")

A module method to pipe between streams and generators forwarding errors and properly cleaning up and provide a callback when the pipeline is complete.

f

[default.pipeline.\_\_promisify\_\_](.././stream/~/default.pipeline.__promisify__ "default.pipeline.__promisify__")

No documentation available

f

[default.setDefaultHighWaterMark](.././stream/~/default.setDefaultHighWaterMark "default.setDefaultHighWaterMark")

Sets the default highWaterMark used by streams.

f

[Stream.addAbortSignal](.././stream/~/Stream.addAbortSignal "Stream.addAbortSignal")

A stream to attach a signal to.

f

[Stream.duplexPair](.././stream/~/Stream.duplexPair "Stream.duplexPair")

The utility function `duplexPair` returns an Array with two items, each being a `Duplex` stream connected to the other side:

f

N

[Stream.finished](.././stream/~/Stream.finished "Stream.finished")

A readable and/or writable stream/webstream.

f

[Stream.finished.\_\_promisify\_\_](.././stream/~/Stream.finished.__promisify__ "Stream.finished.__promisify__")

No documentation available

f

[Stream.getDefaultHighWaterMark](.././stream/~/Stream.getDefaultHighWaterMark "Stream.getDefaultHighWaterMark")

Returns the default highWaterMark used by streams. Defaults to `65536` (64 KiB), or `16` for `objectMode`.

f

[Stream.isErrored](.././stream/~/Stream.isErrored "Stream.isErrored")

Returns whether the stream has encountered an error.

f

[Stream.isReadable](.././stream/~/Stream.isReadable "Stream.isReadable")

Returns whether the stream is readable.

f

N

[Stream.pipeline](.././stream/~/Stream.pipeline "Stream.pipeline")

A module method to pipe between streams and generators forwarding errors and properly cleaning up and provide a callback when the pipeline is complete.

f

[Stream.pipeline.\_\_promisify\_\_](.././stream/~/Stream.pipeline.__promisify__ "Stream.pipeline.__promisify__")

No documentation available

f

[Stream.setDefaultHighWaterMark](.././stream/~/Stream.setDefaultHighWaterMark "Stream.setDefaultHighWaterMark")

Sets the default highWaterMark used by streams.

### Interfaces [#](#Interfaces)

I

[default.ArrayOptions](.././stream/~/default.ArrayOptions "default.ArrayOptions")

No documentation available

*   [concurrency](.././stream/~/default.ArrayOptions#property_concurrency)
*   [signal](.././stream/~/default.ArrayOptions#property_signal)

I

[default.DuplexOptions](.././stream/~/default.DuplexOptions "default.DuplexOptions")

No documentation available

*   [allowHalfOpen](.././stream/~/default.DuplexOptions#property_allowhalfopen)
*   [readableHighWaterMark](.././stream/~/default.DuplexOptions#property_readablehighwatermark)
*   [readableObjectMode](.././stream/~/default.DuplexOptions#property_readableobjectmode)
*   [writableCorked](.././stream/~/default.DuplexOptions#property_writablecorked)
*   [writableHighWaterMark](.././stream/~/default.DuplexOptions#property_writablehighwatermark)
*   [writableObjectMode](.././stream/~/default.DuplexOptions#property_writableobjectmode)

I

[default.FinishedOptions](.././stream/~/default.FinishedOptions "default.FinishedOptions")

No documentation available

*   [error](.././stream/~/default.FinishedOptions#property_error)
*   [readable](.././stream/~/default.FinishedOptions#property_readable)
*   [writable](.././stream/~/default.FinishedOptions#property_writable)

I

[default.Pipe](.././stream/~/default.Pipe "default.Pipe")

No documentation available

*   [close](.././stream/~/default.Pipe#method_close_0)
*   [hasRef](.././stream/~/default.Pipe#method_hasref_0)
*   [ref](.././stream/~/default.Pipe#method_ref_0)
*   [unref](.././stream/~/default.Pipe#method_unref_0)

I

[default.PipelineOptions](.././stream/~/default.PipelineOptions "default.PipelineOptions")

No documentation available

*   [end](.././stream/~/default.PipelineOptions#property_end)
*   [signal](.././stream/~/default.PipelineOptions#property_signal)

I

[default.ReadableOptions](.././stream/~/default.ReadableOptions "default.ReadableOptions")

No documentation available

*   [encoding](.././stream/~/default.ReadableOptions#property_encoding)
*   [read](.././stream/~/default.ReadableOptions#method_read_0)

I

[default.StreamOptions](.././stream/~/default.StreamOptions "default.StreamOptions")

No documentation available

*   [autoDestroy](.././stream/~/default.StreamOptions#property_autodestroy)
*   [construct](.././stream/~/default.StreamOptions#method_construct_0)
*   [destroy](.././stream/~/default.StreamOptions#method_destroy_0)
*   [emitClose](.././stream/~/default.StreamOptions#property_emitclose)
*   [highWaterMark](.././stream/~/default.StreamOptions#property_highwatermark)
*   [objectMode](.././stream/~/default.StreamOptions#property_objectmode)

I

[default.TransformOptions](.././stream/~/default.TransformOptions "default.TransformOptions")

No documentation available

*   [flush](.././stream/~/default.TransformOptions#method_flush_0)
*   [transform](.././stream/~/default.TransformOptions#method_transform_0)

I

[default.WritableOptions](.././stream/~/default.WritableOptions "default.WritableOptions")

No documentation available

*   [decodeStrings](.././stream/~/default.WritableOptions#property_decodestrings)
*   [defaultEncoding](.././stream/~/default.WritableOptions#property_defaultencoding)
*   [final](.././stream/~/default.WritableOptions#method_final_0)
*   [write](.././stream/~/default.WritableOptions#method_write_0)
*   [writev](.././stream/~/default.WritableOptions#method_writev_0)

I

[Stream.ArrayOptions](.././stream/~/Stream.ArrayOptions "Stream.ArrayOptions")

No documentation available

*   [concurrency](.././stream/~/Stream.ArrayOptions#property_concurrency)
*   [signal](.././stream/~/Stream.ArrayOptions#property_signal)

I

[Stream.DuplexOptions](.././stream/~/Stream.DuplexOptions "Stream.DuplexOptions")

No documentation available

*   [allowHalfOpen](.././stream/~/Stream.DuplexOptions#property_allowhalfopen)
*   [readableHighWaterMark](.././stream/~/Stream.DuplexOptions#property_readablehighwatermark)
*   [readableObjectMode](.././stream/~/Stream.DuplexOptions#property_readableobjectmode)
*   [writableCorked](.././stream/~/Stream.DuplexOptions#property_writablecorked)
*   [writableHighWaterMark](.././stream/~/Stream.DuplexOptions#property_writablehighwatermark)
*   [writableObjectMode](.././stream/~/Stream.DuplexOptions#property_writableobjectmode)

I

[Stream.FinishedOptions](.././stream/~/Stream.FinishedOptions "Stream.FinishedOptions")

No documentation available

*   [error](.././stream/~/Stream.FinishedOptions#property_error)
*   [readable](.././stream/~/Stream.FinishedOptions#property_readable)
*   [writable](.././stream/~/Stream.FinishedOptions#property_writable)

I

[Stream.Pipe](.././stream/~/Stream.Pipe "Stream.Pipe")

No documentation available

*   [close](.././stream/~/Stream.Pipe#method_close_0)
*   [hasRef](.././stream/~/Stream.Pipe#method_hasref_0)
*   [ref](.././stream/~/Stream.Pipe#method_ref_0)
*   [unref](.././stream/~/Stream.Pipe#method_unref_0)

I

[Stream.PipelineOptions](.././stream/~/Stream.PipelineOptions "Stream.PipelineOptions")

No documentation available

*   [end](.././stream/~/Stream.PipelineOptions#property_end)
*   [signal](.././stream/~/Stream.PipelineOptions#property_signal)

I

[Stream.ReadableOptions](.././stream/~/Stream.ReadableOptions "Stream.ReadableOptions")

No documentation available

*   [encoding](.././stream/~/Stream.ReadableOptions#property_encoding)
*   [read](.././stream/~/Stream.ReadableOptions#method_read_0)

I

[Stream.StreamOptions](.././stream/~/Stream.StreamOptions "Stream.StreamOptions")

No documentation available

*   [autoDestroy](.././stream/~/Stream.StreamOptions#property_autodestroy)
*   [construct](.././stream/~/Stream.StreamOptions#method_construct_0)
*   [destroy](.././stream/~/Stream.StreamOptions#method_destroy_0)
*   [emitClose](.././stream/~/Stream.StreamOptions#property_emitclose)
*   [highWaterMark](.././stream/~/Stream.StreamOptions#property_highwatermark)
*   [objectMode](.././stream/~/Stream.StreamOptions#property_objectmode)

I

[Stream.TransformOptions](.././stream/~/Stream.TransformOptions "Stream.TransformOptions")

No documentation available

*   [flush](.././stream/~/Stream.TransformOptions#method_flush_0)
*   [transform](.././stream/~/Stream.TransformOptions#method_transform_0)

I

[Stream.WritableOptions](.././stream/~/Stream.WritableOptions "Stream.WritableOptions")

No documentation available

*   [decodeStrings](.././stream/~/Stream.WritableOptions#property_decodestrings)
*   [defaultEncoding](.././stream/~/Stream.WritableOptions#property_defaultencoding)
*   [final](.././stream/~/Stream.WritableOptions#method_final_0)
*   [write](.././stream/~/Stream.WritableOptions#method_write_0)
*   [writev](.././stream/~/Stream.WritableOptions#method_writev_0)

### Type Aliases [#](<#Type Aliases>)

T

[ComposeFnParam](.././stream/~/ComposeFnParam "ComposeFnParam")

No documentation available

T

[default.PipelineCallback](.././stream/~/default.PipelineCallback "default.PipelineCallback")

No documentation available

T

[default.PipelineDestination](.././stream/~/default.PipelineDestination "default.PipelineDestination")

No documentation available

T

[default.PipelineDestinationIterableFunction](.././stream/~/default.PipelineDestinationIterableFunction "default.PipelineDestinationIterableFunction")

No documentation available

T

[default.PipelineDestinationPromiseFunction](.././stream/~/default.PipelineDestinationPromiseFunction "default.PipelineDestinationPromiseFunction")

No documentation available

T

[default.PipelinePromise](.././stream/~/default.PipelinePromise "default.PipelinePromise")

No documentation available

T

[default.PipelineSource](.././stream/~/default.PipelineSource "default.PipelineSource")

No documentation available

T

[default.PipelineSourceFunction](.././stream/~/default.PipelineSourceFunction "default.PipelineSourceFunction")

No documentation available

T

[default.PipelineTransform](.././stream/~/default.PipelineTransform "default.PipelineTransform")

No documentation available

T

[default.PipelineTransformSource](.././stream/~/default.PipelineTransformSource "default.PipelineTransformSource")

No documentation available

T

[default.TransformCallback](.././stream/~/default.TransformCallback "default.TransformCallback")

No documentation available

T

[Stream.PipelineCallback](.././stream/~/Stream.PipelineCallback "Stream.PipelineCallback")

No documentation available

T

[Stream.PipelineDestination](.././stream/~/Stream.PipelineDestination "Stream.PipelineDestination")

No documentation available

T

[Stream.PipelineDestinationIterableFunction](.././stream/~/Stream.PipelineDestinationIterableFunction "Stream.PipelineDestinationIterableFunction")

No documentation available

T

[Stream.PipelineDestinationPromiseFunction](.././stream/~/Stream.PipelineDestinationPromiseFunction "Stream.PipelineDestinationPromiseFunction")

No documentation available

T

[Stream.PipelinePromise](.././stream/~/Stream.PipelinePromise "Stream.PipelinePromise")

No documentation available

T

[Stream.PipelineSource](.././stream/~/Stream.PipelineSource "Stream.PipelineSource")

No documentation available

T

[Stream.PipelineSourceFunction](.././stream/~/Stream.PipelineSourceFunction "Stream.PipelineSourceFunction")

No documentation available

T

[Stream.PipelineTransform](.././stream/~/Stream.PipelineTransform "Stream.PipelineTransform")

No documentation available

T

[Stream.PipelineTransformSource](.././stream/~/Stream.PipelineTransformSource "Stream.PipelineTransformSource")

No documentation available

T

[Stream.TransformCallback](.././stream/~/Stream.TransformCallback "Stream.TransformCallback")

No documentation available
