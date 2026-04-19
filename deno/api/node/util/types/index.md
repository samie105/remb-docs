---
title: "util/types - Node documentation"
source: "https://docs.deno.com/api/node/util/types/"
canonical_url: "https://docs.deno.com/api/node/util/types/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:24.185Z"
content_hash: "81e47c03cbef7630a56aba5fa0b722c07cb49dd01c36e48a7d352f6ab2ab7496"
menu_path: ["util/types - Node documentation"]
section_path: []
---
### Usage in Deno

```typescript
import * as mod from "node:util/types";
```

### Functions [#](#Functions)

f

[isAnyArrayBuffer](../.././util/types/~/isAnyArrayBuffer "isAnyArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) or [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance.

f

[isArgumentsObject](../.././util/types/~/isArgumentsObject "isArgumentsObject")

Returns `true` if the value is an `arguments` object.

f

[isArrayBuffer](../.././util/types/~/isArrayBuffer "isArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instance. This does _not_ include [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[isArrayBufferView](../.././util/types/~/isArrayBufferView "isArrayBufferView")

Returns `true` if the value is an instance of one of the [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) views, such as typed array objects or [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). Equivalent to [`ArrayBuffer.isView()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/isView).

f

[isAsyncFunction](../.././util/types/~/isAsyncFunction "isAsyncFunction")

Returns `true` if the value is an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function). This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[isBigInt64Array](../.././util/types/~/isBigInt64Array "isBigInt64Array")

Returns `true` if the value is a `BigInt64Array` instance.

f

[isBigIntObject](../.././util/types/~/isBigIntObject "isBigIntObject")

Returns `true` if the value is a BigInt object, e.g. created by `Object(BigInt(123))`.

f

[isBigUint64Array](../.././util/types/~/isBigUint64Array "isBigUint64Array")

Returns `true` if the value is a `BigUint64Array` instance.

f

[isBooleanObject](../.././util/types/~/isBooleanObject "isBooleanObject")

Returns `true` if the value is a boolean object, e.g. created by `new Boolean()`.

f

[isBoxedPrimitive](../.././util/types/~/isBoxedPrimitive "isBoxedPrimitive")

Returns `true` if the value is any boxed primitive object, e.g. created by `new Boolean()`, `new String()` or `Object(Symbol())`.

f

[isCryptoKey](../.././util/types/~/isCryptoKey "isCryptoKey")

Returns `true` if `value` is a `CryptoKey`, `false` otherwise.

f

[isDataView](../.././util/types/~/isDataView "isDataView")

Returns `true` if the value is a built-in [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) instance.

f

[isDate](../.././util/types/~/isDate "isDate")

Returns `true` if the value is a built-in [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) instance.

f

[isExternal](../.././util/types/~/isExternal "isExternal")

Returns `true` if the value is a native `External` value.

f

[isFloat32Array](../.././util/types/~/isFloat32Array "isFloat32Array")

Returns `true` if the value is a built-in [`Float32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) instance.

f

[isFloat64Array](../.././util/types/~/isFloat64Array "isFloat64Array")

Returns `true` if the value is a built-in [`Float64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) instance.

f

[isGeneratorFunction](../.././util/types/~/isGeneratorFunction "isGeneratorFunction")

Returns `true` if the value is a generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[isGeneratorObject](../.././util/types/~/isGeneratorObject "isGeneratorObject")

Returns `true` if the value is a generator object as returned from a built-in generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[isInt16Array](../.././util/types/~/isInt16Array "isInt16Array")

Returns `true` if the value is a built-in [`Int16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array) instance.

f

[isInt32Array](../.././util/types/~/isInt32Array "isInt32Array")

Returns `true` if the value is a built-in [`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array) instance.

f

[isInt8Array](../.././util/types/~/isInt8Array "isInt8Array")

Returns `true` if the value is a built-in [`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array) instance.

f

[isKeyObject](../.././util/types/~/isKeyObject "isKeyObject")

Returns `true` if `value` is a `KeyObject`, `false` otherwise.

f

[isMap](../.././util/types/~/isMap "isMap")

Returns `true` if the value is a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[isMapIterator](../.././util/types/~/isMapIterator "isMapIterator")

Returns `true` if the value is an iterator returned for a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[isModuleNamespaceObject](../.././util/types/~/isModuleNamespaceObject "isModuleNamespaceObject")

Returns `true` if the value is an instance of a [Module Namespace Object](https://tc39.github.io/ecma262/#sec-module-namespace-exotic-objects).

f

[isNativeError](../.././util/types/~/isNativeError "isNativeError")

Returns `true` if the value was returned by the constructor of a [built-in `Error` type](https://tc39.es/ecma262/#sec-error-objects).

f

[isNumberObject](../.././util/types/~/isNumberObject "isNumberObject")

Returns `true` if the value is a number object, e.g. created by `new Number()`.

f

[isPromise](../.././util/types/~/isPromise "isPromise")

Returns `true` if the value is a built-in [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

f

[isProxy](../.././util/types/~/isProxy "isProxy")

Returns `true` if the value is a [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) instance.

f

[isRegExp](../.././util/types/~/isRegExp "isRegExp")

Returns `true` if the value is a regular expression object.

f

[isSet](../.././util/types/~/isSet "isSet")

Returns `true` if the value is a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[isSetIterator](../.././util/types/~/isSetIterator "isSetIterator")

Returns `true` if the value is an iterator returned for a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[isSharedArrayBuffer](../.././util/types/~/isSharedArrayBuffer "isSharedArrayBuffer")

Returns `true` if the value is a built-in [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance. This does _not_ include [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[isStringObject](../.././util/types/~/isStringObject "isStringObject")

Returns `true` if the value is a string object, e.g. created by `new String()`.

f

[isSymbolObject](../.././util/types/~/isSymbolObject "isSymbolObject")

Returns `true` if the value is a symbol object, created by calling `Object()` on a `Symbol` primitive.

f

[isTypedArray](../.././util/types/~/isTypedArray "isTypedArray")

Returns `true` if the value is a built-in [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) instance.

f

[isUint16Array](../.././util/types/~/isUint16Array "isUint16Array")

Returns `true` if the value is a built-in [`Uint16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array) instance.

f

[isUint32Array](../.././util/types/~/isUint32Array "isUint32Array")

Returns `true` if the value is a built-in [`Uint32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array) instance.

f

[isUint8Array](../.././util/types/~/isUint8Array "isUint8Array")

Returns `true` if the value is a built-in [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instance.

f

[isUint8ClampedArray](../.././util/types/~/isUint8ClampedArray "isUint8ClampedArray")

Returns `true` if the value is a built-in [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) instance.

f

[isWeakMap](../.././util/types/~/isWeakMap "isWeakMap")

Returns `true` if the value is a built-in [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) instance.

f

[isWeakSet](../.././util/types/~/isWeakSet "isWeakSet")

Returns `true` if the value is a built-in [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) instance.
