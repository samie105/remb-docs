---
title: "dgram - Node documentation"
source: "https://docs.deno.com/api/node/dgram/"
canonical_url: "https://docs.deno.com/api/node/dgram/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:52.185Z"
content_hash: "ee4d2881b70b522bfdf7c23b63769a5a2abaa2acfe2536910bd8eec81e7cf5ad"
menu_path: ["dgram - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/crypto/index.md", "title": "crypto - Node documentation"}
nav_next: {"path": "deno/deno/api/node/diagnostics_channel/index.md", "title": "diagnostics_channel - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:dgram";
```

The `node:dgram` module provides an implementation of UDP datagram sockets.

```js
import dgram from 'node:dgram';

const server = dgram.createSocket('udp4');

server.on('error', (err) => {
  console.error(`server error:\n${err.stack}`);
  server.close();
});

server.on('message', (msg, rinfo) => {
  console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
});

server.on('listening', () => {
  const address = server.address();
  console.log(`server listening ${address.address}:${address.port}`);
});

server.bind(41234);
// Prints: server listening 0.0.0.0:41234
```

### Classes [#](#Classes)

c

[Socket](.././dgram/~/Socket "Socket")

No documentation available

*   [addListener](.././dgram/~/Socket#method_addlistener_0)
*   [addMembership](.././dgram/~/Socket#method_addmembership_0)
*   [addSourceSpecificMembership](.././dgram/~/Socket#method_addsourcespecificmembership_0)
*   [address](.././dgram/~/Socket#method_address_0)
*   [bind](.././dgram/~/Socket#method_bind_0)
*   [close](.././dgram/~/Socket#method_close_0)
*   [connect](.././dgram/~/Socket#method_connect_0)
*   [disconnect](.././dgram/~/Socket#method_disconnect_0)
*   [dropMembership](.././dgram/~/Socket#method_dropmembership_0)
*   [dropSourceSpecificMembership](.././dgram/~/Socket#method_dropsourcespecificmembership_0)
*   [emit](.././dgram/~/Socket#method_emit_0)
*   [getRecvBufferSize](.././dgram/~/Socket#method_getrecvbuffersize_0)
*   [getSendBufferSize](.././dgram/~/Socket#method_getsendbuffersize_0)
*   [getSendQueueCount](.././dgram/~/Socket#method_getsendqueuecount_0)
*   [getSendQueueSize](.././dgram/~/Socket#method_getsendqueuesize_0)
*   [on](.././dgram/~/Socket#method_on_0)
*   [once](.././dgram/~/Socket#method_once_0)
*   [prependListener](.././dgram/~/Socket#method_prependlistener_0)
*   [prependOnceListener](.././dgram/~/Socket#method_prependoncelistener_0)
*   [ref](.././dgram/~/Socket#method_ref_0)
*   [remoteAddress](.././dgram/~/Socket#method_remoteaddress_0)
*   [send](.././dgram/~/Socket#method_send_0)
*   [setBroadcast](.././dgram/~/Socket#method_setbroadcast_0)
*   [setMulticastInterface](.././dgram/~/Socket#method_setmulticastinterface_0)
*   [setMulticastLoopback](.././dgram/~/Socket#method_setmulticastloopback_0)
*   [setMulticastTTL](.././dgram/~/Socket#method_setmulticastttl_0)
*   [setRecvBufferSize](.././dgram/~/Socket#method_setrecvbuffersize_0)
*   [setSendBufferSize](.././dgram/~/Socket#method_setsendbuffersize_0)
*   [setTTL](.././dgram/~/Socket#method_setttl_0)
*   [unref](.././dgram/~/Socket#method_unref_0)

### Functions [#](#Functions)

f

[createSocket](.././dgram/~/createSocket "createSocket")

Creates a `dgram.Socket` object. Once the socket is created, calling `socket.bind()` will instruct the socket to begin listening for datagram messages. When `address` and `port` are not passed to `socket.bind()` the method will bind the socket to the "all interfaces" address on a random port (it does the right thing for both `udp4` and `udp6` sockets). The bound address and port can be retrieved using `socket.address().address` and `socket.address().port`.

### Interfaces [#](#Interfaces)

I

[BindOptions](.././dgram/~/BindOptions "BindOptions")

No documentation available

*   [address](.././dgram/~/BindOptions#property_address)
*   [exclusive](.././dgram/~/BindOptions#property_exclusive)
*   [fd](.././dgram/~/BindOptions#property_fd)
*   [port](.././dgram/~/BindOptions#property_port)

I

[RemoteInfo](.././dgram/~/RemoteInfo "RemoteInfo")

No documentation available

*   [address](.././dgram/~/RemoteInfo#property_address)
*   [family](.././dgram/~/RemoteInfo#property_family)
*   [port](.././dgram/~/RemoteInfo#property_port)
*   [size](.././dgram/~/RemoteInfo#property_size)

I

[SocketOptions](.././dgram/~/SocketOptions "SocketOptions")

No documentation available

*   [ipv6Only](.././dgram/~/SocketOptions#property_ipv6only)
*   [lookup](.././dgram/~/SocketOptions#property_lookup)
*   [receiveBlockList](.././dgram/~/SocketOptions#property_receiveblocklist)
*   [recvBufferSize](.././dgram/~/SocketOptions#property_recvbuffersize)
*   [reuseAddr](.././dgram/~/SocketOptions#property_reuseaddr)
*   [reusePort](.././dgram/~/SocketOptions#property_reuseport)
*   [sendBlockList](.././dgram/~/SocketOptions#property_sendblocklist)
*   [sendBufferSize](.././dgram/~/SocketOptions#property_sendbuffersize)
*   [type](.././dgram/~/SocketOptions#property_type)

### Type Aliases [#](<#Type Aliases>)

T

[SocketType](.././dgram/~/SocketType "SocketType")

No documentation available
