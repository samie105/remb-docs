---
title: "Server-side render (SSR) a React component"
source: "https://bun.com/docs/guides/ecosystem/ssr-react"
canonical_url: "https://bun.com/docs/guides/ecosystem/ssr-react"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:36.881Z"
content_hash: "7810a5e73b7d26da4dc226b8fa437764c7d3772aa95d1955d665ad5438f1a4ef"
menu_path: ["Server-side render (SSR) a React component"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/solidstart/index.md", "title": "Build an app with SolidStart and Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/stric/index.md", "title": "Build an HTTP server using StricJS and Bun"}
---

# Any package manager can be used
bun add react react-dom
```

* * *

To render a React component to an HTML stream server-side (SSR):

ssr-react.tsx

```
import { renderToReadableStream } from "react-dom/server";

function Component(props: { message: string }) {
  return (
    <body>
      <h1>{props.message}</h1>
    </body>
  );
}

const stream = await renderToReadableStream(<Component message="Hello from server!" />);
```

* * *

Combining this with `Bun.serve()`, we get an SSR HTTP server:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.tsx

```
Bun.serve({
  async fetch() {
    const stream = await renderToReadableStream(<Component message="Hello from server!" />);
    return new Response(stream, {
      headers: { "Content-Type": "text/html" },
    });
  },
});
```

* * *

React `19` and later includes an [SSR optimization](https://github.com/facebook/react/pull/25597) that takes advantage of Bun’s “direct” `ReadableStream` implementation. If you run into an error like `export named 'renderToReadableStream' not found`, please make sure to install version `19` of `react` & `react-dom`, or import from `react-dom/server.browser` instead of `react-dom/server`. See [facebook/react#28941](https://github.com/facebook/react/issues/28941) for more information.
