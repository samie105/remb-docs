---
title: "Upload files via HTTP using FormData"
source: "https://bun.com/docs/guides/http/file-uploads"
canonical_url: "https://bun.com/docs/guides/http/file-uploads"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:00.213Z"
content_hash: "c7b80a7e56868f0014a5014b1afecaae75961bf12c072b1b6b27a6d7cce40d17"
menu_path: ["Upload files via HTTP using FormData"]
section_path: []
nav_prev: {"path": "../fetch-unix/index.md", "title": "fetch with unix domain sockets in Bun"}
nav_next: {"path": "../hot/index.md", "title": "Hot reload an HTTP server"}
---

To upload files via HTTP with Bun, use the [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) API. Let’s start with an HTTP server that serves an HTML web form.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const server = Bun.serve({
  port: 4000,
  async fetch(req) {
    const url = new URL(req.url);

    // return index.html for root path
    if (url.pathname === "/")
      return new Response(Bun.file("index.html"), {
        headers: {
          "Content-Type": "text/html",
        },
      });

    return new Response("Not Found", { status: 404 });
  },
});

console.log(`Listening on http://localhost:${server.port}`);
```

* * *

We can define our HTML form in another file, `index.html`.

index.html

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Form</title>
  </head>
  <body>
    <form action="/action" method="post" enctype="multipart/form-data">
      <input type="text" name="name" placeholder="Name" />
      <input type="file" name="profilePicture" />
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>
```

* * *

At this point, we can run the server and visit [`localhost:4000`](http://localhost:4000/) to see our form.

```
bun run index.ts
Listening on http://localhost:4000
```

* * *

Our form will send a `POST` request to the `/action` endpoint with the form data. Let’s handle that request in our server. First we use the [`.formData()`](https://developer.mozilla.org/en-US/docs/Web/API/Request/formData) method on the incoming `Request` to asynchronously parse its contents to a `FormData` instance. Then we can use the [`.get()`](https://developer.mozilla.org/en-US/docs/Web/API/FormData/get) method to extract the value of the `name` and `profilePicture` fields. Here `name` corresponds to a `string` and `profilePicture` is a `Blob`. Finally, we write the `Blob` to disk using [`Bun.write()`](../../../runtime/file-io/index.md#writing-files-bun-write).

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
const server = Bun.serve({
  port: 4000,
  async fetch(req) {
    const url = new URL(req.url);

    // return index.html for root path
    if (url.pathname === "/")
      return new Response(Bun.file("index.html"), {
        headers: {
          "Content-Type": "text/html",
        },
      });

    // parse formdata at /action
    if (url.pathname === "/action") { 
      const formdata = await req.formData(); 
      const name = formdata.get("name"); 
      const profilePicture = formdata.get("profilePicture"); 
      if (!profilePicture) throw new Error("Must upload a profile picture."); 
      // write profilePicture to disk
      await Bun.write("profilePicture.png", profilePicture); 
      return new Response("Success"); 
    } 

    return new Response("Not Found", { status: 404 });
  },
});
```
