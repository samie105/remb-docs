```markdown
# Next.js SKILL.md

## 1. What is Next.js and What Problems It Solves

Next.js is a React framework for building production-grade web applications that support server-side rendering (SSR), static site generation (SSG), and hybrid rendering strategies. It simplifies routing, data fetching, and performance optimization out of the box. It is designed to help developers build fast, scalable, SEO-friendly, and performant web apps with minimal configuration.

Problems solved include:  
- Managing routing with file-system conventions  
- Enabling SSR and SSG with caching and revalidation  
- Automatic code splitting and image/font optimization  
- Seamless handling of server and client components  
- Simplified data fetching and mutation patterns  
- Comprehensive configuration for deployment, caching, security, and internationalization  

---

## 2. Structure of the Official Next.js Documentation

The docs are subdivided into major areas reflecting developer workflows:

### 2.1 Getting Started  
- Introduction and installation  
- Project structure and app-router basics  
- Page layout and routing setup  
- Linking/navigation in apps  
- Server/client component differences  
- Core data management: fetching, mutating, caching, revalidation  
- Styling approaches (CSS, CSS-in-JS, Sass, Tailwind)  
- Media optimization (images, fonts, metadata)  
- Error handling and advanced routing (route handlers, proxy)  
- Deployment and upgrading guides  

### 2.2 Guides  
- Deeper, topic-focused tutorials such as authentication, analytics, caching strategies, debugging, deployment targets, environment vars, forms, internationalization, etc.  
- Migration guides for moving from older Next.js versions and other tools  
- Testing guidance with various tools (Jest, Cypress, Playwright, Vitest)  
- Optimization and production checklists  
- Progressive web apps, view transitions, SSR philosophies  

### 2.3 API Reference  
- Detailed config options (next.config.js settings)  
- File-system conventions for app and pages router (e.g., layout.js, page.js, route files, metadata files, segment configs)  
- React hooks and utility functions (`useRouter`, `useParams`, `revalidatePath`, etc.)  
- Components provided by Next.js (`Image`, `Font`, `Link`, `Script`, `Form`)  
- Server functions to control caching, redirects, responses (`redirect()`, `notFound()`, `cookies()`)  
- Directives to annotate components and modules (e.g., `use client`, `use server`, caching directives)  

---

## 3. How to Navigate These Docs to Answer Common Developer Questions

- **Begin with “Getting Started”** to understand core concepts like routing, components, and data handling in modern Next.js apps using the App Router.  
- For **framework configuration or customization**, head to the API Reference > Configuration > `next.config.js`. This section breaks down every available config option with examples.  
- When needing **file-level conventions** (how to name files like `layout.js`, `page.js`, dynamic routes), consult API Reference > File-system conventions. This is essential for understanding routing and layout nesting.  
- For **data fetching and caching strategies**, explore “Fetching Data”, “Mutating Data”, “Caching”, and “Revalidating” under Getting Started, then cross-check Guides for advanced use cases like ISR and CDN caching.  
- For dealing with **routing nuances and error handling**, check both Getting Started and API Reference for route handlers, intercepting routes, and error.js handling patterns.  
- To understand **React hooks and utilities specific to Next.js**, search under API Reference > Functions for detailed usage and returned values (e.g., `useRouter`, `useParams`).  
- For **deployment or platform-specific concerns**, guides like “Deploying to Platforms” and “Production Checklist” are the go-to resources.  
- Use the **search or URL patterns** to jump directly to topics in API Reference when precise config options, functions, or directives are required.  

---

## 4. Most Important Pages / Concepts for an AI Agent to Know

- **Getting Started Essentials:**  
  - [Installation](https://nextjs.org/docs/app/getting-started/installation)  
  - [Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)  
  - [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)  
  - [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)  
  - [Fetching and Mutating Data](https://nextjs.org/docs/app/getting-started/fetching-data), [Caching](https://nextjs.org/docs/app/getting-started/caching)  
  - [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling)  

- **API Reference Highlights:**  
  - **File-system Conventions:** `page.js`, `layout.js`, `route.js`, `error.js`, dynamic routes, intercepting routes  
  - **Configuration (`next.config.js`)** including caching, redirects, image optimization, environment variables  
  - **Functions:** `redirect()`, `notFound()`, `fetch()`, `revalidatePath()`, `cookies()`  
  - **Directives:** `use client`, `use server`, `use cache` variants  
  - **Components:** `Image`, `Link`, `Font`, `Script`, `Form`  

- **Guides:**  
  - Authentication, Analytics, Deployment, Internationalization, Testing  
  - Migration paths and upgrading guides  
  - Rendering Philosophy and App Router deep dives  

---

## 5. Gotchas and Non-Obvious Things in the Docs Structure

- **Separation Between App Router and Pages Router:**  
  Most modern docs focus on the `/app` router (new paradigm), but some legacy or alternative docs refer to the `/pages` router. Pay attention to the folder context.  
- **File-system conventions are central and extensive:**  
  Many features rely on special file names with structured meaning (e.g., `layout.js` provides nested layouts). Understanding this mapping is critical for routing and rendering questions.  
- **Multiple caching layers and strategies:**  
  Caching is addressed in multiple places — “Caching” under Getting Started, and more advanced guides like “CDN Caching,” “CI Build Caching” etc. Differentiate between Cache Components, Cache Handlers, and cache control functions.  
- **Directives like `use client` and `use server` influence component behavior significantly:**  
  These are sprinkled through API reference and are essential to understanding React component boundaries in Next.js apps.  
- **Metadata files and their special treatment:**  
  App icons, sitemaps, robots.txt, and OpenGraph images are configured via file-system conventions with special filenames.  
- **Overlapping config options in next.config.js:**  
  The config section is very detailed; some settings appear similar (e.g., `cacheLife` vs `cacheHandler`), requiring contextual understanding.  
- **Hybrid nature of the framework:**  
  Next.js mixes server and client code in the same codebase; docs reflect this by separating client/server components, hooks, and APIs. Context is key to avoid confusion.  

---

# Summary

To efficiently answer dev questions about Next.js:  
- Start at “Getting Started” for core concepts  
- Use API Reference to deep dive on files, config, functions, components, and directives  
- Reference guides for specialized topics, migrations, and best practices  
- Mind the app vs pages router context and file conventions as foundational to Next.js  
- Understand caching and rendering strategies are spread across multiple sections and require careful interpretation  

This skill foundation enables the AI agent to parse developer intents, navigate the extensive and feature-rich docs, and produce precise, context-aware guidance.
```