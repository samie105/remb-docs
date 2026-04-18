---
title: "PostgreSQL: Documentation: 18: 18.10. Secure TCP/IP Connections with GSSAPI Encryption"
source: "https://www.postgresql.org/docs/current/gssapi-enc.html"
canonical_url: "https://www.postgresql.org/docs/current/gssapi-enc.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:00.197Z"
content_hash: "a42bf12461858780c8eefc6a4df6e9c4d7ecb9b5b55f74fa88ac14304501d8af"
menu_path: ["PostgreSQL: Documentation: 18: 18.10. Secure TCP/IP Connections with GSSAPI Encryption"]
section_path: []
---
PostgreSQL also has native support for using GSSAPI to encrypt client/server communications for increased security. Support requires that a GSSAPI implementation (such as MIT Kerberos) is installed on both client and server systems, and that support in PostgreSQL is enabled at build time (see [Chapter 17](https://www.postgresql.org/docs/current/installation.html "Chapter 17. Installation from Source Code")).

### 18.10.1. Basic Setup [#](#GSSAPI-SETUP)

The PostgreSQL server will listen for both normal and GSSAPI\-encrypted connections on the same TCP port, and will negotiate with any connecting client whether to use GSSAPI for encryption (and for authentication). By default, this decision is up to the client (which means it can be downgraded by an attacker); see [Section 20.1](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html "20.1. The pg_hba.conf File") about setting up the server to require the use of GSSAPI for some or all connections.

When using GSSAPI for encryption, it is common to use GSSAPI for authentication as well, since the underlying mechanism will determine both client and server identities (according to the GSSAPI implementation) in any case. But this is not required; another PostgreSQL authentication method can be chosen to perform additional verification.

Other than configuration of the negotiation behavior, GSSAPI encryption requires no setup beyond that which is necessary for GSSAPI authentication. (For more information on configuring that, see [Section 20.6](https://www.postgresql.org/docs/current/gssapi-auth.html "20.6. GSSAPI Authentication").)
