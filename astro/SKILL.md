# Astro Developer Skill Profile

## Overview

Astro is a modern web framework designed for building fast, content-driven websites—such as blogs, marketing pages, and e-commerce sites—by leveraging static HTML output and partial hydration for dynamic interactivity. Its key innovation, the Islands Architecture, enables minimal JavaScript on the frontend while retaining rich UI features. Astro supports multiple JavaScript frameworks, flexible integrations, and optimized builds for the modern web.

---

## Key Concepts

- **Islands Architecture**: Renders most of the site as static HTML, inserting interactive JS "islands" only where needed for optimal performance ([Islands architecture](astro/en/concepts/islands/index.md)).
- **Pages & Routing**: Pages are file-based within the project; routing is handled automatically via file structure ([Pages](astro/en/basics/astro-pages/index.md), [Routing](astro/en/guides/routing/index.md)).
- **Components**: Astro components (.astro files) and framework components (React, Vue, etc.) are composable and reusable ([Components](astro/en/basics/astro-components/index.md), [Front-end frameworks](astro/en/guides/framework-components/index.md)).
- **Layouts**: Shared page structures managed via layout components ([Layouts](astro/en/basics/layouts/index.md)).
- **Integrations**: Extend Astro's capabilities via official and community integrations ([Working with integrations](astro/en/guides/integrations/index.md)).
- **Markdown & Content Collections**: Structured content management using Markdown, MDX, and collections ([Markdown](astro/en/guides/markdown-content/index.md), [Content collections](astro/en/guides/content-collections/index.md)).
- **Data Fetching & Endpoints**: Fetch external or internal data at build or runtime, with custom serverless endpoints ([Data fetching](astro/en/guides/data-fetching/index.md), [Endpoints](astro/en/guides/endpoints/index.md)).
- **Astro API**: Access build/runtime utilities, rendering context, and project APIs ([Astro API](astro/en/tutorial/5-astro-api/index.md), [Render context](astro/en/reference/api-reference/index.md)).
- **Configuration**: Centralized project configuration via `astro.config.mjs` ([Configuration overview](astro/en/guides/configuring-astro/index.md)).
- **Styling & Assets**: Supports global/local CSS, custom fonts, image optimization, and static assets ([Styles and CSS](astro/en/guides/styling/index.md), [Fonts](astro/en/guides/fonts/index.md), [Images](astro/en/guides/images/index.md)).
- **Deployment**: Deploy Astro sites across various platforms and hosting solutions ([Deployment overview](astro/en/guides/deploy/index.md)).

---

## Navigation Guide

- **Getting Started**: Begin with the tutorial ([Introduction](astro/en/tutorial/0-introduction/index.md)), installation ([Installation](astro/en/install-and-setup/index.md)), and project structure ([Project structure](astro/en/basics/project-structure/index.md)).
- **Core Web App Features**: Find pages, routing, endpoints, and middleware under `/basics/` and `/guides/`.
- **UI & Components**: Use `/basics/astro-components/`, `/basics/layouts/`, and framework guides in `/guides/framework-components/`.
- **Content Management**: Use `/guides/markdown-content/` and `/guides/content-collections/` for static site content.
- **Styling**: CSS, fonts, images, and related customization under `/guides/styling/`, `/guides/fonts/`, `/guides/images/`.
- **Integrations**: Official and third-party integrations under `/guides/integrations/` and `/guides/integrations-guide/`.
- **Deployment**: Platform-specific deployment guides in `/guides/deploy/`.
- **Configuration & API References**: All config, CLI, and API details are central in `/reference/`.
- **Migration & Upgrades**: See `/guides/upgrade-to/` and `/guides/migrate-to-astro/`.
- **Troubleshooting**: Diagnostics and error help under `/guides/troubleshooting/`.
- **Advanced Features**: Experimental APIs and advanced guides in `/reference/experimental-flags/`.
- **Contribute**: Contribution guide under `/contribute/`.

---

## Top Pages & Local Links

1. [Introduction](astro/en/tutorial/0-introduction/index.md)  
   Start here to understand Astro fundamentals via a hands-on blog tutorial.

2. [Installation](astro/en/install-and-setup/index.md)  
   How to set up Astro locally and create your first project.

3. [Project structure](astro/en/basics/project-structure/index.md)  
   Learn the core directory and file conventions of an Astro site.

