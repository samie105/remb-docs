---
title: "Common HTTP server usage"
source: "https://bun.com/docs/guides/http/server"
canonical_url: "https://bun.com/docs/guides/http/server"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:15.601Z"
content_hash: "0454d1119b58ea22baf743d0ad873aa72df18a38617031201921cd1056388ecd"
menu_path: ["Common HTTP server usage"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/http/proxy/index.md", "title": "Proxy HTTP requests using fetch()"}
nav_next: {"path": "bun/bun/docs/guides/http/simple/index.md", "title": "Write a simple HTTP server"}
---

This starts an HTTP server listening on port `3000`. It demonstrates basic routing with a number of common responses and also handles POST data from standard forms or as JSON. See [`Bun.serve`](bun/bun/docs/runtime/http/server/index.md) for details.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
const server = Bun.serve({
  async fetch(req) {
    const path = new URL(req.url).pathname;

    // respond with text/html
    if (path === "/") return new Response("Welcome to Bun!");

    // redirect
    if (path === "/abc") return Response.redirect("/source", 301);

    // send back a file (in this case, *this* file)
    if (path === "/source") return new Response(Bun.file(import.meta.path));

    // respond with JSON
    if (path === "/api") return Response.json({ some: "buns", for: "you" });

    // receive JSON data to a POST request
    if (req.method === "POST" && path === "/api/post") {
      const data = await req.json();
      console.log("Received JSON:", data);
      return Response.json({ success: true, data });
    }

    // receive POST data from a form
    if (req.method === "POST" && path === "/form") {
      const data = await req.formData();
      console.log(data.get("someField"));
      return new Response("Success");
    }

    // 404s
    return new Response("Page not found", { status: 404 });
  },
});

console.log(`Listening on ${server.url}`);
```

Was this page helpful?
