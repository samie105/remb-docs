---
title: "PostgreSQL: Documentation: 18: F.31. pgrowlocks — show a table's row locking information"
source: "https://www.postgresql.org/docs/current/pgrowlocks.html"
canonical_url: "https://www.postgresql.org/docs/current/pgrowlocks.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:46:26.203Z"
content_hash: "04e037d02d6b7d2f8c9cbb8b7e4b4eaffe3ddcd70cd05258c55adb1482b8e4e7"
menu_path: ["PostgreSQL: Documentation: 18: F.31. pgrowlocks — show a table's row locking information"]
section_path: []
content_language: "en"
---
The `pgrowlocks` module provides a function to show row locking information for a specified table.

By default use is restricted to superusers, roles with privileges of the `pg_stat_scan_tables` role, and users with `SELECT` permissions on the table.

### F.31.1. Overview [#](#PGROWLOCKS-OVERVIEW)

pgrowlocks(text) returns setof record

The parameter is the name of a table. The result is a set of records, with one row for each locked row within the table. The output columns are shown in [Table F.21](https://www.postgresql.org/docs/current/pgrowlocks.html#PGROWLOCKS-COLUMNS "Table F.21. pgrowlocks Output Columns").

**Table F.21. `pgrowlocks` Output Columns**

  
| Name | Type | Description |
| --- | --- | --- |
| `locked_row` | `tid` | Tuple ID (TID) of locked row |
| `locker` | `xid` | Transaction ID of locker, or multixact ID if multitransaction; see [Section 67.1](https://www.postgresql.org/docs/current/transaction-id.html "67.1. Transactions and Identifiers") |
| `multi` | `boolean` | True if locker is a multitransaction |
| `xids` | `xid[]` | Transaction IDs of lockers (more than one if multitransaction) |
| `modes` | `text[]` | Lock mode of lockers (more than one if multitransaction), an array of `For Key Share`, `For Share`, `For No Key Update`, `No Key Update`, `For Update`, `Update`. |
| `pids` | `integer[]` | Process IDs of locking backends (more than one if multitransaction) |

`pgrowlocks` takes `AccessShareLock` for the target table and reads each row one by one to collect the row locking information. This is not very speedy for a large table. Note that:

1.  If an `ACCESS EXCLUSIVE` lock is taken on the table, `pgrowlocks` will be blocked.
    
2.  `pgrowlocks` is not guaranteed to produce a self-consistent snapshot. It is possible that a new row lock is taken, or an old lock is freed, during its execution.
    

`pgrowlocks` does not show the contents of locked rows. If you want to take a look at the row contents at the same time, you could do something like this:

SELECT \* FROM accounts AS a, pgrowlocks('accounts') AS p
  WHERE p.locked\_row = a.ctid;

Be aware however that such a query will be very inefficient.

### F.31.2. Sample Output [#](#PGROWLOCKS-SAMPLE-OUTPUT)

\=# SELECT \* FROM pgrowlocks('t1');
 locked\_row | locker | multi | xids  |     modes      |  pids
------------+--------+-------+-------+----------------+--------
 (0,1)      |    609 | f     | {609} | {"For Share"}  | {3161}
 (0,2)      |    609 | f     | {609} | {"For Share"}  | {3161}
 (0,3)      |    607 | f     | {607} | {"For Update"} | {3107}
 (0,4)      |    607 | f     | {607} | {"For Update"} | {3107}
(4 rows)
