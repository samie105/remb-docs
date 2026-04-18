---
title: "Inferring Types"
source: "https://trpc.io/docs/v9/infer-types"
canonical_url: "https://trpc.io/docs/v9/infer-types"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:13.957Z"
content_hash: "1e17c203090adcf2bd43415109b522a085c912c74f275872ffd26fb1fbd6ddc2"
menu_path: ["Inferring Types"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/further-reading/index.md", "title": "Further Reading"}
nav_next: {"path": "trpc/docs/v9/links/index.md", "title": "Links & Request Batching"}
---

`// trpc-helper.ts`

`// Import AppRouter from your main server router`

`import type {`

`inferProcedureInput,`

`inferProcedureOutput,`

`inferSubscriptionOutput,`

`} from '@trpc/server';`

`import type { AppRouter } from 'api/src/routers/_app';`

`/**`

`* Enum containing all api query paths`

`*/`

`export type TQuery = keyof AppRouter['_def']['queries'];`

`/**`

`* Enum containing all api mutation paths`

`*/`

`export type TMutation = keyof AppRouter['_def']['mutations'];`

`/**`

`* Enum containing all api subscription paths`

`*/`

`export type TSubscription = keyof AppRouter['_def']['subscriptions'];`

`/**`

`* This is a helper method to infer the output of a query resolver`

`* @example type HelloOutput = InferQueryOutput<'hello'>`

`*/`

`export type InferQueryOutput<TRouteKey extends TQuery> = inferProcedureOutput<`

`AppRouter['_def']['queries'][TRouteKey]`

`>;`

`/**`

`* This is a helper method to infer the input of a query resolver`

`* @example type HelloInput = InferQueryInput<'hello'>`

`*/`

`export type InferQueryInput<TRouteKey extends TQuery> = inferProcedureInput<`

`AppRouter['_def']['queries'][TRouteKey]`

`>;`

`/**`

`* This is a helper method to infer the output of a mutation resolver`

`* @example type HelloOutput = InferMutationOutput<'hello'>`

`*/`

`export type InferMutationOutput<TRouteKey extends TMutation> =`

`inferProcedureOutput<AppRouter['_def']['mutations'][TRouteKey]>;`

`/**`

`* This is a helper method to infer the input of a mutation resolver`

`* @example type HelloInput = InferMutationInput<'hello'>`

`*/`

`export type InferMutationInput<TRouteKey extends TMutation> =`

`inferProcedureInput<AppRouter['_def']['mutations'][TRouteKey]>;`

`/**`

`* This is a helper method to infer the output of a subscription resolver`

`* @example type HelloOutput = InferSubscriptionOutput<'hello'>`

`*/`

`export type InferSubscriptionOutput<TRouteKey extends TSubscription> =`

`inferProcedureOutput<AppRouter['_def']['subscriptions'][TRouteKey]>;`

`/**`

`* This is a helper method to infer the asynchronous output of a subscription resolver`

`* @example type HelloAsyncOutput = InferAsyncSubscriptionOutput<'hello'>`

`*/`

`export type InferAsyncSubscriptionOutput<TRouteKey extends TSubscription> =`

`inferSubscriptionOutput<AppRouter, TRouteKey>;`

`/**`

`* This is a helper method to infer the input of a subscription resolver`

`* @example type HelloInput = InferSubscriptionInput<'hello'>`

`*/`

`export type InferSubscriptionInput<TRouteKey extends TSubscription> =`

`inferProcedureInput<AppRouter['_def']['subscriptions'][TRouteKey]>;`
