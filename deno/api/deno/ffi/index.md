---
title: "FFI - Deno documentation"
source: "https://docs.deno.com/api/deno/ffi"
canonical_url: "https://docs.deno.com/api/deno/ffi"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:52:29.049Z"
content_hash: "8a900bf451d4e20015c5af40fabeae0810784a987f88fd2ec9c772907762466f"
menu_path: ["FFI - Deno documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../fetch/index.md", "title": "Fetch - Deno documentation"}
nav_next: {"path": "../file-system/index.md", "title": "File System - Deno documentation"}
---

c

[Deno.UnsafeCallback](./././~/Deno.UnsafeCallback "Deno.UnsafeCallback")

An unsafe function pointer for passing JavaScript functions as C function pointers to foreign function calls.

-   [callback](./././~/Deno.UnsafeCallback#property_callback)
-   [close](./././~/Deno.UnsafeCallback#method_close_0)
-   [definition](./././~/Deno.UnsafeCallback#property_definition)
-   [pointer](./././~/Deno.UnsafeCallback#property_pointer)
-   [ref](./././~/Deno.UnsafeCallback#method_ref_0)
-   [threadSafe](./././~/Deno.UnsafeCallback#method_threadsafe_0)
-   [unref](./././~/Deno.UnsafeCallback#method_unref_0)

c

[Deno.UnsafeFnPointer](./././~/Deno.UnsafeFnPointer "Deno.UnsafeFnPointer")

An unsafe pointer to a function, for calling functions that are not present as symbols.

-   [call](./././~/Deno.UnsafeFnPointer#property_call)
-   [definition](./././~/Deno.UnsafeFnPointer#property_definition)
-   [pointer](./././~/Deno.UnsafeFnPointer#property_pointer)

c

[Deno.UnsafePointer](./././~/Deno.UnsafePointer "Deno.UnsafePointer")

A collection of static functions for interacting with pointer objects.

-   [create](./././~/Deno.UnsafePointer#method_create_0)
-   [equals](./././~/Deno.UnsafePointer#method_equals_0)
-   [of](./././~/Deno.UnsafePointer#method_of_0)
-   [offset](./././~/Deno.UnsafePointer#method_offset_0)
-   [value](./././~/Deno.UnsafePointer#method_value_0)

c

[Deno.UnsafePointerView](./././~/Deno.UnsafePointerView "Deno.UnsafePointerView")

An unsafe pointer view to a memory location as specified by the `pointer` value. The `UnsafePointerView` API follows the standard built in interface `DataView` for accessing the underlying types at an memory location (numbers, strings and raw bytes).

-   [copyInto](./././~/Deno.UnsafePointerView#method_copyinto_0)
-   [getArrayBuffer](./././~/Deno.UnsafePointerView#method_getarraybuffer_0)
-   [getBigInt64](./././~/Deno.UnsafePointerView#method_getbigint64_0)
-   [getBigUint64](./././~/Deno.UnsafePointerView#method_getbiguint64_0)
-   [getBool](./././~/Deno.UnsafePointerView#method_getbool_0)
-   [getCString](./././~/Deno.UnsafePointerView#method_getcstring_0)
-   [getFloat32](./././~/Deno.UnsafePointerView#method_getfloat32_0)
-   [getFloat64](./././~/Deno.UnsafePointerView#method_getfloat64_0)
-   [getInt16](./././~/Deno.UnsafePointerView#method_getint16_0)
-   [getInt32](./././~/Deno.UnsafePointerView#method_getint32_0)
-   [getInt8](./././~/Deno.UnsafePointerView#method_getint8_0)
-   [getPointer](./././~/Deno.UnsafePointerView#method_getpointer_0)
-   [getUint16](./././~/Deno.UnsafePointerView#method_getuint16_0)
-   [getUint32](./././~/Deno.UnsafePointerView#method_getuint32_0)
-   [getUint8](./././~/Deno.UnsafePointerView#method_getuint8_0)
-   [pointer](./././~/Deno.UnsafePointerView#property_pointer)

f

[Deno.dlopen](./././~/Deno.dlopen "Deno.dlopen")

Opens an external dynamic library and registers symbols, making foreign functions available to be called.

I

[Deno.DynamicLibrary](./././~/Deno.DynamicLibrary "Deno.DynamicLibrary")

A dynamic library resource. Use [`Deno.dlopen`](./././~/Deno.dlopen) to load a dynamic library and return this interface.

-   [close](./././~/Deno.DynamicLibrary#method_close_0)
-   [symbols](./././~/Deno.DynamicLibrary#property_symbols)

I

[Deno.ForeignFunction](./././~/Deno.ForeignFunction "Deno.ForeignFunction")

The interface for a foreign function as defined by its parameter and result types.

-   [name](./././~/Deno.ForeignFunction#property_name)
-   [nonblocking](./././~/Deno.ForeignFunction#property_nonblocking)
-   [optional](./././~/Deno.ForeignFunction#property_optional)
-   [parameters](./././~/Deno.ForeignFunction#property_parameters)
-   [result](./././~/Deno.ForeignFunction#property_result)

I

[Deno.ForeignLibraryInterface](./././~/Deno.ForeignLibraryInterface "Deno.ForeignLibraryInterface")

A foreign library interface descriptor.

I

[Deno.ForeignStatic](./././~/Deno.ForeignStatic "Deno.ForeignStatic")

No documentation available

-   [name](./././~/Deno.ForeignStatic#property_name)
-   [optional](./././~/Deno.ForeignStatic#property_optional)
-   [type](./././~/Deno.ForeignStatic#property_type)

I

[Deno.NativeStructType](./././~/Deno.NativeStructType "Deno.NativeStructType")

The native struct type for interfacing with foreign functions.

-   [struct](./././~/Deno.NativeStructType#property_struct)

I

[Deno.PointerObject](./././~/Deno.PointerObject "Deno.PointerObject")

A non-null pointer, represented as an object at runtime. The object's prototype is `null` and cannot be changed. The object cannot be assigned to either and is thus entirely read-only.

-   [brand](./././~/Deno.PointerObject#property_brand)

I

[Deno.UnsafeCallbackDefinition](./././~/Deno.UnsafeCallbackDefinition "Deno.UnsafeCallbackDefinition")

Definition of a unsafe callback function.

-   [parameters](./././~/Deno.UnsafeCallbackDefinition#property_parameters)
-   [result](./././~/Deno.UnsafeCallbackDefinition#property_result)

T

[Deno.ConditionalAsync](./././~/Deno.ConditionalAsync "Deno.ConditionalAsync")

No documentation available

T

[Deno.FromForeignFunction](./././~/Deno.FromForeignFunction "Deno.FromForeignFunction")

No documentation available

T

[Deno.FromNativeParameterTypes](./././~/Deno.FromNativeParameterTypes "Deno.FromNativeParameterTypes")

No documentation available

T

[Deno.FromNativeResultType](./././~/Deno.FromNativeResultType "Deno.FromNativeResultType")

Type conversion for foreign symbol return types.

T

[Deno.FromNativeType](./././~/Deno.FromNativeType "Deno.FromNativeType")

Type conversion for foreign symbol return types and unsafe callback parameters.

T

[Deno.NativeBigIntType](./././~/Deno.NativeBigIntType "Deno.NativeBigIntType")

All BigInt number types for interfacing with foreign functions.

T

[Deno.NativeBooleanType](./././~/Deno.NativeBooleanType "Deno.NativeBooleanType")

The native boolean type for interfacing to foreign functions.

T

[Deno.NativeBufferType](./././~/Deno.NativeBufferType "Deno.NativeBufferType")

The native buffer type for interfacing to foreign functions.

T

[Deno.NativeFunctionType](./././~/Deno.NativeFunctionType "Deno.NativeFunctionType")

The native function type for interfacing with foreign functions.

T

[Deno.NativeI16Enum](./././~/Deno.NativeI16Enum "Deno.NativeI16Enum")

No documentation available

T

[Deno.NativeI32Enum](./././~/Deno.NativeI32Enum "Deno.NativeI32Enum")

No documentation available

T

[Deno.NativeI8Enum](./././~/Deno.NativeI8Enum "Deno.NativeI8Enum")

No documentation available

T

[Deno.NativeNumberType](./././~/Deno.NativeNumberType "Deno.NativeNumberType")

All plain number types for interfacing with foreign functions.

T

[Deno.NativePointerType](./././~/Deno.NativePointerType "Deno.NativePointerType")

The native pointer type for interfacing to foreign functions.

T

[Deno.NativeResultType](./././~/Deno.NativeResultType "Deno.NativeResultType")

No documentation available

T

[Deno.NativeType](./././~/Deno.NativeType "Deno.NativeType")

All supported types for interfacing with foreign functions.

T

[Deno.NativeTypedFunction](./././~/Deno.NativeTypedFunction "Deno.NativeTypedFunction")

No documentation available

T

[Deno.NativeTypedPointer](./././~/Deno.NativeTypedPointer "Deno.NativeTypedPointer")

No documentation available

T

[Deno.NativeU16Enum](./././~/Deno.NativeU16Enum "Deno.NativeU16Enum")

No documentation available

T

[Deno.NativeU32Enum](./././~/Deno.NativeU32Enum "Deno.NativeU32Enum")

No documentation available

T

[Deno.NativeU8Enum](./././~/Deno.NativeU8Enum "Deno.NativeU8Enum")

No documentation available

T

[Deno.NativeVoidType](./././~/Deno.NativeVoidType "Deno.NativeVoidType")

The native void type for interfacing with foreign functions.

T

[Deno.PointerValue](./././~/Deno.PointerValue "Deno.PointerValue")

Pointers are represented either with a `PointerObject` object or a `null` if the pointer is null.

T

[Deno.StaticForeignLibraryInterface](./././~/Deno.StaticForeignLibraryInterface "Deno.StaticForeignLibraryInterface")

A utility type that infers a foreign library interface.

T

[Deno.StaticForeignSymbol](./././~/Deno.StaticForeignSymbol "Deno.StaticForeignSymbol")

A utility type that infers a foreign symbol.

T

[Deno.StaticForeignSymbolReturnType](./././~/Deno.StaticForeignSymbolReturnType "Deno.StaticForeignSymbolReturnType")

No documentation available

T

[Deno.ToNativeParameterTypes](./././~/Deno.ToNativeParameterTypes "Deno.ToNativeParameterTypes")

A utility type for conversion of parameter types of foreign functions.

T

[Deno.ToNativeResultType](./././~/Deno.ToNativeResultType "Deno.ToNativeResultType")

Type conversion for unsafe callback return types.

T

[Deno.ToNativeType](./././~/Deno.ToNativeType "Deno.ToNativeType")

Type conversion for foreign symbol parameters and unsafe callback return types.

T

[Deno.UnsafeCallbackFunction](./././~/Deno.UnsafeCallbackFunction "Deno.UnsafeCallbackFunction")

An unsafe callback function.

v

[Deno.brand](./././~/Deno.brand "Deno.brand")

No documentation available
