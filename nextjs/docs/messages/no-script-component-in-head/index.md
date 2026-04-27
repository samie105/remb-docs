---
title: "No Script Component in Head"
source: "https://nextjs.org/docs/messages/no-script-component-in-head"
canonical_url: "https://nextjs.org/docs/messages/no-script-component-in-head"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:56.225Z"
content_hash: "468093623428e535d7deb5d39fedc058aff2cfbe988826dc1723d15f304a571d"
menu_path: ["No Script Component in Head"]
section_path: []
version: "latest"
content_language: "en"
---
[Docs](/docs)[Errors](/docs)No Script Component in Head

# No Script Component in Head

> Prevent usage of `next/script` in `next/head` component.

## Why This Error Occurred[](#why-this-error-occurred)

The `next/script` component should not be used in a `next/head` component.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Move the `<Script />` component outside of `<Head>` instead.

**Before**

pages/index.js

```
import Script from 'next/script'
import Head from 'next/head'
 
export default function Index() {
  return (
    <Head>
      <title>Next.js</title>
      <Script src="/my-script.js" />
    </Head>
  )
}
```

**After**

pages/index.js

```
import Script from 'next/script'
import Head from 'next/head'
 
export default function Index() {
  return (
    <>
      <Head>
        <title>Next.js</title>
      </Head>
      <Script src="/my-script.js" />
    </>
  )
}
```

## Useful Links[](#useful-links)

-   [next/head](/docs/pages/api-reference/components/head)
-   [next/script](/docs/pages/guides/scripts)

Was this helpful?
