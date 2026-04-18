---
title: "string_decoder - Node documentation"
source: "https://docs.deno.com/api/node/string_decoder/"
canonical_url: "https://docs.deno.com/api/node/string_decoder/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:27.154Z"
content_hash: "60541947b0ba080798e88c7e17a3cdf80f4e55a229bb9f9409b1d7417e759743"
menu_path: ["string_decoder - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:string_decoder";
```

The `node:string_decoder` module provides an API for decoding `Buffer` objects into strings in a manner that preserves encoded multi-byte UTF-8 and UTF-16 characters. It can be accessed using:

```js
import { StringDecoder } from 'node:string_decoder';
```

The following example shows the basic use of the `StringDecoder` class.

```js
import { StringDecoder } from 'node:string_decoder';
const decoder = new StringDecoder('utf8');

const cent = Buffer.from([0xC2, 0xA2]);
console.log(decoder.write(cent)); // Prints: ¢

const euro = Buffer.from([0xE2, 0x82, 0xAC]);
console.log(decoder.write(euro)); // Prints: €
```

When a `Buffer` instance is written to the `StringDecoder` instance, an internal buffer is used to ensure that the decoded string does not contain any incomplete multibyte characters. These are held in the buffer until the next call to `stringDecoder.write()` or until `stringDecoder.end()` is called.

In the following example, the three UTF-8 encoded bytes of the European Euro symbol (`€`) are written over three separate operations:

```js
import { StringDecoder } from 'node:string_decoder';
const decoder = new StringDecoder('utf8');

decoder.write(Buffer.from([0xE2]));
decoder.write(Buffer.from([0x82]));
console.log(decoder.end(Buffer.from([0xAC]))); // Prints: €
```

### Classes [#](#Classes)

c

[StringDecoder](.././string_decoder/~/StringDecoder "StringDecoder")

The `node:string_decoder` module provides an API for decoding `Buffer` objects into strings in a manner that preserves encoded multi-byte UTF-8 and UTF-16 characters. It can be accessed using:

*   [end](.././string_decoder/~/StringDecoder#method_end_0)
*   [write](.././string_decoder/~/StringDecoder#method_write_0)
