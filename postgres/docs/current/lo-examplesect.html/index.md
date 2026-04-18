---
title: "PostgreSQL: Documentation: 18: 33.5. Example Program"
source: "https://www.postgresql.org/docs/current/lo-examplesect.html"
canonical_url: "https://www.postgresql.org/docs/current/lo-examplesect.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:54.194Z"
content_hash: "c23e147a18104f870baba6f559332fbb9f0ba518dc3e7e04f39215b628922488"
menu_path: ["PostgreSQL: Documentation: 18: 33.5. Example Program"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pgcrypto.html/index.md", "title": "PostgreSQL: Documentation: 18: F.26.\u00a0pgcrypto \u2014 cryptographic functions"}
nav_next: {"path": "postgres/docs/current/infoschema-role-routine-grants.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.36.\u00a0role_routine_grants"}
---

/\*-----------------------------------------------------------------
 \*
 \* testlo.c
 \*    test using large objects with libpq
 \*
 \* Portions Copyright (c) 1996-2025, PostgreSQL Global Development Group
 \* Portions Copyright (c) 1994, Regents of the University of California
 \*
 \*
 \* IDENTIFICATION
 \*    src/test/examples/testlo.c
 \*
 \*-----------------------------------------------------------------
 \*/
#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#include "libpq-fe.h"
#include "libpq/libpq-fs.h"

#define BUFSIZE         1024

/\*
 \* importFile -
 \*    import file "in\_filename" into database as large object "lobjOid"
 \*
 \*/
static Oid
importFile(PGconn \*conn, char \*filename)
{
    Oid         lobjId;
    int         lobj\_fd;
    char        buf\[BUFSIZE\];
    int         nbytes,
                tmp;
    int         fd;

    /\*
     \* open the file to be read in
     \*/
    fd = open(filename, O\_RDONLY, 0666);
    if (fd < 0)
    {                           /\* error \*/
        fprintf(stderr, "cannot open unix file\\"%s\\"\\n", filename);
    }

    /\*
     \* create the large object
     \*/
    lobjId = lo\_creat(conn, INV\_READ | INV\_WRITE);
    if (lobjId == 0)
        fprintf(stderr, "cannot create large object");

    lobj\_fd = lo\_open(conn, lobjId, INV\_WRITE);

    /\*
     \* read in from the Unix file and write to the inversion file
     \*/
    while ((nbytes = read(fd, buf, BUFSIZE)) > 0)
    {
        tmp = lo\_write(conn, lobj\_fd, buf, nbytes);
        if (tmp < nbytes)
            fprintf(stderr, "error while reading \\"%s\\"", filename);
    }

    close(fd);
    lo\_close(conn, lobj\_fd);

    return lobjId;
}

static void
pickout(PGconn \*conn, Oid lobjId, int start, int len)
{
    int         lobj\_fd;
    char       \*buf;
    int         nbytes;
    int         nread;

    lobj\_fd = lo\_open(conn, lobjId, INV\_READ);
    if (lobj\_fd < 0)
        fprintf(stderr, "cannot open large object %u", lobjId);

    lo\_lseek(conn, lobj\_fd, start, SEEK\_SET);
    buf = malloc(len + 1);

    nread = 0;
    while (len - nread > 0)
    {
        nbytes = lo\_read(conn, lobj\_fd, buf, len - nread);
        buf\[nbytes\] = '\\0';
        fprintf(stderr, ">>> %s", buf);
        nread += nbytes;
        if (nbytes <= 0)
            break;              /\* no more data? \*/
    }
    free(buf);
    fprintf(stderr, "\\n");
    lo\_close(conn, lobj\_fd);
}

static void
overwrite(PGconn \*conn, Oid lobjId, int start, int len)
{
    int         lobj\_fd;
    char       \*buf;
    int         nbytes;
    int         nwritten;
    int         i;

    lobj\_fd = lo\_open(conn, lobjId, INV\_WRITE);
    if (lobj\_fd < 0)
        fprintf(stderr, "cannot open large object %u", lobjId);

    lo\_lseek(conn, lobj\_fd, start, SEEK\_SET);
    buf = malloc(len + 1);

    for (i = 0; i < len; i++)
        buf\[i\] = 'X';
    buf\[i\] = '\\0';

    nwritten = 0;
    while (len - nwritten > 0)
    {
        nbytes = lo\_write(conn, lobj\_fd, buf + nwritten, len - nwritten);
        nwritten += nbytes;
        if (nbytes <= 0)
        {
            fprintf(stderr, "\\nWRITE FAILED!\\n");
            break;
        }
    }
    free(buf);
    fprintf(stderr, "\\n");
    lo\_close(conn, lobj\_fd);
}

/\*
 \* exportFile -
 \*    export large object "lobjOid" to file "out\_filename"
 \*
 \*/
static void
exportFile(PGconn \*conn, Oid lobjId, char \*filename)
{
    int         lobj\_fd;
    char        buf\[BUFSIZE\];
    int         nbytes,
                tmp;
    int         fd;

    /\*
     \* open the large object
     \*/
    lobj\_fd = lo\_open(conn, lobjId, INV\_READ);
    if (lobj\_fd < 0)
        fprintf(stderr, "cannot open large object %u", lobjId);

    /\*
     \* open the file to be written to
     \*/
    fd = open(filename, O\_CREAT | O\_WRONLY | O\_TRUNC, 0666);
    if (fd < 0)
    {                           /\* error \*/
        fprintf(stderr, "cannot open unix file\\"%s\\"",
                filename);
    }

    /\*
     \* read in from the inversion file and write to the Unix file
     \*/
    while ((nbytes = lo\_read(conn, lobj\_fd, buf, BUFSIZE)) > 0)
    {
        tmp = write(fd, buf, nbytes);
        if (tmp < nbytes)
        {
            fprintf(stderr, "error while writing \\"%s\\"",
                    filename);
        }
    }

    lo\_close(conn, lobj\_fd);
    close(fd);
}

static void
exit\_nicely(PGconn \*conn)
{
    PQfinish(conn);
    exit(1);
}

int
main(int argc, char \*\*argv)
{
    char       \*in\_filename,
               \*out\_filename;
    char       \*database;
    Oid         lobjOid;
    PGconn     \*conn;
    PGresult   \*res;

    if (argc != 4)
    {
        fprintf(stderr, "Usage: %s database\_name in\_filename out\_filename\\n",
                argv\[0\]);
        exit(1);
    }

    database = argv\[1\];
    in\_filename = argv\[2\];
    out\_filename = argv\[3\];

    /\*
     \* set up the connection
     \*/
    conn = PQsetdb(NULL, NULL, NULL, NULL, database);

    /\* check to see that the backend connection was successfully made \*/
    if (PQstatus(conn) != CONNECTION\_OK)
    {
        fprintf(stderr, "%s", PQerrorMessage(conn));
        exit\_nicely(conn);
    }

    /\* Set always-secure search path, so malicious users can't take control. \*/
    res = PQexec(conn,
                 "SELECT pg\_catalog.set\_config('search\_path', '', false)");
    if (PQresultStatus(res) != PGRES\_TUPLES\_OK)
    {
        fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));
        PQclear(res);
        exit\_nicely(conn);
    }
    PQclear(res);

    res = PQexec(conn, "begin");
    PQclear(res);
    printf("importing file \\"%s\\" ...\\n", in\_filename);
/\*  lobjOid = importFile(conn, in\_filename); \*/
    lobjOid = lo\_import(conn, in\_filename);
    if (lobjOid == 0)
        fprintf(stderr, "%s\\n", PQerrorMessage(conn));
    else
    {
        printf("\\tas large object %u.\\n", lobjOid);

        printf("picking out bytes 1000-2000 of the large object\\n");
        pickout(conn, lobjOid, 1000, 1000);

        printf("overwriting bytes 1000-2000 of the large object with X's\\n");
        overwrite(conn, lobjOid, 1000, 1000);

        printf("exporting large object to file \\"%s\\" ...\\n", out\_filename);
/\*      exportFile(conn, lobjOid, out\_filename); \*/
        if (lo\_export(conn, lobjOid, out\_filename) < 0)
            fprintf(stderr, "%s\\n", PQerrorMessage(conn));
    }

    res = PQexec(conn, "end");
    PQclear(res);
    PQfinish(conn);
    return 0;
}


