---
title: "Environment variables"
source: "https://www.prisma.io/docs/orm/more/dev-environment/environment-variables"
canonical_url: "https://www.prisma.io/docs/orm/more/dev-environment/environment-variables"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:59.741Z"
content_hash: "295c6e8ab7fbf59168a39c923f738e726cd2e3e7c37692f6767655c37dd29003"
menu_path: ["Environment variables"]
section_path: []
nav_prev: {"path": "prisma/docs/orm/more/comparisons/prisma-and-typeorm/index.md", "title": "TypeORM"}
nav_next: {"path": "prisma/docs/orm/more/troubleshooting/bundler-issues/index.md", "title": "Bundler issues"}
---

# environment variable already set in the environment of the system
export DATABASE_URL=postgresql://test:test@localhost:5432/test
```

```
DATABASE_URL_WITH_SCHEMA=${DATABASE_URL}?schema=foo
```

This will make the environment variable `DATABASE_URL_WITH_SCHEMA` with value `postgresql://test:test@localhost:5432/test?schema=foo` available for Prisma ORM.

### [Using environment variables in your code](#using-environment-variables-in-your-code)

If you want environment variables to be evaluated at runtime, you need to load them manually in your application code (for example, by using [`dotenv`](https://github.com/motdotla/dotenv)):

```
import * as dotenv from "dotenv";

dotenv.config(); // Load the environment variables
console.log(`The connection URL is ${process.env.DATABASE_URL}`);
```

If you are using a custom file name for your environment variables, you can configure `dotenv` to use that filename:

```
import * as dotenv from "dotenv";

var envFile = path.resolve(join(__dirname, "myenv.env"));
dotenv.config({ path: envFile }); // Load the environment variables
console.log(`The connection URL is ${process.env.DATABASE_URL}`);
```

If you need variable expansion across environment files, you can additionally use [`dotenv-expand`](https://github.com/motdotla/dotenv-expand):

```
import * as dotenv from "dotenv";
const dotenvExpand = require("dotenv-expand");

var envFile = path.resolve(join(__dirname, "myenv.env"));
var mySqlEnv = dotenv.config({ path: envFile });
dotenvExpand.expand(mySqlEnv);
```

If you are using multiple `.env` files, you can reference an environment file in your project's code depending on the environment you are running in.

```
import { config } from "dotenv";

const envFile = process.env.NODE_ENV === "development" ? ".env.development" : ".env.production";
config({ path: envFile });
```

### [Manually set environment variables](#manually-set-environment-variables)

Because Prisma ORM reads from the system's environment when looking for environment variables, it's possible to skip using `.env` completely and create them manually on your local system.

#### [Manually set an environment variable on a Mac/Linux system](#manually-set-an-environment-variable-on-a-maclinux-system)

From a terminal on a Unix machine (Mac/Linux), you export the variable as a key value pair.

```
export DATABASE_URL=postgresql://test:test@localhost:5432/test?schema=public
```

Then check that it has been successfully set using `printenv`:

```
printenv DATABASE_URL
```

```
postgresql://test:test@localhost:5432/test?schema=public
```

#### [Manually set an environment variable on a Windows system](#manually-set-an-environment-variable-on-a-windows-system)

The following examples illustrate how to set the environment variable (for the current user) using both Command Prompt (`cmd.exe`) and PowerShell, depending on your preference.

Then check that it has been successfully set:

### [Using multiple `.env` files](#using-multiple-env-files)

There is a risk that your production database could be deleted if you store different connection URLs to each of your environments within a single `.env` file.

One solution is to have multiple `.env` files which each represent different environments. In practice, this means you create a file for each of your environments:

*   `.env.development`
*   `.env.sample`

Then using a package like [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli), you can load the correct connection URL for the environment you are working in.

1.  Rename your `.env` file to `.env.development`

```
DATABASE_URL="postgresql://prisma:prisma@localhost:5433/dev"
```

2.  Create a new `.env.sample` file and change the database name to `sample` (or your preferred name)

```
DATABASE_URL="postgresql://prisma:prisma@localhost:5433/sample"
```

3.  Install [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli)

In order for Prisma ORM and Jest to know which `.env` file to use, alter your `package.json` scripts to include and call the `dotenv` package and specify which file to use depending on what commands you are running and in which environment you want them to run.

#### [Running migrations on different environments](#running-migrations-on-different-environments)

You can use the [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli) package to specify which environment file Prisma ORM should use when running a migration.

The below script uses `dotenv-cli` to pass the `.env.sample` environment file (which holds a `DATABASE_URL` connection string) to the Prisma ORM migration script.

#### [Migration script](#migration-script)

```
  "scripts": {
    "migrate:postgres": "dotenv -e .env.sample -- npx prisma migrate deploy",
  },
```

#### [Running tests on different environments](#running-tests-on-different-environments)

When running tests, we advise you to [mock Prisma Client](prisma/docs/orm/prisma-client/testing/unit-testing/index.md#mocking-prisma-client). In doing so, you need to tell Jest which environment it should use when running its tests.

By default, Prisma Client will use the environment specified in the default `.env` file located at the project's root.

If you have created a separate `.env.sample` file to specify your testing database, then this environment will need to be passed to Jest.

The below script uses `dotenv-cli` to pass the `.env.sample` environment file (which holds a `DATABASE_URL` connection string) to Jest.

```
  "scripts": {
    "test": "dotenv -e .env.sample -- jest -i"
  },
```

