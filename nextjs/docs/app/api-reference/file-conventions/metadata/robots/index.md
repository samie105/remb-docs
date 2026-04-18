---
title: "robots.txt"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:20.440Z"
content_hash: "da3cbc052e1f2ef283f801860b0ef5f8dd106e79cc75c675995a9638b15efaf1"
menu_path: ["robots.txt"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/metadata/opengraph-image/index.md", "title": "opengraph-image and twitter-image"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/metadata/sitemap/index.md", "title": "sitemap.xml"}
---

# robots.txt

Last updated April 15, 2026

Add or generate a `robots.txt` file that matches the [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots.txt#Standard) in the **root** of `app` directory to tell search engine crawlers which URLs they can access on your site.

## Static `robots.txt`[](#static-robotstxt)

app/robots.txt

```
User-Agent: *
Allow: /
Disallow: /private/
 
Sitemap: https://acme.com/sitemap.xml
```

## Generate a Robots file[](#generate-a-robots-file)

Add a `robots.js` or `robots.ts` file that returns a [`Robots` object](#robots-object).

> **Good to know**: `robots.js` is a special Route Handler that is cached by default unless it uses a [Request-time API](/docs/app/glossary#request-time-apis) or [dynamic config](/docs/app/guides/caching-without-cache-components#dynamic) option.

app/robots.ts

TypeScript

JavaScriptTypeScript

```
import type { MetadataRoute } from 'next'
 
export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/private/',
    },
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

Output:

```
User-Agent: *
Allow: /
Disallow: /private/
 
Sitemap: https://acme.com/sitemap.xml
```

### Customizing specific user agents[](#customizing-specific-user-agents)

You can customize how individual search engine bots crawl your site by passing an array of user agents to the `rules` property. For example:

app/robots.ts

TypeScript

JavaScriptTypeScript

```
import type { MetadataRoute } from 'next'
 
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: 'Googlebot',
        allow: ['/'],
        disallow: '/private/',
      },
      {
        userAgent: ['Applebot', 'Bingbot'],
        disallow: ['/'],
      },
    ],
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

Output:

```
User-Agent: Googlebot
Allow: /
Disallow: /private/
 
User-Agent: Applebot
Disallow: /
 
User-Agent: Bingbot
Disallow: /
 
Sitemap: https://acme.com/sitemap.xml
```

### Robots object[](#robots-object)

```
type Robots = {
  rules:
    | {
        userAgent?: string | string[]
        allow?: string | string[]
        disallow?: string | string[]
        crawlDelay?: number
      }
    | Array<{
        userAgent: string | string[]
        allow?: string | string[]
        disallow?: string | string[]
        crawlDelay?: number
      }>
  sitemap?: string | string[]
  host?: string
}
```

## Version History[](#version-history)

Version

Changes

`v13.3.0`

`robots` introduced.

[Previous

opengraph-image and twitter-image

](/docs/app/api-reference/file-conventions/metadata/opengraph-image)

[Next

sitemap.xml

](/docs/app/api-reference/file-conventions/metadata/sitemap)

Was this helpful?

supported.

Send




