---
title: "zlib - Node documentation"
source: "https://docs.deno.com/api/node/zlib/"
canonical_url: "https://docs.deno.com/api/node/zlib/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:44.889Z"
content_hash: "41ea391255273df50053b4e5809ba86c77301c8c91214b53f049ffe80d153457"
menu_path: ["zlib - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/worker_threads/index.md", "title": "worker_threads - Node documentation"}
nav_next: {"path": "deno/deno/api/web/index.md", "title": "Web Platform APIs"}
---

### Usage in Deno

```typescript
import * as mod from "node:zlib";
```

The `node:zlib` module provides compression functionality implemented using Gzip, Deflate/Inflate, and Brotli.

To access it:

```js
import zlib from 'node:zlib';
```

Compression and decompression are built around the Node.js [Streams API](https://nodejs.org/docs/latest-v22.x/api/stream.html).

Compressing or decompressing a stream (such as a file) can be accomplished by piping the source stream through a `zlib` `Transform` stream into a destination stream:

```js
import { createGzip } from 'node:zlib';
import { pipeline } from 'node:stream';
import {
  createReadStream,
  createWriteStream,
} from 'node:fs';

const gzip = createGzip();
const source = createReadStream('input.txt');
const destination = createWriteStream('input.txt.gz');

pipeline(source, gzip, destination, (err) => {
  if (err) {
    console.error('An error occurred:', err);
    process.exitCode = 1;
  }
});

// Or, Promisified

import { promisify } from 'node:util';
const pipe = promisify(pipeline);

async function do_gzip(input, output) {
  const gzip = createGzip();
  const source = createReadStream(input);
  const destination = createWriteStream(output);
  await pipe(source, gzip, destination);
}

do_gzip('input.txt', 'input.txt.gz')
  .catch((err) => {
    console.error('An error occurred:', err);
    process.exitCode = 1;
  });
```

It is also possible to compress or decompress data in a single step:

```js
import { deflate, unzip } from 'node:zlib';

const input = '.................................';
deflate(input, (err, buffer) => {
  if (err) {
    console.error('An error occurred:', err);
    process.exitCode = 1;
  }
  console.log(buffer.toString('base64'));
});

const buffer = Buffer.from('eJzT0yMAAGTvBe8=', 'base64');
unzip(buffer, (err, buffer) => {
  if (err) {
    console.error('An error occurred:', err);
    process.exitCode = 1;
  }
  console.log(buffer.toString());
});

// Or, Promisified

import { promisify } from 'node:util';
const do_unzip = promisify(unzip);

do_unzip(buffer)
  .then((buf) => console.log(buf.toString()))
  .catch((err) => {
    console.error('An error occurred:', err);
    process.exitCode = 1;
  });
```

### Functions [#](#Functions)

f

[brotliCompress](.././zlib/~/brotliCompress "brotliCompress")

No documentation available

f

[brotliCompressSync](.././zlib/~/brotliCompressSync "brotliCompressSync")

Compress a chunk of data with `BrotliCompress`.

f

[brotliDecompress](.././zlib/~/brotliDecompress "brotliDecompress")

No documentation available

f

[brotliDecompressSync](.././zlib/~/brotliDecompressSync "brotliDecompressSync")

Decompress a chunk of data with `BrotliDecompress`.

f

[crc32](.././zlib/~/crc32 "crc32")

Computes a 32-bit [Cyclic Redundancy Check](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) checksum of `data`. If `value` is specified, it is used as the starting value of the checksum, otherwise, 0 is used as the starting value.

f

[createBrotliCompress](.././zlib/~/createBrotliCompress "createBrotliCompress")

Creates and returns a new `BrotliCompress` object.

f

[createBrotliDecompress](.././zlib/~/createBrotliDecompress "createBrotliDecompress")

Creates and returns a new `BrotliDecompress` object.

f

[createDeflate](.././zlib/~/createDeflate "createDeflate")

Creates and returns a new `Deflate` object.

f

[createDeflateRaw](.././zlib/~/createDeflateRaw "createDeflateRaw")

Creates and returns a new `DeflateRaw` object.

f

[createGunzip](.././zlib/~/createGunzip "createGunzip")

Creates and returns a new `Gunzip` object.

f

[createGzip](.././zlib/~/createGzip "createGzip")

Creates and returns a new `Gzip` object. See `example`.

f

[createInflate](.././zlib/~/createInflate "createInflate")

Creates and returns a new `Inflate` object.

f

[createInflateRaw](.././zlib/~/createInflateRaw "createInflateRaw")

Creates and returns a new `InflateRaw` object.

f

[createUnzip](.././zlib/~/createUnzip "createUnzip")

Creates and returns a new `Unzip` object.

f

[deflate](.././zlib/~/deflate "deflate")

No documentation available

f

[deflateRaw](.././zlib/~/deflateRaw "deflateRaw")

No documentation available

f

[deflateRawSync](.././zlib/~/deflateRawSync "deflateRawSync")

Compress a chunk of data with `DeflateRaw`.

f

[deflateSync](.././zlib/~/deflateSync "deflateSync")

Compress a chunk of data with `Deflate`.

f

[gunzip](.././zlib/~/gunzip "gunzip")

No documentation available

f

[gunzipSync](.././zlib/~/gunzipSync "gunzipSync")

Decompress a chunk of data with `Gunzip`.

f

[gzip](.././zlib/~/gzip "gzip")

No documentation available

f

[gzipSync](.././zlib/~/gzipSync "gzipSync")

Compress a chunk of data with `Gzip`.

f

[inflate](.././zlib/~/inflate "inflate")

No documentation available

f

[inflateRaw](.././zlib/~/inflateRaw "inflateRaw")

No documentation available

f

[inflateRawSync](.././zlib/~/inflateRawSync "inflateRawSync")

Decompress a chunk of data with `InflateRaw`.

f

[inflateSync](.././zlib/~/inflateSync "inflateSync")

Decompress a chunk of data with `Inflate`.

f

[unzip](.././zlib/~/unzip "unzip")

No documentation available

f

[unzipSync](.././zlib/~/unzipSync "unzipSync")

Decompress a chunk of data with `Unzip`.

### Interfaces [#](#Interfaces)

I

[BrotliCompress](.././zlib/~/BrotliCompress "BrotliCompress")

No documentation available

I

[BrotliDecompress](.././zlib/~/BrotliDecompress "BrotliDecompress")

No documentation available

I

[BrotliOptions](.././zlib/~/BrotliOptions "BrotliOptions")

No documentation available

*   [chunkSize](.././zlib/~/BrotliOptions#property_chunksize)
*   [finishFlush](.././zlib/~/BrotliOptions#property_finishflush)
*   [flush](.././zlib/~/BrotliOptions#property_flush)
*   [maxOutputLength](.././zlib/~/BrotliOptions#property_maxoutputlength)
*   [params](.././zlib/~/BrotliOptions#property_params)

I

[Deflate](.././zlib/~/Deflate "Deflate")

No documentation available

I

[DeflateRaw](.././zlib/~/DeflateRaw "DeflateRaw")

No documentation available

I

[Gunzip](.././zlib/~/Gunzip "Gunzip")

No documentation available

I

[Gzip](.././zlib/~/Gzip "Gzip")

No documentation available

I

[Inflate](.././zlib/~/Inflate "Inflate")

No documentation available

I

[InflateRaw](.././zlib/~/InflateRaw "InflateRaw")

No documentation available

I

[Unzip](.././zlib/~/Unzip "Unzip")

No documentation available

I

[Zlib](.././zlib/~/Zlib "Zlib")

No documentation available

*   [bytesRead](.././zlib/~/Zlib#property_bytesread)
*   [bytesWritten](.././zlib/~/Zlib#property_byteswritten)
*   [close](.././zlib/~/Zlib#method_close_0)
*   [flush](.././zlib/~/Zlib#method_flush_0)
*   [shell](.././zlib/~/Zlib#property_shell)

I

[ZlibOptions](.././zlib/~/ZlibOptions "ZlibOptions")

No documentation available

*   [chunkSize](.././zlib/~/ZlibOptions#property_chunksize)
*   [dictionary](.././zlib/~/ZlibOptions#property_dictionary)
*   [finishFlush](.././zlib/~/ZlibOptions#property_finishflush)
*   [flush](.././zlib/~/ZlibOptions#property_flush)
*   [info](.././zlib/~/ZlibOptions#property_info)
*   [level](.././zlib/~/ZlibOptions#property_level)
*   [maxOutputLength](.././zlib/~/ZlibOptions#property_maxoutputlength)
*   [memLevel](.././zlib/~/ZlibOptions#property_memlevel)
*   [strategy](.././zlib/~/ZlibOptions#property_strategy)
*   [windowBits](.././zlib/~/ZlibOptions#property_windowbits)

I

[ZlibParams](.././zlib/~/ZlibParams "ZlibParams")

No documentation available

*   [params](.././zlib/~/ZlibParams#method_params_0)

I

[ZlibReset](.././zlib/~/ZlibReset "ZlibReset")

No documentation available

*   [reset](.././zlib/~/ZlibReset#method_reset_0)

### Namespaces [#](#Namespaces)

N

[constants](.././zlib/~/constants "constants")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[CompressCallback](.././zlib/~/CompressCallback "CompressCallback")

No documentation available

T

[InputType](.././zlib/~/InputType "InputType")

No documentation available

### Variables [#](#Variables)

v

[constants.BROTLI\_DECODE](.././zlib/~/constants.BROTLI_DECODE "constants.BROTLI_DECODE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_BLOCK\_TYPE\_TREES](.././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_BLOCK_TYPE_TREES "constants.BROTLI_DECODER_ERROR_ALLOC_BLOCK_TYPE_TREES")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_CONTEXT\_MAP](.././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MAP "constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MAP")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_CONTEXT\_MODES](.././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MODES "constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MODES")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_RING\_BUFFER\_1](.././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_1 "constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_1")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_RING\_BUFFER\_2](.././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_2 "constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_2")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_TREE\_GROUPS](.././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_TREE_GROUPS "constants.BROTLI_DECODER_ERROR_ALLOC_TREE_GROUPS")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_DICTIONARY\_NOT\_SET](.././zlib/~/constants.BROTLI_DECODER_ERROR_DICTIONARY_NOT_SET "constants.BROTLI_DECODER_ERROR_DICTIONARY_NOT_SET")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_BLOCK\_LENGTH\_1](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_1 "constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_1")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_BLOCK\_LENGTH\_2](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_2 "constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_2")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_CL\_SPACE](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_CL_SPACE "constants.BROTLI_DECODER_ERROR_FORMAT_CL_SPACE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_CONTEXT\_MAP\_REPEAT](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_CONTEXT_MAP_REPEAT "constants.BROTLI_DECODER_ERROR_FORMAT_CONTEXT_MAP_REPEAT")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_DICTIONARY](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_DICTIONARY "constants.BROTLI_DECODER_ERROR_FORMAT_DICTIONARY")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_DISTANCE](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_DISTANCE "constants.BROTLI_DECODER_ERROR_FORMAT_DISTANCE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_EXUBERANT\_META\_NIBBLE](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_META_NIBBLE "constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_META_NIBBLE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_EXUBERANT\_NIBBLE](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_NIBBLE "constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_NIBBLE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_HUFFMAN\_SPACE](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_HUFFMAN_SPACE "constants.BROTLI_DECODER_ERROR_FORMAT_HUFFMAN_SPACE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_PADDING\_1](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_1 "constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_1")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_PADDING\_2](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_2 "constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_2")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_RESERVED](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_RESERVED "constants.BROTLI_DECODER_ERROR_FORMAT_RESERVED")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_SIMPLE\_HUFFMAN\_ALPHABET](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_ALPHABET "constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_ALPHABET")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_SIMPLE\_HUFFMAN\_SAME](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_SAME "constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_SAME")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_TRANSFORM](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_TRANSFORM "constants.BROTLI_DECODER_ERROR_FORMAT_TRANSFORM")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_WINDOW\_BITS](.././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_WINDOW_BITS "constants.BROTLI_DECODER_ERROR_FORMAT_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_INVALID\_ARGUMENTS](.././zlib/~/constants.BROTLI_DECODER_ERROR_INVALID_ARGUMENTS "constants.BROTLI_DECODER_ERROR_INVALID_ARGUMENTS")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_UNREACHABLE](.././zlib/~/constants.BROTLI_DECODER_ERROR_UNREACHABLE "constants.BROTLI_DECODER_ERROR_UNREACHABLE")

No documentation available

v

[constants.BROTLI\_DECODER\_NEEDS\_MORE\_INPUT](.././zlib/~/constants.BROTLI_DECODER_NEEDS_MORE_INPUT "constants.BROTLI_DECODER_NEEDS_MORE_INPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_NEEDS\_MORE\_OUTPUT](.././zlib/~/constants.BROTLI_DECODER_NEEDS_MORE_OUTPUT "constants.BROTLI_DECODER_NEEDS_MORE_OUTPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_NO\_ERROR](.././zlib/~/constants.BROTLI_DECODER_NO_ERROR "constants.BROTLI_DECODER_NO_ERROR")

No documentation available

v

[constants.BROTLI\_DECODER\_PARAM\_DISABLE\_RING\_BUFFER\_REALLOCATION](.././zlib/~/constants.BROTLI_DECODER_PARAM_DISABLE_RING_BUFFER_REALLOCATION "constants.BROTLI_DECODER_PARAM_DISABLE_RING_BUFFER_REALLOCATION")

No documentation available

v

[constants.BROTLI\_DECODER\_PARAM\_LARGE\_WINDOW](.././zlib/~/constants.BROTLI_DECODER_PARAM_LARGE_WINDOW "constants.BROTLI_DECODER_PARAM_LARGE_WINDOW")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_ERROR](.././zlib/~/constants.BROTLI_DECODER_RESULT_ERROR "constants.BROTLI_DECODER_RESULT_ERROR")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_NEEDS\_MORE\_INPUT](.././zlib/~/constants.BROTLI_DECODER_RESULT_NEEDS_MORE_INPUT "constants.BROTLI_DECODER_RESULT_NEEDS_MORE_INPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_NEEDS\_MORE\_OUTPUT](.././zlib/~/constants.BROTLI_DECODER_RESULT_NEEDS_MORE_OUTPUT "constants.BROTLI_DECODER_RESULT_NEEDS_MORE_OUTPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_SUCCESS](.././zlib/~/constants.BROTLI_DECODER_RESULT_SUCCESS "constants.BROTLI_DECODER_RESULT_SUCCESS")

No documentation available

v

[constants.BROTLI\_DECODER\_SUCCESS](.././zlib/~/constants.BROTLI_DECODER_SUCCESS "constants.BROTLI_DECODER_SUCCESS")

No documentation available

v

[constants.BROTLI\_DEFAULT\_MODE](.././zlib/~/constants.BROTLI_DEFAULT_MODE "constants.BROTLI_DEFAULT_MODE")

No documentation available

v

[constants.BROTLI\_DEFAULT\_QUALITY](.././zlib/~/constants.BROTLI_DEFAULT_QUALITY "constants.BROTLI_DEFAULT_QUALITY")

No documentation available

v

[constants.BROTLI\_DEFAULT\_WINDOW](.././zlib/~/constants.BROTLI_DEFAULT_WINDOW "constants.BROTLI_DEFAULT_WINDOW")

No documentation available

v

[constants.BROTLI\_ENCODE](.././zlib/~/constants.BROTLI_ENCODE "constants.BROTLI_ENCODE")

No documentation available

v

[constants.BROTLI\_LARGE\_MAX\_WINDOW\_BITS](.././zlib/~/constants.BROTLI_LARGE_MAX_WINDOW_BITS "constants.BROTLI_LARGE_MAX_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_MAX\_INPUT\_BLOCK\_BITS](.././zlib/~/constants.BROTLI_MAX_INPUT_BLOCK_BITS "constants.BROTLI_MAX_INPUT_BLOCK_BITS")

No documentation available

v

[constants.BROTLI\_MAX\_QUALITY](.././zlib/~/constants.BROTLI_MAX_QUALITY "constants.BROTLI_MAX_QUALITY")

No documentation available

v

[constants.BROTLI\_MAX\_WINDOW\_BITS](.././zlib/~/constants.BROTLI_MAX_WINDOW_BITS "constants.BROTLI_MAX_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_MIN\_INPUT\_BLOCK\_BITS](.././zlib/~/constants.BROTLI_MIN_INPUT_BLOCK_BITS "constants.BROTLI_MIN_INPUT_BLOCK_BITS")

No documentation available

v

[constants.BROTLI\_MIN\_QUALITY](.././zlib/~/constants.BROTLI_MIN_QUALITY "constants.BROTLI_MIN_QUALITY")

No documentation available

v

[constants.BROTLI\_MIN\_WINDOW\_BITS](.././zlib/~/constants.BROTLI_MIN_WINDOW_BITS "constants.BROTLI_MIN_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_MODE\_FONT](.././zlib/~/constants.BROTLI_MODE_FONT "constants.BROTLI_MODE_FONT")

No documentation available

v

[constants.BROTLI\_MODE\_GENERIC](.././zlib/~/constants.BROTLI_MODE_GENERIC "constants.BROTLI_MODE_GENERIC")

No documentation available

v

[constants.BROTLI\_MODE\_TEXT](.././zlib/~/constants.BROTLI_MODE_TEXT "constants.BROTLI_MODE_TEXT")

No documentation available

v

[constants.BROTLI\_OPERATION\_EMIT\_METADATA](.././zlib/~/constants.BROTLI_OPERATION_EMIT_METADATA "constants.BROTLI_OPERATION_EMIT_METADATA")

No documentation available

v

[constants.BROTLI\_OPERATION\_FINISH](.././zlib/~/constants.BROTLI_OPERATION_FINISH "constants.BROTLI_OPERATION_FINISH")

No documentation available

v

[constants.BROTLI\_OPERATION\_FLUSH](.././zlib/~/constants.BROTLI_OPERATION_FLUSH "constants.BROTLI_OPERATION_FLUSH")

No documentation available

v

[constants.BROTLI\_OPERATION\_PROCESS](.././zlib/~/constants.BROTLI_OPERATION_PROCESS "constants.BROTLI_OPERATION_PROCESS")

No documentation available

v

[constants.BROTLI\_PARAM\_DISABLE\_LITERAL\_CONTEXT\_MODELING](.././zlib/~/constants.BROTLI_PARAM_DISABLE_LITERAL_CONTEXT_MODELING "constants.BROTLI_PARAM_DISABLE_LITERAL_CONTEXT_MODELING")

No documentation available

v

[constants.BROTLI\_PARAM\_LARGE\_WINDOW](.././zlib/~/constants.BROTLI_PARAM_LARGE_WINDOW "constants.BROTLI_PARAM_LARGE_WINDOW")

No documentation available

v

[constants.BROTLI\_PARAM\_LGBLOCK](.././zlib/~/constants.BROTLI_PARAM_LGBLOCK "constants.BROTLI_PARAM_LGBLOCK")

No documentation available

v

[constants.BROTLI\_PARAM\_LGWIN](.././zlib/~/constants.BROTLI_PARAM_LGWIN "constants.BROTLI_PARAM_LGWIN")

No documentation available

v

[constants.BROTLI\_PARAM\_MODE](.././zlib/~/constants.BROTLI_PARAM_MODE "constants.BROTLI_PARAM_MODE")

No documentation available

v

[constants.BROTLI\_PARAM\_NDIRECT](.././zlib/~/constants.BROTLI_PARAM_NDIRECT "constants.BROTLI_PARAM_NDIRECT")

No documentation available

v

[constants.BROTLI\_PARAM\_NPOSTFIX](.././zlib/~/constants.BROTLI_PARAM_NPOSTFIX "constants.BROTLI_PARAM_NPOSTFIX")

No documentation available

v

[constants.BROTLI\_PARAM\_QUALITY](.././zlib/~/constants.BROTLI_PARAM_QUALITY "constants.BROTLI_PARAM_QUALITY")

No documentation available

v

[constants.BROTLI\_PARAM\_SIZE\_HINT](.././zlib/~/constants.BROTLI_PARAM_SIZE_HINT "constants.BROTLI_PARAM_SIZE_HINT")

No documentation available

v

[constants.DEFLATE](.././zlib/~/constants.DEFLATE "constants.DEFLATE")

No documentation available

v

[constants.DEFLATERAW](.././zlib/~/constants.DEFLATERAW "constants.DEFLATERAW")

No documentation available

v

[constants.GUNZIP](.././zlib/~/constants.GUNZIP "constants.GUNZIP")

No documentation available

v

[constants.GZIP](.././zlib/~/constants.GZIP "constants.GZIP")

No documentation available

v

[constants.INFLATE](.././zlib/~/constants.INFLATE "constants.INFLATE")

No documentation available

v

[constants.INFLATERAW](.././zlib/~/constants.INFLATERAW "constants.INFLATERAW")

No documentation available

v

[constants.UNZIP](.././zlib/~/constants.UNZIP "constants.UNZIP")

No documentation available

v

[constants.Z\_BEST\_COMPRESSION](.././zlib/~/constants.Z_BEST_COMPRESSION "constants.Z_BEST_COMPRESSION")

No documentation available

v

[constants.Z\_BEST\_SPEED](.././zlib/~/constants.Z_BEST_SPEED "constants.Z_BEST_SPEED")

No documentation available

v

[constants.Z\_BLOCK](.././zlib/~/constants.Z_BLOCK "constants.Z_BLOCK")

No documentation available

v

[constants.Z\_BUF\_ERROR](.././zlib/~/constants.Z_BUF_ERROR "constants.Z_BUF_ERROR")

No documentation available

v

[constants.Z\_DATA\_ERROR](.././zlib/~/constants.Z_DATA_ERROR "constants.Z_DATA_ERROR")

No documentation available

v

[constants.Z\_DEFAULT\_CHUNK](.././zlib/~/constants.Z_DEFAULT_CHUNK "constants.Z_DEFAULT_CHUNK")

No documentation available

v

[constants.Z\_DEFAULT\_COMPRESSION](.././zlib/~/constants.Z_DEFAULT_COMPRESSION "constants.Z_DEFAULT_COMPRESSION")

No documentation available

v

[constants.Z\_DEFAULT\_LEVEL](.././zlib/~/constants.Z_DEFAULT_LEVEL "constants.Z_DEFAULT_LEVEL")

No documentation available

v

[constants.Z\_DEFAULT\_MEMLEVEL](.././zlib/~/constants.Z_DEFAULT_MEMLEVEL "constants.Z_DEFAULT_MEMLEVEL")

No documentation available

v

[constants.Z\_DEFAULT\_STRATEGY](.././zlib/~/constants.Z_DEFAULT_STRATEGY "constants.Z_DEFAULT_STRATEGY")

No documentation available

v

[constants.Z\_DEFAULT\_WINDOWBITS](.././zlib/~/constants.Z_DEFAULT_WINDOWBITS "constants.Z_DEFAULT_WINDOWBITS")

No documentation available

v

[constants.Z\_ERRNO](.././zlib/~/constants.Z_ERRNO "constants.Z_ERRNO")

No documentation available

v

[constants.Z\_FILTERED](.././zlib/~/constants.Z_FILTERED "constants.Z_FILTERED")

No documentation available

v

[constants.Z\_FINISH](.././zlib/~/constants.Z_FINISH "constants.Z_FINISH")

No documentation available

v

[constants.Z\_FIXED](.././zlib/~/constants.Z_FIXED "constants.Z_FIXED")

No documentation available

v

[constants.Z\_FULL\_FLUSH](.././zlib/~/constants.Z_FULL_FLUSH "constants.Z_FULL_FLUSH")

No documentation available

v

[constants.Z\_HUFFMAN\_ONLY](.././zlib/~/constants.Z_HUFFMAN_ONLY "constants.Z_HUFFMAN_ONLY")

No documentation available

v

[constants.Z\_MAX\_CHUNK](.././zlib/~/constants.Z_MAX_CHUNK "constants.Z_MAX_CHUNK")

No documentation available

v

[constants.Z\_MAX\_LEVEL](.././zlib/~/constants.Z_MAX_LEVEL "constants.Z_MAX_LEVEL")

No documentation available

v

[constants.Z\_MAX\_MEMLEVEL](.././zlib/~/constants.Z_MAX_MEMLEVEL "constants.Z_MAX_MEMLEVEL")

No documentation available

v

[constants.Z\_MAX\_WINDOWBITS](.././zlib/~/constants.Z_MAX_WINDOWBITS "constants.Z_MAX_WINDOWBITS")

No documentation available

v

[constants.Z\_MEM\_ERROR](.././zlib/~/constants.Z_MEM_ERROR "constants.Z_MEM_ERROR")

No documentation available

v

[constants.Z\_MIN\_CHUNK](.././zlib/~/constants.Z_MIN_CHUNK "constants.Z_MIN_CHUNK")

No documentation available

v

[constants.Z\_MIN\_LEVEL](.././zlib/~/constants.Z_MIN_LEVEL "constants.Z_MIN_LEVEL")

No documentation available

v

[constants.Z\_MIN\_MEMLEVEL](.././zlib/~/constants.Z_MIN_MEMLEVEL "constants.Z_MIN_MEMLEVEL")

No documentation available

v

[constants.Z\_MIN\_WINDOWBITS](.././zlib/~/constants.Z_MIN_WINDOWBITS "constants.Z_MIN_WINDOWBITS")

No documentation available

v

[constants.Z\_NEED\_DICT](.././zlib/~/constants.Z_NEED_DICT "constants.Z_NEED_DICT")

No documentation available

v

[constants.Z\_NO\_COMPRESSION](.././zlib/~/constants.Z_NO_COMPRESSION "constants.Z_NO_COMPRESSION")

No documentation available

v

[constants.Z\_NO\_FLUSH](.././zlib/~/constants.Z_NO_FLUSH "constants.Z_NO_FLUSH")

No documentation available

v

[constants.Z\_OK](.././zlib/~/constants.Z_OK "constants.Z_OK")

No documentation available

v

[constants.Z\_PARTIAL\_FLUSH](.././zlib/~/constants.Z_PARTIAL_FLUSH "constants.Z_PARTIAL_FLUSH")

No documentation available

v

[constants.Z\_RLE](.././zlib/~/constants.Z_RLE "constants.Z_RLE")

No documentation available

v

[constants.Z\_STREAM\_END](.././zlib/~/constants.Z_STREAM_END "constants.Z_STREAM_END")

No documentation available

v

[constants.Z\_STREAM\_ERROR](.././zlib/~/constants.Z_STREAM_ERROR "constants.Z_STREAM_ERROR")

No documentation available

v

[constants.Z\_SYNC\_FLUSH](.././zlib/~/constants.Z_SYNC_FLUSH "constants.Z_SYNC_FLUSH")

No documentation available

v

[constants.Z\_TREES](.././zlib/~/constants.Z_TREES "constants.Z_TREES")

No documentation available

v

[constants.Z\_VERSION\_ERROR](.././zlib/~/constants.Z_VERSION_ERROR "constants.Z_VERSION_ERROR")

No documentation available

v

[constants.ZLIB\_VERNUM](.././zlib/~/constants.ZLIB_VERNUM "constants.ZLIB_VERNUM")

No documentation available

v

[Z\_ASCII](.././zlib/~/Z_ASCII "Z_ASCII")

No documentation available

v

[Z\_BEST\_COMPRESSION](.././zlib/~/Z_BEST_COMPRESSION "Z_BEST_COMPRESSION")

No documentation available

v

[Z\_BEST\_SPEED](.././zlib/~/Z_BEST_SPEED "Z_BEST_SPEED")

No documentation available

v

[Z\_BINARY](.././zlib/~/Z_BINARY "Z_BINARY")

No documentation available

v

[Z\_BLOCK](.././zlib/~/Z_BLOCK "Z_BLOCK")

No documentation available

v

[Z\_BUF\_ERROR](.././zlib/~/Z_BUF_ERROR "Z_BUF_ERROR")

No documentation available

v

[Z\_DATA\_ERROR](.././zlib/~/Z_DATA_ERROR "Z_DATA_ERROR")

No documentation available

v

[Z\_DEFAULT\_COMPRESSION](.././zlib/~/Z_DEFAULT_COMPRESSION "Z_DEFAULT_COMPRESSION")

No documentation available

v

[Z\_DEFAULT\_STRATEGY](.././zlib/~/Z_DEFAULT_STRATEGY "Z_DEFAULT_STRATEGY")

No documentation available

v

[Z\_DEFLATED](.././zlib/~/Z_DEFLATED "Z_DEFLATED")

No documentation available

v

[Z\_ERRNO](.././zlib/~/Z_ERRNO "Z_ERRNO")

No documentation available

v

[Z\_FILTERED](.././zlib/~/Z_FILTERED "Z_FILTERED")

No documentation available

v

[Z\_FINISH](.././zlib/~/Z_FINISH "Z_FINISH")

No documentation available

v

[Z\_FIXED](.././zlib/~/Z_FIXED "Z_FIXED")

No documentation available

v

[Z\_FULL\_FLUSH](.././zlib/~/Z_FULL_FLUSH "Z_FULL_FLUSH")

No documentation available

v

[Z\_HUFFMAN\_ONLY](.././zlib/~/Z_HUFFMAN_ONLY "Z_HUFFMAN_ONLY")

No documentation available

v

[Z\_MEM\_ERROR](.././zlib/~/Z_MEM_ERROR "Z_MEM_ERROR")

No documentation available

v

[Z\_NEED\_DICT](.././zlib/~/Z_NEED_DICT "Z_NEED_DICT")

No documentation available

v

[Z\_NO\_COMPRESSION](.././zlib/~/Z_NO_COMPRESSION "Z_NO_COMPRESSION")

No documentation available

v

[Z\_NO\_FLUSH](.././zlib/~/Z_NO_FLUSH "Z_NO_FLUSH")

No documentation available

v

[Z\_OK](.././zlib/~/Z_OK "Z_OK")

No documentation available

v

[Z\_PARTIAL\_FLUSH](.././zlib/~/Z_PARTIAL_FLUSH "Z_PARTIAL_FLUSH")

No documentation available

v

[Z\_RLE](.././zlib/~/Z_RLE "Z_RLE")

No documentation available

v

[Z\_STREAM\_END](.././zlib/~/Z_STREAM_END "Z_STREAM_END")

No documentation available

v

[Z\_STREAM\_ERROR](.././zlib/~/Z_STREAM_ERROR "Z_STREAM_ERROR")

No documentation available

v

[Z\_SYNC\_FLUSH](.././zlib/~/Z_SYNC_FLUSH "Z_SYNC_FLUSH")

No documentation available

v

[Z\_TEXT](.././zlib/~/Z_TEXT "Z_TEXT")

No documentation available

v

[Z\_TREES](.././zlib/~/Z_TREES "Z_TREES")

No documentation available

v

[Z\_UNKNOWN](.././zlib/~/Z_UNKNOWN "Z_UNKNOWN")

No documentation available

v

[Z\_VERSION\_ERROR](.././zlib/~/Z_VERSION_ERROR "Z_VERSION_ERROR")

No documentation available
