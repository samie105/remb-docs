---
title: "http - Node documentation"
source: "https://docs.deno.com/api/node/http/"
canonical_url: "https://docs.deno.com/api/node/http/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:21.104Z"
content_hash: "8cd4561d4d65a0759d0658fe0f8069085c2174d362b234d29768c6a79e36d0f3"
menu_path: ["http - Node documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/node/fs/promises/index.md", "title": "fs/promises - Node documentation"}
nav_next: {"path": "deno/deno/api/node/http2/index.md", "title": "http2 - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:http";
```

To use the HTTP server and client one must import the `node:http` module.

The HTTP interfaces in Node.js are designed to support many features of the protocol which have been traditionally difficult to use. In particular, large, possibly chunk-encoded, messages. The interface is careful to never buffer entire requests or responses, so the user is able to stream data.

HTTP message headers are represented by an object like this:

```json
{ "content-length": "123",
  "content-type": "text/plain",
  "connection": "keep-alive",
  "host": "example.com",
  "accept": "*" }
```

Keys are lowercased. Values are not modified.

In order to support the full spectrum of possible HTTP applications, the Node.js HTTP API is very low-level. It deals with stream handling and message parsing only. It parses a message into headers and body but it does not parse the actual headers or the body.

See `message.headers` for details on how duplicate headers are handled.

The raw headers as they were received are retained in the `rawHeaders` property, which is an array of `[key, value, key2, value2, ...]`. For example, the previous message header object might have a `rawHeaders` list like the following:

```js
[ 'ConTent-Length', '123456',
  'content-LENGTH', '123',
  'content-type', 'text/plain',
  'CONNECTION', 'keep-alive',
  'Host', 'example.com',
  'accepT', '*' ]
```

### Classes [#](#Classes)

c

[Agent](.././http/~/Agent "Agent")

An `Agent` is responsible for managing connection persistence and reuse for HTTP clients. It maintains a queue of pending requests for a given host and port, reusing a single socket connection for each until the queue is empty, at which time the socket is either destroyed or put into a pool where it is kept to be used again for requests to the same host and port. Whether it is destroyed or pooled depends on the `keepAlive` `option`.

*   [destroy](.././http/~/Agent#method_destroy_0)
*   [freeSockets](.././http/~/Agent#property_freesockets)
*   [maxFreeSockets](.././http/~/Agent#property_maxfreesockets)
*   [maxSockets](.././http/~/Agent#property_maxsockets)
*   [maxTotalSockets](.././http/~/Agent#property_maxtotalsockets)
*   [requests](.././http/~/Agent#property_requests)
*   [sockets](.././http/~/Agent#property_sockets)

c

[ClientRequest](.././http/~/ClientRequest "ClientRequest")

No documentation available

*   [abort](.././http/~/ClientRequest#method_abort_0)
*   [aborted](.././http/~/ClientRequest#property_aborted)
*   [addListener](.././http/~/ClientRequest#method_addlistener_0)
*   [getRawHeaderNames](.././http/~/ClientRequest#method_getrawheadernames_0)
*   [host](.././http/~/ClientRequest#property_host)
*   [maxHeadersCount](.././http/~/ClientRequest#property_maxheaderscount)
*   [method](.././http/~/ClientRequest#property_method)
*   [on](.././http/~/ClientRequest#method_on_0)
*   [onSocket](.././http/~/ClientRequest#method_onsocket_0)
*   [once](.././http/~/ClientRequest#method_once_0)
*   [path](.././http/~/ClientRequest#property_path)
*   [prependListener](.././http/~/ClientRequest#method_prependlistener_0)
*   [prependOnceListener](.././http/~/ClientRequest#method_prependoncelistener_0)
*   [protocol](.././http/~/ClientRequest#property_protocol)
*   [reusedSocket](.././http/~/ClientRequest#property_reusedsocket)
*   [setNoDelay](.././http/~/ClientRequest#method_setnodelay_0)
*   [setSocketKeepAlive](.././http/~/ClientRequest#method_setsocketkeepalive_0)
*   [setTimeout](.././http/~/ClientRequest#method_settimeout_0)

c

[IncomingMessage](.././http/~/IncomingMessage "IncomingMessage")

An `IncomingMessage` object is created by [Server](.././http/~/Server) or [ClientRequest](.././http/~/ClientRequest) and passed as the first argument to the `'request'` and `'response'` event respectively. It may be used to access response status, headers, and data.

*   [aborted](.././http/~/IncomingMessage#property_aborted)
*   [complete](.././http/~/IncomingMessage#property_complete)
*   [connection](.././http/~/IncomingMessage#property_connection)
*   [destroy](.././http/~/IncomingMessage#method_destroy_0)
*   [headers](.././http/~/IncomingMessage#property_headers)
*   [headersDistinct](.././http/~/IncomingMessage#property_headersdistinct)
*   [httpVersion](.././http/~/IncomingMessage#property_httpversion)
*   [httpVersionMajor](.././http/~/IncomingMessage#property_httpversionmajor)
*   [httpVersionMinor](.././http/~/IncomingMessage#property_httpversionminor)
*   [method](.././http/~/IncomingMessage#property_method)
*   [rawHeaders](.././http/~/IncomingMessage#property_rawheaders)
*   [rawTrailers](.././http/~/IncomingMessage#property_rawtrailers)
*   [setTimeout](.././http/~/IncomingMessage#method_settimeout_0)
*   [socket](.././http/~/IncomingMessage#property_socket)
*   [statusCode](.././http/~/IncomingMessage#property_statuscode)
*   [statusMessage](.././http/~/IncomingMessage#property_statusmessage)
*   [trailers](.././http/~/IncomingMessage#property_trailers)
*   [trailersDistinct](.././http/~/IncomingMessage#property_trailersdistinct)
*   [url](.././http/~/IncomingMessage#property_url)

c

[OutgoingMessage](.././http/~/OutgoingMessage "OutgoingMessage")

This class serves as the parent class of [ClientRequest](.././http/~/ClientRequest) and [ServerResponse](.././http/~/ServerResponse). It is an abstract outgoing message from the perspective of the participants of an HTTP transaction.

*   [addTrailers](.././http/~/OutgoingMessage#method_addtrailers_0)
*   [appendHeader](.././http/~/OutgoingMessage#method_appendheader_0)
*   [chunkedEncoding](.././http/~/OutgoingMessage#property_chunkedencoding)
*   [connection](.././http/~/OutgoingMessage#property_connection)
*   [finished](.././http/~/OutgoingMessage#property_finished)
*   [flushHeaders](.././http/~/OutgoingMessage#method_flushheaders_0)
*   [getHeader](.././http/~/OutgoingMessage#method_getheader_0)
*   [getHeaderNames](.././http/~/OutgoingMessage#method_getheadernames_0)
*   [getHeaders](.././http/~/OutgoingMessage#method_getheaders_0)
*   [hasHeader](.././http/~/OutgoingMessage#method_hasheader_0)
*   [headersSent](.././http/~/OutgoingMessage#property_headerssent)
*   [removeHeader](.././http/~/OutgoingMessage#method_removeheader_0)
*   [req](.././http/~/OutgoingMessage#property_req)
*   [sendDate](.././http/~/OutgoingMessage#property_senddate)
*   [setHeader](.././http/~/OutgoingMessage#method_setheader_0)
*   [setHeaders](.././http/~/OutgoingMessage#method_setheaders_0)
*   [setTimeout](.././http/~/OutgoingMessage#method_settimeout_0)
*   [shouldKeepAlive](.././http/~/OutgoingMessage#property_shouldkeepalive)
*   [socket](.././http/~/OutgoingMessage#property_socket)
*   [useChunkedEncodingByDefault](.././http/~/OutgoingMessage#property_usechunkedencodingbydefault)

c

[Server](.././http/~/Server "Server")

No documentation available

*   [addListener](.././http/~/Server#method_addlistener_0)
*   [closeAllConnections](.././http/~/Server#method_closeallconnections_0)
*   [closeIdleConnections](.././http/~/Server#method_closeidleconnections_0)
*   [emit](.././http/~/Server#method_emit_0)
*   [headersTimeout](.././http/~/Server#property_headerstimeout)
*   [keepAliveTimeout](.././http/~/Server#property_keepalivetimeout)
*   [maxHeadersCount](.././http/~/Server#property_maxheaderscount)
*   [maxRequestsPerSocket](.././http/~/Server#property_maxrequestspersocket)
*   [on](.././http/~/Server#method_on_0)
*   [once](.././http/~/Server#method_once_0)
*   [prependListener](.././http/~/Server#method_prependlistener_0)
*   [prependOnceListener](.././http/~/Server#method_prependoncelistener_0)
*   [requestTimeout](.././http/~/Server#property_requesttimeout)
*   [setTimeout](.././http/~/Server#method_settimeout_0)
*   [timeout](.././http/~/Server#property_timeout)

c

[ServerResponse](.././http/~/ServerResponse "ServerResponse")

This object is created internally by an HTTP server, not by the user. It is passed as the second parameter to the `'request'` event.

*   [assignSocket](.././http/~/ServerResponse#method_assignsocket_0)
*   [detachSocket](.././http/~/ServerResponse#method_detachsocket_0)
*   [statusCode](.././http/~/ServerResponse#property_statuscode)
*   [statusMessage](.././http/~/ServerResponse#property_statusmessage)
*   [strictContentLength](.././http/~/ServerResponse#property_strictcontentlength)
*   [writeContinue](.././http/~/ServerResponse#method_writecontinue_0)
*   [writeEarlyHints](.././http/~/ServerResponse#method_writeearlyhints_0)
*   [writeHead](.././http/~/ServerResponse#method_writehead_0)
*   [writeProcessing](.././http/~/ServerResponse#method_writeprocessing_0)

### Functions [#](#Functions)

f

[createServer](.././http/~/createServer "createServer")

Returns a new instance of [Server](.././http/~/Server).

f

[get](.././http/~/get "get")

No documentation available

f

[request](.././http/~/request "request")

No documentation available

f

[setMaxIdleHTTPParsers](.././http/~/setMaxIdleHTTPParsers "setMaxIdleHTTPParsers")

Set the maximum number of idle HTTP parsers.

f

[validateHeaderName](.././http/~/validateHeaderName "validateHeaderName")

Performs the low-level validations on the provided `name` that are done when `res.setHeader(name, value)` is called.

f

[validateHeaderValue](.././http/~/validateHeaderValue "validateHeaderValue")

Performs the low-level validations on the provided `value` that are done when `res.setHeader(name, value)` is called.

### Interfaces [#](#Interfaces)

I

[AgentOptions](.././http/~/AgentOptions "AgentOptions")

No documentation available

*   [keepAlive](.././http/~/AgentOptions#property_keepalive)
*   [keepAliveMsecs](.././http/~/AgentOptions#property_keepalivemsecs)
*   [maxFreeSockets](.././http/~/AgentOptions#property_maxfreesockets)
*   [maxSockets](.././http/~/AgentOptions#property_maxsockets)
*   [maxTotalSockets](.././http/~/AgentOptions#property_maxtotalsockets)
*   [scheduling](.././http/~/AgentOptions#property_scheduling)
*   [timeout](.././http/~/AgentOptions#property_timeout)

I

[ClientRequestArgs](.././http/~/ClientRequestArgs "ClientRequestArgs")

No documentation available

*   [\_defaultAgent](.././http/~/ClientRequestArgs#property__defaultagent)
*   [agent](.././http/~/ClientRequestArgs#property_agent)
*   [auth](.././http/~/ClientRequestArgs#property_auth)
*   [createConnection](.././http/~/ClientRequestArgs#property_createconnection)
*   [defaultPort](.././http/~/ClientRequestArgs#property_defaultport)
*   [family](.././http/~/ClientRequestArgs#property_family)
*   [headers](.././http/~/ClientRequestArgs#property_headers)
*   [hints](.././http/~/ClientRequestArgs#property_hints)
*   [host](.././http/~/ClientRequestArgs#property_host)
*   [hostname](.././http/~/ClientRequestArgs#property_hostname)
*   [insecureHTTPParser](.././http/~/ClientRequestArgs#property_insecurehttpparser)
*   [joinDuplicateHeaders](.././http/~/ClientRequestArgs#property_joinduplicateheaders)
*   [localAddress](.././http/~/ClientRequestArgs#property_localaddress)
*   [localPort](.././http/~/ClientRequestArgs#property_localport)
*   [lookup](.././http/~/ClientRequestArgs#property_lookup)
*   [maxHeaderSize](.././http/~/ClientRequestArgs#property_maxheadersize)
*   [method](.././http/~/ClientRequestArgs#property_method)
*   [path](.././http/~/ClientRequestArgs#property_path)
*   [port](.././http/~/ClientRequestArgs#property_port)
*   [protocol](.././http/~/ClientRequestArgs#property_protocol)
*   [setDefaultHeaders](.././http/~/ClientRequestArgs#property_setdefaultheaders)
*   [setHost](.././http/~/ClientRequestArgs#property_sethost)
*   [signal](.././http/~/ClientRequestArgs#property_signal)
*   [socketPath](.././http/~/ClientRequestArgs#property_socketpath)
*   [timeout](.././http/~/ClientRequestArgs#property_timeout)
*   [uniqueHeaders](.././http/~/ClientRequestArgs#property_uniqueheaders)

I

[IncomingHttpHeaders](.././http/~/IncomingHttpHeaders "IncomingHttpHeaders")

No documentation available

*   [accept](.././http/~/IncomingHttpHeaders#property_accept)
*   [accept-language](.././http/~/IncomingHttpHeaders#property_accept-language)
*   [accept-patch](.././http/~/IncomingHttpHeaders#property_accept-patch)
*   [accept-ranges](.././http/~/IncomingHttpHeaders#property_accept-ranges)
*   [access-control-allow-credentials](.././http/~/IncomingHttpHeaders#property_access-control-allow-credentials)
*   [access-control-allow-headers](.././http/~/IncomingHttpHeaders#property_access-control-allow-headers)
*   [access-control-allow-methods](.././http/~/IncomingHttpHeaders#property_access-control-allow-methods)
*   [access-control-allow-origin](.././http/~/IncomingHttpHeaders#property_access-control-allow-origin)
*   [access-control-expose-headers](.././http/~/IncomingHttpHeaders#property_access-control-expose-headers)
*   [access-control-max-age](.././http/~/IncomingHttpHeaders#property_access-control-max-age)
*   [access-control-request-headers](.././http/~/IncomingHttpHeaders#property_access-control-request-headers)
*   [access-control-request-method](.././http/~/IncomingHttpHeaders#property_access-control-request-method)
*   [age](.././http/~/IncomingHttpHeaders#property_age)
*   [allow](.././http/~/IncomingHttpHeaders#property_allow)
*   [alt-svc](.././http/~/IncomingHttpHeaders#property_alt-svc)
*   [authorization](.././http/~/IncomingHttpHeaders#property_authorization)
*   [cache-control](.././http/~/IncomingHttpHeaders#property_cache-control)
*   [connection](.././http/~/IncomingHttpHeaders#property_connection)
*   [content-disposition](.././http/~/IncomingHttpHeaders#property_content-disposition)
*   [content-encoding](.././http/~/IncomingHttpHeaders#property_content-encoding)
*   [content-language](.././http/~/IncomingHttpHeaders#property_content-language)
*   [content-length](.././http/~/IncomingHttpHeaders#property_content-length)
*   [content-location](.././http/~/IncomingHttpHeaders#property_content-location)
*   [content-range](.././http/~/IncomingHttpHeaders#property_content-range)
*   [content-type](.././http/~/IncomingHttpHeaders#property_content-type)
*   [cookie](.././http/~/IncomingHttpHeaders#property_cookie)
*   [date](.././http/~/IncomingHttpHeaders#property_date)
*   [etag](.././http/~/IncomingHttpHeaders#property_etag)
*   [expect](.././http/~/IncomingHttpHeaders#property_expect)
*   [expires](.././http/~/IncomingHttpHeaders#property_expires)
*   [forwarded](.././http/~/IncomingHttpHeaders#property_forwarded)
*   [from](.././http/~/IncomingHttpHeaders#property_from)
*   [host](.././http/~/IncomingHttpHeaders#property_host)
*   [if-match](.././http/~/IncomingHttpHeaders#property_if-match)
*   [if-modified-since](.././http/~/IncomingHttpHeaders#property_if-modified-since)
*   [if-none-match](.././http/~/IncomingHttpHeaders#property_if-none-match)
*   [if-unmodified-since](.././http/~/IncomingHttpHeaders#property_if-unmodified-since)
*   [last-modified](.././http/~/IncomingHttpHeaders#property_last-modified)
*   [location](.././http/~/IncomingHttpHeaders#property_location)
*   [origin](.././http/~/IncomingHttpHeaders#property_origin)
*   [pragma](.././http/~/IncomingHttpHeaders#property_pragma)
*   [proxy-authenticate](.././http/~/IncomingHttpHeaders#property_proxy-authenticate)
*   [proxy-authorization](.././http/~/IncomingHttpHeaders#property_proxy-authorization)
*   [public-key-pins](.././http/~/IncomingHttpHeaders#property_public-key-pins)
*   [range](.././http/~/IncomingHttpHeaders#property_range)
*   [referer](.././http/~/IncomingHttpHeaders#property_referer)
*   [retry-after](.././http/~/IncomingHttpHeaders#property_retry-after)
*   [sec-websocket-accept](.././http/~/IncomingHttpHeaders#property_sec-websocket-accept)
*   [sec-websocket-extensions](.././http/~/IncomingHttpHeaders#property_sec-websocket-extensions)
*   [sec-websocket-key](.././http/~/IncomingHttpHeaders#property_sec-websocket-key)
*   [sec-websocket-protocol](.././http/~/IncomingHttpHeaders#property_sec-websocket-protocol)
*   [sec-websocket-version](.././http/~/IncomingHttpHeaders#property_sec-websocket-version)
*   [set-cookie](.././http/~/IncomingHttpHeaders#property_set-cookie)
*   [strict-transport-security](.././http/~/IncomingHttpHeaders#property_strict-transport-security)
*   [tk](.././http/~/IncomingHttpHeaders#property_tk)
*   [trailer](.././http/~/IncomingHttpHeaders#property_trailer)
*   [transfer-encoding](.././http/~/IncomingHttpHeaders#property_transfer-encoding)
*   [upgrade](.././http/~/IncomingHttpHeaders#property_upgrade)
*   [user-agent](.././http/~/IncomingHttpHeaders#property_user-agent)
*   [vary](.././http/~/IncomingHttpHeaders#property_vary)
*   [via](.././http/~/IncomingHttpHeaders#property_via)
*   [warning](.././http/~/IncomingHttpHeaders#property_warning)
*   [www-authenticate](.././http/~/IncomingHttpHeaders#property_www-authenticate)

I

[InformationEvent](.././http/~/InformationEvent "InformationEvent")

No documentation available

*   [headers](.././http/~/InformationEvent#property_headers)
*   [httpVersion](.././http/~/InformationEvent#property_httpversion)
*   [httpVersionMajor](.././http/~/InformationEvent#property_httpversionmajor)
*   [httpVersionMinor](.././http/~/InformationEvent#property_httpversionminor)
*   [rawHeaders](.././http/~/InformationEvent#property_rawheaders)
*   [statusCode](.././http/~/InformationEvent#property_statuscode)
*   [statusMessage](.././http/~/InformationEvent#property_statusmessage)

I

[OutgoingHttpHeaders](.././http/~/OutgoingHttpHeaders "OutgoingHttpHeaders")

No documentation available

*   [accept](.././http/~/OutgoingHttpHeaders#property_accept)
*   [accept-charset](.././http/~/OutgoingHttpHeaders#property_accept-charset)
*   [accept-encoding](.././http/~/OutgoingHttpHeaders#property_accept-encoding)
*   [accept-language](.././http/~/OutgoingHttpHeaders#property_accept-language)
*   [accept-ranges](.././http/~/OutgoingHttpHeaders#property_accept-ranges)
*   [access-control-allow-credentials](.././http/~/OutgoingHttpHeaders#property_access-control-allow-credentials)
*   [access-control-allow-headers](.././http/~/OutgoingHttpHeaders#property_access-control-allow-headers)
*   [access-control-allow-methods](.././http/~/OutgoingHttpHeaders#property_access-control-allow-methods)
*   [access-control-allow-origin](.././http/~/OutgoingHttpHeaders#property_access-control-allow-origin)
*   [access-control-expose-headers](.././http/~/OutgoingHttpHeaders#property_access-control-expose-headers)
*   [access-control-max-age](.././http/~/OutgoingHttpHeaders#property_access-control-max-age)
*   [access-control-request-headers](.././http/~/OutgoingHttpHeaders#property_access-control-request-headers)
*   [access-control-request-method](.././http/~/OutgoingHttpHeaders#property_access-control-request-method)
*   [age](.././http/~/OutgoingHttpHeaders#property_age)
*   [allow](.././http/~/OutgoingHttpHeaders#property_allow)
*   [authorization](.././http/~/OutgoingHttpHeaders#property_authorization)
*   [cache-control](.././http/~/OutgoingHttpHeaders#property_cache-control)
*   [cdn-cache-control](.././http/~/OutgoingHttpHeaders#property_cdn-cache-control)
*   [connection](.././http/~/OutgoingHttpHeaders#property_connection)
*   [content-disposition](.././http/~/OutgoingHttpHeaders#property_content-disposition)
*   [content-encoding](.././http/~/OutgoingHttpHeaders#property_content-encoding)
*   [content-language](.././http/~/OutgoingHttpHeaders#property_content-language)
*   [content-length](.././http/~/OutgoingHttpHeaders#property_content-length)
*   [content-location](.././http/~/OutgoingHttpHeaders#property_content-location)
*   [content-range](.././http/~/OutgoingHttpHeaders#property_content-range)
*   [content-security-policy](.././http/~/OutgoingHttpHeaders#property_content-security-policy)
*   [content-security-policy-report-only](.././http/~/OutgoingHttpHeaders#property_content-security-policy-report-only)
*   [content-type](.././http/~/OutgoingHttpHeaders#property_content-type)
*   [cookie](.././http/~/OutgoingHttpHeaders#property_cookie)
*   [date](.././http/~/OutgoingHttpHeaders#property_date)
*   [dav](.././http/~/OutgoingHttpHeaders#property_dav)
*   [dnt](.././http/~/OutgoingHttpHeaders#property_dnt)
*   [etag](.././http/~/OutgoingHttpHeaders#property_etag)
*   [expect](.././http/~/OutgoingHttpHeaders#property_expect)
*   [expires](.././http/~/OutgoingHttpHeaders#property_expires)
*   [forwarded](.././http/~/OutgoingHttpHeaders#property_forwarded)
*   [from](.././http/~/OutgoingHttpHeaders#property_from)
*   [host](.././http/~/OutgoingHttpHeaders#property_host)
*   [if-match](.././http/~/OutgoingHttpHeaders#property_if-match)
*   [if-modified-since](.././http/~/OutgoingHttpHeaders#property_if-modified-since)
*   [if-none-match](.././http/~/OutgoingHttpHeaders#property_if-none-match)
*   [if-range](.././http/~/OutgoingHttpHeaders#property_if-range)
*   [if-unmodified-since](.././http/~/OutgoingHttpHeaders#property_if-unmodified-since)
*   [last-modified](.././http/~/OutgoingHttpHeaders#property_last-modified)
*   [link](.././http/~/OutgoingHttpHeaders#property_link)
*   [location](.././http/~/OutgoingHttpHeaders#property_location)
*   [max-forwards](.././http/~/OutgoingHttpHeaders#property_max-forwards)
*   [origin](.././http/~/OutgoingHttpHeaders#property_origin)
*   [pragma](.././http/~/OutgoingHttpHeaders#property_pragma)
*   [proxy-authenticate](.././http/~/OutgoingHttpHeaders#property_proxy-authenticate)
*   [proxy-authorization](.././http/~/OutgoingHttpHeaders#property_proxy-authorization)
*   [public-key-pins](.././http/~/OutgoingHttpHeaders#property_public-key-pins)
*   [public-key-pins-report-only](.././http/~/OutgoingHttpHeaders#property_public-key-pins-report-only)
*   [range](.././http/~/OutgoingHttpHeaders#property_range)
*   [referer](.././http/~/OutgoingHttpHeaders#property_referer)
*   [referrer-policy](.././http/~/OutgoingHttpHeaders#property_referrer-policy)
*   [refresh](.././http/~/OutgoingHttpHeaders#property_refresh)
*   [retry-after](.././http/~/OutgoingHttpHeaders#property_retry-after)
*   [sec-websocket-accept](.././http/~/OutgoingHttpHeaders#property_sec-websocket-accept)
*   [sec-websocket-extensions](.././http/~/OutgoingHttpHeaders#property_sec-websocket-extensions)
*   [sec-websocket-key](.././http/~/OutgoingHttpHeaders#property_sec-websocket-key)
*   [sec-websocket-protocol](.././http/~/OutgoingHttpHeaders#property_sec-websocket-protocol)
*   [sec-websocket-version](.././http/~/OutgoingHttpHeaders#property_sec-websocket-version)
*   [server](.././http/~/OutgoingHttpHeaders#property_server)
*   [set-cookie](.././http/~/OutgoingHttpHeaders#property_set-cookie)
*   [strict-transport-security](.././http/~/OutgoingHttpHeaders#property_strict-transport-security)
*   [te](.././http/~/OutgoingHttpHeaders#property_te)
*   [trailer](.././http/~/OutgoingHttpHeaders#property_trailer)
*   [transfer-encoding](.././http/~/OutgoingHttpHeaders#property_transfer-encoding)
*   [upgrade](.././http/~/OutgoingHttpHeaders#property_upgrade)
*   [upgrade-insecure-requests](.././http/~/OutgoingHttpHeaders#property_upgrade-insecure-requests)
*   [user-agent](.././http/~/OutgoingHttpHeaders#property_user-agent)
*   [vary](.././http/~/OutgoingHttpHeaders#property_vary)
*   [via](.././http/~/OutgoingHttpHeaders#property_via)
*   [warning](.././http/~/OutgoingHttpHeaders#property_warning)
*   [www-authenticate](.././http/~/OutgoingHttpHeaders#property_www-authenticate)
*   [x-content-type-options](.././http/~/OutgoingHttpHeaders#property_x-content-type-options)
*   [x-dns-prefetch-control](.././http/~/OutgoingHttpHeaders#property_x-dns-prefetch-control)
*   [x-frame-options](.././http/~/OutgoingHttpHeaders#property_x-frame-options)
*   [x-xss-protection](.././http/~/OutgoingHttpHeaders#property_x-xss-protection)

I

[RequestOptions](.././http/~/RequestOptions "RequestOptions")

No documentation available

I

[ServerOptions](.././http/~/ServerOptions "ServerOptions")

No documentation available

*   [IncomingMessage](.././http/~/ServerOptions#property_incomingmessage)
*   [ServerResponse](.././http/~/ServerOptions#property_serverresponse)
*   [connectionsCheckingInterval](.././http/~/ServerOptions#property_connectionscheckinginterval)
*   [highWaterMark](.././http/~/ServerOptions#property_highwatermark)
*   [insecureHTTPParser](.././http/~/ServerOptions#property_insecurehttpparser)
*   [joinDuplicateHeaders](.././http/~/ServerOptions#property_joinduplicateheaders)
*   [keepAlive](.././http/~/ServerOptions#property_keepalive)
*   [keepAliveInitialDelay](.././http/~/ServerOptions#property_keepaliveinitialdelay)
*   [keepAliveTimeout](.././http/~/ServerOptions#property_keepalivetimeout)
*   [maxHeaderSize](.././http/~/ServerOptions#property_maxheadersize)
*   [noDelay](.././http/~/ServerOptions#property_nodelay)
*   [requestTimeout](.././http/~/ServerOptions#property_requesttimeout)
*   [uniqueHeaders](.././http/~/ServerOptions#property_uniqueheaders)

### Type Aliases [#](<#Type Aliases>)

T

[OutgoingHttpHeader](.././http/~/OutgoingHttpHeader "OutgoingHttpHeader")

No documentation available

T

[RequestListener](.././http/~/RequestListener "RequestListener")

No documentation available

### Variables [#](#Variables)

v

[CloseEvent](.././http/~/CloseEvent "CloseEvent")

No documentation available

v

[globalAgent](.././http/~/globalAgent "globalAgent")

Global instance of `Agent` which is used as the default for all HTTP client requests. Diverges from a default `Agent` configuration by having `keepAlive` enabled and a `timeout` of 5 seconds.

v

[maxHeaderSize](.././http/~/maxHeaderSize "maxHeaderSize")

Read-only property specifying the maximum allowed size of HTTP headers in bytes. Defaults to 16KB. Configurable using the `--max-http-header-size` CLI option.

v

[MessageEvent](.././http/~/MessageEvent "MessageEvent")

No documentation available

v

[METHODS](.././http/~/METHODS "METHODS")

No documentation available

v

[STATUS\_CODES](.././http/~/STATUS_CODES "STATUS_CODES")

No documentation available

v

[WebSocket](.././http/~/WebSocket "WebSocket")

A browser-compatible implementation of [WebSocket](https://nodejs.org/docs/latest/api/http.html#websocket).
