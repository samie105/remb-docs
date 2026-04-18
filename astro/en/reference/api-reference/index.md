---
title: "Astro render context"
source: "https://docs.astro.build/en/reference/api-reference/"
canonical_url: "https://docs.astro.build/en/reference/api-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:34.136Z"
content_hash: "36f3b322de18a8f9993010919a156d3ba8ef3c93914562ca592c91295793923a"
menu_path: ["Astro render context"]
section_path: []
nav_prev: {"path": "astro/en/reference/routing-reference/index.md", "title": "Routing Reference"}
nav_next: {"path": "astro/en/reference/modules/astro-actions/index.md", "title": "Actions API Reference"}
---

# Astro render context

When rendering a page, Astro provides a runtime API specific to the current render. This includes useful information such as the current page URL as well as APIs to perform actions like redirecting to another page.

In `.astro` components, this context is available from the `Astro` global object. Endpoint functions are also called with this same context object as their first argument, whose properties mirror the Astro global properties.

Some properties are only available for routes rendered on demand or may have limited functionality on prerendered pages.

The `Astro` global object is available to all `.astro` files. Use the `context` object in [endpoint functions](/en/guides/endpoints/) to serve static or live server endpoints and in [middleware](/en/guides/middleware/) to inject behavior when a page or endpoint is about to be rendered.

## The context object

