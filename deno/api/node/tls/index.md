---
title: "tls - Node documentation"
source: "https://docs.deno.com/api/node/tls/"
canonical_url: "https://docs.deno.com/api/node/tls/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:14:34.018Z"
content_hash: "77f6bad8b9fd73d65e56306ecd0fa2373688e9d25c7ac7dddf9a29b2251e34b0"
menu_path: ["tls - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../timers/promises/index.md", "title": "timers/promises - Node documentation"}
nav_next: {"path": "../trace_events/index.md", "title": "trace_events - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:tls";
```

The `node:tls` module provides an implementation of the Transport Layer Security (TLS) and Secure Socket Layer (SSL) protocols that is built on top of OpenSSL. The module can be accessed using:

```js
import tls from 'node:tls';
```

c

[Server](.././tls/~/Server "Server")

Accepts encrypted connections using TLS or SSL.

-   [addContext](.././tls/~/Server#method_addcontext_0)
-   [addListener](.././tls/~/Server#method_addlistener_0)
-   [emit](.././tls/~/Server#method_emit_0)
-   [getTicketKeys](.././tls/~/Server#method_getticketkeys_0)
-   [on](.././tls/~/Server#method_on_0)
-   [once](.././tls/~/Server#method_once_0)
-   [prependListener](.././tls/~/Server#method_prependlistener_0)
-   [prependOnceListener](.././tls/~/Server#method_prependoncelistener_0)
-   [setSecureContext](.././tls/~/Server#method_setsecurecontext_0)
-   [setTicketKeys](.././tls/~/Server#method_setticketkeys_0)

c

[TLSSocket](.././tls/~/TLSSocket "TLSSocket")

Performs transparent encryption of written data and all required TLS negotiation.

-   [addListener](.././tls/~/TLSSocket#method_addlistener_0)
-   [alpnProtocol](.././tls/~/TLSSocket#property_alpnprotocol)
-   [authorizationError](.././tls/~/TLSSocket#property_authorizationerror)
-   [authorized](.././tls/~/TLSSocket#property_authorized)
-   [disableRenegotiation](.././tls/~/TLSSocket#method_disablerenegotiation_0)
-   [emit](.././tls/~/TLSSocket#method_emit_0)
-   [enableTrace](.././tls/~/TLSSocket#method_enabletrace_0)
-   [encrypted](.././tls/~/TLSSocket#property_encrypted)
-   [exportKeyingMaterial](.././tls/~/TLSSocket#method_exportkeyingmaterial_0)
-   [getCertificate](.././tls/~/TLSSocket#method_getcertificate_0)
-   [getCipher](.././tls/~/TLSSocket#method_getcipher_0)
-   [getEphemeralKeyInfo](.././tls/~/TLSSocket#method_getephemeralkeyinfo_0)
-   [getFinished](.././tls/~/TLSSocket#method_getfinished_0)
-   [getPeerCertificate](.././tls/~/TLSSocket#method_getpeercertificate_0)
-   [getPeerFinished](.././tls/~/TLSSocket#method_getpeerfinished_0)
-   [getPeerX509Certificate](.././tls/~/TLSSocket#method_getpeerx509certificate_0)
-   [getProtocol](.././tls/~/TLSSocket#method_getprotocol_0)
-   [getSession](.././tls/~/TLSSocket#method_getsession_0)
-   [getSharedSigalgs](.././tls/~/TLSSocket#method_getsharedsigalgs_0)
-   [getTLSTicket](.././tls/~/TLSSocket#method_gettlsticket_0)
-   [getX509Certificate](.././tls/~/TLSSocket#method_getx509certificate_0)
-   [isSessionReused](.././tls/~/TLSSocket#method_issessionreused_0)
-   [on](.././tls/~/TLSSocket#method_on_0)
-   [once](.././tls/~/TLSSocket#method_once_0)
-   [prependListener](.././tls/~/TLSSocket#method_prependlistener_0)
-   [prependOnceListener](.././tls/~/TLSSocket#method_prependoncelistener_0)
-   [renegotiate](.././tls/~/TLSSocket#method_renegotiate_0)
-   [setMaxSendFragment](.././tls/~/TLSSocket#method_setmaxsendfragment_0)

f

[checkServerIdentity](.././tls/~/checkServerIdentity "checkServerIdentity")

Verifies the certificate `cert` is issued to `hostname`.

f

[connect](.././tls/~/connect "connect")

The `callback` function, if specified, will be added as a listener for the `'secureConnect'` event.

f

[createSecureContext](.././tls/~/createSecureContext "createSecureContext")

`[createServer](.././tls/~/createServer)` sets the default value of the `honorCipherOrder` option to `true`, other APIs that create secure contexts leave it unset.

f

[createServer](.././tls/~/createServer "createServer")

Creates a new [Server](.././tls/~/Server). The `secureConnectionListener`, if provided, is automatically set as a listener for the `'secureConnection'` event.

f

[getCiphers](.././tls/~/getCiphers "getCiphers")

Returns an array with the names of the supported TLS ciphers. The names are lower-case for historical reasons, but must be uppercased to be used in the `ciphers` option of `[createSecureContext](.././tls/~/createSecureContext)`.

f

[createSecurePair](.././tls/~/createSecurePair "createSecurePair")

No documentation available

I

[Certificate](.././tls/~/Certificate "Certificate")

No documentation available

-   [C](.././tls/~/Certificate#property_c)
-   [CN](.././tls/~/Certificate#property_cn)
-   [L](.././tls/~/Certificate#property_l)
-   [O](.././tls/~/Certificate#property_o)
-   [OU](.././tls/~/Certificate#property_ou)
-   [ST](.././tls/~/Certificate#property_st)

I

[CipherNameAndProtocol](.././tls/~/CipherNameAndProtocol "CipherNameAndProtocol")

No documentation available

-   [name](.././tls/~/CipherNameAndProtocol#property_name)
-   [standardName](.././tls/~/CipherNameAndProtocol#property_standardname)
-   [version](.././tls/~/CipherNameAndProtocol#property_version)

I

[CommonConnectionOptions](.././tls/~/CommonConnectionOptions "CommonConnectionOptions")

No documentation available

-   [ALPNProtocols](.././tls/~/CommonConnectionOptions#property_alpnprotocols)
-   [SNICallback](.././tls/~/CommonConnectionOptions#property_snicallback)
-   [enableTrace](.././tls/~/CommonConnectionOptions#property_enabletrace)
-   [rejectUnauthorized](.././tls/~/CommonConnectionOptions#property_rejectunauthorized)
-   [requestCert](.././tls/~/CommonConnectionOptions#property_requestcert)
-   [secureContext](.././tls/~/CommonConnectionOptions#property_securecontext)

I

[ConnectionOptions](.././tls/~/ConnectionOptions "ConnectionOptions")

No documentation available

-   [checkServerIdentity](.././tls/~/ConnectionOptions#property_checkserveridentity)
-   [host](.././tls/~/ConnectionOptions#property_host)
-   [lookup](.././tls/~/ConnectionOptions#property_lookup)
-   [minDHSize](.././tls/~/ConnectionOptions#property_mindhsize)
-   [path](.././tls/~/ConnectionOptions#property_path)
-   [port](.././tls/~/ConnectionOptions#property_port)
-   [pskCallback](.././tls/~/ConnectionOptions#method_pskcallback_0)
-   [servername](.././tls/~/ConnectionOptions#property_servername)
-   [session](.././tls/~/ConnectionOptions#property_session)
-   [socket](.././tls/~/ConnectionOptions#property_socket)
-   [timeout](.././tls/~/ConnectionOptions#property_timeout)

I

[DetailedPeerCertificate](.././tls/~/DetailedPeerCertificate "DetailedPeerCertificate")

No documentation available

-   [issuerCertificate](.././tls/~/DetailedPeerCertificate#property_issuercertificate)

I

[EphemeralKeyInfo](.././tls/~/EphemeralKeyInfo "EphemeralKeyInfo")

No documentation available

-   [name](.././tls/~/EphemeralKeyInfo#property_name)
-   [size](.././tls/~/EphemeralKeyInfo#property_size)
-   [type](.././tls/~/EphemeralKeyInfo#property_type)

I

[KeyObject](.././tls/~/KeyObject "KeyObject")

No documentation available

-   [passphrase](.././tls/~/KeyObject#property_passphrase)
-   [pem](.././tls/~/KeyObject#property_pem)

I

[PeerCertificate](.././tls/~/PeerCertificate "PeerCertificate")

No documentation available

-   [asn1Curve](.././tls/~/PeerCertificate#property_asn1curve)
-   [bits](.././tls/~/PeerCertificate#property_bits)
-   [ca](.././tls/~/PeerCertificate#property_ca)
-   [exponent](.././tls/~/PeerCertificate#property_exponent)
-   [ext\_key\_usage](.././tls/~/PeerCertificate#property_ext_key_usage)
-   [fingerprint](.././tls/~/PeerCertificate#property_fingerprint)
-   [fingerprint256](.././tls/~/PeerCertificate#property_fingerprint256)
-   [fingerprint512](.././tls/~/PeerCertificate#property_fingerprint512)
-   [infoAccess](.././tls/~/PeerCertificate#property_infoaccess)
-   [issuer](.././tls/~/PeerCertificate#property_issuer)
-   [modulus](.././tls/~/PeerCertificate#property_modulus)
-   [nistCurve](.././tls/~/PeerCertificate#property_nistcurve)
-   [pubkey](.././tls/~/PeerCertificate#property_pubkey)
-   [raw](.././tls/~/PeerCertificate#property_raw)
-   [serialNumber](.././tls/~/PeerCertificate#property_serialnumber)
-   [subject](.././tls/~/PeerCertificate#property_subject)
-   [subjectaltname](.././tls/~/PeerCertificate#property_subjectaltname)
-   [valid\_from](.././tls/~/PeerCertificate#property_valid_from)
-   [valid\_to](.././tls/~/PeerCertificate#property_valid_to)

I

[PSKCallbackNegotation](.././tls/~/PSKCallbackNegotation "PSKCallbackNegotation")

No documentation available

-   [identity](.././tls/~/PSKCallbackNegotation#property_identity)
-   [psk](.././tls/~/PSKCallbackNegotation#property_psk)

I

[PxfObject](.././tls/~/PxfObject "PxfObject")

No documentation available

-   [buf](.././tls/~/PxfObject#property_buf)
-   [passphrase](.././tls/~/PxfObject#property_passphrase)

I

[SecureContext](.././tls/~/SecureContext "SecureContext")

No documentation available

-   [context](.././tls/~/SecureContext#property_context)

I

[SecureContextOptions](.././tls/~/SecureContextOptions "SecureContextOptions")

No documentation available

-   [ALPNCallback](.././tls/~/SecureContextOptions#property_alpncallback)
-   [allowPartialTrustChain](.././tls/~/SecureContextOptions#property_allowpartialtrustchain)
-   [ca](.././tls/~/SecureContextOptions#property_ca)
-   [cert](.././tls/~/SecureContextOptions#property_cert)
-   [ciphers](.././tls/~/SecureContextOptions#property_ciphers)
-   [clientCertEngine](.././tls/~/SecureContextOptions#property_clientcertengine)
-   [crl](.././tls/~/SecureContextOptions#property_crl)
-   [dhparam](.././tls/~/SecureContextOptions#property_dhparam)
-   [ecdhCurve](.././tls/~/SecureContextOptions#property_ecdhcurve)
-   [honorCipherOrder](.././tls/~/SecureContextOptions#property_honorcipherorder)
-   [key](.././tls/~/SecureContextOptions#property_key)
-   [maxVersion](.././tls/~/SecureContextOptions#property_maxversion)
-   [minVersion](.././tls/~/SecureContextOptions#property_minversion)
-   [passphrase](.././tls/~/SecureContextOptions#property_passphrase)
-   [pfx](.././tls/~/SecureContextOptions#property_pfx)
-   [privateKeyEngine](.././tls/~/SecureContextOptions#property_privatekeyengine)
-   [privateKeyIdentifier](.././tls/~/SecureContextOptions#property_privatekeyidentifier)
-   [secureOptions](.././tls/~/SecureContextOptions#property_secureoptions)
-   [secureProtocol](.././tls/~/SecureContextOptions#property_secureprotocol)
-   [sessionIdContext](.././tls/~/SecureContextOptions#property_sessionidcontext)
-   [sessionTimeout](.././tls/~/SecureContextOptions#property_sessiontimeout)
-   [sigalgs](.././tls/~/SecureContextOptions#property_sigalgs)
-   [ticketKeys](.././tls/~/SecureContextOptions#property_ticketkeys)

I

[TlsOptions](.././tls/~/TlsOptions "TlsOptions")

No documentation available

-   [handshakeTimeout](.././tls/~/TlsOptions#property_handshaketimeout)
-   [pskCallback](.././tls/~/TlsOptions#method_pskcallback_0)
-   [pskIdentityHint](.././tls/~/TlsOptions#property_pskidentityhint)
-   [sessionTimeout](.././tls/~/TlsOptions#property_sessiontimeout)
-   [ticketKeys](.././tls/~/TlsOptions#property_ticketkeys)

I

[TLSSocketOptions](.././tls/~/TLSSocketOptions "TLSSocketOptions")

No documentation available

-   [isServer](.././tls/~/TLSSocketOptions#property_isserver)
-   [requestOCSP](.././tls/~/TLSSocketOptions#property_requestocsp)
-   [server](.././tls/~/TLSSocketOptions#property_server)
-   [session](.././tls/~/TLSSocketOptions#property_session)

I

[SecurePair](.././tls/~/SecurePair "SecurePair")

No documentation available

-   [cleartext](.././tls/~/SecurePair#property_cleartext)
-   [encrypted](.././tls/~/SecurePair#property_encrypted)

T

[SecureVersion](.././tls/~/SecureVersion "SecureVersion")

No documentation available

v

[CLIENT\_RENEG\_LIMIT](.././tls/~/CLIENT_RENEG_LIMIT "CLIENT_RENEG_LIMIT")

No documentation available

v

[CLIENT\_RENEG\_WINDOW](.././tls/~/CLIENT_RENEG_WINDOW "CLIENT_RENEG_WINDOW")

No documentation available

v

[DEFAULT\_CIPHERS](.././tls/~/DEFAULT_CIPHERS "DEFAULT_CIPHERS")

The default value of the `ciphers` option of `createSecureContext()`. It can be assigned any of the supported OpenSSL ciphers. Defaults to the content of `crypto.constants.defaultCoreCipherList`, unless changed using CLI options using `--tls-default-ciphers`.

v

[DEFAULT\_ECDH\_CURVE](.././tls/~/DEFAULT_ECDH_CURVE "DEFAULT_ECDH_CURVE")

The default curve name to use for ECDH key agreement in a tls server. The default value is `'auto'`. See `createSecureContext()` for further information.

v

[DEFAULT\_MAX\_VERSION](.././tls/~/DEFAULT_MAX_VERSION "DEFAULT_MAX_VERSION")

The default value of the `maxVersion` option of `createSecureContext()`. It can be assigned any of the supported TLS protocol versions, `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. **Default:** `'TLSv1.3'`, unless changed using CLI options. Using `--tls-max-v1.2` sets the default to `'TLSv1.2'`. Using `--tls-max-v1.3` sets the default to `'TLSv1.3'`. If multiple of the options are provided, the highest maximum is used.

v

[DEFAULT\_MIN\_VERSION](.././tls/~/DEFAULT_MIN_VERSION "DEFAULT_MIN_VERSION")

The default value of the `minVersion` option of `createSecureContext()`. It can be assigned any of the supported TLS protocol versions, `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. **Default:** `'TLSv1.2'`, unless changed using CLI options. Using `--tls-min-v1.0` sets the default to `'TLSv1'`. Using `--tls-min-v1.1` sets the default to `'TLSv1.1'`. Using `--tls-min-v1.3` sets the default to `'TLSv1.3'`. If multiple of the options are provided, the lowest minimum is used.

v

[rootCertificates](.././tls/~/rootCertificates "rootCertificates")

An immutable array of strings representing the root certificates (in PEM format) from the bundled Mozilla CA store as supplied by the current Node.js version.
