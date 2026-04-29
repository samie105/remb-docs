---
title: "PostgreSQL: Documentation: 18: CONNECT"
source: "https://www.postgresql.org/docs/current/ecpg-sql-connect.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-connect.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:28.345Z"
content_hash: "d0df23783e944960d92c6740d1f11a896897942e2f41ca7fc6cd270b625d4a63"
menu_path: ["PostgreSQL: Documentation: 18: CONNECT"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ecpg-sql-commands.html/index.md", "title": "PostgreSQL: Documentation: 18: 34.14.\u00a0Embedded SQL Commands"}
nav_next: {"path": "postgres/docs/current/ecpg-sql-deallocate-descriptor.html/index.md", "title": "PostgreSQL: Documentation: 18: DEALLOCATE DESCRIPTOR"}
---

CONNECT — establish a database connection

## Synopsis

CONNECT TO _`connection_target`_ \[ AS _`connection_name`_ \] \[ USER _`connection_user`_ \]
CONNECT TO DEFAULT
CONNECT _`connection_user`_
DATABASE _`connection_target`_

## Description

The `CONNECT` command establishes a connection between the client and the PostgreSQL server.

## Parameters

_`connection_target`_ [#](#ECPG-SQL-CONNECT-CONNECTION-TARGET)

_`connection_target`_ specifies the target server of the connection on one of several forms.

\[ _`database_name`_ \] \[ `@`_`host`_ \] \[ `:`_`port`_ \] [#](#ECPG-SQL-CONNECT-CONNECTION-TARGET-DATABASE-NAME)

Connect over TCP/IP

`unix:postgresql://`_`host`_ \[ `:`_`port`_ \] `/` \[ _`database_name`_ \] \[ `?`_`connection_option`_ \] [#](#ECPG-SQL-CONNECT-CONNECTION-TARGET-UNIX-DOMAIN-SOCKETS)

Connect over Unix-domain sockets

`tcp:postgresql://`_`host`_ \[ `:`_`port`_ \] `/` \[ _`database_name`_ \] \[ `?`_`connection_option`_ \] [#](#ECPG-SQL-CONNECT-CONNECTION-TARGET-TCP-IP)

Connect over TCP/IP

SQL string constant [#](#ECPG-SQL-CONNECT-CONNECTION-TARGET-CONSTANT)

containing a value in one of the above forms

host variable [#](#ECPG-SQL-CONNECT-CONNECTION-TARGET-HOST-VARIABLE)

host variable of type `char[]` or `VARCHAR[]` containing a value in one of the above forms

_`connection_name`_ [#](#ECPG-SQL-CONNECT-CONNECTION-NAME)

An optional identifier for the connection, so that it can be referred to in other commands. This can be an SQL identifier or a host variable.

_`connection_user`_ [#](#ECPG-SQL-CONNECT-CONNECTION-USER)

The user name for the database connection.

This parameter can also specify user name and password, using one the forms ``_`user_name`_/_`password`_``, ``_`user_name`_ IDENTIFIED BY _`password`_``, or ``_`user_name`_ USING _`password`_``.

User name and password can be SQL identifiers, string constants, or host variables.

`DEFAULT` [#](#ECPG-SQL-CONNECT-DEFAULT)

Use all default connection parameters, as defined by libpq.

## Examples

Here a several variants for specifying connection parameters:

EXEC SQL CONNECT TO "connectdb" AS main;
EXEC SQL CONNECT TO "connectdb" AS second;
EXEC SQL CONNECT TO "unix:postgresql://200.46.204.71/connectdb" AS main USER connectuser;
EXEC SQL CONNECT TO "unix:postgresql://localhost/connectdb" AS main USER connectuser;
EXEC SQL CONNECT TO 'connectdb' AS main;
EXEC SQL CONNECT TO 'unix:postgresql://localhost/connectdb' AS main USER :user;
EXEC SQL CONNECT TO :db AS :id;
EXEC SQL CONNECT TO :db USER connectuser USING :pw;
EXEC SQL CONNECT TO @localhost AS main USER connectdb;
EXEC SQL CONNECT TO REGRESSDB1 as main;
EXEC SQL CONNECT TO AS main USER connectdb;
EXEC SQL CONNECT TO connectdb AS :id;
EXEC SQL CONNECT TO connectdb AS main USER connectuser/connectdb;
EXEC SQL CONNECT TO connectdb AS main;
EXEC SQL CONNECT TO connectdb@localhost AS main;
EXEC SQL CONNECT TO tcp:postgresql://localhost/ USER connectdb;
EXEC SQL CONNECT TO tcp:postgresql://localhost/connectdb USER connectuser IDENTIFIED BY connectpw;
EXEC SQL CONNECT TO tcp:postgresql://localhost:20/connectdb USER connectuser IDENTIFIED BY connectpw;
EXEC SQL CONNECT TO unix:postgresql://localhost/ AS main USER connectdb;
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb AS main USER connectuser;
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb USER connectuser IDENTIFIED BY "connectpw";
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb USER connectuser USING "connectpw";
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb?connect\_timeout=14 USER connectuser;

Here is an example program that illustrates the use of host variables to specify connection parameters:

int
main(void)
{
EXEC SQL BEGIN DECLARE SECTION;
    char \*dbname     = "testdb";    /\* database name \*/
    char \*user       = "testuser";  /\* connection user name \*/
    char \*connection = "tcp:postgresql://localhost:5432/testdb";
                                    /\* connection string \*/
    char ver\[256\];                  /\* buffer to store the version string \*/
EXEC SQL END DECLARE SECTION;

    ECPGdebug(1, stderr);

    EXEC SQL CONNECT TO :dbname USER :user;
    EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL COMMIT;
    EXEC SQL SELECT version() INTO :ver;
    EXEC SQL DISCONNECT;

    printf("version: %s\\n", ver);

    EXEC SQL CONNECT TO :connection USER :user;
    EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL COMMIT;
    EXEC SQL SELECT version() INTO :ver;
    EXEC SQL DISCONNECT;

    printf("version: %s\\n", ver);

    return 0;
}

## Compatibility

`CONNECT` is specified in the SQL standard, but the format of the connection parameters is implementation-specific.
