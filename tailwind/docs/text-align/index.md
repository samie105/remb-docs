---
title: "text-align"
source: "https://tailwindcss.com/docs/text-align"
canonical_url: "https://tailwindcss.com/docs/text-align"
docset: "tailwind"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:13.175Z"
content_hash: "5f05034244a13252e5466433c158004af1c034c449384f3468d3717946642d0e"
menu_path: ["text-align"]
section_path: []
nav_prev: {"path": "tailwind/docs/list-style-type/index.md", "title": "list-style-type"}
nav_next: {"path": "tailwind/docs/color/index.md", "title": "color"}
---

Utilities for controlling the alignment of text.

Class

Styles

`text-left`

`text-align: left;`

`text-center`

`text-align: center;`

`text-right`

`text-align: right;`

`text-justify`

`text-align: justify;`

`text-start`

`text-align: start;`

`text-end`

`text-align: end;`

## [Examples](#examples)

### [Left aligning text](#left-aligning-text)

Use the `text-left` utility to left align the text of an element:

So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I _was_ a marine biologist.

```
<p class="text-left">So I started to walk into the water...</p>
```

### [Right aligning text](#right-aligning-text)

Use the `text-right` utility to right align the text of an element:

So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I _was_ a marine biologist.

```
<p class="text-right">So I started to walk into the water...</p>
```

### [Centering text](#centering-text)

Use the `text-center` utility to center the text of an element:

So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I _was_ a marine biologist.

```
<p class="text-center">So I started to walk into the water...</p>
```

### [Justifying text](#justifying-text)

Use the `text-justify` utility to justify the text of an element:

So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I _was_ a marine biologist.

```
<p class="text-justify">So I started to walk into the water...</p>
```

### [Using logical properties](#using-logical-properties)

Use the `text-start` and `text-end` utilities, which use [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts) to map to either the left or right side based on the text direction:

بدأتُ أسير نحو الماء. لن أكذب عليكم يا رفاق، كنتُ مرعوبًا. لكنني واصلتُ المسير، وبينما كنتُ أشق طريقي عبر الأمواج، غمرني هدوءٌ غريب. لا أعلم إن كان ذلك تدخّلًا إلهيًا أم صلة قرابة بين جميع الكائنات الحية، لكنني أقول لك يا جيري، في تلك اللحظة، كنتُ عالم أحياء بحرية.

```
<div dir="rtl" lang="ar">  <p class="text-end">فبدأت بالسير نحو الماء...</p></div>
```

### [Responsive design](#responsive-design)

Prefix a `text-align` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
<p class="text-left md:text-center ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](tailwind/docs/hover-focus-and-other-states/index.md).

