---
title: "Seeding"
source: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding"
canonical_url: "https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:41:46.788Z"
content_hash: "70829becede5a64cc321787060c53c71ff576de02b98352e4703cce50df60074"
menu_path: ["Seeding"]
section_path: []
tab_variants: ["npm","pnpm","yarn","bun","npm","pnpm","yarn","bun","npm","pnpm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "../prototyping-your-schema/index.md", "title": "Prototyping your schema"}
nav_next: {"path": "../squashing-migrations/index.md", "title": "Squashing migrations"}
---

# -e Exit immediately when a command returns a non-zero status.
# -x Print commands before they are executed
set -ex
# Seeding command go
run ./seed/
```

The following example uses [psql](https://www.postgresql.org/docs/13/app-psql.html) to run a SQL script in the same folder as `seed.sh`:

seed.sh

```
#!/bin/sh
# -e Exit immediately when a command returns a non-zero status.
# -x Print commands before they are executed
set -ex
# Seeding command
psql file.sql
```

### [User-defined arguments](#user-defined-arguments)

`prisma db seed` allows you to define custom arguments in your seed file that you can pass to the `prisma db seed` command. For example, you could define your own arguments to seed different data for different environments or partially seeding data in some tables.

Here is an example seed file that defines a custom argument to seed different data in different environments:

seed.js

```
import { parseArgs } from "node:util";

const options = {
  environment: { type: "string" },
};

async function main() {
  const {
    values: { environment },
  } = parseArgs({ options });

  switch (environment) {
    case "development":
      /** data for your development */
      break;
    case "test":
      /** data for your test environment */
      break;
    default:
      break;
  }
}

main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
```

You can then provide the `environment` argument when using `prisma db seed` by adding a [delimiter](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_02) — `--` —, followed by your custom arguments:

Here's a non-exhaustive list of other tools you can integrate with Prisma ORM in your development workflow to seed your database:

-   [Supabase community project](https://github.com/supabase-community/seed)
-   [Replibyte](https://www.replibyte.com/docs/introduction/)
