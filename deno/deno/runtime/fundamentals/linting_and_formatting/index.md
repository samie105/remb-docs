---
title: "Linting and formatting"
source: "https://docs.deno.com/runtime/fundamentals/linting_and_formatting/"
canonical_url: "https://docs.deno.com/runtime/fundamentals/linting_and_formatting/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:08.961Z"
content_hash: "6c4c7492d49cbafebfb6d42328e663fd06f4c2f2961b75efdeac5ec07bfc79b3"
menu_path: ["Linting and formatting"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/fundamentals/workspaces/index.md", "title": "Workspaces and monorepos"}
nav_next: {"path": "deno/deno/runtime/fundamentals/http_server/index.md", "title": "Writing an HTTP Server"}
---

# or
deno run -A npm:eslint --init
```

Create an `eslint.config.js`:

```js
// eslint.config.js
import js from "@eslint/js";
import importPlugin from "eslint-plugin-import"; // example plugin

export default [
  js.configs.recommended,
  {
    files: ["**/*.ts", "**/*.js"],
    languageOptions: { globals: { Deno: "readonly" } },
    plugins: { import: importPlugin },
    rules: {
      // e.g. "import/order": "warn"
    },
  },
];
```

To run ESLint run:

\>\_

```sh
deno run -A npm:eslint .
```

Optionally, you can add a task in your `deno.json` to run ESLint:

```json
{
  "tasks": { "eslint": "eslint . --ext .ts,.js" }
}
```

And run it with:

\>\_

```sh
deno task eslint
```

### Prettier

To use Prettier in your Deno projects, your project will need a `node_modules` directory in your project that VSCode extensions can pick up.

Then install the Prettier extension for VSCode and configure it to be your default formatter:

In VSCode:

1.  Open the Command Palette (with Cmd+Shift+P)
2.  Select **Format Document With...**
3.  Select **Configure Default Formatter...**
4.  Select **Prettier - Code formatter**


