---
title: "Drizzle <> Gel"
source: "https://orm.drizzle.team/docs/get-started-gel"
canonical_url: "https://orm.drizzle.team/docs/get-started-gel"
docset: "drizzle"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:04.136Z"
content_hash: "20440a2d8dc28a25080f89011a9675b349c39b432586706c1751836fe76e8fb0"
menu_path: ["Drizzle <> Gel"]
section_path: []
---
Drizzle has native support for Gel connections with the `gel-js` client.

#### Step 1 - Install packages[](#step-1---install-packages)

npm

yarn

pnpm

bun

```
npm i drizzle-orm gel
npm i -D drizzle-kit
```

```
yarn add drizzle-orm gel
yarn add -D drizzle-kit
```

```
pnpm add drizzle-orm gel
pnpm add -D drizzle-kit
```

```
bun add drizzle-orm gel
bun add -D drizzle-kit
```

#### Step 2 - Initialize the driver and make a query[](#step-2---initialize-the-driver-and-make-a-query)

gel

gel with config

```
// Make sure to install the 'gel' package 
import { drizzle } from 'drizzle-orm/gel';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```

```
// Make sure to install the 'gel' package
import { drizzle } from "drizzle-orm/gel";

// You can specify any property from the gel connection options
const db = drizzle({
  connection: {
    dsn: process.env.DATABASE_URL,
    tlsSecurity: "default",
  },
});

const result = await db.execute("select 1");
```

If you need to provide your existing driver:

```
// Make sure to install the 'gel' package 
import { drizzle } from "drizzle-orm/gel";
import { createClient } from "gel";

const gelClient = createClient();
const db = drizzle({ client: gelClient });

const result = await db.execute('select 1');
```

#### What’s next?[](#whats-next)
