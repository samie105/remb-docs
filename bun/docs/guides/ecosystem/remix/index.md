---
title: "Build an app with Remix and Bun"
source: "https://bun.com/docs/guides/ecosystem/remix"
canonical_url: "https://bun.com/docs/guides/ecosystem/remix"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:13.963Z"
content_hash: "6ef8db043d99b2a84846ea087140e56b5694c165efec7a73a7a4f371a09975d4"
menu_path: ["Build an app with Remix and Bun"]
section_path: []
nav_prev: {"path": "bun/docs/guides/ecosystem/react/index.md", "title": "Build a React app with Bun"}
nav_next: {"path": "bun/docs/guides/ecosystem/sentry/index.md", "title": "Add Sentry to a Bun app"}
---

* * *

Initialize a Remix app with `create-remix`.

terminal

```
bun create remix
```

```
 remix   v1.19.3 💿 Let's build a better website...

   dir   Where should we create your new project?
         ./my-app

      ◼  Using basic template See https://remix.run/docs/en/main/guides/templates#templates for more
      ✔  Template copied

   git   Initialize a new git repository?
         Yes

  deps   Install dependencies with bun?
         Yes

      ✔  Dependencies installed
      ✔  Git initialized

  done   That's it!
         Enter your project directory using cd ./my-app
         Check out README.md for development and deploy instructions.
```

* * *

To start the dev server, run `bun run dev` from the project root. This will start the dev server using the `remix dev` command. Note that Node.js will be used to run the dev server.

terminal

```
cd my-app
bun run dev
```

```
$ remix dev

💿  remix dev

info  building...
info  built (263ms)
Remix App Server started at http://localhost:3000 (http://172.20.0.143:3000)
```

* * *

Open [http://localhost:3000](http://localhost:3000/) to see the app. Any changes you make to `app/routes/_index.tsx` will be hot-reloaded in the browser.

* * *

To build and start your app, run `bun run build`

terminal

```
bun run build
```

```
$ remix build
info  building... (NODE_ENV=production)
info  built (158ms)
```

Then `bun run start` from the project root.

terminal

```
bun start
```

```
$ remix-serve ./build/index.js
[remix-serve] http://localhost:3000 (http://192.168.86.237:3000)
```

* * *

Read the [Remix docs](https://remix.run/) for more information on how to build apps with Remix.
