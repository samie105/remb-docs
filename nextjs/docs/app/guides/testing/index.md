---
title: "Testing"
source: "https://nextjs.org/docs/app/guides/testing"
canonical_url: "https://nextjs.org/docs/app/guides/testing"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:15:46.587Z"
content_hash: "2c8cc72a7b4596b7de9da3863a079f2914b2e868c56e138b9fc870512cb3d2c3"
menu_path: ["Testing"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/guides/tailwind-v3-css/index.md", "title": "How to install Tailwind CSS v3 in your Next.js application"}
nav_next: {"path": "nextjs/docs/app/guides/testing/cypress/index.md", "title": "How to set up Cypress with Next.js"}
---

# Testing

Last updated April 23, 2026

In React and Next.js, there are a few different types of tests you can write, each with its own purpose and use cases. This page provides an overview of types and commonly used tools you can use to test your application.

## Types of tests[](#types-of-tests)

-   **Unit Testing** involves testing individual units (or blocks of code) in isolation. In React, a unit can be a single function, hook, or component.
-   **Component Testing** is a more focused version of unit testing where the primary subject of the tests is React components. This may involve testing how components are rendered, their interaction with props, and their behavior in response to user events.
-   **Integration Testing** involves testing how multiple units work together. This can be a combination of components, hooks, and functions.
-   **End-to-End (E2E) Testing** involves testing user flows in an environment that simulates real user scenarios, like the browser. This means testing specific tasks (e.g. signup flow) in a production-like environment.
-   **Snapshot Testing** involves capturing the rendered output of a component and saving it to a snapshot file. When tests run, the current rendered output of the component is compared against the saved snapshot. Changes in the snapshot are used to indicate unexpected changes in behavior.

## Async Server Components[](#async-server-components)

Since `async` Server Components are new to the React ecosystem, some tools do not fully support them. In the meantime, we recommend using **End-to-End Testing** over **Unit Testing** for `async` components.

## Guides[](#guides)

See the guides below to learn how to set up Next.js with these commonly used testing tools:

[

### Cypress

Learn how to set up Cypress with Next.js for End-to-End (E2E) and Component Testing.

](/docs/app/guides/testing/cypress)[

### Jest

Learn how to set up Jest with Next.js for Unit Testing and Snapshot Testing.

](/docs/app/guides/testing/jest)[

### Playwright

Learn how to set up Playwright with Next.js for End-to-End (E2E) Testing.

](/docs/app/guides/testing/playwright)[

### Vitest

Learn how to set up Vitest with Next.js for Unit Testing.

](/docs/app/guides/testing/vitest)

Was this helpful?
