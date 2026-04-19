---
title: "util - Node documentation"
source: "https://docs.deno.com/api/node/util/"
canonical_url: "https://docs.deno.com/api/node/util/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:23.433Z"
content_hash: "c3076497f0ed997e2bbe952cf47dde51e93995a67fa0aec659875753ae569fdb"
menu_path: ["util - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:util";
```

The `node:util` module supports the needs of Node.js internal APIs. Many of the utilities are useful for application and module developers as well. To access it:

```js
import util from 'node:util';
```

### Classes [#](#Classes)

c

[MIMEParams](.././util/~/MIMEParams "MIMEParams")

No documentation available

*   [delete](.././util/~/MIMEParams#method_delete_0)
*   [entries](.././util/~/MIMEParams#method_entries_0)
*   [get](.././util/~/MIMEParams#method_get_0)
*   [has](.././util/~/MIMEParams#method_has_0)
*   [keys](.././util/~/MIMEParams#method_keys_0)
*   [set](.././util/~/MIMEParams#method_set_0)
*   [values](.././util/~/MIMEParams#method_values_0)

c

[MIMEType](.././util/~/MIMEType "MIMEType")

No documentation available

*   [essence](.././util/~/MIMEType#property_essence)
*   [params](.././util/~/MIMEType#property_params)
*   [subtype](.././util/~/MIMEType#property_subtype)
*   [toString](.././util/~/MIMEType#method_tostring_0)
*   [type](.././util/~/MIMEType#property_type)

c

v

[TextDecoder](.././util/~/TextDecoder "TextDecoder")

An implementation of the [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/) `TextDecoder` API.

*   [decode](.././util/~/TextDecoder#method_decode_0)
*   [encoding](.././util/~/TextDecoder#property_encoding)
*   [fatal](.././util/~/TextDecoder#property_fatal)
*   [ignoreBOM](.././util/~/TextDecoder#property_ignorebom)

c

v

[TextEncoder](.././util/~/TextEncoder "TextEncoder")

An implementation of the [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/) `TextEncoder` API. All instances of `TextEncoder` only support UTF-8 encoding.

*   [encode](.././util/~/TextEncoder#method_encode_0)
*   [encodeInto](.././util/~/TextEncoder#method_encodeinto_0)
*   [encoding](.././util/~/TextEncoder#property_encoding)

### Functions [#](#Functions)

f

[aborted](.././util/~/aborted "aborted")

Listens to abort event on the provided `signal` and returns a promise that resolves when the `signal` is aborted. If `resource` is provided, it weakly references the operation's associated object, so if `resource` is garbage collected before the `signal` aborts, then returned promise shall remain pending. This prevents memory leaks in long-running or non-cancelable operations.

f

[callbackify](.././util/~/callbackify "callbackify")

Takes an `async` function (or a function that returns a `Promise`) and returns a function following the error-first callback style, i.e. taking an `(err, value) => ...` callback as the last argument. In the callback, the first argument will be the rejection reason (or `null` if the `Promise` resolved), and the second argument will be the resolved value.

f

[debuglog](.././util/~/debuglog "debuglog")

The `util.debuglog()` method is used to create a function that conditionally writes debug messages to `stderr` based on the existence of the `NODE_DEBUG`environment variable. If the `section` name appears within the value of that environment variable, then the returned function operates similar to `console.error()`. If not, then the returned function is a no-op.

f

[deprecate](.././util/~/deprecate "deprecate")

The `util.deprecate()` method wraps `fn` (which may be a function or class) in such a way that it is marked as deprecated.

f

[format](.././util/~/format "format")

The `util.format()` method returns a formatted string using the first argument as a `printf`\-like format string which can contain zero or more format specifiers. Each specifier is replaced with the converted value from the corresponding argument. Supported specifiers are:

f

[formatWithOptions](.././util/~/formatWithOptions "formatWithOptions")

This function is identical to [format](.././util/~/format), except in that it takes an `inspectOptions` argument which specifies options that are passed along to [inspect](.././util/~/inspect).

f

[getCallSites](.././util/~/getCallSites "getCallSites")

Returns an array of call site objects containing the stack of the caller function.

f

[getSystemErrorMap](.././util/~/getSystemErrorMap "getSystemErrorMap")

No documentation available

f

[getSystemErrorMessage](.././util/~/getSystemErrorMessage "getSystemErrorMessage")

Returns the string message for a numeric error code that comes from a Node.js API. The mapping between error codes and string messages is platform-dependent.

f

[getSystemErrorName](.././util/~/getSystemErrorName "getSystemErrorName")

Returns the string name for a numeric error code that comes from a Node.js API. The mapping between error codes and error names is platform-dependent. See `Common System Errors` for the names of common errors.

f

[inherits](.././util/~/inherits "inherits")

Usage of `util.inherits()` is discouraged. Please use the ES6 `class` and `extends` keywords to get language level inheritance support. Also note that the two styles are [semantically incompatible](https://github.com/nodejs/node/issues/4179).

f

N

[inspect](.././util/~/inspect "inspect")

The `util.inspect()` method returns a string representation of `object` that is intended for debugging. The output of `util.inspect` may change at any time and should not be depended upon programmatically. Additional `options` may be passed that alter the result. `util.inspect()` will use the constructor's name and/or `@@toStringTag` to make an identifiable tag for an inspected value.

f

[isDeepStrictEqual](.././util/~/isDeepStrictEqual "isDeepStrictEqual")

Returns `true` if there is deep strict equality between `val1` and `val2`. Otherwise, returns `false`.

f

[parseArgs](.././util/~/parseArgs "parseArgs")

Provides a higher level API for command-line argument parsing than interacting with `process.argv` directly. Takes a specification for the expected arguments and returns a structured object with the parsed options and positionals.

f

[parseEnv](.././util/~/parseEnv "parseEnv")

Stability: 1.1 - Active development Given an example `.env` file:

f

N

[promisify](.././util/~/promisify "promisify")

Takes a function following the common error-first callback style, i.e. taking an `(err, value) => ...` callback as the last argument, and returns a version that returns promises.

f

[stripVTControlCharacters](.././util/~/stripVTControlCharacters "stripVTControlCharacters")

Returns `str` with any ANSI escape codes removed.

f

[styleText](.././util/~/styleText "styleText")

This function returns a formatted text considering the `format` passed.

f

[toUSVString](.././util/~/toUSVString "toUSVString")

Returns the `string` after replacing any surrogate code points (or equivalently, any unpaired surrogate code units) with the Unicode "replacement character" U+FFFD.

f

[transferableAbortController](.././util/~/transferableAbortController "transferableAbortController")

No documentation available

f

[transferableAbortSignal](.././util/~/transferableAbortSignal "transferableAbortSignal")

No documentation available

f

[types.isAnyArrayBuffer](.././util/types/~/types.isAnyArrayBuffer "types.isAnyArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) or [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance.

f

[types.isArgumentsObject](.././util/types/~/types.isArgumentsObject "types.isArgumentsObject")

Returns `true` if the value is an `arguments` object.

f

[types.isArrayBuffer](.././util/types/~/types.isArrayBuffer "types.isArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instance. This does _not_ include [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[types.isArrayBufferView](.././util/types/~/types.isArrayBufferView "types.isArrayBufferView")

Returns `true` if the value is an instance of one of the [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) views, such as typed array objects or [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). Equivalent to [`ArrayBuffer.isView()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/isView).

