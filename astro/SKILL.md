## Overview

Astro is a content-driven web framework optimized for performance through server-first rendering and islands architecture. It enables fast, modern sites with partial hydration and framework-agnostic components. An agent needs to know Astro to scaffold projects, manage file-based routing, and optimize interactive islands.

## Mental Model

Astro follows a server-first, content-driven philosophy where pages are built as islands of interactivity in a sea of static HTML. The framework uses file-based routing inside `src/pages/`, `.astro` components for templating, and opt-in client hydration via directives. Canonical pages: `astro/en/concepts/why-astro/index.md`, `astro/en/concepts/islands/index.md`, `astro/en/basics/project-structure/index.md`, `astro/en/basics/astro-components/index.md`.

## Learning Paths

**Getting Started**
1. `astro/en/getting-started/index.md`
2. `astro/en/install-and-setup/index.md`
3. `astro/en/basics/project-structure/index.md`
4. `astro/en/develop-and-build/index.md`

**Building Sites**
1. `astro/en/basics/astro-components/index.md`
2. `astro/en/basics/astro-pages/index.md`
3. `astro/en/basics/layouts/index.md`
4. `astro/en/guides/routing/index.md`
5. `astro/en/guides/content-collections/index.md`

**Production & Architecture**
1. `astro/en/guides/actions/index.md`
2. `astro/en/guides/authentication/index.md`
3. `astro/en/guides/astro-db/index.md`
4. `astro/en/guides/on-demand-rendering/index.md`
5. `astro/en/guides/server-islands/index.md`

## Concept Map

- Fundamentals
  - Getting Started
    - Prerequisites → `astro/en/getting-started/index.md`
    - Installation → `astro/en/install-and-setup/index.md`
    - Manual install → `astro/en/install-and-setup/index.md`
    - Project structure → `astro/en/basics/project-structure/index.md`
  - Core Philosophy
    - Why Astro → `astro/en/concepts/why-astro/index.md`
    - Islands architecture → `astro/en/concepts/islands/index.md`
    - Server islands → `astro/en/guides/server-islands/index.md`
- Building the UI
  - Components
    - Astro components → `astro/en/basics/astro-components/index.md`
    - Framework components → `astro/en/guides/framework-components/index.md`
    - Slots and props → `astro/en/basics/astro-components/index.md`
  - Pages & Navigation
    - Pages → `astro/en/basics/astro-pages/index.md`
    - Layouts → `astro/en/basics/layouts/index.md`
    - Routing → `astro/en/guides/routing/index.md`
- Content & Data
  - Content Systems
    - CMS guides → `astro/en/guides/cms/index.md`
    - Content collections → `astro/en/guides/content-collections/index.md`
    - Fetching data → `astro/en/guides/endpoints/index.md`
  - Integrations
    - Integrating with Astro → `astro/en/guides/framework-components/index.md`
    - MDX → `astro/en/guides/integrations-guide/mdx/index.md`
    - Astro DB → `astro/en/guides/astro-db/index.md`
- Backend & Logic
  - API & Actions
    - Actions → `astro/en/guides/actions/index.md`
    - Endpoints → `astro/en/guides/endpoints/index.md`
    - Authentication → `astro/en/guides/authentication/index.md`
  - Backend Services
    - Appwrite → `astro/en/guides/backend/appwrite/index.md`
    - Firebase → `astro/en/guides/backend/firebase/index.md`
    - Supabase → `astro/en/guides/backend/supabase/index.md`
- Deployment & Operations
  - Build & Deploy
    - Develop and build → `astro/en/develop-and-build/index.md`
    - How to deploy → `astro/en/guides/deploy/index.md`
    - More deployment guides → `astro/en/guides/deploy/index.md`
  - Troubleshooting
    - What went wrong → `astro/en/guides/troubleshooting/index.md`
- Reference & Learning
  - Resources
    - Official resources → `astro/en/astro-courses/index.md`
    - Community resources → `astro/en/contribute/index.md`
    - Astro courses → `astro/en/astro-courses/index.md`
  - Configuration
    - CLI reference → `astro/en/reference/cli-reference/index.md`
    - Directives reference → `astro/en/reference/directives-reference/index.md`
    - Project configuration → `astro/en/basics/project-structure/index.md`
  - Testing Knowledge
    - Test your knowledge → `astro/en/tutorial/0-introduction/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Scaffold a new project | `astro/en/install-and-setup/index.md` |
| Understand project folders | `astro/en/basics/project-structure/index.md` |
| Start the dev server or build | `astro/en/develop-and-build/index.md` |
| Create a reusable UI block | `astro/en/basics/astro-components/index.md` |
| Build a routed page | `astro/en/basics/astro-pages/index.md` |
| Share a page shell | `astro/en/basics/layouts/index.md` |
| Add a React/Vue/Svelte component | `astro/en/guides/framework-components/index.md` |
| Control when JS hydrates | `astro/en/reference/directives-reference/index.md` |
| Handle form submissions | `astro/en/guides/actions/index.md` |
| Add user login | `astro/en/guides/authentication/index.md` |
| Set up a database | `astro/en/guides/astro-db/index.md` |
| Fetch remote data | `astro/en/guides/endpoints/index.md` |
| Manage Markdown/MDX content | `astro/en/guides/integrations-guide/mdx/index.md` |
| Deploy your site | `astro/en/guides/deploy/index.md` |
| Fix a build error | `astro/en/guides/troubleshooting/index.md` |
| Learn by doing | `astro/en/tutorial/0-introduction/index.md` |

## Top Must-Know Pages

1. `astro/en/getting-started/index.md` — Entry point with installation commands and next steps.
2. `astro/en/concepts/why-astro/index.md` — Explains the server-first, content-driven design principles.
3. `astro/en/concepts/islands/index.md` — Defines islands architecture and partial hydration.
4. `astro/en/basics/project-structure/index.md` — Maps directories and files in an Astro project.
5. `astro/en/basics/astro-components/index.md` — Covers the `.astro` component syntax and lifecycle.
6. `astro/en/basics/astro-pages/index.md` — Describes file-based routing and supported page types.
7. `astro/en/guides/routing/index.md` — Details static and dynamic route patterns.
8. `astro/en/guides/actions/index.md` — Shows how to write and call type-safe server actions.
9. `astro/en/guides/astro-db/index.md` — Guides setting up tables and queries with Astro DB.
10. `astro/en/reference/directives-reference/index.md` — Reference for client and server directives.