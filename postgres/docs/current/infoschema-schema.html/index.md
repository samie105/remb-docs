---
title: "PostgreSQL: Documentation: 18: 35.1. The Schema"
source: "https://www.postgresql.org/docs/current/infoschema-schema.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-schema.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:08.664Z"
content_hash: "504b3623226caa8d3fd3c4516c6948ad7fdbf26abf9ba3057a90f40dd1c8c139"
menu_path: ["PostgreSQL: Documentation: 18: 35.1. The Schema"]
section_path: []
---
The information schema itself is a schema named `information_schema`. This schema automatically exists in all databases. The owner of this schema is the initial database user in the cluster, and that user naturally has all the privileges on this schema, including the ability to drop it (but the space savings achieved by that are minuscule).

By default, the information schema is not in the schema search path, so you need to access all objects in it through qualified names. Since the names of some of the objects in the information schema are generic names that might occur in user applications, you should be careful if you want to put the information schema in the path.
