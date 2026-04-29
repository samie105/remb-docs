---
title: "Image Service API"
source: "https://docs.astro.build/en/reference/image-service-reference/"
canonical_url: "https://docs.astro.build/en/reference/image-service-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:20.363Z"
content_hash: "430bf8bf4eebcaef1276d30763b657b0f771d2f02ee563a0874f3b3674b782fa"
menu_path: ["Image Service API"]
section_path: []
nav_prev: {"path": "astro/en/reference/content-loader-reference/index.md", "title": "Astro Content Loader API"}
nav_next: {"path": "astro/en/reference/dev-toolbar-app-reference/index.md", "title": "Dev Toolbar App API"}
---

# Image Service API

`astro:assets` was designed to make it easy for any image optimization service to build a service on top of Astro.

## What is an Image Service?

[Section titled “What is an Image Service?”](#what-is-an-image-service)

Astro provides two types of image services: Local and External.

*   **Local services** handle image transformations directly at build for static sites, or at runtime both in development mode and for on-demand rendering. These are often wrappers around libraries like Sharp, ImageMagick, or Squoosh. In dev mode and in production routes rendered on demand, local services use an API endpoint to do the transformation.
*   **External services** point to URLs and can add support for services such as Cloudinary, Vercel, or any [RIAPI](https://github.com/riapi/riapi)\-compliant server.

## Building using the Image Services API

[Section titled “Building using the Image Services API”](#building-using-the-image-services-api)

Service definitions take the shape of an exported default object with various required methods (“hooks”).

External services provide a `getURL()` that points to the `src` of the output `<img>` tag.

Local services provide a `transform()` method to perform transformations on your image, and `getURL()` and `parseURL()` methods to use an endpoint for dev mode and when rendered on demand.

Both types of services can provide `getHTMLAttributes()` to determine the other attributes of the output `<img>` and `validateOptions()` to validate and augment the passed options.

### External Services

[Section titled “External Services”](#external-services)

An external service points to a remote URL to be used as the `src` attribute of the final `<img>` tag. This remote URL is responsible for downloading, transforming, and returning the image.

```
import type { ExternalImageService, ImageTransform, AstroConfig } from "astro";
const service: ExternalImageService = {  validateOptions(options: ImageTransform, imageConfig: AstroConfig['image']) {    const serviceConfig = imageConfig.service.config;
    // Enforce the user set max width.    if (options.width && options.width > serviceConfig.maxWidth) {      console.warn(`Image width ${options.width} exceeds max width ${serviceConfig.maxWidth}. Falling back to max width.`);      options.width = serviceConfig.maxWidth;    }
    return options;  },  getURL(options, imageConfig) {    return `https://mysupercdn.com/${options.src}?q=${options.quality}&w=${options.width}&h=${options.height}`;  },  getHTMLAttributes(options, imageConfig) {    const { src, format, quality, ...attributes } = options;    return {      ...attributes,      loading: options.loading ?? 'lazy',      decoding: options.decoding ?? 'async',    };  }};

export default service;
```

### Local Services

[Section titled “Local Services”](#local-services)

To create your own local service, you can point to the [built-in endpoint](https://github.com/withastro/astro/blob/main/packages/astro/src/assets/endpoint/generic.ts) (`/_image`), or you can additionally create your own endpoint that can call the service’s methods.

```
import type { ImageTransform, LocalImageService, AstroConfig } from "astro";
const service: LocalImageService<AstroConfig["image"]> = {  getURL(options: ImageTransform, imageConfig) {    const searchParams = new URLSearchParams();    searchParams.append('href', typeof options.src === "string" ? options.src : options.src.src);    options.width && searchParams.append('w', options.width.toString());    options.height && searchParams.append('h', options.height.toString());    options.quality && searchParams.append('q', options.quality.toString());    options.format && searchParams.append('f', options.format);    return `/my_custom_endpoint_that_transforms_images?${searchParams}`;    // Or use the built-in endpoint, which will call your parseURL and transform functions:    // return `/_image?${searchParams}`;  },  parseURL(url: URL, imageConfig) {    const params = url.searchParams;    return {      src: params.get('href')!,      width: params.has('w') ? parseInt(params.get('w')!) : undefined,      height: params.has('h') ? parseInt(params.get('h')!) : undefined,      format: params.get('f'),      quality: params.get('q'),    };  },  async transform(inputBuffer: Uint8Array, options: { src: string, [key: string]: any }, imageConfig) {    const { buffer } = await mySuperLibraryThatEncodesImages(options);    return {      data: buffer,      format: options.format,    };  },  getHTMLAttributes(options, imageConfig) {    let targetWidth = options.width;    let targetHeight = options.height;    if (typeof options.src === "object") {      const aspectRatio = options.src.width / options.src.height;
      if (targetHeight && !targetWidth) {        targetWidth = Math.round(targetHeight * aspectRatio);      } else if (targetWidth && !targetHeight) {        targetHeight = Math.round(targetWidth / aspectRatio);      }    }
    const { src, width, height, format, quality, ...attributes } = options;
    return {      ...attributes,      width: targetWidth,      height: targetHeight,      loading: attributes.loading ?? 'lazy',      decoding: attributes.decoding ?? 'async',    };  },  propertiesToHash: ['src', 'width', 'height', 'format', 'quality'],};export default service;
```

At build time for static sites and pre-rendered routes, both `<Image />` and `getImage(options)` call the `transform()` function. They pass options either through component attributes or an `options` argument, respectively. The transformed images will be built to a `dist/_astro` folder. Their file names will contain a hash of the properties passed to `propertiesToHash`. This property is optional and will default to `['src', 'width', 'height', 'format', 'quality']`. If your custom image service has more options that change the generated images, add these to the array.

In dev mode and when using an adapter to render on demand, Astro doesn’t know ahead of time which images need to be optimized. Astro uses a GET endpoint (by default, `/_image`) to process the images at runtime. `<Image />` and `getImage()` pass their options to `getURL()`, which will return the endpoint URL. Then, the endpoint calls `parseURL()` and passes the resulting properties to `transform()`.

#### getConfiguredImageService & imageConfig

[Section titled “getConfiguredImageService & imageConfig”](#getconfiguredimageservice--imageconfig)

If you implement your own endpoint as an Astro endpoint, you can use [`getConfiguredImageService`](../modules/astro-assets/index.md#getconfiguredimageservice) and [`imageConfig`](../modules/astro-assets/index.md#imageconfig) to call your service’s `parseURL` and `transform` methods and provide the image config.

To access the image service config ([`image.service.config`](../configuration-reference/index.md#imageservice)), you can use `imageConfig.service.config`.

```
import type { APIRoute } from "astro";import { getConfiguredImageService, imageConfig } from 'astro:assets';
export const GET: APIRoute = async ({ request }) => {  const imageService = await getConfiguredImageService();
  const imageTransform = imageService.parseURL(new URL(request.url), imageConfig);  // ... fetch the image from imageTransform.src and store it in inputBuffer  const { data, format } = await imageService.transform(inputBuffer, imageTransform, imageConfig);  return new Response(data, {      status: 200,      headers: {        'Content-Type': mime.getType(format) || ''      }    }  );}
```

[See the built-in endpoint](https://github.com/withastro/astro/blob/main/packages/astro/src/assets/endpoint/generic.ts) for a full example.

## Hooks

[Section titled “Hooks”](#hooks)

### `getURL()`

[Section titled “getURL()”](#geturl)

**Type:** `(options: [ImageTransform](../modules/astro-assets/index.md#imagetransform), imageConfig: [AstroConfig[‘image’]](/en/reference/configuration-reference/#image-options)) => string | Promise<string>`  

**Added in:** `astro@2.1.0`

**Required for local and external services**

For local services, this hook returns the URL of the endpoint that generates your image (for on-demand rendering and in dev mode). It is unused during build. The local endpoint that `getURL()` points to may call both `parseURL()` and `transform()`.

For external services, this hook returns the final URL of the image.

For both types of services, `options` are the properties passed by the user as attributes of the `<Image />` component or as options to `getImage()`.

### `parseURL()`

[Section titled “parseURL()”](#parseurl)

**Type:** `(url: URL, imageConfig: [AstroConfig[‘image’]](/en/reference/configuration-reference/#image-options)) => { src: string, [key: string]: any } | undefined | Promise<{ src: string, [key: string]: any }> | Promise<undefined>`  

**Added in:** `astro@2.1.0`

**Required for local services only; unavailable for external services**

This hook parses the generated URLs by `getURL()` back into an object with the different properties to be used by `transform` (for on-demand rendering and in dev mode). It is unused during build.

### `transform()`

[Section titled “transform()”](#transform)

**Type:** `(inputBuffer: Uint8Array, options: { src: string, [key: string]: any }, imageConfig: [AstroConfig[‘image’]](/en/reference/configuration-reference/#image-options)) => Promise<{ data: Uint8Array; format: [ImageOutputFormat](../modules/astro-assets/index.md#imageoutputformat) }>`  

**Added in:** `astro@2.1.0`

**Required for local services only; unavailable for external services**

This hook transforms and returns the image and is called during the build to create the final asset files.

You must return a `format` to ensure that the proper MIME type is served to users for on-demand rendering and development mode.

### `getHTMLAttributes()`

[Section titled “getHTMLAttributes()”](#gethtmlattributes)

**Type:** `(options: [ImageTransform](../modules/astro-assets/index.md#imagetransform), imageConfig: [AstroConfig[‘image’]](/en/reference/configuration-reference/#image-options) ) => Record<string, any> | Promise<Record<string, any>>`  

**Added in:** `astro@2.1.0`

**Optional for both local and external services**

This hook returns all additional attributes used to render the image as HTML, based on the parameters passed by the user (`options`).

### `getSrcSet()`

[Section titled “getSrcSet()”](#getsrcset)

**Type:** `(options: [ImageTransform](../modules/astro-assets/index.md#imagetransform), imageConfig: [AstroConfig[‘image’]](/en/reference/configuration-reference/#image-options) ) => UnresolvedSrcSetValue[] | Promise<UnresolvedSrcSetValue[]>`  

**Added in:** `astro@3.3.0`

**Optional for both local and external services.**

This hook generates multiple variants of the specified image, for example, to generate a `srcset` attribute on an `<img>` or `<picture>`’s `source`.

This hook returns an array of objects with the following properties:

```
export type UnresolvedSrcSetValue = {  transform: ImageTransform;  descriptor?: string;  attributes?: Record<string, any>;};
```

### `validateOptions()`

[Section titled “validateOptions()”](#validateoptions)

**Type:** `(options: [ImageTransform](../modules/astro-assets/index.md#imagetransform), imageConfig: [AstroConfig[‘image’]](/en/reference/configuration-reference/#image-options) ) => ImageTransform | Promise<ImageTransform>`

**Added in:** `astro@2.1.4`

**Optional for both local and external services**

This hook allows you to validate and augment the options passed by the user. This is useful for setting default options, or telling the user that a parameter is required.

[See how `validateOptions()` is used in Astro built-in services](https://github.com/withastro/astro/blob/0ab6bad7dffd413c975ab00e545f8bc150f6a92f/packages/astro/src/assets/services/service.ts#L124).

### `getRemoteSize()`

[Section titled “getRemoteSize()”](#getremotesize)

**Type:** `(url: string, imageConfig: [AstroConfig[‘image’]](/en/reference/configuration-reference/#image-options) ) => Omit<[ImageMetadata](../modules/astro-assets/index.md#imagemetadata-1), ‘src’ | ‘fsPath’> | Promise<Omit<[ImageMetadata](../modules/astro-assets/index.md#imagemetadata-1), ‘src’ | ‘fsPath’>>`

**Added in:** `astro@6.0.0`

**Optional for both local and external services**

This hook allows you to extend the behavior of [`inferRemoteSize()`](../modules/astro-assets/index.md#inferremotesize). This is useful for reducing network traffic by caching images, or when you can predict image information from the image URL.

## User configuration

[Section titled “User configuration”](#user-configuration)

Configure the image service to use in `astro.config.mjs`. The config takes the following form:

```
import { defineConfig } from "astro/config";
export default defineConfig({  image: {    service: {      entrypoint: "your-entrypoint", // 'astro/assets/services/sharp' | string,      config: {        // ... service-specific config. Optional.      }    }  },});
```

## Typing custom image service props

[Section titled “Typing custom image service props”](#typing-custom-image-service-props)

**Added in:** `astro@5.16.6`

If your image service supports additional props in Astro’s `<Image>` component, `<Picture>` component, or the `getImage()` function, you can add types for these by extending the `Astro.CustomImageProps` interface.

For example, to add a custom `blur` prop that your image service supports:

```
declare namespace Astro {  interface CustomImageProps {    /** Apply a Gaussian blur with this radius to the image. */    blur?: number;  }}
```

You can expose these types to users by making your image service an [Astro integration](../integrations-reference/index.md) and using the [`injectTypes()`](../integrations-reference/index.md#injecttypes-option) helper.

Then, users will be able to get autocomplete and type safety for your custom props:

```
<Image blur="yes" src={myPhoto}  />//     ^^^^^^^^^^//     Type 'string' is not assignable to type 'number | undefined'.
```

[Contribute](../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
