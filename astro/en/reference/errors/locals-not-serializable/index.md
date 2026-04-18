---
title: "Astro.locals is not serializable"
source: "https://docs.astro.build/en/reference/errors/locals-not-serializable/"
canonical_url: "https://docs.astro.build/en/reference/errors/locals-not-serializable/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:34.914Z"
content_hash: "68a67cad126a90a198225b027ecf70f807d2eee2e68577e64ccd5d7d6f9a1464"
menu_path: ["Astro.locals is not serializable"]
section_path: []
---
# Astro.locals is not serializable

> **LocalsNotSerializable**: The information stored in `Astro.locals` for the path “`HREF`” is not serializable. Make sure you store only serializable data. (E03034)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when a user attempts to store something that is not serializable in `locals`.

For example:

```
import {defineMiddleware} from "astro/middleware";export const onRequest = defineMiddleware((context, next) => {  context.locals = {    foo() {      alert("Hello world!")    }  };  return next();});
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
