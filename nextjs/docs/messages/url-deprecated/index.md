---
title: "`url` is deprecated"
source: "https://nextjs.org/docs/messages/url-deprecated"
canonical_url: "https://nextjs.org/docs/messages/url-deprecated"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:18:08.729Z"
content_hash: "79038a116dd5f99a38e61026d12e3fe213a911f026a032aef80b394e200d3f60"
menu_path: ["`url` is deprecated"]
section_path: []
version: "latest"
content_language: "en"
---
[Docs](/docs)[Errors](/docs)\`url\` is deprecated

# \`url\` is deprecated

## Why This Error Occurred[](#why-this-error-occurred)

In versions prior to 6.x the `url` property got magically injected into every `Page` component (every page inside the `pages` directory).

The reason this is going away is that we want to make things very predictable and explicit. Having a magical url property coming out of nowhere doesn't aid that goal.

> **Note**: ⚠️ In some cases using React Dev Tools may trigger this warning even if you do not reference `url` anywhere in your code. Try temporarily disabling the extension and see if the warning persists.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

Since Next 5 we provide a way to explicitly inject the Next.js router object into pages and all their descending components. The `router` property that is injected will hold the same values as `url`, like `pathname`, `asPath`, and `query`.

Here's an example of using `withRouter`:

pages/index.js

```
import { withRouter } from 'next/router'
 
class Page extends React.Component {
  render() {
    const { router } = this.props
    console.log(router)
    return <div>{router.pathname}</div>
  }
}
 
export default withRouter(Page)
```

We provide a codemod (a code to code transformation) to automatically change the `url` property usages to `withRouter`.

You can find this codemod and instructions on how to run it here: [Use `withRouter`](/docs/pages/guides/upgrading/codemods#url-to-withrouter)

Was this helpful?
