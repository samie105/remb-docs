---
title: "Write-Type-Provider"
source: "https://fastify.dev/docs/latest/Guides/Write-Type-Provider/"
canonical_url: "https://fastify.io/docs/latest/Guides/Write-Type-Provider/"
docset: "fastify"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:13.892Z"
content_hash: "19d3b4c829643d9d104249d8851a2fe1267946047518399f67a94f3ac3fb9e53"
menu_path: ["Write-Type-Provider"]
section_path: []
nav_prev: {"path": "fastify/docs/latest/Reference/Validation-and-Serialization/index.md", "title": "Validation-and-Serialization"}
nav_next: {"path": "fastify/docs/latest/Guides/Recommendations/index.md", "title": "Recommendations"}
---

Version: latest (v5.8.x)

## How to write your own type provider[​](#how-to-write-your-own-type-provider "Direct link to How to write your own type provider")

Things to keep in mind when implementing a custom [type provider](/docs/latest/Reference/Type-Providers/):

### Type Contravariance[​](#type-contravariance "Direct link to Type Contravariance")

Whereas exhaustive type narrowing checks normally rely on `never` to represent an unreachable state, reduction in type provider interfaces should only be done up to `unknown`.

The reasoning is that certain methods of `FastifyInstance` are contravariant on `TypeProvider`, which can lead to TypeScript surfacing assignability issues unless the custom type provider interface is substitutable with `FastifyTypeProviderDefault`.

For example, `FastifyTypeProviderDefault` will not be assignable to the following:

```
export interface NotSubstitutableTypeProvider extends FastifyTypeProvider {   // bad, nothing is assignable to `never` (except for itself)  validator: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : never;  serializer: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : never;}
```

Unless changed to:

```
export interface SubstitutableTypeProvider extends FastifyTypeProvider {  // good, anything can be assigned to `unknown`  validator: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : unknown;  serializer: this['schema'] extends /** custom check here**/ ? /** narrowed type here **/ : unknown;}
```
