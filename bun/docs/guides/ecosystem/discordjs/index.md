---
title: "Create a Discord bot"
source: "https://bun.com/docs/guides/ecosystem/discordjs"
canonical_url: "https://bun.com/docs/guides/ecosystem/discordjs"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:45.597Z"
content_hash: "cf1b76d99ab2be4370afa7aa209f17bdc3419f5ab614e2e67ea82a51b0572870"
menu_path: ["Create a Discord bot"]
section_path: []
---
[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

Discord.js works out of the box with Bun. Let’s write a bot. First create a directory and initialize it with `bun init`.

terminal

```
mkdir my-bot
cd my-bot
bun init
```

* * *

Now install Discord.js.

terminal

```
bun add discord.js
```

* * *

Before we go further, we need to go to the [Discord developer portal](https://discord.com/developers/applications), login/signup, create a new _Application_, then create a new _Bot_ within that application. Follow the [official guide](https://discordjs.guide/legacy/preparations/app-setup#creating-your-bot) for step-by-step instructions.

* * *

Once complete, you’ll be presented with your bot’s _private key_. Let’s add this to a file called `.env.local`. Bun automatically reads this file and loads it into `process.env`.

This is an example token that has already been invalidated.

.env.local

```
DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
```

* * *

Be sure to add `.env.local` to your `.gitignore`! It is dangerous to check your bot’s private key into version control.

.gitignore

```
node_modules
.env.local
```

* * *

Now let’s actually write our bot in a new file called `bot.ts`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)bot.ts

```
// import discord.js
import { Client, Events, GatewayIntentBits } from "discord.js";

// create a new Client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

// listen for the client to be ready
client.once(Events.ClientReady, c => {
  console.log(`Ready! Logged in as ${c.user.tag}`);
});

// login with the token from .env.local
client.login(process.env.DISCORD_TOKEN);
```

* * *

Now we can run our bot with `bun run`. It may take a several seconds for the client to initialize the first time you run the file.

terminal

```
bun run bot.ts
```

```
Ready! Logged in as my-bot#1234
```

* * *

You’re up and running with a bare-bones Discord.js bot! This is a basic guide to setting up your bot with Bun; we recommend the [official discord.js docs](https://discordjs.guide/) for complete information on the `discord.js` API.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/discordjs.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/discordjs>)

[

Build an app with Astro and Bun

Previous

](/docs/guides/ecosystem/astro)[

Containerize a Bun application with Docker

Next

](/docs/guides/ecosystem/docker)
