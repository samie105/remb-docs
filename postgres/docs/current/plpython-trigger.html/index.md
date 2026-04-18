---
title: "PostgreSQL: Documentation: 18: 44.5. Trigger Functions"
source: "https://www.postgresql.org/docs/current/plpython-trigger.html"
canonical_url: "https://www.postgresql.org/docs/current/plpython-trigger.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:50.719Z"
content_hash: "ec2bd94de23f7ea30949fd06970c3d39c191870450855f2b10c575352bfbde1c"
menu_path: ["PostgreSQL: Documentation: 18: 44.5. Trigger Functions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ecpg-sql-whenever.html/index.md", "title": "PostgreSQL: Documentation: 18: WHENEVER"}
nav_next: {"path": "postgres/docs/current/xfunc.html/index.md", "title": "PostgreSQL: Documentation: 18: 36.3.\u00a0User-Defined Functions"}
---

When a function is used as a trigger, the dictionary `TD` contains trigger-related values:

`TD["event"]`

contains the event as a string: `INSERT`, `UPDATE`, `DELETE`, or `TRUNCATE`.

`TD["when"]`

contains one of `BEFORE`, `AFTER`, or `INSTEAD OF`.

`TD["level"]`

contains `ROW` or `STATEMENT`.

`TD["new"]`  
`TD["old"]`

For a row-level trigger, one or both of these fields contain the respective trigger rows, depending on the trigger event.

`TD["name"]`

contains the trigger name.

`TD["table_name"]`

contains the name of the table on which the trigger occurred.

`TD["table_schema"]`

contains the schema of the table on which the trigger occurred.

`TD["relid"]`

contains the OID of the table on which the trigger occurred.

`TD["args"]`

If the `CREATE TRIGGER` command included arguments, they are available in `TD["args"][0]` to ``TD["args"][_`n`_-1]``.

If `TD["when"]` is `BEFORE` or `INSTEAD OF` and `TD["level"]` is `ROW`, you can return `None` or `"OK"` from the Python function to indicate the row is unmodified, `"SKIP"` to abort the event, or if `TD["event"]` is `INSERT` or `UPDATE` you can return `"MODIFY"` to indicate you've modified the new row. Otherwise the return value is ignored.


