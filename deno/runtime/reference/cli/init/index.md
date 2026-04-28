---
title: "deno init"
source: "https://docs.deno.com/runtime/reference/cli/init/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/init/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:30:02.606Z"
content_hash: "2eb4bde59d0a2a6660efc09311909ad6426421be4f3890ceebaf27744bf6aec0"
menu_path: ["deno init"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/info/index.md", "title": "deno info"}
nav_next: {"path": "deno/runtime/reference/cli/install/index.md", "title": "deno install"}
---

**On this page**

-   [Examples](#examples)
-   [Init a JSR package](#init-a-jsr-package)
-   [Initialize a web server](#initialize-a-web-server)
-   [Initialize an empty project](#initialize-an-empty-project)
-   [Generate a library project](#generate-a-library-project)
-   [Options](#options)

## Examples

\>\_

```sh
deno init
✅ Project initialized
Run these commands to get started

  // Run the program
  deno run main.ts

  // Run the program and watch for file changes
  deno task dev

  // Run the tests
  deno test

deno run main.ts
Add 2 + 3 = 5

deno test
Check file:///dev/main_test.ts
running 1 test from main_test.ts
addTest ... ok (6ms)

ok | 1 passed | 0 failed (29ms)
```

The `init` subcommand will create two files (`main.ts` and `main_test.ts`). These files provide a basic example of how to write a Deno program and how to write tests for it. The `main.ts` file exports a `add` function that adds two numbers together and the `main_test.ts` file contains a test for this function.

You can also specify an argument to `deno init` to initialize a project in a specific directory:

\>\_

```sh
deno init my_deno_project
✅ Project initialized

Run these commands to get started

  cd my_deno_project

  // Run the program
  deno run main.ts

  // Run the program and watch for file changes
  deno task dev

  // Run the tests
  deno test
```

## Init a JSR package

By running `deno init --lib` Deno will bootstrap a project that is ready to be published on [JSR](https://jsr.io/).

\>\_

```sh
deno init --lib
✅ Project initialized

Run these commands to get started

  # Run the tests
  deno test

  # Run the tests and watch for file changes
  deno task dev

  # Publish to JSR (dry run)
  deno publish --dry-run
```

Inside `deno.json` you'll see that the entries for `name`, `exports` and `version` are prefilled.

deno.json

```json
{
  "name": "my-lib",
  "version": "0.1.0",
  "exports": "./mod.ts",
  "tasks": {
    "dev": "deno test --watch mod.ts"
  },
  "imports": {
    "@std/assert": "jsr:@std/assert@1"
  }
}
```

## Initialize a web server

Running `deno init --serve` bootstraps a web server that works with [`deno serve`](/runtime/reference/cli/serve).

\>\_

```sh
deno init --serve
✅ Project initialized

Run these commands to get started

  # Run the server
  deno serve -R main.ts

  # Run the server and watch for file changes
  deno task dev

  # Run the tests
  deno -R test
```

Your [`deno.json`](/runtime/fundamentals/configuration/) file will look like this:

deno.json

```json
{
  "tasks": {
    "dev": "deno serve --watch -R main.ts"
  },
  "imports": {
    "@std/assert": "jsr:@std/assert@1",
    "@std/http": "jsr:@std/http@1"
  }
}
```

Now, you can start your web server, which [watches for changes](/runtime/getting_started/command_line_interface/#watch-mode), by running `deno task dev`.

\>\_

```sh
deno task dev
Task dev deno serve --watch -R main.ts
Watcher Process started.
deno serve: Listening on http://0.0.0.0:8000/
```

## Initialize an empty project

Running `deno init --empty` bootstraps an empty project with a basic console log.

\>\_

```sh
deno init --empty
✅ Project initialized

Run these commands to get started

  # Run the program
  deno run main.ts

  # Run the program and watch for file changes
  deno task dev
```

Your [`deno.json`](/runtime/fundamentals/configuration/) file will look like this:

deno.json

```json
{
  "tasks": {
    "dev": "deno run --watch main.ts"
  }
}
```

Now, you can run the project, which [watches for changes](/runtime/getting_started/command_line_interface/#watch-mode), by running `deno task dev`.

\>\_

```sh
deno task dev
Task dev deno run --watch main.ts
Watcher Process started.
Hello world!
```

## Generate a library project

You can append a `--lib` flag to add extra parameters to your `deno.json`, such as "name", "version" and an "exports" fields.

\>\_

```sh
deno init my_deno_project --lib
✅ Project initialized
```

The resulting `deno.json` will be as follows:

deno.json

```jsonc
{
  "name": "my_deno_project",
  "version": "0.1.0",
  "exports": "./mod.ts",
  "tasks": {
    "dev": "deno test --watch mod.ts"
  },
  "license": "MIT",
  "imports": {
    "@std/assert": "jsr:@std/assert@1"
  }
}
```

Command line usage:

```
deno init [OPTIONS] [DIRECTORY OR PACKAGE]...
```

scaffolds a basic Deno project with a script, test, and configuration file

## Options

`--empty`

Generate a minimal project with just main.ts and deno.json.

`--jsr`

Generate a project from a JSR package.

`--lib`

Generate an example library project.

`--npm`

Generate a npm create-\* project.

`--serve`

Generate an example project for `deno serve`.

`--yes, -y`

Bypass the prompt and run with full permissions.
