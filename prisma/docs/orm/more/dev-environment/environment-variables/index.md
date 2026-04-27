---
title: "Environment variables"
source: "https://www.prisma.io/docs/orm/more/dev-environment/environment-variables"
canonical_url: "https://www.prisma.io/docs/orm/more/dev-environment/environment-variables"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-27T19:37:32.048Z"
content_hash: "2367755ce77a040e3d7ccd1fa606d6f06886eff2288a8fd858c018b6ec509821"
menu_path: ["Environment variables"]
section_path: []
tab_variants: ["Command Prompt","PowerShell","Command Prompt","PowerShell"]
content_language: "en"
---
An environment variable is a key value pair of string data that is stored on your machine's local environment. Refer to our [Environment variables reference documentation](https://www.prisma.io/docs/orm/reference/environment-variables-reference) for specific details.

Typically the name of the variable is uppercase, this is then followed by an equals sign then the value of the variable:

```
MY_VALUE=prisma
```

The environment variable belongs to the environment where a process is running. Any program can read and create these environment variables. They are a cheap and effective way to store simple information.

Prisma ORM always reads environment variables from the system's environment.

When you initialize Prisma ORM in your project with `prisma init`, it creates a convenience `.env` file for you to set your [`connection url`](https://www.prisma.io/docs/orm/reference/connection-urls) as an environment variable. When you use Prisma CLI or Prisma Client, the `.env` file content and the variables defined in it are added to the [`process.env` object](https://nodejs.org/api/process.html#processenv), where Prisma ORM can read it and use it.

### [Using an `.env` file](#using-an-env-file)

The Prisma CLI looks for `.env` files, in order, in the following locations:

1.  In the root folder of your project (`./.env`)
2.  From the same folder as the schema specified by the `--schema` argument
3.  From the same folder as the schema taken from `"prisma": {"schema": "/path/to/schema.prisma"}` in `package.json`
4.  From the `./prisma` folder

If a `.env` file is located in step 1., but additional, clashing `.env` variables are located in steps 2. - 4., the CLI will throw an error. For example, if you specify a `DATABASE_URL` variable in two different `.env` files, you will get the following error:

```
Error: There is a conflict between env vars in .env and prisma/.env
Conflicting env vars:
  DATABASE_URL

We suggest to move the contents of prisma/.env to .env to consolidate your env vars.
```

The following table describes where the Prisma CLI looks for the `.env` file:

| **Command** | **schema location** | **`.env` file locations checked, in order** |
| --- | --- | --- |
| `prisma [command]` | `./prisma/schema.prisma` | `./.env`  
`./prisma/.env` |
| `prisma [command] --schema=./a/b/schema.prisma` | `./a/b/schema.prisma` | `./.env`  
`./a/b/.env`  
`./prisma/.env` |
| `prisma [command]` | `"prisma": {"schema": "/path/to/schema.prisma"}` | `.env`  
`./path/to/schema/.env`  
`./prisma/.env` |
| `prisma [command]` | No schema (for example, when running `prisma db pull` in an empty directory) | `./.env`  
`./prisma/.env` |

Any environment variables defined in that `.env` file will automatically be loaded when running a Prisma CLI command.

Refer to the `dotenv` documentation for information about [what happens if an environment variable is defined in two places](https://www.npmjs.com/package/dotenv#what-happens-to-environment-variables-that-were-already-set).

#### [Expanding variables with `.env` files](#expanding-variables-with-env-files)

Variables stored in `.env` files can be expanded using the format specified by [dotenv-expand](https://github.com/motdotla/dotenv-expand).

.env

```
DATABASE_URL=postgresql://test:test@localhost:5432/test
DATABASE_URL_WITH_SCHEMA=${DATABASE_URL}?schema=public
```

Additionally, you can use environment variables in the expansion that are set _outside_ of the `.env` file. For example a database URL that is set on a PaaS like Heroku or similar:

```
# environment variable already set in the environment of the system
export DATABASE_URL=postgresql://test:test@localhost:5432/test
```

.env

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

-   `.env.development`
-   `.env.sample`

Then using a package like [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli), you can load the correct connection URL for the environment you are working in.

1.  Rename your `.env` file to `.env.development`

.env.development

```
DATABASE_URL="postgresql://prisma:prisma@localhost:5433/dev"
```

2.  Create a new `.env.sample` file and change the database name to `sample` (or your preferred name)

.env.sample

```
DATABASE_URL="postgresql://prisma:prisma@localhost:5433/sample"
```

3.  Install [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli)

In order for Prisma ORM and Jest to know which `.env` file to use, alter your `package.json` scripts to include and call the `dotenv` package and specify which file to use depending on what commands you are running and in which environment you want them to run.

#### [Running migrations on different environments](#running-migrations-on-different-environments)

You can use the [`dotenv-cli`](https://www.npmjs.com/package/dotenv-cli) package to specify which environment file Prisma ORM should use when running a migration.

The below script uses `dotenv-cli` to pass the `.env.sample` environment file (which holds a `DATABASE_URL` connection string) to the Prisma ORM migration script.

#### [Migration script](#migration-script)

package.json

```
  "scripts": {
    "migrate:postgres": "dotenv -e .env.sample -- npx prisma migrate deploy",
  },
```

#### [Running tests on different environments](#running-tests-on-different-environments)

When running tests, we advise you to [mock Prisma Client](https://www.prisma.io/docs/orm/prisma-client/testing/unit-testing#mocking-prisma-client). In doing so, you need to tell Jest which environment it should use when running its tests.

By default, Prisma Client will use the environment specified in the default `.env` file located at the project's root.

If you have created a separate `.env.sample` file to specify your testing database, then this environment will need to be passed to Jest.

The below script uses `dotenv-cli` to pass the `.env.sample` environment file (which holds a `DATABASE_URL` connection string) to Jest.

package.json

```
  "scripts": {
    "test": "dotenv -e .env.sample -- jest -i"
  },
```
