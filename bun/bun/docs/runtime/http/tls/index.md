---
title: "TLS"
source: "https://bun.com/docs/runtime/http/tls"
canonical_url: "https://bun.com/docs/runtime/http/tls"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:10.648Z"
content_hash: "649da1e9213238996495c276a1a67e06f9014c51349d097c0d2beba8b6b6dc3b"
menu_path: ["TLS"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/http/routing/index.md", "title": "Routing"}
nav_next: {"path": "bun/bun/docs/runtime/http/server/index.md", "title": "Server"}
---

Bun supports TLS out of the box, powered by [BoringSSL](https://boringssl.googlesource.com/boringssl). Enable TLS by passing in a value for `key` and `cert`; both are required to enable TLS.

```
Bun.serve({
  tls: {
    key: Bun.file("./key.pem"), 
    cert: Bun.file("./cert.pem"), 
  },
});
```

The `key` and `cert` fields expect the _contents_ of your TLS key and certificate, _not a path to it_. This can be a string, `BunFile`, `TypedArray`, or `Buffer`.

```
Bun.serve({
  tls: {
    key: Bun.file("./key.pem"), // BunFile
    key: fs.readFileSync("./key.pem"), // Buffer
    key: fs.readFileSync("./key.pem", "utf8"), // string
    key: [Bun.file("./key1.pem"), Bun.file("./key2.pem")], // array of above
  },
});
```

### Passphrase

If your private key is encrypted with a passphrase, provide a value for `passphrase` to decrypt it.

```
Bun.serve({
  tls: {
    key: Bun.file("./key.pem"),
    cert: Bun.file("./cert.pem"),
    passphrase: "my-secret-passphrase", 
  },
});
```

### CA Certificates

Optionally, you can override the trusted CA certificates by passing a value for `ca`. By default, the server will trust the list of well-known CAs curated by Mozilla. When `ca` is specified, the Mozilla list is overwritten.

```
Bun.serve({
  tls: {
    key: Bun.file("./key.pem"), // path to TLS key
    cert: Bun.file("./cert.pem"), // path to TLS cert
    ca: Bun.file("./ca.pem"), // path to root CA certificate
  },
});
```

### Diffie-Hellman

To override Diffie-Hellman parameters:

```
Bun.serve({
  tls: {
    dhParamsFile: "/path/to/dhparams.pem", // path to Diffie Hellman parameters
  },
});
```

* * *

## Server name indication (SNI)

To configure the server name indication (SNI) for the server, set the `serverName` field in the `tls` object.

```
Bun.serve({
  tls: {
    serverName: "my-server.com", // SNI
  },
});
```

To allow multiple server names, pass an array of objects to `tls`, each with a `serverName` field.

```
Bun.serve({
  tls: [
    {
      key: Bun.file("./key1.pem"),
      cert: Bun.file("./cert1.pem"),
      serverName: "my-server1.com", 
    },
    {
      key: Bun.file("./key2.pem"),
      cert: Bun.file("./cert2.pem"),
      serverName: "my-server2.com", 
    },
  ],
});
```
