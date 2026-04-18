---
title: "env"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/env"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/env"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:20:37.011Z"
content_hash: "b65404a732645e6bcf248f591448fb3c9934c875b1ddb84a8839b1916a7b3971"
menu_path: ["env"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/distDir/index.md", "title": "distDir"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/exportPathMap/index.md", "title": "exportPathMap"}
---

# env

Last updated April 15, 2026

> Since the release of [Next.js 9.4](https://nextjs.org/blog/next-9-4) we now have a more intuitive and ergonomic experience for [adding environment variables](/docs/pages/guides/environment-variables). Give it a try!

> **Good to know**: environment variables specified in this way will **always** be included in the JavaScript bundle, prefixing the environment variable name with `NEXT_PUBLIC_` only has an effect when specifying them [through the environment or .env files](/docs/pages/guides/environment-variables).

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

Was this helpful?

supported.

Send




