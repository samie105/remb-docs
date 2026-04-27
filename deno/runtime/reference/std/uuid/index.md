---
title: "@std/uuid"
source: "https://docs.deno.com/runtime/reference/std/uuid/"
canonical_url: "https://docs.deno.com/runtime/reference/std/uuid/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:48:57.668Z"
content_hash: "f4a1ebb45496215b7f5a85cd4029bee0c905bdc1f4ee7657fc383ee667ce04b2"
menu_path: ["@std/uuid"]
section_path: []
content_language: "en"
---
**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Generators and validators for [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html) UUIDs for versions v1, v3, v4, v5, v6 and v7.

Use the built-in [`crypto.randomUUID()`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID) function instead of this package, if you only need to generate v4 UUIDs.

Based on [`npm:uuid`](https://www.npmjs.com/package/uuid).

```js
import { v5, NAMESPACE_DNS, NIL_UUID } from "@std/uuid";
import { assert, assertFalse } from "@std/assert";

const data = new TextEncoder().encode("deno.land");
const uuid = await v5.generate(NAMESPACE_DNS, data);

assert(v5.validate(uuid));
assertFalse(v5.validate(NIL_UUID));
```

### Add to your project

\>\_

```sh
deno add jsr:@std/uuid
```

[See all symbols in @std/uuid on](https://jsr.io/@std/uuid/doc)