f

[types.isAsyncFunction](.././util/types/~/types.isAsyncFunction "types.isAsyncFunction")

Returns `true` if the value is an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function). This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[types.isBigInt64Array](.././util/types/~/types.isBigInt64Array "types.isBigInt64Array")

Returns `true` if the value is a `BigInt64Array` instance.

f

[types.isBigIntObject](.././util/types/~/types.isBigIntObject "types.isBigIntObject")

Returns `true` if the value is a BigInt object, e.g. created by `Object(BigInt(123))`.

f

[types.isBigUint64Array](.././util/types/~/types.isBigUint64Array "types.isBigUint64Array")

Returns `true` if the value is a `BigUint64Array` instance.

f

[types.isBooleanObject](.././util/types/~/types.isBooleanObject "types.isBooleanObject")

Returns `true` if the value is a boolean object, e.g. created by `new Boolean()`.

f

[types.isBoxedPrimitive](.././util/types/~/types.isBoxedPrimitive "types.isBoxedPrimitive")

Returns `true` if the value is any boxed primitive object, e.g. created by `new Boolean()`, `new String()` or `Object(Symbol())`.

f

[types.isCryptoKey](.././util/types/~/types.isCryptoKey "types.isCryptoKey")

Returns `true` if `value` is a `CryptoKey`, `false` otherwise.

