---
title: "PostgreSQL: Documentation: 18: 38.4. A Table Rewrite Event Trigger Example"
source: "https://www.postgresql.org/docs/current/event-trigger-table-rewrite-example.html"
canonical_url: "https://www.postgresql.org/docs/current/event-trigger-table-rewrite-example.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:29.380Z"
content_hash: "f07b6d6af1138e030e59f3fbd7d3302c627a0688c17a230adab593163ffe5f43"
menu_path: ["PostgreSQL: Documentation: 18: 38.4. A Table Rewrite Event Trigger Example"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-alterdefaultprivileges.html/index.md", "title": "PostgreSQL: Documentation: 18: ALTER DEFAULT PRIVILEGES"}
nav_next: {"path": "postgres/docs/current/app-pg-ctl.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_ctl"}
---

Thanks to the `table_rewrite` event, it is possible to implement a table rewriting policy only allowing the rewrite in maintenance windows.

Here's an example implementing such a policy.

CREATE OR REPLACE FUNCTION no\_rewrite()
 RETURNS event\_trigger
 LANGUAGE plpgsql AS
$$
---
--- Implement local Table Rewriting policy:
---   public.foo is not allowed rewriting, ever
---   other tables are only allowed rewriting between 1am and 6am
---   unless they have more than 100 blocks
---
DECLARE
  table\_oid oid := pg\_event\_trigger\_table\_rewrite\_oid();
  current\_hour integer := extract('hour' from current\_time);
  pages integer;
  max\_pages integer := 100;
BEGIN
  IF pg\_event\_trigger\_table\_rewrite\_oid() = 'public.foo'::regclass
  THEN
        RAISE EXCEPTION 'you''re not allowed to rewrite the table %',
                        table\_oid::regclass;
  END IF;

  SELECT INTO pages relpages FROM pg\_class WHERE oid = table\_oid;
  IF pages > max\_pages
  THEN
        RAISE EXCEPTION 'rewrites only allowed for table with less than % pages',
                        max\_pages;
  END IF;

  IF current\_hour NOT BETWEEN 1 AND 6
  THEN
        RAISE EXCEPTION 'rewrites only allowed between 1am and 6am';
  END IF;
END;
$$;

CREATE EVENT TRIGGER no\_rewrite\_allowed
                  ON table\_rewrite
   EXECUTE FUNCTION no\_rewrite();
