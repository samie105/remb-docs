---
title: "border-collapse"
source: "https://tailwindcss.com/docs/border-collapse"
canonical_url: "https://tailwindcss.com/docs/border-collapse"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:30:22.712Z"
content_hash: "a955dc1b229c4558ca450495f505116086b482e228f9047838b15b065dc92c65"
menu_path: ["border-collapse"]
section_path: []
content_language: "en"
nav_prev: {"path": "../backdrop-filter-sepia/index.md", "title": "backdrop-filter: sepia()"}
nav_next: {"path": "../border-spacing/index.md", "title": "border-spacing"}
---

## [Examples](#examples)

### [Collapsing table borders](#collapsing-table-borders)

Use the `border-collapse` utility to combine adjacent cell borders into a single border when possible:

| State | City |
| --- | --- |
| Indiana | Indianapolis |
| Ohio | Columbus |
| Michigan | Detroit |

```
<table class="border-collapse border border-gray-400 ...">  <thead>    <tr>      <th class="border border-gray-300 ...">State</th>      <th class="border border-gray-300 ...">City</th>    </tr>  </thead>  <tbody>    <tr>      <td class="border border-gray-300 ...">Indiana</td>      <td class="border border-gray-300 ...">Indianapolis</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Ohio</td>      <td class="border border-gray-300 ...">Columbus</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Michigan</td>      <td class="border border-gray-300 ...">Detroit</td>    </tr>  </tbody></table>
```

Note that this includes collapsing borders on the top-level `<table>` tag.

### [Separating table borders](#separating-table-borders)

Use the `border-separate` utility to force each cell to display its own separate borders:

| State | City |
| --- | --- |
| Indiana | Indianapolis |
| Ohio | Columbus |
| Michigan | Detroit |

```
<table class="border-separate border border-gray-400 ...">  <thead>    <tr>      <th class="border border-gray-300 ...">State</th>      <th class="border border-gray-300 ...">City</th>    </tr>  </thead>  <tbody>    <tr>      <td class="border border-gray-300 ...">Indiana</td>      <td class="border border-gray-300 ...">Indianapolis</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Ohio</td>      <td class="border border-gray-300 ...">Columbus</td>    </tr>    <tr>      <td class="border border-gray-300 ...">Michigan</td>      <td class="border border-gray-300 ...">Detroit</td>    </tr>  </tbody></table>
```

### [Responsive design](#responsive-design)

Prefix a `border-collapse` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<table class="border-collapse md:border-separate ...">  <!-- ... --></table>
```

Learn more about using variants in the [variants documentation](../hover-focus-and-other-states/index.md).
