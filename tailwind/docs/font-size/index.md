---
title: "font-size"
source: "https://tailwindcss.com/docs/font-size"
canonical_url: "https://tailwindcss.com/docs/font-size"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-27T20:07:07.019Z"
content_hash: "b315f446df4564791d7d7306c38625048bf8a5d8f9736c931fbdda46d29a88c7"
menu_path: ["font-size"]
section_path: []
content_language: "en"
---
Typography

Utilities for controlling the font size of an element.

## [Examples](#examples)

### [Basic example](#basic-example)

Use utilities like `text-sm` and `text-lg` to set the font size of an element:

text-sm

The quick brown fox jumps over the lazy dog.

text-base

The quick brown fox jumps over the lazy dog.

text-lg

The quick brown fox jumps over the lazy dog.

text-xl

The quick brown fox jumps over the lazy dog.

text-2xl

The quick brown fox jumps over the lazy dog.

```
<p class="text-sm ...">The quick brown fox ...</p><p class="text-base ...">The quick brown fox ...</p><p class="text-lg ...">The quick brown fox ...</p><p class="text-xl ...">The quick brown fox ...</p><p class="text-2xl ...">The quick brown fox ...</p>
```

### [Setting the line-height](#setting-the-line-height)

Use utilities like `text-sm/6` and `text-lg/7` to set the font size and line-height of an element at the same time:

text-sm/6

So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I _was_ a marine biologist.

text-sm/7

So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I _was_ a marine biologist.

text-sm/8

So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I _was_ a marine biologist.

```
<p class="text-sm/6 ...">So I started to walk into the water...</p><p class="text-sm/7 ...">So I started to walk into the water...</p><p class="text-sm/8 ...">So I started to walk into the water...</p>
```

### [Using a custom value](#using-a-custom-value)

Use the `text-[<value>]` syntax to set the font size based on a completely custom value:

```
<p class="text-[14px] ...">  Lorem ipsum dolor sit amet...</p>
```

For CSS variables, you can also use the `text-(length:<custom-property>)` syntax:

```
<p class="text-(length:--my-text-size) ...">  Lorem ipsum dolor sit amet...</p>
```

This is just a shorthand for `text-[length:var(<custom-property>)]` that adds the `var()` function for you automatically.

### [Responsive design](#responsive-design)

Prefix a `font-size` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="text-sm md:text-base ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

## [Customizing your theme](#customizing-your-theme)

Use the `--text-*` theme variables to customize the font size utilities in your project:

```
@theme {  --text-tiny: 0.625rem; }
```

Now the `text-tiny` utility can be used in your markup:

```
<div class="text-tiny">  <!-- ... --></div>
```

You can also provide default `line-height`, `letter-spacing`, and `font-weight` values for a font size:

```
@theme {  --text-tiny: 0.625rem;  --text-tiny--line-height: 1.5rem;   --text-tiny--letter-spacing: 0.125rem;   --text-tiny--font-weight: 500; }
```

Learn more about customizing your theme in the [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme).
