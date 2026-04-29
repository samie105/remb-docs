---
title: "PostgreSQL: Documentation: 18: 39.4. Rules on INSERT, UPDATE, and DELETE"
source: "https://www.postgresql.org/docs/current/rules-update.html"
canonical_url: "https://www.postgresql.org/docs/current/rules-update.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:09.554Z"
content_hash: "5f71e1148752c9861ddcd7344ebeca0e215565ef0cc3c7dbe71a1cc804a441f0"
menu_path: ["PostgreSQL: Documentation: 18: 39.4. Rules on INSERT, UPDATE, and DELETE"]
section_path: []
nav_prev: {"path": "../rules-triggers.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.7.\u00a0Rules Versus Triggers"}
nav_next: {"path": "../rules-views.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.2.\u00a0Views and the Rule System"}
---

Rules that are defined on `INSERT`, `UPDATE`, and `DELETE` are significantly different from the view rules described in the previous sections. First, their `CREATE RULE` command allows more:

Second, they don't modify the query tree in place. Instead they create zero or more new query trees and can throw away the original one.

### 39.4.1. How Update Rules Work [#](#RULES-UPDATE-HOW)

Keep the syntax:

CREATE \[ OR REPLACE \] RULE _`name`_ AS ON _`event`_
    TO _`table`_ \[ WHERE _`condition`_ \]
    DO \[ ALSO | INSTEAD \] { NOTHING | _`command`_ | ( _`command`_ ; _`command`_ ... ) }

in mind. In the following, _update rules_ means rules that are defined on `INSERT`, `UPDATE`, or `DELETE`.

Update rules get applied by the rule system when the result relation and the command type of a query tree are equal to the object and event given in the `CREATE RULE` command. For update rules, the rule system creates a list of query trees. Initially the query-tree list is empty. There can be zero (`NOTHING` key word), one, or multiple actions. To simplify, we will look at a rule with one action. This rule can have a qualification or not and it can be `INSTEAD` or `ALSO` (the default).

What is a rule qualification? It is a restriction that tells when the actions of the rule should be done and when not. This qualification can only reference the pseudorelations `NEW` and/or `OLD`, which basically represent the relation that was given as object (but with a special meaning).

So we have three cases that produce the following query trees for a one-action rule.

No qualification, with either `ALSO` or `INSTEAD`

the query tree from the rule action with the original query tree's qualification added

Qualification given and `ALSO`

the query tree from the rule action with the rule qualification and the original query tree's qualification added

Qualification given and `INSTEAD`

the query tree from the rule action with the rule qualification and the original query tree's qualification; and the original query tree with the negated rule qualification added

Finally, if the rule is `ALSO`, the unchanged original query tree is added to the list. Since only qualified `INSTEAD` rules already add the original query tree, we end up with either one or two output query trees for a rule with one action.

For `ON INSERT` rules, the original query (if not suppressed by `INSTEAD`) is done before any actions added by rules. This allows the actions to see the inserted row(s). But for `ON UPDATE` and `ON DELETE` rules, the original query is done after the actions added by rules. This ensures that the actions can see the to-be-updated or to-be-deleted rows; otherwise, the actions might do nothing because they find no rows matching their qualifications.

The query trees generated from rule actions are thrown into the rewrite system again, and maybe more rules get applied resulting in additional or fewer query trees. So a rule's actions must have either a different command type or a different result relation than the rule itself is on, otherwise this recursive process will end up in an infinite loop. (Recursive expansion of a rule will be detected and reported as an error.)

The query trees found in the actions of the `pg_rewrite` system catalog are only templates. Since they can reference the range-table entries for `NEW` and `OLD`, some substitutions have to be made before they can be used. For any reference to `NEW`, the target list of the original query is searched for a corresponding entry. If found, that entry's expression replaces the reference. Otherwise, `NEW` means the same as `OLD` (for an `UPDATE`) or is replaced by a null value (for an `INSERT`). Any reference to `OLD` is replaced by a reference to the range-table entry that is the result relation.

After the system is done applying update rules, it applies view rules to the produced query tree(s). Views cannot insert new update actions so there is no need to apply update rules to the output of view rewriting.

#### 39.4.1.1. A First Rule Step by Step [#](#RULES-UPDATE-HOW-FIRST)

