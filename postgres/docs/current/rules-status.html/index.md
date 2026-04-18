---
title: "PostgreSQL: Documentation: 18: 39.6. Rules and Command Status"
source: "https://www.postgresql.org/docs/current/rules-status.html"
canonical_url: "https://www.postgresql.org/docs/current/rules-status.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:21.583Z"
content_hash: "48e7d073ca9684f4018356b95efc4b63cf1aa2a031c30cac29a12cf323383d5a"
menu_path: ["PostgreSQL: Documentation: 18: 39.6. Rules and Command Status"]
section_path: []
nav_prev: {"path": "postgres/docs/current/rules-privileges.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.5.\u00a0Rules and Privileges"}
nav_next: {"path": "postgres/docs/current/rules-triggers.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.7.\u00a0Rules Versus Triggers"}
---

The PostgreSQL server returns a command status string, such as `INSERT 149592 1`, for each command it receives. This is simple enough when there are no rules involved, but what happens when the query is rewritten by rules?

Rules affect the command status as follows:

*   If there is no unconditional `INSTEAD` rule for the query, then the originally given query will be executed, and its command status will be returned as usual. (But note that if there were any conditional `INSTEAD` rules, the negation of their qualifications will have been added to the original query. This might reduce the number of rows it processes, and if so the reported status will be affected.)
    
*   If there is any unconditional `INSTEAD` rule for the query, then the original query will not be executed at all. In this case, the server will return the command status for the last query that was inserted by an `INSTEAD` rule (conditional or unconditional) and is of the same command type (`INSERT`, `UPDATE`, or `DELETE`) as the original query. If no query meeting those requirements is added by any rule, then the returned command status shows the original query type and zeroes for the row-count and OID fields.
    

The programmer can ensure that any desired `INSTEAD` rule is the one that sets the command status in the second case, by giving it the alphabetically last rule name among the active rules, so that it gets applied last.
