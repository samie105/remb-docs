---
title: "tty - Node documentation"
source: "https://docs.deno.com/api/node/tty/"
canonical_url: "https://docs.deno.com/api/node/tty/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:46.115Z"
content_hash: "1544383eb605a91e43a11548f85325ebfad1f825d865682f435434458f50b61c"
menu_path: ["tty - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/trace_events/index.md", "title": "trace_events - Node documentation"}
nav_next: {"path": "deno/deno/api/node/url/index.md", "title": "url - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:tty";
```

The `node:tty` module provides the `tty.ReadStream` and `tty.WriteStream` classes. In most cases, it will not be necessary or possible to use this module directly. However, it can be accessed using:

```js
import tty from 'node:tty';
```

When Node.js detects that it is being run with a text terminal ("TTY") attached, `process.stdin` will, by default, be initialized as an instance of `tty.ReadStream` and both `process.stdout` and `process.stderr` will, by default, be instances of `tty.WriteStream`. The preferred method of determining whether Node.js is being run within a TTY context is to check that the value of the `process.stdout.isTTY` property is `true`:

```console
$ node -p -e "Boolean(process.stdout.isTTY)"
true
$ node -p -e "Boolean(process.stdout.isTTY)" | cat
false
```

In most cases, there should be little to no reason for an application to manually create instances of the `tty.ReadStream` and `tty.WriteStream` classes.

### Classes [#](#Classes)

c

[ReadStream](.././tty/~/ReadStream "ReadStream")

Represents the readable side of a TTY. In normal circumstances `process.stdin` will be the only `tty.ReadStream` instance in a Node.js process and there should be no reason to create additional instances.

*   [isRaw](.././tty/~/ReadStream#property_israw)
*   [isTTY](.././tty/~/ReadStream#property_istty)
*   [setRawMode](.././tty/~/ReadStream#method_setrawmode_0)

c

[WriteStream](.././tty/~/WriteStream "WriteStream")

Represents the writable side of a TTY. In normal circumstances, `process.stdout` and `process.stderr` will be the only`tty.WriteStream` instances created for a Node.js process and there should be no reason to create additional instances.

*   [addListener](.././tty/~/WriteStream#method_addlistener_0)
*   [clearLine](.././tty/~/WriteStream#method_clearline_0)
*   [clearScreenDown](.././tty/~/WriteStream#method_clearscreendown_0)
*   [columns](.././tty/~/WriteStream#property_columns)
*   [cursorTo](.././tty/~/WriteStream#method_cursorto_0)
*   [emit](.././tty/~/WriteStream#method_emit_0)
*   [getColorDepth](.././tty/~/WriteStream#method_getcolordepth_0)
*   [getWindowSize](.././tty/~/WriteStream#method_getwindowsize_0)
*   [hasColors](.././tty/~/WriteStream#method_hascolors_0)
*   [isTTY](.././tty/~/WriteStream#property_istty)
*   [moveCursor](.././tty/~/WriteStream#method_movecursor_0)
*   [on](.././tty/~/WriteStream#method_on_0)
*   [once](.././tty/~/WriteStream#method_once_0)
*   [prependListener](.././tty/~/WriteStream#method_prependlistener_0)
*   [prependOnceListener](.././tty/~/WriteStream#method_prependoncelistener_0)
*   [rows](.././tty/~/WriteStream#property_rows)

### Functions [#](#Functions)

f

[isatty](.././tty/~/isatty "isatty")

The `tty.isatty()` method returns `true` if the given `fd` is associated with a TTY and `false` if it is not, including whenever `fd` is not a non-negative integer.

### Type Aliases [#](<#Type Aliases>)

T

[Direction](.././tty/~/Direction "Direction")

\-1 - to the left from cursor 0 - the entire line 1 - to the right from cursor
