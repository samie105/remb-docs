---
title: "Addressing \"App Container Deprecated\" Error in Next.js"
source: "https://nextjs.org/docs/messages/app-container-deprecated"
canonical_url: "https://nextjs.org/docs/messages/app-container-deprecated"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:03.289Z"
content_hash: "d9ff6663a6c3fb983d922bec63eb64178d7b716073531be317889106dff6ab7e"
menu_path: ["Addressing \"App Container Deprecated\" Error in Next.js"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../../app/index.md", "title": "App Router"}
nav_next: {"path": "../blocking-route/index.md", "title": "Uncached data was accessed outside of `<Suspense>`"}
---

# Addressing "App Container Deprecated" Error in Next.js

This document guides developers on how to resolve the "App Container Deprecated" error in Next.js by updating their custom App component.

## Why This Error Occurred[](#why-this-error-occurred)

The "App Container Deprecated" error usually occurs when you are using the `<Container>` component in your custom `<App>` (`pages/_app.js`). Prior to version `9.0.4` of Next.js, the `<Container>` component was used to handle scrolling to hashes.

From version `9.0.4` onwards, this functionality was moved up the component tree, rendering the `<Container>` component unnecessary in your custom `<App>`.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

To resolve this issue, you need to remove the `<Container>` component from your custom `<App>` (`pages/_app.js`).

**Before**

pages/\_app.js

```
import React from 'react'
import App, { Container } from 'next/app'
 
class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props
    return (
      <Container>
        <Component {...pageProps} />
      </Container>
    )
  }
}
 
export default MyApp
```

**After**

pages/\_app.js

```
import React from 'react'
import App from 'next/app'
 
class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props
    return <Component {...pageProps} />
  }
}
 
export default MyApp
```

After making this change, your custom `<App>` should work as expected without the `<Container>` component.

## Useful Links[](#useful-links)

-   [Custom App](/docs/pages/building-your-application/routing/custom-app)

Was this helpful?
