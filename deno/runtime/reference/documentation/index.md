---
title: "Documentation Tests"
source: "https://docs.deno.com/runtime/reference/documentation/"
canonical_url: "https://docs.deno.com/runtime/reference/documentation/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:36:18.818Z"
content_hash: "182d79029a627b402796eea406e06de4b676643e92bfb635509e5a6935a48fed"
menu_path: ["Documentation Tests"]
section_path: []
content_language: "en"
nav_prev: {"path": "../jsx/index.md", "title": "JSX"}
nav_next: {"path": "../bundling/index.md", "title": "Bundling"}
---

Deno supports both type-checking evaluating your documentation examples.

This makes sure that examples within your documentation are up to date and working.

The basic idea is this:

```ts
/**
 * # Examples
 *
 * ```ts
 * const x = 42;
 * ```
 */
```

The triple backticks mark the start and end of code blocks, the language is determined by the language identifier attribute which may be any of the following:

-   `js`
-   `javascript`
-   `mjs`
-   `cjs`
-   `jsx`
-   `ts`
-   `typescript`
-   `mts`
-   `cts`
-   `tsx`

If no language identifier is specified then the language is inferred from media type of the source document that the code block is extracted from.

Another attribute supported is `ignore`, which tells the test runner to skip type-checking the code block.

```ts
/**
 * # Does not pass type check
 *
 * ```typescript ignore
 * const x: string = 42;
 * ```
 */
```

If this example was in a file named foo.ts, running `deno test --doc foo.ts` will extract this example, and then both type-check and evaluate it as a standalone module living in the same directory as the module being documented.

To document your exports, import the module using a relative path specifier:

```ts
/**
 * # Examples
 *
 * ```ts
 * import { foo } from "./foo.ts";
 * ```
 */
export function foo(): string {
  return "foo";
}
```

For more guides on testing in Deno, check out:

-   [Basic testing tutorial](/examples/testing_tutorial/)
-   [Mocking data in tests tutorial](/examples/mocking_tutorial/)
-   [Testing web applications tutorial](/examples/web_testing_tutorial/)
