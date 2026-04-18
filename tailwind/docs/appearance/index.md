---
title: "appearance"
source: "https://tailwindcss.com/docs/appearance"
canonical_url: "https://tailwindcss.com/docs/appearance"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T17:14:59.030Z"
content_hash: "13171eca81b5337cd75041d7e57f383d56b86554d38aa9a9f5ff4d16d201206f"
menu_path: ["appearance"]
section_path: []
nav_prev: {"path": "tailwind/docs/accent-color/index.md", "title": "accent-color"}
nav_next: {"path": "tailwind/docs/caret-color/index.md", "title": "caret-color"}
---

Utilities for suppressing native form control styling.

Class

Styles

`appearance-none`

`appearance: none;`

`appearance-auto`

`appearance: auto;`

## [Examples](#examples)

### [Removing default appearance](#removing-default-appearance)

Use `appearance-none` to reset any browser specific styling on an element:

Default browser styles applied

Remove default browser styles

```
<select>  <option>Yes</option>  <option>No</option>  <option>Maybe</option></select><div class="grid">  <select class="col-start-1 row-start-1 appearance-none bg-gray-50 dark:bg-gray-800 ...">    <option>Yes</option>    <option>No</option>    <option>Maybe</option>  </select>  <svg class="pointer-events-none col-start-1 row-start-1 ...">    <!-- ... -->  </svg></div>
```

This utility is often used when creating custom form components.

### [Restoring default appearance](#restoring-default-appearance)

Use `appearance-auto` to restore the default browser specific styling on an element:

Try emulating \`forced-colors: active\` in your developer tools to see the difference

Falls back to default appearance

Keeps custom appearance

```
<label>  <div>    <input type="checkbox" class="appearance-none forced-colors:appearance-auto ..." />    <svg class="invisible peer-checked:visible forced-colors:hidden ...">      <!-- ... -->    </svg>  </div>  Falls back to default appearance</label><label>  <div>    <input type="checkbox" class="appearance-none ..." />    <svg class="invisible peer-checked:visible ...">      <!-- ... -->    </svg>  </div>  Keeps custom appearance</label>
```

This is useful for reverting to the standard browser controls in certain accessibility modes.

### [Responsive design](#responsive-design)

Prefix an `appearance` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<select class="appearance-auto md:appearance-none ...">  <!-- ... --></select>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).


