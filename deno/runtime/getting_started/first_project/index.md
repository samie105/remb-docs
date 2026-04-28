---
title: "Making a Deno project"
source: "https://docs.deno.com/runtime/getting_started/first_project/"
canonical_url: "https://docs.deno.com/runtime/getting_started/first_project/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:23:44.499Z"
content_hash: "abf40ba77eb39ebd1f098a43ee6ab7f6aab71ab56ca68d9afac85213fcd803e1"
menu_path: ["Making a Deno project"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/getting_started/installation/index.md", "title": "Installation"}
nav_next: {"path": "deno/runtime/getting_started/setup_your_environment/index.md", "title": "Set up your environment"}
---

**On this page**

-   [Initialize a new project](#initialize-a-new-project)
-   [Run your project](#run-your-project)
-   [Run your tests](#run-your-tests)

Deno has many [built in tools](/runtime/reference/cli/) to make your development experience as smooth as possible. One of these tools is the [project initializer](/runtime/reference/cli/init), which creates a new Deno project with a basic file structure and configuration.

While you are welcome to use JavaScript, Deno has built-in support for [TypeScript](https://www.typescriptlang.org/) as well, so we'll be using TypeScript in this guide. If you'd prefer to use JavaScript, you can rename the files to `.js` and remove the type annotations.

## Initialize a new project

To initialize a new Deno project, run the following command in your terminal:

\>\_

```bash
deno init my_project
```

This will create a new directory called `my_project` with the following structure:

```plaintext
my_project
├── deno.json
├── main_test.ts
└── main.ts
```

A `deno.json` file is created to [configure your project](/runtime/fundamentals/configuration/), and two TypeScript files are created; `main.ts` and `main_test.ts`. The `main.ts` file is where you'll write your application code, on initial creation it will contain a simple program which adds two numbers together. The `main_test.ts` file is where you can write tests, initially it will contain a test for your addition program.

## Run your project

You can run this program with the following command:

\>\_

```bash
$ deno main.ts
Add 2 + 3 = 5
```

## Run your tests

Deno has a [built in test runner](/runtime/fundamentals/testing/). You can write tests for your code and run them with the `deno test` command. Run the tests in your new project with:

\>\_

```bash
$ deno test
running 1 test from ./main_test.ts     
addTest ... ok (1ms)

ok | 1 passed | 0 failed (3ms)
```

Now that you have a basic project set up you can start building your application. Check out our [examples and tutorials](/examples/) for more ideas on what to build with Deno.

You can [learn more about using TypeScript in Deno here](/runtime/fundamentals/typescript).