Say we want to trace changes to the `sl_avail` column in the `shoelace_data` relation. So we set up a log table and a rule that conditionally writes a log entry when an `UPDATE` is performed on `shoelace_data`.

CREATE TABLE shoelace\_log (
    sl\_name    text,          -- shoelace changed
    sl\_avail   integer,       -- new available value
    log\_who    text,          -- who did it
    log\_when   timestamp      -- when
);

CREATE RULE log\_shoelace AS ON UPDATE TO shoelace\_data
    WHERE NEW.sl\_avail <> OLD.sl\_avail
    DO INSERT INTO shoelace\_log VALUES (
                                    NEW.sl\_name,
                                    NEW.sl\_avail,
                                    current\_user,
                                    current\_timestamp
                                );

Now someone does:

UPDATE shoelace\_data SET sl\_avail = 6 WHERE sl\_name = 'sl7';

and we look at the log table:

SELECT \* FROM shoelace\_log;

 sl\_name | sl\_avail | log\_who | log\_when
---------+----------+---------+----------------------------------
 sl7     |        6 | Al      | Tue Oct 20 16:14:45 1998 MET DST
(1 row)

That's what we expected. What happened in the background is the following. The parser created the query tree:

UPDATE shoelace\_data SET sl\_avail = 6
  FROM shoelace\_data shoelace\_data
 WHERE shoelace\_data.sl\_name = 'sl7';

There is a rule `log_shoelace` that is `ON UPDATE` with the rule qualification expression:

NEW.sl\_avail <> OLD.sl\_avail

and the action:

INSERT INTO shoelace\_log VALUES (
       new.sl\_name, new.sl\_avail,
       current\_user, current\_timestamp )
  FROM shoelace\_data new, shoelace\_data old;

