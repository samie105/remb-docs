---
title: "@std/crypto"
source: "https://docs.deno.com/runtime/reference/std/crypto/"
canonical_url: "https://docs.deno.com/runtime/reference/std/crypto/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:40:26.589Z"
content_hash: "e88f052792f060656310e925fa5f7be801824ddc70361ab34330c21539613cc7"
menu_path: ["@std/crypto"]
section_path: []
content_language: "en"
---
**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Extensions to the [Web Crypto](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) supporting additional encryption APIs, but also delegating to the built-in APIs when possible.

```js
import { crypto } from "@std/crypto/crypto";

const message = "Hello, Deno!";
const encoder = new TextEncoder();
const data = encoder.encode(message);

await crypto.subtle.digest("BLAKE3", data);
```

### Add to your project

\>\_

```sh
deno add jsr:@std/crypto
```

[See all symbols in @std/crypto on](https://jsr.io/@std/crypto/doc)
