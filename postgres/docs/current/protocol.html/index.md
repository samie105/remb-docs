---
title: "PostgreSQL: Documentation: 18: Chapter 54. Frontend/Backend Protocol"
source: "https://www.postgresql.org/docs/current/protocol.html"
canonical_url: "https://www.postgresql.org/docs/current/protocol.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:33.465Z"
content_hash: "7f7e97e5325512d109e7bc82c50f8aa11d67e7649c68120b95523935311ffb2a"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 54. Frontend/Backend Protocol"]
section_path: []
---
PostgreSQL uses a message-based protocol for communication between frontends and backends (clients and servers). The protocol is supported over TCP/IP and also over Unix-domain sockets. Port number 5432 has been registered with IANA as the customary TCP port number for servers supporting this protocol, but in practice any non-privileged port number can be used.

This document describes version 3.2 of the protocol, introduced in PostgreSQL version 18. The server and the libpq client library are backwards compatible with protocol version 3.0, implemented in PostgreSQL 7.4 and later.

In order to serve multiple clients efficiently, the server launches a new “backend” process for each client. In the current implementation, a new child process is created immediately after an incoming connection is detected. This is transparent to the protocol, however. For purposes of the protocol, the terms “backend” and “server” are interchangeable; likewise “frontend” and “client” are interchangeable.
