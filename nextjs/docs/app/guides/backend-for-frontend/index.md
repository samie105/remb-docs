---
title: "How to use Next.js as a backend for your frontend"
source: "https://nextjs.org/docs/app/guides/backend-for-frontend"
canonical_url: "https://nextjs.org/docs/app/guides/backend-for-frontend"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:14:07.211Z"
content_hash: "9d107ad109e51c4d333ab25cfc5b69ea14a5746de3466c29f8cf192ee176c250"
menu_path: ["How to use Next.js as a backend for your frontend"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/authentication/index.md", "title": "How to implement authentication in Next.js"}
nav_next: {"path": "nextjs/docs/app/guides/caching-without-cache-components/index.md", "title": "Caching and Revalidating (Previous Model)"}
---

# How to use Next.js as a backend for your frontend

Last updated April 15, 2026

Next.js supports the "Backend for Frontend" pattern. This lets you create public endpoints to handle HTTP requests and return any content type—not just HTML. You can also access data sources and perform side effects like updating remote data.

If you are starting a new project, using `create-next-app` with the `--api` flag automatically includes an example `route.ts` in your new project's `app/` folder, demonstrating how to create an API endpoint.

pnpmnpmyarnbun

Terminal

```
pnpm create next-app --api
```

> **Good to know**: Next.js backend capabilities are not a full backend replacement. They serve as an API layer that:
> 
> *   is publicly reachable
> *   handles any HTTP request
> *   can return any content type

To implement this pattern, use:

*   [Route Handlers](/docs/app/api-reference/file-conventions/route)
*   [`proxy`](/docs/app/api-reference/file-conventions/proxy)
*   In Pages Router, [API Routes](/docs/pages/building-your-application/routing/api-routes)

## Public Endpoints[](#public-endpoints)

Route Handlers are public HTTP endpoints. Any client can access them.

Create a Route Handler using the `route.ts` or `route.js` file convention:

/app/api/route.ts

TypeScript

JavaScriptTypeScript

```
export function GET(request: Request) {}
```

This handles `GET` requests sent to `/api`.

Use `try/catch` blocks for operations that may throw an exception:

/app/api/route.ts

TypeScript

JavaScriptTypeScript

```
import { submit } from '@/lib/submit'
 
export async function POST(request: Request) {
  try {
    await submit(request)
    return new Response(null, { status: 204 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected error'
 
    return new Response(message, { status: 500 })
  }
}
```

Avoid exposing sensitive information in error messages sent to the client.

To restrict access, implement authentication and authorization. See [Authentication](/docs/app/guides/authentication).

## Content types[](#content-types)

Route Handlers let you serve non-UI responses, including JSON, XML, images, files, and plain text.

Next.js uses file conventions for common endpoints:

*   [`sitemap.xml`](/docs/app/api-reference/file-conventions/metadata/sitemap)
*   [`opengraph-image.jpg`, `twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image)
*   [favicon, app icon, and apple-icon](/docs/app/api-reference/file-conventions/metadata/app-icons)
*   [`manifest.json`](/docs/app/api-reference/file-conventions/metadata/manifest)
*   [`robots.txt`](/docs/app/api-reference/file-conventions/metadata/robots)

You can also define custom ones, such as:

*   `llms.txt`
*   `rss.xml`
*   `.well-known`

For example, `app/rss.xml/route.ts` creates a Route Handler for `rss.xml`.

/app/rss.xml/route.ts

TypeScript

JavaScriptTypeScript

```
export async function GET(request: Request) {
  const rssResponse = await fetch(/* rss endpoint */)
  const rssData = await rssResponse.json()
 
  const rssFeed = `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>${rssData.title}</title>
 <description>${rssData.description}</description>
 <link>${rssData.link}</link>
 <copyright>${rssData.copyright}</copyright>
 ${rssData.items.map((item) => {
   return `<item>
    <title>${item.title}</title>
    <description>${item.description}</description>
    <link>${item.link}</link>
    <pubDate>${item.publishDate}</pubDate>
    <guid isPermaLink="false">${item.guid}</guid>
 </item>`
 })}
</channel>
</rss>`
 
  const headers = new Headers({ 'content-type': 'application/xml' })
 
  return new Response(rssFeed, { headers })
}
```

Sanitize any input used to generate markup.

### Content negotiation[](#content-negotiation)

You can use [rewrites](/docs/app/api-reference/config/next-config-js/rewrites) with header matching to serve different content types from the same URL based on the request's `Accept` header. This is known as [content negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation).

For example, a documentation site might serve HTML pages to browsers and raw Markdown to AI agents from the same `/docs/…` URLs.

**1\. Configure a rewrite that matches the `Accept` header:**

next.config.js

```
module.exports = {
  async rewrites() {
    return [
      {
        source: '/docs/:slug*',
        destination: '/docs/md/:slug*',
        has: [
          {
            type: 'header',
            key: 'accept',
            value: '(.*)text/markdown(.*)',
          },
        ],
      },
    ]
  },
}
```

When a request to `/docs/getting-started` includes `Accept: text/markdown`, the rewrite routes it to `/docs/md/getting-started`. A Route Handler at that path returns the Markdown response. Clients that do not send `text/markdown` in their `Accept` header continue to receive the normal HTML page.

**2\. Create a Route Handler for the Markdown response:**

app/docs/md/\[...slug\]/route.ts

TypeScript

JavaScriptTypeScript

```
import { getDocsMd, generateDocsStaticParams } from '@/lib/docs'
 
export async function generateStaticParams() {
  return generateDocsStaticParams()
}
 
export async function GET(_: Request, ctx: RouteContext<'/docs/md/[...slug]'>) {
  const { slug } = await ctx.params
  const mdDoc = await getDocsMd({ slug })
 
  if (mdDoc == null) {
    return new Response(null, { status: 404 })
  }
 
  return new Response(mdDoc, {
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      Vary: 'Accept',
    },
  })
}
```

The [`Vary: Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary) response header tells caches that the response body depends on the `Accept` request header. Without it, a shared cache could serve a cached Markdown response to a browser (or vice versa). Most hosting providers already include the `Accept` header in their cache key, but setting `Vary` explicitly ensures correct behavior across all CDNs and proxy caches.

