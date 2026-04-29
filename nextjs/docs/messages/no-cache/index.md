---
title: "No Cache Detected"
source: "https://nextjs.org/docs/messages/no-cache"
canonical_url: "https://nextjs.org/docs/messages/no-cache"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:17:38.796Z"
content_hash: "69017274a09a42a0eb922757eb041bd656acf5172293ae487ae63560bd3845cd"
menu_path: ["No Cache Detected"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../no-before-interactive-script-outside-document/index.md", "title": "No Before Interactive Script Outside Document"}
nav_next: {"path": "../no-css-tags/index.md", "title": "No CSS Tags"}
---

# No Cache Detected

## Why This Error Occurred[](#why-this-error-occurred)

A Next.js build was triggered in a continuous integration environment, but no cache was detected.

This results in slower builds and can hurt Next.js' filesystem cache of client-side bundles across builds.

## Possible Ways to Fix It[](#possible-ways-to-fix-it)

> **Note**: If this is a new project, or being built for the first time in your CI, you can ignore this error. However, you'll want to make sure it doesn't continue to happen and fix it if it does!

Follow the instructions in [CI Build Caching](/docs/pages/guides/ci-build-caching) to ensure your Next.js cache is persisted between builds.

Was this helpful?
