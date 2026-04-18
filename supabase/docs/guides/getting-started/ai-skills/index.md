---
title: "Agent Skills"
source: "https://supabase.com/docs/guides/getting-started/ai-skills"
canonical_url: "https://supabase.com/docs/guides/getting-started/ai-skills"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:52.273Z"
content_hash: "ca740db1adc9ab6463591ca0bdf86e8f59d13ffb835e517fe443a656d097a979"
menu_path: ["Getting started","Getting started","AI Tools","AI Tools","Agent Skills","Agent Skills"]
section_path: ["Getting started","Getting started","AI Tools","AI Tools","Agent Skills","Agent Skills"]
nav_prev: {"path": "supabase/docs/guides/functions/websockets/index.md", "title": "Handling WebSockets"}
nav_next: {"path": "supabase/docs/guides/getting-started/architecture/index.md", "title": "Architecture"}
---

# 

Agent Skills

* * *

Agent Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently. Agents are increasingly capable, but often don't have the context they need to do real work reliably. Skills solve this by giving agents access to procedural knowledge and company-, team-, and user-specific context they can load on demand. Agents with access to a set of skills can extend their capabilities based on the task they're working on.

## Installing skills[#](#installing-skills)

Install all Supabase skills using the skills CLI:

```
1npx skills add supabase/agent-skills
```

To install a specific skill from the repository:

```
1npx skills add supabase/agent-skills --skill SKILL_NAME
```

### Claude Code plugin[#](#claude-code-plugin)

You can also install the skills as Claude Code plugins:

```
1/plugin marketplace add supabase/agent-skills2/plugin install supabase@supabase-agent-skills
```

Skills work with 18+ AI agents including Claude Code, GitHub Copilot, Cursor, Cline, and many others.

## Available skills[#](#available-skills)

Skill

Description

Install command

[supabase](https://github.com/supabase/agent-skills/tree/main/skills/supabase)

Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client libraries and SSR integrations (supabase-js, @supabase/ssr) in Next.js, React, SvelteKit, Astro, Remix; auth issues (login, logout, sessions, JWT, cookies, getSession, getUser, getClaims, RLS); Supabase CLI or MCP server; schema changes, migrations, security audits, Postgres extensions (pg\_graphql, pg\_cron, pg\_vector).

`npx skills add supabase/agent-skills --skill supabase`

[supabase-postgres-best-practices](https://github.com/supabase/agent-skills/tree/main/skills/supabase-postgres-best-practices)

Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations.

`npx skills add supabase/agent-skills --skill supabase-postgres-best-practices`

## Finding more skills[#](#finding-more-skills)

Browse the [skills.sh directory](https://skills.sh) to discover skills from the community. You can also search for skills using the CLI:

```
1npx skills find QUERY
```

## Learn more[#](#learn-more)

*   [Agent Skills Repository](https://github.com/supabase/agent-skills)
*   [Agent Skills Documentation](https://agentskills.io/home)
*   [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