[Section titled “The context object”](#the-context-object)

The following properties are available on the `Astro` global (e.g. `Astro.props`, `Astro.redirect()`) and are also available on the context object (e.g. `context.props`, `context.redirect()`) passed to endpoint functions and middleware.

### `props`

[Section titled “props”](#props)

`props` is an object containing any values that have been passed as [component attributes](/en/basics/astro-components/#component-props).

```
---const { title, date } = Astro.props;---<div>  <h1>{title}</h1>  <p>{date}</p></div>
```

```
---import Heading from '../components/Heading.astro';---<Heading title="My First Post" date="09 Aug 2022" />
```

Learn more about how [Markdown and MDX layouts](/en/guides/markdown-content/#frontmatter-layout-property) handle props.

The `props` object also contains any `props` passed from `getStaticPaths()` when rendering static routes.

*   [Astro.props](#tab-panel-2002)
*   [context.props](#tab-panel-2003)

```
---export function getStaticPaths() {  return [    { params: { id: '1' }, props: { author: 'Blu' } },    { params: { id: '2' }, props: { author: 'Erika' } },    { params: { id: '3' }, props: { author: 'Matthew' } }  ];}
const { id } = Astro.params;const { author } = Astro.props;---
```

See also: [Data Passing with `props`](/en/reference/routing-reference/#data-passing-with-props)

### `params`

[Section titled “params”](#params)

`params` is an object containing the values of dynamic route segments matched for a request. Its keys must match the [parameters](/en/guides/routing/#dynamic-routes) in the page or endpoint file path.

In static builds, this will be the `params` returned by `getStaticPaths()` used for prerendering [dynamic routes](/en/guides/routing/#dynamic-routes):

*   [Astro.params](#tab-panel-2004)
*   [context.params](#tab-panel-2005)

```
---export function getStaticPaths() {  return [    { params: { id: '1' } },    { params: { id: '2' } },    { params: { id: '3' } }  ];}const { id } = Astro.params;---<h1>{id}</h1>
```

When routes are rendered on demand, `params` can be any value matching the path segments in the dynamic route pattern.

```
---import { getPost } from '../api';
const post = await getPost(Astro.params.id);
// No posts found with this IDif (!post) {  return Astro.redirect("/404")}---<html>  <h1>{post.name}</h1></html>
```

See also: [`params`](/en/reference/routing-reference/#params)

### `url`

[Section titled “url”](#url)

**Type:** `URL`  

**Added in:** `astro@1.0.0`

`url` is a [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL) object constructed from the current `request.url` value. It is useful for interacting with individual properties of the request URL, like pathname and origin.

`Astro.url` is equivalent to doing `new URL(Astro.request.url)`.

`url` will be a `localhost` URL in dev mode. When building a site, prerendered routes will receive a URL based on the [`site`](/en/reference/configuration-reference/#site) and [`base`](/en/reference/configuration-reference/#base) options. If `site` is not configured, prerendered pages will receive a `localhost` URL during builds as well.

```
<h1>The current URL is: {Astro.url}</h1><h1>The current URL pathname is: {Astro.url.pathname}</h1><h1>The current URL origin is: {Astro.url.origin}</h1>
```

You can also use `url` to create new URLs by passing it as an argument to [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL).

```
---// Example: Construct a canonical URL using your production domainconst canonicalURL = new URL(Astro.url.pathname, Astro.site);// Example: Construct a URL for SEO meta tags using your current domainconst socialImageURL = new URL('/images/preview.png', Astro.url);---<link rel="canonical" href={canonicalURL} /><meta property="og:image" content={socialImageURL} />
```

### `site`

[Section titled “site”](#site)

**Type:** `URL | undefined`

`site` returns a `URL` made from `site` in your Astro config. It returns `undefined` if you have not set a value for [`site`](/en/reference/configuration-reference/#site) in your Astro config.

```
<link    rel="alternate"    type="application/rss+xml"    title="Your Site's Title"    href={new URL("rss.xml", Astro.site)}/>
```

### `clientAddress`

[Section titled “clientAddress”](#clientaddress)

**Type:** `string`  

**Added in:** `astro@1.0.0`

`clientAddress` specifies the [IP address](https://en.wikipedia.org/wiki/IP_address) of the request. This property is only available for routes rendered on demand and cannot be used on prerendered pages.

*   [Astro.clientAddress](#tab-panel-2006)
*   [context.clientAddress](#tab-panel-2007)

```
---export const prerender = false; // Not needed in 'server' mode---
<div>Your IP address is: <span class="address">{Astro.clientAddress}</span></div>
```

### `isPrerendered`

[Section titled “isPrerendered”](#isprerendered)

**Type**: `boolean`  

**Added in:** `astro@5.0.0`

A boolean representing whether or not the current page is prerendered.

You can use this property to run conditional logic in middleware, for example, to avoid accessing headers in prerendered pages.

### `generator`

[Section titled “generator”](#generator)

**Type:** `string`  

**Added in:** `astro@1.0.0`

`generator` provides the current version of Astro your project is running. This is a convenient way to add a [`<meta name="generator">`](https://html.spec.whatwg.org/multipage/semantics.html#meta-generator) tag with your current version of Astro. It follows the format `"Astro v5.x.x"`.

*   [Astro.generator](#tab-panel-2008)
*   [context.generator](#tab-panel-2009)

```
<html>  <head>    <meta name="generator" content={Astro.generator} />  </head>  <body>    <footer>      <p>Built with <a href="https://astro.build">{Astro.generator}</a></p>    </footer>  </body></html>
```

### `request`

[Section titled “request”](#request)

**Type:** `Request`

`request` is a standard [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object. It can be used to get the `url`, `headers`, `method`, and even the body of the request.

*   [Astro.request](#tab-panel-2010)
*   [context.request](#tab-panel-2011)

```
<p>Received a {Astro.request.method} request to "{Astro.request.url}".</p><p>Received request headers:</p><p><code>{JSON.stringify(Object.fromEntries(Astro.request.headers))}</code></p>
```

### `response`

[Section titled “response”](#response)

**Type:** `ResponseInit & { readonly headers: Headers }`

`response` is a standard `ResponseInit` object. It has the following structure.

*   `status`: The numeric status code of the response, e.g., `200`.
*   `statusText`: The status message associated with the status code, e.g., `'OK'`.
*   `headers`: A [`Headers`](https://developer.mozilla.org/en-US/docs/Web/API/Headers) instance that you can use to set the HTTP headers of the response.

`Astro.response` is used to set the `status`, `statusText`, and `headers` for a page’s response.

```
---if (condition) {  Astro.response.status = 404;  Astro.response.statusText = 'Not found';}---
```

Or to set a header:

```
---Astro.response.headers.set('Set-Cookie', 'a=b; Path=/;');---
```

### `redirect()`

[Section titled “redirect()”](#redirect)

**Type:** `(path: string, status?: number) => Response`

**Added in:** `astro@1.5.0`

`redirect()` returns a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object that allows you to redirect to another page, and optionally provide an [HTTP response status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages) as a second parameter.

A page (and not a child component) must `return` the result of `Astro.redirect()` for the redirect to occur.

For statically-generated routes, this will produce a client redirect using a [`<meta http-equiv="refresh">` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#http-equiv) and does not support status codes.

For on-demand rendered routes, setting a custom status code is supported when redirecting. If not specified, redirects will be served with a `302` status code.

The following example redirects a user to a login page:

*   [Astro.redirect()](#tab-panel-2012)
*   [context.redirect()](#tab-panel-2013)

```
---import { isLoggedIn } from '../utils';
const cookie = Astro.request.headers.get('cookie');
// If the user is not logged in, redirect them to the login pageif (!isLoggedIn(cookie)) {  return Astro.redirect('/login');}---
<p>User information</p>
```

### `rewrite()`

[Section titled “rewrite()”](#rewrite)

**Type:** `(rewritePayload: string | URL | Request) => Promise<Response>`  

**Added in:** `astro@4.13.0`

`rewrite()` allows you to serve content from a different URL or path without redirecting the browser to a new page.

The method accepts either a string, a `URL`, or a `Request` for the location of the path.

Use a string to provide an explicit path:

*   [Astro.rewrite()](#tab-panel-2014)
*   [context.rewrite()](#tab-panel-2015)

```
---return Astro.rewrite("/login")---
```

Use a `URL` type when you need to construct the URL path for the rewrite. The following example renders a page’s parent path by creating a new URL from the relative `"../"` path:

*   [Astro.rewrite()](#tab-panel-2016)
*   [context.rewrite()](#tab-panel-2017)

```
---return Astro.rewrite(new URL("../", Astro.url))---
```

Use a `Request` type for complete control of the `Request` sent to the server for the new path. The following example sends a request to render the parent page while also providing headers:

*   [Astro.rewrite()](#tab-panel-2018)
*   [context.rewrite()](#tab-panel-2019)

```
---return Astro.rewrite(new Request(new URL("../", Astro.url), {  headers: {    "x-custom-header": JSON.stringify(Astro.locals.someValue)  }}))---
```

### `originPathname`

[Section titled “originPathname”](#originpathname)

**Type:** `string`  

**Added in:** `astro@5.0.0`

`originPathname` defines the original pathname of the request, before rewrites were applied.

*   [Astro.originPathname](#tab-panel-2020)
*   [context.originPathname](#tab-panel-2021)

```
<p>The origin path is {Astro.originPathname}</p><p>The rewritten path is {Astro.url.pathname}</p>
```

### `locals`

[Section titled “locals”](#locals)

**Added in:** `astro@2.4.0`

`locals` is an object used to store and access arbitrary information during the lifecycle of a request. `Astro.locals` is an object containing any values from the `context.locals` object set by middleware. Use this to access data returned by middleware in your `.astro` files.

Middleware functions can both read and write the values of `context.locals`:

```
import type { MiddlewareHandler } from 'astro';
export const onRequest: MiddlewareHandler = ({ locals }, next) => {  if (!locals.title) {    locals.title = "Default Title";  }  return next();}
```

Astro components and API endpoints can read values from `locals` when they render:

*   [Astro.locals](#tab-panel-2022)
*   [context.locals](#tab-panel-2023)

```
---const title = Astro.locals.title;---<h1>{title}</h1>
```

### `preferredLocale`

[Section titled “preferredLocale”](#preferredlocale)

**Type:** `string | undefined`  

**Added in:** `astro@3.5.0`

`preferredLocale` is a computed value to find the best match between your visitor’s browser language preferences and the locales supported by your site.

It is computed by checking the configured locales in your [`i18n.locales`](/en/reference/configuration-reference/#i18nlocales) array and the locales supported by the user’s browser via the header `Accept-Language`. This value is `undefined` if no such match exists.

This property is only available for routes rendered on demand and cannot be used on prerendered, static pages.

### `preferredLocaleList`

[Section titled “preferredLocaleList”](#preferredlocalelist)

**Type:** `string[] | undefined`  

**Added in:** `astro@3.5.0`

`preferredLocaleList` represents the array of all locales that are both requested by the browser and supported by your website. This produces a list of all compatible languages between your site and your visitor.

If none of the browser’s requested languages are found in your locales array, then the value is `[]`. This occurs when you do not support any of your visitor’s preferred locales.

If the browser does not specify any preferred languages, then this value will be [`i18n.locales`](/en/reference/configuration-reference/#i18nlocales): all of your supported locales will be considered equally preferred by a visitor with no preferences.

This property is only available for routes rendered on demand and cannot be used on prerendered, static pages.

### `currentLocale`

[Section titled “currentLocale”](#currentlocale)

**Type:** `string | undefined`  

**Added in:** `astro@3.5.6`

The locale computed from the current URL, using the syntax specified in your `locales` configuration. If the URL does not contain a `/[locale]/` prefix, then the value will default to [`i18n.defaultLocale`](/en/reference/configuration-reference/#i18ndefaultlocale).

### `getActionResult()`

[Section titled “getActionResult()”](#getactionresult)

**Type:** `(action: TAction) => ActionReturnType<TAction> | undefined`  

**Added in:** `astro@4.15.0`

`getActionResult()` is a function that returns the result of an [Action](/en/guides/actions/) submission. This accepts an action function as an argument (e.g. `actions.logout`) and returns a `data` or `error` object when a submission is received. Otherwise, it will return `undefined`.

```
---import { actions } from 'astro:actions';
const result = Astro.getActionResult(actions.logout);---
<form action={actions.logout}>  <button type="submit">Log out</button></form>{result?.error && <p>Failed to log out. Please try again.</p>}
```

### `callAction()`

[Section titled “callAction()”](#callaction)

**Added in:** `astro@4.15.0`

`callAction()` is a function used to call an Action handler directly from your Astro component. This function accepts an Action function as the first argument (e.g. `actions.logout`) and any input that action receives as the second argument. It returns the result of the action as a promise.

```
---import { actions } from 'astro:actions';
const { data, error } = await Astro.callAction(actions.logout, { userId: '123' });---
```

### `routePattern`

[Section titled “routePattern”](#routepattern)

**Type**: `string`  

**Added in:** `astro@5.0.0`

The route pattern responsible for generating the current page or route. In file-based routing, this resembles the file path in your project used to create the route. When integrations create routes for your project, `context.routePattern` is identical to the value for `injectRoute.pattern`.

The value will start with a leading slash and look similar to the path of a page component relative to your `src/pages/` folder without a file extension.

For example, the file `src/pages/en/blog/[slug].astro` will return `/en/blog/[slug]` for `routePattern`. Every page on your site generated by that file (e.g. `/en/blog/post-1/`, `/en/blog/post-2/`, etc.) shares the same value for `routePattern`. In the case of `index.*` routes, the route pattern will not include the word “index.” For example, `src/pages/index.astro` will return `/`.

You can use this property to understand which route is rendering your component. This allows you to target or analyze similarly-generated page URLs together. For example, you can use it to conditionally render certain information, or collect metrics about which routes are slower.

### `cookies`

[Section titled “cookies”](#cookies)

**Type:** `AstroCookies`  

**Added in:** `astro@1.4.0`

`cookies` contains utilities for reading and manipulating cookies for [routes rendered on demand](/en/guides/on-demand-rendering/).

#### Cookie utilities

[Section titled “Cookie utilities”](#cookie-utilities)

##### `cookies.get()`

[Section titled “cookies.get()”](#cookiesget)

**Type:** `(key: string, options?: [AstroCookieGetOptions](#astrocookiegetoptions)) => [AstroCookie](#astrocookie-type) | undefined`

Gets the cookie as an [`AstroCookie`](#astrocookie-type) object, which contains the `value` and utility functions for converting the cookie to non-string types.

##### `cookies.has()`

[Section titled “cookies.has()”](#cookieshas)

**Type:** `(key: string, options?: [AstroCookieGetOptions](#astrocookiegetoptions)) => boolean`

Whether this cookie exists. If the cookie has been set via `Astro.cookies.set()` this will return true, otherwise, it will check cookies in the `Astro.request`.

##### `cookies.set()`

[Section titled “cookies.set()”](#cookiesset)

**Type:** `(key: string, value: string | object, options?: [AstroCookieSetOptions](#astrocookiesetoptions)) => void`

Sets the cookie `key` to the given value. This will attempt to convert the cookie value to a string. Options provide ways to set [cookie features](https://www.npmjs.com/package/cookie#options-1), such as the `maxAge` or `httpOnly`.

##### `cookies.delete()`

[Section titled “cookies.delete()”](#cookiesdelete)

**Type:** `(key: string, options?: AstroCookieDeleteOptions) => void`

Invalidates a cookie by setting the expiration date in the past (0 in Unix time).

Once a cookie is “deleted” (expired), `Astro.cookies.has()` will return `false` and `Astro.cookies.get()` will return an [`AstroCookie`](#astrocookie-type) with a `value` of `undefined`. Options available when deleting a cookie are: `domain`, `path`, `httpOnly`, `sameSite`, and `secure`.

##### `cookies.merge()`

[Section titled “cookies.merge()”](#cookiesmerge)

**Type:** `(cookies: AstroCookies) => void`

Merges a new `AstroCookies` instance into the current instance. Any new cookies will be added to the current instance and any cookies with the same name will overwrite existing values.

##### `cookies.headers()`

[Section titled “cookies.headers()”](#cookiesheaders)

**Type:** `() => Iterator<string>`

Gets the header values for `Set-Cookie` that will be sent out with the response.

#### `AstroCookie` Type

[Section titled “AstroCookie Type”](#astrocookie-type)

The type returned from getting a cookie via `Astro.cookies.get()`. It has the following properties:

##### `AstroCookie.value`

[Section titled “AstroCookie.value”](#astrocookievalue)

**Type:** `string`

The raw string value of the cookie.

##### `AstroCookie.json()`

[Section titled “AstroCookie.json()”](#astrocookiejson)

**Type:** `() => Record<string, any>`

Parses the cookie value via `JSON.parse()`, returning an object. Throws if the cookie value is not valid JSON.

##### `AstroCookie.number()`

[Section titled “AstroCookie.number()”](#astrocookienumber)

**Type:** `() => number`

Parses the cookie value as a Number. Returns NaN if not a valid number.

##### `AstroCookie.boolean()`

[Section titled “AstroCookie.boolean()”](#astrocookieboolean)

**Type:** `() => boolean`

Converts the cookie value to a boolean.

#### `AstroCookieGetOptions`

[Section titled “AstroCookieGetOptions”](#astrocookiegetoptions)

**Added in:** `astro@4.1.0`

The `AstroCookieGetOption` interface allows you to specify options when you get a cookie.

##### `AstroCookieGetOptions.decode()`

[Section titled “AstroCookieGetOptions.decode()”](#astrocookiegetoptionsdecode)

**Type:** `(value: string) => string`

Allows customization of how a cookie is deserialized into a value.

#### `AstroCookieSetOptions`

[Section titled “AstroCookieSetOptions”](#astrocookiesetoptions)

**Added in:** `astro@4.1.0`

`AstroCookieSetOptions` is an object that can be passed to `Astro.cookies.set()` when setting a cookie to customize how the cookie is serialized.

##### `AstroCookieSetOptions.domain`

[Section titled “AstroCookieSetOptions.domain”](#astrocookiesetoptionsdomain)

**Type:** `string`

Specifies the domain. If no domain is set, most clients will interpret to apply to the current domain.

##### `AstroCookieSetOptions.expires`

[Section titled “AstroCookieSetOptions.expires”](#astrocookiesetoptionsexpires)

**Type:** `Date`

Specifies the date on which the cookie will expire.

##### `AstroCookieSetOptions.httpOnly`

[Section titled “AstroCookieSetOptions.httpOnly”](#astrocookiesetoptionshttponly)

**Type:** `boolean`

If true, the cookie will not be accessible client-side.

##### `AstroCookieSetOptions.maxAge`

[Section titled “AstroCookieSetOptions.maxAge”](#astrocookiesetoptionsmaxage)

**Type:** `number`

Specifies a number, in seconds, for which the cookie is valid.

##### `AstroCookieSetOptions.path`

[Section titled “AstroCookieSetOptions.path”](#astrocookiesetoptionspath)

**Type:** `string`

Specifies a subpath of the domain in which the cookie is applied.

##### `AstroCookieSetOptions.partitioned`

[Section titled “AstroCookieSetOptions.partitioned”](#astrocookiesetoptionspartitioned)

**Type:** `boolean`  

**Added in:** `astro@5.17.0`

If true, the cookie is a [partitioned cookie](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Partitioned_cookies). Partitioned cookies can only be read within the context of the top-level site on which they were set, which allows cross-site tracking to be blocked while still enabling legitimate uses of third-party cookies.

Partitioned cookies must be set with `secure: true`.

##### `AstroCookieSetOptions.sameSite`

[Section titled “AstroCookieSetOptions.sameSite”](#astrocookiesetoptionssamesite)

**Type:** `boolean | 'lax' | 'none' | 'strict'`

Specifies the value of the [SameSite](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-09#section-5.4.7) cookie header.

##### `AstroCookieSetOptions.secure`

[Section titled “AstroCookieSetOptions.secure”](#astrocookiesetoptionssecure)

**Type:** `boolean`

If true, the cookie is only set on https sites.

##### `AstroCookieSetOptions.encode()`

[Section titled “AstroCookieSetOptions.encode()”](#astrocookiesetoptionsencode)

**Type:** `(value: string) => string`

Allows customizing how the cookie is serialized.

### `session`

[Section titled “session”](#session)

**Type:** `AstroSession`

**Added in:** `astro@5.7.0`

`session` is an object that allows data to be stored between requests for [routes rendered on demand](/en/guides/on-demand-rendering/). It is associated with a cookie that contains the session ID only: the data itself is not stored in the cookie.

The session is created when first used, and the session cookie is automatically set. The `session` object is `undefined` if no session storage has been configured, or if the current route is prerendered, and will log an error if you try to use it.

See [the session guide](/en/guides/sessions/) for more information on how to use sessions in your Astro project.

#### `session.get()`

[Section titled “session.get()”](#sessionget)

**Type**: `(key: string) => Promise<any>`

Returns the value of the given key in the session. If the key does not exist, it returns `undefined`.

*   [Astro.session](#tab-panel-2024)
*   [context.session](#tab-panel-2025)

```
---const cart = await Astro.session?.get('cart');---<button>🛒 {cart?.length}</button>
```

#### `session.set()`

[Section titled “session.set()”](#sessionset)

**Type**: `(key: string, value: any, options?: { ttl: number }) => void`

Sets the value of the given key in the session. The value can be any serializable type. This method is synchronous and the value is immediately available for retrieval, but it is not saved to the backend until the end of the request. The `ttl` option sets the value’s expiration time, in seconds.

*   [Astro.session](#tab-panel-2026)
*   [context.session](#tab-panel-2027)

```
---const { slug } = Astro.params;Astro.session?.set('lastViewedProduct', slug);---
```

#### `session.regenerate()`

[Section titled “session.regenerate()”](#sessionregenerate)

**Type**: `() => void`

Regenerates the session ID. Call this when a user logs in or escalates their privileges, to prevent session fixation attacks.

*   [Astro.session](#tab-panel-2028)
*   [context.session](#tab-panel-2029)

```
---Astro.session?.regenerate();---
```

#### `session.destroy()`

[Section titled “session.destroy()”](#sessiondestroy)

**Type**: `() => void`

Destroys the session, deleting the cookie and the object from the backend. Call this when a user logs out or their session is otherwise invalidated.

*   [Astro.session](#tab-panel-2030)
*   [context.session](#tab-panel-2031)

```
---Astro.session?.destroy();return Astro.redirect('/login');---
```

#### `session.load()`

[Section titled “session.load()”](#sessionload)

**Type**: `(id: string) => Promise<void>`

Loads a session by ID. In normal use, a session is loaded automatically from the request cookie. Use this method to load a session from a different ID. This is useful if you are handling the session ID yourself, or if you want to keep track of a session without using cookies.

*   [Astro.session](#tab-panel-2032)
*   [context.session](#tab-panel-2033)

```
---// Load the session from a header instead of cookiesconst sessionId = Astro.request.headers.get('x-session-id');await Astro.session?.load(sessionId);const cart = await Astro.session?.get('cart');---<h1>Your cart</h1><ul>  {cart?.map((item) => (    <li>{item.name}</li>  ))}</ul>
```

### `csp`

[Section titled “csp”](#csp)

**Type**: `object | undefined`

**Added in:** `astro@6.0.0`

Astro’s CSP runtime APIs enable support for [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) to help minimize certain types of security threats by controlling which resources a document is allowed to load. This provides additional protection against [cross-site scripting (XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting) attacks.

You can customize the `<meta>` element per page from the `Astro` global inside `.astro` components, or the `APIContext` type in endpoints and middleware.

When resources are inserted multiple times or from multiple sources (e.g. defined in your [`csp` config](/en/reference/configuration-reference/#securitycsp) and added using the following CSP runtime APIs, Astro will merge and deduplicate all resources to create your `<meta>` element.

#### `csp.insertDirective()`

[Section titled “csp.insertDirective()”](#cspinsertdirective)

**Type:** `(directive: CspDirective) => void`  

**Added in:** `astro@6.0.0`

Adds a single directive to the current page. You can call this method multiple times to add additional directives.

```
---Astro.csp?.insertDirective("default-src 'self'");Astro.csp?.insertDirective("img-src 'self' https://images.cdn.example.com");---
```

After the build, the `<meta>` element for this individual page will incorporate your additional directives alongside the existing `script-src` and `style-src` directives:

```
<metahttp-equiv="content-security-policy"content="  default-src 'self';  img-src 'self' https://images.cdn.example.com;  script-src 'self' 'sha256-somehash';  style-src 'self' 'sha256-somehash';  ">
```

#### `csp.insertStyleResource()`

[Section titled “csp.insertStyleResource()”](#cspinsertstyleresource)

**Type:** `(resource: string) => void`  

**Added in:** `astro@6.0.0`

Inserts a new resource to be used for the `style-src` directive.

```
---Astro.csp?.insertStyleResource("https://styles.cdn.example.com");---
```

After the build, the `<meta>` element for this individual page will add your source to the default `style-src` directive:

```
<metahttp-equiv="content-security-policy"content="  script-src 'self' 'sha256-somehash';  style-src https://styles.cdn.example.com 'sha256-somehash';  ">
```

#### `csp.insertStyleHash()`

[Section titled “csp.insertStyleHash()”](#cspinsertstylehash)

**Type:** `(hash: CspHash) => void`  

**Added in:** `astro@6.0.0`

Adds a new hash to the `style-src` directive.

```
---Astro.csp?.insertStyleHash("sha512-styleHash");---
```

After the build, the `<meta>` element for this individual page will add your hash to the default `style-src` directive:

```
<metahttp-equiv="content-security-policy"content="  script-src 'self' 'sha256-somehash';  style-src 'self' 'sha256-somehash' 'sha512-styleHash';  ">
```

#### `csp.insertScriptResource()`

[Section titled “csp.insertScriptResource()”](#cspinsertscriptresource)

**Type:** `(resource: string) => void`  

**Added in:** `astro@6.0.0`

Inserts a new valid source to be used for the `script-src` directive.

```
---Astro.csp?.insertScriptResource("https://scripts.cdn.example.com");---
```

After the build, the `<meta>` element for this individual page will add your source to the default `script-src` directive:

```
<metahttp-equiv="content-security-policy"content="  script-src https://scripts.cdn.example.com 'sha256-somehash';  style-src 'self' 'sha256-somehash';  ">
```

#### `csp.insertScriptHash()`

[Section titled “csp.insertScriptHash()”](#cspinsertscripthash)

**Type:** `(hash: CspHash) => void`  

**Added in:** `astro@6.0.0`

Adds a new hash to the `script-src` directive.

```
---Astro.csp?.insertScriptHash("sha512-scriptHash");---
```

After the build, the `<meta>` element for this individual page will add your hash to the default `script-src` directive:

```
<metahttp-equiv="content-security-policy"content="  script-src 'self' 'sha256-somehash' 'sha512-styleHash';  style-src 'self' 'sha256-somehash';  ">
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


