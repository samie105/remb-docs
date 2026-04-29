---
title: "sqlite - Node documentation"
source: "https://docs.deno.com/api/node/sqlite/"
canonical_url: "https://docs.deno.com/api/node/sqlite/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:11:50.750Z"
content_hash: "1ab248979756d08cb76922da473de2e4b5d362a7ac681eb46e84363d61c8c3f9"
menu_path: ["sqlite - Node documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../sea/index.md", "title": "sea - Node documentation"}
nav_next: {"path": "../stream/index.md", "title": "stream - Node documentation"}
---

### Usage in Deno

```typescript
import * as mod from "node:sqlite";
```

Deno compatibility

This module has been added in Deno v2.2.

The `node:sqlite` module facilitates working with SQLite databases. To access it:

```js
import sqlite from 'node:sqlite';
```

This module is only available under the `node:` scheme. The following will not work:

```js
import sqlite from 'sqlite';
```

The following example shows the basic usage of the `node:sqlite` module to open an in-memory database, write data to the database, and then read the data back.

```js
import { DatabaseSync } from 'node:sqlite';
const database = new DatabaseSync(':memory:');

// Execute SQL statements from strings.
database.exec(`
  CREATE TABLE data(
    key INTEGER PRIMARY KEY,
    value TEXT
  ) STRICT
`);
// Create a prepared statement to insert data into the database.
const insert = database.prepare('INSERT INTO data (key, value) VALUES (?, ?)');
// Execute the prepared statement with bound values.
insert.run(1, 'hello');
insert.run(2, 'world');
// Create a prepared statement to read data from the database.
const query = database.prepare('SELECT * FROM data ORDER BY key');
// Execute the prepared statement and log the result set.
console.log(query.all());
// Prints: [ { key: 1, value: 'hello' }, { key: 2, value: 'world' } ]
```

c

[DatabaseSync](.././sqlite/~/DatabaseSync "DatabaseSync")

