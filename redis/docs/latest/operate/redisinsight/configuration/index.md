---
title: "Redis Insight configuration settings"
source: "https://redis.io/docs/latest/operate/redisinsight/configuration/"
canonical_url: "https://redis.io/docs/latest/operate/redisinsight/configuration/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:29.908Z"
content_hash: "726488816b9e56a15bd435a8367357555081ac34ab115871c500acc42d79b81c"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight configuration settings","→","Redis Insight configuration settings"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight configuration settings","→","Redis Insight configuration settings"]
nav_prev: {"path": "redis/docs/latest/develop/reference/clients/index.md", "title": "Redis client handling"}
nav_next: {"path": "redis/docs/latest/operate/rc/databases/active-active/create-active-active-database/index.md", "title": "Create an Active-Active database"}
---

# Redis Insight configuration settings

Redis Insight

## Configuration environment variables

Variable

Purpose

Default

Additional info

RI\_APP\_PORT

The port that Redis Insight listens on.

*   Docker: 5540
*   desktop: 5530

See [Express Documentation](https://expressjs.com/en/api.html#app.listen)

RI\_APP\_HOST

The host that Redis Insight connects to.

*   Docker: 0.0.0.0
*   desktop: 127.0.0.1

See [Express Documentation](https://expressjs.com/en/api.html#app.listen)

RI\_SERVER\_TLS\_KEY

Private key for HTTPS.

n/a

Private key in [PEM format](https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/#ftoc-heading-3). Can be a path to a file or a string in PEM format.

RI\_SERVER\_TLS\_CERT

Certificate for supplied private key.

n/a

Public certificate in [PEM format](https://www.ssl.com/guide/pem-der-crt-and-cer-x-509-encodings-and-conversions/#ftoc-heading-3). Can be a path to a file or a string in PEM format.

RI\_ENCRYPTION\_KEY

Key to encrypt data with.

n/a

Available only for Docker.  
Redis insight stores sensitive information (database passwords, Workbench history, etc.) locally (using [sqlite3](https://github.com/TryGhost/node-sqlite3)). This variable allows you to store sensitive information encrypted using the specified encryption key.  
Note: The same encryption key should be provided for subsequent `docker run` commands with the same volume attached to decrypt the information.

RI\_LOG\_LEVEL

Configures the log level of the application.

`info`

Supported logging levels are prioritized from highest to lowest:

*   error
*   warn
*   info
*   http
*   verbose
*   debug
*   silly

RI\_FILES\_LOGGER

Logs to file.

`true`

By default, you can find log files in the following folders:

*   Docker: `/data/logs`
*   desktop: `<user-home-dir>/.redisinsight-app/logs`

RI\_STDOUT\_LOGGER

Logs to STDOUT.

`true`

RI\_PROXY\_PATH

Configures a subpath for a proxy.

n/a

Available only for Docker.

RI\_DATABASE\_MANAGEMENT

When set to `false`, this disables the ability to manage database connections (adding, editing, or deleting).

`true`

RI\_ACCEPT\_TERMS\_AND\_CONDITIONS

This environment variable allows you to accept the End User License Agreement (EULA) without displaying it in the UI. By setting this variable, you acknowledge that your use of Redis Insight is governed either by your signed agreement with Redis or, if none exists, by the Redis Enterprise Software Subscription Agreement. If neither applies, your use is subject to the Server Side Public License (SSPL).

`true`

## Preconfigure database connections

Redis Insight allows you to preconfigure database connections using environment variables or a JSON file, enabling centralized and efficient configuration. There are two ways to preconfigure database connections in Redis Insight Electron and Docker:

1.  Use environment variables.
2.  Use a JSON file.

### Preconfigure database connections using environment variables

Redis Insight allows you to preconfigure database connections using environment variables.

**NOTES**:

*   To configure multiple database connections, replace the asterisk (\*) in each environment variable with a unique identifier for each database connection. If setting up only one connection, you can omit the asterisk, and Redis Insight will default to using 0 as the ID.
*   If you modify environment variables, the changes will take effect after restarting Redis Insight.
*   If you restart Redis Insight without these environment variables, all previously added database connections will be removed.

Variable

Purpose

Default

Additional info

RI\_REDIS\_HOST\*

Host of a Redis database.

N/A

RI\_REDIS\_PORT\*

Port of a Redis database.

`6379`

RI\_REDIS\_ALIAS\*

Alias of a database connection.

`{host}:{port}`

RI\_REDIS\_USERNAME\*

Username to connect to a Redis database.

`default`

RI\_REDIS\_PASSWORD\*

Password to connect to a Redis database.

No password

RI\_REDIS\_TLS\*

Indicates whether TLS certificates should be used to connect.

`false`

Accepts `true` or `false`

RI\_REDIS\_TLS\_CA\_BASE64\*

CA certificate in base64 format.

N/A

Specify a CA certificate in this environment variable or provide a file path using `RI_REDIS_TLS_CA_PATH*`.

RI\_REDIS\_TLS\_CA\_PATH\*

Path to the CA certificate file.

N/A

RI\_REDIS\_TLS\_CERT\_BASE64\*

Client certificate in base64 format.

N/A

Specify a client certificate in this environment variable or provide a file path using `RI_REDIS_TLS_CERT_PATH*`.

RI\_REDIS\_TLS\_CERT\_PATH\*

Path to the Client certificate file.

N/A

RI\_REDIS\_TLS\_KEY\_BASE64\*

Private key for the client certificate in base64 format.

N/A

Indicate a private key in this environment variable or use another variable to get it from a file.

RI\_REDIS\_TLS\_KEY\_PATH\*

Path to private key file.

N/A

RI\_REDIS\_DB

Database index to connect to.

N/A

### Preconfigure database connections using a JSON file

Redis Insight also allows you to preconfigure database connections using a JSON file.

**NOTES**

*   The JSON file format should match the one used when exporting database connections from Redis Insight.
*   The `id` field in the JSON file should include unique identifiers to avoid conflicts for database connections.
*   Changes to the JSON file will take effect after restarting Redis Insight.
*   If the JSON file is removed, all database connections added via the file will be removed.

Variable

Purpose

Default

Additional info

RI\_PRE\_SETUP\_DATABASES\_PATH

Path to a JSON file containing the database connections to preconfigure

## Use Redis Insight behind a reverse proxy

When you configure Redis Insight to run behind a reverse proxy like [NGINX](https://www.nginx.com/), set the request timeout to over 30 seconds on the reverse proxy because some requests can be long-running.

Redis Insight also allows you to manage its connection timeout on the form to configure the connection details. The default timeout is 30 seconds.

Hosting Redis Insight behind a prefix path (path-rewriting) is not supported.

## On this page

