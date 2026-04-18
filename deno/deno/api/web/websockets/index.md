---
title: "WebSockets - Web documentation"
source: "https://docs.deno.com/api/web/websockets"
canonical_url: "https://docs.deno.com/api/web/websockets"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:15:15.943Z"
content_hash: "aad5f87a89749a983050608b509838a81da3687f5dc28080a403102f3854a913"
menu_path: ["WebSockets - Web documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/web/wasm/index.md", "title": "Wasm - Web documentation"}
nav_next: {"path": "deno/deno/api/web/workers/index.md", "title": "Workers - Web documentation"}
---

### Interfaces [#](#Interfaces)

I

v

[CloseEvent](./././~/CloseEvent "CloseEvent")

The `CloseEvent` interface represents an event that occurs when a `WebSocket` connection is closed.

*   [code](./././~/CloseEvent#property_code)
*   [prototype](./././~/CloseEvent#property_prototype)
*   [reason](./././~/CloseEvent#property_reason)
*   [wasClean](./././~/CloseEvent#property_wasclean)

I

[CloseEventInit](./././~/CloseEventInit "CloseEventInit")

Configuration options for a `WebSocket` "close" event.

*   [code](./././~/CloseEventInit#property_code)
*   [reason](./././~/CloseEventInit#property_reason)
*   [wasClean](./././~/CloseEventInit#property_wasclean)

I

v

[WebSocket](./././~/WebSocket "WebSocket")

Provides the API for creating and managing a WebSocket connection to a server, as well as for sending and receiving data on the connection.

*   [CLOSED](./././~/WebSocket#property_closed)
*   [CLOSING](./././~/WebSocket#property_closing)
*   [CONNECTING](./././~/WebSocket#property_connecting)
*   [OPEN](./././~/WebSocket#property_open)
*   [addEventListener](./././~/WebSocket#method_addeventlistener_0)
*   [binaryType](./././~/WebSocket#property_binarytype)
*   [bufferedAmount](./././~/WebSocket#property_bufferedamount)
*   [close](./././~/WebSocket#method_close_0)
*   [extensions](./././~/WebSocket#property_extensions)
*   [onclose](./././~/WebSocket#property_onclose)
*   [onerror](./././~/WebSocket#property_onerror)
*   [onmessage](./././~/WebSocket#property_onmessage)
*   [onopen](./././~/WebSocket#property_onopen)
*   [protocol](./././~/WebSocket#property_protocol)
*   [prototype](./././~/WebSocket#property_prototype)
*   [readyState](./././~/WebSocket#property_readystate)
*   [removeEventListener](./././~/WebSocket#method_removeeventlistener_0)
*   [send](./././~/WebSocket#method_send_0)
*   [url](./././~/WebSocket#property_url)

I

[WebSocketCloseInfo](./././~/WebSocketCloseInfo "WebSocketCloseInfo")

No documentation available

*   [code](./././~/WebSocketCloseInfo#property_code)
*   [reason](./././~/WebSocketCloseInfo#property_reason)

I

[WebSocketConnection](./././~/WebSocketConnection "WebSocketConnection")

No documentation available

*   [extensions](./././~/WebSocketConnection#property_extensions)
*   [protocol](./././~/WebSocketConnection#property_protocol)
*   [readable](./././~/WebSocketConnection#property_readable)
*   [writable](./././~/WebSocketConnection#property_writable)

I

v

[WebSocketError](./././~/WebSocketError "WebSocketError")

No documentation available

*   [closeCode](./././~/WebSocketError#property_closecode)
*   [prototype](./././~/WebSocketError#property_prototype)
*   [reason](./././~/WebSocketError#property_reason)

I

[WebSocketEventMap](./././~/WebSocketEventMap "WebSocketEventMap")

Interface mapping `WebSocket` event names to their corresponding event types. Used for strongly typed event handling with `addEventListener` and `removeEventListener`.

*   [close](./././~/WebSocketEventMap#property_close)
*   [error](./././~/WebSocketEventMap#property_error)
*   [message](./././~/WebSocketEventMap#property_message)
*   [open](./././~/WebSocketEventMap#property_open)

I

[WebSocketOptions](./././~/WebSocketOptions "WebSocketOptions")

Options for a WebSocket instance. This feature is non-standard.

*   [client](./././~/WebSocketOptions#property_client)
*   [headers](./././~/WebSocketOptions#property_headers)
*   [protocols](./././~/WebSocketOptions#property_protocols)

I

v

[WebSocketStream](./././~/WebSocketStream "WebSocketStream")

No documentation available

*   [close](./././~/WebSocketStream#method_close_0)
*   [closed](./././~/WebSocketStream#property_closed)
*   [opened](./././~/WebSocketStream#property_opened)
*   [prototype](./././~/WebSocketStream#property_prototype)
*   [url](./././~/WebSocketStream#property_url)

I

[WebSocketStreamOptions](./././~/WebSocketStreamOptions "WebSocketStreamOptions")

No documentation available

*   [headers](./././~/WebSocketStreamOptions#property_headers)
*   [protocols](./././~/WebSocketStreamOptions#property_protocols)
*   [signal](./././~/WebSocketStreamOptions#property_signal)

### Type Aliases [#](<#Type Aliases>)

T

[BinaryType](./././~/BinaryType "BinaryType")

Specifies the type of binary data being received over a `WebSocket` connection.


