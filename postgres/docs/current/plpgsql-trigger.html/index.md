---
title: "PostgreSQL: Documentation: 18: 41.10. Trigger Functions"
source: "https://www.postgresql.org/docs/current/plpgsql-trigger.html"
canonical_url: "https://www.postgresql.org/docs/current/plpgsql-trigger.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:49.450Z"
content_hash: "99c558cd738be13023f3e0eeaf7756b003cd944e607b4546c9d0915702e6a9bc"
menu_path: ["PostgreSQL: Documentation: 18: 41.10. Trigger Functions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/plpgsql-statements.html/index.md", "title": "PostgreSQL: Documentation: 18: 41.5.\u00a0Basic Statements"}
nav_next: {"path": "postgres/docs/current/plpython-data.html/index.md", "title": "PostgreSQL: Documentation: 18: 44.2.\u00a0Data Values"}
---

PL/pgSQL can be used to define trigger functions on data changes or database events. A trigger function is created with the `CREATE FUNCTION` command, declaring it as a function with no arguments and a return type of `trigger` (for data change triggers) or `event_trigger` (for database event triggers). Special local variables named ``TG__`something`_`` are automatically defined to describe the condition that triggered the call.

### 41.10.1. Triggers on Data Changes [#](#PLPGSQL-DML-TRIGGER)

