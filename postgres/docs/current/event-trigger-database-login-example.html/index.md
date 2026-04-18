---
title: "PostgreSQL: Documentation: 18: 38.5. A Database Login Event Trigger Example"
source: "https://www.postgresql.org/docs/current/event-trigger-database-login-example.html"
canonical_url: "https://www.postgresql.org/docs/current/event-trigger-database-login-example.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:14.286Z"
content_hash: "22c019cbcea73d819e565c3477daf34deac570e8bfb8d2f420c5504a6e6da4da"
menu_path: ["PostgreSQL: Documentation: 18: 38.5. A Database Login Event Trigger Example"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-parameters.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.33.\u00a0parameters"}
nav_next: {"path": "postgres/docs/current/pgprewarm.html/index.md", "title": "PostgreSQL: Documentation: 18: F.30.\u00a0pg_prewarm \u2014 preload relation data into buffer caches"}
---

The event trigger on the `login` event can be useful for logging user logins, for verifying the connection and assigning roles according to current circumstances, or for session data initialization. It is very important that any event trigger using the `login` event checks whether or not the database is in recovery before performing any writes. Writing to a standby server will make it inaccessible.

The following example demonstrates these options.

\-- create test tables and roles
CREATE TABLE user\_login\_log (
  "user" text,
  "session\_start" timestamp with time zone
);
CREATE ROLE day\_worker;
CREATE ROLE night\_worker;

-- the example trigger function
CREATE OR REPLACE FUNCTION init\_session()
  RETURNS event\_trigger SECURITY DEFINER
  LANGUAGE plpgsql AS
$$
DECLARE
  hour integer = EXTRACT('hour' FROM current\_time at time zone 'utc');
  rec boolean;
BEGIN
-- 1. Forbid logging in between 2AM and 4AM.
IF hour BETWEEN 2 AND 4 THEN
  RAISE EXCEPTION 'Login forbidden';
END IF;

-- The checks below cannot be performed on standby servers so
-- ensure the database is not in recovery before we perform any
-- operations.
SELECT pg\_is\_in\_recovery() INTO rec;
IF rec THEN
  RETURN;
END IF;

-- 2. Assign some roles. At daytime, grant the day\_worker role, else the
-- night\_worker role.
IF hour BETWEEN 8 AND 20 THEN
  EXECUTE 'REVOKE night\_worker FROM ' || quote\_ident(session\_user);
  EXECUTE 'GRANT day\_worker TO ' || quote\_ident(session\_user);
ELSE
  EXECUTE 'REVOKE day\_worker FROM ' || quote\_ident(session\_user);
  EXECUTE 'GRANT night\_worker TO ' || quote\_ident(session\_user);
END IF;

-- 3. Initialize user session data
CREATE TEMP TABLE session\_storage (x float, y integer);
ALTER TABLE session\_storage OWNER TO session\_user;

-- 4. Log the connection time
INSERT INTO public.user\_login\_log VALUES (session\_user, current\_timestamp);

END;
$$;

-- trigger definition
CREATE EVENT TRIGGER init\_session
  ON login
  EXECUTE FUNCTION init\_session();
ALTER EVENT TRIGGER init\_session ENABLE ALWAYS;
