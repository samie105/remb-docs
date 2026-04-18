---
title: "FAQ / Troubleshooting"
source: "https://trpc.io/docs/v10/faq"
canonical_url: "https://trpc.io/faq"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:46.198Z"
content_hash: "70da03accda58ec77372d2261f8dde6d15d5ea9cdd877fe40b55c86615b61875"
menu_path: ["FAQ / Troubleshooting"]
section_path: []
---
Collection of frequently asked questions with ideas on how to troubleshoot & resolve them.

Feel free to contribute to this page with improvements or create a new discussion [on GitHub](https://github.com/trpc/trpc/discussions) if you have a question that isn't answered here. Also, have look through the [GitHub Discussions](https://github.com/trpc/trpc/discussions) and our [Discord](https://trpc.io/discord) if your question isn't answered here.

## It doesn't work! I'm getting `any` everywhere[​](#it-doesnt-work-im-getting-any-everywhere "Direct link to it-doesnt-work-im-getting-any-everywhere")

*   Make sure you have no type errors in your code
*   Make sure you have `"strict": true` in your `tsconfig.json`
*   Make sure your `@trpc/*`\-versions match in your `package.json`

## How do I make a middleware change the type of my `Context`?[​](#how-do-i-make-a-middleware-change-the-type-of-my-context "Direct link to how-do-i-make-a-middleware-change-the-type-of-my-context")

See [Context Extension](https://trpc.io/docs/server/middlewares#context-extension).

## Is tRPC production ready?[​](#is-trpc-production-ready "Direct link to Is tRPC production ready?")

Yes. tRPC is very stable and is used by thousands of companies, even big ones like [Netflix](https://netflix.com/) & [Pleo](https://pleo.io/) are using tRPC in production.

## Why doesn't tRPC work in my monorepo?[​](#why-doesnt-trpc-work-in-my-monorepo "Direct link to Why doesn't tRPC work in my monorepo?")

This is difficult question to answer, but since tRPC doesn't have any build step, it's unlikely that the problem is on tRPC's side.

Here are some things to check:

*   Make sure you have the same version of all `@trpc/*` across all your project
*   Make sure you have `"strict": true` in all your `tsconfig.json`s
*   Make sure you have no type errors in your app
*   In the case that you have a dedicated server and client `tsconfig.json` files without a bundled server monorepo package, make sure you have `"paths": [...]` in your client `tsconfig.json` like your server `tsconfig.json`,so that the client can find the same file.

You can also have a look at our [Awesome tRPC](https://trpc.io/docs/community/awesome-trpc)\-collection to find several open-source projects that are using tRPC in a monorepo.

## Is a monorepo mandatory?[​](#is-a-monorepo-mandatory "Direct link to Is a monorepo mandatory?")

No, a monorepo is not mandatory but you will lose some of the benefits of using tRPC if you don't use it since you will lose guarantees that your client and server works together.

One way you can leverage tRPC is to publish a private npm package with the types of your backend repo and consume them in your frontend repo.

> _Related discussion: [https://github.com/trpc/trpc/discussions/1860](https://github.com/trpc/trpc/discussions/1860)_

## Can I dynamically return a different output depending on what input I send?[​](#can-i-dynamically-return-a-different-output-depending-on-what-input-i-send "Direct link to Can I dynamically return a different output depending on what input I send?")

No, not currently, in order for tRPC to do that automatically, we need something called "Higher kinded types" which is not yet supported in TypeScript.

> _Related discussion: [https://github.com/trpc/trpc/discussions/2150](https://github.com/trpc/trpc/discussions/2150)_

## Can I apply a middleware to a full router?[​](#can-i-apply-a-middleware-to-a-full-router "Direct link to Can I apply a middleware to a full router?")

No, but you can use [base procedures](https://trpc.io/docs/server/procedures#reusable-base-procedures) instead, which offers more flexibility than if this was done on a per-router-level.

## Does tRPC work with Next.js 13 App Layouts & RSC?[​](#does-trpc-work-with-nextjs-13-app-layouts--rsc "Direct link to Does tRPC work with Next.js 13 App Layouts & RSC?")

Yes, tRPC works with Next.js 13 App Layouts & React Server Components, but we have not built any official examples of it yet.

For more information, you can read & follow [this issue](https://github.com/trpc/trpc/issues/3297) where we've referenced a few examples of it.

## Am I safe with using features marked as as `unstable_`?[​](#unstable "Direct link to unstable")

**tl;dr**: Yes!

If you encounter a feature in tRPC that is marked as `unstable_` it means that the API is unstable and might change in minor version bumps, but:

*   Specifics of the implementation might change in minor changes - its name and options might change
*   If it exists in tRPC it's already used it in production
*   We very much encourage you to use it
*   If any changes are done to `unstable_`\-feature, they will be included in the release notes (& you'll see type errors)
*   Please report any suggestion on the API design or issues on [github.com/trpc/trpc/issues](https://github.com/trpc/trpc/issues) or in the `#🧪-unstable-experimental-features` on [our Discord](https://trpc.io/discord)

## Am I safe with using features marked as as `experimental_`?[​](#experimental "Direct link to experimental")

If you encounter a feature in tRPC that is marked as `experimental_` it means that the API is unstable and is very likely to change during any bump of tRPC.

*   Wide range of the feature and its usage might change
*   The feature might not be well-tested
*   We might drop the feature entirely
*   It's up to you to read the latest docs and upgrade without a guided migration path
*   Changes might not be well-documented in the release notes
*   Bugs are not guaranteed to be fixed

We do, however, love input! Please report any suggestion on the API design or issues in the `#🧪-unstable-experimental-features` on [our Discord](https://trpc.io/discord).

## Is tRPC strict with semver?[​](#semver "Direct link to Is tRPC strict with semver?")

Yes, tRPC is very strict with [semantic versioning](https://semver.org/) and we will never introduce breaking changes in a minor version bump.

With this, we also consider changes on `export`ed TypeScript `type`s as major changes, apart from ones marked as `@internal` in the JSDoc.

## Why is tRPC on such a high version already?[​](#why-is-trpc-on-such-a-high-version-already "Direct link to Why is tRPC on such a high version already?")

When tRPC started and had very few users and we often iterated on the API design whilst being strict with semver.

*   The first 9 versions of tRPC were released in the first 8 months of the project.
*   [Version 10](https://trpc.io/blog/announcing-trpc-10) which we released 14 months after v9 should be seen as the real "version 2" of tRPC where we did any fundamental changes to the API decisions. _(2 is 10 in binary, amirite?)_

We expect the API to be stable now and are planning to release codemods for any breaking changes in the future, just like we did with the v9->v10 upgrade.

* * *

## Anything else you want to know?[​](#anything-else-you-want-to-know "Direct link to Anything else you want to know?")

Please write a feature request on [GitHub](https://github.com/trpc/trpc/issues), write in [GitHub Discussions](https://github.com/trpc/trpc/discussions), or [Discord](https://trpc.io/discord). You're also free to suggest improvement of this page or any other page using the "Edit this page" button at the bottom of the page.
