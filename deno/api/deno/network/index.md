---
title: "Network - Deno documentation"
source: "https://docs.deno.com/api/deno/network"
canonical_url: "https://docs.deno.com/api/deno/network"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:54:22.807Z"
content_hash: "e624abcd9f3babfa06138cd4be0e648b07e1c20860a783b66ea8a34d0584f9bd"
menu_path: ["Network - Deno documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/deno/linter/index.md", "title": "Linter - Deno documentation"}
nav_next: {"path": "deno/api/deno/permissions/index.md", "title": "Permissions - Deno documentation"}
---

c

[Deno.QuicEndpoint](./././~/Deno.QuicEndpoint "Deno.QuicEndpoint")

No documentation available

-   [addr](./././~/Deno.QuicEndpoint#property_addr)
-   [close](./././~/Deno.QuicEndpoint#method_close_0)
-   [listen](./././~/Deno.QuicEndpoint#method_listen_0)

f

[Deno.connect](./././~/Deno.connect "Deno.connect")

Connects to the hostname (default is "127.0.0.1") and port on the named transport (default is "tcp"), and resolves to the connection (`Conn`).

f

[Deno.connectQuic](./././~/Deno.connectQuic "Deno.connectQuic")

Establishes a secure connection over QUIC using a hostname and port. The cert file is optional and if not included Mozilla's root certificates will be used. See also [https://github.com/ctz/webpki-roots](https://github.com/ctz/webpki-roots) for specifics.

f

[Deno.connectTls](./././~/Deno.connectTls "Deno.connectTls")

Establishes a secure connection over TLS (transport layer security) using an optional list of CA certs, hostname (default is "127.0.0.1") and port.

f

[Deno.listen](./././~/Deno.listen "Deno.listen")

Listen announces on the local transport address.

f

[Deno.listenDatagram](./././~/Deno.listenDatagram "Deno.listenDatagram")

Listen announces on the local transport address.

f

[Deno.listenTls](./././~/Deno.listenTls "Deno.listenTls")

Listen announces on the local transport address over TLS (transport layer security).

f

[Deno.networkInterfaces](./././~/Deno.networkInterfaces "Deno.networkInterfaces")

Returns an array of the network interface information.

f

[Deno.resolveDns](./././~/Deno.resolveDns "Deno.resolveDns")

Performs DNS resolution against the given query, returning resolved records.

f

[Deno.startTls](./././~/Deno.startTls "Deno.startTls")

Start TLS handshake from an existing connection using an optional list of CA certificates, and hostname (default is "127.0.0.1"). Specifying CA certs is optional. By default the configured root certificates are used. Using this function requires that the other end of the connection is prepared for a TLS handshake.

f

[Deno.upgradeWebTransport](./././~/Deno.upgradeWebTransport "Deno.upgradeWebTransport")

Upgrade a QUIC connection into a WebTransport instance.

I

[Deno.CaaRecord](./././~/Deno.CaaRecord "Deno.CaaRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"CAA"` record type specified, it will resolve with an array of objects with this interface.

-   [critical](./././~/Deno.CaaRecord#property_critical)
-   [tag](./././~/Deno.CaaRecord#property_tag)
-   [value](./././~/Deno.CaaRecord#property_value)

I

[Deno.Conn](./././~/Deno.Conn "Deno.Conn")

No documentation available

-   [close](./././~/Deno.Conn#method_close_0)
-   [closeWrite](./././~/Deno.Conn#method_closewrite_0)
-   [localAddr](./././~/Deno.Conn#property_localaddr)
-   [read](./././~/Deno.Conn#method_read_0)
-   [readable](./././~/Deno.Conn#property_readable)
-   [ref](./././~/Deno.Conn#method_ref_0)
-   [remoteAddr](./././~/Deno.Conn#property_remoteaddr)
-   [unref](./././~/Deno.Conn#method_unref_0)
-   [writable](./././~/Deno.Conn#property_writable)
-   [write](./././~/Deno.Conn#method_write_0)

I

[Deno.ConnectOptions](./././~/Deno.ConnectOptions "Deno.ConnectOptions")

No documentation available

-   [hostname](./././~/Deno.ConnectOptions#property_hostname)
-   [port](./././~/Deno.ConnectOptions#property_port)
-   [signal](./././~/Deno.ConnectOptions#property_signal)
-   [transport](./././~/Deno.ConnectOptions#property_transport)

I

[Deno.ConnectQuicOptions](./././~/Deno.ConnectQuicOptions "Deno.ConnectQuicOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.ConnectQuicOptions#property_alpnprotocols)
-   [caCerts](./././~/Deno.ConnectQuicOptions#property_cacerts)
-   [endpoint](./././~/Deno.ConnectQuicOptions#property_endpoint)
-   [hostname](./././~/Deno.ConnectQuicOptions#property_hostname)
-   [port](./././~/Deno.ConnectQuicOptions#property_port)
-   [serverName](./././~/Deno.ConnectQuicOptions#property_servername)
-   [zeroRtt](./././~/Deno.ConnectQuicOptions#property_zerortt)

I

[Deno.ConnectTlsOptions](./././~/Deno.ConnectTlsOptions "Deno.ConnectTlsOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.ConnectTlsOptions#property_alpnprotocols)
-   [caCerts](./././~/Deno.ConnectTlsOptions#property_cacerts)
-   [hostname](./././~/Deno.ConnectTlsOptions#property_hostname)
-   [port](./././~/Deno.ConnectTlsOptions#property_port)
-   [unsafelyDisableHostnameVerification](./././~/Deno.ConnectTlsOptions#property_unsafelydisablehostnameverification)

I

[Deno.DatagramConn](./././~/Deno.DatagramConn "Deno.DatagramConn")

A generic transport listener for message-oriented protocols.

-   [addr](./././~/Deno.DatagramConn#property_addr)
-   [close](./././~/Deno.DatagramConn#method_close_0)
-   [joinMulticastV4](./././~/Deno.DatagramConn#method_joinmulticastv4_0)
-   [joinMulticastV6](./././~/Deno.DatagramConn#method_joinmulticastv6_0)
-   [receive](./././~/Deno.DatagramConn#method_receive_0)
-   [send](./././~/Deno.DatagramConn#method_send_0)

I

[Deno.Listener](./././~/Deno.Listener "Deno.Listener")

A generic network listener for stream-oriented protocols.

-   [accept](./././~/Deno.Listener#method_accept_0)
-   [addr](./././~/Deno.Listener#property_addr)
-   [close](./././~/Deno.Listener#method_close_0)
-   [ref](./././~/Deno.Listener#method_ref_0)
-   [unref](./././~/Deno.Listener#method_unref_0)

I

[Deno.ListenOptions](./././~/Deno.ListenOptions "Deno.ListenOptions")

No documentation available

-   [hostname](./././~/Deno.ListenOptions#property_hostname)
-   [port](./././~/Deno.ListenOptions#property_port)
-   [tcpBacklog](./././~/Deno.ListenOptions#property_tcpbacklog)

I

[Deno.ListenTlsOptions](./././~/Deno.ListenTlsOptions "Deno.ListenTlsOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.ListenTlsOptions#property_alpnprotocols)
-   [transport](./././~/Deno.ListenTlsOptions#property_transport)

I

[Deno.MulticastV4Membership](./././~/Deno.MulticastV4Membership "Deno.MulticastV4Membership")

Represents membership of a IPv4 multicast group.

-   [leave](./././~/Deno.MulticastV4Membership#property_leave)
-   [setLoopback](./././~/Deno.MulticastV4Membership#property_setloopback)
-   [setTTL](./././~/Deno.MulticastV4Membership#property_setttl)

I

[Deno.MulticastV6Membership](./././~/Deno.MulticastV6Membership "Deno.MulticastV6Membership")

Represents membership of a IPv6 multicast group.

-   [leave](./././~/Deno.MulticastV6Membership#property_leave)
-   [setLoopback](./././~/Deno.MulticastV6Membership#property_setloopback)

I

[Deno.MxRecord](./././~/Deno.MxRecord "Deno.MxRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"MX"` record type specified, it will return an array of objects with this interface.

-   [exchange](./././~/Deno.MxRecord#property_exchange)
-   [preference](./././~/Deno.MxRecord#property_preference)

I

[Deno.NaptrRecord](./././~/Deno.NaptrRecord "Deno.NaptrRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"NAPTR"` record type specified, it will return an array of objects with this interface.

-   [flags](./././~/Deno.NaptrRecord#property_flags)
-   [order](./././~/Deno.NaptrRecord#property_order)
-   [preference](./././~/Deno.NaptrRecord#property_preference)
-   [regexp](./././~/Deno.NaptrRecord#property_regexp)
-   [replacement](./././~/Deno.NaptrRecord#property_replacement)
-   [services](./././~/Deno.NaptrRecord#property_services)

I

[Deno.NetAddr](./././~/Deno.NetAddr "Deno.NetAddr")

No documentation available

-   [hostname](./././~/Deno.NetAddr#property_hostname)
-   [port](./././~/Deno.NetAddr#property_port)
-   [transport](./././~/Deno.NetAddr#property_transport)

I

[Deno.NetworkInterfaceInfo](./././~/Deno.NetworkInterfaceInfo "Deno.NetworkInterfaceInfo")

The information for a network interface returned from a call to [`Deno.networkInterfaces`](./././~/Deno.networkInterfaces).

-   [address](./././~/Deno.NetworkInterfaceInfo#property_address)
-   [cidr](./././~/Deno.NetworkInterfaceInfo#property_cidr)
-   [family](./././~/Deno.NetworkInterfaceInfo#property_family)
-   [mac](./././~/Deno.NetworkInterfaceInfo#property_mac)
-   [name](./././~/Deno.NetworkInterfaceInfo#property_name)
-   [netmask](./././~/Deno.NetworkInterfaceInfo#property_netmask)
-   [scopeid](./././~/Deno.NetworkInterfaceInfo#property_scopeid)

I

[Deno.QuicAcceptOptions](./././~/Deno.QuicAcceptOptions "Deno.QuicAcceptOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.QuicAcceptOptions#property_alpnprotocols)
-   [zeroRtt](./././~/Deno.QuicAcceptOptions#property_zerortt)

I

[Deno.QuicBidirectionalStream](./././~/Deno.QuicBidirectionalStream "Deno.QuicBidirectionalStream")

No documentation available

-   [readable](./././~/Deno.QuicBidirectionalStream#property_readable)
-   [writable](./././~/Deno.QuicBidirectionalStream#property_writable)

I

[Deno.QuicCloseInfo](./././~/Deno.QuicCloseInfo "Deno.QuicCloseInfo")

No documentation available

-   [closeCode](./././~/Deno.QuicCloseInfo#property_closecode)
-   [reason](./././~/Deno.QuicCloseInfo#property_reason)

I

[Deno.QuicConn](./././~/Deno.QuicConn "Deno.QuicConn")

No documentation available

-   [close](./././~/Deno.QuicConn#method_close_0)
-   [closed](./././~/Deno.QuicConn#property_closed)
-   [createBidirectionalStream](./././~/Deno.QuicConn#method_createbidirectionalstream_0)
-   [createUnidirectionalStream](./././~/Deno.QuicConn#method_createunidirectionalstream_0)
-   [endpoint](./././~/Deno.QuicConn#property_endpoint)
-   [handshake](./././~/Deno.QuicConn#property_handshake)
-   [incomingBidirectionalStreams](./././~/Deno.QuicConn#property_incomingbidirectionalstreams)
-   [incomingUnidirectionalStreams](./././~/Deno.QuicConn#property_incomingunidirectionalstreams)
-   [maxDatagramSize](./././~/Deno.QuicConn#property_maxdatagramsize)
-   [protocol](./././~/Deno.QuicConn#property_protocol)
-   [readDatagram](./././~/Deno.QuicConn#method_readdatagram_0)
-   [remoteAddr](./././~/Deno.QuicConn#property_remoteaddr)
-   [sendDatagram](./././~/Deno.QuicConn#method_senddatagram_0)
-   [serverName](./././~/Deno.QuicConn#property_servername)

I

[Deno.QuicEndpointOptions](./././~/Deno.QuicEndpointOptions "Deno.QuicEndpointOptions")

No documentation available

-   [hostname](./././~/Deno.QuicEndpointOptions#property_hostname)
-   [port](./././~/Deno.QuicEndpointOptions#property_port)

I

[Deno.QuicIncoming](./././~/Deno.QuicIncoming "Deno.QuicIncoming")

An incoming connection for which the server has not yet begun its part of the handshake.

-   [accept](./././~/Deno.QuicIncoming#method_accept_0)
-   [ignore](./././~/Deno.QuicIncoming#method_ignore_0)
-   [localIp](./././~/Deno.QuicIncoming#property_localip)
-   [refuse](./././~/Deno.QuicIncoming#method_refuse_0)
-   [remoteAddr](./././~/Deno.QuicIncoming#property_remoteaddr)
-   [remoteAddressValidated](./././~/Deno.QuicIncoming#property_remoteaddressvalidated)

I

[Deno.QuicListener](./././~/Deno.QuicListener "Deno.QuicListener")

Specialized listener that accepts QUIC connections.

-   [accept](./././~/Deno.QuicListener#method_accept_0)
-   [endpoint](./././~/Deno.QuicListener#property_endpoint)
-   [incoming](./././~/Deno.QuicListener#method_incoming_0)
-   [stop](./././~/Deno.QuicListener#method_stop_0)

I

[Deno.QuicListenOptions](./././~/Deno.QuicListenOptions "Deno.QuicListenOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.QuicListenOptions#property_alpnprotocols)
-   [cert](./././~/Deno.QuicListenOptions#property_cert)
-   [key](./././~/Deno.QuicListenOptions#property_key)

I

[Deno.QuicReceiveStream](./././~/Deno.QuicReceiveStream "Deno.QuicReceiveStream")

No documentation available

-   [id](./././~/Deno.QuicReceiveStream#property_id)

I

[Deno.QuicSendStream](./././~/Deno.QuicSendStream "Deno.QuicSendStream")

No documentation available

-   [id](./././~/Deno.QuicSendStream#property_id)
-   [sendOrder](./././~/Deno.QuicSendStream#property_sendorder)

I

[Deno.QuicSendStreamOptions](./././~/Deno.QuicSendStreamOptions "Deno.QuicSendStreamOptions")

No documentation available

-   [sendOrder](./././~/Deno.QuicSendStreamOptions#property_sendorder)
-   [waitUntilAvailable](./././~/Deno.QuicSendStreamOptions#property_waituntilavailable)

I

[Deno.QuicServerTransportOptions](./././~/Deno.QuicServerTransportOptions "Deno.QuicServerTransportOptions")

No documentation available

-   [preferredAddressV4](./././~/Deno.QuicServerTransportOptions#property_preferredaddressv4)
-   [preferredAddressV6](./././~/Deno.QuicServerTransportOptions#property_preferredaddressv6)

I

[Deno.QuicTransportOptions](./././~/Deno.QuicTransportOptions "Deno.QuicTransportOptions")

No documentation available

-   [congestionControl](./././~/Deno.QuicTransportOptions#property_congestioncontrol)
-   [keepAliveInterval](./././~/Deno.QuicTransportOptions#property_keepaliveinterval)
-   [maxConcurrentBidirectionalStreams](./././~/Deno.QuicTransportOptions#property_maxconcurrentbidirectionalstreams)
-   [maxConcurrentUnidirectionalStreams](./././~/Deno.QuicTransportOptions#property_maxconcurrentunidirectionalstreams)
-   [maxIdleTimeout](./././~/Deno.QuicTransportOptions#property_maxidletimeout)

I

[Deno.ResolveDnsOptions](./././~/Deno.ResolveDnsOptions "Deno.ResolveDnsOptions")

Options which can be set when using [`Deno.resolveDns`](./././~/Deno.resolveDns).

-   [nameServer](./././~/Deno.ResolveDnsOptions#property_nameserver)
-   [signal](./././~/Deno.ResolveDnsOptions#property_signal)

I

[Deno.SoaRecord](./././~/Deno.SoaRecord "Deno.SoaRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"SOA"` record type specified, it will return an array of objects with this interface.

-   [expire](./././~/Deno.SoaRecord#property_expire)
-   [minimum](./././~/Deno.SoaRecord#property_minimum)
-   [mname](./././~/Deno.SoaRecord#property_mname)
-   [refresh](./././~/Deno.SoaRecord#property_refresh)
-   [retry](./././~/Deno.SoaRecord#property_retry)
-   [rname](./././~/Deno.SoaRecord#property_rname)
-   [serial](./././~/Deno.SoaRecord#property_serial)

I

[Deno.SrvRecord](./././~/Deno.SrvRecord "Deno.SrvRecord")

If [`Deno.resolveDns`](./././~/Deno.resolveDns) is called with `"SRV"` record type specified, it will return an array of objects with this interface.

-   [port](./././~/Deno.SrvRecord#property_port)
-   [priority](./././~/Deno.SrvRecord#property_priority)
-   [target](./././~/Deno.SrvRecord#property_target)
-   [weight](./././~/Deno.SrvRecord#property_weight)

I

[Deno.StartTlsOptions](./././~/Deno.StartTlsOptions "Deno.StartTlsOptions")

No documentation available

-   [alpnProtocols](./././~/Deno.StartTlsOptions#property_alpnprotocols)
-   [caCerts](./././~/Deno.StartTlsOptions#property_cacerts)
-   [hostname](./././~/Deno.StartTlsOptions#property_hostname)
-   [unsafelyDisableHostnameVerification](./././~/Deno.StartTlsOptions#property_unsafelydisablehostnameverification)

I

[Deno.TcpConn](./././~/Deno.TcpConn "Deno.TcpConn")

No documentation available

-   [setKeepAlive](./././~/Deno.TcpConn#method_setkeepalive_0)
-   [setNoDelay](./././~/Deno.TcpConn#method_setnodelay_0)

I

[Deno.TcpListenOptions](./././~/Deno.TcpListenOptions "Deno.TcpListenOptions")

No documentation available

-   [reusePort](./././~/Deno.TcpListenOptions#property_reuseport)

I

[Deno.TlsCertifiedKeyPem](./././~/Deno.TlsCertifiedKeyPem "Deno.TlsCertifiedKeyPem")

Provides certified key material from strings. The key material is provided in `PEM`\-format (Privacy Enhanced Mail, [https://www.rfc-editor.org/rfc/rfc1422](https://www.rfc-editor.org/rfc/rfc1422)) which can be identified by having `-----BEGIN-----` and `-----END-----` markers at the beginning and end of the strings. This type of key is not compatible with `DER`\-format keys which are binary.

-   [cert](./././~/Deno.TlsCertifiedKeyPem#property_cert)
-   [key](./././~/Deno.TlsCertifiedKeyPem#property_key)
-   [keyFormat](./././~/Deno.TlsCertifiedKeyPem#property_keyformat)

I

[Deno.TlsConn](./././~/Deno.TlsConn "Deno.TlsConn")

No documentation available

-   [handshake](./././~/Deno.TlsConn#method_handshake_0)

I

[Deno.TlsHandshakeInfo](./././~/Deno.TlsHandshakeInfo "Deno.TlsHandshakeInfo")

No documentation available

-   [alpnProtocol](./././~/Deno.TlsHandshakeInfo#property_alpnprotocol)

I

[Deno.UdpListenOptions](./././~/Deno.UdpListenOptions "Deno.UdpListenOptions")

Unstable options which can be set when opening a datagram listener via [`Deno.listenDatagram`](./././~/Deno.listenDatagram).

-   [loopback](./././~/Deno.UdpListenOptions#property_loopback)
-   [reuseAddress](./././~/Deno.UdpListenOptions#property_reuseaddress)

I

[Deno.UnixAddr](./././~/Deno.UnixAddr "Deno.UnixAddr")

No documentation available

-   [path](./././~/Deno.UnixAddr#property_path)
-   [transport](./././~/Deno.UnixAddr#property_transport)

I

[Deno.UnixConn](./././~/Deno.UnixConn "Deno.UnixConn")

No documentation available

I

[Deno.UnixConnectOptions](./././~/Deno.UnixConnectOptions "Deno.UnixConnectOptions")

No documentation available

-   [path](./././~/Deno.UnixConnectOptions#property_path)
-   [transport](./././~/Deno.UnixConnectOptions#property_transport)

I

[Deno.UnixListenOptions](./././~/Deno.UnixListenOptions "Deno.UnixListenOptions")

Options which can be set when opening a Unix listener via [`Deno.listen`](./././~/Deno.listen) or [`Deno.listenDatagram`](./././~/Deno.listenDatagram).

-   [path](./././~/Deno.UnixListenOptions#property_path)

I

[Deno.VsockAddr](./././~/Deno.VsockAddr "Deno.VsockAddr")

No documentation available

-   [cid](./././~/Deno.VsockAddr#property_cid)
-   [port](./././~/Deno.VsockAddr#property_port)
-   [transport](./././~/Deno.VsockAddr#property_transport)

I

[Deno.VsockConn](./././~/Deno.VsockConn "Deno.VsockConn")

No documentation available

I

[Deno.VsockConnectOptions](./././~/Deno.VsockConnectOptions "Deno.VsockConnectOptions")

No documentation available

-   [cid](./././~/Deno.VsockConnectOptions#property_cid)
-   [port](./././~/Deno.VsockConnectOptions#property_port)
-   [transport](./././~/Deno.VsockConnectOptions#property_transport)

I

[Deno.VsockListenOptions](./././~/Deno.VsockListenOptions "Deno.VsockListenOptions")

Options which can be set when opening a VSOCK listener via [`Deno.listen`](./././~/Deno.listen).

-   [cid](./././~/Deno.VsockListenOptions#property_cid)
-   [port](./././~/Deno.VsockListenOptions#property_port)

T

[Deno.Addr](./././~/Deno.Addr "Deno.Addr")

No documentation available

T

[Deno.RecordType](./././~/Deno.RecordType "Deno.RecordType")

The type of the resource record to resolve via DNS using [`Deno.resolveDns`](./././~/Deno.resolveDns).

T

[Deno.TcpListener](./././~/Deno.TcpListener "Deno.TcpListener")

Specialized listener that accepts TCP connections.

T

[Deno.TlsListener](./././~/Deno.TlsListener "Deno.TlsListener")

Specialized listener that accepts TLS connections.

T

[Deno.UnixListener](./././~/Deno.UnixListener "Deno.UnixListener")

Specialized listener that accepts Unix connections.

T

[Deno.VsockListener](./././~/Deno.VsockListener "Deno.VsockListener")

Specialized listener that accepts VSOCK connections.
