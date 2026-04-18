---
title: "Streams - Web documentation"
source: "https://docs.deno.com/api/web/streams"
canonical_url: "https://docs.deno.com/api/web/streams"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:41.843Z"
content_hash: "fc6186e9ba4f106a40037aae00a8d8f079f3b012baa0b299396cc7145eb27ed5"
menu_path: ["Streams - Web documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/web/storage/index.md", "title": "Storage - Web documentation"}
nav_next: {"path": "deno/deno/api/web/temporal/index.md", "title": "404Sorry, couldn\u2019t find that page."}
---

### Interfaces [#](#Interfaces)

I

v

[ByteLengthQueuingStrategy](./././~/ByteLengthQueuingStrategy "ByteLengthQueuingStrategy")

No documentation available

*   [highWaterMark](./././~/ByteLengthQueuingStrategy#property_highwatermark)
*   [prototype](./././~/ByteLengthQueuingStrategy#property_prototype)
*   [size](./././~/ByteLengthQueuingStrategy#property_size)

I

v

[CompressionStream](./././~/CompressionStream "CompressionStream")

An API for compressing a stream of data.

*   [prototype](./././~/CompressionStream#property_prototype)
*   [readable](./././~/CompressionStream#property_readable)
*   [writable](./././~/CompressionStream#property_writable)

I

v

[CountQueuingStrategy](./././~/CountQueuingStrategy "CountQueuingStrategy")

This Streams API interface provides a built-in byte length queuing strategy that can be used when constructing streams.

*   [highWaterMark](./././~/CountQueuingStrategy#property_highwatermark)
*   [prototype](./././~/CountQueuingStrategy#property_prototype)
*   [size](./././~/CountQueuingStrategy#property_size)

I

v

[DecompressionStream](./././~/DecompressionStream "DecompressionStream")

An API for decompressing a stream of data.

*   [prototype](./././~/DecompressionStream#property_prototype)
*   [readable](./././~/DecompressionStream#property_readable)
*   [writable](./././~/DecompressionStream#property_writable)

I

[GenericTransformStream](./././~/GenericTransformStream "GenericTransformStream")

No documentation available

*   [readable](./././~/GenericTransformStream#property_readable)
*   [writable](./././~/GenericTransformStream#property_writable)

I

[QueuingStrategy](./././~/QueuingStrategy "QueuingStrategy")

No documentation available

*   [highWaterMark](./././~/QueuingStrategy#property_highwatermark)
*   [size](./././~/QueuingStrategy#property_size)

I

[QueuingStrategyInit](./././~/QueuingStrategyInit "QueuingStrategyInit")

No documentation available

*   [highWaterMark](./././~/QueuingStrategyInit#property_highwatermark)

I

[QueuingStrategySize](./././~/QueuingStrategySize "QueuingStrategySize")

No documentation available

I

v

[ReadableByteStreamController](./././~/ReadableByteStreamController "ReadableByteStreamController")

No documentation available

*   [byobRequest](./././~/ReadableByteStreamController#property_byobrequest)
*   [close](./././~/ReadableByteStreamController#method_close_0)
*   [desiredSize](./././~/ReadableByteStreamController#property_desiredsize)
*   [enqueue](./././~/ReadableByteStreamController#method_enqueue_0)
*   [error](./././~/ReadableByteStreamController#method_error_0)
*   [prototype](./././~/ReadableByteStreamController#property_prototype)

I

v

[ReadableStream](./././~/ReadableStream "ReadableStream")

This Streams API interface represents a readable stream of byte data. The Fetch API offers a concrete instance of a ReadableStream through the body property of a Response object.

*   [cancel](./././~/ReadableStream#method_cancel_0)
*   [from](./././~/ReadableStream#method_from_0)
*   [getReader](./././~/ReadableStream#method_getreader_0)
*   [locked](./././~/ReadableStream#property_locked)
*   [pipeThrough](./././~/ReadableStream#method_pipethrough_0)
*   [pipeTo](./././~/ReadableStream#method_pipeto_0)
*   [prototype](./././~/ReadableStream#property_prototype)
*   [tee](./././~/ReadableStream#method_tee_0)
*   [values](./././~/ReadableStream#method_values_0)

I

v

[ReadableStreamBYOBReader](./././~/ReadableStreamBYOBReader "ReadableStreamBYOBReader")

No documentation available

*   [prototype](./././~/ReadableStreamBYOBReader#property_prototype)
*   [read](./././~/ReadableStreamBYOBReader#method_read_0)
*   [releaseLock](./././~/ReadableStreamBYOBReader#method_releaselock_0)

I

[ReadableStreamBYOBReaderReadOptions](./././~/ReadableStreamBYOBReaderReadOptions "ReadableStreamBYOBReaderReadOptions")

No documentation available

*   [min](./././~/ReadableStreamBYOBReaderReadOptions#property_min)

I

v

[ReadableStreamBYOBRequest](./././~/ReadableStreamBYOBRequest "ReadableStreamBYOBRequest")

No documentation available

*   [prototype](./././~/ReadableStreamBYOBRequest#property_prototype)
*   [respond](./././~/ReadableStreamBYOBRequest#method_respond_0)
*   [respondWithNewView](./././~/ReadableStreamBYOBRequest#method_respondwithnewview_0)
*   [view](./././~/ReadableStreamBYOBRequest#property_view)

I

v

[ReadableStreamDefaultController](./././~/ReadableStreamDefaultController "ReadableStreamDefaultController")

No documentation available

*   [close](./././~/ReadableStreamDefaultController#method_close_0)
*   [desiredSize](./././~/ReadableStreamDefaultController#property_desiredsize)
*   [enqueue](./././~/ReadableStreamDefaultController#method_enqueue_0)
*   [error](./././~/ReadableStreamDefaultController#method_error_0)
*   [prototype](./././~/ReadableStreamDefaultController#property_prototype)

I

v

[ReadableStreamDefaultReader](./././~/ReadableStreamDefaultReader "ReadableStreamDefaultReader")

No documentation available

*   [prototype](./././~/ReadableStreamDefaultReader#property_prototype)
*   [read](./././~/ReadableStreamDefaultReader#method_read_0)
*   [releaseLock](./././~/ReadableStreamDefaultReader#method_releaselock_0)

I

[ReadableStreamGenericReader](./././~/ReadableStreamGenericReader "ReadableStreamGenericReader")

No documentation available

*   [cancel](./././~/ReadableStreamGenericReader#method_cancel_0)
*   [closed](./././~/ReadableStreamGenericReader#property_closed)

I

[ReadableStreamGetReaderOptions](./././~/ReadableStreamGetReaderOptions "ReadableStreamGetReaderOptions")

No documentation available

*   [mode](./././~/ReadableStreamGetReaderOptions#property_mode)

I

[ReadableStreamIteratorOptions](./././~/ReadableStreamIteratorOptions "ReadableStreamIteratorOptions")

No documentation available

*   [preventCancel](./././~/ReadableStreamIteratorOptions#property_preventcancel)

I

[ReadableStreamReadDoneResult](./././~/ReadableStreamReadDoneResult "ReadableStreamReadDoneResult")

No documentation available

*   [done](./././~/ReadableStreamReadDoneResult#property_done)
*   [value](./././~/ReadableStreamReadDoneResult#property_value)

I

[ReadableStreamReadValueResult](./././~/ReadableStreamReadValueResult "ReadableStreamReadValueResult")

No documentation available

*   [done](./././~/ReadableStreamReadValueResult#property_done)
*   [value](./././~/ReadableStreamReadValueResult#property_value)

I

[ReadableWritablePair](./././~/ReadableWritablePair "ReadableWritablePair")

No documentation available

*   [readable](./././~/ReadableWritablePair#property_readable)
*   [writable](./././~/ReadableWritablePair#property_writable)

I

[StreamPipeOptions](./././~/StreamPipeOptions "StreamPipeOptions")

No documentation available

*   [preventAbort](./././~/StreamPipeOptions#property_preventabort)
*   [preventCancel](./././~/StreamPipeOptions#property_preventcancel)
*   [preventClose](./././~/StreamPipeOptions#property_preventclose)
*   [signal](./././~/StreamPipeOptions#property_signal)

I

[Transformer](./././~/Transformer "Transformer")

No documentation available

*   [cancel](./././~/Transformer#property_cancel)
*   [flush](./././~/Transformer#property_flush)
*   [readableType](./././~/Transformer#property_readabletype)
*   [start](./././~/Transformer#property_start)
*   [transform](./././~/Transformer#property_transform)
*   [writableType](./././~/Transformer#property_writabletype)

I

[TransformerCancelCallback](./././~/TransformerCancelCallback "TransformerCancelCallback")

No documentation available

I

[TransformerFlushCallback](./././~/TransformerFlushCallback "TransformerFlushCallback")

No documentation available

I

[TransformerStartCallback](./././~/TransformerStartCallback "TransformerStartCallback")

No documentation available

I

[TransformerTransformCallback](./././~/TransformerTransformCallback "TransformerTransformCallback")

No documentation available

I

v

[TransformStream](./././~/TransformStream "TransformStream")

No documentation available

*   [prototype](./././~/TransformStream#property_prototype)
*   [readable](./././~/TransformStream#property_readable)
*   [writable](./././~/TransformStream#property_writable)

I

v

[TransformStreamDefaultController](./././~/TransformStreamDefaultController "TransformStreamDefaultController")

No documentation available

*   [desiredSize](./././~/TransformStreamDefaultController#property_desiredsize)
*   [enqueue](./././~/TransformStreamDefaultController#method_enqueue_0)
*   [error](./././~/TransformStreamDefaultController#method_error_0)
*   [prototype](./././~/TransformStreamDefaultController#property_prototype)
*   [terminate](./././~/TransformStreamDefaultController#method_terminate_0)

I

[UnderlyingByteSource](./././~/UnderlyingByteSource "UnderlyingByteSource")

No documentation available

*   [autoAllocateChunkSize](./././~/UnderlyingByteSource#property_autoallocatechunksize)
*   [cancel](./././~/UnderlyingByteSource#property_cancel)
*   [pull](./././~/UnderlyingByteSource#property_pull)
*   [start](./././~/UnderlyingByteSource#property_start)
*   [type](./././~/UnderlyingByteSource#property_type)

I

[UnderlyingDefaultSource](./././~/UnderlyingDefaultSource "UnderlyingDefaultSource")

No documentation available

*   [cancel](./././~/UnderlyingDefaultSource#property_cancel)
*   [pull](./././~/UnderlyingDefaultSource#property_pull)
*   [start](./././~/UnderlyingDefaultSource#property_start)
*   [type](./././~/UnderlyingDefaultSource#property_type)

I

[UnderlyingSink](./././~/UnderlyingSink "UnderlyingSink")

No documentation available

*   [abort](./././~/UnderlyingSink#property_abort)
*   [close](./././~/UnderlyingSink#property_close)
*   [start](./././~/UnderlyingSink#property_start)
*   [type](./././~/UnderlyingSink#property_type)
*   [write](./././~/UnderlyingSink#property_write)

I

[UnderlyingSinkAbortCallback](./././~/UnderlyingSinkAbortCallback "UnderlyingSinkAbortCallback")

No documentation available

I

[UnderlyingSinkCloseCallback](./././~/UnderlyingSinkCloseCallback "UnderlyingSinkCloseCallback")

No documentation available

I

[UnderlyingSinkStartCallback](./././~/UnderlyingSinkStartCallback "UnderlyingSinkStartCallback")

No documentation available

I

[UnderlyingSinkWriteCallback](./././~/UnderlyingSinkWriteCallback "UnderlyingSinkWriteCallback")

No documentation available

I

[UnderlyingSource](./././~/UnderlyingSource "UnderlyingSource")

No documentation available

*   [autoAllocateChunkSize](./././~/UnderlyingSource#property_autoallocatechunksize)
*   [cancel](./././~/UnderlyingSource#property_cancel)
*   [pull](./././~/UnderlyingSource#property_pull)
*   [start](./././~/UnderlyingSource#property_start)
*   [type](./././~/UnderlyingSource#property_type)

I

[UnderlyingSourceCancelCallback](./././~/UnderlyingSourceCancelCallback "UnderlyingSourceCancelCallback")

No documentation available

I

[UnderlyingSourcePullCallback](./././~/UnderlyingSourcePullCallback "UnderlyingSourcePullCallback")

No documentation available

I

[UnderlyingSourceStartCallback](./././~/UnderlyingSourceStartCallback "UnderlyingSourceStartCallback")

No documentation available

I

v

[WritableStream](./././~/WritableStream "WritableStream")

This Streams API interface provides a standard abstraction for writing streaming data to a destination, known as a sink. This object comes with built-in backpressure and queuing.

*   [abort](./././~/WritableStream#method_abort_0)
*   [close](./././~/WritableStream#method_close_0)
*   [getWriter](./././~/WritableStream#method_getwriter_0)
*   [locked](./././~/WritableStream#property_locked)
*   [prototype](./././~/WritableStream#property_prototype)

I

v

[WritableStreamDefaultController](./././~/WritableStreamDefaultController "WritableStreamDefaultController")

This Streams API interface represents a controller allowing control of a WritableStream's state. When constructing a WritableStream, the underlying sink is given a corresponding WritableStreamDefaultController instance to manipulate.

*   [error](./././~/WritableStreamDefaultController#method_error_0)
*   [prototype](./././~/WritableStreamDefaultController#property_prototype)
*   [signal](./././~/WritableStreamDefaultController#property_signal)

I

v

[WritableStreamDefaultWriter](./././~/WritableStreamDefaultWriter "WritableStreamDefaultWriter")

This Streams API interface is the object returned by WritableStream.getWriter() and once created locks the < writer to the WritableStream ensuring that no other streams can write to the underlying sink.

*   [abort](./././~/WritableStreamDefaultWriter#method_abort_0)
*   [close](./././~/WritableStreamDefaultWriter#method_close_0)
*   [closed](./././~/WritableStreamDefaultWriter#property_closed)
*   [desiredSize](./././~/WritableStreamDefaultWriter#property_desiredsize)
*   [prototype](./././~/WritableStreamDefaultWriter#property_prototype)
*   [ready](./././~/WritableStreamDefaultWriter#property_ready)
*   [releaseLock](./././~/WritableStreamDefaultWriter#method_releaselock_0)
*   [write](./././~/WritableStreamDefaultWriter#method_write_0)

### Type Aliases [#](<#Type Aliases>)

T

[CompressionFormat](./././~/CompressionFormat "CompressionFormat")

No documentation available

T

[ReadableStreamController](./././~/ReadableStreamController "ReadableStreamController")

No documentation available

T

[ReadableStreamReader](./././~/ReadableStreamReader "ReadableStreamReader")

No documentation available

T

[ReadableStreamReaderMode](./././~/ReadableStreamReaderMode "ReadableStreamReaderMode")

No documentation available

T

[ReadableStreamReadResult](./././~/ReadableStreamReadResult "ReadableStreamReadResult")

No documentation available

T

[ReadableStreamType](./././~/ReadableStreamType "ReadableStreamType")

No documentation available


