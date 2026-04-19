---
title: "wasi - Node documentation"
source: "https://docs.deno.com/api/node/wasi/"
canonical_url: "https://docs.deno.com/api/node/wasi/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:03.781Z"
content_hash: "d56e7a38d7f3657185545d6ee4ad62028f832c3573750051e8329396d0799751"
menu_path: ["wasi - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:wasi";
```

Deno compatibility

All exports are non-functional stubs.

**The `node:wasi` module does not currently provide the** **comprehensive file system security properties provided by some WASI runtimes.** **Full support for secure file system sandboxing may or may not be implemented in** **future. In the mean time, do not rely on it to run untrusted code.**

The WASI API provides an implementation of the [WebAssembly System Interface](https://wasi.dev/) specification. WASI gives WebAssembly applications access to the underlying operating system via a collection of POSIX-like functions.

```js
import { readFile } from 'node:fs/promises';
import { WASI } from 'node:wasi';
import { argv, env } from 'node:process';

const wasi = new WASI({
  version: 'preview1',
  args: argv,
  env,
  preopens: {
    '/local': '/some/real/path/that/wasm/can/access',
  },
});

const wasm = await WebAssembly.compile(
  await readFile(new URL('./demo.wasm', import.meta.url)),
);
const instance = await WebAssembly.instantiate(wasm, wasi.getImportObject());

wasi.start(instance);
```

To run the above example, create a new WebAssembly text format file named `demo.wat`:

```text
(module
    ;; Import the required fd_write WASI function which will write the given io vectors to stdout
    ;; The function signature for fd_write is:
    ;; (File Descriptor, *iovs, iovs_len, nwritten) -> Returns number of bytes written
    (import "wasi_snapshot_preview1" "fd_write" (func $fd_write (param i32 i32 i32 i32) (result i32)))

    (memory 1)
    (export "memory" (memory 0))

    ;; Write 'hello world\n' to memory at an offset of 8 bytes
    ;; Note the trailing newline which is required for the text to appear
    (data (i32.const 8) "hello world\n")

    (func $main (export "_start")
        ;; Creating a new io vector within linear memory
        (i32.store (i32.const 0) (i32.const 8))  ;; iov.iov_base - This is a pointer to the start of the 'hello world\n' string
        (i32.store (i32.const 4) (i32.const 12))  ;; iov.iov_len - The length of the 'hello world\n' string

        (call $fd_write
            (i32.const 1) ;; file_descriptor - 1 for stdout
            (i32.const 0) ;; *iovs - The pointer to the iov array, which is stored at memory location 0
            (i32.const 1) ;; iovs_len - We're printing 1 string stored in an iov - so one.
            (i32.const 20) ;; nwritten - A place in memory to store the number of bytes written
        )
        drop ;; Discard the number of bytes written from the top of the stack
    )
)
```

Use [wabt](https://github.com/WebAssembly/wabt) to compile `.wat` to `.wasm`

```bash
wat2wasm demo.wat
```

### Classes [#](#Classes)

c

[WASI](.././wasi/~/WASI "WASI")

No documentation available

*   [getImportObject](.././wasi/~/WASI#method_getimportobject_0)
*   [initialize](.././wasi/~/WASI#method_initialize_0)
*   [start](.././wasi/~/WASI#method_start_0)
*   [wasiImport](.././wasi/~/WASI#property_wasiimport)

### Interfaces [#](#Interfaces)

I

[WASIOptions](.././wasi/~/WASIOptions "WASIOptions")

No documentation available

*   [args](.././wasi/~/WASIOptions#property_args)
*   [env](.././wasi/~/WASIOptions#property_env)
*   [preopens](.././wasi/~/WASIOptions#property_preopens)
*   [returnOnExit](.././wasi/~/WASIOptions#property_returnonexit)
*   [stderr](.././wasi/~/WASIOptions#property_stderr)
*   [stdin](.././wasi/~/WASIOptions#property_stdin)
*   [stdout](.././wasi/~/WASIOptions#property_stdout)
*   [version](.././wasi/~/WASIOptions#property_version)
