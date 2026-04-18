---
title: "@std/xml"
source: "https://docs.deno.com/runtime/reference/std/xml/"
canonical_url: "https://docs.deno.com/runtime/reference/std/xml/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:07:08.857Z"
content_hash: "675c828b7b916b0576815cf372130bd8ce801841d03db2c76f67a3af0ca0cced"
menu_path: ["@std/xml"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/std/math/index.md", "title": "@std/math"}
nav_next: {"path": "deno/deno/runtime/reference/web_platform_apis/index.md", "title": "Web Platform APIs"}
---

On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

## Overview

XML parsing and serialization for Deno.

This module implements a non-validating XML 1.0 parser based on the [W3C XML 1.0 (Fifth Edition)](https://www.w3.org/TR/xml/) specification.

## Parsing APIs

Two parsing APIs are provided for different use cases:

API

Use Case

Output

[`parse`](https://jsr.io/@std/xml@0.1.0/doc/~/parse)

Parse a complete XML string

Document tree

[`parseXmlStream`](https://jsr.io/@std/xml@0.1.0/doc/~/parseXmlStream)

Streaming with maximum throughput

Direct callbacks

## Quick Examples

### DOM-style parsing

```js
import { parse } from "@std/xml";
import { assertEquals } from "@std/assert";

const doc = parse("<root><item>Hello</item></root>");
assertEquals(doc.root.name.local, "root");
```

### High-performance streaming with callbacks

For maximum throughput when processing large files:

```js
import { parseXmlStream } from "@std/xml";

const response = await fetch("https://example.com/feed.xml");
const textStream = response.body!.pipeThrough(new TextDecoderStream());

let itemCount = 0;
await parseXmlStream(textStream, {
  onStartElement(name) {
    if (name === "item") itemCount++;
  },
});
console.log(`Found ${itemCount} items`);
```

### Streaming with byte streams

For convenience with fetch responses:

```js
import { parseXmlStreamFromBytes } from "@std/xml";

const response = await fetch("https://example.com/feed.xml");

await parseXmlStreamFromBytes(response.body!, {
  onStartElement(name) {
    console.log(`Element: ${name}`);
  },
});
```

## Position Tracking

Both parsers support optional position tracking (line, column, offset) for debugging and error reporting:

*   **DOM parser ([`parse`](https://jsr.io/@std/xml@0.1.0/doc/~/parse))**: Position tracking is **enabled by default** to provide detailed error messages. Disable with `{ trackPosition: false }` for a performance boost when parsing trusted XML.
    
*   **Streaming parser ([`parseXmlStream`](https://jsr.io/@std/xml@0.1.0/doc/~/parseXmlStream))**: Position tracking is **disabled by default** for optimal streaming performance. Enable with `{ trackPosition: true }` when you need position info.
    

### Add to your project

\>\_

```sh
deno add jsr:@std/xml
```

[See all symbols in @std/xml on](https://jsr.io/@std/xml/doc)
