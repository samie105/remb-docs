---
title: "Redis Insight v3.0.3, February 2026"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.3.0.3/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.3.0.3/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:13.600Z"
content_hash: "13b382d849a69661a78640f7cb848404fafd3f5283ecebaf72e2444a927bc084"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v3.0.3, February 2026","→","Redis Insight v3.0.3, February 2026"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v3.0.3, February 2026","→","Redis Insight v3.0.3, February 2026"]
nav_prev: {"path": "../v.3.0.2/index.md", "title": "Redis Insight v3.0.2, January 2026"}
nav_next: {"path": "../v.3.2.0/index.md", "title": "Redis Insight v3.2.0, February 2026"}
---

# Redis Insight v3.0.3, February 2026

Redis Insight v3.0.3

## 3.0.3 (February 2026)

This release includes new features, improvements, and bug fixes for Redis Insight.

### Details

*   Redis Data Integration (RDI) now uses API v2 when available, showing detailed pipeline status, component statuses, and richer metrics on the Statistics page.
*   RDI pipeline **Start** and **Stop** buttons now correctly reflect component status for newer RDI versions (for example, `flink-collector-source`).
*   LZ4 decompression support for MessagePack-CSharp format, so Redis Insight can correctly display LZ4-compressed MessagePack values.
*   API now returns `4xx` (for example, `400`) for client-side `FT.CREATE` errors instead of `5xx`, improving error handling and monitoring.
*   Bulk delete from **Tree View**: you can delete all keys under a folder or namespace via a delete action on the folder, which opens the **Bulk actions** panel with the pattern pre-filled.
*   **Tutorials**: the open tutorial now shows an open-folder icon instead of the book icon.
*   **String key editor**: the edit area uses the full available space for easier editing.
*   **Copilot**: links in responses no longer overflow the message and insights containers.
*   Docker and store releases are enabled again for this version.

### Bug fixes

*   [#4658](https://github.com/redis/RedisInsight/issues/4658) Implemented fallback to `DEL` when `UNLINK` is unavailable, restoring compatibility with Redis 3.2.12 and similar versions.
*   [#5383](https://github.com/redis/RedisInsight/issues/5383) Fixed default database sorting order so the most recently used databases appear at the top of the list.
*   [#5381](https://github.com/redis/RedisInsight/issues/5381) Restored missing Pub/Sub functionality: message clear option, full message display with line wrapping, and descending chronological order (most recent messages first).
*   [#5382](https://github.com/redis/RedisInsight/issues/5382) Implemented bulk delete for folders in **Tree View**; delete action on a folder opens **Bulk Actions** with the folder pattern pre-filled.

**SHA-512 Checksums**

Package

SHA-512

Windows

+IkHnTZw0saEKT5xYfWFrBEhGOUfc0tP5DygmnpB6r7uFUw42HyATopYr6WsYQrmzAzlhYxgcG61v125WfXR8g==

Linux AppImage

/OugHCsutRHzqaxe3ppS6N5XkpFarZMc+RTro5owjclv+FvfV6gV+NZzEmzB9bUJgHhu5ImB7/2RbKGexXh/Hw==

Linux Debian

CSsxeuwhPwQTCOjuiJDQQZZEWB9wyoERrlGP3Pj8qAyDvk9We0DdpMyLintYwaYPjhyK5KDKHMpu1UEZ/GOh4w==

Linux RPM

Xq0BEuSIsGR/4+QqsSWc/eAawstWZPQqSIj1rT6HqOTJTdp2ovZNZSz85trTMalxf+WJAEmaId3DKHkubEycZQ==

MacOS Intel

FNdl0wn2J5bfKTv9Et6LTtIdNPOIj3WLvh8hrh/VwrA153KHgZxplyLoX6bvazpnyVptSz5vhQVBwP5yYWbYFQ==

MacOS Apple silicon

jgMyLuRFl2suJo/m3cjwrR1I5v5AMEQIY7Xwj0SihTdhlPzM0WYvSHbZyQUoVyx+tE+tnt1CwV/hQIQpRjVZEA==

## On this page
