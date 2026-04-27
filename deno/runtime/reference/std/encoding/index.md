---
title: "@std/encoding"
source: "https://docs.deno.com/runtime/reference/std/encoding/"
canonical_url: "https://docs.deno.com/runtime/reference/std/encoding/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:41:43.052Z"
content_hash: "78656a15415f6d623db3b5be41045325ba47464367f3d709aed470fce81b6c52"
menu_path: ["@std/encoding"]
section_path: []
content_language: "en"
---
**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Utilities for encoding and decoding common formats like hex, base64, and varint.

## Basic Usage

```js
import { encodeBase64, decodeBase64 } from "@std/encoding";
import { assertEquals } from "@std/assert";

const foobar = new TextEncoder().encode("foobar");
assertEquals(encodeBase64(foobar), "Zm9vYmFy");
assertEquals(decodeBase64("Zm9vYmFy"), foobar);
```

## Various Encoding Formats

```js
import {
  encodeHex,
  encodeBase32,
  encodeBase58,
  encodeBase64,
  encodeAscii85,
  decodeHex,
  decodeBase32,
  decodeBase58,
  decodeBase64,
  decodeAscii85,
} from "@std/encoding";
import { assertEquals } from "@std/assert";

// Many different encodings for different character sets
assertEquals(encodeHex("Hello world!"), "48656c6c6f20776f726c6421");
assertEquals(encodeBase32("Hello world!"), "JBSWY3DPEB3W64TMMQQQ====");
assertEquals(encodeBase58("Hello world!"), "2NEpo7TZRhna7vSvL");
assertEquals(encodeBase64("Hello world!"), "SGVsbG8gd29ybGQh");
assertEquals(encodeAscii85("Hello world!"), "87cURD]j7BEbo80");

// Decoding
assertEquals(new TextDecoder().decode(decodeHex("48656c6c6f20776f726c6421")), "Hello world!");
assertEquals(new TextDecoder().decode(decodeBase32("JBSWY3DPEB3W64TMMQQQ====")), "Hello world!");
assertEquals(new TextDecoder().decode(decodeBase58("2NEpo7TZRhna7vSvL")), "Hello world!");
assertEquals(new TextDecoder().decode(decodeBase64("SGVsbG8gd29ybGQh")), "Hello world!");
assertEquals(new TextDecoder().decode(decodeAscii85("87cURD]j7BEbo80")), "Hello world!");
```

## URL-Safe Base64

```js
import { encodeBase64, encodeBase64Url } from "@std/encoding";
import { assertEquals } from "@std/assert";

assertEquals(encodeBase64("ice creams"), "aWNlIGNyZWFtcw=="); // Not url-safe because of `=`
assertEquals(encodeBase64Url("ice creams"), "aWNlIGNyZWFtcw"); // URL-safe!

// Base64Url replaces + with - and / with _
assertEquals(encodeBase64("subjects?"), "c3ViamVjdHM/"); // slash is not URL-safe
assertEquals(encodeBase64Url("subjects?"), "c3ViamVjdHM_"); // _ is URL-safe
```

## Binary Data Encoding

```js
import { encodeHex, encodeBase64 } from "@std/encoding";
import { assertEquals } from "@std/assert";

// Working with binary data
const binaryData = new Uint8Array([0xDE, 0xAD, 0xBE, 0xEF]);
assertEquals(encodeHex(binaryData), "deadbeef");
assertEquals(encodeBase64(binaryData), "3q2+7w==");
```

## Varint Encoding

Learn more from the [protobuf Varint encoding docs](https://protobuf.dev/programming-guides/encoding/#varints).

```js
import { encodeVarint, decodeVarint } from "@std/encoding";
import { assertEquals } from "@std/assert";

// Varint encoding support
assertEquals(encodeVarint(9601n), [new Uint8Array([129, 75]), 2]);

// Decode a varint
const bytes = new Uint8Array([129, 75]);
assertEquals(decodeVarint(bytes), [9601n, 2]);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/encoding
```

[See all symbols in @std/encoding on](https://jsr.io/@std/encoding/doc)
