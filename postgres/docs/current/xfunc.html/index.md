---
title: "PostgreSQL: Documentation: 18: 36.3. User-Defined Functions"
source: "https://www.postgresql.org/docs/current/xfunc.html"
canonical_url: "https://www.postgresql.org/docs/current/xfunc.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:54.750Z"
content_hash: "14094696174546d91a05a15c5fb90e863549df8e59269104bc19f241f2b789e0"
menu_path: ["PostgreSQL: Documentation: 18: 36.3. User-Defined Functions"]
section_path: []
---
PostgreSQL provides four kinds of functions:

*   query language functions (functions written in SQL) ([Section 36.5](https://www.postgresql.org/docs/current/xfunc-sql.html "36.5. Query Language (SQL) Functions"))
    
*   procedural language functions (functions written in, for example, PL/pgSQL or PL/Tcl) ([Section 36.8](https://www.postgresql.org/docs/current/xfunc-pl.html "36.8. Procedural Language Functions"))
    
*   internal functions ([Section 36.9](https://www.postgresql.org/docs/current/xfunc-internal.html "36.9. Internal Functions"))
    
*   C-language functions ([Section 36.10](https://www.postgresql.org/docs/current/xfunc-c.html "36.10. C-Language Functions"))
    

Every kind of function can take base types, composite types, or combinations of these as arguments (parameters). In addition, every kind of function can return a base type or a composite type. Functions can also be defined to return sets of base or composite values.

Many kinds of functions can take or return certain pseudo-types (such as polymorphic types), but the available facilities vary. Consult the description of each kind of function for more details.

It's easiest to define SQL functions, so we'll start by discussing those. Most of the concepts presented for SQL functions will carry over to the other types of functions.

Throughout this chapter, it can be useful to look at the reference page of the [`CREATE FUNCTION`](https://www.postgresql.org/docs/current/sql-createfunction.html "CREATE FUNCTION") command to understand the examples better. Some examples from this chapter can be found in `funcs.sql` and `funcs.c` in the `src/tutorial` directory in the PostgreSQL source distribution.
