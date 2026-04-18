---
title: "Agent Skills"
source: "https://trpc.io/docs/skills"
canonical_url: "https://trpc.io/docs/skills"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:58.507Z"
content_hash: "aebc0e629e8e8e87bddba989d1c9c87f63207ba79e618b881536a5ce9fa54a61"
menu_path: ["Agent Skills"]
section_path: []
nav_prev: {"path": "trpc/docs/quickstart/index.md", "title": "Quickstart"}
nav_next: {"path": "trpc/docs/concepts/index.md", "title": "Concepts"}
---

tRPC ships with [TanStack Intent](https://tanstack.com/intent/latest/docs/getting-started/quick-start-consumers) skills to help AI coding agents work with tRPC. When your agent works on a task that matches a skill mapping, the corresponding skill file is automatically loaded into context.

## Setup[​](#setup "Direct link to Setup")

### 1\. Run install[​](#1-run-install "Direct link to 1. Run install")

The `install` command guides your agent through setup:

bash

`npx @tanstack/intent@latest install`

This prints a prompt that instructs your AI agent to configure itself to access the skills shipped in tRPC and your other installed packages.

### 2\. Use skills in your workflow[​](#2-use-skills-in-your-workflow "Direct link to 2. Use skills in your workflow")

When your agent works on a task that matches a mapping, it automatically loads the corresponding `SKILL.md` into context to guide implementation.

### 3\. Keep skills up-to-date[​](#3-keep-skills-up-to-date "Direct link to 3. Keep skills up-to-date")

Skills version with library releases. When you update a library (e.g. `npm update @trpc/server`), the new version brings updated skills automatically. The skills are shipped with the library, so you always get the version that matches your installed code.

To see what skills are available:

bash

`npx @tanstack/intent@latest list`

To check if any skills reference outdated source documentation:

bash

`npx @tanstack/intent@latest stale`

### 4\. Submit feedback (optional)[​](#4-submit-feedback-optional "Direct link to 4. Submit feedback (optional)")

After using a skill, you can submit feedback to help maintainers improve it:

bash

`npx @tanstack/intent@latest meta feedback-collection`

This prints a prompt that guides your agent to collect structured feedback about gaps, errors, and improvements.

## Learn more[​](#learn-more "Direct link to Learn more")

For full documentation on TanStack Intent, see the [Quick Start for Consumers](https://tanstack.com/intent/latest/docs/getting-started/quick-start-consumers) guide.

