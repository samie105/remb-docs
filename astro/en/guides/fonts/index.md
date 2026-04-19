---
title: "Using custom fonts"
source: "https://docs.astro.build/en/guides/fonts/"
canonical_url: "https://docs.astro.build/en/guides/fonts/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:27.504Z"
content_hash: "983c3cdd162d9863fe85a987c41321557c7dc35a1113e64f375a9d0afe9843ac"
menu_path: ["Using custom fonts"]
section_path: []
nav_prev: {"path": "astro/en/guides/styling/index.md", "title": "Styles and CSS"}
nav_next: {"path": "astro/en/guides/syntax-highlighting/index.md", "title": "Syntax Highlighting"}
---

# Using custom fonts

This guide will show you how to add [web fonts](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts) to your project and use them in your components.

Astro provides a way to use fonts from your filesystem and various font providers (e.g. Fontsource, Google) through a unified, [fully customizable](/en/reference/configuration-reference/#fonts), and type-safe API.

Web fonts can impact page performance at both load time and rendering time. This API helps you keep your site performant with automatic [web font optimizations](https://web.dev/learn/performance/optimize-web-fonts) including preload links, optimized fallbacks, and opinionated defaults. [See common usage examples](#examples).

The Fonts API focuses on performance and privacy by downloading and caching fonts so they’re served from your site. This can avoid sending user data to third-party sites, and also ensures that a consistent set of fonts is available to all your visitors.

## Configuring custom fonts

[Section titled “Configuring custom fonts”](#configuring-custom-fonts)

Registering custom fonts for your Astro project is done through [the `fonts` option](/en/reference/configuration-reference/#fonts) in your Astro config.

For each font you want to use, you must specify its [name](/en/reference/configuration-reference/#fontname), a [CSS variable](/en/reference/configuration-reference/#fontcssvariable), and an Astro font provider.

Astro provides [built-in support for the most popular font providers](/en/reference/font-provider-reference/#built-in-providers): Adobe, Bunny, Fontshare, Fontsource, Google, Google Icons and NPM, as well as for using your own local font files. Additionally, you can [further customize your font configuration](#granular-font-configuration) to optimize performance and visitor experience.

### Using a local font file

[Section titled “Using a local font file”](#using-a-local-font-file)

This example will demonstrate adding a custom font using the font file `DistantGalaxy.woff2`.

1.  Add your font file inside the [`src/` directory](/en/basics/project-structure/#src), for example `src/assets/fonts/`.
    
2.  Create a new font family in your Astro config file using the [local font provider](/en/reference/font-provider-reference/#local) and specify the variants to be included:
    
    ```
    import { defineConfig, fontProviders } from "astro/config";
    export default defineConfig({  fonts: [{    provider: fontProviders.local(),    name: "DistantGalaxy",    cssVariable: "--font-distant-galaxy",    options: {      variants: [{        src: ['./src/assets/fonts/DistantGalaxy.woff2'],        weight: 'normal',        style: 'normal'      }]    }  }]});
    ```
    
3.  Your font is now configured and ready to be [added to your page head](#applying-custom-fonts) so that it can be used in your project.
    

### Using Fontsource

[Section titled “Using Fontsource”](#using-fontsource)

Astro supports [several font providers](/en/reference/font-provider-reference/#built-in-providers) out of the box, including support for [Fontsource](https://fontsource.org/) that simplifies using Google Fonts and other open-source fonts.

The following example will use Fontsource to add custom font support, but the process is similar for any of Astro’s built-in font providers (e.g. [Adobe](https://fonts.adobe.com/), [Bunny](https://fonts.bunny.net/)).

1.  Find the font you want to use in [Fontsource’s catalog](https://fontsource.org/). This example will use [Roboto](https://fontsource.org/fonts/roboto).
    
2.  Create a new font family in your Astro config file using the [Fontsource provider](/en/reference/font-provider-reference/#fontsource):
    
    ```
    import { defineConfig, fontProviders } from "astro/config";
    export default defineConfig({  fonts: [{    provider: fontProviders.fontsource(),    name: "Roboto",    cssVariable: "--font-roboto",  }]});
    ```
    
3.  Your font is now configured and ready to be [added to your page head](#applying-custom-fonts) so that it can be used in your project.
    

## Applying custom fonts

[Section titled “Applying custom fonts”](#applying-custom-fonts)

After [a font is configured](#configuring-custom-fonts), it must be added to your page head with an identifying CSS variable. Then, you can use this variable when defining your page styles.

1.  Import and include the [`<Font />`](/en/reference/modules/astro-assets/#font-) component with the required `cssVariable` property in the head of your page, usually in a dedicated `Head.astro` component or in a [layout](/en/basics/layouts/) component directly:
    
    ```
    ---import { Font } from "astro:assets";---
    <html>  <head>    <Font cssVariable="--font-distant-galaxy" />  </head>  <body>    <slot />  </body></html>
    ```
    
2.  In any page rendered with that layout, including the layout component itself, you can now define styles with your font’s `cssVariable` to apply your custom font.
    
    In the following example, the `<h1>` heading will have the custom font applied, while the paragraph `<p>` will not.
    
    ```
    ---import Layout from "../layouts/Layout.astro";---<Layout>  <h1>In a galaxy far, far away...</h1>
      <p>Custom fonts make my headings much cooler!</p>
      <style>  h1 {    font-family: var(--font-distant-galaxy);  }  </style></Layout>
    ```
    

## Preloading fonts

[Section titled “Preloading fonts”](#preloading-fonts)

Font preloading should be done sparingly, as it can block the loading of other important resources or download fonts that are unnecessary for the current page. Consider preloading only the most essential fonts, necessary for displaying content visible above the fold.

To preload a font, pass the [`preload` property](/en/reference/modules/astro-assets/#preload) to the corresponding `<Font />` component. If multiple files correspond to a font, you can also specify which one to preload by passing an array.

```
---import { Font } from "astro:assets";---
<html>  <head>    <Font cssVariable="--font-distant-galaxy" preload />  </head>  <body>    <slot />  </body></html>
```

## Register fonts in Tailwind

[Section titled “Register fonts in Tailwind”](#register-fonts-in-tailwind)

If you are using [Tailwind](/en/guides/styling/#tailwind) for styling, you will not apply your styles with the `font-face` CSS property.

Instead, after [configuring your custom font](#configuring-custom-fonts) and [adding it to your page head](#applying-custom-fonts), you will need to update your Tailwind configuration to register your font:

*   [Tailwind CSS 4.0](#tab-panel-1627)
*   [Tailwind CSS 3.0](#tab-panel-1628)

```
@import "tailwindcss";
@theme inline {  --font-sans: var(--font-roboto);}
```

See [Tailwind’s docs on adding custom font families](https://tailwindcss.com/docs/font-family#using-a-custom-value) for more information.

## Using variable fonts

[Section titled “Using variable fonts”](#using-variable-fonts)

To use [variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide) in your project, specify the available weight range instead of individual weights in your provider’s configuration.

*   [Local provider](#tab-panel-1629)
*   [Other providers](#tab-panel-1630)

When [using a local font file](#using-a-local-font-file), you can specify that the font is variable by setting the [`weight` property of the variant](/en/reference/font-provider-reference/#weight) to a string corresponding to the exact weight range available for the font.

The following example configures Inter as a local variable font with the available weight range:

```
import { defineConfig, fontProviders } from "astro/config";
export default defineConfig({  fonts: [{    provider: fontProviders.local(),    name: "Inter",    cssVariable: "--font-inter",    options: {      variants: [        {          weight: "100 900",          style: "normal",          src: ["./src/assets/fonts/InterVariable.woff2"],        },      ],    },  }]});
```

## Customizing font fallbacks

[Section titled “Customizing font fallbacks”](#customizing-font-fallbacks)

Fallback fonts are used when the primary font has not yet loaded, contains missing characters, or cannot be loaded for any reason. When the fallback font differs significantly from the primary font, layout shifts may occur during page loading.

To avoid this, Astro automatically tries to generate optimized fallback fonts from the last [defined fallback](/en/reference/configuration-reference/#fontfallbacks) if it is a [generic font family](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#generic-name). It uses `sans-serif` by default, but it may not match the desired appearance of your primary font. You can adjust it in your font configuration:

```
import { defineConfig, fontProviders } from "astro/config";
export default defineConfig({  fonts: [{    provider: fontProviders.fontsource(),    name: "Cousine",    cssVariable: "--font-cousine",    fallbacks: ["monospace"]  }]});
```

You can also opt out of the default optimization by setting [`font.optimizedFallbacks`](/en/reference/configuration-reference/#fontoptimizedfallbacks) to `false` in your font configuration. Astro will then use the fallback fonts specified in your configuration without any additional automatic processing.

## Accessing font data programmatically

[Section titled “Accessing font data programmatically”](#accessing-font-data-programmatically)

Astro exposes a low-level API for accessing font family data programmatically through the [`fontData`](/en/reference/modules/astro-assets/#fontdata) object. This can be useful for advanced use cases where you need direct access to font files, such as generating OpenGraph images with [Satori](https://github.com/vercel/satori) in an [API Route](/en/guides/endpoints/#server-endpoints-api-routes).

This low-level API gives you access to all font files downloaded by Astro for your project, along with their metadata. This means that you are responsible for filtering font files to find the specific file you need, and for resolving the file path to use based on the build output structure.

The following example generates an OpenGraph image in a static file endpoint, assuming that only [one font and its format have been configured](/en/reference/configuration-reference/#fontformats) with a [format supported by Satori](https://github.com/vercel/satori?tab=readme-ov-file#fonts):

```
import type { APIRoute } from "astro";import { fontData } from "astro:assets";import { outDir } from "astro:config/server";import { readFile } from "node:fs/promises";import satori from "satori";import { html } from "satori-html";import sharp from "sharp";
export const GET: APIRoute = async (context) => {  const fontPath = fontData["--font-roboto"][0]?.src[0]?.url;
  if (fontPath === undefined) {    throw new Error("Cannot find the font path.");  }
  const data = import.meta.env.DEV    ? await fetch(new URL(fontPath, context.url.origin)).then(async (res) => res.arrayBuffer())    : await readFile(new URL(`.${fontPath}`, outDir));
  const svg = await satori(    html`<div style="color: black;">hello, world</div>`,    {      width: 600,      height: 400,      fonts: [        {          name: "Roboto",          data,          weight: 400,          style: "normal",        },      ],    },  );
  const pngBuffer = await sharp(Buffer.from(svg))    .resize(600, 400)    .png()    .toBuffer();
  return new Response(new Uint8Array(pngBuffer), {    headers: {      "Content-Type": "image/png",    },  });};
```

## Granular font configuration

[Section titled “Granular font configuration”](#granular-font-configuration)

A font family is defined by a combination of properties such as weights and styles (e.g. `weights: [500, 600]` and `styles: ["normal", "bold"]`), but you may want to download only certain combinations of these.

For greater control over which font files are downloaded, you can specify the same font (ie. with the same `cssVariable`, `name`, and `provider` properties) multiple times with different combinations. Astro will merge the results and download only the required files. For example, it is possible to download normal `500` and `600` while downloading only italic `500`:

```
import { defineConfig, fontProviders } from "astro/config";
export default defineConfig({  fonts: [    {      name: "Roboto",      cssVariable: "--roboto",      provider: fontProviders.google(),      weights: [500, 600],      styles: ["normal"]    },    {      name: "Roboto",      cssVariable: "--roboto",      provider: fontProviders.google(),      weights: [500],      styles: ["italic"]    }  ]});
```

## Caching

[Section titled “Caching”](#caching)

The Fonts API caching implementation was designed to be practical in development and efficient in production. During builds, font files are copied to the `_astro/fonts` output directory, so they can benefit from HTTP caching of static assets (usually a year).

To clear the cache in development, remove the `.astro/fonts` directory. To clear the build cache, remove the `node_modules/.astro/fonts` directory.

## Examples

[Section titled “Examples”](#examples)

Astro’s font feature is based on flexible configuration options. Your own project’s font configuration may look different from simplified examples, so the following are provided to show what various font configurations might look like when used in production.

```
import { defineConfig, fontProviders } from "astro/config";
export default defineConfig({  fonts: [    {      name: "Roboto",      cssVariable: "--font-roboto",      provider: fontProviders.google(),      // Default included:      // weights: [400] ,      // styles: ["normal", "italic"],      // subsets: ["latin"],      // fallbacks: ["sans-serif"],      // formats: ["woff2"],    },    {      name: "Inter",      cssVariable: "--font-inter",      provider: fontProviders.fontsource(),      // Specify weights that are actually used      weights: [400, 500, 600, 700],      // Specify styles that are actually used      styles: ["normal"],      // Download only font files for characters used on the page      subsets: ["latin", "cyrillic"],      // Download more font formats      formats: ["woff2", "woff"],    },    {      name: "JetBrains Mono",      cssVariable: "--font-jetbrains-mono",      provider: fontProviders.fontsource(),      // Download only font files for characters used on the page      subsets: ["latin", "latin-ext"],      // Use a fallback font family matching the intended appearance      fallbacks: ["monospace"],    },    {      name: "Poppins",      cssVariable: "--font-poppins",      provider: fontProviders.local(),      options: {        // Weight and style are not specified so Astro        // will try to infer them for each variant        variants: [          {            src: [              "./src/assets/fonts/Poppins-regular.woff2",              "./src/assets/fonts/Poppins-regular.woff",            ]          },          {            src: [              "./src/assets/fonts/Poppins-bold.woff2",              "./src/assets/fonts/Poppins-bold.woff",            ]          },        ]      }    }  ],});
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
