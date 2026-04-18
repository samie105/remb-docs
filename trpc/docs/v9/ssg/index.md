---
title: "Static Site Generation"
source: "https://trpc.io/docs/v9/ssg"
canonical_url: "https://trpc.io/docs/v9/ssg"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:55.707Z"
content_hash: "bba6196367a3ecee6f0caba939997a4c565fcdd13f5d2eff3b656cd6942d647d"
menu_path: ["Static Site Generation"]
section_path: []
---
Static site generation requires executing tRPC queries inside `getStaticProps` on each page.

pages/posts/\[id\].tsx

tsx

`import { createSSGHelpers } from '@trpc/react/ssg';`

`import {`

  `GetStaticPaths,`

  `GetStaticPropsContext,`

  `InferGetStaticPropsType,`

`} from 'next';`

`import { prisma } from 'server/context';`

`import { appRouter } from 'server/routers/_app';`

`import superjson from 'superjson';`

`import { trpc } from 'utils/trpc';`

`export async function getStaticProps(`

  `context: GetStaticPropsContext<{ id: string }>,`

`) {`

  `const ssg = await createSSGHelpers({`

    `router: appRouter,`

    `ctx: {},`

    `transformer: superjson, // optional - adds superjson serialization`

  `});`

  `const id = context.params?.id as string;`

  `` // prefetch `post.byId` ``

  `await ssg.fetchQuery('post.byId', {`

    `id,`

  `});`

  `return {`

    `props: {`

      `trpcState: ssg.dehydrate(),`

      `id,`

    `},`

    `revalidate: 1,`

  `};`

`}`

`export const getStaticPaths: GetStaticPaths = async () => {`

  `const posts = await prisma.post.findMany({`

    `select: {`

      `id: true,`

    `},`

  `});`

  `return {`

    `paths: posts.map((post) => ({`

      `params: {`

        `id: post.id,`

      `},`

    `})),`

    `// https://nextjs.org/docs/basic-features/data-fetching#fallback-blocking`

    `fallback: 'blocking',`

  `};`

`};`

`export default function PostViewPage(`

  `props: InferGetStaticPropsType<typeof getStaticProps>,`

`) {`

  `const { id } = props;`

  `const postQuery = trpc.useQuery(['post.byId', { id }]);`

  `if (postQuery.status !== 'success') {`

    `` // won't happen since we're using `fallback: "blocking"` ``

    `return <>Loading...</>;`

  `}`

  `const { data } = postQuery;`

  `return (`

    `<>`

      `<h1>{data.title}</h1>`

      `<em>Created {data.createdAt.toLocaleDateString('en-us')}</em>`

      `<p>{data.text}</p>`

      `<h2>Raw data:</h2>`

      `<pre>{JSON.stringify(data, null, 4)}</pre>`

    `</>`

  `);`

`}`
