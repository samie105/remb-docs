---
title: "Platform - Web documentation"
source: "https://docs.deno.com/api/web/platform"
canonical_url: "https://docs.deno.com/api/web/platform"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:11.685Z"
content_hash: "654809b145f4f630abb756720eb4b43e12aac537524efdeec495d4659f397d97"
menu_path: ["Platform - Web documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/web/performance/index.md", "title": "Performance - Web documentation"}
nav_next: {"path": "deno/deno/api/web/storage/index.md", "title": "Storage - Web documentation"}
---

### Functions [#](#Functions)

f

[alert](./././~/alert "alert")

Shows the given message and waits for the enter key pressed.

f

[clearInterval](./././~/clearInterval "clearInterval")

Cancels a timed, repeating action which was previously started by a call to `setInterval()`

f

[clearTimeout](./././~/clearTimeout "clearTimeout")

Cancels a scheduled action initiated by `setTimeout()`

f

[close](./././~/close "close")

Exits the current Deno process.

f

[confirm](./././~/confirm "confirm")

Shows the given message and waits for the answer. Returns the user's answer as boolean.

f

[prompt](./././~/prompt "prompt")

Shows the given message and waits for the user's input. Returns the user's input as string.

f

[queueMicrotask](./././~/queueMicrotask "queueMicrotask")

A microtask is a short function which is executed after the function or module which created it exits and only if the JavaScript execution stack is empty, but before returning control to the event loop being used to drive the script's execution environment. This event loop may be either the main event loop or the event loop driving a web worker.

f

[reportError](./././~/reportError "reportError")

Dispatch an uncaught exception. Similar to a synchronous version of:

f

[setInterval](./././~/setInterval "setInterval")

Repeatedly calls a function , with a fixed time delay between each call.

f

[setTimeout](./././~/setTimeout "setTimeout")

Sets a timer which executes a function once after the delay (in milliseconds) elapses. Returns an id which may be used to cancel the timeout.

f

[structuredClone](./././~/structuredClone "structuredClone")

Creates a deep copy of a given value using the structured clone algorithm.

### Interfaces [#](#Interfaces)

I

v

[AbortController](./././~/AbortController "AbortController")

A controller object that allows you to abort one or more DOM requests as and when desired.

