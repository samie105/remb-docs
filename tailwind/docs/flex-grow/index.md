---
title: "flex-grow"
source: "https://tailwindcss.com/docs/flex-grow"
canonical_url: "https://tailwindcss.com/docs/flex-grow"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T19:57:13.327Z"
content_hash: "909812deed33508e67a05b9da5e1bef6c3cdac5a99b411bde6b134ecef68ade1"
menu_path: ["flex-grow"]
section_path: []
content_language: "en"
---
[](/)

[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

1.  Flexbox & Grid
2.  flex-grow

Flexbox & Grid

# flex-grow

Utilities for controlling how flex items grow.

| Class | Styles |
| --- | --- |
| `grow` | 
`flex-grow: 1;`

 |
| `grow-<number>` | 

`flex-grow: <number>;`

 |
| `grow-[<value>]` | 

`flex-grow: <value>;`

 |
| `grow-(<custom-property>)` | 

`flex-grow: var(<custom-property>);`

 |

Use `grow` to allow a flex item to grow to fill any available space:

01

02

03

```
<div class="flex ...">  <div class="size-14 flex-none ...">01</div>  <div class="size-14 grow ...">02</div>  <div class="size-14 flex-none ...">03</div></div>
```

Use `grow-<number>` utilities like `grow-3` to make flex items grow proportionally based on their growth factor, allowing them to fill the available space relative to each other:

01

02

03

```
<div class="flex ...">  <div class="size-14 grow-3 ...">01</div>  <div class="size-14 grow-7 ...">02</div>  <div class="size-14 grow-3 ...">03</div></div>
```

Use `grow-0` to prevent a flex item from growing:

01

02

03

```
<div class="flex ...">  <div class="size-14 grow ...">01</div>  <div class="size-14 grow-0 ...">02</div>  <div class="size-14 grow ...">03</div></div>
```

Use the `grow-[<value>]` syntax to set the flex grow factor based on a completely custom value:

```
<div class="grow-[25vw] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `grow-(<custom-property>)` syntax:

```
<div class="grow-(--my-grow) ...">  <!-- ... --></div>
```

This is just a shorthand for `grow-[var(<custom-property>)]` that adds the `var()` function for you automatically.

Prefix a `flex-grow` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="grow md:grow-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](/docs/hover-focus-and-other-states).

### On this page

-   [Quick reference](#quick-reference)
-   [Examples](#examples)
    -   [Allowing items to grow](#allowing-items-to-grow)
    -   [Growing items based on factor](#growing-items-based-on-factor)
    -   [Preventing items from growing](#preventing-items-from-growing)
    -   [Using a custom value](#using-a-custom-value)
    -   [Responsive design](#responsive-design)

[

![Refactoring UI](/_next/static/media/book-promo.3012c0f6.png)

From the creators of Tailwind CSS

Make your ideas look awesome, without relying on a designer.

> “This is the survival kit I wish I had when I started building apps.”
> 
> Derrick Reimer, SavvyCal

](https://www.refactoringui.com/?ref=sidebar)

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
