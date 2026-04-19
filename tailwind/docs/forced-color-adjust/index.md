---
title: "forced-color-adjust"
source: "https://tailwindcss.com/docs/forced-color-adjust"
canonical_url: "https://tailwindcss.com/docs/forced-color-adjust"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:19:05.397Z"
content_hash: "4659759cf1bad6d74adb74ceb44bc3de678ec9c91a55771737ac246369bd68df"
menu_path: ["forced-color-adjust"]
section_path: []
nav_prev: {"path": "tailwind/docs/stroke-width/index.md", "title": "stroke-width"}
nav_next: {"path": "tailwind/docs/installation/using-vite/index.md", "title": "Get started with Tailwind CSS"}
---

Utilities for opting in and out of forced colors.

Class

Styles

`forced-color-adjust-auto`

`forced-color-adjust: auto;`

`forced-color-adjust-none`

`forced-color-adjust: none;`

## [Examples](#examples)

### [Opting out of forced colors](#opting-out-of-forced-colors)

Use the `forced-color-adjust-none` utility to opt an element out of the colors enforced by forced colors mode. This is useful in situations where enforcing a limited color palette will degrade usability.

Try emulating \`forced-colors: active\` in your developer tools to see the changes

![Two each of gray, white, and black shirts laying flat.](/_next/static/media/t-shirt.250cd197.jpg)

Basic Tee

$35

```
<form>  <img src="/img/shirt.jpg" />  <div>    <h3>Basic Tee</h3>    <h3>$35</h3>    <fieldset>      <legend class="sr-only">Choose a color</legend>      <div class="forced-color-adjust-none ...">        <label>          <input class="sr-only" type="radio" name="color-choice" value="White" />          <span class="sr-only">White</span>          <span class="size-6 rounded-full border border-black/10 bg-white"></span>        </label>        <!-- ... -->      </div>    </fieldset>  </div></form>
```

You can also use the [forced colors variant](tailwind/docs/hover-focus-and-other-states/index.md#forced-colors) to conditionally add styles when the user has enabled a forced color mode.

### [Restoring forced colors](#restoring-forced-colors)

Use the `forced-color-adjust-auto` utility to make an element adhere to colors enforced by forced colors mode:

```
<form>  <fieldset class="forced-color-adjust-none lg:forced-color-adjust-auto ...">    <legend>Choose a color:</legend>    <select class="hidden lg:block">      <option value="White">White</option>      <option value="Gray">Gray</option>      <option value="Black">Black</option>    </select>    <div class="lg:hidden">      <label>        <input class="sr-only" type="radio" name="color-choice" value="White" />        <!-- ... -->      </label>      <!-- ... -->    </div>  </fieldset></form>
```

This can be useful if you want to undo the `forced-color-adjust-none` utility, for example on a larger screen size.

### [Responsive design](#responsive-design)

Prefix a `forced-color-adjust` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<div class="forced-color-adjust-none md:forced-color-adjust-auto ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).
