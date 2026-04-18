---
title: "PostgreSQL: Documentation: 18: 11.10. Operator Classes and Operator Families"
source: "https://www.postgresql.org/docs/current/indexes-opclass.html"
canonical_url: "https://www.postgresql.org/docs/current/indexes-opclass.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:06.228Z"
content_hash: "5e7752cde8ff8fb711b15e2cadf8d56876152f1657e6065441b056d15b59e2f6"
menu_path: ["PostgreSQL: Documentation: 18: 11.10. Operator Classes and Operator Families"]
section_path: []
nav_prev: {"path": "postgres/docs/current/logical-replication-architecture.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.9.\u00a0Architecture"}
nav_next: {"path": "postgres/docs/current/indexes-examine.html/index.md", "title": "PostgreSQL: Documentation: 18: 11.12.\u00a0Examining Index Usage"}
---

An index definition can specify an _operator class_ for each column of an index.

CREATE INDEX _`name`_ ON _`table`_ (_`column`_ _`opclass`_ \[ ( _`opclass_options`_ ) \] \[_`sort options`_\] \[, ...\]);

The operator class identifies the operators to be used by the index for that column. For example, a B-tree index on the type `int4` would use the `int4_ops` class; this operator class includes comparison functions for values of type `int4`. In practice the default operator class for the column's data type is usually sufficient. The main reason for having operator classes is that for some data types, there could be more than one meaningful index behavior. For example, we might want to sort a complex-number data type either by absolute value or by real part. We could do this by defining two operator classes for the data type and then selecting the proper class when making an index. The operator class determines the basic sort ordering (which can then be modified by adding sort options `COLLATE`, `ASC`/`DESC` and/or `NULLS FIRST`/`NULLS LAST`).

There are also some built-in operator classes besides the default ones:

*   The operator classes `text_pattern_ops`, `varchar_pattern_ops`, and `bpchar_pattern_ops` support B-tree indexes on the types `text`, `varchar`, and `char` respectively. The difference from the default operator classes is that the values are compared strictly character by character rather than according to the locale-specific collation rules. This makes these operator classes suitable for use by queries involving pattern matching expressions (`LIKE` or POSIX regular expressions) when the database does not use the standard “C” locale. As an example, you might index a `varchar` column like this:
    
    CREATE INDEX test\_index ON test\_table (col varchar\_pattern\_ops);
    
    Note that you should also create an index with the default operator class if you want queries involving ordinary `<`, `<=`, `>`, or `>=` comparisons to use an index. Such queries cannot use the ``_`xxx`__pattern_ops`` operator classes. (Ordinary equality comparisons can use these operator classes, however.) It is possible to create multiple indexes on the same column with different operator classes. If you do use the C locale, you do not need the ``_`xxx`__pattern_ops`` operator classes, because an index with the default operator class is usable for pattern-matching queries in the C locale.
    

The following query shows all defined operator classes:

SELECT am.amname AS index\_method,
       opc.opcname AS opclass\_name,
       opc.opcintype::regtype AS indexed\_type,
       opc.opcdefault AS is\_default
    FROM pg\_am am, pg\_opclass opc
    WHERE opc.opcmethod = am.oid
    ORDER BY index\_method, opclass\_name;

An operator class is actually just a subset of a larger structure called an _operator family_. In cases where several data types have similar behaviors, it is frequently useful to define cross-data-type operators and allow these to work with indexes. To do this, the operator classes for each of the types must be grouped into the same operator family. The cross-type operators are members of the family, but are not associated with any single class within the family.

This expanded version of the previous query shows the operator family each operator class belongs to:

SELECT am.amname AS index\_method,
       opc.opcname AS opclass\_name,
       opf.opfname AS opfamily\_name,
       opc.opcintype::regtype AS indexed\_type,
       opc.opcdefault AS is\_default
    FROM pg\_am am, pg\_opclass opc, pg\_opfamily opf
    WHERE opc.opcmethod = am.oid AND
          opc.opcfamily = opf.oid
    ORDER BY index\_method, opclass\_name;

This query shows all defined operator families and all the operators included in each family:

SELECT am.amname AS index\_method,
       opf.opfname AS opfamily\_name,
       amop.amopopr::regoperator AS opfamily\_operator
    FROM pg\_am am, pg\_opfamily opf, pg\_amop amop
    WHERE opf.opfmethod = am.oid AND
          amop.amopfamily = opf.oid
    ORDER BY index\_method, opfamily\_name, opfamily\_operator;

### Tip

[psql](https://www.postgresql.org/docs/current/app-psql.html "psql") has commands `\dAc`, `\dAf`, and `\dAo`, which provide slightly more sophisticated versions of these queries.
