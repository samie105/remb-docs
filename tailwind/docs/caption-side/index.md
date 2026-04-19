---
title: "caption-side"
source: "https://tailwindcss.com/docs/caption-side"
canonical_url: "https://tailwindcss.com/docs/caption-side"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:21.274Z"
content_hash: "989c0ba782f2b120d133631a7b58c728e9b271bad4a82f4bbc6e0d7b8cfa03c4"
menu_path: ["caption-side"]
section_path: []
nav_prev: {"path": "tailwind/docs/table-layout/index.md", "title": "table-layout"}
nav_next: {"path": "tailwind/docs/transition-property/index.md", "title": "transition-property"}
---

Utilities for controlling the alignment of a caption element inside of a table.

Class

Styles

`caption-top`

`caption-side: top;`

`caption-bottom`

`caption-side: bottom;`

## [Examples](#examples)

### [Placing at top of table](#placing-at-top-of-table)

Use the `caption-top` utility to position a caption element at the top of a table:

Table 3.1: Professional wrestlers and their signature moves.

Wrestler

Signature Move(s)

"Stone Cold" Steve Austin

Stone Cold Stunner, Lou Thesz Press

Bret "The Hitman" Hart

The Sharpshooter

Razor Ramon

Razor's Edge, Fallaway Slam

```
<table>  <caption class="caption-top">    Table 3.1: Professional wrestlers and their signature moves.  </caption>  <thead>    <tr>      <th>Wrestler</th>      <th>Signature Move(s)</th>    </tr>  </thead>  <tbody>    <tr>      <td>"Stone Cold" Steve Austin</td>      <td>Stone Cold Stunner, Lou Thesz Press</td>    </tr>    <tr>      <td>Bret "The Hitman" Hart</td>      <td>The Sharpshooter</td>    </tr>    <tr>      <td>Razor Ramon</td>      <td>Razor's Edge, Fallaway Slam</td>    </tr>  </tbody></table>
```

### [Placing at bottom of table](#placing-at-bottom-of-table)

Use the `caption-bottom` utility to position a caption element at the bottom of a table:

Table 3.1: Professional wrestlers and their signature moves.

Wrestler

Signature Move(s)

"Stone Cold" Steve Austin

Stone Cold Stunner, Lou Thesz Press

Bret "The Hitman" Hart

The Sharpshooter

Razor Ramon

Razor's Edge, Fallaway Slam

```
<table>  <caption class="caption-bottom">    Table 3.1: Professional wrestlers and their signature moves.  </caption>  <thead>    <tr>      <th>Wrestler</th>      <th>Signature Move(s)</th>    </tr>  </thead>  <tbody>    <tr>      <td>"Stone Cold" Steve Austin</td>      <td>Stone Cold Stunner, Lou Thesz Press</td>    </tr>    <tr>      <td>Bret "The Hitman" Hart</td>      <td>The Sharpshooter</td>    </tr>    <tr>      <td>Razor Ramon</td>      <td>Razor's Edge, Fallaway Slam</td>    </tr>  </tbody></table>
```

### [Responsive design](#responsive-design)

Prefix a `caption-side` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<caption class="caption-top md:caption-bottom ...">  <!-- ... --></caption>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).
