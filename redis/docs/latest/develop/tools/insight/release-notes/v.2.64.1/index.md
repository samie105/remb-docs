---
title: "Redis Insight v2.64.1, December 2024"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.64.1/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.64.1/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:58.175Z"
content_hash: "283c7e04213bbe5a511f30b2aa08c0b289f423909673b6f61b24d15b4fce5f8e"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.64.1, December 2024","→","Redis Insight v2.64.1, December 2024"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v2.64.1, December 2024","→","Redis Insight v2.64.1, December 2024"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.64.0/index.md", "title": "Redis Insight v2.64.0, December 2024"}
nav_next: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.66.0/index.md", "title": "Redis Insight v2.66.0, January 2025"}
---

# Redis Insight v2.64.1, December 2024

Redis Insight v2.64.1

## 2.64.1 (December 2024)

This is a maintenance release for Redis Insight 2.64.

Update urgency: `HIGH`: There is a critical bug that may affect a subset of users. Upgrade!

### Details

*   [#4236](https://github.com/RedisInsight/RedisInsight/pull/4236) Reverts the change to use JSONPath ($) by default rather than (.). These changes could cause issues with shards in Redis Software Active-Active databases.

**SHA-256 Checksums**

Package

SHA-256

Windows

hIK4qrC50Gd4jZnpHnwRIIVyDWtOfvfFID9nv8xfdcDgf4LvJcGLa9zVYkbfvwUv+aEaaBCohJJZMIGFC6iYHQ==

Linux AppImage

ll999oWjvKppawlYBPN6phGNa+mDiWmefIvkbQNAd7JPZFbHTYuLFWMWo4F1NrnZlr6vnPF6awbu7ubbiZL0HA==

Linux Debian

4MKHfmmapfhxXUln0X+rpFXzm2dH6IPj2BIwlNRPQDGhpQ5flzOtLlV1iNGm9xqennZUv+hx+cVQodzPIj8FTw==

MacOS Intel

5FkllEVCbD9M1fYww7N6XT3Qknl5tWrkHKWQWGhjkUiR/nZ89u+A84UzynB5H/lzBCFwUWJidfGJ4akrX2J7Hg==

MacOS Apple silicon

2gWxZqGlAo0RyQKa0h8puyXMkIg1vF/Gobd9vS9DNWZMr3aYJojALx6f7pfknBoL7MDmZI29Mohtx4mnQPbjGQ==

## On this page
