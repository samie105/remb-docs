---
title: "Language Middleware ​"
source: "https://hono.dev/docs/middleware/builtin/language"
canonical_url: "https://hono.dev/docs/middleware/builtin/language"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:56.492Z"
content_hash: "e14eaa3417686861685f49bbddf982bb0ef643aad331dd0114648b99aedcc244"
menu_path: ["Language Middleware ​"]
section_path: []
---
## Language Middleware [​](#language-middleware)

The Language Detector middleware automatically determines a user's preferred language (locale) from various sources and makes it available via `c.get('language')`. Detection strategies include query parameters, cookies, headers, and URL path segments. Perfect for internationalization (i18n) and locale-specific content.

## Import [​](#import)

ts

```
import { Hono } from 'hono'
import { languageDetector } from 'hono/language'
```

## Basic Usage [​](#basic-usage)

Detect language from query string, cookie, and header (default order), with fallback to English:

ts

```
const app = new Hono()

app.use(
  languageDetector({
    supportedLanguages: ['en', 'ar', 'ja'], // Must include fallback
    fallbackLanguage: 'en', // Required
  })
)

app.get('/', (c) => {
  const lang = c.get('language')
  return c.text(`Hello! Your language is ${lang}`)
})
```

### Client Examples [​](#client-examples)

sh

```
# Via path
curl http://localhost:8787/ar/home

# Via query parameter
curl http://localhost:8787/?lang=ar

# Via cookie
curl -H 'Cookie: language=ja' http://localhost:8787/

# Via header
curl -H 'Accept-Language: ar,en;q=0.9' http://localhost:8787/
```

## Default Configuration [​](#default-configuration)

ts

```
export const DEFAULT_OPTIONS: DetectorOptions = {
  order: ['querystring', 'cookie', 'header'],
  lookupQueryString: 'lang',
  lookupCookie: 'language',
  lookupFromHeaderKey: 'accept-language',
  lookupFromPathIndex: 0,
  caches: ['cookie'],
  ignoreCase: true,
  fallbackLanguage: 'en',
  supportedLanguages: ['en'],
  cookieOptions: {
    sameSite: 'Strict',
    secure: true,
    maxAge: 365 * 24 * 60 * 60,
    httpOnly: true,
  },
  debug: false,
}
```

## Key Behaviors [​](#key-behaviors)

### Detection Workflow [​](#detection-workflow)

1.  **Order**: Checks sources in this sequence by default:
    
    *   Query parameter (?lang=ar)
    *   Cookie (language=ar)
    *   Accept-Language header
2.  **Caching**: Stores detected language in a cookie (1 year by default)
    
3.  **Fallback**: Uses `fallbackLanguage` if no valid detection (must be in `supportedLanguages`)
    

## Advanced Configuration [​](#advanced-configuration)

### Custom Detection Order [​](#custom-detection-order)

Prioritize URL path detection (e.g., /en/about):

ts

```
app.use(
  languageDetector({
    order: ['path', 'cookie', 'querystring', 'header'],
    lookupFromPathIndex: 0, // /en/profile → index 0 = 'en'
    supportedLanguages: ['en', 'ar'],
    fallbackLanguage: 'en',
  })
)
```

### Progressive Locale Matching [​](#progressive-locale-matching)

When a detected locale code like `ja-JP` is not in `supportedLanguages`, the middleware progressively truncates subtags to find a match. For example, `zh-Hant-CN` will try `zh-Hant`, then `zh`. An exact match is always preferred.

ts

```
app.use(
  languageDetector({
    supportedLanguages: ['en', 'ja', 'zh-Hant'],
    fallbackLanguage: 'en',
  })
)

// Accept-Language: ja-JP → matches 'ja'
// Accept-Language: zh-Hant-CN → matches 'zh-Hant'
```

### Language Code Transformation [​](#language-code-transformation)

Normalize complex codes (e.g., en-US → en):

ts

```
app.use(
  languageDetector({
    convertDetectedLanguage: (lang) => lang.split('-')[0],
    supportedLanguages: ['en', 'ja'],
    fallbackLanguage: 'en',
  })
)
```

### Cookie Configuration [​](#cookie-configuration)

ts

```
app.use(
  languageDetector({
    lookupCookie: 'app_lang',
    caches: ['cookie'],
    cookieOptions: {
      path: '/', // Cookie path
      sameSite: 'Lax', // Cookie same-site policy
      secure: true, // Only send over HTTPS
      maxAge: 86400 * 365, // 1 year expiration
      httpOnly: true, // Not accessible via JavaScript
      domain: '.example.com', // Optional: specific domain
    },
  })
)
```

To disable cookie caching:

ts

```
languageDetector({
  caches: false,
})
```

### Debugging [​](#debugging)

Log detection steps:

ts

```
languageDetector({
  debug: true, // Shows: "Detected from querystring: ar"
})
```

## Options Reference [​](#options-reference)

### Basic Options [​](#basic-options)

Option

Type

Default

Required

Description

`supportedLanguages`

`string[]`

`['en']`

Yes

Allowed language codes

`fallbackLanguage`

`string`

`'en'`

Yes

Default language

`order`

`DetectorType[]`

`['querystring', 'cookie', 'header']`

No

Detection sequence

`debug`

`boolean`

`false`

No

Enable logging

### Detection Options [​](#detection-options)

Option

Type

Default

Description

`lookupQueryString`

`string`

`'lang'`

Query parameter name

`lookupCookie`

`string`

`'language'`

Cookie name

`lookupFromHeaderKey`

`string`

`'accept-language'`

Header name

`lookupFromPathIndex`

`number`

`0`

Path segment index

### Cookie Options [​](#cookie-options)

Option

Type

Default

Description

`caches`

`CacheType[] | false`

`['cookie']`

Cache settings

`cookieOptions.path`

`string`

`'/'`

Cookie path

`cookieOptions.sameSite`

`'Strict' | 'Lax' | 'None'`

`'Strict'`

SameSite policy

`cookieOptions.secure`

`boolean`

`true`

HTTPS only

`cookieOptions.maxAge`

`number`

`31536000`

Expiration (seconds)

`cookieOptions.httpOnly`

`boolean`

`true`

JS accessibility

`cookieOptions.domain`

`string`

`undefined`

Cookie domain

### Advanced Options [​](#advanced-options)

Option

Type

Default

Description

`ignoreCase`

`boolean`

`true`

Case-insensitive matching

`convertDetectedLanguage`

`(lang: string) => string`

`undefined`

Language code transformer

## Validation & Error Handling [​](#validation-error-handling)

*   `fallbackLanguage` must be in `supportedLanguages` (throws error during setup)
*   `lookupFromPathIndex` must be ≥ 0
*   Invalid configurations throw errors during middleware initialization
*   Failed detections silently use `fallbackLanguage`

## Common Recipes [​](#common-recipes)

### Path-Based Routing [​](#path-based-routing)

ts

```
app.get('/:lang/home', (c) => {
  const lang = c.get('language') // 'en', 'ar', etc.
  return c.json({ message: getLocalizedContent(lang) })
})
```

### Multiple Supported Languages [​](#multiple-supported-languages)

ts

```
languageDetector({
  supportedLanguages: ['en', 'en-GB', 'ar', 'ar-EG'],
  convertDetectedLanguage: (lang) => lang.replace('_', '-'), // Normalize
})
```
