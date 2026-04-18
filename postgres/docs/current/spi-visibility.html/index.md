---
title: "PostgreSQL: Documentation: 18: 45.5. Visibility of Data Changes"
source: "https://www.postgresql.org/docs/current/spi-visibility.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-visibility.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:11.037Z"
content_hash: "4df6917d8bf10abc102a8301c26e1a03e85082c2439806364d8eefc301f9ad2d"
menu_path: ["PostgreSQL: Documentation: 18: 45.5. Visibility of Data Changes"]
section_path: []
---
February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-visibility.html "PostgreSQL 18 - 45.5. Visibility of Data Changes") ([18](/docs/18/spi-visibility.html "PostgreSQL 18 - 45.5. Visibility of Data Changes")) / [17](/docs/17/spi-visibility.html "PostgreSQL 17 - 45.5. Visibility of Data Changes") / [16](/docs/16/spi-visibility.html "PostgreSQL 16 - 45.5. Visibility of Data Changes") / [15](/docs/15/spi-visibility.html "PostgreSQL 15 - 45.5. Visibility of Data Changes") / [14](/docs/14/spi-visibility.html "PostgreSQL 14 - 45.5. Visibility of Data Changes")

Development Versions: [devel](/docs/devel/spi-visibility.html "PostgreSQL devel - 45.5. Visibility of Data Changes")

Unsupported versions: [13](/docs/13/spi-visibility.html "PostgreSQL 13 - 45.5. Visibility of Data Changes") / [12](/docs/12/spi-visibility.html "PostgreSQL 12 - 45.5. Visibility of Data Changes") / [11](/docs/11/spi-visibility.html "PostgreSQL 11 - 45.5. Visibility of Data Changes") / [10](/docs/10/spi-visibility.html "PostgreSQL 10 - 45.5. Visibility of Data Changes") / [9.6](/docs/9.6/spi-visibility.html "PostgreSQL 9.6 - 45.5. Visibility of Data Changes") / [9.5](/docs/9.5/spi-visibility.html "PostgreSQL 9.5 - 45.5. Visibility of Data Changes") / [9.4](/docs/9.4/spi-visibility.html "PostgreSQL 9.4 - 45.5. Visibility of Data Changes") / [9.3](/docs/9.3/spi-visibility.html "PostgreSQL 9.3 - 45.5. Visibility of Data Changes") / [9.2](/docs/9.2/spi-visibility.html "PostgreSQL 9.2 - 45.5. Visibility of Data Changes") / [9.1](/docs/9.1/spi-visibility.html "PostgreSQL 9.1 - 45.5. Visibility of Data Changes") / [9.0](/docs/9.0/spi-visibility.html "PostgreSQL 9.0 - 45.5. Visibility of Data Changes") / [8.4](/docs/8.4/spi-visibility.html "PostgreSQL 8.4 - 45.5. Visibility of Data Changes") / [8.3](/docs/8.3/spi-visibility.html "PostgreSQL 8.3 - 45.5. Visibility of Data Changes") / [8.2](/docs/8.2/spi-visibility.html "PostgreSQL 8.2 - 45.5. Visibility of Data Changes") / [8.1](/docs/8.1/spi-visibility.html "PostgreSQL 8.1 - 45.5. Visibility of Data Changes") / [8.0](/docs/8.0/spi-visibility.html "PostgreSQL 8.0 - 45.5. Visibility of Data Changes") / [7.4](/docs/7.4/spi-visibility.html "PostgreSQL 7.4 - 45.5. Visibility of Data Changes") / [7.3](/docs/7.3/spi-visibility.html "PostgreSQL 7.3 - 45.5. Visibility of Data Changes") / [7.2](/docs/7.2/spi-visibility.html "PostgreSQL 7.2 - 45.5. Visibility of Data Changes") / [7.1](/docs/7.1/spi-visibility.html "PostgreSQL 7.1 - 45.5. Visibility of Data Changes")

## 45.5. Visibility of Data Changes [#](#SPI-VISIBILITY)

The following rules govern the visibility of data changes in functions that use SPI (or any other C function):

*   During the execution of an SQL command, any data changes made by the command are invisible to the command itself. For example, in:
    
    INSERT INTO a SELECT \* FROM a;
    
    the inserted rows are invisible to the `SELECT` part.
    
*   Changes made by a command C are visible to all commands that are started after C, no matter whether they are started inside C (during the execution of C) or after C is done.
    
*   Commands executed via SPI inside a function called by an SQL command (either an ordinary function or a trigger) follow one or the other of the above rules depending on the read/write flag passed to SPI. Commands executed in read-only mode follow the first rule: they cannot see changes of the calling command. Commands executed in read-write mode follow the second rule: they can see all changes made so far.
    
*   All standard procedural languages set the SPI read-write mode depending on the volatility attribute of the function. Commands of `STABLE` and `IMMUTABLE` functions are done in read-only mode, while commands of `VOLATILE` functions are done in read-write mode. While authors of C functions are able to violate this convention, it's unlikely to be a good idea to do so.
    

The next section contains an example that illustrates the application of these rules.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-visibility.html/) to report a documentation issue.
