---
title: "Extract links from a webpage using HTMLRewriter"
source: "https://bun.com/docs/guides/html-rewriter/extract-links"
canonical_url: "https://bun.com/docs/guides/html-rewriter/extract-links"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:26.326Z"
content_hash: "fb59fe603704e6e5b7b09171cb111cffb299f8b718754fe5da6fc4a02e87f7ef"
menu_path: ["Extract links from a webpage using HTMLRewriter"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/tanstack-start/index.md", "title": "Use TanStack Start with Bun"}
nav_next: {"path": "bun/bun/docs/guides/http/cluster/index.md", "title": "Start a cluster of HTTP servers"}
---

Bun’s [HTMLRewriter](bun/bun/docs/runtime/html-rewriter/index.md) API can be used to efficiently extract links from HTML content. It works by chaining together CSS selectors to match the elements, text, and attributes you want to process. Here is an example of how to extract links from a webpage. You can pass `.transform` a `Response`, `Blob`, or `string`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)extract-links.ts

```
async function extractLinks(url: string) {
  const links = new Set<string>();
  const response = await fetch(url);

  const rewriter = new HTMLRewriter().on("a[href]", {
    element(el) {
      const href = el.getAttribute("href");
      if (href) {
        links.add(href);
      }
    },
  });

  // Wait for the response to be processed
  await rewriter.transform(response).blob();
  console.log([...links]); // ["https://bun.com", "/docs", ...]
}

// Extract all links from the Bun website
await extractLinks("https://bun.com");
```

* * *

## Convert relative URLs to absolute

When scraping websites, you often want to convert relative URLs (like `/docs`) to absolute URLs. Here’s how to handle URL resolution:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)extract-links.ts

```
async function extractLinksFromURL(url: string) {
  const response = await fetch(url);
  const links = new Set<string>();

  const rewriter = new HTMLRewriter().on("a[href]", {
    element(el) {
      const href = el.getAttribute("href");
      if (href) {
        // Convert relative URLs to absolute
        try { 
          const absoluteURL = new URL(href, url).href; 
          links.add(absoluteURL);
        } catch { 
          links.add(href); 
        } 
      }
    },
  });

  // Wait for the response to be processed
  await rewriter.transform(response).blob();
  return [...links];
}

const websiteLinks = await extractLinksFromURL("https://example.com");
```

* * *

See [Docs > API > HTMLRewriter](bun/bun/docs/runtime/html-rewriter/index.md) for complete documentation on HTML transformation with Bun.

