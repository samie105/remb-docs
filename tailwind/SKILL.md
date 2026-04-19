# Tailwind CSS Agent Skill Guide

## Overview
Tailwind CSS is a utility-first CSS framework that enables developers to rapidly build custom user interfaces by composing small, single-purpose CSS classes directly in their markup. It solves the problem of maintainability and scalability in large projects by reducing the need for bespoke CSS and offering a design system in code.

---

## Key Concepts

- **Utility Classes**: Small, atomic classes for styling (e.g., `px-4`, `text-lg`) allowing developers to compose UI without writing custom CSS ([Styling with utility classes](tailwind/docs/styling-with-utility-classes/index.md)).
- **Variants**: Suffixes that modify utilities based on state (hover, focus) or breakpoints (responsive design), e.g., `md:text-lg`, `hover:bg-blue-500` ([Hover, focus, and other states](tailwind/docs/hover-focus-and-other-states/index.md), [Responsive design](tailwind/docs/responsive-design/index.md)).
- **Theme Customization**: Central design tokens for typography, colors, spacing, etc., customizable in configuration ([Theme variables](tailwind/docs/theme/index.md), [Colors](tailwind/docs/colors/index.md)).
- **Dark Mode**: Built-in support for toggling site themes based on user's OS or preferences ([Dark mode](tailwind/docs/dark-mode/index.md)).
- **Plugin System**: Extend Tailwind with additional utilities, directives, or custom styles ([Adding custom styles](tailwind/docs/adding-custom-styles/index.md), [Functions and directives](tailwind/docs/functions-and-directives/index.md)).
- **Zero-Runtime**: Tailwind generates static CSS at build time, scanning source files for class names ([Detecting classes in source files](tailwind/docs/detecting-classes-in-source-files/index.md)).
- **Preflight**: Tailwind’s opinionated base styles to normalize browser differences ([Preflight](tailwind/docs/preflight/index.md)).

---

## Navigation Guide

### Common Tasks & Relevant Sections
- **Setup/Installation**: [Documentation](tailwind/docs/installation/index.md), [Editor setup](tailwind/docs/editor-setup/index.md), [Compatibility](tailwind/docs/compatibility/index.md).
- **Upgrading**: [Upgrade guide](tailwind/docs/upgrade-guide/index.md).
- **Styling Elements**: Use utility classes. Core reference lives under many pages (see below).
- **States & Responsive**: [Hover, focus, and other states](tailwind/docs/hover-focus-and-other-states/index.md), [Responsive design](tailwind/docs/responsive-design/index.md).
- **Theme/Custom Design**: [Theme variables](tailwind/docs/theme/index.md), [Colors](tailwind/docs/colors/index.md).
- **Dark Mode**: [Dark mode](tailwind/docs/dark-mode/index.md).
- **Extending Tailwind**: [Adding custom styles](tailwind/docs/adding-custom-styles/index.md), [Functions and directives](tailwind/docs/functions-and-directives/index.md).
- **Utility Reference**: All atomic CSS utility classes are documented in individual pages (e.g., [padding](tailwind/docs/padding/index.md)), organized by CSS property or effect.

---

## Top 15 Must-Know Pages

1. [Documentation](tailwind/docs/installation/index.md)
   - Start here: installation, workflow, and general architecture.
2. [Editor setup](tailwind/docs/editor-setup/index.md)
   - Recommended tooling and syntax support for editors.
3. [Compatibility](tailwind/docs/compatibility/index.md)
   - Supported browsers and integration notes.
4. [Upgrade guide](tailwind/docs/upgrade-guide/index.md)
   - Guidance and breaking changes for major version upgrades.
5. [Styling with utility classes](tailwind/docs/styling-with-utility-classes/index.md)
   - Core principle: how to build UIs with Atomic CSS classes.
6. [Hover, focus, and other states](tailwind/docs/hover-focus-and-other-states/index.md)
   - Apply styles conditionally based on user interaction/state.
7. [Responsive design](tailwind/docs/responsive-design/index.md)
   - Adaptive layouts with responsive utility syntax.
8. [Dark mode](tailwind/docs/dark-mode/index.md)
   - Add dark mode support with Tailwind’s variants.
9. [Theme variables](tailwind/docs/theme/index.md)
   - Define and use design tokens (color, spacing, typography).
10. [Colors](tailwind/docs/colors/index.md)
    - Use and customize Tailwind’s built-in color palette.
11. [Adding custom styles](tailwind/docs/adding-custom-styles/index.md)
    - Best practices for extending Tailwind CSS with custom rules.
12. [Detecting classes in source files](tailwind/docs/detecting-classes-in-source-files/index.md)
    - How Tailwind scans and extracts classes during build.
13. [Functions and directives](tailwind/docs/functions-and-directives/index.md)
    - Advanced config and extensions using Tailwind’s custom syntax.
14. [Preflight](tailwind/docs/preflight/index.md)
    - Tailwind’s base CSS reset and normalization layer.
15. [Overflow](tailwind/docs/overflow/index.md) / [grid-auto-flow](tailwind/docs/grid-auto-flow/index.md) / [max-width](tailwind/docs/max-width/index.md) / [font-feature-settings](tailwind/docs/font-feature-settings/index.md)
    - Examples of atomic utility reference pages; use these for exact class API and CSS mappings.

---

## Gotchas & Non-Obvious Structure

- **Utility Class Reference Pages**: Each CSS property or concept is a separate doc, with granular details (e.g., [padding](tailwind/docs/padding/index.md), [margin](tailwind/docs/margin/index.md)). Use these for exact syntax/class lists.
- **Variants and Responsive Utilities**: Look under their dedicated pages for patterns, but the utility reference docs show all supported variants when relevant.
- **Customization**: Configuration and extending Tailwind is covered both in "theme" and in "adding custom styles" pages. When in doubt, check both.
- **Preflight**: Automatically included unless manually disabled; see the [Preflight](tailwind/docs/preflight/index.md) page.
- **Detecting Classes**: Tailwind only generates styles for classes it detects in your source files ([Detecting classes in source files](tailwind/docs/detecting-classes-in-source-files/index.md)). Dynamic class names may require special handling.

---

## How to Find the Right Page

- For **setup, build, or upgrade questions**, start with Getting Started, Editor Setup, Compatibility, and Upgrade Guide.
- For **design or customization**, visit Theme Variables, Colors, or Adding Custom Styles.
- For **specific CSS property utilities** (width, flex, color, grid, filter, etc.), match your CSS property to the respective page (e.g., [width](tailwind/docs/width/index.md), [font-weight](tailwind/docs/font-weight/index.md)).
- For **responsive or interactive styling**, review Responsive Design, and Hover/Focus/State.
- For **troubleshooting build/class problems**, check Detecting Classes in Source Files and Preflight.

---