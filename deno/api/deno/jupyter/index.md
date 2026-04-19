---
title: "Jupyter - Deno documentation"
source: "https://docs.deno.com/api/deno/jupyter"
canonical_url: "https://docs.deno.com/api/deno/jupyter"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:10:00.350Z"
content_hash: "540b786a589fe3fe3ad45815cf66cf7447af62d274548c9d05ef58010613266e"
menu_path: ["Jupyter - Deno documentation"]
section_path: []
---
### Functions [#](#Functions)

f

[Deno.jupyter.broadcast](./././~/Deno.jupyter.broadcast "Deno.jupyter.broadcast")

Broadcast a message on IO pub channel.

f

[Deno.jupyter.display](./././~/Deno.jupyter.display "Deno.jupyter.display")

Display function for Jupyter Deno Kernel. Mimics the behavior of IPython's `display(obj, raw=True)` function to allow asynchronous displaying of objects in Jupyter.

f

[Deno.jupyter.format](./././~/Deno.jupyter.format "Deno.jupyter.format")

Format an object for displaying in Deno

f

[Deno.jupyter.html](./././~/Deno.jupyter.html "Deno.jupyter.html")

Show HTML in Jupyter frontends with a tagged template function.

f

[Deno.jupyter.image](./././~/Deno.jupyter.image "Deno.jupyter.image")

Display a JPG or PNG image.

f

[Deno.jupyter.md](./././~/Deno.jupyter.md "Deno.jupyter.md")

Show Markdown in Jupyter frontends with a tagged template function.

f

[Deno.jupyter.svg](./././~/Deno.jupyter.svg "Deno.jupyter.svg")

SVG Tagged Template Function.

### Interfaces [#](#Interfaces)

I

[Deno.jupyter.Displayable](./././~/Deno.jupyter.Displayable "Deno.jupyter.Displayable")

No documentation available

*   [$display](./././~/Deno.jupyter.Displayable#property_$display)

I

[Deno.jupyter.DisplayOptions](./././~/Deno.jupyter.DisplayOptions "Deno.jupyter.DisplayOptions")

No documentation available

*   [display\_id](./././~/Deno.jupyter.DisplayOptions#property_display_id)
*   [raw](./././~/Deno.jupyter.DisplayOptions#property_raw)
*   [update](./././~/Deno.jupyter.DisplayOptions#property_update)

I

[Deno.jupyter.MediaBundle](./././~/Deno.jupyter.MediaBundle "Deno.jupyter.MediaBundle")

A collection of supported media types and data for Jupyter frontends.

*   [application/geo+json](./././~/Deno.jupyter.MediaBundle#property_application/geo+json)
*   [application/javascript](./././~/Deno.jupyter.MediaBundle#property_application/javascript)
*   [application/json](./././~/Deno.jupyter.MediaBundle#property_application/json)
*   [application/pdf](./././~/Deno.jupyter.MediaBundle#property_application/pdf)
*   [application/vdom.v1+json](./././~/Deno.jupyter.MediaBundle#property_application/vdom_v1+json)
*   [application/vnd.plotly.v1+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_plotly_v1+json)
*   [application/vnd.vega.v5+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_vega_v5+json)
*   [application/vnd.vegalite.v4+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_vegalite_v4+json)
*   [application/vnd.vegalite.v5+json](./././~/Deno.jupyter.MediaBundle#property_application/vnd_vegalite_v5+json)
*   [image/gif](./././~/Deno.jupyter.MediaBundle#property_image/gif)
*   [image/jpeg](./././~/Deno.jupyter.MediaBundle#property_image/jpeg)
*   [image/png](./././~/Deno.jupyter.MediaBundle#property_image/png)
*   [image/svg+xml](./././~/Deno.jupyter.MediaBundle#property_image/svg+xml)
*   [text/html](./././~/Deno.jupyter.MediaBundle#property_text/html)
*   [text/markdown](./././~/Deno.jupyter.MediaBundle#property_text/markdown)
*   [text/plain](./././~/Deno.jupyter.MediaBundle#property_text/plain)

I

[Deno.jupyter.VegaObject](./././~/Deno.jupyter.VegaObject "Deno.jupyter.VegaObject")

No documentation available

*   [$schema](./././~/Deno.jupyter.VegaObject#property_$schema)

### Namespaces [#](#Namespaces)

N

[Deno.jupyter](./././~/Deno.jupyter "Deno.jupyter")

A namespace containing runtime APIs available in Jupyter notebooks.

### Variables [#](#Variables)

v

[Deno.jupyter.$display](./././~/Deno.jupyter.$display "Deno.jupyter.$display")

No documentation available