`generateStaticParams` lets you pre-render the Markdown variants at build time so they can be served from the edge without hitting the origin server on every request.

**3\. Test it with `curl`:**

```
# Returns Markdown
curl -H "Accept: text/markdown" https://example.com/docs/getting-started
 
# Returns the normal HTML page
curl https://example.com/docs/getting-started
```

> **Good to know:**
> 
> *   The `/docs/md/...` route is still directly accessible without the rewrite. If you want to restrict it to only serve via the rewrite, use [`proxy`](/docs/app/api-reference/file-conventions/proxy) to block direct requests that don't include the expected `Accept` header.
> *   For more advanced negotiation logic, you can use [`proxy`](/docs/app/api-reference/file-conventions/proxy) instead of rewrites for more flexibility.

### Consuming request payloads[](#consuming-request-payloads)

Use Request [instance methods](https://developer.mozilla.org/en-US/docs/Web/API/Request#instance_methods) like `.json()`, `.formData()`, or `.text()` to access the request body.

`GET` and `HEAD` requests don’t carry a body.

/app/api/echo-body/route.ts

TypeScript

JavaScriptTypeScript

```
export async function POST(request: Request) {
  const res = await request.json()
  return Response.json({ res })
}
```

> **Good to know**: Validate data before passing it to other systems

/app/api/send-email/route.ts

TypeScript

JavaScriptTypeScript

```
import { sendMail, validateInputs } from '@/lib/email-transporter'
 
export async function POST(request: Request) {
  const formData = await request.formData()
  const email = formData.get('email')
  const contents = formData.get('contents')
 
  try {
    await validateInputs({ email, contents })
    const info = await sendMail({ email, contents })
 
    return Response.json({ messageId: info.messageId })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'
 
    return new Response(message, { status: 500 })
  }
}
```

You can only read the request body once. Clone the request if you need to read it again:

/app/api/clone/route.ts

TypeScript

JavaScriptTypeScript

```
export async function POST(request: Request) {
  try {
    const clonedRequest = request.clone()
 
    await request.body()
    await clonedRequest.body()
    await request.body() // Throws error
 
    return new Response(null, { status: 204 })
  } catch {
    return new Response(null, { status: 500 })
  }
}
```

## Manipulating data[](#manipulating-data)

Route Handlers can transform, filter, and aggregate data from one or more sources. This keeps logic out of the frontend and avoids exposing internal systems.

You can also offload heavy computations to the server and reduce client battery and data usage.

```
import { parseWeatherData } from '@/lib/weather'
 
export async function POST(request: Request) {
  const body = await request.json()
  const searchParams = new URLSearchParams({ lat: body.lat, lng: body.lng })
 
  try {
    const weatherResponse = await fetch(`${weatherEndpoint}?${searchParams}`)
 
    if (!weatherResponse.ok) {
      /* handle error */
    }
 
    const weatherData = await weatherResponse.text()
    const payload = parseWeatherData.asJSON(weatherData)
 
    return new Response(payload, { status: 200 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'
 
    return new Response(message, { status: 500 })
  }
}
```

> **Good to know**: This example uses `POST` to avoid putting geo-location data in the URL. `GET` requests may be cached or logged, which could expose sensitive info.

## Proxying to a backend[](#proxying-to-a-backend)

You can use a Route Handler as a `proxy` to another backend. Add validation logic before forwarding the request.

/app/api/\[...slug\]/route.ts

TypeScript

JavaScriptTypeScript

```
import { isValidRequest } from '@/lib/utils'
 
export async function POST(request: Request, { params }) {
  const clonedRequest = request.clone()
  const isValid = await isValidRequest(clonedRequest)
 
  if (!isValid) {
    return new Response(null, { status: 400, statusText: 'Bad Request' })
  }
 
  const { slug } = await params
  const pathname = slug.join('/')
  const proxyURL = new URL(pathname, 'https://nextjs.org')
  const proxyRequest = new Request(proxyURL, request)
 
  try {
    return fetch(proxyRequest)
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'
 
    return new Response(message, { status: 500 })
  }
}
```

Or use:

*   `proxy` [rewrites](#proxy)
*   [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites) in `next.config.js`.

## NextRequest and NextResponse[](#nextrequest-and-nextresponse)

Next.js extends the [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) Web APIs with methods that simplify common operations. These extensions are available in both Route Handlers and Proxy.

Both provide methods for reading and manipulating cookies.

`NextRequest` includes the [`nextUrl`](/docs/app/api-reference/functions/next-request#nexturl) property, which exposes parsed values from the incoming request, for example, it makes it easier to access request pathname and search params.

`NextResponse` provides helpers like `next()`, `json()`, `redirect()`, and `rewrite()`.

You can pass `NextRequest` to any function expecting `Request`. Likewise, you can return `NextResponse` where a `Response` is expected.

/app/echo-pathname/route.ts

TypeScript

JavaScriptTypeScript

```
import { type NextRequest, NextResponse } from 'next/server'
 
export async function GET(request: NextRequest) {
  const nextUrl = request.nextUrl
 
  if (nextUrl.searchParams.get('redirect')) {
    return NextResponse.redirect(new URL('/', request.url))
  }
 
  if (nextUrl.searchParams.get('rewrite')) {
    return NextResponse.rewrite(new URL('/', request.url))
  }
 
  return NextResponse.json({ pathname: nextUrl.pathname })
}
```

Learn more about [`NextRequest`](/docs/app/api-reference/functions/next-request) and [`NextResponse`](/docs/app/api-reference/functions/next-response).

## Webhooks and callback URLs[](#webhooks-and-callback-urls)

Use Route Handlers to receive event notifications from third-party applications.

For example, revalidate a route when content changes in a CMS. Configure the CMS to call a specific endpoint on changes.

/app/webhook/route.ts

TypeScript

JavaScriptTypeScript

```
import { type NextRequest, NextResponse } from 'next/server'
 
export async function GET(request: NextRequest) {
  const token = request.nextUrl.searchParams.get('token')
 
  if (token !== process.env.REVALIDATE_SECRET_TOKEN) {
    return NextResponse.json({ success: false }, { status: 401 })
  }
 
  const tag = request.nextUrl.searchParams.get('tag')
 
  if (!tag) {
    return NextResponse.json({ success: false }, { status: 400 })
  }
 
  revalidateTag(tag)
 
  return NextResponse.json({ success: true })
}
```

Callback URLs are another use case. When a user completes a third-party flow, the third party sends them to a callback URL. Use a Route Handler to verify the response and decide where to redirect the user.

/app/auth/callback/route.ts

TypeScript

JavaScriptTypeScript

```
import { type NextRequest, NextResponse } from 'next/server'
 
export async function GET(request: NextRequest) {
  const token = request.nextUrl.searchParams.get('session_token')
  const redirectUrl = request.nextUrl.searchParams.get('redirect_url')
 
  const response = NextResponse.redirect(new URL(redirectUrl, request.url))
 
  response.cookies.set({
    value: token,
    name: '_token',
    path: '/',
    secure: true,
    httpOnly: true,
    expires: undefined, // session cookie
  })
 
  return response
}
```

## Redirects[](#redirects)

app/api/route.ts

TypeScript

JavaScriptTypeScript

```
import { redirect } from 'next/navigation'
 
export async function GET(request: Request) {
  redirect('https://nextjs.org/')
}
```

Learn more about redirects in [`redirect`](/docs/app/api-reference/functions/redirect) and [`permanentRedirect`](/docs/app/api-reference/functions/permanentRedirect)

## Proxy[](#proxy)

Only one `proxy` file is allowed per project. Use `config.matcher` to target specific paths. Learn more about [`proxy`](/docs/app/api-reference/file-conventions/proxy).

Use `proxy` to generate a response before the request reaches a route path.

proxy.ts

TypeScript

JavaScriptTypeScript

```
import { isAuthenticated } from '@lib/auth'
 
export const config = {
  matcher: '/api/:function*',
}
 
export function proxy(request: Request) {
  if (!isAuthenticated(request)) {
    return Response.json(
      { success: false, message: 'authentication failed' },
      { status: 401 }
    )
  }
}
```

You can also proxy requests using `proxy`:

proxy.ts

TypeScript

JavaScriptTypeScript

```
import { NextResponse } from 'next/server'
 
export function proxy(request: Request) {
  if (request.nextUrl.pathname === '/proxy-this-path') {
    const rewriteUrl = new URL('https://nextjs.org')
    return NextResponse.rewrite(rewriteUrl)
  }
}
```

Another type of response `proxy` can produce are redirects:

proxy.ts

TypeScript

JavaScriptTypeScript

```
import { NextResponse } from 'next/server'
 
export function proxy(request: Request) {
  if (request.nextUrl.pathname === '/v1/docs') {
    request.nextUrl.pathname = '/v2/docs'
    return NextResponse.redirect(request.nextUrl)
  }
}
```

## Security[](#security)

### Working with headers[](#working-with-headers)

Be deliberate about where headers go, and avoid directly passing incoming request headers to the outgoing response.

*   **Upstream request headers**: In Proxy, `NextResponse.next({ request: { headers } })` modifies the headers your server receives and does not expose them to the client.
*   **Response headers**: `new Response(..., { headers })`, `NextResponse.json(..., { headers })`, `NextResponse.next({ headers })`, or `response.headers.set(...)` send headers back to the client. If sensitive values were appended to these headers, they will be visible to clients.

Learn more in [NextResponse headers in Proxy](/docs/app/api-reference/functions/next-response#next).

### Rate limiting[](#rate-limiting)

You can implement rate limiting in your Next.js backend. In addition to code-based checks, enable any rate limiting features provided by your host.

/app/resource/route.ts

TypeScript

JavaScriptTypeScript

```
import { NextResponse } from 'next/server'
import { checkRateLimit } from '@/lib/rate-limit'
 
export async function POST(request: Request) {
  const { rateLimited } = await checkRateLimit(request)
 
  if (rateLimited) {
    return NextResponse.json({ error: 'Rate limit exceeded' }, { status: 429 })
  }
 
  return new Response(null, { status: 204 })
}
```

### Verify payloads[](#verify-payloads)

Never trust incoming request data. Validate content type and size, and sanitize against XSS before use.

Use timeouts to prevent abuse and protect server resources.

Store user-generated static assets in dedicated services. When possible, upload them from the browser and store the returned URI in your database to reduce request size.

### Access to protected resources[](#access-to-protected-resources)

Always verify credentials before granting access. Do not rely on proxy alone for authentication and authorization.

Remove sensitive or unnecessary data from responses and backend logs.

Rotate credentials and API keys regularly.

## Preflight Requests[](#preflight-requests)

Preflight requests use the `OPTIONS` method to ask the server if a request is allowed based on origin, method, and headers.

If `OPTIONS` is not defined, Next.js adds it automatically and sets the `Allow` header based on the other defined methods.

*   [CORS](/docs/app/api-reference/file-conventions/route#cors)

## Library patterns[](#library-patterns)

Community libraries often use the factory pattern for Route Handlers.

/app/api/\[...path\]/route.ts

```
import { createHandler } from 'third-party-library'
 
const handler = createHandler({
  /* library-specific options */
})
 
export const GET = handler
// or
export { handler as POST }
```

This creates a shared handler for `GET` and `POST` requests. The library customizes behavior based on the `method` and `pathname` in the request.

Libraries can also provide a `proxy` factory.

proxy.ts

```
import { createMiddleware } from 'third-party-library'
 
export default createMiddleware()
```

> **Good to know**: Third-party libraries may still refer to `proxy` as `middleware`.

## More examples[](#more-examples)

See more examples on using [Router Handlers](/docs/app/api-reference/file-conventions/route#examples) and the [`proxy`](/docs/app/api-reference/file-conventions/proxy#examples) API references.

These examples include, working with [Cookies](/docs/app/api-reference/file-conventions/route#cookies), [Headers](/docs/app/api-reference/file-conventions/route#headers), [Streaming](/docs/app/api-reference/file-conventions/route#streaming), Proxy [negative matching](/docs/app/api-reference/file-conventions/proxy#negative-matching), and other useful code snippets.

## Caveats[](#caveats)

### Server Components[](#server-components)

Fetch data in Server Components directly from its source, not via Route Handlers.

For Server Components prerendered at build time, using Route Handlers will fail the build step. This is because, while building there is no server listening for these requests.

For Server Components rendered on demand, fetching from Route Handlers is slower due to the extra HTTP round trip between the handler and the render process.

> A server side `fetch` request uses absolute URLs. This implies an HTTP round trip, to an external server. During development, your own development server acts as the external server. At build time there is no server, and at runtime, the server is available through your public facing domain.

Server Components cover most data-fetching needs. However, fetching data client side might be necessary for:

*   Data that depends on client-only Web APIs:
    *   Geo-location API
    *   Storage API
    *   Audio API
    *   File API
*   Frequently polled data

For these, use community libraries like [`swr`](https://swr.vercel.app/) or [`react-query`](https://tanstack.com/query/latest/docs/framework/react/overview).

### Server Actions[](#server-actions)

Server Actions let you run server-side code from the client. Their primary purpose is to mutate data from your frontend client.

Server Actions are queued. Using them for data fetching introduces sequential execution.

### `export` mode[](#export-mode)

`export` mode outputs a static site without a runtime server. Features that require the Next.js runtime are [not supported](/docs/app/guides/static-exports#unsupported-features), because this mode produces a static site, and no runtime server.

In `export mode`, only `GET` Route Handlers are supported, in combination with the [`dynamic`](/docs/app/guides/caching-without-cache-components#dynamic) route segment config, set to `'force-static'`.

This can be used to generate static HTML, JSON, TXT, or other files.

app/hello-world/route.ts

```
export const dynamic = 'force-static'
 
export function GET() {
  return new Response('Hello World', { status: 200 })
}
```

### Deployment environment[](#deployment-environment)

Some hosts deploy Route Handlers as lambda functions. This means:

*   Route Handlers cannot share data between requests.
*   The environment may not support writing to File System.
*   Long-running handlers may be terminated due to timeouts.
*   WebSockets won’t work because the connection closes on timeout, or after the response is generated.

## API Reference

Learn more about Route Handlers, Proxy, and Rewrites

[

### route.js

API reference for the route.js special file.

](/docs/app/api-reference/file-conventions/route)[

### proxy.js

API reference for the proxy.js file.

](/docs/app/api-reference/file-conventions/proxy)[

### rewrites

Add rewrites to your Next.js app.

](/docs/app/api-reference/config/next-config-js/rewrites)

[Previous

Authentication

](/docs/app/guides/authentication)

[Next

Caching (Previous Model)

](/docs/app/guides/caching-without-cache-components)

Was this helpful?

supported.

Send