A [data change trigger](https://www.postgresql.org/docs/current/triggers.html "Chapter 37. Triggers") is declared as a function with no arguments and a return type of `trigger`. Note that the function must be declared with no arguments even if it expects to receive some arguments specified in `CREATE TRIGGER` — such arguments are passed via `TG_ARGV`, as described below.

When a PL/pgSQL function is called as a trigger, several special variables are created automatically in the top-level block. They are:

`NEW` `record` [#](#PLPGSQL-DML-TRIGGER-NEW)

new database row for `INSERT`/`UPDATE` operations in row-level triggers. This variable is null in statement-level triggers and for `DELETE` operations.

`OLD` `record` [#](#PLPGSQL-DML-TRIGGER-OLD)

old database row for `UPDATE`/`DELETE` operations in row-level triggers. This variable is null in statement-level triggers and for `INSERT` operations.

`TG_NAME` `name` [#](#PLPGSQL-DML-TRIGGER-TG-NAME)

name of the trigger which fired.

`TG_WHEN` `text` [#](#PLPGSQL-DML-TRIGGER-TG-WHEN)

`BEFORE`, `AFTER`, or `INSTEAD OF`, depending on the trigger's definition.

`TG_LEVEL` `text` [#](#PLPGSQL-DML-TRIGGER-TG-LEVEL)

`ROW` or `STATEMENT`, depending on the trigger's definition.

`TG_OP` `text` [#](#PLPGSQL-DML-TRIGGER-TG-OP)

operation for which the trigger was fired: `INSERT`, `UPDATE`, `DELETE`, or `TRUNCATE`.

`TG_RELID` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`) [#](#PLPGSQL-DML-TRIGGER-TG-RELID)

object ID of the table that caused the trigger invocation.

`TG_RELNAME` `name` [#](#PLPGSQL-DML-TRIGGER-TG-RELNAME)

table that caused the trigger invocation. This is now deprecated, and could disappear in a future release. Use `TG_TABLE_NAME` instead.

`TG_TABLE_NAME` `name` [#](#PLPGSQL-DML-TRIGGER-TG-TABLE-NAME)

table that caused the trigger invocation.

`TG_TABLE_SCHEMA` `name` [#](#PLPGSQL-DML-TRIGGER-TG-TABLE-SCHEMA)

schema of the table that caused the trigger invocation.

`TG_NARGS` `integer` [#](#PLPGSQL-DML-TRIGGER-TG-NARGS)

number of arguments given to the trigger function in the `CREATE TRIGGER` statement.

`TG_ARGV` `text[]` [#](#PLPGSQL-DML-TRIGGER-TG-ARGV)

arguments from the `CREATE TRIGGER` statement. The index counts from 0. Invalid indexes (less than 0 or greater than or equal to `tg_nargs`) result in a null value.

A trigger function must return either `NULL` or a record/row value having exactly the structure of the table the trigger was fired for.

Row-level triggers fired `BEFORE` can return null to signal the trigger manager to skip the rest of the operation for this row (i.e., subsequent triggers are not fired, and the `INSERT`/`UPDATE`/`DELETE` does not occur for this row). If a nonnull value is returned then the operation proceeds with that row value. Returning a row value different from the original value of `NEW` alters the row that will be inserted or updated. Thus, if the trigger function wants the triggering action to succeed normally without altering the row value, `NEW` (or a value equal thereto) has to be returned. To alter the row to be stored, it is possible to replace single values directly in `NEW` and return the modified `NEW`, or to build a complete new record/row to return. In the case of a before-trigger on `DELETE`, the returned value has no direct effect, but it has to be nonnull to allow the trigger action to proceed. Note that `NEW` is null in `DELETE` triggers, so returning that is usually not sensible. The usual idiom in `DELETE` triggers is to return `OLD`.

`INSTEAD OF` triggers (which are always row-level triggers, and may only be used on views) can return null to signal that they did not perform any updates, and that the rest of the operation for this row should be skipped (i.e., subsequent triggers are not fired, and the row is not counted in the rows-affected status for the surrounding `INSERT`/`UPDATE`/`DELETE`). Otherwise a nonnull value should be returned, to signal that the trigger performed the requested operation. For `INSERT` and `UPDATE` operations, the return value should be `NEW`, which the trigger function may modify to support `INSERT RETURNING` and `UPDATE RETURNING` (this will also affect the row value passed to any subsequent triggers, or passed to a special `EXCLUDED` alias reference within an `INSERT` statement with an `ON CONFLICT DO UPDATE` clause). For `DELETE` operations, the return value should be `OLD`.

The return value of a row-level trigger fired `AFTER` or a statement-level trigger fired `BEFORE` or `AFTER` is always ignored; it might as well be null. However, any of these types of triggers might still abort the entire operation by raising an error.

[Example 41.3](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-TRIGGER-EXAMPLE "Example 41.3. A PL/pgSQL Trigger Function") shows an example of a trigger function in PL/pgSQL.

**Example 41.3. A PL/pgSQL Trigger Function**

This example trigger ensures that any time a row is inserted or updated in the table, the current user name and time are stamped into the row. And it checks that an employee's name is given and that the salary is a positive value.

CREATE TABLE emp (
    empname           text,
    salary            integer,
    last\_date         timestamp,
    last\_user         text
);

CREATE FUNCTION emp\_stamp() RETURNS trigger AS $emp\_stamp$
    BEGIN
        -- Check that empname and salary are given
        IF NEW.empname IS NULL THEN
            RAISE EXCEPTION 'empname cannot be null';
        END IF;
        IF NEW.salary IS NULL THEN
            RAISE EXCEPTION '% cannot have null salary', NEW.empname;
        END IF;

        -- Who works for us when they must pay for it?
        IF NEW.salary < 0 THEN
            RAISE EXCEPTION '% cannot have a negative salary', NEW.empname;
        END IF;

        -- Remember who changed the payroll when
        NEW.last\_date := current\_timestamp;
        NEW.last\_user := current\_user;
        RETURN NEW;
    END;
$emp\_stamp$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_stamp BEFORE INSERT OR UPDATE ON emp
    FOR EACH ROW EXECUTE FUNCTION emp\_stamp();

Another way to log changes to a table involves creating a new table that holds a row for each insert, update, or delete that occurs. This approach can be thought of as auditing changes to a table. [Example 41.4](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-TRIGGER-AUDIT-EXAMPLE "Example 41.4. A PL/pgSQL Trigger Function for Auditing") shows an example of an audit trigger function in PL/pgSQL.

**Example 41.4. A PL/pgSQL Trigger Function for Auditing**

This example trigger ensures that any insert, update or delete of a row in the `emp` table is recorded (i.e., audited) in the `emp_audit` table. The current time and user name are stamped into the row, together with the type of operation performed on it.

CREATE TABLE emp (
    empname           text NOT NULL,
    salary            integer
);

CREATE TABLE emp\_audit(
    operation         char(1)   NOT NULL,
    stamp             timestamp NOT NULL,
    userid            text      NOT NULL,
    empname           text      NOT NULL,
    salary            integer
);

CREATE OR REPLACE FUNCTION process\_emp\_audit() RETURNS TRIGGER AS $emp\_audit$
    BEGIN
        --
        -- Create a row in emp\_audit to reflect the operation performed on emp,
        -- making use of the special variable TG\_OP to work out the operation.
        --
        IF (TG\_OP = 'DELETE') THEN
            INSERT INTO emp\_audit SELECT 'D', now(), current\_user, OLD.\*;
        ELSIF (TG\_OP = 'UPDATE') THEN
            INSERT INTO emp\_audit SELECT 'U', now(), current\_user, NEW.\*;
        ELSIF (TG\_OP = 'INSERT') THEN
            INSERT INTO emp\_audit SELECT 'I', now(), current\_user, NEW.\*;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$emp\_audit$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_audit
AFTER INSERT OR UPDATE OR DELETE ON emp
    FOR EACH ROW EXECUTE FUNCTION process\_emp\_audit();

A variation of the previous example uses a view joining the main table to the audit table, to show when each entry was last modified. This approach still records the full audit trail of changes to the table, but also presents a simplified view of the audit trail, showing just the last modified timestamp derived from the audit trail for each entry. [Example 41.5](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-VIEW-TRIGGER-AUDIT-EXAMPLE "Example 41.5. A PL/pgSQL View Trigger Function for Auditing") shows an example of an audit trigger on a view in PL/pgSQL.

**Example 41.5. A PL/pgSQL View Trigger Function for Auditing**

This example uses a trigger on the view to make it updatable, and ensure that any insert, update or delete of a row in the view is recorded (i.e., audited) in the `emp_audit` table. The current time and user name are recorded, together with the type of operation performed, and the view displays the last modified time of each row.

CREATE TABLE emp (
    empname           text PRIMARY KEY,
    salary            integer
);

CREATE TABLE emp\_audit(
    operation         char(1)   NOT NULL,
    userid            text      NOT NULL,
    empname           text      NOT NULL,
    salary            integer,
    stamp             timestamp NOT NULL
);

CREATE VIEW emp\_view AS
    SELECT e.empname,
           e.salary,
           max(ea.stamp) AS last\_updated
      FROM emp e
      LEFT JOIN emp\_audit ea ON ea.empname = e.empname
     GROUP BY 1, 2;

CREATE OR REPLACE FUNCTION update\_emp\_view() RETURNS TRIGGER AS $$
    BEGIN
        --
        -- Perform the required operation on emp, and create a row in emp\_audit
        -- to reflect the change made to emp.
        --
        IF (TG\_OP = 'DELETE') THEN
            DELETE FROM emp WHERE empname = OLD.empname;
            IF NOT FOUND THEN RETURN NULL; END IF;

            OLD.last\_updated = now();
            INSERT INTO emp\_audit VALUES('D', current\_user, OLD.\*);
            RETURN OLD;
        ELSIF (TG\_OP = 'UPDATE') THEN
            UPDATE emp SET salary = NEW.salary WHERE empname = OLD.empname;
            IF NOT FOUND THEN RETURN NULL; END IF;

            NEW.last\_updated = now();
            INSERT INTO emp\_audit VALUES('U', current\_user, NEW.\*);
            RETURN NEW;
        ELSIF (TG\_OP = 'INSERT') THEN
            INSERT INTO emp VALUES(NEW.empname, NEW.salary);

            NEW.last\_updated = now();
            INSERT INTO emp\_audit VALUES('I', current\_user, NEW.\*);
            RETURN NEW;
        END IF;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_audit
INSTEAD OF INSERT OR UPDATE OR DELETE ON emp\_view
    FOR EACH ROW EXECUTE FUNCTION update\_emp\_view();

One use of triggers is to maintain a summary table of another table. The resulting summary can be used in place of the original table for certain queries — often with vastly reduced run times. This technique is commonly used in Data Warehousing, where the tables of measured or observed data (called fact tables) might be extremely large. [Example 41.6](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-TRIGGER-SUMMARY-EXAMPLE "Example 41.6. A PL/pgSQL Trigger Function for Maintaining a Summary Table") shows an example of a trigger function in PL/pgSQL that maintains a summary table for a fact table in a data warehouse.

**Example 41.6. A PL/pgSQL Trigger Function for Maintaining a Summary Table**

The schema detailed here is partly based on the _Grocery Store_ example from _The Data Warehouse Toolkit_ by Ralph Kimball.

\--
-- Main tables - time dimension and sales fact.
--
CREATE TABLE time\_dimension (
    time\_key                    integer NOT NULL,
    day\_of\_week                 integer NOT NULL,
    day\_of\_month                integer NOT NULL,
    month                       integer NOT NULL,
    quarter                     integer NOT NULL,
    year                        integer NOT NULL
);
CREATE UNIQUE INDEX time\_dimension\_key ON time\_dimension(time\_key);

CREATE TABLE sales\_fact (
    time\_key                    integer NOT NULL,
    product\_key                 integer NOT NULL,
    store\_key                   integer NOT NULL,
    amount\_sold                 numeric(12,2) NOT NULL,
    units\_sold                  integer NOT NULL,
    amount\_cost                 numeric(12,2) NOT NULL
);
CREATE INDEX sales\_fact\_time ON sales\_fact(time\_key);

--
-- Summary table - sales by time.
--
CREATE TABLE sales\_summary\_bytime (
    time\_key                    integer NOT NULL,
    amount\_sold                 numeric(15,2) NOT NULL,
    units\_sold                  numeric(12) NOT NULL,
    amount\_cost                 numeric(15,2) NOT NULL
);
CREATE UNIQUE INDEX sales\_summary\_bytime\_key ON sales\_summary\_bytime(time\_key);

--
-- Function and trigger to amend summarized column(s) on UPDATE, INSERT, DELETE.
--
CREATE OR REPLACE FUNCTION maint\_sales\_summary\_bytime() RETURNS TRIGGER
AS $maint\_sales\_summary\_bytime$
    DECLARE
        delta\_time\_key          integer;
        delta\_amount\_sold       numeric(15,2);
        delta\_units\_sold        numeric(12);
        delta\_amount\_cost       numeric(15,2);
    BEGIN

        -- Work out the increment/decrement amount(s).
        IF (TG\_OP = 'DELETE') THEN

            delta\_time\_key = OLD.time\_key;
            delta\_amount\_sold = -1 \* OLD.amount\_sold;
            delta\_units\_sold = -1 \* OLD.units\_sold;
            delta\_amount\_cost = -1 \* OLD.amount\_cost;

        ELSIF (TG\_OP = 'UPDATE') THEN

            -- forbid updates that change the time\_key -
            -- (probably not too onerous, as DELETE + INSERT is how most
            -- changes will be made).
            IF ( OLD.time\_key != NEW.time\_key) THEN
                RAISE EXCEPTION 'Update of time\_key : % -> % not allowed',
                                                      OLD.time\_key, NEW.time\_key;
            END IF;

            delta\_time\_key = OLD.time\_key;
            delta\_amount\_sold = NEW.amount\_sold - OLD.amount\_sold;
            delta\_units\_sold = NEW.units\_sold - OLD.units\_sold;
            delta\_amount\_cost = NEW.amount\_cost - OLD.amount\_cost;

        ELSIF (TG\_OP = 'INSERT') THEN

            delta\_time\_key = NEW.time\_key;
            delta\_amount\_sold = NEW.amount\_sold;
            delta\_units\_sold = NEW.units\_sold;
            delta\_amount\_cost = NEW.amount\_cost;

        END IF;

        -- Insert or update the summary row with the new values.
        <<insert\_update>>
        LOOP
            UPDATE sales\_summary\_bytime
                SET amount\_sold = amount\_sold + delta\_amount\_sold,
                    units\_sold = units\_sold + delta\_units\_sold,
                    amount\_cost = amount\_cost + delta\_amount\_cost
                WHERE time\_key = delta\_time\_key;

            EXIT insert\_update WHEN found;

            BEGIN
                INSERT INTO sales\_summary\_bytime (
                            time\_key,
                            amount\_sold,
                            units\_sold,
                            amount\_cost)
                    VALUES (
                            delta\_time\_key,
                            delta\_amount\_sold,
                            delta\_units\_sold,
                            delta\_amount\_cost
                           );

                EXIT insert\_update;

            EXCEPTION
                WHEN UNIQUE\_VIOLATION THEN
                    -- do nothing
            END;
        END LOOP insert\_update;

        RETURN NULL;

    END;
$maint\_sales\_summary\_bytime$ LANGUAGE plpgsql;

CREATE TRIGGER maint\_sales\_summary\_bytime
AFTER INSERT OR UPDATE OR DELETE ON sales\_fact
    FOR EACH ROW EXECUTE FUNCTION maint\_sales\_summary\_bytime();

INSERT INTO sales\_fact VALUES(1,1,1,10,3,15);
INSERT INTO sales\_fact VALUES(1,2,1,20,5,35);
INSERT INTO sales\_fact VALUES(2,2,1,40,15,135);
INSERT INTO sales\_fact VALUES(2,3,1,10,1,13);
SELECT \* FROM sales\_summary\_bytime;
DELETE FROM sales\_fact WHERE product\_key = 1;
SELECT \* FROM sales\_summary\_bytime;
UPDATE sales\_fact SET units\_sold = units\_sold \* 2;
SELECT \* FROM sales\_summary\_bytime;

`AFTER` triggers can also make use of _transition tables_ to inspect the entire set of rows changed by the triggering statement. The `CREATE TRIGGER` command assigns names to one or both transition tables, and then the function can refer to those names as though they were read-only temporary tables. [Example 41.7](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-TRIGGER-AUDIT-TRANSITION-EXAMPLE "Example 41.7. Auditing with Transition Tables") shows an example.

**Example 41.7. Auditing with Transition Tables**

This example produces the same results as [Example 41.4](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-TRIGGER-AUDIT-EXAMPLE "Example 41.4. A PL/pgSQL Trigger Function for Auditing"), but instead of using a trigger that fires for every row, it uses a trigger that fires once per statement, after collecting the relevant information in a transition table. This can be significantly faster than the row-trigger approach when the invoking statement has modified many rows. Notice that we must make a separate trigger declaration for each kind of event, since the `REFERENCING` clauses must be different for each case. But this does not stop us from using a single trigger function if we choose. (In practice, it might be better to use three separate functions and avoid the run-time tests on `TG_OP`.)

CREATE TABLE emp (
    empname           text NOT NULL,
    salary            integer
);

CREATE TABLE emp\_audit(
    operation         char(1)   NOT NULL,
    stamp             timestamp NOT NULL,
    userid            text      NOT NULL,
    empname           text      NOT NULL,
    salary            integer
);

CREATE OR REPLACE FUNCTION process\_emp\_audit() RETURNS TRIGGER AS $emp\_audit$
    BEGIN
        --
        -- Create rows in emp\_audit to reflect the operations performed on emp,
        -- making use of the special variable TG\_OP to work out the operation.
        --
        IF (TG\_OP = 'DELETE') THEN
            INSERT INTO emp\_audit
                SELECT 'D', now(), current\_user, o.\* FROM old\_table o;
        ELSIF (TG\_OP = 'UPDATE') THEN
            INSERT INTO emp\_audit
                SELECT 'U', now(), current\_user, n.\* FROM new\_table n;
        ELSIF (TG\_OP = 'INSERT') THEN
            INSERT INTO emp\_audit
                SELECT 'I', now(), current\_user, n.\* FROM new\_table n;
        END IF;
        RETURN NULL; -- result is ignored since this is an AFTER trigger
    END;
$emp\_audit$ LANGUAGE plpgsql;

CREATE TRIGGER emp\_audit\_ins
    AFTER INSERT ON emp
    REFERENCING NEW TABLE AS new\_table
    FOR EACH STATEMENT EXECUTE FUNCTION process\_emp\_audit();
CREATE TRIGGER emp\_audit\_upd
    AFTER UPDATE ON emp
    REFERENCING OLD TABLE AS old\_table NEW TABLE AS new\_table
    FOR EACH STATEMENT EXECUTE FUNCTION process\_emp\_audit();
CREATE TRIGGER emp\_audit\_del
    AFTER DELETE ON emp
    REFERENCING OLD TABLE AS old\_table
    FOR EACH STATEMENT EXECUTE FUNCTION process\_emp\_audit();

  

### 41.10.2. Triggers on Events [#](#PLPGSQL-EVENT-TRIGGER)

PL/pgSQL can be used to define [event triggers](https://www.postgresql.org/docs/current/event-triggers.html "Chapter 38. Event Triggers"). PostgreSQL requires that a function that is to be called as an event trigger must be declared as a function with no arguments and a return type of `event_trigger`.

When a PL/pgSQL function is called as an event trigger, several special variables are created automatically in the top-level block. They are:

`TG_EVENT` `text` [#](#PLPGSQL-EVENT-TRIGGER-TG-EVENT)

event the trigger is fired for.

`TG_TAG` `text` [#](#PLPGSQL-EVENT-TRIGGER-TG-TAG)

command tag for which the trigger is fired.

[Example 41.8](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-EVENT-TRIGGER-EXAMPLE "Example 41.8. A PL/pgSQL Event Trigger Function") shows an example of an event trigger function in PL/pgSQL.

**Example 41.8. A PL/pgSQL Event Trigger Function**

This example trigger simply raises a `NOTICE` message each time a supported command is executed.

CREATE OR REPLACE FUNCTION snitch() RETURNS event\_trigger AS $$
BEGIN
    RAISE NOTICE 'snitch: % %', tg\_event, tg\_tag;
END;
$$ LANGUAGE plpgsql;

CREATE EVENT TRIGGER snitch ON ddl\_command\_start EXECUTE FUNCTION snitch();
