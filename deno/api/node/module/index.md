---
title: "module - Node documentation"
source: "https://docs.deno.com/api/node/module/"
canonical_url: "https://docs.deno.com/api/node/module/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:08:34.835Z"
content_hash: "2d54f2d7b1de98436968c48ddc9ecd314d2dcbe2c51cee313aff43e99d8bd2c2"
menu_path: ["module - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/inspector/promises/index.md", "title": "inspector/promises - Node documentation"}
nav_next: {"path": "deno/api/node/net/index.md", "title": "net - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:module";
```

c

I

N

[Module](.././module/~/Module "Module")

No documentation available

-   [children](.././module/~/Module#property_children)
-   [exports](.././module/~/Module#property_exports)
-   [filename](.././module/~/Module#property_filename)
-   [id](.././module/~/Module#property_id)
-   [isPreloading](.././module/~/Module#property_ispreloading)
-   [loaded](.././module/~/Module#property_loaded)
-   [parent](.././module/~/Module#property_parent)
-   [path](.././module/~/Module#property_path)
-   [paths](.././module/~/Module#property_paths)
-   [require](.././module/~/Module#method_require_0)

c

[Module.SourceMap](.././module/~/Module.SourceMap "Module.SourceMap")

No documentation available

-   [findEntry](.././module/~/Module.SourceMap#method_findentry_0)
-   [findOrigin](.././module/~/Module.SourceMap#method_findorigin_0)
-   [payload](.././module/~/Module.SourceMap#property_payload)

f

[Module.createRequire](.././module/~/Module.createRequire "Module.createRequire")

No documentation available

f

[Module.enableCompileCache](.././module/~/Module.enableCompileCache "Module.enableCompileCache")

Enable [module compile cache](https://nodejs.org/docs/latest-v22.x/api/module.html#module-compile-cache) in the current Node.js instance.

f

[Module.findPackageJSON](.././module/~/Module.findPackageJSON "Module.findPackageJSON")

```js
// /path/to/project/packages/bar/bar.js
import { findPackageJSON } from 'node:module';

findPackageJSON('..', import.meta.url);
// '/path/to/project/package.json'
// Same result when passing an absolute specifier instead:
findPackageJSON(new URL('../', import.meta.url));
findPackageJSON(import.meta.resolve('../'));

findPackageJSON('some-package', import.meta.url);
// '/path/to/project/packages/bar/node_modules/some-package/package.json'
// When passing an absolute specifier, you might get a different result if the
// resolved module is inside a subfolder that has nested `package.json`.
findPackageJSON(import.meta.resolve('some-package'));
// '/path/to/project/packages/bar/node_modules/some-package/some-subfolder/package.json'

findPackageJSON('@foo/qux', import.meta.url);
// '/path/to/project/packages/qux/package.json'
```

f

[Module.findSourceMap](.././module/~/Module.findSourceMap "Module.findSourceMap")

`path` is the resolved path for the file for which a corresponding source map should be fetched.

f

[Module.flushCompileCache](.././module/~/Module.flushCompileCache "Module.flushCompileCache")

Flush the [module compile cache](https://nodejs.org/docs/latest-v22.x/api/module.html#module-compile-cache) accumulated from modules already loaded in the current Node.js instance to disk. This returns after all the flushing file system operations come to an end, no matter they succeed or not. If there are any errors, this will fail silently, since compile cache misses should not interfere with the actual operation of the application.

f

[Module.getCompileCacheDir](.././module/~/Module.getCompileCacheDir "Module.getCompileCacheDir")

No documentation available

f

[Module.isBuiltin](.././module/~/Module.isBuiltin "Module.isBuiltin")

No documentation available

f

[Module.register](.././module/~/Module.register "Module.register")

Register a module that exports hooks that customize Node.js module resolution and loading behavior. See [Customization hooks](https://nodejs.org/docs/latest-v22.x/api/module.html#customization-hooks).

f

[Module.runMain](.././module/~/Module.runMain "Module.runMain")

No documentation available

f

[Module.stripTypeScriptTypes](.././module/~/Module.stripTypeScriptTypes "Module.stripTypeScriptTypes")

`module.stripTypeScriptTypes()` removes type annotations from TypeScript code. It can be used to strip type annotations from TypeScript code before running it with `vm.runInContext()` or `vm.compileFunction()`. By default, it will throw an error if the code contains TypeScript features that require transformation such as `Enums`, see [type-stripping](https://nodejs.org/docs/latest-v22.x/api/typescript.md#type-stripping) for more information. When mode is `'transform'`, it also transforms TypeScript features to JavaScript, see [transform TypeScript features](https://nodejs.org/docs/latest-v22.x/api/typescript.md#typescript-features) for more information. When mode is `'strip'`, source maps are not generated, because locations are preserved. If `sourceMap` is provided, when mode is `'strip'`, an error will be thrown.

f

[Module.syncBuiltinESMExports](.././module/~/Module.syncBuiltinESMExports "Module.syncBuiltinESMExports")

The `module.syncBuiltinESMExports()` method updates all the live bindings for builtin `ES Modules` to match the properties of the `CommonJS` exports. It does not add or remove exported names from the `ES Modules`.

f

[Module.wrap](.././module/~/Module.wrap "Module.wrap")

No documentation available

I

[ImportMeta](.././module/~/ImportMeta "ImportMeta")

No documentation available

-   [dirname](.././module/~/ImportMeta#property_dirname)
-   [filename](.././module/~/ImportMeta#property_filename)
-   [resolve](.././module/~/ImportMeta#method_resolve_0)
-   [url](.././module/~/ImportMeta#property_url)

I

[Module.EnableCompileCacheResult](.././module/~/Module.EnableCompileCacheResult "Module.EnableCompileCacheResult")

No documentation available

-   [directory](.././module/~/Module.EnableCompileCacheResult#property_directory)
-   [message](.././module/~/Module.EnableCompileCacheResult#property_message)
-   [status](.././module/~/Module.EnableCompileCacheResult#property_status)

I

[Module.ImportAttributes](.././module/~/Module.ImportAttributes "Module.ImportAttributes")

No documentation available

-   [type](.././module/~/Module.ImportAttributes#property_type)

I

[Module.LoadFnOutput](.././module/~/Module.LoadFnOutput "Module.LoadFnOutput")

No documentation available

-   [format](.././module/~/Module.LoadFnOutput#property_format)
-   [shortCircuit](.././module/~/Module.LoadFnOutput#property_shortcircuit)
-   [source](.././module/~/Module.LoadFnOutput#property_source)

I

[Module.LoadHookContext](.././module/~/Module.LoadHookContext "Module.LoadHookContext")

No documentation available

-   [conditions](.././module/~/Module.LoadHookContext#property_conditions)
-   [format](.././module/~/Module.LoadHookContext#property_format)
-   [importAttributes](.././module/~/Module.LoadHookContext#property_importattributes)

I

[Module.RegisterOptions](.././module/~/Module.RegisterOptions "Module.RegisterOptions")

No documentation available

-   [data](.././module/~/Module.RegisterOptions#property_data)
-   [parentURL](.././module/~/Module.RegisterOptions#property_parenturl)
-   [transferList](.././module/~/Module.RegisterOptions#property_transferlist)

I

[Module.ResolveFnOutput](.././module/~/Module.ResolveFnOutput "Module.ResolveFnOutput")

No documentation available

-   [format](.././module/~/Module.ResolveFnOutput#property_format)
-   [importAttributes](.././module/~/Module.ResolveFnOutput#property_importattributes)
-   [shortCircuit](.././module/~/Module.ResolveFnOutput#property_shortcircuit)
-   [url](.././module/~/Module.ResolveFnOutput#property_url)

I

[Module.ResolveHookContext](.././module/~/Module.ResolveHookContext "Module.ResolveHookContext")

No documentation available

-   [conditions](.././module/~/Module.ResolveHookContext#property_conditions)
-   [importAttributes](.././module/~/Module.ResolveHookContext#property_importattributes)
-   [parentURL](.././module/~/Module.ResolveHookContext#property_parenturl)

I

[Module.SourceMapConstructorOptions](.././module/~/Module.SourceMapConstructorOptions "Module.SourceMapConstructorOptions")

No documentation available

-   [lineLengths](.././module/~/Module.SourceMapConstructorOptions#property_linelengths)

I

[Module.SourceMapPayload](.././module/~/Module.SourceMapPayload "Module.SourceMapPayload")

No documentation available

-   [file](.././module/~/Module.SourceMapPayload#property_file)
-   [mappings](.././module/~/Module.SourceMapPayload#property_mappings)
-   [names](.././module/~/Module.SourceMapPayload#property_names)
-   [sourceRoot](.././module/~/Module.SourceMapPayload#property_sourceroot)
-   [sources](.././module/~/Module.SourceMapPayload#property_sources)
-   [sourcesContent](.././module/~/Module.SourceMapPayload#property_sourcescontent)
-   [version](.././module/~/Module.SourceMapPayload#property_version)

I

[Module.SourceMapping](.././module/~/Module.SourceMapping "Module.SourceMapping")

No documentation available

-   [generatedColumn](.././module/~/Module.SourceMapping#property_generatedcolumn)
-   [generatedLine](.././module/~/Module.SourceMapping#property_generatedline)
-   [originalColumn](.././module/~/Module.SourceMapping#property_originalcolumn)
-   [originalLine](.././module/~/Module.SourceMapping#property_originalline)
-   [originalSource](.././module/~/Module.SourceMapping#property_originalsource)

I

[Module.SourceOrigin](.././module/~/Module.SourceOrigin "Module.SourceOrigin")

No documentation available

-   [columnNumber](.././module/~/Module.SourceOrigin#property_columnnumber)
-   [fileName](.././module/~/Module.SourceOrigin#property_filename)
-   [lineNumber](.././module/~/Module.SourceOrigin#property_linenumber)
-   [name](.././module/~/Module.SourceOrigin#property_name)

I

[Module.StripTypeScriptTypesOptions](.././module/~/Module.StripTypeScriptTypesOptions "Module.StripTypeScriptTypesOptions")

No documentation available

-   [mode](.././module/~/Module.StripTypeScriptTypesOptions#property_mode)
-   [sourceMap](.././module/~/Module.StripTypeScriptTypesOptions#property_sourcemap)
-   [sourceUrl](.././module/~/Module.StripTypeScriptTypesOptions#property_sourceurl)

I

[Require](.././module/~/Require "Require")

No documentation available

-   [cache](.././module/~/Require#property_cache)
-   [extensions](.././module/~/Require#property_extensions)
-   [main](.././module/~/Require#property_main)
-   [resolve](.././module/~/Require#property_resolve)

I

[RequireResolve](.././module/~/RequireResolve "RequireResolve")

No documentation available

-   [paths](.././module/~/RequireResolve#method_paths_0)

I

[RequireResolveOptions](.././module/~/RequireResolveOptions "RequireResolveOptions")

No documentation available

-   [paths](.././module/~/RequireResolveOptions#property_paths)

I

[NodeModule](.././module/~/NodeModule "NodeModule")

No documentation available

I

[NodeRequire](.././module/~/NodeRequire "NodeRequire")

No documentation available

I

[RequireExtensions](.././module/~/RequireExtensions "RequireExtensions")

No documentation available

-   [.js](.././module/~/RequireExtensions#property__js)
-   [.json](.././module/~/RequireExtensions#property__json)
-   [.node](.././module/~/RequireExtensions#property__node)

N

[Module.constants](.././module/~/Module.constants "Module.constants")

No documentation available

N

[Module.constants.compileCacheStatus](.././module/~/Module.constants.compileCacheStatus "Module.constants.compileCacheStatus")

The following constants are returned as the `status` field in the object returned by enableCompileCache to indicate the result of the attempt to enable the [module compile cache](https://nodejs.org/docs/latest-v22.x/api/module.html#module-compile-cache).

T

[Module.InitializeHook](.././module/~/Module.InitializeHook "Module.InitializeHook")

The `initialize` hook provides a way to define a custom function that runs in the hooks thread when the hooks module is initialized. Initialization happens when the hooks module is registered via register.

T

[Module.LoadHook](.././module/~/Module.LoadHook "Module.LoadHook")

The `load` hook provides a way to define a custom method of determining how a URL should be interpreted, retrieved, and parsed. It is also in charge of validating the import attributes.

T

[Module.ModuleFormat](.././module/~/Module.ModuleFormat "Module.ModuleFormat")

No documentation available

T

[Module.ModuleSource](.././module/~/Module.ModuleSource "Module.ModuleSource")

No documentation available

T

[Module.ResolveHook](.././module/~/Module.ResolveHook "Module.ResolveHook")

The `resolve` hook chain is responsible for telling Node.js where to find and how to cache a given `import` statement or expression, or `require` call. It can optionally return a format (such as `'module'`) as a hint to the `load` hook. If a format is specified, the `load` hook is ultimately responsible for providing the final `format` value (and it is free to ignore the hint provided by `resolve`); if `resolve` provides a `format`, a custom `load` hook is required even if only to pass the value to the Node.js default `load` hook.

v

[\_\_dirname](.././module/~/__dirname "__dirname")

The directory name of the current module. This is the same as the `path.dirname()` of the `__filename`.

v

[\_\_filename](.././module/~/__filename "__filename")

The file name of the current module. This is the current module file's absolute path with symlinks resolved.

v

[exports](.././module/~/exports "exports")

The `exports` variable is available within a module's file-level scope, and is assigned the value of `module.exports` before the module is evaluated.

v

[module](.././module/~/module "module")

A reference to the current module.

v

[Module.builtinModules](.././module/~/Module.builtinModules "Module.builtinModules")

A list of the names of all modules provided by Node.js. Can be used to verify if a module is maintained by a third party or not.

v

[Module.constants.compileCacheStatus.ALREADY\_ENABLED](.././module/~/Module.constants.compileCacheStatus.ALREADY_ENABLED "Module.constants.compileCacheStatus.ALREADY_ENABLED")

The compile cache has already been enabled before, either by a previous call to enableCompileCache, or by the `NODE_COMPILE_CACHE=dir` environment variable. The directory used to store the compile cache will be returned in the `directory` field in the returned object.

v

[Module.constants.compileCacheStatus.DISABLED](.././module/~/Module.constants.compileCacheStatus.DISABLED "Module.constants.compileCacheStatus.DISABLED")

Node.js cannot enable the compile cache because the environment variable `NODE_DISABLE_COMPILE_CACHE=1` has been set.

v

[Module.constants.compileCacheStatus.ENABLED](.././module/~/Module.constants.compileCacheStatus.ENABLED "Module.constants.compileCacheStatus.ENABLED")

Node.js has enabled the compile cache successfully. The directory used to store the compile cache will be returned in the `directory` field in the returned object.

v

[Module.constants.compileCacheStatus.FAILED](.././module/~/Module.constants.compileCacheStatus.FAILED "Module.constants.compileCacheStatus.FAILED")

Node.js fails to enable the compile cache. This can be caused by the lack of permission to use the specified directory, or various kinds of file system errors. The detail of the failure will be returned in the `message` field in the returned object.

v

[require](.././module/~/require "require")

No documentation available
