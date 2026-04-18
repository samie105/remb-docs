---
title: "PostgreSQL: Documentation: 18: TYPE"
source: "https://www.postgresql.org/docs/current/ecpg-sql-type.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-type.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:59.980Z"
content_hash: "aceefea9bfff273e10b2fc2870babf3d99d60d3da77e7fd8cb59dffd49beba6c"
menu_path: ["PostgreSQL: Documentation: 18: TYPE"]
section_path: []
---
TYPE — define a new data type

## Synopsis

TYPE _`type_name`_ IS _`ctype`_

## Description

The `TYPE` command defines a new C type. It is equivalent to putting a `typedef` into a declare section.

This command is only recognized when `ecpg` is run with the `-c` option.

## Parameters

_`type_name`_ [#](#ECPG-SQL-TYPE-TYPE-NAME)

The name for the new type. It must be a valid C type name.

_`ctype`_ [#](#ECPG-SQL-TYPE-CTYPE)

A C type specification.

## Examples

EXEC SQL TYPE customer IS
    struct
    {
        varchar name\[50\];
        int     phone;
    };

EXEC SQL TYPE cust\_ind IS
    struct ind
    {
        short   name\_ind;
        short   phone\_ind;
    };

EXEC SQL TYPE c IS char reference;
EXEC SQL TYPE ind IS union { int integer; short smallint; };
EXEC SQL TYPE intarray IS int\[AMOUNT\];
EXEC SQL TYPE str IS varchar\[BUFFERSIZ\];
EXEC SQL TYPE string IS char\[11\];

Here is an example program that uses `EXEC SQL TYPE`:

EXEC SQL WHENEVER SQLERROR SQLPRINT;

EXEC SQL TYPE tt IS
    struct
    {
        varchar v\[256\];
        int     i;
    };

EXEC SQL TYPE tt\_ind IS
    struct ind {
        short   v\_ind;
        short   i\_ind;
    };

int
main(void)
{
EXEC SQL BEGIN DECLARE SECTION;
    tt t;
    tt\_ind t\_ind;
EXEC SQL END DECLARE SECTION;

    EXEC SQL CONNECT TO testdb AS con1;
    EXEC SQL SELECT pg\_catalog.set\_config('search\_path', '', false); EXEC SQL COMMIT;

    EXEC SQL SELECT current\_database(), 256 INTO :t:t\_ind LIMIT 1;

    printf("t.v = %s\\n", t.v.arr);
    printf("t.i = %d\\n", t.i);

    printf("t\_ind.v\_ind = %d\\n", t\_ind.v\_ind);
    printf("t\_ind.i\_ind = %d\\n", t\_ind.i\_ind);

    EXEC SQL DISCONNECT con1;

    return 0;
}

The output from this program looks like this:

t.v = testdb
t.i = 256
t\_ind.v\_ind = 0
t\_ind.i\_ind = 0

## Compatibility

The `TYPE` command is a PostgreSQL extension.
