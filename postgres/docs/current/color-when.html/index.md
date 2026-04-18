---
title: "PostgreSQL: Documentation: 18: N.1. When Color is Used"
source: "https://www.postgresql.org/docs/current/color-when.html"
canonical_url: "https://www.postgresql.org/docs/current/color-when.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:12.836Z"
content_hash: "346ff0b307d17194303d15b07911f132c29053fc77fa4e645ece0715105d257a"
menu_path: ["PostgreSQL: Documentation: 18: N.1. When Color is Used"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-available-extension-versions.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.4.\u00a0pg_available_extension_versions"}
nav_next: {"path": "postgres/docs/current/datetime-invalid-input.html/index.md", "title": "PostgreSQL: Documentation: 18: B.2.\u00a0Handling of Invalid or Ambiguous Timestamps"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/color-when.html "PostgreSQL 18 - N.1. When Color is Used") ([18](/docs/18/color-when.html "PostgreSQL 18 - N.1. When Color is Used")) / [17](/docs/17/color-when.html "PostgreSQL 17 - N.1. When Color is Used") / [16](/docs/16/color-when.html "PostgreSQL 16 - N.1. When Color is Used") / [15](/docs/15/color-when.html "PostgreSQL 15 - N.1. When Color is Used") / [14](/docs/14/color-when.html "PostgreSQL 14 - N.1. When Color is Used")

Development Versions: [devel](/docs/devel/color-when.html "PostgreSQL devel - N.1. When Color is Used")

Unsupported versions: [13](/docs/13/color-when.html "PostgreSQL 13 - N.1. When Color is Used")

## N.1. When Color is Used [#](#COLOR-WHEN)

To use colorized output, set the environment variable `PG_COLOR` as follows:

1.  If the value is `always`, then color is used.
    
2.  If the value is `auto` and the standard error stream is associated with a terminal device, then color is used.
    
3.  Otherwise, color is not used.
    

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/color-when.html/) to report a documentation issue.


