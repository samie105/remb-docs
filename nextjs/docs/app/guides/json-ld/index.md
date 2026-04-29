---
title: "How to implement JSON-LD in your Next.js application"
source: "https://nextjs.org/docs/app/guides/json-ld"
canonical_url: "https://nextjs.org/docs/app/guides/json-ld"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:13:49.384Z"
content_hash: "3ce884318d43ba548dbfd57df3451b3925b1803490d5737ac5a1b646e5289112"
menu_path: ["How to implement JSON-LD in your Next.js application"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/guides/internationalization/index.md", "title": "Internationalization"}
nav_next: {"path": "nextjs/docs/app/guides/lazy-loading/index.md", "title": "How to lazy load Client Components and libraries"}
---

# How to implement JSON-LD in your Next.js application

Last updated April 23, 2026

[JSON-LD](https://json-ld.org/) is a format for structured data that can be used by search engines and AI to help them understand the structure of the page beyond pure content. For example, you can use it to describe a person, an event, an organization, a movie, a book, a recipe, and many other types of entities.

Our current recommendation for JSON-LD is to render structured data as a `<script>` tag in your `layout.js` or `page.js` components.

The following snippet uses `JSON.stringify`, which does not sanitize malicious strings used in XSS injection. To prevent this type of vulnerability, you can scrub `HTML` tags from the `JSON-LD` payload, for example, by replacing the character, `<`, with its unicode equivalent, `\u003c`.

Review your organization's recommended approach to sanitize potentially dangerous strings, or use community maintained alternatives for `JSON.stringify` such as, [serialize-javascript](https://www.npmjs.com/package/serialize-javascript).

app/products/\[id\]/page.tsx

JavaScriptTypeScript

```
export default async function Page({ params }) {
  const { id } = await params
  const product = await getProduct(id)
 
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.name,
    image: product.image,
    description: product.description,
  }
 
  return (
    <section>
      {/* Add JSON-LD to your page */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd).replace(/</g, '\\u003c'),
        }}
      />
      {/* ... */}
    </section>
  )
}
```

You can validate and test your structured data with the [Rich Results Test](https://search.google.com/test/rich-results) for Google or the generic [Schema Markup Validator](https://validator.schema.org/).

You can type your JSON-LD with TypeScript using community packages like [`schema-dts`](https://www.npmjs.com/package/schema-dts):

```
import { Product, WithContext } from 'schema-dts'
 
const jsonLd: WithContext<Product> = {
  '@context': 'https://schema.org',
  '@type': 'Product',
  name: 'Next.js Sticker',
  image: 'https://nextjs.org/imgs/sticker.png',
  description: 'Dynamic at the speed of static.',
}
```

> **Good to know**: The `next/script` component is optimized for loading and executing JavaScript. Since JSON-LD is structured data, not executable code, a native `<script>` tag is the right choice here.

Was this helpful?
