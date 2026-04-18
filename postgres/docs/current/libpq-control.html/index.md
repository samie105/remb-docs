---
title: "PostgreSQL: Documentation: 18: 32.11. Control Functions"
source: "https://www.postgresql.org/docs/current/libpq-control.html"
canonical_url: "https://www.postgresql.org/docs/current/libpq-control.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:21.349Z"
content_hash: "fc5eb1cd40906afbf6e0d3ed9406192000429b46fb0dd08f4fbb4f877f3e0cdf"
menu_path: ["PostgreSQL: Documentation: 18: 32.11. Control Functions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/external-admin-tools.html/index.md", "title": "PostgreSQL: Documentation: 18: H.2.\u00a0Administration Tools"}
nav_next: {"path": "postgres/docs/current/sql-dropcollation.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP COLLATION"}
---

These functions control miscellaneous details of libpq's behavior.

`PQclientEncoding` [#](#LIBPQ-PQCLIENTENCODING)

Returns the client encoding.

int PQclientEncoding(const PGconn \*_`conn`_);

Note that it returns the encoding ID, not a symbolic string such as `EUC_JP`. If unsuccessful, it returns -1. To convert an encoding ID to an encoding name, you can use:

char \*pg\_encoding\_to\_char(int _`encoding_id`_);

`PQsetClientEncoding` [#](#LIBPQ-PQSETCLIENTENCODING)

Sets the client encoding.

int PQsetClientEncoding(PGconn \*_`conn`_, const char \*_`encoding`_);

_`conn`_ is a connection to the server, and _`encoding`_ is the encoding you want to use. If the function successfully sets the encoding, it returns 0, otherwise -1. The current encoding for this connection can be determined by using [`PQclientEncoding`](postgres/docs/current/libpq-control.html/index.md#LIBPQ-PQCLIENTENCODING).

`PQsetErrorVerbosity` [#](#LIBPQ-PQSETERRORVERBOSITY)

Determines the verbosity of messages returned by [`PQerrorMessage`](https://www.postgresql.org/docs/current/libpq-status.html#LIBPQ-PQERRORMESSAGE) and [`PQresultErrorMessage`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQRESULTERRORMESSAGE).

typedef enum
{
    PQERRORS\_TERSE,
    PQERRORS\_DEFAULT,
    PQERRORS\_VERBOSE,
    PQERRORS\_SQLSTATE
} PGVerbosity;

PGVerbosity PQsetErrorVerbosity(PGconn \*conn, PGVerbosity verbosity);

[`PQsetErrorVerbosity`](postgres/docs/current/libpq-control.html/index.md#LIBPQ-PQSETERRORVERBOSITY) sets the verbosity mode, returning the connection's previous setting. In _TERSE_ mode, returned messages include severity, primary text, and position only; this will normally fit on a single line. The _DEFAULT_ mode produces messages that include the above plus any detail, hint, or context fields (these might span multiple lines). The _VERBOSE_ mode includes all available fields. The _SQLSTATE_ mode includes only the error severity and the `SQLSTATE` error code, if one is available (if not, the output is like _TERSE_ mode).

Changing the verbosity setting does not affect the messages available from already-existing `PGresult` objects, only subsequently-created ones. (But see [`PQresultVerboseErrorMessage`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQRESULTVERBOSEERRORMESSAGE) if you want to print a previous error with a different verbosity.)

`PQsetErrorContextVisibility` [#](#LIBPQ-PQSETERRORCONTEXTVISIBILITY)

Determines the handling of `CONTEXT` fields in messages returned by [`PQerrorMessage`](https://www.postgresql.org/docs/current/libpq-status.html#LIBPQ-PQERRORMESSAGE) and [`PQresultErrorMessage`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQRESULTERRORMESSAGE).

typedef enum
{
    PQSHOW\_CONTEXT\_NEVER,
    PQSHOW\_CONTEXT\_ERRORS,
    PQSHOW\_CONTEXT\_ALWAYS
} PGContextVisibility;

PGContextVisibility PQsetErrorContextVisibility(PGconn \*conn, PGContextVisibility show\_context);

[`PQsetErrorContextVisibility`](postgres/docs/current/libpq-control.html/index.md#LIBPQ-PQSETERRORCONTEXTVISIBILITY) sets the context display mode, returning the connection's previous setting. This mode controls whether the `CONTEXT` field is included in messages. The _NEVER_ mode never includes `CONTEXT`, while _ALWAYS_ always includes it if available. In _ERRORS_ mode (the default), `CONTEXT` fields are included only in error messages, not in notices and warnings. (However, if the verbosity setting is _TERSE_ or _SQLSTATE_, `CONTEXT` fields are omitted regardless of the context display mode.)

Changing this mode does not affect the messages available from already-existing `PGresult` objects, only subsequently-created ones. (But see [`PQresultVerboseErrorMessage`](https://www.postgresql.org/docs/current/libpq-exec.html#LIBPQ-PQRESULTVERBOSEERRORMESSAGE) if you want to print a previous error with a different display mode.)

`PQtrace` [#](#LIBPQ-PQTRACE)

Enables tracing of the client/server communication to a debugging file stream.

void PQtrace(PGconn \*conn, FILE \*stream);

Each line consists of: an optional timestamp, a direction indicator (`F` for messages from client to server or `B` for messages from server to client), message length, message type, and message contents. Non-message contents fields (timestamp, direction, length and message type) are separated by a tab. Message contents are separated by a space. Protocol strings are enclosed in double quotes, while strings used as data values are enclosed in single quotes. Non-printable chars are printed as hexadecimal escapes. Further message-type-specific detail can be found in [Section 54.7](https://www.postgresql.org/docs/current/protocol-message-formats.html "54.7. Message Formats").

### Note

On Windows, if the libpq library and an application are compiled with different flags, this function call will crash the application because the internal representation of the `FILE` pointers differ. Specifically, multithreaded/single-threaded, release/debug, and static/dynamic flags should be the same for the library and all applications using that library.

`PQsetTraceFlags` [#](#LIBPQ-PQSETTRACEFLAGS)

Controls the tracing behavior of client/server communication.

void PQsetTraceFlags(PGconn \*conn, int flags);

`flags` contains flag bits describing the operating mode of tracing. If `flags` contains `PQTRACE_SUPPRESS_TIMESTAMPS`, then the timestamp is not included when printing each message. If `flags` contains `PQTRACE_REGRESS_MODE`, then some fields are redacted when printing each message, such as object OIDs, to make the output more convenient to use in testing frameworks. This function must be called after calling `PQtrace`.

`PQuntrace` [#](#LIBPQ-PQUNTRACE)

Disables tracing started by [`PQtrace`](postgres/docs/current/libpq-control.html/index.md#LIBPQ-PQTRACE).

void PQuntrace(PGconn \*conn);

