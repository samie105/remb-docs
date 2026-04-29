---
title: "Wasm - Web documentation"
source: "https://docs.deno.com/api/web/wasm"
canonical_url: "https://docs.deno.com/api/web/wasm"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T18:01:22.474Z"
content_hash: "795366668c5af2f5505c5dc085513ea24bc6142e4fc5eb1b652d4722a0fb7fb3"
menu_path: ["Wasm - Web documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../url/index.md", "title": "URL - Web documentation"}
nav_next: {"path": "../websockets/index.md", "title": "WebSockets - Web documentation"}
---

c

[WebAssembly.CompileError](./././~/WebAssembly.CompileError "WebAssembly.CompileError")

The `WebAssembly.CompileError` object indicates an error during WebAssembly decoding or validation.

c

[WebAssembly.Global](./././~/WebAssembly.Global "WebAssembly.Global")

A `WebAssembly.Global` object represents a global variable instance, accessible from both JavaScript and importable/exportable across one or more `WebAssembly.Module` instances. This allows dynamic linking of multiple modules.

-   [value](./././~/WebAssembly.Global#property_value)
-   [valueOf](./././~/WebAssembly.Global#method_valueof_0)

c

[WebAssembly.Instance](./././~/WebAssembly.Instance "WebAssembly.Instance")

A `WebAssembly.Instance` object is a stateful, executable instance of a `WebAssembly.Module`. Instance objects contain all the Exported WebAssembly functions that allow calling into WebAssembly code from JavaScript.

-   [exports](./././~/WebAssembly.Instance#property_exports)

c

[WebAssembly.LinkError](./././~/WebAssembly.LinkError "WebAssembly.LinkError")

The `WebAssembly.LinkError` object indicates an error during module instantiation (besides traps from the start function).

c

[WebAssembly.Memory](./././~/WebAssembly.Memory "WebAssembly.Memory")

The `WebAssembly.Memory` object is a resizable `ArrayBuffer` or `SharedArrayBuffer` that holds the raw bytes of memory accessed by a WebAssembly Instance.

-   [buffer](./././~/WebAssembly.Memory#property_buffer)
-   [grow](./././~/WebAssembly.Memory#method_grow_0)

c

[WebAssembly.Module](./././~/WebAssembly.Module "WebAssembly.Module")

A `WebAssembly.Module` object contains stateless WebAssembly code that has already been compiled by the browser — this can be efficiently shared with Workers, and instantiated multiple times.

-   [customSections](./././~/WebAssembly.Module#method_customsections_0)
-   [exports](./././~/WebAssembly.Module#method_exports_0)
-   [imports](./././~/WebAssembly.Module#method_imports_0)

c

[WebAssembly.RuntimeError](./././~/WebAssembly.RuntimeError "WebAssembly.RuntimeError")

The `WebAssembly.RuntimeError` object is the error type that is thrown whenever WebAssembly specifies a trap.

c

[WebAssembly.Table](./././~/WebAssembly.Table "WebAssembly.Table")

The `WebAssembly.Table()` object is a JavaScript wrapper object — an array-like structure representing a WebAssembly Table, which stores function references. A table created by JavaScript or in WebAssembly code will be accessible and mutable from both JavaScript and WebAssembly.

-   [get](./././~/WebAssembly.Table#method_get_0)
-   [grow](./././~/WebAssembly.Table#method_grow_0)
-   [length](./././~/WebAssembly.Table#property_length)
-   [set](./././~/WebAssembly.Table#method_set_0)

f

[WebAssembly.compile](./././~/WebAssembly.compile "WebAssembly.compile")

The `WebAssembly.compile()` function compiles WebAssembly binary code into a `WebAssembly.Module` object. This function is useful if it is necessary to compile a module before it can be instantiated (otherwise, the `WebAssembly.instantiate()` function should be used).

f

[WebAssembly.compileStreaming](./././~/WebAssembly.compileStreaming "WebAssembly.compileStreaming")

The `WebAssembly.compileStreaming()` function compiles a `WebAssembly.Module` directly from a streamed underlying source. This function is useful if it is necessary to a compile a module before it can be instantiated (otherwise, the `WebAssembly.instantiateStreaming()` function should be used).

f

[WebAssembly.instantiate](./././~/WebAssembly.instantiate "WebAssembly.instantiate")

The WebAssembly.instantiate() function allows you to compile and instantiate WebAssembly code.

f

[WebAssembly.instantiateStreaming](./././~/WebAssembly.instantiateStreaming "WebAssembly.instantiateStreaming")

The `WebAssembly.instantiateStreaming()` function compiles and instantiates a WebAssembly module directly from a streamed underlying source. This is the most efficient, optimized way to load wasm code.

f

[WebAssembly.validate](./././~/WebAssembly.validate "WebAssembly.validate")

The `WebAssembly.validate()` function validates a given typed array of WebAssembly binary code, returning whether the bytes form a valid wasm module (`true`) or not (`false`).

I

[WebAssembly.GlobalDescriptor](./././~/WebAssembly.GlobalDescriptor "WebAssembly.GlobalDescriptor")

The `GlobalDescriptor` describes the options you can pass to `new WebAssembly.Global()`.

-   [mutable](./././~/WebAssembly.GlobalDescriptor#property_mutable)
-   [value](./././~/WebAssembly.GlobalDescriptor#property_value)

I

[WebAssembly.MemoryDescriptor](./././~/WebAssembly.MemoryDescriptor "WebAssembly.MemoryDescriptor")

The `MemoryDescriptor` describes the options you can pass to `new WebAssembly.Memory()`.

-   [initial](./././~/WebAssembly.MemoryDescriptor#property_initial)
-   [maximum](./././~/WebAssembly.MemoryDescriptor#property_maximum)
-   [shared](./././~/WebAssembly.MemoryDescriptor#property_shared)

I

[WebAssembly.ModuleExportDescriptor](./././~/WebAssembly.ModuleExportDescriptor "WebAssembly.ModuleExportDescriptor")

A `ModuleExportDescriptor` is the description of a declared export in a `WebAssembly.Module`.

-   [kind](./././~/WebAssembly.ModuleExportDescriptor#property_kind)
-   [name](./././~/WebAssembly.ModuleExportDescriptor#property_name)

I

[WebAssembly.ModuleImportDescriptor](./././~/WebAssembly.ModuleImportDescriptor "WebAssembly.ModuleImportDescriptor")

A `ModuleImportDescriptor` is the description of a declared import in a `WebAssembly.Module`.

-   [kind](./././~/WebAssembly.ModuleImportDescriptor#property_kind)
-   [module](./././~/WebAssembly.ModuleImportDescriptor#property_module)
-   [name](./././~/WebAssembly.ModuleImportDescriptor#property_name)

I

[WebAssembly.TableDescriptor](./././~/WebAssembly.TableDescriptor "WebAssembly.TableDescriptor")

The `TableDescriptor` describes the options you can pass to `new WebAssembly.Table()`.

-   [element](./././~/WebAssembly.TableDescriptor#property_element)
-   [initial](./././~/WebAssembly.TableDescriptor#property_initial)
-   [maximum](./././~/WebAssembly.TableDescriptor#property_maximum)

I

[WebAssembly.WebAssemblyInstantiatedSource](./././~/WebAssembly.WebAssemblyInstantiatedSource "WebAssembly.WebAssemblyInstantiatedSource")

The value returned from `WebAssembly.instantiate`.

-   [instance](./././~/WebAssembly.WebAssemblyInstantiatedSource#property_instance)
-   [module](./././~/WebAssembly.WebAssemblyInstantiatedSource#property_module)

N

[WebAssembly](./././~/WebAssembly "WebAssembly")

No documentation available

T

[WebAssembly.Exports](./././~/WebAssembly.Exports "WebAssembly.Exports")

No documentation available

T

[WebAssembly.ExportValue](./././~/WebAssembly.ExportValue "WebAssembly.ExportValue")

No documentation available

T

[WebAssembly.ImportExportKind](./././~/WebAssembly.ImportExportKind "WebAssembly.ImportExportKind")

No documentation available

T

[WebAssembly.Imports](./././~/WebAssembly.Imports "WebAssembly.Imports")

No documentation available

T

[WebAssembly.ImportValue](./././~/WebAssembly.ImportValue "WebAssembly.ImportValue")

No documentation available

T

[WebAssembly.ModuleImports](./././~/WebAssembly.ModuleImports "WebAssembly.ModuleImports")

No documentation available

T

[WebAssembly.TableKind](./././~/WebAssembly.TableKind "WebAssembly.TableKind")

No documentation available

T

[WebAssembly.ValueType](./././~/WebAssembly.ValueType "WebAssembly.ValueType")

No documentation available
