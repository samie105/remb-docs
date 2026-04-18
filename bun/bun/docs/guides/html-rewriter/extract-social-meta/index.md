---
title: "Extract social share images and Open Graph tags"
source: "https://bun.com/docs/guides/html-rewriter/extract-social-meta"
canonical_url: "https://bun.com/docs/guides/html-rewriter/extract-social-meta"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:46.346Z"
content_hash: "533384d97ce2485178ece885f55dbc27af937c74147eb4de2500b4016e5de6ff"
menu_path: ["Extract social share images and Open Graph tags"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/html-rewriter/extract-links/index.md", "title": "Extract links from a webpage using HTMLRewriter"}
nav_next: {"path": "bun/bun/docs/guides/http/cluster/index.md", "title": "Start a cluster of HTTP servers"}
---

Bun’s [HTMLRewriter](bun/bun/docs/runtime/html-rewriter/index.md) API can be used to efficiently extract social share images and Open Graph metadata from HTML content. This is particularly useful for building link preview features, social media cards, or web scrapers. We can use HTMLRewriter to match CSS selectors to HTML elements, text, and attributes we want to process.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)extract-social-meta.ts

```
interface SocialMetadata {
  title?: string;
  description?: string;
  image?: string;
  url?: string;
  siteName?: string;
  type?: string;
}

async function extractSocialMetadata(url: string): Promise<SocialMetadata> {
  const metadata: SocialMetadata = {};
  const response = await fetch(url);

  const rewriter = new HTMLRewriter()
    // Extract Open Graph meta tags
    .on('meta[property^="og:"]', {
      element(el) {
        const property = el.getAttribute("property");
        const content = el.getAttribute("content");
        if (property && content) {
          // Convert "og:image" to "image" etc.
          const key = property.replace("og:", "") as keyof SocialMetadata;
          metadata[key] = content;
        }
      },
    })
    // Extract Twitter Card meta tags as fallback
    .on('meta[name^="twitter:"]', {
      element(el) {
        const name = el.getAttribute("name");
        const content = el.getAttribute("content");
        if (name && content) {
          const key = name.replace("twitter:", "") as keyof SocialMetadata;
          // Only use Twitter Card data if we don't have OG data
          if (!metadata[key]) {
            metadata[key] = content;
          }
        }
      },
    })
    // Fallback to regular meta tags
    .on('meta[name="description"]', {
      element(el) {
        const content = el.getAttribute("content");
        if (content && !metadata.description) {
          metadata.description = content;
        }
      },
    })
    // Fallback to title tag
    .on("title", {
      text(text) {
        if (!metadata.title) {
          metadata.title = text.text;
        }
      },
    });

  // Process the response
  await rewriter.transform(response).blob();

  // Convert relative image URLs to absolute
  if (metadata.image && !metadata.image.startsWith("http")) {
    try {
      metadata.image = new URL(metadata.image, url).href;
    } catch {
      // Keep the original URL if parsing fails
    }
  }

  return metadata;
}
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)Example Usage

```
// Example usage
const metadata = await extractSocialMetadata("https://bun.com");
console.log(metadata);
// {
//   title: "Bun — A fast all-in-one JavaScript runtime",
//   description: "Bundle, transpile, install and run JavaScript & TypeScript projects — all in Bun. Bun is a fast all-in-one JavaScript runtime & toolkit designed for speed, complete with a bundler, test runner, and Node.js-compatible package manager.",
//   image: "https://bun.com/share.jpg",
//   type: "website",
//   ...
// }
```

Was this page helpful?
