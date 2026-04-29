---
title: "PostgreSQL: Documentation: 18: N.2. Configuring the Colors"
source: "https://www.postgresql.org/docs/current/color-which.html"
canonical_url: "https://www.postgresql.org/docs/current/color-which.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:49.216Z"
content_hash: "4866c9d6ad33af39a3d657c1a9ade25b126ea59990ad87ee04f2cc2af7658ad1"
menu_path: ["PostgreSQL: Documentation: 18: N.2. Configuring the Colors"]
section_path: []
nav_prev: {"path": "../color-when.html/index.md", "title": "PostgreSQL: Documentation: 18: N.1.\u00a0When Color is Used"}
nav_next: {"path": "../config-setting.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.1.\u00a0Setting Parameters"}
---

The actual colors to be used are configured using the environment variable `PG_COLORS` (note plural). The value is a colon-separated list of ``_`key`_=_`value`_`` pairs. The keys specify what the color is to be used for. The values are SGR (Select Graphic Rendition) specifications, which are interpreted by the terminal.

The following keys are currently in use:

`error`

used to highlight the text “error” in error messages

`warning`

used to highlight the text “warning” in warning messages

`note`

used to highlight the text “detail” and “hint” in such messages

`locus`

used to highlight location information (e.g., program name and file name) in messages

The default value is `error=01;31:warning=01;35:note=01;36:locus=01` (`01;31` = bold red, `01;35` = bold magenta, `01;36` = bold cyan, `01` = bold default color).

### Tip

This color specification format is also used by other software packages such as GCC, GNU coreutils, and GNU grep.
