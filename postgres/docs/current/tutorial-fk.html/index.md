---
title: "PostgreSQL: Documentation: 18: 3.3. Foreign Keys"
source: "https://www.postgresql.org/docs/current/tutorial-fk.html"
canonical_url: "https://www.postgresql.org/docs/current/tutorial-fk.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:08.638Z"
content_hash: "2fc64d5b5348bf5470ee3ab9274ff9951f837dadf1aa7f00608f0386a4317c20"
menu_path: ["PostgreSQL: Documentation: 18: 3.3. Foreign Keys"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-listen.html/index.md", "title": "PostgreSQL: Documentation: 18: LISTEN"}
nav_next: {"path": "postgres/docs/current/release-prior.html/index.md", "title": "PostgreSQL: Documentation: 18: E.5.\u00a0Prior Releases"}
---

Recall the `weather` and `cities` tables from [Chapter 2](https://www.postgresql.org/docs/current/tutorial-sql.html "Chapter 2. The SQL Language"). Consider the following problem: You want to make sure that no one can insert rows in the `weather` table that do not have a matching entry in the `cities` table. This is called maintaining the _referential integrity_ of your data. In simplistic database systems this would be implemented (if at all) by first looking at the `cities` table to check if a matching record exists, and then inserting or rejecting the new `weather` records. This approach has a number of problems and is very inconvenient, so PostgreSQL can do this for you.

The new declaration of the tables would look like this:

CREATE TABLE cities (
        name     varchar(80) primary key,
        location point
);

CREATE TABLE weather (
        city      varchar(80) references cities(name),
        temp\_lo   int,
        temp\_hi   int,
        prcp      real,
        date      date
);

Now try inserting an invalid record:

INSERT INTO weather VALUES ('Berkeley', 45, 53, 0.0, '1994-11-28');

ERROR:  insert or update on table "weather" violates foreign key constraint "weather\_city\_fkey"
DETAIL:  Key (city)=(Berkeley) is not present in table "cities".

The behavior of foreign keys can be finely tuned to your application. We will not go beyond this simple example in this tutorial, but just refer you to [Chapter 5](https://www.postgresql.org/docs/current/ddl.html "Chapter 5. Data Definition") for more information. Making correct use of foreign keys will definitely improve the quality of your database applications, so you are strongly encouraged to learn about them.
