---
title: "No CSS Tags"
source: "https://nextjs.org/docs/messages/no-css-tags"
canonical_url: "https://nextjs.org/docs/messages/no-css-tags"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:12.962Z"
content_hash: "c75d679205663377f262ef8aba7da2cc63b8971d35d4794fd3188761394fcb94"
menu_path: ["No CSS Tags"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-cache/index.md", "title": "No Cache Detected"}
nav_next: {"path": "nextjs/docs/messages/no-document-import-in-page/index.md", "title": "No Document Import in Page"}
---

# No CSS Tags

> Prevent manual stylesheet tags.

## Why This Error Occurred[](#why-this-error-occurred)

A `link` element was used to link to an external stylesheet. This can negatively affect CSS resource loading on your webpage.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

There are multiple ways to include styles using Next.js' built-in CSS support, including the option to use `@import` within the root stylesheet that is imported in `pages/_app.js`:

styles.css

```
/* Root stylesheet */
@import 'extra.css';
 
body {
  /* ... */
}
```

Another option is to use CSS Modules to import the CSS file scoped specifically to the component.

pages/index.js

```
import styles from './extra.module.css'
 
export class Home {
  render() {
    return (
      <div>
        <button type="button" className={styles.active}>
          Open
        </button>
      </div>
    )
  }
}
```

Refer to the [Built-In CSS Support](/docs/app/getting-started/css) documentation to learn about all the ways to include CSS to your application.

Was this helpful?

supported.

Send




