---
title: "Using Wasm modules"
source: "https://supabase.com/docs/guides/functions/wasm"
canonical_url: "https://supabase.com/docs/guides/functions/wasm"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:42.235Z"
content_hash: "756521c7e661a0b1fde5654dfdbd3b80495bd790c4eb8e8e7467764e0935353b"
menu_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","Wasm Modules","Wasm Modules"]
section_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","Wasm Modules","Wasm Modules"]
nav_prev: {"path": "supabase/docs/guides/functions/unit-test/index.md", "title": "Testing your Edge Functions"}
nav_next: {"path": "supabase/docs/guides/functions/websockets/index.md", "title": "Handling WebSockets"}
---

# 

Using Wasm modules

## 

Use WebAssembly in Edge Functions.

* * *

Edge Functions supports running [WebAssembly (Wasm)](https://developer.mozilla.org/en-US/docs/WebAssembly) modules. WebAssembly is useful if you want to optimize code that's slower to run in JavaScript or require low-level manipulation.

This allows you to:

*   Optimize performance-critical code beyond JavaScript capabilities
*   Port existing libraries from other languages (C, C++, Rust) to JavaScript
*   Access low-level system operations not available in JavaScript

For example, libraries like [magick-wasm](../examples/image-manipulation/index.md) port existing C libraries to WebAssembly for complex image processing.

* * *

### Writing a Wasm module[#](#writing-a-wasm-module)

You can use different languages and SDKs to write Wasm modules. For this tutorial, we will write a simple Wasm module in Rust that adds two numbers.

Follow this [guide on writing Wasm modules in Rust](https://developer.mozilla.org/en-US/docs/WebAssembly/Rust_to_Wasm) to setup your dev environment.

1

### Create a new Edge Function

Create a new Edge Function called `wasm-add`

```
1supabase functions new wasm-add
```

2

### Create a new Cargo project

Create a new Cargo project for the Wasm module inside the function's directory:

```
1cd supabase/functions/wasm-add2cargo new --lib add-wasm
```

3

### Add the Wasm module code

Add the following code to `add-wasm/src/lib.rs`.

```
1use wasm_bindgen::prelude::*;23#[wasm_bindgen]4pub fn add(a: u32, b: u32) -> u32 {5    a + b6}
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/wasm-modules/add-wasm/src/lib.rs)

4

### Update the Cargo.toml file

Update the `add-wasm/Cargo.toml` to include the `wasm-bindgen` dependency.

```
1[package]2name = "add-wasm"3version = "0.1.0"4description = "A simple wasm module that adds two numbers"5license = "MIT/Apache-2.0"6edition = "2021"78[lib]9crate-type = ["cdylib"]1011[dependencies]12wasm-bindgen = "0.2"
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/wasm-modules/add-wasm/Cargo.toml)

5

### Build the Wasm module

Build the package by running:

```
1wasm-pack build --target deno
```

This will produce a Wasm binary file inside `add-wasm/pkg` directory.

* * *

## Calling the Wasm module from the Edge Function[#](#calling-the-wasm-module-from-the-edge-function)

Update your Edge Function to call the add function from the Wasm module:

```
1import { add } from './add-wasm/pkg/add_wasm.js'23Deno.serve(async (req) => {4  const { a, b } = await req.json()5  return new Response(JSON.stringify({ result: add(a, b) }), {6    headers: { 'Content-Type': 'application/json' },7  })8})
```

[View source](https://github.com/supabase/supabase/blob/e8df67d5d5291e05ea56596aee0f2b7fa152929b/examples/edge-functions/supabase/functions/wasm-modules/index.ts)

Supabase Edge Functions currently use Deno 1.46. From [Deno 2.1, importing Wasm modules](https://deno.com/blog/v2.1) will require even less boilerplate code.

* * *

## Bundle and deploy[#](#bundle-and-deploy)

Before deploying, ensure the Wasm module is bundled with your function by defining it in `supabase/config.toml`:

*   You will need update Supabase CLI to 2.7.0 or higher for the `static_files` support.
*   Static files cannot be deployed using the `--use-api` API flag. You need to build them with [Docker on the CLI](../quickstart/index.md#step-6-deploy-to-production).

```
1[functions.wasm-add]2static_files = [ "./functions/wasm-add/add-wasm/pkg/*"]
```

Deploy the function by running:

```
1supabase functions deploy wasm-add
```
