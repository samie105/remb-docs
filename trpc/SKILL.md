# SKILL.md

## Overview

tRPC is a library for building end-to-end typesafe APIs in TypeScript. It enables seamless communication between client and server by allowing direct invocation of backend functions—typed and validated at compile time, without needing to manually define API schemas or routes. This radically simplifies development and minimizes boilerplate, solving common pains around maintaining consistency, safety, and productivity in API development.

---

## Key Concepts

- **End-to-End Type Safety:** Ensures type correctness across client and server in real time, preventing runtime errors due to type mismatches.
- **RPC (Remote Procedure Call) Model:** Treats API endpoints as callable functions rather than traditional REST routes; you just call functions remotely.
- **Procedure Composition:** Procedures (queries, mutations, subscriptions) are grouped together in routers for modularity and clarity.
- **Minimal Boilerplate:** No need for separate schema definitions or route declarations—types and API are inferred directly from code.
- **AI Agent Skills Integration:** Out-of-the-box support for connecting with AI coding agents for smarter automation and contextual help.

---

## Navigation Guide

- **Intro/Getting Started:**  
  Use [trpc/docs/index.md] and [trpc/docs/quickstart/index.md] for fundamental details, installation, and setup.
- **Conceptual Reference:**  
  [trpc/docs/concepts/index.md] explains the RPC paradigm, procedural architecture, and tRPC’s mindset.
- **AI Agent & Automation:**  
  [trpc/docs/skills/index.md] outlines agent skill mappings for automated developer workflows.
- **Examples & Practical Usage:**  
  [trpc/docs/example-apps/index.md] showcases real app implementations for hands-on learning.
- **API Reference / Advanced Guides:**  
  Look toward section paths and menu paths for deeper configuration and advanced use patterns.

---

## Top Pages & Task Links

1. [Introduction](trpc/docs/index.md)  
   — Library overview, goals, and core value proposition.

2. [Quickstart](trpc/docs/quickstart/index.md)  
   — How to quickly get up and running, basic installation and setup.

3. [Agent Skills](trpc/docs/skills/index.md)  
   — Skills for AI agents integrating with tRPC, automation tips.

4. [Concepts](trpc/docs/concepts/index.md)  
   — RPC explained, procedural architecture, mental model.

5. [Example Apps](trpc/docs/example-apps/index.md)  
   — Links to real-world projects and demos using tRPC, with source references.

---

## Notable Gotchas & Structure Quirks

- **Doc Section Gaps:**  
  The sample includes only high-level documentation. API references, advanced guides, and deeper how-tos are likely in other section paths not shown here. For detailed type, router, or middleware examples, explore beyond menu_path roots as needed.

- **Agent Skills Integration:**  
  tRPC documentation assumes potential use with AI coding agents and references TanStack Intent. When automating tasks, be sure to check [trpc/docs/skills/index.md] for skill mappings and setup requirements.

- **RPC Mindset:**  
  tRPC expects developers to think in terms of functions rather than RESTful endpoints—procedures are called directly, and type safety flows automatically. Reviewing [trpc/docs/concepts/index.md] will help avoid classic API design pitfalls and align your approach.

---

## Additional Navigation & Troubleshooting

- **Common Tasks:**  
  - "How do I create a procedure?": See [trpc/docs/concepts/index.md].
  - "How do I run an example app?": See [trpc/docs/example-apps/index.md].
  - "How do I link an AI agent to tRPC?": See [trpc/docs/skills/index.md].
  - "How do I set up my project?": Start with [trpc/docs/quickstart/index.md].
- **Missing Details?**  
  If a page seems missing, check section paths and menu paths for hidden subsections or advanced documentation.

---

## For Fast Reference

- General intro: [trpc/docs/index.md]
- Setup and installation: [trpc/docs/quickstart/index.md]
- AI agent skills: [trpc/docs/skills/index.md]
- Concepts and mindset: [trpc/docs/concepts/index.md]
- Example projects: [trpc/docs/example-apps/index.md]

---

# End