---
title: "vm - Node documentation"
source: "https://docs.deno.com/api/node/vm/"
canonical_url: "https://docs.deno.com/api/node/vm/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:05.390Z"
content_hash: "d676b7188f06e78713725be1094ff9bca07fee8f47a8f9e3d7a0c5a1f82977d6"
menu_path: ["vm - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/v8/index.md", "title": "v8 - Node documentation"}
nav_next: {"path": "deno/deno/api/node/wasi/index.md", "title": "wasi - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:vm";
```

The `node:vm` module enables compiling and running code within V8 Virtual Machine contexts.

**The `node:vm` module is not a security** **mechanism. Do not use it to run untrusted code.**

JavaScript code can be compiled and run immediately or compiled, saved, and run later.

A common use case is to run the code in a different V8 Context. This means invoked code has a different global object than the invoking code.

One can provide the context by `contextifying` an object. The invoked code treats any property in the context like a global variable. Any changes to global variables caused by the invoked code are reflected in the context object.

```js
import vm from 'node:vm';

const x = 1;

const context = { x: 2 };
vm.createContext(context); // Contextify the object.

const code = 'x += 40; var y = 17;';
// `x` and `y` are global variables in the context.
// Initially, x has the value 2 because that is the value of context.x.
vm.runInContext(code, context);

console.log(context.x); // 42
console.log(context.y); // 17

console.log(x); // 1; y is not defined.
```

### Classes [#](#Classes)

c

[Module](.././vm/~/Module "Module")

This feature is only available with the `--experimental-vm-modules` command flag enabled.

*   [context](.././vm/~/Module#property_context)
*   [dependencySpecifiers](.././vm/~/Module#property_dependencyspecifiers)
*   [error](.././vm/~/Module#property_error)
*   [evaluate](.././vm/~/Module#method_evaluate_0)
*   [identifier](.././vm/~/Module#property_identifier)
*   [link](.././vm/~/Module#method_link_0)
*   [namespace](.././vm/~/Module#property_namespace)
*   [status](.././vm/~/Module#property_status)

c

[Script](.././vm/~/Script "Script")

No documentation available

*   [cachedData](.././vm/~/Script#property_cacheddata)
*   [cachedDataProduced](.././vm/~/Script#property_cacheddataproduced)
*   [cachedDataRejected](.././vm/~/Script#property_cacheddatarejected)
*   [createCachedData](.././vm/~/Script#method_createcacheddata_0)
*   [runInContext](.././vm/~/Script#method_runincontext_0)
*   [runInNewContext](.././vm/~/Script#method_runinnewcontext_0)
*   [runInThisContext](.././vm/~/Script#method_runinthiscontext_0)
*   [sourceMapURL](.././vm/~/Script#property_sourcemapurl)

c

[SourceTextModule](.././vm/~/SourceTextModule "SourceTextModule")

This feature is only available with the `--experimental-vm-modules` command flag enabled.

c

[SyntheticModule](.././vm/~/SyntheticModule "SyntheticModule")

This feature is only available with the `--experimental-vm-modules` command flag enabled.

*   [setExport](.././vm/~/SyntheticModule#method_setexport_0)

### Functions [#](#Functions)

f

[compileFunction](.././vm/~/compileFunction "compileFunction")

Compiles the given code into the provided context (if no context is supplied, the current context is used), and returns it wrapped inside a function with the given `params`.

f

[createContext](.././vm/~/createContext "createContext")

No documentation available

f

[isContext](.././vm/~/isContext "isContext")

Returns `true` if the given `object` object has been contextified using [createContext](.././vm/~/createContext), or if it's the global object of a context created using `vm.constants.DONT_CONTEXTIFY`.

f

[measureMemory](.././vm/~/measureMemory "measureMemory")

No documentation available

f

[runInContext](.././vm/~/runInContext "runInContext")

The `vm.runInContext()` method compiles `code`, runs it within the context of the `contextifiedObject`, then returns the result. Running code does not have access to the local scope. The `contextifiedObject` object _must_ have been previously `contextified` using the [createContext](.././vm/~/createContext) method.

f

[runInNewContext](.././vm/~/runInNewContext "runInNewContext")

This method is a shortcut to `(new vm.Script(code, options)).runInContext(vm.createContext(options), options)`. If `options` is a string, then it specifies the filename.

f

[runInThisContext](.././vm/~/runInThisContext "runInThisContext")

`vm.runInThisContext()` compiles `code`, runs it within the context of the current `global` and returns the result. Running code does not have access to local scope, but does have access to the current `global` object.

### Interfaces [#](#Interfaces)

I

[BaseOptions](.././vm/~/BaseOptions "BaseOptions")

No documentation available

*   [columnOffset](.././vm/~/BaseOptions#property_columnoffset)
*   [filename](.././vm/~/BaseOptions#property_filename)
*   [lineOffset](.././vm/~/BaseOptions#property_lineoffset)

I

[CompileFunctionOptions](.././vm/~/CompileFunctionOptions "CompileFunctionOptions")

No documentation available

*   [cachedData](.././vm/~/CompileFunctionOptions#property_cacheddata)
*   [contextExtensions](.././vm/~/CompileFunctionOptions#property_contextextensions)
*   [parsingContext](.././vm/~/CompileFunctionOptions#property_parsingcontext)
*   [produceCachedData](.././vm/~/CompileFunctionOptions#property_producecacheddata)

I

[Context](.././vm/~/Context "Context")

No documentation available

I

[CreateContextOptions](.././vm/~/CreateContextOptions "CreateContextOptions")

No documentation available

*   [codeGeneration](.././vm/~/CreateContextOptions#property_codegeneration)
*   [microtaskMode](.././vm/~/CreateContextOptions#property_microtaskmode)
*   [name](.././vm/~/CreateContextOptions#property_name)
*   [origin](.././vm/~/CreateContextOptions#property_origin)

I

[MeasureMemoryOptions](.././vm/~/MeasureMemoryOptions "MeasureMemoryOptions")

No documentation available

*   [execution](.././vm/~/MeasureMemoryOptions#property_execution)
*   [mode](.././vm/~/MeasureMemoryOptions#property_mode)

I

[MemoryMeasurement](.././vm/~/MemoryMeasurement "MemoryMeasurement")

No documentation available

*   [total](.././vm/~/MemoryMeasurement#property_total)

I

[ModuleEvaluateOptions](.././vm/~/ModuleEvaluateOptions "ModuleEvaluateOptions")

No documentation available

*   [breakOnSigint](.././vm/~/ModuleEvaluateOptions#property_breakonsigint)
*   [timeout](.././vm/~/ModuleEvaluateOptions#property_timeout)

I

[RunningCodeInNewContextOptions](.././vm/~/RunningCodeInNewContextOptions "RunningCodeInNewContextOptions")

No documentation available

*   [cachedData](.././vm/~/RunningCodeInNewContextOptions#property_cacheddata)
*   [importModuleDynamically](.././vm/~/RunningCodeInNewContextOptions#property_importmoduledynamically)

I

[RunningCodeOptions](.././vm/~/RunningCodeOptions "RunningCodeOptions")

No documentation available

*   [cachedData](.././vm/~/RunningCodeOptions#property_cacheddata)
*   [importModuleDynamically](.././vm/~/RunningCodeOptions#property_importmoduledynamically)

I

[RunningScriptInNewContextOptions](.././vm/~/RunningScriptInNewContextOptions "RunningScriptInNewContextOptions")

No documentation available

*   [contextCodeGeneration](.././vm/~/RunningScriptInNewContextOptions#property_contextcodegeneration)
*   [contextName](.././vm/~/RunningScriptInNewContextOptions#property_contextname)
*   [contextOrigin](.././vm/~/RunningScriptInNewContextOptions#property_contextorigin)
*   [microtaskMode](.././vm/~/RunningScriptInNewContextOptions#property_microtaskmode)

I

[RunningScriptOptions](.././vm/~/RunningScriptOptions "RunningScriptOptions")

No documentation available

*   [breakOnSigint](.././vm/~/RunningScriptOptions#property_breakonsigint)
*   [displayErrors](.././vm/~/RunningScriptOptions#property_displayerrors)
*   [timeout](.././vm/~/RunningScriptOptions#property_timeout)

I

[ScriptOptions](.././vm/~/ScriptOptions "ScriptOptions")

No documentation available

*   [cachedData](.././vm/~/ScriptOptions#property_cacheddata)
*   [importModuleDynamically](.././vm/~/ScriptOptions#property_importmoduledynamically)
*   [produceCachedData](.././vm/~/ScriptOptions#property_producecacheddata)

I

[SourceTextModuleOptions](.././vm/~/SourceTextModuleOptions "SourceTextModuleOptions")

No documentation available

*   [cachedData](.././vm/~/SourceTextModuleOptions#property_cacheddata)
*   [columnOffset](.././vm/~/SourceTextModuleOptions#property_columnoffset)
*   [context](.././vm/~/SourceTextModuleOptions#property_context)
*   [identifier](.././vm/~/SourceTextModuleOptions#property_identifier)
*   [importModuleDynamically](.././vm/~/SourceTextModuleOptions#property_importmoduledynamically)
*   [initializeImportMeta](.././vm/~/SourceTextModuleOptions#property_initializeimportmeta)
*   [lineOffset](.././vm/~/SourceTextModuleOptions#property_lineoffset)

I

[SyntheticModuleOptions](.././vm/~/SyntheticModuleOptions "SyntheticModuleOptions")

No documentation available

*   [context](.././vm/~/SyntheticModuleOptions#property_context)
*   [identifier](.././vm/~/SyntheticModuleOptions#property_identifier)

### Namespaces [#](#Namespaces)

N

[constants](.././vm/~/constants "constants")

Returns an object containing commonly used constants for VM operations.

### Type Aliases [#](<#Type Aliases>)

T

[MeasureMemoryMode](.././vm/~/MeasureMemoryMode "MeasureMemoryMode")

No documentation available

T

[ModuleLinker](.././vm/~/ModuleLinker "ModuleLinker")

No documentation available

T

[ModuleStatus](.././vm/~/ModuleStatus "ModuleStatus")

No documentation available

### Variables [#](#Variables)

v

[constants.DONT\_CONTEXTIFY](.././vm/~/constants.DONT_CONTEXTIFY "constants.DONT_CONTEXTIFY")

This constant, when used as the `contextObject` argument in vm APIs, instructs Node.js to create a context without wrapping its global object with another object in a Node.js-specific manner. As a result, the `globalThis` value inside the new context would behave more closely to an ordinary one.

v

[constants.USE\_MAIN\_CONTEXT\_DEFAULT\_LOADER](.././vm/~/constants.USE_MAIN_CONTEXT_DEFAULT_LOADER "constants.USE_MAIN_CONTEXT_DEFAULT_LOADER")

A constant that can be used as the `importModuleDynamically` option to `vm.Script` and `vm.compileFunction()` so that Node.js uses the default ESM loader from the main context to load the requested module.
