---
title: "http2 - Node documentation"
source: "https://docs.deno.com/api/node/http2/"
canonical_url: "https://docs.deno.com/api/node/http2/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:07:26.876Z"
content_hash: "19a176d8afb77d7f437c7089fcd96518a794e5b051b58a3f3de93eb671f635e1"
menu_path: ["http2 - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/node/http/index.md", "title": "http - Node documentation"}
nav_next: {"path": "deno/api/node/https/index.md", "title": "https - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:http2";
```

The `node:http2` module provides an implementation of the [HTTP/2](https://tools.ietf.org/html/rfc7540) protocol. It can be accessed using:

```js
import http2 from 'node:http2';
```

c

[Http2ServerRequest](.././http2/~/Http2ServerRequest "Http2ServerRequest")

A `Http2ServerRequest` object is created by Server or SecureServer and passed as the first argument to the `'request'` event. It may be used to access a request status, headers, and data.

-   [aborted](.././http2/~/Http2ServerRequest#property_aborted)
-   [addListener](.././http2/~/Http2ServerRequest#method_addlistener_0)
-   [authority](.././http2/~/Http2ServerRequest#property_authority)
-   [complete](.././http2/~/Http2ServerRequest#property_complete)
-   [connection](.././http2/~/Http2ServerRequest#property_connection)
-   [emit](.././http2/~/Http2ServerRequest#method_emit_0)
-   [headers](.././http2/~/Http2ServerRequest#property_headers)
-   [httpVersion](.././http2/~/Http2ServerRequest#property_httpversion)
-   [httpVersionMajor](.././http2/~/Http2ServerRequest#property_httpversionmajor)
-   [httpVersionMinor](.././http2/~/Http2ServerRequest#property_httpversionminor)
-   [method](.././http2/~/Http2ServerRequest#property_method)
-   [on](.././http2/~/Http2ServerRequest#method_on_0)
-   [once](.././http2/~/Http2ServerRequest#method_once_0)
-   [prependListener](.././http2/~/Http2ServerRequest#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/Http2ServerRequest#method_prependoncelistener_0)
-   [rawHeaders](.././http2/~/Http2ServerRequest#property_rawheaders)
-   [rawTrailers](.././http2/~/Http2ServerRequest#property_rawtrailers)
-   [read](.././http2/~/Http2ServerRequest#method_read_0)
-   [scheme](.././http2/~/Http2ServerRequest#property_scheme)
-   [setTimeout](.././http2/~/Http2ServerRequest#method_settimeout_0)
-   [socket](.././http2/~/Http2ServerRequest#property_socket)
-   [stream](.././http2/~/Http2ServerRequest#property_stream)
-   [trailers](.././http2/~/Http2ServerRequest#property_trailers)
-   [url](.././http2/~/Http2ServerRequest#property_url)

c

[Http2ServerResponse](.././http2/~/Http2ServerResponse "Http2ServerResponse")

This object is created internally by an HTTP server, not by the user. It is passed as the second parameter to the `'request'` event.

-   [addListener](.././http2/~/Http2ServerResponse#method_addlistener_0)
-   [addTrailers](.././http2/~/Http2ServerResponse#method_addtrailers_0)
-   [appendHeader](.././http2/~/Http2ServerResponse#method_appendheader_0)
-   [connection](.././http2/~/Http2ServerResponse#property_connection)
-   [createPushResponse](.././http2/~/Http2ServerResponse#method_createpushresponse_0)
-   [emit](.././http2/~/Http2ServerResponse#method_emit_0)
-   [end](.././http2/~/Http2ServerResponse#method_end_0)
-   [finished](.././http2/~/Http2ServerResponse#property_finished)
-   [getHeader](.././http2/~/Http2ServerResponse#method_getheader_0)
-   [getHeaderNames](.././http2/~/Http2ServerResponse#method_getheadernames_0)
-   [getHeaders](.././http2/~/Http2ServerResponse#method_getheaders_0)
-   [hasHeader](.././http2/~/Http2ServerResponse#method_hasheader_0)
-   [headersSent](.././http2/~/Http2ServerResponse#property_headerssent)
-   [on](.././http2/~/Http2ServerResponse#method_on_0)
-   [once](.././http2/~/Http2ServerResponse#method_once_0)
-   [prependListener](.././http2/~/Http2ServerResponse#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/Http2ServerResponse#method_prependoncelistener_0)
-   [removeHeader](.././http2/~/Http2ServerResponse#method_removeheader_0)
-   [req](.././http2/~/Http2ServerResponse#property_req)
-   [sendDate](.././http2/~/Http2ServerResponse#property_senddate)
-   [setHeader](.././http2/~/Http2ServerResponse#method_setheader_0)
-   [setTimeout](.././http2/~/Http2ServerResponse#method_settimeout_0)
-   [socket](.././http2/~/Http2ServerResponse#property_socket)
-   [statusCode](.././http2/~/Http2ServerResponse#property_statuscode)
-   [statusMessage](.././http2/~/Http2ServerResponse#property_statusmessage)
-   [stream](.././http2/~/Http2ServerResponse#property_stream)
-   [write](.././http2/~/Http2ServerResponse#method_write_0)
-   [writeContinue](.././http2/~/Http2ServerResponse#method_writecontinue_0)
-   [writeEarlyHints](.././http2/~/Http2ServerResponse#method_writeearlyhints_0)
-   [writeHead](.././http2/~/Http2ServerResponse#method_writehead_0)

f

[connect](.././http2/~/connect "connect")

Returns a `ClientHttp2Session` instance.

f

[createSecureServer](.././http2/~/createSecureServer "createSecureServer")

Returns a `tls.Server` instance that creates and manages `Http2Session` instances.

f

[createServer](.././http2/~/createServer "createServer")

Returns a `net.Server` instance that creates and manages `Http2Session` instances.

f

[getDefaultSettings](.././http2/~/getDefaultSettings "getDefaultSettings")

No documentation available

f

[getPackedSettings](.././http2/~/getPackedSettings "getPackedSettings")

No documentation available

f

[getUnpackedSettings](.././http2/~/getUnpackedSettings "getUnpackedSettings")

No documentation available

f

[performServerHandshake](.././http2/~/performServerHandshake "performServerHandshake")

Create an HTTP/2 server session from an existing socket.

I

[AlternativeServiceOptions](.././http2/~/AlternativeServiceOptions "AlternativeServiceOptions")

No documentation available

-   [origin](.././http2/~/AlternativeServiceOptions#property_origin)

I

[ClientHttp2Session](.././http2/~/ClientHttp2Session "ClientHttp2Session")

No documentation available

-   [addListener](.././http2/~/ClientHttp2Session#method_addlistener_0)
-   [emit](.././http2/~/ClientHttp2Session#method_emit_0)
-   [on](.././http2/~/ClientHttp2Session#method_on_0)
-   [once](.././http2/~/ClientHttp2Session#method_once_0)
-   [prependListener](.././http2/~/ClientHttp2Session#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/ClientHttp2Session#method_prependoncelistener_0)
-   [request](.././http2/~/ClientHttp2Session#method_request_0)

I

[ClientHttp2Stream](.././http2/~/ClientHttp2Stream "ClientHttp2Stream")

No documentation available

-   [addListener](.././http2/~/ClientHttp2Stream#method_addlistener_0)
-   [emit](.././http2/~/ClientHttp2Stream#method_emit_0)
-   [on](.././http2/~/ClientHttp2Stream#method_on_0)
-   [once](.././http2/~/ClientHttp2Stream#method_once_0)
-   [prependListener](.././http2/~/ClientHttp2Stream#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/ClientHttp2Stream#method_prependoncelistener_0)

I

[ClientSessionOptions](.././http2/~/ClientSessionOptions "ClientSessionOptions")

No documentation available

-   [createConnection](.././http2/~/ClientSessionOptions#property_createconnection)
-   [maxReservedRemoteStreams](.././http2/~/ClientSessionOptions#property_maxreservedremotestreams)
-   [protocol](.././http2/~/ClientSessionOptions#property_protocol)

I

[ClientSessionRequestOptions](.././http2/~/ClientSessionRequestOptions "ClientSessionRequestOptions")

No documentation available

-   [endStream](.././http2/~/ClientSessionRequestOptions#property_endstream)
-   [exclusive](.././http2/~/ClientSessionRequestOptions#property_exclusive)
-   [parent](.././http2/~/ClientSessionRequestOptions#property_parent)
-   [signal](.././http2/~/ClientSessionRequestOptions#property_signal)
-   [waitForTrailers](.././http2/~/ClientSessionRequestOptions#property_waitfortrailers)
-   [weight](.././http2/~/ClientSessionRequestOptions#property_weight)

I

[Http2SecureServer](.././http2/~/Http2SecureServer "Http2SecureServer")

No documentation available

-   [addListener](.././http2/~/Http2SecureServer#method_addlistener_0)
-   [emit](.././http2/~/Http2SecureServer#method_emit_0)
-   [on](.././http2/~/Http2SecureServer#method_on_0)
-   [once](.././http2/~/Http2SecureServer#method_once_0)
-   [prependListener](.././http2/~/Http2SecureServer#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/Http2SecureServer#method_prependoncelistener_0)

I

[Http2Server](.././http2/~/Http2Server "Http2Server")

No documentation available

-   [addListener](.././http2/~/Http2Server#method_addlistener_0)
-   [emit](.././http2/~/Http2Server#method_emit_0)
-   [on](.././http2/~/Http2Server#method_on_0)
-   [once](.././http2/~/Http2Server#method_once_0)
-   [prependListener](.././http2/~/Http2Server#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/Http2Server#method_prependoncelistener_0)

I

[HTTP2ServerCommon](.././http2/~/HTTP2ServerCommon "HTTP2ServerCommon")

No documentation available

-   [setTimeout](.././http2/~/HTTP2ServerCommon#method_settimeout_0)
-   [updateSettings](.././http2/~/HTTP2ServerCommon#method_updatesettings_0)

I

[Http2Session](.././http2/~/Http2Session "Http2Session")

No documentation available

-   [addListener](.././http2/~/Http2Session#method_addlistener_0)
-   [alpnProtocol](.././http2/~/Http2Session#property_alpnprotocol)
-   [close](.././http2/~/Http2Session#method_close_0)
-   [closed](.././http2/~/Http2Session#property_closed)
-   [connecting](.././http2/~/Http2Session#property_connecting)
-   [destroy](.././http2/~/Http2Session#method_destroy_0)
-   [destroyed](.././http2/~/Http2Session#property_destroyed)
-   [emit](.././http2/~/Http2Session#method_emit_0)
-   [encrypted](.././http2/~/Http2Session#property_encrypted)
-   [goaway](.././http2/~/Http2Session#method_goaway_0)
-   [localSettings](.././http2/~/Http2Session#property_localsettings)
-   [on](.././http2/~/Http2Session#method_on_0)
-   [once](.././http2/~/Http2Session#method_once_0)
-   [originSet](.././http2/~/Http2Session#property_originset)
-   [pendingSettingsAck](.././http2/~/Http2Session#property_pendingsettingsack)
-   [ping](.././http2/~/Http2Session#method_ping_0)
-   [prependListener](.././http2/~/Http2Session#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/Http2Session#method_prependoncelistener_0)
-   [ref](.././http2/~/Http2Session#method_ref_0)
-   [remoteSettings](.././http2/~/Http2Session#property_remotesettings)
-   [setLocalWindowSize](.././http2/~/Http2Session#method_setlocalwindowsize_0)
-   [setTimeout](.././http2/~/Http2Session#method_settimeout_0)
-   [settings](.././http2/~/Http2Session#method_settings_0)
-   [socket](.././http2/~/Http2Session#property_socket)
-   [state](.././http2/~/Http2Session#property_state)
-   [type](.././http2/~/Http2Session#property_type)
-   [unref](.././http2/~/Http2Session#method_unref_0)

I

[Http2Stream](.././http2/~/Http2Stream "Http2Stream")

No documentation available

-   [aborted](.././http2/~/Http2Stream#property_aborted)
-   [addListener](.././http2/~/Http2Stream#method_addlistener_0)
-   [bufferSize](.././http2/~/Http2Stream#property_buffersize)
-   [close](.././http2/~/Http2Stream#method_close_0)
-   [closed](.././http2/~/Http2Stream#property_closed)
-   [destroyed](.././http2/~/Http2Stream#property_destroyed)
-   [emit](.././http2/~/Http2Stream#method_emit_0)
-   [endAfterHeaders](.././http2/~/Http2Stream#property_endafterheaders)
-   [id](.././http2/~/Http2Stream#property_id)
-   [on](.././http2/~/Http2Stream#method_on_0)
-   [once](.././http2/~/Http2Stream#method_once_0)
-   [pending](.././http2/~/Http2Stream#property_pending)
-   [prependListener](.././http2/~/Http2Stream#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/Http2Stream#method_prependoncelistener_0)
-   [priority](.././http2/~/Http2Stream#method_priority_0)
-   [rstCode](.././http2/~/Http2Stream#property_rstcode)
-   [sendTrailers](.././http2/~/Http2Stream#method_sendtrailers_0)
-   [sentHeaders](.././http2/~/Http2Stream#property_sentheaders)
-   [sentInfoHeaders](.././http2/~/Http2Stream#property_sentinfoheaders)
-   [sentTrailers](.././http2/~/Http2Stream#property_senttrailers)
-   [session](.././http2/~/Http2Stream#property_session)
-   [setTimeout](.././http2/~/Http2Stream#method_settimeout_0)
-   [state](.././http2/~/Http2Stream#property_state)

I

[IncomingHttpHeaders](.././http2/~/IncomingHttpHeaders "IncomingHttpHeaders")

No documentation available

-   [:authority](.././http2/~/IncomingHttpHeaders#property_:authority)
-   [:method](.././http2/~/IncomingHttpHeaders#property_:method)
-   [:path](.././http2/~/IncomingHttpHeaders#property_:path)
-   [:scheme](.././http2/~/IncomingHttpHeaders#property_:scheme)

I

[IncomingHttpStatusHeader](.././http2/~/IncomingHttpStatusHeader "IncomingHttpStatusHeader")

No documentation available

-   [:status](.././http2/~/IncomingHttpStatusHeader#property_:status)

I

[OutgoingHttpHeaders](.././http/~/OutgoingHttpHeaders "OutgoingHttpHeaders")

No documentation available

-   [accept](.././http/~/OutgoingHttpHeaders#property_accept)
-   [accept-charset](.././http/~/OutgoingHttpHeaders#property_accept-charset)
-   [accept-encoding](.././http/~/OutgoingHttpHeaders#property_accept-encoding)
-   [accept-language](.././http/~/OutgoingHttpHeaders#property_accept-language)
-   [accept-ranges](.././http/~/OutgoingHttpHeaders#property_accept-ranges)
-   [access-control-allow-credentials](.././http/~/OutgoingHttpHeaders#property_access-control-allow-credentials)
-   [access-control-allow-headers](.././http/~/OutgoingHttpHeaders#property_access-control-allow-headers)
-   [access-control-allow-methods](.././http/~/OutgoingHttpHeaders#property_access-control-allow-methods)
-   [access-control-allow-origin](.././http/~/OutgoingHttpHeaders#property_access-control-allow-origin)
-   [access-control-expose-headers](.././http/~/OutgoingHttpHeaders#property_access-control-expose-headers)
-   [access-control-max-age](.././http/~/OutgoingHttpHeaders#property_access-control-max-age)
-   [access-control-request-headers](.././http/~/OutgoingHttpHeaders#property_access-control-request-headers)
-   [access-control-request-method](.././http/~/OutgoingHttpHeaders#property_access-control-request-method)
-   [age](.././http/~/OutgoingHttpHeaders#property_age)
-   [allow](.././http/~/OutgoingHttpHeaders#property_allow)
-   [authorization](.././http/~/OutgoingHttpHeaders#property_authorization)
-   [cache-control](.././http/~/OutgoingHttpHeaders#property_cache-control)
-   [cdn-cache-control](.././http/~/OutgoingHttpHeaders#property_cdn-cache-control)
-   [connection](.././http/~/OutgoingHttpHeaders#property_connection)
-   [content-disposition](.././http/~/OutgoingHttpHeaders#property_content-disposition)
-   [content-encoding](.././http/~/OutgoingHttpHeaders#property_content-encoding)
-   [content-language](.././http/~/OutgoingHttpHeaders#property_content-language)
-   [content-length](.././http/~/OutgoingHttpHeaders#property_content-length)
-   [content-location](.././http/~/OutgoingHttpHeaders#property_content-location)
-   [content-range](.././http/~/OutgoingHttpHeaders#property_content-range)
-   [content-security-policy](.././http/~/OutgoingHttpHeaders#property_content-security-policy)
-   [content-security-policy-report-only](.././http/~/OutgoingHttpHeaders#property_content-security-policy-report-only)
-   [content-type](.././http/~/OutgoingHttpHeaders#property_content-type)
-   [cookie](.././http/~/OutgoingHttpHeaders#property_cookie)
-   [date](.././http/~/OutgoingHttpHeaders#property_date)
-   [dav](.././http/~/OutgoingHttpHeaders#property_dav)
-   [dnt](.././http/~/OutgoingHttpHeaders#property_dnt)
-   [etag](.././http/~/OutgoingHttpHeaders#property_etag)
-   [expect](.././http/~/OutgoingHttpHeaders#property_expect)
-   [expires](.././http/~/OutgoingHttpHeaders#property_expires)
-   [forwarded](.././http/~/OutgoingHttpHeaders#property_forwarded)
-   [from](.././http/~/OutgoingHttpHeaders#property_from)
-   [host](.././http/~/OutgoingHttpHeaders#property_host)
-   [if-match](.././http/~/OutgoingHttpHeaders#property_if-match)
-   [if-modified-since](.././http/~/OutgoingHttpHeaders#property_if-modified-since)
-   [if-none-match](.././http/~/OutgoingHttpHeaders#property_if-none-match)
-   [if-range](.././http/~/OutgoingHttpHeaders#property_if-range)
-   [if-unmodified-since](.././http/~/OutgoingHttpHeaders#property_if-unmodified-since)
-   [last-modified](.././http/~/OutgoingHttpHeaders#property_last-modified)
-   [link](.././http/~/OutgoingHttpHeaders#property_link)
-   [location](.././http/~/OutgoingHttpHeaders#property_location)
-   [max-forwards](.././http/~/OutgoingHttpHeaders#property_max-forwards)
-   [origin](.././http/~/OutgoingHttpHeaders#property_origin)
-   [pragma](.././http/~/OutgoingHttpHeaders#property_pragma)
-   [proxy-authenticate](.././http/~/OutgoingHttpHeaders#property_proxy-authenticate)
-   [proxy-authorization](.././http/~/OutgoingHttpHeaders#property_proxy-authorization)
-   [public-key-pins](.././http/~/OutgoingHttpHeaders#property_public-key-pins)
-   [public-key-pins-report-only](.././http/~/OutgoingHttpHeaders#property_public-key-pins-report-only)
-   [range](.././http/~/OutgoingHttpHeaders#property_range)
-   [referer](.././http/~/OutgoingHttpHeaders#property_referer)
-   [referrer-policy](.././http/~/OutgoingHttpHeaders#property_referrer-policy)
-   [refresh](.././http/~/OutgoingHttpHeaders#property_refresh)
-   [retry-after](.././http/~/OutgoingHttpHeaders#property_retry-after)
-   [sec-websocket-accept](.././http/~/OutgoingHttpHeaders#property_sec-websocket-accept)
-   [sec-websocket-extensions](.././http/~/OutgoingHttpHeaders#property_sec-websocket-extensions)
-   [sec-websocket-key](.././http/~/OutgoingHttpHeaders#property_sec-websocket-key)
-   [sec-websocket-protocol](.././http/~/OutgoingHttpHeaders#property_sec-websocket-protocol)
-   [sec-websocket-version](.././http/~/OutgoingHttpHeaders#property_sec-websocket-version)
-   [server](.././http/~/OutgoingHttpHeaders#property_server)
-   [set-cookie](.././http/~/OutgoingHttpHeaders#property_set-cookie)
-   [strict-transport-security](.././http/~/OutgoingHttpHeaders#property_strict-transport-security)
-   [te](.././http/~/OutgoingHttpHeaders#property_te)
-   [trailer](.././http/~/OutgoingHttpHeaders#property_trailer)
-   [transfer-encoding](.././http/~/OutgoingHttpHeaders#property_transfer-encoding)
-   [upgrade](.././http/~/OutgoingHttpHeaders#property_upgrade)
-   [upgrade-insecure-requests](.././http/~/OutgoingHttpHeaders#property_upgrade-insecure-requests)
-   [user-agent](.././http/~/OutgoingHttpHeaders#property_user-agent)
-   [vary](.././http/~/OutgoingHttpHeaders#property_vary)
-   [via](.././http/~/OutgoingHttpHeaders#property_via)
-   [warning](.././http/~/OutgoingHttpHeaders#property_warning)
-   [www-authenticate](.././http/~/OutgoingHttpHeaders#property_www-authenticate)
-   [x-content-type-options](.././http/~/OutgoingHttpHeaders#property_x-content-type-options)
-   [x-dns-prefetch-control](.././http/~/OutgoingHttpHeaders#property_x-dns-prefetch-control)
-   [x-frame-options](.././http/~/OutgoingHttpHeaders#property_x-frame-options)
-   [x-xss-protection](.././http/~/OutgoingHttpHeaders#property_x-xss-protection)

I

[SecureClientSessionOptions](.././http2/~/SecureClientSessionOptions "SecureClientSessionOptions")

No documentation available

I

[SecureServerOptions](.././http2/~/SecureServerOptions "SecureServerOptions")

No documentation available

-   [allowHTTP1](.././http2/~/SecureServerOptions#property_allowhttp1)
-   [origins](.././http2/~/SecureServerOptions#property_origins)

I

[SecureServerSessionOptions](.././http2/~/SecureServerSessionOptions "SecureServerSessionOptions")

No documentation available

I

[ServerHttp2Session](.././http2/~/ServerHttp2Session "ServerHttp2Session")

No documentation available

-   [addListener](.././http2/~/ServerHttp2Session#method_addlistener_0)
-   [altsvc](.././http2/~/ServerHttp2Session#method_altsvc_0)
-   [emit](.././http2/~/ServerHttp2Session#method_emit_0)
-   [on](.././http2/~/ServerHttp2Session#method_on_0)
-   [once](.././http2/~/ServerHttp2Session#method_once_0)
-   [origin](.././http2/~/ServerHttp2Session#method_origin_0)
-   [prependListener](.././http2/~/ServerHttp2Session#method_prependlistener_0)
-   [prependOnceListener](.././http2/~/ServerHttp2Session#method_prependoncelistener_0)
-   [server](.././http2/~/ServerHttp2Session#property_server)

I

[ServerHttp2Stream](.././http2/~/ServerHttp2Stream "ServerHttp2Stream")

No documentation available

-   [additionalHeaders](.././http2/~/ServerHttp2Stream#method_additionalheaders_0)
-   [headersSent](.././http2/~/ServerHttp2Stream#property_headerssent)
-   [pushAllowed](.././http2/~/ServerHttp2Stream#property_pushallowed)
-   [pushStream](.././http2/~/ServerHttp2Stream#method_pushstream_0)
-   [respond](.././http2/~/ServerHttp2Stream#method_respond_0)
-   [respondWithFD](.././http2/~/ServerHttp2Stream#method_respondwithfd_0)
-   [respondWithFile](.././http2/~/ServerHttp2Stream#method_respondwithfile_0)

I

[ServerOptions](.././http2/~/ServerOptions "ServerOptions")

No documentation available

-   [streamResetBurst](.././http2/~/ServerOptions#property_streamresetburst)
-   [streamResetRate](.././http2/~/ServerOptions#property_streamresetrate)

I

[ServerSessionOptions](.././http2/~/ServerSessionOptions "ServerSessionOptions")

No documentation available

-   [Http1IncomingMessage](.././http2/~/ServerSessionOptions#property_http1incomingmessage)
-   [Http1ServerResponse](.././http2/~/ServerSessionOptions#property_http1serverresponse)
-   [Http2ServerRequest](.././http2/~/ServerSessionOptions#property_http2serverrequest)
-   [Http2ServerResponse](.././http2/~/ServerSessionOptions#property_http2serverresponse)

I

[ServerStreamFileResponseOptions](.././http2/~/ServerStreamFileResponseOptions "ServerStreamFileResponseOptions")

No documentation available

-   [length](.././http2/~/ServerStreamFileResponseOptions#property_length)
-   [offset](.././http2/~/ServerStreamFileResponseOptions#property_offset)
-   [statCheck](.././http2/~/ServerStreamFileResponseOptions#method_statcheck_0)
-   [waitForTrailers](.././http2/~/ServerStreamFileResponseOptions#property_waitfortrailers)

I

[ServerStreamFileResponseOptionsWithError](.././http2/~/ServerStreamFileResponseOptionsWithError "ServerStreamFileResponseOptionsWithError")

No documentation available

-   [onError](.././http2/~/ServerStreamFileResponseOptionsWithError#method_onerror_0)

I

[ServerStreamResponseOptions](.././http2/~/ServerStreamResponseOptions "ServerStreamResponseOptions")

No documentation available

-   [endStream](.././http2/~/ServerStreamResponseOptions#property_endstream)
-   [waitForTrailers](.././http2/~/ServerStreamResponseOptions#property_waitfortrailers)

I

[SessionOptions](.././http2/~/SessionOptions "SessionOptions")

No documentation available

-   [maxDeflateDynamicTableSize](.././http2/~/SessionOptions#property_maxdeflatedynamictablesize)
-   [maxHeaderListPairs](.././http2/~/SessionOptions#property_maxheaderlistpairs)
-   [maxOutstandingPings](.././http2/~/SessionOptions#property_maxoutstandingpings)
-   [maxSendHeaderBlockLength](.././http2/~/SessionOptions#property_maxsendheaderblocklength)
-   [maxSessionMemory](.././http2/~/SessionOptions#property_maxsessionmemory)
-   [paddingStrategy](.././http2/~/SessionOptions#property_paddingstrategy)
-   [peerMaxConcurrentStreams](.././http2/~/SessionOptions#property_peermaxconcurrentstreams)
-   [remoteCustomSettings](.././http2/~/SessionOptions#property_remotecustomsettings)
-   [selectPadding](.././http2/~/SessionOptions#method_selectpadding_0)
-   [settings](.././http2/~/SessionOptions#property_settings)
-   [unknownProtocolTimeout](.././http2/~/SessionOptions#property_unknownprotocoltimeout)

I

[SessionState](.././http2/~/SessionState "SessionState")

No documentation available

-   [deflateDynamicTableSize](.././http2/~/SessionState#property_deflatedynamictablesize)
-   [effectiveLocalWindowSize](.././http2/~/SessionState#property_effectivelocalwindowsize)
-   [effectiveRecvDataLength](.././http2/~/SessionState#property_effectiverecvdatalength)
-   [inflateDynamicTableSize](.././http2/~/SessionState#property_inflatedynamictablesize)
-   [lastProcStreamID](.././http2/~/SessionState#property_lastprocstreamid)
-   [localWindowSize](.././http2/~/SessionState#property_localwindowsize)
-   [nextStreamID](.././http2/~/SessionState#property_nextstreamid)
-   [outboundQueueSize](.././http2/~/SessionState#property_outboundqueuesize)
-   [remoteWindowSize](.././http2/~/SessionState#property_remotewindowsize)

I

[Settings](.././http2/~/Settings "Settings")

No documentation available

-   [enableConnectProtocol](.././http2/~/Settings#property_enableconnectprotocol)
-   [enablePush](.././http2/~/Settings#property_enablepush)
-   [headerTableSize](.././http2/~/Settings#property_headertablesize)
-   [initialWindowSize](.././http2/~/Settings#property_initialwindowsize)
-   [maxConcurrentStreams](.././http2/~/Settings#property_maxconcurrentstreams)
-   [maxFrameSize](.././http2/~/Settings#property_maxframesize)
-   [maxHeaderListSize](.././http2/~/Settings#property_maxheaderlistsize)

I

[StatOptions](.././http2/~/StatOptions "StatOptions")

No documentation available

-   [length](.././http2/~/StatOptions#property_length)
-   [offset](.././http2/~/StatOptions#property_offset)

I

[StreamPriorityOptions](.././http2/~/StreamPriorityOptions "StreamPriorityOptions")

No documentation available

-   [exclusive](.././http2/~/StreamPriorityOptions#property_exclusive)
-   [parent](.././http2/~/StreamPriorityOptions#property_parent)
-   [silent](.././http2/~/StreamPriorityOptions#property_silent)
-   [weight](.././http2/~/StreamPriorityOptions#property_weight)

I

[StreamState](.././http2/~/StreamState "StreamState")

No documentation available

-   [localClose](.././http2/~/StreamState#property_localclose)
-   [localWindowSize](.././http2/~/StreamState#property_localwindowsize)
-   [remoteClose](.././http2/~/StreamState#property_remoteclose)
-   [state](.././http2/~/StreamState#property_state)
-   [sumDependencyWeight](.././http2/~/StreamState#property_sumdependencyweight)
-   [weight](.././http2/~/StreamState#property_weight)

N

[constants](.././http2/~/constants "constants")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_ENABLE\_PUSH](.././http2/~/constants.DEFAULT_SETTINGS_ENABLE_PUSH "constants.DEFAULT_SETTINGS_ENABLE_PUSH")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_HEADER\_TABLE\_SIZE](.././http2/~/constants.DEFAULT_SETTINGS_HEADER_TABLE_SIZE "constants.DEFAULT_SETTINGS_HEADER_TABLE_SIZE")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_INITIAL\_WINDOW\_SIZE](.././http2/~/constants.DEFAULT_SETTINGS_INITIAL_WINDOW_SIZE "constants.DEFAULT_SETTINGS_INITIAL_WINDOW_SIZE")

No documentation available

v

[constants.DEFAULT\_SETTINGS\_MAX\_FRAME\_SIZE](.././http2/~/constants.DEFAULT_SETTINGS_MAX_FRAME_SIZE "constants.DEFAULT_SETTINGS_MAX_FRAME_SIZE")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT](.././http2/~/constants.HTTP2_HEADER_ACCEPT "constants.HTTP2_HEADER_ACCEPT")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_CHARSET](.././http2/~/constants.HTTP2_HEADER_ACCEPT_CHARSET "constants.HTTP2_HEADER_ACCEPT_CHARSET")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_ENCODING](.././http2/~/constants.HTTP2_HEADER_ACCEPT_ENCODING "constants.HTTP2_HEADER_ACCEPT_ENCODING")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_LANGUAGE](.././http2/~/constants.HTTP2_HEADER_ACCEPT_LANGUAGE "constants.HTTP2_HEADER_ACCEPT_LANGUAGE")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCEPT\_RANGES](.././http2/~/constants.HTTP2_HEADER_ACCEPT_RANGES "constants.HTTP2_HEADER_ACCEPT_RANGES")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_CREDENTIALS](.././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_HEADERS](.././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_HEADERS "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_HEADERS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_METHODS](.././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_METHODS "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_METHODS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_ALLOW\_ORIGIN](.././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_ORIGIN "constants.HTTP2_HEADER_ACCESS_CONTROL_ALLOW_ORIGIN")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_EXPOSE\_HEADERS](.././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_EXPOSE_HEADERS "constants.HTTP2_HEADER_ACCESS_CONTROL_EXPOSE_HEADERS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_REQUEST\_HEADERS](.././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_HEADERS "constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_HEADERS")

No documentation available

v

[constants.HTTP2\_HEADER\_ACCESS\_CONTROL\_REQUEST\_METHOD](.././http2/~/constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_METHOD "constants.HTTP2_HEADER_ACCESS_CONTROL_REQUEST_METHOD")

No documentation available

v

[constants.HTTP2\_HEADER\_AGE](.././http2/~/constants.HTTP2_HEADER_AGE "constants.HTTP2_HEADER_AGE")

No documentation available

v

[constants.HTTP2\_HEADER\_ALLOW](.././http2/~/constants.HTTP2_HEADER_ALLOW "constants.HTTP2_HEADER_ALLOW")

No documentation available

v

[constants.HTTP2\_HEADER\_AUTHORITY](.././http2/~/constants.HTTP2_HEADER_AUTHORITY "constants.HTTP2_HEADER_AUTHORITY")

No documentation available

v

[constants.HTTP2\_HEADER\_AUTHORIZATION](.././http2/~/constants.HTTP2_HEADER_AUTHORIZATION "constants.HTTP2_HEADER_AUTHORIZATION")

No documentation available

v

[constants.HTTP2\_HEADER\_CACHE\_CONTROL](.././http2/~/constants.HTTP2_HEADER_CACHE_CONTROL "constants.HTTP2_HEADER_CACHE_CONTROL")

No documentation available

v

[constants.HTTP2\_HEADER\_CONNECTION](.././http2/~/constants.HTTP2_HEADER_CONNECTION "constants.HTTP2_HEADER_CONNECTION")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_DISPOSITION](.././http2/~/constants.HTTP2_HEADER_CONTENT_DISPOSITION "constants.HTTP2_HEADER_CONTENT_DISPOSITION")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_ENCODING](.././http2/~/constants.HTTP2_HEADER_CONTENT_ENCODING "constants.HTTP2_HEADER_CONTENT_ENCODING")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_LANGUAGE](.././http2/~/constants.HTTP2_HEADER_CONTENT_LANGUAGE "constants.HTTP2_HEADER_CONTENT_LANGUAGE")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_LENGTH](.././http2/~/constants.HTTP2_HEADER_CONTENT_LENGTH "constants.HTTP2_HEADER_CONTENT_LENGTH")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_LOCATION](.././http2/~/constants.HTTP2_HEADER_CONTENT_LOCATION "constants.HTTP2_HEADER_CONTENT_LOCATION")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_MD5](.././http2/~/constants.HTTP2_HEADER_CONTENT_MD5 "constants.HTTP2_HEADER_CONTENT_MD5")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_RANGE](.././http2/~/constants.HTTP2_HEADER_CONTENT_RANGE "constants.HTTP2_HEADER_CONTENT_RANGE")

No documentation available

v

[constants.HTTP2\_HEADER\_CONTENT\_TYPE](.././http2/~/constants.HTTP2_HEADER_CONTENT_TYPE "constants.HTTP2_HEADER_CONTENT_TYPE")

No documentation available

v

[constants.HTTP2\_HEADER\_COOKIE](.././http2/~/constants.HTTP2_HEADER_COOKIE "constants.HTTP2_HEADER_COOKIE")

No documentation available

v

[constants.HTTP2\_HEADER\_DATE](.././http2/~/constants.HTTP2_HEADER_DATE "constants.HTTP2_HEADER_DATE")

No documentation available

v

[constants.HTTP2\_HEADER\_ETAG](.././http2/~/constants.HTTP2_HEADER_ETAG "constants.HTTP2_HEADER_ETAG")

No documentation available

v

[constants.HTTP2\_HEADER\_EXPECT](.././http2/~/constants.HTTP2_HEADER_EXPECT "constants.HTTP2_HEADER_EXPECT")

No documentation available

v

[constants.HTTP2\_HEADER\_EXPIRES](.././http2/~/constants.HTTP2_HEADER_EXPIRES "constants.HTTP2_HEADER_EXPIRES")

No documentation available

v

[constants.HTTP2\_HEADER\_FROM](.././http2/~/constants.HTTP2_HEADER_FROM "constants.HTTP2_HEADER_FROM")

No documentation available

v

[constants.HTTP2\_HEADER\_HOST](.././http2/~/constants.HTTP2_HEADER_HOST "constants.HTTP2_HEADER_HOST")

No documentation available

v

[constants.HTTP2\_HEADER\_HTTP2\_SETTINGS](.././http2/~/constants.HTTP2_HEADER_HTTP2_SETTINGS "constants.HTTP2_HEADER_HTTP2_SETTINGS")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_MATCH](.././http2/~/constants.HTTP2_HEADER_IF_MATCH "constants.HTTP2_HEADER_IF_MATCH")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_MODIFIED\_SINCE](.././http2/~/constants.HTTP2_HEADER_IF_MODIFIED_SINCE "constants.HTTP2_HEADER_IF_MODIFIED_SINCE")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_NONE\_MATCH](.././http2/~/constants.HTTP2_HEADER_IF_NONE_MATCH "constants.HTTP2_HEADER_IF_NONE_MATCH")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_RANGE](.././http2/~/constants.HTTP2_HEADER_IF_RANGE "constants.HTTP2_HEADER_IF_RANGE")

No documentation available

v

[constants.HTTP2\_HEADER\_IF\_UNMODIFIED\_SINCE](.././http2/~/constants.HTTP2_HEADER_IF_UNMODIFIED_SINCE "constants.HTTP2_HEADER_IF_UNMODIFIED_SINCE")

No documentation available

v

[constants.HTTP2\_HEADER\_KEEP\_ALIVE](.././http2/~/constants.HTTP2_HEADER_KEEP_ALIVE "constants.HTTP2_HEADER_KEEP_ALIVE")

No documentation available

v

[constants.HTTP2\_HEADER\_LAST\_MODIFIED](.././http2/~/constants.HTTP2_HEADER_LAST_MODIFIED "constants.HTTP2_HEADER_LAST_MODIFIED")

No documentation available

v

[constants.HTTP2\_HEADER\_LINK](.././http2/~/constants.HTTP2_HEADER_LINK "constants.HTTP2_HEADER_LINK")

No documentation available

v

[constants.HTTP2\_HEADER\_LOCATION](.././http2/~/constants.HTTP2_HEADER_LOCATION "constants.HTTP2_HEADER_LOCATION")

No documentation available

v

[constants.HTTP2\_HEADER\_MAX\_FORWARDS](.././http2/~/constants.HTTP2_HEADER_MAX_FORWARDS "constants.HTTP2_HEADER_MAX_FORWARDS")

No documentation available

v

[constants.HTTP2\_HEADER\_METHOD](.././http2/~/constants.HTTP2_HEADER_METHOD "constants.HTTP2_HEADER_METHOD")

No documentation available

v

[constants.HTTP2\_HEADER\_PATH](.././http2/~/constants.HTTP2_HEADER_PATH "constants.HTTP2_HEADER_PATH")

No documentation available

v

[constants.HTTP2\_HEADER\_PREFER](.././http2/~/constants.HTTP2_HEADER_PREFER "constants.HTTP2_HEADER_PREFER")

No documentation available

v

[constants.HTTP2\_HEADER\_PROXY\_AUTHENTICATE](.././http2/~/constants.HTTP2_HEADER_PROXY_AUTHENTICATE "constants.HTTP2_HEADER_PROXY_AUTHENTICATE")

No documentation available

v

[constants.HTTP2\_HEADER\_PROXY\_AUTHORIZATION](.././http2/~/constants.HTTP2_HEADER_PROXY_AUTHORIZATION "constants.HTTP2_HEADER_PROXY_AUTHORIZATION")

No documentation available

v

[constants.HTTP2\_HEADER\_PROXY\_CONNECTION](.././http2/~/constants.HTTP2_HEADER_PROXY_CONNECTION "constants.HTTP2_HEADER_PROXY_CONNECTION")

No documentation available

v

[constants.HTTP2\_HEADER\_RANGE](.././http2/~/constants.HTTP2_HEADER_RANGE "constants.HTTP2_HEADER_RANGE")

No documentation available

v

[constants.HTTP2\_HEADER\_REFERER](.././http2/~/constants.HTTP2_HEADER_REFERER "constants.HTTP2_HEADER_REFERER")

No documentation available

v

[constants.HTTP2\_HEADER\_REFRESH](.././http2/~/constants.HTTP2_HEADER_REFRESH "constants.HTTP2_HEADER_REFRESH")

No documentation available

v

[constants.HTTP2\_HEADER\_RETRY\_AFTER](.././http2/~/constants.HTTP2_HEADER_RETRY_AFTER "constants.HTTP2_HEADER_RETRY_AFTER")

No documentation available

v

[constants.HTTP2\_HEADER\_SCHEME](.././http2/~/constants.HTTP2_HEADER_SCHEME "constants.HTTP2_HEADER_SCHEME")

No documentation available

v

[constants.HTTP2\_HEADER\_SERVER](.././http2/~/constants.HTTP2_HEADER_SERVER "constants.HTTP2_HEADER_SERVER")

No documentation available

v

[constants.HTTP2\_HEADER\_SET\_COOKIE](.././http2/~/constants.HTTP2_HEADER_SET_COOKIE "constants.HTTP2_HEADER_SET_COOKIE")

No documentation available

v

[constants.HTTP2\_HEADER\_STATUS](.././http2/~/constants.HTTP2_HEADER_STATUS "constants.HTTP2_HEADER_STATUS")

No documentation available

v

[constants.HTTP2\_HEADER\_STRICT\_TRANSPORT\_SECURITY](.././http2/~/constants.HTTP2_HEADER_STRICT_TRANSPORT_SECURITY "constants.HTTP2_HEADER_STRICT_TRANSPORT_SECURITY")

No documentation available

v

[constants.HTTP2\_HEADER\_TE](.././http2/~/constants.HTTP2_HEADER_TE "constants.HTTP2_HEADER_TE")

No documentation available

v

[constants.HTTP2\_HEADER\_TRANSFER\_ENCODING](.././http2/~/constants.HTTP2_HEADER_TRANSFER_ENCODING "constants.HTTP2_HEADER_TRANSFER_ENCODING")

No documentation available

v

[constants.HTTP2\_HEADER\_UPGRADE](.././http2/~/constants.HTTP2_HEADER_UPGRADE "constants.HTTP2_HEADER_UPGRADE")

No documentation available

v

[constants.HTTP2\_HEADER\_USER\_AGENT](.././http2/~/constants.HTTP2_HEADER_USER_AGENT "constants.HTTP2_HEADER_USER_AGENT")

No documentation available

v

[constants.HTTP2\_HEADER\_VARY](.././http2/~/constants.HTTP2_HEADER_VARY "constants.HTTP2_HEADER_VARY")

No documentation available

v

[constants.HTTP2\_HEADER\_VIA](.././http2/~/constants.HTTP2_HEADER_VIA "constants.HTTP2_HEADER_VIA")

No documentation available

v

[constants.HTTP2\_HEADER\_WWW\_AUTHENTICATE](.././http2/~/constants.HTTP2_HEADER_WWW_AUTHENTICATE "constants.HTTP2_HEADER_WWW_AUTHENTICATE")

No documentation available

v

[constants.HTTP2\_METHOD\_ACL](.././http2/~/constants.HTTP2_METHOD_ACL "constants.HTTP2_METHOD_ACL")

No documentation available

v

[constants.HTTP2\_METHOD\_BASELINE\_CONTROL](.././http2/~/constants.HTTP2_METHOD_BASELINE_CONTROL "constants.HTTP2_METHOD_BASELINE_CONTROL")

No documentation available

v

[constants.HTTP2\_METHOD\_BIND](.././http2/~/constants.HTTP2_METHOD_BIND "constants.HTTP2_METHOD_BIND")

No documentation available

v

[constants.HTTP2\_METHOD\_CHECKIN](.././http2/~/constants.HTTP2_METHOD_CHECKIN "constants.HTTP2_METHOD_CHECKIN")

No documentation available

v

[constants.HTTP2\_METHOD\_CHECKOUT](.././http2/~/constants.HTTP2_METHOD_CHECKOUT "constants.HTTP2_METHOD_CHECKOUT")

No documentation available

v

[constants.HTTP2\_METHOD\_CONNECT](.././http2/~/constants.HTTP2_METHOD_CONNECT "constants.HTTP2_METHOD_CONNECT")

No documentation available

v

[constants.HTTP2\_METHOD\_COPY](.././http2/~/constants.HTTP2_METHOD_COPY "constants.HTTP2_METHOD_COPY")

No documentation available

v

[constants.HTTP2\_METHOD\_DELETE](.././http2/~/constants.HTTP2_METHOD_DELETE "constants.HTTP2_METHOD_DELETE")

No documentation available

v

[constants.HTTP2\_METHOD\_GET](.././http2/~/constants.HTTP2_METHOD_GET "constants.HTTP2_METHOD_GET")

No documentation available

v

[constants.HTTP2\_METHOD\_HEAD](.././http2/~/constants.HTTP2_METHOD_HEAD "constants.HTTP2_METHOD_HEAD")

No documentation available

v

[constants.HTTP2\_METHOD\_LABEL](.././http2/~/constants.HTTP2_METHOD_LABEL "constants.HTTP2_METHOD_LABEL")

No documentation available

v

[constants.HTTP2\_METHOD\_LINK](.././http2/~/constants.HTTP2_METHOD_LINK "constants.HTTP2_METHOD_LINK")

No documentation available

v

[constants.HTTP2\_METHOD\_LOCK](.././http2/~/constants.HTTP2_METHOD_LOCK "constants.HTTP2_METHOD_LOCK")

No documentation available

v

[constants.HTTP2\_METHOD\_MERGE](.././http2/~/constants.HTTP2_METHOD_MERGE "constants.HTTP2_METHOD_MERGE")

No documentation available

v

[constants.HTTP2\_METHOD\_MKACTIVITY](.././http2/~/constants.HTTP2_METHOD_MKACTIVITY "constants.HTTP2_METHOD_MKACTIVITY")

No documentation available

v

[constants.HTTP2\_METHOD\_MKCALENDAR](.././http2/~/constants.HTTP2_METHOD_MKCALENDAR "constants.HTTP2_METHOD_MKCALENDAR")

No documentation available

v

[constants.HTTP2\_METHOD\_MKCOL](.././http2/~/constants.HTTP2_METHOD_MKCOL "constants.HTTP2_METHOD_MKCOL")

No documentation available

v

[constants.HTTP2\_METHOD\_MKREDIRECTREF](.././http2/~/constants.HTTP2_METHOD_MKREDIRECTREF "constants.HTTP2_METHOD_MKREDIRECTREF")

No documentation available

v

[constants.HTTP2\_METHOD\_MKWORKSPACE](.././http2/~/constants.HTTP2_METHOD_MKWORKSPACE "constants.HTTP2_METHOD_MKWORKSPACE")

No documentation available

v

[constants.HTTP2\_METHOD\_MOVE](.././http2/~/constants.HTTP2_METHOD_MOVE "constants.HTTP2_METHOD_MOVE")

No documentation available

v

[constants.HTTP2\_METHOD\_OPTIONS](.././http2/~/constants.HTTP2_METHOD_OPTIONS "constants.HTTP2_METHOD_OPTIONS")

No documentation available

v

[constants.HTTP2\_METHOD\_ORDERPATCH](.././http2/~/constants.HTTP2_METHOD_ORDERPATCH "constants.HTTP2_METHOD_ORDERPATCH")

No documentation available

v

[constants.HTTP2\_METHOD\_PATCH](.././http2/~/constants.HTTP2_METHOD_PATCH "constants.HTTP2_METHOD_PATCH")

No documentation available

v

[constants.HTTP2\_METHOD\_POST](.././http2/~/constants.HTTP2_METHOD_POST "constants.HTTP2_METHOD_POST")

No documentation available

v

[constants.HTTP2\_METHOD\_PRI](.././http2/~/constants.HTTP2_METHOD_PRI "constants.HTTP2_METHOD_PRI")

No documentation available

v

[constants.HTTP2\_METHOD\_PROPFIND](.././http2/~/constants.HTTP2_METHOD_PROPFIND "constants.HTTP2_METHOD_PROPFIND")

No documentation available

v

[constants.HTTP2\_METHOD\_PROPPATCH](.././http2/~/constants.HTTP2_METHOD_PROPPATCH "constants.HTTP2_METHOD_PROPPATCH")

No documentation available

v

[constants.HTTP2\_METHOD\_PUT](.././http2/~/constants.HTTP2_METHOD_PUT "constants.HTTP2_METHOD_PUT")

No documentation available

v

[constants.HTTP2\_METHOD\_REBIND](.././http2/~/constants.HTTP2_METHOD_REBIND "constants.HTTP2_METHOD_REBIND")

No documentation available

v

[constants.HTTP2\_METHOD\_REPORT](.././http2/~/constants.HTTP2_METHOD_REPORT "constants.HTTP2_METHOD_REPORT")

No documentation available

v

[constants.HTTP2\_METHOD\_SEARCH](.././http2/~/constants.HTTP2_METHOD_SEARCH "constants.HTTP2_METHOD_SEARCH")

No documentation available

v

[constants.HTTP2\_METHOD\_TRACE](.././http2/~/constants.HTTP2_METHOD_TRACE "constants.HTTP2_METHOD_TRACE")

No documentation available

v

[constants.HTTP2\_METHOD\_UNBIND](.././http2/~/constants.HTTP2_METHOD_UNBIND "constants.HTTP2_METHOD_UNBIND")

No documentation available

v

[constants.HTTP2\_METHOD\_UNCHECKOUT](.././http2/~/constants.HTTP2_METHOD_UNCHECKOUT "constants.HTTP2_METHOD_UNCHECKOUT")

No documentation available

v

[constants.HTTP2\_METHOD\_UNLINK](.././http2/~/constants.HTTP2_METHOD_UNLINK "constants.HTTP2_METHOD_UNLINK")

No documentation available

v

[constants.HTTP2\_METHOD\_UNLOCK](.././http2/~/constants.HTTP2_METHOD_UNLOCK "constants.HTTP2_METHOD_UNLOCK")

No documentation available

v

[constants.HTTP2\_METHOD\_UPDATE](.././http2/~/constants.HTTP2_METHOD_UPDATE "constants.HTTP2_METHOD_UPDATE")

No documentation available

v

[constants.HTTP2\_METHOD\_UPDATEREDIRECTREF](.././http2/~/constants.HTTP2_METHOD_UPDATEREDIRECTREF "constants.HTTP2_METHOD_UPDATEREDIRECTREF")

No documentation available

v

[constants.HTTP2\_METHOD\_VERSION\_CONTROL](.././http2/~/constants.HTTP2_METHOD_VERSION_CONTROL "constants.HTTP2_METHOD_VERSION_CONTROL")

No documentation available

v

[constants.HTTP\_STATUS\_ACCEPTED](.././http2/~/constants.HTTP_STATUS_ACCEPTED "constants.HTTP_STATUS_ACCEPTED")

No documentation available

v

[constants.HTTP\_STATUS\_ALREADY\_REPORTED](.././http2/~/constants.HTTP_STATUS_ALREADY_REPORTED "constants.HTTP_STATUS_ALREADY_REPORTED")

No documentation available

v

[constants.HTTP\_STATUS\_BAD\_GATEWAY](.././http2/~/constants.HTTP_STATUS_BAD_GATEWAY "constants.HTTP_STATUS_BAD_GATEWAY")

No documentation available

v

[constants.HTTP\_STATUS\_BAD\_REQUEST](.././http2/~/constants.HTTP_STATUS_BAD_REQUEST "constants.HTTP_STATUS_BAD_REQUEST")

No documentation available

v

[constants.HTTP\_STATUS\_BANDWIDTH\_LIMIT\_EXCEEDED](.././http2/~/constants.HTTP_STATUS_BANDWIDTH_LIMIT_EXCEEDED "constants.HTTP_STATUS_BANDWIDTH_LIMIT_EXCEEDED")

No documentation available

v

[constants.HTTP\_STATUS\_CONFLICT](.././http2/~/constants.HTTP_STATUS_CONFLICT "constants.HTTP_STATUS_CONFLICT")

No documentation available

v

[constants.HTTP\_STATUS\_CONTINUE](.././http2/~/constants.HTTP_STATUS_CONTINUE "constants.HTTP_STATUS_CONTINUE")

No documentation available

v

[constants.HTTP\_STATUS\_CREATED](.././http2/~/constants.HTTP_STATUS_CREATED "constants.HTTP_STATUS_CREATED")

No documentation available

v

[constants.HTTP\_STATUS\_EXPECTATION\_FAILED](.././http2/~/constants.HTTP_STATUS_EXPECTATION_FAILED "constants.HTTP_STATUS_EXPECTATION_FAILED")

No documentation available

v

[constants.HTTP\_STATUS\_FAILED\_DEPENDENCY](.././http2/~/constants.HTTP_STATUS_FAILED_DEPENDENCY "constants.HTTP_STATUS_FAILED_DEPENDENCY")

No documentation available

v

[constants.HTTP\_STATUS\_FORBIDDEN](.././http2/~/constants.HTTP_STATUS_FORBIDDEN "constants.HTTP_STATUS_FORBIDDEN")

No documentation available

v

[constants.HTTP\_STATUS\_FOUND](.././http2/~/constants.HTTP_STATUS_FOUND "constants.HTTP_STATUS_FOUND")

No documentation available

v

[constants.HTTP\_STATUS\_GATEWAY\_TIMEOUT](.././http2/~/constants.HTTP_STATUS_GATEWAY_TIMEOUT "constants.HTTP_STATUS_GATEWAY_TIMEOUT")

No documentation available

v

[constants.HTTP\_STATUS\_GONE](.././http2/~/constants.HTTP_STATUS_GONE "constants.HTTP_STATUS_GONE")

No documentation available

v

[constants.HTTP\_STATUS\_HTTP\_VERSION\_NOT\_SUPPORTED](.././http2/~/constants.HTTP_STATUS_HTTP_VERSION_NOT_SUPPORTED "constants.HTTP_STATUS_HTTP_VERSION_NOT_SUPPORTED")

No documentation available

v

[constants.HTTP\_STATUS\_IM\_USED](.././http2/~/constants.HTTP_STATUS_IM_USED "constants.HTTP_STATUS_IM_USED")

No documentation available

v

[constants.HTTP\_STATUS\_INSUFFICIENT\_STORAGE](.././http2/~/constants.HTTP_STATUS_INSUFFICIENT_STORAGE "constants.HTTP_STATUS_INSUFFICIENT_STORAGE")

No documentation available

v

[constants.HTTP\_STATUS\_INTERNAL\_SERVER\_ERROR](.././http2/~/constants.HTTP_STATUS_INTERNAL_SERVER_ERROR "constants.HTTP_STATUS_INTERNAL_SERVER_ERROR")

No documentation available

v

[constants.HTTP\_STATUS\_LENGTH\_REQUIRED](.././http2/~/constants.HTTP_STATUS_LENGTH_REQUIRED "constants.HTTP_STATUS_LENGTH_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_LOCKED](.././http2/~/constants.HTTP_STATUS_LOCKED "constants.HTTP_STATUS_LOCKED")

No documentation available

v

[constants.HTTP\_STATUS\_LOOP\_DETECTED](.././http2/~/constants.HTTP_STATUS_LOOP_DETECTED "constants.HTTP_STATUS_LOOP_DETECTED")

No documentation available

v

[constants.HTTP\_STATUS\_METHOD\_NOT\_ALLOWED](.././http2/~/constants.HTTP_STATUS_METHOD_NOT_ALLOWED "constants.HTTP_STATUS_METHOD_NOT_ALLOWED")

No documentation available

v

[constants.HTTP\_STATUS\_MISDIRECTED\_REQUEST](.././http2/~/constants.HTTP_STATUS_MISDIRECTED_REQUEST "constants.HTTP_STATUS_MISDIRECTED_REQUEST")

No documentation available

v

[constants.HTTP\_STATUS\_MOVED\_PERMANENTLY](.././http2/~/constants.HTTP_STATUS_MOVED_PERMANENTLY "constants.HTTP_STATUS_MOVED_PERMANENTLY")

No documentation available

v

[constants.HTTP\_STATUS\_MULTI\_STATUS](.././http2/~/constants.HTTP_STATUS_MULTI_STATUS "constants.HTTP_STATUS_MULTI_STATUS")

No documentation available

v

[constants.HTTP\_STATUS\_MULTIPLE\_CHOICES](.././http2/~/constants.HTTP_STATUS_MULTIPLE_CHOICES "constants.HTTP_STATUS_MULTIPLE_CHOICES")

No documentation available

v

[constants.HTTP\_STATUS\_NETWORK\_AUTHENTICATION\_REQUIRED](.././http2/~/constants.HTTP_STATUS_NETWORK_AUTHENTICATION_REQUIRED "constants.HTTP_STATUS_NETWORK_AUTHENTICATION_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_NO\_CONTENT](.././http2/~/constants.HTTP_STATUS_NO_CONTENT "constants.HTTP_STATUS_NO_CONTENT")

No documentation available

v

[constants.HTTP\_STATUS\_NON\_AUTHORITATIVE\_INFORMATION](.././http2/~/constants.HTTP_STATUS_NON_AUTHORITATIVE_INFORMATION "constants.HTTP_STATUS_NON_AUTHORITATIVE_INFORMATION")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_ACCEPTABLE](.././http2/~/constants.HTTP_STATUS_NOT_ACCEPTABLE "constants.HTTP_STATUS_NOT_ACCEPTABLE")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_EXTENDED](.././http2/~/constants.HTTP_STATUS_NOT_EXTENDED "constants.HTTP_STATUS_NOT_EXTENDED")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_FOUND](.././http2/~/constants.HTTP_STATUS_NOT_FOUND "constants.HTTP_STATUS_NOT_FOUND")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_IMPLEMENTED](.././http2/~/constants.HTTP_STATUS_NOT_IMPLEMENTED "constants.HTTP_STATUS_NOT_IMPLEMENTED")

No documentation available

v

[constants.HTTP\_STATUS\_NOT\_MODIFIED](.././http2/~/constants.HTTP_STATUS_NOT_MODIFIED "constants.HTTP_STATUS_NOT_MODIFIED")

No documentation available

v

[constants.HTTP\_STATUS\_OK](.././http2/~/constants.HTTP_STATUS_OK "constants.HTTP_STATUS_OK")

No documentation available

v

[constants.HTTP\_STATUS\_PARTIAL\_CONTENT](.././http2/~/constants.HTTP_STATUS_PARTIAL_CONTENT "constants.HTTP_STATUS_PARTIAL_CONTENT")

No documentation available

v

[constants.HTTP\_STATUS\_PAYLOAD\_TOO\_LARGE](.././http2/~/constants.HTTP_STATUS_PAYLOAD_TOO_LARGE "constants.HTTP_STATUS_PAYLOAD_TOO_LARGE")

No documentation available

v

[constants.HTTP\_STATUS\_PAYMENT\_REQUIRED](.././http2/~/constants.HTTP_STATUS_PAYMENT_REQUIRED "constants.HTTP_STATUS_PAYMENT_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_PERMANENT\_REDIRECT](.././http2/~/constants.HTTP_STATUS_PERMANENT_REDIRECT "constants.HTTP_STATUS_PERMANENT_REDIRECT")

No documentation available

v

[constants.HTTP\_STATUS\_PRECONDITION\_FAILED](.././http2/~/constants.HTTP_STATUS_PRECONDITION_FAILED "constants.HTTP_STATUS_PRECONDITION_FAILED")

No documentation available

v

[constants.HTTP\_STATUS\_PRECONDITION\_REQUIRED](.././http2/~/constants.HTTP_STATUS_PRECONDITION_REQUIRED "constants.HTTP_STATUS_PRECONDITION_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_PROCESSING](.././http2/~/constants.HTTP_STATUS_PROCESSING "constants.HTTP_STATUS_PROCESSING")

No documentation available

v

[constants.HTTP\_STATUS\_PROXY\_AUTHENTICATION\_REQUIRED](.././http2/~/constants.HTTP_STATUS_PROXY_AUTHENTICATION_REQUIRED "constants.HTTP_STATUS_PROXY_AUTHENTICATION_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_RANGE\_NOT\_SATISFIABLE](.././http2/~/constants.HTTP_STATUS_RANGE_NOT_SATISFIABLE "constants.HTTP_STATUS_RANGE_NOT_SATISFIABLE")

No documentation available

v

[constants.HTTP\_STATUS\_REQUEST\_HEADER\_FIELDS\_TOO\_LARGE](.././http2/~/constants.HTTP_STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE "constants.HTTP_STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE")

No documentation available

v

[constants.HTTP\_STATUS\_REQUEST\_TIMEOUT](.././http2/~/constants.HTTP_STATUS_REQUEST_TIMEOUT "constants.HTTP_STATUS_REQUEST_TIMEOUT")

No documentation available

v

[constants.HTTP\_STATUS\_RESET\_CONTENT](.././http2/~/constants.HTTP_STATUS_RESET_CONTENT "constants.HTTP_STATUS_RESET_CONTENT")

No documentation available

v

[constants.HTTP\_STATUS\_SEE\_OTHER](.././http2/~/constants.HTTP_STATUS_SEE_OTHER "constants.HTTP_STATUS_SEE_OTHER")

No documentation available

v

[constants.HTTP\_STATUS\_SERVICE\_UNAVAILABLE](.././http2/~/constants.HTTP_STATUS_SERVICE_UNAVAILABLE "constants.HTTP_STATUS_SERVICE_UNAVAILABLE")

No documentation available

v

[constants.HTTP\_STATUS\_SWITCHING\_PROTOCOLS](.././http2/~/constants.HTTP_STATUS_SWITCHING_PROTOCOLS "constants.HTTP_STATUS_SWITCHING_PROTOCOLS")

No documentation available

v

[constants.HTTP\_STATUS\_TEAPOT](.././http2/~/constants.HTTP_STATUS_TEAPOT "constants.HTTP_STATUS_TEAPOT")

No documentation available

v

[constants.HTTP\_STATUS\_TEMPORARY\_REDIRECT](.././http2/~/constants.HTTP_STATUS_TEMPORARY_REDIRECT "constants.HTTP_STATUS_TEMPORARY_REDIRECT")

No documentation available

v

[constants.HTTP\_STATUS\_TOO\_MANY\_REQUESTS](.././http2/~/constants.HTTP_STATUS_TOO_MANY_REQUESTS "constants.HTTP_STATUS_TOO_MANY_REQUESTS")

No documentation available

v

[constants.HTTP\_STATUS\_UNAUTHORIZED](.././http2/~/constants.HTTP_STATUS_UNAUTHORIZED "constants.HTTP_STATUS_UNAUTHORIZED")

No documentation available

v

[constants.HTTP\_STATUS\_UNAVAILABLE\_FOR\_LEGAL\_REASONS](.././http2/~/constants.HTTP_STATUS_UNAVAILABLE_FOR_LEGAL_REASONS "constants.HTTP_STATUS_UNAVAILABLE_FOR_LEGAL_REASONS")

No documentation available

v

[constants.HTTP\_STATUS\_UNORDERED\_COLLECTION](.././http2/~/constants.HTTP_STATUS_UNORDERED_COLLECTION "constants.HTTP_STATUS_UNORDERED_COLLECTION")

No documentation available

v

[constants.HTTP\_STATUS\_UNPROCESSABLE\_ENTITY](.././http2/~/constants.HTTP_STATUS_UNPROCESSABLE_ENTITY "constants.HTTP_STATUS_UNPROCESSABLE_ENTITY")

No documentation available

v

[constants.HTTP\_STATUS\_UNSUPPORTED\_MEDIA\_TYPE](.././http2/~/constants.HTTP_STATUS_UNSUPPORTED_MEDIA_TYPE "constants.HTTP_STATUS_UNSUPPORTED_MEDIA_TYPE")

No documentation available

v

[constants.HTTP\_STATUS\_UPGRADE\_REQUIRED](.././http2/~/constants.HTTP_STATUS_UPGRADE_REQUIRED "constants.HTTP_STATUS_UPGRADE_REQUIRED")

No documentation available

v

[constants.HTTP\_STATUS\_URI\_TOO\_LONG](.././http2/~/constants.HTTP_STATUS_URI_TOO_LONG "constants.HTTP_STATUS_URI_TOO_LONG")

No documentation available

v

[constants.HTTP\_STATUS\_USE\_PROXY](.././http2/~/constants.HTTP_STATUS_USE_PROXY "constants.HTTP_STATUS_USE_PROXY")

No documentation available

v

[constants.HTTP\_STATUS\_VARIANT\_ALSO\_NEGOTIATES](.././http2/~/constants.HTTP_STATUS_VARIANT_ALSO_NEGOTIATES "constants.HTTP_STATUS_VARIANT_ALSO_NEGOTIATES")

No documentation available

v

[constants.MAX\_INITIAL\_WINDOW\_SIZE](.././http2/~/constants.MAX_INITIAL_WINDOW_SIZE "constants.MAX_INITIAL_WINDOW_SIZE")

No documentation available

v

[constants.MAX\_MAX\_FRAME\_SIZE](.././http2/~/constants.MAX_MAX_FRAME_SIZE "constants.MAX_MAX_FRAME_SIZE")

No documentation available

v

[constants.MIN\_MAX\_FRAME\_SIZE](.././http2/~/constants.MIN_MAX_FRAME_SIZE "constants.MIN_MAX_FRAME_SIZE")

No documentation available

v

[constants.NGHTTP2\_CANCEL](.././http2/~/constants.NGHTTP2_CANCEL "constants.NGHTTP2_CANCEL")

No documentation available

v

[constants.NGHTTP2\_COMPRESSION\_ERROR](.././http2/~/constants.NGHTTP2_COMPRESSION_ERROR "constants.NGHTTP2_COMPRESSION_ERROR")

No documentation available

v

[constants.NGHTTP2\_CONNECT\_ERROR](.././http2/~/constants.NGHTTP2_CONNECT_ERROR "constants.NGHTTP2_CONNECT_ERROR")

No documentation available

v

[constants.NGHTTP2\_DEFAULT\_WEIGHT](.././http2/~/constants.NGHTTP2_DEFAULT_WEIGHT "constants.NGHTTP2_DEFAULT_WEIGHT")

No documentation available

v

[constants.NGHTTP2\_ENHANCE\_YOUR\_CALM](.././http2/~/constants.NGHTTP2_ENHANCE_YOUR_CALM "constants.NGHTTP2_ENHANCE_YOUR_CALM")

No documentation available

v

[constants.NGHTTP2\_ERR\_FRAME\_SIZE\_ERROR](.././http2/~/constants.NGHTTP2_ERR_FRAME_SIZE_ERROR "constants.NGHTTP2_ERR_FRAME_SIZE_ERROR")

No documentation available

v

[constants.NGHTTP2\_FLAG\_ACK](.././http2/~/constants.NGHTTP2_FLAG_ACK "constants.NGHTTP2_FLAG_ACK")

No documentation available

v

[constants.NGHTTP2\_FLAG\_END\_HEADERS](.././http2/~/constants.NGHTTP2_FLAG_END_HEADERS "constants.NGHTTP2_FLAG_END_HEADERS")

No documentation available

v

[constants.NGHTTP2\_FLAG\_END\_STREAM](.././http2/~/constants.NGHTTP2_FLAG_END_STREAM "constants.NGHTTP2_FLAG_END_STREAM")

No documentation available

v

[constants.NGHTTP2\_FLAG\_NONE](.././http2/~/constants.NGHTTP2_FLAG_NONE "constants.NGHTTP2_FLAG_NONE")

No documentation available

v

[constants.NGHTTP2\_FLAG\_PADDED](.././http2/~/constants.NGHTTP2_FLAG_PADDED "constants.NGHTTP2_FLAG_PADDED")

No documentation available

v

[constants.NGHTTP2\_FLAG\_PRIORITY](.././http2/~/constants.NGHTTP2_FLAG_PRIORITY "constants.NGHTTP2_FLAG_PRIORITY")

No documentation available

v

[constants.NGHTTP2\_FLOW\_CONTROL\_ERROR](.././http2/~/constants.NGHTTP2_FLOW_CONTROL_ERROR "constants.NGHTTP2_FLOW_CONTROL_ERROR")

No documentation available

v

[constants.NGHTTP2\_FRAME\_SIZE\_ERROR](.././http2/~/constants.NGHTTP2_FRAME_SIZE_ERROR "constants.NGHTTP2_FRAME_SIZE_ERROR")

No documentation available

v

[constants.NGHTTP2\_HTTP\_1\_1\_REQUIRED](.././http2/~/constants.NGHTTP2_HTTP_1_1_REQUIRED "constants.NGHTTP2_HTTP_1_1_REQUIRED")

No documentation available

v

[constants.NGHTTP2\_INADEQUATE\_SECURITY](.././http2/~/constants.NGHTTP2_INADEQUATE_SECURITY "constants.NGHTTP2_INADEQUATE_SECURITY")

No documentation available

v

[constants.NGHTTP2\_INTERNAL\_ERROR](.././http2/~/constants.NGHTTP2_INTERNAL_ERROR "constants.NGHTTP2_INTERNAL_ERROR")

No documentation available

v

[constants.NGHTTP2\_NO\_ERROR](.././http2/~/constants.NGHTTP2_NO_ERROR "constants.NGHTTP2_NO_ERROR")

No documentation available

v

[constants.NGHTTP2\_PROTOCOL\_ERROR](.././http2/~/constants.NGHTTP2_PROTOCOL_ERROR "constants.NGHTTP2_PROTOCOL_ERROR")

No documentation available

v

[constants.NGHTTP2\_REFUSED\_STREAM](.././http2/~/constants.NGHTTP2_REFUSED_STREAM "constants.NGHTTP2_REFUSED_STREAM")

No documentation available

v

[constants.NGHTTP2\_SESSION\_CLIENT](.././http2/~/constants.NGHTTP2_SESSION_CLIENT "constants.NGHTTP2_SESSION_CLIENT")

No documentation available

v

[constants.NGHTTP2\_SESSION\_SERVER](.././http2/~/constants.NGHTTP2_SESSION_SERVER "constants.NGHTTP2_SESSION_SERVER")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_ENABLE\_PUSH](.././http2/~/constants.NGHTTP2_SETTINGS_ENABLE_PUSH "constants.NGHTTP2_SETTINGS_ENABLE_PUSH")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_HEADER\_TABLE\_SIZE](.././http2/~/constants.NGHTTP2_SETTINGS_HEADER_TABLE_SIZE "constants.NGHTTP2_SETTINGS_HEADER_TABLE_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_INITIAL\_WINDOW\_SIZE](.././http2/~/constants.NGHTTP2_SETTINGS_INITIAL_WINDOW_SIZE "constants.NGHTTP2_SETTINGS_INITIAL_WINDOW_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_MAX\_CONCURRENT\_STREAMS](.././http2/~/constants.NGHTTP2_SETTINGS_MAX_CONCURRENT_STREAMS "constants.NGHTTP2_SETTINGS_MAX_CONCURRENT_STREAMS")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_MAX\_FRAME\_SIZE](.././http2/~/constants.NGHTTP2_SETTINGS_MAX_FRAME_SIZE "constants.NGHTTP2_SETTINGS_MAX_FRAME_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_MAX\_HEADER\_LIST\_SIZE](.././http2/~/constants.NGHTTP2_SETTINGS_MAX_HEADER_LIST_SIZE "constants.NGHTTP2_SETTINGS_MAX_HEADER_LIST_SIZE")

No documentation available

v

[constants.NGHTTP2\_SETTINGS\_TIMEOUT](.././http2/~/constants.NGHTTP2_SETTINGS_TIMEOUT "constants.NGHTTP2_SETTINGS_TIMEOUT")

No documentation available

v

[constants.NGHTTP2\_STREAM\_CLOSED](.././http2/~/constants.NGHTTP2_STREAM_CLOSED "constants.NGHTTP2_STREAM_CLOSED")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_CLOSED](.././http2/~/constants.NGHTTP2_STREAM_STATE_CLOSED "constants.NGHTTP2_STREAM_STATE_CLOSED")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_HALF\_CLOSED\_LOCAL](.././http2/~/constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_LOCAL "constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_LOCAL")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_HALF\_CLOSED\_REMOTE](.././http2/~/constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_REMOTE "constants.NGHTTP2_STREAM_STATE_HALF_CLOSED_REMOTE")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_IDLE](.././http2/~/constants.NGHTTP2_STREAM_STATE_IDLE "constants.NGHTTP2_STREAM_STATE_IDLE")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_OPEN](.././http2/~/constants.NGHTTP2_STREAM_STATE_OPEN "constants.NGHTTP2_STREAM_STATE_OPEN")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_RESERVED\_LOCAL](.././http2/~/constants.NGHTTP2_STREAM_STATE_RESERVED_LOCAL "constants.NGHTTP2_STREAM_STATE_RESERVED_LOCAL")

No documentation available

v

[constants.NGHTTP2\_STREAM\_STATE\_RESERVED\_REMOTE](.././http2/~/constants.NGHTTP2_STREAM_STATE_RESERVED_REMOTE "constants.NGHTTP2_STREAM_STATE_RESERVED_REMOTE")

No documentation available

v

[constants.PADDING\_STRATEGY\_CALLBACK](.././http2/~/constants.PADDING_STRATEGY_CALLBACK "constants.PADDING_STRATEGY_CALLBACK")

No documentation available

v

[constants.PADDING\_STRATEGY\_MAX](.././http2/~/constants.PADDING_STRATEGY_MAX "constants.PADDING_STRATEGY_MAX")

No documentation available

v

[constants.PADDING\_STRATEGY\_NONE](.././http2/~/constants.PADDING_STRATEGY_NONE "constants.PADDING_STRATEGY_NONE")

No documentation available

v

[sensitiveHeaders](.././http2/~/sensitiveHeaders "sensitiveHeaders")

This symbol can be set as a property on the HTTP/2 headers object with an array value in order to provide a list of headers considered sensitive.
