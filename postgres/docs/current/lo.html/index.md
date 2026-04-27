---
title: "PostgreSQL: Documentation: 18: F.21. lo — manage large objects"
source: "https://www.postgresql.org/docs/current/lo.html"
canonical_url: "https://www.postgresql.org/docs/current/lo.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:58.631Z"
content_hash: "02380ef820fb793b656f74ad7b4b8fc39c685dbc36587d5edcb36892aa187fdc"
menu_path: ["PostgreSQL: Documentation: 18: F.21. lo — manage large objects"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/lo.html "PostgreSQL devel - F.21. lo — manage large objects")

The `lo` module provides support for managing Large Objects (also called LOs or BLOBs). This includes a data type `lo` and a trigger `lo_manage`.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

### F.21.1. Rationale [#](#LO-RATIONALE)

One of the problems with the JDBC driver (and this affects the ODBC driver also), is that the specification assumes that references to BLOBs (Binary Large OBjects) are stored within a table, and if that entry is changed, the associated BLOB is deleted from the database.

As PostgreSQL stands, this doesn't occur. Large objects are treated as objects in their own right; a table entry can reference a large object by OID, but there can be multiple table entries referencing the same large object OID, so the system doesn't delete the large object just because you change or remove one such entry.

Now this is fine for PostgreSQL\-specific applications, but standard code using JDBC or ODBC won't delete the objects, resulting in orphan objects — objects that are not referenced by anything, and simply occupy disk space.

The `lo` module allows fixing this by attaching a trigger to tables that contain LO reference columns. The trigger essentially just does a `lo_unlink` whenever you delete or modify a value referencing a large object. When you use this trigger, you are assuming that there is only one database reference to any large object that is referenced in a trigger-controlled column!

The module also provides a data type `lo`, which is really just a [](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DOMAIN)[domain](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-DOMAIN "Domain") over the `oid` type. This is useful for differentiating database columns that hold large object references from those that are OIDs of other things. You don't have to use the `lo` type to use the trigger, but it may be convenient to use it to keep track of which columns in your database represent large objects that you are managing with the trigger. It is also rumored that the ODBC driver gets confused if you don't use `lo` for BLOB columns.

### F.21.2. How to Use It [#](#LO-HOW-TO-USE)

Here's a simple example of usage:

CREATE TABLE image (title text, raster lo);

CREATE TRIGGER t\_raster BEFORE UPDATE OR DELETE ON image
    FOR EACH ROW EXECUTE FUNCTION lo\_manage(raster);

For each column that will contain unique references to large objects, create a `BEFORE UPDATE OR DELETE` trigger, and give the column name as the sole trigger argument. You can also restrict the trigger to only execute on updates to the column by using `BEFORE UPDATE OF` _`column_name`_. If you need multiple `lo` columns in the same table, create a separate trigger for each one, remembering to give a different name to each trigger on the same table.

### F.21.3. Limitations [#](#LO-LIMITATIONS)

-   Dropping a table will still orphan any objects it contains, as the trigger is not executed. You can avoid this by preceding the `DROP TABLE` with ``DELETE FROM _`table`_``.
    
    `TRUNCATE` has the same hazard.
    
    If you already have, or suspect you have, orphaned large objects, see the [vacuumlo](https://www.postgresql.org/docs/current/vacuumlo.html "vacuumlo") module to help you clean them up. It's a good idea to run vacuumlo occasionally as a back-stop to the `lo_manage` trigger.
    
-   Some frontends may create their own tables, and will not create the associated trigger(s). Also, users may not remember (or know) to create the triggers.
