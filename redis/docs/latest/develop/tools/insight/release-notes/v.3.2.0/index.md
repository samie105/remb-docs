---
title: "Redis Insight v3.2.0, February 2026"
source: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.3.2.0/"
canonical_url: "https://redis.io/docs/latest/develop/tools/insight/release-notes/v.3.2.0/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:03.429Z"
content_hash: "1de5c9adb01946e70e2bd32ef87334a6f19b2d6a74209c741c8d67a3ad68ab5e"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v3.2.0, February 2026","→","Redis Insight v3.2.0, February 2026"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Client tools","→","Client tools","→\n      \n        Redis Insight","→","Redis Insight","→\n      \n        Redis Insight release notes","→","Redis Insight release notes","→\n      \n        Redis Insight v3.2.0, February 2026","→","Redis Insight v3.2.0, February 2026"]
nav_prev: {"path": "redis/docs/latest/index.md", "title": "Welcome to Redis Docs"}
nav_next: {"path": "redis/docs/latest/commands/redis-8-6-commands/index.md", "title": "Redis 8.6 Commands Reference"}
---

# Redis Insight v3.2.0, February 2026

Redis Insight v3.2.0

## 3.2.0 (February 2026)

This is the General Availability (GA) release of Redis Insight 3.2.0, which includes new features, build updates, and bug fixes.

### Headlines

Connect to Azure Managed Redis with ease. Auto-discover databases across subscriptions with one-click import and connect using Entra ID and Azure passwordless (OAuth) authentication. To get started, follow the [Azure setup guide](https://github.com/RedisInsight/RedisInsight/blob/main/docs/azure-setup.md) to configure the required permissions.

### Details

*   Added support for Azure Managed Redis and Azure Cache for Redis tiers. This support includes auto-discovery of databases across subscriptions with one-click import, Microsoft Entra ID (OAuth) authentication with automatic background token refresh, and multi-account support to switch easily between different Azure accounts.
*   Simplified the build process by removing the Webpack dependency. Vite is used now for both development and production builds.

### Bug fixes

*   [https://github.com/redis/RedisInsight/pull/5504](https://github.com/redis/RedisInsight/pull/5504) Fixed critical security vulnerabilities CVE-2025-55130 (Node.js) and CVE-2025-15467 (OpenSSL) by upgrading the Node.js version and the Alpine base image in Docker.

**SHA-512 Checksums**

Package

SHA-512

Windows

4sgqVLCjqEmg3N9kAQUZXu1ORln9/RJaQazRK0GLJP9PdCoE57DvdLIQ0NWyo2Y7gKaciWnbYSALSYy1aEaWKA==

Linux AppImage

D3yFi8AX4nax/Tf9zighm592PVT3Gh6aQ07uABWOrBdp6gA1ENIleypQzrgOqpGyJ3NXMmNjgzmQCdCGHZUL3g==

Linux Debian

fuCXfh7tlUXQ6gvf/j4mPYG0qH0q94hcIV550ZTyymfSog8CCsxtKJAsySY0mIc+zSBV1nfFfK7qXwKeEmULsw==

Linux RPM

IdxUbf5M2c2nXd8huWhPxD+V331zsjLQ/T9T5KqkTNw+gPXsjCxPEX99Y6WuaWFrLF4iGDHZarByVqFYOIWnFg==

MacOS Intel

6FUSdjAZeqYHg7U+MU8vY4icEwxiA0t14xi8WKh6VVAIf2ZVzjmFt2c4dHqrZuL5moAUJflhOgcZmp5t0xiJpQ==

MacOS Apple silicon

tgtdVOsdph+l3rtq1N83qBwr4Lktz/hkPHpDdFzp0JRSe17Qer04mw8GibL9tyf8eVhJsUSF6dzGovGIq9Mv2A==

## On this page