f

[types.isDataView](.././util/types/~/types.isDataView "types.isDataView")

Returns `true` if the value is a built-in [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) instance.

f

[types.isDate](.././util/types/~/types.isDate "types.isDate")

Returns `true` if the value is a built-in [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) instance.

f

[types.isExternal](.././util/types/~/types.isExternal "types.isExternal")

Returns `true` if the value is a native `External` value.

f

[types.isFloat32Array](.././util/types/~/types.isFloat32Array "types.isFloat32Array")

Returns `true` if the value is a built-in [`Float32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) instance.

f

[types.isFloat64Array](.././util/types/~/types.isFloat64Array "types.isFloat64Array")

Returns `true` if the value is a built-in [`Float64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) instance.

f

[types.isGeneratorFunction](.././util/types/~/types.isGeneratorFunction "types.isGeneratorFunction")

Returns `true` if the value is a generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[types.isGeneratorObject](.././util/types/~/types.isGeneratorObject "types.isGeneratorObject")

Returns `true` if the value is a generator object as returned from a built-in generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[types.isInt16Array](.././util/types/~/types.isInt16Array "types.isInt16Array")

Returns `true` if the value is a built-in [`Int16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array) instance.

f

[types.isInt32Array](.././util/types/~/types.isInt32Array "types.isInt32Array")

Returns `true` if the value is a built-in [`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array) instance.

f

[types.isInt8Array](.././util/types/~/types.isInt8Array "types.isInt8Array")

Returns `true` if the value is a built-in [`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array) instance.

f

[types.isKeyObject](.././util/types/~/types.isKeyObject "types.isKeyObject")

Returns `true` if `value` is a `KeyObject`, `false` otherwise.

f

[types.isMap](.././util/types/~/types.isMap "types.isMap")

Returns `true` if the value is a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[types.isMapIterator](.././util/types/~/types.isMapIterator "types.isMapIterator")

Returns `true` if the value is an iterator returned for a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[types.isModuleNamespaceObject](.././util/types/~/types.isModuleNamespaceObject "types.isModuleNamespaceObject")

Returns `true` if the value is an instance of a [Module Namespace Object](https://tc39.github.io/ecma262/#sec-module-namespace-exotic-objects).

f

[types.isNativeError](.././util/types/~/types.isNativeError "types.isNativeError")

Returns `true` if the value was returned by the constructor of a [built-in `Error` type](https://tc39.es/ecma262/#sec-error-objects).

f

[types.isNumberObject](.././util/types/~/types.isNumberObject "types.isNumberObject")

Returns `true` if the value is a number object, e.g. created by `new Number()`.

f

[types.isPromise](.././util/types/~/types.isPromise "types.isPromise")

Returns `true` if the value is a built-in [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

f

[types.isProxy](.././util/types/~/types.isProxy "types.isProxy")

Returns `true` if the value is a [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) instance.

f

[types.isRegExp](.././util/types/~/types.isRegExp "types.isRegExp")

Returns `true` if the value is a regular expression object.

f

[types.isSet](.././util/types/~/types.isSet "types.isSet")

Returns `true` if the value is a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[types.isSetIterator](.././util/types/~/types.isSetIterator "types.isSetIterator")

Returns `true` if the value is an iterator returned for a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[types.isSharedArrayBuffer](.././util/types/~/types.isSharedArrayBuffer "types.isSharedArrayBuffer")

Returns `true` if the value is a built-in [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance. This does _not_ include [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[types.isStringObject](.././util/types/~/types.isStringObject "types.isStringObject")

Returns `true` if the value is a string object, e.g. created by `new String()`.

f

[types.isSymbolObject](.././util/types/~/types.isSymbolObject "types.isSymbolObject")

Returns `true` if the value is a symbol object, created by calling `Object()` on a `Symbol` primitive.

f

[types.isTypedArray](.././util/types/~/types.isTypedArray "types.isTypedArray")

Returns `true` if the value is a built-in [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) instance.

f

[types.isUint16Array](.././util/types/~/types.isUint16Array "types.isUint16Array")

Returns `true` if the value is a built-in [`Uint16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array) instance.

