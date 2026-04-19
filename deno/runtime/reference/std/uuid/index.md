---
title: "@std/uuid"
source: "https://docs.deno.com/runtime/reference/std/uuid/"
canonical_url: "https://docs.deno.com/runtime/reference/std/uuid/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:06:41.530Z"
content_hash: "1297b177aa1336a122278b63734d8f173f2f8202098e975b98cded6c544a4738"
menu_path: ["@std/uuid"]
section_path: []
---
On this page

*   [Overview](#overview)
    *   [Add to your project](#add-to-your-project)

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
