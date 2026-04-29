---
title: "PostgreSQL: Documentation: 18: Appendix B. Date/Time Support"
source: "https://www.postgresql.org/docs/current/datetime-appendix.html"
canonical_url: "https://www.postgresql.org/docs/current/datetime-appendix.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:21.361Z"
content_hash: "64ca084662ea6cb71f00158b0d7378cb7af69936a0bde024db80f5a879505e01"
menu_path: ["PostgreSQL: Documentation: 18: Appendix B. Date/Time Support"]
section_path: []
nav_prev: {"path": "../bki.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a068.\u00a0System Catalog Declarations and Initial Contents"}
nav_next: {"path": "../sql-keywords-appendix.html/index.md", "title": "PostgreSQL: Documentation: 18: Appendix\u00a0C.\u00a0SQL Key Words"}
---

PostgreSQL uses an internal heuristic parser for all date/time input support. Dates and times are input as strings, and are broken up into distinct fields with a preliminary determination of what kind of information can be in the field. Each field is interpreted and either assigned a numeric value, ignored, or rejected. The parser contains internal lookup tables for all textual fields, including months, days of the week, and time zones.

This appendix includes information on the content of these lookup tables and describes the steps used by the parser to decode dates and times.
