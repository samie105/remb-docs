---
title: "Build an app with Nuxt and Bun"
source: "https://bun.com/docs/guides/ecosystem/nuxt"
canonical_url: "https://bun.com/docs/guides/ecosystem/nuxt"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:08.183Z"
content_hash: "a4ea1da3fa1ec2928e039290606d8d710816e32a57199bd0fd79ffa241bc755a"
menu_path: ["Build an app with Nuxt and Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/nextjs/index.md", "title": "Build an app with Next.js and Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/pm2/index.md", "title": "Run Bun as a daemon with PM2"}
---

Bun supports [Nuxt](https://nuxt.com/) out of the box. Initialize a Nuxt app with official `nuxi` CLI.

terminal

```
bunx nuxi init my-nuxt-app
```

```
✔ Which package manager would you like to use?
bun
◐ Installing dependencies...
bun install v1.3.3 (16b4bf34)
 + @nuxt/devtools@0.8.2
 + nuxt@3.7.0
 785 packages installed [2.67s]
✔ Installation completed.
✔ Types generated in .nuxt
✨ Nuxt project has been created with the v3 template. Next steps:
 › cd my-nuxt-app
 › Start development server with bun run dev
```

* * *

To start the dev server, run `bun --bun run dev` from the project root. This will execute the `nuxt dev` command (as defined in the `"dev"` script in `package.json`).

terminal

```
cd my-nuxt-app
bun --bun run dev
```

```
nuxt dev
Nuxi 3.6.5
Nuxt 3.6.5 with Nitro 2.5.2
  > Local:    http://localhost:3000/
  > Network:  http://192.168.0.21:3000/
  > Network:  http://[fd8a:d31d:481c:4883:1c64:3d90:9f83:d8a2]:3000/

✔ Nuxt DevTools is enabled v0.8.0 (experimental)
ℹ Vite client warmed up in 547ms
✔ Nitro built in 244 ms
```

* * *

Once the dev server spins up, open [http://localhost:3000](http://localhost:3000/) to see the app. The app will render Nuxt’s built-in `NuxtWelcome` template component. To start developing your app, replace `<NuxtWelcome />` in `app.vue` with your own UI.

* * *

For production build, while the default preset is already compatible with Bun, you can also use [Bun preset](https://nitro.build/deploy/runtimes/bun) to generate better optimized builds.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)nuxt.config.ts

```
export default defineNuxtConfig({
  nitro: {
    preset: "bun", 
  },
});
```

Alternatively, you can set the preset via environment variable:

terminal

```
NITRO_PRESET=bun bun run build
```

After building with bun, run:

terminal

```
bun run ./.output/server/index.mjs
```

* * *

Refer to the [Nuxt website](https://nuxt.com/docs) for complete documentation.

