---
title: "The endpoint did not return a Response."
source: "https://docs.astro.build/en/reference/errors/endpoint-did-not-return-aresponse/"
canonical_url: "https://docs.astro.build/en/reference/errors/endpoint-did-not-return-aresponse/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:22.014Z"
content_hash: "1e4e316a502217c050e0a853b1785be138d8a071d3dd281e83e10cecb472bcf0"
menu_path: ["The endpoint did not return a Response."]
section_path: []
---
# The endpoint did not return a Response.

> **EndpointDidNotReturnAResponse**: An endpoint must return either a `Response`, or a `Promise` that resolves with a `Response`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when an endpoint does not return anything or returns an object that is not a `Response` object.

An endpoint must return either a `Response`, or a `Promise` that resolves with a `Response`. For example:

```
import type { APIContext } from 'astro';
export async function GET({ request, url, cookies }: APIContext): Promise<Response> {    return Response.json({        success: true,        result: 'Data from Astro Endpoint!'    })}
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
