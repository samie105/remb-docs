---
title: "Read and write data to MongoDB using Mongoose and Bun"
source: "https://bun.com/docs/guides/ecosystem/mongoose"
canonical_url: "https://bun.com/docs/guides/ecosystem/mongoose"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:34.699Z"
content_hash: "f3b6613d030d5c96de7ae598ff7e99596f804fc36b599eb93063a85f0c2cbb0d"
menu_path: ["Read and write data to MongoDB using Mongoose and Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/gel/index.md", "title": "Use Gel with Bun"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/hono/index.md", "title": "Build an HTTP server using Hono and Bun"}
---

MongoDB and Mongoose work out of the box with Bun. This guide assumes you’ve already installed MongoDB and are running it as background process/service on your development machine. Follow [this guide](https://www.mongodb.com/docs/manual/installation/) for details.

* * *

Once MongoDB is running, create a directory and initialize it with `bun init`.

terminal

```
mkdir mongoose-app
cd mongoose-app
bun init
```

* * *

Then add Mongoose as a dependency.

terminal

```
bun add mongoose
```

* * *

In `schema.ts` we’ll declare and export an `Animal` model.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)schema.ts

```
import * as mongoose from "mongoose";

const animalSchema = new mongoose.Schema(
  {
    title: { type: String, required: true },
    sound: { type: String, required: true },
  },
  {
    methods: {
      speak() {
        console.log(`${this.sound}!`);
      },
    },
  },
);

export type Animal = mongoose.InferSchemaType<typeof animalSchema>;
export const Animal = mongoose.model("Animal", animalSchema);
```

* * *

Now from `index.ts` we can import `Animal`, connect to MongoDB, and add some data to our database.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import * as mongoose from "mongoose";
import { Animal } from "./schema";

// connect to database
await mongoose.connect("mongodb://127.0.0.1:27017/mongoose-app");

// create new Animal
const cow = new Animal({
  title: "Cow",
  sound: "Moo",
});
await cow.save(); // saves to the database

// read all Animals
const animals = await Animal.find();
animals[0].speak(); // logs "Moo!"

// disconnect
await mongoose.disconnect();
```

* * *

Let’s run this with `bun run`.

terminal

```
bun run index.ts
```

```
Moo!
```

* * *

This is an introduction to using Mongoose with TypeScript and Bun. As you build your application, refer to the official [MongoDB](https://www.mongodb.com/docs) and [Mongoose](https://mongoosejs.com/docs/) sites for complete documentation.
