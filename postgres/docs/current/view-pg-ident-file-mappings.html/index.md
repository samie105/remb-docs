---
title: "PostgreSQL: Documentation: 18: 53.11. pg_ident_file_mappings"
source: "https://www.postgresql.org/docs/current/view-pg-ident-file-mappings.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-ident-file-mappings.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:10.795Z"
content_hash: "793cb15ecb2c8e0af014f7cf96fa9b5dec0e3b0583061966b7b9a7e3c9852f7f"
menu_path: ["PostgreSQL: Documentation: 18: 53.11. pg_ident_file_mappings"]
section_path: []
nav_prev: {"path": "postgres/docs/current/gssapi-auth.html/index.md", "title": "PostgreSQL: Documentation: 18: 20.6.\u00a0GSSAPI Authentication"}
nav_next: {"path": "postgres/docs/current/catalog-pg-subscription.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.54.\u00a0pg_subscription"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-ident-file-mappings.html "PostgreSQL devel - 53.11. pg_ident_file_mappings")

The view `pg_ident_file_mappings` provides a summary of the contents of the client user name mapping configuration file, [`pg_ident.conf`](https://www.postgresql.org/docs/current/auth-username-maps.html "20.2. User Name Maps"). A row appears in this view for each non-empty, non-comment line in the file, with annotations indicating whether the map could be applied successfully.

This view can be helpful for checking whether planned changes in the authentication configuration file will work, or for diagnosing a previous failure. Note that this view reports on the _current_ contents of the file, not on what was last loaded by the server.

By default, the `pg_ident_file_mappings` view can be read only by superusers.

**Table 53.11. `pg_ident_file_mappings` Columns**

Column Type

Description

`map_number` `int4`

Number of this map, in priority order, if valid, otherwise `NULL`

`file_name` `text`

Name of the file containing this map

`line_number` `int4`

Line number of this map in `file_name`

`map_name` `text`

Name of the map

`sys_name` `text`

Detected user name of the client

`pg_username` `text`

Requested PostgreSQL user name

`error` `text`

If not `NULL`, an error message indicating why this line could not be processed

Usually, a row reflecting an incorrect entry will have values for only the `line_number` and `error` fields.

See [Chapter 20](https://www.postgresql.org/docs/current/client-authentication.html "Chapter 20. Client Authentication") for more information about client authentication configuration.
