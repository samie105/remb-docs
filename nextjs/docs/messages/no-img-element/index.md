---
title: "No img element"
source: "https://nextjs.org/docs/messages/no-img-element"
canonical_url: "https://nextjs.org/docs/messages/no-img-element"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:18:26.740Z"
content_hash: "de3dc8519a151244791a1f4f5746d63f092919bfebbc5a260a70a4843b764f20"
menu_path: ["No img element"]
section_path: []
nav_prev: {"path": "nextjs/docs/messages/no-html-link-for-pages/index.md", "title": "No HTML link for pages"}
nav_next: {"path": "nextjs/docs/messages/no-page-custom-font/index.md", "title": "No Page Custom Font"}
---

# No img element

> Prevent usage of `<img>` element due to slower LCP and higher bandwidth.

## Why This Error Occurred[](#why-this-error-occurred)

An `<img>` element was used to display an image instead of `<Image />` from `next/image`.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

1.  Use [`next/image`](/docs/pages/api-reference/components/image) to improve performance with automatic [Image Optimization](/docs/pages/api-reference/components/image).

> **Note**: If deploying to a [managed hosting provider](/docs/pages/getting-started/deploying), remember to check provider pricing since optimized images might be charged differently than the original images.
> 
> Common image optimization platform pricing:
> 
> *   [Vercel pricing](https://vercel.com/pricing)
> *   [Cloudinary pricing](https://cloudinary.com/pricing)
> *   [imgix pricing](https://imgix.com/pricing)

> **Note**: If self-hosting, remember to install [`sharp`](https://www.npmjs.com/package/sharp) and check if your server has enough storage to cache the optimized images.

pages/index.js

```
import Image from 'next/image'
 
function Home() {
  return (
    <Image
      src="https://example.com/hero.jpg"
      alt="Landscape picture"
      width={800}
      height={500}
    />
  )
}
 
export default Home
```

2.  If you would like to use `next/image` features such as blur-up placeholders but disable Image Optimization, you can do so using [unoptimized](/docs/pages/api-reference/components/image#unoptimized):

pages/index.js

```
import Image from 'next/image'
 
const UnoptimizedImage = (props) => {
  return <Image {...props} unoptimized />
}
```

3.  You can also use the `<picture>` element with the nested `<img>` element:

pages/index.js

```
function Home() {
  return (
    <picture>
      <source srcSet="https://example.com/hero.avif" type="image/avif" />
      <source srcSet="https://example.com/hero.webp" type="image/webp" />
      <img
        src="https://example.com/hero.jpg"
        alt="Landscape picture"
        width={800}
        height={500}
      />
    </picture>
  )
}
```

4.  You can use a [custom image loader](/docs/pages/api-reference/components/image#loader) to optimize images. Set [loaderFile](/docs/pages/api-reference/components/image#loaderfile) to the path of your custom loader.

next.config.js

```
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './my/image/loader.js',
  },
}
```

## Useful Links[](#useful-links)

*   [Image Component and Image Optimization](/docs/pages/api-reference/components/image)
*   [next/image API Reference](/docs/pages/api-reference/components/image)
*   [Largest Contentful Paint (LCP)](/learn/seo/web-performance/lcp)
*   [Next.js config loaderFile option](/docs/pages/api-reference/components/image#loaderfile)

Was this helpful?

supported.

Send
