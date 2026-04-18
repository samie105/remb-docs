---
title: "How to optimize third-party libraries"
source: "https://nextjs.org/docs/app/guides/third-party-libraries"
canonical_url: "https://nextjs.org/docs/app/guides/third-party-libraries"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:16:45.481Z"
content_hash: "9ba475ec073e5944089083a728d82a0ffd1ba2500914bdd5d380481aa69b2ea1"
menu_path: ["How to optimize third-party libraries"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/testing/vitest/index.md", "title": "How to set up Vitest with Next.js"}
nav_next: {"path": "nextjs/docs/app/guides/upgrading/index.md", "title": "Upgrade Guides"}
---

# How to optimize third-party libraries

Last updated April 15, 2026

**`@next/third-parties`** is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries in your Next.js application.

All third-party integrations provided by `@next/third-parties` have been optimized for performance and ease of use.

## Getting Started[](#getting-started)

To get started, install the `@next/third-parties` library:

pnpmnpmyarnbun

Terminal

```
pnpm add @next/third-parties@latest next@latest
```

`@next/third-parties` is currently an **experimental** library under active development. We recommend installing it with the **latest** or **canary** flags while we work on adding more third-party integrations.

## Google Third-Parties[](#google-third-parties)

All supported third-party libraries from Google can be imported from `@next/third-parties/google`.

### Google Tag Manager[](#google-tag-manager)

The `GoogleTagManager` component can be used to instantiate a [Google Tag Manager](https://developers.google.com/tag-platform/tag-manager) container to your page. By default, it fetches the original inline script after hydration occurs on the page.

To load Google Tag Manager for all routes, include the component directly in your root layout and pass in your GTM container ID:

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { GoogleTagManager } from '@next/third-parties/google'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <GoogleTagManager gtmId="GTM-XYZ" />
      <body>{children}</body>
    </html>
  )
}
```

To load Google Tag Manager for a single route, include the component in your page file:

app/page.js

```
import { GoogleTagManager } from '@next/third-parties/google'
 
export default function Page() {
  return <GoogleTagManager gtmId="GTM-XYZ" />
}
```

#### Sending Events[](#sending-events)

The `sendGTMEvent` function can be used to track user interactions on your page by sending events using the `dataLayer` object. For this function to work, the `<GoogleTagManager />` component must be included in either a parent layout, page, or component, or directly in the same file.

app/page.js

```
'use client'
 
import { sendGTMEvent } from '@next/third-parties/google'
 
export function EventButton() {
  return (
    <div>
      <button
        onClick={() => sendGTMEvent({ event: 'buttonClicked', value: 'xyz' })}
      >
        Send Event
      </button>
    </div>
  )
}
```

Refer to the Tag Manager [developer documentation](https://developers.google.com/tag-platform/tag-manager/datalayer) to learn about the different variables and events that can be passed into the function.

#### Server-side Tagging[](#server-side-tagging)

If you're using a server-side tag manager and serving `gtm.js` scripts from your tagging server you can use `gtmScriptUrl` option to specify the URL of the script.

#### Options[](#options)

Options to pass to the Google Tag Manager. For a full list of options, read the [Google Tag Manager docs](https://developers.google.com/tag-platform/tag-manager/datalayer).

Name

Type

Description

`gtmId`

Required\*

Your GTM container ID. Usually starts with `GTM-`.

`gtmScriptUrl`

Optional\*

GTM script URL. Defaults to `https://www.googletagmanager.com/gtm.js`.

`dataLayer`

Optional

Data layer object to instantiate the container with.

`dataLayerName`

Optional

Name of the data layer. Defaults to `dataLayer`.

`auth`

Optional

Value of authentication parameter (`gtm_auth`) for environment snippets.

`preview`

Optional

Value of preview parameter (`gtm_preview`) for environment snippets.

