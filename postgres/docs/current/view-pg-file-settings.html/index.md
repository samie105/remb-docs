---
title: "PostgreSQL: Documentation: 18: 53.8. pg_file_settings"
source: "https://www.postgresql.org/docs/current/view-pg-file-settings.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-file-settings.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:52.002Z"
content_hash: "3a02a88f037fa64e0fc092711d9f3d185a7db83a60a1d68f6f9450b5f1c0224e"
menu_path: ["PostgreSQL: Documentation: 18: 53.8. pg_file_settings"]
section_path: []
nav_prev: {"path": "postgres/docs/current/color-which.html/index.md", "title": "PostgreSQL: Documentation: 18: N.2.\u00a0Configuring the Colors"}
nav_next: {"path": "postgres/docs/current/logical-replication-upgrade.html/index.md", "title": "PostgreSQL: Documentation: 18: 29.13.\u00a0Upgrade"}
---

The view `pg_file_settings` provides a summary of the contents of the server's configuration file(s). A row appears in this view for each “name = value” entry appearing in the files, with annotations indicating whether the value could be applied successfully. Additional row(s) may appear for problems not linked to a “name = value” entry, such as syntax errors in the files.

This view is helpful for checking whether planned changes in the configuration files will work, or for diagnosing a previous failure. Note that this view reports on the _current_ contents of the files, not on what was last applied by the server. (The [`pg_settings`](https://www.postgresql.org/docs/current/view-pg-settings.html "53.25. pg_settings") view is usually sufficient to determine that.)

By default, the `pg_file_settings` view can be read only by superusers.

**Table 53.8. `pg_file_settings` Columns**

Column Type

Description

`sourcefile` `text`

Full path name of the configuration file

`sourceline` `int4`

Line number within the configuration file where the entry appears

`seqno` `int4`

Order in which the entries are processed (1.._`n`_)

`name` `text`

Configuration parameter name

`setting` `text`

Value to be assigned to the parameter

`applied` `bool`

True if the value can be applied successfully

`error` `text`

If not null, an error message indicating why this entry could not be applied

If the configuration file contains syntax errors or invalid parameter names, the server will not attempt to apply any settings from it, and therefore all the `applied` fields will read as false. In such a case there will be one or more rows with non-null `error` fields indicating the problem(s). Otherwise, individual settings will be applied if possible. If an individual setting cannot be applied (e.g., invalid value, or the setting cannot be changed after server start) it will have an appropriate message in the `error` field. Another way that an entry might have `applied` = false is that it is overridden by a later entry for the same parameter name; this case is not considered an error so nothing appears in the `error` field.

See [Section 19.1](https://www.postgresql.org/docs/current/config-setting.html "19.1. Setting Parameters") for more information about the various ways to change run-time parameters.


