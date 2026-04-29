---
title: "PostgreSQL: Documentation: 18: Chapter 28. Reliability and the Write-Ahead Log"
source: "https://www.postgresql.org/docs/current/wal.html"
canonical_url: "https://www.postgresql.org/docs/current/wal.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:16.539Z"
content_hash: "d4f2c2cd96e28bc6dd178e43143b9f158e85e12f8625fef429d64968faf28204"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 28. Reliability and the Write-Ahead Log"]
section_path: []
nav_prev: {"path": "../user-manag.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a021.\u00a0Database Roles"}
nav_next: {"path": "../jit.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a030.\u00a0Just-in-Time Compilation (JIT)"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/wal.html "PostgreSQL 18 - Chapter 28. Reliability and the Write-Ahead Log") ([18](/docs/18/wal.html "PostgreSQL 18 - Chapter 28. Reliability and the Write-Ahead Log")) / [17](/docs/17/wal.html "PostgreSQL 17 - Chapter 28. Reliability and the Write-Ahead Log") / [16](/docs/16/wal.html "PostgreSQL 16 - Chapter 28. Reliability and the Write-Ahead Log") / [15](/docs/15/wal.html "PostgreSQL 15 - Chapter 28. Reliability and the Write-Ahead Log") / [14](/docs/14/wal.html "PostgreSQL 14 - Chapter 28. Reliability and the Write-Ahead Log")

Development Versions: [devel](/docs/devel/wal.html "PostgreSQL devel - Chapter 28. Reliability and the Write-Ahead Log")

Unsupported versions: [13](/docs/13/wal.html "PostgreSQL 13 - Chapter 28. Reliability and the Write-Ahead Log") / [12](/docs/12/wal.html "PostgreSQL 12 - Chapter 28. Reliability and the Write-Ahead Log") / [11](/docs/11/wal.html "PostgreSQL 11 - Chapter 28. Reliability and the Write-Ahead Log") / [10](/docs/10/wal.html "PostgreSQL 10 - Chapter 28. Reliability and the Write-Ahead Log") / [9.6](/docs/9.6/wal.html "PostgreSQL 9.6 - Chapter 28. Reliability and the Write-Ahead Log") / [9.5](/docs/9.5/wal.html "PostgreSQL 9.5 - Chapter 28. Reliability and the Write-Ahead Log") / [9.4](/docs/9.4/wal.html "PostgreSQL 9.4 - Chapter 28. Reliability and the Write-Ahead Log") / [9.3](/docs/9.3/wal.html "PostgreSQL 9.3 - Chapter 28. Reliability and the Write-Ahead Log") / [9.2](/docs/9.2/wal.html "PostgreSQL 9.2 - Chapter 28. Reliability and the Write-Ahead Log") / [9.1](/docs/9.1/wal.html "PostgreSQL 9.1 - Chapter 28. Reliability and the Write-Ahead Log") / [9.0](/docs/9.0/wal.html "PostgreSQL 9.0 - Chapter 28. Reliability and the Write-Ahead Log") / [8.4](/docs/8.4/wal.html "PostgreSQL 8.4 - Chapter 28. Reliability and the Write-Ahead Log") / [8.3](/docs/8.3/wal.html "PostgreSQL 8.3 - Chapter 28. Reliability and the Write-Ahead Log") / [8.2](/docs/8.2/wal.html "PostgreSQL 8.2 - Chapter 28. Reliability and the Write-Ahead Log") / [8.1](/docs/8.1/wal.html "PostgreSQL 8.1 - Chapter 28. Reliability and the Write-Ahead Log") / [8.0](/docs/8.0/wal.html "PostgreSQL 8.0 - Chapter 28. Reliability and the Write-Ahead Log") / [7.4](/docs/7.4/wal.html "PostgreSQL 7.4 - Chapter 28. Reliability and the Write-Ahead Log") / [7.3](/docs/7.3/wal.html "PostgreSQL 7.3 - Chapter 28. Reliability and the Write-Ahead Log") / [7.2](/docs/7.2/wal.html "PostgreSQL 7.2 - Chapter 28. Reliability and the Write-Ahead Log") / [7.1](/docs/7.1/wal.html "PostgreSQL 7.1 - Chapter 28. Reliability and the Write-Ahead Log")

## Chapter 28. Reliability and the Write-Ahead Log

This chapter explains how to control the reliability of PostgreSQL, including details about the Write-Ahead Log.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/wal.html/) to report a documentation issue.
