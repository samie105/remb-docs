---
title: "console - Node documentation"
source: "https://docs.deno.com/api/node/console/"
canonical_url: "https://docs.deno.com/api/node/console/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:15.370Z"
content_hash: "a5f8a24cf17e810ba80f5e95451a03edf2b85844900a50dea5d0d11a5b6b5464"
menu_path: ["console - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:console";
```

The `node:console` module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

The module exports two specific components:

*   A `Console` class with methods such as `console.log()`, `console.error()`, and `console.warn()` that can be used to write to any Node.js stream.
*   A global `console` instance configured to write to [`process.stdout`](https://nodejs.org/docs/latest-v22.x/api/process.html#processstdout) and [`process.stderr`](https://nodejs.org/docs/latest-v22.x/api/process.html#processstderr). The global `console` can be used without importing the `node:console` module.

_**Warning**_: The global console object's methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. See the [`note on process I/O`](https://nodejs.org/docs/latest-v22.x/api/process.html#a-note-on-process-io) for more information.

Example using the global `console`:

```js
console.log('hello world');
// Prints: hello world, to stdout
console.log('hello %s', 'world');
// Prints: hello world, to stdout
console.error(new Error('Whoops, something bad happened'));
// Prints error message and stack trace to stderr:
//   Error: Whoops, something bad happened
//     at [eval]:5:15
//     at Script.runInThisContext (node:vm:132:18)
//     at Object.runInThisContext (node:vm:309:38)
//     at node:internal/process/execution:77:19
//     at [eval]-wrapper:6:22
//     at evalScript (node:internal/process/execution:76:60)
//     at node:internal/main/eval_string:23:3

const name = 'Will Robinson';
console.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to stderr
```

Example using the `Console` class:

```js
const out = getStreamSomehow();
const err = getStreamSomehow();
const myConsole = new console.Console(out, err);

myConsole.log('hello world');
// Prints: hello world, to out
myConsole.log('hello %s', 'world');
// Prints: hello world, to out
myConsole.error(new Error('Whoops, something bad happened'));
// Prints: [Error: Whoops, something bad happened], to err

const name = 'Will Robinson';
myConsole.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to err
```

### Interfaces [#](#Interfaces)

I

[Console](.././console/~/Console "Console")

No documentation available

*   [Console](.././console/~/Console#property_console)
*   [assert](.././console/~/Console#method_assert_0)
*   [clear](.././console/~/Console#method_clear_0)
*   [count](.././console/~/Console#method_count_0)
*   [countReset](.././console/~/Console#method_countreset_0)
*   [debug](.././console/~/Console#method_debug_0)
*   [dir](.././console/~/Console#method_dir_0)
*   [dirxml](.././console/~/Console#method_dirxml_0)
*   [error](.././console/~/Console#method_error_0)
*   [group](.././console/~/Console#method_group_0)
*   [groupCollapsed](.././console/~/Console#method_groupcollapsed_0)
*   [groupEnd](.././console/~/Console#method_groupend_0)
*   [info](.././console/~/Console#method_info_0)
*   [log](.././console/~/Console#method_log_0)
*   [profile](.././console/~/Console#method_profile_0)
*   [profileEnd](.././console/~/Console#method_profileend_0)
*   [table](.././console/~/Console#method_table_0)
*   [time](.././console/~/Console#method_time_0)
*   [timeEnd](.././console/~/Console#method_timeend_0)
*   [timeLog](.././console/~/Console#method_timelog_0)
*   [timeStamp](.././console/~/Console#method_timestamp_0)
*   [trace](.././console/~/Console#method_trace_0)
*   [warn](.././console/~/Console#method_warn_0)

I

[console.ConsoleConstructor](.././console/~/console.ConsoleConstructor "console.ConsoleConstructor")

No documentation available

*   [prototype](.././console/~/console.ConsoleConstructor#property_prototype)

I

[console.ConsoleConstructorOptions](.././console/~/console.ConsoleConstructorOptions "console.ConsoleConstructorOptions")

No documentation available

*   [colorMode](.././console/~/console.ConsoleConstructorOptions#property_colormode)
*   [groupIndentation](.././console/~/console.ConsoleConstructorOptions#property_groupindentation)
*   [ignoreErrors](.././console/~/console.ConsoleConstructorOptions#property_ignoreerrors)
*   [inspectOptions](.././console/~/console.ConsoleConstructorOptions#property_inspectoptions)
*   [stderr](.././console/~/console.ConsoleConstructorOptions#property_stderr)
*   [stdout](.././console/~/console.ConsoleConstructorOptions#property_stdout)

### Namespaces [#](#Namespaces)

N

v

[console](.././console/~/console "console")

The `console` module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.