4. [Why Astro?](astro/en/concepts/why-astro/index.md)  
   Framework goals, philosophy, and its unique value proposition.

5. [Islands architecture](astro/en/concepts/islands/index.md)  
   Deep dive into Astro's signature frontend pattern.

6. [Pages](astro/en/basics/astro-pages/index.md)  
   Create and navigate pages in Astro.

7. [Routing](astro/en/guides/routing/index.md)  
   How routing works; customizing routes and dynamic paths.

8. [Components](astro/en/basics/astro-components/index.md)  
   Fundamentals of Astro components and usage.

9. [Layouts](astro/en/basics/layouts/index.md)  
   Shared page layouts and how to implement them.

10. [Working with integrations](astro/en/guides/integrations/index.md)  
    Add functionality via plugins (SSR, framework support, markdown, etc.).

11. [Front-end frameworks](astro/en/guides/framework-components/index.md)  
    Use React, Vue, Svelte, etc. in Astro projects.

12. [Markdown](astro/en/guides/markdown-content/index.md)  
    Use Markdown or MDX for content pages/blog posts.

13. [Content collections](astro/en/guides/content-collections/index.md)  
    Collection-based content structure, validation, and queries.

14. [Data fetching](astro/en/guides/data-fetching/index.md)  
    Guide for fetching external/internal data at build or runtime.

15. [Endpoints](astro/en/guides/endpoints/index.md)  
    Create serverless functions and API endpoints.

16. [Configuration overview](astro/en/guides/configuring-astro/index.md)  
    All configuration options and patterns.

17. [Styles and CSS](astro/en/guides/styling/index.md)  
    Styling strategies, using CSS, preprocessors, and utility libraries.

18. [Deployment overview](astro/en/guides/deploy/index.md)  
    General deployment guidance and platform-specific links.

19. [Troubleshooting](astro/en/guides/troubleshooting/index.md)  
    Common problems and solutions.

20. [Template expressions reference](astro/en/reference/astro-syntax/index.md)  
    Core syntax and templating cheat sheet.

21. [Render context](astro/en/reference/api-reference/index.md)  
    Access runtime context/API.

22. [CLI Commands](astro/en/reference/cli-reference/index.md)  
    Command-line interface documentation.

---

## Notable Gotchas & Structural Quirks

- **Integrations Split**: General integration info is in [Working with integrations](astro/en/guides/integrations/index.md), but framework-specific (React, Vue, etc.) and platform guides are under `/guides/integrations-guide/`.
- **Migration Guides**: Migration info for popular frameworks (e.g., Next.js, Gatsby, etc.) is organized individually under `/guides/migrate-to-astro/from-*`.
- **API References**: All official Astro modules are under `/reference/modules/`, while advanced/external APIs are grouped by feature (integration, adapter, renderer, etc.).
- **Experimental Features**: New or unstable features live in `/reference/experimental-flags/`; exercise caution.
- **Upgrades**: Versioned upgrade guides are in `/guides/upgrade-to/`; check these before updating Astro versions.
- **Deployment Platforms**: Each hosting platform has its own page under `/guides/deploy/`; platform-specific steps are not centralized.

---

## Quick Task Locator

- **Setup:** [Installation](astro/en/install-and-setup/index.md), [Editor setup](astro/en/editor-setup/index.md)
- **Add a page:** [Pages](astro/en/basics/astro-pages/index.md)
- **Add a component or layout:** [Components](astro/en/basics/astro-components/index.md), [Layouts](astro/en/basics/layouts/index.md)
- **Style your site:** [Styles and CSS](astro/en/guides/styling/index.md)
- **Add a framework (React, Vue, etc.):** [Front-end frameworks](astro/en/guides/framework-components/index.md)
- **Fetch data/API:** [Data fetching](astro/en/guides/data-fetching/index.md), [Endpoints](astro/en/guides/endpoints/index.md)
- **Markdown/blog content:** [Markdown](astro/en/guides/markdown-content/index.md), [Content collections](astro/en/guides/content-collections/index.md)
- **Add plugin/integration:** [Working with integrations](astro/en/guides/integrations/index.md)
- **Deploy:** [Deployment overview](astro/en/guides/deploy/index.md)
- **Troubleshoot or find errors:** [Troubles