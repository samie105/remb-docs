---
title: "env"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/env"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/env"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:07:24.636Z"
content_hash: "958c73c1e92f642d1cfc56deaa476dc50a9d3e94e0f9817821c7d67205d9f959"
menu_path: ["env"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/distDir/index.md", "title": "distDir"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/expireTime/index.md", "title": "expireTime"}
---

# env

This is a legacy API and no longer recommended. It's still supported for backward compatibility.

Last updated April 15, 2026

> Since the release of [Next.js 9.4](https://nextjs.org/blog/next-9-4) we now have a more intuitive and ergonomic experience for [adding environment variables](/docs/app/guides/environment-variables). Give it a try!

> **Good to know**: environment variables specified in this way will **always** be included in the JavaScript bundle, prefixing the environment variable name with `NEXT_PUBLIC_` only has an effect when specifying them [through the environment or .env files](/docs/app/guides/environment-variables).

To add environment variables to the JavaScript bundle, open `next.config.js` and add the `env` config:

next.config.js

```
module.exports = {
  env: {
    customKey: 'my-value',
  },
}
```

Now you can access `process.env.customKey` in your code. For example:

```
function Page() {
  return <h1>The value of customKey is: {process.env.customKey}</h1>
}
 
export default Page
```

Next.js will replace `process.env.customKey` with `'my-value'` at build time. Trying to destructure `process.env` variables won't work due to the nature of webpack [DefinePlugin](https://webpack.js.org/plugins/define-plugin/).

For example, the following line:

```
return <h1>The value of customKey is: {process.env.customKey}</h1>
```

Will end up being:

```
return <h1>The value of customKey is: {'my-value'}</h1>
```

[Previous

distDir

](/docs/app/api-reference/config/next-config-js/distDir)

[Next

expireTime

](/docs/app/api-reference/config/next-config-js/expireTime)

Was this helpful?

supported.

Send


