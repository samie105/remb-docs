---
title: "Build an app with Astro and Bun"
source: "https://bun.com/docs/guides/ecosystem/astro"
canonical_url: "https://bun.com/docs/guides/ecosystem/astro"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:32.483Z"
content_hash: "25ed91326460a1feca54ed7baa18b982c5acd6cdb85ad513c1973cae272a2293"
menu_path: ["Build an app with Astro and Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/deployment/vercel/index.md", "title": "Deploy a Bun application on Vercel"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/discordjs/index.md", "title": "Create a Discord bot"}
---

Initialize a fresh Astro app with `bun create astro`. The `create-astro` package detects when you are using `bunx` and will automatically install dependencies using `bun`.

terminal

```
bun create astro
```

```
╭─────╮  Houston:
│ ◠ ◡ ◠  We're glad to have you on board.
╰─────╯

 astro   v3.1.4 Launch sequence initiated.

   dir   Where should we create your new project?
         ./fumbling-field

  tmpl   How would you like to start your new project?
         Use blog template
      ✔  Template copied

  deps   Install dependencies?
         Yes
      ✔  Dependencies installed

    ts   Do you plan to write TypeScript?
         Yes

   use   How strict should TypeScript be?
         Strict
      ✔  TypeScript customized

   git   Initialize a new git repository?
         Yes
      ✔  Git initialized

  next   Liftoff confirmed. Explore your project!

         Enter your project directory using cd ./fumbling-field
         Run `bun run dev` to start the dev server. CTRL+C to stop.
         Add frameworks like react or tailwind using astro add.

         Stuck? Join us at https://astro.build/chat

╭─────╮  Houston:
│ ◠ ◡ ◠  Good luck out there, astronaut! 🚀
╰─────╯
```

* * *

Start the dev server with `bunx`. By default, Bun will run the dev server with Node.js. To use the Bun runtime instead, use the `--bun` flag.

terminal

```
bunx --bun astro dev
```

```
  🚀  astro  v3.1.4 started in 200ms

  ┃ Local    http://localhost:4321/
  ┃ Network  use --host to expose
```

* * *

Open [http://localhost:4321](http://localhost:4321/) with your browser to see the result. Astro will hot-reload your app as you edit your source files.

* * *

Refer to the [Astro docs](https://docs.astro.build/en/getting-started/) for complete documentation.