This class represents a single [connection](https://www.sqlite.org/c3ref/sqlite3.html) to a SQLite database. All APIs exposed by this class execute synchronously.

-   [applyChangeset](.././sqlite/~/DatabaseSync#method_applychangeset_0)
-   [close](.././sqlite/~/DatabaseSync#method_close_0)
-   [createSession](.././sqlite/~/DatabaseSync#method_createsession_0)
-   [enableLoadExtension](.././sqlite/~/DatabaseSync#method_enableloadextension_0)
-   [exec](.././sqlite/~/DatabaseSync#method_exec_0)
-   [function](.././sqlite/~/DatabaseSync#method_function_0)
-   [loadExtension](.././sqlite/~/DatabaseSync#method_loadextension_0)
-   [open](.././sqlite/~/DatabaseSync#method_open_0)
-   [prepare](.././sqlite/~/DatabaseSync#method_prepare_0)

c

[StatementSync](.././sqlite/~/StatementSync "StatementSync")

This class represents a single [prepared statement](https://www.sqlite.org/c3ref/stmt.html). This class cannot be instantiated via its constructor. Instead, instances are created via the`database.prepare()` method. All APIs exposed by this class execute synchronously.

-   [all](.././sqlite/~/StatementSync#method_all_0)
-   [expandedSQL](.././sqlite/~/StatementSync#property_expandedsql)
-   [get](.././sqlite/~/StatementSync#method_get_0)
-   [iterate](.././sqlite/~/StatementSync#method_iterate_0)
-   [run](.././sqlite/~/StatementSync#method_run_0)
-   [setAllowBareNamedParameters](.././sqlite/~/StatementSync#method_setallowbarenamedparameters_0)
-   [setReadBigInts](.././sqlite/~/StatementSync#method_setreadbigints_0)
-   [sourceSQL](.././sqlite/~/StatementSync#property_sourcesql)

I

[ApplyChangesetOptions](.././sqlite/~/ApplyChangesetOptions "ApplyChangesetOptions")

No documentation available

-   [filter](.././sqlite/~/ApplyChangesetOptions#property_filter)
-   [onConflict](.././sqlite/~/ApplyChangesetOptions#property_onconflict)

I

[CreateSessionOptions](.././sqlite/~/CreateSessionOptions "CreateSessionOptions")

No documentation available

-   [db](.././sqlite/~/CreateSessionOptions#property_db)
-   [table](.././sqlite/~/CreateSessionOptions#property_table)

I

[DatabaseSyncOptions](.././sqlite/~/DatabaseSyncOptions "DatabaseSyncOptions")

No documentation available

-   [allowExtension](.././sqlite/~/DatabaseSyncOptions#property_allowextension)
-   [enableDoubleQuotedStringLiterals](.././sqlite/~/DatabaseSyncOptions#property_enabledoublequotedstringliterals)
-   [enableForeignKeyConstraints](.././sqlite/~/DatabaseSyncOptions#property_enableforeignkeyconstraints)
-   [open](.././sqlite/~/DatabaseSyncOptions#property_open)
-   [readOnly](.././sqlite/~/DatabaseSyncOptions#property_readonly)

I

[FunctionOptions](.././sqlite/~/FunctionOptions "FunctionOptions")

No documentation available

-   [deterministic](.././sqlite/~/FunctionOptions#property_deterministic)
-   [directOnly](.././sqlite/~/FunctionOptions#property_directonly)
-   [useBigIntArguments](.././sqlite/~/FunctionOptions#property_usebigintarguments)
-   [varargs](.././sqlite/~/FunctionOptions#property_varargs)

I

[Session](.././sqlite/~/Session "Session")

No documentation available

-   [changeset](.././sqlite/~/Session#method_changeset_0)
-   [close](.././sqlite/~/Session#method_close_0)
-   [patchset](.././sqlite/~/Session#method_patchset_0)

I

[StatementResultingChanges](.././sqlite/~/StatementResultingChanges "StatementResultingChanges")

No documentation available

-   [changes](.././sqlite/~/StatementResultingChanges#property_changes)
-   [lastInsertRowid](.././sqlite/~/StatementResultingChanges#property_lastinsertrowid)

N

[constants](.././sqlite/~/constants "constants")

No documentation available

T

[SQLInputValue](.././sqlite/~/SQLInputValue "SQLInputValue")

No documentation available

T

[SQLOutputValue](.././sqlite/~/SQLOutputValue "SQLOutputValue")

No documentation available

T

[SupportedValueType](.././sqlite/~/SupportedValueType "SupportedValueType")

No documentation available

v

[constants.SQLITE\_CHANGESET\_ABORT](.././sqlite/~/constants.SQLITE_CHANGESET_ABORT "constants.SQLITE_CHANGESET_ABORT")

Abort when a change encounters a conflict and roll back database.

v

[constants.SQLITE\_CHANGESET\_CONFLICT](.././sqlite/~/constants.SQLITE_CHANGESET_CONFLICT "constants.SQLITE_CHANGESET_CONFLICT")

This constant is passed to the conflict handler while processing an INSERT change if the operation would result in duplicate primary key values.

v

[constants.SQLITE\_CHANGESET\_DATA](.././sqlite/~/constants.SQLITE_CHANGESET_DATA "constants.SQLITE_CHANGESET_DATA")

The conflict handler is invoked with this constant when processing a DELETE or UPDATE change if a row with the required PRIMARY KEY fields is present in the database, but one or more other (non primary-key) fields modified by the update do not contain the expected "before" values.

v

[constants.SQLITE\_CHANGESET\_FOREIGN\_KEY](.././sqlite/~/constants.SQLITE_CHANGESET_FOREIGN_KEY "constants.SQLITE_CHANGESET_FOREIGN_KEY")

If foreign key handling is enabled, and applying a changeset leaves the database in a state containing foreign key violations, the conflict handler is invoked with this constant exactly once before the changeset is committed. If the conflict handler returns `SQLITE_CHANGESET_OMIT`, the changes, including those that caused the foreign key constraint violation, are committed. Or, if it returns `SQLITE_CHANGESET_ABORT`, the changeset is rolled back.

v

[constants.SQLITE\_CHANGESET\_NOTFOUND](.././sqlite/~/constants.SQLITE_CHANGESET_NOTFOUND "constants.SQLITE_CHANGESET_NOTFOUND")

The conflict handler is invoked with this constant when processing a DELETE or UPDATE change if a row with the required PRIMARY KEY fields is not present in the database.

v

[constants.SQLITE\_CHANGESET\_OMIT](.././sqlite/~/constants.SQLITE_CHANGESET_OMIT "constants.SQLITE_CHANGESET_OMIT")

Conflicting changes are omitted.

v

[constants.SQLITE\_CHANGESET\_REPLACE](.././sqlite/~/constants.SQLITE_CHANGESET_REPLACE "constants.SQLITE_CHANGESET_REPLACE")

Conflicting changes replace existing values. Note that this value can only be returned when the type of conflict is either `SQLITE_CHANGESET_DATA` or `SQLITE_CHANGESET_CONFLICT`.
