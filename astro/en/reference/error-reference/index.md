---
title: "Error reference"
source: "https://docs.astro.build/en/reference/error-reference/"
canonical_url: "https://docs.astro.build/en/reference/error-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:15.787Z"
content_hash: "176cece70df306a42f2a372f71f0dfebbfbc4213336a345ac2737f15a8219580"
menu_path: ["Error reference"]
section_path: []
nav_prev: {"path": "astro/en/reference/legacy-flags/index.md", "title": "Legacy flags"}
nav_next: {"path": "astro/en/guides/integrations-guide/alpinejs/index.md", "title": "@astrojs/\n\t\t\t\t\talpinejs"}
---

# Error reference

The following reference is a complete list of the errors you may encounter while using Astro. For additional assistance, including common pitfalls, please also see our [Troubleshooting Guide](../../guides/troubleshooting/index.md).

## Astro Errors

[Section titled “Astro Errors”](#astro-errors)

*   [**UnknownCompilerError**](../errors/unknown-compiler-error/index.md)  
    Unknown compiler error.
*   [**ClientAddressNotAvailable**](../errors/client-address-not-available/index.md)  
    `Astro.clientAddress` is not available in current adapter.
*   [**PrerenderClientAddressNotAvailable**](../errors/prerender-client-address-not-available/index.md)  
    `Astro.clientAddress` cannot be used inside prerendered routes.
*   [**StaticClientAddressNotAvailable**](../errors/static-client-address-not-available/index.md)  
    `Astro.clientAddress` is not available in prerendered pages.
*   [**NoMatchingStaticPathFound**](../errors/no-matching-static-path-found/index.md)  
    No static path found for requested path.
*   [**OnlyResponseCanBeReturned**](../errors/only-response-can-be-returned/index.md)  
    Invalid type returned by Astro page.
*   [**MissingMediaQueryDirective**](../errors/missing-media-query-directive/index.md)  
    Missing value for `client:media` directive.
*   [**NoMatchingRenderer**](../errors/no-matching-renderer/index.md)  
    No matching renderer found.
*   [**NoClientEntrypoint**](../errors/no-client-entrypoint/index.md)  
    No client entrypoint specified in renderer.
*   [**NoClientOnlyHint**](../errors/no-client-only-hint/index.md)  
    Missing hint on `client:only` directive.
*   [**InvalidGetStaticPathParam**](../errors/invalid-get-static-path-param/index.md)  
    Invalid value returned by a `getStaticPaths` path.
*   [**InvalidGetStaticPathsEntry**](../errors/invalid-get-static-paths-entry/index.md)  
    Invalid entry inside getStaticPath’s return value
*   [**InvalidGetStaticPathsReturn**](../errors/invalid-get-static-paths-return/index.md)  
    Invalid value returned by getStaticPaths.
*   [**GetStaticPathsExpectedParams**](../errors/get-static-paths-expected-params/index.md)  
    Missing params property on `getStaticPaths` route.
*   [**GetStaticPathsInvalidRouteParam**](../errors/get-static-paths-invalid-route-param/index.md)  
    Invalid route parameter returned by `getStaticPaths()`.
*   [**GetStaticPathsRequired**](../errors/get-static-paths-required/index.md)  
    `getStaticPaths()` function required for dynamic routes.
*   [**ReservedSlotName**](../errors/reserved-slot-name/index.md)  
    Invalid slot name.
*   [**NoAdapterInstalled**](../errors/no-adapter-installed/index.md)  
    Cannot use Server-side Rendering without an adapter.
*   [**AdapterSupportOutputMismatch**](../errors/adapter-support-output-mismatch/index.md)  
    Adapter does not support server output.
*   [**NoAdapterInstalledServerIslands**](../errors/no-adapter-installed-server-islands/index.md)  
    Cannot use Server Islands without an adapter.
*   [**NoMatchingImport**](../errors/no-matching-import/index.md)  
    No import found for component.
*   [**InvalidPrerenderExport**](../errors/invalid-prerender-export/index.md)  
    Invalid prerender export.
*   [**InvalidComponentArgs**](../errors/invalid-component-args/index.md)  
    Invalid component arguments.
*   [**PageNumberParamNotFound**](../errors/page-number-param-not-found/index.md)  
    Page number param not found.
*   [**ImageMissingAlt**](../errors/image-missing-alt/index.md)  
    Image missing required “alt” property.
*   [**InvalidImageService**](../errors/invalid-image-service/index.md)  
    Error while loading image service.
*   [**MissingImageDimension**](../errors/missing-image-dimension/index.md)  
    Missing image dimensions
*   [**FailedToFetchRemoteImageDimensions**](../errors/failed-to-fetch-remote-image-dimensions/index.md)  
    Failed to retrieve remote image dimensions
*   [**RemoteImageNotAllowed**](../errors/remote-image-not-allowed/index.md)  
    Remote image is not allowed
*   [**UnsupportedImageFormat**](../errors/unsupported-image-format/index.md)  
    Unsupported image format
*   [**UnsupportedImageConversion**](../errors/unsupported-image-conversion/index.md)  
    Unsupported image conversion
*   [**CannotOptimizeSvg**](../errors/cannot-optimize-svg/index.md)  
    Cannot optimize SVG
*   [**PrerenderDynamicEndpointPathCollide**](../errors/prerender-dynamic-endpoint-path-collide/index.md)  
    Prerendered dynamic endpoint has path collision.
*   [**PrerenderRouteConflict**](../errors/prerender-route-conflict/index.md)  
    Prerendered route generates the same path as another route.
*   [**ExpectedImage**](../errors/expected-image/index.md)  
    Expected src to be an image.
*   [**ExpectedImageOptions**](../errors/expected-image-options/index.md)  
    Expected image options.
*   [**ExpectedNotESMImage**](../errors/expected-not-esmimage/index.md)  
    Expected image options, not an ESM-imported image.
*   [**GetImageNotUsedOnServer**](../errors/get-image-not-used-on-server/index.md)  
    `getImage()` must be used on the server.
*   [**IncompatibleDescriptorOptions**](../errors/incompatible-descriptor-options/index.md)  
    Cannot set both `densities` and `widths`
*   [**ImageNotFound**](../errors/image-not-found/index.md)  
    Image not found.
*   [**NoImageMetadata**](../errors/no-image-metadata/index.md)  
    Could not process image metadata.
*   [**CouldNotTransformImage**](../errors/could-not-transform-image/index.md)  
    Could not transform image.
*   [**ResponseSentError**](../errors/response-sent-error/index.md)  
    Unable to set response.
*   [**MiddlewareNoDataOrNextCalled**](../errors/middleware-no-data-or-next-called/index.md)  
    The middleware didn’t return a `Response`.
*   [**MiddlewareNotAResponse**](../errors/middleware-not-aresponse/index.md)  
    The middleware returned something that is not a `Response` object.
*   [**EndpointDidNotReturnAResponse**](../errors/endpoint-did-not-return-aresponse/index.md)  
    The endpoint did not return a `Response`.
*   [**LocalsNotAnObject**](../errors/locals-not-an-object/index.md)  
    Value assigned to `locals` is not accepted.
*   [**LocalsReassigned**](../errors/locals-reassigned/index.md)  
    `locals` must not be reassigned.
*   [**AstroResponseHeadersReassigned**](../errors/astro-response-headers-reassigned/index.md)  
    `Astro.response.headers` must not be reassigned.
*   [**MiddlewareCantBeLoaded**](../errors/middleware-cant-be-loaded/index.md)  
    Can’t load the middleware.
*   [**LocalImageUsedWrongly**](../errors/local-image-used-wrongly/index.md)  
    Local images must be imported.
*   [**AstroGlobUsedOutside**](../errors/astro-glob-used-outside/index.md)  
    Astro.glob() used outside of an Astro file.
*   [**AstroGlobNoMatch**](../errors/astro-glob-no-match/index.md)  
    Astro.glob() did not match any files.
*   [**RedirectWithNoLocation**](../errors/redirect-with-no-location/index.md)  
    A redirect must be given a location with the `Location` header.
*   [**UnsupportedExternalRedirect**](../errors/unsupported-external-redirect/index.md)  
    Unsupported or malformed URL.
*   [**InvalidRedirectDestination**](../errors/invalid-redirect-destination/index.md)  
    Invalid redirect destination.
*   [**InvalidDynamicRoute**](../errors/invalid-dynamic-route/index.md)  
    Invalid dynamic route.
*   [**MissingSharp**](../errors/missing-sharp/index.md)  
    Could not find Sharp.
*   [**UnknownViteError**](../errors/unknown-vite-error/index.md)  
    Unknown Vite Error.
*   [**FailedToLoadModuleSSR**](../errors/failed-to-load-module-ssr/index.md)  
    Could not import file.
*   [**InvalidGlob**](../errors/invalid-glob/index.md)  
    Invalid glob pattern.
*   [**FailedToFindPageMapSSR**](../errors/failed-to-find-page-map-ssr/index.md)  
    Astro couldn’t find the correct page to render
*   [**MissingLocale**](../errors/missing-locale/index.md)  
    The provided locale does not exist.
*   [**MissingIndexForInternationalization**](../errors/missing-index-for-internationalization/index.md)  
    Index page not found.
*   [**IncorrectStrategyForI18n**](../errors/incorrect-strategy-for-i18n/index.md)  
    You can’t use the current function with the current strategy
*   [**NoPrerenderedRoutesWithDomains**](../errors/no-prerendered-routes-with-domains/index.md)  
    Prerendered routes aren’t supported when internationalization domains are enabled.
*   [**MissingMiddlewareForInternationalization**](../errors/missing-middleware-for-internationalization/index.md)  
    Enabled manual internationalization routing without having a middleware.
*   [**InvalidI18nMiddlewareConfiguration**](../errors/invalid-i18n-middleware-configuration/index.md)  
    Invalid internationalization middleware configuration
*   [**CantRenderPage**](../errors/cant-render-page/index.md)  
    Astro can’t render the route.
*   [**UnhandledRejection**](../errors/unhandled-rejection/index.md)  
    Unhandled rejection
*   [**i18nNotEnabled**](../errors/i18n-not-enabled/index.md)  
    i18n Not Enabled
*   [**i18nNoLocaleFoundInPath**](../errors/i18n-no-locale-found-in-path/index.md)  
    The path doesn’t contain any locale
*   [**RouteNotFound**](../errors/route-not-found/index.md)  
    Route not found.
*   [**EnvInvalidVariables**](../errors/env-invalid-variables/index.md)  
    Invalid Environment Variables
*   [**EnvPrefixConflictsWithSecret**](../errors/env-prefix-conflicts-with-secret/index.md)  
    envPrefix conflicts with secret environment variables
*   [**ServerOnlyModule**](../errors/server-only-module/index.md)  
    Module is only available server-side
*   [**RewriteWithBodyUsed**](../errors/rewrite-with-body-used/index.md)  
    Cannot use Astro.rewrite after the request body has been read
*   [**ForbiddenRewrite**](../errors/forbidden-rewrite/index.md)  
    Forbidden rewrite to a static route.
*   [**UnknownFilesystemError**](../errors/unknown-filesystem-error/index.md)  
    An unknown error occurred while reading or writing files to disk.
*   [**CannotExtractFontType**](../errors/cannot-extract-font-type/index.md)  
    Cannot extract the font type from the given URL.
*   [**CannotDetermineWeightAndStyleFromFontFile**](../errors/cannot-determine-weight-and-style-from-font-file/index.md)  
    Cannot determine weight and style from font file.
*   [**CannotFetchFontFile**](../errors/cannot-fetch-font-file/index.md)  
    Cannot fetch the given font file.
*   [**FontFamilyNotFound**](../errors/font-family-not-found/index.md)  
    Font family not found
*   [**UnavailableAstroGlobal**](../errors/unavailable-astro-global/index.md)  
    Unavailable Astro global in getStaticPaths()

## CSS Errors

[Section titled “CSS Errors”](#css-errors)

*   [**UnknownCSSError**](../errors/unknown-csserror/index.md)  
    Unknown CSS Error.
*   [**CSSSyntaxError**](../errors/csssyntax-error/index.md)  
    CSS Syntax Error.

## Markdown Errors

[Section titled “Markdown Errors”](#markdown-errors)

*   [**UnknownMarkdownError**](../errors/unknown-markdown-error/index.md)  
    Unknown Markdown Error.
*   [**MarkdownFrontmatterParseError**](../errors/markdown-frontmatter-parse-error/index.md)  
    Failed to parse Markdown frontmatter.
*   [**InvalidFrontmatterInjectionError**](../errors/invalid-frontmatter-injection-error/index.md)  
    Invalid frontmatter injection.
*   [**MdxIntegrationMissingError**](../errors/mdx-integration-missing-error/index.md)  
    MDX integration missing.
*   [**UnknownConfigError**](../errors/unknown-config-error/index.md)  
    Unknown configuration error.
*   [**ConfigNotFound**](../errors/config-not-found/index.md)  
    Specified configuration file not found.
*   [**ConfigLegacyKey**](../errors/config-legacy-key/index.md)  
    Legacy configuration detected.

## CLI Errors

[Section titled “CLI Errors”](#cli-errors)

*   [**UnknownCLIError**](../errors/unknown-clierror/index.md)  
    Unknown CLI Error.
*   [**GenerateContentTypesError**](../errors/generate-content-types-error/index.md)  
    Failed to generate content types.

## Content Collection Errors

[Section titled “Content Collection Errors”](#content-collection-errors)

*   [**UnknownContentCollectionError**](../errors/unknown-content-collection-error/index.md)  
    Unknown Content Collection Error.
*   [**RenderUndefinedEntryError**](../errors/render-undefined-entry-error/index.md)  
    Attempted to render an undefined content collection entry.
*   [**GetEntryDeprecationError**](../errors/get-entry-deprecation-error/index.md)  
    Invalid use of `getDataEntryById` or `getEntryBySlug` function.
*   [**InvalidContentEntryFrontmatterError**](../errors/invalid-content-entry-frontmatter-error/index.md)  
    Content entry frontmatter does not match schema.
*   [**InvalidContentEntryDataError**](../errors/invalid-content-entry-data-error/index.md)  
    Content entry data does not match schema.
*   [**LegacyContentConfigError**](../errors/legacy-content-config-error/index.md)  
    Legacy content config file found.
*   [**ContentCollectionMissingLoader**](../errors/content-collection-missing-loader/index.md)  
    Content collection is missing a `loader` definition.
*   [**ContentCollectionInvalidType**](../errors/content-collection-invalid-type/index.md)  
    Content collection has an invalid `type` field.
*   [**ContentLoaderReturnsInvalidId**](../errors/content-loader-returns-invalid-id/index.md)  
    Content loader returned an entry with an invalid `id`.
*   [**ContentEntryDataError**](../errors/content-entry-data-error/index.md)  
    Content entry data does not match schema.
*   [**LiveContentConfigError**](../errors/live-content-config-error/index.md)  
    Error in live content config.
*   [**ContentLoaderInvalidDataError**](../errors/content-loader-invalid-data-error/index.md)  
    Content entry is missing an ID
*   [**InvalidContentEntrySlugError**](../errors/invalid-content-entry-slug-error/index.md)  
    Invalid content entry slug.
*   [**ContentSchemaContainsSlugError**](../errors/content-schema-contains-slug-error/index.md)  
    Content Schema should not contain `slug`.
*   [**MixedContentDataCollectionError**](../errors/mixed-content-data-collection-error/index.md)  
    Content and data cannot be in same collection.
*   [**ContentCollectionTypeMismatchError**](../errors/content-collection-type-mismatch-error/index.md)  
    Collection contains entries of a different type.
*   [**DataCollectionEntryParseError**](../errors/data-collection-entry-parse-error/index.md)  
    Data collection entry failed to parse.
*   [**DuplicateContentEntrySlugError**](../errors/duplicate-content-entry-slug-error/index.md)  
    Duplicate content entry slug.
*   [**UnsupportedConfigTransformError**](../errors/unsupported-config-transform-error/index.md)  
    Unsupported transform in content config.
*   [**FileParserNotFound**](../errors/file-parser-not-found/index.md)  
    File parser not found
*   [**FileGlobNotSupported**](../errors/file-glob-not-supported/index.md)  
    Glob patterns are not supported in the file loader

## Action Errors

[Section titled “Action Errors”](#action-errors)

*   [**ActionsWithoutServerOutputError**](../errors/actions-without-server-output-error/index.md)  
    Actions must be used with server output.
*   [**ActionsReturnedInvalidDataError**](../errors/actions-returned-invalid-data-error/index.md)  
    Action handler returned invalid data.
*   [**ActionNotFoundError**](../errors/action-not-found-error/index.md)  
    Action not found.
*   [**ActionCalledFromServerError**](../errors/action-called-from-server-error/index.md)  
    Action unexpected called from the server.
*   [**ActionsCantBeLoaded**](../errors/actions-cant-be-loaded/index.md)  
    Can’t load the Astro actions.

## Session Errors

[Section titled “Session Errors”](#session-errors)

*   [**SessionStorageInitError**](../errors/session-storage-init-error/index.md)  
    Session storage could not be initialized.
*   [**SessionStorageSaveError**](../errors/session-storage-save-error/index.md)  
    Session data could not be saved.

## Cache Errors

[Section titled “Cache Errors”](#cache-errors)

*   [**CacheProviderNotFound**](../errors/cache-provider-not-found/index.md)  
    Cache provider not found.
*   [**CacheNotEnabled**](../errors/cache-not-enabled/index.md)  
    Cache is not enabled.
*   [**CacheQueryConfigConflict**](../errors/cache-query-config-conflict/index.md)  
    Conflicting cache query configuration.

[Contribute](../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
