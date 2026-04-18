---
title: "Inferring Types"
source: "https://trpc.io/docs/client/react/infer-types"
canonical_url: "https://trpc.io/docs/client/react/infer-types"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:40.021Z"
content_hash: "1e0f003d105ca662c052c06075577f5d5783501210db586c0de041674a355cc3"
menu_path: ["Inferring Types"]
section_path: []
nav_prev: {"path": "trpc/docs/client/react/getQueryKey/index.md", "title": "getQueryKey"}
nav_next: {"path": "trpc/docs/client/react/server-components/index.md", "title": "Set up with React Server Components"}
---

In addition to the type inference made available by `@trpc/server` ([see here](trpc/docs/client/vanilla/infer-types/index.md)) this integration also provides some inference helpers for usage purely in React.

## Infer React Query options based on your router[​](#infer-react-query-options-based-on-your-router "Direct link to Infer React Query options based on your router")

When creating custom hooks around tRPC procedures, it's sometimes necessary to have the types of the options inferred from the router. You can do so via the `inferReactQueryProcedureOptions` helper exported from `@trpc/react-query`.

trpc.ts

ts

`import {`

  `createTRPCReact,`

  `type inferReactQueryProcedureOptions,`

`} from '@trpc/react-query';`

`import type { inferRouterInputs, inferRouterOutputs } from '@trpc/server';`

`import type { AppRouter } from './server';`

`// infer the types for your router`

`export type ReactQueryOptions = inferReactQueryProcedureOptions<AppRouter>;`

`export type RouterInputs = inferRouterInputs<AppRouter>;`

`export type RouterOutputs = inferRouterOutputs<AppRouter>;`

`export const trpc = createTRPCReact<AppRouter>();`

usePostCreate.ts

ts

`import {`

  `trpc,`

  `type ReactQueryOptions,`

  `type RouterInputs,`

  `type RouterOutputs,`

`} from './trpc';`

`type PostCreateOptions = ReactQueryOptions['post']['create'];`

`function usePostCreate(options?: PostCreateOptions) {`

  `const utils = trpc.useUtils();`

  `return trpc.post.create.useMutation({`

    `...options,`

    `onSuccess(post, variables, onMutateResult, context) {`

      `// invalidate all queries on the post router`

      `// when a new post is created`

      `utils.post.invalidate();`

      `options?.onSuccess?.(post, variables, onMutateResult, context);`

    `},`

  `});`

`}`

usePostById.ts

ts

`import { ReactQueryOptions, RouterInputs, trpc } from './trpc';`

`type PostByIdOptions = ReactQueryOptions['post']['byId'];`

`type PostByIdInput = RouterInputs['post']['byId'];`

`function usePostById(input: PostByIdInput, options?: PostByIdOptions) {`

  `return trpc.post.byId.useQuery(input, options);`

`}`

## Infer abstract types from a "Router Factory"[​](#infer-abstract-types-from-a-router-factory "Direct link to Infer abstract types from a \"Router Factory\"")

If you write a factory which creates a similar router interface several times in your application, you may wish to share client code between usages of the factory. `@trpc/react-query/shared` exports several types which can be used to generate abstract types for a router factory, and build common React components which are passed the router as a prop.

api/factory.ts

tsx

`import { z } from 'zod';`

`import { t, publicProcedure } from './trpc';`

`// @trpc/react-query/shared exports several **Like types which can be used to generate abstract types`

`import { RouterLike, UtilsLike } from '@trpc/react-query/shared';`

`const ThingRequest = z.object({ name: z.string() });`

`const Thing = z.object({ id: z.string(), name: z.string() });`

`const ThingQuery = z.object({ filter: z.string().optional() });`

`const ThingArray = z.array(Thing);`

`// Factory function written by you, however you need,`

`// so long as you can infer the resulting type of t.router() later`

`export function createMyRouter() {`

  `return t.router({`

    `createThing: publicProcedure`

      `.input(ThingRequest)`

      `.output(Thing)`

      `.mutation(({ input }) => ({ id: '1', ...input })),`

    `listThings: publicProcedure`

      `.input(ThingQuery)`

      `.output(ThingArray)`

      `.query(() => []),`

  `})`

`}`

`// Infer the type of your router, and then generate the abstract types for use in the client`

`type MyRouterType = ReturnType<typeof createMyRouter>`

`export type MyRouterLike = RouterLike<MyRouterType>`

`export type MyRouterUtilsLike = UtilsLike<MyRouterType>`

api/server.ts

tsx

`export type AppRouter = typeof appRouter;`

`// Export your MyRouter types to the client`

`export type { MyRouterLike, MyRouterUtilsLike } from './factory';`

frontend/usePostCreate.ts

tsx

`import type { MyRouterLike, MyRouterUtilsLike } from './factory';`

`type MyGenericComponentProps = {`

  `route: MyRouterLike;`

  `utils: MyRouterUtilsLike;`

`};`

`function MyGenericComponent(props: MyGenericComponentProps) {`

  `const { route } = props;`

  `const thing = route.listThings.useQuery({`

    `filter: 'qwerty',`

  `});`

  `const mutation = route.doThing.useMutation({`

    `onSuccess() {`

      `props.utils.listThings.invalidate();`

    `},`

  `});`

  `function handleClick() {`

    `mutation.mutate({`

      `name: 'Thing 1',`

    `});`

  `}`

  `return null; /* ui */`

`}`

`function MyPageComponent() {`

  `const utils = useUtils();`

  `return (`

    `<MyGenericComponent`

      `route={trpc.deep.route.things}`

      `utils={utils.deep.route.things}`

    `/>`

  `);`

`}`

`function MyOtherPageComponent() {`

  `const utils = useUtils();`

  `return (`

    `<MyGenericComponent`

      `route={trpc.different.things}`

      `utils={utils.different.things}`

    `/>`

  `);`

`}`

A more complete working example [can be found here](https://github.com/trpc/trpc/tree/main/packages/tests/server/react/polymorphism.test.tsx)

