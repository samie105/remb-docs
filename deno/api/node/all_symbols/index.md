---
title: "All Symbols - Node documentation"
source: "https://docs.deno.com/api/node/all_symbols"
canonical_url: "https://docs.deno.com/api/node/all_symbols"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T18:03:47.995Z"
content_hash: "2f5dc2d5253954ba9a7f808fef844021ea415751c19cb090d4282cefe0e5feb6"
menu_path: ["All Symbols - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/index.md", "title": "Node.js Built-in APIs"}
nav_next: {"path": "deno/api/node/assert/index.md", "title": "assert - Node documentation"}
---

The `node:assert` module provides a set of assertion functions for verifying invariants.

f

N

[assert](././assert/~/assert "assert")

An alias of ok.

c

[assert.AssertionError](././assert/~/assert.AssertionError "assert.AssertionError")

Indicates the failure of an assertion. All errors thrown by the `node:assert` module will be instances of the `AssertionError` class.

-   [actual](././assert/~/assert.AssertionError#property_actual)
-   [code](././assert/~/assert.AssertionError#property_code)
-   [expected](././assert/~/assert.AssertionError#property_expected)
-   [generatedMessage](././assert/~/assert.AssertionError#property_generatedmessage)
-   [operator](././assert/~/assert.AssertionError#property_operator)

T

[assert.AssertPredicate](././assert/~/assert.AssertPredicate "assert.AssertPredicate")

No documentation available

I

[assert.CallTrackerCall](././assert/~/assert.CallTrackerCall "assert.CallTrackerCall")

No documentation available

-   [arguments](././assert/~/assert.CallTrackerCall#property_arguments)
-   [thisArg](././assert/~/assert.CallTrackerCall#property_thisarg)

I

[assert.CallTrackerReportInformation](././assert/~/assert.CallTrackerReportInformation "assert.CallTrackerReportInformation")

No documentation available

-   [actual](././assert/~/assert.CallTrackerReportInformation#property_actual)
-   [expected](././assert/~/assert.CallTrackerReportInformation#property_expected)
-   [message](././assert/~/assert.CallTrackerReportInformation#property_message)
-   [operator](././assert/~/assert.CallTrackerReportInformation#property_operator)
-   [stack](././assert/~/assert.CallTrackerReportInformation#property_stack)

f

[assert.deepEqual](././assert/~/assert.deepEqual "assert.deepEqual")

**Strict assertion mode**

f

[assert.deepStrictEqual](././assert/~/assert.deepStrictEqual "assert.deepStrictEqual")

Tests for deep equality between the `actual` and `expected` parameters. "Deep" equality means that the enumerable "own" properties of child objects are recursively evaluated also by the following rules.

f

[assert.doesNotMatch](././assert/~/assert.doesNotMatch "assert.doesNotMatch")

Expects the `string` input not to match the regular expression.

f

[assert.doesNotReject](././assert/~/assert.doesNotReject "assert.doesNotReject")

Awaits the `asyncFn` promise or, if `asyncFn` is a function, immediately calls the function and awaits the returned promise to complete. It will then check that the promise is not rejected.

f

[assert.doesNotThrow](././assert/~/assert.doesNotThrow "assert.doesNotThrow")

Asserts that the function `fn` does not throw an error.

f

[assert.equal](././assert/~/assert.equal "assert.equal")

**Strict assertion mode**

f

[assert.fail](././assert/~/assert.fail "assert.fail")

Throws an `AssertionError` with the provided error message or a default error message. If the `message` parameter is an instance of an `Error` then it will be thrown instead of the `AssertionError`.

f

[assert.ifError](././assert/~/assert.ifError "assert.ifError")

Throws `value` if `value` is not `undefined` or `null`. This is useful when testing the `error` argument in callbacks. The stack trace contains all frames from the error passed to `ifError()` including the potential new frames for `ifError()` itself.

f

[assert.match](././assert/~/assert.match "assert.match")

Expects the `string` input to match the regular expression.

f

[assert.notDeepEqual](././assert/~/assert.notDeepEqual "assert.notDeepEqual")

**Strict assertion mode**

f

[assert.notDeepStrictEqual](././assert/~/assert.notDeepStrictEqual "assert.notDeepStrictEqual")

Tests for deep strict inequality. Opposite of deepStrictEqual.

f

[assert.notEqual](././assert/~/assert.notEqual "assert.notEqual")

**Strict assertion mode**

f

[assert.notStrictEqual](././assert/~/assert.notStrictEqual "assert.notStrictEqual")

Tests strict inequality between the `actual` and `expected` parameters as determined by [`Object.is()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is).

f

[assert.ok](././assert/~/assert.ok "assert.ok")

Tests if `value` is truthy. It is equivalent to `assert.equal(!!value, true, message)`.

f

[assert.partialDeepStrictEqual](././assert/~/assert.partialDeepStrictEqual "assert.partialDeepStrictEqual")

`assert.partialDeepStrictEqual()` Asserts the equivalence between the `actual` and `expected` parameters through a deep comparison, ensuring that all properties in the `expected` parameter are present in the `actual` parameter with equivalent values, not allowing type coercion. The main difference with `assert.deepStrictEqual()` is that `assert.partialDeepStrictEqual()` does not require all properties in the `actual` parameter to be present in the `expected` parameter. This method should always pass the same test cases as `assert.deepStrictEqual()`, behaving as a super set of it.

f

[assert.rejects](././assert/~/assert.rejects "assert.rejects")

Awaits the `asyncFn` promise or, if `asyncFn` is a function, immediately calls the function and awaits the returned promise to complete. It will then check that the promise is rejected.

N

v

[assert.strict](././assert/~/assert.strict "assert.strict")

In strict assertion mode, non-strict methods behave like their corresponding strict methods. For example, deepEqual will behave like deepStrictEqual.

T

[assert.strict.AssertionError](././assert/~/assert.strict.AssertionError "assert.strict.AssertionError")

No documentation available

T

[assert.strict.AssertPredicate](././assert/~/assert.strict.AssertPredicate "assert.strict.AssertPredicate")

No documentation available

T

[assert.strict.CallTrackerCall](././assert/~/assert.strict.CallTrackerCall "assert.strict.CallTrackerCall")

No documentation available

T

[assert.strict.CallTrackerReportInformation](././assert/~/assert.strict.CallTrackerReportInformation "assert.strict.CallTrackerReportInformation")

No documentation available

f

[assert.strictEqual](././assert/~/assert.strictEqual "assert.strictEqual")

Tests strict equality between the `actual` and `expected` parameters as determined by [`Object.is()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is).

f

[assert.throws](././assert/~/assert.throws "assert.throws")

Expects the function `fn` to throw an error.

c

[assert.CallTracker](././assert/~/assert.CallTracker "assert.CallTracker")

This feature is deprecated and will be removed in a future version. Please consider using alternatives such as the `mock` helper function.

-   [calls](././assert/~/assert.CallTracker#method_calls_0)
-   [getCalls](././assert/~/assert.CallTracker#method_getcalls_0)
-   [report](././assert/~/assert.CallTracker#method_report_0)
-   [reset](././assert/~/assert.CallTracker#method_reset_0)
-   [verify](././assert/~/assert.CallTracker#method_verify_0)

We strongly discourage the use of the `async_hooks` API. Other APIs that can cover most of its use cases include:

I

[AsyncHook](././async_hooks/~/AsyncHook "AsyncHook")

No documentation available

-   [disable](././async_hooks/~/AsyncHook#method_disable_0)
-   [enable](././async_hooks/~/AsyncHook#method_enable_0)

c

[AsyncLocalStorage](././async_hooks/~/AsyncLocalStorage "AsyncLocalStorage")

This class creates stores that stay coherent through asynchronous operations.

-   [bind](././async_hooks/~/AsyncLocalStorage#method_bind_0)
-   [disable](././async_hooks/~/AsyncLocalStorage#method_disable_0)
-   [enterWith](././async_hooks/~/AsyncLocalStorage#method_enterwith_0)
-   [exit](././async_hooks/~/AsyncLocalStorage#method_exit_0)
-   [getStore](././async_hooks/~/AsyncLocalStorage#method_getstore_0)
-   [run](././async_hooks/~/AsyncLocalStorage#method_run_0)
-   [snapshot](././async_hooks/~/AsyncLocalStorage#method_snapshot_0)

c

[AsyncResource](././async_hooks/~/AsyncResource "AsyncResource")

No documentation available

-   [asyncId](././async_hooks/~/AsyncResource#method_asyncid_0)
-   [bind](././async_hooks/~/AsyncResource#method_bind_0)
-   [emitDestroy](././async_hooks/~/AsyncResource#method_emitdestroy_0)
-   [runInAsyncScope](././async_hooks/~/AsyncResource#method_runinasyncscope_0)
-   [triggerAsyncId](././async_hooks/~/AsyncResource#method_triggerasyncid_0)

I

[AsyncResourceOptions](././async_hooks/~/AsyncResourceOptions "AsyncResourceOptions")

No documentation available

-   [requireManualDestroy](././async_hooks/~/AsyncResourceOptions#property_requiremanualdestroy)
-   [triggerAsyncId](././async_hooks/~/AsyncResourceOptions#property_triggerasyncid)

f

[createHook](././async_hooks/~/createHook "createHook")

No documentation available

f

[executionAsyncId](././async_hooks/~/executionAsyncId "executionAsyncId")

No documentation available

f

[executionAsyncResource](././async_hooks/~/executionAsyncResource "executionAsyncResource")

Resource objects returned by `executionAsyncResource()` are most often internal Node.js handle objects with undocumented APIs. Using any functions or properties on the object is likely to crash your application and should be avoided.

I

[HookCallbacks](././async_hooks/~/HookCallbacks "HookCallbacks")

No documentation available

-   [after](././async_hooks/~/HookCallbacks#method_after_0)
-   [before](././async_hooks/~/HookCallbacks#method_before_0)
-   [destroy](././async_hooks/~/HookCallbacks#method_destroy_0)
-   [init](././async_hooks/~/HookCallbacks#method_init_0)
-   [promiseResolve](././async_hooks/~/HookCallbacks#method_promiseresolve_0)

f

[triggerAsyncId](././async_hooks/~/triggerAsyncId "triggerAsyncId")

Promise contexts may not get valid `triggerAsyncId`s by default. See the section on [promise execution tracking](https://nodejs.org/docs/latest-v22.x/api/async_hooks.html#promise-execution-tracking).

`Buffer` objects are used to represent a fixed-length sequence of bytes. Many Node.js APIs support `Buffer`s.

f

[atob](././buffer/~/atob "atob")

Decodes a string of Base64-encoded data into bytes, and encodes those bytes into a string using Latin-1 (ISO-8859-1).

c

I

v

[Blob](/api/web/~/Blob "Blob")

A [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) encapsulates immutable, raw data that can be safely shared across multiple worker threads.

-   [arrayBuffer](/api/web/~/Blob#method_arraybuffer_0)
-   [bytes](/api/web/~/Blob#method_bytes_0)
-   [size](/api/web/~/Blob#property_size)
-   [slice](/api/web/~/Blob#method_slice_0)
-   [stream](/api/web/~/Blob#method_stream_0)
-   [text](/api/web/~/Blob#method_text_0)
-   [type](/api/web/~/Blob#property_type)

I

[BlobOptions](././buffer/~/BlobOptions "BlobOptions")

No documentation available

-   [endings](././buffer/~/BlobOptions#property_endings)
-   [type](././buffer/~/BlobOptions#property_type)

f

[btoa](././buffer/~/btoa "btoa")

Decodes a string into bytes using Latin-1 (ISO-8859), and encodes those bytes into a string using Base64.

I

v

[Buffer](././buffer/~/Buffer "Buffer")

No documentation available

-   [compare](././buffer/~/Buffer#method_compare_0)
-   [copy](././buffer/~/Buffer#method_copy_0)
-   [equals](././buffer/~/Buffer#method_equals_0)
-   [fill](././buffer/~/Buffer#method_fill_0)
-   [includes](././buffer/~/Buffer#method_includes_0)
-   [indexOf](././buffer/~/Buffer#method_indexof_0)
-   [lastIndexOf](././buffer/~/Buffer#method_lastindexof_0)
-   [readBigInt64BE](././buffer/~/Buffer#method_readbigint64be_0)
-   [readBigInt64LE](././buffer/~/Buffer#method_readbigint64le_0)
-   [readBigUInt64BE](././buffer/~/Buffer#method_readbiguint64be_0)
-   [readBigUInt64LE](././buffer/~/Buffer#method_readbiguint64le_0)
-   [readBigUint64BE](././buffer/~/Buffer#method_readbiguint64be_0)
-   [readBigUint64LE](././buffer/~/Buffer#method_readbiguint64le_0)
-   [readDoubleBE](././buffer/~/Buffer#method_readdoublebe_0)
-   [readDoubleLE](././buffer/~/Buffer#method_readdoublele_0)
-   [readFloatBE](././buffer/~/Buffer#method_readfloatbe_0)
-   [readFloatLE](././buffer/~/Buffer#method_readfloatle_0)
-   [readInt16BE](././buffer/~/Buffer#method_readint16be_0)
-   [readInt16LE](././buffer/~/Buffer#method_readint16le_0)
-   [readInt32BE](././buffer/~/Buffer#method_readint32be_0)
-   [readInt32LE](././buffer/~/Buffer#method_readint32le_0)
-   [readInt8](././buffer/~/Buffer#method_readint8_0)
-   [readIntBE](././buffer/~/Buffer#method_readintbe_0)
-   [readIntLE](././buffer/~/Buffer#method_readintle_0)
-   [readUInt16BE](././buffer/~/Buffer#method_readuint16be_0)
-   [readUInt16LE](././buffer/~/Buffer#method_readuint16le_0)
-   [readUInt32BE](././buffer/~/Buffer#method_readuint32be_0)
-   [readUInt32LE](././buffer/~/Buffer#method_readuint32le_0)
-   [readUInt8](././buffer/~/Buffer#method_readuint8_0)
-   [readUIntBE](././buffer/~/Buffer#method_readuintbe_0)
-   [readUIntLE](././buffer/~/Buffer#method_readuintle_0)
-   [readUint16BE](././buffer/~/Buffer#method_readuint16be_0)
-   [readUint16LE](././buffer/~/Buffer#method_readuint16le_0)
-   [readUint32BE](././buffer/~/Buffer#method_readuint32be_0)
-   [readUint32LE](././buffer/~/Buffer#method_readuint32le_0)
-   [readUint8](././buffer/~/Buffer#method_readuint8_0)
-   [readUintBE](././buffer/~/Buffer#method_readuintbe_0)
-   [readUintLE](././buffer/~/Buffer#method_readuintle_0)
-   [reverse](././buffer/~/Buffer#method_reverse_0)
-   [slice](././buffer/~/Buffer#method_slice_0)
-   [subarray](././buffer/~/Buffer#method_subarray_0)
-   [swap16](././buffer/~/Buffer#method_swap16_0)
-   [swap32](././buffer/~/Buffer#method_swap32_0)
-   [swap64](././buffer/~/Buffer#method_swap64_0)
-   [toJSON](././buffer/~/Buffer#method_tojson_0)
-   [toString](././buffer/~/Buffer#method_tostring_0)
-   [write](././buffer/~/Buffer#method_write_0)
-   [writeBigInt64BE](././buffer/~/Buffer#method_writebigint64be_0)
-   [writeBigInt64LE](././buffer/~/Buffer#method_writebigint64le_0)
-   [writeBigUInt64BE](././buffer/~/Buffer#method_writebiguint64be_0)
-   [writeBigUInt64LE](././buffer/~/Buffer#method_writebiguint64le_0)
-   [writeBigUint64BE](././buffer/~/Buffer#method_writebiguint64be_0)
-   [writeBigUint64LE](././buffer/~/Buffer#method_writebiguint64le_0)
-   [writeDoubleBE](././buffer/~/Buffer#method_writedoublebe_0)
-   [writeDoubleLE](././buffer/~/Buffer#method_writedoublele_0)
-   [writeFloatBE](././buffer/~/Buffer#method_writefloatbe_0)
-   [writeFloatLE](././buffer/~/Buffer#method_writefloatle_0)
-   [writeInt16BE](././buffer/~/Buffer#method_writeint16be_0)
-   [writeInt16LE](././buffer/~/Buffer#method_writeint16le_0)
-   [writeInt32BE](././buffer/~/Buffer#method_writeint32be_0)
-   [writeInt32LE](././buffer/~/Buffer#method_writeint32le_0)
-   [writeInt8](././buffer/~/Buffer#method_writeint8_0)
-   [writeIntBE](././buffer/~/Buffer#method_writeintbe_0)
-   [writeIntLE](././buffer/~/Buffer#method_writeintle_0)
-   [writeUInt16BE](././buffer/~/Buffer#method_writeuint16be_0)
-   [writeUInt16LE](././buffer/~/Buffer#method_writeuint16le_0)
-   [writeUInt32BE](././buffer/~/Buffer#method_writeuint32be_0)
-   [writeUInt32LE](././buffer/~/Buffer#method_writeuint32le_0)
-   [writeUInt8](././buffer/~/Buffer#method_writeuint8_0)
-   [writeUIntBE](././buffer/~/Buffer#method_writeuintbe_0)
-   [writeUIntLE](././buffer/~/Buffer#method_writeuintle_0)
-   [writeUint16BE](././buffer/~/Buffer#method_writeuint16be_0)
-   [writeUint16LE](././buffer/~/Buffer#method_writeuint16le_0)
-   [writeUint32BE](././buffer/~/Buffer#method_writeuint32be_0)
-   [writeUint32LE](././buffer/~/Buffer#method_writeuint32le_0)
-   [writeUint8](././buffer/~/Buffer#method_writeuint8_0)
-   [writeUintBE](././buffer/~/Buffer#method_writeuintbe_0)
-   [writeUintLE](././buffer/~/Buffer#method_writeuintle_0)

I

[BufferConstructor](././buffer/~/BufferConstructor "BufferConstructor")

No documentation available

-   [alloc](././buffer/~/BufferConstructor#method_alloc_0)
-   [allocUnsafe](././buffer/~/BufferConstructor#method_allocunsafe_0)
-   [allocUnsafeSlow](././buffer/~/BufferConstructor#method_allocunsafeslow_0)
-   [byteLength](././buffer/~/BufferConstructor#method_bytelength_0)
-   [compare](././buffer/~/BufferConstructor#method_compare_0)
-   [concat](././buffer/~/BufferConstructor#method_concat_0)
-   [copyBytesFrom](././buffer/~/BufferConstructor#method_copybytesfrom_0)
-   [from](././buffer/~/BufferConstructor#method_from_0)
-   [isBuffer](././buffer/~/BufferConstructor#method_isbuffer_0)
-   [isEncoding](././buffer/~/BufferConstructor#method_isencoding_0)
-   [of](././buffer/~/BufferConstructor#method_of_0)
-   [poolSize](././buffer/~/BufferConstructor#property_poolsize)

T

[BufferEncoding](././buffer/~/BufferEncoding "BufferEncoding")

No documentation available

v

[constants](././buffer/~/constants "constants")

No documentation available

-   [MAX\_LENGTH](././buffer/~/constants#property_max_length)
-   [MAX\_STRING\_LENGTH](././buffer/~/constants#property_max_string_length)

c

I

v

[File](././buffer/~/File "File")

A [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File) provides information about files.

-   [lastModified](././buffer/~/File#property_lastmodified)
-   [name](././buffer/~/File#property_name)

I

[FileOptions](././buffer/~/FileOptions "FileOptions")

No documentation available

-   [endings](././buffer/~/FileOptions#property_endings)
-   [lastModified](././buffer/~/FileOptions#property_lastmodified)
-   [type](././buffer/~/FileOptions#property_type)

T

[ImplicitArrayBuffer](././buffer/~/ImplicitArrayBuffer "ImplicitArrayBuffer")

`Buffer` objects are used to represent a fixed-length sequence of bytes. Many Node.js APIs support `Buffer`s.

v

[INSPECT\_MAX\_BYTES](././buffer/~/INSPECT_MAX_BYTES "INSPECT_MAX_BYTES")

No documentation available

f

[isAscii](././buffer/~/isAscii "isAscii")

This function returns `true` if `input` contains only valid ASCII-encoded data, including the case in which `input` is empty.

f

[isUtf8](././buffer/~/isUtf8 "isUtf8")

This function returns `true` if `input` contains only valid UTF-8-encoded data, including the case in which `input` is empty.

v

[kMaxLength](././buffer/~/kMaxLength "kMaxLength")

No documentation available

v

[kStringMaxLength](././buffer/~/kStringMaxLength "kStringMaxLength")

No documentation available

f

[resolveObjectURL](././buffer/~/resolveObjectURL "resolveObjectURL")

Resolves a `'blob:nodedata:...'` an associated `Blob` object registered using a prior call to `URL.createObjectURL()`.

f

[transcode](././buffer/~/transcode "transcode")

Re-encodes the given `Buffer` or `Uint8Array` instance from one character encoding to another. Returns a new `Buffer` instance.

T

[TranscodeEncoding](././buffer/~/TranscodeEncoding "TranscodeEncoding")

No documentation available

T

[WithImplicitCoercion](././buffer/~/WithImplicitCoercion "WithImplicitCoercion")

No documentation available

v

[SlowBuffer](././buffer/~/SlowBuffer "SlowBuffer")

No documentation available

-   [prototype](././buffer/~/SlowBuffer#property_prototype)

The `node:child_process` module provides the ability to spawn subprocesses in a manner that is similar, but not identical, to [`popen(3)`](http://man7.org/linux/man-pages/man3/popen.3.html). This capability is primarily provided by the [spawn](././child_process/~/spawn) function:

c

[ChildProcess](././child_process/~/ChildProcess "ChildProcess")

Instances of the `ChildProcess` represent spawned child processes.

-   [addListener](././child_process/~/ChildProcess#method_addlistener_0)
-   [channel](././child_process/~/ChildProcess#property_channel)
-   [connected](././child_process/~/ChildProcess#property_connected)
-   [disconnect](././child_process/~/ChildProcess#method_disconnect_0)
-   [emit](././child_process/~/ChildProcess#method_emit_0)
-   [exitCode](././child_process/~/ChildProcess#property_exitcode)
-   [kill](././child_process/~/ChildProcess#method_kill_0)
-   [killed](././child_process/~/ChildProcess#property_killed)
-   [on](././child_process/~/ChildProcess#method_on_0)
-   [once](././child_process/~/ChildProcess#method_once_0)
-   [pid](././child_process/~/ChildProcess#property_pid)
-   [prependListener](././child_process/~/ChildProcess#method_prependlistener_0)
-   [prependOnceListener](././child_process/~/ChildProcess#method_prependoncelistener_0)
-   [ref](././child_process/~/ChildProcess#method_ref_0)
-   [send](././child_process/~/ChildProcess#method_send_0)
-   [signalCode](././child_process/~/ChildProcess#property_signalcode)
-   [spawnargs](././child_process/~/ChildProcess#property_spawnargs)
-   [spawnfile](././child_process/~/ChildProcess#property_spawnfile)
-   [stderr](././child_process/~/ChildProcess#property_stderr)
-   [stdin](././child_process/~/ChildProcess#property_stdin)
-   [stdio](././child_process/~/ChildProcess#property_stdio)
-   [stdout](././child_process/~/ChildProcess#property_stdout)
-   [unref](././child_process/~/ChildProcess#method_unref_0)

I

[ChildProcessByStdio](././child_process/~/ChildProcessByStdio "ChildProcessByStdio")

No documentation available

-   [stderr](././child_process/~/ChildProcessByStdio#property_stderr)
-   [stdin](././child_process/~/ChildProcessByStdio#property_stdin)
-   [stdio](././child_process/~/ChildProcessByStdio#property_stdio)
-   [stdout](././child_process/~/ChildProcessByStdio#property_stdout)

I

[ChildProcessWithoutNullStreams](././child_process/~/ChildProcessWithoutNullStreams "ChildProcessWithoutNullStreams")

No documentation available

-   [stderr](././child_process/~/ChildProcessWithoutNullStreams#property_stderr)
-   [stdin](././child_process/~/ChildProcessWithoutNullStreams#property_stdin)
-   [stdio](././child_process/~/ChildProcessWithoutNullStreams#property_stdio)
-   [stdout](././child_process/~/ChildProcessWithoutNullStreams#property_stdout)

I

[CommonExecOptions](././child_process/~/CommonExecOptions "CommonExecOptions")

No documentation available

-   [encoding](././child_process/~/CommonExecOptions#property_encoding)
-   [input](././child_process/~/CommonExecOptions#property_input)
-   [killSignal](././child_process/~/CommonExecOptions#property_killsignal)
-   [maxBuffer](././child_process/~/CommonExecOptions#property_maxbuffer)
-   [stdio](././child_process/~/CommonExecOptions#property_stdio)

I

[CommonOptions](././child_process/~/CommonOptions "CommonOptions")

No documentation available

-   [timeout](././child_process/~/CommonOptions#property_timeout)
-   [windowsHide](././child_process/~/CommonOptions#property_windowshide)

I

[CommonSpawnOptions](././child_process/~/CommonSpawnOptions "CommonSpawnOptions")

No documentation available

-   [argv0](././child_process/~/CommonSpawnOptions#property_argv0)
-   [shell](././child_process/~/CommonSpawnOptions#property_shell)
-   [stdio](././child_process/~/CommonSpawnOptions#property_stdio)
-   [windowsVerbatimArguments](././child_process/~/CommonSpawnOptions#property_windowsverbatimarguments)

f

[exec](././child_process/~/exec "exec")

Spawns a shell then executes the `command` within that shell, buffering any generated output. The `command` string passed to the exec function is processed directly by the shell and special characters (vary based on [shell](https://en.wikipedia.org/wiki/List_of_command-line_interpreters)) need to be dealt with accordingly:

I

[ExecException](././child_process/~/ExecException "ExecException")

No documentation available

-   [cmd](././child_process/~/ExecException#property_cmd)
-   [code](././child_process/~/ExecException#property_code)
-   [killed](././child_process/~/ExecException#property_killed)
-   [signal](././child_process/~/ExecException#property_signal)
-   [stderr](././child_process/~/ExecException#property_stderr)
-   [stdout](././child_process/~/ExecException#property_stdout)

f

[execFile](././child_process/~/execFile "execFile")

The `child_process.execFile()` function is similar to [exec](././child_process/~/exec) except that it does not spawn a shell by default. Rather, the specified executable `file` is spawned directly as a new process making it slightly more efficient than [exec](././child_process/~/exec).

T

[ExecFileException](././child_process/~/ExecFileException "ExecFileException")

No documentation available

I

[ExecFileOptions](././child_process/~/ExecFileOptions "ExecFileOptions")

No documentation available

-   [killSignal](././child_process/~/ExecFileOptions#property_killsignal)
-   [maxBuffer](././child_process/~/ExecFileOptions#property_maxbuffer)
-   [shell](././child_process/~/ExecFileOptions#property_shell)
-   [signal](././child_process/~/ExecFileOptions#property_signal)
-   [windowsVerbatimArguments](././child_process/~/ExecFileOptions#property_windowsverbatimarguments)

I

[ExecFileOptionsWithBufferEncoding](././child_process/~/ExecFileOptionsWithBufferEncoding "ExecFileOptionsWithBufferEncoding")

No documentation available

-   [encoding](././child_process/~/ExecFileOptionsWithBufferEncoding#property_encoding)

I

[ExecFileOptionsWithOtherEncoding](././child_process/~/ExecFileOptionsWithOtherEncoding "ExecFileOptionsWithOtherEncoding")

No documentation available

-   [encoding](././child_process/~/ExecFileOptionsWithOtherEncoding#property_encoding)

I

[ExecFileOptionsWithStringEncoding](././child_process/~/ExecFileOptionsWithStringEncoding "ExecFileOptionsWithStringEncoding")

No documentation available

-   [encoding](././child_process/~/ExecFileOptionsWithStringEncoding#property_encoding)

f

[execFileSync](././child_process/~/execFileSync "execFileSync")

The `child_process.execFileSync()` method is generally identical to [execFile](././child_process/~/execFile) with the exception that the method will not return until the child process has fully closed. When a timeout has been encountered and `killSignal` is sent, the method won't return until the process has completely exited.

I

[ExecFileSyncOptions](././child_process/~/ExecFileSyncOptions "ExecFileSyncOptions")

No documentation available

-   [shell](././child_process/~/ExecFileSyncOptions#property_shell)

I

[ExecFileSyncOptionsWithBufferEncoding](././child_process/~/ExecFileSyncOptionsWithBufferEncoding "ExecFileSyncOptionsWithBufferEncoding")

No documentation available

-   [encoding](././child_process/~/ExecFileSyncOptionsWithBufferEncoding#property_encoding)

I

[ExecFileSyncOptionsWithStringEncoding](././child_process/~/ExecFileSyncOptionsWithStringEncoding "ExecFileSyncOptionsWithStringEncoding")

No documentation available

-   [encoding](././child_process/~/ExecFileSyncOptionsWithStringEncoding#property_encoding)

I

[ExecOptions](././child_process/~/ExecOptions "ExecOptions")

No documentation available

-   [killSignal](././child_process/~/ExecOptions#property_killsignal)
-   [maxBuffer](././child_process/~/ExecOptions#property_maxbuffer)
-   [shell](././child_process/~/ExecOptions#property_shell)
-   [signal](././child_process/~/ExecOptions#property_signal)

I

[ExecOptionsWithBufferEncoding](././child_process/~/ExecOptionsWithBufferEncoding "ExecOptionsWithBufferEncoding")

No documentation available

-   [encoding](././child_process/~/ExecOptionsWithBufferEncoding#property_encoding)

I

[ExecOptionsWithStringEncoding](././child_process/~/ExecOptionsWithStringEncoding "ExecOptionsWithStringEncoding")

No documentation available

-   [encoding](././child_process/~/ExecOptionsWithStringEncoding#property_encoding)

f

[execSync](././child_process/~/execSync "execSync")

The `child_process.execSync()` method is generally identical to [exec](././child_process/~/exec) with the exception that the method will not return until the child process has fully closed. When a timeout has been encountered and `killSignal` is sent, the method won't return until the process has completely exited. If the child process intercepts and handles the `SIGTERM` signal and doesn't exit, the parent process will wait until the child process has exited.

I

[ExecSyncOptions](././child_process/~/ExecSyncOptions "ExecSyncOptions")

No documentation available

-   [shell](././child_process/~/ExecSyncOptions#property_shell)

I

[ExecSyncOptionsWithBufferEncoding](././child_process/~/ExecSyncOptionsWithBufferEncoding "ExecSyncOptionsWithBufferEncoding")

No documentation available

-   [encoding](././child_process/~/ExecSyncOptionsWithBufferEncoding#property_encoding)

I

[ExecSyncOptionsWithStringEncoding](././child_process/~/ExecSyncOptionsWithStringEncoding "ExecSyncOptionsWithStringEncoding")

No documentation available

-   [encoding](././child_process/~/ExecSyncOptionsWithStringEncoding#property_encoding)

f

[fork](././child_process/~/fork "fork")

The `child_process.fork()` method is a special case of [spawn](././child_process/~/spawn) used specifically to spawn new Node.js processes. Like [spawn](././child_process/~/spawn), a `ChildProcess` object is returned. The returned `ChildProcess` will have an additional communication channel built-in that allows messages to be passed back and forth between the parent and child. See `subprocess.send()` for details.

I

[ForkOptions](././child_process/~/ForkOptions "ForkOptions")

No documentation available

-   [detached](././child_process/~/ForkOptions#property_detached)
-   [execArgv](././child_process/~/ForkOptions#property_execargv)
-   [execPath](././child_process/~/ForkOptions#property_execpath)
-   [silent](././child_process/~/ForkOptions#property_silent)
-   [stdio](././child_process/~/ForkOptions#property_stdio)
-   [windowsVerbatimArguments](././child_process/~/ForkOptions#property_windowsverbatimarguments)

T

[IOType](././child_process/~/IOType "IOType")

No documentation available

I

[MessageOptions](././child_process/~/MessageOptions "MessageOptions")

No documentation available

-   [keepOpen](././child_process/~/MessageOptions#property_keepopen)

I

[MessagingOptions](././child_process/~/MessagingOptions "MessagingOptions")

No documentation available

-   [killSignal](././child_process/~/MessagingOptions#property_killsignal)
-   [serialization](././child_process/~/MessagingOptions#property_serialization)
-   [timeout](././child_process/~/MessagingOptions#property_timeout)

I

[ProcessEnvOptions](././child_process/~/ProcessEnvOptions "ProcessEnvOptions")

No documentation available

-   [cwd](././child_process/~/ProcessEnvOptions#property_cwd)
-   [env](././child_process/~/ProcessEnvOptions#property_env)
-   [gid](././child_process/~/ProcessEnvOptions#property_gid)
-   [uid](././child_process/~/ProcessEnvOptions#property_uid)

I

[PromiseWithChild](././child_process/~/PromiseWithChild "PromiseWithChild")

No documentation available

-   [child](././child_process/~/PromiseWithChild#property_child)

T

[SendHandle](././child_process/~/SendHandle "SendHandle")

No documentation available

T

[Serializable](././child_process/~/Serializable "Serializable")

No documentation available

T

[SerializationType](././child_process/~/SerializationType "SerializationType")

No documentation available

f

[spawn](././child_process/~/spawn "spawn")

The `child_process.spawn()` method spawns a new process using the given `command`, with command-line arguments in `args`. If omitted, `args` defaults to an empty array.

I

[SpawnOptions](././child_process/~/SpawnOptions "SpawnOptions")

No documentation available

-   [detached](././child_process/~/SpawnOptions#property_detached)

I

[SpawnOptionsWithoutStdio](././child_process/~/SpawnOptionsWithoutStdio "SpawnOptionsWithoutStdio")

No documentation available

-   [stdio](././child_process/~/SpawnOptionsWithoutStdio#property_stdio)

I

[SpawnOptionsWithStdioTuple](././child_process/~/SpawnOptionsWithStdioTuple "SpawnOptionsWithStdioTuple")

No documentation available

-   [stdio](././child_process/~/SpawnOptionsWithStdioTuple#property_stdio)

f

[spawnSync](././child_process/~/spawnSync "spawnSync")

The `child_process.spawnSync()` method is generally identical to [spawn](././child_process/~/spawn) with the exception that the function will not return until the child process has fully closed. When a timeout has been encountered and `killSignal` is sent, the method won't return until the process has completely exited. If the process intercepts and handles the `SIGTERM` signal and doesn't exit, the parent process will wait until the child process has exited.

I

[SpawnSyncOptions](././child_process/~/SpawnSyncOptions "SpawnSyncOptions")

No documentation available

-   [encoding](././child_process/~/SpawnSyncOptions#property_encoding)
-   [input](././child_process/~/SpawnSyncOptions#property_input)
-   [maxBuffer](././child_process/~/SpawnSyncOptions#property_maxbuffer)

I

[SpawnSyncOptionsWithBufferEncoding](././child_process/~/SpawnSyncOptionsWithBufferEncoding "SpawnSyncOptionsWithBufferEncoding")

No documentation available

-   [encoding](././child_process/~/SpawnSyncOptionsWithBufferEncoding#property_encoding)

I

[SpawnSyncOptionsWithStringEncoding](././child_process/~/SpawnSyncOptionsWithStringEncoding "SpawnSyncOptionsWithStringEncoding")

No documentation available

-   [encoding](././child_process/~/SpawnSyncOptionsWithStringEncoding#property_encoding)

I

[SpawnSyncReturns](././child_process/~/SpawnSyncReturns "SpawnSyncReturns")

No documentation available

-   [error](././child_process/~/SpawnSyncReturns#property_error)
-   [output](././child_process/~/SpawnSyncReturns#property_output)
-   [pid](././child_process/~/SpawnSyncReturns#property_pid)
-   [signal](././child_process/~/SpawnSyncReturns#property_signal)
-   [status](././child_process/~/SpawnSyncReturns#property_status)
-   [stderr](././child_process/~/SpawnSyncReturns#property_stderr)
-   [stdout](././child_process/~/SpawnSyncReturns#property_stdout)

T

[StdioNull](././child_process/~/StdioNull "StdioNull")

No documentation available

T

[StdioOptions](././child_process/~/StdioOptions "StdioOptions")

No documentation available

T

[StdioPipe](././child_process/~/StdioPipe "StdioPipe")

No documentation available

T

[StdioPipeNamed](././child_process/~/StdioPipeNamed "StdioPipeNamed")

No documentation available

I

[Address](././cluster/~/Address "Address")

No documentation available

-   [address](././cluster/~/Address#property_address)
-   [addressType](././cluster/~/Address#property_addresstype)
-   [port](././cluster/~/Address#property_port)

I

[Cluster](././cluster/~/Cluster "Cluster")

No documentation available

-   [SCHED\_NONE](././cluster/~/Cluster#property_sched_none)
-   [SCHED\_RR](././cluster/~/Cluster#property_sched_rr)
-   [addListener](././cluster/~/Cluster#method_addlistener_0)
-   [disconnect](././cluster/~/Cluster#method_disconnect_0)
-   [emit](././cluster/~/Cluster#method_emit_0)
-   [fork](././cluster/~/Cluster#method_fork_0)
-   [isMaster](././cluster/~/Cluster#property_ismaster)
-   [isPrimary](././cluster/~/Cluster#property_isprimary)
-   [isWorker](././cluster/~/Cluster#property_isworker)
-   [on](././cluster/~/Cluster#method_on_0)
-   [once](././cluster/~/Cluster#method_once_0)
-   [prependListener](././cluster/~/Cluster#method_prependlistener_0)
-   [prependOnceListener](././cluster/~/Cluster#method_prependoncelistener_0)
-   [schedulingPolicy](././cluster/~/Cluster#property_schedulingpolicy)
-   [settings](././cluster/~/Cluster#property_settings)
-   [setupMaster](././cluster/~/Cluster#method_setupmaster_0)
-   [setupPrimary](././cluster/~/Cluster#method_setupprimary_0)
-   [worker](././cluster/~/Cluster#property_worker)
-   [workers](././cluster/~/Cluster#property_workers)

v

[cluster](././cluster/~/cluster "cluster")

No documentation available

I

[ClusterSettings](././cluster/~/ClusterSettings "ClusterSettings")

No documentation available

-   [args](././cluster/~/ClusterSettings#property_args)
-   [cwd](././cluster/~/ClusterSettings#property_cwd)
-   [exec](././cluster/~/ClusterSettings#property_exec)
-   [execArgv](././cluster/~/ClusterSettings#property_execargv)
-   [gid](././cluster/~/ClusterSettings#property_gid)
-   [inspectPort](././cluster/~/ClusterSettings#property_inspectport)
-   [serialization](././cluster/~/ClusterSettings#property_serialization)
-   [silent](././cluster/~/ClusterSettings#property_silent)
-   [stdio](././cluster/~/ClusterSettings#property_stdio)
-   [uid](././cluster/~/ClusterSettings#property_uid)
-   [windowsHide](././cluster/~/ClusterSettings#property_windowshide)

v

[default](././cluster/~/default "default")

No documentation available

T

[SerializationType](././cluster/~/SerializationType "SerializationType")

No documentation available

c

[Worker](././cluster/~/Worker "Worker")

No documentation available

-   [addListener](././cluster/~/Worker#method_addlistener_0)
-   [destroy](././cluster/~/Worker#method_destroy_0)
-   [disconnect](././cluster/~/Worker#method_disconnect_0)
-   [emit](././cluster/~/Worker#method_emit_0)
-   [exitedAfterDisconnect](././cluster/~/Worker#property_exitedafterdisconnect)
-   [id](././cluster/~/Worker#property_id)
-   [isConnected](././cluster/~/Worker#method_isconnected_0)
-   [isDead](././cluster/~/Worker#method_isdead_0)
-   [kill](././cluster/~/Worker#method_kill_0)
-   [on](././cluster/~/Worker#method_on_0)
-   [once](././cluster/~/Worker#method_once_0)
-   [prependListener](././cluster/~/Worker#method_prependlistener_0)
-   [prependOnceListener](././cluster/~/Worker#method_prependoncelistener_0)
-   [process](././cluster/~/Worker#property_process)
-   [send](././cluster/~/Worker#method_send_0)

The `node:console` module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

I

[Console](././console/~/Console "Console")

No documentation available

-   [Console](././console/~/Console#property_console)
-   [assert](././console/~/Console#method_assert_0)
-   [clear](././console/~/Console#method_clear_0)
-   [count](././console/~/Console#method_count_0)
-   [countReset](././console/~/Console#method_countreset_0)
-   [debug](././console/~/Console#method_debug_0)
-   [dir](././console/~/Console#method_dir_0)
-   [dirxml](././console/~/Console#method_dirxml_0)
-   [error](././console/~/Console#method_error_0)
-   [group](././console/~/Console#method_group_0)
-   [groupCollapsed](././console/~/Console#method_groupcollapsed_0)
-   [groupEnd](././console/~/Console#method_groupend_0)
-   [info](././console/~/Console#method_info_0)
-   [log](././console/~/Console#method_log_0)
-   [profile](././console/~/Console#method_profile_0)
-   [profileEnd](././console/~/Console#method_profileend_0)
-   [table](././console/~/Console#method_table_0)
-   [time](././console/~/Console#method_time_0)
-   [timeEnd](././console/~/Console#method_timeend_0)
-   [timeLog](././console/~/Console#method_timelog_0)
-   [timeStamp](././console/~/Console#method_timestamp_0)
-   [trace](././console/~/Console#method_trace_0)
-   [warn](././console/~/Console#method_warn_0)

N

v

[console](././console/~/console "console")

The `console` module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.

I

[console.ConsoleConstructor](././console/~/console.ConsoleConstructor "console.ConsoleConstructor")

No documentation available

-   [prototype](././console/~/console.ConsoleConstructor#property_prototype)

I

[console.ConsoleConstructorOptions](././console/~/console.ConsoleConstructorOptions "console.ConsoleConstructorOptions")

No documentation available

-   [colorMode](././console/~/console.ConsoleConstructorOptions#property_colormode)
-   [groupIndentation](././console/~/console.ConsoleConstructorOptions#property_groupindentation)
-   [ignoreErrors](././console/~/console.ConsoleConstructorOptions#property_ignoreerrors)
-   [inspectOptions](././console/~/console.ConsoleConstructorOptions#property_inspectoptions)
-   [stderr](././console/~/console.ConsoleConstructorOptions#property_stderr)
-   [stdout](././console/~/console.ConsoleConstructorOptions#property_stdout)

v

[constants](././constants/~/constants "constants")

No documentation available

v

[default](././constants/~/default "default")

No documentation available

The `node:crypto` module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

I

[AsymmetricKeyDetails](././crypto/~/AsymmetricKeyDetails "AsymmetricKeyDetails")

No documentation available

-   [divisorLength](././crypto/~/AsymmetricKeyDetails#property_divisorlength)
-   [hashAlgorithm](././crypto/~/AsymmetricKeyDetails#property_hashalgorithm)
-   [mgf1HashAlgorithm](././crypto/~/AsymmetricKeyDetails#property_mgf1hashalgorithm)
-   [modulusLength](././crypto/~/AsymmetricKeyDetails#property_moduluslength)
-   [namedCurve](././crypto/~/AsymmetricKeyDetails#property_namedcurve)
-   [publicExponent](././crypto/~/AsymmetricKeyDetails#property_publicexponent)
-   [saltLength](././crypto/~/AsymmetricKeyDetails#property_saltlength)

I

[BasePrivateKeyEncodingOptions](././crypto/~/BasePrivateKeyEncodingOptions "BasePrivateKeyEncodingOptions")

No documentation available

-   [cipher](././crypto/~/BasePrivateKeyEncodingOptions#property_cipher)
-   [format](././crypto/~/BasePrivateKeyEncodingOptions#property_format)
-   [passphrase](././crypto/~/BasePrivateKeyEncodingOptions#property_passphrase)

T

[BinaryLike](././crypto/~/BinaryLike "BinaryLike")

No documentation available

T

[BinaryToTextEncoding](././crypto/~/BinaryToTextEncoding "BinaryToTextEncoding")

No documentation available

c

[Certificate](././crypto/~/Certificate "Certificate")

No documentation available

-   [exportChallenge](././crypto/~/Certificate#method_exportchallenge_0)
-   [exportPublicKey](././crypto/~/Certificate#method_exportpublickey_0)
-   [verifySpkac](././crypto/~/Certificate#method_verifyspkac_0)

T

[CharacterEncoding](././crypto/~/CharacterEncoding "CharacterEncoding")

No documentation available

f

[checkPrime](././crypto/~/checkPrime "checkPrime")

Checks the primality of the `candidate`.

I

[CheckPrimeOptions](././crypto/~/CheckPrimeOptions "CheckPrimeOptions")

No documentation available

-   [checks](././crypto/~/CheckPrimeOptions#property_checks)

f

[checkPrimeSync](././crypto/~/checkPrimeSync "checkPrimeSync")

Checks the primality of the `candidate`.

c

[Cipher](././crypto/~/Cipher "Cipher")

Instances of the `Cipher` class are used to encrypt data. The class can be used in one of two ways:

-   [final](././crypto/~/Cipher#method_final_0)
-   [setAutoPadding](././crypto/~/Cipher#method_setautopadding_0)
-   [update](././crypto/~/Cipher#method_update_0)

I

[CipherCCM](././crypto/~/CipherCCM "CipherCCM")

No documentation available

-   [getAuthTag](././crypto/~/CipherCCM#method_getauthtag_0)
-   [setAAD](././crypto/~/CipherCCM#method_setaad_0)

I

[CipherCCMOptions](././crypto/~/CipherCCMOptions "CipherCCMOptions")

No documentation available

-   [authTagLength](././crypto/~/CipherCCMOptions#property_authtaglength)

T

[CipherCCMTypes](././crypto/~/CipherCCMTypes "CipherCCMTypes")

No documentation available

I

[CipherChaCha20Poly1305](././crypto/~/CipherChaCha20Poly1305 "CipherChaCha20Poly1305")

No documentation available

-   [getAuthTag](././crypto/~/CipherChaCha20Poly1305#method_getauthtag_0)
-   [setAAD](././crypto/~/CipherChaCha20Poly1305#method_setaad_0)

I

[CipherChaCha20Poly1305Options](././crypto/~/CipherChaCha20Poly1305Options "CipherChaCha20Poly1305Options")

No documentation available

-   [authTagLength](././crypto/~/CipherChaCha20Poly1305Options#property_authtaglength)

T

[CipherChaCha20Poly1305Types](././crypto/~/CipherChaCha20Poly1305Types "CipherChaCha20Poly1305Types")

No documentation available

I

[CipherGCM](././crypto/~/CipherGCM "CipherGCM")

No documentation available

-   [getAuthTag](././crypto/~/CipherGCM#method_getauthtag_0)
-   [setAAD](././crypto/~/CipherGCM#method_setaad_0)

I

[CipherGCMOptions](././crypto/~/CipherGCMOptions "CipherGCMOptions")

No documentation available

-   [authTagLength](././crypto/~/CipherGCMOptions#property_authtaglength)

T

[CipherGCMTypes](././crypto/~/CipherGCMTypes "CipherGCMTypes")

No documentation available

I

[CipherInfo](././crypto/~/CipherInfo "CipherInfo")

No documentation available

-   [blockSize](././crypto/~/CipherInfo#property_blocksize)
-   [ivLength](././crypto/~/CipherInfo#property_ivlength)
-   [keyLength](././crypto/~/CipherInfo#property_keylength)
-   [mode](././crypto/~/CipherInfo#property_mode)
-   [name](././crypto/~/CipherInfo#property_name)
-   [nid](././crypto/~/CipherInfo#property_nid)

I

[CipherInfoOptions](././crypto/~/CipherInfoOptions "CipherInfoOptions")

No documentation available

-   [ivLength](././crypto/~/CipherInfoOptions#property_ivlength)
-   [keyLength](././crypto/~/CipherInfoOptions#property_keylength)

T

[CipherKey](././crypto/~/CipherKey "CipherKey")

No documentation available

T

[CipherMode](././crypto/~/CipherMode "CipherMode")

No documentation available

I

[CipherOCB](././crypto/~/CipherOCB "CipherOCB")

No documentation available

-   [getAuthTag](././crypto/~/CipherOCB#method_getauthtag_0)
-   [setAAD](././crypto/~/CipherOCB#method_setaad_0)

I

[CipherOCBOptions](././crypto/~/CipherOCBOptions "CipherOCBOptions")

No documentation available

-   [authTagLength](././crypto/~/CipherOCBOptions#property_authtaglength)

T

[CipherOCBTypes](././crypto/~/CipherOCBTypes "CipherOCBTypes")

No documentation available

N

[constants](././crypto/~/constants "constants")

No documentation available

v

[constants.defaultCipherList](././crypto/~/constants.defaultCipherList "constants.defaultCipherList")

Specifies the active default cipher list used by the current Node.js process (colon-separated values).

v

[constants.defaultCoreCipherList](././crypto/~/constants.defaultCoreCipherList "constants.defaultCoreCipherList")

Specifies the built-in default cipher list used by Node.js (colon-separated values).

v

[constants.DH\_CHECK\_P\_NOT\_PRIME](././crypto/~/constants.DH_CHECK_P_NOT_PRIME "constants.DH_CHECK_P_NOT_PRIME")

No documentation available

v

[constants.DH\_CHECK\_P\_NOT\_SAFE\_PRIME](././crypto/~/constants.DH_CHECK_P_NOT_SAFE_PRIME "constants.DH_CHECK_P_NOT_SAFE_PRIME")

No documentation available

v

[constants.DH\_NOT\_SUITABLE\_GENERATOR](././crypto/~/constants.DH_NOT_SUITABLE_GENERATOR "constants.DH_NOT_SUITABLE_GENERATOR")

No documentation available

v

[constants.DH\_UNABLE\_TO\_CHECK\_GENERATOR](././crypto/~/constants.DH_UNABLE_TO_CHECK_GENERATOR "constants.DH_UNABLE_TO_CHECK_GENERATOR")

No documentation available

v

[constants.ENGINE\_METHOD\_ALL](././crypto/~/constants.ENGINE_METHOD_ALL "constants.ENGINE_METHOD_ALL")

No documentation available

v

[constants.ENGINE\_METHOD\_CIPHERS](././crypto/~/constants.ENGINE_METHOD_CIPHERS "constants.ENGINE_METHOD_CIPHERS")

No documentation available

v

[constants.ENGINE\_METHOD\_DH](././crypto/~/constants.ENGINE_METHOD_DH "constants.ENGINE_METHOD_DH")

No documentation available

v

[constants.ENGINE\_METHOD\_DIGESTS](././crypto/~/constants.ENGINE_METHOD_DIGESTS "constants.ENGINE_METHOD_DIGESTS")

No documentation available

v

[constants.ENGINE\_METHOD\_DSA](././crypto/~/constants.ENGINE_METHOD_DSA "constants.ENGINE_METHOD_DSA")

No documentation available

v

[constants.ENGINE\_METHOD\_EC](././crypto/~/constants.ENGINE_METHOD_EC "constants.ENGINE_METHOD_EC")

No documentation available

v

[constants.ENGINE\_METHOD\_NONE](././crypto/~/constants.ENGINE_METHOD_NONE "constants.ENGINE_METHOD_NONE")

No documentation available

v

[constants.ENGINE\_METHOD\_PKEY\_ASN1\_METHS](././crypto/~/constants.ENGINE_METHOD_PKEY_ASN1_METHS "constants.ENGINE_METHOD_PKEY_ASN1_METHS")

No documentation available

v

[constants.ENGINE\_METHOD\_PKEY\_METHS](././crypto/~/constants.ENGINE_METHOD_PKEY_METHS "constants.ENGINE_METHOD_PKEY_METHS")

No documentation available

v

[constants.ENGINE\_METHOD\_RAND](././crypto/~/constants.ENGINE_METHOD_RAND "constants.ENGINE_METHOD_RAND")

No documentation available

v

[constants.ENGINE\_METHOD\_RSA](././crypto/~/constants.ENGINE_METHOD_RSA "constants.ENGINE_METHOD_RSA")

No documentation available

v

[constants.OPENSSL\_VERSION\_NUMBER](././crypto/~/constants.OPENSSL_VERSION_NUMBER "constants.OPENSSL_VERSION_NUMBER")

No documentation available

v

[constants.POINT\_CONVERSION\_COMPRESSED](././crypto/~/constants.POINT_CONVERSION_COMPRESSED "constants.POINT_CONVERSION_COMPRESSED")

No documentation available

v

[constants.POINT\_CONVERSION\_HYBRID](././crypto/~/constants.POINT_CONVERSION_HYBRID "constants.POINT_CONVERSION_HYBRID")

No documentation available

v

[constants.POINT\_CONVERSION\_UNCOMPRESSED](././crypto/~/constants.POINT_CONVERSION_UNCOMPRESSED "constants.POINT_CONVERSION_UNCOMPRESSED")

No documentation available

v

[constants.RSA\_NO\_PADDING](././crypto/~/constants.RSA_NO_PADDING "constants.RSA_NO_PADDING")

No documentation available

v

[constants.RSA\_PKCS1\_OAEP\_PADDING](././crypto/~/constants.RSA_PKCS1_OAEP_PADDING "constants.RSA_PKCS1_OAEP_PADDING")

No documentation available

v

[constants.RSA\_PKCS1\_PADDING](././crypto/~/constants.RSA_PKCS1_PADDING "constants.RSA_PKCS1_PADDING")

No documentation available

v

[constants.RSA\_PKCS1\_PSS\_PADDING](././crypto/~/constants.RSA_PKCS1_PSS_PADDING "constants.RSA_PKCS1_PSS_PADDING")

No documentation available

v

[constants.RSA\_PSS\_SALTLEN\_AUTO](././crypto/~/constants.RSA_PSS_SALTLEN_AUTO "constants.RSA_PSS_SALTLEN_AUTO")

Causes the salt length for RSA\_PKCS1\_PSS\_PADDING to be determined automatically when verifying a signature.

v

[constants.RSA\_PSS\_SALTLEN\_DIGEST](././crypto/~/constants.RSA_PSS_SALTLEN_DIGEST "constants.RSA_PSS_SALTLEN_DIGEST")

Sets the salt length for RSA\_PKCS1\_PSS\_PADDING to the digest size when signing or verifying.

v

[constants.RSA\_PSS\_SALTLEN\_MAX\_SIGN](././crypto/~/constants.RSA_PSS_SALTLEN_MAX_SIGN "constants.RSA_PSS_SALTLEN_MAX_SIGN")

Sets the salt length for RSA\_PKCS1\_PSS\_PADDING to the maximum permissible value when signing data.

v

[constants.RSA\_SSLV23\_PADDING](././crypto/~/constants.RSA_SSLV23_PADDING "constants.RSA_SSLV23_PADDING")

No documentation available

v

[constants.RSA\_X931\_PADDING](././crypto/~/constants.RSA_X931_PADDING "constants.RSA_X931_PADDING")

No documentation available

v

[constants.SSL\_OP\_ALL](././crypto/~/constants.SSL_OP_ALL "constants.SSL_OP_ALL")

Applies multiple bug workarounds within OpenSSL. See [https://www.openssl.org/docs/man1.0.2/ssl/SSL\_CTX\_set\_options.html](https://www.openssl.org/docs/man1.0.2/ssl/SSL_CTX_set_options.html) for detail.

v

[constants.SSL\_OP\_ALLOW\_NO\_DHE\_KEX](././crypto/~/constants.SSL_OP_ALLOW_NO_DHE_KEX "constants.SSL_OP_ALLOW_NO_DHE_KEX")

Instructs OpenSSL to allow a non-\[EC\]DHE-based key exchange mode for TLS v1.3

v

[constants.SSL\_OP\_ALLOW\_UNSAFE\_LEGACY\_RENEGOTIATION](././crypto/~/constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION "constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION")

Allows legacy insecure renegotiation between OpenSSL and unpatched clients or servers. See [https://www.openssl.org/docs/man1.0.2/ssl/SSL\_CTX\_set\_options.html](https://www.openssl.org/docs/man1.0.2/ssl/SSL_CTX_set_options.html).

v

[constants.SSL\_OP\_CIPHER\_SERVER\_PREFERENCE](././crypto/~/constants.SSL_OP_CIPHER_SERVER_PREFERENCE "constants.SSL_OP_CIPHER_SERVER_PREFERENCE")

Attempts to use the server's preferences instead of the client's when selecting a cipher. See [https://www.openssl.org/docs/man1.0.2/ssl/SSL\_CTX\_set\_options.html](https://www.openssl.org/docs/man1.0.2/ssl/SSL_CTX_set_options.html).

v

[constants.SSL\_OP\_CISCO\_ANYCONNECT](././crypto/~/constants.SSL_OP_CISCO_ANYCONNECT "constants.SSL_OP_CISCO_ANYCONNECT")

Instructs OpenSSL to use Cisco's version identifier of DTLS\_BAD\_VER.

v

[constants.SSL\_OP\_COOKIE\_EXCHANGE](././crypto/~/constants.SSL_OP_COOKIE_EXCHANGE "constants.SSL_OP_COOKIE_EXCHANGE")

Instructs OpenSSL to turn on cookie exchange.

v

[constants.SSL\_OP\_CRYPTOPRO\_TLSEXT\_BUG](././crypto/~/constants.SSL_OP_CRYPTOPRO_TLSEXT_BUG "constants.SSL_OP_CRYPTOPRO_TLSEXT_BUG")

Instructs OpenSSL to add server-hello extension from an early version of the cryptopro draft.

v

[constants.SSL\_OP\_DONT\_INSERT\_EMPTY\_FRAGMENTS](././crypto/~/constants.SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS "constants.SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS")

Instructs OpenSSL to disable a SSL 3.0/TLS 1.0 vulnerability workaround added in OpenSSL 0.9.6d.

v

[constants.SSL\_OP\_LEGACY\_SERVER\_CONNECT](././crypto/~/constants.SSL_OP_LEGACY_SERVER_CONNECT "constants.SSL_OP_LEGACY_SERVER_CONNECT")

Allows initial connection to servers that do not support RI.

v

[constants.SSL\_OP\_NO\_COMPRESSION](././crypto/~/constants.SSL_OP_NO_COMPRESSION "constants.SSL_OP_NO_COMPRESSION")

Instructs OpenSSL to disable support for SSL/TLS compression.

v

[constants.SSL\_OP\_NO\_ENCRYPT\_THEN\_MAC](././crypto/~/constants.SSL_OP_NO_ENCRYPT_THEN_MAC "constants.SSL_OP_NO_ENCRYPT_THEN_MAC")

Instructs OpenSSL to disable encrypt-then-MAC.

v

[constants.SSL\_OP\_NO\_QUERY\_MTU](././crypto/~/constants.SSL_OP_NO_QUERY_MTU "constants.SSL_OP_NO_QUERY_MTU")

No documentation available

v

[constants.SSL\_OP\_NO\_RENEGOTIATION](././crypto/~/constants.SSL_OP_NO_RENEGOTIATION "constants.SSL_OP_NO_RENEGOTIATION")

Instructs OpenSSL to disable renegotiation.

v

[constants.SSL\_OP\_NO\_SESSION\_RESUMPTION\_ON\_RENEGOTIATION](././crypto/~/constants.SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION "constants.SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION")

Instructs OpenSSL to always start a new session when performing renegotiation.

v

[constants.SSL\_OP\_NO\_SSLv2](././crypto/~/constants.SSL_OP_NO_SSLv2 "constants.SSL_OP_NO_SSLv2")

Instructs OpenSSL to turn off SSL v2

v

[constants.SSL\_OP\_NO\_SSLv3](././crypto/~/constants.SSL_OP_NO_SSLv3 "constants.SSL_OP_NO_SSLv3")

Instructs OpenSSL to turn off SSL v3

v

[constants.SSL\_OP\_NO\_TICKET](././crypto/~/constants.SSL_OP_NO_TICKET "constants.SSL_OP_NO_TICKET")

Instructs OpenSSL to disable use of RFC4507bis tickets.

v

[constants.SSL\_OP\_NO\_TLSv1](././crypto/~/constants.SSL_OP_NO_TLSv1 "constants.SSL_OP_NO_TLSv1")

Instructs OpenSSL to turn off TLS v1

v

[constants.SSL\_OP\_NO\_TLSv1\_1](././crypto/~/constants.SSL_OP_NO_TLSv1_1 "constants.SSL_OP_NO_TLSv1_1")

Instructs OpenSSL to turn off TLS v1.1

v

[constants.SSL\_OP\_NO\_TLSv1\_2](././crypto/~/constants.SSL_OP_NO_TLSv1_2 "constants.SSL_OP_NO_TLSv1_2")

Instructs OpenSSL to turn off TLS v1.2

v

[constants.SSL\_OP\_NO\_TLSv1\_3](././crypto/~/constants.SSL_OP_NO_TLSv1_3 "constants.SSL_OP_NO_TLSv1_3")

Instructs OpenSSL to turn off TLS v1.3

v

[constants.SSL\_OP\_PRIORITIZE\_CHACHA](././crypto/~/constants.SSL_OP_PRIORITIZE_CHACHA "constants.SSL_OP_PRIORITIZE_CHACHA")

Instructs OpenSSL server to prioritize ChaCha20-Poly1305 when the client does. This option has no effect if `SSL_OP_CIPHER_SERVER_PREFERENCE` is not enabled.

v

[constants.SSL\_OP\_TLS\_ROLLBACK\_BUG](././crypto/~/constants.SSL_OP_TLS_ROLLBACK_BUG "constants.SSL_OP_TLS_ROLLBACK_BUG")

Instructs OpenSSL to disable version rollback attack detection.

f

[createCipheriv](././crypto/~/createCipheriv "createCipheriv")

Creates and returns a `Cipher` object, with the given `algorithm`, `key` and initialization vector (`iv`).

f

[createDecipheriv](././crypto/~/createDecipheriv "createDecipheriv")

Creates and returns a `Decipher` object that uses the given `algorithm`, `key` and initialization vector (`iv`).

f

[createDiffieHellman](././crypto/~/createDiffieHellman "createDiffieHellman")

Creates a `DiffieHellman` key exchange object using the supplied `prime` and an optional specific `generator`.

f

[createDiffieHellmanGroup](././crypto/~/createDiffieHellmanGroup "createDiffieHellmanGroup")

An alias for [getDiffieHellman](././crypto/~/getDiffieHellman)

f

[createECDH](././crypto/~/createECDH "createECDH")

Creates an Elliptic Curve Diffie-Hellman (`ECDH`) key exchange object using a predefined curve specified by the `curveName` string. Use [getCurves](././crypto/~/getCurves) to obtain a list of available curve names. On recent OpenSSL releases, `openssl ecparam -list_curves` will also display the name and description of each available elliptic curve.

f

[createHash](././crypto/~/createHash "createHash")

Creates and returns a `Hash` object that can be used to generate hash digests using the given `algorithm`. Optional `options` argument controls stream behavior. For XOF hash functions such as `'shake256'`, the `outputLength` option can be used to specify the desired output length in bytes.

f

[createHmac](././crypto/~/createHmac "createHmac")

Creates and returns an `Hmac` object that uses the given `algorithm` and `key`. Optional `options` argument controls stream behavior.

f

[createPrivateKey](././crypto/~/createPrivateKey "createPrivateKey")

Creates and returns a new key object containing a private key. If `key` is a string or `Buffer`, `format` is assumed to be `'pem'`; otherwise, `key` must be an object with the properties described above.

f

[createPublicKey](././crypto/~/createPublicKey "createPublicKey")

Creates and returns a new key object containing a public key. If `key` is a string or `Buffer`, `format` is assumed to be `'pem'`; if `key` is a `KeyObject` with type `'private'`, the public key is derived from the given private key; otherwise, `key` must be an object with the properties described above.

f

[createSecretKey](././crypto/~/createSecretKey "createSecretKey")

Creates and returns a new key object containing a secret key for symmetric encryption or `Hmac`.

f

[createSign](././crypto/~/createSign "createSign")

Creates and returns a `Sign` object that uses the given `algorithm`. Use [getHashes](././crypto/~/getHashes) to obtain the names of the available digest algorithms. Optional `options` argument controls the `stream.Writable` behavior.

f

[createVerify](././crypto/~/createVerify "createVerify")

Creates and returns a `Verify` object that uses the given algorithm. Use [getHashes](././crypto/~/getHashes) to obtain an array of names of the available signing algorithms. Optional `options` argument controls the `stream.Writable` behavior.

v

[crypto](././crypto/~/crypto "crypto")

No documentation available

c

[Decipher](././crypto/~/Decipher "Decipher")

Instances of the `Decipher` class are used to decrypt data. The class can be used in one of two ways:

-   [final](././crypto/~/Decipher#method_final_0)
-   [setAutoPadding](././crypto/~/Decipher#method_setautopadding_0)
-   [update](././crypto/~/Decipher#method_update_0)

I

[DecipherCCM](././crypto/~/DecipherCCM "DecipherCCM")

No documentation available

-   [setAAD](././crypto/~/DecipherCCM#method_setaad_0)
-   [setAuthTag](././crypto/~/DecipherCCM#method_setauthtag_0)

I

[DecipherChaCha20Poly1305](././crypto/~/DecipherChaCha20Poly1305 "DecipherChaCha20Poly1305")

No documentation available

-   [setAAD](././crypto/~/DecipherChaCha20Poly1305#method_setaad_0)
-   [setAuthTag](././crypto/~/DecipherChaCha20Poly1305#method_setauthtag_0)

I

[DecipherGCM](././crypto/~/DecipherGCM "DecipherGCM")

No documentation available

-   [setAAD](././crypto/~/DecipherGCM#method_setaad_0)
-   [setAuthTag](././crypto/~/DecipherGCM#method_setauthtag_0)

I

[DecipherOCB](././crypto/~/DecipherOCB "DecipherOCB")

No documentation available

-   [setAAD](././crypto/~/DecipherOCB#method_setaad_0)
-   [setAuthTag](././crypto/~/DecipherOCB#method_setauthtag_0)

c

[DiffieHellman](././crypto/~/DiffieHellman "DiffieHellman")

The `DiffieHellman` class is a utility for creating Diffie-Hellman key exchanges.

-   [computeSecret](././crypto/~/DiffieHellman#method_computesecret_0)
-   [generateKeys](././crypto/~/DiffieHellman#method_generatekeys_0)
-   [getGenerator](././crypto/~/DiffieHellman#method_getgenerator_0)
-   [getPrime](././crypto/~/DiffieHellman#method_getprime_0)
-   [getPrivateKey](././crypto/~/DiffieHellman#method_getprivatekey_0)
-   [getPublicKey](././crypto/~/DiffieHellman#method_getpublickey_0)
-   [setPrivateKey](././crypto/~/DiffieHellman#method_setprivatekey_0)
-   [setPublicKey](././crypto/~/DiffieHellman#method_setpublickey_0)
-   [verifyError](././crypto/~/DiffieHellman#property_verifyerror)

f

[diffieHellman](././crypto/~/diffieHellman "diffieHellman")

Computes the Diffie-Hellman secret based on a `privateKey` and a `publicKey`. Both keys must have the same `asymmetricKeyType`, which must be one of `'dh'` (for Diffie-Hellman), `'ec'` (for ECDH), `'x448'`, or `'x25519'` (for ECDH-ES).

T

v

[DiffieHellmanGroup](././crypto/~/DiffieHellmanGroup "DiffieHellmanGroup")

No documentation available

I

[DiffieHellmanGroupConstructor](././crypto/~/DiffieHellmanGroupConstructor "DiffieHellmanGroupConstructor")

No documentation available

-   [prototype](././crypto/~/DiffieHellmanGroupConstructor#property_prototype)

T

[DSAEncoding](././crypto/~/DSAEncoding "DSAEncoding")

No documentation available

I

[DSAKeyPairKeyObjectOptions](././crypto/~/DSAKeyPairKeyObjectOptions "DSAKeyPairKeyObjectOptions")

No documentation available

-   [divisorLength](././crypto/~/DSAKeyPairKeyObjectOptions#property_divisorlength)
-   [modulusLength](././crypto/~/DSAKeyPairKeyObjectOptions#property_moduluslength)

I

[DSAKeyPairOptions](././crypto/~/DSAKeyPairOptions "DSAKeyPairOptions")

No documentation available

-   [divisorLength](././crypto/~/DSAKeyPairOptions#property_divisorlength)
-   [modulusLength](././crypto/~/DSAKeyPairOptions#property_moduluslength)
-   [privateKeyEncoding](././crypto/~/DSAKeyPairOptions#property_privatekeyencoding)
-   [publicKeyEncoding](././crypto/~/DSAKeyPairOptions#property_publickeyencoding)

c

[ECDH](././crypto/~/ECDH "ECDH")

No documentation available

-   [computeSecret](././crypto/~/ECDH#method_computesecret_0)
-   [convertKey](././crypto/~/ECDH#method_convertkey_0)
-   [generateKeys](././crypto/~/ECDH#method_generatekeys_0)
-   [getPrivateKey](././crypto/~/ECDH#method_getprivatekey_0)
-   [getPublicKey](././crypto/~/ECDH#method_getpublickey_0)
-   [setPrivateKey](././crypto/~/ECDH#method_setprivatekey_0)

T

[ECDHKeyFormat](././crypto/~/ECDHKeyFormat "ECDHKeyFormat")

No documentation available

I

[ECKeyPairKeyObjectOptions](././crypto/~/ECKeyPairKeyObjectOptions "ECKeyPairKeyObjectOptions")

No documentation available

-   [namedCurve](././crypto/~/ECKeyPairKeyObjectOptions#property_namedcurve)
-   [paramEncoding](././crypto/~/ECKeyPairKeyObjectOptions#property_paramencoding)

I

[ECKeyPairOptions](././crypto/~/ECKeyPairOptions "ECKeyPairOptions")

No documentation available

-   [privateKeyEncoding](././crypto/~/ECKeyPairOptions#property_privatekeyencoding)
-   [publicKeyEncoding](././crypto/~/ECKeyPairOptions#property_publickeyencoding)

I

[ED25519KeyPairKeyObjectOptions](././crypto/~/ED25519KeyPairKeyObjectOptions "ED25519KeyPairKeyObjectOptions")

No documentation available

I

[ED25519KeyPairOptions](././crypto/~/ED25519KeyPairOptions "ED25519KeyPairOptions")

No documentation available

-   [privateKeyEncoding](././crypto/~/ED25519KeyPairOptions#property_privatekeyencoding)
-   [publicKeyEncoding](././crypto/~/ED25519KeyPairOptions#property_publickeyencoding)

I

[ED448KeyPairKeyObjectOptions](././crypto/~/ED448KeyPairKeyObjectOptions "ED448KeyPairKeyObjectOptions")

No documentation available

I

[ED448KeyPairOptions](././crypto/~/ED448KeyPairOptions "ED448KeyPairOptions")

No documentation available

-   [privateKeyEncoding](././crypto/~/ED448KeyPairOptions#property_privatekeyencoding)
-   [publicKeyEncoding](././crypto/~/ED448KeyPairOptions#property_publickeyencoding)

T

[Encoding](././crypto/~/Encoding "Encoding")

No documentation available

f

[generateKey](././crypto/~/generateKey "generateKey")

Asynchronously generates a new random secret key of the given `length`. The `type` will determine which validations will be performed on the `length`.

f

[generateKeyPair](././crypto/~/generateKeyPair "generateKeyPair")

No documentation available

f

[generateKeyPairSync](././crypto/~/generateKeyPairSync "generateKeyPairSync")

Generates a new asymmetric key pair of the given `type`. RSA, RSA-PSS, DSA, EC, Ed25519, Ed448, X25519, X448, and DH are currently supported.

f

[generateKeySync](././crypto/~/generateKeySync "generateKeySync")

Synchronously generates a new random secret key of the given `length`. The `type` will determine which validations will be performed on the `length`.

f

[generatePrime](././crypto/~/generatePrime "generatePrime")

No documentation available

I

[GeneratePrimeOptions](././crypto/~/GeneratePrimeOptions "GeneratePrimeOptions")

No documentation available

-   [add](././crypto/~/GeneratePrimeOptions#property_add)
-   [bigint](././crypto/~/GeneratePrimeOptions#property_bigint)
-   [rem](././crypto/~/GeneratePrimeOptions#property_rem)
-   [safe](././crypto/~/GeneratePrimeOptions#property_safe)

I

[GeneratePrimeOptionsArrayBuffer](././crypto/~/GeneratePrimeOptionsArrayBuffer "GeneratePrimeOptionsArrayBuffer")

No documentation available

-   [bigint](././crypto/~/GeneratePrimeOptionsArrayBuffer#property_bigint)

I

[GeneratePrimeOptionsBigInt](././crypto/~/GeneratePrimeOptionsBigInt "GeneratePrimeOptionsBigInt")

No documentation available

-   [bigint](././crypto/~/GeneratePrimeOptionsBigInt#property_bigint)

f

[generatePrimeSync](././crypto/~/generatePrimeSync "generatePrimeSync")

Generates a pseudorandom prime of `size` bits.

f

[getCipherInfo](././crypto/~/getCipherInfo "getCipherInfo")

Returns information about a given cipher.

f

[getCiphers](././crypto/~/getCiphers "getCiphers")

No documentation available

f

[getCurves](././crypto/~/getCurves "getCurves")

No documentation available

f

[getDiffieHellman](././crypto/~/getDiffieHellman "getDiffieHellman")

Creates a predefined `DiffieHellmanGroup` key exchange object. The supported groups are listed in the documentation for `DiffieHellmanGroup`.

f

[getFips](././crypto/~/getFips "getFips")

No documentation available

f

[getHashes](././crypto/~/getHashes "getHashes")

No documentation available

f

[getRandomValues](././crypto/~/getRandomValues "getRandomValues")

A convenient alias for webcrypto.getRandomValues. This implementation is not compliant with the Web Crypto spec, to write web-compatible code use webcrypto.getRandomValues instead.

c

[Hash](././crypto/~/Hash "Hash")

The `Hash` class is a utility for creating hash digests of data. It can be used in one of two ways:

-   [copy](././crypto/~/Hash#method_copy_0)
-   [digest](././crypto/~/Hash#method_digest_0)
-   [update](././crypto/~/Hash#method_update_0)

f

[hash](././crypto/~/hash "hash")

A utility for creating one-shot hash digests of data. It can be faster than the object-based `crypto.createHash()` when hashing a smaller amount of data (<= 5MB) that's readily available. If the data can be big or if it is streamed, it's still recommended to use `crypto.createHash()` instead. The `algorithm` is dependent on the available algorithms supported by the version of OpenSSL on the platform. Examples are `'sha256'`, `'sha512'`, etc. On recent releases of OpenSSL, `openssl list -digest-algorithms` will display the available digest algorithms.

I

[HashOptions](././crypto/~/HashOptions "HashOptions")

No documentation available

-   [outputLength](././crypto/~/HashOptions#property_outputlength)

f

[hkdf](././crypto/~/hkdf "hkdf")

HKDF is a simple key derivation function defined in RFC 5869. The given `ikm`, `salt` and `info` are used with the `digest` to derive a key of `keylen` bytes.

f

[hkdfSync](././crypto/~/hkdfSync "hkdfSync")

Provides a synchronous HKDF key derivation function as defined in RFC 5869. The given `ikm`, `salt` and `info` are used with the `digest` to derive a key of `keylen` bytes.

I

[JsonWebKey](././crypto/~/JsonWebKey "JsonWebKey")

No documentation available

-   [crv](././crypto/~/JsonWebKey#property_crv)
-   [d](././crypto/~/JsonWebKey#property_d)
-   [dp](././crypto/~/JsonWebKey#property_dp)
-   [dq](././crypto/~/JsonWebKey#property_dq)
-   [e](././crypto/~/JsonWebKey#property_e)
-   [k](././crypto/~/JsonWebKey#property_k)
-   [kty](././crypto/~/JsonWebKey#property_kty)
-   [n](././crypto/~/JsonWebKey#property_n)
-   [p](././crypto/~/JsonWebKey#property_p)
-   [q](././crypto/~/JsonWebKey#property_q)
-   [qi](././crypto/~/JsonWebKey#property_qi)
-   [x](././crypto/~/JsonWebKey#property_x)
-   [y](././crypto/~/JsonWebKey#property_y)

I

[JsonWebKeyInput](././crypto/~/JsonWebKeyInput "JsonWebKeyInput")

No documentation available

-   [format](././crypto/~/JsonWebKeyInput#property_format)
-   [key](././crypto/~/JsonWebKeyInput#property_key)

I

[JwkKeyExportOptions](././crypto/~/JwkKeyExportOptions "JwkKeyExportOptions")

No documentation available

-   [format](././crypto/~/JwkKeyExportOptions#property_format)

I

[KeyExportOptions](././crypto/~/KeyExportOptions "KeyExportOptions")

No documentation available

-   [cipher](././crypto/~/KeyExportOptions#property_cipher)
-   [format](././crypto/~/KeyExportOptions#property_format)
-   [passphrase](././crypto/~/KeyExportOptions#property_passphrase)
-   [type](././crypto/~/KeyExportOptions#property_type)

T

[KeyFormat](././crypto/~/KeyFormat "KeyFormat")

No documentation available

T

[KeyLike](././crypto/~/KeyLike "KeyLike")

No documentation available

c

[KeyObject](././crypto/~/KeyObject "KeyObject")

No documentation available

-   [asymmetricKeyDetails](././crypto/~/KeyObject#property_asymmetrickeydetails)
-   [asymmetricKeyType](././crypto/~/KeyObject#property_asymmetrickeytype)
-   [equals](././crypto/~/KeyObject#method_equals_0)
-   [export](././crypto/~/KeyObject#method_export_0)
-   [from](././crypto/~/KeyObject#method_from_0)
-   [symmetricKeySize](././crypto/~/KeyObject#property_symmetrickeysize)
-   [toCryptoKey](././crypto/~/KeyObject#method_tocryptokey_0)
-   [type](././crypto/~/KeyObject#property_type)

T

[KeyObjectType](././crypto/~/KeyObjectType "KeyObjectType")

No documentation available

I

[KeyPairKeyObjectResult](././crypto/~/KeyPairKeyObjectResult "KeyPairKeyObjectResult")

No documentation available

-   [privateKey](././crypto/~/KeyPairKeyObjectResult#property_privatekey)
-   [publicKey](././crypto/~/KeyPairKeyObjectResult#property_publickey)

I

[KeyPairSyncResult](././crypto/~/KeyPairSyncResult "KeyPairSyncResult")

No documentation available

-   [privateKey](././crypto/~/KeyPairSyncResult#property_privatekey)
-   [publicKey](././crypto/~/KeyPairSyncResult#property_publickey)

T

[KeyType](././crypto/~/KeyType "KeyType")

No documentation available

T

[LargeNumberLike](././crypto/~/LargeNumberLike "LargeNumberLike")

No documentation available

T

[LegacyCharacterEncoding](././crypto/~/LegacyCharacterEncoding "LegacyCharacterEncoding")

No documentation available

f

[pbkdf2](././crypto/~/pbkdf2 "pbkdf2")

Provides an asynchronous Password-Based Key Derivation Function 2 (PBKDF2) implementation. A selected HMAC digest algorithm specified by `digest` is applied to derive a key of the requested byte length (`keylen`) from the `password`, `salt` and `iterations`.

f

[pbkdf2Sync](././crypto/~/pbkdf2Sync "pbkdf2Sync")

Provides a synchronous Password-Based Key Derivation Function 2 (PBKDF2) implementation. A selected HMAC digest algorithm specified by `digest` is applied to derive a key of the requested byte length (`keylen`) from the `password`, `salt` and `iterations`.

f

[privateDecrypt](././crypto/~/privateDecrypt "privateDecrypt")

Decrypts `buffer` with `privateKey`. `buffer` was previously encrypted using the corresponding public key, for example using [publicEncrypt](././crypto/~/publicEncrypt).

f

[privateEncrypt](././crypto/~/privateEncrypt "privateEncrypt")

Encrypts `buffer` with `privateKey`. The returned data can be decrypted using the corresponding public key, for example using [publicDecrypt](././crypto/~/publicDecrypt).

I

[PrivateKeyInput](././crypto/~/PrivateKeyInput "PrivateKeyInput")

No documentation available

-   [encoding](././crypto/~/PrivateKeyInput#property_encoding)
-   [format](././crypto/~/PrivateKeyInput#property_format)
-   [key](././crypto/~/PrivateKeyInput#property_key)
-   [passphrase](././crypto/~/PrivateKeyInput#property_passphrase)
-   [type](././crypto/~/PrivateKeyInput#property_type)

f

[pseudoRandomBytes](././crypto/~/pseudoRandomBytes "pseudoRandomBytes")

No documentation available

f

[publicDecrypt](././crypto/~/publicDecrypt "publicDecrypt")

No documentation available

f

[publicEncrypt](././crypto/~/publicEncrypt "publicEncrypt")

Encrypts the content of `buffer` with `key` and returns a new `Buffer` with encrypted content. The returned data can be decrypted using the corresponding private key, for example using [privateDecrypt](././crypto/~/privateDecrypt).

I

[PublicKeyInput](././crypto/~/PublicKeyInput "PublicKeyInput")

No documentation available

-   [encoding](././crypto/~/PublicKeyInput#property_encoding)
-   [format](././crypto/~/PublicKeyInput#property_format)
-   [key](././crypto/~/PublicKeyInput#property_key)
-   [type](././crypto/~/PublicKeyInput#property_type)

f

[randomBytes](././crypto/~/randomBytes "randomBytes")

Generates cryptographically strong pseudorandom data. The `size` argument is a number indicating the number of bytes to generate.

f

[randomFill](././crypto/~/randomFill "randomFill")

This function is similar to [randomBytes](././crypto/~/randomBytes) but requires the first argument to be a `Buffer` that will be filled. It also requires that a callback is passed in.

f

[randomFillSync](././crypto/~/randomFillSync "randomFillSync")

Synchronous version of [randomFill](././crypto/~/randomFill).

f

[randomInt](././crypto/~/randomInt "randomInt")

Return a random integer `n` such that `min <= n < max`. This implementation avoids [modulo bias](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Modulo_bias).

f

[randomUUID](././crypto/~/randomUUID "randomUUID")

Generates a random [RFC 4122](https://www.rfc-editor.org/rfc/rfc4122.txt) version 4 UUID. The UUID is generated using a cryptographic pseudorandom number generator.

I

[RandomUUIDOptions](././crypto/~/RandomUUIDOptions "RandomUUIDOptions")

No documentation available

-   [disableEntropyCache](././crypto/~/RandomUUIDOptions#property_disableentropycache)

I

[RSAKeyPairKeyObjectOptions](././crypto/~/RSAKeyPairKeyObjectOptions "RSAKeyPairKeyObjectOptions")

No documentation available

-   [modulusLength](././crypto/~/RSAKeyPairKeyObjectOptions#property_moduluslength)
-   [publicExponent](././crypto/~/RSAKeyPairKeyObjectOptions#property_publicexponent)

I

[RSAKeyPairOptions](././crypto/~/RSAKeyPairOptions "RSAKeyPairOptions")

No documentation available

-   [modulusLength](././crypto/~/RSAKeyPairOptions#property_moduluslength)
-   [privateKeyEncoding](././crypto/~/RSAKeyPairOptions#property_privatekeyencoding)
-   [publicExponent](././crypto/~/RSAKeyPairOptions#property_publicexponent)
-   [publicKeyEncoding](././crypto/~/RSAKeyPairOptions#property_publickeyencoding)

I

[RsaPrivateKey](././crypto/~/RsaPrivateKey "RsaPrivateKey")

No documentation available

-   [key](././crypto/~/RsaPrivateKey#property_key)
-   [oaepHash](././crypto/~/RsaPrivateKey#property_oaephash)
-   [oaepLabel](././crypto/~/RsaPrivateKey#property_oaeplabel)
-   [padding](././crypto/~/RsaPrivateKey#property_padding)
-   [passphrase](././crypto/~/RsaPrivateKey#property_passphrase)

I

[RSAPSSKeyPairKeyObjectOptions](././crypto/~/RSAPSSKeyPairKeyObjectOptions "RSAPSSKeyPairKeyObjectOptions")

No documentation available

-   [hashAlgorithm](././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_hashalgorithm)
-   [mgf1HashAlgorithm](././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_mgf1hashalgorithm)
-   [modulusLength](././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_moduluslength)
-   [publicExponent](././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_publicexponent)
-   [saltLength](././crypto/~/RSAPSSKeyPairKeyObjectOptions#property_saltlength)

I

[RSAPSSKeyPairOptions](././crypto/~/RSAPSSKeyPairOptions "RSAPSSKeyPairOptions")

No documentation available

-   [hashAlgorithm](././crypto/~/RSAPSSKeyPairOptions#property_hashalgorithm)
-   [mgf1HashAlgorithm](././crypto/~/RSAPSSKeyPairOptions#property_mgf1hashalgorithm)
-   [modulusLength](././crypto/~/RSAPSSKeyPairOptions#property_moduluslength)
-   [privateKeyEncoding](././crypto/~/RSAPSSKeyPairOptions#property_privatekeyencoding)
-   [publicExponent](././crypto/~/RSAPSSKeyPairOptions#property_publicexponent)
-   [publicKeyEncoding](././crypto/~/RSAPSSKeyPairOptions#property_publickeyencoding)
-   [saltLength](././crypto/~/RSAPSSKeyPairOptions#property_saltlength)

I

[RsaPublicKey](././crypto/~/RsaPublicKey "RsaPublicKey")

No documentation available

-   [key](././crypto/~/RsaPublicKey#property_key)
-   [padding](././crypto/~/RsaPublicKey#property_padding)

f

[scrypt](././crypto/~/scrypt "scrypt")

Provides an asynchronous [scrypt](https://en.wikipedia.org/wiki/Scrypt) implementation. Scrypt is a password-based key derivation function that is designed to be expensive computationally and memory-wise in order to make brute-force attacks unrewarding.

I

[ScryptOptions](././crypto/~/ScryptOptions "ScryptOptions")

No documentation available

-   [N](././crypto/~/ScryptOptions#property_n)
-   [blockSize](././crypto/~/ScryptOptions#property_blocksize)
-   [cost](././crypto/~/ScryptOptions#property_cost)
-   [maxmem](././crypto/~/ScryptOptions#property_maxmem)
-   [p](././crypto/~/ScryptOptions#property_p)
-   [parallelization](././crypto/~/ScryptOptions#property_parallelization)
-   [r](././crypto/~/ScryptOptions#property_r)

f

[scryptSync](././crypto/~/scryptSync "scryptSync")

Provides a synchronous [scrypt](https://en.wikipedia.org/wiki/Scrypt) implementation. Scrypt is a password-based key derivation function that is designed to be expensive computationally and memory-wise in order to make brute-force attacks unrewarding.

I

[SecureHeapUsage](././crypto/~/SecureHeapUsage "SecureHeapUsage")

No documentation available

-   [min](././crypto/~/SecureHeapUsage#property_min)
-   [total](././crypto/~/SecureHeapUsage#property_total)
-   [used](././crypto/~/SecureHeapUsage#property_used)
-   [utilization](././crypto/~/SecureHeapUsage#property_utilization)

f

[secureHeapUsed](././crypto/~/secureHeapUsed "secureHeapUsed")

No documentation available

f

[setEngine](././crypto/~/setEngine "setEngine")

No documentation available

f

[setFips](././crypto/~/setFips "setFips")

Enables the FIPS compliant crypto provider in a FIPS-enabled Node.js build. Throws an error if FIPS mode is not available.

c

[Sign](././crypto/~/Sign "Sign")

No documentation available

-   [sign](././crypto/~/Sign#method_sign_0)
-   [update](././crypto/~/Sign#method_update_0)

f

[sign](././crypto/~/sign "sign")

Calculates and returns the signature for `data` using the given private key and algorithm. If `algorithm` is `null` or `undefined`, then the algorithm is dependent upon the key type (especially Ed25519 and Ed448).

I

[SigningOptions](././crypto/~/SigningOptions "SigningOptions")

No documentation available

-   [dsaEncoding](././crypto/~/SigningOptions#property_dsaencoding)
-   [padding](././crypto/~/SigningOptions#property_padding)
-   [saltLength](././crypto/~/SigningOptions#property_saltlength)

I

[SignJsonWebKeyInput](././crypto/~/SignJsonWebKeyInput "SignJsonWebKeyInput")

No documentation available

I

[SignKeyObjectInput](././crypto/~/SignKeyObjectInput "SignKeyObjectInput")

No documentation available

-   [key](././crypto/~/SignKeyObjectInput#property_key)

I

[SignPrivateKeyInput](././crypto/~/SignPrivateKeyInput "SignPrivateKeyInput")

No documentation available

v

[subtle](././crypto/~/subtle "subtle")

A convenient alias for `crypto.webcrypto.subtle`.

f

[timingSafeEqual](././crypto/~/timingSafeEqual "timingSafeEqual")

This function compares the underlying bytes that represent the given `ArrayBuffer`, `TypedArray`, or `DataView` instances using a constant-time algorithm.

T

[UUID](././crypto/~/UUID "UUID")

No documentation available

c

[Verify](././crypto/~/Verify "Verify")

The `Verify` class is a utility for verifying signatures. It can be used in one of two ways:

-   [update](././crypto/~/Verify#method_update_0)
-   [verify](././crypto/~/Verify#method_verify_0)

f

[verify](././crypto/~/verify "verify")

Verifies the given signature for `data` using the given key and algorithm. If `algorithm` is `null` or `undefined`, then the algorithm is dependent upon the key type (especially Ed25519 and Ed448).

I

[VerifyJsonWebKeyInput](././crypto/~/VerifyJsonWebKeyInput "VerifyJsonWebKeyInput")

No documentation available

I

[VerifyKeyObjectInput](././crypto/~/VerifyKeyObjectInput "VerifyKeyObjectInput")

No documentation available

-   [key](././crypto/~/VerifyKeyObjectInput#property_key)

I

[VerifyPublicKeyInput](././crypto/~/VerifyPublicKeyInput "VerifyPublicKeyInput")

No documentation available

N

v

[webcrypto](././crypto/~/webcrypto "webcrypto")

No documentation available

I

[webcrypto.AesCbcParams](././crypto/~/webcrypto.AesCbcParams "webcrypto.AesCbcParams")

No documentation available

-   [iv](././crypto/~/webcrypto.AesCbcParams#property_iv)

I

[webcrypto.AesCtrParams](././crypto/~/webcrypto.AesCtrParams "webcrypto.AesCtrParams")

No documentation available

-   [counter](././crypto/~/webcrypto.AesCtrParams#property_counter)
-   [length](././crypto/~/webcrypto.AesCtrParams#property_length)

I

[webcrypto.AesDerivedKeyParams](././crypto/~/webcrypto.AesDerivedKeyParams "webcrypto.AesDerivedKeyParams")

No documentation available

-   [length](././crypto/~/webcrypto.AesDerivedKeyParams#property_length)

I

[webcrypto.AesGcmParams](././crypto/~/webcrypto.AesGcmParams "webcrypto.AesGcmParams")

No documentation available

-   [additionalData](././crypto/~/webcrypto.AesGcmParams#property_additionaldata)
-   [iv](././crypto/~/webcrypto.AesGcmParams#property_iv)
-   [tagLength](././crypto/~/webcrypto.AesGcmParams#property_taglength)

I

[webcrypto.AesKeyAlgorithm](././crypto/~/webcrypto.AesKeyAlgorithm "webcrypto.AesKeyAlgorithm")

No documentation available

-   [length](././crypto/~/webcrypto.AesKeyAlgorithm#property_length)

I

[webcrypto.AesKeyGenParams](././crypto/~/webcrypto.AesKeyGenParams "webcrypto.AesKeyGenParams")

No documentation available

-   [length](././crypto/~/webcrypto.AesKeyGenParams#property_length)

I

[webcrypto.Algorithm](././crypto/~/webcrypto.Algorithm "webcrypto.Algorithm")

No documentation available

-   [name](././crypto/~/webcrypto.Algorithm#property_name)

T

[webcrypto.AlgorithmIdentifier](././crypto/~/webcrypto.AlgorithmIdentifier "webcrypto.AlgorithmIdentifier")

No documentation available

T

[webcrypto.BigInteger](././crypto/~/webcrypto.BigInteger "webcrypto.BigInteger")

No documentation available

T

[webcrypto.BufferSource](././crypto/~/webcrypto.BufferSource "webcrypto.BufferSource")

No documentation available

I

[webcrypto.Crypto](././crypto/~/webcrypto.Crypto "webcrypto.Crypto")

Importing the `webcrypto` object (`import { webcrypto } from 'node:crypto'`) gives an instance of the `Crypto` class. `Crypto` is a singleton that provides access to the remainder of the crypto API.

-   [CryptoKey](././crypto/~/webcrypto.Crypto#property_cryptokey)
-   [getRandomValues](././crypto/~/webcrypto.Crypto#method_getrandomvalues_0)
-   [randomUUID](././crypto/~/webcrypto.Crypto#method_randomuuid_0)
-   [subtle](././crypto/~/webcrypto.Crypto#property_subtle)

I

[webcrypto.CryptoKey](././crypto/~/webcrypto.CryptoKey "webcrypto.CryptoKey")

No documentation available

-   [algorithm](././crypto/~/webcrypto.CryptoKey#property_algorithm)
-   [extractable](././crypto/~/webcrypto.CryptoKey#property_extractable)
-   [type](././crypto/~/webcrypto.CryptoKey#property_type)
-   [usages](././crypto/~/webcrypto.CryptoKey#property_usages)

I

[webcrypto.CryptoKeyConstructor](././crypto/~/webcrypto.CryptoKeyConstructor "webcrypto.CryptoKeyConstructor")

No documentation available

-   [length](././crypto/~/webcrypto.CryptoKeyConstructor#property_length)
-   [name](././crypto/~/webcrypto.CryptoKeyConstructor#property_name)
-   [prototype](././crypto/~/webcrypto.CryptoKeyConstructor#property_prototype)

I

[webcrypto.CryptoKeyPair](././crypto/~/webcrypto.CryptoKeyPair "webcrypto.CryptoKeyPair")

The `CryptoKeyPair` is a simple dictionary object with `publicKey` and `privateKey` properties, representing an asymmetric key pair.

-   [privateKey](././crypto/~/webcrypto.CryptoKeyPair#property_privatekey)
-   [publicKey](././crypto/~/webcrypto.CryptoKeyPair#property_publickey)

I

[webcrypto.EcdhKeyDeriveParams](././crypto/~/webcrypto.EcdhKeyDeriveParams "webcrypto.EcdhKeyDeriveParams")

No documentation available

-   [public](././crypto/~/webcrypto.EcdhKeyDeriveParams#property_public)

I

[webcrypto.EcdsaParams](././crypto/~/webcrypto.EcdsaParams "webcrypto.EcdsaParams")

No documentation available

-   [hash](././crypto/~/webcrypto.EcdsaParams#property_hash)

I

[webcrypto.EcKeyAlgorithm](././crypto/~/webcrypto.EcKeyAlgorithm "webcrypto.EcKeyAlgorithm")

No documentation available

-   [namedCurve](././crypto/~/webcrypto.EcKeyAlgorithm#property_namedcurve)

I

[webcrypto.EcKeyGenParams](././crypto/~/webcrypto.EcKeyGenParams "webcrypto.EcKeyGenParams")

No documentation available

-   [namedCurve](././crypto/~/webcrypto.EcKeyGenParams#property_namedcurve)

I

[webcrypto.EcKeyImportParams](././crypto/~/webcrypto.EcKeyImportParams "webcrypto.EcKeyImportParams")

No documentation available

-   [namedCurve](././crypto/~/webcrypto.EcKeyImportParams#property_namedcurve)

I

[webcrypto.Ed448Params](././crypto/~/webcrypto.Ed448Params "webcrypto.Ed448Params")

No documentation available

-   [context](././crypto/~/webcrypto.Ed448Params#property_context)

T

[webcrypto.HashAlgorithmIdentifier](././crypto/~/webcrypto.HashAlgorithmIdentifier "webcrypto.HashAlgorithmIdentifier")

No documentation available

I

[webcrypto.HkdfParams](././crypto/~/webcrypto.HkdfParams "webcrypto.HkdfParams")

No documentation available

-   [hash](././crypto/~/webcrypto.HkdfParams#property_hash)
-   [info](././crypto/~/webcrypto.HkdfParams#property_info)
-   [salt](././crypto/~/webcrypto.HkdfParams#property_salt)

I

[webcrypto.HmacImportParams](././crypto/~/webcrypto.HmacImportParams "webcrypto.HmacImportParams")

No documentation available

-   [hash](././crypto/~/webcrypto.HmacImportParams#property_hash)
-   [length](././crypto/~/webcrypto.HmacImportParams#property_length)

I

[webcrypto.HmacKeyAlgorithm](././crypto/~/webcrypto.HmacKeyAlgorithm "webcrypto.HmacKeyAlgorithm")

No documentation available

-   [hash](././crypto/~/webcrypto.HmacKeyAlgorithm#property_hash)
-   [length](././crypto/~/webcrypto.HmacKeyAlgorithm#property_length)

I

[webcrypto.HmacKeyGenParams](././crypto/~/webcrypto.HmacKeyGenParams "webcrypto.HmacKeyGenParams")

No documentation available

-   [hash](././crypto/~/webcrypto.HmacKeyGenParams#property_hash)
-   [length](././crypto/~/webcrypto.HmacKeyGenParams#property_length)

I

[webcrypto.JsonWebKey](././crypto/~/webcrypto.JsonWebKey "webcrypto.JsonWebKey")

No documentation available

-   [alg](././crypto/~/webcrypto.JsonWebKey#property_alg)
-   [crv](././crypto/~/webcrypto.JsonWebKey#property_crv)
-   [d](././crypto/~/webcrypto.JsonWebKey#property_d)
-   [dp](././crypto/~/webcrypto.JsonWebKey#property_dp)
-   [dq](././crypto/~/webcrypto.JsonWebKey#property_dq)
-   [e](././crypto/~/webcrypto.JsonWebKey#property_e)
-   [ext](././crypto/~/webcrypto.JsonWebKey#property_ext)
-   [k](././crypto/~/webcrypto.JsonWebKey#property_k)
-   [key\_ops](././crypto/~/webcrypto.JsonWebKey#property_key_ops)
-   [kty](././crypto/~/webcrypto.JsonWebKey#property_kty)
-   [n](././crypto/~/webcrypto.JsonWebKey#property_n)
-   [oth](././crypto/~/webcrypto.JsonWebKey#property_oth)
-   [p](././crypto/~/webcrypto.JsonWebKey#property_p)
-   [q](././crypto/~/webcrypto.JsonWebKey#property_q)
-   [qi](././crypto/~/webcrypto.JsonWebKey#property_qi)
-   [use](././crypto/~/webcrypto.JsonWebKey#property_use)
-   [x](././crypto/~/webcrypto.JsonWebKey#property_x)
-   [y](././crypto/~/webcrypto.JsonWebKey#property_y)

I

[webcrypto.KeyAlgorithm](././crypto/~/webcrypto.KeyAlgorithm "webcrypto.KeyAlgorithm")

No documentation available

-   [name](././crypto/~/webcrypto.KeyAlgorithm#property_name)

T

[webcrypto.KeyFormat](././crypto/~/webcrypto.KeyFormat "webcrypto.KeyFormat")

No documentation available

T

[webcrypto.KeyType](././crypto/~/webcrypto.KeyType "webcrypto.KeyType")

No documentation available

T

[webcrypto.KeyUsage](././crypto/~/webcrypto.KeyUsage "webcrypto.KeyUsage")

No documentation available

T

[webcrypto.NamedCurve](././crypto/~/webcrypto.NamedCurve "webcrypto.NamedCurve")

No documentation available

I

[webcrypto.Pbkdf2Params](././crypto/~/webcrypto.Pbkdf2Params "webcrypto.Pbkdf2Params")

No documentation available

-   [hash](././crypto/~/webcrypto.Pbkdf2Params#property_hash)
-   [iterations](././crypto/~/webcrypto.Pbkdf2Params#property_iterations)
-   [salt](././crypto/~/webcrypto.Pbkdf2Params#property_salt)

I

[webcrypto.RsaHashedImportParams](././crypto/~/webcrypto.RsaHashedImportParams "webcrypto.RsaHashedImportParams")

No documentation available

-   [hash](././crypto/~/webcrypto.RsaHashedImportParams#property_hash)

I

[webcrypto.RsaHashedKeyAlgorithm](././crypto/~/webcrypto.RsaHashedKeyAlgorithm "webcrypto.RsaHashedKeyAlgorithm")

No documentation available

-   [hash](././crypto/~/webcrypto.RsaHashedKeyAlgorithm#property_hash)

I

[webcrypto.RsaHashedKeyGenParams](././crypto/~/webcrypto.RsaHashedKeyGenParams "webcrypto.RsaHashedKeyGenParams")

No documentation available

-   [hash](././crypto/~/webcrypto.RsaHashedKeyGenParams#property_hash)

I

[webcrypto.RsaKeyAlgorithm](././crypto/~/webcrypto.RsaKeyAlgorithm "webcrypto.RsaKeyAlgorithm")

No documentation available

-   [modulusLength](././crypto/~/webcrypto.RsaKeyAlgorithm#property_moduluslength)
-   [publicExponent](././crypto/~/webcrypto.RsaKeyAlgorithm#property_publicexponent)

I

[webcrypto.RsaKeyGenParams](././crypto/~/webcrypto.RsaKeyGenParams "webcrypto.RsaKeyGenParams")

No documentation available

-   [modulusLength](././crypto/~/webcrypto.RsaKeyGenParams#property_moduluslength)
-   [publicExponent](././crypto/~/webcrypto.RsaKeyGenParams#property_publicexponent)

I

[webcrypto.RsaOaepParams](././crypto/~/webcrypto.RsaOaepParams "webcrypto.RsaOaepParams")

No documentation available

-   [label](././crypto/~/webcrypto.RsaOaepParams#property_label)

I

[webcrypto.RsaOtherPrimesInfo](././crypto/~/webcrypto.RsaOtherPrimesInfo "webcrypto.RsaOtherPrimesInfo")

No documentation available

-   [d](././crypto/~/webcrypto.RsaOtherPrimesInfo#property_d)
-   [r](././crypto/~/webcrypto.RsaOtherPrimesInfo#property_r)
-   [t](././crypto/~/webcrypto.RsaOtherPrimesInfo#property_t)

I

[webcrypto.RsaPssParams](././crypto/~/webcrypto.RsaPssParams "webcrypto.RsaPssParams")

No documentation available

-   [saltLength](././crypto/~/webcrypto.RsaPssParams#property_saltlength)

I

[webcrypto.SubtleCrypto](././crypto/~/webcrypto.SubtleCrypto "webcrypto.SubtleCrypto")

No documentation available

-   [decrypt](././crypto/~/webcrypto.SubtleCrypto#method_decrypt_0)
-   [deriveBits](././crypto/~/webcrypto.SubtleCrypto#method_derivebits_0)
-   [deriveKey](././crypto/~/webcrypto.SubtleCrypto#method_derivekey_0)
-   [digest](././crypto/~/webcrypto.SubtleCrypto#method_digest_0)
-   [encrypt](././crypto/~/webcrypto.SubtleCrypto#method_encrypt_0)
-   [exportKey](././crypto/~/webcrypto.SubtleCrypto#method_exportkey_0)
-   [generateKey](././crypto/~/webcrypto.SubtleCrypto#method_generatekey_0)
-   [importKey](././crypto/~/webcrypto.SubtleCrypto#method_importkey_0)
-   [sign](././crypto/~/webcrypto.SubtleCrypto#method_sign_0)
-   [unwrapKey](././crypto/~/webcrypto.SubtleCrypto#method_unwrapkey_0)
-   [verify](././crypto/~/webcrypto.SubtleCrypto#method_verify_0)
-   [wrapKey](././crypto/~/webcrypto.SubtleCrypto#method_wrapkey_0)

I

[X25519KeyPairKeyObjectOptions](././crypto/~/X25519KeyPairKeyObjectOptions "X25519KeyPairKeyObjectOptions")

No documentation available

I

[X25519KeyPairOptions](././crypto/~/X25519KeyPairOptions "X25519KeyPairOptions")

No documentation available

-   [privateKeyEncoding](././crypto/~/X25519KeyPairOptions#property_privatekeyencoding)
-   [publicKeyEncoding](././crypto/~/X25519KeyPairOptions#property_publickeyencoding)

I

[X448KeyPairKeyObjectOptions](././crypto/~/X448KeyPairKeyObjectOptions "X448KeyPairKeyObjectOptions")

No documentation available

I

[X448KeyPairOptions](././crypto/~/X448KeyPairOptions "X448KeyPairOptions")

No documentation available

-   [privateKeyEncoding](././crypto/~/X448KeyPairOptions#property_privatekeyencoding)
-   [publicKeyEncoding](././crypto/~/X448KeyPairOptions#property_publickeyencoding)

c

[X509Certificate](././crypto/~/X509Certificate "X509Certificate")

Encapsulates an X509 certificate and provides read-only access to its information.

-   [ca](././crypto/~/X509Certificate#property_ca)
-   [checkEmail](././crypto/~/X509Certificate#method_checkemail_0)
-   [checkHost](././crypto/~/X509Certificate#method_checkhost_0)
-   [checkIP](././crypto/~/X509Certificate#method_checkip_0)
-   [checkIssued](././crypto/~/X509Certificate#method_checkissued_0)
-   [checkPrivateKey](././crypto/~/X509Certificate#method_checkprivatekey_0)
-   [fingerprint](././crypto/~/X509Certificate#property_fingerprint)
-   [fingerprint256](././crypto/~/X509Certificate#property_fingerprint256)
-   [fingerprint512](././crypto/~/X509Certificate#property_fingerprint512)
-   [infoAccess](././crypto/~/X509Certificate#property_infoaccess)
-   [issuer](././crypto/~/X509Certificate#property_issuer)
-   [issuerCertificate](././crypto/~/X509Certificate#property_issuercertificate)
-   [keyUsage](././crypto/~/X509Certificate#property_keyusage)
-   [publicKey](././crypto/~/X509Certificate#property_publickey)
-   [raw](././crypto/~/X509Certificate#property_raw)
-   [serialNumber](././crypto/~/X509Certificate#property_serialnumber)
-   [subject](././crypto/~/X509Certificate#property_subject)
-   [subjectAltName](././crypto/~/X509Certificate#property_subjectaltname)
-   [toJSON](././crypto/~/X509Certificate#method_tojson_0)
-   [toLegacyObject](././crypto/~/X509Certificate#method_tolegacyobject_0)
-   [toString](././crypto/~/X509Certificate#method_tostring_0)
-   [validFrom](././crypto/~/X509Certificate#property_validfrom)
-   [validFromDate](././crypto/~/X509Certificate#property_validfromdate)
-   [validTo](././crypto/~/X509Certificate#property_validto)
-   [validToDate](././crypto/~/X509Certificate#property_validtodate)
-   [verify](././crypto/~/X509Certificate#method_verify_0)

I

[X509CheckOptions](././crypto/~/X509CheckOptions "X509CheckOptions")

No documentation available

-   [multiLabelWildcards](././crypto/~/X509CheckOptions#property_multilabelwildcards)
-   [partialWildcards](././crypto/~/X509CheckOptions#property_partialwildcards)
-   [singleLabelSubdomains](././crypto/~/X509CheckOptions#property_singlelabelsubdomains)
-   [subject](././crypto/~/X509CheckOptions#property_subject)
-   [wildcards](././crypto/~/X509CheckOptions#property_wildcards)

v

[fips](././crypto/~/fips "fips")

No documentation available

c

[Hmac](././crypto/~/Hmac "Hmac")

The `Hmac` class is a utility for creating cryptographic HMAC digests. It can be used in one of two ways:

-   [digest](././crypto/~/Hmac#method_digest_0)
-   [update](././crypto/~/Hmac#method_update_0)

The `node:dgram` module provides an implementation of UDP datagram sockets.

I

[BindOptions](././dgram/~/BindOptions "BindOptions")

No documentation available

-   [address](././dgram/~/BindOptions#property_address)
-   [exclusive](././dgram/~/BindOptions#property_exclusive)
-   [fd](././dgram/~/BindOptions#property_fd)
-   [port](././dgram/~/BindOptions#property_port)

f

[createSocket](././dgram/~/createSocket "createSocket")

Creates a `dgram.Socket` object. Once the socket is created, calling `socket.bind()` will instruct the socket to begin listening for datagram messages. When `address` and `port` are not passed to `socket.bind()` the method will bind the socket to the "all interfaces" address on a random port (it does the right thing for both `udp4` and `udp6` sockets). The bound address and port can be retrieved using `socket.address().address` and `socket.address().port`.

I

[RemoteInfo](././dgram/~/RemoteInfo "RemoteInfo")

No documentation available

-   [address](././dgram/~/RemoteInfo#property_address)
-   [family](././dgram/~/RemoteInfo#property_family)
-   [port](././dgram/~/RemoteInfo#property_port)
-   [size](././dgram/~/RemoteInfo#property_size)

c

[Socket](././dgram/~/Socket "Socket")

No documentation available

-   [addListener](././dgram/~/Socket#method_addlistener_0)
-   [addMembership](././dgram/~/Socket#method_addmembership_0)
-   [addSourceSpecificMembership](././dgram/~/Socket#method_addsourcespecificmembership_0)
-   [address](././dgram/~/Socket#method_address_0)
-   [bind](././dgram/~/Socket#method_bind_0)
-   [close](././dgram/~/Socket#method_close_0)
-   [connect](././dgram/~/Socket#method_connect_0)
-   [disconnect](././dgram/~/Socket#method_disconnect_0)
-   [dropMembership](././dgram/~/Socket#method_dropmembership_0)
-   [dropSourceSpecificMembership](././dgram/~/Socket#method_dropsourcespecificmembership_0)
-   [emit](././dgram/~/Socket#method_emit_0)
-   [getRecvBufferSize](././dgram/~/Socket#method_getrecvbuffersize_0)
-   [getSendBufferSize](././dgram/~/Socket#method_getsendbuffersize_0)
-   [getSendQueueCount](././dgram/~/Socket#method_getsendqueuecount_0)
-   [getSendQueueSize](././dgram/~/Socket#method_getsendqueuesize_0)
-   [on](././dgram/~/Socket#method_on_0)
-   [once](././dgram/~/Socket#method_once_0)
-   [prependListener](././dgram/~/Socket#method_prependlistener_0)
-   [prependOnceListener](././dgram/~/Socket#method_prependoncelistener_0)
-   [ref](././dgram/~/Socket#method_ref_0)
-   [remoteAddress](././dgram/~/Socket#method_remoteaddress_0)
-   [send](././dgram/~/Socket#method_send_0)
-   [setBroadcast](././dgram/~/Socket#method_setbroadcast_0)
-   [setMulticastInterface](././dgram/~/Socket#method_setmulticastinterface_0)
-   [setMulticastLoopback](././dgram/~/Socket#method_setmulticastloopback_0)
-   [setMulticastTTL](././dgram/~/Socket#method_setmulticastttl_0)
-   [setRecvBufferSize](././dgram/~/Socket#method_setrecvbuffersize_0)
-   [setSendBufferSize](././dgram/~/Socket#method_setsendbuffersize_0)
-   [setTTL](././dgram/~/Socket#method_setttl_0)
-   [unref](././dgram/~/Socket#method_unref_0)

I

[SocketOptions](././dgram/~/SocketOptions "SocketOptions")

No documentation available

-   [ipv6Only](././dgram/~/SocketOptions#property_ipv6only)
-   [lookup](././dgram/~/SocketOptions#property_lookup)
-   [receiveBlockList](././dgram/~/SocketOptions#property_receiveblocklist)
-   [recvBufferSize](././dgram/~/SocketOptions#property_recvbuffersize)
-   [reuseAddr](././dgram/~/SocketOptions#property_reuseaddr)
-   [reusePort](././dgram/~/SocketOptions#property_reuseport)
-   [sendBlockList](././dgram/~/SocketOptions#property_sendblocklist)
-   [sendBufferSize](././dgram/~/SocketOptions#property_sendbuffersize)
-   [type](././dgram/~/SocketOptions#property_type)

T

[SocketType](././dgram/~/SocketType "SocketType")

No documentation available

The `node:diagnostics_channel` module provides an API to create named channels to report arbitrary message data for diagnostics purposes.

c

[Channel](././diagnostics_channel/~/Channel "Channel")

The class `Channel` represents an individual named channel within the data pipeline. It is used to track subscribers and to publish messages when there are subscribers present. It exists as a separate object to avoid channel lookups at publish time, enabling very fast publish speeds and allowing for heavy use while incurring very minimal cost. Channels are created with [channel](././diagnostics_channel/~/channel), constructing a channel directly with `new Channel(name)` is not supported.

-   [bindStore](././diagnostics_channel/~/Channel#method_bindstore_0)
-   [hasSubscribers](././diagnostics_channel/~/Channel#property_hassubscribers)
-   [name](././diagnostics_channel/~/Channel#property_name)
-   [publish](././diagnostics_channel/~/Channel#method_publish_0)
-   [runStores](././diagnostics_channel/~/Channel#method_runstores_0)
-   [subscribe](././diagnostics_channel/~/Channel#method_subscribe_0)
-   [unbindStore](././diagnostics_channel/~/Channel#method_unbindstore_0)
-   [unsubscribe](././diagnostics_channel/~/Channel#method_unsubscribe_0)

f

[channel](././diagnostics_channel/~/channel "channel")

This is the primary entry-point for anyone wanting to publish to a named channel. It produces a channel object which is optimized to reduce overhead at publish time as much as possible.

T

[ChannelListener](././diagnostics_channel/~/ChannelListener "ChannelListener")

No documentation available

f

[hasSubscribers](././diagnostics_channel/~/hasSubscribers "hasSubscribers")

Check if there are active subscribers to the named channel. This is helpful if the message you want to send might be expensive to prepare.

f

[subscribe](././diagnostics_channel/~/subscribe "subscribe")

Register a message handler to subscribe to this channel. This message handler will be run synchronously whenever a message is published to the channel. Any errors thrown in the message handler will trigger an `'uncaughtException'`.

c

[TracingChannel](././diagnostics_channel/~/TracingChannel "TracingChannel")

The class `TracingChannel` is a collection of `TracingChannel Channels` which together express a single traceable action. It is used to formalize and simplify the process of producing events for tracing application flow. [tracingChannel](././diagnostics_channel/~/tracingChannel) is used to construct a `TracingChannel`. As with `Channel` it is recommended to create and reuse a single `TracingChannel` at the top-level of the file rather than creating them dynamically.

-   [asyncEnd](././diagnostics_channel/~/TracingChannel#property_asyncend)
-   [asyncStart](././diagnostics_channel/~/TracingChannel#property_asyncstart)
-   [end](././diagnostics_channel/~/TracingChannel#property_end)
-   [error](././diagnostics_channel/~/TracingChannel#property_error)
-   [start](././diagnostics_channel/~/TracingChannel#property_start)
-   [subscribe](././diagnostics_channel/~/TracingChannel#method_subscribe_0)
-   [traceCallback](././diagnostics_channel/~/TracingChannel#method_tracecallback_0)
-   [tracePromise](././diagnostics_channel/~/TracingChannel#method_tracepromise_0)
-   [traceSync](././diagnostics_channel/~/TracingChannel#method_tracesync_0)
-   [unsubscribe](././diagnostics_channel/~/TracingChannel#method_unsubscribe_0)

f

[tracingChannel](././diagnostics_channel/~/tracingChannel "tracingChannel")

Creates a `TracingChannel` wrapper for the given `TracingChannel Channels`. If a name is given, the corresponding tracing channels will be created in the form of `tracing:${name}:${eventType}` where `eventType` corresponds to the types of `TracingChannel Channels`.

I

[TracingChannelCollection](././diagnostics_channel/~/TracingChannelCollection "TracingChannelCollection")

No documentation available

-   [asyncEnd](././diagnostics_channel/~/TracingChannelCollection#property_asyncend)
-   [asyncStart](././diagnostics_channel/~/TracingChannelCollection#property_asyncstart)
-   [end](././diagnostics_channel/~/TracingChannelCollection#property_end)
-   [error](././diagnostics_channel/~/TracingChannelCollection#property_error)
-   [start](././diagnostics_channel/~/TracingChannelCollection#property_start)

I

[TracingChannelSubscribers](././diagnostics_channel/~/TracingChannelSubscribers "TracingChannelSubscribers")

No documentation available

-   [asyncEnd](././diagnostics_channel/~/TracingChannelSubscribers#property_asyncend)
-   [asyncStart](././diagnostics_channel/~/TracingChannelSubscribers#property_asyncstart)
-   [end](././diagnostics_channel/~/TracingChannelSubscribers#property_end)
-   [error](././diagnostics_channel/~/TracingChannelSubscribers#property_error)
-   [start](././diagnostics_channel/~/TracingChannelSubscribers#property_start)

f

[unsubscribe](././diagnostics_channel/~/unsubscribe "unsubscribe")

Remove a message handler previously registered to this channel with [subscribe](././diagnostics_channel/~/subscribe).

The `node:dns` module enables name resolution. For example, use it to look up IP addresses of host names.

v

[ADDRCONFIG](././dns/~/ADDRCONFIG "ADDRCONFIG")

Limits returned address types to the types of non-loopback addresses configured on the system. For example, IPv4 addresses are only returned if the current system has at least one IPv4 address configured.

v

[ADDRGETNETWORKPARAMS](././dns/~/ADDRGETNETWORKPARAMS "ADDRGETNETWORKPARAMS")

No documentation available

v

[ALL](././dns/~/ALL "ALL")

If `dns.V4MAPPED` is specified, return resolved IPv6 addresses as well as IPv4 mapped IPv6 addresses.

I

[AnyAaaaRecord](././dns/~/AnyAaaaRecord "AnyAaaaRecord")

No documentation available

-   [type](././dns/~/AnyAaaaRecord#property_type)

I

[AnyARecord](././dns/~/AnyARecord "AnyARecord")

No documentation available

-   [type](././dns/~/AnyARecord#property_type)

I

[AnyCnameRecord](././dns/~/AnyCnameRecord "AnyCnameRecord")

No documentation available

-   [type](././dns/~/AnyCnameRecord#property_type)
-   [value](././dns/~/AnyCnameRecord#property_value)

I

[AnyMxRecord](././dns/~/AnyMxRecord "AnyMxRecord")

No documentation available

-   [type](././dns/~/AnyMxRecord#property_type)

I

[AnyNaptrRecord](././dns/~/AnyNaptrRecord "AnyNaptrRecord")

No documentation available

-   [type](././dns/~/AnyNaptrRecord#property_type)

I

[AnyNsRecord](././dns/~/AnyNsRecord "AnyNsRecord")

No documentation available

-   [type](././dns/~/AnyNsRecord#property_type)
-   [value](././dns/~/AnyNsRecord#property_value)

I

[AnyPtrRecord](././dns/~/AnyPtrRecord "AnyPtrRecord")

No documentation available

-   [type](././dns/~/AnyPtrRecord#property_type)
-   [value](././dns/~/AnyPtrRecord#property_value)

T

[AnyRecord](././dns/~/AnyRecord "AnyRecord")

No documentation available

I

[AnySoaRecord](././dns/~/AnySoaRecord "AnySoaRecord")

No documentation available

-   [type](././dns/~/AnySoaRecord#property_type)

I

[AnySrvRecord](././dns/~/AnySrvRecord "AnySrvRecord")

No documentation available

-   [type](././dns/~/AnySrvRecord#property_type)

I

[AnyTxtRecord](././dns/~/AnyTxtRecord "AnyTxtRecord")

No documentation available

-   [entries](././dns/~/AnyTxtRecord#property_entries)
-   [type](././dns/~/AnyTxtRecord#property_type)

v

[BADFAMILY](././dns/~/BADFAMILY "BADFAMILY")

No documentation available

v

[BADFLAGS](././dns/~/BADFLAGS "BADFLAGS")

No documentation available

v

[BADHINTS](././dns/~/BADHINTS "BADHINTS")

No documentation available

v

[BADNAME](././dns/~/BADNAME "BADNAME")

No documentation available

v

[BADQUERY](././dns/~/BADQUERY "BADQUERY")

No documentation available

v

[BADRESP](././dns/~/BADRESP "BADRESP")

No documentation available

v

[BADSTR](././dns/~/BADSTR "BADSTR")

No documentation available

I

[CaaRecord](././dns/~/CaaRecord "CaaRecord")

No documentation available

-   [contactemail](././dns/~/CaaRecord#property_contactemail)
-   [contactphone](././dns/~/CaaRecord#property_contactphone)
-   [critical](././dns/~/CaaRecord#property_critical)
-   [iodef](././dns/~/CaaRecord#property_iodef)
-   [issue](././dns/~/CaaRecord#property_issue)
-   [issuewild](././dns/~/CaaRecord#property_issuewild)

v

[CANCELLED](././dns/~/CANCELLED "CANCELLED")

No documentation available

v

[CONNREFUSED](././dns/~/CONNREFUSED "CONNREFUSED")

No documentation available

v

[DESTRUCTION](././dns/~/DESTRUCTION "DESTRUCTION")

No documentation available

v

[EOF](././dns/~/EOF "EOF")

No documentation available

v

[FILE](././dns/~/FILE "FILE")

No documentation available

v

[FORMERR](././dns/~/FORMERR "FORMERR")

No documentation available

f

[getDefaultResultOrder](././dns/~/getDefaultResultOrder "getDefaultResultOrder")

Get the default value for `order` in [lookup](././dns/~/lookup) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest-v22.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[getServers](././dns/~/getServers "getServers")

Returns an array of IP address strings, formatted according to [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6), that are currently configured for DNS resolution. A string will include a port section if a custom port is used.

v

[LOADIPHLPAPI](././dns/~/LOADIPHLPAPI "LOADIPHLPAPI")

No documentation available

f

[lookup](././dns/~/lookup "lookup")

Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is `0` or not provided, then IPv4 and IPv6 addresses are both returned if found.

I

[LookupAddress](././dns/~/LookupAddress "LookupAddress")

No documentation available

-   [address](././dns/~/LookupAddress#property_address)
-   [family](././dns/~/LookupAddress#property_family)

I

[LookupAllOptions](././dns/~/LookupAllOptions "LookupAllOptions")

No documentation available

-   [all](././dns/~/LookupAllOptions#property_all)

I

[LookupOneOptions](././dns/~/LookupOneOptions "LookupOneOptions")

No documentation available

-   [all](././dns/~/LookupOneOptions#property_all)

I

[LookupOptions](././dns/~/LookupOptions "LookupOptions")

No documentation available

-   [all](././dns/~/LookupOptions#property_all)
-   [family](././dns/~/LookupOptions#property_family)
-   [hints](././dns/~/LookupOptions#property_hints)
-   [order](././dns/~/LookupOptions#property_order)
-   [verbatim](././dns/~/LookupOptions#property_verbatim)

f

[lookupService](././dns/~/lookupService "lookupService")

Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.

I

[MxRecord](././dns/~/MxRecord "MxRecord")

No documentation available

-   [exchange](././dns/~/MxRecord#property_exchange)
-   [priority](././dns/~/MxRecord#property_priority)

I

[NaptrRecord](././dns/~/NaptrRecord "NaptrRecord")

No documentation available

-   [flags](././dns/~/NaptrRecord#property_flags)
-   [order](././dns/~/NaptrRecord#property_order)
-   [preference](././dns/~/NaptrRecord#property_preference)
-   [regexp](././dns/~/NaptrRecord#property_regexp)
-   [replacement](././dns/~/NaptrRecord#property_replacement)
-   [service](././dns/~/NaptrRecord#property_service)

v

[NODATA](././dns/~/NODATA "NODATA")

No documentation available

v

[NOMEM](././dns/~/NOMEM "NOMEM")

No documentation available

v

[NONAME](././dns/~/NONAME "NONAME")

No documentation available

v

[NOTFOUND](././dns/~/NOTFOUND "NOTFOUND")

No documentation available

v

[NOTIMP](././dns/~/NOTIMP "NOTIMP")

No documentation available

v

[NOTINITIALIZED](././dns/~/NOTINITIALIZED "NOTINITIALIZED")

No documentation available

N

[promises](././dns/~/promises "promises")

The `dns.promises` API provides an alternative set of asynchronous DNS methods that return `Promise` objects rather than using callbacks. The API is accessible via `import { promises as dnsPromises } from 'node:dns'` or `import dnsPromises from 'node:dns/promises'`.

I

[RecordWithTtl](././dns/~/RecordWithTtl "RecordWithTtl")

No documentation available

-   [address](././dns/~/RecordWithTtl#property_address)
-   [ttl](././dns/~/RecordWithTtl#property_ttl)

v

[REFUSED](././dns/~/REFUSED "REFUSED")

No documentation available

f

[resolve](././dns/~/resolve "resolve")

No documentation available

f

[resolve4](././dns/~/resolve4 "resolve4")

No documentation available

f

[resolve6](././dns/~/resolve6 "resolve6")

No documentation available

f

[resolveAny](././dns/~/resolveAny "resolveAny")

No documentation available

f

[resolveCaa](././dns/~/resolveCaa "resolveCaa")

No documentation available

f

[resolveCname](././dns/~/resolveCname "resolveCname")

No documentation available

f

[resolveMx](././dns/~/resolveMx "resolveMx")

No documentation available

f

[resolveNaptr](././dns/~/resolveNaptr "resolveNaptr")

No documentation available

f

[resolveNs](././dns/~/resolveNs "resolveNs")

No documentation available

I

[ResolveOptions](././dns/~/ResolveOptions "ResolveOptions")

No documentation available

-   [ttl](././dns/~/ResolveOptions#property_ttl)

f

[resolvePtr](././dns/~/resolvePtr "resolvePtr")

No documentation available

c

[Resolver](././dns/~/Resolver "Resolver")

An independent resolver for DNS requests.

-   [cancel](././dns/~/Resolver#method_cancel_0)
-   [getServers](././dns/~/Resolver#property_getservers)
-   [resolve](././dns/~/Resolver#property_resolve)
-   [resolve4](././dns/~/Resolver#property_resolve4)
-   [resolve6](././dns/~/Resolver#property_resolve6)
-   [resolveAny](././dns/~/Resolver#property_resolveany)
-   [resolveCaa](././dns/~/Resolver#property_resolvecaa)
-   [resolveCname](././dns/~/Resolver#property_resolvecname)
-   [resolveMx](././dns/~/Resolver#property_resolvemx)
-   [resolveNaptr](././dns/~/Resolver#property_resolvenaptr)
-   [resolveNs](././dns/~/Resolver#property_resolvens)
-   [resolvePtr](././dns/~/Resolver#property_resolveptr)
-   [resolveSoa](././dns/~/Resolver#property_resolvesoa)
-   [resolveSrv](././dns/~/Resolver#property_resolvesrv)
-   [resolveTxt](././dns/~/Resolver#property_resolvetxt)
-   [reverse](././dns/~/Resolver#property_reverse)
-   [setLocalAddress](././dns/~/Resolver#method_setlocaladdress_0)
-   [setServers](././dns/~/Resolver#property_setservers)

I

[ResolverOptions](././dns/~/ResolverOptions "ResolverOptions")

No documentation available

-   [timeout](././dns/~/ResolverOptions#property_timeout)
-   [tries](././dns/~/ResolverOptions#property_tries)

f

[resolveSoa](././dns/~/resolveSoa "resolveSoa")

No documentation available

f

[resolveSrv](././dns/~/resolveSrv "resolveSrv")

No documentation available

f

[resolveTxt](././dns/~/resolveTxt "resolveTxt")

No documentation available

I

[ResolveWithTtlOptions](././dns/~/ResolveWithTtlOptions "ResolveWithTtlOptions")

No documentation available

-   [ttl](././dns/~/ResolveWithTtlOptions#property_ttl)

f

[reverse](././dns/~/reverse "reverse")

Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.

v

[SERVFAIL](././dns/~/SERVFAIL "SERVFAIL")

No documentation available

f

[setDefaultResultOrder](././dns/~/setDefaultResultOrder "setDefaultResultOrder")

Set the default value of `order` in [lookup](././dns/~/lookup) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest-v22.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[setServers](././dns/~/setServers "setServers")

Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6) formatted addresses. If the port is the IANA default DNS port (53) it can be omitted.

I

[SoaRecord](././dns/~/SoaRecord "SoaRecord")

No documentation available

-   [expire](././dns/~/SoaRecord#property_expire)
-   [hostmaster](././dns/~/SoaRecord#property_hostmaster)
-   [minttl](././dns/~/SoaRecord#property_minttl)
-   [nsname](././dns/~/SoaRecord#property_nsname)
-   [refresh](././dns/~/SoaRecord#property_refresh)
-   [retry](././dns/~/SoaRecord#property_retry)
-   [serial](././dns/~/SoaRecord#property_serial)

I

[SrvRecord](././dns/~/SrvRecord "SrvRecord")

No documentation available

-   [name](././dns/~/SrvRecord#property_name)
-   [port](././dns/~/SrvRecord#property_port)
-   [priority](././dns/~/SrvRecord#property_priority)
-   [weight](././dns/~/SrvRecord#property_weight)

v

[TIMEOUT](././dns/~/TIMEOUT "TIMEOUT")

No documentation available

v

[V4MAPPED](././dns/~/V4MAPPED "V4MAPPED")

If the IPv6 family was specified, but no IPv6 addresses were found, then return IPv4 mapped IPv6 addresses. It is not supported on some operating systems (e.g. FreeBSD 10.1).

T

[AnyRecordWithTtl](././dns/~/AnyRecordWithTtl "AnyRecordWithTtl")

No documentation available

The `dns.promises` API provides an alternative set of asynchronous DNS methods that return `Promise` objects rather than using callbacks. The API is accessible via `import { promises as dnsPromises } from 'node:dns'` or `import dnsPromises from 'node:dns/promises'`.

v

[ADDRGETNETWORKPARAMS](././dns/promises/~/ADDRGETNETWORKPARAMS "ADDRGETNETWORKPARAMS")

No documentation available

v

[BADFAMILY](././dns/promises/~/BADFAMILY "BADFAMILY")

No documentation available

v

[BADFLAGS](././dns/promises/~/BADFLAGS "BADFLAGS")

No documentation available

v

[BADHINTS](././dns/promises/~/BADHINTS "BADHINTS")

No documentation available

v

[BADNAME](././dns/promises/~/BADNAME "BADNAME")

No documentation available

v

[BADQUERY](././dns/promises/~/BADQUERY "BADQUERY")

No documentation available

v

[BADRESP](././dns/promises/~/BADRESP "BADRESP")

No documentation available

v

[BADSTR](././dns/promises/~/BADSTR "BADSTR")

No documentation available

v

[CANCELLED](././dns/promises/~/CANCELLED "CANCELLED")

No documentation available

v

[CONNREFUSED](././dns/promises/~/CONNREFUSED "CONNREFUSED")

No documentation available

v

[DESTRUCTION](././dns/promises/~/DESTRUCTION "DESTRUCTION")

No documentation available

v

[EOF](././dns/promises/~/EOF "EOF")

No documentation available

v

[FILE](././dns/promises/~/FILE "FILE")

No documentation available

v

[FORMERR](././dns/promises/~/FORMERR "FORMERR")

No documentation available

f

[getDefaultResultOrder](././dns/promises/~/getDefaultResultOrder "getDefaultResultOrder")

Get the default value for `verbatim` in [lookup](././dns/promises/~/lookup) and [dnsPromises.lookup()](https://nodejs.org/docs/latest-v20.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[getServers](././dns/promises/~/getServers "getServers")

Returns an array of IP address strings, formatted according to [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6), that are currently configured for DNS resolution. A string will include a port section if a custom port is used.

v

[LOADIPHLPAPI](././dns/promises/~/LOADIPHLPAPI "LOADIPHLPAPI")

No documentation available

f

[lookup](././dns/promises/~/lookup "lookup")

Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is not provided, then IPv4 and IPv6 addresses are both returned if found.

f

[lookupService](././dns/promises/~/lookupService "lookupService")

Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.

v

[NODATA](././dns/promises/~/NODATA "NODATA")

No documentation available

v

[NOMEM](././dns/promises/~/NOMEM "NOMEM")

No documentation available

v

[NONAME](././dns/promises/~/NONAME "NONAME")

No documentation available

v

[NOTFOUND](././dns/promises/~/NOTFOUND "NOTFOUND")

No documentation available

v

[NOTIMP](././dns/promises/~/NOTIMP "NOTIMP")

No documentation available

v

[NOTINITIALIZED](././dns/promises/~/NOTINITIALIZED "NOTINITIALIZED")

No documentation available

v

[promises.ADDRGETNETWORKPARAMS](././dns/promises/~/promises.ADDRGETNETWORKPARAMS "promises.ADDRGETNETWORKPARAMS")

No documentation available

v

[promises.BADFAMILY](././dns/promises/~/promises.BADFAMILY "promises.BADFAMILY")

No documentation available

v

[promises.BADFLAGS](././dns/promises/~/promises.BADFLAGS "promises.BADFLAGS")

No documentation available

v

[promises.BADHINTS](././dns/promises/~/promises.BADHINTS "promises.BADHINTS")

No documentation available

v

[promises.BADNAME](././dns/promises/~/promises.BADNAME "promises.BADNAME")

No documentation available

v

[promises.BADQUERY](././dns/promises/~/promises.BADQUERY "promises.BADQUERY")

No documentation available

v

[promises.BADRESP](././dns/promises/~/promises.BADRESP "promises.BADRESP")

No documentation available

v

[promises.BADSTR](././dns/promises/~/promises.BADSTR "promises.BADSTR")

No documentation available

v

[promises.CANCELLED](././dns/promises/~/promises.CANCELLED "promises.CANCELLED")

No documentation available

v

[promises.CONNREFUSED](././dns/promises/~/promises.CONNREFUSED "promises.CONNREFUSED")

No documentation available

v

[promises.DESTRUCTION](././dns/promises/~/promises.DESTRUCTION "promises.DESTRUCTION")

No documentation available

v

[promises.EOF](././dns/promises/~/promises.EOF "promises.EOF")

No documentation available

v

[promises.FILE](././dns/promises/~/promises.FILE "promises.FILE")

No documentation available

v

[promises.FORMERR](././dns/promises/~/promises.FORMERR "promises.FORMERR")

No documentation available

f

[promises.getDefaultResultOrder](././dns/promises/~/promises.getDefaultResultOrder "promises.getDefaultResultOrder")

Get the default value for `verbatim` in [lookup](././dns/promises/~/lookup) and [dnsPromises.lookup()](https://nodejs.org/docs/latest-v20.x/api/dns.html#dnspromiseslookuphostname-options). The value could be:

f

[promises.getServers](././dns/promises/~/promises.getServers "promises.getServers")

Returns an array of IP address strings, formatted according to [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6), that are currently configured for DNS resolution. A string will include a port section if a custom port is used.

v

[promises.LOADIPHLPAPI](././dns/promises/~/promises.LOADIPHLPAPI "promises.LOADIPHLPAPI")

No documentation available

f

[promises.lookup](././dns/promises/~/promises.lookup "promises.lookup")

Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is not provided, then IPv4 and IPv6 addresses are both returned if found.

f

[promises.lookupService](././dns/promises/~/promises.lookupService "promises.lookupService")

Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.

v

[promises.NODATA](././dns/promises/~/promises.NODATA "promises.NODATA")

No documentation available

v

[promises.NOMEM](././dns/promises/~/promises.NOMEM "promises.NOMEM")

No documentation available

v

[promises.NONAME](././dns/promises/~/promises.NONAME "promises.NONAME")

No documentation available

v

[promises.NOTFOUND](././dns/promises/~/promises.NOTFOUND "promises.NOTFOUND")

No documentation available

v

[promises.NOTIMP](././dns/promises/~/promises.NOTIMP "promises.NOTIMP")

No documentation available

v

[promises.NOTINITIALIZED](././dns/promises/~/promises.NOTINITIALIZED "promises.NOTINITIALIZED")

No documentation available

v

[promises.REFUSED](././dns/promises/~/promises.REFUSED "promises.REFUSED")

No documentation available

f

[promises.resolve](././dns/promises/~/promises.resolve "promises.resolve")

Uses the DNS protocol to resolve a host name (e.g. `'nodejs.org'`) into an array of the resource records. When successful, the `Promise` is resolved with an array of resource records. The type and structure of individual results vary based on `rrtype`:

f

[promises.resolve4](././dns/promises/~/promises.resolve4 "promises.resolve4")

Uses the DNS protocol to resolve IPv4 addresses (`A` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv4 addresses (e.g. `['74.125.79.104', '74.125.79.105', '74.125.79.106']`).

f

[promises.resolve6](././dns/promises/~/promises.resolve6 "promises.resolve6")

Uses the DNS protocol to resolve IPv6 addresses (`AAAA` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv6 addresses.

f

[promises.resolveAny](././dns/promises/~/promises.resolveAny "promises.resolveAny")

Uses the DNS protocol to resolve all records (also known as `ANY` or `*` query). On success, the `Promise` is resolved with an array containing various types of records. Each object has a property `type` that indicates the type of the current record. And depending on the `type`, additional properties will be present on the object:

f

[promises.resolveCaa](././dns/promises/~/promises.resolveCaa "promises.resolveCaa")

Uses the DNS protocol to resolve `CAA` records for the `hostname`. On success, the `Promise` is resolved with an array of objects containing available certification authority authorization records available for the `hostname` (e.g. `[{critical: 0, iodef: 'mailto:pki@example.com'},{critical: 128, issue: 'pki.example.com'}]`).

f

[promises.resolveCname](././dns/promises/~/promises.resolveCname "promises.resolveCname")

Uses the DNS protocol to resolve `CNAME` records for the `hostname`. On success, the `Promise` is resolved with an array of canonical name records available for the `hostname` (e.g. `['bar.example.com']`).

f

[promises.resolveMx](././dns/promises/~/promises.resolveMx "promises.resolveMx")

Uses the DNS protocol to resolve mail exchange records (`MX` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects containing both a `priority` and `exchange` property (e.g.`[{priority: 10, exchange: 'mx.example.com'}, ...]`).

f

[promises.resolveNaptr](././dns/promises/~/promises.resolveNaptr "promises.resolveNaptr")

Uses the DNS protocol to resolve regular expression-based records (`NAPTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[promises.resolveNs](././dns/promises/~/promises.resolveNs "promises.resolveNs")

Uses the DNS protocol to resolve name server records (`NS` records) for the `hostname`. On success, the `Promise` is resolved with an array of name server records available for `hostname` (e.g.`['ns1.example.com', 'ns2.example.com']`).

f

[promises.resolvePtr](././dns/promises/~/promises.resolvePtr "promises.resolvePtr")

Uses the DNS protocol to resolve pointer records (`PTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of strings containing the reply records.

c

[promises.Resolver](././dns/promises/~/promises.Resolver "promises.Resolver")

An independent resolver for DNS requests.

-   [cancel](././dns/promises/~/promises.Resolver#method_cancel_0)
-   [getServers](././dns/promises/~/promises.Resolver#property_getservers)
-   [resolve](././dns/promises/~/promises.Resolver#property_resolve)
-   [resolve4](././dns/promises/~/promises.Resolver#property_resolve4)
-   [resolve6](././dns/promises/~/promises.Resolver#property_resolve6)
-   [resolveAny](././dns/promises/~/promises.Resolver#property_resolveany)
-   [resolveCaa](././dns/promises/~/promises.Resolver#property_resolvecaa)
-   [resolveCname](././dns/promises/~/promises.Resolver#property_resolvecname)
-   [resolveMx](././dns/promises/~/promises.Resolver#property_resolvemx)
-   [resolveNaptr](././dns/promises/~/promises.Resolver#property_resolvenaptr)
-   [resolveNs](././dns/promises/~/promises.Resolver#property_resolvens)
-   [resolvePtr](././dns/promises/~/promises.Resolver#property_resolveptr)
-   [resolveSoa](././dns/promises/~/promises.Resolver#property_resolvesoa)
-   [resolveSrv](././dns/promises/~/promises.Resolver#property_resolvesrv)
-   [resolveTxt](././dns/promises/~/promises.Resolver#property_resolvetxt)
-   [reverse](././dns/promises/~/promises.Resolver#property_reverse)
-   [setLocalAddress](././dns/promises/~/promises.Resolver#method_setlocaladdress_0)
-   [setServers](././dns/promises/~/promises.Resolver#property_setservers)

f

[promises.resolveSoa](././dns/promises/~/promises.resolveSoa "promises.resolveSoa")

Uses the DNS protocol to resolve a start of authority record (`SOA` record) for the `hostname`. On success, the `Promise` is resolved with an object with the following properties:

f

[promises.resolveSrv](././dns/promises/~/promises.resolveSrv "promises.resolveSrv")

Uses the DNS protocol to resolve service records (`SRV` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[promises.resolveTxt](././dns/promises/~/promises.resolveTxt "promises.resolveTxt")

Uses the DNS protocol to resolve text queries (`TXT` records) for the `hostname`. On success, the `Promise` is resolved with a two-dimensional array of the text records available for `hostname` (e.g.`[ ['v=spf1 ip4:0.0.0.0 ', '~all' ] ]`). Each sub-array contains TXT chunks of one record. Depending on the use case, these could be either joined together or treated separately.

f

[promises.reverse](././dns/promises/~/promises.reverse "promises.reverse")

Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.

v

[promises.SERVFAIL](././dns/promises/~/promises.SERVFAIL "promises.SERVFAIL")

No documentation available

f

[promises.setDefaultResultOrder](././dns/promises/~/promises.setDefaultResultOrder "promises.setDefaultResultOrder")

Set the default value of `order` in `dns.lookup()` and `[lookup](././dns/promises/~/lookup)`. The value could be:

f

[promises.setServers](././dns/promises/~/promises.setServers "promises.setServers")

Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6) formatted addresses. If the port is the IANA default DNS port (53) it can be omitted.

v

[promises.TIMEOUT](././dns/promises/~/promises.TIMEOUT "promises.TIMEOUT")

No documentation available

v

[REFUSED](././dns/promises/~/REFUSED "REFUSED")

No documentation available

f

[resolve](././dns/promises/~/resolve "resolve")

Uses the DNS protocol to resolve a host name (e.g. `'nodejs.org'`) into an array of the resource records. When successful, the `Promise` is resolved with an array of resource records. The type and structure of individual results vary based on `rrtype`:

f

[resolve4](././dns/promises/~/resolve4 "resolve4")

Uses the DNS protocol to resolve IPv4 addresses (`A` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv4 addresses (e.g. `['74.125.79.104', '74.125.79.105', '74.125.79.106']`).

f

[resolve6](././dns/promises/~/resolve6 "resolve6")

Uses the DNS protocol to resolve IPv6 addresses (`AAAA` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv6 addresses.

f

[resolveAny](././dns/promises/~/resolveAny "resolveAny")

Uses the DNS protocol to resolve all records (also known as `ANY` or `*` query). On success, the `Promise` is resolved with an array containing various types of records. Each object has a property `type` that indicates the type of the current record. And depending on the `type`, additional properties will be present on the object:

f

[resolveCaa](././dns/promises/~/resolveCaa "resolveCaa")

Uses the DNS protocol to resolve `CAA` records for the `hostname`. On success, the `Promise` is resolved with an array of objects containing available certification authority authorization records available for the `hostname` (e.g. `[{critical: 0, iodef: 'mailto:pki@example.com'},{critical: 128, issue: 'pki.example.com'}]`).

f

[resolveCname](././dns/promises/~/resolveCname "resolveCname")

Uses the DNS protocol to resolve `CNAME` records for the `hostname`. On success, the `Promise` is resolved with an array of canonical name records available for the `hostname` (e.g. `['bar.example.com']`).

f

[resolveMx](././dns/promises/~/resolveMx "resolveMx")

Uses the DNS protocol to resolve mail exchange records (`MX` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects containing both a `priority` and `exchange` property (e.g.`[{priority: 10, exchange: 'mx.example.com'}, ...]`).

f

[resolveNaptr](././dns/promises/~/resolveNaptr "resolveNaptr")

Uses the DNS protocol to resolve regular expression-based records (`NAPTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[resolveNs](././dns/promises/~/resolveNs "resolveNs")

Uses the DNS protocol to resolve name server records (`NS` records) for the `hostname`. On success, the `Promise` is resolved with an array of name server records available for `hostname` (e.g.`['ns1.example.com', 'ns2.example.com']`).

f

[resolvePtr](././dns/promises/~/resolvePtr "resolvePtr")

Uses the DNS protocol to resolve pointer records (`PTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of strings containing the reply records.

c

[Resolver](././dns/promises/~/Resolver "Resolver")

An independent resolver for DNS requests.

-   [cancel](././dns/promises/~/Resolver#method_cancel_0)
-   [getServers](././dns/promises/~/Resolver#property_getservers)
-   [resolve](././dns/promises/~/Resolver#property_resolve)
-   [resolve4](././dns/promises/~/Resolver#property_resolve4)
-   [resolve6](././dns/promises/~/Resolver#property_resolve6)
-   [resolveAny](././dns/promises/~/Resolver#property_resolveany)
-   [resolveCaa](././dns/promises/~/Resolver#property_resolvecaa)
-   [resolveCname](././dns/promises/~/Resolver#property_resolvecname)
-   [resolveMx](././dns/promises/~/Resolver#property_resolvemx)
-   [resolveNaptr](././dns/promises/~/Resolver#property_resolvenaptr)
-   [resolveNs](././dns/promises/~/Resolver#property_resolvens)
-   [resolvePtr](././dns/promises/~/Resolver#property_resolveptr)
-   [resolveSoa](././dns/promises/~/Resolver#property_resolvesoa)
-   [resolveSrv](././dns/promises/~/Resolver#property_resolvesrv)
-   [resolveTxt](././dns/promises/~/Resolver#property_resolvetxt)
-   [reverse](././dns/promises/~/Resolver#property_reverse)
-   [setLocalAddress](././dns/promises/~/Resolver#method_setlocaladdress_0)
-   [setServers](././dns/promises/~/Resolver#property_setservers)

f

[resolveSoa](././dns/promises/~/resolveSoa "resolveSoa")

Uses the DNS protocol to resolve a start of authority record (`SOA` record) for the `hostname`. On success, the `Promise` is resolved with an object with the following properties:

f

[resolveSrv](././dns/promises/~/resolveSrv "resolveSrv")

Uses the DNS protocol to resolve service records (`SRV` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:

f

[resolveTxt](././dns/promises/~/resolveTxt "resolveTxt")

Uses the DNS protocol to resolve text queries (`TXT` records) for the `hostname`. On success, the `Promise` is resolved with a two-dimensional array of the text records available for `hostname` (e.g.`[ ['v=spf1 ip4:0.0.0.0 ', '~all' ] ]`). Each sub-array contains TXT chunks of one record. Depending on the use case, these could be either joined together or treated separately.

f

[reverse](././dns/promises/~/reverse "reverse")

Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.

v

[SERVFAIL](././dns/promises/~/SERVFAIL "SERVFAIL")

No documentation available

f

[setDefaultResultOrder](././dns/promises/~/setDefaultResultOrder "setDefaultResultOrder")

Set the default value of `order` in `dns.lookup()` and `[lookup](././dns/promises/~/lookup)`. The value could be:

f

[setServers](././dns/promises/~/setServers "setServers")

Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of [RFC 5952](https://tools.ietf.org/html/rfc5952#section-6) formatted addresses. If the port is the IANA default DNS port (53) it can be omitted.

v

[TIMEOUT](././dns/promises/~/TIMEOUT "TIMEOUT")

No documentation available

f

[create](././domain/~/create "create")

No documentation available

c

[Domain](././domain/~/Domain "Domain")

No documentation available

-   [add](././domain/~/Domain#method_add_0)
-   [bind](././domain/~/Domain#method_bind_0)
-   [enter](././domain/~/Domain#method_enter_0)
-   [exit](././domain/~/Domain#method_exit_0)
-   [intercept](././domain/~/Domain#method_intercept_0)
-   [members](././domain/~/Domain#property_members)
-   [remove](././domain/~/Domain#method_remove_0)
-   [run](././domain/~/Domain#method_run_0)

Much of the Node.js core API is built around an idiomatic asynchronous event-driven architecture in which certain kinds of objects (called "emitters") emit named events that cause `Function` objects ("listeners") to be called.

T

[AnyRest](././events/~/AnyRest "AnyRest")

No documentation available

T

[Args](././events/~/Args "Args")

No documentation available

T

[DefaultEventMap](././events/~/DefaultEventMap "DefaultEventMap")

No documentation available

c

I

N

[EventEmitter](././events/~/EventEmitter "EventEmitter")

The `EventEmitter` class is defined and exposed by the `node:events` module:

-   [addAbortListener](././events/~/EventEmitter#method_addabortlistener_0)
-   [addListener](././events/~/EventEmitter#method_addlistener_0)
-   [captureRejectionSymbol](././events/~/EventEmitter#property_capturerejectionsymbol)
-   [captureRejections](././events/~/EventEmitter#property_capturerejections)
-   [defaultMaxListeners](././events/~/EventEmitter#property_defaultmaxlisteners)
-   [emit](././events/~/EventEmitter#method_emit_0)
-   [errorMonitor](././events/~/EventEmitter#property_errormonitor)
-   [eventNames](././events/~/EventEmitter#method_eventnames_0)
-   [getEventListeners](././events/~/EventEmitter#method_geteventlisteners_0)
-   [getMaxListeners](././events/~/EventEmitter#method_getmaxlisteners_0)
-   [listenerCount](././events/~/EventEmitter#method_listenercount_0)
-   [listeners](././events/~/EventEmitter#method_listeners_0)
-   [off](././events/~/EventEmitter#method_off_0)
-   [on](././events/~/EventEmitter#method_on_0)
-   [once](././events/~/EventEmitter#method_once_0)
-   [prependListener](././events/~/EventEmitter#method_prependlistener_0)
-   [prependOnceListener](././events/~/EventEmitter#method_prependoncelistener_0)
-   [rawListeners](././events/~/EventEmitter#method_rawlisteners_0)
-   [removeAllListeners](././events/~/EventEmitter#method_removealllisteners_0)
-   [removeListener](././events/~/EventEmitter#method_removelistener_0)
-   [setMaxListeners](././events/~/EventEmitter#method_setmaxlisteners_0)

I

[EventEmitter.Abortable](././events/~/EventEmitter.Abortable "EventEmitter.Abortable")

No documentation available

-   [signal](././events/~/EventEmitter.Abortable#property_signal)

c

[EventEmitter.EventEmitterAsyncResource](././events/~/EventEmitter.EventEmitterAsyncResource "EventEmitter.EventEmitterAsyncResource")

Integrates `EventEmitter` with `AsyncResource` for `EventEmitter`s that require manual async tracking. Specifically, all events emitted by instances of `events.EventEmitterAsyncResource` will run within its `async context`.

-   [asyncId](././events/~/EventEmitter.EventEmitterAsyncResource#property_asyncid)
-   [asyncResource](././events/~/EventEmitter.EventEmitterAsyncResource#property_asyncresource)
-   [emitDestroy](././events/~/EventEmitter.EventEmitterAsyncResource#method_emitdestroy_0)
-   [triggerAsyncId](././events/~/EventEmitter.EventEmitterAsyncResource#property_triggerasyncid)

I

[EventEmitter.EventEmitterAsyncResourceOptions](././events/~/EventEmitter.EventEmitterAsyncResourceOptions "EventEmitter.EventEmitterAsyncResourceOptions")

No documentation available

-   [name](././events/~/EventEmitter.EventEmitterAsyncResourceOptions#property_name)

I

[EventEmitter.EventEmitterReferencingAsyncResource](././events/~/EventEmitter.EventEmitterReferencingAsyncResource "EventEmitter.EventEmitterReferencingAsyncResource")

No documentation available

-   [eventEmitter](././events/~/EventEmitter.EventEmitterReferencingAsyncResource#property_eventemitter)

I

[EventEmitterOptions](././events/~/EventEmitterOptions "EventEmitterOptions")

No documentation available

-   [captureRejections](././events/~/EventEmitterOptions#property_capturerejections)

T

[EventMap](././events/~/EventMap "EventMap")

No documentation available

T

[Key](././events/~/Key "Key")

No documentation available

T

[Key2](././events/~/Key2 "Key2")

No documentation available

T

[Listener](././events/~/Listener "Listener")

No documentation available

T

[Listener1](././events/~/Listener1 "Listener1")

No documentation available

T

[Listener2](././events/~/Listener2 "Listener2")

No documentation available

I

[StaticEventEmitterIteratorOptions](././events/~/StaticEventEmitterIteratorOptions "StaticEventEmitterIteratorOptions")

No documentation available

-   [close](././events/~/StaticEventEmitterIteratorOptions#property_close)
-   [highWaterMark](././events/~/StaticEventEmitterIteratorOptions#property_highwatermark)
-   [lowWaterMark](././events/~/StaticEventEmitterIteratorOptions#property_lowwatermark)

I

[StaticEventEmitterOptions](././events/~/StaticEventEmitterOptions "StaticEventEmitterOptions")

No documentation available

-   [signal](././events/~/StaticEventEmitterOptions#property_signal)

The `node:fs` module enables interacting with the file system in a way modeled on standard POSIX functions.

I

[\_GlobOptions](././fs/~/_GlobOptions "_GlobOptions")

No documentation available

-   [cwd](././fs/~/_GlobOptions#property_cwd)
-   [exclude](././fs/~/_GlobOptions#property_exclude)
-   [withFileTypes](././fs/~/_GlobOptions#property_withfiletypes)

f

[access](././fs/~/access "access")

Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for possible values of `mode`.

f

[accessSync](././fs/~/accessSync "accessSync")

Synchronously tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for possible values of `mode`.

f

[appendFile](././fs/~/appendFile "appendFile")

Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `Buffer`.

f

[appendFileSync](././fs/~/appendFileSync "appendFileSync")

Synchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `Buffer`.

I

[BigIntOptions](././fs/~/BigIntOptions "BigIntOptions")

No documentation available

-   [bigint](././fs/~/BigIntOptions#property_bigint)

I

[BigIntStats](././fs/~/BigIntStats "BigIntStats")

No documentation available

-   [atimeNs](././fs/~/BigIntStats#property_atimens)
-   [birthtimeNs](././fs/~/BigIntStats#property_birthtimens)
-   [ctimeNs](././fs/~/BigIntStats#property_ctimens)
-   [mtimeNs](././fs/~/BigIntStats#property_mtimens)

I

[BigIntStatsFs](././fs/~/BigIntStatsFs "BigIntStatsFs")

No documentation available

T

[BigIntStatsListener](././fs/~/BigIntStatsListener "BigIntStatsListener")

No documentation available

T

[BufferEncodingOption](././fs/~/BufferEncodingOption "BufferEncodingOption")

No documentation available

f

[chmod](././fs/~/chmod "chmod")

Asynchronously changes the permissions of a file. No arguments other than a possible exception are given to the completion callback.

f

[chmodSync](././fs/~/chmodSync "chmodSync")

For detailed information, see the documentation of the asynchronous version of this API: [chmod](././fs/~/chmod).

f

[chown](././fs/~/chown "chown")

Asynchronously changes owner and group of a file. No arguments other than a possible exception are given to the completion callback.

f

[chownSync](././fs/~/chownSync "chownSync")

Synchronously changes owner and group of a file. Returns `undefined`. This is the synchronous version of [chown](././fs/~/chown).

f

[close](././fs/~/close "close")

Closes the file descriptor. No arguments other than a possible exception are given to the completion callback.

f

[closeSync](././fs/~/closeSync "closeSync")

Closes the file descriptor. Returns `undefined`.

N

[constants](././fs/~/constants "constants")

No documentation available

v

[constants.COPYFILE\_EXCL](././fs/~/constants.COPYFILE_EXCL "constants.COPYFILE_EXCL")

Constant for fs.copyFile. Flag indicating the destination file should not be overwritten if it already exists.

v

[constants.COPYFILE\_FICLONE](././fs/~/constants.COPYFILE_FICLONE "constants.COPYFILE_FICLONE")

Constant for fs.copyFile. copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then a fallback copy mechanism is used.

v

[constants.COPYFILE\_FICLONE\_FORCE](././fs/~/constants.COPYFILE_FICLONE_FORCE "constants.COPYFILE_FICLONE_FORCE")

Constant for fs.copyFile. Copy operation will attempt to create a copy-on-write reflink. If the underlying platform does not support copy-on-write, then the operation will fail with an error.

v

[constants.F\_OK](././fs/~/constants.F_OK "constants.F_OK")

Constant for fs.access(). File is visible to the calling process.

v

[constants.O\_APPEND](././fs/~/constants.O_APPEND "constants.O_APPEND")

Constant for fs.open(). Flag indicating that data will be appended to the end of the file.

v

[constants.O\_CREAT](././fs/~/constants.O_CREAT "constants.O_CREAT")

Constant for fs.open(). Flag indicating to create the file if it does not already exist.

v

[constants.O\_DIRECT](././fs/~/constants.O_DIRECT "constants.O_DIRECT")

Constant for fs.open(). When set, an attempt will be made to minimize caching effects of file I/O.

v

[constants.O\_DIRECTORY](././fs/~/constants.O_DIRECTORY "constants.O_DIRECTORY")

Constant for fs.open(). Flag indicating that the open should fail if the path is not a directory.

v

[constants.O\_DSYNC](././fs/~/constants.O_DSYNC "constants.O_DSYNC")

Constant for fs.open(). Flag indicating that the file is opened for synchronous I/O with write operations waiting for data integrity.

v

[constants.O\_EXCL](././fs/~/constants.O_EXCL "constants.O_EXCL")

Constant for fs.open(). Flag indicating that opening a file should fail if the O\_CREAT flag is set and the file already exists.

v

[constants.O\_NOATIME](././fs/~/constants.O_NOATIME "constants.O_NOATIME")

constant for fs.open(). Flag indicating reading accesses to the file system will no longer result in an update to the atime information associated with the file. This flag is available on Linux operating systems only.

v

[constants.O\_NOCTTY](././fs/~/constants.O_NOCTTY "constants.O_NOCTTY")

Constant for fs.open(). Flag indicating that if path identifies a terminal device, opening the path shall not cause that terminal to become the controlling terminal for the process (if the process does not already have one).

v

[constants.O\_NOFOLLOW](././fs/~/constants.O_NOFOLLOW "constants.O_NOFOLLOW")

Constant for fs.open(). Flag indicating that the open should fail if the path is a symbolic link.

v

[constants.O\_NONBLOCK](././fs/~/constants.O_NONBLOCK "constants.O_NONBLOCK")

Constant for fs.open(). Flag indicating to open the file in nonblocking mode when possible.

v

[constants.O\_RDONLY](././fs/~/constants.O_RDONLY "constants.O_RDONLY")

Constant for fs.open(). Flag indicating to open a file for read-only access.

v

[constants.O\_RDWR](././fs/~/constants.O_RDWR "constants.O_RDWR")

Constant for fs.open(). Flag indicating to open a file for read-write access.

v

[constants.O\_SYMLINK](././fs/~/constants.O_SYMLINK "constants.O_SYMLINK")

Constant for fs.open(). Flag indicating to open the symbolic link itself rather than the resource it is pointing to.

v

[constants.O\_SYNC](././fs/~/constants.O_SYNC "constants.O_SYNC")

Constant for fs.open(). Flag indicating that the file is opened for synchronous I/O.

v

[constants.O\_TRUNC](././fs/~/constants.O_TRUNC "constants.O_TRUNC")

Constant for fs.open(). Flag indicating that if the file exists and is a regular file, and the file is opened successfully for write access, its length shall be truncated to zero.

v

[constants.O\_WRONLY](././fs/~/constants.O_WRONLY "constants.O_WRONLY")

Constant for fs.open(). Flag indicating to open a file for write-only access.

v

[constants.R\_OK](././fs/~/constants.R_OK "constants.R_OK")

Constant for fs.access(). File can be read by the calling process.

v

[constants.S\_IFBLK](././fs/~/constants.S_IFBLK "constants.S_IFBLK")

Constant for fs.Stats mode property for determining a file's type. File type constant for a block-oriented device file.

v

[constants.S\_IFCHR](././fs/~/constants.S_IFCHR "constants.S_IFCHR")

Constant for fs.Stats mode property for determining a file's type. File type constant for a character-oriented device file.

v

[constants.S\_IFDIR](././fs/~/constants.S_IFDIR "constants.S_IFDIR")

Constant for fs.Stats mode property for determining a file's type. File type constant for a directory.

v

[constants.S\_IFIFO](././fs/~/constants.S_IFIFO "constants.S_IFIFO")

Constant for fs.Stats mode property for determining a file's type. File type constant for a FIFO/pipe.

v

[constants.S\_IFLNK](././fs/~/constants.S_IFLNK "constants.S_IFLNK")

Constant for fs.Stats mode property for determining a file's type. File type constant for a symbolic link.

v

[constants.S\_IFMT](././fs/~/constants.S_IFMT "constants.S_IFMT")

Constant for fs.Stats mode property for determining a file's type. Bit mask used to extract the file type code.

v

[constants.S\_IFREG](././fs/~/constants.S_IFREG "constants.S_IFREG")

Constant for fs.Stats mode property for determining a file's type. File type constant for a regular file.

v

[constants.S\_IFSOCK](././fs/~/constants.S_IFSOCK "constants.S_IFSOCK")

Constant for fs.Stats mode property for determining a file's type. File type constant for a socket.

v

[constants.S\_IRGRP](././fs/~/constants.S_IRGRP "constants.S_IRGRP")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable by group.

v

[constants.S\_IROTH](././fs/~/constants.S_IROTH "constants.S_IROTH")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable by others.

v

[constants.S\_IRUSR](././fs/~/constants.S_IRUSR "constants.S_IRUSR")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable by owner.

v

[constants.S\_IRWXG](././fs/~/constants.S_IRWXG "constants.S_IRWXG")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable, writable and executable by group.

v

[constants.S\_IRWXO](././fs/~/constants.S_IRWXO "constants.S_IRWXO")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable, writable and executable by others.

v

[constants.S\_IRWXU](././fs/~/constants.S_IRWXU "constants.S_IRWXU")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating readable, writable and executable by owner.

v

[constants.S\_IWGRP](././fs/~/constants.S_IWGRP "constants.S_IWGRP")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating writable by group.

v

[constants.S\_IWOTH](././fs/~/constants.S_IWOTH "constants.S_IWOTH")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating writable by others.

v

[constants.S\_IWUSR](././fs/~/constants.S_IWUSR "constants.S_IWUSR")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating writable by owner.

v

[constants.S\_IXGRP](././fs/~/constants.S_IXGRP "constants.S_IXGRP")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating executable by group.

v

[constants.S\_IXOTH](././fs/~/constants.S_IXOTH "constants.S_IXOTH")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating executable by others.

v

[constants.S\_IXUSR](././fs/~/constants.S_IXUSR "constants.S_IXUSR")

Constant for fs.Stats mode property for determining access permissions for a file. File mode indicating executable by owner.

v

[constants.UV\_FS\_O\_FILEMAP](././fs/~/constants.UV_FS_O_FILEMAP "constants.UV_FS_O_FILEMAP")

When set, a memory file mapping is used to access the file. This flag is available on Windows operating systems only. On other operating systems, this flag is ignored.

v

[constants.W\_OK](././fs/~/constants.W_OK "constants.W_OK")

Constant for fs.access(). File can be written by the calling process.

v

[constants.X\_OK](././fs/~/constants.X_OK "constants.X_OK")

Constant for fs.access(). File can be executed by the calling process.

f

[copyFile](././fs/~/copyFile "copyFile")

Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. No arguments other than a possible exception are given to the callback function. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.

f

[copyFileSync](././fs/~/copyFileSync "copyFileSync")

Synchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. Returns `undefined`. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.

I

[CopyOptions](././fs/~/CopyOptions "CopyOptions")

No documentation available

-   [filter](././fs/~/CopyOptions#method_filter_0)

I

[CopyOptionsBase](././fs/~/CopyOptionsBase "CopyOptionsBase")

No documentation available

-   [dereference](././fs/~/CopyOptionsBase#property_dereference)
-   [errorOnExist](././fs/~/CopyOptionsBase#property_erroronexist)
-   [force](././fs/~/CopyOptionsBase#property_force)
-   [mode](././fs/~/CopyOptionsBase#property_mode)
-   [preserveTimestamps](././fs/~/CopyOptionsBase#property_preservetimestamps)
-   [recursive](././fs/~/CopyOptionsBase#property_recursive)
-   [verbatimSymlinks](././fs/~/CopyOptionsBase#property_verbatimsymlinks)

I

[CopySyncOptions](././fs/~/CopySyncOptions "CopySyncOptions")

No documentation available

-   [filter](././fs/~/CopySyncOptions#method_filter_0)

f

[cp](././fs/~/cp "cp")

Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

f

[cpSync](././fs/~/cpSync "cpSync")

Synchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

f

[createReadStream](././fs/~/createReadStream "createReadStream")

`options` can include `start` and `end` values to read a range of bytes from the file instead of the entire file. Both `start` and `end` are inclusive and start counting at 0, allowed values are in the \[0, [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)\] range. If `fd` is specified and `start` is omitted or `undefined`, `fs.createReadStream()` reads sequentially from the current file position. The `encoding` can be any one of those accepted by `Buffer`.

I

[CreateReadStreamFSImplementation](././fs/~/CreateReadStreamFSImplementation "CreateReadStreamFSImplementation")

No documentation available

-   [read](././fs/~/CreateReadStreamFSImplementation#property_read)

f

[createWriteStream](././fs/~/createWriteStream "createWriteStream")

`options` may also include a `start` option to allow writing data at some position past the beginning of the file, allowed values are in the \[0, [`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)\] range. Modifying a file rather than replacing it may require the `flags` option to be set to `r+` rather than the default `w`. The `encoding` can be any one of those accepted by `Buffer`.

I

[CreateWriteStreamFSImplementation](././fs/~/CreateWriteStreamFSImplementation "CreateWriteStreamFSImplementation")

No documentation available

-   [write](././fs/~/CreateWriteStreamFSImplementation#property_write)
-   [writev](././fs/~/CreateWriteStreamFSImplementation#property_writev)

T

[CustomEvents](././fs/~/CustomEvents "CustomEvents")

string & {} allows to allow any kind of strings for the event but still allows to have auto completion for the normal events.

c

[Dir](././fs/~/Dir "Dir")

A class representing a directory stream.

-   [close](././fs/~/Dir#method_close_0)
-   [closeSync](././fs/~/Dir#method_closesync_0)
-   [path](././fs/~/Dir#property_path)
-   [read](././fs/~/Dir#method_read_0)
-   [readSync](././fs/~/Dir#method_readsync_0)

c

[Dirent](././fs/~/Dirent "Dirent")

A representation of a directory entry, which can be a file or a subdirectory within the directory, as returned by reading from an `fs.Dir`. The directory entry is a combination of the file name and file type pairs.

-   [isBlockDevice](././fs/~/Dirent#method_isblockdevice_0)
-   [isCharacterDevice](././fs/~/Dirent#method_ischaracterdevice_0)
-   [isDirectory](././fs/~/Dirent#method_isdirectory_0)
-   [isFIFO](././fs/~/Dirent#method_isfifo_0)
-   [isFile](././fs/~/Dirent#method_isfile_0)
-   [isSocket](././fs/~/Dirent#method_issocket_0)
-   [isSymbolicLink](././fs/~/Dirent#method_issymboliclink_0)
-   [name](././fs/~/Dirent#property_name)
-   [parentPath](././fs/~/Dirent#property_parentpath)
-   [path](././fs/~/Dirent#property_path)

T

[EncodingOption](././fs/~/EncodingOption "EncodingOption")

No documentation available

f

[existsSync](././fs/~/existsSync "existsSync")

Returns `true` if the path exists, `false` otherwise.

f

[fchmod](././fs/~/fchmod "fchmod")

Sets the permissions on the file. No arguments other than a possible exception are given to the completion callback.

f

[fchmodSync](././fs/~/fchmodSync "fchmodSync")

Sets the permissions on the file. Returns `undefined`.

f

[fchown](././fs/~/fchown "fchown")

Sets the owner of the file. No arguments other than a possible exception are given to the completion callback.

f

[fchownSync](././fs/~/fchownSync "fchownSync")

Sets the owner of the file. Returns `undefined`.

f

[fdatasync](././fs/~/fdatasync "fdatasync")

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX [`fdatasync(2)`](http://man7.org/linux/man-pages/man2/fdatasync.2.html) documentation for details. No arguments other than a possible exception are given to the completion callback.

f

[fdatasyncSync](././fs/~/fdatasyncSync "fdatasyncSync")

Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX [`fdatasync(2)`](http://man7.org/linux/man-pages/man2/fdatasync.2.html) documentation for details. Returns `undefined`.

I

[FSImplementation](././fs/~/FSImplementation "FSImplementation")

No documentation available

-   [close](././fs/~/FSImplementation#property_close)
-   [open](././fs/~/FSImplementation#property_open)

f

[fstat](././fs/~/fstat "fstat")

Invokes the callback with the `fs.Stats` for the file descriptor.

f

[fstatSync](././fs/~/fstatSync "fstatSync")

Retrieves the `fs.Stats` for the file descriptor.

I

[FSWatcher](././fs/~/FSWatcher "FSWatcher")

No documentation available

-   [addListener](././fs/~/FSWatcher#method_addlistener_0)
-   [close](././fs/~/FSWatcher#method_close_0)
-   [on](././fs/~/FSWatcher#method_on_0)
-   [once](././fs/~/FSWatcher#method_once_0)
-   [prependListener](././fs/~/FSWatcher#method_prependlistener_0)
-   [prependOnceListener](././fs/~/FSWatcher#method_prependoncelistener_0)
-   [ref](././fs/~/FSWatcher#method_ref_0)
-   [unref](././fs/~/FSWatcher#method_unref_0)

f

[fsync](././fs/~/fsync "fsync")

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX [`fsync(2)`](http://man7.org/linux/man-pages/man2/fsync.2.html) documentation for more detail. No arguments other than a possible exception are given to the completion callback.

f

[fsyncSync](././fs/~/fsyncSync "fsyncSync")

Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX [`fsync(2)`](http://man7.org/linux/man-pages/man2/fsync.2.html) documentation for more detail. Returns `undefined`.

f

[ftruncate](././fs/~/ftruncate "ftruncate")

Truncates the file descriptor. No arguments other than a possible exception are given to the completion callback.

f

[ftruncateSync](././fs/~/ftruncateSync "ftruncateSync")

Truncates the file descriptor. Returns `undefined`.

f

[futimes](././fs/~/futimes "futimes")

Change the file system timestamps of the object referenced by the supplied file descriptor. See [utimes](././fs/~/utimes).

f

[futimesSync](././fs/~/futimesSync "futimesSync")

Synchronous version of [futimes](././fs/~/futimes). Returns `undefined`.

f

[glob](././fs/~/glob "glob")

Retrieves the files matching the specified pattern.

I

[GlobOptions](././fs/~/GlobOptions "GlobOptions")

No documentation available

I

[GlobOptionsWithFileTypes](././fs/~/GlobOptionsWithFileTypes "GlobOptionsWithFileTypes")

No documentation available

-   [withFileTypes](././fs/~/GlobOptionsWithFileTypes#property_withfiletypes)

I

[GlobOptionsWithoutFileTypes](././fs/~/GlobOptionsWithoutFileTypes "GlobOptionsWithoutFileTypes")

No documentation available

-   [withFileTypes](././fs/~/GlobOptionsWithoutFileTypes#property_withfiletypes)

f

[globSync](././fs/~/globSync "globSync")

Retrieves the files matching the specified pattern.

f

[lchown](././fs/~/lchown "lchown")

Set the owner of the symbolic link. No arguments other than a possible exception are given to the completion callback.

f

[lchownSync](././fs/~/lchownSync "lchownSync")

Set the owner for the path. Returns `undefined`.

f

[link](././fs/~/link "link")

Creates a new link from the `existingPath` to the `newPath`. See the POSIX [`link(2)`](http://man7.org/linux/man-pages/man2/link.2.html) documentation for more detail. No arguments other than a possible exception are given to the completion callback.

f

[linkSync](././fs/~/linkSync "linkSync")

Creates a new link from the `existingPath` to the `newPath`. See the POSIX [`link(2)`](http://man7.org/linux/man-pages/man2/link.2.html) documentation for more detail. Returns `undefined`.

f

[lstat](././fs/~/lstat "lstat")

Retrieves the `fs.Stats` for the symbolic link referred to by the path. The callback gets two arguments `(err, stats)` where `stats` is a `fs.Stats` object. `lstat()` is identical to `stat()`, except that if `path` is a symbolic link, then the link itself is stat-ed, not the file that it refers to.

v

[lstatSync](././fs/~/lstatSync "lstatSync")

Synchronous lstat(2) - Get file status. Does not dereference symbolic links.

f

[lutimes](././fs/~/lutimes "lutimes")

Changes the access and modification times of a file in the same way as [utimes](././fs/~/utimes), with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.

f

[lutimesSync](././fs/~/lutimesSync "lutimesSync")

Change the file system timestamps of the symbolic link referenced by `path`. Returns `undefined`, or throws an exception when parameters are incorrect or the operation fails. This is the synchronous version of [lutimes](././fs/~/lutimes).

I

[MakeDirectoryOptions](././fs/~/MakeDirectoryOptions "MakeDirectoryOptions")

No documentation available

-   [mode](././fs/~/MakeDirectoryOptions#property_mode)
-   [recursive](././fs/~/MakeDirectoryOptions#property_recursive)

f

[mkdir](././fs/~/mkdir "mkdir")

Asynchronously creates a directory.

f

[mkdirSync](././fs/~/mkdirSync "mkdirSync")

Synchronously creates a directory. Returns `undefined`, or if `recursive` is `true`, the first directory path created. This is the synchronous version of [mkdir](././fs/~/mkdir).

f

[mkdtemp](././fs/~/mkdtemp "mkdtemp")

Creates a unique temporary directory.

f

[mkdtempSync](././fs/~/mkdtempSync "mkdtempSync")

Returns the created directory path.

T

[Mode](././fs/~/Mode "Mode")

No documentation available

T

[NoParamCallback](././fs/~/NoParamCallback "NoParamCallback")

No documentation available

I

[ObjectEncodingOptions](././fs/~/ObjectEncodingOptions "ObjectEncodingOptions")

No documentation available

-   [encoding](././fs/~/ObjectEncodingOptions#property_encoding)

f

[open](././fs/~/open "open")

Asynchronous file open. See the POSIX [`open(2)`](http://man7.org/linux/man-pages/man2/open.2.html) documentation for more details.

f

[openAsBlob](././fs/~/openAsBlob "openAsBlob")

Returns a `Blob` whose data is backed by the given file.

I

[OpenAsBlobOptions](././fs/~/OpenAsBlobOptions "OpenAsBlobOptions")

No documentation available

-   [type](././fs/~/OpenAsBlobOptions#property_type)

f

[opendir](././fs/~/opendir "opendir")

Asynchronously open a directory. See the POSIX [`opendir(3)`](http://man7.org/linux/man-pages/man3/opendir.3.html) documentation for more details.

I

[OpenDirOptions](././fs/~/OpenDirOptions "OpenDirOptions")

No documentation available

-   [bufferSize](././fs/~/OpenDirOptions#property_buffersize)
-   [encoding](././fs/~/OpenDirOptions#property_encoding)
-   [recursive](././fs/~/OpenDirOptions#property_recursive)

f

[opendirSync](././fs/~/opendirSync "opendirSync")

Synchronously open a directory. See [`opendir(3)`](http://man7.org/linux/man-pages/man3/opendir.3.html).

T

[OpenMode](././fs/~/OpenMode "OpenMode")

No documentation available

f

[openSync](././fs/~/openSync "openSync")

Returns an integer representing the file descriptor.

T

[PathLike](././fs/~/PathLike "PathLike")

Valid types for path values in "fs".

T

[PathOrFileDescriptor](././fs/~/PathOrFileDescriptor "PathOrFileDescriptor")

No documentation available

N

[promises](././fs/~/promises "promises")

The `fs/promises` API provides asynchronous file system methods that return promises.

f

[read](././fs/~/read "read")

Read data from the file specified by `fd`.

I

[ReadAsyncOptions](././fs/~/ReadAsyncOptions "ReadAsyncOptions")

No documentation available

-   [buffer](././fs/~/ReadAsyncOptions#property_buffer)

f

[readdir](././fs/~/readdir "readdir")

Reads the contents of a directory. The callback gets two arguments `(err, files)` where `files` is an array of the names of the files in the directory excluding `'.'` and `'..'`.

f

[readdirSync](././fs/~/readdirSync "readdirSync")

Reads the contents of the directory.

f

[readFile](././fs/~/readFile "readFile")

Asynchronously reads the entire contents of a file.

f

[readFileSync](././fs/~/readFileSync "readFileSync")

Returns the contents of the `path`.

f

[readlink](././fs/~/readlink "readlink")

Reads the contents of the symbolic link referred to by `path`. The callback gets two arguments `(err, linkString)`.

f

[readlinkSync](././fs/~/readlinkSync "readlinkSync")

Returns the symbolic link's string value.

T

[ReadPosition](././fs/~/ReadPosition "ReadPosition")

No documentation available

c

[ReadStream](././fs/~/ReadStream "ReadStream")

Instances of `fs.ReadStream` are created and returned using the [createReadStream](././fs/~/createReadStream) function.

-   [addListener](././fs/~/ReadStream#method_addlistener_0)
-   [bytesRead](././fs/~/ReadStream#property_bytesread)
-   [close](././fs/~/ReadStream#method_close_0)
-   [on](././fs/~/ReadStream#method_on_0)
-   [once](././fs/~/ReadStream#method_once_0)
-   [path](././fs/~/ReadStream#property_path)
-   [pending](././fs/~/ReadStream#property_pending)
-   [prependListener](././fs/~/ReadStream#method_prependlistener_0)
-   [prependOnceListener](././fs/~/ReadStream#method_prependoncelistener_0)

T

[ReadStreamEvents](././fs/~/ReadStreamEvents "ReadStreamEvents")

The Keys are events of the ReadStream and the values are the functions that are called when the event is emitted.

I

[ReadStreamOptions](././fs/~/ReadStreamOptions "ReadStreamOptions")

No documentation available

-   [end](././fs/~/ReadStreamOptions#property_end)
-   [fs](././fs/~/ReadStreamOptions#property_fs)

f

[readSync](././fs/~/readSync "readSync")

Returns the number of `bytesRead`.

I

[ReadSyncOptions](././fs/~/ReadSyncOptions "ReadSyncOptions")

No documentation available

-   [length](././fs/~/ReadSyncOptions#property_length)
-   [offset](././fs/~/ReadSyncOptions#property_offset)
-   [position](././fs/~/ReadSyncOptions#property_position)

f

[readv](././fs/~/readv "readv")

Read from a file specified by `fd` and write to an array of `ArrayBufferView`s using `readv()`.

I

[ReadVResult](././fs/~/ReadVResult "ReadVResult")

No documentation available

-   [buffers](././fs/~/ReadVResult#property_buffers)
-   [bytesRead](././fs/~/ReadVResult#property_bytesread)

f

[readvSync](././fs/~/readvSync "readvSync")

For detailed information, see the documentation of the asynchronous version of this API: [readv](././fs/~/readv).

f

N

[realpath](././fs/~/realpath "realpath")

Asynchronously computes the canonical pathname by resolving `.`, `..`, and symbolic links.

f

[realpath.native](././fs/~/realpath.native "realpath.native")

Asynchronous [`realpath(3)`](http://man7.org/linux/man-pages/man3/realpath.3.html).

f

N

[realpathSync](././fs/~/realpathSync "realpathSync")

Returns the resolved pathname.

f

[realpathSync.native](././fs/~/realpathSync.native "realpathSync.native")

No documentation available

f

[rename](././fs/~/rename "rename")

Asynchronously rename file at `oldPath` to the pathname provided as `newPath`. In the case that `newPath` already exists, it will be overwritten. If there is a directory at `newPath`, an error will be raised instead. No arguments other than a possible exception are given to the completion callback.

f

[renameSync](././fs/~/renameSync "renameSync")

Renames the file from `oldPath` to `newPath`. Returns `undefined`.

f

[rm](././fs/~/rm "rm")

Asynchronously removes files and directories (modeled on the standard POSIX `rm` utility). No arguments other than a possible exception are given to the completion callback.

f

[rmdir](././fs/~/rmdir "rmdir")

Asynchronous [`rmdir(2)`](http://man7.org/linux/man-pages/man2/rmdir.2.html). No arguments other than a possible exception are given to the completion callback.

I

[RmDirOptions](././fs/~/RmDirOptions "RmDirOptions")

No documentation available

-   [maxRetries](././fs/~/RmDirOptions#property_maxretries)
-   [recursive](././fs/~/RmDirOptions#property_recursive)
-   [retryDelay](././fs/~/RmDirOptions#property_retrydelay)

f

[rmdirSync](././fs/~/rmdirSync "rmdirSync")

Synchronous [`rmdir(2)`](http://man7.org/linux/man-pages/man2/rmdir.2.html). Returns `undefined`.

I

[RmOptions](././fs/~/RmOptions "RmOptions")

No documentation available

-   [force](././fs/~/RmOptions#property_force)
-   [maxRetries](././fs/~/RmOptions#property_maxretries)
-   [recursive](././fs/~/RmOptions#property_recursive)
-   [retryDelay](././fs/~/RmOptions#property_retrydelay)

f

[rmSync](././fs/~/rmSync "rmSync")

Synchronously removes files and directories (modeled on the standard POSIX `rm` utility). Returns `undefined`.

f

[stat](././fs/~/stat "stat")

Asynchronous [`stat(2)`](http://man7.org/linux/man-pages/man2/stat.2.html). The callback gets two arguments `(err, stats)` where`stats` is an `fs.Stats` object.

f

[statfs](././fs/~/statfs "statfs")

Asynchronous [`statfs(2)`](http://man7.org/linux/man-pages/man2/statfs.2.html). Returns information about the mounted file system which contains `path`. The callback gets two arguments `(err, stats)` where `stats`is an `fs.StatFs` object.

I

[StatFsOptions](././fs/~/StatFsOptions "StatFsOptions")

No documentation available

-   [bigint](././fs/~/StatFsOptions#property_bigint)

f

[statfsSync](././fs/~/statfsSync "statfsSync")

Synchronous [`statfs(2)`](http://man7.org/linux/man-pages/man2/statfs.2.html). Returns information about the mounted file system which contains `path`.

I

[StatOptions](././fs/~/StatOptions "StatOptions")

No documentation available

-   [bigint](././fs/~/StatOptions#property_bigint)

c

I

[Stats](././fs/~/Stats "Stats")

A `fs.Stats` object provides information about a file.

I

[StatsBase](././fs/~/StatsBase "StatsBase")

No documentation available

-   [atime](././fs/~/StatsBase#property_atime)
-   [atimeMs](././fs/~/StatsBase#property_atimems)
-   [birthtime](././fs/~/StatsBase#property_birthtime)
-   [birthtimeMs](././fs/~/StatsBase#property_birthtimems)
-   [blksize](././fs/~/StatsBase#property_blksize)
-   [blocks](././fs/~/StatsBase#property_blocks)
-   [ctime](././fs/~/StatsBase#property_ctime)
-   [ctimeMs](././fs/~/StatsBase#property_ctimems)
-   [dev](././fs/~/StatsBase#property_dev)
-   [gid](././fs/~/StatsBase#property_gid)
-   [ino](././fs/~/StatsBase#property_ino)
-   [isBlockDevice](././fs/~/StatsBase#method_isblockdevice_0)
-   [isCharacterDevice](././fs/~/StatsBase#method_ischaracterdevice_0)
-   [isDirectory](././fs/~/StatsBase#method_isdirectory_0)
-   [isFIFO](././fs/~/StatsBase#method_isfifo_0)
-   [isFile](././fs/~/StatsBase#method_isfile_0)
-   [isSocket](././fs/~/StatsBase#method_issocket_0)
-   [isSymbolicLink](././fs/~/StatsBase#method_issymboliclink_0)
-   [mode](././fs/~/StatsBase#property_mode)
-   [mtime](././fs/~/StatsBase#property_mtime)
-   [mtimeMs](././fs/~/StatsBase#property_mtimems)
-   [nlink](././fs/~/StatsBase#property_nlink)
-   [rdev](././fs/~/StatsBase#property_rdev)
-   [size](././fs/~/StatsBase#property_size)
-   [uid](././fs/~/StatsBase#property_uid)

c

I

[StatsFs](././fs/~/StatsFs "StatsFs")

Provides information about a mounted file system.

I

[StatsFsBase](././fs/~/StatsFsBase "StatsFsBase")

No documentation available

-   [bavail](././fs/~/StatsFsBase#property_bavail)
-   [bfree](././fs/~/StatsFsBase#property_bfree)
-   [blocks](././fs/~/StatsFsBase#property_blocks)
-   [bsize](././fs/~/StatsFsBase#property_bsize)
-   [ffree](././fs/~/StatsFsBase#property_ffree)
-   [files](././fs/~/StatsFsBase#property_files)
-   [type](././fs/~/StatsFsBase#property_type)

T

[StatsListener](././fs/~/StatsListener "StatsListener")

No documentation available

v

[statSync](././fs/~/statSync "statSync")

Synchronous stat(2) - Get file status.

I

[StatSyncFn](././fs/~/StatSyncFn "StatSyncFn")

No documentation available

I

[StatSyncOptions](././fs/~/StatSyncOptions "StatSyncOptions")

No documentation available

-   [throwIfNoEntry](././fs/~/StatSyncOptions#property_throwifnoentry)

I

[StatWatcher](././fs/~/StatWatcher "StatWatcher")

Class: fs.StatWatcher

-   [ref](././fs/~/StatWatcher#method_ref_0)
-   [unref](././fs/~/StatWatcher#method_unref_0)

I

[StreamOptions](././fs/~/StreamOptions "StreamOptions")

No documentation available

-   [autoClose](././fs/~/StreamOptions#property_autoclose)
-   [emitClose](././fs/~/StreamOptions#property_emitclose)
-   [encoding](././fs/~/StreamOptions#property_encoding)
-   [fd](././fs/~/StreamOptions#property_fd)
-   [flags](././fs/~/StreamOptions#property_flags)
-   [highWaterMark](././fs/~/StreamOptions#property_highwatermark)
-   [mode](././fs/~/StreamOptions#property_mode)
-   [signal](././fs/~/StreamOptions#property_signal)
-   [start](././fs/~/StreamOptions#property_start)

f

N

[symlink](././fs/~/symlink "symlink")

Creates the link called `path` pointing to `target`. No arguments other than a possible exception are given to the completion callback.

T

[symlink.Type](././fs/~/symlink.Type "symlink.Type")

No documentation available

f

[symlinkSync](././fs/~/symlinkSync "symlinkSync")

Returns `undefined`.

T

[TimeLike](././fs/~/TimeLike "TimeLike")

No documentation available

f

[truncate](././fs/~/truncate "truncate")

Truncates the file. No arguments other than a possible exception are given to the completion callback. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncate()` is called.

f

[truncateSync](././fs/~/truncateSync "truncateSync")

Truncates the file. Returns `undefined`. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncateSync()` is called.

f

[unlink](././fs/~/unlink "unlink")

Asynchronously removes a file or symbolic link. No arguments other than a possible exception are given to the completion callback.

f

[unlinkSync](././fs/~/unlinkSync "unlinkSync")

Synchronous [`unlink(2)`](http://man7.org/linux/man-pages/man2/unlink.2.html). Returns `undefined`.

f

[unwatchFile](././fs/~/unwatchFile "unwatchFile")

Stop watching for changes on `filename`. If `listener` is specified, only that particular listener is removed. Otherwise, _all_ listeners are removed, effectively stopping watching of `filename`.

f

[utimes](././fs/~/utimes "utimes")

Change the file system timestamps of the object referenced by `path`.

f

[utimesSync](././fs/~/utimesSync "utimesSync")

Returns `undefined`.

f

[watch](././fs/~/watch "watch")

Watch for changes on `filename`, where `filename` is either a file or a directory.

T

[WatchEventType](././fs/~/WatchEventType "WatchEventType")

No documentation available

f

[watchFile](././fs/~/watchFile "watchFile")

Watch for changes on `filename`. The callback `listener` will be called each time the file is accessed.

I

[WatchFileOptions](././fs/~/WatchFileOptions "WatchFileOptions")

Watch for changes on `filename`. The callback `listener` will be called each time the file is accessed.

-   [bigint](././fs/~/WatchFileOptions#property_bigint)
-   [interval](././fs/~/WatchFileOptions#property_interval)
-   [persistent](././fs/~/WatchFileOptions#property_persistent)

T

[WatchListener](././fs/~/WatchListener "WatchListener")

No documentation available

I

[WatchOptions](././fs/~/WatchOptions "WatchOptions")

No documentation available

-   [encoding](././fs/~/WatchOptions#property_encoding)
-   [persistent](././fs/~/WatchOptions#property_persistent)
-   [recursive](././fs/~/WatchOptions#property_recursive)

f

[write](././fs/~/write "write")

Write `buffer` to the file specified by `fd`.

f

[writeFile](././fs/~/writeFile "writeFile")

No documentation available

T

[WriteFileOptions](././fs/~/WriteFileOptions "WriteFileOptions")

No documentation available

f

[writeFileSync](././fs/~/writeFileSync "writeFileSync")

No documentation available

c

[WriteStream](././fs/~/WriteStream "WriteStream")

-   Extends `stream.Writable`

-   [addListener](././fs/~/WriteStream#method_addlistener_0)
-   [bytesWritten](././fs/~/WriteStream#property_byteswritten)
-   [close](././fs/~/WriteStream#method_close_0)
-   [on](././fs/~/WriteStream#method_on_0)
-   [once](././fs/~/WriteStream#method_once_0)
-   [path](././fs/~/WriteStream#property_path)
-   [pending](././fs/~/WriteStream#property_pending)
-   [prependListener](././fs/~/WriteStream#method_prependlistener_0)
-   [prependOnceListener](././fs/~/WriteStream#method_prependoncelistener_0)

T

[WriteStreamEvents](././fs/~/WriteStreamEvents "WriteStreamEvents")

The Keys are events of the WriteStream and the values are the functions that are called when the event is emitted.

I

[WriteStreamOptions](././fs/~/WriteStreamOptions "WriteStreamOptions")

No documentation available

-   [flush](././fs/~/WriteStreamOptions#property_flush)
-   [fs](././fs/~/WriteStreamOptions#property_fs)

f

[writeSync](././fs/~/writeSync "writeSync")

For detailed information, see the documentation of the asynchronous version of this API: [write](././fs/~/write).

f

[writev](././fs/~/writev "writev")

Write an array of `ArrayBufferView`s to the file specified by `fd` using `writev()`.

I

[WriteVResult](././fs/~/WriteVResult "WriteVResult")

No documentation available

-   [buffers](././fs/~/WriteVResult#property_buffers)
-   [bytesWritten](././fs/~/WriteVResult#property_byteswritten)

f

[writevSync](././fs/~/writevSync "writevSync")

For detailed information, see the documentation of the asynchronous version of this API: [writev](././fs/~/writev).

f

[exists](././fs/~/exists "exists")

Test whether or not the given path exists by checking with the file system. Then call the `callback` argument with either true or false:

f

[lchmod](././fs/~/lchmod "lchmod")

Changes the permissions on a symbolic link. No arguments other than a possible exception are given to the completion callback.

f

[lchmodSync](././fs/~/lchmodSync "lchmodSync")

Changes the permissions on a symbolic link. Returns `undefined`.

The `fs/promises` API provides asynchronous file system methods that return promises.

f

[access](././fs/promises/~/access "access")

Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for possible values of `mode`.

f

[appendFile](././fs/promises/~/appendFile "appendFile")

Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `Buffer`.

f

[chmod](././fs/promises/~/chmod "chmod")

Changes the permissions of a file.

f

[chown](././fs/promises/~/chown "chown")

Changes the ownership of a file.

v

[constants](././fs/promises/~/constants "constants")

No documentation available

f

[copyFile](././fs/promises/~/copyFile "copyFile")

Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists.

f

[cp](././fs/promises/~/cp "cp")

Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

I

[CreateReadStreamOptions](././fs/promises/~/CreateReadStreamOptions "CreateReadStreamOptions")

No documentation available

-   [autoClose](././fs/promises/~/CreateReadStreamOptions#property_autoclose)
-   [emitClose](././fs/promises/~/CreateReadStreamOptions#property_emitclose)
-   [encoding](././fs/promises/~/CreateReadStreamOptions#property_encoding)
-   [end](././fs/promises/~/CreateReadStreamOptions#property_end)
-   [highWaterMark](././fs/promises/~/CreateReadStreamOptions#property_highwatermark)
-   [start](././fs/promises/~/CreateReadStreamOptions#property_start)

I

[CreateWriteStreamOptions](././fs/promises/~/CreateWriteStreamOptions "CreateWriteStreamOptions")

No documentation available

-   [autoClose](././fs/promises/~/CreateWriteStreamOptions#property_autoclose)
-   [emitClose](././fs/promises/~/CreateWriteStreamOptions#property_emitclose)
-   [encoding](././fs/promises/~/CreateWriteStreamOptions#property_encoding)
-   [flush](././fs/promises/~/CreateWriteStreamOptions#property_flush)
-   [highWaterMark](././fs/promises/~/CreateWriteStreamOptions#property_highwatermark)
-   [start](././fs/promises/~/CreateWriteStreamOptions#property_start)

I

[FileChangeInfo](././fs/promises/~/FileChangeInfo "FileChangeInfo")

No documentation available

-   [eventType](././fs/promises/~/FileChangeInfo#property_eventtype)
-   [filename](././fs/promises/~/FileChangeInfo#property_filename)

I

[FileHandle](././fs/promises/~/FileHandle "FileHandle")

No documentation available

-   [appendFile](././fs/promises/~/FileHandle#method_appendfile_0)
-   [chmod](././fs/promises/~/FileHandle#method_chmod_0)
-   [chown](././fs/promises/~/FileHandle#method_chown_0)
-   [close](././fs/promises/~/FileHandle#method_close_0)
-   [createReadStream](././fs/promises/~/FileHandle#method_createreadstream_0)
-   [createWriteStream](././fs/promises/~/FileHandle#method_createwritestream_0)
-   [datasync](././fs/promises/~/FileHandle#method_datasync_0)
-   [fd](././fs/promises/~/FileHandle#property_fd)
-   [read](././fs/promises/~/FileHandle#method_read_0)
-   [readFile](././fs/promises/~/FileHandle#method_readfile_0)
-   [readLines](././fs/promises/~/FileHandle#method_readlines_0)
-   [readableWebStream](././fs/promises/~/FileHandle#method_readablewebstream_0)
-   [readv](././fs/promises/~/FileHandle#method_readv_0)
-   [stat](././fs/promises/~/FileHandle#method_stat_0)
-   [sync](././fs/promises/~/FileHandle#method_sync_0)
-   [truncate](././fs/promises/~/FileHandle#method_truncate_0)
-   [utimes](././fs/promises/~/FileHandle#method_utimes_0)
-   [write](././fs/promises/~/FileHandle#method_write_0)
-   [writeFile](././fs/promises/~/FileHandle#method_writefile_0)
-   [writev](././fs/promises/~/FileHandle#method_writev_0)

I

[FileReadOptions](././fs/promises/~/FileReadOptions "FileReadOptions")

No documentation available

-   [buffer](././fs/promises/~/FileReadOptions#property_buffer)
-   [length](././fs/promises/~/FileReadOptions#property_length)
-   [offset](././fs/promises/~/FileReadOptions#property_offset)
-   [position](././fs/promises/~/FileReadOptions#property_position)

I

[FileReadResult](././fs/promises/~/FileReadResult "FileReadResult")

No documentation available

-   [buffer](././fs/promises/~/FileReadResult#property_buffer)
-   [bytesRead](././fs/promises/~/FileReadResult#property_bytesread)

I

[FlagAndOpenMode](././fs/promises/~/FlagAndOpenMode "FlagAndOpenMode")

No documentation available

-   [flag](././fs/promises/~/FlagAndOpenMode#property_flag)
-   [mode](././fs/promises/~/FlagAndOpenMode#property_mode)

f

[glob](././fs/promises/~/glob "glob")

Retrieves the files matching the specified pattern.

f

[lchown](././fs/promises/~/lchown "lchown")

Changes the ownership on a symbolic link.

f

[link](././fs/promises/~/link "link")

Creates a new link from the `existingPath` to the `newPath`. See the POSIX [`link(2)`](http://man7.org/linux/man-pages/man2/link.2.html) documentation for more detail.

f

[lstat](././fs/promises/~/lstat "lstat")

Equivalent to `fsPromises.stat()` unless `path` refers to a symbolic link, in which case the link itself is stat-ed, not the file that it refers to. Refer to the POSIX [`lstat(2)`](http://man7.org/linux/man-pages/man2/lstat.2.html) document for more detail.

f

[lutimes](././fs/promises/~/lutimes "lutimes")

Changes the access and modification times of a file in the same way as `fsPromises.utimes()`, with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.

f

[mkdir](././fs/promises/~/mkdir "mkdir")

Asynchronously creates a directory.

f

[mkdtemp](././fs/promises/~/mkdtemp "mkdtemp")

Creates a unique temporary directory. A unique directory name is generated by appending six random characters to the end of the provided `prefix`. Due to platform inconsistencies, avoid trailing `X` characters in `prefix`. Some platforms, notably the BSDs, can return more than six random characters, and replace trailing `X` characters in `prefix` with random characters.

f

[open](././fs/promises/~/open "open")

Opens a `FileHandle`.

f

[opendir](././fs/promises/~/opendir "opendir")

Asynchronously open a directory for iterative scanning. See the POSIX [`opendir(3)`](http://man7.org/linux/man-pages/man3/opendir.3.html) documentation for more detail.

f

[promises.access](././fs/promises/~/promises.access "promises.access")

Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g.`fs.constants.W_OK | fs.constants.R_OK`). Check `File access constants` for possible values of `mode`.

f

[promises.appendFile](././fs/promises/~/promises.appendFile "promises.appendFile")

Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a `Buffer`.

f

[promises.chmod](././fs/promises/~/promises.chmod "promises.chmod")

Changes the permissions of a file.

f

[promises.chown](././fs/promises/~/promises.chown "promises.chown")

Changes the ownership of a file.

v

[promises.constants](././fs/promises/~/promises.constants "promises.constants")

No documentation available

f

[promises.copyFile](././fs/promises/~/promises.copyFile "promises.copyFile")

Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists.

f

[promises.cp](././fs/promises/~/promises.cp "promises.cp")

Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.

I

[promises.CreateReadStreamOptions](././fs/promises/~/promises.CreateReadStreamOptions "promises.CreateReadStreamOptions")

No documentation available

-   [autoClose](././fs/promises/~/promises.CreateReadStreamOptions#property_autoclose)
-   [emitClose](././fs/promises/~/promises.CreateReadStreamOptions#property_emitclose)
-   [encoding](././fs/promises/~/promises.CreateReadStreamOptions#property_encoding)
-   [end](././fs/promises/~/promises.CreateReadStreamOptions#property_end)
-   [highWaterMark](././fs/promises/~/promises.CreateReadStreamOptions#property_highwatermark)
-   [start](././fs/promises/~/promises.CreateReadStreamOptions#property_start)

I

[promises.CreateWriteStreamOptions](././fs/promises/~/promises.CreateWriteStreamOptions "promises.CreateWriteStreamOptions")

No documentation available

-   [autoClose](././fs/promises/~/promises.CreateWriteStreamOptions#property_autoclose)
-   [emitClose](././fs/promises/~/promises.CreateWriteStreamOptions#property_emitclose)
-   [encoding](././fs/promises/~/promises.CreateWriteStreamOptions#property_encoding)
-   [flush](././fs/promises/~/promises.CreateWriteStreamOptions#property_flush)
-   [highWaterMark](././fs/promises/~/promises.CreateWriteStreamOptions#property_highwatermark)
-   [start](././fs/promises/~/promises.CreateWriteStreamOptions#property_start)

I

[promises.FileChangeInfo](././fs/promises/~/promises.FileChangeInfo "promises.FileChangeInfo")

No documentation available

-   [eventType](././fs/promises/~/promises.FileChangeInfo#property_eventtype)
-   [filename](././fs/promises/~/promises.FileChangeInfo#property_filename)

I

[promises.FileHandle](././fs/promises/~/promises.FileHandle "promises.FileHandle")

No documentation available

-   [appendFile](././fs/promises/~/promises.FileHandle#method_appendfile_0)
-   [chmod](././fs/promises/~/promises.FileHandle#method_chmod_0)
-   [chown](././fs/promises/~/promises.FileHandle#method_chown_0)
-   [close](././fs/promises/~/promises.FileHandle#method_close_0)
-   [createReadStream](././fs/promises/~/promises.FileHandle#method_createreadstream_0)
-   [createWriteStream](././fs/promises/~/promises.FileHandle#method_createwritestream_0)
-   [datasync](././fs/promises/~/promises.FileHandle#method_datasync_0)
-   [fd](././fs/promises/~/promises.FileHandle#property_fd)
-   [read](././fs/promises/~/promises.FileHandle#method_read_0)
-   [readFile](././fs/promises/~/promises.FileHandle#method_readfile_0)
-   [readLines](././fs/promises/~/promises.FileHandle#method_readlines_0)
-   [readableWebStream](././fs/promises/~/promises.FileHandle#method_readablewebstream_0)
-   [readv](././fs/promises/~/promises.FileHandle#method_readv_0)
-   [stat](././fs/promises/~/promises.FileHandle#method_stat_0)
-   [sync](././fs/promises/~/promises.FileHandle#method_sync_0)
-   [truncate](././fs/promises/~/promises.FileHandle#method_truncate_0)
-   [utimes](././fs/promises/~/promises.FileHandle#method_utimes_0)
-   [write](././fs/promises/~/promises.FileHandle#method_write_0)
-   [writeFile](././fs/promises/~/promises.FileHandle#method_writefile_0)
-   [writev](././fs/promises/~/promises.FileHandle#method_writev_0)

I

[promises.FileReadOptions](././fs/promises/~/promises.FileReadOptions "promises.FileReadOptions")

No documentation available

-   [buffer](././fs/promises/~/promises.FileReadOptions#property_buffer)
-   [length](././fs/promises/~/promises.FileReadOptions#property_length)
-   [offset](././fs/promises/~/promises.FileReadOptions#property_offset)
-   [position](././fs/promises/~/promises.FileReadOptions#property_position)

I

[promises.FileReadResult](././fs/promises/~/promises.FileReadResult "promises.FileReadResult")

No documentation available

-   [buffer](././fs/promises/~/promises.FileReadResult#property_buffer)
-   [bytesRead](././fs/promises/~/promises.FileReadResult#property_bytesread)

I

[promises.FlagAndOpenMode](././fs/promises/~/promises.FlagAndOpenMode "promises.FlagAndOpenMode")

No documentation available

-   [flag](././fs/promises/~/promises.FlagAndOpenMode#property_flag)
-   [mode](././fs/promises/~/promises.FlagAndOpenMode#property_mode)

f

[promises.glob](././fs/promises/~/promises.glob "promises.glob")

Retrieves the files matching the specified pattern.

f

[promises.lchown](././fs/promises/~/promises.lchown "promises.lchown")

Changes the ownership on a symbolic link.

f

[promises.link](././fs/promises/~/promises.link "promises.link")

Creates a new link from the `existingPath` to the `newPath`. See the POSIX [`link(2)`](http://man7.org/linux/man-pages/man2/link.2.html) documentation for more detail.

f

[promises.lstat](././fs/promises/~/promises.lstat "promises.lstat")

Equivalent to `fsPromises.stat()` unless `path` refers to a symbolic link, in which case the link itself is stat-ed, not the file that it refers to. Refer to the POSIX [`lstat(2)`](http://man7.org/linux/man-pages/man2/lstat.2.html) document for more detail.

f

[promises.lutimes](././fs/promises/~/promises.lutimes "promises.lutimes")

Changes the access and modification times of a file in the same way as `fsPromises.utimes()`, with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.

f

[promises.mkdir](././fs/promises/~/promises.mkdir "promises.mkdir")

Asynchronously creates a directory.

f

[promises.mkdtemp](././fs/promises/~/promises.mkdtemp "promises.mkdtemp")

Creates a unique temporary directory. A unique directory name is generated by appending six random characters to the end of the provided `prefix`. Due to platform inconsistencies, avoid trailing `X` characters in `prefix`. Some platforms, notably the BSDs, can return more than six random characters, and replace trailing `X` characters in `prefix` with random characters.

f

[promises.open](././fs/promises/~/promises.open "promises.open")

Opens a `FileHandle`.

f

[promises.opendir](././fs/promises/~/promises.opendir "promises.opendir")

Asynchronously open a directory for iterative scanning. See the POSIX [`opendir(3)`](http://man7.org/linux/man-pages/man3/opendir.3.html) documentation for more detail.

I

[promises.ReadableWebStreamOptions](././fs/promises/~/promises.ReadableWebStreamOptions "promises.ReadableWebStreamOptions")

No documentation available

-   [type](././fs/promises/~/promises.ReadableWebStreamOptions#property_type)

f

[promises.readdir](././fs/promises/~/promises.readdir "promises.readdir")

Reads the contents of a directory.

f

[promises.readFile](././fs/promises/~/promises.readFile "promises.readFile")

Asynchronously reads the entire contents of a file.

f

[promises.readlink](././fs/promises/~/promises.readlink "promises.readlink")

Reads the contents of the symbolic link referred to by `path`. See the POSIX [`readlink(2)`](http://man7.org/linux/man-pages/man2/readlink.2.html) documentation for more detail. The promise is fulfilled with the`linkString` upon success.

f

[promises.realpath](././fs/promises/~/promises.realpath "promises.realpath")

Determines the actual location of `path` using the same semantics as the `fs.realpath.native()` function.

f

[promises.rename](././fs/promises/~/promises.rename "promises.rename")

Renames `oldPath` to `newPath`.

f

[promises.rm](././fs/promises/~/promises.rm "promises.rm")

Removes files and directories (modeled on the standard POSIX `rm` utility).

f

[promises.rmdir](././fs/promises/~/promises.rmdir "promises.rmdir")

Removes the directory identified by `path`.

f

[promises.stat](././fs/promises/~/promises.stat "promises.stat")

No documentation available

f

[promises.statfs](././fs/promises/~/promises.statfs "promises.statfs")

No documentation available

f

[promises.symlink](././fs/promises/~/promises.symlink "promises.symlink")

Creates a symbolic link.

f

[promises.truncate](././fs/promises/~/promises.truncate "promises.truncate")

Truncates (shortens or extends the length) of the content at `path` to `len` bytes.

f

[promises.unlink](././fs/promises/~/promises.unlink "promises.unlink")

If `path` refers to a symbolic link, then the link is removed without affecting the file or directory to which that link refers. If the `path` refers to a file path that is not a symbolic link, the file is deleted. See the POSIX [`unlink(2)`](http://man7.org/linux/man-pages/man2/unlink.2.html) documentation for more detail.

f

[promises.utimes](././fs/promises/~/promises.utimes "promises.utimes")

Change the file system timestamps of the object referenced by `path`.

f

[promises.watch](././fs/promises/~/promises.watch "promises.watch")

Returns an async iterator that watches for changes on `filename`, where `filename`is either a file or a directory.

f

[promises.writeFile](././fs/promises/~/promises.writeFile "promises.writeFile")

Asynchronously writes data to a file, replacing the file if it already exists. `data` can be a string, a buffer, an [AsyncIterable](https://tc39.github.io/ecma262/#sec-asynciterable-interface), or an [Iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol) object.

I

[ReadableWebStreamOptions](././fs/promises/~/ReadableWebStreamOptions "ReadableWebStreamOptions")

No documentation available

-   [type](././fs/promises/~/ReadableWebStreamOptions#property_type)

f

[readdir](././fs/promises/~/readdir "readdir")

Reads the contents of a directory.

f

[readFile](././fs/promises/~/readFile "readFile")

Asynchronously reads the entire contents of a file.

f

[readlink](././fs/promises/~/readlink "readlink")

Reads the contents of the symbolic link referred to by `path`. See the POSIX [`readlink(2)`](http://man7.org/linux/man-pages/man2/readlink.2.html) documentation for more detail. The promise is fulfilled with the`linkString` upon success.

f

[realpath](././fs/promises/~/realpath "realpath")

Determines the actual location of `path` using the same semantics as the `fs.realpath.native()` function.

f

[rename](././fs/promises/~/rename "rename")

Renames `oldPath` to `newPath`.

f

[rm](././fs/promises/~/rm "rm")

Removes files and directories (modeled on the standard POSIX `rm` utility).

f

[rmdir](././fs/promises/~/rmdir "rmdir")

Removes the directory identified by `path`.

f

[stat](././fs/promises/~/stat "stat")

No documentation available

f

[statfs](././fs/promises/~/statfs "statfs")

No documentation available

f

[symlink](././fs/promises/~/symlink "symlink")

Creates a symbolic link.

f

[truncate](././fs/promises/~/truncate "truncate")

Truncates (shortens or extends the length) of the content at `path` to `len` bytes.

f

[unlink](././fs/promises/~/unlink "unlink")

If `path` refers to a symbolic link, then the link is removed without affecting the file or directory to which that link refers. If the `path` refers to a file path that is not a symbolic link, the file is deleted. See the POSIX [`unlink(2)`](http://man7.org/linux/man-pages/man2/unlink.2.html) documentation for more detail.

f

[utimes](././fs/promises/~/utimes "utimes")

Change the file system timestamps of the object referenced by `path`.

f

[watch](././fs/promises/~/watch "watch")

Returns an async iterator that watches for changes on `filename`, where `filename`is either a file or a directory.

f

[writeFile](././fs/promises/~/writeFile "writeFile")

Asynchronously writes data to a file, replacing the file if it already exists. `data` can be a string, a buffer, an [AsyncIterable](https://tc39.github.io/ecma262/#sec-asynciterable-interface), or an [Iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol) object.

f

[lchmod](././fs/promises/~/lchmod "lchmod")

No documentation available

f

[promises.lchmod](././fs/promises/~/promises.lchmod "promises.lchmod")

No documentation available

To use the HTTP server and client one must import the `node:http` module.

c

[Agent](././http/~/Agent "Agent")

An `Agent` is responsible for managing connection persistence and reuse for HTTP clients. It maintains a queue of pending requests for a given host and port, reusing a single socket connection for each until the queue is empty, at which time the socket is either destroyed or put into a pool where it is kept to be used again for requests to the same host and port. Whether it is destroyed or pooled depends on the `keepAlive` `option`.

-   [destroy](././http/~/Agent#method_destroy_0)
-   [freeSockets](././http/~/Agent#property_freesockets)
-   [maxFreeSockets](././http/~/Agent#property_maxfreesockets)
-   [maxSockets](././http/~/Agent#property_maxsockets)
-   [maxTotalSockets](././http/~/Agent#property_maxtotalsockets)
-   [requests](././http/~/Agent#property_requests)
-   [sockets](././http/~/Agent#property_sockets)

I

[AgentOptions](././http/~/AgentOptions "AgentOptions")

No documentation available

-   [keepAlive](././http/~/AgentOptions#property_keepalive)
-   [keepAliveMsecs](././http/~/AgentOptions#property_keepalivemsecs)
-   [maxFreeSockets](././http/~/AgentOptions#property_maxfreesockets)
-   [maxSockets](././http/~/AgentOptions#property_maxsockets)
-   [maxTotalSockets](././http/~/AgentOptions#property_maxtotalsockets)
-   [scheduling](././http/~/AgentOptions#property_scheduling)
-   [timeout](././http/~/AgentOptions#property_timeout)

c

[ClientRequest](././http/~/ClientRequest "ClientRequest")

No documentation available

-   [abort](././http/~/ClientRequest#method_abort_0)
-   [aborted](././http/~/ClientRequest#property_aborted)
-   [addListener](././http/~/ClientRequest#method_addlistener_0)
-   [getRawHeaderNames](././http/~/ClientRequest#method_getrawheadernames_0)
-   [host](././http/~/ClientRequest#property_host)
-   [maxHeadersCount](././http/~/ClientRequest#property_maxheaderscount)
-   [method](././http/~/ClientRequest#property_method)
-   [on](././http/~/ClientRequest#method_on_0)
-   [onSocket](././http/~/ClientRequest#method_onsocket_0)
-   [once](././http/~/ClientRequest#method_once_0)
-   [path](././http/~/ClientRequest#property_path)
-   [prependListener](././http/~/ClientRequest#method_prependlistener_0)
-   [prependOnceListener](././http/~/ClientRequest#method_prependoncelistener_0)
-   [protocol](././http/~/ClientRequest#property_protocol)
-   [reusedSocket](././http/~/ClientRequest#property_reusedsocket)
-   [setNoDelay](././http/~/ClientRequest#method_setnodelay_0)
-   [setSocketKeepAlive](././http/~/ClientRequest#method_setsocketkeepalive_0)
-   [setTimeout](././http/~/ClientRequest#method_settimeout_0)

I

[ClientRequestArgs](././http/~/ClientRequestArgs "ClientRequestArgs")

No documentation available

-   [\_defaultAgent](././http/~/ClientRequestArgs#property__defaultagent)
-   [agent](././http/~/ClientRequestArgs#property_agent)
-   [auth](././http/~/ClientRequestArgs#property_auth)
-   [createConnection](././http/~/ClientRequestArgs#property_createconnection)
-   [defaultPort](././http/~/ClientRequestArgs#property_defaultport)
-   [family](././http/~/ClientRequestArgs#property_family)
-   [headers](././http/~/ClientRequestArgs#property_headers)
-   [hints](././http/~/ClientRequestArgs#property_hints)
-   [host](././http/~/ClientRequestArgs#property_host)
-   [hostname](././http/~/ClientRequestArgs#property_hostname)
-   [insecureHTTPParser](././http/~/ClientRequestArgs#property_insecurehttpparser)
-   [joinDuplicateHeaders](././http/~/ClientRequestArgs#property_joinduplicateheaders)
-   [localAddress](././http/~/ClientRequestArgs#property_localaddress)
-   [localPort](././http/~/ClientRequestArgs#property_localport)
-   [lookup](././http/~/ClientRequestArgs#property_lookup)
-   [maxHeaderSize](././http/~/ClientRequestArgs#property_maxheadersize)
-   [method](././http/~/ClientRequestArgs#property_method)
-   [path](././http/~/ClientRequestArgs#property_path)
-   [port](././http/~/ClientRequestArgs#property_port)
-   [protocol](././http/~/ClientRequestArgs#property_protocol)
-   [setDefaultHeaders](././http/~/ClientRequestArgs#property_setdefaultheaders)
-   [setHost](././http/~/ClientRequestArgs#property_sethost)
-   [signal](././http/~/ClientRequestArgs#property_signal)
-   [socketPath](././http/~/ClientRequestArgs#property_socketpath)
-   [timeout](././http/~/ClientRequestArgs#property_timeout)
-   [uniqueHeaders](././http/~/ClientRequestArgs#property_uniqueheaders)

v

[CloseEvent](././http/~/CloseEvent "CloseEvent")

No documentation available

f

[createServer](././http/~/createServer "createServer")

Returns a new instance of [Server](././http/~/Server).

f

[get](././http/~/get "get")

No documentation available

v

[globalAgent](././http/~/globalAgent "globalAgent")

Global instance of `Agent` which is used as the default for all HTTP client requests. Diverges from a default `Agent` configuration by having `keepAlive` enabled and a `timeout` of 5 seconds.

I

[IncomingHttpHeaders](././http/~/IncomingHttpHeaders "IncomingHttpHeaders")

No documentation available

-   [accept](././http/~/IncomingHttpHeaders#property_accept)
-   [accept-language](././http/~/IncomingHttpHeaders#property_accept-language)
-   [accept-patch](././http/~/IncomingHttpHeaders#property_accept-patch)
-   [accept-ranges](././http/~/IncomingHttpHeaders#property_accept-ranges)
-   [access-control-allow-credentials](././http/~/IncomingHttpHeaders#property_access-control-allow-credentials)
-   [access-control-allow-headers](././http/~/IncomingHttpHeaders#property_access-control-allow-headers)
-   [access-control-allow-methods](././http/~/IncomingHttpHeaders#property_access-control-allow-methods)
-   [access-control-allow-origin](././http/~/IncomingHttpHeaders#property_access-control-allow-origin)
-   [access-control-expose-headers](././http/~/IncomingHttpHeaders#property_access-control-expose-headers)
-   [access-control-max-age](././http/~/IncomingHttpHeaders#property_access-control-max-age)
-   [access-control-request-headers](././http/~/IncomingHttpHeaders#property_access-control-request-headers)
-   [access-control-request-method](././http/~/IncomingHttpHeaders#property_access-control-request-method)
-   [age](././http/~/IncomingHttpHeaders#property_age)
-   [allow](././http/~/IncomingHttpHeaders#property_allow)
-   [alt-svc](././http/~/IncomingHttpHeaders#property_alt-svc)
-   [authorization](././http/~/IncomingHttpHeaders#property_authorization)
-   [cache-control](././http/~/IncomingHttpHeaders#property_cache-control)
-   [connection](././http/~/IncomingHttpHeaders#property_connection)
-   [content-disposition](././http/~/IncomingHttpHeaders#property_content-disposition)
-   [content-encoding](././http/~/IncomingHttpHeaders#property_content-encoding)
-   [content-language](././http/~/IncomingHttpHeaders#property_content-language)
-   [content-length](././http/~/IncomingHttpHeaders#property_content-length)
-   [content-location](././http/~/IncomingHttpHeaders#property_content-location)
-   [content-range](././http/~/IncomingHttpHeaders#property_content-range)
-   [content-type](././http/~/IncomingHttpHeaders#property_content-type)
-   [cookie](././http/~/IncomingHttpHeaders#property_cookie)
-   [date](././http/~/IncomingHttpHeaders#property_date)
-   [etag](././http/~/IncomingHttpHeaders#property_etag)
-   [expect](././http/~/IncomingHttpHeaders#property_expect)
-   [expires](././http/~/IncomingHttpHeaders#property_expires)
-   [forwarded](././http/~/IncomingHttpHeaders#property_forwarded)
-   [from](././http/~/IncomingHttpHeaders#property_from)
-   [host](././http/~/IncomingHttpHeaders#property_host)
-   [if-match](././http/~/IncomingHttpHeaders#property_if-match)
-   [if-modified-since](././http/~/IncomingHttpHeaders#property_if-modified-since)
-   [if-none-match](././http/~/IncomingHttpHeaders#property_if-none-match)
-   [if-unmodified-since](././http/~/IncomingHttpHeaders#property_if-unmodified-since)
-   [last-modified](././http/~/IncomingHttpHeaders#property_last-modified)
-   [location](././http/~/IncomingHttpHeaders#property_location)
-   [origin](././http/~/IncomingHttpHeaders#property_origin)
-   [pragma](././http/~/IncomingHttpHeaders#property_pragma)
-   [proxy-authenticate](././http/~/IncomingHttpHeaders#property_proxy-authenticate)
-   [proxy-authorization](././http/~/IncomingHttpHeaders#property_proxy-authorization)
-   [public-key-pins](././http/~/IncomingHttpHeaders#property_public-key-pins)
-   [range](././http/~/IncomingHttpHeaders#property_range)
-   [referer](././http/~/IncomingHttpHeaders#property_referer)
-   [retry-after](././http/~/IncomingHttpHeaders#property_retry-after)
-   [sec-websocket-accept](././http/~/IncomingHttpHeaders#property_sec-websocket-accept)
-   [sec-websocket-extensions](././http/~/IncomingHttpHeaders#property_sec-websocket-extensions)
-   [sec-websocket-key](././http/~/IncomingHttpHeaders#property_sec-websocket-key)
-   [sec-websocket-protocol](././http/~/IncomingHttpHeaders#property_sec-websocket-protocol)
-   [sec-websocket-version](././http/~/IncomingHttpHeaders#property_sec-websocket-version)
-   [set-cookie](././http/~/IncomingHttpHeaders#property_set-cookie)
-   [strict-transport-security](././http/~/IncomingHttpHeaders#property_strict-transport-security)
-   [tk](././http/~/IncomingHttpHeaders#property_tk)
-   [trailer](././http/~/IncomingHttpHeaders#property_trailer)
-   [transfer-encoding](././http/~/IncomingHttpHeaders#property_transfer-encoding)
-   [upgrade](././http/~/IncomingHttpHeaders#property_upgrade)
-   [user-agent](././http/~/IncomingHttpHeaders#property_user-agent)
-   [vary](././http/~/IncomingHttpHeaders#property_vary)
-   [via](././http/~/IncomingHttpHeaders#property_via)
-   [warning](././http/~/IncomingHttpHeaders#property_warning)
-   [www-authenticate](././http/~/IncomingHttpHeaders#property_www-authenticate)

c

[IncomingMessage](././http/~/IncomingMessage "IncomingMessage")

An `IncomingMessage` object is created by [Server](././http/~/Server) or [ClientRequest](././http/~/ClientRequest) and passed as the first argument to the `'request'` and `'response'` event respectively. It may be used to access response status, headers, and data.

-   [aborted](././http/~/IncomingMessage#property_aborted)
-   [complete](././http/~/IncomingMessage#property_complete)
-   [connection](././http/~/IncomingMessage#property_connection)
-   [destroy](././http/~/IncomingMessage#method_destroy_0)
-   [headers](././http/~/IncomingMessage#property_headers)
-   [headersDistinct](././http/~/IncomingMessage#property_headersdistinct)
-   [httpVersion](././http/~/IncomingMessage#property_httpversion)
-   [httpVersionMajor](././http/~/IncomingMessage#property_httpversionmajor)
-   [httpVersionMinor](././http/~/IncomingMessage#property_httpversionminor)
-   [method](././http/~/IncomingMessage#property_method)
-   [rawHeaders](././http/~/IncomingMessage#property_rawheaders)
-   [rawTrailers](././http/~/IncomingMessage#property_rawtrailers)
-   [setTimeout](././http/~/IncomingMessage#method_settimeout_0)
-   [socket](././http/~/IncomingMessage#property_socket)
-   [statusCode](././http/~/IncomingMessage#property_statuscode)
-   [statusMessage](././http/~/IncomingMessage#property_statusmessage)
-   [trailers](././http/~/IncomingMessage#property_trailers)
-   [trailersDistinct](././http/~/IncomingMessage#property_trailersdistinct)
-   [url](././http/~/IncomingMessage#property_url)

I

[InformationEvent](././http/~/InformationEvent "InformationEvent")

No documentation available

-   [headers](././http/~/InformationEvent#property_headers)
-   [httpVersion](././http/~/InformationEvent#property_httpversion)
-   [httpVersionMajor](././http/~/InformationEvent#property_httpversionmajor)
-   [httpVersionMinor](././http/~/InformationEvent#property_httpversionminor)
-   [rawHeaders](././http/~/InformationEvent#property_rawheaders)
-   [statusCode](././http/~/InformationEvent#property_statuscode)
-   [statusMessage](././http/~/InformationEvent#property_statusmessage)

v

[maxHeaderSize](././http/~/maxHeaderSize "maxHeaderSize")

Read-only property specifying the maximum allowed size of HTTP headers in bytes. Defaults to 16KB. Configurable using the `--max-http-header-size` CLI option.

v

[MessageEvent](././http/~/MessageEvent "MessageEvent")

No documentation available

v

[METHODS](././http/~/METHODS "METHODS")

No documentation available

T

[OutgoingHttpHeader](././http/~/OutgoingHttpHeader "OutgoingHttpHeader")

No documentation available

I

[OutgoingHttpHeaders](././http/~/OutgoingHttpHeaders "OutgoingHttpHeaders")

No documentation available

-   [accept](././http/~/OutgoingHttpHeaders#property_accept)
-   [accept-charset](././http/~/OutgoingHttpHeaders#property_accept-charset)
-   [accept-encoding](././http/~/OutgoingHttpHeaders#property_accept-encoding)
-   [accept-language](././http/~/OutgoingHttpHeaders#property_accept-language)
-   [accept-ranges](././http/~/OutgoingHttpHeaders#property_accept-ranges)
-   [access-control-allow-credentials](././http/~/OutgoingHttpHeaders#property_access-control-allow-credentials)
-   [access-control-allow-headers](././http/~/OutgoingHttpHeaders#property_access-control-allow-headers)
-   [access-control-allow-methods](././http/~/OutgoingHttpHeaders#property_access-control-allow-methods)
-   [access-control-allow-origin](././http/~/OutgoingHttpHeaders#property_access-control-allow-origin)
-   [access-control-expose-headers](././http/~/OutgoingHttpHeaders#property_access-control-expose-headers)
-   [access-control-max-age](././http/~/OutgoingHttpHeaders#property_access-control-max-age)
-   [access-control-request-headers](././http/~/OutgoingHttpHeaders#property_access-control-request-headers)
-   [access-control-request-method](././http/~/OutgoingHttpHeaders#property_access-control-request-method)
-   [age](././http/~/OutgoingHttpHeaders#property_age)
-   [allow](././http/~/OutgoingHttpHeaders#property_allow)
-   [authorization](././http/~/OutgoingHttpHeaders#property_authorization)
-   [cache-control](././http/~/OutgoingHttpHeaders#property_cache-control)
-   [cdn-cache-control](././http/~/OutgoingHttpHeaders#property_cdn-cache-control)
-   [connection](././http/~/OutgoingHttpHeaders#property_connection)
-   [content-disposition](././http/~/OutgoingHttpHeaders#property_content-disposition)
-   [content-encoding](././http/~/OutgoingHttpHeaders#property_content-encoding)
-   [content-language](././http/~/OutgoingHttpHeaders#property_content-language)
-   [content-length](././http/~/OutgoingHttpHeaders#property_content-length)
-   [content-location](././http/~/OutgoingHttpHeaders#property_content-location)
-   [content-range](././http/~/OutgoingHttpHeaders#property_content-range)
-   [content-security-policy](././http/~/OutgoingHttpHeaders#property_content-security-policy)
-   [content-security-policy-report-only](././http/~/OutgoingHttpHeaders#property_content-security-policy-report-only)
-   [content-type](././http/~/OutgoingHttpHeaders#property_content-type)
-   [cookie](././http/~/OutgoingHttpHeaders#property_cookie)
-   [date](././http/~/OutgoingHttpHeaders#property_date)
-   [dav](././http/~/OutgoingHttpHeaders#property_dav)
-   [dnt](././http/~/OutgoingHttpHeaders#property_dnt)
-   [etag](././http/~/OutgoingHttpHeaders#property_etag)
-   [expect](././http/~/OutgoingHttpHeaders#property_expect)
-   [expires](././http/~/OutgoingHttpHeaders#property_expires)
-   [forwarded](././http/~/OutgoingHttpHeaders#property_forwarded)
-   [from](././http/~/OutgoingHttpHeaders#property_from)
-   [host](././http/~/OutgoingHttpHeaders#property_host)
-   [if-match](././http/~/OutgoingHttpHeaders#property_if-match)
-   [if-modified-since](././http/~/OutgoingHttpHeaders#property_if-modified-since)
-   [if-none-match](././http/~/OutgoingHttpHeaders#property_if-none-match)
-   [if-range](././http/~/OutgoingHttpHeaders#property_if-range)
-   [if-unmodified-since](././http/~/OutgoingHttpHeaders#property_if-unmodified-since)
-   [last-modified](././http/~/OutgoingHttpHeaders#property_last-modified)
-   [link](././http/~/OutgoingHttpHeaders#property_link)
-   [location](././http/~/OutgoingHttpHeaders#property_location)
-   [max-forwards](././http/~/OutgoingHttpHeaders#property_max-forwards)
-   [origin](././http/~/OutgoingHttpHeaders#property_origin)
-   [pragma](././http/~/OutgoingHttpHeaders#property_pragma)
-   [proxy-authenticate](././http/~/OutgoingHttpHeaders#property_proxy-authenticate)
-   [proxy-authorization](././http/~/OutgoingHttpHeaders#property_proxy-authorization)
-   [public-key-pins](././http/~/OutgoingHttpHeaders#property_public-key-pins)
-   [public-key-pins-report-only](././http/~/OutgoingHttpHeaders#property_public-key-pins-report-only)
-   [range](././http/~/OutgoingHttpHeaders#property_range)
-   [referer](././http/~/OutgoingHttpHeaders#property_referer)
-   [referrer-policy](././http/~/OutgoingHttpHeaders#property_referrer-policy)
-   [refresh](././http/~/OutgoingHttpHeaders#property_refresh)
-   [retry-after](././http/~/OutgoingHttpHeaders#property_retry-after)
-   [sec-websocket-accept](././http/~/OutgoingHttpHeaders#property_sec-websocket-accept)
-   [sec-websocket-extensions](././http/~/OutgoingHttpHeaders#property_sec-websocket-extensions)
-   [sec-websocket-key](././http/~/OutgoingHttpHeaders#property_sec-websocket-key)
-   [sec-websocket-protocol](././http/~/OutgoingHttpHeaders#property_sec-websocket-protocol)
-   [sec-websocket-version](././http/~/OutgoingHttpHeaders#property_sec-websocket-version)
-   [server](././http/~/OutgoingHttpHeaders#property_server)
-   [set-cookie](././http/~/OutgoingHttpHeaders#property_set-cookie)
-   [strict-transport-security](././http/~/OutgoingHttpHeaders#property_strict-transport-security)
-   [te](././http/~/OutgoingHttpHeaders#property_te)
-   [trailer](././http/~/OutgoingHttpHeaders#property_trailer)
-   [transfer-encoding](././http/~/OutgoingHttpHeaders#property_transfer-encoding)
-   [upgrade](././http/~/OutgoingHttpHeaders#property_upgrade)
-   [upgrade-insecure-requests](././http/~/OutgoingHttpHeaders#property_upgrade-insecure-requests)
-   [user-agent](././http/~/OutgoingHttpHeaders#property_user-agent)
-   [vary](././http/~/OutgoingHttpHeaders#property_vary)
-   [via](././http/~/OutgoingHttpHeaders#property_via)
-   [warning](././http/~/OutgoingHttpHeaders#property_warning)
-   [www-authenticate](././http/~/OutgoingHttpHeaders#property_www-authenticate)
-   [x-content-type-options](././http/~/OutgoingHttpHeaders#property_x-content-type-options)
-   [x-dns-prefetch-control](././http/~/OutgoingHttpHeaders#property_x-dns-prefetch-control)
-   [x-frame-options](././http/~/OutgoingHttpHeaders#property_x-frame-options)
-   [x-xss-protection](././http/~/OutgoingHttpHeaders#property_x-xss-protection)

c

[OutgoingMessage](././http/~/OutgoingMessage "OutgoingMessage")

This class serves as the parent class of [ClientRequest](././http/~/ClientRequest) and [ServerResponse](././http/~/ServerResponse). It is an abstract outgoing message from the perspective of the participants of an HTTP transaction.

-   [addTrailers](././http/~/OutgoingMessage#method_addtrailers_0)
-   [appendHeader](././http/~/OutgoingMessage#method_appendheader_0)
-   [chunkedEncoding](././http/~/OutgoingMessage#property_chunkedencoding)
-   [connection](././http/~/OutgoingMessage#property_connection)
-   [finished](././http/~/OutgoingMessage#property_finished)
-   [flushHeaders](././http/~/OutgoingMessage#method_flushheaders_0)
-   [getHeader](././http/~/OutgoingMessage#method_getheader_0)
-   [getHeaderNames](././http/~/OutgoingMessage#method_getheadernames_0)
-   [getHeaders](././http/~/OutgoingMessage#method_getheaders_0)
-   [hasHeader](././http/~/OutgoingMessage#method_hasheader_0)
-   [headersSent](././http/~/OutgoingMessage#property_headerssent)
-   [removeHeader](././http/~/OutgoingMessage#method_removeheader_0)
-   [req](././http/~/OutgoingMessage#property_req)
-   [sendDate](././http/~/OutgoingMessage#property_senddate)
-   [setHeader](././http/~/OutgoingMessage#method_setheader_0)
-   [setHeaders](././http/~/OutgoingMessage#method_setheaders_0)
-   [setTimeout](././http/~/OutgoingMessage#method_settimeout_0)
-   [shouldKeepAlive](././http/~/OutgoingMessage#property_shouldkeepalive)
-   [socket](././http/~/OutgoingMessage#property_socket)
-   [useChunkedEncodingByDefault](././http/~/OutgoingMessage#property_usechunkedencodingbydefault)

f

[request](././http/~/request "request")

No documentation available

T

[RequestListener](././http/~/RequestListener "RequestListener")

No documentation available

I

[RequestOptions](././http/~/RequestOptions "RequestOptions")

No documentation available

c

[Server](././http/~/Server "Server")

No documentation available

-   [addListener](././http/~/Server#method_addlistener_0)
-   [closeAllConnections](././http/~/Server#method_closeallconnections_0)
-   [closeIdleConnections](././http/~/Server#method_closeidleconnections_0)
-   [emit](././http/~/Server#method_emit_0)
-   [headersTimeout](././http/~/Server#property_headerstimeout)
-   [keepAliveTimeout](././http/~/Server#property_keepalivetimeout)
-   [maxHeadersCount](././http/~/Server#property_maxheaderscount)
-   [maxRequestsPerSocket](././http/~/Server#property_maxrequestspersocket)
-   [on](././http/~/Server#method_on_0)
-   [once](././http/~/Server#method_once_0)
-   [prependListener](././http/~/Server#method_prependlistener_0)
-   [prependOnceListener](././http/~/Server#method_prependoncelistener_0)
-   [requestTimeout](././http/~/Server#property_requesttimeout)
-   [setTimeout](././http/~/Server#method_settimeout_0)
-   [timeout](././http/~/Server#property_timeout)

I

[ServerOptions](././http/~/ServerOptions "ServerOptions")

No documentation available

-   [IncomingMessage](././http/~/ServerOptions#property_incomingmessage)
-   [ServerResponse](././http/~/ServerOptions#property_serverresponse)
-   [connectionsCheckingInterval](././http/~/ServerOptions#property_connectionscheckinginterval)
-   [highWaterMark](././http/~/ServerOptions#property_highwatermark)
-   [insecureHTTPParser](././http/~/ServerOptions#property_insecurehttpparser)
-   [joinDuplicateHeaders](././http/~/ServerOptions#property_joinduplicateheaders)
-   [keepAlive](././http/~/ServerOptions#property_keepalive)
-   [keepAliveInitialDelay](././http/~/ServerOptions#property_keepaliveinitialdelay)
-   [keepAliveTimeout](././http/~/ServerOptions#property_keepalivetimeout)
-   [maxHeaderSize](././http/~/ServerOptions#property_maxheadersize)
-   [noDelay](././http/~/ServerOptions#property_nodelay)
-   [requestTimeout](././http/~/ServerOptions#property_requesttimeout)
-   [uniqueHeaders](././http/~/ServerOptions#property_uniqueheaders)

c

[ServerResponse](././http/~/ServerResponse "ServerResponse")

This object is created internally by an HTTP server, not by the user. It is passed as the second parameter to the `'request'` event.

-   [assignSocket](././http/~/ServerResponse#method_assignsocket_0)
-   [detachSocket](././http/~/ServerResponse#method_detachsocket_0)
-   [statusCode](././http/~/ServerResponse#property_statuscode)
-   [statusMessage](././http/~/ServerResponse#property_statusmessage)
-   [strictContentLength](././http/~/ServerResponse#property_strictcontentlength)
-   [writeContinue](././http/~/ServerResponse#method_writecontinue_0)
-   [writeEarlyHints](././http/~/ServerResponse#method_writeearlyhints_0)
-   [writeHead](././http/~/ServerResponse#method_writehead_0)
-   [writeProcessing](././http/~/ServerResponse#method_writeprocessing_0)

f

[setMaxIdleHTTPParsers](././http/~/setMaxIdleHTTPParsers "setMaxIdleHTTPParsers")

Set the maximum number of idle HTTP parsers.

v

[STATUS\_CODES](././http/~/STATUS_CODES "STATUS_CODES")

No documentation available

f

[validateHeaderName](././http/~/validateHeaderName "validateHeaderName")

Performs the low-level validations on the provided `name` that are done when `res.setHeader(name, value)` is called.

f

[validateHeaderValue](././http/~/validateHeaderValue "validateHeaderValue")

Performs the low-level validations on the provided `value` that are done when `res.setHeader(name, value)` is called.

v

[WebSocket](././http/~/WebSocket "WebSocket")

A browser-compatible implementation of [WebSocket](https://nodejs.org/docs/latest/api/http.html#websocket).

The `node:http2` module provides an implementation of the [HTTP/2](https://tools.ietf.org/html/rfc7540) protocol. It can be accessed using:

I

[AlternativeServiceOptions](././http2/~/AlternativeServiceOptions "AlternativeServiceOptions")

No documentation available

-   [origin](././http2/~/AlternativeServiceOptions#property_origin)

I

[ClientHttp2Session](././http2/~/ClientHttp2Session "ClientHttp2Session")

No documentation available

-   [addListener](././http2/~/ClientHttp2Session#method_addlistener_0)
-   [emit](././http2/~/ClientHttp2Session#method_emit_0)
-   [on](././http2/~/ClientHttp2Session#method_on_0)
-   [once](././http2/~/ClientHttp2Session#method_once_0)
-   [prependListener](././http2/~/ClientHttp2Session#method_prependlistener_0)
-   [prependOnceListener](././http2/~/ClientHttp2Session#method_prependoncelistener_0)
-   [request](././http2/~/ClientHttp2Session#method_request_0)

I

[ClientHttp2Stream](././http2/~/ClientHttp2Stream "ClientHttp2Stream")

No documentation available

-   [addListener](././http2/~/ClientHttp2Stream#method_addlistener_0)
-   [emit](././http2/~/ClientHttp2Stream#method_emit_0)
-   [on](././http2/~/ClientHttp2Stream#method_on_0)
-   [once](././http2/~/ClientHttp2Stream#method_once_0)
-   [prependListener](././http2/~/ClientHttp2Stream#method_prependlistener_0)
-   [prependOnceListener](././http2/~/ClientHttp2Stream#method_prependoncelistener_0)

I

[ClientSessionOptions](././http2/~/ClientSessionOptions "ClientSessionOptions")

No documentation available

-   [createConnection](././http2/~/ClientSessionOptions#property_createconnection)
-   [maxReservedRemoteStreams](././http2/~/ClientSessionOptions#property_maxreservedremotestreams)
-   [protocol](././http2/~/ClientSessionOptions#property_protocol)

I

[ClientSessionRequestOptions](././http2/~/ClientSessionRequestOptions "ClientSessionRequestOptions")

No documentation available

-   [endStream](././http2/~/ClientSessionRequestOptions#property_endstream)
-   [exclusive](././http2/~/ClientSessionRequestOptions#property_exclusive)
-   [parent](././http2/~/ClientSessionRequestOptions#property_parent)
-   [signal](././http2/~/ClientSessionRequestOptions#property_signal)
-   [waitForTrailers](././http2/~/ClientSessionRequestOptions#property_waitfortrailers)
-   [weight](././http2/~/ClientSessionRequestOptions#property_weight)

f

[connect](././http2/~/connect "connect")

Returns a `ClientHttp2Session` instance.

N

[constants](././http2/~/constants "constants")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_ENABLE\_PUSH](././http2/~/constants.DEFAULT_SETTINGS_ENABLE_PUSH "constants.DEFAULT_SETTINGS_ENABLE_PUSH")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_HEADER\_TABLE\_SIZE](././http2/~/constants.DEFAULT_SETTINGS_HEADER_TABLE_SIZE "constants.DEFAULT_SETTINGS_HEADER_TABLE_SIZE")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_INITIAL\_WINDOW\_SIZE](././http2/~/constants.DEFAULT_SETTINGS_INITIAL_WINDOW_SIZE "constants.DEFAULT_SETTINGS_INITIAL_WINDOW_SIZE")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_MAX\_FRAME\_SIZE](././http2/~/constants.DEFAULT_SETTINGS_MAX_FRAME_SIZE "constants.DEFAULT_SETTINGS_MAX_FRAME_SIZE")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT](././http2/~/constants.HTTP2_HEADER_ACCEPT "constants.HTTP2_HEADER_ACCEPT")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_CHARSET](././http2/~/constants.HTTP2_HEADER_ACCEPT_CHARSET "constants.HTTP2_HEADER_ACCEPT_CHARSET")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_ENCODING](././http2/~/constants.HTTP2_HEADER_ACCEPT_ENCODING "constants.HTTP2_HEADER_ACCEPT_ENCODING")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_LANGUAGE](././http2/~/constants.HTTP2_HEADER_ACCEPT_LANGUAGE "constants.HTTP2_HEADER_ACCEPT_LANGUAGE")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_RANGES](././http2/~/constants.HTTP2_HEADER_ACCEPT_RANGES "constants.HTTP2_HEADER_ACCEPT_RANGES")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_CREDENTIALS](././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_HEADERS](././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_HEADERS "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_HEADERS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_METHODS](././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_METHODS "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_METHODS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_ORIGIN](././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_ORIGIN "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_ORIGIN")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_EXPOSE\_HEADERS](././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_EXPOSE_HEADERS "constants.HTTP2_HEADER_ACCESS_CONTROL_EXPOSE_HEADERS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_REQUEST\_HEADERS](././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_HEADERS "constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_HEADERS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_REQUEST\_METHOD](././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_METHOD "constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_METHOD")

No documentation available

v

[constants.HTTP2\_HEADER\_AGE](././http2/~/constants.HTTP2_HEADER_AGE "constants.HTTP2_HEADER_AGE")

No documentation available

v

[constants.HTTP2\_HEADER\_ALLOW](././http2/~/constants.HTTP2_HEADER_ALLOW "constants.HTTP2_HEADER_ALLOW")

No documentation available

v

[constants.HTTP2\_HEADER\_AUTHORITY](././http2/~/constants.HTTP2_HEADER_AUTHORITY "constants.HTTP2_HEADER_AUTHORITY")

No documentation available

v

[constants.HTTP2\_HEADER\_AUTHORIZATION](././http2/~/constants.HTTP2_HEADER_AUTHORIZATION "constants.HTTP2_HEADER_AUTHORIZATION")

No documentation available

v

[constants.HTTP2\_HEADER\_CACHE\_CONTROL](././http2/~/constants.HTTP2_HEADER_CACHE_CONTROL "constants.HTTP2_HEADER_CACHE_CONTROL")

No documentation available

v

[constants.HTTP2\_HEADER\_CONNECTION](././http2/~/constants.HTTP2_HEADER_CONNECTION "constants.HTTP2_HEADER_CONNECTION")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_DISPOSITION](././http2/~/constants.HTTP2_HEADER_CONTENT_DISPOSITION "constants.HTTP2_HEADER_CONTENT_DISPOSITION")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_ENCODING](././http2/~/constants.HTTP2_HEADER_CONTENT_ENCODING "constants.HTTP2_HEADER_CONTENT_ENCODING")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_LANGUAGE](././http2/~/constants.HTTP2_HEADER_CONTENT_LANGUAGE "constants.HTTP2_HEADER_CONTENT_LANGUAGE")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_LENGTH](././http2/~/constants.HTTP2_HEADER_CONTENT_LENGTH "constants.HTTP2_HEADER_CONTENT_LENGTH")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_LOCATION](././http2/~/constants.HTTP2_HEADER_CONTENT_LOCATION "constants.HTTP2_HEADER_CONTENT_LOCATION")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_MD5](././http2/~/constants.HTTP2_HEADER_CONTENT_MD5 "constants.HTTP2_HEADER_CONTENT_MD5")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_RANGE](././http2/~/constants.HTTP2_HEADER_CONTENT_RANGE "constants.HTTP2_HEADER_CONTENT_RANGE")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_TYPE](././http2/~/constants.HTTP2_HEADER_CONTENT_TYPE "constants.HTTP2_HEADER_CONTENT_TYPE")

No documentation available

v

[constants.HTTP2\_HEADER\_COOKIE](././http2/~/constants.HTTP2_HEADER_COOKIE "constants.HTTP2_HEADER_COOKIE")

No documentation available

v

[constants.HTTP2\_HEADER\_DATE](././http2/~/constants.HTTP2_HEADER_DATE "constants.HTTP2_HEADER_DATE")

No documentation available

v

[constants.HTTP2\_HEADER\_ETAG](././http2/~/constants.HTTP2_HEADER_ETAG "constants.HTTP2_HEADER_ETAG")

No documentation available

v

[constants.HTTP2\_HEADER\_EXPECT](././http2/~/constants.HTTP2_HEADER_EXPECT "constants.HTTP2_HEADER_EXPECT")

No documentation available

v

[constants.HTTP2\_HEADER\_EXPIRES](././http2/~/constants.HTTP2_HEADER_EXPIRES "constants.HTTP2_HEADER_EXPIRES")

No documentation available

v

[constants.HTTP2\_HEADER\_FROM](././http2/~/constants.HTTP2_HEADER_FROM "constants.HTTP2_HEADER_FROM")

No documentation available

v

[constants.HTTP2\_HEADER\_HOST](././http2/~/constants.HTTP2_HEADER_HOST "constants.HTTP2_HEADER_HOST")

No documentation available

v

[constants.HTTP2\_HEADER\_HTTP2\_SETTINGS](././http2/~/constants.HTTP2_HEADER_HTTP2_SETTINGS "constants.HTTP2_HEADER_HTTP2_SETTINGS")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_MATCH](././http2/~/constants.HTTP2_HEADER_IF_MATCH "constants.HTTP2_HEADER_IF_MATCH")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_MODIFIED\_SINCE](././http2/~/constants.HTTP2_HEADER_IF_MODIFIED_SINCE "constants.HTTP2_HEADER_IF_MODIFIED_SINCE")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_NONE\_MATCH](././http2/~/constants.HTTP2_HEADER_IF_NONE_MATCH "constants.HTTP2_HEADER_IF_NONE_MATCH")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_RANGE](././http2/~/constants.HTTP2_HEADER_IF_RANGE "constants.HTTP2_HEADER_IF_RANGE")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_UNMODIFIED\_SINCE](././http2/~/constants.HTTP2_HEADER_IF_UNMODIFIED_SINCE "constants.HTTP2_HEADER_IF_UNMODIFIED_SINCE")

No documentation available

v

[constants.HTTP2\_HEADER\_KEEP\_ALIVE](././http2/~/constants.HTTP2_HEADER_KEEP_ALIVE "constants.HTTP2_HEADER_KEEP_ALIVE")

No documentation available

v

[constants.HTTP2\_HEADER\_LAST\_MODIFIED](././http2/~/constants.HTTP2_HEADER_LAST_MODIFIED "constants.HTTP2_HEADER_LAST_MODIFIED")

No documentation available

v

[constants.HTTP2\_HEADER\_LINK](././http2/~/constants.HTTP2_HEADER_LINK "constants.HTTP2_HEADER_LINK")

No documentation available

v

[constants.HTTP2\_HEADER\_LOCATION](././http2/~/constants.HTTP2_HEADER_LOCATION "constants.HTTP2_HEADER_LOCATION")

No documentation available

v

[constants.HTTP2\_HEADER\_MAX\_FORWARDS](././http2/~/constants.HTTP2_HEADER_MAX_FORWARDS "constants.HTTP2_HEADER_MAX_FORWARDS")

No documentation available

v

[constants.HTTP2\_HEADER\_METHOD](././http2/~/constants.HTTP2_HEADER_METHOD "constants.HTTP2_HEADER_METHOD")

No documentation available

v

[constants.HTTP2\_HEADER\_PATH](././http2/~/constants.HTTP2_HEADER_PATH "constants.HTTP2_HEADER_PATH")

No documentation available

v

[constants.HTTP2\_HEADER\_PREFER](././http2/~/constants.HTTP2_HEADER_PREFER "constants.HTTP2_HEADER_PREFER")

No documentation available

v

[constants.HTTP2\_HEADER\_PROXY\_AUTHENTICATE](././http2/~/constants.HTTP2_HEADER_PROXY_AUTHENTICATE "constants.HTTP2_HEADER_PROXY_AUTHENTICATE")

No documentation available

v

[constants.HTTP2\_HEADER\_PROXY\_AUTHORIZATION](././http2/~/constants.HTTP2_HEADER_PROXY_AUTHORIZATION "constants.HTTP2_HEADER_PROXY_AUTHORIZATION")

No documentation available

v

[constants.HTTP2\_HEADER\_PROXY\_CONNECTION](././http2/~/constants.HTTP2_HEADER_PROXY_CONNECTION "constants.HTTP2_HEADER_PROXY_CONNECTION")

No documentation available

v

[constants.HTTP2\_HEADER\_RANGE](././http2/~/constants.HTTP2_HEADER_RANGE "constants.HTTP2_HEADER_RANGE")

No documentation available

v

[constants.HTTP2\_HEADER\_REFERER](././http2/~/constants.HTTP2_HEADER_REFERER "constants.HTTP2_HEADER_REFERER")

No documentation available

v

[constants.HTTP2\_HEADER\_REFRESH](././http2/~/constants.HTTP2_HEADER_REFRESH "constants.HTTP2_HEADER_REFRESH")

No documentation available

v

[constants.HTTP2\_HEADER\_RETRY\_AFTER](././http2/~/constants.HTTP2_HEADER_RETRY_AFTER "constants.HTTP2_HEADER_RETRY_AFTER")

No documentation available

v

[constants.HTTP2\_HEADER\_SCHEME](././http2/~/constants.HTTP2_HEADER_SCHEME "constants.HTTP2_HEADER_SCHEME")

No documentation available

v

[constants.HTTP2\_HEADER\_SERVER](././http2/~/constants.HTTP2_HEADER_SERVER "constants.HTTP2_HEADER_SERVER")

No documentation available

v

[constants.HTTP2\_HEADER\_SET\_COOKIE](././http2/~/constants.HTTP2_HEADER_SET_COOKIE "constants.HTTP2_HEADER_SET_COOKIE")

No documentation available

v

[constants.HTTP2\_HEADER\_STATUS](././http2/~/constants.HTTP2_HEADER_STATUS "constants.HTTP2_HEADER_STATUS")

No documentation available

v

[constants.HTTP2\_HEADER\_STRICT\_TRANSPORT\_SECURITY](././http2/~/constants.HTTP2_HEADER_STRICT_TRANSPORT_SECURITY "constants.HTTP2_HEADER_STRICT_TRANSPORT_SECURITY")

No documentation available

v

[constants.HTTP2\_HEADER\_TE](././http2/~/constants.HTTP2_HEADER_TE "constants.HTTP2_HEADER_TE")

No documentation available

v

[constants.HTTP2\_HEADER\_TRANSFER\_ENCODING](././http2/~/constants.HTTP2_HEADER_TRANSFER_ENCODING "constants.HTTP2_HEADER_TRANSFER_ENCODING")

No documentation available

v

[constants.HTTP2\_HEADER\_UPGRADE](././http2/~/constants.HTTP2_HEADER_UPGRADE "constants.HTTP2_HEADER_UPGRADE")

No documentation available

v

[constants.HTTP2\_HEADER\_USER\_AGENT](././http2/~/constants.HTTP2_HEADER_USER_AGENT "constants.HTTP2_HEADER_USER_AGENT")

No documentation available

v

[constants.HTTP2\_HEADER\_VARY](././http2/~/constants.HTTP2_HEADER_VARY "constants.HTTP2_HEADER_VARY")

No documentation available

v

[constants.HTTP2\_HEADER\_VIA](././http2/~/constants.HTTP2_HEADER_VIA "constants.HTTP2_HEADER_VIA")

No documentation available

v

[constants.HTTP2\_HEADER\_WWW\_AUTHENTICATE](././http2/~/constants.HTTP2_HEADER_WWW_AUTHENTICATE "constants.HTTP2_HEADER_WWW_AUTHENTICATE")

No documentation available

v

[constants.HTTP2\_METHOD\_ACL](././http2/~/constants.HTTP2_METHOD_ACL "constants.HTTP2_METHOD_ACL")

No documentation available

v

[constants.HTTP2\_METHOD\_BASELINE\_CONTROL](././http2/~/constants.HTTP2_METHOD_BASELINE_CONTROL "constants.HTTP2_METHOD_BASELINE_CONTROL")

No documentation available

v

[constants.HTTP2\_METHOD\_BIND](././http2/~/constants.HTTP2_METHOD_BIND "constants.HTTP2_METHOD_BIND")

No documentation available

v

[constants.HTTP2\_METHOD\_CHECKIN](././http2/~/constants.HTTP2_METHOD_CHECKIN "constants.HTTP2_METHOD_CHECKIN")

No documentation available

v

[constants.HTTP2\_METHOD\_CHECKOUT](././http2/~/constants.HTTP2_METHOD_CHECKOUT "constants.HTTP2_METHOD_CHECKOUT")

No documentation available

v

[constants.HTTP2\_METHOD\_CONNECT](././http2/~/constants.HTTP2_METHOD_CONNECT "constants.HTTP2_METHOD_CONNECT")

No documentation available

v

[constants.HTTP2\_METHOD\_COPY](././http2/~/constants.HTTP2_METHOD_COPY "constants.HTTP2_METHOD_COPY")

No documentation available

v

[constants.HTTP2\_METHOD\_DELETE](././http2/~/constants.HTTP2_METHOD_DELETE "constants.HTTP2_METHOD_DELETE")

No documentation available

v

[constants.HTTP2\_METHOD\_GET](././http2/~/constants.HTTP2_METHOD_GET "constants.HTTP2_METHOD_GET")

No documentation available

v

[constants.HTTP2\_METHOD\_HEAD](././http2/~/constants.HTTP2_METHOD_HEAD "constants.HTTP2_METHOD_HEAD")

No documentation available

v

[constants.HTTP2\_METHOD\_LABEL](././http2/~/constants.HTTP2_METHOD_LABEL "constants.HTTP2_METHOD_LABEL")

No documentation available

v

[constants.HTTP2\_METHOD\_LINK](././http2/~/constants.HTTP2_METHOD_LINK "constants.HTTP2_METHOD_LINK")

No documentation available

v

[constants.HTTP2\_METHOD\_LOCK](././http2/~/constants.HTTP2_METHOD_LOCK "constants.HTTP2_METHOD_LOCK")

No documentation available

v

[constants.HTTP2\_METHOD\_MERGE](././http2/~/constants.HTTP2_METHOD_MERGE "constants.HTTP2_METHOD_MERGE")

No documentation available

v

[constants.HTTP2\_METHOD\_MKACTIVITY](././http2/~/constants.HTTP2_METHOD_MKACTIVITY "constants.HTTP2_METHOD_MKACTIVITY")

No documentation available

v

[constants.HTTP2\_METHOD\_MKCALENDAR](././http2/~/constants.HTTP2_METHOD_MKCALENDAR "constants.HTTP2_METHOD_MKCALENDAR")

No documentation available

v

[constants.HTTP2\_METHOD\_MKCOL](././http2/~/constants.HTTP2_METHOD_MKCOL "constants.HTTP2_METHOD_MKCOL")

No documentation available

v

[constants.HTTP2\_METHOD\_MKREDIRECTREF](././http2/~/constants.HTTP2_METHOD_MKREDIRECTREF "constants.HTTP2_METHOD_MKREDIRECTREF")

No documentation available

v

[constants.HTTP2\_METHOD\_MKWORKSPACE](././http2/~/constants.HTTP2_METHOD_MKWORKSPACE "constants.HTTP2_METHOD_MKWORKSPACE")

No documentation available

v

[constants.HTTP2\_METHOD\_MOVE](././http2/~/constants.HTTP2_METHOD_MOVE "constants.HTTP2_METHOD_MOVE")

No documentation available

v

[constants.HTTP2\_METHOD\_OPTIONS](././http2/~/constants.HTTP2_METHOD_OPTIONS "constants.HTTP2_METHOD_OPTIONS")

No documentation available

v

[constants.HTTP2\_METHOD\_ORDERPATCH](././http2/~/constants.HTTP2_METHOD_ORDERPATCH "constants.HTTP2_METHOD_ORDERPATCH")

No documentation available

v

[constants.HTTP2\_METHOD\_PATCH](././http2/~/constants.HTTP2_METHOD_PATCH "constants.HTTP2_METHOD_PATCH")

No documentation available

v

[constants.HTTP2\_METHOD\_POST](././http2/~/constants.HTTP2_METHOD_POST "constants.HTTP2_METHOD_POST")

No documentation available

v

[constants.HTTP2\_METHOD\_PRI](././http2/~/constants.HTTP2_METHOD_PRI "constants.HTTP2_METHOD_PRI")

No documentation available

v

[constants.HTTP2\_METHOD\_PROPFIND](././http2/~/constants.HTTP2_METHOD_PROPFIND "constants.HTTP2_METHOD_PROPFIND")

No documentation available

v

[constants.HTTP2\_METHOD\_PROPPATCH](././http2/~/constants.HTTP2_METHOD_PROPPATCH "constants.HTTP2_METHOD_PROPPATCH")

No documentation available

v

[constants.HTTP2\_METHOD\_PUT](././http2/~/constants.HTTP2_METHOD_PUT "constants.HTTP2_METHOD_PUT")

No documentation available

v

[constants.HTTP2\_METHOD\_REBIND](././http2/~/constants.HTTP2_METHOD_REBIND "constants.HTTP2_METHOD_REBIND")

No documentation available

v

[constants.HTTP2\_METHOD\_REPORT](././http2/~/constants.HTTP2_METHOD_REPORT "constants.HTTP2_METHOD_REPORT")

No documentation available

v

[constants.HTTP2\_METHOD\_SEARCH](././http2/~/constants.HTTP2_METHOD_SEARCH "constants.HTTP2_METHOD_SEARCH")

No documentation available

v

[constants.HTTP2\_METHOD\_TRACE](././http2/~/constants.HTTP2_METHOD_TRACE "constants.HTTP2_METHOD_TRACE")

No documentation available

v

[constants.HTTP2\_METHOD\_UNBIND](././http2/~/constants.HTTP2_METHOD_UNBIND "constants.HTTP2_METHOD_UNBIND")

No documentation available

v

[constants.HTTP2\_METHOD\_UNCHECKOUT](././http2/~/constants.HTTP2_METHOD_UNCHECKOUT "constants.HTTP2_METHOD_UNCHECKOUT")

No documentation available

v

[constants.HTTP2\_METHOD\_UNLINK](././http2/~/constants.HTTP2_METHOD_UNLINK "constants.HTTP2_METHOD_UNLINK")

No documentation available

v

[constants.HTTP2\_METHOD\_UNLOCK](././http2/~/constants.HTTP2_METHOD_UNLOCK "constants.HTTP2_METHOD_UNLOCK")

No documentation available

v

[constants.HTTP2\_METHOD\_UPDATE](././http2/~/constants.HTTP2_METHOD_UPDATE "constants.HTTP2_METHOD_UPDATE")

No documentation available

v

[constants.HTTP2\_METHOD\_UPDATEREDIRECTREF](././http2/~/constants.HTTP2_METHOD_UPDATEREDIRECTREF "constants.HTTP2_METHOD_UPDATEREDIRECTREF")

No documentation available

v

[constants.HTTP2\_METHOD\_VERSION\_CONTROL](././http2/~/constants.HTTP2_METHOD_VERSION_CONTROL "constants.HTTP2_METHOD_VERSION_CONTROL")

No documentation available

v

[constants.HTTP\_STATUS\_ACCEPTED](././http2/~/constants.HTTP_STATUS_ACCEPTED "constants.HTTP_STATUS_ACCEPTED")

No documentation available

v

[constants.HTTP\_STATUS\_ALREADY\_REPORTED](././http2/~/constants.HTTP_STATUS_ALREADY_REPORTED "constants.HTTP_STATUS_ALREADY_REPORTED")

No documentation available

v

[constants.HTTP\_STATUS\_BAD\_GATEWAY](././http2/~/constants.HTTP_STATUS_BAD_GATEWAY "constants.HTTP_STATUS_BAD_GATEWAY")

No documentation available

v

[constants.HTTP\_STATUS\_BAD\_REQUEST](././http2/~/constants.HTTP_STATUS_BAD_REQUEST "constants.HTTP_STATUS_BAD_REQUEST")

No documentation available

v

[constants.HTTP\_STATUS\_BANDWIDTH\_LIMIT\_EXCEEDED](././http2/~/constants.HTTP_STATUS_BANDWIDTH_LIMIT_EXCEEDED "constants.HTTP_STATUS_BANDWIDTH_LIMIT_EXCEEDED")

No documentation available

v

[constants.HTTP\_STATUS\_CONFLICT](././http2/~/constants.HTTP_STATUS_CONFLICT "constants.HTTP_STATUS_CONFLICT")

No documentation available

v

[constants.HTTP\_STATUS\_CONTINUE](././http2/~/constants.HTTP_STATUS_CONTINUE "constants.HTTP_STATUS_CONTINUE")

No documentation available

v

[constants.HTTP\_STATUS\_CREATED](././http2/~/constants.HTTP_STATUS_CREATED "constants.HTTP_STATUS_CREATED")

No documentation available

v

[constants.HTTP\_STATUS\_EXPECTATION\_FAILED](././http2/~/constants.HTTP_STATUS_EXPECTATION_FAILED "constants.HTTP_STATUS_EXPECTATION_FAILED")

No documentation available

v

[constants.HTTP\_STATUS\_FAILED\_DEPENDENCY](././http2/~/constants.HTTP_STATUS_FAILED_DEPENDENCY "constants.HTTP_STATUS_FAILED_DEPENDENCY")

No documentation available

v

[constants.HTTP\_STATUS\_FORBIDDEN](././http2/~/constants.HTTP_STATUS_FORBIDDEN "constants.HTTP_STATUS_FORBIDDEN")

No documentation available

v

[constants.HTTP\_STATUS\_FOUND](././http2/~/constants.HTTP_STATUS_FOUND "constants.HTTP_STATUS_FOUND")

No documentation available

v

[constants.HTTP\_STATUS\_GATEWAY\_TIMEOUT](././http2/~/constants.HTTP_STATUS_GATEWAY_TIMEOUT "constants.HTTP_STATUS_GATEWAY_TIMEOUT")

No documentation available

v

[constants.HTTP\_STATUS\_GONE](././http2/~/constants.HTTP_STATUS_GONE "constants.HTTP_STATUS_GONE")

No documentation available

v

[constants.HTTP\_STATUS\_HTTP\_VERSION\_NOT\_SUPPORTED](././http2/~/constants.HTTP_STATUS_HTTP_VERSION_NOT_SUPPORTED "constants.HTTP_STATUS_HTTP_VERSION_NOT_SUPPORTED")

No documentation available

v

[constants.HTTP\_STATUS\_IM\_USED](././http2/~/constants.HTTP_STATUS_IM_USED "constants.HTTP_STATUS_IM_USED")

No documentation available

v

[constants.HTTP\_STATUS\_INSUFFICIENT\_STORAGE](././http2/~/constants.HTTP_STATUS_INSUFFICIENT_STORAGE "constants.HTTP_STATUS_INSUFFICIENT_STORAGE")

No documentation available

v

[constants.HTTP\_STATUS\_INTERNAL\_SERVER\_ERROR](././http2/~/constants.HTTP_STATUS_INTERNAL_SERVER_ERROR "constants.HTTP_STATUS_INTERNAL_SERVER_ERROR")

No documentation available

v

[constants.HTTP\_STATUS\_LENGTH\_REQUIRED](././http2/~/constants.HTTP_STATUS_LENGTH_REQUIRED "constants.HTTP_STATUS_LENGTH_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_LOCKED](././http2/~/constants.HTTP_STATUS_LOCKED "constants.HTTP_STATUS_LOCKED")

No documentation available

v

[constants.HTTP\_STATUS\_LOOP\_DETECTED](././http2/~/constants.HTTP_STATUS_LOOP_DETECTED "constants.HTTP_STATUS_LOOP_DETECTED")

No documentation available

v

[constants.HTTP\_STATUS\_METHOD\_NOT\_ALLOWED](././http2/~/constants.HTTP_STATUS_METHOD_NOT_ALLOWED "constants.HTTP_STATUS_METHOD_NOT_ALLOWED")

No documentation available

v

[constants.HTTP\_STATUS\_MISDIRECTED\_REQUEST](././http2/~/constants.HTTP_STATUS_MISDIRECTED_REQUEST "constants.HTTP_STATUS_MISDIRECTED_REQUEST")

No documentation available

v

[constants.HTTP\_STATUS\_MOVED\_PERMANENTLY](././http2/~/constants.HTTP_STATUS_MOVED_PERMANENTLY "constants.HTTP_STATUS_MOVED_PERMANENTLY")

No documentation available

v

[constants.HTTP\_STATUS\_MULTI\_STATUS](././http2/~/constants.HTTP_STATUS_MULTI_STATUS "constants.HTTP_STATUS_MULTI_STATUS")

No documentation available

v

[constants.HTTP\_STATUS\_MULTIPLE\_CHOICES](././http2/~/constants.HTTP_STATUS_MULTIPLE_CHOICES "constants.HTTP_STATUS_MULTIPLE_CHOICES")

No documentation available

v

[constants.HTTP\_STATUS\_NETWORK\_AUTHENTICATION\_REQUIRED](././http2/~/constants.HTTP_STATUS_NETWORK_AUTHENTICATION_REQUIRED "constants.HTTP_STATUS_NETWORK_AUTHENTICATION_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_NO\_CONTENT](././http2/~/constants.HTTP_STATUS_NO_CONTENT "constants.HTTP_STATUS_NO_CONTENT")

No documentation available

v

[constants.HTTP\_STATUS\_NON\_AUTHORITATIVE\_INFORMATION](././http2/~/constants.HTTP_STATUS_NON_AUTHORITATIVE_INFORMATION "constants.HTTP_STATUS_NON_AUTHORITATIVE_INFORMATION")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_ACCEPTABLE](././http2/~/constants.HTTP_STATUS_NOT_ACCEPTABLE "constants.HTTP_STATUS_NOT_ACCEPTABLE")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_EXTENDED](././http2/~/constants.HTTP_STATUS_NOT_EXTENDED "constants.HTTP_STATUS_NOT_EXTENDED")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_FOUND](././http2/~/constants.HTTP_STATUS_NOT_FOUND "constants.HTTP_STATUS_NOT_FOUND")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_IMPLEMENTED](././http2/~/constants.HTTP_STATUS_NOT_IMPLEMENTED "constants.HTTP_STATUS_NOT_IMPLEMENTED")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_MODIFIED](././http2/~/constants.HTTP_STATUS_NOT_MODIFIED "constants.HTTP_STATUS_NOT_MODIFIED")

No documentation available

v

[constants.HTTP\_STATUS\_OK](././http2/~/constants.HTTP_STATUS_OK "constants.HTTP_STATUS_OK")

No documentation available

v

[constants.HTTP\_STATUS\_PARTIAL\_CONTENT](././http2/~/constants.HTTP_STATUS_PARTIAL_CONTENT "constants.HTTP_STATUS_PARTIAL_CONTENT")

No documentation available

v

[constants.HTTP\_STATUS\_PAYLOAD\_TOO\_LARGE](././http2/~/constants.HTTP_STATUS_PAYLOAD_TOO_LARGE "constants.HTTP_STATUS_PAYLOAD_TOO_LARGE")

No documentation available

v

[constants.HTTP\_STATUS\_PAYMENT\_REQUIRED](././http2/~/constants.HTTP_STATUS_PAYMENT_REQUIRED "constants.HTTP_STATUS_PAYMENT_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_PERMANENT\_REDIRECT](././http2/~/constants.HTTP_STATUS_PERMANENT_REDIRECT "constants.HTTP_STATUS_PERMANENT_REDIRECT")

No documentation available

v

[constants.HTTP\_STATUS\_PRECONDITION\_FAILED](././http2/~/constants.HTTP_STATUS_PRECONDITION_FAILED "constants.HTTP_STATUS_PRECONDITION_FAILED")

No documentation available

v

[constants.HTTP\_STATUS\_PRECONDITION\_REQUIRED](././http2/~/constants.HTTP_STATUS_PRECONDITION_REQUIRED "constants.HTTP_STATUS_PRECONDITION_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_PROCESSING](././http2/~/constants.HTTP_STATUS_PROCESSING "constants.HTTP_STATUS_PROCESSING")

No documentation available

v

[constants.HTTP\_STATUS\_PROXY\_AUTHENTICATION\_REQUIRED](././http2/~/constants.HTTP_STATUS_PROXY_AUTHENTICATION_REQUIRED "constants.HTTP_STATUS_PROXY_AUTHENTICATION_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_RANGE\_NOT\_SATISFIABLE](././http2/~/constants.HTTP_STATUS_RANGE_NOT_SATISFIABLE "constants.HTTP_STATUS_RANGE_NOT_SATISFIABLE")

No documentation available

v

[constants.HTTP\_STATUS\_REQUEST\_HEADER\_FIELDS\_TOO\_LARGE](././http2/~/constants.HTTP_STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE "constants.HTTP_STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE")

No documentation available

v

[constants.HTTP\_STATUS\_REQUEST\_TIMEOUT](././http2/~/constants.HTTP_STATUS_REQUEST_TIMEOUT "constants.HTTP_STATUS_REQUEST_TIMEOUT")

No documentation available

v

[constants.HTTP\_STATUS\_RESET\_CONTENT](././http2/~/constants.HTTP_STATUS_RESET_CONTENT "constants.HTTP_STATUS_RESET_CONTENT")

No documentation available

v

[constants.HTTP\_STATUS\_SEE\_OTHER](././http2/~/constants.HTTP_STATUS_SEE_OTHER "constants.HTTP_STATUS_SEE_OTHER")

No documentation available

v

[constants.HTTP\_STATUS\_SERVICE\_UNAVAILABLE](././http2/~/constants.HTTP_STATUS_SERVICE_UNAVAILABLE "constants.HTTP_STATUS_SERVICE_UNAVAILABLE")

No documentation available

v

[constants.HTTP\_STATUS\_SWITCHING\_PROTOCOLS](././http2/~/constants.HTTP_STATUS_SWITCHING_PROTOCOLS "constants.HTTP_STATUS_SWITCHING_PROTOCOLS")

No documentation available

v

[constants.HTTP\_STATUS\_TEAPOT](././http2/~/constants.HTTP_STATUS_TEAPOT "constants.HTTP_STATUS_TEAPOT")

No documentation available

v

[constants.HTTP\_STATUS\_TEMPORARY\_REDIRECT](././http2/~/constants.HTTP_STATUS_TEMPORARY_REDIRECT "constants.HTTP_STATUS_TEMPORARY_REDIRECT")

No documentation available

v

[constants.HTTP\_STATUS\_TOO\_MANY\_REQUESTS](././http2/~/constants.HTTP_STATUS_TOO_MANY_REQUESTS "constants.HTTP_STATUS_TOO_MANY_REQUESTS")

No documentation available

v

[constants.HTTP\_STATUS\_UNAUTHORIZED](././http2/~/constants.HTTP_STATUS_UNAUTHORIZED "constants.HTTP_STATUS_UNAUTHORIZED")

No documentation available

v

[constants.HTTP\_STATUS\_UNAVAILABLE\_FOR\_LEGAL\_REASONS](././http2/~/constants.HTTP_STATUS_UNAVAILABLE_FOR_LEGAL_REASONS "constants.HTTP_STATUS_UNAVAILABLE_FOR_LEGAL_REASONS")

No documentation available

v

[constants.HTTP\_STATUS\_UNORDERED\_COLLECTION](././http2/~/constants.HTTP_STATUS_UNORDERED_COLLECTION "constants.HTTP_STATUS_UNORDERED_COLLECTION")

No documentation available

v

[constants.HTTP\_STATUS\_UNPROCESSABLE\_ENTITY](././http2/~/constants.HTTP_STATUS_UNPROCESSABLE_ENTITY "constants.HTTP_STATUS_UNPROCESSABLE_ENTITY")

No documentation available

v

[constants.HTTP\_STATUS\_UNSUPPORTED\_MEDIA\_TYPE](././http2/~/constants.HTTP_STATUS_UNSUPPORTED_MEDIA_TYPE "constants.HTTP_STATUS_UNSUPPORTED_MEDIA_TYPE")

No documentation available

v

[constants.HTTP\_STATUS\_UPGRADE\_REQUIRED](././http2/~/constants.HTTP_STATUS_UPGRADE_REQUIRED "constants.HTTP_STATUS_UPGRADE_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_URI\_TOO\_LONG](././http2/~/constants.HTTP_STATUS_URI_TOO_LONG "constants.HTTP_STATUS_URI_TOO_LONG")

No documentation available

v

[constants.HTTP\_STATUS\_USE\_PROXY](././http2/~/constants.HTTP_STATUS_USE_PROXY "constants.HTTP_STATUS_USE_PROXY")

No documentation available

v

[constants.HTTP\_STATUS\_VARIANT\_ALSO\_NEGOTIATES](././http2/~/constants.HTTP_STATUS_VARIANT_ALSO_NEGOTIATES "constants.HTTP_STATUS_VARIANT_ALSO_NEGOTIATES")

No documentation available

v

[constants.MAX\_INITIAL\_WINDOW\_SIZE](././http2/~/constants.MAX_INITIAL_WINDOW_SIZE "constants.MAX_INITIAL_WINDOW_SIZE")

No documentation available

v

[constants.MAX\_MAX\_FRAME\_SIZE](././http2/~/constants.MAX_MAX_FRAME_SIZE "constants.MAX_MAX_FRAME_SIZE")

No documentation available

v

[constants.MIN\_MAX\_FRAME\_SIZE](././http2/~/constants.MIN_MAX_FRAME_SIZE "constants.MIN_MAX_FRAME_SIZE")

No documentation available

v

[constants.NGHTTP2\_CANCEL](././http2/~/constants.NGHTTP2_CANCEL "constants.NGHTTP2_CANCEL")

No documentation available

v

[constants.NGHTTP2\_COMPRESSION\_ERROR](././http2/~/constants.NGHTTP2_COMPRESSION_ERROR "constants.NGHTTP2_COMPRESSION_ERROR")

No documentation available

v

[constants.NGHTTP2\_CONNECT\_ERROR](././http2/~/constants.NGHTTP2_CONNECT_ERROR "constants.NGHTTP2_CONNECT_ERROR")

No documentation available

v

[constants.NGHTTP2\_DEFAULT\_WEIGHT](././http2/~/constants.NGHTTP2_DEFAULT_WEIGHT "constants.NGHTTP2_DEFAULT_WEIGHT")

No documentation available

v

[constants.NGHTTP2\_ENHANCE\_YOUR\_CALM](././http2/~/constants.NGHTTP2_ENHANCE_YOUR_CALM "constants.NGHTTP2_ENHANCE_YOUR_CALM")

No documentation available

v

[constants.NGHTTP2\_ERR\_FRAME\_SIZE\_ERROR](././http2/~/constants.NGHTTP2_ERR_FRAME_SIZE_ERROR "constants.NGHTTP2_ERR_FRAME_SIZE_ERROR")

No documentation available

v

[constants.NGHTTP2\_FLAG\_ACK](././http2/~/constants.NGHTTP2_FLAG_ACK "constants.NGHTTP2_FLAG_ACK")

No documentation available

v

[constants.NGHTTP2\_FLAG\_END\_HEADERS](././http2/~/constants.NGHTTP2_FLAG_END_HEADERS "constants.NGHTTP2_FLAG_END_HEADERS")

No documentation available

v

[constants.NGHTTP2\_FLAG\_END\_STREAM](././http2/~/constants.NGHTTP2_FLAG_END_STREAM "constants.NGHTTP2_FLAG_END_STREAM")

No documentation available

v

[constants.NGHTTP2\_FLAG\_NONE](././http2/~/constants.NGHTTP2_FLAG_NONE "constants.NGHTTP2_FLAG_NONE")

No documentation available

v

[constants.NGHTTP2\_FLAG\_PADDED](././http2/~/constants.NGHTTP2_FLAG_PADDED "constants.NGHTTP2_FLAG_PADDED")

No documentation available

v

[constants.NGHTTP2\_FLAG\_PRIORITY](././http2/~/constants.NGHTTP2_FLAG_PRIORITY "constants.NGHTTP2_FLAG_PRIORITY")

No documentation available

v

[constants.NGHTTP2\_FLOW\_CONTROL\_ERROR](././http2/~/constants.NGHTTP2_FLOW_CONTROL_ERROR "constants.NGHTTP2_FLOW_CONTROL_ERROR")

No documentation available

v

[constants.NGHTTP2\_FRAME\_SIZE\_ERROR](././http2/~/constants.NGHTTP2_FRAME_SIZE_ERROR "constants.NGHTTP2_FRAME_SIZE_ERROR")

No documentation available

v

[constants.NGHTTP2\_HTTP\_1\_1\_REQUIRED](././http2/~/constants.NGHTTP2_HTTP_1_1_REQUIRED "constants.NGHTTP2_HTTP_1_1_REQUIRED")

No documentation available

v

[constants.NGHTTP2\_INADEQUATE\_SECURITY](././http2/~/constants.NGHTTP2_INADEQUATE_SECURITY "constants.NGHTTP2_INADEQUATE_SECURITY")

No documentation available

v

[constants.NGHTTP2\_INTERNAL\_ERROR](././http2/~/constants.NGHTTP2_INTERNAL_ERROR "constants.NGHTTP2_INTERNAL_ERROR")

No documentation available

v

[constants.NGHTTP2\_NO\_ERROR](././http2/~/constants.NGHTTP2_NO_ERROR "constants.NGHTTP2_NO_ERROR")

No documentation available

v

[constants.NGHTTP2\_PROTOCOL\_ERROR](././http2/~/constants.NGHTTP2_PROTOCOL_ERROR "constants.NGHTTP2_PROTOCOL_ERROR")

No documentation available

v

[constants.NGHTTP2\_REFUSED\_STREAM](././http2/~/constants.NGHTTP2_REFUSED_STREAM "constants.NGHTTP2_REFUSED_STREAM")

No documentation available

v

[constants.NGHTTP2\_SESSION\_CLIENT](././http2/~/constants.NGHTTP2_SESSION_CLIENT "constants.NGHTTP2_SESSION_CLIENT")

No documentation available

v

[constants.NGHTTP2\_SESSION\_SERVER](././http2/~/constants.NGHTTP2_SESSION_SERVER "constants.NGHTTP2_SESSION_SERVER")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_ENABLE\_PUSH](././http2/~/constants.NGHTTP2_SETTINGS_ENABLE_PUSH "constants.NGHTTP2_SETTINGS_ENABLE_PUSH")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_HEADER\_TABLE\_SIZE](././http2/~/constants.NGHTTP2_SETTINGS_HEADER_TABLE_SIZE "constants.NGHTTP2_SETTINGS_HEADER_TABLE_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_INITIAL\_WINDOW\_SIZE](././http2/~/constants.NGHTTP2_SETTINGS_INITIAL_WINDOW_SIZE "constants.NGHTTP2_SETTINGS_INITIAL_WINDOW_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_MAX\_CONCURRENT\_STREAMS](././http2/~/constants.NGHTTP2_SETTINGS_MAX_CONCURRENT_STREAMS "constants.NGHTTP2_SETTINGS_MAX_CONCURRENT_STREAMS")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_MAX\_FRAME\_SIZE](././http2/~/constants.NGHTTP2_SETTINGS_MAX_FRAME_SIZE "constants.NGHTTP2_SETTINGS_MAX_FRAME_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_MAX\_HEADER\_LIST\_SIZE](././http2/~/constants.NGHTTP2_SETTINGS_MAX_HEADER_LIST_SIZE "constants.NGHTTP2_SETTINGS_MAX_HEADER_LIST_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_TIMEOUT](././http2/~/constants.NGHTTP2_SETTINGS_TIMEOUT "constants.NGHTTP2_SETTINGS_TIMEOUT")

No documentation available

v

[constants.NGHTTP2\_STREAM\_CLOSED](././http2/~/constants.NGHTTP2_STREAM_CLOSED "constants.NGHTTP2_STREAM_CLOSED")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_CLOSED](././http2/~/constants.NGHTTP2_STREAM_STATE_CLOSED "constants.NGHTTP2_STREAM_STATE_CLOSED")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_HALF\_CLOSED\_LOCAL](././http2/~/constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_LOCAL "constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_LOCAL")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_HALF\_CLOSED\_REMOTE](././http2/~/constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_REMOTE "constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_REMOTE")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_IDLE](././http2/~/constants.NGHTTP2_STREAM_STATE_IDLE "constants.NGHTTP2_STREAM_STATE_IDLE")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_OPEN](././http2/~/constants.NGHTTP2_STREAM_STATE_OPEN "constants.NGHTTP2_STREAM_STATE_OPEN")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_RESERVED\_LOCAL](././http2/~/constants.NGHTTP2_STREAM_STATE_RESERVED_LOCAL "constants.NGHTTP2_STREAM_STATE_RESERVED_LOCAL")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_RESERVED\_REMOTE](././http2/~/constants.NGHTTP2_STREAM_STATE_RESERVED_REMOTE "constants.NGHTTP2_STREAM_STATE_RESERVED_REMOTE")

No documentation available

v

[constants.PADDING\_STRATEGY\_CALLBACK](././http2/~/constants.PADDING_STRATEGY_CALLBACK "constants.PADDING_STRATEGY_CALLBACK")

No documentation available

v

[constants.PADDING\_STRATEGY\_MAX](././http2/~/constants.PADDING_STRATEGY_MAX "constants.PADDING_STRATEGY_MAX")

No documentation available

v

[constants.PADDING\_STRATEGY\_NONE](././http2/~/constants.PADDING_STRATEGY_NONE "constants.PADDING_STRATEGY_NONE")

No documentation available

f

[createSecureServer](././http2/~/createSecureServer "createSecureServer")

Returns a `tls.Server` instance that creates and manages `Http2Session` instances.

f

[createServer](././http2/~/createServer "createServer")

Returns a `net.Server` instance that creates and manages `Http2Session` instances.

f

[getDefaultSettings](././http2/~/getDefaultSettings "getDefaultSettings")

No documentation available

f

[getPackedSettings](././http2/~/getPackedSettings "getPackedSettings")

No documentation available

f

[getUnpackedSettings](././http2/~/getUnpackedSettings "getUnpackedSettings")

No documentation available

I

[Http2SecureServer](././http2/~/Http2SecureServer "Http2SecureServer")

No documentation available

-   [addListener](././http2/~/Http2SecureServer#method_addlistener_0)
-   [emit](././http2/~/Http2SecureServer#method_emit_0)
-   [on](././http2/~/Http2SecureServer#method_on_0)
-   [once](././http2/~/Http2SecureServer#method_once_0)
-   [prependListener](././http2/~/Http2SecureServer#method_prependlistener_0)
-   [prependOnceListener](././http2/~/Http2SecureServer#method_prependoncelistener_0)

I

[Http2Server](././http2/~/Http2Server "Http2Server")

No documentation available

-   [addListener](././http2/~/Http2Server#method_addlistener_0)
-   [emit](././http2/~/Http2Server#method_emit_0)
-   [on](././http2/~/Http2Server#method_on_0)
-   [once](././http2/~/Http2Server#method_once_0)
-   [prependListener](././http2/~/Http2Server#method_prependlistener_0)
-   [prependOnceListener](././http2/~/Http2Server#method_prependoncelistener_0)

I

[HTTP2ServerCommon](././http2/~/HTTP2ServerCommon "HTTP2ServerCommon")

No documentation available

-   [setTimeout](././http2/~/HTTP2ServerCommon#method_settimeout_0)
-   [updateSettings](././http2/~/HTTP2ServerCommon#method_updatesettings_0)

c

[Http2ServerRequest](././http2/~/Http2ServerRequest "Http2ServerRequest")

A `Http2ServerRequest` object is created by Server or SecureServer and passed as the first argument to the `'request'` event. It may be used to access a request status, headers, and data.

-   [aborted](././http2/~/Http2ServerRequest#property_aborted)
-   [addListener](././http2/~/Http2ServerRequest#method_addlistener_0)
-   [authority](././http2/~/Http2ServerRequest#property_authority)
-   [complete](././http2/~/Http2ServerRequest#property_complete)
-   [connection](././http2/~/Http2ServerRequest#property_connection)
-   [emit](././http2/~/Http2ServerRequest#method_emit_0)
-   [headers](././http2/~/Http2ServerRequest#property_headers)
-   [httpVersion](././http2/~/Http2ServerRequest#property_httpversion)
-   [httpVersionMajor](././http2/~/Http2ServerRequest#property_httpversionmajor)
-   [httpVersionMinor](././http2/~/Http2ServerRequest#property_httpversionminor)
-   [method](././http2/~/Http2ServerRequest#property_method)
-   [on](././http2/~/Http2ServerRequest#method_on_0)
-   [once](././http2/~/Http2ServerRequest#method_once_0)
-   [prependListener](././http2/~/Http2ServerRequest#method_prependlistener_0)
-   [prependOnceListener](././http2/~/Http2ServerRequest#method_prependoncelistener_0)
-   [rawHeaders](././http2/~/Http2ServerRequest#property_rawheaders)
-   [rawTrailers](././http2/~/Http2ServerRequest#property_rawtrailers)
-   [read](././http2/~/Http2ServerRequest#method_read_0)
-   [scheme](././http2/~/Http2ServerRequest#property_scheme)
-   [setTimeout](././http2/~/Http2ServerRequest#method_settimeout_0)
-   [socket](././http2/~/Http2ServerRequest#property_socket)
-   [stream](././http2/~/Http2ServerRequest#property_stream)
-   [trailers](././http2/~/Http2ServerRequest#property_trailers)
-   [url](././http2/~/Http2ServerRequest#property_url)

c

[Http2ServerResponse](././http2/~/Http2ServerResponse "Http2ServerResponse")

This object is created internally by an HTTP server, not by the user. It is passed as the second parameter to the `'request'` event.

-   [addListener](././http2/~/Http2ServerResponse#method_addlistener_0)
-   [addTrailers](././http2/~/Http2ServerResponse#method_addtrailers_0)
-   [appendHeader](././http2/~/Http2ServerResponse#method_appendheader_0)
-   [connection](././http2/~/Http2ServerResponse#property_connection)
-   [createPushResponse](././http2/~/Http2ServerResponse#method_createpushresponse_0)
-   [emit](././http2/~/Http2ServerResponse#method_emit_0)
-   [end](././http2/~/Http2ServerResponse#method_end_0)
-   [finished](././http2/~/Http2ServerResponse#property_finished)
-   [getHeader](././http2/~/Http2ServerResponse#method_getheader_0)
-   [getHeaderNames](././http2/~/Http2ServerResponse#method_getheadernames_0)
-   [getHeaders](././http2/~/Http2ServerResponse#method_getheaders_0)
-   [hasHeader](././http2/~/Http2ServerResponse#method_hasheader_0)
-   [headersSent](././http2/~/Http2ServerResponse#property_headerssent)
-   [on](././http2/~/Http2ServerResponse#method_on_0)
-   [once](././http2/~/Http2ServerResponse#method_once_0)
-   [prependListener](././http2/~/Http2ServerResponse#method_prependlistener_0)
-   [prependOnceListener](././http2/~/Http2ServerResponse#method_prependoncelistener_0)
-   [removeHeader](././http2/~/Http2ServerResponse#method_removeheader_0)
-   [req](././http2/~/Http2ServerResponse#property_req)
-   [sendDate](././http2/~/Http2ServerResponse#property_senddate)
-   [setHeader](././http2/~/Http2ServerResponse#method_setheader_0)
-   [setTimeout](././http2/~/Http2ServerResponse#method_settimeout_0)
-   [socket](././http2/~/Http2ServerResponse#property_socket)
-   [statusCode](././http2/~/Http2ServerResponse#property_statuscode)
-   [statusMessage](././http2/~/Http2ServerResponse#property_statusmessage)
-   [stream](././http2/~/Http2ServerResponse#property_stream)
-   [write](././http2/~/Http2ServerResponse#method_write_0)
-   [writeContinue](././http2/~/Http2ServerResponse#method_writecontinue_0)
-   [writeEarlyHints](././http2/~/Http2ServerResponse#method_writeearlyhints_0)
-   [writeHead](././http2/~/Http2ServerResponse#method_writehead_0)

I

[Http2Session](././http2/~/Http2Session "Http2Session")

No documentation available

-   [addListener](././http2/~/Http2Session#method_addlistener_0)
-   [alpnProtocol](././http2/~/Http2Session#property_alpnprotocol)
-   [close](././http2/~/Http2Session#method_close_0)
-   [closed](././http2/~/Http2Session#property_closed)
-   [connecting](././http2/~/Http2Session#property_connecting)
-   [destroy](././http2/~/Http2Session#method_destroy_0)
-   [destroyed](././http2/~/Http2Session#property_destroyed)
-   [emit](././http2/~/Http2Session#method_emit_0)
-   [encrypted](././http2/~/Http2Session#property_encrypted)
-   [goaway](././http2/~/Http2Session#method_goaway_0)
-   [localSettings](././http2/~/Http2Session#property_localsettings)
-   [on](././http2/~/Http2Session#method_on_0)
-   [once](././http2/~/Http2Session#method_once_0)
-   [originSet](././http2/~/Http2Session#property_originset)
-   [pendingSettingsAck](././http2/~/Http2Session#property_pendingsettingsack)
-   [ping](././http2/~/Http2Session#method_ping_0)
-   [prependListener](././http2/~/Http2Session#method_prependlistener_0)
-   [prependOnceListener](././http2/~/Http2Session#method_prependoncelistener_0)
-   [ref](././http2/~/Http2Session#method_ref_0)
-   [remoteSettings](././http2/~/Http2Session#property_remotesettings)
-   [setLocalWindowSize](././http2/~/Http2Session#method_setlocalwindowsize_0)
-   [setTimeout](././http2/~/Http2Session#method_settimeout_0)
-   [settings](././http2/~/Http2Session#method_settings_0)
-   [socket](././http2/~/Http2Session#property_socket)
-   [state](././http2/~/Http2Session#property_state)
-   [type](././http2/~/Http2Session#property_type)
-   [unref](././http2/~/Http2Session#method_unref_0)

I

[Http2Stream](././http2/~/Http2Stream "Http2Stream")

No documentation available

-   [aborted](././http2/~/Http2Stream#property_aborted)
-   [addListener](././http2/~/Http2Stream#method_addlistener_0)
-   [bufferSize](././http2/~/Http2Stream#property_buffersize)
-   [close](././http2/~/Http2Stream#method_close_0)
-   [closed](././http2/~/Http2Stream#property_closed)
-   [destroyed](././http2/~/Http2Stream#property_destroyed)
-   [emit](././http2/~/Http2Stream#method_emit_0)
-   [endAfterHeaders](././http2/~/Http2Stream#property_endafterheaders)
-   [id](././http2/~/Http2Stream#property_id)
-   [on](././http2/~/Http2Stream#method_on_0)
-   [once](././http2/~/Http2Stream#method_once_0)
-   [pending](././http2/~/Http2Stream#property_pending)
-   [prependListener](././http2/~/Http2Stream#method_prependlistener_0)
-   [prependOnceListener](././http2/~/Http2Stream#method_prependoncelistener_0)
-   [priority](././http2/~/Http2Stream#method_priority_0)
-   [rstCode](././http2/~/Http2Stream#property_rstcode)
-   [sendTrailers](././http2/~/Http2Stream#method_sendtrailers_0)
-   [sentHeaders](././http2/~/Http2Stream#property_sentheaders)
-   [sentInfoHeaders](././http2/~/Http2Stream#property_sentinfoheaders)
-   [sentTrailers](././http2/~/Http2Stream#property_senttrailers)
-   [session](././http2/~/Http2Stream#property_session)
-   [setTimeout](././http2/~/Http2Stream#method_settimeout_0)
-   [state](././http2/~/Http2Stream#property_state)

I

[IncomingHttpHeaders](././http2/~/IncomingHttpHeaders "IncomingHttpHeaders")

No documentation available

-   [:authority](././http2/~/IncomingHttpHeaders#property_:authority)
-   [:method](././http2/~/IncomingHttpHeaders#property_:method)
-   [:path](././http2/~/IncomingHttpHeaders#property_:path)
-   [:scheme](././http2/~/IncomingHttpHeaders#property_:scheme)

I

[IncomingHttpStatusHeader](././http2/~/IncomingHttpStatusHeader "IncomingHttpStatusHeader")

No documentation available

-   [:status](././http2/~/IncomingHttpStatusHeader#property_:status)

f

[performServerHandshake](././http2/~/performServerHandshake "performServerHandshake")

Create an HTTP/2 server session from an existing socket.

I

[SecureClientSessionOptions](././http2/~/SecureClientSessionOptions "SecureClientSessionOptions")

No documentation available

I

[SecureServerOptions](././http2/~/SecureServerOptions "SecureServerOptions")

No documentation available

-   [allowHTTP1](././http2/~/SecureServerOptions#property_allowhttp1)
-   [origins](././http2/~/SecureServerOptions#property_origins)

I

[SecureServerSessionOptions](././http2/~/SecureServerSessionOptions "SecureServerSessionOptions")

No documentation available

v

[sensitiveHeaders](././http2/~/sensitiveHeaders "sensitiveHeaders")

This symbol can be set as a property on the HTTP/2 headers object with an array value in order to provide a list of headers considered sensitive.

I

[ServerHttp2Session](././http2/~/ServerHttp2Session "ServerHttp2Session")

No documentation available

-   [addListener](././http2/~/ServerHttp2Session#method_addlistener_0)
-   [altsvc](././http2/~/ServerHttp2Session#method_altsvc_0)
-   [emit](././http2/~/ServerHttp2Session#method_emit_0)
-   [on](././http2/~/ServerHttp2Session#method_on_0)
-   [once](././http2/~/ServerHttp2Session#method_once_0)
-   [origin](././http2/~/ServerHttp2Session#method_origin_0)
-   [prependListener](././http2/~/ServerHttp2Session#method_prependlistener_0)
-   [prependOnceListener](././http2/~/ServerHttp2Session#method_prependoncelistener_0)
-   [server](././http2/~/ServerHttp2Session#property_server)

I

[ServerHttp2Stream](././http2/~/ServerHttp2Stream "ServerHttp2Stream")

No documentation available

-   [additionalHeaders](././http2/~/ServerHttp2Stream#method_additionalheaders_0)
-   [headersSent](././http2/~/ServerHttp2Stream#property_headerssent)
-   [pushAllowed](././http2/~/ServerHttp2Stream#property_pushallowed)
-   [pushStream](././http2/~/ServerHttp2Stream#method_pushstream_0)
-   [respond](././http2/~/ServerHttp2Stream#method_respond_0)
-   [respondWithFD](././http2/~/ServerHttp2Stream#method_respondwithfd_0)
-   [respondWithFile](././http2/~/ServerHttp2Stream#method_respondwithfile_0)

I

[ServerOptions](././http2/~/ServerOptions "ServerOptions")

No documentation available

-   [streamResetBurst](././http2/~/ServerOptions#property_streamresetburst)
-   [streamResetRate](././http2/~/ServerOptions#property_streamresetrate)

I

[ServerSessionOptions](././http2/~/ServerSessionOptions "ServerSessionOptions")

No documentation available

-   [Http1IncomingMessage](././http2/~/ServerSessionOptions#property_http1incomingmessage)
-   [Http1ServerResponse](././http2/~/ServerSessionOptions#property_http1serverresponse)
-   [Http2ServerRequest](././http2/~/ServerSessionOptions#property_http2serverrequest)
-   [Http2ServerResponse](././http2/~/ServerSessionOptions#property_http2serverresponse)

I

[ServerStreamFileResponseOptions](././http2/~/ServerStreamFileResponseOptions "ServerStreamFileResponseOptions")

No documentation available

-   [length](././http2/~/ServerStreamFileResponseOptions#property_length)
-   [offset](././http2/~/ServerStreamFileResponseOptions#property_offset)
-   [statCheck](././http2/~/ServerStreamFileResponseOptions#method_statcheck_0)
-   [waitForTrailers](././http2/~/ServerStreamFileResponseOptions#property_waitfortrailers)

I

[ServerStreamFileResponseOptionsWithError](././http2/~/ServerStreamFileResponseOptionsWithError "ServerStreamFileResponseOptionsWithError")

No documentation available

-   [onError](././http2/~/ServerStreamFileResponseOptionsWithError#method_onerror_0)

I

[ServerStreamResponseOptions](././http2/~/ServerStreamResponseOptions "ServerStreamResponseOptions")

No documentation available

-   [endStream](././http2/~/ServerStreamResponseOptions#property_endstream)
-   [waitForTrailers](././http2/~/ServerStreamResponseOptions#property_waitfortrailers)

I

[SessionOptions](././http2/~/SessionOptions "SessionOptions")

No documentation available

-   [maxDeflateDynamicTableSize](././http2/~/SessionOptions#property_maxdeflatedynamictablesize)
-   [maxHeaderListPairs](././http2/~/SessionOptions#property_maxheaderlistpairs)
-   [maxOutstandingPings](././http2/~/SessionOptions#property_maxoutstandingpings)
-   [maxSendHeaderBlockLength](././http2/~/SessionOptions#property_maxsendheaderblocklength)
-   [maxSessionMemory](././http2/~/SessionOptions#property_maxsessionmemory)
-   [paddingStrategy](././http2/~/SessionOptions#property_paddingstrategy)
-   [peerMaxConcurrentStreams](././http2/~/SessionOptions#property_peermaxconcurrentstreams)
-   [remoteCustomSettings](././http2/~/SessionOptions#property_remotecustomsettings)
-   [selectPadding](././http2/~/SessionOptions#method_selectpadding_0)
-   [settings](././http2/~/SessionOptions#property_settings)
-   [unknownProtocolTimeout](././http2/~/SessionOptions#property_unknownprotocoltimeout)

I

[SessionState](././http2/~/SessionState "SessionState")

No documentation available

-   [deflateDynamicTableSize](././http2/~/SessionState#property_deflatedynamictablesize)
-   [effectiveLocalWindowSize](././http2/~/SessionState#property_effectivelocalwindowsize)
-   [effectiveRecvDataLength](././http2/~/SessionState#property_effectiverecvdatalength)
-   [inflateDynamicTableSize](././http2/~/SessionState#property_inflatedynamictablesize)
-   [lastProcStreamID](././http2/~/SessionState#property_lastprocstreamid)
-   [localWindowSize](././http2/~/SessionState#property_localwindowsize)
-   [nextStreamID](././http2/~/SessionState#property_nextstreamid)
-   [outboundQueueSize](././http2/~/SessionState#property_outboundqueuesize)
-   [remoteWindowSize](././http2/~/SessionState#property_remotewindowsize)

I

[Settings](././http2/~/Settings "Settings")

No documentation available

-   [enableConnectProtocol](././http2/~/Settings#property_enableconnectprotocol)
-   [enablePush](././http2/~/Settings#property_enablepush)
-   [headerTableSize](././http2/~/Settings#property_headertablesize)
-   [initialWindowSize](././http2/~/Settings#property_initialwindowsize)
-   [maxConcurrentStreams](././http2/~/Settings#property_maxconcurrentstreams)
-   [maxFrameSize](././http2/~/Settings#property_maxframesize)
-   [maxHeaderListSize](././http2/~/Settings#property_maxheaderlistsize)

I

[StatOptions](././http2/~/StatOptions "StatOptions")

No documentation available

-   [length](././http2/~/StatOptions#property_length)
-   [offset](././http2/~/StatOptions#property_offset)

I

[StreamPriorityOptions](././http2/~/StreamPriorityOptions "StreamPriorityOptions")

No documentation available

-   [exclusive](././http2/~/StreamPriorityOptions#property_exclusive)
-   [parent](././http2/~/StreamPriorityOptions#property_parent)
-   [silent](././http2/~/StreamPriorityOptions#property_silent)
-   [weight](././http2/~/StreamPriorityOptions#property_weight)

I

[StreamState](././http2/~/StreamState "StreamState")

No documentation available

-   [localClose](././http2/~/StreamState#property_localclose)
-   [localWindowSize](././http2/~/StreamState#property_localwindowsize)
-   [remoteClose](././http2/~/StreamState#property_remoteclose)
-   [state](././http2/~/StreamState#property_state)
-   [sumDependencyWeight](././http2/~/StreamState#property_sumdependencyweight)
-   [weight](././http2/~/StreamState#property_weight)

HTTPS is the HTTP protocol over TLS/SSL. In Node.js this is implemented as a separate module.

c

[Agent](././https/~/Agent "Agent")

An `Agent` object for HTTPS similar to `http.Agent`. See [request](././https/~/request) for more information.

-   [options](././https/~/Agent#property_options)

I

[AgentOptions](././https/~/AgentOptions "AgentOptions")

No documentation available

-   [maxCachedSessions](././https/~/AgentOptions#property_maxcachedsessions)

f

[createServer](././https/~/createServer "createServer")

Or

f

[get](././https/~/get "get")

Like `http.get()` but for HTTPS.

v

[globalAgent](././https/~/globalAgent "globalAgent")

No documentation available

f

[request](././https/~/request "request")

Makes a request to a secure web server.

T

[RequestOptions](././https/~/RequestOptions "RequestOptions")

No documentation available

c

I

[Server](././https/~/Server "Server")

No documentation available

-   [addListener](././https/~/Server#method_addlistener_0)
-   [closeAllConnections](././https/~/Server#method_closeallconnections_0)
-   [closeIdleConnections](././https/~/Server#method_closeidleconnections_0)
-   [emit](././https/~/Server#method_emit_0)
-   [on](././https/~/Server#method_on_0)
-   [once](././https/~/Server#method_once_0)
-   [prependListener](././https/~/Server#method_prependlistener_0)
-   [prependOnceListener](././https/~/Server#method_prependoncelistener_0)

T

[ServerOptions](././https/~/ServerOptions "ServerOptions")

No documentation available

f

[close](././inspector/~/close "close")

Deactivate the inspector. Blocks until there are no active connections.

N

[Console](././inspector/~/Console "Console")

No documentation available

v

[console](././inspector/~/console "console")

An object to send messages to the remote inspector console.

I

[Console.ConsoleMessage](././inspector/~/Console.ConsoleMessage "Console.ConsoleMessage")

Console message.

-   [column](././inspector/~/Console.ConsoleMessage#property_column)
-   [level](././inspector/~/Console.ConsoleMessage#property_level)
-   [line](././inspector/~/Console.ConsoleMessage#property_line)
-   [source](././inspector/~/Console.ConsoleMessage#property_source)
-   [text](././inspector/~/Console.ConsoleMessage#property_text)
-   [url](././inspector/~/Console.ConsoleMessage#property_url)

I

[Console.MessageAddedEventDataType](././inspector/~/Console.MessageAddedEventDataType "Console.MessageAddedEventDataType")

No documentation available

-   [message](././inspector/~/Console.MessageAddedEventDataType#property_message)

N

[Debugger](././inspector/~/Debugger "Debugger")

No documentation available

I

[Debugger.BreakLocation](././inspector/~/Debugger.BreakLocation "Debugger.BreakLocation")

No documentation available

-   [columnNumber](././inspector/~/Debugger.BreakLocation#property_columnnumber)
-   [lineNumber](././inspector/~/Debugger.BreakLocation#property_linenumber)
-   [scriptId](././inspector/~/Debugger.BreakLocation#property_scriptid)
-   [type](././inspector/~/Debugger.BreakLocation#property_type)

T

[Debugger.BreakpointId](././inspector/~/Debugger.BreakpointId "Debugger.BreakpointId")

Breakpoint identifier.

I

[Debugger.BreakpointResolvedEventDataType](././inspector/~/Debugger.BreakpointResolvedEventDataType "Debugger.BreakpointResolvedEventDataType")

No documentation available

-   [breakpointId](././inspector/~/Debugger.BreakpointResolvedEventDataType#property_breakpointid)
-   [location](././inspector/~/Debugger.BreakpointResolvedEventDataType#property_location)

I

[Debugger.CallFrame](././inspector/~/Debugger.CallFrame "Debugger.CallFrame")

JavaScript call frame. Array of call frames form the call stack.

-   [callFrameId](././inspector/~/Debugger.CallFrame#property_callframeid)
-   [functionLocation](././inspector/~/Debugger.CallFrame#property_functionlocation)
-   [functionName](././inspector/~/Debugger.CallFrame#property_functionname)
-   [location](././inspector/~/Debugger.CallFrame#property_location)
-   [returnValue](././inspector/~/Debugger.CallFrame#property_returnvalue)
-   [scopeChain](././inspector/~/Debugger.CallFrame#property_scopechain)
-   [this](././inspector/~/Debugger.CallFrame#property_this)
-   [url](././inspector/~/Debugger.CallFrame#property_url)

T

[Debugger.CallFrameId](././inspector/~/Debugger.CallFrameId "Debugger.CallFrameId")

Call frame identifier.

I

[Debugger.ContinueToLocationParameterType](././inspector/~/Debugger.ContinueToLocationParameterType "Debugger.ContinueToLocationParameterType")

No documentation available

-   [location](././inspector/~/Debugger.ContinueToLocationParameterType#property_location)
-   [targetCallFrames](././inspector/~/Debugger.ContinueToLocationParameterType#property_targetcallframes)

I

[Debugger.EnableReturnType](././inspector/~/Debugger.EnableReturnType "Debugger.EnableReturnType")

No documentation available

-   [debuggerId](././inspector/~/Debugger.EnableReturnType#property_debuggerid)

I

[Debugger.EvaluateOnCallFrameParameterType](././inspector/~/Debugger.EvaluateOnCallFrameParameterType "Debugger.EvaluateOnCallFrameParameterType")

No documentation available

-   [callFrameId](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_callframeid)
-   [expression](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_expression)
-   [generatePreview](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_generatepreview)
-   [includeCommandLineAPI](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_includecommandlineapi)
-   [objectGroup](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_objectgroup)
-   [returnByValue](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_returnbyvalue)
-   [silent](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_silent)
-   [throwOnSideEffect](././inspector/~/Debugger.EvaluateOnCallFrameParameterType#property_throwonsideeffect)

I

[Debugger.EvaluateOnCallFrameReturnType](././inspector/~/Debugger.EvaluateOnCallFrameReturnType "Debugger.EvaluateOnCallFrameReturnType")

No documentation available

-   [exceptionDetails](././inspector/~/Debugger.EvaluateOnCallFrameReturnType#property_exceptiondetails)
-   [result](././inspector/~/Debugger.EvaluateOnCallFrameReturnType#property_result)

I

[Debugger.GetPossibleBreakpointsParameterType](././inspector/~/Debugger.GetPossibleBreakpointsParameterType "Debugger.GetPossibleBreakpointsParameterType")

No documentation available

-   [end](././inspector/~/Debugger.GetPossibleBreakpointsParameterType#property_end)
-   [restrictToFunction](././inspector/~/Debugger.GetPossibleBreakpointsParameterType#property_restricttofunction)
-   [start](././inspector/~/Debugger.GetPossibleBreakpointsParameterType#property_start)

I

[Debugger.GetPossibleBreakpointsReturnType](././inspector/~/Debugger.GetPossibleBreakpointsReturnType "Debugger.GetPossibleBreakpointsReturnType")

No documentation available

-   [locations](././inspector/~/Debugger.GetPossibleBreakpointsReturnType#property_locations)

I

[Debugger.GetScriptSourceParameterType](././inspector/~/Debugger.GetScriptSourceParameterType "Debugger.GetScriptSourceParameterType")

No documentation available

-   [scriptId](././inspector/~/Debugger.GetScriptSourceParameterType#property_scriptid)

I

[Debugger.GetScriptSourceReturnType](././inspector/~/Debugger.GetScriptSourceReturnType "Debugger.GetScriptSourceReturnType")

No documentation available

-   [scriptSource](././inspector/~/Debugger.GetScriptSourceReturnType#property_scriptsource)

I

[Debugger.GetStackTraceParameterType](././inspector/~/Debugger.GetStackTraceParameterType "Debugger.GetStackTraceParameterType")

No documentation available

-   [stackTraceId](././inspector/~/Debugger.GetStackTraceParameterType#property_stacktraceid)

I

[Debugger.GetStackTraceReturnType](././inspector/~/Debugger.GetStackTraceReturnType "Debugger.GetStackTraceReturnType")

No documentation available

-   [stackTrace](././inspector/~/Debugger.GetStackTraceReturnType#property_stacktrace)

I

[Debugger.Location](././inspector/~/Debugger.Location "Debugger.Location")

Location in the source code.

-   [columnNumber](././inspector/~/Debugger.Location#property_columnnumber)
-   [lineNumber](././inspector/~/Debugger.Location#property_linenumber)
-   [scriptId](././inspector/~/Debugger.Location#property_scriptid)

I

[Debugger.PausedEventDataType](././inspector/~/Debugger.PausedEventDataType "Debugger.PausedEventDataType")

No documentation available

-   [asyncCallStackTraceId](././inspector/~/Debugger.PausedEventDataType#property_asynccallstacktraceid)
-   [asyncStackTrace](././inspector/~/Debugger.PausedEventDataType#property_asyncstacktrace)
-   [asyncStackTraceId](././inspector/~/Debugger.PausedEventDataType#property_asyncstacktraceid)
-   [callFrames](././inspector/~/Debugger.PausedEventDataType#property_callframes)
-   [data](././inspector/~/Debugger.PausedEventDataType#property_data)
-   [hitBreakpoints](././inspector/~/Debugger.PausedEventDataType#property_hitbreakpoints)
-   [reason](././inspector/~/Debugger.PausedEventDataType#property_reason)

I

[Debugger.PauseOnAsyncCallParameterType](././inspector/~/Debugger.PauseOnAsyncCallParameterType "Debugger.PauseOnAsyncCallParameterType")

No documentation available

-   [parentStackTraceId](././inspector/~/Debugger.PauseOnAsyncCallParameterType#property_parentstacktraceid)

I

[Debugger.RemoveBreakpointParameterType](././inspector/~/Debugger.RemoveBreakpointParameterType "Debugger.RemoveBreakpointParameterType")

No documentation available

-   [breakpointId](././inspector/~/Debugger.RemoveBreakpointParameterType#property_breakpointid)

I

[Debugger.RestartFrameParameterType](././inspector/~/Debugger.RestartFrameParameterType "Debugger.RestartFrameParameterType")

No documentation available

-   [callFrameId](././inspector/~/Debugger.RestartFrameParameterType#property_callframeid)

I

[Debugger.RestartFrameReturnType](././inspector/~/Debugger.RestartFrameReturnType "Debugger.RestartFrameReturnType")

No documentation available

-   [asyncStackTrace](././inspector/~/Debugger.RestartFrameReturnType#property_asyncstacktrace)
-   [asyncStackTraceId](././inspector/~/Debugger.RestartFrameReturnType#property_asyncstacktraceid)
-   [callFrames](././inspector/~/Debugger.RestartFrameReturnType#property_callframes)

I

[Debugger.Scope](././inspector/~/Debugger.Scope "Debugger.Scope")

Scope description.

-   [endLocation](././inspector/~/Debugger.Scope#property_endlocation)
-   [name](././inspector/~/Debugger.Scope#property_name)
-   [object](././inspector/~/Debugger.Scope#property_object)
-   [startLocation](././inspector/~/Debugger.Scope#property_startlocation)
-   [type](././inspector/~/Debugger.Scope#property_type)

I

[Debugger.ScriptFailedToParseEventDataType](././inspector/~/Debugger.ScriptFailedToParseEventDataType "Debugger.ScriptFailedToParseEventDataType")

No documentation available

-   [endColumn](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_endcolumn)
-   [endLine](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_endline)
-   [executionContextAuxData](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextauxdata)
-   [executionContextId](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextid)
-   [hasSourceURL](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_hassourceurl)
-   [hash](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_hash)
-   [isModule](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_ismodule)
-   [length](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_length)
-   [scriptId](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_scriptid)
-   [sourceMapURL](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_sourcemapurl)
-   [stackTrace](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_stacktrace)
-   [startColumn](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_startcolumn)
-   [startLine](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_startline)
-   [url](././inspector/~/Debugger.ScriptFailedToParseEventDataType#property_url)

I

[Debugger.ScriptParsedEventDataType](././inspector/~/Debugger.ScriptParsedEventDataType "Debugger.ScriptParsedEventDataType")

No documentation available

-   [endColumn](././inspector/~/Debugger.ScriptParsedEventDataType#property_endcolumn)
-   [endLine](././inspector/~/Debugger.ScriptParsedEventDataType#property_endline)
-   [executionContextAuxData](././inspector/~/Debugger.ScriptParsedEventDataType#property_executioncontextauxdata)
-   [executionContextId](././inspector/~/Debugger.ScriptParsedEventDataType#property_executioncontextid)
-   [hasSourceURL](././inspector/~/Debugger.ScriptParsedEventDataType#property_hassourceurl)
-   [hash](././inspector/~/Debugger.ScriptParsedEventDataType#property_hash)
-   [isLiveEdit](././inspector/~/Debugger.ScriptParsedEventDataType#property_isliveedit)
-   [isModule](././inspector/~/Debugger.ScriptParsedEventDataType#property_ismodule)
-   [length](././inspector/~/Debugger.ScriptParsedEventDataType#property_length)
-   [scriptId](././inspector/~/Debugger.ScriptParsedEventDataType#property_scriptid)
-   [sourceMapURL](././inspector/~/Debugger.ScriptParsedEventDataType#property_sourcemapurl)
-   [stackTrace](././inspector/~/Debugger.ScriptParsedEventDataType#property_stacktrace)
-   [startColumn](././inspector/~/Debugger.ScriptParsedEventDataType#property_startcolumn)
-   [startLine](././inspector/~/Debugger.ScriptParsedEventDataType#property_startline)
-   [url](././inspector/~/Debugger.ScriptParsedEventDataType#property_url)

I

[Debugger.ScriptPosition](././inspector/~/Debugger.ScriptPosition "Debugger.ScriptPosition")

Location in the source code.

-   [columnNumber](././inspector/~/Debugger.ScriptPosition#property_columnnumber)
-   [lineNumber](././inspector/~/Debugger.ScriptPosition#property_linenumber)

I

[Debugger.SearchInContentParameterType](././inspector/~/Debugger.SearchInContentParameterType "Debugger.SearchInContentParameterType")

No documentation available

-   [caseSensitive](././inspector/~/Debugger.SearchInContentParameterType#property_casesensitive)
-   [isRegex](././inspector/~/Debugger.SearchInContentParameterType#property_isregex)
-   [query](././inspector/~/Debugger.SearchInContentParameterType#property_query)
-   [scriptId](././inspector/~/Debugger.SearchInContentParameterType#property_scriptid)

I

[Debugger.SearchInContentReturnType](././inspector/~/Debugger.SearchInContentReturnType "Debugger.SearchInContentReturnType")

No documentation available

-   [result](././inspector/~/Debugger.SearchInContentReturnType#property_result)

I

[Debugger.SearchMatch](././inspector/~/Debugger.SearchMatch "Debugger.SearchMatch")

Search match for resource.

-   [lineContent](././inspector/~/Debugger.SearchMatch#property_linecontent)
-   [lineNumber](././inspector/~/Debugger.SearchMatch#property_linenumber)

I

[Debugger.SetAsyncCallStackDepthParameterType](././inspector/~/Debugger.SetAsyncCallStackDepthParameterType "Debugger.SetAsyncCallStackDepthParameterType")

No documentation available

-   [maxDepth](././inspector/~/Debugger.SetAsyncCallStackDepthParameterType#property_maxdepth)

I

[Debugger.SetBlackboxedRangesParameterType](././inspector/~/Debugger.SetBlackboxedRangesParameterType "Debugger.SetBlackboxedRangesParameterType")

No documentation available

-   [positions](././inspector/~/Debugger.SetBlackboxedRangesParameterType#property_positions)
-   [scriptId](././inspector/~/Debugger.SetBlackboxedRangesParameterType#property_scriptid)

I

[Debugger.SetBlackboxPatternsParameterType](././inspector/~/Debugger.SetBlackboxPatternsParameterType "Debugger.SetBlackboxPatternsParameterType")

No documentation available

-   [patterns](././inspector/~/Debugger.SetBlackboxPatternsParameterType#property_patterns)

I

[Debugger.SetBreakpointByUrlParameterType](././inspector/~/Debugger.SetBreakpointByUrlParameterType "Debugger.SetBreakpointByUrlParameterType")

No documentation available

-   [columnNumber](././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_columnnumber)
-   [condition](././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_condition)
-   [lineNumber](././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_linenumber)
-   [scriptHash](././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_scripthash)
-   [url](././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_url)
-   [urlRegex](././inspector/~/Debugger.SetBreakpointByUrlParameterType#property_urlregex)

I

[Debugger.SetBreakpointByUrlReturnType](././inspector/~/Debugger.SetBreakpointByUrlReturnType "Debugger.SetBreakpointByUrlReturnType")

No documentation available

-   [breakpointId](././inspector/~/Debugger.SetBreakpointByUrlReturnType#property_breakpointid)
-   [locations](././inspector/~/Debugger.SetBreakpointByUrlReturnType#property_locations)

I

[Debugger.SetBreakpointParameterType](././inspector/~/Debugger.SetBreakpointParameterType "Debugger.SetBreakpointParameterType")

No documentation available

-   [condition](././inspector/~/Debugger.SetBreakpointParameterType#property_condition)
-   [location](././inspector/~/Debugger.SetBreakpointParameterType#property_location)

I

[Debugger.SetBreakpointReturnType](././inspector/~/Debugger.SetBreakpointReturnType "Debugger.SetBreakpointReturnType")

No documentation available

-   [actualLocation](././inspector/~/Debugger.SetBreakpointReturnType#property_actuallocation)
-   [breakpointId](././inspector/~/Debugger.SetBreakpointReturnType#property_breakpointid)

I

[Debugger.SetBreakpointsActiveParameterType](././inspector/~/Debugger.SetBreakpointsActiveParameterType "Debugger.SetBreakpointsActiveParameterType")

No documentation available

-   [active](././inspector/~/Debugger.SetBreakpointsActiveParameterType#property_active)

I

[Debugger.SetPauseOnExceptionsParameterType](././inspector/~/Debugger.SetPauseOnExceptionsParameterType "Debugger.SetPauseOnExceptionsParameterType")

No documentation available

-   [state](././inspector/~/Debugger.SetPauseOnExceptionsParameterType#property_state)

I

[Debugger.SetReturnValueParameterType](././inspector/~/Debugger.SetReturnValueParameterType "Debugger.SetReturnValueParameterType")

No documentation available

-   [newValue](././inspector/~/Debugger.SetReturnValueParameterType#property_newvalue)

I

[Debugger.SetScriptSourceParameterType](././inspector/~/Debugger.SetScriptSourceParameterType "Debugger.SetScriptSourceParameterType")

No documentation available

-   [dryRun](././inspector/~/Debugger.SetScriptSourceParameterType#property_dryrun)
-   [scriptId](././inspector/~/Debugger.SetScriptSourceParameterType#property_scriptid)
-   [scriptSource](././inspector/~/Debugger.SetScriptSourceParameterType#property_scriptsource)

I

[Debugger.SetScriptSourceReturnType](././inspector/~/Debugger.SetScriptSourceReturnType "Debugger.SetScriptSourceReturnType")

No documentation available

-   [asyncStackTrace](././inspector/~/Debugger.SetScriptSourceReturnType#property_asyncstacktrace)
-   [asyncStackTraceId](././inspector/~/Debugger.SetScriptSourceReturnType#property_asyncstacktraceid)
-   [callFrames](././inspector/~/Debugger.SetScriptSourceReturnType#property_callframes)
-   [exceptionDetails](././inspector/~/Debugger.SetScriptSourceReturnType#property_exceptiondetails)
-   [stackChanged](././inspector/~/Debugger.SetScriptSourceReturnType#property_stackchanged)

I

[Debugger.SetSkipAllPausesParameterType](././inspector/~/Debugger.SetSkipAllPausesParameterType "Debugger.SetSkipAllPausesParameterType")

No documentation available

-   [skip](././inspector/~/Debugger.SetSkipAllPausesParameterType#property_skip)

I

[Debugger.SetVariableValueParameterType](././inspector/~/Debugger.SetVariableValueParameterType "Debugger.SetVariableValueParameterType")

No documentation available

-   [callFrameId](././inspector/~/Debugger.SetVariableValueParameterType#property_callframeid)
-   [newValue](././inspector/~/Debugger.SetVariableValueParameterType#property_newvalue)
-   [scopeNumber](././inspector/~/Debugger.SetVariableValueParameterType#property_scopenumber)
-   [variableName](././inspector/~/Debugger.SetVariableValueParameterType#property_variablename)

I

[Debugger.StepIntoParameterType](././inspector/~/Debugger.StepIntoParameterType "Debugger.StepIntoParameterType")

No documentation available

-   [breakOnAsyncCall](././inspector/~/Debugger.StepIntoParameterType#property_breakonasynccall)

N

[HeapProfiler](././inspector/~/HeapProfiler "HeapProfiler")

No documentation available

I

[HeapProfiler.AddHeapSnapshotChunkEventDataType](././inspector/~/HeapProfiler.AddHeapSnapshotChunkEventDataType "HeapProfiler.AddHeapSnapshotChunkEventDataType")

No documentation available

-   [chunk](././inspector/~/HeapProfiler.AddHeapSnapshotChunkEventDataType#property_chunk)

I

[HeapProfiler.AddInspectedHeapObjectParameterType](././inspector/~/HeapProfiler.AddInspectedHeapObjectParameterType "HeapProfiler.AddInspectedHeapObjectParameterType")

No documentation available

-   [heapObjectId](././inspector/~/HeapProfiler.AddInspectedHeapObjectParameterType#property_heapobjectid)

I

[HeapProfiler.GetHeapObjectIdParameterType](././inspector/~/HeapProfiler.GetHeapObjectIdParameterType "HeapProfiler.GetHeapObjectIdParameterType")

No documentation available

-   [objectId](././inspector/~/HeapProfiler.GetHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetHeapObjectIdReturnType](././inspector/~/HeapProfiler.GetHeapObjectIdReturnType "HeapProfiler.GetHeapObjectIdReturnType")

No documentation available

-   [heapSnapshotObjectId](././inspector/~/HeapProfiler.GetHeapObjectIdReturnType#property_heapsnapshotobjectid)

I

[HeapProfiler.GetObjectByHeapObjectIdParameterType](././inspector/~/HeapProfiler.GetObjectByHeapObjectIdParameterType "HeapProfiler.GetObjectByHeapObjectIdParameterType")

No documentation available

-   [objectGroup](././inspector/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectgroup)
-   [objectId](././inspector/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetObjectByHeapObjectIdReturnType](././inspector/~/HeapProfiler.GetObjectByHeapObjectIdReturnType "HeapProfiler.GetObjectByHeapObjectIdReturnType")

No documentation available

-   [result](././inspector/~/HeapProfiler.GetObjectByHeapObjectIdReturnType#property_result)

I

[HeapProfiler.GetSamplingProfileReturnType](././inspector/~/HeapProfiler.GetSamplingProfileReturnType "HeapProfiler.GetSamplingProfileReturnType")

No documentation available

-   [profile](././inspector/~/HeapProfiler.GetSamplingProfileReturnType#property_profile)

T

[HeapProfiler.HeapSnapshotObjectId](././inspector/~/HeapProfiler.HeapSnapshotObjectId "HeapProfiler.HeapSnapshotObjectId")

Heap snapshot object id.

I

[HeapProfiler.HeapStatsUpdateEventDataType](././inspector/~/HeapProfiler.HeapStatsUpdateEventDataType "HeapProfiler.HeapStatsUpdateEventDataType")

No documentation available

-   [statsUpdate](././inspector/~/HeapProfiler.HeapStatsUpdateEventDataType#property_statsupdate)

I

[HeapProfiler.LastSeenObjectIdEventDataType](././inspector/~/HeapProfiler.LastSeenObjectIdEventDataType "HeapProfiler.LastSeenObjectIdEventDataType")

No documentation available

-   [lastSeenObjectId](././inspector/~/HeapProfiler.LastSeenObjectIdEventDataType#property_lastseenobjectid)
-   [timestamp](././inspector/~/HeapProfiler.LastSeenObjectIdEventDataType#property_timestamp)

I

[HeapProfiler.ReportHeapSnapshotProgressEventDataType](././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType "HeapProfiler.ReportHeapSnapshotProgressEventDataType")

No documentation available

-   [done](././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_done)
-   [finished](././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_finished)
-   [total](././inspector/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_total)

I

[HeapProfiler.SamplingHeapProfile](././inspector/~/HeapProfiler.SamplingHeapProfile "HeapProfiler.SamplingHeapProfile")

Profile.

-   [head](././inspector/~/HeapProfiler.SamplingHeapProfile#property_head)

I

[HeapProfiler.SamplingHeapProfileNode](././inspector/~/HeapProfiler.SamplingHeapProfileNode "HeapProfiler.SamplingHeapProfileNode")

Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.

-   [callFrame](././inspector/~/HeapProfiler.SamplingHeapProfileNode#property_callframe)
-   [children](././inspector/~/HeapProfiler.SamplingHeapProfileNode#property_children)
-   [selfSize](././inspector/~/HeapProfiler.SamplingHeapProfileNode#property_selfsize)

I

[HeapProfiler.StartSamplingParameterType](././inspector/~/HeapProfiler.StartSamplingParameterType "HeapProfiler.StartSamplingParameterType")

No documentation available

-   [samplingInterval](././inspector/~/HeapProfiler.StartSamplingParameterType#property_samplinginterval)

I

[HeapProfiler.StartTrackingHeapObjectsParameterType](././inspector/~/HeapProfiler.StartTrackingHeapObjectsParameterType "HeapProfiler.StartTrackingHeapObjectsParameterType")

No documentation available

-   [trackAllocations](././inspector/~/HeapProfiler.StartTrackingHeapObjectsParameterType#property_trackallocations)

I

[HeapProfiler.StopSamplingReturnType](././inspector/~/HeapProfiler.StopSamplingReturnType "HeapProfiler.StopSamplingReturnType")

No documentation available

-   [profile](././inspector/~/HeapProfiler.StopSamplingReturnType#property_profile)

I

[HeapProfiler.StopTrackingHeapObjectsParameterType](././inspector/~/HeapProfiler.StopTrackingHeapObjectsParameterType "HeapProfiler.StopTrackingHeapObjectsParameterType")

No documentation available

-   [reportProgress](././inspector/~/HeapProfiler.StopTrackingHeapObjectsParameterType#property_reportprogress)

I

[HeapProfiler.TakeHeapSnapshotParameterType](././inspector/~/HeapProfiler.TakeHeapSnapshotParameterType "HeapProfiler.TakeHeapSnapshotParameterType")

No documentation available

-   [reportProgress](././inspector/~/HeapProfiler.TakeHeapSnapshotParameterType#property_reportprogress)

I

[InspectorConsole](././inspector/~/InspectorConsole "InspectorConsole")

No documentation available

-   [assert](././inspector/~/InspectorConsole#method_assert_0)
-   [clear](././inspector/~/InspectorConsole#method_clear_0)
-   [count](././inspector/~/InspectorConsole#method_count_0)
-   [countReset](././inspector/~/InspectorConsole#method_countreset_0)
-   [debug](././inspector/~/InspectorConsole#method_debug_0)
-   [dir](././inspector/~/InspectorConsole#method_dir_0)
-   [dirxml](././inspector/~/InspectorConsole#method_dirxml_0)
-   [error](././inspector/~/InspectorConsole#method_error_0)
-   [group](././inspector/~/InspectorConsole#method_group_0)
-   [groupCollapsed](././inspector/~/InspectorConsole#method_groupcollapsed_0)
-   [groupEnd](././inspector/~/InspectorConsole#method_groupend_0)
-   [info](././inspector/~/InspectorConsole#method_info_0)
-   [log](././inspector/~/InspectorConsole#method_log_0)
-   [profile](././inspector/~/InspectorConsole#method_profile_0)
-   [profileEnd](././inspector/~/InspectorConsole#method_profileend_0)
-   [table](././inspector/~/InspectorConsole#method_table_0)
-   [time](././inspector/~/InspectorConsole#method_time_0)
-   [timeLog](././inspector/~/InspectorConsole#method_timelog_0)
-   [timeStamp](././inspector/~/InspectorConsole#method_timestamp_0)
-   [trace](././inspector/~/InspectorConsole#method_trace_0)
-   [warn](././inspector/~/InspectorConsole#method_warn_0)

I

[InspectorNotification](././inspector/~/InspectorNotification "InspectorNotification")

No documentation available

-   [method](././inspector/~/InspectorNotification#property_method)
-   [params](././inspector/~/InspectorNotification#property_params)

N

[Network](././inspector/~/Network "Network")

No documentation available

I

[Network.Headers](././inspector/~/Network.Headers "Network.Headers")

Request / response headers as keys / values of JSON object.

f

[Network.loadingFailed](././inspector/~/Network.loadingFailed "Network.loadingFailed")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.LoadingFailedEventDataType](././inspector/~/Network.LoadingFailedEventDataType "Network.LoadingFailedEventDataType")

No documentation available

-   [errorText](././inspector/~/Network.LoadingFailedEventDataType#property_errortext)
-   [requestId](././inspector/~/Network.LoadingFailedEventDataType#property_requestid)
-   [timestamp](././inspector/~/Network.LoadingFailedEventDataType#property_timestamp)
-   [type](././inspector/~/Network.LoadingFailedEventDataType#property_type)

f

[Network.loadingFinished](././inspector/~/Network.loadingFinished "Network.loadingFinished")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.LoadingFinishedEventDataType](././inspector/~/Network.LoadingFinishedEventDataType "Network.LoadingFinishedEventDataType")

No documentation available

-   [requestId](././inspector/~/Network.LoadingFinishedEventDataType#property_requestid)
-   [timestamp](././inspector/~/Network.LoadingFinishedEventDataType#property_timestamp)

T

[Network.MonotonicTime](././inspector/~/Network.MonotonicTime "Network.MonotonicTime")

Monotonically increasing time in seconds since an arbitrary point in the past.

I

[Network.Request](././inspector/~/Network.Request "Network.Request")

HTTP request data.

-   [headers](././inspector/~/Network.Request#property_headers)
-   [method](././inspector/~/Network.Request#property_method)
-   [url](././inspector/~/Network.Request#property_url)

T

[Network.RequestId](././inspector/~/Network.RequestId "Network.RequestId")

Unique request identifier.

f

[Network.requestWillBeSent](././inspector/~/Network.requestWillBeSent "Network.requestWillBeSent")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.RequestWillBeSentEventDataType](././inspector/~/Network.RequestWillBeSentEventDataType "Network.RequestWillBeSentEventDataType")

No documentation available

-   [request](././inspector/~/Network.RequestWillBeSentEventDataType#property_request)
-   [requestId](././inspector/~/Network.RequestWillBeSentEventDataType#property_requestid)
-   [timestamp](././inspector/~/Network.RequestWillBeSentEventDataType#property_timestamp)
-   [wallTime](././inspector/~/Network.RequestWillBeSentEventDataType#property_walltime)

T

[Network.ResourceType](././inspector/~/Network.ResourceType "Network.ResourceType")

Resource type as it was perceived by the rendering engine.

I

[Network.Response](././inspector/~/Network.Response "Network.Response")

HTTP response data.

-   [headers](././inspector/~/Network.Response#property_headers)
-   [status](././inspector/~/Network.Response#property_status)
-   [statusText](././inspector/~/Network.Response#property_statustext)
-   [url](././inspector/~/Network.Response#property_url)

f

[Network.responseReceived](././inspector/~/Network.responseReceived "Network.responseReceived")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.ResponseReceivedEventDataType](././inspector/~/Network.ResponseReceivedEventDataType "Network.ResponseReceivedEventDataType")

No documentation available

-   [requestId](././inspector/~/Network.ResponseReceivedEventDataType#property_requestid)
-   [response](././inspector/~/Network.ResponseReceivedEventDataType#property_response)
-   [timestamp](././inspector/~/Network.ResponseReceivedEventDataType#property_timestamp)
-   [type](././inspector/~/Network.ResponseReceivedEventDataType#property_type)

T

[Network.TimeSinceEpoch](././inspector/~/Network.TimeSinceEpoch "Network.TimeSinceEpoch")

UTC time in seconds, counted from January 1, 1970.

N

[NodeRuntime](././inspector/~/NodeRuntime "NodeRuntime")

No documentation available

I

[NodeRuntime.NotifyWhenWaitingForDisconnectParameterType](././inspector/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType "NodeRuntime.NotifyWhenWaitingForDisconnectParameterType")

No documentation available

-   [enabled](././inspector/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType#property_enabled)

N

[NodeTracing](././inspector/~/NodeTracing "NodeTracing")

No documentation available

I

[NodeTracing.DataCollectedEventDataType](././inspector/~/NodeTracing.DataCollectedEventDataType "NodeTracing.DataCollectedEventDataType")

No documentation available

-   [value](././inspector/~/NodeTracing.DataCollectedEventDataType#property_value)

I

[NodeTracing.GetCategoriesReturnType](././inspector/~/NodeTracing.GetCategoriesReturnType "NodeTracing.GetCategoriesReturnType")

No documentation available

-   [categories](././inspector/~/NodeTracing.GetCategoriesReturnType#property_categories)

I

[NodeTracing.StartParameterType](././inspector/~/NodeTracing.StartParameterType "NodeTracing.StartParameterType")

No documentation available

-   [traceConfig](././inspector/~/NodeTracing.StartParameterType#property_traceconfig)

I

[NodeTracing.TraceConfig](././inspector/~/NodeTracing.TraceConfig "NodeTracing.TraceConfig")

No documentation available

-   [includedCategories](././inspector/~/NodeTracing.TraceConfig#property_includedcategories)
-   [recordMode](././inspector/~/NodeTracing.TraceConfig#property_recordmode)

N

[NodeWorker](././inspector/~/NodeWorker "NodeWorker")

No documentation available

I

[NodeWorker.AttachedToWorkerEventDataType](././inspector/~/NodeWorker.AttachedToWorkerEventDataType "NodeWorker.AttachedToWorkerEventDataType")

No documentation available

-   [sessionId](././inspector/~/NodeWorker.AttachedToWorkerEventDataType#property_sessionid)
-   [waitingForDebugger](././inspector/~/NodeWorker.AttachedToWorkerEventDataType#property_waitingfordebugger)
-   [workerInfo](././inspector/~/NodeWorker.AttachedToWorkerEventDataType#property_workerinfo)

I

[NodeWorker.DetachedFromWorkerEventDataType](././inspector/~/NodeWorker.DetachedFromWorkerEventDataType "NodeWorker.DetachedFromWorkerEventDataType")

No documentation available

-   [sessionId](././inspector/~/NodeWorker.DetachedFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.DetachParameterType](././inspector/~/NodeWorker.DetachParameterType "NodeWorker.DetachParameterType")

No documentation available

-   [sessionId](././inspector/~/NodeWorker.DetachParameterType#property_sessionid)

I

[NodeWorker.EnableParameterType](././inspector/~/NodeWorker.EnableParameterType "NodeWorker.EnableParameterType")

No documentation available

-   [waitForDebuggerOnStart](././inspector/~/NodeWorker.EnableParameterType#property_waitfordebuggeronstart)

I

[NodeWorker.ReceivedMessageFromWorkerEventDataType](././inspector/~/NodeWorker.ReceivedMessageFromWorkerEventDataType "NodeWorker.ReceivedMessageFromWorkerEventDataType")

No documentation available

-   [message](././inspector/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_message)
-   [sessionId](././inspector/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.SendMessageToWorkerParameterType](././inspector/~/NodeWorker.SendMessageToWorkerParameterType "NodeWorker.SendMessageToWorkerParameterType")

No documentation available

-   [message](././inspector/~/NodeWorker.SendMessageToWorkerParameterType#property_message)
-   [sessionId](././inspector/~/NodeWorker.SendMessageToWorkerParameterType#property_sessionid)

T

[NodeWorker.SessionID](././inspector/~/NodeWorker.SessionID "NodeWorker.SessionID")

Unique identifier of attached debugging session.

T

[NodeWorker.WorkerID](././inspector/~/NodeWorker.WorkerID "NodeWorker.WorkerID")

No documentation available

I

[NodeWorker.WorkerInfo](././inspector/~/NodeWorker.WorkerInfo "NodeWorker.WorkerInfo")

No documentation available

-   [title](././inspector/~/NodeWorker.WorkerInfo#property_title)
-   [type](././inspector/~/NodeWorker.WorkerInfo#property_type)
-   [url](././inspector/~/NodeWorker.WorkerInfo#property_url)
-   [workerId](././inspector/~/NodeWorker.WorkerInfo#property_workerid)

f

[open](././inspector/~/open "open")

Activate inspector on host and port. Equivalent to `node --inspect=[[host:]port]`, but can be done programmatically after node has started.

N

[Profiler](././inspector/~/Profiler "Profiler")

No documentation available

I

[Profiler.ConsoleProfileFinishedEventDataType](././inspector/~/Profiler.ConsoleProfileFinishedEventDataType "Profiler.ConsoleProfileFinishedEventDataType")

No documentation available

-   [id](././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_id)
-   [location](././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_location)
-   [profile](././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_profile)
-   [title](././inspector/~/Profiler.ConsoleProfileFinishedEventDataType#property_title)

I

[Profiler.ConsoleProfileStartedEventDataType](././inspector/~/Profiler.ConsoleProfileStartedEventDataType "Profiler.ConsoleProfileStartedEventDataType")

No documentation available

-   [id](././inspector/~/Profiler.ConsoleProfileStartedEventDataType#property_id)
-   [location](././inspector/~/Profiler.ConsoleProfileStartedEventDataType#property_location)
-   [title](././inspector/~/Profiler.ConsoleProfileStartedEventDataType#property_title)

I

[Profiler.CoverageRange](././inspector/~/Profiler.CoverageRange "Profiler.CoverageRange")

Coverage data for a source range.

-   [count](././inspector/~/Profiler.CoverageRange#property_count)
-   [endOffset](././inspector/~/Profiler.CoverageRange#property_endoffset)
-   [startOffset](././inspector/~/Profiler.CoverageRange#property_startoffset)

I

[Profiler.FunctionCoverage](././inspector/~/Profiler.FunctionCoverage "Profiler.FunctionCoverage")

Coverage data for a JavaScript function.

-   [functionName](././inspector/~/Profiler.FunctionCoverage#property_functionname)
-   [isBlockCoverage](././inspector/~/Profiler.FunctionCoverage#property_isblockcoverage)
-   [ranges](././inspector/~/Profiler.FunctionCoverage#property_ranges)

I

[Profiler.GetBestEffortCoverageReturnType](././inspector/~/Profiler.GetBestEffortCoverageReturnType "Profiler.GetBestEffortCoverageReturnType")

No documentation available

-   [result](././inspector/~/Profiler.GetBestEffortCoverageReturnType#property_result)

I

[Profiler.PositionTickInfo](././inspector/~/Profiler.PositionTickInfo "Profiler.PositionTickInfo")

Specifies a number of samples attributed to a certain source position.

-   [line](././inspector/~/Profiler.PositionTickInfo#property_line)
-   [ticks](././inspector/~/Profiler.PositionTickInfo#property_ticks)

I

[Profiler.Profile](././inspector/~/Profiler.Profile "Profiler.Profile")

Profile.

-   [endTime](././inspector/~/Profiler.Profile#property_endtime)
-   [nodes](././inspector/~/Profiler.Profile#property_nodes)
-   [samples](././inspector/~/Profiler.Profile#property_samples)
-   [startTime](././inspector/~/Profiler.Profile#property_starttime)
-   [timeDeltas](././inspector/~/Profiler.Profile#property_timedeltas)

I

[Profiler.ProfileNode](././inspector/~/Profiler.ProfileNode "Profiler.ProfileNode")

Profile node. Holds callsite information, execution statistics and child nodes.

-   [callFrame](././inspector/~/Profiler.ProfileNode#property_callframe)
-   [children](././inspector/~/Profiler.ProfileNode#property_children)
-   [deoptReason](././inspector/~/Profiler.ProfileNode#property_deoptreason)
-   [hitCount](././inspector/~/Profiler.ProfileNode#property_hitcount)
-   [id](././inspector/~/Profiler.ProfileNode#property_id)
-   [positionTicks](././inspector/~/Profiler.ProfileNode#property_positionticks)

I

[Profiler.ScriptCoverage](././inspector/~/Profiler.ScriptCoverage "Profiler.ScriptCoverage")

Coverage data for a JavaScript script.

-   [functions](././inspector/~/Profiler.ScriptCoverage#property_functions)
-   [scriptId](././inspector/~/Profiler.ScriptCoverage#property_scriptid)
-   [url](././inspector/~/Profiler.ScriptCoverage#property_url)

I

[Profiler.SetSamplingIntervalParameterType](././inspector/~/Profiler.SetSamplingIntervalParameterType "Profiler.SetSamplingIntervalParameterType")

No documentation available

-   [interval](././inspector/~/Profiler.SetSamplingIntervalParameterType#property_interval)

I

[Profiler.StartPreciseCoverageParameterType](././inspector/~/Profiler.StartPreciseCoverageParameterType "Profiler.StartPreciseCoverageParameterType")

No documentation available

-   [callCount](././inspector/~/Profiler.StartPreciseCoverageParameterType#property_callcount)
-   [detailed](././inspector/~/Profiler.StartPreciseCoverageParameterType#property_detailed)

I

[Profiler.StopReturnType](././inspector/~/Profiler.StopReturnType "Profiler.StopReturnType")

No documentation available

-   [profile](././inspector/~/Profiler.StopReturnType#property_profile)

I

[Profiler.TakePreciseCoverageReturnType](././inspector/~/Profiler.TakePreciseCoverageReturnType "Profiler.TakePreciseCoverageReturnType")

No documentation available

-   [result](././inspector/~/Profiler.TakePreciseCoverageReturnType#property_result)

N

[Runtime](././inspector/~/Runtime "Runtime")

No documentation available

I

[Runtime.AwaitPromiseParameterType](././inspector/~/Runtime.AwaitPromiseParameterType "Runtime.AwaitPromiseParameterType")

No documentation available

-   [generatePreview](././inspector/~/Runtime.AwaitPromiseParameterType#property_generatepreview)
-   [promiseObjectId](././inspector/~/Runtime.AwaitPromiseParameterType#property_promiseobjectid)
-   [returnByValue](././inspector/~/Runtime.AwaitPromiseParameterType#property_returnbyvalue)

I

[Runtime.AwaitPromiseReturnType](././inspector/~/Runtime.AwaitPromiseReturnType "Runtime.AwaitPromiseReturnType")

No documentation available

-   [exceptionDetails](././inspector/~/Runtime.AwaitPromiseReturnType#property_exceptiondetails)
-   [result](././inspector/~/Runtime.AwaitPromiseReturnType#property_result)

I

[Runtime.CallArgument](././inspector/~/Runtime.CallArgument "Runtime.CallArgument")

Represents function call argument. Either remote object id `objectId`, primitive `value`, unserializable primitive value or neither of (for undefined) them should be specified.

-   [objectId](././inspector/~/Runtime.CallArgument#property_objectid)
-   [unserializableValue](././inspector/~/Runtime.CallArgument#property_unserializablevalue)
-   [value](././inspector/~/Runtime.CallArgument#property_value)

I

[Runtime.CallFrame](././inspector/~/Runtime.CallFrame "Runtime.CallFrame")

Stack entry for runtime errors and assertions.

-   [columnNumber](././inspector/~/Runtime.CallFrame#property_columnnumber)
-   [functionName](././inspector/~/Runtime.CallFrame#property_functionname)
-   [lineNumber](././inspector/~/Runtime.CallFrame#property_linenumber)
-   [scriptId](././inspector/~/Runtime.CallFrame#property_scriptid)
-   [url](././inspector/~/Runtime.CallFrame#property_url)

I

[Runtime.CallFunctionOnParameterType](././inspector/~/Runtime.CallFunctionOnParameterType "Runtime.CallFunctionOnParameterType")

No documentation available

-   [arguments](././inspector/~/Runtime.CallFunctionOnParameterType#property_arguments)
-   [awaitPromise](././inspector/~/Runtime.CallFunctionOnParameterType#property_awaitpromise)
-   [executionContextId](././inspector/~/Runtime.CallFunctionOnParameterType#property_executioncontextid)
-   [functionDeclaration](././inspector/~/Runtime.CallFunctionOnParameterType#property_functiondeclaration)
-   [generatePreview](././inspector/~/Runtime.CallFunctionOnParameterType#property_generatepreview)
-   [objectGroup](././inspector/~/Runtime.CallFunctionOnParameterType#property_objectgroup)
-   [objectId](././inspector/~/Runtime.CallFunctionOnParameterType#property_objectid)
-   [returnByValue](././inspector/~/Runtime.CallFunctionOnParameterType#property_returnbyvalue)
-   [silent](././inspector/~/Runtime.CallFunctionOnParameterType#property_silent)
-   [userGesture](././inspector/~/Runtime.CallFunctionOnParameterType#property_usergesture)

I

[Runtime.CallFunctionOnReturnType](././inspector/~/Runtime.CallFunctionOnReturnType "Runtime.CallFunctionOnReturnType")

No documentation available

-   [exceptionDetails](././inspector/~/Runtime.CallFunctionOnReturnType#property_exceptiondetails)
-   [result](././inspector/~/Runtime.CallFunctionOnReturnType#property_result)

I

[Runtime.CompileScriptParameterType](././inspector/~/Runtime.CompileScriptParameterType "Runtime.CompileScriptParameterType")

No documentation available

-   [executionContextId](././inspector/~/Runtime.CompileScriptParameterType#property_executioncontextid)
-   [expression](././inspector/~/Runtime.CompileScriptParameterType#property_expression)
-   [persistScript](././inspector/~/Runtime.CompileScriptParameterType#property_persistscript)
-   [sourceURL](././inspector/~/Runtime.CompileScriptParameterType#property_sourceurl)

I

[Runtime.CompileScriptReturnType](././inspector/~/Runtime.CompileScriptReturnType "Runtime.CompileScriptReturnType")

No documentation available

-   [exceptionDetails](././inspector/~/Runtime.CompileScriptReturnType#property_exceptiondetails)
-   [scriptId](././inspector/~/Runtime.CompileScriptReturnType#property_scriptid)

I

[Runtime.ConsoleAPICalledEventDataType](././inspector/~/Runtime.ConsoleAPICalledEventDataType "Runtime.ConsoleAPICalledEventDataType")

No documentation available

-   [args](././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_args)
-   [context](././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_context)
-   [executionContextId](././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_executioncontextid)
-   [stackTrace](././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_stacktrace)
-   [timestamp](././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_timestamp)
-   [type](././inspector/~/Runtime.ConsoleAPICalledEventDataType#property_type)

I

[Runtime.CustomPreview](././inspector/~/Runtime.CustomPreview "Runtime.CustomPreview")

No documentation available

-   [bindRemoteObjectFunctionId](././inspector/~/Runtime.CustomPreview#property_bindremoteobjectfunctionid)
-   [configObjectId](././inspector/~/Runtime.CustomPreview#property_configobjectid)
-   [formatterObjectId](././inspector/~/Runtime.CustomPreview#property_formatterobjectid)
-   [hasBody](././inspector/~/Runtime.CustomPreview#property_hasbody)
-   [header](././inspector/~/Runtime.CustomPreview#property_header)

I

[Runtime.EntryPreview](././inspector/~/Runtime.EntryPreview "Runtime.EntryPreview")

No documentation available

-   [key](././inspector/~/Runtime.EntryPreview#property_key)
-   [value](././inspector/~/Runtime.EntryPreview#property_value)

I

[Runtime.EvaluateParameterType](././inspector/~/Runtime.EvaluateParameterType "Runtime.EvaluateParameterType")

No documentation available

-   [awaitPromise](././inspector/~/Runtime.EvaluateParameterType#property_awaitpromise)
-   [contextId](././inspector/~/Runtime.EvaluateParameterType#property_contextid)
-   [expression](././inspector/~/Runtime.EvaluateParameterType#property_expression)
-   [generatePreview](././inspector/~/Runtime.EvaluateParameterType#property_generatepreview)
-   [includeCommandLineAPI](././inspector/~/Runtime.EvaluateParameterType#property_includecommandlineapi)
-   [objectGroup](././inspector/~/Runtime.EvaluateParameterType#property_objectgroup)
-   [returnByValue](././inspector/~/Runtime.EvaluateParameterType#property_returnbyvalue)
-   [silent](././inspector/~/Runtime.EvaluateParameterType#property_silent)
-   [userGesture](././inspector/~/Runtime.EvaluateParameterType#property_usergesture)

I

[Runtime.EvaluateReturnType](././inspector/~/Runtime.EvaluateReturnType "Runtime.EvaluateReturnType")

No documentation available

-   [exceptionDetails](././inspector/~/Runtime.EvaluateReturnType#property_exceptiondetails)
-   [result](././inspector/~/Runtime.EvaluateReturnType#property_result)

I

[Runtime.ExceptionDetails](././inspector/~/Runtime.ExceptionDetails "Runtime.ExceptionDetails")

Detailed information about exception (or error) that was thrown during script compilation or execution.

-   [columnNumber](././inspector/~/Runtime.ExceptionDetails#property_columnnumber)
-   [exception](././inspector/~/Runtime.ExceptionDetails#property_exception)
-   [exceptionId](././inspector/~/Runtime.ExceptionDetails#property_exceptionid)
-   [executionContextId](././inspector/~/Runtime.ExceptionDetails#property_executioncontextid)
-   [lineNumber](././inspector/~/Runtime.ExceptionDetails#property_linenumber)
-   [scriptId](././inspector/~/Runtime.ExceptionDetails#property_scriptid)
-   [stackTrace](././inspector/~/Runtime.ExceptionDetails#property_stacktrace)
-   [text](././inspector/~/Runtime.ExceptionDetails#property_text)
-   [url](././inspector/~/Runtime.ExceptionDetails#property_url)

I

[Runtime.ExceptionRevokedEventDataType](././inspector/~/Runtime.ExceptionRevokedEventDataType "Runtime.ExceptionRevokedEventDataType")

No documentation available

-   [exceptionId](././inspector/~/Runtime.ExceptionRevokedEventDataType#property_exceptionid)
-   [reason](././inspector/~/Runtime.ExceptionRevokedEventDataType#property_reason)

I

[Runtime.ExceptionThrownEventDataType](././inspector/~/Runtime.ExceptionThrownEventDataType "Runtime.ExceptionThrownEventDataType")

No documentation available

-   [exceptionDetails](././inspector/~/Runtime.ExceptionThrownEventDataType#property_exceptiondetails)
-   [timestamp](././inspector/~/Runtime.ExceptionThrownEventDataType#property_timestamp)

I

[Runtime.ExecutionContextCreatedEventDataType](././inspector/~/Runtime.ExecutionContextCreatedEventDataType "Runtime.ExecutionContextCreatedEventDataType")

No documentation available

-   [context](././inspector/~/Runtime.ExecutionContextCreatedEventDataType#property_context)

I

[Runtime.ExecutionContextDescription](././inspector/~/Runtime.ExecutionContextDescription "Runtime.ExecutionContextDescription")

Description of an isolated world.

-   [auxData](././inspector/~/Runtime.ExecutionContextDescription#property_auxdata)
-   [id](././inspector/~/Runtime.ExecutionContextDescription#property_id)
-   [name](././inspector/~/Runtime.ExecutionContextDescription#property_name)
-   [origin](././inspector/~/Runtime.ExecutionContextDescription#property_origin)

I

[Runtime.ExecutionContextDestroyedEventDataType](././inspector/~/Runtime.ExecutionContextDestroyedEventDataType "Runtime.ExecutionContextDestroyedEventDataType")

No documentation available

-   [executionContextId](././inspector/~/Runtime.ExecutionContextDestroyedEventDataType#property_executioncontextid)

T

[Runtime.ExecutionContextId](././inspector/~/Runtime.ExecutionContextId "Runtime.ExecutionContextId")

Id of an execution context.

I

[Runtime.GetPropertiesParameterType](././inspector/~/Runtime.GetPropertiesParameterType "Runtime.GetPropertiesParameterType")

No documentation available

-   [accessorPropertiesOnly](././inspector/~/Runtime.GetPropertiesParameterType#property_accessorpropertiesonly)
-   [generatePreview](././inspector/~/Runtime.GetPropertiesParameterType#property_generatepreview)
-   [objectId](././inspector/~/Runtime.GetPropertiesParameterType#property_objectid)
-   [ownProperties](././inspector/~/Runtime.GetPropertiesParameterType#property_ownproperties)

I

[Runtime.GetPropertiesReturnType](././inspector/~/Runtime.GetPropertiesReturnType "Runtime.GetPropertiesReturnType")

No documentation available

-   [exceptionDetails](././inspector/~/Runtime.GetPropertiesReturnType#property_exceptiondetails)
-   [internalProperties](././inspector/~/Runtime.GetPropertiesReturnType#property_internalproperties)
-   [result](././inspector/~/Runtime.GetPropertiesReturnType#property_result)

I

[Runtime.GlobalLexicalScopeNamesParameterType](././inspector/~/Runtime.GlobalLexicalScopeNamesParameterType "Runtime.GlobalLexicalScopeNamesParameterType")

No documentation available

-   [executionContextId](././inspector/~/Runtime.GlobalLexicalScopeNamesParameterType#property_executioncontextid)

I

[Runtime.GlobalLexicalScopeNamesReturnType](././inspector/~/Runtime.GlobalLexicalScopeNamesReturnType "Runtime.GlobalLexicalScopeNamesReturnType")

No documentation available

-   [names](././inspector/~/Runtime.GlobalLexicalScopeNamesReturnType#property_names)

I

[Runtime.InspectRequestedEventDataType](././inspector/~/Runtime.InspectRequestedEventDataType "Runtime.InspectRequestedEventDataType")

No documentation available

-   [hints](././inspector/~/Runtime.InspectRequestedEventDataType#property_hints)
-   [object](././inspector/~/Runtime.InspectRequestedEventDataType#property_object)

I

[Runtime.InternalPropertyDescriptor](././inspector/~/Runtime.InternalPropertyDescriptor "Runtime.InternalPropertyDescriptor")

Object internal property descriptor. This property isn't normally visible in JavaScript code.

-   [name](././inspector/~/Runtime.InternalPropertyDescriptor#property_name)
-   [value](././inspector/~/Runtime.InternalPropertyDescriptor#property_value)

I

[Runtime.ObjectPreview](././inspector/~/Runtime.ObjectPreview "Runtime.ObjectPreview")

Object containing abbreviated remote object value.

-   [description](././inspector/~/Runtime.ObjectPreview#property_description)
-   [entries](././inspector/~/Runtime.ObjectPreview#property_entries)
-   [overflow](././inspector/~/Runtime.ObjectPreview#property_overflow)
-   [properties](././inspector/~/Runtime.ObjectPreview#property_properties)
-   [subtype](././inspector/~/Runtime.ObjectPreview#property_subtype)
-   [type](././inspector/~/Runtime.ObjectPreview#property_type)

I

[Runtime.PropertyDescriptor](././inspector/~/Runtime.PropertyDescriptor "Runtime.PropertyDescriptor")

Object property descriptor.

-   [configurable](././inspector/~/Runtime.PropertyDescriptor#property_configurable)
-   [enumerable](././inspector/~/Runtime.PropertyDescriptor#property_enumerable)
-   [get](././inspector/~/Runtime.PropertyDescriptor#property_get)
-   [isOwn](././inspector/~/Runtime.PropertyDescriptor#property_isown)
-   [name](././inspector/~/Runtime.PropertyDescriptor#property_name)
-   [set](././inspector/~/Runtime.PropertyDescriptor#property_set)
-   [symbol](././inspector/~/Runtime.PropertyDescriptor#property_symbol)
-   [value](././inspector/~/Runtime.PropertyDescriptor#property_value)
-   [wasThrown](././inspector/~/Runtime.PropertyDescriptor#property_wasthrown)
-   [writable](././inspector/~/Runtime.PropertyDescriptor#property_writable)

I

[Runtime.PropertyPreview](././inspector/~/Runtime.PropertyPreview "Runtime.PropertyPreview")

No documentation available

-   [name](././inspector/~/Runtime.PropertyPreview#property_name)
-   [subtype](././inspector/~/Runtime.PropertyPreview#property_subtype)
-   [type](././inspector/~/Runtime.PropertyPreview#property_type)
-   [value](././inspector/~/Runtime.PropertyPreview#property_value)
-   [valuePreview](././inspector/~/Runtime.PropertyPreview#property_valuepreview)

I

[Runtime.QueryObjectsParameterType](././inspector/~/Runtime.QueryObjectsParameterType "Runtime.QueryObjectsParameterType")

No documentation available

-   [prototypeObjectId](././inspector/~/Runtime.QueryObjectsParameterType#property_prototypeobjectid)

I

[Runtime.QueryObjectsReturnType](././inspector/~/Runtime.QueryObjectsReturnType "Runtime.QueryObjectsReturnType")

No documentation available

-   [objects](././inspector/~/Runtime.QueryObjectsReturnType#property_objects)

I

[Runtime.ReleaseObjectGroupParameterType](././inspector/~/Runtime.ReleaseObjectGroupParameterType "Runtime.ReleaseObjectGroupParameterType")

No documentation available

-   [objectGroup](././inspector/~/Runtime.ReleaseObjectGroupParameterType#property_objectgroup)

I

[Runtime.ReleaseObjectParameterType](././inspector/~/Runtime.ReleaseObjectParameterType "Runtime.ReleaseObjectParameterType")

No documentation available

-   [objectId](././inspector/~/Runtime.ReleaseObjectParameterType#property_objectid)

I

[Runtime.RemoteObject](././inspector/~/Runtime.RemoteObject "Runtime.RemoteObject")

Mirror object referencing original JavaScript object.

-   [className](././inspector/~/Runtime.RemoteObject#property_classname)
-   [customPreview](././inspector/~/Runtime.RemoteObject#property_custompreview)
-   [description](././inspector/~/Runtime.RemoteObject#property_description)
-   [objectId](././inspector/~/Runtime.RemoteObject#property_objectid)
-   [preview](././inspector/~/Runtime.RemoteObject#property_preview)
-   [subtype](././inspector/~/Runtime.RemoteObject#property_subtype)
-   [type](././inspector/~/Runtime.RemoteObject#property_type)
-   [unserializableValue](././inspector/~/Runtime.RemoteObject#property_unserializablevalue)
-   [value](././inspector/~/Runtime.RemoteObject#property_value)

T

[Runtime.RemoteObjectId](././inspector/~/Runtime.RemoteObjectId "Runtime.RemoteObjectId")

Unique object identifier.

I

[Runtime.RunScriptParameterType](././inspector/~/Runtime.RunScriptParameterType "Runtime.RunScriptParameterType")

No documentation available

-   [awaitPromise](././inspector/~/Runtime.RunScriptParameterType#property_awaitpromise)
-   [executionContextId](././inspector/~/Runtime.RunScriptParameterType#property_executioncontextid)
-   [generatePreview](././inspector/~/Runtime.RunScriptParameterType#property_generatepreview)
-   [includeCommandLineAPI](././inspector/~/Runtime.RunScriptParameterType#property_includecommandlineapi)
-   [objectGroup](././inspector/~/Runtime.RunScriptParameterType#property_objectgroup)
-   [returnByValue](././inspector/~/Runtime.RunScriptParameterType#property_returnbyvalue)
-   [scriptId](././inspector/~/Runtime.RunScriptParameterType#property_scriptid)
-   [silent](././inspector/~/Runtime.RunScriptParameterType#property_silent)

I

[Runtime.RunScriptReturnType](././inspector/~/Runtime.RunScriptReturnType "Runtime.RunScriptReturnType")

No documentation available

-   [exceptionDetails](././inspector/~/Runtime.RunScriptReturnType#property_exceptiondetails)
-   [result](././inspector/~/Runtime.RunScriptReturnType#property_result)

T

[Runtime.ScriptId](././inspector/~/Runtime.ScriptId "Runtime.ScriptId")

Unique script identifier.

I

[Runtime.SetCustomObjectFormatterEnabledParameterType](././inspector/~/Runtime.SetCustomObjectFormatterEnabledParameterType "Runtime.SetCustomObjectFormatterEnabledParameterType")

No documentation available

-   [enabled](././inspector/~/Runtime.SetCustomObjectFormatterEnabledParameterType#property_enabled)

I

[Runtime.StackTrace](././inspector/~/Runtime.StackTrace "Runtime.StackTrace")

Call frames for assertions or error messages.

-   [callFrames](././inspector/~/Runtime.StackTrace#property_callframes)
-   [description](././inspector/~/Runtime.StackTrace#property_description)
-   [parent](././inspector/~/Runtime.StackTrace#property_parent)
-   [parentId](././inspector/~/Runtime.StackTrace#property_parentid)

I

[Runtime.StackTraceId](././inspector/~/Runtime.StackTraceId "Runtime.StackTraceId")

If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.

-   [debuggerId](././inspector/~/Runtime.StackTraceId#property_debuggerid)
-   [id](././inspector/~/Runtime.StackTraceId#property_id)

T

[Runtime.Timestamp](././inspector/~/Runtime.Timestamp "Runtime.Timestamp")

Number of milliseconds since epoch.

T

[Runtime.UniqueDebuggerId](././inspector/~/Runtime.UniqueDebuggerId "Runtime.UniqueDebuggerId")

Unique identifier of current debugger.

T

[Runtime.UnserializableValue](././inspector/~/Runtime.UnserializableValue "Runtime.UnserializableValue")

Primitive value which cannot be JSON-stringified.

N

[Schema](././inspector/~/Schema "Schema")

No documentation available

I

[Schema.Domain](././inspector/~/Schema.Domain "Schema.Domain")

Description of the protocol domain.

-   [name](././inspector/~/Schema.Domain#property_name)
-   [version](././inspector/~/Schema.Domain#property_version)

I

[Schema.GetDomainsReturnType](././inspector/~/Schema.GetDomainsReturnType "Schema.GetDomainsReturnType")

No documentation available

-   [domains](././inspector/~/Schema.GetDomainsReturnType#property_domains)

c

[Session](././inspector/~/Session "Session")

The `inspector.Session` is used for dispatching messages to the V8 inspector back-end and receiving message responses and notifications.

-   [addListener](././inspector/~/Session#method_addlistener_0)
-   [connect](././inspector/~/Session#method_connect_0)
-   [connectToMainThread](././inspector/~/Session#method_connecttomainthread_0)
-   [disconnect](././inspector/~/Session#method_disconnect_0)
-   [emit](././inspector/~/Session#method_emit_0)
-   [on](././inspector/~/Session#method_on_0)
-   [once](././inspector/~/Session#method_once_0)
-   [post](././inspector/~/Session#method_post_0)
-   [prependListener](././inspector/~/Session#method_prependlistener_0)
-   [prependOnceListener](././inspector/~/Session#method_prependoncelistener_0)

f

[url](././inspector/~/url "url")

Return the URL of the active inspector, or `undefined` if there is none.

f

[waitForDebugger](././inspector/~/waitForDebugger "waitForDebugger")

Blocks until a client (existing or connected later) has sent `Runtime.runIfWaitingForDebugger` command.

The `node:inspector/promises` module provides an API for interacting with the V8 inspector.

N

[Console](././inspector/promises/~/Console "Console")

No documentation available

I

[Console.ConsoleMessage](././inspector/promises/~/Console.ConsoleMessage "Console.ConsoleMessage")

Console message.

-   [column](././inspector/promises/~/Console.ConsoleMessage#property_column)
-   [level](././inspector/promises/~/Console.ConsoleMessage#property_level)
-   [line](././inspector/promises/~/Console.ConsoleMessage#property_line)
-   [source](././inspector/promises/~/Console.ConsoleMessage#property_source)
-   [text](././inspector/promises/~/Console.ConsoleMessage#property_text)
-   [url](././inspector/promises/~/Console.ConsoleMessage#property_url)

I

[Console.MessageAddedEventDataType](././inspector/promises/~/Console.MessageAddedEventDataType "Console.MessageAddedEventDataType")

No documentation available

-   [message](././inspector/promises/~/Console.MessageAddedEventDataType#property_message)

N

[Debugger](././inspector/promises/~/Debugger "Debugger")

No documentation available

I

[Debugger.BreakLocation](././inspector/promises/~/Debugger.BreakLocation "Debugger.BreakLocation")

No documentation available

-   [columnNumber](././inspector/promises/~/Debugger.BreakLocation#property_columnnumber)
-   [lineNumber](././inspector/promises/~/Debugger.BreakLocation#property_linenumber)
-   [scriptId](././inspector/promises/~/Debugger.BreakLocation#property_scriptid)
-   [type](././inspector/promises/~/Debugger.BreakLocation#property_type)

T

[Debugger.BreakpointId](././inspector/promises/~/Debugger.BreakpointId "Debugger.BreakpointId")

Breakpoint identifier.

I

[Debugger.BreakpointResolvedEventDataType](././inspector/promises/~/Debugger.BreakpointResolvedEventDataType "Debugger.BreakpointResolvedEventDataType")

No documentation available

-   [breakpointId](././inspector/promises/~/Debugger.BreakpointResolvedEventDataType#property_breakpointid)
-   [location](././inspector/promises/~/Debugger.BreakpointResolvedEventDataType#property_location)

I

[Debugger.CallFrame](././inspector/promises/~/Debugger.CallFrame "Debugger.CallFrame")

JavaScript call frame. Array of call frames form the call stack.

-   [callFrameId](././inspector/promises/~/Debugger.CallFrame#property_callframeid)
-   [functionLocation](././inspector/promises/~/Debugger.CallFrame#property_functionlocation)
-   [functionName](././inspector/promises/~/Debugger.CallFrame#property_functionname)
-   [location](././inspector/promises/~/Debugger.CallFrame#property_location)
-   [returnValue](././inspector/promises/~/Debugger.CallFrame#property_returnvalue)
-   [scopeChain](././inspector/promises/~/Debugger.CallFrame#property_scopechain)
-   [this](././inspector/promises/~/Debugger.CallFrame#property_this)
-   [url](././inspector/promises/~/Debugger.CallFrame#property_url)

T

[Debugger.CallFrameId](././inspector/promises/~/Debugger.CallFrameId "Debugger.CallFrameId")

Call frame identifier.

I

[Debugger.ContinueToLocationParameterType](././inspector/promises/~/Debugger.ContinueToLocationParameterType "Debugger.ContinueToLocationParameterType")

No documentation available

-   [location](././inspector/promises/~/Debugger.ContinueToLocationParameterType#property_location)
-   [targetCallFrames](././inspector/promises/~/Debugger.ContinueToLocationParameterType#property_targetcallframes)

I

[Debugger.EnableReturnType](././inspector/promises/~/Debugger.EnableReturnType "Debugger.EnableReturnType")

No documentation available

-   [debuggerId](././inspector/promises/~/Debugger.EnableReturnType#property_debuggerid)

I

[Debugger.EvaluateOnCallFrameParameterType](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType "Debugger.EvaluateOnCallFrameParameterType")

No documentation available

-   [callFrameId](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_callframeid)
-   [expression](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_expression)
-   [generatePreview](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_generatepreview)
-   [includeCommandLineAPI](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_includecommandlineapi)
-   [objectGroup](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_objectgroup)
-   [returnByValue](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_returnbyvalue)
-   [silent](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_silent)
-   [throwOnSideEffect](././inspector/promises/~/Debugger.EvaluateOnCallFrameParameterType#property_throwonsideeffect)

I

[Debugger.EvaluateOnCallFrameReturnType](././inspector/promises/~/Debugger.EvaluateOnCallFrameReturnType "Debugger.EvaluateOnCallFrameReturnType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Debugger.EvaluateOnCallFrameReturnType#property_exceptiondetails)
-   [result](././inspector/promises/~/Debugger.EvaluateOnCallFrameReturnType#property_result)

I

[Debugger.GetPossibleBreakpointsParameterType](././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType "Debugger.GetPossibleBreakpointsParameterType")

No documentation available

-   [end](././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType#property_end)
-   [restrictToFunction](././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType#property_restricttofunction)
-   [start](././inspector/promises/~/Debugger.GetPossibleBreakpointsParameterType#property_start)

I

[Debugger.GetPossibleBreakpointsReturnType](././inspector/promises/~/Debugger.GetPossibleBreakpointsReturnType "Debugger.GetPossibleBreakpointsReturnType")

No documentation available

-   [locations](././inspector/promises/~/Debugger.GetPossibleBreakpointsReturnType#property_locations)

I

[Debugger.GetScriptSourceParameterType](././inspector/promises/~/Debugger.GetScriptSourceParameterType "Debugger.GetScriptSourceParameterType")

No documentation available

-   [scriptId](././inspector/promises/~/Debugger.GetScriptSourceParameterType#property_scriptid)

I

[Debugger.GetScriptSourceReturnType](././inspector/promises/~/Debugger.GetScriptSourceReturnType "Debugger.GetScriptSourceReturnType")

No documentation available

-   [scriptSource](././inspector/promises/~/Debugger.GetScriptSourceReturnType#property_scriptsource)

I

[Debugger.GetStackTraceParameterType](././inspector/promises/~/Debugger.GetStackTraceParameterType "Debugger.GetStackTraceParameterType")

No documentation available

-   [stackTraceId](././inspector/promises/~/Debugger.GetStackTraceParameterType#property_stacktraceid)

I

[Debugger.GetStackTraceReturnType](././inspector/promises/~/Debugger.GetStackTraceReturnType "Debugger.GetStackTraceReturnType")

No documentation available

-   [stackTrace](././inspector/promises/~/Debugger.GetStackTraceReturnType#property_stacktrace)

I

[Debugger.Location](././inspector/promises/~/Debugger.Location "Debugger.Location")

Location in the source code.

-   [columnNumber](././inspector/promises/~/Debugger.Location#property_columnnumber)
-   [lineNumber](././inspector/promises/~/Debugger.Location#property_linenumber)
-   [scriptId](././inspector/promises/~/Debugger.Location#property_scriptid)

I

[Debugger.PausedEventDataType](././inspector/promises/~/Debugger.PausedEventDataType "Debugger.PausedEventDataType")

No documentation available

-   [asyncCallStackTraceId](././inspector/promises/~/Debugger.PausedEventDataType#property_asynccallstacktraceid)
-   [asyncStackTrace](././inspector/promises/~/Debugger.PausedEventDataType#property_asyncstacktrace)
-   [asyncStackTraceId](././inspector/promises/~/Debugger.PausedEventDataType#property_asyncstacktraceid)
-   [callFrames](././inspector/promises/~/Debugger.PausedEventDataType#property_callframes)
-   [data](././inspector/promises/~/Debugger.PausedEventDataType#property_data)
-   [hitBreakpoints](././inspector/promises/~/Debugger.PausedEventDataType#property_hitbreakpoints)
-   [reason](././inspector/promises/~/Debugger.PausedEventDataType#property_reason)

I

[Debugger.PauseOnAsyncCallParameterType](././inspector/promises/~/Debugger.PauseOnAsyncCallParameterType "Debugger.PauseOnAsyncCallParameterType")

No documentation available

-   [parentStackTraceId](././inspector/promises/~/Debugger.PauseOnAsyncCallParameterType#property_parentstacktraceid)

I

[Debugger.RemoveBreakpointParameterType](././inspector/promises/~/Debugger.RemoveBreakpointParameterType "Debugger.RemoveBreakpointParameterType")

No documentation available

-   [breakpointId](././inspector/promises/~/Debugger.RemoveBreakpointParameterType#property_breakpointid)

I

[Debugger.RestartFrameParameterType](././inspector/promises/~/Debugger.RestartFrameParameterType "Debugger.RestartFrameParameterType")

No documentation available

-   [callFrameId](././inspector/promises/~/Debugger.RestartFrameParameterType#property_callframeid)

I

[Debugger.RestartFrameReturnType](././inspector/promises/~/Debugger.RestartFrameReturnType "Debugger.RestartFrameReturnType")

No documentation available

-   [asyncStackTrace](././inspector/promises/~/Debugger.RestartFrameReturnType#property_asyncstacktrace)
-   [asyncStackTraceId](././inspector/promises/~/Debugger.RestartFrameReturnType#property_asyncstacktraceid)
-   [callFrames](././inspector/promises/~/Debugger.RestartFrameReturnType#property_callframes)

I

[Debugger.Scope](././inspector/promises/~/Debugger.Scope "Debugger.Scope")

Scope description.

-   [endLocation](././inspector/promises/~/Debugger.Scope#property_endlocation)
-   [name](././inspector/promises/~/Debugger.Scope#property_name)
-   [object](././inspector/promises/~/Debugger.Scope#property_object)
-   [startLocation](././inspector/promises/~/Debugger.Scope#property_startlocation)
-   [type](././inspector/promises/~/Debugger.Scope#property_type)

I

[Debugger.ScriptFailedToParseEventDataType](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType "Debugger.ScriptFailedToParseEventDataType")

No documentation available

-   [endColumn](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_endcolumn)
-   [endLine](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_endline)
-   [executionContextAuxData](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextauxdata)
-   [executionContextId](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_executioncontextid)
-   [hasSourceURL](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_hassourceurl)
-   [hash](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_hash)
-   [isModule](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_ismodule)
-   [length](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_length)
-   [scriptId](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_scriptid)
-   [sourceMapURL](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_sourcemapurl)
-   [stackTrace](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_stacktrace)
-   [startColumn](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_startcolumn)
-   [startLine](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_startline)
-   [url](././inspector/promises/~/Debugger.ScriptFailedToParseEventDataType#property_url)

I

[Debugger.ScriptParsedEventDataType](././inspector/promises/~/Debugger.ScriptParsedEventDataType "Debugger.ScriptParsedEventDataType")

No documentation available

-   [endColumn](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_endcolumn)
-   [endLine](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_endline)
-   [executionContextAuxData](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_executioncontextauxdata)
-   [executionContextId](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_executioncontextid)
-   [hasSourceURL](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_hassourceurl)
-   [hash](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_hash)
-   [isLiveEdit](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_isliveedit)
-   [isModule](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_ismodule)
-   [length](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_length)
-   [scriptId](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_scriptid)
-   [sourceMapURL](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_sourcemapurl)
-   [stackTrace](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_stacktrace)
-   [startColumn](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_startcolumn)
-   [startLine](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_startline)
-   [url](././inspector/promises/~/Debugger.ScriptParsedEventDataType#property_url)

I

[Debugger.ScriptPosition](././inspector/promises/~/Debugger.ScriptPosition "Debugger.ScriptPosition")

Location in the source code.

-   [columnNumber](././inspector/promises/~/Debugger.ScriptPosition#property_columnnumber)
-   [lineNumber](././inspector/promises/~/Debugger.ScriptPosition#property_linenumber)

I

[Debugger.SearchInContentParameterType](././inspector/promises/~/Debugger.SearchInContentParameterType "Debugger.SearchInContentParameterType")

No documentation available

-   [caseSensitive](././inspector/promises/~/Debugger.SearchInContentParameterType#property_casesensitive)
-   [isRegex](././inspector/promises/~/Debugger.SearchInContentParameterType#property_isregex)
-   [query](././inspector/promises/~/Debugger.SearchInContentParameterType#property_query)
-   [scriptId](././inspector/promises/~/Debugger.SearchInContentParameterType#property_scriptid)

I

[Debugger.SearchInContentReturnType](././inspector/promises/~/Debugger.SearchInContentReturnType "Debugger.SearchInContentReturnType")

No documentation available

-   [result](././inspector/promises/~/Debugger.SearchInContentReturnType#property_result)

I

[Debugger.SearchMatch](././inspector/promises/~/Debugger.SearchMatch "Debugger.SearchMatch")

Search match for resource.

-   [lineContent](././inspector/promises/~/Debugger.SearchMatch#property_linecontent)
-   [lineNumber](././inspector/promises/~/Debugger.SearchMatch#property_linenumber)

I

[Debugger.SetAsyncCallStackDepthParameterType](././inspector/promises/~/Debugger.SetAsyncCallStackDepthParameterType "Debugger.SetAsyncCallStackDepthParameterType")

No documentation available

-   [maxDepth](././inspector/promises/~/Debugger.SetAsyncCallStackDepthParameterType#property_maxdepth)

I

[Debugger.SetBlackboxedRangesParameterType](././inspector/promises/~/Debugger.SetBlackboxedRangesParameterType "Debugger.SetBlackboxedRangesParameterType")

No documentation available

-   [positions](././inspector/promises/~/Debugger.SetBlackboxedRangesParameterType#property_positions)
-   [scriptId](././inspector/promises/~/Debugger.SetBlackboxedRangesParameterType#property_scriptid)

I

[Debugger.SetBlackboxPatternsParameterType](././inspector/promises/~/Debugger.SetBlackboxPatternsParameterType "Debugger.SetBlackboxPatternsParameterType")

No documentation available

-   [patterns](././inspector/promises/~/Debugger.SetBlackboxPatternsParameterType#property_patterns)

I

[Debugger.SetBreakpointByUrlParameterType](././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType "Debugger.SetBreakpointByUrlParameterType")

No documentation available

-   [columnNumber](././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_columnnumber)
-   [condition](././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_condition)
-   [lineNumber](././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_linenumber)
-   [scriptHash](././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_scripthash)
-   [url](././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_url)
-   [urlRegex](././inspector/promises/~/Debugger.SetBreakpointByUrlParameterType#property_urlregex)

I

[Debugger.SetBreakpointByUrlReturnType](././inspector/promises/~/Debugger.SetBreakpointByUrlReturnType "Debugger.SetBreakpointByUrlReturnType")

No documentation available

-   [breakpointId](././inspector/promises/~/Debugger.SetBreakpointByUrlReturnType#property_breakpointid)
-   [locations](././inspector/promises/~/Debugger.SetBreakpointByUrlReturnType#property_locations)

I

[Debugger.SetBreakpointParameterType](././inspector/promises/~/Debugger.SetBreakpointParameterType "Debugger.SetBreakpointParameterType")

No documentation available

-   [condition](././inspector/promises/~/Debugger.SetBreakpointParameterType#property_condition)
-   [location](././inspector/promises/~/Debugger.SetBreakpointParameterType#property_location)

I

[Debugger.SetBreakpointReturnType](././inspector/promises/~/Debugger.SetBreakpointReturnType "Debugger.SetBreakpointReturnType")

No documentation available

-   [actualLocation](././inspector/promises/~/Debugger.SetBreakpointReturnType#property_actuallocation)
-   [breakpointId](././inspector/promises/~/Debugger.SetBreakpointReturnType#property_breakpointid)

I

[Debugger.SetBreakpointsActiveParameterType](././inspector/promises/~/Debugger.SetBreakpointsActiveParameterType "Debugger.SetBreakpointsActiveParameterType")

No documentation available

-   [active](././inspector/promises/~/Debugger.SetBreakpointsActiveParameterType#property_active)

I

[Debugger.SetPauseOnExceptionsParameterType](././inspector/promises/~/Debugger.SetPauseOnExceptionsParameterType "Debugger.SetPauseOnExceptionsParameterType")

No documentation available

-   [state](././inspector/promises/~/Debugger.SetPauseOnExceptionsParameterType#property_state)

I

[Debugger.SetReturnValueParameterType](././inspector/promises/~/Debugger.SetReturnValueParameterType "Debugger.SetReturnValueParameterType")

No documentation available

-   [newValue](././inspector/promises/~/Debugger.SetReturnValueParameterType#property_newvalue)

I

[Debugger.SetScriptSourceParameterType](././inspector/promises/~/Debugger.SetScriptSourceParameterType "Debugger.SetScriptSourceParameterType")

No documentation available

-   [dryRun](././inspector/promises/~/Debugger.SetScriptSourceParameterType#property_dryrun)
-   [scriptId](././inspector/promises/~/Debugger.SetScriptSourceParameterType#property_scriptid)
-   [scriptSource](././inspector/promises/~/Debugger.SetScriptSourceParameterType#property_scriptsource)

I

[Debugger.SetScriptSourceReturnType](././inspector/promises/~/Debugger.SetScriptSourceReturnType "Debugger.SetScriptSourceReturnType")

No documentation available

-   [asyncStackTrace](././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_asyncstacktrace)
-   [asyncStackTraceId](././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_asyncstacktraceid)
-   [callFrames](././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_callframes)
-   [exceptionDetails](././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_exceptiondetails)
-   [stackChanged](././inspector/promises/~/Debugger.SetScriptSourceReturnType#property_stackchanged)

I

[Debugger.SetSkipAllPausesParameterType](././inspector/promises/~/Debugger.SetSkipAllPausesParameterType "Debugger.SetSkipAllPausesParameterType")

No documentation available

-   [skip](././inspector/promises/~/Debugger.SetSkipAllPausesParameterType#property_skip)

I

[Debugger.SetVariableValueParameterType](././inspector/promises/~/Debugger.SetVariableValueParameterType "Debugger.SetVariableValueParameterType")

No documentation available

-   [callFrameId](././inspector/promises/~/Debugger.SetVariableValueParameterType#property_callframeid)
-   [newValue](././inspector/promises/~/Debugger.SetVariableValueParameterType#property_newvalue)
-   [scopeNumber](././inspector/promises/~/Debugger.SetVariableValueParameterType#property_scopenumber)
-   [variableName](././inspector/promises/~/Debugger.SetVariableValueParameterType#property_variablename)

I

[Debugger.StepIntoParameterType](././inspector/promises/~/Debugger.StepIntoParameterType "Debugger.StepIntoParameterType")

No documentation available

-   [breakOnAsyncCall](././inspector/promises/~/Debugger.StepIntoParameterType#property_breakonasynccall)

N

[HeapProfiler](././inspector/promises/~/HeapProfiler "HeapProfiler")

No documentation available

I

[HeapProfiler.AddHeapSnapshotChunkEventDataType](././inspector/promises/~/HeapProfiler.AddHeapSnapshotChunkEventDataType "HeapProfiler.AddHeapSnapshotChunkEventDataType")

No documentation available

-   [chunk](././inspector/promises/~/HeapProfiler.AddHeapSnapshotChunkEventDataType#property_chunk)

I

[HeapProfiler.AddInspectedHeapObjectParameterType](././inspector/promises/~/HeapProfiler.AddInspectedHeapObjectParameterType "HeapProfiler.AddInspectedHeapObjectParameterType")

No documentation available

-   [heapObjectId](././inspector/promises/~/HeapProfiler.AddInspectedHeapObjectParameterType#property_heapobjectid)

I

[HeapProfiler.GetHeapObjectIdParameterType](././inspector/promises/~/HeapProfiler.GetHeapObjectIdParameterType "HeapProfiler.GetHeapObjectIdParameterType")

No documentation available

-   [objectId](././inspector/promises/~/HeapProfiler.GetHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetHeapObjectIdReturnType](././inspector/promises/~/HeapProfiler.GetHeapObjectIdReturnType "HeapProfiler.GetHeapObjectIdReturnType")

No documentation available

-   [heapSnapshotObjectId](././inspector/promises/~/HeapProfiler.GetHeapObjectIdReturnType#property_heapsnapshotobjectid)

I

[HeapProfiler.GetObjectByHeapObjectIdParameterType](././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdParameterType "HeapProfiler.GetObjectByHeapObjectIdParameterType")

No documentation available

-   [objectGroup](././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectgroup)
-   [objectId](././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdParameterType#property_objectid)

I

[HeapProfiler.GetObjectByHeapObjectIdReturnType](././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdReturnType "HeapProfiler.GetObjectByHeapObjectIdReturnType")

No documentation available

-   [result](././inspector/promises/~/HeapProfiler.GetObjectByHeapObjectIdReturnType#property_result)

I

[HeapProfiler.GetSamplingProfileReturnType](././inspector/promises/~/HeapProfiler.GetSamplingProfileReturnType "HeapProfiler.GetSamplingProfileReturnType")

No documentation available

-   [profile](././inspector/promises/~/HeapProfiler.GetSamplingProfileReturnType#property_profile)

T

[HeapProfiler.HeapSnapshotObjectId](././inspector/promises/~/HeapProfiler.HeapSnapshotObjectId "HeapProfiler.HeapSnapshotObjectId")

Heap snapshot object id.

I

[HeapProfiler.HeapStatsUpdateEventDataType](././inspector/promises/~/HeapProfiler.HeapStatsUpdateEventDataType "HeapProfiler.HeapStatsUpdateEventDataType")

No documentation available

-   [statsUpdate](././inspector/promises/~/HeapProfiler.HeapStatsUpdateEventDataType#property_statsupdate)

I

[HeapProfiler.LastSeenObjectIdEventDataType](././inspector/promises/~/HeapProfiler.LastSeenObjectIdEventDataType "HeapProfiler.LastSeenObjectIdEventDataType")

No documentation available

-   [lastSeenObjectId](././inspector/promises/~/HeapProfiler.LastSeenObjectIdEventDataType#property_lastseenobjectid)
-   [timestamp](././inspector/promises/~/HeapProfiler.LastSeenObjectIdEventDataType#property_timestamp)

I

[HeapProfiler.ReportHeapSnapshotProgressEventDataType](././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType "HeapProfiler.ReportHeapSnapshotProgressEventDataType")

No documentation available

-   [done](././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_done)
-   [finished](././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_finished)
-   [total](././inspector/promises/~/HeapProfiler.ReportHeapSnapshotProgressEventDataType#property_total)

I

[HeapProfiler.SamplingHeapProfile](././inspector/promises/~/HeapProfiler.SamplingHeapProfile "HeapProfiler.SamplingHeapProfile")

Profile.

-   [head](././inspector/promises/~/HeapProfiler.SamplingHeapProfile#property_head)

I

[HeapProfiler.SamplingHeapProfileNode](././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode "HeapProfiler.SamplingHeapProfileNode")

Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.

-   [callFrame](././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode#property_callframe)
-   [children](././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode#property_children)
-   [selfSize](././inspector/promises/~/HeapProfiler.SamplingHeapProfileNode#property_selfsize)

I

[HeapProfiler.StartSamplingParameterType](././inspector/promises/~/HeapProfiler.StartSamplingParameterType "HeapProfiler.StartSamplingParameterType")

No documentation available

-   [samplingInterval](././inspector/promises/~/HeapProfiler.StartSamplingParameterType#property_samplinginterval)

I

[HeapProfiler.StartTrackingHeapObjectsParameterType](././inspector/promises/~/HeapProfiler.StartTrackingHeapObjectsParameterType "HeapProfiler.StartTrackingHeapObjectsParameterType")

No documentation available

-   [trackAllocations](././inspector/promises/~/HeapProfiler.StartTrackingHeapObjectsParameterType#property_trackallocations)

I

[HeapProfiler.StopSamplingReturnType](././inspector/promises/~/HeapProfiler.StopSamplingReturnType "HeapProfiler.StopSamplingReturnType")

No documentation available

-   [profile](././inspector/promises/~/HeapProfiler.StopSamplingReturnType#property_profile)

I

[HeapProfiler.StopTrackingHeapObjectsParameterType](././inspector/promises/~/HeapProfiler.StopTrackingHeapObjectsParameterType "HeapProfiler.StopTrackingHeapObjectsParameterType")

No documentation available

-   [reportProgress](././inspector/promises/~/HeapProfiler.StopTrackingHeapObjectsParameterType#property_reportprogress)

I

[HeapProfiler.TakeHeapSnapshotParameterType](././inspector/promises/~/HeapProfiler.TakeHeapSnapshotParameterType "HeapProfiler.TakeHeapSnapshotParameterType")

No documentation available

-   [reportProgress](././inspector/promises/~/HeapProfiler.TakeHeapSnapshotParameterType#property_reportprogress)

N

[Network](././inspector/promises/~/Network "Network")

No documentation available

I

[Network.Headers](././inspector/promises/~/Network.Headers "Network.Headers")

Request / response headers as keys / values of JSON object.

f

[Network.loadingFailed](././inspector/promises/~/Network.loadingFailed "Network.loadingFailed")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.LoadingFailedEventDataType](././inspector/promises/~/Network.LoadingFailedEventDataType "Network.LoadingFailedEventDataType")

No documentation available

-   [errorText](././inspector/promises/~/Network.LoadingFailedEventDataType#property_errortext)
-   [requestId](././inspector/promises/~/Network.LoadingFailedEventDataType#property_requestid)
-   [timestamp](././inspector/promises/~/Network.LoadingFailedEventDataType#property_timestamp)
-   [type](././inspector/promises/~/Network.LoadingFailedEventDataType#property_type)

f

[Network.loadingFinished](././inspector/promises/~/Network.loadingFinished "Network.loadingFinished")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.LoadingFinishedEventDataType](././inspector/promises/~/Network.LoadingFinishedEventDataType "Network.LoadingFinishedEventDataType")

No documentation available

-   [requestId](././inspector/promises/~/Network.LoadingFinishedEventDataType#property_requestid)
-   [timestamp](././inspector/promises/~/Network.LoadingFinishedEventDataType#property_timestamp)

T

[Network.MonotonicTime](././inspector/promises/~/Network.MonotonicTime "Network.MonotonicTime")

Monotonically increasing time in seconds since an arbitrary point in the past.

I

[Network.Request](././inspector/promises/~/Network.Request "Network.Request")

HTTP request data.

-   [headers](././inspector/promises/~/Network.Request#property_headers)
-   [method](././inspector/promises/~/Network.Request#property_method)
-   [url](././inspector/promises/~/Network.Request#property_url)

T

[Network.RequestId](././inspector/promises/~/Network.RequestId "Network.RequestId")

Unique request identifier.

f

[Network.requestWillBeSent](././inspector/promises/~/Network.requestWillBeSent "Network.requestWillBeSent")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.RequestWillBeSentEventDataType](././inspector/promises/~/Network.RequestWillBeSentEventDataType "Network.RequestWillBeSentEventDataType")

No documentation available

-   [request](././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_request)
-   [requestId](././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_requestid)
-   [timestamp](././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_timestamp)
-   [wallTime](././inspector/promises/~/Network.RequestWillBeSentEventDataType#property_walltime)

T

[Network.ResourceType](././inspector/promises/~/Network.ResourceType "Network.ResourceType")

Resource type as it was perceived by the rendering engine.

I

[Network.Response](././inspector/promises/~/Network.Response "Network.Response")

HTTP response data.

-   [headers](././inspector/promises/~/Network.Response#property_headers)
-   [status](././inspector/promises/~/Network.Response#property_status)
-   [statusText](././inspector/promises/~/Network.Response#property_statustext)
-   [url](././inspector/promises/~/Network.Response#property_url)

f

[Network.responseReceived](././inspector/promises/~/Network.responseReceived "Network.responseReceived")

This feature is only available with the `--experimental-network-inspection` flag enabled.

I

[Network.ResponseReceivedEventDataType](././inspector/promises/~/Network.ResponseReceivedEventDataType "Network.ResponseReceivedEventDataType")

No documentation available

-   [requestId](././inspector/promises/~/Network.ResponseReceivedEventDataType#property_requestid)
-   [response](././inspector/promises/~/Network.ResponseReceivedEventDataType#property_response)
-   [timestamp](././inspector/promises/~/Network.ResponseReceivedEventDataType#property_timestamp)
-   [type](././inspector/promises/~/Network.ResponseReceivedEventDataType#property_type)

T

[Network.TimeSinceEpoch](././inspector/promises/~/Network.TimeSinceEpoch "Network.TimeSinceEpoch")

UTC time in seconds, counted from January 1, 1970.

N

[NodeRuntime](././inspector/promises/~/NodeRuntime "NodeRuntime")

No documentation available

I

[NodeRuntime.NotifyWhenWaitingForDisconnectParameterType](././inspector/promises/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType "NodeRuntime.NotifyWhenWaitingForDisconnectParameterType")

No documentation available

-   [enabled](././inspector/promises/~/NodeRuntime.NotifyWhenWaitingForDisconnectParameterType#property_enabled)

N

[NodeTracing](././inspector/promises/~/NodeTracing "NodeTracing")

No documentation available

I

[NodeTracing.DataCollectedEventDataType](././inspector/promises/~/NodeTracing.DataCollectedEventDataType "NodeTracing.DataCollectedEventDataType")

No documentation available

-   [value](././inspector/promises/~/NodeTracing.DataCollectedEventDataType#property_value)

I

[NodeTracing.GetCategoriesReturnType](././inspector/promises/~/NodeTracing.GetCategoriesReturnType "NodeTracing.GetCategoriesReturnType")

No documentation available

-   [categories](././inspector/promises/~/NodeTracing.GetCategoriesReturnType#property_categories)

I

[NodeTracing.StartParameterType](././inspector/promises/~/NodeTracing.StartParameterType "NodeTracing.StartParameterType")

No documentation available

-   [traceConfig](././inspector/promises/~/NodeTracing.StartParameterType#property_traceconfig)

I

[NodeTracing.TraceConfig](././inspector/promises/~/NodeTracing.TraceConfig "NodeTracing.TraceConfig")

No documentation available

-   [includedCategories](././inspector/promises/~/NodeTracing.TraceConfig#property_includedcategories)
-   [recordMode](././inspector/promises/~/NodeTracing.TraceConfig#property_recordmode)

N

[NodeWorker](././inspector/promises/~/NodeWorker "NodeWorker")

No documentation available

I

[NodeWorker.AttachedToWorkerEventDataType](././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType "NodeWorker.AttachedToWorkerEventDataType")

No documentation available

-   [sessionId](././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType#property_sessionid)
-   [waitingForDebugger](././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType#property_waitingfordebugger)
-   [workerInfo](././inspector/promises/~/NodeWorker.AttachedToWorkerEventDataType#property_workerinfo)

I

[NodeWorker.DetachedFromWorkerEventDataType](././inspector/promises/~/NodeWorker.DetachedFromWorkerEventDataType "NodeWorker.DetachedFromWorkerEventDataType")

No documentation available

-   [sessionId](././inspector/promises/~/NodeWorker.DetachedFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.DetachParameterType](././inspector/promises/~/NodeWorker.DetachParameterType "NodeWorker.DetachParameterType")

No documentation available

-   [sessionId](././inspector/promises/~/NodeWorker.DetachParameterType#property_sessionid)

I

[NodeWorker.EnableParameterType](././inspector/promises/~/NodeWorker.EnableParameterType "NodeWorker.EnableParameterType")

No documentation available

-   [waitForDebuggerOnStart](././inspector/promises/~/NodeWorker.EnableParameterType#property_waitfordebuggeronstart)

I

[NodeWorker.ReceivedMessageFromWorkerEventDataType](././inspector/promises/~/NodeWorker.ReceivedMessageFromWorkerEventDataType "NodeWorker.ReceivedMessageFromWorkerEventDataType")

No documentation available

-   [message](././inspector/promises/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_message)
-   [sessionId](././inspector/promises/~/NodeWorker.ReceivedMessageFromWorkerEventDataType#property_sessionid)

I

[NodeWorker.SendMessageToWorkerParameterType](././inspector/promises/~/NodeWorker.SendMessageToWorkerParameterType "NodeWorker.SendMessageToWorkerParameterType")

No documentation available

-   [message](././inspector/promises/~/NodeWorker.SendMessageToWorkerParameterType#property_message)
-   [sessionId](././inspector/promises/~/NodeWorker.SendMessageToWorkerParameterType#property_sessionid)

T

[NodeWorker.SessionID](././inspector/promises/~/NodeWorker.SessionID "NodeWorker.SessionID")

Unique identifier of attached debugging session.

T

[NodeWorker.WorkerID](././inspector/promises/~/NodeWorker.WorkerID "NodeWorker.WorkerID")

No documentation available

I

[NodeWorker.WorkerInfo](././inspector/promises/~/NodeWorker.WorkerInfo "NodeWorker.WorkerInfo")

No documentation available

-   [title](././inspector/promises/~/NodeWorker.WorkerInfo#property_title)
-   [type](././inspector/promises/~/NodeWorker.WorkerInfo#property_type)
-   [url](././inspector/promises/~/NodeWorker.WorkerInfo#property_url)
-   [workerId](././inspector/promises/~/NodeWorker.WorkerInfo#property_workerid)

N

[Profiler](././inspector/promises/~/Profiler "Profiler")

No documentation available

I

[Profiler.ConsoleProfileFinishedEventDataType](././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType "Profiler.ConsoleProfileFinishedEventDataType")

No documentation available

-   [id](././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_id)
-   [location](././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_location)
-   [profile](././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_profile)
-   [title](././inspector/promises/~/Profiler.ConsoleProfileFinishedEventDataType#property_title)

I

[Profiler.ConsoleProfileStartedEventDataType](././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType "Profiler.ConsoleProfileStartedEventDataType")

No documentation available

-   [id](././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType#property_id)
-   [location](././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType#property_location)
-   [title](././inspector/promises/~/Profiler.ConsoleProfileStartedEventDataType#property_title)

I

[Profiler.CoverageRange](././inspector/promises/~/Profiler.CoverageRange "Profiler.CoverageRange")

Coverage data for a source range.

-   [count](././inspector/promises/~/Profiler.CoverageRange#property_count)
-   [endOffset](././inspector/promises/~/Profiler.CoverageRange#property_endoffset)
-   [startOffset](././inspector/promises/~/Profiler.CoverageRange#property_startoffset)

I

[Profiler.FunctionCoverage](././inspector/promises/~/Profiler.FunctionCoverage "Profiler.FunctionCoverage")

Coverage data for a JavaScript function.

-   [functionName](././inspector/promises/~/Profiler.FunctionCoverage#property_functionname)
-   [isBlockCoverage](././inspector/promises/~/Profiler.FunctionCoverage#property_isblockcoverage)
-   [ranges](././inspector/promises/~/Profiler.FunctionCoverage#property_ranges)

I

[Profiler.GetBestEffortCoverageReturnType](././inspector/promises/~/Profiler.GetBestEffortCoverageReturnType "Profiler.GetBestEffortCoverageReturnType")

No documentation available

-   [result](././inspector/promises/~/Profiler.GetBestEffortCoverageReturnType#property_result)

I

[Profiler.PositionTickInfo](././inspector/promises/~/Profiler.PositionTickInfo "Profiler.PositionTickInfo")

Specifies a number of samples attributed to a certain source position.

-   [line](././inspector/promises/~/Profiler.PositionTickInfo#property_line)
-   [ticks](././inspector/promises/~/Profiler.PositionTickInfo#property_ticks)

I

[Profiler.Profile](././inspector/promises/~/Profiler.Profile "Profiler.Profile")

Profile.

-   [endTime](././inspector/promises/~/Profiler.Profile#property_endtime)
-   [nodes](././inspector/promises/~/Profiler.Profile#property_nodes)
-   [samples](././inspector/promises/~/Profiler.Profile#property_samples)
-   [startTime](././inspector/promises/~/Profiler.Profile#property_starttime)
-   [timeDeltas](././inspector/promises/~/Profiler.Profile#property_timedeltas)

I

[Profiler.ProfileNode](././inspector/promises/~/Profiler.ProfileNode "Profiler.ProfileNode")

Profile node. Holds callsite information, execution statistics and child nodes.

-   [callFrame](././inspector/promises/~/Profiler.ProfileNode#property_callframe)
-   [children](././inspector/promises/~/Profiler.ProfileNode#property_children)
-   [deoptReason](././inspector/promises/~/Profiler.ProfileNode#property_deoptreason)
-   [hitCount](././inspector/promises/~/Profiler.ProfileNode#property_hitcount)
-   [id](././inspector/promises/~/Profiler.ProfileNode#property_id)
-   [positionTicks](././inspector/promises/~/Profiler.ProfileNode#property_positionticks)

I

[Profiler.ScriptCoverage](././inspector/promises/~/Profiler.ScriptCoverage "Profiler.ScriptCoverage")

Coverage data for a JavaScript script.

-   [functions](././inspector/promises/~/Profiler.ScriptCoverage#property_functions)
-   [scriptId](././inspector/promises/~/Profiler.ScriptCoverage#property_scriptid)
-   [url](././inspector/promises/~/Profiler.ScriptCoverage#property_url)

I

[Profiler.SetSamplingIntervalParameterType](././inspector/promises/~/Profiler.SetSamplingIntervalParameterType "Profiler.SetSamplingIntervalParameterType")

No documentation available

-   [interval](././inspector/promises/~/Profiler.SetSamplingIntervalParameterType#property_interval)

I

[Profiler.StartPreciseCoverageParameterType](././inspector/promises/~/Profiler.StartPreciseCoverageParameterType "Profiler.StartPreciseCoverageParameterType")

No documentation available

-   [callCount](././inspector/promises/~/Profiler.StartPreciseCoverageParameterType#property_callcount)
-   [detailed](././inspector/promises/~/Profiler.StartPreciseCoverageParameterType#property_detailed)

I

[Profiler.StopReturnType](././inspector/promises/~/Profiler.StopReturnType "Profiler.StopReturnType")

No documentation available

-   [profile](././inspector/promises/~/Profiler.StopReturnType#property_profile)

I

[Profiler.TakePreciseCoverageReturnType](././inspector/promises/~/Profiler.TakePreciseCoverageReturnType "Profiler.TakePreciseCoverageReturnType")

No documentation available

-   [result](././inspector/promises/~/Profiler.TakePreciseCoverageReturnType#property_result)

N

[Runtime](././inspector/promises/~/Runtime "Runtime")

No documentation available

I

[Runtime.AwaitPromiseParameterType](././inspector/promises/~/Runtime.AwaitPromiseParameterType "Runtime.AwaitPromiseParameterType")

No documentation available

-   [generatePreview](././inspector/promises/~/Runtime.AwaitPromiseParameterType#property_generatepreview)
-   [promiseObjectId](././inspector/promises/~/Runtime.AwaitPromiseParameterType#property_promiseobjectid)
-   [returnByValue](././inspector/promises/~/Runtime.AwaitPromiseParameterType#property_returnbyvalue)

I

[Runtime.AwaitPromiseReturnType](././inspector/promises/~/Runtime.AwaitPromiseReturnType "Runtime.AwaitPromiseReturnType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Runtime.AwaitPromiseReturnType#property_exceptiondetails)
-   [result](././inspector/promises/~/Runtime.AwaitPromiseReturnType#property_result)

I

[Runtime.CallArgument](././inspector/promises/~/Runtime.CallArgument "Runtime.CallArgument")

Represents function call argument. Either remote object id `objectId`, primitive `value`, unserializable primitive value or neither of (for undefined) them should be specified.

-   [objectId](././inspector/promises/~/Runtime.CallArgument#property_objectid)
-   [unserializableValue](././inspector/promises/~/Runtime.CallArgument#property_unserializablevalue)
-   [value](././inspector/promises/~/Runtime.CallArgument#property_value)

I

[Runtime.CallFrame](././inspector/promises/~/Runtime.CallFrame "Runtime.CallFrame")

Stack entry for runtime errors and assertions.

-   [columnNumber](././inspector/promises/~/Runtime.CallFrame#property_columnnumber)
-   [functionName](././inspector/promises/~/Runtime.CallFrame#property_functionname)
-   [lineNumber](././inspector/promises/~/Runtime.CallFrame#property_linenumber)
-   [scriptId](././inspector/promises/~/Runtime.CallFrame#property_scriptid)
-   [url](././inspector/promises/~/Runtime.CallFrame#property_url)

I

[Runtime.CallFunctionOnParameterType](././inspector/promises/~/Runtime.CallFunctionOnParameterType "Runtime.CallFunctionOnParameterType")

No documentation available

-   [arguments](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_arguments)
-   [awaitPromise](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_awaitpromise)
-   [executionContextId](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_executioncontextid)
-   [functionDeclaration](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_functiondeclaration)
-   [generatePreview](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_generatepreview)
-   [objectGroup](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_objectgroup)
-   [objectId](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_objectid)
-   [returnByValue](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_returnbyvalue)
-   [silent](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_silent)
-   [userGesture](././inspector/promises/~/Runtime.CallFunctionOnParameterType#property_usergesture)

I

[Runtime.CallFunctionOnReturnType](././inspector/promises/~/Runtime.CallFunctionOnReturnType "Runtime.CallFunctionOnReturnType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Runtime.CallFunctionOnReturnType#property_exceptiondetails)
-   [result](././inspector/promises/~/Runtime.CallFunctionOnReturnType#property_result)

I

[Runtime.CompileScriptParameterType](././inspector/promises/~/Runtime.CompileScriptParameterType "Runtime.CompileScriptParameterType")

No documentation available

-   [executionContextId](././inspector/promises/~/Runtime.CompileScriptParameterType#property_executioncontextid)
-   [expression](././inspector/promises/~/Runtime.CompileScriptParameterType#property_expression)
-   [persistScript](././inspector/promises/~/Runtime.CompileScriptParameterType#property_persistscript)
-   [sourceURL](././inspector/promises/~/Runtime.CompileScriptParameterType#property_sourceurl)

I

[Runtime.CompileScriptReturnType](././inspector/promises/~/Runtime.CompileScriptReturnType "Runtime.CompileScriptReturnType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Runtime.CompileScriptReturnType#property_exceptiondetails)
-   [scriptId](././inspector/promises/~/Runtime.CompileScriptReturnType#property_scriptid)

I

[Runtime.ConsoleAPICalledEventDataType](././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType "Runtime.ConsoleAPICalledEventDataType")

No documentation available

-   [args](././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_args)
-   [context](././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_context)
-   [executionContextId](././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_executioncontextid)
-   [stackTrace](././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_stacktrace)
-   [timestamp](././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_timestamp)
-   [type](././inspector/promises/~/Runtime.ConsoleAPICalledEventDataType#property_type)

I

[Runtime.CustomPreview](././inspector/promises/~/Runtime.CustomPreview "Runtime.CustomPreview")

No documentation available

-   [bindRemoteObjectFunctionId](././inspector/promises/~/Runtime.CustomPreview#property_bindremoteobjectfunctionid)
-   [configObjectId](././inspector/promises/~/Runtime.CustomPreview#property_configobjectid)
-   [formatterObjectId](././inspector/promises/~/Runtime.CustomPreview#property_formatterobjectid)
-   [hasBody](././inspector/promises/~/Runtime.CustomPreview#property_hasbody)
-   [header](././inspector/promises/~/Runtime.CustomPreview#property_header)

I

[Runtime.EntryPreview](././inspector/promises/~/Runtime.EntryPreview "Runtime.EntryPreview")

No documentation available

-   [key](././inspector/promises/~/Runtime.EntryPreview#property_key)
-   [value](././inspector/promises/~/Runtime.EntryPreview#property_value)

I

[Runtime.EvaluateParameterType](././inspector/promises/~/Runtime.EvaluateParameterType "Runtime.EvaluateParameterType")

No documentation available

-   [awaitPromise](././inspector/promises/~/Runtime.EvaluateParameterType#property_awaitpromise)
-   [contextId](././inspector/promises/~/Runtime.EvaluateParameterType#property_contextid)
-   [expression](././inspector/promises/~/Runtime.EvaluateParameterType#property_expression)
-   [generatePreview](././inspector/promises/~/Runtime.EvaluateParameterType#property_generatepreview)
-   [includeCommandLineAPI](././inspector/promises/~/Runtime.EvaluateParameterType#property_includecommandlineapi)
-   [objectGroup](././inspector/promises/~/Runtime.EvaluateParameterType#property_objectgroup)
-   [returnByValue](././inspector/promises/~/Runtime.EvaluateParameterType#property_returnbyvalue)
-   [silent](././inspector/promises/~/Runtime.EvaluateParameterType#property_silent)
-   [userGesture](././inspector/promises/~/Runtime.EvaluateParameterType#property_usergesture)

I

[Runtime.EvaluateReturnType](././inspector/promises/~/Runtime.EvaluateReturnType "Runtime.EvaluateReturnType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Runtime.EvaluateReturnType#property_exceptiondetails)
-   [result](././inspector/promises/~/Runtime.EvaluateReturnType#property_result)

I

[Runtime.ExceptionDetails](././inspector/promises/~/Runtime.ExceptionDetails "Runtime.ExceptionDetails")

Detailed information about exception (or error) that was thrown during script compilation or execution.

-   [columnNumber](././inspector/promises/~/Runtime.ExceptionDetails#property_columnnumber)
-   [exception](././inspector/promises/~/Runtime.ExceptionDetails#property_exception)
-   [exceptionId](././inspector/promises/~/Runtime.ExceptionDetails#property_exceptionid)
-   [executionContextId](././inspector/promises/~/Runtime.ExceptionDetails#property_executioncontextid)
-   [lineNumber](././inspector/promises/~/Runtime.ExceptionDetails#property_linenumber)
-   [scriptId](././inspector/promises/~/Runtime.ExceptionDetails#property_scriptid)
-   [stackTrace](././inspector/promises/~/Runtime.ExceptionDetails#property_stacktrace)
-   [text](././inspector/promises/~/Runtime.ExceptionDetails#property_text)
-   [url](././inspector/promises/~/Runtime.ExceptionDetails#property_url)

I

[Runtime.ExceptionRevokedEventDataType](././inspector/promises/~/Runtime.ExceptionRevokedEventDataType "Runtime.ExceptionRevokedEventDataType")

No documentation available

-   [exceptionId](././inspector/promises/~/Runtime.ExceptionRevokedEventDataType#property_exceptionid)
-   [reason](././inspector/promises/~/Runtime.ExceptionRevokedEventDataType#property_reason)

I

[Runtime.ExceptionThrownEventDataType](././inspector/promises/~/Runtime.ExceptionThrownEventDataType "Runtime.ExceptionThrownEventDataType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Runtime.ExceptionThrownEventDataType#property_exceptiondetails)
-   [timestamp](././inspector/promises/~/Runtime.ExceptionThrownEventDataType#property_timestamp)

I

[Runtime.ExecutionContextCreatedEventDataType](././inspector/promises/~/Runtime.ExecutionContextCreatedEventDataType "Runtime.ExecutionContextCreatedEventDataType")

No documentation available

-   [context](././inspector/promises/~/Runtime.ExecutionContextCreatedEventDataType#property_context)

I

[Runtime.ExecutionContextDescription](././inspector/promises/~/Runtime.ExecutionContextDescription "Runtime.ExecutionContextDescription")

Description of an isolated world.

-   [auxData](././inspector/promises/~/Runtime.ExecutionContextDescription#property_auxdata)
-   [id](././inspector/promises/~/Runtime.ExecutionContextDescription#property_id)
-   [name](././inspector/promises/~/Runtime.ExecutionContextDescription#property_name)
-   [origin](././inspector/promises/~/Runtime.ExecutionContextDescription#property_origin)

I

[Runtime.ExecutionContextDestroyedEventDataType](././inspector/promises/~/Runtime.ExecutionContextDestroyedEventDataType "Runtime.ExecutionContextDestroyedEventDataType")

No documentation available

-   [executionContextId](././inspector/promises/~/Runtime.ExecutionContextDestroyedEventDataType#property_executioncontextid)

T

[Runtime.ExecutionContextId](././inspector/promises/~/Runtime.ExecutionContextId "Runtime.ExecutionContextId")

Id of an execution context.

I

[Runtime.GetPropertiesParameterType](././inspector/promises/~/Runtime.GetPropertiesParameterType "Runtime.GetPropertiesParameterType")

No documentation available

-   [accessorPropertiesOnly](././inspector/promises/~/Runtime.GetPropertiesParameterType#property_accessorpropertiesonly)
-   [generatePreview](././inspector/promises/~/Runtime.GetPropertiesParameterType#property_generatepreview)
-   [objectId](././inspector/promises/~/Runtime.GetPropertiesParameterType#property_objectid)
-   [ownProperties](././inspector/promises/~/Runtime.GetPropertiesParameterType#property_ownproperties)

I

[Runtime.GetPropertiesReturnType](././inspector/promises/~/Runtime.GetPropertiesReturnType "Runtime.GetPropertiesReturnType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Runtime.GetPropertiesReturnType#property_exceptiondetails)
-   [internalProperties](././inspector/promises/~/Runtime.GetPropertiesReturnType#property_internalproperties)
-   [result](././inspector/promises/~/Runtime.GetPropertiesReturnType#property_result)

I

[Runtime.GlobalLexicalScopeNamesParameterType](././inspector/promises/~/Runtime.GlobalLexicalScopeNamesParameterType "Runtime.GlobalLexicalScopeNamesParameterType")

No documentation available

-   [executionContextId](././inspector/promises/~/Runtime.GlobalLexicalScopeNamesParameterType#property_executioncontextid)

I

[Runtime.GlobalLexicalScopeNamesReturnType](././inspector/promises/~/Runtime.GlobalLexicalScopeNamesReturnType "Runtime.GlobalLexicalScopeNamesReturnType")

No documentation available

-   [names](././inspector/promises/~/Runtime.GlobalLexicalScopeNamesReturnType#property_names)

I

[Runtime.InspectRequestedEventDataType](././inspector/promises/~/Runtime.InspectRequestedEventDataType "Runtime.InspectRequestedEventDataType")

No documentation available

-   [hints](././inspector/promises/~/Runtime.InspectRequestedEventDataType#property_hints)
-   [object](././inspector/promises/~/Runtime.InspectRequestedEventDataType#property_object)

I

[Runtime.InternalPropertyDescriptor](././inspector/promises/~/Runtime.InternalPropertyDescriptor "Runtime.InternalPropertyDescriptor")

Object internal property descriptor. This property isn't normally visible in JavaScript code.

-   [name](././inspector/promises/~/Runtime.InternalPropertyDescriptor#property_name)
-   [value](././inspector/promises/~/Runtime.InternalPropertyDescriptor#property_value)

I

[Runtime.ObjectPreview](././inspector/promises/~/Runtime.ObjectPreview "Runtime.ObjectPreview")

Object containing abbreviated remote object value.

-   [description](././inspector/promises/~/Runtime.ObjectPreview#property_description)
-   [entries](././inspector/promises/~/Runtime.ObjectPreview#property_entries)
-   [overflow](././inspector/promises/~/Runtime.ObjectPreview#property_overflow)
-   [properties](././inspector/promises/~/Runtime.ObjectPreview#property_properties)
-   [subtype](././inspector/promises/~/Runtime.ObjectPreview#property_subtype)
-   [type](././inspector/promises/~/Runtime.ObjectPreview#property_type)

I

[Runtime.PropertyDescriptor](././inspector/promises/~/Runtime.PropertyDescriptor "Runtime.PropertyDescriptor")

Object property descriptor.

-   [configurable](././inspector/promises/~/Runtime.PropertyDescriptor#property_configurable)
-   [enumerable](././inspector/promises/~/Runtime.PropertyDescriptor#property_enumerable)
-   [get](././inspector/promises/~/Runtime.PropertyDescriptor#property_get)
-   [isOwn](././inspector/promises/~/Runtime.PropertyDescriptor#property_isown)
-   [name](././inspector/promises/~/Runtime.PropertyDescriptor#property_name)
-   [set](././inspector/promises/~/Runtime.PropertyDescriptor#property_set)
-   [symbol](././inspector/promises/~/Runtime.PropertyDescriptor#property_symbol)
-   [value](././inspector/promises/~/Runtime.PropertyDescriptor#property_value)
-   [wasThrown](././inspector/promises/~/Runtime.PropertyDescriptor#property_wasthrown)
-   [writable](././inspector/promises/~/Runtime.PropertyDescriptor#property_writable)

I

[Runtime.PropertyPreview](././inspector/promises/~/Runtime.PropertyPreview "Runtime.PropertyPreview")

No documentation available

-   [name](././inspector/promises/~/Runtime.PropertyPreview#property_name)
-   [subtype](././inspector/promises/~/Runtime.PropertyPreview#property_subtype)
-   [type](././inspector/promises/~/Runtime.PropertyPreview#property_type)
-   [value](././inspector/promises/~/Runtime.PropertyPreview#property_value)
-   [valuePreview](././inspector/promises/~/Runtime.PropertyPreview#property_valuepreview)

I

[Runtime.QueryObjectsParameterType](././inspector/promises/~/Runtime.QueryObjectsParameterType "Runtime.QueryObjectsParameterType")

No documentation available

-   [prototypeObjectId](././inspector/promises/~/Runtime.QueryObjectsParameterType#property_prototypeobjectid)

I

[Runtime.QueryObjectsReturnType](././inspector/promises/~/Runtime.QueryObjectsReturnType "Runtime.QueryObjectsReturnType")

No documentation available

-   [objects](././inspector/promises/~/Runtime.QueryObjectsReturnType#property_objects)

I

[Runtime.ReleaseObjectGroupParameterType](././inspector/promises/~/Runtime.ReleaseObjectGroupParameterType "Runtime.ReleaseObjectGroupParameterType")

No documentation available

-   [objectGroup](././inspector/promises/~/Runtime.ReleaseObjectGroupParameterType#property_objectgroup)

I

[Runtime.ReleaseObjectParameterType](././inspector/promises/~/Runtime.ReleaseObjectParameterType "Runtime.ReleaseObjectParameterType")

No documentation available

-   [objectId](././inspector/promises/~/Runtime.ReleaseObjectParameterType#property_objectid)

I

[Runtime.RemoteObject](././inspector/promises/~/Runtime.RemoteObject "Runtime.RemoteObject")

Mirror object referencing original JavaScript object.

-   [className](././inspector/promises/~/Runtime.RemoteObject#property_classname)
-   [customPreview](././inspector/promises/~/Runtime.RemoteObject#property_custompreview)
-   [description](././inspector/promises/~/Runtime.RemoteObject#property_description)
-   [objectId](././inspector/promises/~/Runtime.RemoteObject#property_objectid)
-   [preview](././inspector/promises/~/Runtime.RemoteObject#property_preview)
-   [subtype](././inspector/promises/~/Runtime.RemoteObject#property_subtype)
-   [type](././inspector/promises/~/Runtime.RemoteObject#property_type)
-   [unserializableValue](././inspector/promises/~/Runtime.RemoteObject#property_unserializablevalue)
-   [value](././inspector/promises/~/Runtime.RemoteObject#property_value)

T

[Runtime.RemoteObjectId](././inspector/promises/~/Runtime.RemoteObjectId "Runtime.RemoteObjectId")

Unique object identifier.

I

[Runtime.RunScriptParameterType](././inspector/promises/~/Runtime.RunScriptParameterType "Runtime.RunScriptParameterType")

No documentation available

-   [awaitPromise](././inspector/promises/~/Runtime.RunScriptParameterType#property_awaitpromise)
-   [executionContextId](././inspector/promises/~/Runtime.RunScriptParameterType#property_executioncontextid)
-   [generatePreview](././inspector/promises/~/Runtime.RunScriptParameterType#property_generatepreview)
-   [includeCommandLineAPI](././inspector/promises/~/Runtime.RunScriptParameterType#property_includecommandlineapi)
-   [objectGroup](././inspector/promises/~/Runtime.RunScriptParameterType#property_objectgroup)
-   [returnByValue](././inspector/promises/~/Runtime.RunScriptParameterType#property_returnbyvalue)
-   [scriptId](././inspector/promises/~/Runtime.RunScriptParameterType#property_scriptid)
-   [silent](././inspector/promises/~/Runtime.RunScriptParameterType#property_silent)

I

[Runtime.RunScriptReturnType](././inspector/promises/~/Runtime.RunScriptReturnType "Runtime.RunScriptReturnType")

No documentation available

-   [exceptionDetails](././inspector/promises/~/Runtime.RunScriptReturnType#property_exceptiondetails)
-   [result](././inspector/promises/~/Runtime.RunScriptReturnType#property_result)

T

[Runtime.ScriptId](././inspector/promises/~/Runtime.ScriptId "Runtime.ScriptId")

Unique script identifier.

I

[Runtime.SetCustomObjectFormatterEnabledParameterType](././inspector/promises/~/Runtime.SetCustomObjectFormatterEnabledParameterType "Runtime.SetCustomObjectFormatterEnabledParameterType")

No documentation available

-   [enabled](././inspector/promises/~/Runtime.SetCustomObjectFormatterEnabledParameterType#property_enabled)

I

[Runtime.StackTrace](././inspector/promises/~/Runtime.StackTrace "Runtime.StackTrace")

Call frames for assertions or error messages.

-   [callFrames](././inspector/promises/~/Runtime.StackTrace#property_callframes)
-   [description](././inspector/promises/~/Runtime.StackTrace#property_description)
-   [parent](././inspector/promises/~/Runtime.StackTrace#property_parent)
-   [parentId](././inspector/promises/~/Runtime.StackTrace#property_parentid)

I

[Runtime.StackTraceId](././inspector/promises/~/Runtime.StackTraceId "Runtime.StackTraceId")

If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.

-   [debuggerId](././inspector/promises/~/Runtime.StackTraceId#property_debuggerid)
-   [id](././inspector/promises/~/Runtime.StackTraceId#property_id)

T

[Runtime.Timestamp](././inspector/promises/~/Runtime.Timestamp "Runtime.Timestamp")

Number of milliseconds since epoch.

T

[Runtime.UniqueDebuggerId](././inspector/promises/~/Runtime.UniqueDebuggerId "Runtime.UniqueDebuggerId")

Unique identifier of current debugger.

T

[Runtime.UnserializableValue](././inspector/promises/~/Runtime.UnserializableValue "Runtime.UnserializableValue")

Primitive value which cannot be JSON-stringified.

N

[Schema](././inspector/promises/~/Schema "Schema")

No documentation available

I

[Schema.Domain](././inspector/promises/~/Schema.Domain "Schema.Domain")

Description of the protocol domain.

-   [name](././inspector/promises/~/Schema.Domain#property_name)
-   [version](././inspector/promises/~/Schema.Domain#property_version)

I

[Schema.GetDomainsReturnType](././inspector/promises/~/Schema.GetDomainsReturnType "Schema.GetDomainsReturnType")

No documentation available

-   [domains](././inspector/promises/~/Schema.GetDomainsReturnType#property_domains)

c

[Session](././inspector/promises/~/Session "Session")

The `inspector.Session` is used for dispatching messages to the V8 inspector back-end and receiving message responses and notifications.

-   [addListener](././inspector/promises/~/Session#method_addlistener_0)
-   [connect](././inspector/promises/~/Session#method_connect_0)
-   [connectToMainThread](././inspector/promises/~/Session#method_connecttomainthread_0)
-   [disconnect](././inspector/promises/~/Session#method_disconnect_0)
-   [emit](././inspector/promises/~/Session#method_emit_0)
-   [on](././inspector/promises/~/Session#method_on_0)
-   [once](././inspector/promises/~/Session#method_once_0)
-   [post](././inspector/promises/~/Session#method_post_0)
-   [prependListener](././inspector/promises/~/Session#method_prependlistener_0)
-   [prependOnceListener](././inspector/promises/~/Session#method_prependoncelistener_0)

v

[\_\_dirname](././module/~/__dirname "__dirname")

The directory name of the current module. This is the same as the `path.dirname()` of the `__filename`.

v

[\_\_filename](././module/~/__filename "__filename")

The file name of the current module. This is the current module file's absolute path with symlinks resolved.

v

[exports](././module/~/exports "exports")

The `exports` variable is available within a module's file-level scope, and is assigned the value of `module.exports` before the module is evaluated.

I

[ImportMeta](././module/~/ImportMeta "ImportMeta")

No documentation available

-   [dirname](././module/~/ImportMeta#property_dirname)
-   [filename](././module/~/ImportMeta#property_filename)
-   [resolve](././module/~/ImportMeta#method_resolve_0)
-   [url](././module/~/ImportMeta#property_url)

c

I

N

[Module](././module/~/Module "Module")

No documentation available

-   [children](././module/~/Module#property_children)
-   [exports](././module/~/Module#property_exports)
-   [filename](././module/~/Module#property_filename)
-   [id](././module/~/Module#property_id)
-   [isPreloading](././module/~/Module#property_ispreloading)
-   [loaded](././module/~/Module#property_loaded)
-   [parent](././module/~/Module#property_parent)
-   [path](././module/~/Module#property_path)
-   [paths](././module/~/Module#property_paths)
-   [require](././module/~/Module#method_require_0)

v

[module](././module/~/module "module")

A reference to the current module.

v

[Module.builtinModules](././module/~/Module.builtinModules "Module.builtinModules")

A list of the names of all modules provided by Node.js. Can be used to verify if a module is maintained by a third party or not.

N

[Module.constants](././module/~/Module.constants "Module.constants")

No documentation available

N

[Module.constants.compileCacheStatus](././module/~/Module.constants.compileCacheStatus "Module.constants.compileCacheStatus")

The following constants are returned as the `status` field in the object returned by enableCompileCache to indicate the result of the attempt to enable the [module compile cache](https://nodejs.org/docs/latest-v22.x/api/module.html#module-compile-cache).

v

[Module.constants.compileCacheStatus.ALREADY\_ENABLED](././module/~/Module.constants.compileCacheStatus.ALREADY_ENABLED "Module.constants.compileCacheStatus.ALREADY_ENABLED")

The compile cache has already been enabled before, either by a previous call to enableCompileCache, or by the `NODE_COMPILE_CACHE=dir` environment variable. The directory used to store the compile cache will be returned in the `directory` field in the returned object.

v

[Module.constants.compileCacheStatus.DISABLED](././module/~/Module.constants.compileCacheStatus.DISABLED "Module.constants.compileCacheStatus.DISABLED")

Node.js cannot enable the compile cache because the environment variable `NODE_DISABLE_COMPILE_CACHE=1` has been set.

v

[Module.constants.compileCacheStatus.ENABLED](././module/~/Module.constants.compileCacheStatus.ENABLED "Module.constants.compileCacheStatus.ENABLED")

Node.js has enabled the compile cache successfully. The directory used to store the compile cache will be returned in the `directory` field in the returned object.

v

[Module.constants.compileCacheStatus.FAILED](././module/~/Module.constants.compileCacheStatus.FAILED "Module.constants.compileCacheStatus.FAILED")

Node.js fails to enable the compile cache. This can be caused by the lack of permission to use the specified directory, or various kinds of file system errors. The detail of the failure will be returned in the `message` field in the returned object.

f

[Module.createRequire](././module/~/Module.createRequire "Module.createRequire")

No documentation available

f

[Module.enableCompileCache](././module/~/Module.enableCompileCache "Module.enableCompileCache")

Enable [module compile cache](https://nodejs.org/docs/latest-v22.x/api/module.html#module-compile-cache) in the current Node.js instance.

I

[Module.EnableCompileCacheResult](././module/~/Module.EnableCompileCacheResult "Module.EnableCompileCacheResult")

No documentation available

-   [directory](././module/~/Module.EnableCompileCacheResult#property_directory)
-   [message](././module/~/Module.EnableCompileCacheResult#property_message)
-   [status](././module/~/Module.EnableCompileCacheResult#property_status)

f

[Module.findPackageJSON](././module/~/Module.findPackageJSON "Module.findPackageJSON")

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

[Module.findSourceMap](././module/~/Module.findSourceMap "Module.findSourceMap")

`path` is the resolved path for the file for which a corresponding source map should be fetched.

f

[Module.flushCompileCache](././module/~/Module.flushCompileCache "Module.flushCompileCache")

Flush the [module compile cache](https://nodejs.org/docs/latest-v22.x/api/module.html#module-compile-cache) accumulated from modules already loaded in the current Node.js instance to disk. This returns after all the flushing file system operations come to an end, no matter they succeed or not. If there are any errors, this will fail silently, since compile cache misses should not interfere with the actual operation of the application.

f

[Module.getCompileCacheDir](././module/~/Module.getCompileCacheDir "Module.getCompileCacheDir")

No documentation available

I

[Module.ImportAttributes](././module/~/Module.ImportAttributes "Module.ImportAttributes")

No documentation available

-   [type](././module/~/Module.ImportAttributes#property_type)

T

[Module.InitializeHook](././module/~/Module.InitializeHook "Module.InitializeHook")

The `initialize` hook provides a way to define a custom function that runs in the hooks thread when the hooks module is initialized. Initialization happens when the hooks module is registered via register.

f

[Module.isBuiltin](././module/~/Module.isBuiltin "Module.isBuiltin")

No documentation available

I

[Module.LoadFnOutput](././module/~/Module.LoadFnOutput "Module.LoadFnOutput")

No documentation available

-   [format](././module/~/Module.LoadFnOutput#property_format)
-   [shortCircuit](././module/~/Module.LoadFnOutput#property_shortcircuit)
-   [source](././module/~/Module.LoadFnOutput#property_source)

T

[Module.LoadHook](././module/~/Module.LoadHook "Module.LoadHook")

The `load` hook provides a way to define a custom method of determining how a URL should be interpreted, retrieved, and parsed. It is also in charge of validating the import attributes.

I

[Module.LoadHookContext](././module/~/Module.LoadHookContext "Module.LoadHookContext")

No documentation available

-   [conditions](././module/~/Module.LoadHookContext#property_conditions)
-   [format](././module/~/Module.LoadHookContext#property_format)
-   [importAttributes](././module/~/Module.LoadHookContext#property_importattributes)

T

[Module.ModuleFormat](././module/~/Module.ModuleFormat "Module.ModuleFormat")

No documentation available

T

[Module.ModuleSource](././module/~/Module.ModuleSource "Module.ModuleSource")

No documentation available

f

[Module.register](././module/~/Module.register "Module.register")

Register a module that exports hooks that customize Node.js module resolution and loading behavior. See [Customization hooks](https://nodejs.org/docs/latest-v22.x/api/module.html#customization-hooks).

I

[Module.RegisterOptions](././module/~/Module.RegisterOptions "Module.RegisterOptions")

No documentation available

-   [data](././module/~/Module.RegisterOptions#property_data)
-   [parentURL](././module/~/Module.RegisterOptions#property_parenturl)
-   [transferList](././module/~/Module.RegisterOptions#property_transferlist)

I

[Module.ResolveFnOutput](././module/~/Module.ResolveFnOutput "Module.ResolveFnOutput")

No documentation available

-   [format](././module/~/Module.ResolveFnOutput#property_format)
-   [importAttributes](././module/~/Module.ResolveFnOutput#property_importattributes)
-   [shortCircuit](././module/~/Module.ResolveFnOutput#property_shortcircuit)
-   [url](././module/~/Module.ResolveFnOutput#property_url)

T

[Module.ResolveHook](././module/~/Module.ResolveHook "Module.ResolveHook")

The `resolve` hook chain is responsible for telling Node.js where to find and how to cache a given `import` statement or expression, or `require` call. It can optionally return a format (such as `'module'`) as a hint to the `load` hook. If a format is specified, the `load` hook is ultimately responsible for providing the final `format` value (and it is free to ignore the hint provided by `resolve`); if `resolve` provides a `format`, a custom `load` hook is required even if only to pass the value to the Node.js default `load` hook.

I

[Module.ResolveHookContext](././module/~/Module.ResolveHookContext "Module.ResolveHookContext")

No documentation available

-   [conditions](././module/~/Module.ResolveHookContext#property_conditions)
-   [importAttributes](././module/~/Module.ResolveHookContext#property_importattributes)
-   [parentURL](././module/~/Module.ResolveHookContext#property_parenturl)

f

[Module.runMain](././module/~/Module.runMain "Module.runMain")

No documentation available

c

[Module.SourceMap](././module/~/Module.SourceMap "Module.SourceMap")

No documentation available

-   [findEntry](././module/~/Module.SourceMap#method_findentry_0)
-   [findOrigin](././module/~/Module.SourceMap#method_findorigin_0)
-   [payload](././module/~/Module.SourceMap#property_payload)

I

[Module.SourceMapConstructorOptions](././module/~/Module.SourceMapConstructorOptions "Module.SourceMapConstructorOptions")

No documentation available

-   [lineLengths](././module/~/Module.SourceMapConstructorOptions#property_linelengths)

I

[Module.SourceMapPayload](././module/~/Module.SourceMapPayload "Module.SourceMapPayload")

No documentation available

-   [file](././module/~/Module.SourceMapPayload#property_file)
-   [mappings](././module/~/Module.SourceMapPayload#property_mappings)
-   [names](././module/~/Module.SourceMapPayload#property_names)
-   [sourceRoot](././module/~/Module.SourceMapPayload#property_sourceroot)
-   [sources](././module/~/Module.SourceMapPayload#property_sources)
-   [sourcesContent](././module/~/Module.SourceMapPayload#property_sourcescontent)
-   [version](././module/~/Module.SourceMapPayload#property_version)

I

[Module.SourceMapping](././module/~/Module.SourceMapping "Module.SourceMapping")

No documentation available

-   [generatedColumn](././module/~/Module.SourceMapping#property_generatedcolumn)
-   [generatedLine](././module/~/Module.SourceMapping#property_generatedline)
-   [originalColumn](././module/~/Module.SourceMapping#property_originalcolumn)
-   [originalLine](././module/~/Module.SourceMapping#property_originalline)
-   [originalSource](././module/~/Module.SourceMapping#property_originalsource)

I

[Module.SourceOrigin](././module/~/Module.SourceOrigin "Module.SourceOrigin")

No documentation available

-   [columnNumber](././module/~/Module.SourceOrigin#property_columnnumber)
-   [fileName](././module/~/Module.SourceOrigin#property_filename)
-   [lineNumber](././module/~/Module.SourceOrigin#property_linenumber)
-   [name](././module/~/Module.SourceOrigin#property_name)

f

[Module.stripTypeScriptTypes](././module/~/Module.stripTypeScriptTypes "Module.stripTypeScriptTypes")

`module.stripTypeScriptTypes()` removes type annotations from TypeScript code. It can be used to strip type annotations from TypeScript code before running it with `vm.runInContext()` or `vm.compileFunction()`. By default, it will throw an error if the code contains TypeScript features that require transformation such as `Enums`, see [type-stripping](https://nodejs.org/docs/latest-v22.x/api/typescript.md#type-stripping) for more information. When mode is `'transform'`, it also transforms TypeScript features to JavaScript, see [transform TypeScript features](https://nodejs.org/docs/latest-v22.x/api/typescript.md#typescript-features) for more information. When mode is `'strip'`, source maps are not generated, because locations are preserved. If `sourceMap` is provided, when mode is `'strip'`, an error will be thrown.

I

[Module.StripTypeScriptTypesOptions](././module/~/Module.StripTypeScriptTypesOptions "Module.StripTypeScriptTypesOptions")

No documentation available

-   [mode](././module/~/Module.StripTypeScriptTypesOptions#property_mode)
-   [sourceMap](././module/~/Module.StripTypeScriptTypesOptions#property_sourcemap)
-   [sourceUrl](././module/~/Module.StripTypeScriptTypesOptions#property_sourceurl)

f

[Module.syncBuiltinESMExports](././module/~/Module.syncBuiltinESMExports "Module.syncBuiltinESMExports")

The `module.syncBuiltinESMExports()` method updates all the live bindings for builtin `ES Modules` to match the properties of the `CommonJS` exports. It does not add or remove exported names from the `ES Modules`.

f

[Module.wrap](././module/~/Module.wrap "Module.wrap")

No documentation available

I

[Require](././module/~/Require "Require")

No documentation available

-   [cache](././module/~/Require#property_cache)
-   [extensions](././module/~/Require#property_extensions)
-   [main](././module/~/Require#property_main)
-   [resolve](././module/~/Require#property_resolve)

v

[require](././module/~/require "require")

No documentation available

I

[RequireResolve](././module/~/RequireResolve "RequireResolve")

No documentation available

-   [paths](././module/~/RequireResolve#method_paths_0)

I

[RequireResolveOptions](././module/~/RequireResolveOptions "RequireResolveOptions")

No documentation available

-   [paths](././module/~/RequireResolveOptions#property_paths)

I

[NodeModule](././module/~/NodeModule "NodeModule")

No documentation available

I

[NodeRequire](././module/~/NodeRequire "NodeRequire")

No documentation available

I

[RequireExtensions](././module/~/RequireExtensions "RequireExtensions")

No documentation available

-   [.js](././module/~/RequireExtensions#property__js)
-   [.json](././module/~/RequireExtensions#property__json)
-   [.node](././module/~/RequireExtensions#property__node)

Stability: 2 - Stable

I

[AddressInfo](././net/~/AddressInfo "AddressInfo")

No documentation available

-   [address](././net/~/AddressInfo#property_address)
-   [family](././net/~/AddressInfo#property_family)
-   [port](././net/~/AddressInfo#property_port)

c

[BlockList](././net/~/BlockList "BlockList")

The `BlockList` object can be used with some network APIs to specify rules for disabling inbound or outbound access to specific IP addresses, IP ranges, or IP subnets.

-   [addAddress](././net/~/BlockList#method_addaddress_0)
-   [addRange](././net/~/BlockList#method_addrange_0)
-   [addSubnet](././net/~/BlockList#method_addsubnet_0)
-   [check](././net/~/BlockList#method_check_0)
-   [isBlockList](././net/~/BlockList#method_isblocklist_0)
-   [rules](././net/~/BlockList#property_rules)

f

[connect](././net/~/connect "connect")

Aliases to [createConnection](././net/~/createConnection).

f

[createConnection](././net/~/createConnection "createConnection")

A factory function, which creates a new [Socket](././net/~/Socket), immediately initiates connection with `socket.connect()`, then returns the `net.Socket` that starts the connection.

f

[createServer](././net/~/createServer "createServer")

Creates a new TCP or `IPC` server.

I

[DropArgument](././net/~/DropArgument "DropArgument")

No documentation available

-   [localAddress](././net/~/DropArgument#property_localaddress)
-   [localFamily](././net/~/DropArgument#property_localfamily)
-   [localPort](././net/~/DropArgument#property_localport)
-   [remoteAddress](././net/~/DropArgument#property_remoteaddress)
-   [remoteFamily](././net/~/DropArgument#property_remotefamily)
-   [remotePort](././net/~/DropArgument#property_remoteport)

f

[getDefaultAutoSelectFamily](././net/~/getDefaultAutoSelectFamily "getDefaultAutoSelectFamily")

Gets the current default value of the `autoSelectFamily` option of `socket.connect(options)`. The initial default value is `true`, unless the command line option`--no-network-family-autoselection` is provided.

f

[getDefaultAutoSelectFamilyAttemptTimeout](././net/~/getDefaultAutoSelectFamilyAttemptTimeout "getDefaultAutoSelectFamilyAttemptTimeout")

Gets the current default value of the `autoSelectFamilyAttemptTimeout` option of `socket.connect(options)`. The initial default value is `250` or the value specified via the command line option `--network-family-autoselection-attempt-timeout`.

I

[IpcNetConnectOpts](././net/~/IpcNetConnectOpts "IpcNetConnectOpts")

No documentation available

-   [timeout](././net/~/IpcNetConnectOpts#property_timeout)

I

[IpcSocketConnectOpts](././net/~/IpcSocketConnectOpts "IpcSocketConnectOpts")

No documentation available

-   [path](././net/~/IpcSocketConnectOpts#property_path)

T

[IPVersion](././net/~/IPVersion "IPVersion")

No documentation available

f

[isIP](././net/~/isIP "isIP")

Returns `6` if `input` is an IPv6 address. Returns `4` if `input` is an IPv4 address in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) with no leading zeroes. Otherwise, returns`0`.

f

[isIPv4](././net/~/isIPv4 "isIPv4")

Returns `true` if `input` is an IPv4 address in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) with no leading zeroes. Otherwise, returns `false`.

f

[isIPv6](././net/~/isIPv6 "isIPv6")

Returns `true` if `input` is an IPv6 address. Otherwise, returns `false`.

I

[ListenOptions](././net/~/ListenOptions "ListenOptions")

No documentation available

-   [backlog](././net/~/ListenOptions#property_backlog)
-   [exclusive](././net/~/ListenOptions#property_exclusive)
-   [host](././net/~/ListenOptions#property_host)
-   [ipv6Only](././net/~/ListenOptions#property_ipv6only)
-   [path](././net/~/ListenOptions#property_path)
-   [port](././net/~/ListenOptions#property_port)
-   [readableAll](././net/~/ListenOptions#property_readableall)
-   [reusePort](././net/~/ListenOptions#property_reuseport)
-   [writableAll](././net/~/ListenOptions#property_writableall)

T

[LookupFunction](././net/~/LookupFunction "LookupFunction")

No documentation available

T

[NetConnectOpts](././net/~/NetConnectOpts "NetConnectOpts")

No documentation available

I

[OnReadOpts](././net/~/OnReadOpts "OnReadOpts")

No documentation available

-   [buffer](././net/~/OnReadOpts#property_buffer)
-   [callback](././net/~/OnReadOpts#method_callback_0)

c

[Server](././net/~/Server "Server")

This class is used to create a TCP or `IPC` server.

-   [addListener](././net/~/Server#method_addlistener_0)
-   [address](././net/~/Server#method_address_0)
-   [close](././net/~/Server#method_close_0)
-   [connections](././net/~/Server#property_connections)
-   [emit](././net/~/Server#method_emit_0)
-   [getConnections](././net/~/Server#method_getconnections_0)
-   [listen](././net/~/Server#method_listen_0)
-   [listening](././net/~/Server#property_listening)
-   [maxConnections](././net/~/Server#property_maxconnections)
-   [on](././net/~/Server#method_on_0)
-   [once](././net/~/Server#method_once_0)
-   [prependListener](././net/~/Server#method_prependlistener_0)
-   [prependOnceListener](././net/~/Server#method_prependoncelistener_0)
-   [ref](././net/~/Server#method_ref_0)
-   [unref](././net/~/Server#method_unref_0)

I

[ServerOpts](././net/~/ServerOpts "ServerOpts")

No documentation available

-   [allowHalfOpen](././net/~/ServerOpts#property_allowhalfopen)
-   [blockList](././net/~/ServerOpts#property_blocklist)
-   [highWaterMark](././net/~/ServerOpts#property_highwatermark)
-   [keepAlive](././net/~/ServerOpts#property_keepalive)
-   [keepAliveInitialDelay](././net/~/ServerOpts#property_keepaliveinitialdelay)
-   [noDelay](././net/~/ServerOpts#property_nodelay)
-   [pauseOnConnect](././net/~/ServerOpts#property_pauseonconnect)

f

[setDefaultAutoSelectFamily](././net/~/setDefaultAutoSelectFamily "setDefaultAutoSelectFamily")

Sets the default value of the `autoSelectFamily` option of `socket.connect(options)`.

f

[setDefaultAutoSelectFamilyAttemptTimeout](././net/~/setDefaultAutoSelectFamilyAttemptTimeout "setDefaultAutoSelectFamilyAttemptTimeout")

Sets the default value of the `autoSelectFamilyAttemptTimeout` option of `socket.connect(options)`.

c

[Socket](././net/~/Socket "Socket")

No documentation available

-   [addListener](././net/~/Socket#method_addlistener_0)
-   [address](././net/~/Socket#method_address_0)
-   [autoSelectFamilyAttemptedAddresses](././net/~/Socket#property_autoselectfamilyattemptedaddresses)
-   [bufferSize](././net/~/Socket#property_buffersize)
-   [bytesRead](././net/~/Socket#property_bytesread)
-   [bytesWritten](././net/~/Socket#property_byteswritten)
-   [connect](././net/~/Socket#method_connect_0)
-   [connecting](././net/~/Socket#property_connecting)
-   [destroySoon](././net/~/Socket#method_destroysoon_0)
-   [destroyed](././net/~/Socket#property_destroyed)
-   [emit](././net/~/Socket#method_emit_0)
-   [end](././net/~/Socket#method_end_0)
-   [localAddress](././net/~/Socket#property_localaddress)
-   [localFamily](././net/~/Socket#property_localfamily)
-   [localPort](././net/~/Socket#property_localport)
-   [on](././net/~/Socket#method_on_0)
-   [once](././net/~/Socket#method_once_0)
-   [pause](././net/~/Socket#method_pause_0)
-   [pending](././net/~/Socket#property_pending)
-   [prependListener](././net/~/Socket#method_prependlistener_0)
-   [prependOnceListener](././net/~/Socket#method_prependoncelistener_0)
-   [readyState](././net/~/Socket#property_readystate)
-   [ref](././net/~/Socket#method_ref_0)
-   [remoteAddress](././net/~/Socket#property_remoteaddress)
-   [remoteFamily](././net/~/Socket#property_remotefamily)
-   [remotePort](././net/~/Socket#property_remoteport)
-   [resetAndDestroy](././net/~/Socket#method_resetanddestroy_0)
-   [resume](././net/~/Socket#method_resume_0)
-   [setEncoding](././net/~/Socket#method_setencoding_0)
-   [setKeepAlive](././net/~/Socket#method_setkeepalive_0)
-   [setNoDelay](././net/~/Socket#method_setnodelay_0)
-   [setTimeout](././net/~/Socket#method_settimeout_0)
-   [timeout](././net/~/Socket#property_timeout)
-   [unref](././net/~/Socket#method_unref_0)
-   [write](././net/~/Socket#method_write_0)

c

[SocketAddress](././net/~/SocketAddress "SocketAddress")

No documentation available

-   [address](././net/~/SocketAddress#property_address)
-   [family](././net/~/SocketAddress#property_family)
-   [flowlabel](././net/~/SocketAddress#property_flowlabel)
-   [parse](././net/~/SocketAddress#method_parse_0)
-   [port](././net/~/SocketAddress#property_port)

I

[SocketAddressInitOptions](././net/~/SocketAddressInitOptions "SocketAddressInitOptions")

No documentation available

-   [address](././net/~/SocketAddressInitOptions#property_address)
-   [family](././net/~/SocketAddressInitOptions#property_family)
-   [flowlabel](././net/~/SocketAddressInitOptions#property_flowlabel)
-   [port](././net/~/SocketAddressInitOptions#property_port)

T

[SocketConnectOpts](././net/~/SocketConnectOpts "SocketConnectOpts")

No documentation available

I

[SocketConstructorOpts](././net/~/SocketConstructorOpts "SocketConstructorOpts")

No documentation available

-   [allowHalfOpen](././net/~/SocketConstructorOpts#property_allowhalfopen)
-   [fd](././net/~/SocketConstructorOpts#property_fd)
-   [onread](././net/~/SocketConstructorOpts#property_onread)
-   [readable](././net/~/SocketConstructorOpts#property_readable)
-   [signal](././net/~/SocketConstructorOpts#property_signal)
-   [writable](././net/~/SocketConstructorOpts#property_writable)

T

[SocketReadyState](././net/~/SocketReadyState "SocketReadyState")

No documentation available

I

[TcpNetConnectOpts](././net/~/TcpNetConnectOpts "TcpNetConnectOpts")

No documentation available

-   [timeout](././net/~/TcpNetConnectOpts#property_timeout)

I

[TcpSocketConnectOpts](././net/~/TcpSocketConnectOpts "TcpSocketConnectOpts")

No documentation available

-   [autoSelectFamily](././net/~/TcpSocketConnectOpts#property_autoselectfamily)
-   [autoSelectFamilyAttemptTimeout](././net/~/TcpSocketConnectOpts#property_autoselectfamilyattempttimeout)
-   [blockList](././net/~/TcpSocketConnectOpts#property_blocklist)
-   [family](././net/~/TcpSocketConnectOpts#property_family)
-   [hints](././net/~/TcpSocketConnectOpts#property_hints)
-   [host](././net/~/TcpSocketConnectOpts#property_host)
-   [keepAlive](././net/~/TcpSocketConnectOpts#property_keepalive)
-   [keepAliveInitialDelay](././net/~/TcpSocketConnectOpts#property_keepaliveinitialdelay)
-   [localAddress](././net/~/TcpSocketConnectOpts#property_localaddress)
-   [localPort](././net/~/TcpSocketConnectOpts#property_localport)
-   [lookup](././net/~/TcpSocketConnectOpts#property_lookup)
-   [noDelay](././net/~/TcpSocketConnectOpts#property_nodelay)
-   [port](././net/~/TcpSocketConnectOpts#property_port)

I

[ConnectOpts](././net/~/ConnectOpts "ConnectOpts")

No documentation available

The `node:os` module provides operating system-related utility methods and properties. It can be accessed using:

f

[arch](././os/~/arch "arch")

Returns the operating system CPU architecture for which the Node.js binary was compiled. Possible values are `'arm'`, `'arm64'`, `'ia32'`, `'loong64'`, `'mips'`, `'mipsel'`, `'ppc'`, `'ppc64'`, `'riscv64'`, `'s390'`, `'s390x'`, and `'x64'`.

f

[availableParallelism](././os/~/availableParallelism "availableParallelism")

Returns an estimate of the default amount of parallelism a program should use. Always returns a value greater than zero.

N

[constants](././os/~/constants "constants")

No documentation available

N

[constants.dlopen](././os/~/constants.dlopen "constants.dlopen")

No documentation available

v

[constants.dlopen.RTLD\_DEEPBIND](././os/~/constants.dlopen.RTLD_DEEPBIND "constants.dlopen.RTLD_DEEPBIND")

No documentation available

v

[constants.dlopen.RTLD\_GLOBAL](././os/~/constants.dlopen.RTLD_GLOBAL "constants.dlopen.RTLD_GLOBAL")

No documentation available

v

[constants.dlopen.RTLD\_LAZY](././os/~/constants.dlopen.RTLD_LAZY "constants.dlopen.RTLD_LAZY")

No documentation available

v

[constants.dlopen.RTLD\_LOCAL](././os/~/constants.dlopen.RTLD_LOCAL "constants.dlopen.RTLD_LOCAL")

No documentation available

v

[constants.dlopen.RTLD\_NOW](././os/~/constants.dlopen.RTLD_NOW "constants.dlopen.RTLD_NOW")

No documentation available

N

[constants.errno](././os/~/constants.errno "constants.errno")

No documentation available

v

[constants.errno.E2BIG](././os/~/constants.errno.E2BIG "constants.errno.E2BIG")

No documentation available

v

[constants.errno.EACCES](././os/~/constants.errno.EACCES "constants.errno.EACCES")

No documentation available

v

[constants.errno.EADDRINUSE](././os/~/constants.errno.EADDRINUSE "constants.errno.EADDRINUSE")

No documentation available

v

[constants.errno.EADDRNOTAVAIL](././os/~/constants.errno.EADDRNOTAVAIL "constants.errno.EADDRNOTAVAIL")

No documentation available

v

[constants.errno.EAFNOSUPPORT](././os/~/constants.errno.EAFNOSUPPORT "constants.errno.EAFNOSUPPORT")

No documentation available

v

[constants.errno.EAGAIN](././os/~/constants.errno.EAGAIN "constants.errno.EAGAIN")

No documentation available

v

[constants.errno.EALREADY](././os/~/constants.errno.EALREADY "constants.errno.EALREADY")

No documentation available

v

[constants.errno.EBADF](././os/~/constants.errno.EBADF "constants.errno.EBADF")

No documentation available

v

[constants.errno.EBADMSG](././os/~/constants.errno.EBADMSG "constants.errno.EBADMSG")

No documentation available

v

[constants.errno.EBUSY](././os/~/constants.errno.EBUSY "constants.errno.EBUSY")

No documentation available

v

[constants.errno.ECANCELED](././os/~/constants.errno.ECANCELED "constants.errno.ECANCELED")

No documentation available

v

[constants.errno.ECHILD](././os/~/constants.errno.ECHILD "constants.errno.ECHILD")

No documentation available

v

[constants.errno.ECONNABORTED](././os/~/constants.errno.ECONNABORTED "constants.errno.ECONNABORTED")

No documentation available

v

[constants.errno.ECONNREFUSED](././os/~/constants.errno.ECONNREFUSED "constants.errno.ECONNREFUSED")

No documentation available

v

[constants.errno.ECONNRESET](././os/~/constants.errno.ECONNRESET "constants.errno.ECONNRESET")

No documentation available

v

[constants.errno.EDEADLK](././os/~/constants.errno.EDEADLK "constants.errno.EDEADLK")

No documentation available

v

[constants.errno.EDESTADDRREQ](././os/~/constants.errno.EDESTADDRREQ "constants.errno.EDESTADDRREQ")

No documentation available

v

[constants.errno.EDOM](././os/~/constants.errno.EDOM "constants.errno.EDOM")

No documentation available

v

[constants.errno.EDQUOT](././os/~/constants.errno.EDQUOT "constants.errno.EDQUOT")

No documentation available

v

[constants.errno.EEXIST](././os/~/constants.errno.EEXIST "constants.errno.EEXIST")

No documentation available

v

[constants.errno.EFAULT](././os/~/constants.errno.EFAULT "constants.errno.EFAULT")

No documentation available

v

[constants.errno.EFBIG](././os/~/constants.errno.EFBIG "constants.errno.EFBIG")

No documentation available

v

[constants.errno.EHOSTUNREACH](././os/~/constants.errno.EHOSTUNREACH "constants.errno.EHOSTUNREACH")

No documentation available

v

[constants.errno.EIDRM](././os/~/constants.errno.EIDRM "constants.errno.EIDRM")

No documentation available

v

[constants.errno.EILSEQ](././os/~/constants.errno.EILSEQ "constants.errno.EILSEQ")

No documentation available

v

[constants.errno.EINPROGRESS](././os/~/constants.errno.EINPROGRESS "constants.errno.EINPROGRESS")

No documentation available

v

[constants.errno.EINTR](././os/~/constants.errno.EINTR "constants.errno.EINTR")

No documentation available

v

[constants.errno.EINVAL](././os/~/constants.errno.EINVAL "constants.errno.EINVAL")

No documentation available

v

[constants.errno.EIO](././os/~/constants.errno.EIO "constants.errno.EIO")

No documentation available

v

[constants.errno.EISCONN](././os/~/constants.errno.EISCONN "constants.errno.EISCONN")

No documentation available

v

[constants.errno.EISDIR](././os/~/constants.errno.EISDIR "constants.errno.EISDIR")

No documentation available

v

[constants.errno.ELOOP](././os/~/constants.errno.ELOOP "constants.errno.ELOOP")

No documentation available

v

[constants.errno.EMFILE](././os/~/constants.errno.EMFILE "constants.errno.EMFILE")

No documentation available

v

[constants.errno.EMLINK](././os/~/constants.errno.EMLINK "constants.errno.EMLINK")

No documentation available

v

[constants.errno.EMSGSIZE](././os/~/constants.errno.EMSGSIZE "constants.errno.EMSGSIZE")

No documentation available

v

[constants.errno.EMULTIHOP](././os/~/constants.errno.EMULTIHOP "constants.errno.EMULTIHOP")

No documentation available

v

[constants.errno.ENAMETOOLONG](././os/~/constants.errno.ENAMETOOLONG "constants.errno.ENAMETOOLONG")

No documentation available

v

[constants.errno.ENETDOWN](././os/~/constants.errno.ENETDOWN "constants.errno.ENETDOWN")

No documentation available

v

[constants.errno.ENETRESET](././os/~/constants.errno.ENETRESET "constants.errno.ENETRESET")

No documentation available

v

[constants.errno.ENETUNREACH](././os/~/constants.errno.ENETUNREACH "constants.errno.ENETUNREACH")

No documentation available

v

[constants.errno.ENFILE](././os/~/constants.errno.ENFILE "constants.errno.ENFILE")

No documentation available

v

[constants.errno.ENOBUFS](././os/~/constants.errno.ENOBUFS "constants.errno.ENOBUFS")

No documentation available

v

[constants.errno.ENODATA](././os/~/constants.errno.ENODATA "constants.errno.ENODATA")

No documentation available

v

[constants.errno.ENODEV](././os/~/constants.errno.ENODEV "constants.errno.ENODEV")

No documentation available

v

[constants.errno.ENOENT](././os/~/constants.errno.ENOENT "constants.errno.ENOENT")

No documentation available

v

[constants.errno.ENOEXEC](././os/~/constants.errno.ENOEXEC "constants.errno.ENOEXEC")

No documentation available

v

[constants.errno.ENOLCK](././os/~/constants.errno.ENOLCK "constants.errno.ENOLCK")

No documentation available

v

[constants.errno.ENOLINK](././os/~/constants.errno.ENOLINK "constants.errno.ENOLINK")

No documentation available

v

[constants.errno.ENOMEM](././os/~/constants.errno.ENOMEM "constants.errno.ENOMEM")

No documentation available

v

[constants.errno.ENOMSG](././os/~/constants.errno.ENOMSG "constants.errno.ENOMSG")

No documentation available

v

[constants.errno.ENOPROTOOPT](././os/~/constants.errno.ENOPROTOOPT "constants.errno.ENOPROTOOPT")

No documentation available

v

[constants.errno.ENOSPC](././os/~/constants.errno.ENOSPC "constants.errno.ENOSPC")

No documentation available

v

[constants.errno.ENOSR](././os/~/constants.errno.ENOSR "constants.errno.ENOSR")

No documentation available

v

[constants.errno.ENOSTR](././os/~/constants.errno.ENOSTR "constants.errno.ENOSTR")

No documentation available

v

[constants.errno.ENOSYS](././os/~/constants.errno.ENOSYS "constants.errno.ENOSYS")

No documentation available

v

[constants.errno.ENOTCONN](././os/~/constants.errno.ENOTCONN "constants.errno.ENOTCONN")

No documentation available

v

[constants.errno.ENOTDIR](././os/~/constants.errno.ENOTDIR "constants.errno.ENOTDIR")

No documentation available

v

[constants.errno.ENOTEMPTY](././os/~/constants.errno.ENOTEMPTY "constants.errno.ENOTEMPTY")

No documentation available

v

[constants.errno.ENOTSOCK](././os/~/constants.errno.ENOTSOCK "constants.errno.ENOTSOCK")

No documentation available

v

[constants.errno.ENOTSUP](././os/~/constants.errno.ENOTSUP "constants.errno.ENOTSUP")

No documentation available

v

[constants.errno.ENOTTY](././os/~/constants.errno.ENOTTY "constants.errno.ENOTTY")

No documentation available

v

[constants.errno.ENXIO](././os/~/constants.errno.ENXIO "constants.errno.ENXIO")

No documentation available

v

[constants.errno.EOPNOTSUPP](././os/~/constants.errno.EOPNOTSUPP "constants.errno.EOPNOTSUPP")

No documentation available

v

[constants.errno.EOVERFLOW](././os/~/constants.errno.EOVERFLOW "constants.errno.EOVERFLOW")

No documentation available

v

[constants.errno.EPERM](././os/~/constants.errno.EPERM "constants.errno.EPERM")

No documentation available

v

[constants.errno.EPIPE](././os/~/constants.errno.EPIPE "constants.errno.EPIPE")

No documentation available

v

[constants.errno.EPROTO](././os/~/constants.errno.EPROTO "constants.errno.EPROTO")

No documentation available

v

[constants.errno.EPROTONOSUPPORT](././os/~/constants.errno.EPROTONOSUPPORT "constants.errno.EPROTONOSUPPORT")

No documentation available

v

[constants.errno.EPROTOTYPE](././os/~/constants.errno.EPROTOTYPE "constants.errno.EPROTOTYPE")

No documentation available

v

[constants.errno.ERANGE](././os/~/constants.errno.ERANGE "constants.errno.ERANGE")

No documentation available

v

[constants.errno.EROFS](././os/~/constants.errno.EROFS "constants.errno.EROFS")

No documentation available

v

[constants.errno.ESPIPE](././os/~/constants.errno.ESPIPE "constants.errno.ESPIPE")

No documentation available

v

[constants.errno.ESRCH](././os/~/constants.errno.ESRCH "constants.errno.ESRCH")

No documentation available

v

[constants.errno.ESTALE](././os/~/constants.errno.ESTALE "constants.errno.ESTALE")

No documentation available

v

[constants.errno.ETIME](././os/~/constants.errno.ETIME "constants.errno.ETIME")

No documentation available

v

[constants.errno.ETIMEDOUT](././os/~/constants.errno.ETIMEDOUT "constants.errno.ETIMEDOUT")

No documentation available

v

[constants.errno.ETXTBSY](././os/~/constants.errno.ETXTBSY "constants.errno.ETXTBSY")

No documentation available

v

[constants.errno.EWOULDBLOCK](././os/~/constants.errno.EWOULDBLOCK "constants.errno.EWOULDBLOCK")

No documentation available

v

[constants.errno.EXDEV](././os/~/constants.errno.EXDEV "constants.errno.EXDEV")

No documentation available

v

[constants.errno.WSA\_E\_CANCELLED](././os/~/constants.errno.WSA_E_CANCELLED "constants.errno.WSA_E_CANCELLED")

No documentation available

v

[constants.errno.WSA\_E\_NO\_MORE](././os/~/constants.errno.WSA_E_NO_MORE "constants.errno.WSA_E_NO_MORE")

No documentation available

v

[constants.errno.WSAEACCES](././os/~/constants.errno.WSAEACCES "constants.errno.WSAEACCES")

No documentation available

v

[constants.errno.WSAEADDRINUSE](././os/~/constants.errno.WSAEADDRINUSE "constants.errno.WSAEADDRINUSE")

No documentation available

v

[constants.errno.WSAEADDRNOTAVAIL](././os/~/constants.errno.WSAEADDRNOTAVAIL "constants.errno.WSAEADDRNOTAVAIL")

No documentation available

v

[constants.errno.WSAEAFNOSUPPORT](././os/~/constants.errno.WSAEAFNOSUPPORT "constants.errno.WSAEAFNOSUPPORT")

No documentation available

v

[constants.errno.WSAEALREADY](././os/~/constants.errno.WSAEALREADY "constants.errno.WSAEALREADY")

No documentation available

v

[constants.errno.WSAEBADF](././os/~/constants.errno.WSAEBADF "constants.errno.WSAEBADF")

No documentation available

v

[constants.errno.WSAECANCELLED](././os/~/constants.errno.WSAECANCELLED "constants.errno.WSAECANCELLED")

No documentation available

v

[constants.errno.WSAECONNABORTED](././os/~/constants.errno.WSAECONNABORTED "constants.errno.WSAECONNABORTED")

No documentation available

v

[constants.errno.WSAECONNREFUSED](././os/~/constants.errno.WSAECONNREFUSED "constants.errno.WSAECONNREFUSED")

No documentation available

v

[constants.errno.WSAECONNRESET](././os/~/constants.errno.WSAECONNRESET "constants.errno.WSAECONNRESET")

No documentation available

v

[constants.errno.WSAEDESTADDRREQ](././os/~/constants.errno.WSAEDESTADDRREQ "constants.errno.WSAEDESTADDRREQ")

No documentation available

v

[constants.errno.WSAEDISCON](././os/~/constants.errno.WSAEDISCON "constants.errno.WSAEDISCON")

No documentation available

v

[constants.errno.WSAEDQUOT](././os/~/constants.errno.WSAEDQUOT "constants.errno.WSAEDQUOT")

No documentation available

v

[constants.errno.WSAEFAULT](././os/~/constants.errno.WSAEFAULT "constants.errno.WSAEFAULT")

No documentation available

v

[constants.errno.WSAEHOSTDOWN](././os/~/constants.errno.WSAEHOSTDOWN "constants.errno.WSAEHOSTDOWN")

No documentation available

v

[constants.errno.WSAEHOSTUNREACH](././os/~/constants.errno.WSAEHOSTUNREACH "constants.errno.WSAEHOSTUNREACH")

No documentation available

v

[constants.errno.WSAEINPROGRESS](././os/~/constants.errno.WSAEINPROGRESS "constants.errno.WSAEINPROGRESS")

No documentation available

v

[constants.errno.WSAEINTR](././os/~/constants.errno.WSAEINTR "constants.errno.WSAEINTR")

No documentation available

v

[constants.errno.WSAEINVAL](././os/~/constants.errno.WSAEINVAL "constants.errno.WSAEINVAL")

No documentation available

v

[constants.errno.WSAEINVALIDPROCTABLE](././os/~/constants.errno.WSAEINVALIDPROCTABLE "constants.errno.WSAEINVALIDPROCTABLE")

No documentation available

v

[constants.errno.WSAEINVALIDPROVIDER](././os/~/constants.errno.WSAEINVALIDPROVIDER "constants.errno.WSAEINVALIDPROVIDER")

No documentation available

v

[constants.errno.WSAEISCONN](././os/~/constants.errno.WSAEISCONN "constants.errno.WSAEISCONN")

No documentation available

v

[constants.errno.WSAELOOP](././os/~/constants.errno.WSAELOOP "constants.errno.WSAELOOP")

No documentation available

v

[constants.errno.WSAEMFILE](././os/~/constants.errno.WSAEMFILE "constants.errno.WSAEMFILE")

No documentation available

v

[constants.errno.WSAEMSGSIZE](././os/~/constants.errno.WSAEMSGSIZE "constants.errno.WSAEMSGSIZE")

No documentation available

v

[constants.errno.WSAENAMETOOLONG](././os/~/constants.errno.WSAENAMETOOLONG "constants.errno.WSAENAMETOOLONG")

No documentation available

v

[constants.errno.WSAENETDOWN](././os/~/constants.errno.WSAENETDOWN "constants.errno.WSAENETDOWN")

No documentation available

v

[constants.errno.WSAENETRESET](././os/~/constants.errno.WSAENETRESET "constants.errno.WSAENETRESET")

No documentation available

v

[constants.errno.WSAENETUNREACH](././os/~/constants.errno.WSAENETUNREACH "constants.errno.WSAENETUNREACH")

No documentation available

v

[constants.errno.WSAENOBUFS](././os/~/constants.errno.WSAENOBUFS "constants.errno.WSAENOBUFS")

No documentation available

v

[constants.errno.WSAENOMORE](././os/~/constants.errno.WSAENOMORE "constants.errno.WSAENOMORE")

No documentation available

v

[constants.errno.WSAENOPROTOOPT](././os/~/constants.errno.WSAENOPROTOOPT "constants.errno.WSAENOPROTOOPT")

No documentation available

v

[constants.errno.WSAENOTCONN](././os/~/constants.errno.WSAENOTCONN "constants.errno.WSAENOTCONN")

No documentation available

v

[constants.errno.WSAENOTEMPTY](././os/~/constants.errno.WSAENOTEMPTY "constants.errno.WSAENOTEMPTY")

No documentation available

v

[constants.errno.WSAENOTSOCK](././os/~/constants.errno.WSAENOTSOCK "constants.errno.WSAENOTSOCK")

No documentation available

v

[constants.errno.WSAEOPNOTSUPP](././os/~/constants.errno.WSAEOPNOTSUPP "constants.errno.WSAEOPNOTSUPP")

No documentation available

v

[constants.errno.WSAEPFNOSUPPORT](././os/~/constants.errno.WSAEPFNOSUPPORT "constants.errno.WSAEPFNOSUPPORT")

No documentation available

v

[constants.errno.WSAEPROCLIM](././os/~/constants.errno.WSAEPROCLIM "constants.errno.WSAEPROCLIM")

No documentation available

v

[constants.errno.WSAEPROTONOSUPPORT](././os/~/constants.errno.WSAEPROTONOSUPPORT "constants.errno.WSAEPROTONOSUPPORT")

No documentation available

v

[constants.errno.WSAEPROTOTYPE](././os/~/constants.errno.WSAEPROTOTYPE "constants.errno.WSAEPROTOTYPE")

No documentation available

v

[constants.errno.WSAEPROVIDERFAILEDINIT](././os/~/constants.errno.WSAEPROVIDERFAILEDINIT "constants.errno.WSAEPROVIDERFAILEDINIT")

No documentation available

v

[constants.errno.WSAEREFUSED](././os/~/constants.errno.WSAEREFUSED "constants.errno.WSAEREFUSED")

No documentation available

v

[constants.errno.WSAEREMOTE](././os/~/constants.errno.WSAEREMOTE "constants.errno.WSAEREMOTE")

No documentation available

v

[constants.errno.WSAESHUTDOWN](././os/~/constants.errno.WSAESHUTDOWN "constants.errno.WSAESHUTDOWN")

No documentation available

v

[constants.errno.WSAESOCKTNOSUPPORT](././os/~/constants.errno.WSAESOCKTNOSUPPORT "constants.errno.WSAESOCKTNOSUPPORT")

No documentation available

v

[constants.errno.WSAESTALE](././os/~/constants.errno.WSAESTALE "constants.errno.WSAESTALE")

No documentation available

v

[constants.errno.WSAETIMEDOUT](././os/~/constants.errno.WSAETIMEDOUT "constants.errno.WSAETIMEDOUT")

No documentation available

v

[constants.errno.WSAETOOMANYREFS](././os/~/constants.errno.WSAETOOMANYREFS "constants.errno.WSAETOOMANYREFS")

No documentation available

v

[constants.errno.WSAEUSERS](././os/~/constants.errno.WSAEUSERS "constants.errno.WSAEUSERS")

No documentation available

v

[constants.errno.WSAEWOULDBLOCK](././os/~/constants.errno.WSAEWOULDBLOCK "constants.errno.WSAEWOULDBLOCK")

No documentation available

v

[constants.errno.WSANOTINITIALISED](././os/~/constants.errno.WSANOTINITIALISED "constants.errno.WSANOTINITIALISED")

No documentation available

v

[constants.errno.WSASERVICE\_NOT\_FOUND](././os/~/constants.errno.WSASERVICE_NOT_FOUND "constants.errno.WSASERVICE_NOT_FOUND")

No documentation available

v

[constants.errno.WSASYSCALLFAILURE](././os/~/constants.errno.WSASYSCALLFAILURE "constants.errno.WSASYSCALLFAILURE")

No documentation available

v

[constants.errno.WSASYSNOTREADY](././os/~/constants.errno.WSASYSNOTREADY "constants.errno.WSASYSNOTREADY")

No documentation available

v

[constants.errno.WSATYPE\_NOT\_FOUND](././os/~/constants.errno.WSATYPE_NOT_FOUND "constants.errno.WSATYPE_NOT_FOUND")

No documentation available

v

[constants.errno.WSAVERNOTSUPPORTED](././os/~/constants.errno.WSAVERNOTSUPPORTED "constants.errno.WSAVERNOTSUPPORTED")

No documentation available

N

[constants.priority](././os/~/constants.priority "constants.priority")

No documentation available

v

[constants.priority.PRIORITY\_ABOVE\_NORMAL](././os/~/constants.priority.PRIORITY_ABOVE_NORMAL "constants.priority.PRIORITY_ABOVE_NORMAL")

No documentation available

v

[constants.priority.PRIORITY\_BELOW\_NORMAL](././os/~/constants.priority.PRIORITY_BELOW_NORMAL "constants.priority.PRIORITY_BELOW_NORMAL")

No documentation available

v

[constants.priority.PRIORITY\_HIGH](././os/~/constants.priority.PRIORITY_HIGH "constants.priority.PRIORITY_HIGH")

No documentation available

v

[constants.priority.PRIORITY\_HIGHEST](././os/~/constants.priority.PRIORITY_HIGHEST "constants.priority.PRIORITY_HIGHEST")

No documentation available

v

[constants.priority.PRIORITY\_LOW](././os/~/constants.priority.PRIORITY_LOW "constants.priority.PRIORITY_LOW")

No documentation available

v

[constants.priority.PRIORITY\_NORMAL](././os/~/constants.priority.PRIORITY_NORMAL "constants.priority.PRIORITY_NORMAL")

No documentation available

N

v

[constants.signals](././os/~/constants.signals "constants.signals")

No documentation available

v

[constants.UV\_UDP\_REUSEADDR](././os/~/constants.UV_UDP_REUSEADDR "constants.UV_UDP_REUSEADDR")

No documentation available

I

[CpuInfo](././os/~/CpuInfo "CpuInfo")

The `node:os` module provides operating system-related utility methods and properties. It can be accessed using:

-   [model](././os/~/CpuInfo#property_model)
-   [speed](././os/~/CpuInfo#property_speed)
-   [times](././os/~/CpuInfo#property_times)

f

[cpus](././os/~/cpus "cpus")

Returns an array of objects containing information about each logical CPU core. The array will be empty if no CPU information is available, such as if the `/proc` file system is unavailable.

v

[devNull](././os/~/devNull "devNull")

No documentation available

f

[endianness](././os/~/endianness "endianness")

Returns a string identifying the endianness of the CPU for which the Node.js binary was compiled.

v

[EOL](././os/~/EOL "EOL")

The operating system-specific end-of-line marker.

f

[freemem](././os/~/freemem "freemem")

Returns the amount of free system memory in bytes as an integer.

f

[getPriority](././os/~/getPriority "getPriority")

Returns the scheduling priority for the process specified by `pid`. If `pid` is not provided or is `0`, the priority of the current process is returned.

f

[homedir](././os/~/homedir "homedir")

Returns the string path of the current user's home directory.

f

[hostname](././os/~/hostname "hostname")

Returns the host name of the operating system as a string.

f

[loadavg](././os/~/loadavg "loadavg")

Returns an array containing the 1, 5, and 15 minute load averages.

f

[machine](././os/~/machine "machine")

Returns the machine type as a string, such as `arm`, `arm64`, `aarch64`, `mips`, `mips64`, `ppc64`, `ppc64le`, `s390`, `s390x`, `i386`, `i686`, `x86_64`.

I

[NetworkInterfaceBase](././os/~/NetworkInterfaceBase "NetworkInterfaceBase")

No documentation available

-   [address](././os/~/NetworkInterfaceBase#property_address)
-   [cidr](././os/~/NetworkInterfaceBase#property_cidr)
-   [internal](././os/~/NetworkInterfaceBase#property_internal)
-   [mac](././os/~/NetworkInterfaceBase#property_mac)
-   [netmask](././os/~/NetworkInterfaceBase#property_netmask)

T

[NetworkInterfaceInfo](././os/~/NetworkInterfaceInfo "NetworkInterfaceInfo")

No documentation available

I

[NetworkInterfaceInfoIPv4](././os/~/NetworkInterfaceInfoIPv4 "NetworkInterfaceInfoIPv4")

No documentation available

-   [family](././os/~/NetworkInterfaceInfoIPv4#property_family)
-   [scopeid](././os/~/NetworkInterfaceInfoIPv4#property_scopeid)

I

[NetworkInterfaceInfoIPv6](././os/~/NetworkInterfaceInfoIPv6 "NetworkInterfaceInfoIPv6")

No documentation available

-   [family](././os/~/NetworkInterfaceInfoIPv6#property_family)
-   [scopeid](././os/~/NetworkInterfaceInfoIPv6#property_scopeid)

f

[networkInterfaces](././os/~/networkInterfaces "networkInterfaces")

Returns an object containing network interfaces that have been assigned a network address.

f

[platform](././os/~/platform "platform")

Returns a string identifying the operating system platform for which the Node.js binary was compiled. The value is set at compile time. Possible values are `'aix'`, `'darwin'`, `'freebsd'`, `'linux'`, `'openbsd'`, `'sunos'`, and `'win32'`.

f

[release](././os/~/release "release")

Returns the operating system as a string.

f

[setPriority](././os/~/setPriority "setPriority")

Attempts to set the scheduling priority for the process specified by `pid`. If `pid` is not provided or is `0`, the process ID of the current process is used.

T

[SignalConstants](././os/~/SignalConstants "SignalConstants")

No documentation available

f

[tmpdir](././os/~/tmpdir "tmpdir")

Returns the operating system's default directory for temporary files as a string.

f

[totalmem](././os/~/totalmem "totalmem")

Returns the total amount of system memory in bytes as an integer.

f

[type](././os/~/type "type")

Returns the operating system name as returned by [`uname(3)`](https://linux.die.net/man/3/uname). For example, it returns `'Linux'` on Linux, `'Darwin'` on macOS, and `'Windows_NT'` on Windows.

f

[uptime](././os/~/uptime "uptime")

Returns the system uptime in number of seconds.

I

[UserInfo](././os/~/UserInfo "UserInfo")

No documentation available

-   [gid](././os/~/UserInfo#property_gid)
-   [homedir](././os/~/UserInfo#property_homedir)
-   [shell](././os/~/UserInfo#property_shell)
-   [uid](././os/~/UserInfo#property_uid)
-   [username](././os/~/UserInfo#property_username)

f

[userInfo](././os/~/userInfo "userInfo")

Returns information about the currently effective user. On POSIX platforms, this is typically a subset of the password file. The returned object includes the `username`, `uid`, `gid`, `shell`, and `homedir`. On Windows, the `uid` and `gid` fields are `-1`, and `shell` is `null`.

f

[version](././os/~/version "version")

Returns a string identifying the kernel version.

The `node:path` module provides utilities for working with file and directory paths. It can be accessed using:

N

v

[default](././path/~/default "default")

The `node:path` module provides utilities for working with file and directory paths. It can be accessed using:

I

[default.FormatInputPathObject](././path/~/default.FormatInputPathObject "default.FormatInputPathObject")

No documentation available

-   [base](././path/~/default.FormatInputPathObject#property_base)
-   [dir](././path/~/default.FormatInputPathObject#property_dir)
-   [ext](././path/~/default.FormatInputPathObject#property_ext)
-   [name](././path/~/default.FormatInputPathObject#property_name)
-   [root](././path/~/default.FormatInputPathObject#property_root)

I

[default.ParsedPath](././path/~/default.ParsedPath "default.ParsedPath")

A parsed path object generated by path.parse() or consumed by path.format().

-   [base](././path/~/default.ParsedPath#property_base)
-   [dir](././path/~/default.ParsedPath#property_dir)
-   [ext](././path/~/default.ParsedPath#property_ext)
-   [name](././path/~/default.ParsedPath#property_name)
-   [root](././path/~/default.ParsedPath#property_root)

I

[default.PlatformPath](././path/~/default.PlatformPath "default.PlatformPath")

No documentation available

-   [basename](././path/~/default.PlatformPath#method_basename_0)
-   [delimiter](././path/~/default.PlatformPath#property_delimiter)
-   [dirname](././path/~/default.PlatformPath#method_dirname_0)
-   [extname](././path/~/default.PlatformPath#method_extname_0)
-   [format](././path/~/default.PlatformPath#method_format_0)
-   [isAbsolute](././path/~/default.PlatformPath#method_isabsolute_0)
-   [join](././path/~/default.PlatformPath#method_join_0)
-   [matchesGlob](././path/~/default.PlatformPath#method_matchesglob_0)
-   [normalize](././path/~/default.PlatformPath#method_normalize_0)
-   [parse](././path/~/default.PlatformPath#method_parse_0)
-   [posix](././path/~/default.PlatformPath#property_posix)
-   [relative](././path/~/default.PlatformPath#method_relative_0)
-   [resolve](././path/~/default.PlatformPath#method_resolve_0)
-   [sep](././path/~/default.PlatformPath#property_sep)
-   [toNamespacedPath](././path/~/default.PlatformPath#method_tonamespacedpath_0)
-   [win32](././path/~/default.PlatformPath#property_win32)

N

v

[path](././path/~/path "path")

The `node:path` module provides utilities for working with file and directory paths. It can be accessed using:

I

[path.FormatInputPathObject](././path/~/path.FormatInputPathObject "path.FormatInputPathObject")

No documentation available

-   [base](././path/~/path.FormatInputPathObject#property_base)
-   [dir](././path/~/path.FormatInputPathObject#property_dir)
-   [ext](././path/~/path.FormatInputPathObject#property_ext)
-   [name](././path/~/path.FormatInputPathObject#property_name)
-   [root](././path/~/path.FormatInputPathObject#property_root)

I

[path.ParsedPath](././path/~/path.ParsedPath "path.ParsedPath")

A parsed path object generated by path.parse() or consumed by path.format().

-   [base](././path/~/path.ParsedPath#property_base)
-   [dir](././path/~/path.ParsedPath#property_dir)
-   [ext](././path/~/path.ParsedPath#property_ext)
-   [name](././path/~/path.ParsedPath#property_name)
-   [root](././path/~/path.ParsedPath#property_root)

I

[path.PlatformPath](././path/~/path.PlatformPath "path.PlatformPath")

No documentation available

-   [basename](././path/~/path.PlatformPath#method_basename_0)
-   [delimiter](././path/~/path.PlatformPath#property_delimiter)
-   [dirname](././path/~/path.PlatformPath#method_dirname_0)
-   [extname](././path/~/path.PlatformPath#method_extname_0)
-   [format](././path/~/path.PlatformPath#method_format_0)
-   [isAbsolute](././path/~/path.PlatformPath#method_isabsolute_0)
-   [join](././path/~/path.PlatformPath#method_join_0)
-   [matchesGlob](././path/~/path.PlatformPath#method_matchesglob_0)
-   [normalize](././path/~/path.PlatformPath#method_normalize_0)
-   [parse](././path/~/path.PlatformPath#method_parse_0)
-   [posix](././path/~/path.PlatformPath#property_posix)
-   [relative](././path/~/path.PlatformPath#method_relative_0)
-   [resolve](././path/~/path.PlatformPath#method_resolve_0)
-   [sep](././path/~/path.PlatformPath#property_sep)
-   [toNamespacedPath](././path/~/path.PlatformPath#method_tonamespacedpath_0)
-   [win32](././path/~/path.PlatformPath#property_win32)

This module provides an implementation of a subset of the W3C [Web Performance APIs](https://w3c.github.io/perf-timing-primer/) as well as additional APIs for Node.js-specific performance measurements.

N

[constants](././perf_hooks/~/constants "constants")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_ALL\_AVAILABLE\_GARBAGE](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_ALL_AVAILABLE_GARBAGE "constants.NODE_PERFORMANCE_GC_FLAGS_ALL_AVAILABLE_GARBAGE")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_ALL\_EXTERNAL\_MEMORY](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_ALL_EXTERNAL_MEMORY "constants.NODE_PERFORMANCE_GC_FLAGS_ALL_EXTERNAL_MEMORY")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_CONSTRUCT\_RETAINED](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_CONSTRUCT_RETAINED "constants.NODE_PERFORMANCE_GC_FLAGS_CONSTRUCT_RETAINED")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_FORCED](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_FORCED "constants.NODE_PERFORMANCE_GC_FLAGS_FORCED")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_NO](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_NO "constants.NODE_PERFORMANCE_GC_FLAGS_NO")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_SCHEDULE\_IDLE](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_SCHEDULE_IDLE "constants.NODE_PERFORMANCE_GC_FLAGS_SCHEDULE_IDLE")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_FLAGS\_SYNCHRONOUS\_PHANTOM\_PROCESSING](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_FLAGS_SYNCHRONOUS_PHANTOM_PROCESSING "constants.NODE_PERFORMANCE_GC_FLAGS_SYNCHRONOUS_PHANTOM_PROCESSING")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_INCREMENTAL](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_INCREMENTAL "constants.NODE_PERFORMANCE_GC_INCREMENTAL")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_MAJOR](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_MAJOR "constants.NODE_PERFORMANCE_GC_MAJOR")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_MINOR](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_MINOR "constants.NODE_PERFORMANCE_GC_MINOR")

No documentation available

v

[constants.NODE\_PERFORMANCE\_GC\_WEAKCB](././perf_hooks/~/constants.NODE_PERFORMANCE_GC_WEAKCB "constants.NODE_PERFORMANCE_GC_WEAKCB")

No documentation available

f

[createHistogram](././perf_hooks/~/createHistogram "createHistogram")

Returns a `RecordableHistogram`.

I

[CreateHistogramOptions](././perf_hooks/~/CreateHistogramOptions "CreateHistogramOptions")

No documentation available

-   [figures](././perf_hooks/~/CreateHistogramOptions#property_figures)
-   [max](././perf_hooks/~/CreateHistogramOptions#property_max)
-   [min](././perf_hooks/~/CreateHistogramOptions#property_min)

T

[EntryType](././perf_hooks/~/EntryType "EntryType")

No documentation available

I

[EventLoopMonitorOptions](././perf_hooks/~/EventLoopMonitorOptions "EventLoopMonitorOptions")

No documentation available

-   [resolution](././perf_hooks/~/EventLoopMonitorOptions#property_resolution)

T

[EventLoopUtilityFunction](././perf_hooks/~/EventLoopUtilityFunction "EventLoopUtilityFunction")

No documentation available

I

[EventLoopUtilization](././perf_hooks/~/EventLoopUtilization "EventLoopUtilization")

No documentation available

-   [active](././perf_hooks/~/EventLoopUtilization#property_active)
-   [idle](././perf_hooks/~/EventLoopUtilization#property_idle)
-   [utilization](././perf_hooks/~/EventLoopUtilization#property_utilization)

I

[Histogram](././perf_hooks/~/Histogram "Histogram")

No documentation available

-   [count](././perf_hooks/~/Histogram#property_count)
-   [countBigInt](././perf_hooks/~/Histogram#property_countbigint)
-   [exceeds](././perf_hooks/~/Histogram#property_exceeds)
-   [exceedsBigInt](././perf_hooks/~/Histogram#property_exceedsbigint)
-   [max](././perf_hooks/~/Histogram#property_max)
-   [maxBigInt](././perf_hooks/~/Histogram#property_maxbigint)
-   [mean](././perf_hooks/~/Histogram#property_mean)
-   [min](././perf_hooks/~/Histogram#property_min)
-   [minBigInt](././perf_hooks/~/Histogram#property_minbigint)
-   [percentile](././perf_hooks/~/Histogram#method_percentile_0)
-   [percentileBigInt](././perf_hooks/~/Histogram#method_percentilebigint_0)
-   [percentiles](././perf_hooks/~/Histogram#property_percentiles)
-   [percentilesBigInt](././perf_hooks/~/Histogram#property_percentilesbigint)
-   [reset](././perf_hooks/~/Histogram#method_reset_0)
-   [stddev](././perf_hooks/~/Histogram#property_stddev)

I

[IntervalHistogram](././perf_hooks/~/IntervalHistogram "IntervalHistogram")

No documentation available

-   [disable](././perf_hooks/~/IntervalHistogram#method_disable_0)
-   [enable](././perf_hooks/~/IntervalHistogram#method_enable_0)

I

[MarkOptions](././perf_hooks/~/MarkOptions "MarkOptions")

No documentation available

-   [detail](././perf_hooks/~/MarkOptions#property_detail)
-   [startTime](././perf_hooks/~/MarkOptions#property_starttime)

I

[MeasureOptions](././perf_hooks/~/MeasureOptions "MeasureOptions")

No documentation available

-   [detail](././perf_hooks/~/MeasureOptions#property_detail)
-   [duration](././perf_hooks/~/MeasureOptions#property_duration)
-   [end](././perf_hooks/~/MeasureOptions#property_end)
-   [start](././perf_hooks/~/MeasureOptions#property_start)

f

[monitorEventLoopDelay](././perf_hooks/~/monitorEventLoopDelay "monitorEventLoopDelay")

No documentation available

I

[NodeGCPerformanceDetail](././perf_hooks/~/NodeGCPerformanceDetail "NodeGCPerformanceDetail")

No documentation available

-   [flags](././perf_hooks/~/NodeGCPerformanceDetail#property_flags)
-   [kind](././perf_hooks/~/NodeGCPerformanceDetail#property_kind)

I

[Performance](././perf_hooks/~/Performance "Performance")

No documentation available

-   [clearMarks](././perf_hooks/~/Performance#method_clearmarks_0)
-   [clearMeasures](././perf_hooks/~/Performance#method_clearmeasures_0)
-   [clearResourceTimings](././perf_hooks/~/Performance#method_clearresourcetimings_0)
-   [eventLoopUtilization](././perf_hooks/~/Performance#property_eventlooputilization)
-   [getEntries](././perf_hooks/~/Performance#method_getentries_0)
-   [getEntriesByName](././perf_hooks/~/Performance#method_getentriesbyname_0)
-   [getEntriesByType](././perf_hooks/~/Performance#method_getentriesbytype_0)
-   [mark](././perf_hooks/~/Performance#method_mark_0)
-   [markResourceTiming](././perf_hooks/~/Performance#method_markresourcetiming_0)
-   [measure](././perf_hooks/~/Performance#method_measure_0)
-   [nodeTiming](././perf_hooks/~/Performance#property_nodetiming)
-   [now](././perf_hooks/~/Performance#method_now_0)
-   [setResourceTimingBufferSize](././perf_hooks/~/Performance#method_setresourcetimingbuffersize_0)
-   [timeOrigin](././perf_hooks/~/Performance#property_timeorigin)
-   [timerify](././perf_hooks/~/Performance#method_timerify_0)
-   [toJSON](././perf_hooks/~/Performance#method_tojson_0)

v

[performance](././perf_hooks/~/performance "performance")

No documentation available

c

v

[PerformanceEntry](././perf_hooks/~/PerformanceEntry "PerformanceEntry")

The constructor of this class is not exposed to users directly.

-   [detail](././perf_hooks/~/PerformanceEntry#property_detail)
-   [duration](././perf_hooks/~/PerformanceEntry#property_duration)
-   [entryType](././perf_hooks/~/PerformanceEntry#property_entrytype)
-   [name](././perf_hooks/~/PerformanceEntry#property_name)
-   [startTime](././perf_hooks/~/PerformanceEntry#property_starttime)
-   [toJSON](././perf_hooks/~/PerformanceEntry#method_tojson_0)

c

v

[PerformanceMark](././perf_hooks/~/PerformanceMark "PerformanceMark")

Exposes marks created via the `Performance.mark()` method.

-   [duration](././perf_hooks/~/PerformanceMark#property_duration)
-   [entryType](././perf_hooks/~/PerformanceMark#property_entrytype)

c

v

[PerformanceMeasure](././perf_hooks/~/PerformanceMeasure "PerformanceMeasure")

Exposes measures created via the `Performance.measure()` method.

-   [entryType](././perf_hooks/~/PerformanceMeasure#property_entrytype)

c

[PerformanceNodeTiming](././perf_hooks/~/PerformanceNodeTiming "PerformanceNodeTiming")

_This property is an extension by Node.js. It is not available in Web browsers._

-   [bootstrapComplete](././perf_hooks/~/PerformanceNodeTiming#property_bootstrapcomplete)
-   [entryType](././perf_hooks/~/PerformanceNodeTiming#property_entrytype)
-   [environment](././perf_hooks/~/PerformanceNodeTiming#property_environment)
-   [idleTime](././perf_hooks/~/PerformanceNodeTiming#property_idletime)
-   [loopExit](././perf_hooks/~/PerformanceNodeTiming#property_loopexit)
-   [loopStart](././perf_hooks/~/PerformanceNodeTiming#property_loopstart)
-   [nodeStart](././perf_hooks/~/PerformanceNodeTiming#property_nodestart)
-   [uvMetricsInfo](././perf_hooks/~/PerformanceNodeTiming#property_uvmetricsinfo)
-   [v8Start](././perf_hooks/~/PerformanceNodeTiming#property_v8start)

c

v

[PerformanceObserver](././perf_hooks/~/PerformanceObserver "PerformanceObserver")

No documentation available

-   [disconnect](././perf_hooks/~/PerformanceObserver#method_disconnect_0)
-   [observe](././perf_hooks/~/PerformanceObserver#method_observe_0)
-   [takeRecords](././perf_hooks/~/PerformanceObserver#method_takerecords_0)

T

[PerformanceObserverCallback](././perf_hooks/~/PerformanceObserverCallback "PerformanceObserverCallback")

No documentation available

c

v

[PerformanceObserverEntryList](././perf_hooks/~/PerformanceObserverEntryList "PerformanceObserverEntryList")

No documentation available

-   [getEntries](././perf_hooks/~/PerformanceObserverEntryList#method_getentries_0)
-   [getEntriesByName](././perf_hooks/~/PerformanceObserverEntryList#method_getentriesbyname_0)
-   [getEntriesByType](././perf_hooks/~/PerformanceObserverEntryList#method_getentriesbytype_0)

c

v

[PerformanceResourceTiming](././perf_hooks/~/PerformanceResourceTiming "PerformanceResourceTiming")

Provides detailed network timing data regarding the loading of an application's resources.

-   [connectEnd](././perf_hooks/~/PerformanceResourceTiming#property_connectend)
-   [connectStart](././perf_hooks/~/PerformanceResourceTiming#property_connectstart)
-   [decodedBodySize](././perf_hooks/~/PerformanceResourceTiming#property_decodedbodysize)
-   [domainLookupEnd](././perf_hooks/~/PerformanceResourceTiming#property_domainlookupend)
-   [domainLookupStart](././perf_hooks/~/PerformanceResourceTiming#property_domainlookupstart)
-   [encodedBodySize](././perf_hooks/~/PerformanceResourceTiming#property_encodedbodysize)
-   [entryType](././perf_hooks/~/PerformanceResourceTiming#property_entrytype)
-   [fetchStart](././perf_hooks/~/PerformanceResourceTiming#property_fetchstart)
-   [redirectEnd](././perf_hooks/~/PerformanceResourceTiming#property_redirectend)
-   [redirectStart](././perf_hooks/~/PerformanceResourceTiming#property_redirectstart)
-   [requestStart](././perf_hooks/~/PerformanceResourceTiming#property_requeststart)
-   [responseEnd](././perf_hooks/~/PerformanceResourceTiming#property_responseend)
-   [secureConnectionStart](././perf_hooks/~/PerformanceResourceTiming#property_secureconnectionstart)
-   [toJSON](././perf_hooks/~/PerformanceResourceTiming#method_tojson_0)
-   [transferSize](././perf_hooks/~/PerformanceResourceTiming#property_transfersize)
-   [workerStart](././perf_hooks/~/PerformanceResourceTiming#property_workerstart)

I

[RecordableHistogram](././perf_hooks/~/RecordableHistogram "RecordableHistogram")

No documentation available

-   [add](././perf_hooks/~/RecordableHistogram#method_add_0)
-   [record](././perf_hooks/~/RecordableHistogram#method_record_0)
-   [recordDelta](././perf_hooks/~/RecordableHistogram#method_recorddelta_0)

I

[TimerifyOptions](././perf_hooks/~/TimerifyOptions "TimerifyOptions")

No documentation available

-   [histogram](././perf_hooks/~/TimerifyOptions#property_histogram)

I

[UVMetrics](././perf_hooks/~/UVMetrics "UVMetrics")

No documentation available

-   [events](././perf_hooks/~/UVMetrics#property_events)
-   [eventsWaiting](././perf_hooks/~/UVMetrics#property_eventswaiting)
-   [loopCount](././perf_hooks/~/UVMetrics#property_loopcount)

T

[Architecture](././process/~/Architecture "Architecture")

No documentation available

T

[BeforeExitListener](././process/~/BeforeExitListener "BeforeExitListener")

No documentation available

I

[CpuUsage](././process/~/CpuUsage "CpuUsage")

No documentation available

-   [system](././process/~/CpuUsage#property_system)
-   [user](././process/~/CpuUsage#property_user)

T

[DisconnectListener](././process/~/DisconnectListener "DisconnectListener")

No documentation available

I

[EmitWarningOptions](././process/~/EmitWarningOptions "EmitWarningOptions")

No documentation available

-   [code](././process/~/EmitWarningOptions#property_code)
-   [ctor](././process/~/EmitWarningOptions#property_ctor)
-   [detail](././process/~/EmitWarningOptions#property_detail)
-   [type](././process/~/EmitWarningOptions#property_type)

T

[ExitListener](././process/~/ExitListener "ExitListener")

No documentation available

I

[HRTime](././process/~/HRTime "HRTime")

No documentation available

-   [bigint](././process/~/HRTime#method_bigint_0)

I

[MemoryUsage](././process/~/MemoryUsage "MemoryUsage")

No documentation available

-   [arrayBuffers](././process/~/MemoryUsage#property_arraybuffers)
-   [external](././process/~/MemoryUsage#property_external)
-   [heapTotal](././process/~/MemoryUsage#property_heaptotal)
-   [heapUsed](././process/~/MemoryUsage#property_heapused)
-   [rss](././process/~/MemoryUsage#property_rss)

I

[MemoryUsageFn](././process/~/MemoryUsageFn "MemoryUsageFn")

No documentation available

-   [rss](././process/~/MemoryUsageFn#method_rss_0)

T

[MessageListener](././process/~/MessageListener "MessageListener")

No documentation available

T

[MultipleResolveListener](././process/~/MultipleResolveListener "MultipleResolveListener")

No documentation available

T

[MultipleResolveType](././process/~/MultipleResolveType "MultipleResolveType")

No documentation available

T

[Platform](././process/~/Platform "Platform")

No documentation available

I

[Process](././process/~/Process "Process")

No documentation available

-   [abort](././process/~/Process#method_abort_0)
-   [addListener](././process/~/Process#method_addlistener_0)
-   [allowedNodeEnvironmentFlags](././process/~/Process#property_allowednodeenvironmentflags)
-   [arch](././process/~/Process#property_arch)
-   [argv](././process/~/Process#property_argv)
-   [argv0](././process/~/Process#property_argv0)
-   [availableMemory](././process/~/Process#method_availablememory_0)
-   [channel](././process/~/Process#property_channel)
-   [chdir](././process/~/Process#method_chdir_0)
-   [config](././process/~/Process#property_config)
-   [connected](././process/~/Process#property_connected)
-   [constrainedMemory](././process/~/Process#method_constrainedmemory_0)
-   [cpuUsage](././process/~/Process#method_cpuusage_0)
-   [cwd](././process/~/Process#method_cwd_0)
-   [debugPort](././process/~/Process#property_debugport)
-   [disconnect](././process/~/Process#method_disconnect_0)
-   [dlopen](././process/~/Process#method_dlopen_0)
-   [emit](././process/~/Process#method_emit_0)
-   [emitWarning](././process/~/Process#method_emitwarning_0)
-   [env](././process/~/Process#property_env)
-   [execArgv](././process/~/Process#property_execargv)
-   [execPath](././process/~/Process#property_execpath)
-   [exit](././process/~/Process#method_exit_0)
-   [exitCode](././process/~/Process#property_exitcode)
-   [features](././process/~/Process#property_features)
-   [finalization](././process/~/Process#property_finalization)
-   [getActiveResourcesInfo](././process/~/Process#method_getactiveresourcesinfo_0)
-   [getBuiltinModule](././process/~/Process#method_getbuiltinmodule_0)
-   [getegid](././process/~/Process#property_getegid)
-   [geteuid](././process/~/Process#property_geteuid)
-   [getgid](././process/~/Process#property_getgid)
-   [getgroups](././process/~/Process#property_getgroups)
-   [getuid](././process/~/Process#property_getuid)
-   [hasUncaughtExceptionCaptureCallback](././process/~/Process#method_hasuncaughtexceptioncapturecallback_0)
-   [hrtime](././process/~/Process#property_hrtime)
-   [kill](././process/~/Process#method_kill_0)
-   [listeners](././process/~/Process#method_listeners_0)
-   [loadEnvFile](././process/~/Process#method_loadenvfile_0)
-   [mainModule](././process/~/Process#property_mainmodule)
-   [memoryUsage](././process/~/Process#property_memoryusage)
-   [nextTick](././process/~/Process#method_nexttick_0)
-   [on](././process/~/Process#method_on_0)
-   [once](././process/~/Process#method_once_0)
-   [permission](././process/~/Process#property_permission)
-   [pid](././process/~/Process#property_pid)
-   [platform](././process/~/Process#property_platform)
-   [ppid](././process/~/Process#property_ppid)
-   [prependListener](././process/~/Process#method_prependlistener_0)
-   [prependOnceListener](././process/~/Process#method_prependoncelistener_0)
-   [ref](././process/~/Process#method_ref_0)
-   [release](././process/~/Process#property_release)
-   [report](././process/~/Process#property_report)
-   [resourceUsage](././process/~/Process#method_resourceusage_0)
-   [send](././process/~/Process#method_send_0)
-   [setSourceMapsEnabled](././process/~/Process#method_setsourcemapsenabled_0)
-   [setUncaughtExceptionCaptureCallback](././process/~/Process#method_setuncaughtexceptioncapturecallback_0)
-   [setegid](././process/~/Process#property_setegid)
-   [seteuid](././process/~/Process#property_seteuid)
-   [setgid](././process/~/Process#property_setgid)
-   [setgroups](././process/~/Process#property_setgroups)
-   [setuid](././process/~/Process#property_setuid)
-   [sourceMapsEnabled](././process/~/Process#property_sourcemapsenabled)
-   [stderr](././process/~/Process#property_stderr)
-   [stdin](././process/~/Process#property_stdin)
-   [stdout](././process/~/Process#property_stdout)
-   [throwDeprecation](././process/~/Process#property_throwdeprecation)
-   [title](././process/~/Process#property_title)
-   [traceDeprecation](././process/~/Process#property_tracedeprecation)
-   [umask](././process/~/Process#method_umask_0)
-   [unref](././process/~/Process#method_unref_0)
-   [uptime](././process/~/Process#method_uptime_0)
-   [version](././process/~/Process#property_version)
-   [versions](././process/~/Process#property_versions)

v

[process](././process/~/process "process")

No documentation available

I

[ProcessConfig](././process/~/ProcessConfig "ProcessConfig")

No documentation available

-   [target\_defaults](././process/~/ProcessConfig#property_target_defaults)
-   [variables](././process/~/ProcessConfig#property_variables)

I

[ProcessEnv](././process/~/ProcessEnv "ProcessEnv")

No documentation available

-   [TZ](././process/~/ProcessEnv#property_tz)

I

[ProcessFeatures](././process/~/ProcessFeatures "ProcessFeatures")

No documentation available

-   [cached\_builtins](././process/~/ProcessFeatures#property_cached_builtins)
-   [debug](././process/~/ProcessFeatures#property_debug)
-   [inspector](././process/~/ProcessFeatures#property_inspector)
-   [ipv6](././process/~/ProcessFeatures#property_ipv6)
-   [require\_module](././process/~/ProcessFeatures#property_require_module)
-   [tls](././process/~/ProcessFeatures#property_tls)
-   [tls\_alpn](././process/~/ProcessFeatures#property_tls_alpn)
-   [tls\_ocsp](././process/~/ProcessFeatures#property_tls_ocsp)
-   [tls\_sni](././process/~/ProcessFeatures#property_tls_sni)
-   [typescript](././process/~/ProcessFeatures#property_typescript)
-   [uv](././process/~/ProcessFeatures#property_uv)

I

[ProcessPermission](././process/~/ProcessPermission "ProcessPermission")

No documentation available

-   [has](././process/~/ProcessPermission#method_has_0)

I

[ProcessRelease](././process/~/ProcessRelease "ProcessRelease")

No documentation available

-   [headersUrl](././process/~/ProcessRelease#property_headersurl)
-   [libUrl](././process/~/ProcessRelease#property_liburl)
-   [lts](././process/~/ProcessRelease#property_lts)
-   [name](././process/~/ProcessRelease#property_name)
-   [sourceUrl](././process/~/ProcessRelease#property_sourceurl)

I

[ProcessReport](././process/~/ProcessReport "ProcessReport")

No documentation available

-   [compact](././process/~/ProcessReport#property_compact)
-   [directory](././process/~/ProcessReport#property_directory)
-   [filename](././process/~/ProcessReport#property_filename)
-   [getReport](././process/~/ProcessReport#method_getreport_0)
-   [reportOnFatalError](././process/~/ProcessReport#property_reportonfatalerror)
-   [reportOnSignal](././process/~/ProcessReport#property_reportonsignal)
-   [reportOnUncaughtException](././process/~/ProcessReport#property_reportonuncaughtexception)
-   [signal](././process/~/ProcessReport#property_signal)
-   [writeReport](././process/~/ProcessReport#method_writereport_0)

I

[ProcessVersions](././process/~/ProcessVersions "ProcessVersions")

No documentation available

-   [ares](././process/~/ProcessVersions#property_ares)
-   [http\_parser](././process/~/ProcessVersions#property_http_parser)
-   [modules](././process/~/ProcessVersions#property_modules)
-   [node](././process/~/ProcessVersions#property_node)
-   [openssl](././process/~/ProcessVersions#property_openssl)
-   [uv](././process/~/ProcessVersions#property_uv)
-   [v8](././process/~/ProcessVersions#property_v8)
-   [zlib](././process/~/ProcessVersions#property_zlib)

I

[ReadStream](././process/~/ReadStream "ReadStream")

No documentation available

T

[RejectionHandledListener](././process/~/RejectionHandledListener "RejectionHandledListener")

No documentation available

I

[ResourceUsage](././process/~/ResourceUsage "ResourceUsage")

No documentation available

-   [fsRead](././process/~/ResourceUsage#property_fsread)
-   [fsWrite](././process/~/ResourceUsage#property_fswrite)
-   [involuntaryContextSwitches](././process/~/ResourceUsage#property_involuntarycontextswitches)
-   [ipcReceived](././process/~/ResourceUsage#property_ipcreceived)
-   [ipcSent](././process/~/ResourceUsage#property_ipcsent)
-   [majorPageFault](././process/~/ResourceUsage#property_majorpagefault)
-   [maxRSS](././process/~/ResourceUsage#property_maxrss)
-   [minorPageFault](././process/~/ResourceUsage#property_minorpagefault)
-   [sharedMemorySize](././process/~/ResourceUsage#property_sharedmemorysize)
-   [signalsCount](././process/~/ResourceUsage#property_signalscount)
-   [swappedOut](././process/~/ResourceUsage#property_swappedout)
-   [systemCPUTime](././process/~/ResourceUsage#property_systemcputime)
-   [unsharedDataSize](././process/~/ResourceUsage#property_unshareddatasize)
-   [unsharedStackSize](././process/~/ResourceUsage#property_unsharedstacksize)
-   [userCPUTime](././process/~/ResourceUsage#property_usercputime)
-   [voluntaryContextSwitches](././process/~/ResourceUsage#property_voluntarycontextswitches)

T

[Signals](././process/~/Signals "Signals")

No documentation available

T

[SignalsListener](././process/~/SignalsListener "SignalsListener")

No documentation available

I

[Socket](././process/~/Socket "Socket")

No documentation available

-   [isTTY](././process/~/Socket#property_istty)

T

[UncaughtExceptionListener](././process/~/UncaughtExceptionListener "UncaughtExceptionListener")

No documentation available

T

[UncaughtExceptionOrigin](././process/~/UncaughtExceptionOrigin "UncaughtExceptionOrigin")

No documentation available

T

[UnhandledRejectionListener](././process/~/UnhandledRejectionListener "UnhandledRejectionListener")

Most of the time the unhandledRejection will be an Error, but this should not be relied upon as _anything_ can be thrown/rejected, it is therefore unsafe to assume that the value is an Error.

T

[WarningListener](././process/~/WarningListener "WarningListener")

No documentation available

T

[WorkerListener](././process/~/WorkerListener "WorkerListener")

No documentation available

I

[WriteStream](././process/~/WriteStream "WriteStream")

No documentation available

\*\*The version of the punycode module bundled in Node.js is being deprecated. \*\*In a future major version of Node.js this module will be removed. Users currently depending on the `punycode` module should switch to using the userland-provided [Punycode.js](https://github.com/bestiejs/punycode.js) module instead. For punycode-based URL encoding, see `url.domainToASCII` or, more generally, the `WHATWG URL API`.

f

[decode](././punycode/~/decode "decode")

The `punycode.decode()` method converts a [Punycode](https://tools.ietf.org/html/rfc3492) string of ASCII-only characters to the equivalent string of Unicode codepoints.

f

[encode](././punycode/~/encode "encode")

The `punycode.encode()` method converts a string of Unicode codepoints to a [Punycode](https://tools.ietf.org/html/rfc3492) string of ASCII-only characters.

f

[toASCII](././punycode/~/toASCII "toASCII")

The `punycode.toASCII()` method converts a Unicode string representing an Internationalized Domain Name to [Punycode](https://tools.ietf.org/html/rfc3492). Only the non-ASCII parts of the domain name will be converted. Calling `punycode.toASCII()` on a string that already only contains ASCII characters will have no effect.

f

[toUnicode](././punycode/~/toUnicode "toUnicode")

The `punycode.toUnicode()` method converts a string representing a domain name containing [Punycode](https://tools.ietf.org/html/rfc3492) encoded characters into Unicode. Only the [Punycode](https://tools.ietf.org/html/rfc3492) encoded parts of the domain name are be converted.

I

v

[ucs2](././punycode/~/ucs2 "ucs2")

No documentation available

-   [decode](././punycode/~/ucs2#method_decode_0)
-   [encode](././punycode/~/ucs2#method_encode_0)

v

[version](././punycode/~/version "version")

No documentation available

The `node:querystring` module provides utilities for parsing and formatting URL query strings. It can be accessed using:

v

[decode](././querystring/~/decode "decode")

The querystring.decode() function is an alias for querystring.parse().

v

[encode](././querystring/~/encode "encode")

The querystring.encode() function is an alias for querystring.stringify().

f

[escape](././querystring/~/escape "escape")

The `querystring.escape()` method performs URL percent-encoding on the given `str` in a manner that is optimized for the specific requirements of URL query strings.

f

[parse](././querystring/~/parse "parse")

The `querystring.parse()` method parses a URL query string (`str`) into a collection of key and value pairs.

I

[ParsedUrlQuery](././querystring/~/ParsedUrlQuery "ParsedUrlQuery")

No documentation available

I

[ParsedUrlQueryInput](././querystring/~/ParsedUrlQueryInput "ParsedUrlQueryInput")

No documentation available

I

[ParseOptions](././querystring/~/ParseOptions "ParseOptions")

No documentation available

-   [decodeURIComponent](././querystring/~/ParseOptions#property_decodeuricomponent)
-   [maxKeys](././querystring/~/ParseOptions#property_maxkeys)

f

[stringify](././querystring/~/stringify "stringify")

The `querystring.stringify()` method produces a URL query string from a given `obj` by iterating through the object's "own properties".

I

[StringifyOptions](././querystring/~/StringifyOptions "StringifyOptions")

The `node:querystring` module provides utilities for parsing and formatting URL query strings. It can be accessed using:

-   [encodeURIComponent](././querystring/~/StringifyOptions#property_encodeuricomponent)

f

[unescape](././querystring/~/unescape "unescape")

The `querystring.unescape()` method performs decoding of URL percent-encoded characters on the given `str`.

The `node:readline` module provides an interface for reading data from a [Readable](https://nodejs.org/docs/latest-v22.x/api/stream.html#readable-streams) stream (such as [`process.stdin`](https://nodejs.org/docs/latest-v22.x/api/process.html#processstdin)) one line at a time.

T

[AsyncCompleter](././readline/~/AsyncCompleter "AsyncCompleter")

No documentation available

f

[clearLine](././readline/~/clearLine "clearLine")

The `readline.clearLine()` method clears current line of given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) stream in a specified direction identified by `dir`.

f

[clearScreenDown](././readline/~/clearScreenDown "clearScreenDown")

The `readline.clearScreenDown()` method clears the given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) stream from the current position of the cursor down.

T

[Completer](././readline/~/Completer "Completer")

No documentation available

T

[CompleterResult](././readline/~/CompleterResult "CompleterResult")

No documentation available

f

[createInterface](././readline/~/createInterface "createInterface")

The `readline.createInterface()` method creates a new `readline.Interface` instance.

I

[CursorPos](././readline/~/CursorPos "CursorPos")

No documentation available

-   [cols](././readline/~/CursorPos#property_cols)
-   [rows](././readline/~/CursorPos#property_rows)

f

[cursorTo](././readline/~/cursorTo "cursorTo")

The `readline.cursorTo()` method moves cursor to the specified position in a given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) `stream`.

T

[Direction](././readline/~/Direction "Direction")

No documentation available

f

[emitKeypressEvents](././readline/~/emitKeypressEvents "emitKeypressEvents")

The `readline.emitKeypressEvents()` method causes the given `Readable` stream to begin emitting `'keypress'` events corresponding to received input.

c

[Interface](././readline/~/Interface "Interface")

Instances of the `readline.Interface` class are constructed using the `readline.createInterface()` method. Every instance is associated with a single `input` [Readable](https://nodejs.org/docs/latest-v22.x/api/stream.html#readable-streams) stream and a single `output` [Writable](https://nodejs.org/docs/latest-v22.x/api/stream.html#writable-streams) stream. The `output` stream is used to print prompts for user input that arrives on, and is read from, the `input` stream.

-   [addListener](././readline/~/Interface#method_addlistener_0)
-   [close](././readline/~/Interface#method_close_0)
-   [cursor](././readline/~/Interface#property_cursor)
-   [emit](././readline/~/Interface#method_emit_0)
-   [getCursorPos](././readline/~/Interface#method_getcursorpos_0)
-   [getPrompt](././readline/~/Interface#method_getprompt_0)
-   [line](././readline/~/Interface#property_line)
-   [on](././readline/~/Interface#method_on_0)
-   [once](././readline/~/Interface#method_once_0)
-   [pause](././readline/~/Interface#method_pause_0)
-   [prependListener](././readline/~/Interface#method_prependlistener_0)
-   [prependOnceListener](././readline/~/Interface#method_prependoncelistener_0)
-   [prompt](././readline/~/Interface#method_prompt_0)
-   [question](././readline/~/Interface#method_question_0)
-   [resume](././readline/~/Interface#method_resume_0)
-   [setPrompt](././readline/~/Interface#method_setprompt_0)
-   [terminal](././readline/~/Interface#property_terminal)
-   [write](././readline/~/Interface#method_write_0)

I

[Key](././readline/~/Key "Key")

No documentation available

-   [ctrl](././readline/~/Key#property_ctrl)
-   [meta](././readline/~/Key#property_meta)
-   [name](././readline/~/Key#property_name)
-   [sequence](././readline/~/Key#property_sequence)
-   [shift](././readline/~/Key#property_shift)

f

[moveCursor](././readline/~/moveCursor "moveCursor")

The `readline.moveCursor()` method moves the cursor _relative_ to its current position in a given [TTY](https://nodejs.org/docs/latest-v22.x/api/tty.html) `stream`.

N

[promises](././readline/~/promises "promises")

No documentation available

T

[ReadLine](././readline/~/ReadLine "ReadLine")

No documentation available

I

[ReadLineOptions](././readline/~/ReadLineOptions "ReadLineOptions")

No documentation available

-   [completer](././readline/~/ReadLineOptions#property_completer)
-   [crlfDelay](././readline/~/ReadLineOptions#property_crlfdelay)
-   [escapeCodeTimeout](././readline/~/ReadLineOptions#property_escapecodetimeout)
-   [history](././readline/~/ReadLineOptions#property_history)
-   [historySize](././readline/~/ReadLineOptions#property_historysize)
-   [input](././readline/~/ReadLineOptions#property_input)
-   [output](././readline/~/ReadLineOptions#property_output)
-   [prompt](././readline/~/ReadLineOptions#property_prompt)
-   [removeHistoryDuplicates](././readline/~/ReadLineOptions#property_removehistoryduplicates)
-   [signal](././readline/~/ReadLineOptions#property_signal)
-   [tabSize](././readline/~/ReadLineOptions#property_tabsize)
-   [terminal](././readline/~/ReadLineOptions#property_terminal)

T

[Completer](././readline/promises/~/Completer "Completer")

No documentation available

f

[createInterface](././readline/promises/~/createInterface "createInterface")

The `readlinePromises.createInterface()` method creates a new `readlinePromises.Interface` instance.

c

[Interface](././readline/promises/~/Interface "Interface")

Instances of the `readlinePromises.Interface` class are constructed using the `readlinePromises.createInterface()` method. Every instance is associated with a single `input` `Readable` stream and a single `output` `Writable` stream. The `output` stream is used to print prompts for user input that arrives on, and is read from, the `input` stream.

-   [question](././readline/promises/~/Interface#method_question_0)

T

[promises.Completer](././readline/promises/~/promises.Completer "promises.Completer")

No documentation available

f

[promises.createInterface](././readline/promises/~/promises.createInterface "promises.createInterface")

The `readlinePromises.createInterface()` method creates a new `readlinePromises.Interface` instance.

c

[promises.Interface](././readline/promises/~/promises.Interface "promises.Interface")

Instances of the `readlinePromises.Interface` class are constructed using the `readlinePromises.createInterface()` method. Every instance is associated with a single `input` `Readable` stream and a single `output` `Writable` stream. The `output` stream is used to print prompts for user input that arrives on, and is read from, the `input` stream.

-   [question](././readline/promises/~/promises.Interface#method_question_0)

c

[promises.Readline](././readline/promises/~/promises.Readline "promises.Readline")

No documentation available

-   [clearLine](././readline/promises/~/promises.Readline#method_clearline_0)
-   [clearScreenDown](././readline/promises/~/promises.Readline#method_clearscreendown_0)
-   [commit](././readline/promises/~/promises.Readline#method_commit_0)
-   [cursorTo](././readline/promises/~/promises.Readline#method_cursorto_0)
-   [moveCursor](././readline/promises/~/promises.Readline#method_movecursor_0)
-   [rollback](././readline/promises/~/promises.Readline#method_rollback_0)

I

[promises.ReadLineOptions](././readline/promises/~/promises.ReadLineOptions "promises.ReadLineOptions")

No documentation available

-   [completer](././readline/promises/~/promises.ReadLineOptions#property_completer)

c

[Readline](././readline/promises/~/Readline "Readline")

No documentation available

-   [clearLine](././readline/promises/~/Readline#method_clearline_0)
-   [clearScreenDown](././readline/promises/~/Readline#method_clearscreendown_0)
-   [commit](././readline/promises/~/Readline#method_commit_0)
-   [cursorTo](././readline/promises/~/Readline#method_cursorto_0)
-   [moveCursor](././readline/promises/~/Readline#method_movecursor_0)
-   [rollback](././readline/promises/~/Readline#method_rollback_0)

I

[ReadLineOptions](././readline/promises/~/ReadLineOptions "ReadLineOptions")

No documentation available

-   [completer](././readline/promises/~/ReadLineOptions#property_completer)

c

[Recoverable](././repl/~/Recoverable "Recoverable")

No documentation available

-   [err](././repl/~/Recoverable#property_err)

v

[REPL\_MODE\_SLOPPY](././repl/~/REPL_MODE_SLOPPY "REPL_MODE_SLOPPY")

A flag passed in the REPL options. Evaluates expressions in sloppy mode.

v

[REPL\_MODE\_STRICT](././repl/~/REPL_MODE_STRICT "REPL_MODE_STRICT")

A flag passed in the REPL options. Evaluates expressions in strict mode. This is equivalent to prefacing every repl statement with `'use strict'`.

I

[REPLCommand](././repl/~/REPLCommand "REPLCommand")

No documentation available

-   [action](././repl/~/REPLCommand#property_action)
-   [help](././repl/~/REPLCommand#property_help)

T

[REPLCommandAction](././repl/~/REPLCommandAction "REPLCommandAction")

No documentation available

T

[REPLEval](././repl/~/REPLEval "REPLEval")

No documentation available

I

[ReplOptions](././repl/~/ReplOptions "ReplOptions")

No documentation available

-   [breakEvalOnSigint](././repl/~/ReplOptions#property_breakevalonsigint)
-   [completer](././repl/~/ReplOptions#property_completer)
-   [eval](././repl/~/ReplOptions#property_eval)
-   [ignoreUndefined](././repl/~/ReplOptions#property_ignoreundefined)
-   [input](././repl/~/ReplOptions#property_input)
-   [output](././repl/~/ReplOptions#property_output)
-   [preview](././repl/~/ReplOptions#property_preview)
-   [prompt](././repl/~/ReplOptions#property_prompt)
-   [replMode](././repl/~/ReplOptions#property_replmode)
-   [terminal](././repl/~/ReplOptions#property_terminal)
-   [useColors](././repl/~/ReplOptions#property_usecolors)
-   [useGlobal](././repl/~/ReplOptions#property_useglobal)
-   [writer](././repl/~/ReplOptions#property_writer)

c

[REPLServer](././repl/~/REPLServer "REPLServer")

No documentation available

-   [addListener](././repl/~/REPLServer#method_addlistener_0)
-   [clearBufferedCommand](././repl/~/REPLServer#method_clearbufferedcommand_0)
-   [commands](././repl/~/REPLServer#property_commands)
-   [completer](././repl/~/REPLServer#property_completer)
-   [context](././repl/~/REPLServer#property_context)
-   [defineCommand](././repl/~/REPLServer#method_definecommand_0)
-   [displayPrompt](././repl/~/REPLServer#method_displayprompt_0)
-   [editorMode](././repl/~/REPLServer#property_editormode)
-   [emit](././repl/~/REPLServer#method_emit_0)
-   [eval](././repl/~/REPLServer#property_eval)
-   [ignoreUndefined](././repl/~/REPLServer#property_ignoreundefined)
-   [input](././repl/~/REPLServer#property_input)
-   [inputStream](././repl/~/REPLServer#property_inputstream)
-   [last](././repl/~/REPLServer#property_last)
-   [lastError](././repl/~/REPLServer#property_lasterror)
-   [on](././repl/~/REPLServer#method_on_0)
-   [once](././repl/~/REPLServer#method_once_0)
-   [output](././repl/~/REPLServer#property_output)
-   [outputStream](././repl/~/REPLServer#property_outputstream)
-   [prependListener](././repl/~/REPLServer#method_prependlistener_0)
-   [prependOnceListener](././repl/~/REPLServer#method_prependoncelistener_0)
-   [replMode](././repl/~/REPLServer#property_replmode)
-   [setupHistory](././repl/~/REPLServer#method_setuphistory_0)
-   [underscoreAssigned](././repl/~/REPLServer#property_underscoreassigned)
-   [underscoreErrAssigned](././repl/~/REPLServer#property_underscoreerrassigned)
-   [useColors](././repl/~/REPLServer#property_usecolors)
-   [useGlobal](././repl/~/REPLServer#property_useglobal)
-   [writer](././repl/~/REPLServer#property_writer)

T

[REPLWriter](././repl/~/REPLWriter "REPLWriter")

No documentation available

f

[start](././repl/~/start "start")

No documentation available

v

[writer](././repl/~/writer "writer")

This is the default "writer" value, if none is passed in the REPL options, and it can be overridden by custom print functions.

T

[AssetKey](././sea/~/AssetKey "AssetKey")

No documentation available

f

[getAsset](././sea/~/getAsset "getAsset")

No documentation available

f

[getAssetAsBlob](././sea/~/getAssetAsBlob "getAssetAsBlob")

No documentation available

f

[getRawAsset](././sea/~/getRawAsset "getRawAsset")

No documentation available

f

[isSea](././sea/~/isSea "isSea")

No documentation available

I

[ApplyChangesetOptions](././sqlite/~/ApplyChangesetOptions "ApplyChangesetOptions")

No documentation available

-   [filter](././sqlite/~/ApplyChangesetOptions#property_filter)
-   [onConflict](././sqlite/~/ApplyChangesetOptions#property_onconflict)

N

[constants](././sqlite/~/constants "constants")

No documentation available

v

[constants.SQLITE\_CHANGESET\_ABORT](././sqlite/~/constants.SQLITE_CHANGESET_ABORT "constants.SQLITE_CHANGESET_ABORT")

Abort when a change encounters a conflict and roll back database.

v

[constants.SQLITE\_CHANGESET\_CONFLICT](././sqlite/~/constants.SQLITE_CHANGESET_CONFLICT "constants.SQLITE_CHANGESET_CONFLICT")

This constant is passed to the conflict handler while processing an INSERT change if the operation would result in duplicate primary key values.

v

[constants.SQLITE\_CHANGESET\_DATA](././sqlite/~/constants.SQLITE_CHANGESET_DATA "constants.SQLITE_CHANGESET_DATA")

The conflict handler is invoked with this constant when processing a DELETE or UPDATE change if a row with the required PRIMARY KEY fields is present in the database, but one or more other (non primary-key) fields modified by the update do not contain the expected "before" values.

v

[constants.SQLITE\_CHANGESET\_FOREIGN\_KEY](././sqlite/~/constants.SQLITE_CHANGESET_FOREIGN_KEY "constants.SQLITE_CHANGESET_FOREIGN_KEY")

If foreign key handling is enabled, and applying a changeset leaves the database in a state containing foreign key violations, the conflict handler is invoked with this constant exactly once before the changeset is committed. If the conflict handler returns `SQLITE_CHANGESET_OMIT`, the changes, including those that caused the foreign key constraint violation, are committed. Or, if it returns `SQLITE_CHANGESET_ABORT`, the changeset is rolled back.

v

[constants.SQLITE\_CHANGESET\_NOTFOUND](././sqlite/~/constants.SQLITE_CHANGESET_NOTFOUND "constants.SQLITE_CHANGESET_NOTFOUND")

The conflict handler is invoked with this constant when processing a DELETE or UPDATE change if a row with the required PRIMARY KEY fields is not present in the database.

v

[constants.SQLITE\_CHANGESET\_OMIT](././sqlite/~/constants.SQLITE_CHANGESET_OMIT "constants.SQLITE_CHANGESET_OMIT")

Conflicting changes are omitted.

v

[constants.SQLITE\_CHANGESET\_REPLACE](././sqlite/~/constants.SQLITE_CHANGESET_REPLACE "constants.SQLITE_CHANGESET_REPLACE")

Conflicting changes replace existing values. Note that this value can only be returned when the type of conflict is either `SQLITE_CHANGESET_DATA` or `SQLITE_CHANGESET_CONFLICT`.

I

[CreateSessionOptions](././sqlite/~/CreateSessionOptions "CreateSessionOptions")

No documentation available

-   [db](././sqlite/~/CreateSessionOptions#property_db)
-   [table](././sqlite/~/CreateSessionOptions#property_table)

c

[DatabaseSync](././sqlite/~/DatabaseSync "DatabaseSync")

This class represents a single [connection](https://www.sqlite.org/c3ref/sqlite3.html) to a SQLite database. All APIs exposed by this class execute synchronously.

-   [applyChangeset](././sqlite/~/DatabaseSync#method_applychangeset_0)
-   [close](././sqlite/~/DatabaseSync#method_close_0)
-   [createSession](././sqlite/~/DatabaseSync#method_createsession_0)
-   [enableLoadExtension](././sqlite/~/DatabaseSync#method_enableloadextension_0)
-   [exec](././sqlite/~/DatabaseSync#method_exec_0)
-   [function](././sqlite/~/DatabaseSync#method_function_0)
-   [loadExtension](././sqlite/~/DatabaseSync#method_loadextension_0)
-   [open](././sqlite/~/DatabaseSync#method_open_0)
-   [prepare](././sqlite/~/DatabaseSync#method_prepare_0)

I

[DatabaseSyncOptions](././sqlite/~/DatabaseSyncOptions "DatabaseSyncOptions")

No documentation available

-   [allowExtension](././sqlite/~/DatabaseSyncOptions#property_allowextension)
-   [enableDoubleQuotedStringLiterals](././sqlite/~/DatabaseSyncOptions#property_enabledoublequotedstringliterals)
-   [enableForeignKeyConstraints](././sqlite/~/DatabaseSyncOptions#property_enableforeignkeyconstraints)
-   [open](././sqlite/~/DatabaseSyncOptions#property_open)
-   [readOnly](././sqlite/~/DatabaseSyncOptions#property_readonly)

I

[FunctionOptions](././sqlite/~/FunctionOptions "FunctionOptions")

No documentation available

-   [deterministic](././sqlite/~/FunctionOptions#property_deterministic)
-   [directOnly](././sqlite/~/FunctionOptions#property_directonly)
-   [useBigIntArguments](././sqlite/~/FunctionOptions#property_usebigintarguments)
-   [varargs](././sqlite/~/FunctionOptions#property_varargs)

I

[Session](././sqlite/~/Session "Session")

No documentation available

-   [changeset](././sqlite/~/Session#method_changeset_0)
-   [close](././sqlite/~/Session#method_close_0)
-   [patchset](././sqlite/~/Session#method_patchset_0)

T

[SQLInputValue](././sqlite/~/SQLInputValue "SQLInputValue")

No documentation available

T

[SQLOutputValue](././sqlite/~/SQLOutputValue "SQLOutputValue")

No documentation available

I

[StatementResultingChanges](././sqlite/~/StatementResultingChanges "StatementResultingChanges")

No documentation available

-   [changes](././sqlite/~/StatementResultingChanges#property_changes)
-   [lastInsertRowid](././sqlite/~/StatementResultingChanges#property_lastinsertrowid)

c

[StatementSync](././sqlite/~/StatementSync "StatementSync")

This class represents a single [prepared statement](https://www.sqlite.org/c3ref/stmt.html). This class cannot be instantiated via its constructor. Instead, instances are created via the`database.prepare()` method. All APIs exposed by this class execute synchronously.

-   [all](././sqlite/~/StatementSync#method_all_0)
-   [expandedSQL](././sqlite/~/StatementSync#property_expandedsql)
-   [get](././sqlite/~/StatementSync#method_get_0)
-   [iterate](././sqlite/~/StatementSync#method_iterate_0)
-   [run](././sqlite/~/StatementSync#method_run_0)
-   [setAllowBareNamedParameters](././sqlite/~/StatementSync#method_setallowbarenamedparameters_0)
-   [setReadBigInts](././sqlite/~/StatementSync#method_setreadbigints_0)
-   [sourceSQL](././sqlite/~/StatementSync#property_sourcesql)

T

[SupportedValueType](././sqlite/~/SupportedValueType "SupportedValueType")

No documentation available

A stream is an abstract interface for working with streaming data in Node.js. The `node:stream` module provides an API for implementing the stream interface.

T

[ComposeFnParam](././stream/~/ComposeFnParam "ComposeFnParam")

No documentation available

c

N

[default](././stream/~/default "default")

No documentation available

-   [compose](././stream/~/default#method_compose_0)
-   [pipe](././stream/~/default#method_pipe_0)

f

[default.addAbortSignal](././stream/~/default.addAbortSignal "default.addAbortSignal")

A stream to attach a signal to.

I

[default.ArrayOptions](././stream/~/default.ArrayOptions "default.ArrayOptions")

No documentation available

-   [concurrency](././stream/~/default.ArrayOptions#property_concurrency)
-   [signal](././stream/~/default.ArrayOptions#property_signal)

c

I

[default.Duplex](././stream/~/default.Duplex "default.Duplex")

Duplex streams are streams that implement both the `Readable` and `Writable` interfaces.

-   [addListener](././stream/~/default.Duplex#method_addlistener_0)
-   [allowHalfOpen](././stream/~/default.Duplex#property_allowhalfopen)
-   [emit](././stream/~/default.Duplex#method_emit_0)
-   [from](././stream/~/default.Duplex#method_from_0)
-   [fromWeb](././stream/~/default.Duplex#method_fromweb_0)
-   [on](././stream/~/default.Duplex#method_on_0)
-   [once](././stream/~/default.Duplex#method_once_0)
-   [prependListener](././stream/~/default.Duplex#method_prependlistener_0)
-   [prependOnceListener](././stream/~/default.Duplex#method_prependoncelistener_0)
-   [removeListener](././stream/~/default.Duplex#method_removelistener_0)
-   [toWeb](././stream/~/default.Duplex#method_toweb_0)

I

[default.DuplexOptions](././stream/~/default.DuplexOptions "default.DuplexOptions")

No documentation available

-   [allowHalfOpen](././stream/~/default.DuplexOptions#property_allowhalfopen)
-   [readableHighWaterMark](././stream/~/default.DuplexOptions#property_readablehighwatermark)
-   [readableObjectMode](././stream/~/default.DuplexOptions#property_readableobjectmode)
-   [writableCorked](././stream/~/default.DuplexOptions#property_writablecorked)
-   [writableHighWaterMark](././stream/~/default.DuplexOptions#property_writablehighwatermark)
-   [writableObjectMode](././stream/~/default.DuplexOptions#property_writableobjectmode)

f

[default.duplexPair](././stream/~/default.duplexPair "default.duplexPair")

The utility function `duplexPair` returns an Array with two items, each being a `Duplex` stream connected to the other side:

f

N

[default.finished](././stream/~/default.finished "default.finished")

A readable and/or writable stream/webstream.

f

[default.finished.\_\_promisify\_\_](././stream/~/default.finished.__promisify__ "default.finished.__promisify__")

No documentation available

I

[default.FinishedOptions](././stream/~/default.FinishedOptions "default.FinishedOptions")

No documentation available

-   [error](././stream/~/default.FinishedOptions#property_error)
-   [readable](././stream/~/default.FinishedOptions#property_readable)
-   [writable](././stream/~/default.FinishedOptions#property_writable)

f

[default.getDefaultHighWaterMark](././stream/~/default.getDefaultHighWaterMark "default.getDefaultHighWaterMark")

Returns the default highWaterMark used by streams. Defaults to `65536` (64 KiB), or `16` for `objectMode`.

f

[default.isErrored](././stream/~/default.isErrored "default.isErrored")

Returns whether the stream has encountered an error.

f

[default.isReadable](././stream/~/default.isReadable "default.isReadable")

Returns whether the stream is readable.

c

[default.PassThrough](././stream/~/default.PassThrough "default.PassThrough")

The `stream.PassThrough` class is a trivial implementation of a `Transform` stream that simply passes the input bytes across to the output. Its purpose is primarily for examples and testing, but there are some use cases where `stream.PassThrough` is useful as a building block for novel sorts of streams.

I

[default.Pipe](././stream/~/default.Pipe "default.Pipe")

No documentation available

-   [close](././stream/~/default.Pipe#method_close_0)
-   [hasRef](././stream/~/default.Pipe#method_hasref_0)
-   [ref](././stream/~/default.Pipe#method_ref_0)
-   [unref](././stream/~/default.Pipe#method_unref_0)

f

N

[default.pipeline](././stream/~/default.pipeline "default.pipeline")

A module method to pipe between streams and generators forwarding errors and properly cleaning up and provide a callback when the pipeline is complete.

f

[default.pipeline.\_\_promisify\_\_](././stream/~/default.pipeline.__promisify__ "default.pipeline.__promisify__")

No documentation available

T

[default.PipelineCallback](././stream/~/default.PipelineCallback "default.PipelineCallback")

No documentation available

T

[default.PipelineDestination](././stream/~/default.PipelineDestination "default.PipelineDestination")

No documentation available

T

[default.PipelineDestinationIterableFunction](././stream/~/default.PipelineDestinationIterableFunction "default.PipelineDestinationIterableFunction")

No documentation available

T

[default.PipelineDestinationPromiseFunction](././stream/~/default.PipelineDestinationPromiseFunction "default.PipelineDestinationPromiseFunction")

No documentation available

I

[default.PipelineOptions](././stream/~/default.PipelineOptions "default.PipelineOptions")

No documentation available

-   [end](././stream/~/default.PipelineOptions#property_end)
-   [signal](././stream/~/default.PipelineOptions#property_signal)

T

[default.PipelinePromise](././stream/~/default.PipelinePromise "default.PipelinePromise")

No documentation available

T

[default.PipelineSource](././stream/~/default.PipelineSource "default.PipelineSource")

No documentation available

T

[default.PipelineSourceFunction](././stream/~/default.PipelineSourceFunction "default.PipelineSourceFunction")

No documentation available

T

[default.PipelineTransform](././stream/~/default.PipelineTransform "default.PipelineTransform")

No documentation available

T

[default.PipelineTransformSource](././stream/~/default.PipelineTransformSource "default.PipelineTransformSource")

No documentation available

c

[default.Readable](././stream/~/default.Readable "default.Readable")

No documentation available

-   [\_construct](././stream/~/default.Readable#method__construct_0)
-   [\_destroy](././stream/~/default.Readable#method__destroy_0)
-   [\_read](././stream/~/default.Readable#method__read_0)
-   [addListener](././stream/~/default.Readable#method_addlistener_0)
-   [asIndexedPairs](././stream/~/default.Readable#method_asindexedpairs_0)
-   [closed](././stream/~/default.Readable#property_closed)
-   [destroy](././stream/~/default.Readable#method_destroy_0)
-   [destroyed](././stream/~/default.Readable#property_destroyed)
-   [drop](././stream/~/default.Readable#method_drop_0)
-   [emit](././stream/~/default.Readable#method_emit_0)
-   [errored](././stream/~/default.Readable#property_errored)
-   [every](././stream/~/default.Readable#method_every_0)
-   [filter](././stream/~/default.Readable#method_filter_0)
-   [find](././stream/~/default.Readable#method_find_0)
-   [flatMap](././stream/~/default.Readable#method_flatmap_0)
-   [forEach](././stream/~/default.Readable#method_foreach_0)
-   [from](././stream/~/default.Readable#method_from_0)
-   [fromWeb](././stream/~/default.Readable#method_fromweb_0)
-   [isDisturbed](././stream/~/default.Readable#method_isdisturbed_0)
-   [isPaused](././stream/~/default.Readable#method_ispaused_0)
-   [iterator](././stream/~/default.Readable#method_iterator_0)
-   [map](././stream/~/default.Readable#method_map_0)
-   [on](././stream/~/default.Readable#method_on_0)
-   [once](././stream/~/default.Readable#method_once_0)
-   [pause](././stream/~/default.Readable#method_pause_0)
-   [prependListener](././stream/~/default.Readable#method_prependlistener_0)
-   [prependOnceListener](././stream/~/default.Readable#method_prependoncelistener_0)
-   [push](././stream/~/default.Readable#method_push_0)
-   [read](././stream/~/default.Readable#method_read_0)
-   [readable](././stream/~/default.Readable#property_readable)
-   [readableAborted](././stream/~/default.Readable#property_readableaborted)
-   [readableDidRead](././stream/~/default.Readable#property_readabledidread)
-   [readableEncoding](././stream/~/default.Readable#property_readableencoding)
-   [readableEnded](././stream/~/default.Readable#property_readableended)
-   [readableFlowing](././stream/~/default.Readable#property_readableflowing)
-   [readableHighWaterMark](././stream/~/default.Readable#property_readablehighwatermark)
-   [readableLength](././stream/~/default.Readable#property_readablelength)
-   [readableObjectMode](././stream/~/default.Readable#property_readableobjectmode)
-   [reduce](././stream/~/default.Readable#method_reduce_0)
-   [removeListener](././stream/~/default.Readable#method_removelistener_0)
-   [resume](././stream/~/default.Readable#method_resume_0)
-   [setEncoding](././stream/~/default.Readable#method_setencoding_0)
-   [some](././stream/~/default.Readable#method_some_0)
-   [take](././stream/~/default.Readable#method_take_0)
-   [toArray](././stream/~/default.Readable#method_toarray_0)
-   [toWeb](././stream/~/default.Readable#method_toweb_0)
-   [unpipe](././stream/~/default.Readable#method_unpipe_0)
-   [unshift](././stream/~/default.Readable#method_unshift_0)
-   [wrap](././stream/~/default.Readable#method_wrap_0)

I

[default.ReadableOptions](././stream/~/default.ReadableOptions "default.ReadableOptions")

No documentation available

-   [encoding](././stream/~/default.ReadableOptions#property_encoding)
-   [read](././stream/~/default.ReadableOptions#method_read_0)

f

[default.setDefaultHighWaterMark](././stream/~/default.setDefaultHighWaterMark "default.setDefaultHighWaterMark")

Sets the default highWaterMark used by streams.

I

[default.StreamOptions](././stream/~/default.StreamOptions "default.StreamOptions")

No documentation available

-   [autoDestroy](././stream/~/default.StreamOptions#property_autodestroy)
-   [construct](././stream/~/default.StreamOptions#method_construct_0)
-   [destroy](././stream/~/default.StreamOptions#method_destroy_0)
-   [emitClose](././stream/~/default.StreamOptions#property_emitclose)
-   [highWaterMark](././stream/~/default.StreamOptions#property_highwatermark)
-   [objectMode](././stream/~/default.StreamOptions#property_objectmode)

c

[default.Transform](././stream/~/default.Transform "default.Transform")

Transform streams are `Duplex` streams where the output is in some way related to the input. Like all `Duplex` streams, `Transform` streams implement both the `Readable` and `Writable` interfaces.

-   [\_flush](././stream/~/default.Transform#method__flush_0)
-   [\_transform](././stream/~/default.Transform#method__transform_0)

T

[default.TransformCallback](././stream/~/default.TransformCallback "default.TransformCallback")

No documentation available

I

[default.TransformOptions](././stream/~/default.TransformOptions "default.TransformOptions")

No documentation available

-   [flush](././stream/~/default.TransformOptions#method_flush_0)
-   [transform](././stream/~/default.TransformOptions#method_transform_0)

c

[default.Writable](././stream/~/default.Writable "default.Writable")

No documentation available

-   [\_construct](././stream/~/default.Writable#method__construct_0)
-   [\_destroy](././stream/~/default.Writable#method__destroy_0)
-   [\_final](././stream/~/default.Writable#method__final_0)
-   [\_write](././stream/~/default.Writable#method__write_0)
-   [\_writev](././stream/~/default.Writable#method__writev_0)
-   [addListener](././stream/~/default.Writable#method_addlistener_0)
-   [closed](././stream/~/default.Writable#property_closed)
-   [cork](././stream/~/default.Writable#method_cork_0)
-   [destroy](././stream/~/default.Writable#method_destroy_0)
-   [destroyed](././stream/~/default.Writable#property_destroyed)
-   [emit](././stream/~/default.Writable#method_emit_0)
-   [end](././stream/~/default.Writable#method_end_0)
-   [errored](././stream/~/default.Writable#property_errored)
-   [fromWeb](././stream/~/default.Writable#method_fromweb_0)
-   [on](././stream/~/default.Writable#method_on_0)
-   [once](././stream/~/default.Writable#method_once_0)
-   [prependListener](././stream/~/default.Writable#method_prependlistener_0)
-   [prependOnceListener](././stream/~/default.Writable#method_prependoncelistener_0)
-   [removeListener](././stream/~/default.Writable#method_removelistener_0)
-   [setDefaultEncoding](././stream/~/default.Writable#method_setdefaultencoding_0)
-   [toWeb](././stream/~/default.Writable#method_toweb_0)
-   [uncork](././stream/~/default.Writable#method_uncork_0)
-   [writable](././stream/~/default.Writable#property_writable)
-   [writableCorked](././stream/~/default.Writable#property_writablecorked)
-   [writableEnded](././stream/~/default.Writable#property_writableended)
-   [writableFinished](././stream/~/default.Writable#property_writablefinished)
-   [writableHighWaterMark](././stream/~/default.Writable#property_writablehighwatermark)
-   [writableLength](././stream/~/default.Writable#property_writablelength)
-   [writableNeedDrain](././stream/~/default.Writable#property_writableneeddrain)
-   [writableObjectMode](././stream/~/default.Writable#property_writableobjectmode)
-   [write](././stream/~/default.Writable#method_write_0)

I

[default.WritableOptions](././stream/~/default.WritableOptions "default.WritableOptions")

No documentation available

-   [decodeStrings](././stream/~/default.WritableOptions#property_decodestrings)
-   [defaultEncoding](././stream/~/default.WritableOptions#property_defaultencoding)
-   [final](././stream/~/default.WritableOptions#method_final_0)
-   [write](././stream/~/default.WritableOptions#method_write_0)
-   [writev](././stream/~/default.WritableOptions#method_writev_0)

c

N

[Stream](././stream/~/Stream "Stream")

No documentation available

-   [compose](././stream/~/Stream#method_compose_0)
-   [pipe](././stream/~/Stream#method_pipe_0)

f

[Stream.addAbortSignal](././stream/~/Stream.addAbortSignal "Stream.addAbortSignal")

A stream to attach a signal to.

I

[Stream.ArrayOptions](././stream/~/Stream.ArrayOptions "Stream.ArrayOptions")

No documentation available

-   [concurrency](././stream/~/Stream.ArrayOptions#property_concurrency)
-   [signal](././stream/~/Stream.ArrayOptions#property_signal)

c

I

[Stream.Duplex](././stream/~/Stream.Duplex "Stream.Duplex")

Duplex streams are streams that implement both the `Readable` and `Writable` interfaces.

-   [addListener](././stream/~/Stream.Duplex#method_addlistener_0)
-   [allowHalfOpen](././stream/~/Stream.Duplex#property_allowhalfopen)
-   [emit](././stream/~/Stream.Duplex#method_emit_0)
-   [from](././stream/~/Stream.Duplex#method_from_0)
-   [fromWeb](././stream/~/Stream.Duplex#method_fromweb_0)
-   [on](././stream/~/Stream.Duplex#method_on_0)
-   [once](././stream/~/Stream.Duplex#method_once_0)
-   [prependListener](././stream/~/Stream.Duplex#method_prependlistener_0)
-   [prependOnceListener](././stream/~/Stream.Duplex#method_prependoncelistener_0)
-   [removeListener](././stream/~/Stream.Duplex#method_removelistener_0)
-   [toWeb](././stream/~/Stream.Duplex#method_toweb_0)

I

[Stream.DuplexOptions](././stream/~/Stream.DuplexOptions "Stream.DuplexOptions")

No documentation available

-   [allowHalfOpen](././stream/~/Stream.DuplexOptions#property_allowhalfopen)
-   [readableHighWaterMark](././stream/~/Stream.DuplexOptions#property_readablehighwatermark)
-   [readableObjectMode](././stream/~/Stream.DuplexOptions#property_readableobjectmode)
-   [writableCorked](././stream/~/Stream.DuplexOptions#property_writablecorked)
-   [writableHighWaterMark](././stream/~/Stream.DuplexOptions#property_writablehighwatermark)
-   [writableObjectMode](././stream/~/Stream.DuplexOptions#property_writableobjectmode)

f

[Stream.duplexPair](././stream/~/Stream.duplexPair "Stream.duplexPair")

The utility function `duplexPair` returns an Array with two items, each being a `Duplex` stream connected to the other side:

f

N

[Stream.finished](././stream/~/Stream.finished "Stream.finished")

A readable and/or writable stream/webstream.

f

[Stream.finished.\_\_promisify\_\_](././stream/~/Stream.finished.__promisify__ "Stream.finished.__promisify__")

No documentation available

I

[Stream.FinishedOptions](././stream/~/Stream.FinishedOptions "Stream.FinishedOptions")

No documentation available

-   [error](././stream/~/Stream.FinishedOptions#property_error)
-   [readable](././stream/~/Stream.FinishedOptions#property_readable)
-   [writable](././stream/~/Stream.FinishedOptions#property_writable)

f

[Stream.getDefaultHighWaterMark](././stream/~/Stream.getDefaultHighWaterMark "Stream.getDefaultHighWaterMark")

Returns the default highWaterMark used by streams. Defaults to `65536` (64 KiB), or `16` for `objectMode`.

f

[Stream.isErrored](././stream/~/Stream.isErrored "Stream.isErrored")

Returns whether the stream has encountered an error.

f

[Stream.isReadable](././stream/~/Stream.isReadable "Stream.isReadable")

Returns whether the stream is readable.

c

[Stream.PassThrough](././stream/~/Stream.PassThrough "Stream.PassThrough")

The `stream.PassThrough` class is a trivial implementation of a `Transform` stream that simply passes the input bytes across to the output. Its purpose is primarily for examples and testing, but there are some use cases where `stream.PassThrough` is useful as a building block for novel sorts of streams.

I

[Stream.Pipe](././stream/~/Stream.Pipe "Stream.Pipe")

No documentation available

-   [close](././stream/~/Stream.Pipe#method_close_0)
-   [hasRef](././stream/~/Stream.Pipe#method_hasref_0)
-   [ref](././stream/~/Stream.Pipe#method_ref_0)
-   [unref](././stream/~/Stream.Pipe#method_unref_0)

f

N

[Stream.pipeline](././stream/~/Stream.pipeline "Stream.pipeline")

A module method to pipe between streams and generators forwarding errors and properly cleaning up and provide a callback when the pipeline is complete.

f

[Stream.pipeline.\_\_promisify\_\_](././stream/~/Stream.pipeline.__promisify__ "Stream.pipeline.__promisify__")

No documentation available

T

[Stream.PipelineCallback](././stream/~/Stream.PipelineCallback "Stream.PipelineCallback")

No documentation available

T

[Stream.PipelineDestination](././stream/~/Stream.PipelineDestination "Stream.PipelineDestination")

No documentation available

T

[Stream.PipelineDestinationIterableFunction](././stream/~/Stream.PipelineDestinationIterableFunction "Stream.PipelineDestinationIterableFunction")

No documentation available

T

[Stream.PipelineDestinationPromiseFunction](././stream/~/Stream.PipelineDestinationPromiseFunction "Stream.PipelineDestinationPromiseFunction")

No documentation available

I

[Stream.PipelineOptions](././stream/~/Stream.PipelineOptions "Stream.PipelineOptions")

No documentation available

-   [end](././stream/~/Stream.PipelineOptions#property_end)
-   [signal](././stream/~/Stream.PipelineOptions#property_signal)

T

[Stream.PipelinePromise](././stream/~/Stream.PipelinePromise "Stream.PipelinePromise")

No documentation available

T

[Stream.PipelineSource](././stream/~/Stream.PipelineSource "Stream.PipelineSource")

No documentation available

T

[Stream.PipelineSourceFunction](././stream/~/Stream.PipelineSourceFunction "Stream.PipelineSourceFunction")

No documentation available

T

[Stream.PipelineTransform](././stream/~/Stream.PipelineTransform "Stream.PipelineTransform")

No documentation available

T

[Stream.PipelineTransformSource](././stream/~/Stream.PipelineTransformSource "Stream.PipelineTransformSource")

No documentation available

c

[Stream.Readable](././stream/~/Stream.Readable "Stream.Readable")

No documentation available

-   [\_construct](././stream/~/Stream.Readable#method__construct_0)
-   [\_destroy](././stream/~/Stream.Readable#method__destroy_0)
-   [\_read](././stream/~/Stream.Readable#method__read_0)
-   [addListener](././stream/~/Stream.Readable#method_addlistener_0)
-   [asIndexedPairs](././stream/~/Stream.Readable#method_asindexedpairs_0)
-   [closed](././stream/~/Stream.Readable#property_closed)
-   [destroy](././stream/~/Stream.Readable#method_destroy_0)
-   [destroyed](././stream/~/Stream.Readable#property_destroyed)
-   [drop](././stream/~/Stream.Readable#method_drop_0)
-   [emit](././stream/~/Stream.Readable#method_emit_0)
-   [errored](././stream/~/Stream.Readable#property_errored)
-   [every](././stream/~/Stream.Readable#method_every_0)
-   [filter](././stream/~/Stream.Readable#method_filter_0)
-   [find](././stream/~/Stream.Readable#method_find_0)
-   [flatMap](././stream/~/Stream.Readable#method_flatmap_0)
-   [forEach](././stream/~/Stream.Readable#method_foreach_0)
-   [from](././stream/~/Stream.Readable#method_from_0)
-   [fromWeb](././stream/~/Stream.Readable#method_fromweb_0)
-   [isDisturbed](././stream/~/Stream.Readable#method_isdisturbed_0)
-   [isPaused](././stream/~/Stream.Readable#method_ispaused_0)
-   [iterator](././stream/~/Stream.Readable#method_iterator_0)
-   [map](././stream/~/Stream.Readable#method_map_0)
-   [on](././stream/~/Stream.Readable#method_on_0)
-   [once](././stream/~/Stream.Readable#method_once_0)
-   [pause](././stream/~/Stream.Readable#method_pause_0)
-   [prependListener](././stream/~/Stream.Readable#method_prependlistener_0)
-   [prependOnceListener](././stream/~/Stream.Readable#method_prependoncelistener_0)
-   [push](././stream/~/Stream.Readable#method_push_0)
-   [read](././stream/~/Stream.Readable#method_read_0)
-   [readable](././stream/~/Stream.Readable#property_readable)
-   [readableAborted](././stream/~/Stream.Readable#property_readableaborted)
-   [readableDidRead](././stream/~/Stream.Readable#property_readabledidread)
-   [readableEncoding](././stream/~/Stream.Readable#property_readableencoding)
-   [readableEnded](././stream/~/Stream.Readable#property_readableended)
-   [readableFlowing](././stream/~/Stream.Readable#property_readableflowing)
-   [readableHighWaterMark](././stream/~/Stream.Readable#property_readablehighwatermark)
-   [readableLength](././stream/~/Stream.Readable#property_readablelength)
-   [readableObjectMode](././stream/~/Stream.Readable#property_readableobjectmode)
-   [reduce](././stream/~/Stream.Readable#method_reduce_0)
-   [removeListener](././stream/~/Stream.Readable#method_removelistener_0)
-   [resume](././stream/~/Stream.Readable#method_resume_0)
-   [setEncoding](././stream/~/Stream.Readable#method_setencoding_0)
-   [some](././stream/~/Stream.Readable#method_some_0)
-   [take](././stream/~/Stream.Readable#method_take_0)
-   [toArray](././stream/~/Stream.Readable#method_toarray_0)
-   [toWeb](././stream/~/Stream.Readable#method_toweb_0)
-   [unpipe](././stream/~/Stream.Readable#method_unpipe_0)
-   [unshift](././stream/~/Stream.Readable#method_unshift_0)
-   [wrap](././stream/~/Stream.Readable#method_wrap_0)

I

[Stream.ReadableOptions](././stream/~/Stream.ReadableOptions "Stream.ReadableOptions")

No documentation available

-   [encoding](././stream/~/Stream.ReadableOptions#property_encoding)
-   [read](././stream/~/Stream.ReadableOptions#method_read_0)

f

[Stream.setDefaultHighWaterMark](././stream/~/Stream.setDefaultHighWaterMark "Stream.setDefaultHighWaterMark")

Sets the default highWaterMark used by streams.

I

[Stream.StreamOptions](././stream/~/Stream.StreamOptions "Stream.StreamOptions")

No documentation available

-   [autoDestroy](././stream/~/Stream.StreamOptions#property_autodestroy)
-   [construct](././stream/~/Stream.StreamOptions#method_construct_0)
-   [destroy](././stream/~/Stream.StreamOptions#method_destroy_0)
-   [emitClose](././stream/~/Stream.StreamOptions#property_emitclose)
-   [highWaterMark](././stream/~/Stream.StreamOptions#property_highwatermark)
-   [objectMode](././stream/~/Stream.StreamOptions#property_objectmode)

c

[Stream.Transform](././stream/~/Stream.Transform "Stream.Transform")

Transform streams are `Duplex` streams where the output is in some way related to the input. Like all `Duplex` streams, `Transform` streams implement both the `Readable` and `Writable` interfaces.

-   [\_flush](././stream/~/Stream.Transform#method__flush_0)
-   [\_transform](././stream/~/Stream.Transform#method__transform_0)

T

[Stream.TransformCallback](././stream/~/Stream.TransformCallback "Stream.TransformCallback")

No documentation available

I

[Stream.TransformOptions](././stream/~/Stream.TransformOptions "Stream.TransformOptions")

No documentation available

-   [flush](././stream/~/Stream.TransformOptions#method_flush_0)
-   [transform](././stream/~/Stream.TransformOptions#method_transform_0)

c

[Stream.Writable](././stream/~/Stream.Writable "Stream.Writable")

No documentation available

-   [\_construct](././stream/~/Stream.Writable#method__construct_0)
-   [\_destroy](././stream/~/Stream.Writable#method__destroy_0)
-   [\_final](././stream/~/Stream.Writable#method__final_0)
-   [\_write](././stream/~/Stream.Writable#method__write_0)
-   [\_writev](././stream/~/Stream.Writable#method__writev_0)
-   [addListener](././stream/~/Stream.Writable#method_addlistener_0)
-   [closed](././stream/~/Stream.Writable#property_closed)
-   [cork](././stream/~/Stream.Writable#method_cork_0)
-   [destroy](././stream/~/Stream.Writable#method_destroy_0)
-   [destroyed](././stream/~/Stream.Writable#property_destroyed)
-   [emit](././stream/~/Stream.Writable#method_emit_0)
-   [end](././stream/~/Stream.Writable#method_end_0)
-   [errored](././stream/~/Stream.Writable#property_errored)
-   [fromWeb](././stream/~/Stream.Writable#method_fromweb_0)
-   [on](././stream/~/Stream.Writable#method_on_0)
-   [once](././stream/~/Stream.Writable#method_once_0)
-   [prependListener](././stream/~/Stream.Writable#method_prependlistener_0)
-   [prependOnceListener](././stream/~/Stream.Writable#method_prependoncelistener_0)
-   [removeListener](././stream/~/Stream.Writable#method_removelistener_0)
-   [setDefaultEncoding](././stream/~/Stream.Writable#method_setdefaultencoding_0)
-   [toWeb](././stream/~/Stream.Writable#method_toweb_0)
-   [uncork](././stream/~/Stream.Writable#method_uncork_0)
-   [writable](././stream/~/Stream.Writable#property_writable)
-   [writableCorked](././stream/~/Stream.Writable#property_writablecorked)
-   [writableEnded](././stream/~/Stream.Writable#property_writableended)
-   [writableFinished](././stream/~/Stream.Writable#property_writablefinished)
-   [writableHighWaterMark](././stream/~/Stream.Writable#property_writablehighwatermark)
-   [writableLength](././stream/~/Stream.Writable#property_writablelength)
-   [writableNeedDrain](././stream/~/Stream.Writable#property_writableneeddrain)
-   [writableObjectMode](././stream/~/Stream.Writable#property_writableobjectmode)
-   [write](././stream/~/Stream.Writable#method_write_0)

I

[Stream.WritableOptions](././stream/~/Stream.WritableOptions "Stream.WritableOptions")

No documentation available

-   [decodeStrings](././stream/~/Stream.WritableOptions#property_decodestrings)
-   [defaultEncoding](././stream/~/Stream.WritableOptions#property_defaultencoding)
-   [final](././stream/~/Stream.WritableOptions#method_final_0)
-   [write](././stream/~/Stream.WritableOptions#method_write_0)
-   [writev](././stream/~/Stream.WritableOptions#method_writev_0)

The utility consumer functions provide common options for consuming streams.

f

[arrayBuffer](././stream/consumers/~/arrayBuffer "arrayBuffer")

No documentation available

f

[blob](././stream/consumers/~/blob "blob")

No documentation available

f

[buffer](././stream/consumers/~/buffer "buffer")

No documentation available

f

[json](././stream/consumers/~/json "json")

No documentation available

f

[text](././stream/consumers/~/text "text")

No documentation available

f

[finished](././stream/promises/~/finished "finished")

No documentation available

I

[FinishedOptions](././stream/promises/~/FinishedOptions "FinishedOptions")

No documentation available

-   [cleanup](././stream/promises/~/FinishedOptions#property_cleanup)

f

[pipeline](././stream/promises/~/pipeline "pipeline")

No documentation available

T

[BufferSource](././stream/web/~/BufferSource "BufferSource")

No documentation available

I

v

[ByteLengthQueuingStrategy](././stream/web/~/ByteLengthQueuingStrategy "ByteLengthQueuingStrategy")

This Streams API interface provides a built-in byte length queuing strategy that can be used when constructing streams.

-   [highWaterMark](././stream/web/~/ByteLengthQueuingStrategy#property_highwatermark)
-   [prototype](././stream/web/~/ByteLengthQueuingStrategy#property_prototype)
-   [size](././stream/web/~/ByteLengthQueuingStrategy#property_size)

I

v

[CompressionStream](././stream/web/~/CompressionStream "CompressionStream")

No documentation available

-   [prototype](././stream/web/~/CompressionStream#property_prototype)
-   [readable](././stream/web/~/CompressionStream#property_readable)
-   [writable](././stream/web/~/CompressionStream#property_writable)

I

v

[CountQueuingStrategy](././stream/web/~/CountQueuingStrategy "CountQueuingStrategy")

This Streams API interface provides a built-in byte length queuing strategy that can be used when constructing streams.

-   [highWaterMark](././stream/web/~/CountQueuingStrategy#property_highwatermark)
-   [prototype](././stream/web/~/CountQueuingStrategy#property_prototype)
-   [size](././stream/web/~/CountQueuingStrategy#property_size)

I

v

[DecompressionStream](././stream/web/~/DecompressionStream "DecompressionStream")

No documentation available

-   [prototype](././stream/web/~/DecompressionStream#property_prototype)
-   [readable](././stream/web/~/DecompressionStream#property_readable)
-   [writable](././stream/web/~/DecompressionStream#property_writable)

I

[QueuingStrategy](././stream/web/~/QueuingStrategy "QueuingStrategy")

No documentation available

-   [highWaterMark](././stream/web/~/QueuingStrategy#property_highwatermark)
-   [size](././stream/web/~/QueuingStrategy#property_size)

I

[QueuingStrategyInit](././stream/web/~/QueuingStrategyInit "QueuingStrategyInit")

No documentation available

-   [highWaterMark](././stream/web/~/QueuingStrategyInit#property_highwatermark)

I

[QueuingStrategySize](././stream/web/~/QueuingStrategySize "QueuingStrategySize")

No documentation available

I

v

[ReadableByteStreamController](././stream/web/~/ReadableByteStreamController "ReadableByteStreamController")

No documentation available

-   [byobRequest](././stream/web/~/ReadableByteStreamController#property_byobrequest)
-   [close](././stream/web/~/ReadableByteStreamController#method_close_0)
-   [desiredSize](././stream/web/~/ReadableByteStreamController#property_desiredsize)
-   [enqueue](././stream/web/~/ReadableByteStreamController#method_enqueue_0)
-   [error](././stream/web/~/ReadableByteStreamController#method_error_0)
-   [prototype](././stream/web/~/ReadableByteStreamController#property_prototype)

I

[ReadableByteStreamControllerCallback](././stream/web/~/ReadableByteStreamControllerCallback "ReadableByteStreamControllerCallback")

No documentation available

I

v

[ReadableStream](././stream/web/~/ReadableStream "ReadableStream")

This Streams API interface represents a readable stream of byte data.

-   [cancel](././stream/web/~/ReadableStream#method_cancel_0)
-   [from](././stream/web/~/ReadableStream#method_from_0)
-   [getReader](././stream/web/~/ReadableStream#method_getreader_0)
-   [locked](././stream/web/~/ReadableStream#property_locked)
-   [pipeThrough](././stream/web/~/ReadableStream#method_pipethrough_0)
-   [pipeTo](././stream/web/~/ReadableStream#method_pipeto_0)
-   [prototype](././stream/web/~/ReadableStream#property_prototype)
-   [tee](././stream/web/~/ReadableStream#method_tee_0)
-   [values](././stream/web/~/ReadableStream#method_values_0)

I

[ReadableStreamAsyncIterator](././stream/web/~/ReadableStreamAsyncIterator "ReadableStreamAsyncIterator")

No documentation available

I

v

[ReadableStreamBYOBReader](././stream/web/~/ReadableStreamBYOBReader "ReadableStreamBYOBReader")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBReader)

-   [prototype](././stream/web/~/ReadableStreamBYOBReader#property_prototype)
-   [read](././stream/web/~/ReadableStreamBYOBReader#method_read_0)
-   [releaseLock](././stream/web/~/ReadableStreamBYOBReader#method_releaselock_0)

I

v

[ReadableStreamBYOBRequest](././stream/web/~/ReadableStreamBYOBRequest "ReadableStreamBYOBRequest")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBRequest)

-   [prototype](././stream/web/~/ReadableStreamBYOBRequest#property_prototype)
-   [respond](././stream/web/~/ReadableStreamBYOBRequest#method_respond_0)
-   [respondWithNewView](././stream/web/~/ReadableStreamBYOBRequest#method_respondwithnewview_0)
-   [view](././stream/web/~/ReadableStreamBYOBRequest#property_view)

T

[ReadableStreamController](././stream/web/~/ReadableStreamController "ReadableStreamController")

No documentation available

I

v

[ReadableStreamDefaultController](././stream/web/~/ReadableStreamDefaultController "ReadableStreamDefaultController")

No documentation available

-   [close](././stream/web/~/ReadableStreamDefaultController#method_close_0)
-   [desiredSize](././stream/web/~/ReadableStreamDefaultController#property_desiredsize)
-   [enqueue](././stream/web/~/ReadableStreamDefaultController#method_enqueue_0)
-   [error](././stream/web/~/ReadableStreamDefaultController#method_error_0)
-   [prototype](././stream/web/~/ReadableStreamDefaultController#property_prototype)

I

v

[ReadableStreamDefaultReader](././stream/web/~/ReadableStreamDefaultReader "ReadableStreamDefaultReader")

No documentation available

-   [prototype](././stream/web/~/ReadableStreamDefaultReader#property_prototype)
-   [read](././stream/web/~/ReadableStreamDefaultReader#method_read_0)
-   [releaseLock](././stream/web/~/ReadableStreamDefaultReader#method_releaselock_0)

I

[ReadableStreamErrorCallback](././stream/web/~/ReadableStreamErrorCallback "ReadableStreamErrorCallback")

No documentation available

I

[ReadableStreamGenericReader](././stream/web/~/ReadableStreamGenericReader "ReadableStreamGenericReader")

No documentation available

-   [cancel](././stream/web/~/ReadableStreamGenericReader#method_cancel_0)
-   [closed](././stream/web/~/ReadableStreamGenericReader#property_closed)

I

[ReadableStreamGetReaderOptions](././stream/web/~/ReadableStreamGetReaderOptions "ReadableStreamGetReaderOptions")

No documentation available

-   [mode](././stream/web/~/ReadableStreamGetReaderOptions#property_mode)

I

[ReadableStreamReadDoneResult](././stream/web/~/ReadableStreamReadDoneResult "ReadableStreamReadDoneResult")

No documentation available

-   [done](././stream/web/~/ReadableStreamReadDoneResult#property_done)
-   [value](././stream/web/~/ReadableStreamReadDoneResult#property_value)

T

[ReadableStreamReader](././stream/web/~/ReadableStreamReader "ReadableStreamReader")

No documentation available

T

[ReadableStreamReaderMode](././stream/web/~/ReadableStreamReaderMode "ReadableStreamReaderMode")

No documentation available

T

[ReadableStreamReadResult](././stream/web/~/ReadableStreamReadResult "ReadableStreamReadResult")

No documentation available

I

[ReadableStreamReadValueResult](././stream/web/~/ReadableStreamReadValueResult "ReadableStreamReadValueResult")

No documentation available

-   [done](././stream/web/~/ReadableStreamReadValueResult#property_done)
-   [value](././stream/web/~/ReadableStreamReadValueResult#property_value)

I

[ReadableWritablePair](././stream/web/~/ReadableWritablePair "ReadableWritablePair")

No documentation available

-   [readable](././stream/web/~/ReadableWritablePair#property_readable)
-   [writable](././stream/web/~/ReadableWritablePair#property_writable)

I

[StreamPipeOptions](././stream/web/~/StreamPipeOptions "StreamPipeOptions")

No documentation available

-   [preventAbort](././stream/web/~/StreamPipeOptions#property_preventabort)
-   [preventCancel](././stream/web/~/StreamPipeOptions#property_preventcancel)
-   [preventClose](././stream/web/~/StreamPipeOptions#property_preventclose)
-   [signal](././stream/web/~/StreamPipeOptions#property_signal)

I

[TextDecoderOptions](././stream/web/~/TextDecoderOptions "TextDecoderOptions")

No documentation available

-   [fatal](././stream/web/~/TextDecoderOptions#property_fatal)
-   [ignoreBOM](././stream/web/~/TextDecoderOptions#property_ignorebom)

I

v

[TextDecoderStream](././stream/web/~/TextDecoderStream "TextDecoderStream")

No documentation available

-   [encoding](././stream/web/~/TextDecoderStream#property_encoding)
-   [fatal](././stream/web/~/TextDecoderStream#property_fatal)
-   [ignoreBOM](././stream/web/~/TextDecoderStream#property_ignorebom)
-   [prototype](././stream/web/~/TextDecoderStream#property_prototype)
-   [readable](././stream/web/~/TextDecoderStream#property_readable)
-   [writable](././stream/web/~/TextDecoderStream#property_writable)

I

v

[TextEncoderStream](././stream/web/~/TextEncoderStream "TextEncoderStream")

No documentation available

-   [encoding](././stream/web/~/TextEncoderStream#property_encoding)
-   [prototype](././stream/web/~/TextEncoderStream#property_prototype)
-   [readable](././stream/web/~/TextEncoderStream#property_readable)
-   [writable](././stream/web/~/TextEncoderStream#property_writable)

I

[Transformer](././stream/web/~/Transformer "Transformer")

No documentation available

-   [flush](././stream/web/~/Transformer#property_flush)
-   [readableType](././stream/web/~/Transformer#property_readabletype)
-   [start](././stream/web/~/Transformer#property_start)
-   [transform](././stream/web/~/Transformer#property_transform)
-   [writableType](././stream/web/~/Transformer#property_writabletype)

I

[TransformerFlushCallback](././stream/web/~/TransformerFlushCallback "TransformerFlushCallback")

No documentation available

I

[TransformerStartCallback](././stream/web/~/TransformerStartCallback "TransformerStartCallback")

No documentation available

I

[TransformerTransformCallback](././stream/web/~/TransformerTransformCallback "TransformerTransformCallback")

No documentation available

I

v

[TransformStream](././stream/web/~/TransformStream "TransformStream")

No documentation available

-   [prototype](././stream/web/~/TransformStream#property_prototype)
-   [readable](././stream/web/~/TransformStream#property_readable)
-   [writable](././stream/web/~/TransformStream#property_writable)

I

v

[TransformStreamDefaultController](././stream/web/~/TransformStreamDefaultController "TransformStreamDefaultController")

No documentation available

-   [desiredSize](././stream/web/~/TransformStreamDefaultController#property_desiredsize)
-   [enqueue](././stream/web/~/TransformStreamDefaultController#method_enqueue_0)
-   [error](././stream/web/~/TransformStreamDefaultController#method_error_0)
-   [prototype](././stream/web/~/TransformStreamDefaultController#property_prototype)
-   [terminate](././stream/web/~/TransformStreamDefaultController#method_terminate_0)

I

[UnderlyingByteSource](././stream/web/~/UnderlyingByteSource "UnderlyingByteSource")

No documentation available

-   [autoAllocateChunkSize](././stream/web/~/UnderlyingByteSource#property_autoallocatechunksize)
-   [cancel](././stream/web/~/UnderlyingByteSource#property_cancel)
-   [pull](././stream/web/~/UnderlyingByteSource#property_pull)
-   [start](././stream/web/~/UnderlyingByteSource#property_start)
-   [type](././stream/web/~/UnderlyingByteSource#property_type)

I

[UnderlyingSink](././stream/web/~/UnderlyingSink "UnderlyingSink")

No documentation available

-   [abort](././stream/web/~/UnderlyingSink#property_abort)
-   [close](././stream/web/~/UnderlyingSink#property_close)
-   [start](././stream/web/~/UnderlyingSink#property_start)
-   [type](././stream/web/~/UnderlyingSink#property_type)
-   [write](././stream/web/~/UnderlyingSink#property_write)

I

[UnderlyingSinkAbortCallback](././stream/web/~/UnderlyingSinkAbortCallback "UnderlyingSinkAbortCallback")

No documentation available

I

[UnderlyingSinkCloseCallback](././stream/web/~/UnderlyingSinkCloseCallback "UnderlyingSinkCloseCallback")

No documentation available

I

[UnderlyingSinkStartCallback](././stream/web/~/UnderlyingSinkStartCallback "UnderlyingSinkStartCallback")

No documentation available

I

[UnderlyingSinkWriteCallback](././stream/web/~/UnderlyingSinkWriteCallback "UnderlyingSinkWriteCallback")

No documentation available

I

[UnderlyingSource](././stream/web/~/UnderlyingSource "UnderlyingSource")

No documentation available

-   [cancel](././stream/web/~/UnderlyingSource#property_cancel)
-   [pull](././stream/web/~/UnderlyingSource#property_pull)
-   [start](././stream/web/~/UnderlyingSource#property_start)
-   [type](././stream/web/~/UnderlyingSource#property_type)

I

[UnderlyingSourceCancelCallback](././stream/web/~/UnderlyingSourceCancelCallback "UnderlyingSourceCancelCallback")

No documentation available

I

[UnderlyingSourcePullCallback](././stream/web/~/UnderlyingSourcePullCallback "UnderlyingSourcePullCallback")

No documentation available

I

[UnderlyingSourceStartCallback](././stream/web/~/UnderlyingSourceStartCallback "UnderlyingSourceStartCallback")

No documentation available

I

v

[WritableStream](././stream/web/~/WritableStream "WritableStream")

This Streams API interface provides a standard abstraction for writing streaming data to a destination, known as a sink. This object comes with built-in back pressure and queuing.

-   [abort](././stream/web/~/WritableStream#method_abort_0)
-   [close](././stream/web/~/WritableStream#method_close_0)
-   [getWriter](././stream/web/~/WritableStream#method_getwriter_0)
-   [locked](././stream/web/~/WritableStream#property_locked)
-   [prototype](././stream/web/~/WritableStream#property_prototype)

I

v

[WritableStreamDefaultController](././stream/web/~/WritableStreamDefaultController "WritableStreamDefaultController")

This Streams API interface represents a controller allowing control of a WritableStream's state. When constructing a WritableStream, the underlying sink is given a corresponding WritableStreamDefaultController instance to manipulate.

-   [error](././stream/web/~/WritableStreamDefaultController#method_error_0)
-   [prototype](././stream/web/~/WritableStreamDefaultController#property_prototype)

I

v

[WritableStreamDefaultWriter](././stream/web/~/WritableStreamDefaultWriter "WritableStreamDefaultWriter")

This Streams API interface is the object returned by WritableStream.getWriter() and once created locks the < writer to the WritableStream ensuring that no other streams can write to the underlying sink.

-   [abort](././stream/web/~/WritableStreamDefaultWriter#method_abort_0)
-   [close](././stream/web/~/WritableStreamDefaultWriter#method_close_0)
-   [closed](././stream/web/~/WritableStreamDefaultWriter#property_closed)
-   [desiredSize](././stream/web/~/WritableStreamDefaultWriter#property_desiredsize)
-   [prototype](././stream/web/~/WritableStreamDefaultWriter#property_prototype)
-   [ready](././stream/web/~/WritableStreamDefaultWriter#property_ready)
-   [releaseLock](././stream/web/~/WritableStreamDefaultWriter#method_releaselock_0)
-   [write](././stream/web/~/WritableStreamDefaultWriter#method_write_0)

The `node:string_decoder` module provides an API for decoding `Buffer` objects into strings in a manner that preserves encoded multi-byte UTF-8 and UTF-16 characters. It can be accessed using:

c

[StringDecoder](././string_decoder/~/StringDecoder "StringDecoder")

The `node:string_decoder` module provides an API for decoding `Buffer` objects into strings in a manner that preserves encoded multi-byte UTF-8 and UTF-16 characters. It can be accessed using:

-   [end](././string_decoder/~/StringDecoder#method_end_0)
-   [write](././string_decoder/~/StringDecoder#method_write_0)

The `node:test` module facilitates the creation of JavaScript tests. To access it:

f

[after](././test/~/after "after")

This function creates a hook that runs after executing a suite.

f

[afterEach](././test/~/afterEach "afterEach")

This function creates a hook that runs after each test in the current suite. The `afterEach()` hook is run even if the test fails.

N

[assert](././test/~/assert "assert")

An object whose methods are used to configure available assertions on the `TestContext` objects in the current process. The methods from `node:assert` and snapshot testing functions are available by default.

f

[assert.register](././test/~/assert.register "assert.register")

Defines a new assertion function with the provided name and function. If an assertion already exists with the same name, it is overwritten.

I

[AssertSnapshotOptions](././test/~/AssertSnapshotOptions "AssertSnapshotOptions")

No documentation available

-   [serializers](././test/~/AssertSnapshotOptions#property_serializers)

f

[before](././test/~/before "before")

This function creates a hook that runs before executing a suite.

f

[beforeEach](././test/~/beforeEach "beforeEach")

This function creates a hook that runs before each test in the current suite.

f

N

[default](././test/~/default "default")

The `test()` function is the value imported from the `test` module. Each invocation of this function results in reporting the test to the `TestsStream`.

f

[default.after](././test/~/default.after "default.after")

This function creates a hook that runs after executing a suite.

f

[default.afterEach](././test/~/default.afterEach "default.afterEach")

This function creates a hook that runs after each test in the current suite. The `afterEach()` hook is run even if the test fails.

N

[default.assert](././test/~/default.assert "default.assert")

An object whose methods are used to configure available assertions on the `TestContext` objects in the current process. The methods from `node:assert` and snapshot testing functions are available by default.

f

[default.assert.register](././test/~/default.assert.register "default.assert.register")

Defines a new assertion function with the provided name and function. If an assertion already exists with the same name, it is overwritten.

f

[default.before](././test/~/default.before "default.before")

This function creates a hook that runs before executing a suite.

f

[default.beforeEach](././test/~/default.beforeEach "default.beforeEach")

This function creates a hook that runs before each test in the current suite.

f

N

[default.describe](././test/~/default.describe "default.describe")

Alias for [suite](././test/~/suite).

f

[default.describe.only](././test/~/default.describe.only "default.describe.only")

Shorthand for marking a suite as `only`. This is the same as calling [describe](././test/~/describe) with `options.only` set to `true`.

f

[default.describe.skip](././test/~/default.describe.skip "default.describe.skip")

Shorthand for skipping a suite. This is the same as calling [describe](././test/~/describe) with `options.skip` set to `true`.

f

[default.describe.todo](././test/~/default.describe.todo "default.describe.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [describe](././test/~/describe) with `options.todo` set to `true`.

f

N

[default.it](././test/~/default.it "default.it")

Alias for [test](././test/~/test).

f

[default.it.only](././test/~/default.it.only "default.it.only")

Shorthand for marking a test as `only`. This is the same as calling [it](././test/~/it) with `options.only` set to `true`.

f

[default.it.skip](././test/~/default.it.skip "default.it.skip")

Shorthand for skipping a test. This is the same as calling [it](././test/~/it) with `options.skip` set to `true`.

f

[default.it.todo](././test/~/default.it.todo "default.it.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [it](././test/~/it) with `options.todo` set to `true`.

v

[default.mock](././test/~/default.mock "default.mock")

No documentation available

f

[default.only](././test/~/default.only "default.only")

Shorthand for marking a test as `only`. This is the same as calling [test](././test/~/test) with `options.only` set to `true`.

f

[default.run](././test/~/default.run "default.run")

**Note:** `shard` is used to horizontally parallelize test running across machines or processes, ideal for large-scale executions across varied environments. It's incompatible with `watch` mode, tailored for rapid code iteration by automatically rerunning tests on file changes.

f

[default.skip](././test/~/default.skip "default.skip")

Shorthand for skipping a test. This is the same as calling [test](././test/~/test) with `options.skip` set to `true`.

N

[default.snapshot](././test/~/default.snapshot "default.snapshot")

No documentation available

f

[default.snapshot.setDefaultSnapshotSerializers](././test/~/default.snapshot.setDefaultSnapshotSerializers "default.snapshot.setDefaultSnapshotSerializers")

This function is used to customize the default serialization mechanism used by the test runner.

f

[default.snapshot.setResolveSnapshotPath](././test/~/default.snapshot.setResolveSnapshotPath "default.snapshot.setResolveSnapshotPath")

This function is used to set a custom resolver for the location of the snapshot file used for snapshot testing. By default, the snapshot filename is the same as the entry point filename with `.snapshot` appended.

f

N

[default.suite](././test/~/default.suite "default.suite")

The `suite()` function is imported from the `node:test` module.

f

[default.suite.only](././test/~/default.suite.only "default.suite.only")

Shorthand for marking a suite as `only`. This is the same as calling [suite](././test/~/suite) with `options.only` set to `true`.

f

[default.suite.skip](././test/~/default.suite.skip "default.suite.skip")

Shorthand for skipping a suite. This is the same as calling [suite](././test/~/suite) with `options.skip` set to `true`.

f

[default.suite.todo](././test/~/default.suite.todo "default.suite.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [suite](././test/~/suite) with `options.todo` set to `true`.

f

[default.todo](././test/~/default.todo "default.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [test](././test/~/test) with `options.todo` set to `true`.

f

N

[describe](././test/~/describe "describe")

Alias for [suite](././test/~/suite).

f

[describe.only](././test/~/describe.only "describe.only")

Shorthand for marking a suite as `only`. This is the same as calling [describe](././test/~/describe) with `options.only` set to `true`.

f

[describe.skip](././test/~/describe.skip "describe.skip")

Shorthand for skipping a suite. This is the same as calling [describe](././test/~/describe) with `options.skip` set to `true`.

f

[describe.todo](././test/~/describe.todo "describe.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [describe](././test/~/describe) with `options.todo` set to `true`.

T

[FunctionPropertyNames](././test/~/FunctionPropertyNames "FunctionPropertyNames")

No documentation available

T

[HookFn](././test/~/HookFn "HookFn")

The hook function. The first argument is the context in which the hook is called. If the hook uses callbacks, the callback function is passed as the second argument.

I

[HookOptions](././test/~/HookOptions "HookOptions")

Configuration options for hooks.

-   [signal](././test/~/HookOptions#property_signal)
-   [timeout](././test/~/HookOptions#property_timeout)

f

N

[it](././test/~/it "it")

Alias for [test](././test/~/test).

f

[it.only](././test/~/it.only "it.only")

Shorthand for marking a test as `only`. This is the same as calling [it](././test/~/it) with `options.only` set to `true`.

f

[it.skip](././test/~/it.skip "it.skip")

Shorthand for skipping a test. This is the same as calling [it](././test/~/it) with `options.skip` set to `true`.

f

[it.todo](././test/~/it.todo "it.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [it](././test/~/it) with `options.todo` set to `true`.

T

[Mock](././test/~/Mock "Mock")

No documentation available

v

[mock](././test/~/mock "mock")

No documentation available

I

[MockFunctionCall](././test/~/MockFunctionCall "MockFunctionCall")

No documentation available

-   [arguments](././test/~/MockFunctionCall#property_arguments)
-   [error](././test/~/MockFunctionCall#property_error)
-   [result](././test/~/MockFunctionCall#property_result)
-   [stack](././test/~/MockFunctionCall#property_stack)
-   [target](././test/~/MockFunctionCall#property_target)
-   [this](././test/~/MockFunctionCall#property_this)

c

[MockFunctionContext](././test/~/MockFunctionContext "MockFunctionContext")

The `MockFunctionContext` class is used to inspect or manipulate the behavior of mocks created via the `MockTracker` APIs.

-   [callCount](././test/~/MockFunctionContext#method_callcount_0)
-   [calls](././test/~/MockFunctionContext#property_calls)
-   [mockImplementation](././test/~/MockFunctionContext#method_mockimplementation_0)
-   [mockImplementationOnce](././test/~/MockFunctionContext#method_mockimplementationonce_0)
-   [resetCalls](././test/~/MockFunctionContext#method_resetcalls_0)
-   [restore](././test/~/MockFunctionContext#method_restore_0)

I

[MockFunctionOptions](././test/~/MockFunctionOptions "MockFunctionOptions")

No documentation available

-   [times](././test/~/MockFunctionOptions#property_times)

I

[MockMethodOptions](././test/~/MockMethodOptions "MockMethodOptions")

No documentation available

-   [getter](././test/~/MockMethodOptions#property_getter)
-   [setter](././test/~/MockMethodOptions#property_setter)

c

[MockModuleContext](././test/~/MockModuleContext "MockModuleContext")

No documentation available

-   [restore](././test/~/MockModuleContext#method_restore_0)

I

[MockModuleOptions](././test/~/MockModuleOptions "MockModuleOptions")

No documentation available

-   [cache](././test/~/MockModuleOptions#property_cache)
-   [defaultExport](././test/~/MockModuleOptions#property_defaultexport)
-   [namedExports](././test/~/MockModuleOptions#property_namedexports)

c

[MockTimers](././test/~/MockTimers "MockTimers")

Mocking timers is a technique commonly used in software testing to simulate and control the behavior of timers, such as `setInterval` and `setTimeout`, without actually waiting for the specified time intervals.

-   [enable](././test/~/MockTimers#method_enable_0)
-   [reset](././test/~/MockTimers#method_reset_0)
-   [runAll](././test/~/MockTimers#method_runall_0)
-   [setTime](././test/~/MockTimers#method_settime_0)
-   [tick](././test/~/MockTimers#method_tick_0)

I

[MockTimersOptions](././test/~/MockTimersOptions "MockTimersOptions")

No documentation available

-   [apis](././test/~/MockTimersOptions#property_apis)
-   [now](././test/~/MockTimersOptions#property_now)

c

[MockTracker](././test/~/MockTracker "MockTracker")

The `MockTracker` class is used to manage mocking functionality. The test runner module provides a top level `mock` export which is a `MockTracker` instance. Each test also provides its own `MockTracker` instance via the test context's `mock` property.

-   [fn](././test/~/MockTracker#method_fn_0)
-   [getter](././test/~/MockTracker#method_getter_0)
-   [method](././test/~/MockTracker#method_method_0)
-   [module](././test/~/MockTracker#method_module_0)
-   [reset](././test/~/MockTracker#method_reset_0)
-   [restoreAll](././test/~/MockTracker#method_restoreall_0)
-   [setter](././test/~/MockTracker#method_setter_0)
-   [timers](././test/~/MockTracker#property_timers)

T

[NoOpFunction](././test/~/NoOpFunction "NoOpFunction")

No documentation available

f

[only](././test/~/only "only")

Shorthand for marking a test as `only`. This is the same as calling [test](././test/~/test) with `options.only` set to `true`.

f

[run](././test/~/run "run")

**Note:** `shard` is used to horizontally parallelize test running across machines or processes, ideal for large-scale executions across varied environments. It's incompatible with `watch` mode, tailored for rapid code iteration by automatically rerunning tests on file changes.

I

[RunOptions](././test/~/RunOptions "RunOptions")

No documentation available

-   [argv](././test/~/RunOptions#property_argv)
-   [branchCoverage](././test/~/RunOptions#property_branchcoverage)
-   [concurrency](././test/~/RunOptions#property_concurrency)
-   [coverage](././test/~/RunOptions#property_coverage)
-   [coverageExcludeGlobs](././test/~/RunOptions#property_coverageexcludeglobs)
-   [coverageIncludeGlobs](././test/~/RunOptions#property_coverageincludeglobs)
-   [execArgv](././test/~/RunOptions#property_execargv)
-   [files](././test/~/RunOptions#property_files)
-   [forceExit](././test/~/RunOptions#property_forceexit)
-   [functionCoverage](././test/~/RunOptions#property_functioncoverage)
-   [globPatterns](././test/~/RunOptions#property_globpatterns)
-   [inspectPort](././test/~/RunOptions#property_inspectport)
-   [isolation](././test/~/RunOptions#property_isolation)
-   [lineCoverage](././test/~/RunOptions#property_linecoverage)
-   [only](././test/~/RunOptions#property_only)
-   [setup](././test/~/RunOptions#property_setup)
-   [shard](././test/~/RunOptions#property_shard)
-   [signal](././test/~/RunOptions#property_signal)
-   [testNamePatterns](././test/~/RunOptions#property_testnamepatterns)
-   [testSkipPatterns](././test/~/RunOptions#property_testskippatterns)
-   [timeout](././test/~/RunOptions#property_timeout)
-   [watch](././test/~/RunOptions#property_watch)

f

[skip](././test/~/skip "skip")

Shorthand for skipping a test. This is the same as calling [test](././test/~/test) with `options.skip` set to `true`.

N

[snapshot](././test/~/snapshot "snapshot")

No documentation available

f

[snapshot.setDefaultSnapshotSerializers](././test/~/snapshot.setDefaultSnapshotSerializers "snapshot.setDefaultSnapshotSerializers")

This function is used to customize the default serialization mechanism used by the test runner.

f

[snapshot.setResolveSnapshotPath](././test/~/snapshot.setResolveSnapshotPath "snapshot.setResolveSnapshotPath")

This function is used to set a custom resolver for the location of the snapshot file used for snapshot testing. By default, the snapshot filename is the same as the entry point filename with `.snapshot` appended.

f

N

[suite](././test/~/suite "suite")

The `suite()` function is imported from the `node:test` module.

f

[suite.only](././test/~/suite.only "suite.only")

Shorthand for marking a suite as `only`. This is the same as calling [suite](././test/~/suite) with `options.only` set to `true`.

f

[suite.skip](././test/~/suite.skip "suite.skip")

Shorthand for skipping a suite. This is the same as calling [suite](././test/~/suite) with `options.skip` set to `true`.

f

[suite.todo](././test/~/suite.todo "suite.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [suite](././test/~/suite) with `options.todo` set to `true`.

c

[SuiteContext](././test/~/SuiteContext "SuiteContext")

An instance of `SuiteContext` is passed to each suite function in order to interact with the test runner. However, the `SuiteContext` constructor is not exposed as part of the API.

-   [filePath](././test/~/SuiteContext#property_filepath)
-   [name](././test/~/SuiteContext#property_name)
-   [signal](././test/~/SuiteContext#property_signal)

T

[SuiteFn](././test/~/SuiteFn "SuiteFn")

The type of a suite test function. The argument to this function is a [SuiteContext](././test/~/SuiteContext) object.

f

N

[test](././test/~/test "test")

The `test()` function is the value imported from the `test` module. Each invocation of this function results in reporting the test to the `TestsStream`.

f

[test.after](././test/~/test.after "test.after")

This function creates a hook that runs after executing a suite.

f

[test.afterEach](././test/~/test.afterEach "test.afterEach")

This function creates a hook that runs after each test in the current suite. The `afterEach()` hook is run even if the test fails.

N

[test.assert](././test/~/test.assert "test.assert")

An object whose methods are used to configure available assertions on the `TestContext` objects in the current process. The methods from `node:assert` and snapshot testing functions are available by default.

f

[test.assert.register](././test/~/test.assert.register "test.assert.register")

Defines a new assertion function with the provided name and function. If an assertion already exists with the same name, it is overwritten.

f

[test.before](././test/~/test.before "test.before")

This function creates a hook that runs before executing a suite.

f

[test.beforeEach](././test/~/test.beforeEach "test.beforeEach")

This function creates a hook that runs before each test in the current suite.

f

N

[test.describe](././test/~/test.describe "test.describe")

Alias for [suite](././test/~/suite).

f

[test.describe.only](././test/~/test.describe.only "test.describe.only")

Shorthand for marking a suite as `only`. This is the same as calling [describe](././test/~/describe) with `options.only` set to `true`.

f

[test.describe.skip](././test/~/test.describe.skip "test.describe.skip")

Shorthand for skipping a suite. This is the same as calling [describe](././test/~/describe) with `options.skip` set to `true`.

f

[test.describe.todo](././test/~/test.describe.todo "test.describe.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [describe](././test/~/describe) with `options.todo` set to `true`.

f

N

[test.it](././test/~/test.it "test.it")

Alias for [test](././test/~/test).

f

[test.it.only](././test/~/test.it.only "test.it.only")

Shorthand for marking a test as `only`. This is the same as calling [it](././test/~/it) with `options.only` set to `true`.

f

[test.it.skip](././test/~/test.it.skip "test.it.skip")

Shorthand for skipping a test. This is the same as calling [it](././test/~/it) with `options.skip` set to `true`.

f

[test.it.todo](././test/~/test.it.todo "test.it.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [it](././test/~/it) with `options.todo` set to `true`.

v

[test.mock](././test/~/test.mock "test.mock")

No documentation available

f

[test.only](././test/~/test.only "test.only")

Shorthand for marking a test as `only`. This is the same as calling [test](././test/~/test) with `options.only` set to `true`.

f

[test.run](././test/~/test.run "test.run")

**Note:** `shard` is used to horizontally parallelize test running across machines or processes, ideal for large-scale executions across varied environments. It's incompatible with `watch` mode, tailored for rapid code iteration by automatically rerunning tests on file changes.

f

[test.skip](././test/~/test.skip "test.skip")

Shorthand for skipping a test. This is the same as calling [test](././test/~/test) with `options.skip` set to `true`.

N

[test.snapshot](././test/~/test.snapshot "test.snapshot")

No documentation available

f

[test.snapshot.setDefaultSnapshotSerializers](././test/~/test.snapshot.setDefaultSnapshotSerializers "test.snapshot.setDefaultSnapshotSerializers")

This function is used to customize the default serialization mechanism used by the test runner.

f

[test.snapshot.setResolveSnapshotPath](././test/~/test.snapshot.setResolveSnapshotPath "test.snapshot.setResolveSnapshotPath")

This function is used to set a custom resolver for the location of the snapshot file used for snapshot testing. By default, the snapshot filename is the same as the entry point filename with `.snapshot` appended.

f

N

[test.suite](././test/~/test.suite "test.suite")

The `suite()` function is imported from the `node:test` module.

f

[test.suite.only](././test/~/test.suite.only "test.suite.only")

Shorthand for marking a suite as `only`. This is the same as calling [suite](././test/~/suite) with `options.only` set to `true`.

f

[test.suite.skip](././test/~/test.suite.skip "test.suite.skip")

Shorthand for skipping a suite. This is the same as calling [suite](././test/~/suite) with `options.skip` set to `true`.

f

[test.suite.todo](././test/~/test.suite.todo "test.suite.todo")

Shorthand for marking a suite as `TODO`. This is the same as calling [suite](././test/~/suite) with `options.todo` set to `true`.

f

[test.todo](././test/~/test.todo "test.todo")

Shorthand for marking a test as `TODO`. This is the same as calling [test](././test/~/test) with `options.todo` set to `true`.

c

[TestContext](././test/~/TestContext "TestContext")

An instance of `TestContext` is passed to each test function in order to interact with the test runner. However, the `TestContext` constructor is not exposed as part of the API.

-   [after](././test/~/TestContext#method_after_0)
-   [afterEach](././test/~/TestContext#method_aftereach_0)
-   [assert](././test/~/TestContext#property_assert)
-   [before](././test/~/TestContext#method_before_0)
-   [beforeEach](././test/~/TestContext#method_beforeeach_0)
-   [diagnostic](././test/~/TestContext#method_diagnostic_0)
-   [filePath](././test/~/TestContext#property_filepath)
-   [fullName](././test/~/TestContext#property_fullname)
-   [mock](././test/~/TestContext#property_mock)
-   [name](././test/~/TestContext#property_name)
-   [plan](././test/~/TestContext#method_plan_0)
-   [runOnly](././test/~/TestContext#method_runonly_0)
-   [signal](././test/~/TestContext#property_signal)
-   [skip](././test/~/TestContext#method_skip_0)
-   [test](././test/~/TestContext#property_test)
-   [todo](././test/~/TestContext#method_todo_0)
-   [waitFor](././test/~/TestContext#method_waitfor_0)

I

[TestContextAssert](././test/~/TestContextAssert "TestContextAssert")

No documentation available

-   [fileSnapshot](././test/~/TestContextAssert#method_filesnapshot_0)
-   [snapshot](././test/~/TestContextAssert#method_snapshot_0)

T

[TestContextHookFn](././test/~/TestContextHookFn "TestContextHookFn")

The hook function. The first argument is a `TestContext` object. If the hook uses callbacks, the callback function is passed as the second argument.

I

[TestContextWaitForOptions](././test/~/TestContextWaitForOptions "TestContextWaitForOptions")

No documentation available

-   [interval](././test/~/TestContextWaitForOptions#property_interval)
-   [timeout](././test/~/TestContextWaitForOptions#property_timeout)

T

[TestFn](././test/~/TestFn "TestFn")

The type of a function passed to [test](././test/~/test). The first argument to this function is a [TestContext](././test/~/TestContext) object. If the test uses callbacks, the callback function is passed as the second argument.

I

[TestOptions](././test/~/TestOptions "TestOptions")

No documentation available

-   [concurrency](././test/~/TestOptions#property_concurrency)
-   [only](././test/~/TestOptions#property_only)
-   [plan](././test/~/TestOptions#property_plan)
-   [signal](././test/~/TestOptions#property_signal)
-   [skip](././test/~/TestOptions#property_skip)
-   [timeout](././test/~/TestOptions#property_timeout)
-   [todo](././test/~/TestOptions#property_todo)

I

[TestShard](././test/~/TestShard "TestShard")

No documentation available

-   [index](././test/~/TestShard#property_index)
-   [total](././test/~/TestShard#property_total)

c

[TestsStream](././test/~/TestsStream "TestsStream")

A successful call to `run()` will return a new `TestsStream` object, streaming a series of events representing the execution of the tests.

-   [addListener](././test/~/TestsStream#method_addlistener_0)
-   [emit](././test/~/TestsStream#method_emit_0)
-   [on](././test/~/TestsStream#method_on_0)
-   [once](././test/~/TestsStream#method_once_0)
-   [prependListener](././test/~/TestsStream#method_prependlistener_0)
-   [prependOnceListener](././test/~/TestsStream#method_prependoncelistener_0)

T

[Timer](././test/~/Timer "Timer")

No documentation available

f

[todo](././test/~/todo "todo")

Shorthand for marking a test as `TODO`. This is the same as calling [test](././test/~/test) with `options.todo` set to `true`.

The `node:test/reporters` module exposes the builtin-reporters for `node:test`. To access it:

f

[dot](././test/reporters/~/dot "dot")

The `dot` reporter outputs the test results in a compact format, where each passing test is represented by a `.`, and each failing test is represented by a `X`.

f

[junit](././test/reporters/~/junit "junit")

The `junit` reporter outputs test results in a jUnit XML format.

v

[lcov](././test/reporters/~/lcov "lcov")

The `lcov` reporter outputs test coverage when used with the [`--experimental-test-coverage`](https://nodejs.org/docs/latest-v22.x/api/cli.html#--experimental-test-coverage) flag.

c

[LcovReporter](././test/reporters/~/LcovReporter "LcovReporter")

No documentation available

I

[ReporterConstructorWrapper](././test/reporters/~/ReporterConstructorWrapper "ReporterConstructorWrapper")

No documentation available

v

[spec](././test/reporters/~/spec "spec")

The `spec` reporter outputs the test results in a human-readable format.

c

[SpecReporter](././test/reporters/~/SpecReporter "SpecReporter")

No documentation available

f

[tap](././test/reporters/~/tap "tap")

The `tap` reporter outputs the test results in the [TAP](https://testanything.org/) format.

T

[TestEvent](././test/reporters/~/TestEvent "TestEvent")

No documentation available

T

[TestEventGenerator](././test/reporters/~/TestEventGenerator "TestEventGenerator")

No documentation available

The `timer` module exposes a global API for scheduling functions to be called at some future period of time. Because the timer functions are globals, there is no need to import `node:timers` to use the API.

f

[clearImmediate](././timers/~/clearImmediate "clearImmediate")

Cancels an `Immediate` object created by `setImmediate()`.

f

[clearInterval](././timers/~/clearInterval "clearInterval")

Cancels a `Timeout` object created by `setInterval()`.

f

[clearTimeout](././timers/~/clearTimeout "clearTimeout")

Cancels a `Timeout` object created by `setTimeout()`.

I

[Immediate](././timers/~/Immediate "Immediate")

This object is created internally and is returned from `setImmediate()`. It can be passed to `clearImmediate()` in order to cancel the scheduled actions.

-   [\_onImmediate](././timers/~/Immediate#method__onimmediate_0)
-   [hasRef](././timers/~/Immediate#method_hasref_0)
-   [ref](././timers/~/Immediate#method_ref_0)
-   [unref](././timers/~/Immediate#method_unref_0)

N

[promises](././timers/~/promises "promises")

The `timers/promises` API provides an alternative set of timer functions that return `Promise` objects. The API is accessible via `require('node:timers/promises')`.

f

[queueMicrotask](././timers/~/queueMicrotask "queueMicrotask")

The `queueMicrotask()` method queues a microtask to invoke `callback`. If `callback` throws an exception, the `process` object `'uncaughtException'` event will be emitted.

f

N

[setImmediate](././timers/~/setImmediate "setImmediate")

Schedules the "immediate" execution of the `callback` after I/O events' callbacks.

f

[setInterval](././timers/~/setInterval "setInterval")

Schedules repeated execution of `callback` every `delay` milliseconds.

f

N

[setTimeout](././timers/~/setTimeout "setTimeout")

Schedules execution of a one-time `callback` after `delay` milliseconds.

I

[Timeout](././timers/~/Timeout "Timeout")

This object is created internally and is returned from `setTimeout()` and `setInterval()`. It can be passed to either `clearTimeout()` or `clearInterval()` in order to cancel the scheduled actions.

-   [\_onTimeout](././timers/~/Timeout#method__ontimeout_0)
-   [close](././timers/~/Timeout#method_close_0)
-   [hasRef](././timers/~/Timeout#method_hasref_0)
-   [ref](././timers/~/Timeout#method_ref_0)
-   [refresh](././timers/~/Timeout#method_refresh_0)
-   [unref](././timers/~/Timeout#method_unref_0)

I

[TimerOptions](././timers/~/TimerOptions "TimerOptions")

No documentation available

-   [ref](././timers/~/TimerOptions#property_ref)

I

[Timer](././timers/~/Timer "Timer")

No documentation available

-   [hasRef](././timers/~/Timer#method_hasref_0)
-   [refresh](././timers/~/Timer#method_refresh_0)

The `timers/promises` API provides an alternative set of timer functions that return `Promise` objects. The API is accessible via `require('node:timers/promises')`.

I

[promises.Scheduler](././timers/promises/~/promises.Scheduler "promises.Scheduler")

No documentation available

-   [wait](././timers/promises/~/promises.Scheduler#method_wait_0)
-   [yield](././timers/promises/~/promises.Scheduler#method_yield_0)

v

[promises.scheduler](././timers/promises/~/promises.scheduler "promises.scheduler")

No documentation available

f

[promises.setImmediate](././timers/promises/~/promises.setImmediate "promises.setImmediate")

No documentation available

f

[promises.setInterval](././timers/promises/~/promises.setInterval "promises.setInterval")

Returns an async iterator that generates values in an interval of `delay` ms. If `ref` is `true`, you need to call `next()` of async iterator explicitly or implicitly to keep the event loop alive.

f

[promises.setTimeout](././timers/promises/~/promises.setTimeout "promises.setTimeout")

No documentation available

I

[Scheduler](././timers/promises/~/Scheduler "Scheduler")

No documentation available

-   [wait](././timers/promises/~/Scheduler#method_wait_0)
-   [yield](././timers/promises/~/Scheduler#method_yield_0)

v

[scheduler](././timers/promises/~/scheduler "scheduler")

No documentation available

f

[setImmediate](././timers/promises/~/setImmediate "setImmediate")

No documentation available

f

[setImmediate.setImmediate](././timers/promises/~/setImmediate.setImmediate "setImmediate.setImmediate")

No documentation available

f

[setInterval](././timers/promises/~/setInterval "setInterval")

Returns an async iterator that generates values in an interval of `delay` ms. If `ref` is `true`, you need to call `next()` of async iterator explicitly or implicitly to keep the event loop alive.

f

[setTimeout](././timers/promises/~/setTimeout "setTimeout")

No documentation available

f

[setTimeout.setTimeout](././timers/promises/~/setTimeout.setTimeout "setTimeout.setTimeout")

No documentation available

The `node:tls` module provides an implementation of the Transport Layer Security (TLS) and Secure Socket Layer (SSL) protocols that is built on top of OpenSSL. The module can be accessed using:

I

[Certificate](././tls/~/Certificate "Certificate")

No documentation available

-   [C](././tls/~/Certificate#property_c)
-   [CN](././tls/~/Certificate#property_cn)
-   [L](././tls/~/Certificate#property_l)
-   [O](././tls/~/Certificate#property_o)
-   [OU](././tls/~/Certificate#property_ou)
-   [ST](././tls/~/Certificate#property_st)

f

[checkServerIdentity](././tls/~/checkServerIdentity "checkServerIdentity")

Verifies the certificate `cert` is issued to `hostname`.

I

[CipherNameAndProtocol](././tls/~/CipherNameAndProtocol "CipherNameAndProtocol")

No documentation available

-   [name](././tls/~/CipherNameAndProtocol#property_name)
-   [standardName](././tls/~/CipherNameAndProtocol#property_standardname)
-   [version](././tls/~/CipherNameAndProtocol#property_version)

v

[CLIENT\_RENEG\_LIMIT](././tls/~/CLIENT_RENEG_LIMIT "CLIENT_RENEG_LIMIT")

No documentation available

v

[CLIENT\_RENEG\_WINDOW](././tls/~/CLIENT_RENEG_WINDOW "CLIENT_RENEG_WINDOW")

No documentation available

I

[CommonConnectionOptions](././tls/~/CommonConnectionOptions "CommonConnectionOptions")

No documentation available

-   [ALPNProtocols](././tls/~/CommonConnectionOptions#property_alpnprotocols)
-   [SNICallback](././tls/~/CommonConnectionOptions#property_snicallback)
-   [enableTrace](././tls/~/CommonConnectionOptions#property_enabletrace)
-   [rejectUnauthorized](././tls/~/CommonConnectionOptions#property_rejectunauthorized)
-   [requestCert](././tls/~/CommonConnectionOptions#property_requestcert)
-   [secureContext](././tls/~/CommonConnectionOptions#property_securecontext)

f

[connect](././tls/~/connect "connect")

The `callback` function, if specified, will be added as a listener for the `'secureConnect'` event.

I

[ConnectionOptions](././tls/~/ConnectionOptions "ConnectionOptions")

No documentation available

-   [checkServerIdentity](././tls/~/ConnectionOptions#property_checkserveridentity)
-   [host](././tls/~/ConnectionOptions#property_host)
-   [lookup](././tls/~/ConnectionOptions#property_lookup)
-   [minDHSize](././tls/~/ConnectionOptions#property_mindhsize)
-   [path](././tls/~/ConnectionOptions#property_path)
-   [port](././tls/~/ConnectionOptions#property_port)
-   [pskCallback](././tls/~/ConnectionOptions#method_pskcallback_0)
-   [servername](././tls/~/ConnectionOptions#property_servername)
-   [session](././tls/~/ConnectionOptions#property_session)
-   [socket](././tls/~/ConnectionOptions#property_socket)
-   [timeout](././tls/~/ConnectionOptions#property_timeout)

f

[createSecureContext](././tls/~/createSecureContext "createSecureContext")

`[createServer](././tls/~/createServer)` sets the default value of the `honorCipherOrder` option to `true`, other APIs that create secure contexts leave it unset.

f

[createServer](././tls/~/createServer "createServer")

Creates a new [Server](././tls/~/Server). The `secureConnectionListener`, if provided, is automatically set as a listener for the `'secureConnection'` event.

v

[DEFAULT\_CIPHERS](././tls/~/DEFAULT_CIPHERS "DEFAULT_CIPHERS")

The default value of the `ciphers` option of `createSecureContext()`. It can be assigned any of the supported OpenSSL ciphers. Defaults to the content of `crypto.constants.defaultCoreCipherList`, unless changed using CLI options using `--tls-default-ciphers`.

v

[DEFAULT\_ECDH\_CURVE](././tls/~/DEFAULT_ECDH_CURVE "DEFAULT_ECDH_CURVE")

The default curve name to use for ECDH key agreement in a tls server. The default value is `'auto'`. See `createSecureContext()` for further information.

v

[DEFAULT\_MAX\_VERSION](././tls/~/DEFAULT_MAX_VERSION "DEFAULT_MAX_VERSION")

The default value of the `maxVersion` option of `createSecureContext()`. It can be assigned any of the supported TLS protocol versions, `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. **Default:** `'TLSv1.3'`, unless changed using CLI options. Using `--tls-max-v1.2` sets the default to `'TLSv1.2'`. Using `--tls-max-v1.3` sets the default to `'TLSv1.3'`. If multiple of the options are provided, the highest maximum is used.

v

[DEFAULT\_MIN\_VERSION](././tls/~/DEFAULT_MIN_VERSION "DEFAULT_MIN_VERSION")

The default value of the `minVersion` option of `createSecureContext()`. It can be assigned any of the supported TLS protocol versions, `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. **Default:** `'TLSv1.2'`, unless changed using CLI options. Using `--tls-min-v1.0` sets the default to `'TLSv1'`. Using `--tls-min-v1.1` sets the default to `'TLSv1.1'`. Using `--tls-min-v1.3` sets the default to `'TLSv1.3'`. If multiple of the options are provided, the lowest minimum is used.

I

[DetailedPeerCertificate](././tls/~/DetailedPeerCertificate "DetailedPeerCertificate")

No documentation available

-   [issuerCertificate](././tls/~/DetailedPeerCertificate#property_issuercertificate)

I

[EphemeralKeyInfo](././tls/~/EphemeralKeyInfo "EphemeralKeyInfo")

No documentation available

-   [name](././tls/~/EphemeralKeyInfo#property_name)
-   [size](././tls/~/EphemeralKeyInfo#property_size)
-   [type](././tls/~/EphemeralKeyInfo#property_type)

f

[getCiphers](././tls/~/getCiphers "getCiphers")

Returns an array with the names of the supported TLS ciphers. The names are lower-case for historical reasons, but must be uppercased to be used in the `ciphers` option of `[createSecureContext](././tls/~/createSecureContext)`.

I

[KeyObject](././tls/~/KeyObject "KeyObject")

No documentation available

-   [passphrase](././tls/~/KeyObject#property_passphrase)
-   [pem](././tls/~/KeyObject#property_pem)

I

[PeerCertificate](././tls/~/PeerCertificate "PeerCertificate")

No documentation available

-   [asn1Curve](././tls/~/PeerCertificate#property_asn1curve)
-   [bits](././tls/~/PeerCertificate#property_bits)
-   [ca](././tls/~/PeerCertificate#property_ca)
-   [exponent](././tls/~/PeerCertificate#property_exponent)
-   [ext\_key\_usage](././tls/~/PeerCertificate#property_ext_key_usage)
-   [fingerprint](././tls/~/PeerCertificate#property_fingerprint)
-   [fingerprint256](././tls/~/PeerCertificate#property_fingerprint256)
-   [fingerprint512](././tls/~/PeerCertificate#property_fingerprint512)
-   [infoAccess](././tls/~/PeerCertificate#property_infoaccess)
-   [issuer](././tls/~/PeerCertificate#property_issuer)
-   [modulus](././tls/~/PeerCertificate#property_modulus)
-   [nistCurve](././tls/~/PeerCertificate#property_nistcurve)
-   [pubkey](././tls/~/PeerCertificate#property_pubkey)
-   [raw](././tls/~/PeerCertificate#property_raw)
-   [serialNumber](././tls/~/PeerCertificate#property_serialnumber)
-   [subject](././tls/~/PeerCertificate#property_subject)
-   [subjectaltname](././tls/~/PeerCertificate#property_subjectaltname)
-   [valid\_from](././tls/~/PeerCertificate#property_valid_from)
-   [valid\_to](././tls/~/PeerCertificate#property_valid_to)

I

[PSKCallbackNegotation](././tls/~/PSKCallbackNegotation "PSKCallbackNegotation")

No documentation available

-   [identity](././tls/~/PSKCallbackNegotation#property_identity)
-   [psk](././tls/~/PSKCallbackNegotation#property_psk)

I

[PxfObject](././tls/~/PxfObject "PxfObject")

No documentation available

-   [buf](././tls/~/PxfObject#property_buf)
-   [passphrase](././tls/~/PxfObject#property_passphrase)

v

[rootCertificates](././tls/~/rootCertificates "rootCertificates")

An immutable array of strings representing the root certificates (in PEM format) from the bundled Mozilla CA store as supplied by the current Node.js version.

I

[SecureContext](././tls/~/SecureContext "SecureContext")

No documentation available

-   [context](././tls/~/SecureContext#property_context)

I

[SecureContextOptions](././tls/~/SecureContextOptions "SecureContextOptions")

No documentation available

-   [ALPNCallback](././tls/~/SecureContextOptions#property_alpncallback)
-   [allowPartialTrustChain](././tls/~/SecureContextOptions#property_allowpartialtrustchain)
-   [ca](././tls/~/SecureContextOptions#property_ca)
-   [cert](././tls/~/SecureContextOptions#property_cert)
-   [ciphers](././tls/~/SecureContextOptions#property_ciphers)
-   [clientCertEngine](././tls/~/SecureContextOptions#property_clientcertengine)
-   [crl](././tls/~/SecureContextOptions#property_crl)
-   [dhparam](././tls/~/SecureContextOptions#property_dhparam)
-   [ecdhCurve](././tls/~/SecureContextOptions#property_ecdhcurve)
-   [honorCipherOrder](././tls/~/SecureContextOptions#property_honorcipherorder)
-   [key](././tls/~/SecureContextOptions#property_key)
-   [maxVersion](././tls/~/SecureContextOptions#property_maxversion)
-   [minVersion](././tls/~/SecureContextOptions#property_minversion)
-   [passphrase](././tls/~/SecureContextOptions#property_passphrase)
-   [pfx](././tls/~/SecureContextOptions#property_pfx)
-   [privateKeyEngine](././tls/~/SecureContextOptions#property_privatekeyengine)
-   [privateKeyIdentifier](././tls/~/SecureContextOptions#property_privatekeyidentifier)
-   [secureOptions](././tls/~/SecureContextOptions#property_secureoptions)
-   [secureProtocol](././tls/~/SecureContextOptions#property_secureprotocol)
-   [sessionIdContext](././tls/~/SecureContextOptions#property_sessionidcontext)
-   [sessionTimeout](././tls/~/SecureContextOptions#property_sessiontimeout)
-   [sigalgs](././tls/~/SecureContextOptions#property_sigalgs)
-   [ticketKeys](././tls/~/SecureContextOptions#property_ticketkeys)

T

[SecureVersion](././tls/~/SecureVersion "SecureVersion")

No documentation available

c

[Server](././tls/~/Server "Server")

Accepts encrypted connections using TLS or SSL.

-   [addContext](././tls/~/Server#method_addcontext_0)
-   [addListener](././tls/~/Server#method_addlistener_0)
-   [emit](././tls/~/Server#method_emit_0)
-   [getTicketKeys](././tls/~/Server#method_getticketkeys_0)
-   [on](././tls/~/Server#method_on_0)
-   [once](././tls/~/Server#method_once_0)
-   [prependListener](././tls/~/Server#method_prependlistener_0)
-   [prependOnceListener](././tls/~/Server#method_prependoncelistener_0)
-   [setSecureContext](././tls/~/Server#method_setsecurecontext_0)
-   [setTicketKeys](././tls/~/Server#method_setticketkeys_0)

I

[TlsOptions](././tls/~/TlsOptions "TlsOptions")

No documentation available

-   [handshakeTimeout](././tls/~/TlsOptions#property_handshaketimeout)
-   [pskCallback](././tls/~/TlsOptions#method_pskcallback_0)
-   [pskIdentityHint](././tls/~/TlsOptions#property_pskidentityhint)
-   [sessionTimeout](././tls/~/TlsOptions#property_sessiontimeout)
-   [ticketKeys](././tls/~/TlsOptions#property_ticketkeys)

c

[TLSSocket](././tls/~/TLSSocket "TLSSocket")

Performs transparent encryption of written data and all required TLS negotiation.

-   [addListener](././tls/~/TLSSocket#method_addlistener_0)
-   [alpnProtocol](././tls/~/TLSSocket#property_alpnprotocol)
-   [authorizationError](././tls/~/TLSSocket#property_authorizationerror)
-   [authorized](././tls/~/TLSSocket#property_authorized)
-   [disableRenegotiation](././tls/~/TLSSocket#method_disablerenegotiation_0)
-   [emit](././tls/~/TLSSocket#method_emit_0)
-   [enableTrace](././tls/~/TLSSocket#method_enabletrace_0)
-   [encrypted](././tls/~/TLSSocket#property_encrypted)
-   [exportKeyingMaterial](././tls/~/TLSSocket#method_exportkeyingmaterial_0)
-   [getCertificate](././tls/~/TLSSocket#method_getcertificate_0)
-   [getCipher](././tls/~/TLSSocket#method_getcipher_0)
-   [getEphemeralKeyInfo](././tls/~/TLSSocket#method_getephemeralkeyinfo_0)
-   [getFinished](././tls/~/TLSSocket#method_getfinished_0)
-   [getPeerCertificate](././tls/~/TLSSocket#method_getpeercertificate_0)
-   [getPeerFinished](././tls/~/TLSSocket#method_getpeerfinished_0)
-   [getPeerX509Certificate](././tls/~/TLSSocket#method_getpeerx509certificate_0)
-   [getProtocol](././tls/~/TLSSocket#method_getprotocol_0)
-   [getSession](././tls/~/TLSSocket#method_getsession_0)
-   [getSharedSigalgs](././tls/~/TLSSocket#method_getsharedsigalgs_0)
-   [getTLSTicket](././tls/~/TLSSocket#method_gettlsticket_0)
-   [getX509Certificate](././tls/~/TLSSocket#method_getx509certificate_0)
-   [isSessionReused](././tls/~/TLSSocket#method_issessionreused_0)
-   [on](././tls/~/TLSSocket#method_on_0)
-   [once](././tls/~/TLSSocket#method_once_0)
-   [prependListener](././tls/~/TLSSocket#method_prependlistener_0)
-   [prependOnceListener](././tls/~/TLSSocket#method_prependoncelistener_0)
-   [renegotiate](././tls/~/TLSSocket#method_renegotiate_0)
-   [setMaxSendFragment](././tls/~/TLSSocket#method_setmaxsendfragment_0)

I

[TLSSocketOptions](././tls/~/TLSSocketOptions "TLSSocketOptions")

No documentation available

-   [isServer](././tls/~/TLSSocketOptions#property_isserver)
-   [requestOCSP](././tls/~/TLSSocketOptions#property_requestocsp)
-   [server](././tls/~/TLSSocketOptions#property_server)
-   [session](././tls/~/TLSSocketOptions#property_session)

f

[createSecurePair](././tls/~/createSecurePair "createSecurePair")

No documentation available

I

[SecurePair](././tls/~/SecurePair "SecurePair")

No documentation available

-   [cleartext](././tls/~/SecurePair#property_cleartext)
-   [encrypted](././tls/~/SecurePair#property_encrypted)

f

[createTracing](././trace_events/~/createTracing "createTracing")

No documentation available

I

[CreateTracingOptions](././trace_events/~/CreateTracingOptions "CreateTracingOptions")

No documentation available

-   [categories](././trace_events/~/CreateTracingOptions#property_categories)

f

[getEnabledCategories](././trace_events/~/getEnabledCategories "getEnabledCategories")

No documentation available

I

[Tracing](././trace_events/~/Tracing "Tracing")

No documentation available

-   [categories](././trace_events/~/Tracing#property_categories)
-   [disable](././trace_events/~/Tracing#method_disable_0)
-   [enable](././trace_events/~/Tracing#method_enable_0)
-   [enabled](././trace_events/~/Tracing#property_enabled)

The `node:tty` module provides the `tty.ReadStream` and `tty.WriteStream` classes. In most cases, it will not be necessary or possible to use this module directly. However, it can be accessed using:

T

[Direction](././tty/~/Direction "Direction")

\-1 - to the left from cursor 0 - the entire line 1 - to the right from cursor

f

[isatty](././tty/~/isatty "isatty")

The `tty.isatty()` method returns `true` if the given `fd` is associated with a TTY and `false` if it is not, including whenever `fd` is not a non-negative integer.

c

[ReadStream](././tty/~/ReadStream "ReadStream")

Represents the readable side of a TTY. In normal circumstances `process.stdin` will be the only `tty.ReadStream` instance in a Node.js process and there should be no reason to create additional instances.

-   [isRaw](././tty/~/ReadStream#property_israw)
-   [isTTY](././tty/~/ReadStream#property_istty)
-   [setRawMode](././tty/~/ReadStream#method_setrawmode_0)

c

[WriteStream](././tty/~/WriteStream "WriteStream")

Represents the writable side of a TTY. In normal circumstances, `process.stdout` and `process.stderr` will be the only`tty.WriteStream` instances created for a Node.js process and there should be no reason to create additional instances.

-   [addListener](././tty/~/WriteStream#method_addlistener_0)
-   [clearLine](././tty/~/WriteStream#method_clearline_0)
-   [clearScreenDown](././tty/~/WriteStream#method_clearscreendown_0)
-   [columns](././tty/~/WriteStream#property_columns)
-   [cursorTo](././tty/~/WriteStream#method_cursorto_0)
-   [emit](././tty/~/WriteStream#method_emit_0)
-   [getColorDepth](././tty/~/WriteStream#method_getcolordepth_0)
-   [getWindowSize](././tty/~/WriteStream#method_getwindowsize_0)
-   [hasColors](././tty/~/WriteStream#method_hascolors_0)
-   [isTTY](././tty/~/WriteStream#property_istty)
-   [moveCursor](././tty/~/WriteStream#method_movecursor_0)
-   [on](././tty/~/WriteStream#method_on_0)
-   [once](././tty/~/WriteStream#method_once_0)
-   [prependListener](././tty/~/WriteStream#method_prependlistener_0)
-   [prependOnceListener](././tty/~/WriteStream#method_prependoncelistener_0)
-   [rows](././tty/~/WriteStream#property_rows)

The `node:url` module provides utilities for URL resolution and parsing. It can be accessed using:

f

[domainToASCII](././url/~/domainToASCII "domainToASCII")

Returns the [Punycode](https://tools.ietf.org/html/rfc5891#section-4.4) ASCII serialization of the `domain`. If `domain` is an invalid domain, the empty string is returned.

f

[domainToUnicode](././url/~/domainToUnicode "domainToUnicode")

Returns the Unicode serialization of the `domain`. If `domain` is an invalid domain, the empty string is returned.

f

[fileURLToPath](././url/~/fileURLToPath "fileURLToPath")

This function ensures the correct decodings of percent-encoded characters as well as ensuring a cross-platform valid absolute path string.

I

[FileUrlToPathOptions](././url/~/FileUrlToPathOptions "FileUrlToPathOptions")

No documentation available

-   [windows](././url/~/FileUrlToPathOptions#property_windows)

f

[format](././url/~/format "format")

The `url.format()` method returns a formatted URL string derived from `urlObject`.

I

[Global](././url/~/Global "Global")

No documentation available

-   [URL](././url/~/Global#property_url)
-   [URLSearchParams](././url/~/Global#property_urlsearchparams)

f

[parse](././url/~/parse "parse")

No documentation available

f

[pathToFileURL](././url/~/pathToFileURL "pathToFileURL")

This function ensures that `path` is resolved absolutely, and that the URL control characters are correctly encoded when converting into a File URL.

I

[PathToFileUrlOptions](././url/~/PathToFileUrlOptions "PathToFileUrlOptions")

No documentation available

-   [windows](././url/~/PathToFileUrlOptions#property_windows)

f

[resolve](././url/~/resolve "resolve")

The `url.resolve()` method resolves a target URL relative to a base URL in a manner similar to that of a web browser resolving an anchor tag.

c

I

v

[URL](././url/~/URL "URL")

Browser-compatible `URL` class, implemented by following the WHATWG URL Standard. [Examples of parsed URLs](https://url.spec.whatwg.org/#example-url-parsing) may be found in the Standard itself. The `URL` class is also available on the global object.

-   [canParse](././url/~/URL#method_canparse_0)
-   [createObjectURL](././url/~/URL#method_createobjecturl_0)
-   [hash](././url/~/URL#property_hash)
-   [host](././url/~/URL#property_host)
-   [hostname](././url/~/URL#property_hostname)
-   [href](././url/~/URL#property_href)
-   [origin](././url/~/URL#property_origin)
-   [parse](././url/~/URL#method_parse_0)
-   [password](././url/~/URL#property_password)
-   [pathname](././url/~/URL#property_pathname)
-   [port](././url/~/URL#property_port)
-   [protocol](././url/~/URL#property_protocol)
-   [revokeObjectURL](././url/~/URL#method_revokeobjecturl_0)
-   [search](././url/~/URL#property_search)
-   [searchParams](././url/~/URL#property_searchparams)
-   [toJSON](././url/~/URL#method_tojson_0)
-   [toString](././url/~/URL#method_tostring_0)
-   [username](././url/~/URL#property_username)

I

[Url](././url/~/Url "Url")

No documentation available

-   [auth](././url/~/Url#property_auth)
-   [hash](././url/~/Url#property_hash)
-   [host](././url/~/Url#property_host)
-   [hostname](././url/~/Url#property_hostname)
-   [href](././url/~/Url#property_href)
-   [path](././url/~/Url#property_path)
-   [pathname](././url/~/Url#property_pathname)
-   [port](././url/~/Url#property_port)
-   [protocol](././url/~/Url#property_protocol)
-   [query](././url/~/Url#property_query)
-   [search](././url/~/Url#property_search)
-   [slashes](././url/~/Url#property_slashes)

I

[URLFormatOptions](././url/~/URLFormatOptions "URLFormatOptions")

No documentation available

-   [auth](././url/~/URLFormatOptions#property_auth)
-   [fragment](././url/~/URLFormatOptions#property_fragment)
-   [search](././url/~/URLFormatOptions#property_search)
-   [unicode](././url/~/URLFormatOptions#property_unicode)

I

[UrlObject](././url/~/UrlObject "UrlObject")

No documentation available

-   [auth](././url/~/UrlObject#property_auth)
-   [hash](././url/~/UrlObject#property_hash)
-   [host](././url/~/UrlObject#property_host)
-   [hostname](././url/~/UrlObject#property_hostname)
-   [href](././url/~/UrlObject#property_href)
-   [pathname](././url/~/UrlObject#property_pathname)
-   [port](././url/~/UrlObject#property_port)
-   [protocol](././url/~/UrlObject#property_protocol)
-   [query](././url/~/UrlObject#property_query)
-   [search](././url/~/UrlObject#property_search)
-   [slashes](././url/~/UrlObject#property_slashes)

c

I

v

[URLSearchParams](././url/~/URLSearchParams "URLSearchParams")

The `URLSearchParams` API provides read and write access to the query of a `URL`. The `URLSearchParams` class can also be used standalone with one of the four following constructors. The `URLSearchParams` class is also available on the global object.

-   [append](././url/~/URLSearchParams#method_append_0)
-   [delete](././url/~/URLSearchParams#method_delete_0)
-   [entries](././url/~/URLSearchParams#method_entries_0)
-   [forEach](././url/~/URLSearchParams#method_foreach_0)
-   [get](././url/~/URLSearchParams#method_get_0)
-   [getAll](././url/~/URLSearchParams#method_getall_0)
-   [has](././url/~/URLSearchParams#method_has_0)
-   [keys](././url/~/URLSearchParams#method_keys_0)
-   [set](././url/~/URLSearchParams#method_set_0)
-   [size](././url/~/URLSearchParams#property_size)
-   [sort](././url/~/URLSearchParams#method_sort_0)
-   [toString](././url/~/URLSearchParams#method_tostring_0)
-   [values](././url/~/URLSearchParams#method_values_0)

I

[URLSearchParamsIterator](././url/~/URLSearchParamsIterator "URLSearchParamsIterator")

No documentation available

f

[urlToHttpOptions](././url/~/urlToHttpOptions "urlToHttpOptions")

This utility function converts a URL object into an ordinary options object as expected by the `http.request()` and `https.request()` APIs.

I

[UrlWithParsedQuery](././url/~/UrlWithParsedQuery "UrlWithParsedQuery")

No documentation available

-   [query](././url/~/UrlWithParsedQuery#property_query)

I

[UrlWithStringQuery](././url/~/UrlWithStringQuery "UrlWithStringQuery")

No documentation available

-   [query](././url/~/UrlWithStringQuery#property_query)

The `node:util` module supports the needs of Node.js internal APIs. Many of the utilities are useful for application and module developers as well. To access it:

f

[aborted](././util/~/aborted "aborted")

Listens to abort event on the provided `signal` and returns a promise that resolves when the `signal` is aborted. If `resource` is provided, it weakly references the operation's associated object, so if `resource` is garbage collected before the `signal` aborts, then returned promise shall remain pending. This prevents memory leaks in long-running or non-cancelable operations.

T

[ApplyOptionalModifiers](././util/~/ApplyOptionalModifiers "ApplyOptionalModifiers")

No documentation available

T

[BackgroundColors](././util/~/BackgroundColors "BackgroundColors")

No documentation available

f

[callbackify](././util/~/callbackify "callbackify")

Takes an `async` function (or a function that returns a `Promise`) and returns a function following the error-first callback style, i.e. taking an `(err, value) => ...` callback as the last argument. In the callback, the first argument will be the rejection reason (or `null` if the `Promise` resolved), and the second argument will be the resolved value.

I

[CallSiteObject](././util/~/CallSiteObject "CallSiteObject")

No documentation available

-   [columnNumber](././util/~/CallSiteObject#property_columnnumber)
-   [functionName](././util/~/CallSiteObject#property_functionname)
-   [lineNumber](././util/~/CallSiteObject#property_linenumber)
-   [scriptId](././util/~/CallSiteObject#property_scriptid)
-   [scriptName](././util/~/CallSiteObject#property_scriptname)

T

[CustomInspectFunction](././util/~/CustomInspectFunction "CustomInspectFunction")

No documentation available

T

[CustomPromisify](././util/~/CustomPromisify "CustomPromisify")

No documentation available

I

[CustomPromisifyLegacy](././util/~/CustomPromisifyLegacy "CustomPromisifyLegacy")

No documentation available

-   [\_\_promisify\_\_](././util/~/CustomPromisifyLegacy#property___promisify__)

I

[CustomPromisifySymbol](././util/~/CustomPromisifySymbol "CustomPromisifySymbol")

No documentation available

v

[debug](././util/~/debug "debug")

No documentation available

f

[debuglog](././util/~/debuglog "debuglog")

The `util.debuglog()` method is used to create a function that conditionally writes debug messages to `stderr` based on the existence of the `NODE_DEBUG`environment variable. If the `section` name appears within the value of that environment variable, then the returned function operates similar to `console.error()`. If not, then the returned function is a no-op.

I

[DebugLogger](././util/~/DebugLogger "DebugLogger")

No documentation available

-   [enabled](././util/~/DebugLogger#property_enabled)

T

[DebugLoggerFunction](././util/~/DebugLoggerFunction "DebugLoggerFunction")

No documentation available

f

[deprecate](././util/~/deprecate "deprecate")

The `util.deprecate()` method wraps `fn` (which may be a function or class) in such a way that it is marked as deprecated.

I

[EncodeIntoResult](././util/~/EncodeIntoResult "EncodeIntoResult")

No documentation available

-   [read](././util/~/EncodeIntoResult#property_read)
-   [written](././util/~/EncodeIntoResult#property_written)

T

[ExtractOptionValue](././util/~/ExtractOptionValue "ExtractOptionValue")

No documentation available

T

[ForegroundColors](././util/~/ForegroundColors "ForegroundColors")

No documentation available

f

[format](././util/~/format "format")

The `util.format()` method returns a formatted string using the first argument as a `printf`\-like format string which can contain zero or more format specifiers. Each specifier is replaced with the converted value from the corresponding argument. Supported specifiers are:

f

[formatWithOptions](././util/~/formatWithOptions "formatWithOptions")

This function is identical to [format](././util/~/format), except in that it takes an `inspectOptions` argument which specifies options that are passed along to [inspect](././util/~/inspect).

f

[getCallSites](././util/~/getCallSites "getCallSites")

Returns an array of call site objects containing the stack of the caller function.

I

[GetCallSitesOptions](././util/~/GetCallSitesOptions "GetCallSitesOptions")

No documentation available

-   [sourceMap](././util/~/GetCallSitesOptions#property_sourcemap)

f

[getSystemErrorMap](././util/~/getSystemErrorMap "getSystemErrorMap")

No documentation available

f

[getSystemErrorMessage](././util/~/getSystemErrorMessage "getSystemErrorMessage")

Returns the string message for a numeric error code that comes from a Node.js API. The mapping between error codes and string messages is platform-dependent.

f

[getSystemErrorName](././util/~/getSystemErrorName "getSystemErrorName")

Returns the string name for a numeric error code that comes from a Node.js API. The mapping between error codes and error names is platform-dependent. See `Common System Errors` for the names of common errors.

T

[IfDefaultsFalse](././util/~/IfDefaultsFalse "IfDefaultsFalse")

No documentation available

T

[IfDefaultsTrue](././util/~/IfDefaultsTrue "IfDefaultsTrue")

No documentation available

f

[inherits](././util/~/inherits "inherits")

Usage of `util.inherits()` is discouraged. Please use the ES6 `class` and `extends` keywords to get language level inheritance support. Also note that the two styles are [semantically incompatible](https://github.com/nodejs/node/issues/4179).

f

N

[inspect](././util/~/inspect "inspect")

The `util.inspect()` method returns a string representation of `object` that is intended for debugging. The output of `util.inspect` may change at any time and should not be depended upon programmatically. Additional `options` may be passed that alter the result. `util.inspect()` will use the constructor's name and/or `@@toStringTag` to make an identifiable tag for an inspected value.

v

[inspect.colors](././util/~/inspect.colors "inspect.colors")

No documentation available

v

[inspect.custom](././util/~/inspect.custom "inspect.custom")

That can be used to declare custom inspect functions.

v

[inspect.defaultOptions](././util/~/inspect.defaultOptions "inspect.defaultOptions")

No documentation available

v

[inspect.replDefaults](././util/~/inspect.replDefaults "inspect.replDefaults")

Allows changing inspect settings from the repl.

v

[inspect.styles](././util/~/inspect.styles "inspect.styles")

No documentation available

I

[InspectOptions](././util/~/InspectOptions "InspectOptions")

No documentation available

-   [breakLength](././util/~/InspectOptions#property_breaklength)
-   [colors](././util/~/InspectOptions#property_colors)
-   [compact](././util/~/InspectOptions#property_compact)
-   [customInspect](././util/~/InspectOptions#property_custominspect)
-   [depth](././util/~/InspectOptions#property_depth)
-   [getters](././util/~/InspectOptions#property_getters)
-   [maxArrayLength](././util/~/InspectOptions#property_maxarraylength)
-   [maxStringLength](././util/~/InspectOptions#property_maxstringlength)
-   [numericSeparator](././util/~/InspectOptions#property_numericseparator)
-   [showHidden](././util/~/InspectOptions#property_showhidden)
-   [showProxy](././util/~/InspectOptions#property_showproxy)
-   [sorted](././util/~/InspectOptions#property_sorted)

I

[InspectOptionsStylized](././util/~/InspectOptionsStylized "InspectOptionsStylized")

No documentation available

-   [stylize](././util/~/InspectOptionsStylized#method_stylize_0)

f

[isDeepStrictEqual](././util/~/isDeepStrictEqual "isDeepStrictEqual")

Returns `true` if there is deep strict equality between `val1` and `val2`. Otherwise, returns `false`.

c

[MIMEParams](././util/~/MIMEParams "MIMEParams")

No documentation available

-   [delete](././util/~/MIMEParams#method_delete_0)
-   [entries](././util/~/MIMEParams#method_entries_0)
-   [get](././util/~/MIMEParams#method_get_0)
-   [has](././util/~/MIMEParams#method_has_0)
-   [keys](././util/~/MIMEParams#method_keys_0)
-   [set](././util/~/MIMEParams#method_set_0)
-   [values](././util/~/MIMEParams#method_values_0)

c

[MIMEType](././util/~/MIMEType "MIMEType")

No documentation available

-   [essence](././util/~/MIMEType#property_essence)
-   [params](././util/~/MIMEType#property_params)
-   [subtype](././util/~/MIMEType#property_subtype)
-   [toString](././util/~/MIMEType#method_tostring_0)
-   [type](././util/~/MIMEType#property_type)

T

[Modifiers](././util/~/Modifiers "Modifiers")

No documentation available

T

[OptionToken](././util/~/OptionToken "OptionToken")

No documentation available

f

[parseArgs](././util/~/parseArgs "parseArgs")

Provides a higher level API for command-line argument parsing than interacting with `process.argv` directly. Takes a specification for the expected arguments and returns a structured object with the parsed options and positionals.

I

[ParseArgsConfig](././util/~/ParseArgsConfig "ParseArgsConfig")

No documentation available

-   [allowNegative](././util/~/ParseArgsConfig#property_allownegative)
-   [allowPositionals](././util/~/ParseArgsConfig#property_allowpositionals)
-   [args](././util/~/ParseArgsConfig#property_args)
-   [options](././util/~/ParseArgsConfig#property_options)
-   [strict](././util/~/ParseArgsConfig#property_strict)
-   [tokens](././util/~/ParseArgsConfig#property_tokens)

I

[ParseArgsOptionDescriptor](././util/~/ParseArgsOptionDescriptor "ParseArgsOptionDescriptor")

No documentation available

-   [default](././util/~/ParseArgsOptionDescriptor#property_default)
-   [multiple](././util/~/ParseArgsOptionDescriptor#property_multiple)
-   [short](././util/~/ParseArgsOptionDescriptor#property_short)
-   [type](././util/~/ParseArgsOptionDescriptor#property_type)

I

[ParseArgsOptionsConfig](././util/~/ParseArgsOptionsConfig "ParseArgsOptionsConfig")

No documentation available

T

[ParseArgsOptionsType](././util/~/ParseArgsOptionsType "ParseArgsOptionsType")

Type of argument used in [parseArgs](././util/~/parseArgs).

T

[ParsedOptionToken](././util/~/ParsedOptionToken "ParsedOptionToken")

No documentation available

T

[ParsedPositionals](././util/~/ParsedPositionals "ParsedPositionals")

No documentation available

T

[ParsedPositionalToken](././util/~/ParsedPositionalToken "ParsedPositionalToken")

No documentation available

T

[ParsedResults](././util/~/ParsedResults "ParsedResults")

No documentation available

T

[ParsedTokens](././util/~/ParsedTokens "ParsedTokens")

No documentation available

T

[ParsedValues](././util/~/ParsedValues "ParsedValues")

No documentation available

f

[parseEnv](././util/~/parseEnv "parseEnv")

Stability: 1.1 - Active development Given an example `.env` file:

T

[PreciseParsedResults](././util/~/PreciseParsedResults "PreciseParsedResults")

No documentation available

T

[PreciseTokenForOptions](././util/~/PreciseTokenForOptions "PreciseTokenForOptions")

No documentation available

f

N

[promisify](././util/~/promisify "promisify")

Takes a function following the common error-first callback style, i.e. taking an `(err, value) => ...` callback as the last argument, and returns a version that returns promises.

v

[promisify.custom](././util/~/promisify.custom "promisify.custom")

That can be used to declare custom promisified variants of functions.

f

[stripVTControlCharacters](././util/~/stripVTControlCharacters "stripVTControlCharacters")

Returns `str` with any ANSI escape codes removed.

T

[Style](././util/~/Style "Style")

No documentation available

f

[styleText](././util/~/styleText "styleText")

This function returns a formatted text considering the `format` passed.

c

v

[TextDecoder](././util/~/TextDecoder "TextDecoder")

An implementation of the [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/) `TextDecoder` API.

-   [decode](././util/~/TextDecoder#method_decode_0)
-   [encoding](././util/~/TextDecoder#property_encoding)
-   [fatal](././util/~/TextDecoder#property_fatal)
-   [ignoreBOM](././util/~/TextDecoder#property_ignorebom)

c

v

[TextEncoder](././util/~/TextEncoder "TextEncoder")

An implementation of the [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/) `TextEncoder` API. All instances of `TextEncoder` only support UTF-8 encoding.

-   [encode](././util/~/TextEncoder#method_encode_0)
-   [encodeInto](././util/~/TextEncoder#method_encodeinto_0)
-   [encoding](././util/~/TextEncoder#property_encoding)

T

[Token](././util/~/Token "Token")

No documentation available

T

[TokenForOptions](././util/~/TokenForOptions "TokenForOptions")

No documentation available

f

[toUSVString](././util/~/toUSVString "toUSVString")

Returns the `string` after replacing any surrogate code points (or equivalently, any unpaired surrogate code units) with the Unicode "replacement character" U+FFFD.

f

[transferableAbortController](././util/~/transferableAbortController "transferableAbortController")

No documentation available

f

[transferableAbortSignal](././util/~/transferableAbortSignal "transferableAbortSignal")

No documentation available

N

[types](././util/~/types "types")

No documentation available

f

[isArray](././util/~/isArray "isArray")

Alias for [`Array.isArray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray).

f

[isBoolean](././util/~/isBoolean "isBoolean")

Returns `true` if the given `object` is a `Boolean`. Otherwise, returns `false`.

f

[isBuffer](././util/~/isBuffer "isBuffer")

Returns `true` if the given `object` is a `Buffer`. Otherwise, returns `false`.

f

[isDate](././util/~/isDate "isDate")

Returns `true` if the given `object` is a `Date`. Otherwise, returns `false`.

f

[isError](././util/~/isError "isError")

Returns `true` if the given `object` is an `Error`. Otherwise, returns `false`.

f

[isFunction](././util/~/isFunction "isFunction")

Returns `true` if the given `object` is a `Function`. Otherwise, returns `false`.

f

[isNull](././util/~/isNull "isNull")

Returns `true` if the given `object` is strictly `null`. Otherwise, returns`false`.

f

[isNullOrUndefined](././util/~/isNullOrUndefined "isNullOrUndefined")

Returns `true` if the given `object` is `null` or `undefined`. Otherwise, returns `false`.

f

[isNumber](././util/~/isNumber "isNumber")

Returns `true` if the given `object` is a `Number`. Otherwise, returns `false`.

f

[isObject](././util/~/isObject "isObject")

Returns `true` if the given `object` is strictly an `Object`**and** not a`Function` (even though functions are objects in JavaScript). Otherwise, returns `false`.

f

[isPrimitive](././util/~/isPrimitive "isPrimitive")

Returns `true` if the given `object` is a primitive type. Otherwise, returns`false`.

f

[isRegExp](././util/~/isRegExp "isRegExp")

Returns `true` if the given `object` is a `RegExp`. Otherwise, returns `false`.

f

[isString](././util/~/isString "isString")

Returns `true` if the given `object` is a `string`. Otherwise, returns `false`.

f

[isSymbol](././util/~/isSymbol "isSymbol")

Returns `true` if the given `object` is a `Symbol`. Otherwise, returns `false`.

f

[isUndefined](././util/~/isUndefined "isUndefined")

Returns `true` if the given `object` is `undefined`. Otherwise, returns `false`.

f

[log](././util/~/log "log")

The `util.log()` method prints the given `string` to `stdout` with an included timestamp.

f

[isAnyArrayBuffer](././util/types/~/isAnyArrayBuffer "isAnyArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) or [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance.

f

[isArgumentsObject](././util/types/~/isArgumentsObject "isArgumentsObject")

Returns `true` if the value is an `arguments` object.

f

[isArrayBuffer](././util/types/~/isArrayBuffer "isArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instance. This does _not_ include [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[isArrayBufferView](././util/types/~/isArrayBufferView "isArrayBufferView")

Returns `true` if the value is an instance of one of the [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) views, such as typed array objects or [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). Equivalent to [`ArrayBuffer.isView()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/isView).

f

[isAsyncFunction](././util/types/~/isAsyncFunction "isAsyncFunction")

Returns `true` if the value is an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function). This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[isBigInt64Array](././util/types/~/isBigInt64Array "isBigInt64Array")

Returns `true` if the value is a `BigInt64Array` instance.

f

[isBigIntObject](././util/types/~/isBigIntObject "isBigIntObject")

Returns `true` if the value is a BigInt object, e.g. created by `Object(BigInt(123))`.

f

[isBigUint64Array](././util/types/~/isBigUint64Array "isBigUint64Array")

Returns `true` if the value is a `BigUint64Array` instance.

f

[isBooleanObject](././util/types/~/isBooleanObject "isBooleanObject")

Returns `true` if the value is a boolean object, e.g. created by `new Boolean()`.

f

[isBoxedPrimitive](././util/types/~/isBoxedPrimitive "isBoxedPrimitive")

Returns `true` if the value is any boxed primitive object, e.g. created by `new Boolean()`, `new String()` or `Object(Symbol())`.

f

[isCryptoKey](././util/types/~/isCryptoKey "isCryptoKey")

Returns `true` if `value` is a `CryptoKey`, `false` otherwise.

f

[isDataView](././util/types/~/isDataView "isDataView")

Returns `true` if the value is a built-in [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) instance.

f

[isDate](././util/types/~/isDate "isDate")

Returns `true` if the value is a built-in [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) instance.

f

[isExternal](././util/types/~/isExternal "isExternal")

Returns `true` if the value is a native `External` value.

f

[isFloat32Array](././util/types/~/isFloat32Array "isFloat32Array")

Returns `true` if the value is a built-in [`Float32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) instance.

f

[isFloat64Array](././util/types/~/isFloat64Array "isFloat64Array")

Returns `true` if the value is a built-in [`Float64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) instance.

f

[isGeneratorFunction](././util/types/~/isGeneratorFunction "isGeneratorFunction")

Returns `true` if the value is a generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[isGeneratorObject](././util/types/~/isGeneratorObject "isGeneratorObject")

Returns `true` if the value is a generator object as returned from a built-in generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[isInt16Array](././util/types/~/isInt16Array "isInt16Array")

Returns `true` if the value is a built-in [`Int16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array) instance.

f

[isInt32Array](././util/types/~/isInt32Array "isInt32Array")

Returns `true` if the value is a built-in [`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array) instance.

f

[isInt8Array](././util/types/~/isInt8Array "isInt8Array")

Returns `true` if the value is a built-in [`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array) instance.

f

[isKeyObject](././util/types/~/isKeyObject "isKeyObject")

Returns `true` if `value` is a `KeyObject`, `false` otherwise.

f

[isMap](././util/types/~/isMap "isMap")

Returns `true` if the value is a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[isMapIterator](././util/types/~/isMapIterator "isMapIterator")

Returns `true` if the value is an iterator returned for a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[isModuleNamespaceObject](././util/types/~/isModuleNamespaceObject "isModuleNamespaceObject")

Returns `true` if the value is an instance of a [Module Namespace Object](https://tc39.github.io/ecma262/#sec-module-namespace-exotic-objects).

f

[isNativeError](././util/types/~/isNativeError "isNativeError")

Returns `true` if the value was returned by the constructor of a [built-in `Error` type](https://tc39.es/ecma262/#sec-error-objects).

f

[isNumberObject](././util/types/~/isNumberObject "isNumberObject")

Returns `true` if the value is a number object, e.g. created by `new Number()`.

f

[isPromise](././util/types/~/isPromise "isPromise")

Returns `true` if the value is a built-in [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

f

[isProxy](././util/types/~/isProxy "isProxy")

Returns `true` if the value is a [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) instance.

f

[isRegExp](././util/types/~/isRegExp "isRegExp")

Returns `true` if the value is a regular expression object.

f

[isSet](././util/types/~/isSet "isSet")

Returns `true` if the value is a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[isSetIterator](././util/types/~/isSetIterator "isSetIterator")

Returns `true` if the value is an iterator returned for a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[isSharedArrayBuffer](././util/types/~/isSharedArrayBuffer "isSharedArrayBuffer")

Returns `true` if the value is a built-in [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance. This does _not_ include [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[isStringObject](././util/types/~/isStringObject "isStringObject")

Returns `true` if the value is a string object, e.g. created by `new String()`.

f

[isSymbolObject](././util/types/~/isSymbolObject "isSymbolObject")

Returns `true` if the value is a symbol object, created by calling `Object()` on a `Symbol` primitive.

f

[isTypedArray](././util/types/~/isTypedArray "isTypedArray")

Returns `true` if the value is a built-in [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) instance.

f

[isUint16Array](././util/types/~/isUint16Array "isUint16Array")

Returns `true` if the value is a built-in [`Uint16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array) instance.

f

[isUint32Array](././util/types/~/isUint32Array "isUint32Array")

Returns `true` if the value is a built-in [`Uint32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array) instance.

f

[isUint8Array](././util/types/~/isUint8Array "isUint8Array")

Returns `true` if the value is a built-in [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instance.

f

[isUint8ClampedArray](././util/types/~/isUint8ClampedArray "isUint8ClampedArray")

Returns `true` if the value is a built-in [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) instance.

f

[isWeakMap](././util/types/~/isWeakMap "isWeakMap")

Returns `true` if the value is a built-in [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) instance.

f

[isWeakSet](././util/types/~/isWeakSet "isWeakSet")

Returns `true` if the value is a built-in [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) instance.

f

[types.isAnyArrayBuffer](././util/types/~/types.isAnyArrayBuffer "types.isAnyArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) or [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance.

f

[types.isArgumentsObject](././util/types/~/types.isArgumentsObject "types.isArgumentsObject")

Returns `true` if the value is an `arguments` object.

f

[types.isArrayBuffer](././util/types/~/types.isArrayBuffer "types.isArrayBuffer")

Returns `true` if the value is a built-in [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instance. This does _not_ include [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[types.isArrayBufferView](././util/types/~/types.isArrayBufferView "types.isArrayBufferView")

Returns `true` if the value is an instance of one of the [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) views, such as typed array objects or [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView). Equivalent to [`ArrayBuffer.isView()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/isView).

f

[types.isAsyncFunction](././util/types/~/types.isAsyncFunction "types.isAsyncFunction")

Returns `true` if the value is an [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function). This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[types.isBigInt64Array](././util/types/~/types.isBigInt64Array "types.isBigInt64Array")

Returns `true` if the value is a `BigInt64Array` instance.

f

[types.isBigIntObject](././util/types/~/types.isBigIntObject "types.isBigIntObject")

Returns `true` if the value is a BigInt object, e.g. created by `Object(BigInt(123))`.

f

[types.isBigUint64Array](././util/types/~/types.isBigUint64Array "types.isBigUint64Array")

Returns `true` if the value is a `BigUint64Array` instance.

f

[types.isBooleanObject](././util/types/~/types.isBooleanObject "types.isBooleanObject")

Returns `true` if the value is a boolean object, e.g. created by `new Boolean()`.

f

[types.isBoxedPrimitive](././util/types/~/types.isBoxedPrimitive "types.isBoxedPrimitive")

Returns `true` if the value is any boxed primitive object, e.g. created by `new Boolean()`, `new String()` or `Object(Symbol())`.

f

[types.isCryptoKey](././util/types/~/types.isCryptoKey "types.isCryptoKey")

Returns `true` if `value` is a `CryptoKey`, `false` otherwise.

f

[types.isDataView](././util/types/~/types.isDataView "types.isDataView")

Returns `true` if the value is a built-in [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView) instance.

f

[types.isDate](././util/types/~/types.isDate "types.isDate")

Returns `true` if the value is a built-in [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) instance.

f

[types.isExternal](././util/types/~/types.isExternal "types.isExternal")

Returns `true` if the value is a native `External` value.

f

[types.isFloat32Array](././util/types/~/types.isFloat32Array "types.isFloat32Array")

Returns `true` if the value is a built-in [`Float32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) instance.

f

[types.isFloat64Array](././util/types/~/types.isFloat64Array "types.isFloat64Array")

Returns `true` if the value is a built-in [`Float64Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) instance.

f

[types.isGeneratorFunction](././util/types/~/types.isGeneratorFunction "types.isGeneratorFunction")

Returns `true` if the value is a generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[types.isGeneratorObject](././util/types/~/types.isGeneratorObject "types.isGeneratorObject")

Returns `true` if the value is a generator object as returned from a built-in generator function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used.

f

[types.isInt16Array](././util/types/~/types.isInt16Array "types.isInt16Array")

Returns `true` if the value is a built-in [`Int16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array) instance.

f

[types.isInt32Array](././util/types/~/types.isInt32Array "types.isInt32Array")

Returns `true` if the value is a built-in [`Int32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array) instance.

f

[types.isInt8Array](././util/types/~/types.isInt8Array "types.isInt8Array")

Returns `true` if the value is a built-in [`Int8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array) instance.

f

[types.isKeyObject](././util/types/~/types.isKeyObject "types.isKeyObject")

Returns `true` if `value` is a `KeyObject`, `false` otherwise.

f

[types.isMap](././util/types/~/types.isMap "types.isMap")

Returns `true` if the value is a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[types.isMapIterator](././util/types/~/types.isMapIterator "types.isMapIterator")

Returns `true` if the value is an iterator returned for a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance.

f

[types.isModuleNamespaceObject](././util/types/~/types.isModuleNamespaceObject "types.isModuleNamespaceObject")

Returns `true` if the value is an instance of a [Module Namespace Object](https://tc39.github.io/ecma262/#sec-module-namespace-exotic-objects).

f

[types.isNativeError](././util/types/~/types.isNativeError "types.isNativeError")

Returns `true` if the value was returned by the constructor of a [built-in `Error` type](https://tc39.es/ecma262/#sec-error-objects).

f

[types.isNumberObject](././util/types/~/types.isNumberObject "types.isNumberObject")

Returns `true` if the value is a number object, e.g. created by `new Number()`.

f

[types.isPromise](././util/types/~/types.isPromise "types.isPromise")

Returns `true` if the value is a built-in [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

f

[types.isProxy](././util/types/~/types.isProxy "types.isProxy")

Returns `true` if the value is a [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) instance.

f

[types.isRegExp](././util/types/~/types.isRegExp "types.isRegExp")

Returns `true` if the value is a regular expression object.

f

[types.isSet](././util/types/~/types.isSet "types.isSet")

Returns `true` if the value is a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[types.isSetIterator](././util/types/~/types.isSetIterator "types.isSetIterator")

Returns `true` if the value is an iterator returned for a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) instance.

f

[types.isSharedArrayBuffer](././util/types/~/types.isSharedArrayBuffer "types.isSharedArrayBuffer")

Returns `true` if the value is a built-in [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) instance. This does _not_ include [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) instances. Usually, it is desirable to test for both; See `util.types.isAnyArrayBuffer()` for that.

f

[types.isStringObject](././util/types/~/types.isStringObject "types.isStringObject")

Returns `true` if the value is a string object, e.g. created by `new String()`.

f

[types.isSymbolObject](././util/types/~/types.isSymbolObject "types.isSymbolObject")

Returns `true` if the value is a symbol object, created by calling `Object()` on a `Symbol` primitive.

f

[types.isTypedArray](././util/types/~/types.isTypedArray "types.isTypedArray")

Returns `true` if the value is a built-in [`TypedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray) instance.

f

[types.isUint16Array](././util/types/~/types.isUint16Array "types.isUint16Array")

Returns `true` if the value is a built-in [`Uint16Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array) instance.

f

[types.isUint32Array](././util/types/~/types.isUint32Array "types.isUint32Array")

Returns `true` if the value is a built-in [`Uint32Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array) instance.

f

[types.isUint8Array](././util/types/~/types.isUint8Array "types.isUint8Array")

Returns `true` if the value is a built-in [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) instance.

f

[types.isUint8ClampedArray](././util/types/~/types.isUint8ClampedArray "types.isUint8ClampedArray")

Returns `true` if the value is a built-in [`Uint8ClampedArray`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) instance.

f

[types.isWeakMap](././util/types/~/types.isWeakMap "types.isWeakMap")

Returns `true` if the value is a built-in [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) instance.

f

[types.isWeakSet](././util/types/~/types.isWeakSet "types.isWeakSet")

Returns `true` if the value is a built-in [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) instance.

I

[After](././v8/~/After "After")

Called immediately after a promise continuation executes. This may be after a `then()`, `catch()`, or `finally()` handler or before an await after another await.

I

[Before](././v8/~/Before "Before")

Called before a promise continuation executes. This can be in the form of `then()`, `catch()`, or `finally()` handlers or an await resuming.

f

[cachedDataVersionTag](././v8/~/cachedDataVersionTag "cachedDataVersionTag")

Returns an integer representing a version tag derived from the V8 version, command-line flags, and detected CPU features. This is useful for determining whether a `vm.Script` `cachedData` buffer is compatible with this instance of V8.

c

[DefaultDeserializer](././v8/~/DefaultDeserializer "DefaultDeserializer")

A subclass of `Deserializer` corresponding to the format written by `DefaultSerializer`.

c

[DefaultSerializer](././v8/~/DefaultSerializer "DefaultSerializer")

A subclass of `Serializer` that serializes `TypedArray`(in particular `Buffer`) and `DataView` objects as host objects, and only stores the part of their underlying `ArrayBuffer`s that they are referring to.

f

[deserialize](././v8/~/deserialize "deserialize")

Uses a `DefaultDeserializer` with default options to read a JS value from a buffer.

c

[Deserializer](././v8/~/Deserializer "Deserializer")

No documentation available

-   [getWireFormatVersion](././v8/~/Deserializer#method_getwireformatversion_0)
-   [readDouble](././v8/~/Deserializer#method_readdouble_0)
-   [readHeader](././v8/~/Deserializer#method_readheader_0)
-   [readRawBytes](././v8/~/Deserializer#method_readrawbytes_0)
-   [readUint32](././v8/~/Deserializer#method_readuint32_0)
-   [readUint64](././v8/~/Deserializer#method_readuint64_0)
-   [readValue](././v8/~/Deserializer#method_readvalue_0)
-   [transferArrayBuffer](././v8/~/Deserializer#method_transferarraybuffer_0)

T

[DoesZapCodeSpaceFlag](././v8/~/DoesZapCodeSpaceFlag "DoesZapCodeSpaceFlag")

No documentation available

c

[GCProfiler](././v8/~/GCProfiler "GCProfiler")

This API collects GC data in current thread.

-   [start](././v8/~/GCProfiler#method_start_0)
-   [stop](././v8/~/GCProfiler#method_stop_0)

I

[GCProfilerResult](././v8/~/GCProfilerResult "GCProfilerResult")

No documentation available

-   [endTime](././v8/~/GCProfilerResult#property_endtime)
-   [startTime](././v8/~/GCProfilerResult#property_starttime)
-   [statistics](././v8/~/GCProfilerResult#property_statistics)
-   [version](././v8/~/GCProfilerResult#property_version)

f

[getHeapCodeStatistics](././v8/~/getHeapCodeStatistics "getHeapCodeStatistics")

Get statistics about code and its metadata in the heap, see V8 [`GetHeapCodeAndMetadataStatistics`](https://v8docs.nodesource.com/node-13.2/d5/dda/classv8_1_1_isolate.html#a6079122af17612ef54ef3348ce170866) API. Returns an object with the following properties:

f

[getHeapSnapshot](././v8/~/getHeapSnapshot "getHeapSnapshot")

Generates a snapshot of the current V8 heap and returns a Readable Stream that may be used to read the JSON serialized representation. This JSON stream format is intended to be used with tools such as Chrome DevTools. The JSON schema is undocumented and specific to the V8 engine. Therefore, the schema may change from one version of V8 to the next.

f

[getHeapSpaceStatistics](././v8/~/getHeapSpaceStatistics "getHeapSpaceStatistics")

Returns statistics about the V8 heap spaces, i.e. the segments which make up the V8 heap. Neither the ordering of heap spaces, nor the availability of a heap space can be guaranteed as the statistics are provided via the V8 [`GetHeapSpaceStatistics`](https://v8docs.nodesource.com/node-13.2/d5/dda/classv8_1_1_isolate.html#ac673576f24fdc7a33378f8f57e1d13a4) function and may change from one V8 version to the next.

f

[getHeapStatistics](././v8/~/getHeapStatistics "getHeapStatistics")

Returns an object with the following properties:

I

[HeapCodeStatistics](././v8/~/HeapCodeStatistics "HeapCodeStatistics")

No documentation available

-   [bytecode\_and\_metadata\_size](././v8/~/HeapCodeStatistics#property_bytecode_and_metadata_size)
-   [code\_and\_metadata\_size](././v8/~/HeapCodeStatistics#property_code_and_metadata_size)
-   [external\_script\_source\_size](././v8/~/HeapCodeStatistics#property_external_script_source_size)

I

[HeapInfo](././v8/~/HeapInfo "HeapInfo")

No documentation available

-   [does\_zap\_garbage](././v8/~/HeapInfo#property_does_zap_garbage)
-   [external\_memory](././v8/~/HeapInfo#property_external_memory)
-   [heap\_size\_limit](././v8/~/HeapInfo#property_heap_size_limit)
-   [malloced\_memory](././v8/~/HeapInfo#property_malloced_memory)
-   [number\_of\_detached\_contexts](././v8/~/HeapInfo#property_number_of_detached_contexts)
-   [number\_of\_native\_contexts](././v8/~/HeapInfo#property_number_of_native_contexts)
-   [peak\_malloced\_memory](././v8/~/HeapInfo#property_peak_malloced_memory)
-   [total\_available\_size](././v8/~/HeapInfo#property_total_available_size)
-   [total\_global\_handles\_size](././v8/~/HeapInfo#property_total_global_handles_size)
-   [total\_heap\_size](././v8/~/HeapInfo#property_total_heap_size)
-   [total\_heap\_size\_executable](././v8/~/HeapInfo#property_total_heap_size_executable)
-   [total\_physical\_size](././v8/~/HeapInfo#property_total_physical_size)
-   [used\_global\_handles\_size](././v8/~/HeapInfo#property_used_global_handles_size)
-   [used\_heap\_size](././v8/~/HeapInfo#property_used_heap_size)

I

[HeapSnapshotOptions](././v8/~/HeapSnapshotOptions "HeapSnapshotOptions")

No documentation available

-   [exposeInternals](././v8/~/HeapSnapshotOptions#property_exposeinternals)
-   [exposeNumericValues](././v8/~/HeapSnapshotOptions#property_exposenumericvalues)

I

[HeapSpaceInfo](././v8/~/HeapSpaceInfo "HeapSpaceInfo")

No documentation available

-   [physical\_space\_size](././v8/~/HeapSpaceInfo#property_physical_space_size)
-   [space\_available\_size](././v8/~/HeapSpaceInfo#property_space_available_size)
-   [space\_name](././v8/~/HeapSpaceInfo#property_space_name)
-   [space\_size](././v8/~/HeapSpaceInfo#property_space_size)
-   [space\_used\_size](././v8/~/HeapSpaceInfo#property_space_used_size)

I

[HeapSpaceStatistics](././v8/~/HeapSpaceStatistics "HeapSpaceStatistics")

No documentation available

-   [physicalSpaceSize](././v8/~/HeapSpaceStatistics#property_physicalspacesize)
-   [spaceAvailableSize](././v8/~/HeapSpaceStatistics#property_spaceavailablesize)
-   [spaceName](././v8/~/HeapSpaceStatistics#property_spacename)
-   [spaceSize](././v8/~/HeapSpaceStatistics#property_spacesize)
-   [spaceUsedSize](././v8/~/HeapSpaceStatistics#property_spaceusedsize)

I

[HeapStatistics](././v8/~/HeapStatistics "HeapStatistics")

No documentation available

-   [externalMemory](././v8/~/HeapStatistics#property_externalmemory)
-   [heapSizeLimit](././v8/~/HeapStatistics#property_heapsizelimit)
-   [mallocedMemory](././v8/~/HeapStatistics#property_mallocedmemory)
-   [peakMallocedMemory](././v8/~/HeapStatistics#property_peakmallocedmemory)
-   [totalAvailableSize](././v8/~/HeapStatistics#property_totalavailablesize)
-   [totalGlobalHandlesSize](././v8/~/HeapStatistics#property_totalglobalhandlessize)
-   [totalHeapSize](././v8/~/HeapStatistics#property_totalheapsize)
-   [totalHeapSizeExecutable](././v8/~/HeapStatistics#property_totalheapsizeexecutable)
-   [totalPhysicalSize](././v8/~/HeapStatistics#property_totalphysicalsize)
-   [usedGlobalHandlesSize](././v8/~/HeapStatistics#property_usedglobalhandlessize)
-   [usedHeapSize](././v8/~/HeapStatistics#property_usedheapsize)

I

[HookCallbacks](././v8/~/HookCallbacks "HookCallbacks")

Key events in the lifetime of a promise have been categorized into four areas: creation of a promise, before/after a continuation handler is called or around an await, and when the promise resolves or rejects.

-   [after](././v8/~/HookCallbacks#property_after)
-   [before](././v8/~/HookCallbacks#property_before)
-   [init](././v8/~/HookCallbacks#property_init)
-   [settled](././v8/~/HookCallbacks#property_settled)

I

[Init](././v8/~/Init "Init")

Called when a promise is constructed. This does not mean that corresponding before/after events will occur, only that the possibility exists. This will happen if a promise is created without ever getting a continuation.

I

[PromiseHooks](././v8/~/PromiseHooks "PromiseHooks")

No documentation available

-   [createHook](././v8/~/PromiseHooks#property_createhook)
-   [onAfter](././v8/~/PromiseHooks#property_onafter)
-   [onBefore](././v8/~/PromiseHooks#property_onbefore)
-   [onInit](././v8/~/PromiseHooks#property_oninit)
-   [onSettled](././v8/~/PromiseHooks#property_onsettled)

v

[promiseHooks](././v8/~/promiseHooks "promiseHooks")

The `promiseHooks` interface can be used to track promise lifecycle events.

f

[queryObjects](././v8/~/queryObjects "queryObjects")

This is similar to the [`queryObjects()` console API](https://developer.chrome.com/docs/devtools/console/utilities#queryObjects-function) provided by the Chromium DevTools console. It can be used to search for objects that have the matching constructor on its prototype chain in the heap after a full garbage collection, which can be useful for memory leak regression tests. To avoid surprising results, users should avoid using this API on constructors whose implementation they don't control, or on constructors that can be invoked by other parties in the application.

f

[serialize](././v8/~/serialize "serialize")

Uses a `DefaultSerializer` to serialize `value` into a buffer.

c

[Serializer](././v8/~/Serializer "Serializer")

No documentation available

-   [releaseBuffer](././v8/~/Serializer#method_releasebuffer_0)
-   [transferArrayBuffer](././v8/~/Serializer#method_transferarraybuffer_0)
-   [writeDouble](././v8/~/Serializer#method_writedouble_0)
-   [writeHeader](././v8/~/Serializer#method_writeheader_0)
-   [writeRawBytes](././v8/~/Serializer#method_writerawbytes_0)
-   [writeUint32](././v8/~/Serializer#method_writeuint32_0)
-   [writeUint64](././v8/~/Serializer#method_writeuint64_0)
-   [writeValue](././v8/~/Serializer#method_writevalue_0)

f

[setFlagsFromString](././v8/~/setFlagsFromString "setFlagsFromString")

The `v8.setFlagsFromString()` method can be used to programmatically set V8 command-line flags. This method should be used with care. Changing settings after the VM has started may result in unpredictable behavior, including crashes and data loss; or it may simply do nothing.

f

[setHeapSnapshotNearHeapLimit](././v8/~/setHeapSnapshotNearHeapLimit "setHeapSnapshotNearHeapLimit")

The API is a no-op if `--heapsnapshot-near-heap-limit` is already set from the command line or the API is called more than once. `limit` must be a positive integer. See [`--heapsnapshot-near-heap-limit`](https://nodejs.org/docs/latest-v22.x/api/cli.html#--heapsnapshot-near-heap-limitmax_count) for more information.

I

[Settled](././v8/~/Settled "Settled")

Called when the promise receives a resolution or rejection value. This may occur synchronously in the case of Promise.resolve() or Promise.reject().

I

[StartupSnapshot](././v8/~/StartupSnapshot "StartupSnapshot")

No documentation available

-   [addDeserializeCallback](././v8/~/StartupSnapshot#method_adddeserializecallback_0)
-   [addSerializeCallback](././v8/~/StartupSnapshot#method_addserializecallback_0)
-   [isBuildingSnapshot](././v8/~/StartupSnapshot#method_isbuildingsnapshot_0)
-   [setDeserializeMainFunction](././v8/~/StartupSnapshot#method_setdeserializemainfunction_0)

v

[startupSnapshot](././v8/~/startupSnapshot "startupSnapshot")

The `v8.startupSnapshot` interface can be used to add serialization and deserialization hooks for custom startup snapshots.

T

[StartupSnapshotCallbackFn](././v8/~/StartupSnapshotCallbackFn "StartupSnapshotCallbackFn")

No documentation available

f

[stopCoverage](././v8/~/stopCoverage "stopCoverage")

The `v8.stopCoverage()` method allows the user to stop the coverage collection started by `NODE_V8_COVERAGE`, so that V8 can release the execution count records and optimize code. This can be used in conjunction with [takeCoverage](././v8/~/takeCoverage) if the user wants to collect the coverage on demand.

f

[takeCoverage](././v8/~/takeCoverage "takeCoverage")

The `v8.takeCoverage()` method allows the user to write the coverage started by `NODE_V8_COVERAGE` to disk on demand. This method can be invoked multiple times during the lifetime of the process. Each time the execution counter will be reset and a new coverage report will be written to the directory specified by `NODE_V8_COVERAGE`.

f

[writeHeapSnapshot](././v8/~/writeHeapSnapshot "writeHeapSnapshot")

Generates a snapshot of the current V8 heap and writes it to a JSON file. This file is intended to be used with tools such as Chrome DevTools. The JSON schema is undocumented and specific to the V8 engine, and may change from one version of V8 to the next.

The `node:vm` module enables compiling and running code within V8 Virtual Machine contexts.

I

[BaseOptions](././vm/~/BaseOptions "BaseOptions")

No documentation available

-   [columnOffset](././vm/~/BaseOptions#property_columnoffset)
-   [filename](././vm/~/BaseOptions#property_filename)
-   [lineOffset](././vm/~/BaseOptions#property_lineoffset)

f

[compileFunction](././vm/~/compileFunction "compileFunction")

Compiles the given code into the provided context (if no context is supplied, the current context is used), and returns it wrapped inside a function with the given `params`.

I

[CompileFunctionOptions](././vm/~/CompileFunctionOptions "CompileFunctionOptions")

No documentation available

-   [cachedData](././vm/~/CompileFunctionOptions#property_cacheddata)
-   [contextExtensions](././vm/~/CompileFunctionOptions#property_contextextensions)
-   [parsingContext](././vm/~/CompileFunctionOptions#property_parsingcontext)
-   [produceCachedData](././vm/~/CompileFunctionOptions#property_producecacheddata)

N

[constants](././vm/~/constants "constants")

Returns an object containing commonly used constants for VM operations.

v

[constants.DONT\_CONTEXTIFY](././vm/~/constants.DONT_CONTEXTIFY "constants.DONT_CONTEXTIFY")

This constant, when used as the `contextObject` argument in vm APIs, instructs Node.js to create a context without wrapping its global object with another object in a Node.js-specific manner. As a result, the `globalThis` value inside the new context would behave more closely to an ordinary one.

v

[constants.USE\_MAIN\_CONTEXT\_DEFAULT\_LOADER](././vm/~/constants.USE_MAIN_CONTEXT_DEFAULT_LOADER "constants.USE_MAIN_CONTEXT_DEFAULT_LOADER")

A constant that can be used as the `importModuleDynamically` option to `vm.Script` and `vm.compileFunction()` so that Node.js uses the default ESM loader from the main context to load the requested module.

I

[Context](././vm/~/Context "Context")

No documentation available

f

[createContext](././vm/~/createContext "createContext")

No documentation available

I

[CreateContextOptions](././vm/~/CreateContextOptions "CreateContextOptions")

No documentation available

-   [codeGeneration](././vm/~/CreateContextOptions#property_codegeneration)
-   [microtaskMode](././vm/~/CreateContextOptions#property_microtaskmode)
-   [name](././vm/~/CreateContextOptions#property_name)
-   [origin](././vm/~/CreateContextOptions#property_origin)

f

[isContext](././vm/~/isContext "isContext")

Returns `true` if the given `object` object has been contextified using [createContext](././vm/~/createContext), or if it's the global object of a context created using `vm.constants.DONT_CONTEXTIFY`.

f

[measureMemory](././vm/~/measureMemory "measureMemory")

No documentation available

T

[MeasureMemoryMode](././vm/~/MeasureMemoryMode "MeasureMemoryMode")

No documentation available

I

[MeasureMemoryOptions](././vm/~/MeasureMemoryOptions "MeasureMemoryOptions")

No documentation available

-   [execution](././vm/~/MeasureMemoryOptions#property_execution)
-   [mode](././vm/~/MeasureMemoryOptions#property_mode)

I

[MemoryMeasurement](././vm/~/MemoryMeasurement "MemoryMeasurement")

No documentation available

-   [total](././vm/~/MemoryMeasurement#property_total)

c

[Module](././vm/~/Module "Module")

This feature is only available with the `--experimental-vm-modules` command flag enabled.

-   [context](././vm/~/Module#property_context)
-   [dependencySpecifiers](././vm/~/Module#property_dependencyspecifiers)
-   [error](././vm/~/Module#property_error)
-   [evaluate](././vm/~/Module#method_evaluate_0)
-   [identifier](././vm/~/Module#property_identifier)
-   [link](././vm/~/Module#method_link_0)
-   [namespace](././vm/~/Module#property_namespace)
-   [status](././vm/~/Module#property_status)

I

[ModuleEvaluateOptions](././vm/~/ModuleEvaluateOptions "ModuleEvaluateOptions")

No documentation available

-   [breakOnSigint](././vm/~/ModuleEvaluateOptions#property_breakonsigint)
-   [timeout](././vm/~/ModuleEvaluateOptions#property_timeout)

T

[ModuleLinker](././vm/~/ModuleLinker "ModuleLinker")

No documentation available

T

[ModuleStatus](././vm/~/ModuleStatus "ModuleStatus")

No documentation available

f

[runInContext](././vm/~/runInContext "runInContext")

The `vm.runInContext()` method compiles `code`, runs it within the context of the `contextifiedObject`, then returns the result. Running code does not have access to the local scope. The `contextifiedObject` object _must_ have been previously `contextified` using the [createContext](././vm/~/createContext) method.

f

[runInNewContext](././vm/~/runInNewContext "runInNewContext")

This method is a shortcut to `(new vm.Script(code, options)).runInContext(vm.createContext(options), options)`. If `options` is a string, then it specifies the filename.

f

[runInThisContext](././vm/~/runInThisContext "runInThisContext")

`vm.runInThisContext()` compiles `code`, runs it within the context of the current `global` and returns the result. Running code does not have access to local scope, but does have access to the current `global` object.

I

[RunningCodeInNewContextOptions](././vm/~/RunningCodeInNewContextOptions "RunningCodeInNewContextOptions")

No documentation available

-   [cachedData](././vm/~/RunningCodeInNewContextOptions#property_cacheddata)
-   [importModuleDynamically](././vm/~/RunningCodeInNewContextOptions#property_importmoduledynamically)

I

[RunningCodeOptions](././vm/~/RunningCodeOptions "RunningCodeOptions")

No documentation available

-   [cachedData](././vm/~/RunningCodeOptions#property_cacheddata)
-   [importModuleDynamically](././vm/~/RunningCodeOptions#property_importmoduledynamically)

I

[RunningScriptInNewContextOptions](././vm/~/RunningScriptInNewContextOptions "RunningScriptInNewContextOptions")

No documentation available

-   [contextCodeGeneration](././vm/~/RunningScriptInNewContextOptions#property_contextcodegeneration)
-   [contextName](././vm/~/RunningScriptInNewContextOptions#property_contextname)
-   [contextOrigin](././vm/~/RunningScriptInNewContextOptions#property_contextorigin)
-   [microtaskMode](././vm/~/RunningScriptInNewContextOptions#property_microtaskmode)

I

[RunningScriptOptions](././vm/~/RunningScriptOptions "RunningScriptOptions")

No documentation available

-   [breakOnSigint](././vm/~/RunningScriptOptions#property_breakonsigint)
-   [displayErrors](././vm/~/RunningScriptOptions#property_displayerrors)
-   [timeout](././vm/~/RunningScriptOptions#property_timeout)

c

[Script](././vm/~/Script "Script")

No documentation available

-   [cachedData](././vm/~/Script#property_cacheddata)
-   [cachedDataProduced](././vm/~/Script#property_cacheddataproduced)
-   [cachedDataRejected](././vm/~/Script#property_cacheddatarejected)
-   [createCachedData](././vm/~/Script#method_createcacheddata_0)
-   [runInContext](././vm/~/Script#method_runincontext_0)
-   [runInNewContext](././vm/~/Script#method_runinnewcontext_0)
-   [runInThisContext](././vm/~/Script#method_runinthiscontext_0)
-   [sourceMapURL](././vm/~/Script#property_sourcemapurl)

I

[ScriptOptions](././vm/~/ScriptOptions "ScriptOptions")

No documentation available

-   [cachedData](././vm/~/ScriptOptions#property_cacheddata)
-   [importModuleDynamically](././vm/~/ScriptOptions#property_importmoduledynamically)
-   [produceCachedData](././vm/~/ScriptOptions#property_producecacheddata)

c

[SourceTextModule](././vm/~/SourceTextModule "SourceTextModule")

This feature is only available with the `--experimental-vm-modules` command flag enabled.

I

[SourceTextModuleOptions](././vm/~/SourceTextModuleOptions "SourceTextModuleOptions")

No documentation available

-   [cachedData](././vm/~/SourceTextModuleOptions#property_cacheddata)
-   [columnOffset](././vm/~/SourceTextModuleOptions#property_columnoffset)
-   [context](././vm/~/SourceTextModuleOptions#property_context)
-   [identifier](././vm/~/SourceTextModuleOptions#property_identifier)
-   [importModuleDynamically](././vm/~/SourceTextModuleOptions#property_importmoduledynamically)
-   [initializeImportMeta](././vm/~/SourceTextModuleOptions#property_initializeimportmeta)
-   [lineOffset](././vm/~/SourceTextModuleOptions#property_lineoffset)

c

[SyntheticModule](././vm/~/SyntheticModule "SyntheticModule")

This feature is only available with the `--experimental-vm-modules` command flag enabled.

-   [setExport](././vm/~/SyntheticModule#method_setexport_0)

I

[SyntheticModuleOptions](././vm/~/SyntheticModuleOptions "SyntheticModuleOptions")

No documentation available

-   [context](././vm/~/SyntheticModuleOptions#property_context)
-   [identifier](././vm/~/SyntheticModuleOptions#property_identifier)

c

[WASI](././wasi/~/WASI "WASI")

No documentation available

-   [getImportObject](././wasi/~/WASI#method_getimportobject_0)
-   [initialize](././wasi/~/WASI#method_initialize_0)
-   [start](././wasi/~/WASI#method_start_0)
-   [wasiImport](././wasi/~/WASI#property_wasiimport)

I

[WASIOptions](././wasi/~/WASIOptions "WASIOptions")

No documentation available

-   [args](././wasi/~/WASIOptions#property_args)
-   [env](././wasi/~/WASIOptions#property_env)
-   [preopens](././wasi/~/WASIOptions#property_preopens)
-   [returnOnExit](././wasi/~/WASIOptions#property_returnonexit)
-   [stderr](././wasi/~/WASIOptions#property_stderr)
-   [stdin](././wasi/~/WASIOptions#property_stdin)
-   [stdout](././wasi/~/WASIOptions#property_stdout)
-   [version](././wasi/~/WASIOptions#property_version)

The `node:worker_threads` module enables the use of threads that execute JavaScript in parallel. To access it:

c

I

v

[BroadcastChannel](././worker_threads/~/BroadcastChannel "BroadcastChannel")

Instances of `BroadcastChannel` allow asynchronous one-to-many communication with all other `BroadcastChannel` instances bound to the same channel name.

-   [close](././worker_threads/~/BroadcastChannel#method_close_0)
-   [name](././worker_threads/~/BroadcastChannel#property_name)
-   [onmessage](././worker_threads/~/BroadcastChannel#property_onmessage)
-   [onmessageerror](././worker_threads/~/BroadcastChannel#property_onmessageerror)
-   [postMessage](././worker_threads/~/BroadcastChannel#method_postmessage_0)

f

[getEnvironmentData](././worker_threads/~/getEnvironmentData "getEnvironmentData")

Within a worker thread, `worker.getEnvironmentData()` returns a clone of data passed to the spawning thread's `worker.setEnvironmentData()`. Every new `Worker` receives its own copy of the environment data automatically.

v

[isInternalThread](././worker_threads/~/isInternalThread "isInternalThread")

No documentation available

v

[isMainThread](././worker_threads/~/isMainThread "isMainThread")

No documentation available

f

[isMarkedAsUntransferable](././worker_threads/~/isMarkedAsUntransferable "isMarkedAsUntransferable")

Check if an object is marked as not transferable with [markAsUntransferable](././worker_threads/~/markAsUntransferable).

f

[markAsUncloneable](././worker_threads/~/markAsUncloneable "markAsUncloneable")

Mark an object as not cloneable. If `object` is used as `message` in a `port.postMessage()` call, an error is thrown. This is a no-op if `object` is a primitive value.

f

[markAsUntransferable](././worker_threads/~/markAsUntransferable "markAsUntransferable")

No documentation available

c

v

[MessageChannel](././worker_threads/~/MessageChannel "MessageChannel")

Instances of the `worker.MessageChannel` class represent an asynchronous, two-way communications channel. The `MessageChannel` has no methods of its own. `new MessageChannel()` yields an object with `port1` and `port2` properties, which refer to linked `MessagePort` instances.

-   [port1](././worker_threads/~/MessageChannel#property_port1)
-   [port2](././worker_threads/~/MessageChannel#property_port2)

c

v

[MessagePort](././worker_threads/~/MessagePort "MessagePort")

Instances of the `worker.MessagePort` class represent one end of an asynchronous, two-way communications channel. It can be used to transfer structured data, memory regions and other `MessagePort`s between different `Worker`s.

-   [addEventListener](././worker_threads/~/MessagePort#property_addeventlistener)
-   [addListener](././worker_threads/~/MessagePort#method_addlistener_0)
-   [close](././worker_threads/~/MessagePort#method_close_0)
-   [dispatchEvent](././worker_threads/~/MessagePort#property_dispatchevent)
-   [emit](././worker_threads/~/MessagePort#method_emit_0)
-   [off](././worker_threads/~/MessagePort#method_off_0)
-   [on](././worker_threads/~/MessagePort#method_on_0)
-   [once](././worker_threads/~/MessagePort#method_once_0)
-   [postMessage](././worker_threads/~/MessagePort#method_postmessage_0)
-   [prependListener](././worker_threads/~/MessagePort#method_prependlistener_0)
-   [prependOnceListener](././worker_threads/~/MessagePort#method_prependoncelistener_0)
-   [ref](././worker_threads/~/MessagePort#method_ref_0)
-   [removeEventListener](././worker_threads/~/MessagePort#property_removeeventlistener)
-   [removeListener](././worker_threads/~/MessagePort#method_removelistener_0)
-   [start](././worker_threads/~/MessagePort#method_start_0)
-   [unref](././worker_threads/~/MessagePort#method_unref_0)

f

[moveMessagePortToContext](././worker_threads/~/moveMessagePortToContext "moveMessagePortToContext")

No documentation available

v

[parentPort](././worker_threads/~/parentPort "parentPort")

No documentation available

f

[receiveMessageOnPort](././worker_threads/~/receiveMessageOnPort "receiveMessageOnPort")

No documentation available

I

[ResourceLimits](././worker_threads/~/ResourceLimits "ResourceLimits")

No documentation available

-   [codeRangeSizeMb](././worker_threads/~/ResourceLimits#property_coderangesizemb)
-   [maxOldGenerationSizeMb](././worker_threads/~/ResourceLimits#property_maxoldgenerationsizemb)
-   [maxYoungGenerationSizeMb](././worker_threads/~/ResourceLimits#property_maxyounggenerationsizemb)
-   [stackSizeMb](././worker_threads/~/ResourceLimits#property_stacksizemb)

v

[resourceLimits](././worker_threads/~/resourceLimits "resourceLimits")

No documentation available

T

[Serializable](././worker_threads/~/Serializable "Serializable")

No documentation available

f

[setEnvironmentData](././worker_threads/~/setEnvironmentData "setEnvironmentData")

The `worker.setEnvironmentData()` API sets the content of `worker.getEnvironmentData()` in the current thread and all new `Worker` instances spawned from the current context.

v

[SHARE\_ENV](././worker_threads/~/SHARE_ENV "SHARE_ENV")

No documentation available

v

[threadId](././worker_threads/~/threadId "threadId")

No documentation available

T

[TransferListItem](././worker_threads/~/TransferListItem "TransferListItem")

No documentation available

c

[Worker](././worker_threads/~/Worker "Worker")

No documentation available

-   [addListener](././worker_threads/~/Worker#method_addlistener_0)
-   [emit](././worker_threads/~/Worker#method_emit_0)
-   [getHeapSnapshot](././worker_threads/~/Worker#method_getheapsnapshot_0)
-   [off](././worker_threads/~/Worker#method_off_0)
-   [on](././worker_threads/~/Worker#method_on_0)
-   [once](././worker_threads/~/Worker#method_once_0)
-   [performance](././worker_threads/~/Worker#property_performance)
-   [postMessage](././worker_threads/~/Worker#method_postmessage_0)
-   [postMessageToThread](././worker_threads/~/Worker#method_postmessagetothread_0)
-   [prependListener](././worker_threads/~/Worker#method_prependlistener_0)
-   [prependOnceListener](././worker_threads/~/Worker#method_prependoncelistener_0)
-   [ref](././worker_threads/~/Worker#method_ref_0)
-   [removeListener](././worker_threads/~/Worker#method_removelistener_0)
-   [resourceLimits](././worker_threads/~/Worker#property_resourcelimits)
-   [stderr](././worker_threads/~/Worker#property_stderr)
-   [stdin](././worker_threads/~/Worker#property_stdin)
-   [stdout](././worker_threads/~/Worker#property_stdout)
-   [terminate](././worker_threads/~/Worker#method_terminate_0)
-   [threadId](././worker_threads/~/Worker#property_threadid)
-   [unref](././worker_threads/~/Worker#method_unref_0)

v

[workerData](././worker_threads/~/workerData "workerData")

No documentation available

I

[WorkerOptions](././worker_threads/~/WorkerOptions "WorkerOptions")

No documentation available

-   [argv](././worker_threads/~/WorkerOptions#property_argv)
-   [env](././worker_threads/~/WorkerOptions#property_env)
-   [eval](././worker_threads/~/WorkerOptions#property_eval)
-   [execArgv](././worker_threads/~/WorkerOptions#property_execargv)
-   [name](././worker_threads/~/WorkerOptions#property_name)
-   [resourceLimits](././worker_threads/~/WorkerOptions#property_resourcelimits)
-   [stderr](././worker_threads/~/WorkerOptions#property_stderr)
-   [stdin](././worker_threads/~/WorkerOptions#property_stdin)
-   [stdout](././worker_threads/~/WorkerOptions#property_stdout)
-   [trackUnmanagedFds](././worker_threads/~/WorkerOptions#property_trackunmanagedfds)
-   [transferList](././worker_threads/~/WorkerOptions#property_transferlist)
-   [workerData](././worker_threads/~/WorkerOptions#property_workerdata)

I

[WorkerPerformance](././worker_threads/~/WorkerPerformance "WorkerPerformance")

No documentation available

-   [eventLoopUtilization](././worker_threads/~/WorkerPerformance#property_eventlooputilization)

The `node:zlib` module provides compression functionality implemented using Gzip, Deflate/Inflate, and Brotli.

I

[BrotliCompress](././zlib/~/BrotliCompress "BrotliCompress")

No documentation available

f

[brotliCompress](././zlib/~/brotliCompress "brotliCompress")

No documentation available

f

[brotliCompressSync](././zlib/~/brotliCompressSync "brotliCompressSync")

Compress a chunk of data with `BrotliCompress`.

I

[BrotliDecompress](././zlib/~/BrotliDecompress "BrotliDecompress")

No documentation available

f

[brotliDecompress](././zlib/~/brotliDecompress "brotliDecompress")

No documentation available

f

[brotliDecompressSync](././zlib/~/brotliDecompressSync "brotliDecompressSync")

Decompress a chunk of data with `BrotliDecompress`.

I

[BrotliOptions](././zlib/~/BrotliOptions "BrotliOptions")

No documentation available

-   [chunkSize](././zlib/~/BrotliOptions#property_chunksize)
-   [finishFlush](././zlib/~/BrotliOptions#property_finishflush)
-   [flush](././zlib/~/BrotliOptions#property_flush)
-   [maxOutputLength](././zlib/~/BrotliOptions#property_maxoutputlength)
-   [params](././zlib/~/BrotliOptions#property_params)

T

[CompressCallback](././zlib/~/CompressCallback "CompressCallback")

No documentation available

N

[constants](././zlib/~/constants "constants")

No documentation available

v

[constants.BROTLI\_DECODE](././zlib/~/constants.BROTLI_DECODE "constants.BROTLI_DECODE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_BLOCK\_TYPE\_TREES](././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_BLOCK_TYPE_TREES "constants.BROTLI_DECODER_ERROR_ALLOC_BLOCK_TYPE_TREES")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_CONTEXT\_MAP](././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MAP "constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MAP")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_CONTEXT\_MODES](././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MODES "constants.BROTLI_DECODER_ERROR_ALLOC_CONTEXT_MODES")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_RING\_BUFFER\_1](././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_1 "constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_1")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_RING\_BUFFER\_2](././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_2 "constants.BROTLI_DECODER_ERROR_ALLOC_RING_BUFFER_2")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_ALLOC\_TREE\_GROUPS](././zlib/~/constants.BROTLI_DECODER_ERROR_ALLOC_TREE_GROUPS "constants.BROTLI_DECODER_ERROR_ALLOC_TREE_GROUPS")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_DICTIONARY\_NOT\_SET](././zlib/~/constants.BROTLI_DECODER_ERROR_DICTIONARY_NOT_SET "constants.BROTLI_DECODER_ERROR_DICTIONARY_NOT_SET")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_BLOCK\_LENGTH\_1](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_1 "constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_1")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_BLOCK\_LENGTH\_2](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_2 "constants.BROTLI_DECODER_ERROR_FORMAT_BLOCK_LENGTH_2")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_CL\_SPACE](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_CL_SPACE "constants.BROTLI_DECODER_ERROR_FORMAT_CL_SPACE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_CONTEXT\_MAP\_REPEAT](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_CONTEXT_MAP_REPEAT "constants.BROTLI_DECODER_ERROR_FORMAT_CONTEXT_MAP_REPEAT")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_DICTIONARY](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_DICTIONARY "constants.BROTLI_DECODER_ERROR_FORMAT_DICTIONARY")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_DISTANCE](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_DISTANCE "constants.BROTLI_DECODER_ERROR_FORMAT_DISTANCE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_EXUBERANT\_META\_NIBBLE](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_META_NIBBLE "constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_META_NIBBLE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_EXUBERANT\_NIBBLE](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_NIBBLE "constants.BROTLI_DECODER_ERROR_FORMAT_EXUBERANT_NIBBLE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_HUFFMAN\_SPACE](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_HUFFMAN_SPACE "constants.BROTLI_DECODER_ERROR_FORMAT_HUFFMAN_SPACE")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_PADDING\_1](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_1 "constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_1")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_PADDING\_2](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_2 "constants.BROTLI_DECODER_ERROR_FORMAT_PADDING_2")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_RESERVED](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_RESERVED "constants.BROTLI_DECODER_ERROR_FORMAT_RESERVED")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_SIMPLE\_HUFFMAN\_ALPHABET](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_ALPHABET "constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_ALPHABET")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_SIMPLE\_HUFFMAN\_SAME](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_SAME "constants.BROTLI_DECODER_ERROR_FORMAT_SIMPLE_HUFFMAN_SAME")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_TRANSFORM](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_TRANSFORM "constants.BROTLI_DECODER_ERROR_FORMAT_TRANSFORM")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_FORMAT\_WINDOW\_BITS](././zlib/~/constants.BROTLI_DECODER_ERROR_FORMAT_WINDOW_BITS "constants.BROTLI_DECODER_ERROR_FORMAT_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_INVALID\_ARGUMENTS](././zlib/~/constants.BROTLI_DECODER_ERROR_INVALID_ARGUMENTS "constants.BROTLI_DECODER_ERROR_INVALID_ARGUMENTS")

No documentation available

v

[constants.BROTLI\_DECODER\_ERROR\_UNREACHABLE](././zlib/~/constants.BROTLI_DECODER_ERROR_UNREACHABLE "constants.BROTLI_DECODER_ERROR_UNREACHABLE")

No documentation available

v

[constants.BROTLI\_DECODER\_NEEDS\_MORE\_INPUT](././zlib/~/constants.BROTLI_DECODER_NEEDS_MORE_INPUT "constants.BROTLI_DECODER_NEEDS_MORE_INPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_NEEDS\_MORE\_OUTPUT](././zlib/~/constants.BROTLI_DECODER_NEEDS_MORE_OUTPUT "constants.BROTLI_DECODER_NEEDS_MORE_OUTPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_NO\_ERROR](././zlib/~/constants.BROTLI_DECODER_NO_ERROR "constants.BROTLI_DECODER_NO_ERROR")

No documentation available

v

[constants.BROTLI\_DECODER\_PARAM\_DISABLE\_RING\_BUFFER\_REALLOCATION](././zlib/~/constants.BROTLI_DECODER_PARAM_DISABLE_RING_BUFFER_REALLOCATION "constants.BROTLI_DECODER_PARAM_DISABLE_RING_BUFFER_REALLOCATION")

No documentation available

v

[constants.BROTLI\_DECODER\_PARAM\_LARGE\_WINDOW](././zlib/~/constants.BROTLI_DECODER_PARAM_LARGE_WINDOW "constants.BROTLI_DECODER_PARAM_LARGE_WINDOW")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_ERROR](././zlib/~/constants.BROTLI_DECODER_RESULT_ERROR "constants.BROTLI_DECODER_RESULT_ERROR")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_NEEDS\_MORE\_INPUT](././zlib/~/constants.BROTLI_DECODER_RESULT_NEEDS_MORE_INPUT "constants.BROTLI_DECODER_RESULT_NEEDS_MORE_INPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_NEEDS\_MORE\_OUTPUT](././zlib/~/constants.BROTLI_DECODER_RESULT_NEEDS_MORE_OUTPUT "constants.BROTLI_DECODER_RESULT_NEEDS_MORE_OUTPUT")

No documentation available

v

[constants.BROTLI\_DECODER\_RESULT\_SUCCESS](././zlib/~/constants.BROTLI_DECODER_RESULT_SUCCESS "constants.BROTLI_DECODER_RESULT_SUCCESS")

No documentation available

v

[constants.BROTLI\_DECODER\_SUCCESS](././zlib/~/constants.BROTLI_DECODER_SUCCESS "constants.BROTLI_DECODER_SUCCESS")

No documentation available

v

[constants.BROTLI\_DEFAULT\_MODE](././zlib/~/constants.BROTLI_DEFAULT_MODE "constants.BROTLI_DEFAULT_MODE")

No documentation available

v

[constants.BROTLI\_DEFAULT\_QUALITY](././zlib/~/constants.BROTLI_DEFAULT_QUALITY "constants.BROTLI_DEFAULT_QUALITY")

No documentation available

v

[constants.BROTLI\_DEFAULT\_WINDOW](././zlib/~/constants.BROTLI_DEFAULT_WINDOW "constants.BROTLI_DEFAULT_WINDOW")

No documentation available

v

[constants.BROTLI\_ENCODE](././zlib/~/constants.BROTLI_ENCODE "constants.BROTLI_ENCODE")

No documentation available

v

[constants.BROTLI\_LARGE\_MAX\_WINDOW\_BITS](././zlib/~/constants.BROTLI_LARGE_MAX_WINDOW_BITS "constants.BROTLI_LARGE_MAX_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_MAX\_INPUT\_BLOCK\_BITS](././zlib/~/constants.BROTLI_MAX_INPUT_BLOCK_BITS "constants.BROTLI_MAX_INPUT_BLOCK_BITS")

No documentation available

v

[constants.BROTLI\_MAX\_QUALITY](././zlib/~/constants.BROTLI_MAX_QUALITY "constants.BROTLI_MAX_QUALITY")

No documentation available

v

[constants.BROTLI\_MAX\_WINDOW\_BITS](././zlib/~/constants.BROTLI_MAX_WINDOW_BITS "constants.BROTLI_MAX_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_MIN\_INPUT\_BLOCK\_BITS](././zlib/~/constants.BROTLI_MIN_INPUT_BLOCK_BITS "constants.BROTLI_MIN_INPUT_BLOCK_BITS")

No documentation available

v

[constants.BROTLI\_MIN\_QUALITY](././zlib/~/constants.BROTLI_MIN_QUALITY "constants.BROTLI_MIN_QUALITY")

No documentation available

v

[constants.BROTLI\_MIN\_WINDOW\_BITS](././zlib/~/constants.BROTLI_MIN_WINDOW_BITS "constants.BROTLI_MIN_WINDOW_BITS")

No documentation available

v

[constants.BROTLI\_MODE\_FONT](././zlib/~/constants.BROTLI_MODE_FONT "constants.BROTLI_MODE_FONT")

No documentation available

v

[constants.BROTLI\_MODE\_GENERIC](././zlib/~/constants.BROTLI_MODE_GENERIC "constants.BROTLI_MODE_GENERIC")

No documentation available

v

[constants.BROTLI\_MODE\_TEXT](././zlib/~/constants.BROTLI_MODE_TEXT "constants.BROTLI_MODE_TEXT")

No documentation available

v

[constants.BROTLI\_OPERATION\_EMIT\_METADATA](././zlib/~/constants.BROTLI_OPERATION_EMIT_METADATA "constants.BROTLI_OPERATION_EMIT_METADATA")

No documentation available

v

[constants.BROTLI\_OPERATION\_FINISH](././zlib/~/constants.BROTLI_OPERATION_FINISH "constants.BROTLI_OPERATION_FINISH")

No documentation available

v

[constants.BROTLI\_OPERATION\_FLUSH](././zlib/~/constants.BROTLI_OPERATION_FLUSH "constants.BROTLI_OPERATION_FLUSH")

No documentation available

v

[constants.BROTLI\_OPERATION\_PROCESS](././zlib/~/constants.BROTLI_OPERATION_PROCESS "constants.BROTLI_OPERATION_PROCESS")

No documentation available

v

[constants.BROTLI\_PARAM\_DISABLE\_LITERAL\_CONTEXT\_MODELING](././zlib/~/constants.BROTLI_PARAM_DISABLE_LITERAL_CONTEXT_MODELING "constants.BROTLI_PARAM_DISABLE_LITERAL_CONTEXT_MODELING")

No documentation available

v

[constants.BROTLI\_PARAM\_LARGE\_WINDOW](././zlib/~/constants.BROTLI_PARAM_LARGE_WINDOW "constants.BROTLI_PARAM_LARGE_WINDOW")

No documentation available

v

[constants.BROTLI\_PARAM\_LGBLOCK](././zlib/~/constants.BROTLI_PARAM_LGBLOCK "constants.BROTLI_PARAM_LGBLOCK")

No documentation available

v

[constants.BROTLI\_PARAM\_LGWIN](././zlib/~/constants.BROTLI_PARAM_LGWIN "constants.BROTLI_PARAM_LGWIN")

No documentation available

v

[constants.BROTLI\_PARAM\_MODE](././zlib/~/constants.BROTLI_PARAM_MODE "constants.BROTLI_PARAM_MODE")

No documentation available

v

[constants.BROTLI\_PARAM\_NDIRECT](././zlib/~/constants.BROTLI_PARAM_NDIRECT "constants.BROTLI_PARAM_NDIRECT")

No documentation available

v

[constants.BROTLI\_PARAM\_NPOSTFIX](././zlib/~/constants.BROTLI_PARAM_NPOSTFIX "constants.BROTLI_PARAM_NPOSTFIX")

No documentation available

v

[constants.BROTLI\_PARAM\_QUALITY](././zlib/~/constants.BROTLI_PARAM_QUALITY "constants.BROTLI_PARAM_QUALITY")

No documentation available

v

[constants.BROTLI\_PARAM\_SIZE\_HINT](././zlib/~/constants.BROTLI_PARAM_SIZE_HINT "constants.BROTLI_PARAM_SIZE_HINT")

No documentation available

v

[constants.DEFLATE](././zlib/~/constants.DEFLATE "constants.DEFLATE")

No documentation available

v

[constants.DEFLATERAW](././zlib/~/constants.DEFLATERAW "constants.DEFLATERAW")

No documentation available

v

[constants.GUNZIP](././zlib/~/constants.GUNZIP "constants.GUNZIP")

No documentation available

v

[constants.GZIP](././zlib/~/constants.GZIP "constants.GZIP")

No documentation available

v

[constants.INFLATE](././zlib/~/constants.INFLATE "constants.INFLATE")

No documentation available

v

[constants.INFLATERAW](././zlib/~/constants.INFLATERAW "constants.INFLATERAW")

No documentation available

v

[constants.UNZIP](././zlib/~/constants.UNZIP "constants.UNZIP")

No documentation available

v

[constants.Z\_BEST\_COMPRESSION](././zlib/~/constants.Z_BEST_COMPRESSION "constants.Z_BEST_COMPRESSION")

No documentation available

v

[constants.Z\_BEST\_SPEED](././zlib/~/constants.Z_BEST_SPEED "constants.Z_BEST_SPEED")

No documentation available

v

[constants.Z\_BLOCK](././zlib/~/constants.Z_BLOCK "constants.Z_BLOCK")

No documentation available

v

[constants.Z\_BUF\_ERROR](././zlib/~/constants.Z_BUF_ERROR "constants.Z_BUF_ERROR")

No documentation available

v

[constants.Z\_DATA\_ERROR](././zlib/~/constants.Z_DATA_ERROR "constants.Z_DATA_ERROR")

No documentation available

v

[constants.Z\_DEFAULT\_CHUNK](././zlib/~/constants.Z_DEFAULT_CHUNK "constants.Z_DEFAULT_CHUNK")

No documentation available

v

[constants.Z\_DEFAULT\_COMPRESSION](././zlib/~/constants.Z_DEFAULT_COMPRESSION "constants.Z_DEFAULT_COMPRESSION")

No documentation available

v

[constants.Z\_DEFAULT\_LEVEL](././zlib/~/constants.Z_DEFAULT_LEVEL "constants.Z_DEFAULT_LEVEL")

No documentation available

v

[constants.Z\_DEFAULT\_MEMLEVEL](././zlib/~/constants.Z_DEFAULT_MEMLEVEL "constants.Z_DEFAULT_MEMLEVEL")

No documentation available

v

[constants.Z\_DEFAULT\_STRATEGY](././zlib/~/constants.Z_DEFAULT_STRATEGY "constants.Z_DEFAULT_STRATEGY")

No documentation available

v

[constants.Z\_DEFAULT\_WINDOWBITS](././zlib/~/constants.Z_DEFAULT_WINDOWBITS "constants.Z_DEFAULT_WINDOWBITS")

No documentation available

v

[constants.Z\_ERRNO](././zlib/~/constants.Z_ERRNO "constants.Z_ERRNO")

No documentation available

v

[constants.Z\_FILTERED](././zlib/~/constants.Z_FILTERED "constants.Z_FILTERED")

No documentation available

v

[constants.Z\_FINISH](././zlib/~/constants.Z_FINISH "constants.Z_FINISH")

No documentation available

v

[constants.Z\_FIXED](././zlib/~/constants.Z_FIXED "constants.Z_FIXED")

No documentation available

v

[constants.Z\_FULL\_FLUSH](././zlib/~/constants.Z_FULL_FLUSH "constants.Z_FULL_FLUSH")

No documentation available

v

[constants.Z\_HUFFMAN\_ONLY](././zlib/~/constants.Z_HUFFMAN_ONLY "constants.Z_HUFFMAN_ONLY")

No documentation available

v

[constants.Z\_MAX\_CHUNK](././zlib/~/constants.Z_MAX_CHUNK "constants.Z_MAX_CHUNK")

No documentation available

v

[constants.Z\_MAX\_LEVEL](././zlib/~/constants.Z_MAX_LEVEL "constants.Z_MAX_LEVEL")

No documentation available

v

[constants.Z\_MAX\_MEMLEVEL](././zlib/~/constants.Z_MAX_MEMLEVEL "constants.Z_MAX_MEMLEVEL")

No documentation available

v

[constants.Z\_MAX\_WINDOWBITS](././zlib/~/constants.Z_MAX_WINDOWBITS "constants.Z_MAX_WINDOWBITS")

No documentation available

v

[constants.Z\_MEM\_ERROR](././zlib/~/constants.Z_MEM_ERROR "constants.Z_MEM_ERROR")

No documentation available

v

[constants.Z\_MIN\_CHUNK](././zlib/~/constants.Z_MIN_CHUNK "constants.Z_MIN_CHUNK")

No documentation available

v

[constants.Z\_MIN\_LEVEL](././zlib/~/constants.Z_MIN_LEVEL "constants.Z_MIN_LEVEL")

No documentation available

v

[constants.Z\_MIN\_MEMLEVEL](././zlib/~/constants.Z_MIN_MEMLEVEL "constants.Z_MIN_MEMLEVEL")

No documentation available

v

[constants.Z\_MIN\_WINDOWBITS](././zlib/~/constants.Z_MIN_WINDOWBITS "constants.Z_MIN_WINDOWBITS")

No documentation available

v

[constants.Z\_NEED\_DICT](././zlib/~/constants.Z_NEED_DICT "constants.Z_NEED_DICT")

No documentation available

v

[constants.Z\_NO\_COMPRESSION](././zlib/~/constants.Z_NO_COMPRESSION "constants.Z_NO_COMPRESSION")

No documentation available

v

[constants.Z\_NO\_FLUSH](././zlib/~/constants.Z_NO_FLUSH "constants.Z_NO_FLUSH")

No documentation available

v

[constants.Z\_OK](././zlib/~/constants.Z_OK "constants.Z_OK")

No documentation available

v

[constants.Z\_PARTIAL\_FLUSH](././zlib/~/constants.Z_PARTIAL_FLUSH "constants.Z_PARTIAL_FLUSH")

No documentation available

v

[constants.Z\_RLE](././zlib/~/constants.Z_RLE "constants.Z_RLE")

No documentation available

v

[constants.Z\_STREAM\_END](././zlib/~/constants.Z_STREAM_END "constants.Z_STREAM_END")

No documentation available

v

[constants.Z\_STREAM\_ERROR](././zlib/~/constants.Z_STREAM_ERROR "constants.Z_STREAM_ERROR")

No documentation available

v

[constants.Z\_SYNC\_FLUSH](././zlib/~/constants.Z_SYNC_FLUSH "constants.Z_SYNC_FLUSH")

No documentation available

v

[constants.Z\_TREES](././zlib/~/constants.Z_TREES "constants.Z_TREES")

No documentation available

v

[constants.Z\_VERSION\_ERROR](././zlib/~/constants.Z_VERSION_ERROR "constants.Z_VERSION_ERROR")

No documentation available

v

[constants.ZLIB\_VERNUM](././zlib/~/constants.ZLIB_VERNUM "constants.ZLIB_VERNUM")

No documentation available

f

[crc32](././zlib/~/crc32 "crc32")

Computes a 32-bit [Cyclic Redundancy Check](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) checksum of `data`. If `value` is specified, it is used as the starting value of the checksum, otherwise, 0 is used as the starting value.

f

[createBrotliCompress](././zlib/~/createBrotliCompress "createBrotliCompress")

Creates and returns a new `BrotliCompress` object.

f

[createBrotliDecompress](././zlib/~/createBrotliDecompress "createBrotliDecompress")

Creates and returns a new `BrotliDecompress` object.

f

[createDeflate](././zlib/~/createDeflate "createDeflate")

Creates and returns a new `Deflate` object.

f

[createDeflateRaw](././zlib/~/createDeflateRaw "createDeflateRaw")

Creates and returns a new `DeflateRaw` object.

f

[createGunzip](././zlib/~/createGunzip "createGunzip")

Creates and returns a new `Gunzip` object.

f

[createGzip](././zlib/~/createGzip "createGzip")

Creates and returns a new `Gzip` object. See `example`.

f

[createInflate](././zlib/~/createInflate "createInflate")

Creates and returns a new `Inflate` object.

f

[createInflateRaw](././zlib/~/createInflateRaw "createInflateRaw")

Creates and returns a new `InflateRaw` object.

f

[createUnzip](././zlib/~/createUnzip "createUnzip")

Creates and returns a new `Unzip` object.

I

[Deflate](././zlib/~/Deflate "Deflate")

No documentation available

f

[deflate](././zlib/~/deflate "deflate")

No documentation available

I

[DeflateRaw](././zlib/~/DeflateRaw "DeflateRaw")

No documentation available

f

[deflateRaw](././zlib/~/deflateRaw "deflateRaw")

No documentation available

f

[deflateRawSync](././zlib/~/deflateRawSync "deflateRawSync")

Compress a chunk of data with `DeflateRaw`.

f

[deflateSync](././zlib/~/deflateSync "deflateSync")

Compress a chunk of data with `Deflate`.

I

[Gunzip](././zlib/~/Gunzip "Gunzip")

No documentation available

f

[gunzip](././zlib/~/gunzip "gunzip")

No documentation available

f

[gunzipSync](././zlib/~/gunzipSync "gunzipSync")

Decompress a chunk of data with `Gunzip`.

I

[Gzip](././zlib/~/Gzip "Gzip")

No documentation available

f

[gzip](././zlib/~/gzip "gzip")

No documentation available

f

[gzipSync](././zlib/~/gzipSync "gzipSync")

Compress a chunk of data with `Gzip`.

I

[Inflate](././zlib/~/Inflate "Inflate")

No documentation available

f

[inflate](././zlib/~/inflate "inflate")

No documentation available

I

[InflateRaw](././zlib/~/InflateRaw "InflateRaw")

No documentation available

f

[inflateRaw](././zlib/~/inflateRaw "inflateRaw")

No documentation available

f

[inflateRawSync](././zlib/~/inflateRawSync "inflateRawSync")

Decompress a chunk of data with `InflateRaw`.

f

[inflateSync](././zlib/~/inflateSync "inflateSync")

Decompress a chunk of data with `Inflate`.

T

[InputType](././zlib/~/InputType "InputType")

No documentation available

I

[Unzip](././zlib/~/Unzip "Unzip")

No documentation available

f

[unzip](././zlib/~/unzip "unzip")

No documentation available

f

[unzipSync](././zlib/~/unzipSync "unzipSync")

Decompress a chunk of data with `Unzip`.

I

[Zlib](././zlib/~/Zlib "Zlib")

No documentation available

-   [bytesRead](././zlib/~/Zlib#property_bytesread)
-   [bytesWritten](././zlib/~/Zlib#property_byteswritten)
-   [close](././zlib/~/Zlib#method_close_0)
-   [flush](././zlib/~/Zlib#method_flush_0)
-   [shell](././zlib/~/Zlib#property_shell)

I

[ZlibOptions](././zlib/~/ZlibOptions "ZlibOptions")

No documentation available

-   [chunkSize](././zlib/~/ZlibOptions#property_chunksize)
-   [dictionary](././zlib/~/ZlibOptions#property_dictionary)
-   [finishFlush](././zlib/~/ZlibOptions#property_finishflush)
-   [flush](././zlib/~/ZlibOptions#property_flush)
-   [info](././zlib/~/ZlibOptions#property_info)
-   [level](././zlib/~/ZlibOptions#property_level)
-   [maxOutputLength](././zlib/~/ZlibOptions#property_maxoutputlength)
-   [memLevel](././zlib/~/ZlibOptions#property_memlevel)
-   [strategy](././zlib/~/ZlibOptions#property_strategy)
-   [windowBits](././zlib/~/ZlibOptions#property_windowbits)

I

[ZlibParams](././zlib/~/ZlibParams "ZlibParams")

No documentation available

-   [params](././zlib/~/ZlibParams#method_params_0)

I

[ZlibReset](././zlib/~/ZlibReset "ZlibReset")

No documentation available

-   [reset](././zlib/~/ZlibReset#method_reset_0)

v

[Z\_ASCII](././zlib/~/Z_ASCII "Z_ASCII")

No documentation available

v

[Z\_BEST\_COMPRESSION](././zlib/~/Z_BEST_COMPRESSION "Z_BEST_COMPRESSION")

No documentation available

v

[Z\_BEST\_SPEED](././zlib/~/Z_BEST_SPEED "Z_BEST_SPEED")

No documentation available

v

[Z\_BINARY](././zlib/~/Z_BINARY "Z_BINARY")

No documentation available

v

[Z\_BLOCK](././zlib/~/Z_BLOCK "Z_BLOCK")

No documentation available

v

[Z\_BUF\_ERROR](././zlib/~/Z_BUF_ERROR "Z_BUF_ERROR")

No documentation available

v

[Z\_DATA\_ERROR](././zlib/~/Z_DATA_ERROR "Z_DATA_ERROR")

No documentation available

v

[Z\_DEFAULT\_COMPRESSION](././zlib/~/Z_DEFAULT_COMPRESSION "Z_DEFAULT_COMPRESSION")

No documentation available

v

[Z\_DEFAULT\_STRATEGY](././zlib/~/Z_DEFAULT_STRATEGY "Z_DEFAULT_STRATEGY")

No documentation available

v

[Z\_DEFLATED](././zlib/~/Z_DEFLATED "Z_DEFLATED")

No documentation available

v

[Z\_ERRNO](././zlib/~/Z_ERRNO "Z_ERRNO")

No documentation available

v

[Z\_FILTERED](././zlib/~/Z_FILTERED "Z_FILTERED")

No documentation available

v

[Z\_FINISH](././zlib/~/Z_FINISH "Z_FINISH")

No documentation available

v

[Z\_FIXED](././zlib/~/Z_FIXED "Z_FIXED")

No documentation available

v

[Z\_FULL\_FLUSH](././zlib/~/Z_FULL_FLUSH "Z_FULL_FLUSH")

No documentation available

v

[Z\_HUFFMAN\_ONLY](././zlib/~/Z_HUFFMAN_ONLY "Z_HUFFMAN_ONLY")

No documentation available

v

[Z\_MEM\_ERROR](././zlib/~/Z_MEM_ERROR "Z_MEM_ERROR")

No documentation available

v

[Z\_NEED\_DICT](././zlib/~/Z_NEED_DICT "Z_NEED_DICT")

No documentation available

v

[Z\_NO\_COMPRESSION](././zlib/~/Z_NO_COMPRESSION "Z_NO_COMPRESSION")

No documentation available

v

[Z\_NO\_FLUSH](././zlib/~/Z_NO_FLUSH "Z_NO_FLUSH")

No documentation available

v

[Z\_OK](././zlib/~/Z_OK "Z_OK")

No documentation available

v

[Z\_PARTIAL\_FLUSH](././zlib/~/Z_PARTIAL_FLUSH "Z_PARTIAL_FLUSH")

No documentation available

v

[Z\_RLE](././zlib/~/Z_RLE "Z_RLE")

No documentation available

v

[Z\_STREAM\_END](././zlib/~/Z_STREAM_END "Z_STREAM_END")

No documentation available

v

[Z\_STREAM\_ERROR](././zlib/~/Z_STREAM_ERROR "Z_STREAM_ERROR")

No documentation available

v

[Z\_SYNC\_FLUSH](././zlib/~/Z_SYNC_FLUSH "Z_SYNC_FLUSH")

No documentation available

v

[Z\_TEXT](././zlib/~/Z_TEXT "Z_TEXT")

No documentation available

v

[Z\_TREES](././zlib/~/Z_TREES "Z_TREES")

No documentation available

v

[Z\_UNKNOWN](././zlib/~/Z_UNKNOWN "Z_UNKNOWN")

No documentation available

v

[Z\_VERSION\_ERROR](././zlib/~/Z_VERSION_ERROR "Z_VERSION_ERROR")

No documentation available
