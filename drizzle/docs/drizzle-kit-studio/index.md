---
title: "drizzle-kit studio"
source: "https://orm.drizzle.team/docs/drizzle-kit-studio"
canonical_url: "https://orm.drizzle.team/docs/drizzle-kit-studio"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:11.235Z"
content_hash: "3698404c76435318dfc509578412d7715e78d99a0c8169bc4d1e61efdc8a634a"
menu_path: ["drizzle-kit studio"]
section_path: []
nav_prev: {"path": "drizzle/docs/drizzle-kit-up/index.md", "title": "drizzle-kit up"}
nav_next: {"path": "drizzle/docs/kit-custom-migrations/index.md", "title": "Migrations with Drizzle Kit"}
---

`drizzle-kit studio` command spins up a server for [Drizzle Studio](https://orm.drizzle.team/drizzle-studio/overview) hosted on [local.drizzle.studio](https://local.drizzle.studio/). It requires you to specify database connection credentials via [drizzle.config.ts](drizzle/docs/drizzle-config-file/index.md) config file.

By default it will start a Drizzle Studio server on `127.0.0.1:4983`

```
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname"
  },
});
```

```
npx drizzle-kit migrate
```

### Configuring `host` and `port`[](#configuring-host-and-port)

By default Drizzle Studio server starts on `127.0.0.1:4983`, you can config `host` and `port` via CLI options

npm

yarn

pnpm

bun

```
npx drizzle-kit studio --port=3000
npx drizzle-kit studio --host=0.0.0.0
npx drizzle-kit studio --host=0.0.0.0 --port=3000
```

```
yarn drizzle-kit studio --port=3000
yarn drizzle-kit studio --host=0.0.0.0
yarn drizzle-kit studio --host=0.0.0.0 --port=3000
```

```
pnpm drizzle-kit studio --port=3000
pnpm drizzle-kit studio --host=0.0.0.0
pnpm drizzle-kit studio --host=0.0.0.0 --port=3000
```

```
bunx drizzle-kit studio --port=3000
bunx drizzle-kit studio --host=0.0.0.0
bunx drizzle-kit studio --host=0.0.0.0 --port=3000
```

### Logging[](#logging)

You can enable logging of every SQL statement by providing `verbose` flag

npm

yarn

pnpm

bun

```
npx drizzle-kit studio --verbose
```

```
yarn drizzle-kit studio --verbose
```

```
pnpm drizzle-kit studio --verbose
```

```
bunx drizzle-kit studio --verbose
```

### Safari and Brave support[](#safari-and-brave-support)

Safari and Brave block access to localhost by default. You need to install [mkcert](https://github.com/FiloSottile/mkcert) and generate self-signed certificate:

1.  Follow the mkcert [installation steps](https://github.com/FiloSottile/mkcert#installation)
2.  Run `mkcert -install`
3.  Restart your `drizzle-kit studio`

### Embeddable version of Drizzle Studio[](#embeddable-version-of-drizzle-studio)

While hosted version of Drizzle Studio for local development is free forever and meant to just enrich Drizzle ecosystem, we have a B2B offering of an embeddable version of Drizzle Studio for businesses.

**Drizzle Studio component** - is a pre-bundled framework agnostic web component of Drizzle Studio which you can embed into your UI `React` `Vue` `Svelte` `VanillaJS` etc.

That is an extremely powerful UI element that can elevate your offering if you provide Database as a SaaS or a data centric SaaS solutions based on SQL or for private non-customer facing in-house usage.

Database platforms using Drizzle Studio:

*   [Turso](https://turso.tech/), our first customers since Oct 2023!
*   [Neon](https://neon.tech/), [launch post](https://neon.tech/docs/changelog/2024-05-24)
*   [Hydra](https://www.hydra.so/)

Data centric platforms using Drizzle Studio:

*   [Nuxt Hub](https://hub.nuxt.com/), Sébastien Chopin’s [launch post](https://x.com/Atinux/status/1768663789832929520)
*   [Deco.cx](https://deco.cx/)

You can read a detailed overview [here](https://www.npmjs.com/package/@drizzle-team/studio) and if you’re interested - hit us in DMs on [Twitter](https://x.com/drizzleorm) or in [Discord #drizzle-studio](https://driz.link/discord) channel.

### Drizzle Studio chrome extension[](#drizzle-studio-chrome-extension)

Drizzle Studio [chrome extension](https://chromewebstore.google.com/detail/drizzle-studio/mjkojjodijpaneehkgmeckeljgkimnmd) lets you browse your [PlanetScale](https://planetscale.com/), [Cloudflare](https://developers.cloudflare.com/d1/) and [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres) serverless databases directly in their vendor admin panels!

### Limitations[](#limitations)

Our hosted version Drizzle Studio is meant to be used for local development and not meant to be used on remote (VPS, etc).

If you want to deploy Drizzle Studio to your VPS - we have an alpha version of Drizzle Studio Gateway, hit us in DMs on [Twitter](https://x.com/drizzleorm) or in [Discord #drizzle-studio](https://driz.link/discord) channel.

### Is it open source?[](#is-it-open-source)

No. Drizzle ORM and Drizzle Kit are fully open sourced, while Studio is not.

Drizzle Studio for local development is free to use forever to enrich Drizzle ecosystem, open sourcing one would’ve break our ability to provide B2B offerings and monetise it, unfortunately.