\*`gtmId` can be omitted when `gtmScriptUrl` is provided to support [Google tag gateway for advertisers](https://developers.google.com/tag-platform/tag-manager/gateway/setup-guide?setup=manual).

### Google Analytics[](#google-analytics)

The `GoogleAnalytics` component can be used to include [Google Analytics 4](https://developers.google.com/analytics/devguides/collection/ga4) to your page via the Google tag (`gtag.js`). By default, it fetches the original scripts after hydration occurs on the page.

> **Recommendation**: If Google Tag Manager is already included in your application, you can configure Google Analytics directly using it, rather than including Google Analytics as a separate component. Refer to the [documentation](https://developers.google.com/analytics/devguides/collection/ga4/tag-options#what-is-gtm) to learn more about the differences between Tag Manager and `gtag.js`.

To load Google Analytics for all routes, include the component directly in your root layout and pass in your measurement ID:

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
import { GoogleAnalytics } from '@next/third-parties/google'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <GoogleAnalytics gaId="G-XYZ" />
    </html>
  )
}
```

To load Google Analytics for a single route, include the component in your page file:

app/page.js

```
import { GoogleAnalytics } from '@next/third-parties/google'
 
export default function Page() {
  return <GoogleAnalytics gaId="G-XYZ" />
}
```

#### Sending Events[](#sending-events-1)

The `sendGAEvent` function can be used to measure user interactions on your page by sending events using the `dataLayer` object. For this function to work, the `<GoogleAnalytics />` component must be included in either a parent layout, page, or component, or directly in the same file.

app/page.js

```
'use client'
 
import { sendGAEvent } from '@next/third-parties/google'
 
export function EventButton() {
  return (
    <div>
      <button
        onClick={() => sendGAEvent('event', 'buttonClicked', { value: 'xyz' })}
      >
        Send Event
      </button>
    </div>
  )
}
```

Refer to the Google Analytics [developer documentation](https://developers.google.com/analytics/devguides/collection/ga4/event-parameters) to learn more about event parameters.

#### Tracking Pageviews[](#tracking-pageviews)

Google Analytics automatically tracks pageviews when the browser history state changes. This means that client-side navigations between Next.js routes will send pageview data without any configuration.

To ensure that client-side navigations are being measured correctly, verify that the [_“Enhanced Measurement”_](https://support.google.com/analytics/answer/9216061#enable_disable) property is enabled in your Admin panel and the _“Page changes based on browser history events”_ checkbox is selected.

> **Note**: If you decide to manually send pageview events, make sure to disable the default pageview measurement to avoid having duplicate data. Refer to the Google Analytics [developer documentation](https://developers.google.com/analytics/devguides/collection/ga4/views?client_type=gtag#manual_pageviews) to learn more.

#### Options[](#options-1)

Options to pass to the `<GoogleAnalytics>` component.

Name

Type

Description

`gaId`

Required

Your [measurement ID](https://support.google.com/analytics/answer/12270356). Usually starts with `G-`.

`dataLayerName`

Optional

Name of the data layer. Defaults to `dataLayer`.

`nonce`

Optional

A [nonce](/docs/app/guides/content-security-policy#nonces).

### Google Maps Embed[](#google-maps-embed)

The `GoogleMapsEmbed` component can be used to add a [Google Maps Embed](https://developers.google.com/maps/documentation/embed/embedding-map) to your page. By default, it uses the `loading` attribute to lazy-load the embed below the fold.

app/page.js

```
import { GoogleMapsEmbed } from '@next/third-parties/google'
 
export default function Page() {
  return (
    <GoogleMapsEmbed
      apiKey="XYZ"
      height={200}
      width="100%"
      mode="place"
      q="Brooklyn+Bridge,New+York,NY"
    />
  )
}
```

#### Options[](#options-2)

Options to pass to the Google Maps Embed. For a full list of options, read the [Google Map Embed docs](https://developers.google.com/maps/documentation/embed/embedding-map).

Name

Type

Description

`apiKey`

Required

Your api key.

`mode`

Required

[Map mode](https://developers.google.com/maps/documentation/embed/embedding-map#choosing_map_modes)

`height`

Optional

Height of the embed. Defaults to `auto`.

`width`

Optional

Width of the embed. Defaults to `auto`.

`style`

Optional

Pass styles to the iframe.

`allowfullscreen`

Optional

Property to allow certain map parts to go full screen.

`loading`

Optional

Defaults to lazy. Consider changing if you know your embed will be above the fold.

`q`

Optional

Defines map marker location. _This may be required depending on the map mode_.

`center`

Optional

Defines the center of the map view.

`zoom`

Optional

Sets initial zoom level of the map.

`maptype`

Optional

Defines type of map tiles to load.

`language`

Optional

Defines the language to use for UI elements and for the display of labels on map tiles.

`region`

Optional

Defines the appropriate borders and labels to display, based on geo-political sensitivities.

### YouTube Embed[](#youtube-embed)

The `YouTubeEmbed` component can be used to load and display a YouTube embed. This component loads faster by using [`lite-youtube-embed`](https://github.com/paulirish/lite-youtube-embed) under the hood.

app/page.js

```
import { YouTubeEmbed } from '@next/third-parties/google'
 
export default function Page() {
  return <YouTubeEmbed videoid="ogfYd705cRs" height={400} params="controls=0" />
}
```

#### Options[](#options-3)

Name

Type

Description

`videoid`

Required

YouTube video id.

`width`

Optional

Width of the video container. Defaults to `auto`

`height`

Optional

Height of the video container. Defaults to `auto`

`playlabel`

Optional

A visually hidden label for the play button for accessibility.

`params`

Optional

The video player params defined [here](https://developers.google.com/youtube/player_parameters#Parameters).  
Params are passed as a query param string.  
Eg: `params="controls=0&start=10&end=30"`

`style`

Optional

Used to apply styles to the video container.

[Previous

Vitest

](/docs/app/guides/testing/vitest)

[Next

Upgrading

](/docs/app/guides/upgrading)

Was this helpful?

supported.

Send




