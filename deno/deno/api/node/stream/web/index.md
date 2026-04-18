---
title: "stream/web - Node documentation"
source: "https://docs.deno.com/api/node/stream/web/"
canonical_url: "https://docs.deno.com/api/node/stream/web/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:00.578Z"
content_hash: "8324303d62ea3e0e8f6555e1a93f779aa2c3f00739b09d27333983d2c1798368"
menu_path: ["stream/web - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/stream/promises/index.md", "title": "stream/promises - Node documentation"}
nav_next: {"path": "deno/deno/api/node/string_decoder/index.md", "title": "string_decoder - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:stream/web";
```

### Interfaces [#](#Interfaces)

I

v

[ByteLengthQueuingStrategy](../.././stream/web/~/ByteLengthQueuingStrategy "ByteLengthQueuingStrategy")

This Streams API interface provides a built-in byte length queuing strategy that can be used when constructing streams.

*   [highWaterMark](../.././stream/web/~/ByteLengthQueuingStrategy#property_highwatermark)
*   [prototype](../.././stream/web/~/ByteLengthQueuingStrategy#property_prototype)
*   [size](../.././stream/web/~/ByteLengthQueuingStrategy#property_size)

I

v

[CompressionStream](../.././stream/web/~/CompressionStream "CompressionStream")

No documentation available

*   [prototype](../.././stream/web/~/CompressionStream#property_prototype)
*   [readable](../.././stream/web/~/CompressionStream#property_readable)
*   [writable](../.././stream/web/~/CompressionStream#property_writable)

I

v

[CountQueuingStrategy](../.././stream/web/~/CountQueuingStrategy "CountQueuingStrategy")

This Streams API interface provides a built-in byte length queuing strategy that can be used when constructing streams.

*   [highWaterMark](../.././stream/web/~/CountQueuingStrategy#property_highwatermark)
*   [prototype](../.././stream/web/~/CountQueuingStrategy#property_prototype)
*   [size](../.././stream/web/~/CountQueuingStrategy#property_size)

I

v

[DecompressionStream](../.././stream/web/~/DecompressionStream "DecompressionStream")

No documentation available

*   [prototype](../.././stream/web/~/DecompressionStream#property_prototype)
*   [readable](../.././stream/web/~/DecompressionStream#property_readable)
*   [writable](../.././stream/web/~/DecompressionStream#property_writable)

I

[QueuingStrategy](../.././stream/web/~/QueuingStrategy "QueuingStrategy")

No documentation available

*   [highWaterMark](../.././stream/web/~/QueuingStrategy#property_highwatermark)
*   [size](../.././stream/web/~/QueuingStrategy#property_size)

I

[QueuingStrategyInit](../.././stream/web/~/QueuingStrategyInit "QueuingStrategyInit")

No documentation available

*   [highWaterMark](../.././stream/web/~/QueuingStrategyInit#property_highwatermark)

I

[QueuingStrategySize](../.././stream/web/~/QueuingStrategySize "QueuingStrategySize")

No documentation available

I

v

[ReadableByteStreamController](../.././stream/web/~/ReadableByteStreamController "ReadableByteStreamController")

No documentation available

*   [byobRequest](../.././stream/web/~/ReadableByteStreamController#property_byobrequest)
*   [close](../.././stream/web/~/ReadableByteStreamController#method_close_0)
*   [desiredSize](../.././stream/web/~/ReadableByteStreamController#property_desiredsize)
*   [enqueue](../.././stream/web/~/ReadableByteStreamController#method_enqueue_0)
*   [error](../.././stream/web/~/ReadableByteStreamController#method_error_0)
*   [prototype](../.././stream/web/~/ReadableByteStreamController#property_prototype)

I

[ReadableByteStreamControllerCallback](../.././stream/web/~/ReadableByteStreamControllerCallback "ReadableByteStreamControllerCallback")

No documentation available

I

v

[ReadableStream](../.././stream/web/~/ReadableStream "ReadableStream")

This Streams API interface represents a readable stream of byte data.

*   [cancel](../.././stream/web/~/ReadableStream#method_cancel_0)
*   [from](../.././stream/web/~/ReadableStream#method_from_0)
*   [getReader](../.././stream/web/~/ReadableStream#method_getreader_0)
*   [locked](../.././stream/web/~/ReadableStream#property_locked)
*   [pipeThrough](../.././stream/web/~/ReadableStream#method_pipethrough_0)
*   [pipeTo](../.././stream/web/~/ReadableStream#method_pipeto_0)
*   [prototype](../.././stream/web/~/ReadableStream#property_prototype)
*   [tee](../.././stream/web/~/ReadableStream#method_tee_0)
*   [values](../.././stream/web/~/ReadableStream#method_values_0)

I

[ReadableStreamAsyncIterator](../.././stream/web/~/ReadableStreamAsyncIterator "ReadableStreamAsyncIterator")

No documentation available

I

v

[ReadableStreamBYOBReader](../.././stream/web/~/ReadableStreamBYOBReader "ReadableStreamBYOBReader")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBReader)

*   [prototype](../.././stream/web/~/ReadableStreamBYOBReader#property_prototype)
*   [read](../.././stream/web/~/ReadableStreamBYOBReader#method_read_0)
*   [releaseLock](../.././stream/web/~/ReadableStreamBYOBReader#method_releaselock_0)

I

v

[ReadableStreamBYOBRequest](../.././stream/web/~/ReadableStreamBYOBRequest "ReadableStreamBYOBRequest")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBRequest)

*   [prototype](../.././stream/web/~/ReadableStreamBYOBRequest#property_prototype)
*   [respond](../.././stream/web/~/ReadableStreamBYOBRequest#method_respond_0)
*   [respondWithNewView](../.././stream/web/~/ReadableStreamBYOBRequest#method_respondwithnewview_0)
*   [view](../.././stream/web/~/ReadableStreamBYOBRequest#property_view)

I

v

[ReadableStreamDefaultController](../.././stream/web/~/ReadableStreamDefaultController "ReadableStreamDefaultController")

No documentation available

*   [close](../.././stream/web/~/ReadableStreamDefaultController#method_close_0)
*   [desiredSize](../.././stream/web/~/ReadableStreamDefaultController#property_desiredsize)
*   [enqueue](../.././stream/web/~/ReadableStreamDefaultController#method_enqueue_0)
*   [error](../.././stream/web/~/ReadableStreamDefaultController#method_error_0)
*   [prototype](../.././stream/web/~/ReadableStreamDefaultController#property_prototype)

I

v

[ReadableStreamDefaultReader](../.././stream/web/~/ReadableStreamDefaultReader "ReadableStreamDefaultReader")

No documentation available

*   [prototype](../.././stream/web/~/ReadableStreamDefaultReader#property_prototype)
*   [read](../.././stream/web/~/ReadableStreamDefaultReader#method_read_0)
*   [releaseLock](../.././stream/web/~/ReadableStreamDefaultReader#method_releaselock_0)

I

[ReadableStreamErrorCallback](../.././stream/web/~/ReadableStreamErrorCallback "ReadableStreamErrorCallback")

No documentation available

I

[ReadableStreamGenericReader](../.././stream/web/~/ReadableStreamGenericReader "ReadableStreamGenericReader")

No documentation available

*   [cancel](../.././stream/web/~/ReadableStreamGenericReader#method_cancel_0)
*   [closed](../.././stream/web/~/ReadableStreamGenericReader#property_closed)

I

[ReadableStreamGetReaderOptions](../.././stream/web/~/ReadableStreamGetReaderOptions "ReadableStreamGetReaderOptions")

No documentation available

*   [mode](../.././stream/web/~/ReadableStreamGetReaderOptions#property_mode)

I

[ReadableStreamReadDoneResult](../.././stream/web/~/ReadableStreamReadDoneResult "ReadableStreamReadDoneResult")

No documentation available

*   [done](../.././stream/web/~/ReadableStreamReadDoneResult#property_done)
*   [value](../.././stream/web/~/ReadableStreamReadDoneResult#property_value)

I

[ReadableStreamReadValueResult](../.././stream/web/~/ReadableStreamReadValueResult "ReadableStreamReadValueResult")

No documentation available

*   [done](../.././stream/web/~/ReadableStreamReadValueResult#property_done)
*   [value](../.././stream/web/~/ReadableStreamReadValueResult#property_value)

I

[ReadableWritablePair](../.././stream/web/~/ReadableWritablePair "ReadableWritablePair")

No documentation available

*   [readable](../.././stream/web/~/ReadableWritablePair#property_readable)
*   [writable](../.././stream/web/~/ReadableWritablePair#property_writable)

I

[StreamPipeOptions](../.././stream/web/~/StreamPipeOptions "StreamPipeOptions")

No documentation available

*   [preventAbort](../.././stream/web/~/StreamPipeOptions#property_preventabort)
*   [preventCancel](../.././stream/web/~/StreamPipeOptions#property_preventcancel)
*   [preventClose](../.././stream/web/~/StreamPipeOptions#property_preventclose)
*   [signal](../.././stream/web/~/StreamPipeOptions#property_signal)

I

[TextDecoderOptions](../.././stream/web/~/TextDecoderOptions "TextDecoderOptions")

No documentation available

*   [fatal](../.././stream/web/~/TextDecoderOptions#property_fatal)
*   [ignoreBOM](../.././stream/web/~/TextDecoderOptions#property_ignorebom)

I

v

[TextDecoderStream](../.././stream/web/~/TextDecoderStream "TextDecoderStream")

No documentation available

*   [encoding](../.././stream/web/~/TextDecoderStream#property_encoding)
*   [fatal](../.././stream/web/~/TextDecoderStream#property_fatal)
*   [ignoreBOM](../.././stream/web/~/TextDecoderStream#property_ignorebom)
*   [prototype](../.././stream/web/~/TextDecoderStream#property_prototype)
*   [readable](../.././stream/web/~/TextDecoderStream#property_readable)
*   [writable](../.././stream/web/~/TextDecoderStream#property_writable)

I

v

[TextEncoderStream](../.././stream/web/~/TextEncoderStream "TextEncoderStream")

No documentation available

*   [encoding](../.././stream/web/~/TextEncoderStream#property_encoding)
*   [prototype](../.././stream/web/~/TextEncoderStream#property_prototype)
*   [readable](../.././stream/web/~/TextEncoderStream#property_readable)
*   [writable](../.././stream/web/~/TextEncoderStream#property_writable)

I

[Transformer](../.././stream/web/~/Transformer "Transformer")

No documentation available

*   [flush](../.././stream/web/~/Transformer#property_flush)
*   [readableType](../.././stream/web/~/Transformer#property_readabletype)
*   [start](../.././stream/web/~/Transformer#property_start)
*   [transform](../.././stream/web/~/Transformer#property_transform)
*   [writableType](../.././stream/web/~/Transformer#property_writabletype)

I

[TransformerFlushCallback](../.././stream/web/~/TransformerFlushCallback "TransformerFlushCallback")

No documentation available

I

[TransformerStartCallback](../.././stream/web/~/TransformerStartCallback "TransformerStartCallback")

No documentation available

I

[TransformerTransformCallback](../.././stream/web/~/TransformerTransformCallback "TransformerTransformCallback")

No documentation available

I

v

[TransformStream](../.././stream/web/~/TransformStream "TransformStream")

No documentation available

*   [prototype](../.././stream/web/~/TransformStream#property_prototype)
*   [readable](../.././stream/web/~/TransformStream#property_readable)
*   [writable](../.././stream/web/~/TransformStream#property_writable)

I

v

[TransformStreamDefaultController](../.././stream/web/~/TransformStreamDefaultController "TransformStreamDefaultController")

No documentation available

*   [desiredSize](../.././stream/web/~/TransformStreamDefaultController#property_desiredsize)
*   [enqueue](../.././stream/web/~/TransformStreamDefaultController#method_enqueue_0)
*   [error](../.././stream/web/~/TransformStreamDefaultController#method_error_0)
*   [prototype](../.././stream/web/~/TransformStreamDefaultController#property_prototype)
*   [terminate](../.././stream/web/~/TransformStreamDefaultController#method_terminate_0)

I

[UnderlyingByteSource](../.././stream/web/~/UnderlyingByteSource "UnderlyingByteSource")

No documentation available

*   [autoAllocateChunkSize](../.././stream/web/~/UnderlyingByteSource#property_autoallocatechunksize)
*   [cancel](../.././stream/web/~/UnderlyingByteSource#property_cancel)
*   [pull](../.././stream/web/~/UnderlyingByteSource#property_pull)
*   [start](../.././stream/web/~/UnderlyingByteSource#property_start)
*   [type](../.././stream/web/~/UnderlyingByteSource#property_type)

I

[UnderlyingSink](../.././stream/web/~/UnderlyingSink "UnderlyingSink")

No documentation available

*   [abort](../.././stream/web/~/UnderlyingSink#property_abort)
*   [close](../.././stream/web/~/UnderlyingSink#property_close)
*   [start](../.././stream/web/~/UnderlyingSink#property_start)
*   [type](../.././stream/web/~/UnderlyingSink#property_type)
*   [write](../.././stream/web/~/UnderlyingSink#property_write)

I

[UnderlyingSinkAbortCallback](../.././stream/web/~/UnderlyingSinkAbortCallback "UnderlyingSinkAbortCallback")

No documentation available

I

[UnderlyingSinkCloseCallback](../.././stream/web/~/UnderlyingSinkCloseCallback "UnderlyingSinkCloseCallback")

No documentation available

I

[UnderlyingSinkStartCallback](../.././stream/web/~/UnderlyingSinkStartCallback "UnderlyingSinkStartCallback")

No documentation available

I

[UnderlyingSinkWriteCallback](../.././stream/web/~/UnderlyingSinkWriteCallback "UnderlyingSinkWriteCallback")

No documentation available

I

[UnderlyingSource](../.././stream/web/~/UnderlyingSource "UnderlyingSource")

No documentation available

*   [cancel](../.././stream/web/~/UnderlyingSource#property_cancel)
*   [pull](../.././stream/web/~/UnderlyingSource#property_pull)
*   [start](../.././stream/web/~/UnderlyingSource#property_start)
*   [type](../.././stream/web/~/UnderlyingSource#property_type)

I

[UnderlyingSourceCancelCallback](../.././stream/web/~/UnderlyingSourceCancelCallback "UnderlyingSourceCancelCallback")

No documentation available

I

[UnderlyingSourcePullCallback](../.././stream/web/~/UnderlyingSourcePullCallback "UnderlyingSourcePullCallback")

No documentation available

I

[UnderlyingSourceStartCallback](../.././stream/web/~/UnderlyingSourceStartCallback "UnderlyingSourceStartCallback")

No documentation available

I

v

[WritableStream](../.././stream/web/~/WritableStream "WritableStream")

This Streams API interface provides a standard abstraction for writing streaming data to a destination, known as a sink. This object comes with built-in back pressure and queuing.

*   [abort](../.././stream/web/~/WritableStream#method_abort_0)
*   [close](../.././stream/web/~/WritableStream#method_close_0)
*   [getWriter](../.././stream/web/~/WritableStream#method_getwriter_0)
*   [locked](../.././stream/web/~/WritableStream#property_locked)
*   [prototype](../.././stream/web/~/WritableStream#property_prototype)

I

v

[WritableStreamDefaultController](../.././stream/web/~/WritableStreamDefaultController "WritableStreamDefaultController")

This Streams API interface represents a controller allowing control of a WritableStream's state. When constructing a WritableStream, the underlying sink is given a corresponding WritableStreamDefaultController instance to manipulate.

*   [error](../.././stream/web/~/WritableStreamDefaultController#method_error_0)
*   [prototype](../.././stream/web/~/WritableStreamDefaultController#property_prototype)

I

v

[WritableStreamDefaultWriter](../.././stream/web/~/WritableStreamDefaultWriter "WritableStreamDefaultWriter")

This Streams API interface is the object returned by WritableStream.getWriter() and once created locks the < writer to the WritableStream ensuring that no other streams can write to the underlying sink.

*   [abort](../.././stream/web/~/WritableStreamDefaultWriter#method_abort_0)
*   [close](../.././stream/web/~/WritableStreamDefaultWriter#method_close_0)
*   [closed](../.././stream/web/~/WritableStreamDefaultWriter#property_closed)
*   [desiredSize](../.././stream/web/~/WritableStreamDefaultWriter#property_desiredsize)
*   [prototype](../.././stream/web/~/WritableStreamDefaultWriter#property_prototype)
*   [ready](../.././stream/web/~/WritableStreamDefaultWriter#property_ready)
*   [releaseLock](../.././stream/web/~/WritableStreamDefaultWriter#method_releaselock_0)
*   [write](../.././stream/web/~/WritableStreamDefaultWriter#method_write_0)

### Type Aliases [#](<#Type Aliases>)

T

[BufferSource](../.././stream/web/~/BufferSource "BufferSource")

No documentation available

T

[ReadableStreamController](../.././stream/web/~/ReadableStreamController "ReadableStreamController")

No documentation available

T

[ReadableStreamReader](../.././stream/web/~/ReadableStreamReader "ReadableStreamReader")

No documentation available

T

[ReadableStreamReaderMode](../.././stream/web/~/ReadableStreamReaderMode "ReadableStreamReaderMode")

No documentation available

T

[ReadableStreamReadResult](../.././stream/web/~/ReadableStreamReadResult "ReadableStreamReadResult")

No documentation available

