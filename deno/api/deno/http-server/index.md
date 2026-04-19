---
title: "HTTP Server - Deno documentation"
source: "https://docs.deno.com/api/deno/http-server"
canonical_url: "https://docs.deno.com/api/deno/http-server"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:09:43.885Z"
content_hash: "1e59fde25683bc2d545b3094394eafcf34aae63ec355ff1014ea959325fbc3ee"
menu_path: ["HTTP Server - Deno documentation"]
section_path: []
---
### Functions [#](#Functions)

f

[Deno.serve](./././~/Deno.serve "Deno.serve")

Serves HTTP requests with the given handler.

### Interfaces [#](#Interfaces)

I

[Deno.HttpServer](./././~/Deno.HttpServer "Deno.HttpServer")

An instance of the server created using `Deno.serve()` API.

*   [addr](./././~/Deno.HttpServer#property_addr)
*   [finished](./././~/Deno.HttpServer#property_finished)
*   [ref](./././~/Deno.HttpServer#method_ref_0)
*   [shutdown](./././~/Deno.HttpServer#method_shutdown_0)
*   [unref](./././~/Deno.HttpServer#method_unref_0)

I

[Deno.ServeDefaultExport](./././~/Deno.ServeDefaultExport "Deno.ServeDefaultExport")

Interface that module run with `deno serve` subcommand must conform to.

*   [fetch](./././~/Deno.ServeDefaultExport#property_fetch)
*   [onListen](./././~/Deno.ServeDefaultExport#property_onlisten)

I

[Deno.ServeHandlerInfo](./././~/Deno.ServeHandlerInfo "Deno.ServeHandlerInfo")

Additional information for an HTTP request and its connection.

*   [completed](./././~/Deno.ServeHandlerInfo#property_completed)
*   [remoteAddr](./././~/Deno.ServeHandlerInfo#property_remoteaddr)

I

[Deno.ServeInit](./././~/Deno.ServeInit "Deno.ServeInit")

No documentation available

*   [handler](./././~/Deno.ServeInit#property_handler)

I

[Deno.ServeOptions](./././~/Deno.ServeOptions "Deno.ServeOptions")

Options which can be set when calling [`Deno.serve`](./././~/Deno.serve).

*   [onError](./././~/Deno.ServeOptions#property_onerror)
*   [onListen](./././~/Deno.ServeOptions#property_onlisten)
*   [signal](./././~/Deno.ServeOptions#property_signal)

I

[Deno.ServeTcpOptions](./././~/Deno.ServeTcpOptions "Deno.ServeTcpOptions")

Options that can be passed to `Deno.serve` to create a server listening on a TCP port.

*   [hostname](./././~/Deno.ServeTcpOptions#property_hostname)
*   [port](./././~/Deno.ServeTcpOptions#property_port)
*   [reusePort](./././~/Deno.ServeTcpOptions#property_reuseport)
*   [tcpBacklog](./././~/Deno.ServeTcpOptions#property_tcpbacklog)
*   [transport](./././~/Deno.ServeTcpOptions#property_transport)

I

[Deno.ServeUnixOptions](./././~/Deno.ServeUnixOptions "Deno.ServeUnixOptions")

Options that can be passed to `Deno.serve` to create a server listening on a Unix domain socket.

*   [path](./././~/Deno.ServeUnixOptions#property_path)
*   [transport](./././~/Deno.ServeUnixOptions#property_transport)

I

[Deno.ServeVsockOptions](./././~/Deno.ServeVsockOptions "Deno.ServeVsockOptions")

Options that can be passed to `Deno.serve` to create a server listening on a VSOCK socket.

*   [cid](./././~/Deno.ServeVsockOptions#property_cid)
*   [port](./././~/Deno.ServeVsockOptions#property_port)
*   [transport](./././~/Deno.ServeVsockOptions#property_transport)

### Type Aliases [#](<#Type Aliases>)

T

[Deno.ServeHandler](./././~/Deno.ServeHandler "Deno.ServeHandler")

A handler for HTTP requests. Consumes a request and returns a response.
