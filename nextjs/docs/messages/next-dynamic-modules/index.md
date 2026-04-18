---
title: "`next/dynamic` has deprecated loading multiple modules at once"
source: "https://nextjs.org/docs/messages/next-dynamic-modules"
canonical_url: "https://nextjs.org/docs/messages/next-dynamic-modules"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:17:57.106Z"
content_hash: "7d8875ae7b2198c4b3127c18a84b46aa51b874ab4af82921bf77c6eebb3804dc"
menu_path: ["`next/dynamic` has deprecated loading multiple modules at once"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/missing-suspense-with-csr-bailout/index.md", "title": "Missing Suspense boundary with useSearchParams"}
nav_next: {"path": "nextjs/docs/messages/next-request-in-use-cache/index.md", "title": "Cannot access `cookies()` or `headers()` in `\"use cache\"`"}
---

# \`next/dynamic\` has deprecated loading multiple modules at once

## Why This Error Occurred[](#why-this-error-occurred)

The ability to load multiple modules at once has been deprecated in `next/dynamic` to be closer to React's implementation (`React.lazy` and `Suspense`).

Updating code that relies on this behavior is relatively straightforward! We've provided an example of a before/after to help you migrate your application:

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Migrate to using separate dynamic calls for each module.

**Before**

example.js

```
import dynamic from 'next/dynamic'
 
const HelloBundle = dynamic({
  modules: () => {
    const components = {
      Hello1: () => import('../components/hello1').then((m) => m.default),
      Hello2: () => import('../components/hello2').then((m) => m.default),
    }
 
    return components
  },
  render: (props, { Hello1, Hello2 }) => (
    <div>
      <h1>{props.title}</h1>
      <Hello1 />
      <Hello2 />
    </div>
  ),
})
 
function DynamicBundle() {
  return <HelloBundle title="Dynamic Bundle" />
}
 
export default DynamicBundle
```

**After**

example.js

```
import dynamic from 'next/dynamic'
 
const Hello1 = dynamic(() => import('../components/hello1'))
const Hello2 = dynamic(() => import('../components/hello2'))
 
function HelloBundle({ title }) {
  return (
    <div>
      <h1>{title}</h1>
      <Hello1 />
      <Hello2 />
    </div>
  )
}
 
function DynamicBundle() {
  return <HelloBundle title="Dynamic Bundle" />
}
 
export default DynamicBundle
```

Was this helpful?

supported.

Send