f

[types.isUint32Array](.././util/types/~/types.isUint32Array "types.isUint32Array")

Returns `true` if the value is a built-in [`Uint32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array) instance.

f

[types.isUint8Array](.././util/types/~/types.isUint8Array "types.isUint8Array")

Returns `true` if the value is a built-in [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instance.

f

[types.isUint8ClampedArray](.././util/types/~/types.isUint8ClampedArray "types.isUint8ClampedArray")

Returns `true` if the value is a built-in [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) instance.

f

[types.isWeakMap](.././util/types/~/types.isWeakMap "types.isWeakMap")

Returns `true` if the value is a built-in [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) instance.

f

[types.isWeakSet](.././util/types/~/types.isWeakSet "types.isWeakSet")

Returns `true` if the value is a built-in [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) instance.

f

[isArray](.././util/~/isArray "isArray")

Alias for [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray).

f

[isBoolean](.././util/~/isBoolean "isBoolean")

Returns `true` if the given `object` is a `Boolean`. Otherwise, returns `false`.

f

[isBuffer](.././util/~/isBuffer "isBuffer")

Returns `true` if the given `object` is a `Buffer`. Otherwise, returns `false`.

f

[isDate](.././util/~/isDate "isDate")

Returns `true` if the given `object` is a `Date`. Otherwise, returns `false`.

f

[isError](.././util/~/isError "isError")

Returns `true` if the given `object` is an `Error`. Otherwise, returns `false`.

f

[isFunction](.././util/~/isFunction "isFunction")

Returns `true` if the given `object` is a `Function`. Otherwise, returns `false`.

f

[isNull](.././util/~/isNull "isNull")

Returns `true` if the given `object` is strictly `null`. Otherwise, returns`false`.

f

[isNullOrUndefined](.././util/~/isNullOrUndefined "isNullOrUndefined")

Returns `true` if the given `object` is `null` or `undefined`. Otherwise, returns `false`.

f

[isNumber](.././util/~/isNumber "isNumber")

Returns `true` if the given `object` is a `Number`. Otherwise, returns `false`.

f

[isObject](.././util/~/isObject "isObject")

Returns `true` if the given `object` is strictly an `Object`**and** not a`Function` (even though functions are objects in JavaScript). Otherwise, returns `false`.

f

[isPrimitive](.././util/~/isPrimitive "isPrimitive")

Returns `true` if the given `object` is a primitive type. Otherwise, returns`false`.

f

[isRegExp](.././util/~/isRegExp "isRegExp")

Returns `true` if the given `object` is a `RegExp`. Otherwise, returns `false`.

f

[isString](.././util/~/isString "isString")

Returns `true` if the given `object` is a `string`. Otherwise, returns `false`.

f

[isSymbol](.././util/~/isSymbol "isSymbol")

Returns `true` if the given `object` is a `Symbol`. Otherwise, returns `false`.

f

[isUndefined](.././util/~/isUndefined "isUndefined")

Returns `true` if the given `object` is `undefined`. Otherwise, returns `false`.

f

[log](.././util/~/log "log")

The `util.log()` method prints the given `string` to `stdout` with an included timestamp.

### Interfaces [#](#Interfaces)

I

[CallSiteObject](.././util/~/CallSiteObject "CallSiteObject")

No documentation available

*   [columnNumber](.././util/~/CallSiteObject#property_columnnumber)
*   [functionName](.././util/~/CallSiteObject#property_functionname)
*   [lineNumber](.././util/~/CallSiteObject#property_linenumber)
*   [scriptId](.././util/~/CallSiteObject#property_scriptid)
*   [scriptName](.././util/~/CallSiteObject#property_scriptname)

I

[CustomPromisifyLegacy](.././util/~/CustomPromisifyLegacy "CustomPromisifyLegacy")

No documentation available

*   [\_\_promisify\_\_](.././util/~/CustomPromisifyLegacy#property___promisify__)

I

[CustomPromisifySymbol](.././util/~/CustomPromisifySymbol "CustomPromisifySymbol")

No documentation available

I

[DebugLogger](.././util/~/DebugLogger "DebugLogger")

No documentation available

*   [enabled](.././util/~/DebugLogger#property_enabled)

I

[EncodeIntoResult](.././util/~/EncodeIntoResult "EncodeIntoResult")

No documentation available

*   [read](.././util/~/EncodeIntoResult#property_read)
*   [written](.././util/~/EncodeIntoResult#property_written)

I

[GetCallSitesOptions](.././util/~/GetCallSitesOptions "GetCallSitesOptions")

No documentation available

*   [sourceMap](.././util/~/GetCallSitesOptions#property_sourcemap)

I

[InspectOptions](.././util/~/InspectOptions "InspectOptions")

No documentation available

*   [breakLength](.././util/~/InspectOptions#property_breaklength)
*   [colors](.././util/~/InspectOptions#property_colors)
*   [compact](.././util/~/InspectOptions#property_compact)
*   [customInspect](.././util/~/InspectOptions#property_custominspect)
*   [depth](.././util/~/InspectOptions#property_depth)
*   [getters](.././util/~/InspectOptions#property_getters)
*   [maxArrayLength](.././util/~/InspectOptions#property_maxarraylength)
*   [maxStringLength](.././util/~/InspectOptions#property_maxstringlength)
*   [numericSeparator](.././util/~/InspectOptions#property_numericseparator)
*   [showHidden](.././util/~/InspectOptions#property_showhidden)
*   [showProxy](.././util/~/InspectOptions#property_showproxy)
*   [sorted](.././util/~/InspectOptions#property_sorted)

I

[InspectOptionsStylized](.././util/~/InspectOptionsStylized "InspectOptionsStylized")

No documentation available

*   [stylize](.././util/~/InspectOptionsStylized#method_stylize_0)

I

[ParseArgsConfig](.././util/~/ParseArgsConfig "ParseArgsConfig")

No documentation available

*   [allowNegative](.././util/~/ParseArgsConfig#property_allownegative)
*   [allowPositionals](.././util/~/ParseArgsConfig#property_allowpositionals)
*   [args](.././util/~/ParseArgsConfig#property_args)
*   [options](.././util/~/ParseArgsConfig#property_options)
*   [strict](.././util/~/ParseArgsConfig#property_strict)
*   [tokens](.././util/~/ParseArgsConfig#property_tokens)

I

[ParseArgsOptionDescriptor](.././util/~/ParseArgsOptionDescriptor "ParseArgsOptionDescriptor")

No documentation available

*   [default](.././util/~/ParseArgsOptionDescriptor#property_default)
*   [multiple](.././util/~/ParseArgsOptionDescriptor#property_multiple)
*   [short](.././util/~/ParseArgsOptionDescriptor#property_short)
*   [type](.././util/~/ParseArgsOptionDescriptor#property_type)

I

[ParseArgsOptionsConfig](.././util/~/ParseArgsOptionsConfig "ParseArgsOptionsConfig")

No documentation available

### Namespaces [#](#Namespaces)

N

[types](.././util/~/types "types")

No documentation available

### Type Aliases [#](<#Type Aliases>)

T

[ApplyOptionalModifiers](.././util/~/ApplyOptionalModifiers "ApplyOptionalModifiers")

No documentation available

T

[BackgroundColors](.././util/~/BackgroundColors "BackgroundColors")

No documentation available

T

[CustomInspectFunction](.././util/~/CustomInspectFunction "CustomInspectFunction")

No documentation available

T

[CustomPromisify](.././util/~/CustomPromisify "CustomPromisify")

No documentation available

T

[DebugLoggerFunction](.././util/~/DebugLoggerFunction "DebugLoggerFunction")

No documentation available

T

[ExtractOptionValue](.././util/~/ExtractOptionValue "ExtractOptionValue")

No documentation available

T

[ForegroundColors](.././util/~/ForegroundColors "ForegroundColors")

No documentation available

T

[IfDefaultsFalse](.././util/~/IfDefaultsFalse "IfDefaultsFalse")

No documentation available

T

[IfDefaultsTrue](.././util/~/IfDefaultsTrue "IfDefaultsTrue")

No documentation available

T

[Modifiers](.././util/~/Modifiers "Modifiers")

No documentation available

T

[OptionToken](.././util/~/OptionToken "OptionToken")

No documentation available

T

[ParseArgsOptionsType](.././util/~/ParseArgsOptionsType "ParseArgsOptionsType")

Type of argument used in [parseArgs](.././util/~/parseArgs).

T

[ParsedOptionToken](.././util/~/ParsedOptionToken "ParsedOptionToken")

No documentation available

T

[ParsedPositionals](.././util/~/ParsedPositionals "ParsedPositionals")

No documentation available

T

[ParsedPositionalToken](.././util/~/ParsedPositionalToken "ParsedPositionalToken")

No documentation available

T

[ParsedResults](.././util/~/ParsedResults "ParsedResults")

No documentation available

T

[ParsedTokens](.././util/~/ParsedTokens "ParsedTokens")

No documentation available

T

[ParsedValues](.././util/~/ParsedValues "ParsedValues")

No documentation available

T

[PreciseParsedResults](.././util/~/PreciseParsedResults "PreciseParsedResults")

No documentation available

T

[PreciseTokenForOptions](.././util/~/PreciseTokenForOptions "PreciseTokenForOptions")

No documentation available

T

[Style](.././util/~/Style "Style")

No documentation available

T

[Token](.././util/~/Token "Token")

No documentation available

T

[TokenForOptions](.././util/~/TokenForOptions "TokenForOptions")

No documentation available

### Variables [#](#Variables)

v

[debug](.././util/~/debug "debug")

No documentation available

v

[inspect.colors](.././util/~/inspect.colors "inspect.colors")

No documentation available

v

[inspect.custom](.././util/~/inspect.custom "inspect.custom")

That can be used to declare custom inspect functions.

v

[inspect.defaultOptions](.././util/~/inspect.defaultOptions "inspect.defaultOptions")

No documentation available

v

[inspect.replDefaults](.././util/~/inspect.replDefaults "inspect.replDefaults")

Allows changing inspect settings from the repl.

v

[inspect.styles](.././util/~/inspect.styles "inspect.styles")

No documentation available

v

[promisify.custom](.././util/~/promisify.custom "promisify.custom")

That can be used to declare custom promisified variants of functions.
