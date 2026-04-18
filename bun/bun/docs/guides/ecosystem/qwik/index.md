---
title: "Build an app with Qwik and Bun"
source: "https://bun.com/docs/guides/ecosystem/qwik"
canonical_url: "https://bun.com/docs/guides/ecosystem/qwik"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:36.796Z"
content_hash: "1fe81360723b153aec83a33fa4aa9d6f00a0fcd8e74eae75700ba22ffcd0baf2"
menu_path: ["Build an app with Qwik and Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/prisma-postgres/index.md", "title": "Use Prisma Postgres with Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/react/index.md", "title": "Build a React app with Bun"}
---

Initialize a new Qwik app with `bunx create-qwik`. The `create-qwik` package detects when you are using `bunx` and will automatically install dependencies using `bun`.

terminal

```
bun create qwik
```

```
      ............
    .::: :--------:.
   .::::  .:-------:.
  .:::::.   .:-------.
  ::::::.     .:------.
 ::::::.        :-----:
 ::::::.       .:-----.
  :::::::.     .-----.
   ::::::::..   ---:.
    .:::::::::. :-:.
     ..::::::::::::
             ...::::

┌  Let's create a  Qwik App  ✨ (v1.2.10)
│
◇  Where would you like to create your new project? (Use '.' or './' for current directory)
│  ./my-app
│
●  Creating new project in  /path/to/my-app  ... 🐇
│
◇  Select a starter
│  Basic App
│
◇  Would you like to install bun dependencies?
│  Yes
│
◇  Initialize a new git repository?
│  No
│
◇  Finishing the install. Wanna hear a joke?
│  Yes
│
○  ────────────────────────────────────────────────────────╮
│                                                          │
│  How do you know if there’s an elephant under your bed?  │
│  Your head hits the ceiling!                             │
│                                                          │
├──────────────────────────────────────────────────────────╯
│
◇  App Created 🐰
│
◇  Installed bun dependencies 📋
│
○  Result ─────────────────────────────────────────────╮
│                                                      │
│  Success!  Project created in my-app directory       │
│                                                      │
│  Integrations? Add Netlify, Cloudflare, Tailwind...  │
│  bun qwik add                                        │
│                                                      │
│  Relevant docs:                                      │
│  https://qwik.dev/docs/getting-started/              │
│                                                      │
│  Questions? Start the conversation at:               │
│  https://qwik.dev/chat                               │
│  https://twitter.com/QwikDev                         │
│                                                      │
│  Presentations, Podcasts and Videos:                 │
│  https://qwik.dev/media/                             │
│                                                      │
│  Next steps:                                         │
│  cd my-app                                           │
│  bun start                                           │
│                                                      │
│                                                      │
├──────────────────────────────────────────────────────╯
│
└  Happy coding! 🎉

```

* * *

Run `bun run dev` to start the development server.

terminal

```
bun run dev
```

```
$ vite--mode ssr

VITE v4.4.7  ready in 1190 ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
➜  press h to show help
```

* * *

Open [http://localhost:5173](http://localhost:5173/) with your browser to see the result. Qwik will hot-reload your app as you edit your source files.

* * *

Refer to the [Qwik docs](https://qwik.dev/docs/getting-started/) for complete documentation.

Was this page helpful?