*   [abort](./././~/AbortController#method_abort_0)
*   [prototype](./././~/AbortController#property_prototype)
*   [signal](./././~/AbortController#property_signal)

I

v

[AbortSignal](./././~/AbortSignal "AbortSignal")

A signal object that allows you to communicate with a DOM request (such as a Fetch) and abort it if required via an AbortController object.

*   [abort](./././~/AbortSignal#method_abort_0)
*   [aborted](./././~/AbortSignal#property_aborted)
*   [addEventListener](./././~/AbortSignal#method_addeventlistener_0)
*   [any](./././~/AbortSignal#method_any_0)
*   [onabort](./././~/AbortSignal#property_onabort)
*   [prototype](./././~/AbortSignal#property_prototype)
*   [reason](./././~/AbortSignal#property_reason)
*   [removeEventListener](./././~/AbortSignal#method_removeeventlistener_0)
*   [throwIfAborted](./././~/AbortSignal#method_throwifaborted_0)
*   [timeout](./././~/AbortSignal#method_timeout_0)

I

[AbortSignalEventMap](./././~/AbortSignalEventMap "AbortSignalEventMap")

No documentation available

*   [abort](./././~/AbortSignalEventMap#property_abort)

I

v

[DOMException](./././~/DOMException "DOMException")

No documentation available

*   [ABORT\_ERR](./././~/DOMException#property_abort_err)
*   [DATA\_CLONE\_ERR](./././~/DOMException#property_data_clone_err)
*   [DOMSTRING\_SIZE\_ERR](./././~/DOMException#property_domstring_size_err)
*   [HIERARCHY\_REQUEST\_ERR](./././~/DOMException#property_hierarchy_request_err)
*   [INDEX\_SIZE\_ERR](./././~/DOMException#property_index_size_err)
*   [INUSE\_ATTRIBUTE\_ERR](./././~/DOMException#property_inuse_attribute_err)
*   [INVALID\_ACCESS\_ERR](./././~/DOMException#property_invalid_access_err)
*   [INVALID\_CHARACTER\_ERR](./././~/DOMException#property_invalid_character_err)
*   [INVALID\_MODIFICATION\_ERR](./././~/DOMException#property_invalid_modification_err)
*   [INVALID\_NODE\_TYPE\_ERR](./././~/DOMException#property_invalid_node_type_err)
*   [INVALID\_STATE\_ERR](./././~/DOMException#property_invalid_state_err)
*   [NAMESPACE\_ERR](./././~/DOMException#property_namespace_err)
*   [NETWORK\_ERR](./././~/DOMException#property_network_err)
*   [NOT\_FOUND\_ERR](./././~/DOMException#property_not_found_err)
*   [NOT\_SUPPORTED\_ERR](./././~/DOMException#property_not_supported_err)
*   [NO\_DATA\_ALLOWED\_ERR](./././~/DOMException#property_no_data_allowed_err)
*   [NO\_MODIFICATION\_ALLOWED\_ERR](./././~/DOMException#property_no_modification_allowed_err)
*   [QUOTA\_EXCEEDED\_ERR](./././~/DOMException#property_quota_exceeded_err)
*   [SECURITY\_ERR](./././~/DOMException#property_security_err)
*   [SYNTAX\_ERR](./././~/DOMException#property_syntax_err)
*   [TIMEOUT\_ERR](./././~/DOMException#property_timeout_err)
*   [TYPE\_MISMATCH\_ERR](./././~/DOMException#property_type_mismatch_err)
*   [URL\_MISMATCH\_ERR](./././~/DOMException#property_url_mismatch_err)
*   [VALIDATION\_ERR](./././~/DOMException#property_validation_err)
*   [WRONG\_DOCUMENT\_ERR](./././~/DOMException#property_wrong_document_err)
*   [code](./././~/DOMException#property_code)
*   [message](./././~/DOMException#property_message)
*   [name](./././~/DOMException#property_name)
*   [prototype](./././~/DOMException#property_prototype)

I

[DomIterable](./././~/DomIterable "DomIterable")

No documentation available

*   [entries](./././~/DomIterable#method_entries_0)
*   [forEach](./././~/DomIterable#method_foreach_0)
*   [keys](./././~/DomIterable#method_keys_0)
*   [values](./././~/DomIterable#method_values_0)

I

[DOMStringList](./././~/DOMStringList "DOMStringList")

No documentation available

*   [contains](./././~/DOMStringList#method_contains_0)
*   [item](./././~/DOMStringList#method_item_0)
*   [length](./././~/DOMStringList#property_length)

I

[ErrorConstructor](./././~/ErrorConstructor "ErrorConstructor")

No documentation available

*   [captureStackTrace](./././~/ErrorConstructor#method_capturestacktrace_0)
*   [stackTraceLimit](./././~/ErrorConstructor#property_stacktracelimit)

I

v

[ImageData](./././~/ImageData "ImageData")

No documentation available

*   [colorSpace](./././~/ImageData#property_colorspace)
*   [data](./././~/ImageData#property_data)
*   [height](./././~/ImageData#property_height)
*   [pixelFormat](./././~/ImageData#property_pixelformat)
*   [prototype](./././~/ImageData#property_prototype)
*   [width](./././~/ImageData#property_width)

I

[ImageDataSettings](./././~/ImageDataSettings "ImageDataSettings")

No documentation available

*   [colorSpace](./././~/ImageDataSettings#property_colorspace)
*   [pixelFormat](./././~/ImageDataSettings#property_pixelformat)

I

[ImportMeta](./././~/ImportMeta "ImportMeta")

Deno provides extra properties on `import.meta`. These are included here to ensure that these are still available when using the Deno namespace in conjunction with other type libs, like `dom`.

*   [dirname](./././~/ImportMeta#property_dirname)
*   [filename](./././~/ImportMeta#property_filename)
*   [main](./././~/ImportMeta#property_main)
*   [resolve](./././~/ImportMeta#method_resolve_0)
*   [url](./././~/ImportMeta#property_url)

I

v

[Location](./././~/Location "Location")

The location (URL) of the object it is linked to. Changes done on it are reflected on the object it relates to. Accessible via `globalThis.location`.

*   [ancestorOrigins](./././~/Location#property_ancestororigins)
*   [assign](./././~/Location#method_assign_0)
*   [hash](./././~/Location#property_hash)
*   [host](./././~/Location#property_host)
*   [hostname](./././~/Location#property_hostname)
*   [href](./././~/Location#property_href)
*   [origin](./././~/Location#property_origin)
*   [pathname](./././~/Location#property_pathname)
*   [port](./././~/Location#property_port)
*   [protocol](./././~/Location#property_protocol)
*   [prototype](./././~/Location#property_prototype)
*   [reload](./././~/Location#method_reload_0)
*   [replace](./././~/Location#method_replace_0)
*   [search](./././~/Location#property_search)
*   [toString](./././~/Location#method_tostring_0)

I

v

[Navigator](./././~/Navigator "Navigator")

Provides information about the Deno runtime environment and the system on which it's running. Similar to the browser `Navigator` object but adapted for the Deno context.

*   [gpu](./././~/Navigator#property_gpu)
*   [hardwareConcurrency](./././~/Navigator#property_hardwareconcurrency)
*   [language](./././~/Navigator#property_language)
*   [languages](./././~/Navigator#property_languages)
*   [platform](./././~/Navigator#property_platform)
*   [prototype](./././~/Navigator#property_prototype)
*   [userAgent](./././~/Navigator#property_useragent)

I

v

[QuotaExceededError](./././~/QuotaExceededError "QuotaExceededError")

Represents an error when a quota has been exceeded.

*   [prototype](./././~/QuotaExceededError#property_prototype)
*   [quota](./././~/QuotaExceededError#property_quota)
*   [requested](./././~/QuotaExceededError#property_requested)

I

[QuotaExceededErrorOptions](./././~/QuotaExceededErrorOptions "QuotaExceededErrorOptions")

No documentation available

*   [quota](./././~/QuotaExceededErrorOptions#property_quota)
*   [requested](./././~/QuotaExceededErrorOptions#property_requested)

I

[RegExpConstructor](./././~/RegExpConstructor "RegExpConstructor")

No documentation available

*   [escape](./././~/RegExpConstructor#method_escape_0)

I

[StructuredSerializeOptions](./././~/StructuredSerializeOptions "StructuredSerializeOptions")

Options that control structured serialization operations such as `structuredClone(value, options)` and `MessagePort.postMessage(message, options)`.

*   [transfer](./././~/StructuredSerializeOptions#property_transfer)

I

[Uint8Array](./././~/Uint8Array "Uint8Array")

No documentation available

*   [setFromBase64](./././~/Uint8Array#method_setfrombase64_0)
*   [setFromHex](./././~/Uint8Array#method_setfromhex_0)
*   [toBase64](./././~/Uint8Array#method_tobase64_0)
*   [toHex](./././~/Uint8Array#method_tohex_0)

I

[Uint8ArrayConstructor](./././~/Uint8ArrayConstructor "Uint8ArrayConstructor")

No documentation available

*   [fromBase64](./././~/Uint8ArrayConstructor#method_frombase64_0)
*   [fromHex](./././~/Uint8ArrayConstructor#method_fromhex_0)

I

[VoidFunction](./././~/VoidFunction "VoidFunction")

No documentation available

I

v

[WebTransport](./././~/WebTransport "WebTransport")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransport)

*   [close](./././~/WebTransport#method_close_0)
*   [closed](./././~/WebTransport#property_closed)
*   [createBidirectionalStream](./././~/WebTransport#method_createbidirectionalstream_0)
*   [createSendGroup](./././~/WebTransport#method_createsendgroup_0)
*   [createUnidirectionalStream](./././~/WebTransport#method_createunidirectionalstream_0)
*   [datagrams](./././~/WebTransport#property_datagrams)
*   [incomingBidirectionalStreams](./././~/WebTransport#property_incomingbidirectionalstreams)
*   [incomingUnidirectionalStreams](./././~/WebTransport#property_incomingunidirectionalstreams)
*   [prototype](./././~/WebTransport#property_prototype)
*   [ready](./././~/WebTransport#property_ready)

I

v

[WebTransportBidirectionalStream](./././~/WebTransportBidirectionalStream "WebTransportBidirectionalStream")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransportBidirectionalStream)

*   [prototype](./././~/WebTransportBidirectionalStream#property_prototype)
*   [readable](./././~/WebTransportBidirectionalStream#property_readable)
*   [writable](./././~/WebTransportBidirectionalStream#property_writable)

I

[WebTransportCloseInfo](./././~/WebTransportCloseInfo "WebTransportCloseInfo")

No documentation available

*   [closeCode](./././~/WebTransportCloseInfo#property_closecode)
*   [reason](./././~/WebTransportCloseInfo#property_reason)

I

v

[WebTransportDatagramDuplexStream](./././~/WebTransportDatagramDuplexStream "WebTransportDatagramDuplexStream")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransportDatagramDuplexStream)

*   [incomingHighWaterMark](./././~/WebTransportDatagramDuplexStream#property_incominghighwatermark)
*   [incomingMaxAge](./././~/WebTransportDatagramDuplexStream#property_incomingmaxage)
*   [maxDatagramSize](./././~/WebTransportDatagramDuplexStream#property_maxdatagramsize)
*   [outgoingHighWaterMark](./././~/WebTransportDatagramDuplexStream#property_outgoinghighwatermark)
*   [outgoingMaxAge](./././~/WebTransportDatagramDuplexStream#property_outgoingmaxage)
*   [prototype](./././~/WebTransportDatagramDuplexStream#property_prototype)
*   [readable](./././~/WebTransportDatagramDuplexStream#property_readable)
*   [writable](./././~/WebTransportDatagramDuplexStream#property_writable)

I

v

[WebTransportError](./././~/WebTransportError "WebTransportError")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransportError)

*   [prototype](./././~/WebTransportError#property_prototype)
*   [source](./././~/WebTransportError#property_source)
*   [streamErrorCode](./././~/WebTransportError#property_streamerrorcode)

I

[WebTransportErrorOptions](./././~/WebTransportErrorOptions "WebTransportErrorOptions")

No documentation available

*   [source](./././~/WebTransportErrorOptions#property_source)
*   [streamErrorCode](./././~/WebTransportErrorOptions#property_streamerrorcode)

I

[WebTransportHash](./././~/WebTransportHash "WebTransportHash")

No documentation available

*   [algorithm](./././~/WebTransportHash#property_algorithm)
*   [value](./././~/WebTransportHash#property_value)

I

[WebTransportOptions](./././~/WebTransportOptions "WebTransportOptions")

No documentation available

*   [allowPooling](./././~/WebTransportOptions#property_allowpooling)
*   [congestionControl](./././~/WebTransportOptions#property_congestioncontrol)
*   [requireUnreliable](./././~/WebTransportOptions#property_requireunreliable)
*   [serverCertificateHashes](./././~/WebTransportOptions#property_servercertificatehashes)

I

v

[WebTransportReceiveStream](./././~/WebTransportReceiveStream "WebTransportReceiveStream")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransportReceiveStream)

*   [getStats](./././~/WebTransportReceiveStream#method_getstats_0)
*   [prototype](./././~/WebTransportReceiveStream#property_prototype)

I

[WebTransportReceiveStreamStats](./././~/WebTransportReceiveStreamStats "WebTransportReceiveStreamStats")

No documentation available

*   [bytesRead](./././~/WebTransportReceiveStreamStats#property_bytesread)
*   [bytesReceived](./././~/WebTransportReceiveStreamStats#property_bytesreceived)

I

v

[WebTransportSendGroup](./././~/WebTransportSendGroup "WebTransportSendGroup")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransportSendGroup)

*   [getStats](./././~/WebTransportSendGroup#method_getstats_0)
*   [prototype](./././~/WebTransportSendGroup#property_prototype)

I

v

[WebTransportSendStream](./././~/WebTransportSendStream "WebTransportSendStream")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransportSendStream)

*   [getStats](./././~/WebTransportSendStream#method_getstats_0)
*   [getWriter](./././~/WebTransportSendStream#method_getwriter_0)
*   [prototype](./././~/WebTransportSendStream#property_prototype)
*   [sendGroup](./././~/WebTransportSendStream#property_sendgroup)
*   [sendOrder](./././~/WebTransportSendStream#property_sendorder)

I

[WebTransportSendStreamOptions](./././~/WebTransportSendStreamOptions "WebTransportSendStreamOptions")

No documentation available

*   [sendGroup](./././~/WebTransportSendStreamOptions#property_sendgroup)
*   [sendOrder](./././~/WebTransportSendStreamOptions#property_sendorder)
*   [waitUntilAvailable](./././~/WebTransportSendStreamOptions#property_waituntilavailable)

I

[WebTransportSendStreamStats](./././~/WebTransportSendStreamStats "WebTransportSendStreamStats")

No documentation available

*   [bytesAcknowledged](./././~/WebTransportSendStreamStats#property_bytesacknowledged)
*   [bytesSent](./././~/WebTransportSendStreamStats#property_bytessent)
*   [bytesWritten](./././~/WebTransportSendStreamStats#property_byteswritten)

I

v

[WebTransportWriter](./././~/WebTransportWriter "WebTransportWriter")

[MDN Reference](https://developer.mozilla.org/docs/Web/API/WebTransportWriter)

*   [atomicWrite](./././~/WebTransportWriter#method_atomicwrite_0)
*   [prototype](./././~/WebTransportWriter#property_prototype)

I

v

[Window](./././~/Window "Window")

Represents the global window object in the Deno runtime environment.

*   [Deno](./././~/Window#property_deno)
*   [Location](./././~/Window#property_location)
*   [Navigator](./././~/Window#property_navigator)
*   [addEventListener](./././~/Window#method_addeventlistener_0)
*   [alert](./././~/Window#property_alert)
*   [caches](./././~/Window#property_caches)
*   [close](./././~/Window#property_close)
*   [closed](./././~/Window#property_closed)
*   [confirm](./././~/Window#property_confirm)
*   [localStorage](./././~/Window#property_localstorage)
*   [location](./././~/Window#property_location)
*   [name](./././~/Window#property_name)
*   [navigator](./././~/Window#property_navigator)
*   [onbeforeunload](./././~/Window#property_onbeforeunload)
*   [onerror](./././~/Window#property_onerror)
*   [onload](./././~/Window#property_onload)
*   [onrejectionhandled](./././~/Window#property_onrejectionhandled)
*   [onunhandledrejection](./././~/Window#property_onunhandledrejection)
*   [onunload](./././~/Window#property_onunload)
*   [prompt](./././~/Window#property_prompt)
*   [prototype](./././~/Window#property_prototype)
*   [removeEventListener](./././~/Window#method_removeeventlistener_0)
*   [self](./././~/Window#property_self)
*   [sessionStorage](./././~/Window#property_sessionstorage)
*   [window](./././~/Window#property_window)

I

[WindowEventMap](./././~/WindowEventMap "WindowEventMap")

Defines the mapping between event names and their corresponding event types for the `Window` interface in Deno.

*   [error](./././~/WindowEventMap#property_error)
*   [rejectionhandled](./././~/WindowEventMap#property_rejectionhandled)
*   [unhandledrejection](./././~/WindowEventMap#property_unhandledrejection)

### Type Aliases [#](<#Type Aliases>)

T

[AllowSharedBufferSource](./././~/AllowSharedBufferSource "AllowSharedBufferSource")

No documentation available

T

[BufferSource](./././~/BufferSource "BufferSource")

No documentation available

T

[ImageDataArray](./././~/ImageDataArray "ImageDataArray")

No documentation available

T

[ImageDataPixelFormat](./././~/ImageDataPixelFormat "ImageDataPixelFormat")

No documentation available

T

[PredefinedColorSpace](./././~/PredefinedColorSpace "PredefinedColorSpace")

No documentation available

T

[WebTransportCongestionControl](./././~/WebTransportCongestionControl "WebTransportCongestionControl")

No documentation available

T

[WebTransportErrorSource](./././~/WebTransportErrorSource "WebTransportErrorSource")

No documentation available

### Variables [#](#Variables)

v

[closed](./././~/closed "closed")

Indicates whether the current window (context) is closed. In Deno, this property is primarily for API compatibility with browsers.

v

[location](./././~/location "location")

No documentation available

v

[name](./././~/name "name")

No documentation available

v

[navigator](./././~/navigator "navigator")

Provides access to the Deno runtime's `Navigator` interface, which contains information about the environment in which the script is running.

v

[self](./././~/self "self")

Reference to the global object itself. Equivalent to the global `window` object in browser environments.

