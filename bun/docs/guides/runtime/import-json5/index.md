---
title: "Import a JSON5 file"
source: "https://bun.com/docs/guides/runtime/import-json5"
canonical_url: "https://bun.com/docs/guides/runtime/import-json5"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:53.593Z"
content_hash: "46c054eec1006ffa675f557979b4057e5d6b00ca475cb53c2661cf1aaab77f3b"
menu_path: ["Import a JSON5 file"]
section_path: []
nav_prev: {"path": "bun/docs/guides/runtime/import-json/index.md", "title": "Import a JSON file"}
nav_next: {"path": "bun/docs/guides/runtime/import-toml/index.md", "title": "Import a TOML file"}
---

Bun natively supports `.json5` imports.

config.json5

```
{
  // Comments are allowed
  database: {
    host: "localhost",
    port: 5432,
    name: "myapp",
  },

  server: {
    port: 3000,
    timeout: 30,
  },

  features: {
    auth: true,
    rateLimit: true,
  },
}
```

* * *

Import the file like any other source file.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.ts

```
import config from "./config.json5";

config.database.host; // => "localhost"
config.server.port; // => 3000
config.features.auth; // => true
```

* * *

You can also use named imports to destructure top-level properties:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.ts

```
import { database, server, features } from "./config.json5";

console.log(database.name); // => "myapp"
console.log(server.timeout); // => 30
console.log(features.rateLimit); // => true
```

* * *

For parsing JSON5 strings at runtime, use `Bun.JSON5.parse()`:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.ts

```
const data = JSON5.parse(`{
  name: 'John Doe',
  age: 30,
  hobbies: [
    'reading',
    'coding',
  ],
}`);

console.log(data.name); // => "John Doe"
console.log(data.hobbies); // => ["reading", "coding"]
```

* * *

See [Docs > API > JSON5](bun/docs/runtime/json5/index.md) for complete documentation on JSON5 support in Bun.