(This looks a little strange since you cannot normally write `INSERT ... VALUES ... FROM`. The `FROM` clause here is just to indicate that there are range-table entries in the query tree for `new` and `old`. These are needed so that they can be referenced by variables in the `INSERT` command's query tree.)

The rule is a qualified `ALSO` rule, so the rule system has to return two query trees: the modified rule action and the original query tree. In step 1, the range table of the original query is incorporated into the rule's action query tree. This results in:

INSERT INTO shoelace\_log VALUES (
       new.sl\_name, new.sl\_avail,
       current\_user, current\_timestamp )
  FROM shoelace\_data new, shoelace\_data old,
       **shoelace\_data shoelace\_data**;

In step 2, the rule qualification is added to it, so the result set is restricted to rows where `sl_avail` changes:

INSERT INTO shoelace\_log VALUES (
       new.sl\_name, new.sl\_avail,
       current\_user, current\_timestamp )
  FROM shoelace\_data new, shoelace\_data old,
       shoelace\_data shoelace\_data
 **WHERE new.sl\_avail <> old.sl\_avail**;

(This looks even stranger, since `INSERT ... VALUES` doesn't have a `WHERE` clause either, but the planner and executor will have no difficulty with it. They need to support this same functionality anyway for `INSERT ... SELECT`.)

In step 3, the original query tree's qualification is added, restricting the result set further to only the rows that would have been touched by the original query:

INSERT INTO shoelace\_log VALUES (
       new.sl\_name, new.sl\_avail,
       current\_user, current\_timestamp )
  FROM shoelace\_data new, shoelace\_data old,
       shoelace\_data shoelace\_data
 WHERE new.sl\_avail <> old.sl\_avail
   **AND shoelace\_data.sl\_name = 'sl7'**;

Step 4 replaces references to `NEW` by the target list entries from the original query tree or by the matching variable references from the result relation:

INSERT INTO shoelace\_log VALUES (
       **shoelace\_data.sl\_name**, **6**,
       current\_user, current\_timestamp )
  FROM shoelace\_data new, shoelace\_data old,
       shoelace\_data shoelace\_data
 WHERE **6** <> old.sl\_avail
   AND shoelace\_data.sl\_name = 'sl7';

Step 5 changes `OLD` references into result relation references:

INSERT INTO shoelace\_log VALUES (
       shoelace\_data.sl\_name, 6,
       current\_user, current\_timestamp )
  FROM shoelace\_data new, shoelace\_data old,
       shoelace\_data shoelace\_data
 WHERE 6 <> **shoelace\_data.sl\_avail**
   AND shoelace\_data.sl\_name = 'sl7';

That's it. Since the rule is `ALSO`, we also output the original query tree. In short, the output from the rule system is a list of two query trees that correspond to these statements:

INSERT INTO shoelace\_log VALUES (
       shoelace\_data.sl\_name, 6,
       current\_user, current\_timestamp )
  FROM shoelace\_data
 WHERE 6 <> shoelace\_data.sl\_avail
   AND shoelace\_data.sl\_name = 'sl7';

UPDATE shoelace\_data SET sl\_avail = 6
 WHERE sl\_name = 'sl7';

These are executed in this order, and that is exactly what the rule was meant to do.

The substitutions and the added qualifications ensure that, if the original query would be, say:

UPDATE shoelace\_data SET sl\_color = 'green'
 WHERE sl\_name = 'sl7';

no log entry would get written. In that case, the original query tree does not contain a target list entry for `sl_avail`, so `NEW.sl_avail` will get replaced by `shoelace_data.sl_avail`. Thus, the extra command generated by the rule is:

INSERT INTO shoelace\_log VALUES (
       shoelace\_data.sl\_name, **shoelace\_data.sl\_avail**,
       current\_user, current\_timestamp )
  FROM shoelace\_data
 WHERE **shoelace\_data.sl\_avail** <> shoelace\_data.sl\_avail
   AND shoelace\_data.sl\_name = 'sl7';

and that qualification will never be true.

It will also work if the original query modifies multiple rows. So if someone issued the command:

UPDATE shoelace\_data SET sl\_avail = 0
 WHERE sl\_color = 'black';

four rows in fact get updated (`sl1`, `sl2`, `sl3`, and `sl4`). But `sl3` already has `sl_avail = 0`. In this case, the original query trees qualification is different and that results in the extra query tree:

INSERT INTO shoelace\_log
SELECT shoelace\_data.sl\_name, 0,
       current\_user, current\_timestamp
  FROM shoelace\_data
 WHERE 0 <> shoelace\_data.sl\_avail
   AND **shoelace\_data.sl\_color = 'black'**;

being generated by the rule. This query tree will surely insert three new log entries. And that's absolutely correct.

Here we can see why it is important that the original query tree is executed last. If the `UPDATE` had been executed first, all the rows would have already been set to zero, so the logging `INSERT` would not find any row where `0 <> shoelace_data.sl_avail`.

### 39.4.2. Cooperation with Views [#](#RULES-UPDATE-VIEWS)

A simple way to protect view relations from the mentioned possibility that someone can try to run `INSERT`, `UPDATE`, or `DELETE` on them is to let those query trees get thrown away. So we could create the rules:

CREATE RULE shoe\_ins\_protect AS ON INSERT TO shoe
    DO INSTEAD NOTHING;
CREATE RULE shoe\_upd\_protect AS ON UPDATE TO shoe
    DO INSTEAD NOTHING;
CREATE RULE shoe\_del\_protect AS ON DELETE TO shoe
    DO INSTEAD NOTHING;

If someone now tries to do any of these operations on the view relation `shoe`, the rule system will apply these rules. Since the rules have no actions and are `INSTEAD`, the resulting list of query trees will be empty and the whole query will become nothing because there is nothing left to be optimized or executed after the rule system is done with it.

A more sophisticated way to use the rule system is to create rules that rewrite the query tree into one that does the right operation on the real tables. To do that on the `shoelace` view, we create the following rules:

CREATE RULE shoelace\_ins AS ON INSERT TO shoelace
    DO INSTEAD
    INSERT INTO shoelace\_data VALUES (
           NEW.sl\_name,
           NEW.sl\_avail,
           NEW.sl\_color,
           NEW.sl\_len,
           NEW.sl\_unit
    );

CREATE RULE shoelace\_upd AS ON UPDATE TO shoelace
    DO INSTEAD
    UPDATE shoelace\_data
       SET sl\_name = NEW.sl\_name,
           sl\_avail = NEW.sl\_avail,
           sl\_color = NEW.sl\_color,
           sl\_len = NEW.sl\_len,
           sl\_unit = NEW.sl\_unit
     WHERE sl\_name = OLD.sl\_name;

CREATE RULE shoelace\_del AS ON DELETE TO shoelace
    DO INSTEAD
    DELETE FROM shoelace\_data
     WHERE sl\_name = OLD.sl\_name;

If you want to support `RETURNING` queries on the view, you need to make the rules include `RETURNING` clauses that compute the view rows. This is usually pretty trivial for views on a single table, but it's a bit tedious for join views such as `shoelace`. An example for the insert case is:

CREATE RULE shoelace\_ins AS ON INSERT TO shoelace
    DO INSTEAD
    INSERT INTO shoelace\_data VALUES (
           NEW.sl\_name,
           NEW.sl\_avail,
           NEW.sl\_color,
           NEW.sl\_len,
           NEW.sl\_unit
    )
    RETURNING
           shoelace\_data.\*,
           (SELECT shoelace\_data.sl\_len \* u.un\_fact
            FROM unit u WHERE shoelace\_data.sl\_unit = u.un\_name);

Note that this one rule supports both `INSERT` and `INSERT RETURNING` queries on the view — the `RETURNING` clause is simply ignored for `INSERT`.

Note that in the `RETURNING` clause of a rule, `OLD` and `NEW` refer to the pseudorelations added as extra range table entries to the rewritten query, rather than old/new rows in the result relation. Thus, for example, in a rule supporting `UPDATE` queries on this view, if the `RETURNING` clause contained `old.sl_name`, the old name would always be returned, regardless of whether the `RETURNING` clause in the query on the view specified `OLD` or `NEW`, which might be confusing. To avoid this confusion, and support returning old and new values in queries on the view, the `RETURNING` clause in the rule definition should refer to entries from the result relation such as `shoelace_data.sl_name`, without specifying `OLD` or `NEW`.

Now assume that once in a while, a pack of shoelaces arrives at the shop and a big parts list along with it. But you don't want to manually update the `shoelace` view every time. Instead we set up two little tables: one where you can insert the items from the part list, and one with a special trick. The creation commands for these are:

CREATE TABLE shoelace\_arrive (
    arr\_name    text,
    arr\_quant   integer
);

CREATE TABLE shoelace\_ok (
    ok\_name     text,
    ok\_quant    integer
);

CREATE RULE shoelace\_ok\_ins AS ON INSERT TO shoelace\_ok
    DO INSTEAD
    UPDATE shoelace
       SET sl\_avail = sl\_avail + NEW.ok\_quant
     WHERE sl\_name = NEW.ok\_name;

Now you can fill the table `shoelace_arrive` with the data from the parts list:

SELECT \* FROM shoelace\_arrive;

 arr\_name | arr\_quant
----------+-----------
 sl3      |        10
 sl6      |        20
 sl8      |        20
(3 rows)

Take a quick look at the current data:

SELECT \* FROM shoelace;

 sl\_name  | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm
----------+----------+----------+--------+---------+-----------
 sl1      |        5 | black    |     80 | cm      |        80
 sl2      |        6 | black    |    100 | cm      |       100
 sl7      |        6 | brown    |     60 | cm      |        60
 sl3      |        0 | black    |     35 | inch    |      88.9
 sl4      |        8 | black    |     40 | inch    |     101.6
 sl8      |        1 | brown    |     40 | inch    |     101.6
 sl5      |        4 | brown    |      1 | m       |       100
 sl6      |        0 | brown    |    0.9 | m       |        90
(8 rows)

Now move the arrived shoelaces in:

INSERT INTO shoelace\_ok SELECT \* FROM shoelace\_arrive;

and check the results:

SELECT \* FROM shoelace ORDER BY sl\_name;

 sl\_name  | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm
----------+----------+----------+--------+---------+-----------
 sl1      |        5 | black    |     80 | cm      |        80
 sl2      |        6 | black    |    100 | cm      |       100
 sl7      |        6 | brown    |     60 | cm      |        60
 sl4      |        8 | black    |     40 | inch    |     101.6
 sl3      |       10 | black    |     35 | inch    |      88.9
 sl8      |       21 | brown    |     40 | inch    |     101.6
 sl5      |        4 | brown    |      1 | m       |       100
 sl6      |       20 | brown    |    0.9 | m       |        90
(8 rows)

SELECT \* FROM shoelace\_log;

 sl\_name | sl\_avail | log\_who| log\_when
---------+----------+--------+----------------------------------
 sl7     |        6 | Al     | Tue Oct 20 19:14:45 1998 MET DST
 sl3     |       10 | Al     | Tue Oct 20 19:25:16 1998 MET DST
 sl6     |       20 | Al     | Tue Oct 20 19:25:16 1998 MET DST
 sl8     |       21 | Al     | Tue Oct 20 19:25:16 1998 MET DST
(4 rows)

It's a long way from the one `INSERT ... SELECT` to these results. And the description of the query-tree transformation will be the last in this chapter. First, there is the parser's output:

INSERT INTO shoelace\_ok
SELECT shoelace\_arrive.arr\_name, shoelace\_arrive.arr\_quant
  FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok;

Now the first rule `shoelace_ok_ins` is applied and turns this into:

UPDATE shoelace
   SET sl\_avail = shoelace.sl\_avail + shoelace\_arrive.arr\_quant
  FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,
       shoelace\_ok old, shoelace\_ok new,
       shoelace shoelace
 WHERE shoelace.sl\_name = shoelace\_arrive.arr\_name;

and throws away the original `INSERT` on `shoelace_ok`. This rewritten query is passed to the rule system again, and the second applied rule `shoelace_upd` produces:

UPDATE shoelace\_data
   SET sl\_name = shoelace.sl\_name,
       sl\_avail = shoelace.sl\_avail + shoelace\_arrive.arr\_quant,
       sl\_color = shoelace.sl\_color,
       sl\_len = shoelace.sl\_len,
       sl\_unit = shoelace.sl\_unit
  FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,
       shoelace\_ok old, shoelace\_ok new,
       shoelace shoelace, shoelace old,
       shoelace new, shoelace\_data shoelace\_data
 WHERE shoelace.sl\_name = shoelace\_arrive.arr\_name
   AND shoelace\_data.sl\_name = shoelace.sl\_name;

Again it's an `INSTEAD` rule and the previous query tree is trashed. Note that this query still uses the view `shoelace`. But the rule system isn't finished with this step, so it continues and applies the `_RETURN` rule on it, and we get:

UPDATE shoelace\_data
   SET sl\_name = s.sl\_name,
       sl\_avail = s.sl\_avail + shoelace\_arrive.arr\_quant,
       sl\_color = s.sl\_color,
       sl\_len = s.sl\_len,
       sl\_unit = s.sl\_unit
  FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,
       shoelace\_ok old, shoelace\_ok new,
       shoelace shoelace, shoelace old,
       shoelace new, shoelace\_data shoelace\_data,
       shoelace old, shoelace new,
       shoelace\_data s, unit u
 WHERE s.sl\_name = shoelace\_arrive.arr\_name
   AND shoelace\_data.sl\_name = s.sl\_name;

Finally, the rule `log_shoelace` gets applied, producing the extra query tree:

INSERT INTO shoelace\_log
SELECT s.sl\_name,
       s.sl\_avail + shoelace\_arrive.arr\_quant,
       current\_user,
       current\_timestamp
  FROM shoelace\_arrive shoelace\_arrive, shoelace\_ok shoelace\_ok,
       shoelace\_ok old, shoelace\_ok new,
       shoelace shoelace, shoelace old,
       shoelace new, shoelace\_data shoelace\_data,
       shoelace old, shoelace new,
       shoelace\_data s, unit u,
       shoelace\_data old, shoelace\_data new
       shoelace\_log shoelace\_log
 WHERE s.sl\_name = shoelace\_arrive.arr\_name
   AND shoelace\_data.sl\_name = s.sl\_name
   AND (s.sl\_avail + shoelace\_arrive.arr\_quant) <> s.sl\_avail;

After that the rule system runs out of rules and returns the generated query trees.

So we end up with two final query trees that are equivalent to the SQL statements:

INSERT INTO shoelace\_log
SELECT s.sl\_name,
       s.sl\_avail + shoelace\_arrive.arr\_quant,
       current\_user,
       current\_timestamp
  FROM shoelace\_arrive shoelace\_arrive, shoelace\_data shoelace\_data,
       shoelace\_data s
 WHERE s.sl\_name = shoelace\_arrive.arr\_name
   AND shoelace\_data.sl\_name = s.sl\_name
   AND s.sl\_avail + shoelace\_arrive.arr\_quant <> s.sl\_avail;

UPDATE shoelace\_data
   SET sl\_avail = shoelace\_data.sl\_avail + shoelace\_arrive.arr\_quant
  FROM shoelace\_arrive shoelace\_arrive,
       shoelace\_data shoelace\_data,
       shoelace\_data s
 WHERE s.sl\_name = shoelace\_arrive.sl\_name
   AND shoelace\_data.sl\_name = s.sl\_name;

The result is that data coming from one relation inserted into another, changed into updates on a third, changed into updating a fourth plus logging that final update in a fifth gets reduced into two queries.

There is a little detail that's a bit ugly. Looking at the two queries, it turns out that the `shoelace_data` relation appears twice in the range table where it could definitely be reduced to one. The planner does not handle it and so the execution plan for the rule systems output of the `INSERT` will be

Nested Loop
  ->  Merge Join
        ->  Seq Scan
              ->  Sort
                    ->  Seq Scan on s
        ->  Seq Scan
              ->  Sort
                    ->  Seq Scan on shoelace\_arrive
  ->  Seq Scan on shoelace\_data

while omitting the extra range table entry would result in a

Merge Join
  ->  Seq Scan
        ->  Sort
              ->  Seq Scan on s
  ->  Seq Scan
        ->  Sort
              ->  Seq Scan on shoelace\_arrive

which produces exactly the same entries in the log table. Thus, the rule system caused one extra scan on the table `shoelace_data` that is absolutely not necessary. And the same redundant scan is done once more in the `UPDATE`. But it was a really hard job to make that all possible at all.

Now we make a final demonstration of the PostgreSQL rule system and its power. Say you add some shoelaces with extraordinary colors to your database:

INSERT INTO shoelace VALUES ('sl9', 0, 'pink', 35.0, 'inch', 0.0);
INSERT INTO shoelace VALUES ('sl10', 1000, 'magenta', 40.0, 'inch', 0.0);

We would like to make a view to check which `shoelace` entries do not fit any shoe in color. The view for this is:

CREATE VIEW shoelace\_mismatch AS
    SELECT \* FROM shoelace WHERE NOT EXISTS
        (SELECT shoename FROM shoe WHERE slcolor = sl\_color);

Its output is:

SELECT \* FROM shoelace\_mismatch;

 sl\_name | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm
---------+----------+----------+--------+---------+-----------
 sl9     |        0 | pink     |     35 | inch    |      88.9
 sl10    |     1000 | magenta  |     40 | inch    |     101.6

Now we want to set it up so that mismatching shoelaces that are not in stock are deleted from the database. To make it a little harder for PostgreSQL, we don't delete it directly. Instead we create one more view:

CREATE VIEW shoelace\_can\_delete AS
    SELECT \* FROM shoelace\_mismatch WHERE sl\_avail = 0;

and do it this way:

DELETE FROM shoelace WHERE EXISTS
    (SELECT \* FROM shoelace\_can\_delete
             WHERE sl\_name = shoelace.sl\_name);

The results are:

SELECT \* FROM shoelace;

 sl\_name | sl\_avail | sl\_color | sl\_len | sl\_unit | sl\_len\_cm
---------+----------+----------+--------+---------+-----------
 sl1     |        5 | black    |     80 | cm      |        80
 sl2     |        6 | black    |    100 | cm      |       100
 sl7     |        6 | brown    |     60 | cm      |        60
 sl4     |        8 | black    |     40 | inch    |     101.6
 sl3     |       10 | black    |     35 | inch    |      88.9
 sl8     |       21 | brown    |     40 | inch    |     101.6
 sl10    |     1000 | magenta  |     40 | inch    |     101.6
 sl5     |        4 | brown    |      1 | m       |       100
 sl6     |       20 | brown    |    0.9 | m       |        90
(9 rows)

A `DELETE` on a view, with a subquery qualification that in total uses 4 nesting/joined views, where one of them itself has a subquery qualification containing a view and where calculated view columns are used, gets rewritten into one single query tree that deletes the requested data from a real table.

There are probably only a few situations out in the real world where such a construct is necessary. But it makes you feel comfortable that it works.
