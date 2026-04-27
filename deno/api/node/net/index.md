---
title: "net - Node documentation"
source: "https://docs.deno.com/api/node/net/"
canonical_url: "https://docs.deno.com/api/node/net/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:08:59.118Z"
content_hash: "7403a1feee3ee7d1c15510d9eb2543adc55aba632fa40a7278b5a13156a88d9d"
menu_path: ["net - Node documentation"]
section_path: []
content_language: "en"
---
### Usage in Deno

```typescript
import * as mod from "node:net";
```

> Stability: 2 - Stable

The `node:net` module provides an asynchronous network API for creating stream-based TCP or `IPC` servers ([createServer](.././net/~/createServer)) and clients ([createConnection](.././net/~/createConnection)).

It can be accessed using:

```js
import net from 'node:net';
```

c

[BlockList](.././net/~/BlockList "BlockList")

The `BlockList` object can be used with some network APIs to specify rules for disabling inbound or outbound access to specific IP addresses, IP ranges, or IP subnets.

-   [addAddress](.././net/~/BlockList#method_addaddress_0)
-   [addRange](.././net/~/BlockList#method_addrange_0)
-   [addSubnet](.././net/~/BlockList#method_addsubnet_0)
-   [check](.././net/~/BlockList#method_check_0)
-   [isBlockList](.././net/~/BlockList#method_isblocklist_0)
-   [rules](.././net/~/BlockList#property_rules)

c

[Server](.././net/~/Server "Server")

This class is used to create a TCP or `IPC` server.

-   [addListener](.././net/~/Server#method_addlistener_0)
-   [address](.././net/~/Server#method_address_0)
-   [close](.././net/~/Server#method_close_0)
-   [connections](.././net/~/Server#property_connections)
-   [emit](.././net/~/Server#method_emit_0)
-   [getConnections](.././net/~/Server#method_getconnections_0)
-   [listen](.././net/~/Server#method_listen_0)
-   [listening](.././net/~/Server#property_listening)
-   [maxConnections](.././net/~/Server#property_maxconnections)
-   [on](.././net/~/Server#method_on_0)
-   [once](.././net/~/Server#method_once_0)
-   [prependListener](.././net/~/Server#method_prependlistener_0)
-   [prependOnceListener](.././net/~/Server#method_prependoncelistener_0)
-   [ref](.././net/~/Server#method_ref_0)
-   [unref](.././net/~/Server#method_unref_0)

c

[Socket](.././net/~/Socket "Socket")

No documentation available

-   [addListener](.././net/~/Socket#method_addlistener_0)
-   [address](.././net/~/Socket#method_address_0)
-   [autoSelectFamilyAttemptedAddresses](.././net/~/Socket#property_autoselectfamilyattemptedaddresses)
-   [bufferSize](.././net/~/Socket#property_buffersize)
-   [bytesRead](.././net/~/Socket#property_bytesread)
-   [bytesWritten](.././net/~/Socket#property_byteswritten)
-   [connect](.././net/~/Socket#method_connect_0)
-   [connecting](.././net/~/Socket#property_connecting)
-   [destroySoon](.././net/~/Socket#method_destroysoon_0)
-   [destroyed](.././net/~/Socket#property_destroyed)
-   [emit](.././net/~/Socket#method_emit_0)
-   [end](.././net/~/Socket#method_end_0)
-   [localAddress](.././net/~/Socket#property_localaddress)
-   [localFamily](.././net/~/Socket#property_localfamily)
-   [localPort](.././net/~/Socket#property_localport)
-   [on](.././net/~/Socket#method_on_0)
-   [once](.././net/~/Socket#method_once_0)
-   [pause](.././net/~/Socket#method_pause_0)
-   [pending](.././net/~/Socket#property_pending)
-   [prependListener](.././net/~/Socket#method_prependlistener_0)
-   [prependOnceListener](.././net/~/Socket#method_prependoncelistener_0)
-   [readyState](.././net/~/Socket#property_readystate)
-   [ref](.././net/~/Socket#method_ref_0)
-   [remoteAddress](.././net/~/Socket#property_remoteaddress)
-   [remoteFamily](.././net/~/Socket#property_remotefamily)
-   [remotePort](.././net/~/Socket#property_remoteport)
-   [resetAndDestroy](.././net/~/Socket#method_resetanddestroy_0)
-   [resume](.././net/~/Socket#method_resume_0)
-   [setEncoding](.././net/~/Socket#method_setencoding_0)
-   [setKeepAlive](.././net/~/Socket#method_setkeepalive_0)
-   [setNoDelay](.././net/~/Socket#method_setnodelay_0)
-   [setTimeout](.././net/~/Socket#method_settimeout_0)
-   [timeout](.././net/~/Socket#property_timeout)
-   [unref](.././net/~/Socket#method_unref_0)
-   [write](.././net/~/Socket#method_write_0)

c

[SocketAddress](.././net/~/SocketAddress "SocketAddress")

No documentation available

-   [address](.././net/~/SocketAddress#property_address)
-   [family](.././net/~/SocketAddress#property_family)
-   [flowlabel](.././net/~/SocketAddress#property_flowlabel)
-   [parse](.././net/~/SocketAddress#method_parse_0)
-   [port](.././net/~/SocketAddress#property_port)

f

[connect](.././net/~/connect "connect")

Aliases to [createConnection](.././net/~/createConnection).

f

[createConnection](.././net/~/createConnection "createConnection")

A factory function, which creates a new [Socket](.././net/~/Socket), immediately initiates connection with `socket.connect()`, then returns the `net.Socket` that starts the connection.

f

[createServer](.././net/~/createServer "createServer")

Creates a new TCP or `IPC` server.

f

[getDefaultAutoSelectFamily](.././net/~/getDefaultAutoSelectFamily "getDefaultAutoSelectFamily")

Gets the current default value of the `autoSelectFamily` option of `socket.connect(options)`. The initial default value is `true`, unless the command line option`--no-network-family-autoselection` is provided.

f

[getDefaultAutoSelectFamilyAttemptTimeout](.././net/~/getDefaultAutoSelectFamilyAttemptTimeout "getDefaultAutoSelectFamilyAttemptTimeout")

Gets the current default value of the `autoSelectFamilyAttemptTimeout` option of `socket.connect(options)`. The initial default value is `250` or the value specified via the command line option `--network-family-autoselection-attempt-timeout`.

f

[isIP](.././net/~/isIP "isIP")

Returns `6` if `input` is an IPv6 address. Returns `4` if `input` is an IPv4 address in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) with no leading zeroes. Otherwise, returns`0`.

f

[isIPv4](.././net/~/isIPv4 "isIPv4")

Returns `true` if `input` is an IPv4 address in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) with no leading zeroes. Otherwise, returns `false`.

f

[isIPv6](.././net/~/isIPv6 "isIPv6")

Returns `true` if `input` is an IPv6 address. Otherwise, returns `false`.

f

[setDefaultAutoSelectFamily](.././net/~/setDefaultAutoSelectFamily "setDefaultAutoSelectFamily")

Sets the default value of the `autoSelectFamily` option of `socket.connect(options)`.

f

[setDefaultAutoSelectFamilyAttemptTimeout](.././net/~/setDefaultAutoSelectFamilyAttemptTimeout "setDefaultAutoSelectFamilyAttemptTimeout")

Sets the default value of the `autoSelectFamilyAttemptTimeout` option of `socket.connect(options)`.

I

[AddressInfo](.././net/~/AddressInfo "AddressInfo")

No documentation available

-   [address](.././net/~/AddressInfo#property_address)
-   [family](.././net/~/AddressInfo#property_family)
-   [port](.././net/~/AddressInfo#property_port)

I

[DropArgument](.././net/~/DropArgument "DropArgument")

No documentation available

-   [localAddress](.././net/~/DropArgument#property_localaddress)
-   [localFamily](.././net/~/DropArgument#property_localfamily)
-   [localPort](.././net/~/DropArgument#property_localport)
-   [remoteAddress](.././net/~/DropArgument#property_remoteaddress)
-   [remoteFamily](.././net/~/DropArgument#property_remotefamily)
-   [remotePort](.././net/~/DropArgument#property_remoteport)

I

[IpcNetConnectOpts](.././net/~/IpcNetConnectOpts "IpcNetConnectOpts")

No documentation available

-   [timeout](.././net/~/IpcNetConnectOpts#property_timeout)

I

[IpcSocketConnectOpts](.././net/~/IpcSocketConnectOpts "IpcSocketConnectOpts")

No documentation available

-   [path](.././net/~/IpcSocketConnectOpts#property_path)

I

[ListenOptions](.././net/~/ListenOptions "ListenOptions")

No documentation available

-   [backlog](.././net/~/ListenOptions#property_backlog)
-   [exclusive](.././net/~/ListenOptions#property_exclusive)
-   [host](.././net/~/ListenOptions#property_host)
-   [ipv6Only](.././net/~/ListenOptions#property_ipv6only)
-   [path](.././net/~/ListenOptions#property_path)
-   [port](.././net/~/ListenOptions#property_port)
-   [readableAll](.././net/~/ListenOptions#property_readableall)
-   [reusePort](.././net/~/ListenOptions#property_reuseport)
-   [writableAll](.././net/~/ListenOptions#property_writableall)

I

[OnReadOpts](.././net/~/OnReadOpts "OnReadOpts")

No documentation available

-   [buffer](.././net/~/OnReadOpts#property_buffer)
-   [callback](.././net/~/OnReadOpts#method_callback_0)

I

[ServerOpts](.././net/~/ServerOpts "ServerOpts")

No documentation available

-   [allowHalfOpen](.././net/~/ServerOpts#property_allowhalfopen)
-   [blockList](.././net/~/ServerOpts#property_blocklist)
-   [highWaterMark](.././net/~/ServerOpts#property_highwatermark)
-   [keepAlive](.././net/~/ServerOpts#property_keepalive)
-   [keepAliveInitialDelay](.././net/~/ServerOpts#property_keepaliveinitialdelay)
-   [noDelay](.././net/~/ServerOpts#property_nodelay)
-   [pauseOnConnect](.././net/~/ServerOpts#property_pauseonconnect)

I

[SocketAddressInitOptions](.././net/~/SocketAddressInitOptions "SocketAddressInitOptions")

No documentation available

-   [address](.././net/~/SocketAddressInitOptions#property_address)
-   [family](.././net/~/SocketAddressInitOptions#property_family)
-   [flowlabel](.././net/~/SocketAddressInitOptions#property_flowlabel)
-   [port](.././net/~/SocketAddressInitOptions#property_port)

I

[SocketConstructorOpts](.././net/~/SocketConstructorOpts "SocketConstructorOpts")

No documentation available

-   [allowHalfOpen](.././net/~/SocketConstructorOpts#property_allowhalfopen)
-   [fd](.././net/~/SocketConstructorOpts#property_fd)
-   [onread](.././net/~/SocketConstructorOpts#property_onread)
-   [readable](.././net/~/SocketConstructorOpts#property_readable)
-   [signal](.././net/~/SocketConstructorOpts#property_signal)
-   [writable](.././net/~/SocketConstructorOpts#property_writable)

I

[TcpNetConnectOpts](.././net/~/TcpNetConnectOpts "TcpNetConnectOpts")

No documentation available

-   [timeout](.././net/~/TcpNetConnectOpts#property_timeout)

I

[TcpSocketConnectOpts](.././net/~/TcpSocketConnectOpts "TcpSocketConnectOpts")

No documentation available

-   [autoSelectFamily](.././net/~/TcpSocketConnectOpts#property_autoselectfamily)
-   [autoSelectFamilyAttemptTimeout](.././net/~/TcpSocketConnectOpts#property_autoselectfamilyattempttimeout)
-   [blockList](.././net/~/TcpSocketConnectOpts#property_blocklist)
-   [family](.././net/~/TcpSocketConnectOpts#property_family)
-   [hints](.././net/~/TcpSocketConnectOpts#property_hints)
-   [host](.././net/~/TcpSocketConnectOpts#property_host)
-   [keepAlive](.././net/~/TcpSocketConnectOpts#property_keepalive)
-   [keepAliveInitialDelay](.././net/~/TcpSocketConnectOpts#property_keepaliveinitialdelay)
-   [localAddress](.././net/~/TcpSocketConnectOpts#property_localaddress)
-   [localPort](.././net/~/TcpSocketConnectOpts#property_localport)
-   [lookup](.././net/~/TcpSocketConnectOpts#property_lookup)
-   [noDelay](.././net/~/TcpSocketConnectOpts#property_nodelay)
-   [port](.././net/~/TcpSocketConnectOpts#property_port)

I

[ConnectOpts](.././net/~/ConnectOpts "ConnectOpts")

No documentation available

T

[IPVersion](.././net/~/IPVersion "IPVersion")

No documentation available

T

[LookupFunction](.././net/~/LookupFunction "LookupFunction")

No documentation available

T

[NetConnectOpts](.././net/~/NetConnectOpts "NetConnectOpts")

No documentation available

T

[SocketConnectOpts](.././net/~/SocketConnectOpts "SocketConnectOpts")

No documentation available

T

[SocketReadyState](.././net/~/SocketReadyState "SocketReadyState")

No documentation available
