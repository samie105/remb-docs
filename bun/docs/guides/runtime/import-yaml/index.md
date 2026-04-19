---
title: "Import a YAML file"
source: "https://bun.com/docs/guides/runtime/import-yaml"
canonical_url: "https://bun.com/docs/guides/runtime/import-yaml"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:02.445Z"
content_hash: "29fb336010ca765dd458cc42b3e6973b85652445d2863c1d41e7031fbc816182"
menu_path: ["Import a YAML file"]
section_path: []
---
Bun natively supports `.yaml` and `.yml` imports.

config.yaml

```
database:
  host: localhost
  port: 5432
  name: myapp

server:
  port: 3000
  timeout: 30

features:
  auth: true
  rateLimit: true
```

* * *

Import the file like any other source file.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.ts

```
import config from "./config.yaml";

config.database.host; // => "localhost"
config.server.port; // => 3000
config.features.auth; // => true
```

* * *

You can also use named imports to destructure top-level properties:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.ts

```
import { database, server, features } from "./config.yaml";

console.log(database.name); // => "myapp"
console.log(server.timeout); // => 30
console.log(features.rateLimit); // => true
```

* * *

Bun also supports [Import Attributes](https://github.com/tc39/proposal-import-attributes) syntax:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.ts

```
import config from "./config.yaml" with { type: "yaml" };

config.database.port; // => 5432
```

* * *

For parsing YAML strings at runtime, use `Bun.YAML.parse()`:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.ts

```
const yamlString = `
name: John Doe
age: 30
hobbies:
  - reading
  - coding
`;

const data = Bun.YAML.parse(yamlString);
console.log(data.name); // => "John Doe"
console.log(data.hobbies); // => ["reading", "coding"]
```

* * *

## TypeScript Support

To add TypeScript support for your YAML imports, create a declaration file with `.d.ts` appended to the YAML filename (e.g., `config.yaml` → `config.yaml.d.ts`);

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)config.yaml.d.ts

```
const contents: {
  database: {
    host: string;
    port: number;
    name: string;
  };
  server: {
    port: number;
    timeout: number;
  };
  features: {
    auth: boolean;
    rateLimit: boolean;
  };
};

export = contents;
```

* * *

See [Docs > API > YAML](https://bun.com/docs/runtime/yaml) for complete documentation on YAML support in Bun.
