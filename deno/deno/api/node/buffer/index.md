---
title: "buffer - Node documentation"
source: "https://docs.deno.com/api/node/buffer/"
canonical_url: "https://docs.deno.com/api/node/buffer/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:32.939Z"
content_hash: "85bd8628f68cf575b39237eb97f815b1616237d7a1039e8e7022b1bd96e7e205"
menu_path: ["buffer - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/async_hooks/index.md", "title": "async_hooks - Node documentation"}
nav_next: {"path": "deno/deno/api/node/child_process/index.md", "title": "child_process - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:buffer";
```

`Buffer` objects are used to represent a fixed-length sequence of bytes. Many Node.js APIs support `Buffer`s.

The `Buffer` class is a subclass of JavaScript's [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) class and extends it with methods that cover additional use cases. Node.js APIs accept plain [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) s wherever `Buffer`s are supported as well.

While the `Buffer` class is available within the global scope, it is still recommended to explicitly reference it via an import or require statement.

```js
import { Buffer } from 'node:buffer';

// Creates a zero-filled Buffer of length 10.
const buf1 = Buffer.alloc(10);

// Creates a Buffer of length 10,
// filled with bytes which all have the value `1`.
const buf2 = Buffer.alloc(10, 1);

// Creates an uninitialized buffer of length 10.
// This is faster than calling Buffer.alloc() but the returned
// Buffer instance might contain old data that needs to be
// overwritten using fill(), write(), or other functions that fill the Buffer's
// contents.
const buf3 = Buffer.allocUnsafe(10);

// Creates a Buffer containing the bytes [1, 2, 3].
const buf4 = Buffer.from([1, 2, 3]);

// Creates a Buffer containing the bytes [1, 1, 1, 1] – the entries
// are all truncated using `(value &#x26; 255)` to fit into the range 0–255.
const buf5 = Buffer.from([257, 257.5, -255, '1']);

// Creates a Buffer containing the UTF-8-encoded bytes for the string 'tést':
// [0x74, 0xc3, 0xa9, 0x73, 0x74] (in hexadecimal notation)
// [116, 195, 169, 115, 116] (in decimal notation)
const buf6 = Buffer.from('tést');

// Creates a Buffer containing the Latin-1 bytes [0x74, 0xe9, 0x73, 0x74].
const buf7 = Buffer.from('tést', 'latin1');
```

### Classes [#](#Classes)

c

I

v

[Blob](/api/web/~/Blob "Blob")

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) encapsulates immutable, raw data that can be safely shared across multiple worker threads.

*   [arrayBuffer](/api/web/~/Blob#method_arraybuffer_0)
*   [bytes](/api/web/~/Blob#method_bytes_0)
*   [size](/api/web/~/Blob#property_size)
*   [slice](/api/web/~/Blob#method_slice_0)
*   [stream](/api/web/~/Blob#method_stream_0)
*   [text](/api/web/~/Blob#method_text_0)
*   [type](/api/web/~/Blob#property_type)

c

I

v

[File](.././buffer/~/File "File")

A [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File) provides information about files.

*   [lastModified](.././buffer/~/File#property_lastmodified)
*   [name](.././buffer/~/File#property_name)

### Functions [#](#Functions)

f

[atob](.././buffer/~/atob "atob")

Decodes a string of Base64-encoded data into bytes, and encodes those bytes into a string using Latin-1 (ISO-8859-1).

f

[btoa](.././buffer/~/btoa "btoa")

Decodes a string into bytes using Latin-1 (ISO-8859), and encodes those bytes into a string using Base64.

f

[isAscii](.././buffer/~/isAscii "isAscii")

This function returns `true` if `input` contains only valid ASCII-encoded data, including the case in which `input` is empty.

f

[isUtf8](.././buffer/~/isUtf8 "isUtf8")

This function returns `true` if `input` contains only valid UTF-8-encoded data, including the case in which `input` is empty.

f

[resolveObjectURL](.././buffer/~/resolveObjectURL "resolveObjectURL")

Resolves a `'blob:nodedata:...'` an associated `Blob` object registered using a prior call to `URL.createObjectURL()`.

f

[transcode](.././buffer/~/transcode "transcode")

Re-encodes the given `Buffer` or `Uint8Array` instance from one character encoding to another. Returns a new `Buffer` instance.

### Interfaces [#](#Interfaces)

I

[BlobOptions](.././buffer/~/BlobOptions "BlobOptions")

No documentation available

*   [endings](.././buffer/~/BlobOptions#property_endings)
*   [type](.././buffer/~/BlobOptions#property_type)

I

v

[Buffer](.././buffer/~/Buffer "Buffer")

No documentation available

*   [compare](.././buffer/~/Buffer#method_compare_0)
*   [copy](.././buffer/~/Buffer#method_copy_0)
*   [equals](.././buffer/~/Buffer#method_equals_0)
*   [fill](.././buffer/~/Buffer#method_fill_0)
*   [includes](.././buffer/~/Buffer#method_includes_0)
*   [indexOf](.././buffer/~/Buffer#method_indexof_0)
*   [lastIndexOf](.././buffer/~/Buffer#method_lastindexof_0)
*   [readBigInt64BE](.././buffer/~/Buffer#method_readbigint64be_0)
*   [readBigInt64LE](.././buffer/~/Buffer#method_readbigint64le_0)
*   [readBigUInt64BE](.././buffer/~/Buffer#method_readbiguint64be_0)
*   [readBigUInt64LE](.././buffer/~/Buffer#method_readbiguint64le_0)
*   [readBigUint64BE](.././buffer/~/Buffer#method_readbiguint64be_0)
*   [readBigUint64LE](.././buffer/~/Buffer#method_readbiguint64le_0)
*   [readDoubleBE](.././buffer/~/Buffer#method_readdoublebe_0)
*   [readDoubleLE](.././buffer/~/Buffer#method_readdoublele_0)
*   [readFloatBE](.././buffer/~/Buffer#method_readfloatbe_0)
*   [readFloatLE](.././buffer/~/Buffer#method_readfloatle_0)
*   [readInt16BE](.././buffer/~/Buffer#method_readint16be_0)
*   [readInt16LE](.././buffer/~/Buffer#method_readint16le_0)
*   [readInt32BE](.././buffer/~/Buffer#method_readint32be_0)
*   [readInt32LE](.././buffer/~/Buffer#method_readint32le_0)
*   [readInt8](.././buffer/~/Buffer#method_readint8_0)
*   [readIntBE](.././buffer/~/Buffer#method_readintbe_0)
*   [readIntLE](.././buffer/~/Buffer#method_readintle_0)
*   [readUInt16BE](.././buffer/~/Buffer#method_readuint16be_0)
*   [readUInt16LE](.././buffer/~/Buffer#method_readuint16le_0)
*   [readUInt32BE](.././buffer/~/Buffer#method_readuint32be_0)
*   [readUInt32LE](.././buffer/~/Buffer#method_readuint32le_0)
*   [readUInt8](.././buffer/~/Buffer#method_readuint8_0)
*   [readUIntBE](.././buffer/~/Buffer#method_readuintbe_0)
*   [readUIntLE](.././buffer/~/Buffer#method_readuintle_0)
*   [readUint16BE](.././buffer/~/Buffer#method_readuint16be_0)
*   [readUint16LE](.././buffer/~/Buffer#method_readuint16le_0)
*   [readUint32BE](.././buffer/~/Buffer#method_readuint32be_0)
*   [readUint32LE](.././buffer/~/Buffer#method_readuint32le_0)
*   [readUint8](.././buffer/~/Buffer#method_readuint8_0)
*   [readUintBE](.././buffer/~/Buffer#method_readuintbe_0)
*   [readUintLE](.././buffer/~/Buffer#method_readuintle_0)
*   [reverse](.././buffer/~/Buffer#method_reverse_0)
*   [slice](.././buffer/~/Buffer#method_slice_0)
*   [subarray](.././buffer/~/Buffer#method_subarray_0)
*   [swap16](.././buffer/~/Buffer#method_swap16_0)
*   [swap32](.././buffer/~/Buffer#method_swap32_0)
*   [swap64](.././buffer/~/Buffer#method_swap64_0)
*   [toJSON](.././buffer/~/Buffer#method_tojson_0)
*   [toString](.././buffer/~/Buffer#method_tostring_0)
*   [write](.././buffer/~/Buffer#method_write_0)
*   [writeBigInt64BE](.././buffer/~/Buffer#method_writebigint64be_0)
*   [writeBigInt64LE](.././buffer/~/Buffer#method_writebigint64le_0)
*   [writeBigUInt64BE](.././buffer/~/Buffer#method_writebiguint64be_0)
*   [writeBigUInt64LE](.././buffer/~/Buffer#method_writebiguint64le_0)
*   [writeBigUint64BE](.././buffer/~/Buffer#method_writebiguint64be_0)
*   [writeBigUint64LE](.././buffer/~/Buffer#method_writebiguint64le_0)
*   [writeDoubleBE](.././buffer/~/Buffer#method_writedoublebe_0)
*   [writeDoubleLE](.././buffer/~/Buffer#method_writedoublele_0)
*   [writeFloatBE](.././buffer/~/Buffer#method_writefloatbe_0)
*   [writeFloatLE](.././buffer/~/Buffer#method_writefloatle_0)
*   [writeInt16BE](.././buffer/~/Buffer#method_writeint16be_0)
*   [writeInt16LE](.././buffer/~/Buffer#method_writeint16le_0)
*   [writeInt32BE](.././buffer/~/Buffer#method_writeint32be_0)
*   [writeInt32LE](.././buffer/~/Buffer#method_writeint32le_0)
*   [writeInt8](.././buffer/~/Buffer#method_writeint8_0)
*   [writeIntBE](.././buffer/~/Buffer#method_writeintbe_0)
*   [writeIntLE](.././buffer/~/Buffer#method_writeintle_0)
*   [writeUInt16BE](.././buffer/~/Buffer#method_writeuint16be_0)
*   [writeUInt16LE](.././buffer/~/Buffer#method_writeuint16le_0)
*   [writeUInt32BE](.././buffer/~/Buffer#method_writeuint32be_0)
*   [writeUInt32LE](.././buffer/~/Buffer#method_writeuint32le_0)
*   [writeUInt8](.././buffer/~/Buffer#method_writeuint8_0)
*   [writeUIntBE](.././buffer/~/Buffer#method_writeuintbe_0)
*   [writeUIntLE](.././buffer/~/Buffer#method_writeuintle_0)
*   [writeUint16BE](.././buffer/~/Buffer#method_writeuint16be_0)
*   [writeUint16LE](.././buffer/~/Buffer#method_writeuint16le_0)
*   [writeUint32BE](.././buffer/~/Buffer#method_writeuint32be_0)
*   [writeUint32LE](.././buffer/~/Buffer#method_writeuint32le_0)
*   [writeUint8](.././buffer/~/Buffer#method_writeuint8_0)
*   [writeUintBE](.././buffer/~/Buffer#method_writeuintbe_0)
*   [writeUintLE](.././buffer/~/Buffer#method_writeuintle_0)

I

[BufferConstructor](.././buffer/~/BufferConstructor "BufferConstructor")

No documentation available

*   [alloc](.././buffer/~/BufferConstructor#method_alloc_0)
*   [allocUnsafe](.././buffer/~/BufferConstructor#method_allocunsafe_0)
*   [allocUnsafeSlow](.././buffer/~/BufferConstructor#method_allocunsafeslow_0)
*   [byteLength](.././buffer/~/BufferConstructor#method_bytelength_0)
*   [compare](.././buffer/~/BufferConstructor#method_compare_0)
*   [concat](.././buffer/~/BufferConstructor#method_concat_0)
*   [copyBytesFrom](.././buffer/~/BufferConstructor#method_copybytesfrom_0)
*   [from](.././buffer/~/BufferConstructor#method_from_0)
*   [isBuffer](.././buffer/~/BufferConstructor#method_isbuffer_0)
*   [isEncoding](.././buffer/~/BufferConstructor#method_isencoding_0)
*   [of](.././buffer/~/BufferConstructor#method_of_0)
*   [poolSize](.././buffer/~/BufferConstructor#property_poolsize)

I

[FileOptions](.././buffer/~/FileOptions "FileOptions")

No documentation available

*   [endings](.././buffer/~/FileOptions#property_endings)
*   [lastModified](.././buffer/~/FileOptions#property_lastmodified)
*   [type](.././buffer/~/FileOptions#property_type)

### Type Aliases [#](<#Type Aliases>)

T

[BufferEncoding](.././buffer/~/BufferEncoding "BufferEncoding")

No documentation available

T

[ImplicitArrayBuffer](.././buffer/~/ImplicitArrayBuffer "ImplicitArrayBuffer")

`Buffer` objects are used to represent a fixed-length sequence of bytes. Many Node.js APIs support `Buffer`s.

T

[TranscodeEncoding](.././buffer/~/TranscodeEncoding "TranscodeEncoding")

No documentation available

T

[WithImplicitCoercion](.././buffer/~/WithImplicitCoercion "WithImplicitCoercion")

No documentation available

### Variables [#](#Variables)

v

[constants](.././buffer/~/constants "constants")

No documentation available

*   [MAX\_LENGTH](.././buffer/~/constants#property_max_length)
*   [MAX\_STRING\_LENGTH](.././buffer/~/constants#property_max_string_length)

v

[INSPECT\_MAX\_BYTES](.././buffer/~/INSPECT_MAX_BYTES "INSPECT_MAX_BYTES")

No documentation available

v

[kMaxLength](.././buffer/~/kMaxLength "kMaxLength")

No documentation available

v

[kStringMaxLength](.././buffer/~/kStringMaxLength "kStringMaxLength")

No documentation available

v

[SlowBuffer](.././buffer/~/SlowBuffer "SlowBuffer")

No documentation available

*   [prototype](.././buffer/~/SlowBuffer#property_prototype)

