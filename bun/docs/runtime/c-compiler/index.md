---
title: "C Compiler"
source: "https://bun.com/docs/runtime/c-compiler"
canonical_url: "https://bun.com/docs/runtime/c-compiler"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:53.522Z"
content_hash: "33b5614e449cd022e58db2c8c00a0a57e981a49ed5bfe885de09707ab25a3ce3"
menu_path: ["C Compiler"]
section_path: []
nav_prev: {"path": "bun/docs/runtime/bunfig/index.md", "title": "bunfig.toml"}
nav_next: {"path": "bun/docs/runtime/child-process/index.md", "title": "Spawn"}
---

`bun:ffi` has experimental support for compiling and running C from JavaScript with low overhead.

* * *

## Usage (cc in `bun:ffi`)

See the [introduction blog post](https://bun.com/blog/compile-and-run-c-in-js) for more information. JavaScript:

hello.ts

```
import { cc } from "bun:ffi";
import source from "./hello.c" with { type: "file" };

const {
  symbols: { hello },
} = cc({
  source,
  symbols: {
    hello: {
      args: [],
      returns: "int",
    },
  },
});

console.log("What is the answer to the universe?", hello());
```

C source:

hello.c

```
int hello() {
  return 42;
}
```

When you run `hello.js`, it will print:

terminal

```
bun hello.js
What is the answer to the universe? 42
```

Under the hood, `cc` uses [TinyCC](https://bellard.org/tcc/) to compile the C code and then link it with the JavaScript runtime, efficiently converting types in-place.

### Primitive types

The same `FFIType` values in [`dlopen`](../ffi/index.md) are supported in `cc`.

`FFIType`

C Type

Aliases

cstring

`char*`

function

`(void*)(*)()`

`fn`, `callback`

ptr

`void*`

`pointer`, `void*`, `char*`

i8

`int8_t`

`int8_t`

i16

`int16_t`

`int16_t`

i32

`int32_t`

`int32_t`, `int`

i64

`int64_t`

`int64_t`

i64\_fast

`int64_t`

u8

`uint8_t`

`uint8_t`

u16

`uint16_t`

`uint16_t`

u32

`uint32_t`

`uint32_t`

u64

`uint64_t`

`uint64_t`

u64\_fast

`uint64_t`

f32

`float`

`float`

f64

`double`

`double`

bool

`bool`

char

`char`

napi\_env

`napi_env`

napi\_value

`napi_value`

### Strings, objects, and non-primitive types

To make it easier to work with strings, objects, and other non-primitive types that don’t map 1:1 to C types, `cc` supports N-API. To pass or receive a JavaScript values without any type conversions from a C function, you can use `napi_value`. You can also pass a `napi_env` to receive the N-API environment used to call the JavaScript function.

#### Returning a C string to JavaScript

For example, if you have a string in C, you can return it to JavaScript like this:

hello.ts

```
import { cc } from "bun:ffi";
import source from "./hello.c" with { type: "file" };

const {
  symbols: { hello },
} = cc({
  source,
  symbols: {
    hello: {
      args: ["napi_env"],
      returns: "napi_value",
    },
  },
});

const result = hello();
```

And in C:

hello.c

```
#include <node/node_api.h>

napi_value hello(napi_env env) {
  napi_value result;
  napi_create_string_utf8(env, "Hello, Napi!", NAPI_AUTO_LENGTH, &result);
  return result;
}
```

You can also use this to return other types like objects and arrays:

hello.c

```
#include <node/node_api.h>

napi_value hello(napi_env env) {
  napi_value result;
  napi_create_object(env, &result);
  return result;
}
```

### `cc` Reference

#### `library: string[]`

Use the `library` array to specify the libraries to link with the C code.

```
type Library = string[];

cc({
  source: "hello.c",
  library: ["sqlite3"],
});
```

#### `symbols`

Use the `symbols` object to specify the functions and variables to expose to JavaScript.

```
type Symbols = {
  [key: string]: {
    args: FFIType[];
    returns: FFIType;
  };
};
```

#### `source`

The `source` is a file path to the C code that should be compiled and linked with the JavaScript runtime.

```
type Source = string | URL | BunFile;

cc({
  source: "hello.c",
  symbols: {
    hello: {
      args: [],
      returns: "int",
    },
  },
});
```

#### `flags: string | string[]`

The `flags` is an optional array of strings that should be passed to the TinyCC compiler.

```
type Flags = string | string[];
```

These are flags like `-I` for include directories and `-D` for preprocessor definitions.

#### `define: Record<string, string>`

The `define` is an optional object that should be passed to the TinyCC compiler.

```
type Defines = Record<string, string>;

cc({
  source: "hello.c",
  define: {
    NDEBUG: "1",
  },
});
```

These are preprocessor definitions passed to the TinyCC compiler.
