---
title: "PostgreSQL: Documentation: 18: CREATE SERVER"
source: "https://www.postgresql.org/docs/current/sql-createserver.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-createserver.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:32.454Z"
content_hash: "982fea055af3e981e12d13b191038702ec81414e651453de51211095dd3dbf3e"
menu_path: ["PostgreSQL: Documentation: 18: CREATE SERVER"]
section_path: []
---
CREATE SERVER — define a new foreign server

## Synopsis

CREATE SERVER \[ IF NOT EXISTS \] _`server_name`_ \[ TYPE '_`server_type`_' \] \[ VERSION '_`server_version`_' \]
    FOREIGN DATA WRAPPER _`fdw_name`_
    \[ OPTIONS ( _`option`_ '_`value`_' \[, ... \] ) \]

## Description

`CREATE SERVER` defines a new foreign server. The user who defines the server becomes its owner.

A foreign server typically encapsulates connection information that a foreign-data wrapper uses to access an external data resource. Additional user-specific connection information may be specified by means of user mappings.

The server name must be unique within the database.

Creating a server requires `USAGE` privilege on the foreign-data wrapper being used.

## Parameters

`IF NOT EXISTS`

Do not throw an error if a server with the same name already exists. A notice is issued in this case. Note that there is no guarantee that the existing server is anything like the one that would have been created.

_`server_name`_

The name of the foreign server to be created.

_`server_type`_

Optional server type, potentially useful to foreign-data wrappers.

_`server_version`_

Optional server version, potentially useful to foreign-data wrappers.

_`fdw_name`_

The name of the foreign-data wrapper that manages the server.

``OPTIONS ( _`option`_ '_`value`_' [, ... ] )``

This clause specifies the options for the server. The options typically define the connection details of the server, but the actual names and values are dependent on the server's foreign-data wrapper.

## Notes

When using the [dblink](https://www.postgresql.org/docs/current/dblink.html "F.11. dblink — connect to other PostgreSQL databases") module, a foreign server's name can be used as an argument of the [dblink\_connect](https://www.postgresql.org/docs/current/contrib-dblink-connect.html "dblink_connect") function to indicate the connection parameters. It is necessary to have the `USAGE` privilege on the foreign server to be able to use it in this way.

If the foreign server supports sort pushdown, it is necessary for it to have the same sort ordering as the local server.

## Examples

Create a server `myserver` that uses the foreign-data wrapper `postgres_fdw`:

CREATE SERVER myserver FOREIGN DATA WRAPPER postgres\_fdw OPTIONS (host 'foo', dbname 'foodb', port '5432');

See [postgres\_fdw](https://www.postgresql.org/docs/current/postgres-fdw.html "F.38. postgres_fdw — access data stored in external PostgreSQL servers") for more details.

## Compatibility

`CREATE SERVER` conforms to ISO/IEC 9075-9 (SQL/MED).
