---
title: "TOML"
source: "https://bun.com/docs/runtime/toml"
canonical_url: "https://bun.com/docs/runtime/toml"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:53.428Z"
content_hash: "3afbab592529bd9854a786c54ca5d5c0110b45d7d2ff2b5f79f0d2bc8f31ce5e"
menu_path: ["TOML"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/templating/create/index.md", "title": "bun create"}
nav_next: {"path": "bun/bun/docs/runtime/templating/init/index.md", "title": "bun init"}
---

# Application config
title = "My App"

[owner]
name = "John Doe"

[database]
enabled = true
ports = [8000, 8001, 8002]
connection_max = 5000

[servers.alpha]
ip = "10.0.0.1"
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"
`);
```

#### Error Handling

`Bun.TOML.parse()` throws if the TOML is invalid:

```
try {
  Bun.TOML.parse("invalid = = =");
} catch (error) {
  console.error("Failed to parse TOML:", error.message);
}
```

* * *

## Module Import

### ES Modules

You can import TOML files directly as ES modules. The TOML content is parsed and made available as both default and named exports:

config.toml

```
[database]
host = "localhost"
port = 5432
name = "myapp"

[redis]
host = "localhost"
port = 6379

[features]
auth = true
rateLimit = true
analytics = false
```

#### Default Import

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import config from "./config.toml";

console.log(config.database.host); // "localhost"
console.log(config.redis.port); // 6379
```

#### Named Imports

You can destructure top-level TOML tables as named imports:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import { database, redis, features } from "./config.toml";

console.log(database.host); // "localhost"
console.log(redis.port); // 6379
console.log(features.auth); // true
```

Or combine both:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import config, { database, features } from "./config.toml";

// Use the full config object
console.log(config);

// Or use specific parts
if (features.rateLimit) {
  setupRateLimiting(database);
}
```

#### Import Attributes

You can also use import attributes to load any file as TOML:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import myConfig from "./my.config" with { type: "toml" };
```

### CommonJS

TOML files can also be required in CommonJS:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
const config = require("./config.toml");
console.log(config.database.name); // "myapp"

// Destructuring also works
const { database, redis } = require("./config.toml");
console.log(database.port); // 5432
```

* * *

## Hot Reloading with TOML

When you run your application with `bun --hot`, changes to TOML files are automatically detected and reloaded without restarting:

config.toml

```
[server]
port = 3000
host = "localhost"

[features]
debug = true
verbose = false
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
import { server, features } from "./config.toml";

console.log(`Starting server on ${server.host}:${server.port}`);

Bun.serve({
  port: server.port,
  hostname: server.host,
  fetch(req) {
    if (features.verbose) {
      console.log(`${req.method} ${req.url}`);
    }
    return new Response("Hello World");
  },
});
```

Run with hot reloading:

terminal

```
bun --hot server.ts
```

Now when you modify `config.toml`, the changes are immediately reflected in your running application.

* * *

## Bundler Integration

When you import TOML files and bundle with Bun, the TOML is parsed at build time and included as a JavaScript module:

terminal

```
bun build app.ts --outdir=dist
```

This means:

*   Zero runtime TOML parsing overhead in production
*   Smaller bundle sizes
*   Tree-shaking support for unused properties (named imports)

### Dynamic Imports

TOML files can be dynamically imported:

```
const config = await import("./config.toml");
```
