---
title: "PostgreSQL: Documentation: 18: 32.15. Environment Variables"
source: "https://www.postgresql.org/docs/current/libpq-envars.html"
canonical_url: "https://www.postgresql.org/docs/current/libpq-envars.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:47.836Z"
content_hash: "a9f6762a427ee21baa215b01250425347df9c11b945f8268df4cee7758a8ad35"
menu_path: ["PostgreSQL: Documentation: 18: 32.15. Environment Variables"]
section_path: []
nav_prev: {"path": "postgres/docs/current/external-interfaces.html/index.md", "title": "PostgreSQL: Documentation: 18: H.1.\u00a0Client Interfaces"}
nav_next: {"path": "postgres/docs/current/view-pg-indexes.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.12.\u00a0pg_indexes"}
---

The following environment variables can be used to select default connection parameter values, which will be used by [`PQconnectdb`](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-PQCONNECTDB), [`PQsetdbLogin`](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-PQSETDBLOGIN) and [`PQsetdb`](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-PQSETDB) if no value is directly specified by the calling code. These are useful to avoid hard-coding database connection information into simple client applications, for example.

*   `PGHOST` behaves the same as the [host](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-HOST) connection parameter.
    
*   `PGSSLNEGOTIATION` behaves the same as the [sslnegotiation](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLNEGOTIATION) connection parameter.
    
*   `PGHOSTADDR` behaves the same as the [hostaddr](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-HOSTADDR) connection parameter. This can be set instead of or in addition to `PGHOST` to avoid DNS lookup overhead.
    
*   `PGPORT` behaves the same as the [port](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-PORT) connection parameter.
    
*   `PGDATABASE` behaves the same as the [dbname](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-DBNAME) connection parameter.
    
*   `PGUSER` behaves the same as the [user](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-USER) connection parameter.
    
*   `PGPASSWORD` behaves the same as the [password](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-PASSWORD) connection parameter. Use of this environment variable is not recommended for security reasons, as some operating systems allow non-root users to see process environment variables via ps; instead consider using a password file (see [Section 32.16](https://www.postgresql.org/docs/current/libpq-pgpass.html "32.16. The Password File")).
    
*   `PGPASSFILE` behaves the same as the [passfile](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-PASSFILE) connection parameter.
    
*   `PGREQUIREAUTH` behaves the same as the [require\_auth](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-REQUIRE-AUTH) connection parameter.
    
*   `PGCHANNELBINDING` behaves the same as the [channel\_binding](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-CHANNEL-BINDING) connection parameter.
    
*   `PGSERVICE` behaves the same as the [service](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SERVICE) connection parameter.
    
*   `PGSERVICEFILE` specifies the name of the per-user connection service file (see [Section 32.17](https://www.postgresql.org/docs/current/libpq-pgservice.html "32.17. The Connection Service File")). Defaults to `~/.pg_service.conf`, or `%APPDATA%\postgresql\.pg_service.conf` on Microsoft Windows.
    
*   `PGOPTIONS` behaves the same as the [options](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-OPTIONS) connection parameter.
    
*   `PGAPPNAME` behaves the same as the [application\_name](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-APPLICATION-NAME) connection parameter.
    
*   `PGSSLMODE` behaves the same as the [sslmode](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLMODE) connection parameter.
    
*   `PGREQUIRESSL` behaves the same as the [requiressl](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-REQUIRESSL) connection parameter. This environment variable is deprecated in favor of the `PGSSLMODE` variable; setting both variables suppresses the effect of this one.
    
*   `PGSSLCOMPRESSION` behaves the same as the [sslcompression](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLCOMPRESSION) connection parameter.
    
*   `PGSSLCERT` behaves the same as the [sslcert](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLCERT) connection parameter.
    
*   `PGSSLKEY` behaves the same as the [sslkey](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLKEY) connection parameter.
    
*   `PGSSLCERTMODE` behaves the same as the [sslcertmode](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLCERTMODE) connection parameter.
    
*   `PGSSLROOTCERT` behaves the same as the [sslrootcert](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLROOTCERT) connection parameter.
    
*   `PGSSLCRL` behaves the same as the [sslcrl](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLCRL) connection parameter.
    
*   `PGSSLCRLDIR` behaves the same as the [sslcrldir](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLCRLDIR) connection parameter.
    
*   `PGSSLSNI` behaves the same as the [sslsni](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSLSNI) connection parameter.
    
*   `PGREQUIREPEER` behaves the same as the [requirepeer](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-REQUIREPEER) connection parameter.
    
*   `PGSSLMINPROTOCOLVERSION` behaves the same as the [ssl\_min\_protocol\_version](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSL-MIN-PROTOCOL-VERSION) connection parameter.
    
*   `PGSSLMAXPROTOCOLVERSION` behaves the same as the [ssl\_max\_protocol\_version](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-SSL-MAX-PROTOCOL-VERSION) connection parameter.
    
*   `PGGSSENCMODE` behaves the same as the [gssencmode](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-GSSENCMODE) connection parameter.
    
*   `PGKRBSRVNAME` behaves the same as the [krbsrvname](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-KRBSRVNAME) connection parameter.
    
*   `PGGSSLIB` behaves the same as the [gsslib](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-GSSLIB) connection parameter.
    
*   `PGGSSDELEGATION` behaves the same as the [gssdelegation](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-GSSDELEGATION) connection parameter.
    
*   `PGCONNECT_TIMEOUT` behaves the same as the [connect\_timeout](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-CONNECT-TIMEOUT) connection parameter.
    
*   `PGCLIENTENCODING` behaves the same as the [client\_encoding](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-CLIENT-ENCODING) connection parameter.
    
*   `PGTARGETSESSIONATTRS` behaves the same as the [target\_session\_attrs](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-TARGET-SESSION-ATTRS) connection parameter.
    
*   `PGLOADBALANCEHOSTS` behaves the same as the [load\_balance\_hosts](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-LOAD-BALANCE-HOSTS) connection parameter.
    
*   `PGMINPROTOCOLVERSION` behaves the same as the [min\_protocol\_version](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-MIN-PROTOCOL-VERSION) connection parameter.
    
*   `PGMAXPROTOCOLVERSION` behaves the same as the [max\_protocol\_version](postgres/docs/current/libpq-connect.html/index.md#LIBPQ-CONNECT-MAX-PROTOCOL-VERSION) connection parameter.
    

The following environment variables can be used to specify default behavior for each PostgreSQL session. (See also the [ALTER ROLE](https://www.postgresql.org/docs/current/sql-alterrole.html "ALTER ROLE") and [ALTER DATABASE](https://www.postgresql.org/docs/current/sql-alterdatabase.html "ALTER DATABASE") commands for ways to set default behavior on a per-user or per-database basis.)

*   `PGDATESTYLE` sets the default style of date/time representation. (Equivalent to `SET datestyle TO ...`.)
    
*   `PGTZ` sets the default time zone. (Equivalent to `SET timezone TO ...`.)
    
*   `PGGEQO` sets the default mode for the genetic query optimizer. (Equivalent to `SET geqo TO ...`.)
    

Refer to the SQL command [SET](https://www.postgresql.org/docs/current/sql-set.html "SET") for information on correct values for these environment variables.

The following environment variables determine internal behavior of libpq; they override compiled-in defaults.

*   `PGSYSCONFDIR` sets the directory containing the `pg_service.conf` file and in a future version possibly other system-wide configuration files.
    
*   `PGLOCALEDIR` sets the directory containing the `locale` files for message localization.
