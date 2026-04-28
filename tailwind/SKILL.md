## Overview

Tailwind CSS is a utility-first CSS framework that provides low-level, composable classes directly in HTML to build custom designs rapidly. An agent needs to know it because it is the dominant styling layer in modern web stacks, relying on a JIT engine, design tokens, and responsive variants rather than traditional CSS authoring.

## Mental Model

Tailwind replaces hand-written CSS with constrained, single-purpose utility classes generated from a centralized `theme` configuration. Its JIT engine produces styles on demand based on the classes found in your `content` files, while responsive prefixes (`sm:`, `lg:`) and state variants (`hover:`, `focus:`) handle conditional styles without custom media queries or selectors. When defaults are insufficient, arbitrary values and CSS extensions are supported via the same class-based API. Canonical pages: `tailwind/docs/utility-first/index.md`, `tailwind/docs/configuration/index.md`, `tailwind/docs/adding-custom-styles/index.md`.

## Learning Paths

1. **Getting Started** — `tailwind/docs/installation/index.md` → `tailwind/docs/utility-first/index.md` → `tailwind/docs/hover-focus-and-other-states/index.md` → `tailwind/docs/responsive-design/index.md`
2. **Production Ready** — `tailwind/docs/content/index.md` → `tailwind/docs/configuration/index.md` → `tailwind/docs/theme/index.md` → `tailwind/docs/adding-custom-styles/index.md`
3. **Reference Deep-Dive** — `tailwind/docs/flex/index.md` → `tailwind/docs/align-items/index.md` → `tailwind/docs/align-content/index.md` → `tailwind/docs/backdrop-filter/index.md` → `tailwind/docs/aspect-ratio/index.md`

## Concept Map

- Philosophy & Workflow
  - Utility-First: `tailwind/docs/utility-first/index.md`
  - Reusing Styles: `tailwind/docs/reusing-styles/index.md`
  - Handling States: `tailwind/docs/hover-focus-and-other-states/index.md`
  - Responsive Design: `tailwind/docs/responsive-design/index.md`
- Configuration & Theming
  - Content Sources: `tailwind/docs/content/index.md`
  - Configuration File: `tailwind/docs/configuration/index.md`
  - Theme Tokens: `tailwind/docs/theme/index.md`
  - Customizing Your Theme: `tailwind/docs/adding-custom-styles/index.md`
    - Using Arbitrary Values: `tailwind/docs/adding-custom-styles/index.md`
    - Using a Custom Value: `tailwind/docs/adding-custom-styles/index.md`
    - Using Negative Values: `tailwind/docs/margin/index.md`
    - Using Percentages: `tailwind/docs/width/index.md`
    - Using Logical Properties: `tailwind/docs/margin/index.md`
- Layout & Box Model
  - Display: `tailwind/docs/display/index.md`
  - Flexbox: `tailwind/docs/flex/index.md`
    - Align Items: `tailwind/docs/align-items/index.md`
    - Align Content: `tailwind/docs/align-content/index.md`
    - Align Self: `tailwind/docs/align-self/index.md`
      - Auto / Start / Center / End / Stretch: `tailwind/docs/align-self/index.md`
  - Grid: `tailwind/docs/grid-template-columns/index.md`
  - Positioning: `tailwind/docs/position/index.md`
  - Spacing: `tailwind/docs/padding/index.md`, `tailwind/docs/margin/index.md`
  - Sizing: `tailwind/docs/width/index.md`, `tailwind/docs/height/index.md`, `tailwind/docs/aspect-ratio/index.md`
- Visual & Effects
  - Opacity: `tailwind/docs/opacity/index.md`
    - Changing the Opacity: `tailwind/docs/opacity/index.md`
  - Shadows: `tailwind/docs/box-shadow/index.md`
    - Setting the Shadow Color: `tailwind/docs/box-shadow/index.md`
  - Filters: `tailwind/docs/filter/index.md`
    - Backdrop Filters: `tailwind/docs/backdrop-filter/index.md`
      - Blur: `tailwind/docs/backdrop-filter-blur/index.md`
      - Brightness: `tailwind/docs/backdrop-filter-brightness/index.md`
      - Contrast: `tailwind/docs/backdrop-filter-contrast/index.md`
      - Grayscale: `tailwind/docs/backdrop-filter-grayscale/index.md`
      - Invert: `tailwind/docs/backdrop-filter-invert/index.md`
      - Opacity: `tailwind/docs/backdrop-filter-opacity/index.md`
      - Saturate: `tailwind/docs/backdrop-filter-saturate/index.md`
      - Sepia: `tailwind/docs/backdrop-filter-sepia/index.md`
  - Blend Modes: `tailwind/docs/background-blend-mode/index.md`
- Color & Typography
  - Text Color: `tailwind/docs/text-color/index.md`
  - Background Color: `tailwind/docs/background-color/index.md`
  - Accent Color: `tailwind/docs/accent-color/index.md`
  - Font Size: `tailwind/docs/font-size/index.md`
  - Font Weight: `tailwind/docs/font-weight/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Install or set up Tailwind | `tailwind/docs/installation/index.md` |
| Learn the utility-first mindset | `tailwind/docs/utility-first/index.md` |
| Configure content paths for the JIT engine | `tailwind/docs/content/index.md` |
| Customize default theme tokens | `tailwind/docs/theme/index.md` |
| Add arbitrary values or custom CSS | `tailwind/docs/adding-custom-styles/index.md` |
| Handle hover, focus, and other states | `tailwind/docs/hover-focus-and-other-states/index.md` |
| Build responsive layouts | `tailwind/docs/responsive-design/index.md` |
| Control flexbox alignment | `tailwind/docs/align-items/index.md` |
| Apply backdrop visual effects | `tailwind/docs/backdrop-filter/index.md` |
| Set aspect ratio on media | `tailwind/docs/aspect-ratio/index.md` |
| Use negative spacing or inset values | `tailwind/docs/margin/index.md` |
| Apply logical property variants | `tailwind/docs/margin/index.md` |
| Adjust element opacity | `tailwind/docs/opacity/index.md` |
| Customize shadow colors | `tailwind/docs/box-shadow/index.md` |

## Top Must-Know Pages

1. `tailwind/docs/installation/index.md` — Set up Tailwind in your project and configure the content paths that drive the JIT engine.
2. `tailwind/docs/utility-first/index.md` — Learn the core philosophy of styling with composable, single-purpose utility classes instead of custom CSS.
3. `tailwind/docs/responsive-design/index.md` — Master breakpoint prefixes like `sm:` and `lg:` to build adaptive layouts without writing media queries.
4. `tailwind/docs/hover-focus-and-other-states/index.md` — Apply conditional styles for hover, focus, disabled, and other interactive states directly in class strings.
5. `tailwind/docs/adding-custom-styles/index.md` — Extend the framework with arbitrary values, arbitrary properties, and custom theme overrides.
6. `tailwind/docs/configuration/index.md` — Understand the `tailwind.config.js` structure to control theme tokens, variants, and plugins.
7. `tailwind/docs/content/index.md` — Define which files the JIT engine should scan to ensure all used utilities are generated.
8. `tailwind/docs/flex/index.md` — Control flex container behavior including direction, wrapping, and ordering of child items.
9. `tailwind/docs/align-items/index.md` — Align flex and grid items along the cross axis using utilities like `items-center` and `items-stretch`.
10. `tailwind/docs/backdrop-filter/index.md` — Apply background blur, brightness, and other backdrop effects to elements overlapping content.