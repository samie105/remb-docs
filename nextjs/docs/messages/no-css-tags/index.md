---
title: "No CSS Tags"
source: "https://nextjs.org/docs/messages/no-css-tags"
canonical_url: "https://nextjs.org/docs/messages/no-css-tags"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:38.401Z"
content_hash: "b44592f9905d6a98034b9a586910c6e4181375a1c0f90f7f1679630fb8675717"
menu_path: ["No CSS Tags"]
section_path: []
version: "latest"
content_language: "en"
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

Refer to the [Built-In CSS Support](../../app/getting-started/css/index.md) documentation to learn about all the ways to include CSS to your application.

Was this helpful?
