---
title: "I/O - Deno documentation"
source: "https://docs.deno.com/api/deno/io"
canonical_url: "https://docs.deno.com/api/deno/io"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:53:32.684Z"
content_hash: "a5f0005df647dedb12d4f86668b2f86fa2a3ba41c0c0772e53fd27e48f7831fd"
menu_path: ["I/O - Deno documentation"]
section_path: []
content_language: "en"
---
E

[Deno.SeekMode](./././~/Deno.SeekMode "Deno.SeekMode")

A enum which defines the seek mode for IO related APIs that support seeking.

f

[Deno.consoleSize](./././~/Deno.consoleSize "Deno.consoleSize")

Gets the size of the console as columns/rows.

f

[Deno.inspect](./././~/Deno.inspect "Deno.inspect")

Converts the input into a string that has the same format as printed by `console.log()`.

I

[Deno.InspectOptions](./././~/Deno.InspectOptions "Deno.InspectOptions")

Option which can be specified when performing [`Deno.inspect`](./././~/Deno.inspect).

-   [breakLength](./././~/Deno.InspectOptions#property_breaklength)
-   [colors](./././~/Deno.InspectOptions#property_colors)
-   [compact](./././~/Deno.InspectOptions#property_compact)
-   [depth](./././~/Deno.InspectOptions#property_depth)
-   [escapeSequences](./././~/Deno.InspectOptions#property_escapesequences)
-   [getters](./././~/Deno.InspectOptions#property_getters)
-   [iterableLimit](./././~/Deno.InspectOptions#property_iterablelimit)
-   [showHidden](./././~/Deno.InspectOptions#property_showhidden)
-   [showProxy](./././~/Deno.InspectOptions#property_showproxy)
-   [sorted](./././~/Deno.InspectOptions#property_sorted)
-   [strAbbreviateSize](./././~/Deno.InspectOptions#property_strabbreviatesize)
-   [trailingComma](./././~/Deno.InspectOptions#property_trailingcomma)

I

[Deno.SetRawOptions](./././~/Deno.SetRawOptions "Deno.SetRawOptions")

No documentation available

-   [cbreak](./././~/Deno.SetRawOptions#property_cbreak)

v

[Deno.stderr](./././~/Deno.stderr "Deno.stderr")

A reference to `stderr` which can be used to write directly to `stderr`. It implements the Deno specific [`Writer`](https://jsr.io/@std/io/doc/types/~/Writer), [`WriterSync`](https://jsr.io/@std/io/doc/types/~/WriterSync), and [`Closer`](https://jsr.io/@std/io/doc/types/~/Closer) interfaces as well as provides a `WritableStream` interface.

-   [close](./././~/Deno.stderr#method_close_0)
-   [isTerminal](./././~/Deno.stderr#method_isterminal_0)
-   [writable](./././~/Deno.stderr#property_writable)
-   [write](./././~/Deno.stderr#method_write_0)
-   [writeSync](./././~/Deno.stderr#method_writesync_0)

v

[Deno.stdin](./././~/Deno.stdin "Deno.stdin")

A reference to `stdin` which can be used to read directly from `stdin`.

-   [close](./././~/Deno.stdin#method_close_0)
-   [isTerminal](./././~/Deno.stdin#method_isterminal_0)
-   [read](./././~/Deno.stdin#method_read_0)
-   [readSync](./././~/Deno.stdin#method_readsync_0)
-   [readable](./././~/Deno.stdin#property_readable)
-   [setRaw](./././~/Deno.stdin#method_setraw_0)

v

[Deno.stdout](./././~/Deno.stdout "Deno.stdout")

A reference to `stdout` which can be used to write directly to `stdout`. It implements the Deno specific [`Writer`](https://jsr.io/@std/io/doc/types/~/Writer), [`WriterSync`](https://jsr.io/@std/io/doc/types/~/WriterSync), and [`Closer`](https://jsr.io/@std/io/doc/types/~/Closer) interfaces as well as provides a `WritableStream` interface.

-   [close](./././~/Deno.stdout#method_close_0)
-   [isTerminal](./././~/Deno.stdout#method_isterminal_0)
-   [writable](./././~/Deno.stdout#property_writable)
-   [write](./././~/Deno.stdout#method_write_0)
-   [writeSync](./././~/Deno.stdout#method_writesync_0)
