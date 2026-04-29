---
title: "Astro Content Loader API"
source: "https://docs.astro.build/en/reference/content-loader-reference/"
canonical_url: "https://docs.astro.build/en/reference/content-loader-reference/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:03.967Z"
content_hash: "c4655017173d3eb9e5942660beeb318319c0631adbab6654ee3c3a68f08e93b5"
menu_path: ["Astro Content Loader API"]
section_path: []
nav_prev: {"path": "../renderer-reference/index.md", "title": "Astro Renderer API"}
nav_next: {"path": "../image-service-reference/index.md", "title": "Image Service API"}
---

# Astro Content Loader API

Astro’s Content Loader API allows you to load your data from any source, local or remote, and interact with Astro’s content layer to manage your [content collections](/en/guides/content-collections/).

This API includes two ready-to-use loaders for content stored locally. It also provides tools for building your own custom objects that can load data from any source into content collections.

Learn more about [querying data loaded from build-time loaders](/en/guides/content-collections/#querying-build-time-collections) or [accessing live data from live loaders](/en/guides/content-collections/#accessing-live-data) with guided explanations and example usage in the content collections guide.

## Build-time loaders

[Section titled “Build-time loaders”](#build-time-loaders)

Build-time loaders are objects with a [`load()` method](#loaderload) that is called at build time to fetch data and update the data store. This object can also define a schema for the entries, which can be used to validate the data and generate static types.

Astro’s [`glob()`](#glob-loader) and [`file()`](#file-loader) loaders are examples of object loaders that are provided out-of-the-box for use with local content. For remote content, no prebuilt loaders are provided. You will have to build an object loader or use a [community-published loader](https://astro.build/integrations/?search=&categories%5B%5D=loaders) to retrieve remote content and interact with the data store.

For simple data fetching, you can also [define a loader as an async function](#defining-a-loader-as-a-function) that returns an array or object containing entries.

### `glob()` loader

[Section titled “glob() loader”](#glob-loader)

**Type:** `(options: GlobOptions) => [Loader](#the-loader-object)`  

**Added in:** `astro@5.0.0`

The `glob()` loader creates entries from directories of files from anywhere on the filesystem. The supported file types are Markdown, MDX, Markdoc, JSON, YAML, and TOML files.

This loader accepts an object with the following properties: `pattern`, `base` (optional), `generateId` (optional), and `retainBody` (optional).

```
import { defineCollection } from 'astro:content';import { glob } from 'astro/loaders';
const pages = defineCollection({  /* Retrieve all Markdown files in your pages directory. */  loader: glob({ pattern: "**/*.md", base: "./src/data/pages" }),});const blog = defineCollection({  /* Retrieve all Markdown and MDX files in your blog directory. */  loader: glob({ pattern: "**/*.(md|mdx)", base: "./src/data/blog" }),});const notes = defineCollection({  /* Retrieve all Markdown files in your notes directory and prevent   * the raw body of content files from being stored in the data store. */  loader: glob({    pattern: '**/*.md',    base: './src/data/notes',    retainBody: false  }),});const authors = defineCollection({  /* Retrieve all JSON files in your authors directory while retaining   * uppercase letters in the ID. */  loader: glob({    pattern: '**/*.json',    base: "./src/data/authors",    generateId: ({ entry }) => entry.replace(/\.json$/, ''),  }),});
export const collections = { pages, blog, authors };
```

#### `pattern`

[Section titled “pattern”](#pattern)

**Type:** `string | string[]`

The `pattern` property accepts a string or an array of strings using glob matching (e.g. wildcards, globstars). The patterns must be relative to the base directory of entry files to match.

You can learn more about the syntax to use in the [micromatch documentation](https://github.com/micromatch/micromatch#matching-features). You can also verify the validity of your pattern using an online tool like the [DigitalOcean Glob Tool](https://www.digitalocean.com/community/tools/glob).

#### `base`

[Section titled “base”](#base)

**Type:** `string | URL`  
**Default:** `"."`

A relative path or [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL) to the directory from which to resolve the `pattern`.

#### `generateId()`

[Section titled “generateId()”](#generateid)

**Type:** `(options: GenerateIdOptions) => string`

A callback function that returns a unique string per entry in a collection. It accepts an object as parameter with the following properties:

*   `entry` - the path to the entry file, relative to the base directory
*   `base` - the base directory [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL)
*   `data` - the parsed, unvalidated data of the entry

By default it uses [`github-slugger`](https://github.com/Flet/github-slugger) to generate a slug with [kebab-cased](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case) words.

#### `retainBody`

[Section titled “retainBody”](#retainbody)

**Type:** `boolean`  
**Default:** `true`

**Added in:** `astro@5.17.0`

Whether or not to store the raw body of content files in the data store.

When `retainBody` is `false`, [`entry.body`](/en/reference/modules/astro-content/#collectionentrybody) will be `undefined` instead of containing the raw file contents.

Setting this property to `false` significantly reduces the deployed size of the data store and helps avoid hitting size limits for sites with very large collections.

For Markdown files, the rendered body will still be available in the [`entry.rendered.html` property](#dataentryrenderedhtml), and the [`entry.filePath` property](#dataentryfilepath) will still point to the original file.

For MDX collections, this will dramatically reduce the size of the collection, as there will no longer be any body retained in the store.

### `file()` loader

[Section titled “file() loader”](#file-loader)

**Type:** `(fileName: string, options?: FileOptions) => [Loader](#the-loader-object)`  

**Added in:** `astro@5.0.0`

The `file()` loader creates entries from a single file that contains an array of objects with a unique `id` field, or an object with IDs as keys and entries as values.

It supports JSON, YAML, or TOML files and you can provide a custom `parser` for data files it cannot parse by default, or to parse data asynchronously.

This loader accepts a `fileName` property and an optional options object as second argument:

```
import { defineCollection } from 'astro:content';import { file } from 'astro/loaders';
const authors = defineCollection({  /* Retrieve all entries from a JSON file. */  loader: file("src/data/authors.json"),});const products = defineCollection({  /* Retrieve all entries from a CSV file using a custom parser. */  loader: file("src/data/products.csv", {    parser: (fileContent) => { /* your parser logic */ },  }),});
export const collections = { authors, products };
```

#### `fileName`

[Section titled “fileName”](#filename)

**Type:** `string`

Sets the path to the file to load, relative to the root directory.

#### Options

[Section titled “Options”](#options)

**Type:** `FileOptions`

An optional object with the following properties:

##### `parser()`

[Section titled “parser()”](#parser)

**Type:** `(text: string) => Record<string, Record<string, unknown>> | Array<Record<string, unknown>> | Promise<Record<string, Record<string, unknown>> | Array<Record<string, unknown>>>`

A callback function to create a collection from a file’s contents. Use it when you need to process files other than JSON, YAML, or TOML that not supported by default (e.g. `.csv`) or when using [nested `.json` documents](/en/guides/content-collections/#nested-json-documents).

### Building a loader

[Section titled “Building a loader”](#building-a-loader)

The Content Loader API is flexible and full-featured, allowing for a variety of data fetching options. It is possible to build both simple and complex loaders. Your custom loader will depend on both the source and the shape of your data, as well as how you choose to manage the persistent data storage layer.

Most loaders will export a function that accepts configuration options and returns a [loader object](#the-loader-object) including a `name` for your loader, a `load()` method, and a `schema` defining your entries.

#### Loading collections into the data store

[Section titled “Loading collections into the data store”](#loading-collections-into-the-data-store)

The [`load()`](#loaderload) function returned in the loader object defines how your content is fetched, parsed, validated and updated. It accepts a `context` object that allows you to customize your data handling in a variety of ways and interact with the data store. A typical `load()` function will:

*   Fetch your data from a source.
*   Clear the existing data store.
*   Parse and validate your data entries according to a provided schema.
*   Update the data store with new entries.

The `load()` method also provides helpers to log messages to the console, render content to HTML, watch for changes in dev mode and reload data, provide access to metadata and even the full Astro config, and more.

See the full [`LoaderContext`](#loadercontext) list of properties for all options available to the `load()` function.

#### Providing a schema

[Section titled “Providing a schema”](#providing-a-schema)

Providing a Zod [`schema`](#loaderschema) in your loader allows you to validate your fetched content entries with [`parseData()`](#loadercontextparsedata) before adding them to the data [store](#loadercontextstore). This schema will also be used as the collection’s default schema when one does not exist in `src/content.config.ts` to provide type safety and editor tooling. You do not also need a schema defined in the content collection if the loader provides this property.

However, if the content collection also [defines a schema](/en/guides/content-collections/#defining-the-collection-schema), that schema will be used instead of your loader’s schema. This is to allow users of your loader to extend its schema, or transform data for use in their project. If you are [publishing and distributing a loader](#distributing-your-loader) for others to use, you may wish to document this behavior and encourage users not to define a collection schema themselves, or how to do so safely if they need data returned in a different format.

If you need to dynamically generate the schema based on the configuration options or by introspecting an API, you can use [`createSchema()`](#loadercreateschema) instead.

#### Loader example

[Section titled “Loader example”](#loader-example)

The following example shows a loader that fetches data from a provided feed URL (using a custom `loadFeedData` utility) and updates the data store with new entries each time the site is built:

```
// 1. Import the `Loader` type and any other dependencies neededimport type { Loader } from 'astro/loaders';import { z } from 'astro/zod';import { loadFeedData } from "./feed.js";
// 2. Define any options that your loader needsexport function feedLoader(options: { url: string, apiKey: string }) {  const feedUrl = new URL(options.url);  // 3. Return a loader object  return {    name: "feed-loader",    load: async ({ store, parseData }) => {      const feed = await loadFeedData(feedUrl, options.apiKey);
      store.clear();
      for (const item of feed.items) {        const id = item.guid;        const data = await parseData({          id,          data: item,        });        store.set({          id,          data,        });      }    },    // 4. Define the schema of an entry.    schema: z.object({      // ...    })  } satisfies Loader;}
```

#### Defining your collection with your loader

[Section titled “Defining your collection with your loader”](#defining-your-collection-with-your-loader)

Use your custom loader as the value of the `loader` property when you define your collection in `src/content.config.ts`. Configuration options can be passed to your loader as arguments:

```
import { defineCollection } from 'astro:content';import { feedLoader } from './feed-loader.ts';
const blog = defineCollection({  loader: feedLoader({    url: "https://api.example.com/posts",    apiKey: "my-secret",  }),});
export const collections = { blog };
```

### Defining a loader as a function

[Section titled “Defining a loader as a function”](#defining-a-loader-as-a-function)

For simple data fetches that do not need custom data store handling, validation, logging, or any other helpers provided by the [build-time loader object](#the-loader-object), you can define your loader as a function.

The function can be async and must return either an array of entries that each contain a unique `id` field, or an object where each key is a unique ID and each value is the entry.

This pattern provides a convenient shorthand to accomplish the basic tasks normally performed by the `load()` function to [load collections into the data store](#loading-collections-into-the-data-store). At build-time, the loader will automatically clear the data store and reload all the entries. No further customization options or helpers for data handling are provided.

These loaders are often simple enough that you may choose to define them inline in the `src/content.config.ts` file:

```
import { defineCollection } from "astro:content";
const countries = defineCollection({  loader: async () => {    const response = await fetch("https://restcountries.com/v3.1/all");    const data = await response.json();    // Must return an array of entries with an id property    // or an object with IDs as keys and entries as values    return data.map((country) => ({      id: country.cca3,      ...country,    }));  },});
export const collections = { countries };
```

## Live Loaders

[Section titled “Live Loaders”](#live-loaders)

The Live Loader API is built to handle querying any data in real time. Live loaders can filter incoming data and verify content with type safety. Since live loaders fetch data fresh upon every request, there is no data store to update. These loaders are designed to return either data or an `Error` object to allow you to handle errors gracefully.

### Building a live loader

[Section titled “Building a live loader”](#building-a-live-loader)

Most live loaders will export a function that accepts configuration options and returns a [live loader object](#the-liveloader-object) including a `name` for your loader and two methods to define how to load your collection of entries and how to load a single entry: `loadCollection()` and `loadEntry()`.

#### Loading live data

[Section titled “Loading live data”](#loading-live-data)

To return data about your collection, you must provide a [`loadCollection()`](#liveloaderloadcollection) function that fetches data, and returns an array of content [`entries`](#livedatacollectionentries) or an error.

To return a single live collection entry, you must provide a [`loadEntry()`](#liveloaderloadentry) function that fetches data filtered for a given `id`, and returns a single [`entry`](#livedataentry), `undefined`, or an error.

The data fetching for both of these functions is typically done using a [`try...catch` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) to [handle errors when accessing live data](#error-handling-in-live-loaders).

See the full [Live Loader API](#live-loader-api) for more about the functions and types available for building your live loader.

#### Providing a schema for live loaders

[Section titled “Providing a schema for live loaders”](#providing-a-schema-for-live-loaders)

Live loaders do not include a schema property. Instead, you can provide type safety by [defining a Zod schema for your collection](/en/guides/content-collections/#using-zod-schemas-with-live-collections) in `src/live.config.ts`, or by passing generic types to the `LiveLoader` interface for the data they return.

#### Example live loader

[Section titled “Example live loader”](#example-live-loader)

The following example shows a live loader that defines data fetching from a CMS (using a custom `fetchFromCMS` utility) for both a collection of entries and a single entry, including type safety and error handling:

```
import type { LiveLoader } from 'astro/loaders';import { fetchFromCMS } from './cms-client.js';
interface Article {  id: string;  title: string;  htmlContent: string;  author: string;}
interface EntryFilter {  id: string;}
interface CollectionFilter {  author?: string;}
export function articleLoader(config: { apiKey: string }): LiveLoader<Article, EntryFilter, CollectionFilter> {  return {    name: 'article-loader',    loadCollection: async ({ filter }) => {      try {        const articles = await fetchFromCMS({          apiKey: config.apiKey,          type: 'article',          filter,        });
        return {          entries: articles.map((article) => ({            id: article.id,            data: article,          })),        };      } catch (error) {        return {          error: new Error('Failed to load articles', { cause: error }),        };      }    },    loadEntry: async ({ filter }) => {      try {        // filter will be { id: "some-id" } when called with a string        const article = await fetchFromCMS({          apiKey: config.apiKey,          type: 'article',          id: filter.id,        });
        if (!article) {          return {            error: new Error('Article not found'),          };        }
        return {          id: article.id,          data: article,          rendered: {            html: article.htmlContent,          },        };      } catch (error) {        return {          error: new Error('Failed to load article', { cause: error }),        };      }    },  };}
```

#### Defining your live collection with your loader

[Section titled “Defining your live collection with your loader”](#defining-your-live-collection-with-your-loader)

Use your custom live loader as the value of the `loader` property when you define your collection in `src/live.config.ts`. Configuration options can be passed to your loader as arguments:

```
import { defineLiveCollection } from 'astro:content';import { articleLoader } from './article-loader.ts';
const blog = defineLiveCollection({  loader: articleLoader({    apiKey: "my-secret",  }),});
export const collections = { blog };
```

#### Error handling in live loaders

[Section titled “Error handling in live loaders”](#error-handling-in-live-loaders)

Live loaders return an [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) subclass for errors. You can create [custom error types](#creating-live-loader-error-types) and use them for more specific error handling if needed. If an error is thrown in the live loader, it will be caught and returned, wrapped in a `LiveCollectionError`.

Astro will generate some errors itself, depending on the response from the live loader:

*   If `loadEntry` returns `undefined`, Astro will return a `LiveEntryNotFoundError` to the user.
*   If a schema is defined for the collection and the data does not match the schema, Astro will return a `LiveCollectionValidationError`.
*   If the loader returns an invalid cache hint, Astro will return a `LiveCollectionCacheHintError`. The `cacheHint` field is optional, so if you do not have valid data to return, you can simply omit it.

```
import type { LiveLoader } from 'astro/loaders';import type { MyData } from "./types";import { MyLoaderError } from './errors';
export function myLoader(config): LiveLoader<MyData, never, never, MyLoaderError> {  return {    name: 'my-loader',    loadCollection: async () => {      // Return your custom error type      return {        error: new MyLoaderError('Failed to load', 'LOAD_ERROR'),      };    },    // ...  };}
```

##### Creating live loader error types

[Section titled “Creating live loader error types”](#creating-live-loader-error-types)

You can create custom error types for [errors returned by your loader](#error-handling-in-live-loaders) and pass them as a generic to get proper typing:

```
import type { LiveLoader } from "astro/loaders";import type { MyData } from "./types"
export class MyLoaderError extends Error {  constructor(message: string, public code?: string) {    super(message);    this.name = 'MyLoaderError';  }}
export function myLoader(config): LiveLoader<MyData, never, never, MyLoaderError> {  return {    name: 'my-loader',    loadCollection: async () => {      // Return your custom error type      return {        error: new MyLoaderError('Failed to load', 'LOAD_ERROR'),      };    },    // ...  };}
```

When you use `getLiveCollection()` or `getLiveEntry()`, TypeScript will infer the custom error type, allowing you to handle it appropriately:

```
---export const prerender = false; // Not needed in 'server' mode
import { getLiveEntry } from 'astro:content';import { MyLoaderError } from "../my-loader";
const { entry, error } = await getLiveEntry('products', '123');
if (error) {  if (error instanceof MyLoaderError) {    console.error(`Loader error: ${error.message} (code: ${error.code})`);  } else {    console.error(`Unexpected error: ${error.message}`);  }  return Astro.rewrite('/500');}---
```

#### Defining custom filter types

[Section titled “Defining custom filter types”](#defining-custom-filter-types)

Live loaders can define custom filter types for both `getLiveCollection()` and `getLiveEntry()`. This enables type-safe querying that matches your API’s capabilities, making it easier for users to discover available filters and ensure they are used correctly. If you include JSDoc comments in your filter types, the user will see these in their IDE as hints when using the loader.

```
import type { LiveLoader } from 'astro/loaders';import { fetchProduct, fetchCategory, type Product } from './store-client';
interface CollectionFilter {  category?: string;  /** Minimum price to filter products */  minPrice?: number;  /** Maximum price to filter products */  maxPrice?: number;}
interface EntryFilter {  /** Alias for `sku` */  id?: string;  slug?: string;  sku?: string;}
export function productLoader(config: {  apiKey: string;  endpoint: string;}): LiveLoader<Product, EntryFilter, CollectionFilter> {  return {    name: 'product-loader',    loadCollection: async ({ filter }) => {      // filter is typed as CollectionFilter      const data = await fetchCategory({        apiKey: config.apiKey,        category: filter?.category ?? 'all',        minPrice: filter?.minPrice,        maxPrice: filter?.maxPrice,      });
      return {        entries: data.products.map((product) => ({          id: product.sku,          data: product,        })),      };    },    loadEntry: async ({ filter }) => {      // filter is typed as EntryFilter | { id: string }      const product = await fetchProduct({        apiKey: config.apiKey,        slug: filter.slug,        sku: filter.sku || filter.id,      });      if (!product) {        return {          error: new Error('Product not found'),        };      }      return {        id: product.sku,        data: product,      };    },  };}
```

#### Cache hints

[Section titled “Cache hints”](#cache-hints)

Live loaders can provide cache hints to help with response caching. You can use this data to send HTTP cache headers or otherwise inform your caching strategy.

```
import type { LiveLoader } from "astro/loaders";import { loadStoreProduct, loadStoreProducts, getLastModifiedDate } from "./store";import type { Product, ProductEntryFilter, ProductCollectionFilter } from "./types";
export function myLoader(config): LiveLoader<Product, ProductEntryFilter, ProductCollectionFilter> {  return {    name: 'cached-loader',    loadCollection: async ({ filter }) => {      const products = await loadStoreProducts(filter);      return {        entries: products.map((item) => ({          id: item.id,          data: item,          // You can optionally provide cache hints for each entry          cacheHint: {            tags: [`product-${item.id}`, `category-${item.category}`],          },        })),        cacheHint: {          // All fields are optional, and are combined with each entry's cache hints          // tags are merged from all entries          // lastModified is the most recent lastModified of all entries and the collection          lastModified: getLastModifiedDate(products),          tags: ['products'],        },      };    },    loadEntry: async ({ filter }) => {      const item = await loadStoreProduct(filter);      return {        id: item.id,        data: item,        cacheHint: {          lastModified: new Date(item.lastModified),          tags: [`product-${item.id}`, `category-${item.category}`],        },      };    },  };}
```

You can then use these hints in your pages. If you have [experimental route caching](/en/reference/experimental-flags/route-caching/) enabled, pass cache hints directly to `Astro.cache.set()`:

```
---export const prerender = false; // Not needed in 'server' mode
import { getLiveEntry } from 'astro:content';
const { entry, error, cacheHint } = await getLiveEntry('products', Astro.params.id);
if (error) {  return Astro.redirect('/404');}
// Pass cache hints to route cachingif (cacheHint) {  Astro.cache.set(cacheHint);}Astro.cache.set({ maxAge: 300 });---
<h1>{entry.data.name}</h1><p>{entry.data.description}</p>
```

Without route caching enabled, you can use cache hints to set response headers manually for your own caching strategy:

```
---export const prerender = false; // Not needed in 'server' mode
import { getLiveEntry } from 'astro:content';
const { entry, error, cacheHint } = await getLiveEntry('products', Astro.params.id);
if (error) {  return Astro.redirect('/404');}
if (cacheHint?.tags) {  Astro.response.headers.set('Cache-Tag', cacheHint.tags.join(','));}
if (cacheHint?.lastModified) {  Astro.response.headers.set('Last-Modified', cacheHint.lastModified.toUTCString());}---
<h1>{entry.data.name}</h1><p>{entry.data.description}</p>
```

## Distributing your loader

[Section titled “Distributing your loader”](#distributing-your-loader)

Loaders can be defined in your site or as a separate npm package. If you want to share your loader with the community, you can [publish it to npm with the `withastro` and `astro-loader` keywords](/en/guides/integrations/#packagejson-data).

A loader should export a function that returns a `LiveLoader` object for live loaders or a `Loader` object for build-time loaders, allowing users to configure it with their own settings.

## Object loader API

[Section titled “Object loader API”](#object-loader-api)

**Added in:** `astro@5.0.0`

This section shows the API for defining a [build-time object loader](#building-a-loader).

### The `Loader` object

[Section titled “The Loader object”](#the-loader-object)

**Type:** `Loader`

A loader function returns an object with two required properties. In addition to providing a name for the loader, this object describes how to fetch the collection data.

Optionally, you can return a third property defining a schema to validate your collection entries. Use the [Typescript `satisfies` operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator) instead of a return type annotation to provide type safety inside your loader object and to preserve type inference when your loader is used in a collection.

#### `Loader.name`

[Section titled “Loader.name”](#loadername)

**Type:** `string`

**Added in:** `astro@5.0.0`

A unique name for the loader, used in logs and [for conditional loading](/en/reference/integrations-reference/#refreshcontent-option).

#### `Loader.load()`

[Section titled “Loader.load()”](#loaderload)

**Type:** `(context: [LoaderContext](#loadercontext)) => Promise<void>`

**Added in:** `astro@5.0.0`

An async function that is called at build time to load data and update the store. It is passed a [`LoaderContext`](#loadercontext) object that contains helper functions and properties for writing your loader’s implementation logic, as well as the `store` database and methods for interacting with it.

#### `Loader.schema`

[Section titled “Loader.schema”](#loaderschema)

**Type:** `ZodSchema`

**Added in:** `astro@5.0.0`

An optional [Zod schema](/en/guides/content-collections/#defining-datatypes-with-zod) that defines the shape of the entries. It is used to both validate the data and also to generate TypeScript types for the collection.

When you need to dynamically generate the schema at build time based on configuration options or by introspecting an API, use [`createSchema()`](#loadercreateschema) instead.

If present, it will be overridden by any Zod `schema` defined for the collection in the `src/content.config.ts` file.

#### `Loader.createSchema()`

[Section titled “Loader.createSchema()”](#loadercreateschema)

**Type:** `() => Promise<{ schema: ZodSchema; types: string }>`

**Added in:** `astro@6.0.0`

An optional async function that returns an object containing a [Zod schema](/en/guides/content-collections/#defining-datatypes-with-zod) and types. It is used to dynamically generate the schema at build time based on the configuration options or by introspecting an API.

When you only need to provide a static schema, provide a Zod validation object using [`schema`](#loaderschema) instead.

If present, it will be overridden by any Zod `schema` defined for the collection in the `src/content.config.ts` file.

The returned `types` contents will be written to a TypeScript file, and must export an `Entry` type or interface:

```
import type { Loader } from 'astro/loaders';import { z } from 'astro/zod';import { loadFeedData, getSchema, getTypes } from "./feed.js";
export function myLoader(options: { url: string, apiKey: string }) {  const feedUrl = new URL(options.url);
  return {    name: "feed-loader",    load: async ({ store, parseData }) => {      const feed = await loadFeedData(feedUrl, options.apiKey);
      store.clear();
      for (const item of feed.items) {        const id = item.guid;        const data = await parseData({          id,          data: item,        });        store.set({          id,          data,        });      }    },    createSchema: async () => {      const schema = await getSchema();      const types = await getTypes();
      return {        schema,        types: `export type Entry = ${types}`,      };    },  } satisfies Loader;}
```

### `LoaderContext`

[Section titled “LoaderContext”](#loadercontext)

This object is passed to the [`load()`](#loaderload) method of the loader, and contains the following properties:

#### `LoaderContext.collection`

[Section titled “LoaderContext.collection”](#loadercontextcollection)

**Type:** `string`

**Added in:** `astro@5.0.0`

The unique name of the collection. This is the key in the `collections` object in the `src/content.config.ts` file.

#### `LoaderContext.store`

[Section titled “LoaderContext.store”](#loadercontextstore)

**Type:** [`DataStore`](#datastore)

**Added in:** `astro@5.0.0`

A database to store the actual data. Use this to update the store with new entries. See [`DataStore`](#datastore) for more information.

#### `LoaderContext.meta`

[Section titled “LoaderContext.meta”](#loadercontextmeta)

**Type:** `MetaStore`

**Added in:** `astro@5.0.0`

A key-value store scoped to the collection, designed for things like sync tokens and last-modified times. This metadata is persisted between builds alongside the collection data but is only available inside the loader.

```
const lastModified = meta.get("lastModified");// ...meta.set("lastModified", new Date().toISOString());
```

#### `LoaderContext.logger`

[Section titled “LoaderContext.logger”](#loadercontextlogger)

**Type:** [`AstroIntegrationLogger`](/en/reference/integrations-reference/#astrointegrationlogger)

**Added in:** `astro@5.0.0`

A logger that can be used to log messages to the console. Use this instead of `console.log` for more helpful logs that include loader-specific content such as the loader name or information about the loading process in the log message. See [`AstroIntegrationLogger`](/en/reference/integrations-reference/#astrointegrationlogger) for more information.

```
return {  name: 'file-loader',  load: async ({ config, store, logger, watcher }) => {    const url = new URL(fileName, config.root);    const filePath = fileURLToPath(url);    await syncData(filePath, store);
    watcher?.on('change', async (changedPath) => {      if (changedPath === filePath) {        logger.info(`Reloading data from ${fileName}`);        await syncData(filePath, store);      }    });  },};
```

#### `LoaderContext.config`

[Section titled “LoaderContext.config”](#loadercontextconfig)

**Type:** `AstroConfig`

**Added in:** `astro@5.0.0`

The full, resolved Astro configuration object with all defaults applied. See [the configuration reference](/en/reference/configuration-reference/) for more information.

```
return {  name: 'file-loader',  load: async ({ config, store, logger, watcher }) => {    const url = new URL(fileName, config.root);    const filePath = fileURLToPath(url);    await syncData(filePath, store);
    watcher?.on('change', async (changedPath) => {      if (changedPath === filePath) {        logger.info(`Reloading data from ${fileName}`);        await syncData(filePath, store);      }    });  },};
```

#### `LoaderContext.parseData()`

[Section titled “LoaderContext.parseData()”](#loadercontextparsedata)

**Type:** `(props: ParseDataOptions<TData>) => Promise<TData>`

**Added in:** `astro@5.0.0`

Validates and parses the data according to the collection schema. Pass data to this function to validate and parse it before storing it in the data store.

```
import type { Loader } from "astro/loaders";import { loadFeed } from "./feed.js";
export function feedLoader({ url }) {  const feedUrl = new URL(url);  return {    name: "feed-loader",    load: async ({ store, logger, parseData, meta, generateDigest }) => {      logger.info("Loading posts");      const feed = loadFeed(feedUrl);      store.clear();
      for (const item of feed.items) {        const id = item.guid;        const data = await parseData({          id,          data: item,        });        store.set({          id,          data,        });      }    },  } satisfies Loader;}
```

#### `LoaderContext.renderMarkdown()`

[Section titled “LoaderContext.renderMarkdown()”](#loadercontextrendermarkdown)

**Type:** `(content: string, options?: { fileURL?: URL }) => Promise<RenderedContent>`

**Added in:** `astro@5.9.0`

Renders a Markdown string to HTML, returning a `RenderedContent` object.

This allows you to render Markdown content directly within your loaders using the same Markdown processing as Astro’s built-in `glob()` loader and provides access to the `render()` function and `<Content />` component for [rendering body content](/en/guides/content-collections/#rendering-body-content).

Assign this object to the [rendered](#dataentryrendered) field of the [DataEntry](#dataentry) object to allow users to [render the content in a page](/en/guides/content-collections/#rendering-body-content). If the Markdown content includes frontmatter, it will be parsed and available in `metadata.frontmatter`. The frontmatter will be excluded from the HTML output.

```
import type { Loader } from 'astro/loaders';import { loadFromCMS } from './cms.js';
export function myLoader(settings) {  return {    name: 'cms-loader',    async load({ renderMarkdown, store }) {      const entries = await loadFromCMS();
      store.clear();
      for (const entry of entries) {        store.set({          id: entry.id,          data: entry,          // Assume each entry has a 'content' field with markdown content          rendered: await renderMarkdown(entry.content),        });      }    },  } satisfies Loader;}
```

##### `fileURL`

[Section titled “fileURL”](#fileurl)

**Type:** `URL`

**Added in:** `astro@6.0.0`

Specifies the file path to use for resolving relative image paths in Markdown content.

The following example uses the [configured root directory](/en/reference/configuration-reference/#root) to resolve image paths:

```
for (const file of files) {  const content = await readFile(file.path, 'utf8');  store.set({    id: file.id,    data: file.data,    rendered: await renderMarkdown(content, {      fileURL: new URL(file.path, config.root),    }),  });}
```

#### `LoaderContext.generateDigest()`

[Section titled “LoaderContext.generateDigest()”](#loadercontextgeneratedigest)

**Type:** `(data: Record<string, unknown> | string) => string`

**Added in:** `astro@5.0.0`

Generates a non-cryptographic content digest of an object or string. This can be used to track if the data has changed by setting [the `digest` field](#dataentrydigest) of an entry.

```
import type { Loader } from "astro/loaders";import { loadFeed } from "./feed.js";
export function feedLoader({ url }) {  const feedUrl = new URL(url);  return {    name: "feed-loader",    load: async ({ store, logger, parseData, meta, generateDigest }) => {      logger.info("Loading posts");      const feed = loadFeed(feedUrl);      store.clear();
      for (const item of feed.items) {        const id = item.guid;        const data = await parseData({          id,          data: item,        });
        const digest = generateDigest(data);
        store.set({          id,          data,          digest,        });      }    },  } satisfies Loader;}
```

#### `LoaderContext.watcher`

[Section titled “LoaderContext.watcher”](#loadercontextwatcher)

**Type:** `FSWatcher`

**Added in:** `astro@5.0.0`

When running in dev mode, this is a filesystem watcher that can be used to trigger updates. See [`ViteDevServer`](https://vite.dev/guide/api-javascript.html#vitedevserver) for more information.

```
return {  name: 'file-loader',  load: async ({ config, store, watcher }) => {    const url = new URL(fileName, config.root);    const filePath = fileURLToPath(url);    await syncData(filePath, store);
    watcher?.on('change', async (changedPath) => {      if (changedPath === filePath) {        logger.info(`Reloading data from ${fileName}`);        await syncData(filePath, store);      }    });  },};
```

#### `LoaderContext.refreshContextData`

[Section titled “LoaderContext.refreshContextData”](#loadercontextrefreshcontextdata)

**Type:** `Record<string, unknown>`

**Added in:** `astro@5.0.0`

If the loader has been triggered by an integration, this may optionally contain extra data set by that integration. It is only set when the loader is triggered by an integration. See the [`astro:server:setup`](/en/reference/integrations-reference/#refreshcontent-option) hook reference for more information.

```
import type { Loader } from "astro/loaders";import { processWebhook } from "./lib/webhooks";
export function myLoader(options: { url: string }) {  return {    name: "my-loader",    load: async ({ refreshContextData, store, logger }) => {      if(refreshContextData?.webhookBody) {        logger.info("Webhook triggered with body");        processWebhook(store, refreshContextData.webhookBody);      }      // ...    },  } satisfies Loader;}
```

### `DataStore`

[Section titled “DataStore”](#datastore)

The data store is a loader’s interface to the content collection data. It is a key-value (KV) store, scoped to the collection, and therefore a loader can only access the data for its own collection.

#### `DataStore.get()`

[Section titled “DataStore.get()”](#datastoreget)

**Type:** `(key: string) => [DataEntry](#dataentry) | undefined`

**Added in:** `astro@5.0.0`

Get an entry from the store by its ID. Returns `undefined` if the entry does not exist.

```
const existingEntry = store.get("my-entry");
```

The returned object is a [`DataEntry`](#dataentry) object.

#### `DataStore.set()`

[Section titled “DataStore.set()”](#datastoreset)

**Type:** `(entry: [DataEntry](#dataentry)) => boolean`

**Added in:** `astro@5.0.0`

Used after data has been [validated and parsed](#loadercontextparsedata) to add an entry to the store, returning `true` if the entry was set. This returns `false` when the [`digest`](#dataentrydigest) property determines that an entry has not changed and should not be updated.

```
    for (const item of feed.items) {      const id = item.guid;      const data = await parseData({        id,        data: item,      });      const digest = generateDigest(data);      store.set({        id,        data,        rendered: {          html: data.description ?? "",        },        digest,      });    }
```

#### `DataStore.entries()`

[Section titled “DataStore.entries()”](#datastoreentries)

**Type:** `() => Array<[id: string, [DataEntry](#dataentry)]>`

**Added in:** `astro@5.0.0`

Get all entries in the collection as an array of key-value pairs.

#### `DataStore.keys()`

[Section titled “DataStore.keys()”](#datastorekeys)

**Type:** `() => Array<string>`

**Added in:** `astro@5.0.0`

Get all the keys of the entries in the collection.

#### `DataStore.values()`

[Section titled “DataStore.values()”](#datastorevalues)

**Type:** `() => Array<[DataEntry](#dataentry)>`

**Added in:** `astro@5.0.0`

Get all entries in the collection as an array.

#### `DataStore.delete()`

[Section titled “DataStore.delete()”](#datastoredelete)

**Type:** `(key: string) => void`

**Added in:** `astro@5.0.0`

Delete an entry from the store by its ID.

#### `DataStore.clear()`

[Section titled “DataStore.clear()”](#datastoreclear)

**Type:** `() => void`

**Added in:** `astro@5.0.0`

Clear all entries from the collection.

#### `DataStore.has()`

[Section titled “DataStore.has()”](#datastorehas)

**Type:** `(key: string) => boolean`

**Added in:** `astro@5.0.0`

Check if an entry exists in the store by its ID.

### `DataEntry`

[Section titled “DataEntry”](#dataentry)

This is the type of the object that is stored in the data store. It has the following properties:

#### `DataEntry.id`

[Section titled “DataEntry.id”](#dataentryid)

**Type:** `string`

**Added in:** `astro@5.0.0`

An identifier for the entry, which must be unique within the collection. This is used to look up the entry in the store and is the key used with [`getEntry()`](/en/reference/modules/astro-content/#getentry) for that collection.

#### `DataEntry.data`

[Section titled “DataEntry.data”](#dataentrydata)

**Type:** `Record<string, unknown>`

**Added in:** `astro@5.0.0`

The actual data for the entry. When a user accesses the collection, this will have TypeScript types generated according to the collection schema.

It is the loader’s responsibility to use [`parseData()`](#loadercontextparsedata) to validate and parse the data before storing it in the data store: no validation is done when getting or setting the data.

#### `DataEntry.filePath`

[Section titled “DataEntry.filePath”](#dataentryfilepath)

**Type:** `string | undefined`

**Added in:** `astro@5.0.0`

A path to the file that is the source of this entry, relative to the root of the site. This only applies to file-based loaders and is used to resolve paths such as images or other assets.

If not set, then any fields in the schema that use [the `image()` helper](/en/guides/images/#images-in-content-collections) will be treated as [public paths](/en/guides/images/#where-to-store-images) and not transformed.

#### `DataEntry.body`

[Section titled “DataEntry.body”](#dataentrybody)

**Type:** `string | undefined`

**Added in:** `astro@5.0.0`

The raw body of the entry, if applicable. If the entry includes [rendered content](#dataentryrendered), then this field can be used to store the raw source. This is optional and is not used internally.

#### `DataEntry.digest`

[Section titled “DataEntry.digest”](#dataentrydigest)

**Type:** `string | undefined`

**Added in:** `astro@5.0.0`

An optional content digest for the entry. This can be used to check if the data has changed.

When [setting an entry](#datastoreset), the entry will only update if the digest does not match an existing entry with the same ID.

The format of the digest is up to the loader, but it must be a string that changes when the data changes. This can be done with the [`generateDigest`](#loadercontextgeneratedigest) function.

#### `DataEntry.rendered`

[Section titled “DataEntry.rendered”](#dataentryrendered)

**Type:** `RenderedContent | undefined`

**Added in:** `astro@5.0.0`

Stores an object with an entry’s rendered content and metadata if it has been rendered to HTML. For example, this can be used to store the rendered content of a Markdown entry, or HTML from a CMS.

If this field is provided, then [the `render()` function and `<Content />` component](/en/guides/content-collections/#rendering-body-content) are available to render the entry in a page.

If the entry has Markdown content then you can use the [`renderMarkdown()`](#loadercontextrendermarkdown) function to generate this object from the Markdown string.

##### `DataEntry.rendered.html`

[Section titled “DataEntry.rendered.html”](#dataentryrenderedhtml)

**Type:** `string`

Contains the rendered HTML string. This is used by [`render()`](/en/reference/modules/astro-content/#render) to return a component that renders this HTML.

##### `DataEntry.rendered.metadata`

[Section titled “DataEntry.rendered.metadata”](#dataentryrenderedmetadata)

**Type:** `object | undefined`

Describes the metadata present in this file. This includes the `imagePaths`, the `headings`, the `frontmatter`, and any other metadata present in the file. When the file has not been rendered as HTML, this value will be `undefined`.

###### `DataEntry.rendered.metadata.imagePaths`

[Section titled “DataEntry.rendered.metadata.imagePaths”](#dataentryrenderedmetadataimagepaths)

**Type:** `string[]`

Specifies the list of images paths present in this entry. Each path is relative to the [entry `filePath`](#dataentryfilepath).

###### `DataEntry.rendered.metadata.headings`

[Section titled “DataEntry.rendered.metadata.headings”](#dataentryrenderedmetadataheadings)

**Type:** `MarkdownHeading[]`

Specifies the list of headings present in this file. Each heading is described by a `depth` determined by the heading level (`h1 -> h6`), a `slug` generated with [`github-slugger`](https://github.com/Flet/github-slugger), and its `text` content.

###### `DataEntry.rendered.metadata.frontmatter`

[Section titled “DataEntry.rendered.metadata.frontmatter”](#dataentryrenderedmetadatafrontmatter)

**Type:** `Record<string, any>`

Describes the raw frontmatter, parsed from the file. This may include [programmatically injected data from remark plugins](/en/guides/markdown-content/#modifying-frontmatter-programmatically).

## Live loader API

[Section titled “Live loader API”](#live-loader-api)

**Added in:** `astro@6.0.0`

This section shows the API for defining a [live loader](#live-loaders).

### The `LiveLoader` object

[Section titled “The LiveLoader object”](#the-liveloader-object)

**Type:** `LiveLoader<TData, TEntryFilter, TCollectionFilter, TError>`

**Added in:** `astro@6.0.0`

A live loader function returns an object with three required live loader properties. In addition to providing a name for the loader, this object describes how to fetch both single entries and an entire collection from your live data source.

Use the `LiveLoader` generic type to provide type safety in your loader. This type accepts the following type parameters, in this order:

*   **`TData`** (defaults to `Record<string, unknown>`): The data structure of each entry returned by the loader.
*   **`TEntryFilter`** (defaults to `never`): The filter object type accepted by [`getLiveEntry()`](/en/reference/modules/astro-content/#getliveentry) and accessible in [`loadEntry()`](#liveloaderloadentry). Use `never` when you don’t support filtering single entries.
*   **`TCollectionFilter`** (defaults to `never`): The filter object type accepted by [`getLiveCollection()`](/en/reference/modules/astro-content/#getlivecollection) and accessible in [`loadCollection()`](#liveloaderloadcollection). Use `never` when you don’t support filtering collections.
*   **`TError`** (defaults to `Error`): A [custom `Error` class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#custom_error_types) that can be returned by the loader for more granular error handling.

#### `LiveLoader.name`

[Section titled “LiveLoader.name”](#liveloadername)

**Type:** `string`

**Added in:** `astro@6.0.0`

A unique name for the loader, used in logs.

#### `LiveLoader.loadCollection()`

[Section titled “LiveLoader.loadCollection()”](#liveloaderloadcollection)

**Type:** `(context: [LoadCollectionContext](#loadcollectioncontext)<TCollectionFilter>) => Promise<[LiveDataCollection](#livedatacollection)<TData> | { error: TError; }>`

**Added in:** `astro@6.0.0`

Defines a method to load a collection of entries. This function receives a [context object](#loadcollectioncontext) containing an optional `filter` property and must return the data associated with this collection or the errors.

#### `LiveLoader.loadEntry()`

[Section titled “LiveLoader.loadEntry()”](#liveloaderloadentry)

**Type:** `(context: [LoadEntryContext](#loadentrycontext)<TEntryFilter>) => Promise<[LiveDataEntry](#livedataentry)<TData> | undefined | { error: TError; }>`

**Added in:** `astro@6.0.0`

Defines a method to load a single entry. This function receives a [context object](#loadentrycontext) containing a `filter` property and returns either the data associated with the requested entry, `undefined` when the entry cannot be found, or the errors.

### `LoadCollectionContext`

[Section titled “LoadCollectionContext”](#loadcollectioncontext)

**Type:** `{ filter?: TCollectionFilter; }`

**Added in:** `astro@6.0.0`

This object is passed to the [`loadCollection()` method](#liveloaderloadcollection) of the loader and contains the following properties:

#### `LoadCollectionContext.filter`

[Section titled “LoadCollectionContext.filter”](#loadcollectioncontextfilter)

**Type:** `Record<string, any> | never`  
**Default:** `never`

**Added in:** `astro@6.0.0`

An object describing the [filters supported by your loader](#defining-custom-filter-types).

### `LoadEntryContext`

[Section titled “LoadEntryContext”](#loadentrycontext)

**Type:** `{ filter: TEntryFilter; }`

**Added in:** `astro@6.0.0`

This object is passed to the [`loadEntry()` method](#liveloaderloadentry) of the loader and contains the following properties:

#### `LoadEntryContext.filter`

[Section titled “LoadEntryContext.filter”](#loadentrycontextfilter)

**Type:** `Record<string, any> | never`  
**Default:** `never`

**Added in:** `astro@6.0.0`

An object describing the [filters supported by your loader](#defining-custom-filter-types).

### `LiveDataEntry`

[Section titled “LiveDataEntry”](#livedataentry)

**Type:** `{ id: string; data: TData; rendered?: { html: string }; cacheHint?: [CacheHint](#cachehint); }`

**Added in:** `astro@6.0.0`

This is the type object that is returned by the [`loadEntry()`](#liveloaderloadentry) method. It contains the following properties:

#### `LiveDataEntry.id`

[Section titled “LiveDataEntry.id”](#livedataentryid)

**Type:** `string`

**Added in:** `astro@6.0.0`

An identifier for the entry, which must be unique within the collection. This is the key used with [`getLiveEntry()`](/en/reference/modules/astro-content/#getliveentry) for that collection.

#### `LiveDataEntry.data`

[Section titled “LiveDataEntry.data”](#livedataentrydata)

**Type:** `Record<string, unknown>`

**Added in:** `astro@6.0.0`

The actual data for the entry. When a user accesses the collection, this will have TypeScript types generated according to the collection schema.

It is the loader’s responsibility to validate and parse the data before returning it.

#### `LiveDataEntry.rendered`

[Section titled “LiveDataEntry.rendered”](#livedataentryrendered)

**Type:** `{ html: string }`

**Added in:** `astro@6.0.0`

An object with an entry’s rendered content if it has been rendered to HTML. For example, this can be the rendered content of a Markdown entry, or HTML from a CMS.

If this field is provided, then [the `render()` function and `<Content />` component](/en/guides/content-collections/#rendering-body-content) are available to render the entry in a page.

If the loader does not return a `rendered` property for an entry, the `<Content />` component will render nothing.

#### `LiveDataEntry.cacheHint`

[Section titled “LiveDataEntry.cacheHint”](#livedataentrycachehint)

**Type:** [`CacheHint`](#cachehint)

**Added in:** `astro@6.0.0`

An optional object to provide a hint for how to cache this specific entry.

### `LiveDataCollection`

[Section titled “LiveDataCollection”](#livedatacollection)

**Type:** `{ entries: Array<[LiveDataEntry](#livedataentry)<TData>>; cacheHint?: [CacheHint](#cachehint); }`

**Added in:** `astro@6.0.0`

This is the type object that is returned by the [`loadCollection()`](#liveloaderloadcollection) method. It contains the following properties:

#### `LiveDataCollection.entries`

[Section titled “LiveDataCollection.entries”](#livedatacollectionentries)

**Type:** `Array<[LiveDataEntry](#livedataentry)<TData>>`

**Added in:** `astro@6.0.0`

An array of [`LiveDataEntry`](#livedataentry) objects.

#### `LiveDataCollection.cacheHint`

[Section titled “LiveDataCollection.cacheHint”](#livedatacollectioncachehint)

**Type:** [`CacheHint`](#cachehint)

**Added in:** `astro@6.0.0`

An optional object providing guidance on how to cache this collection. This object will be merged with the cache hints defined for each individual entry, if provided.

### `CacheHint`

[Section titled “CacheHint”](#cachehint)

An object that loaders can return through the `cacheHint` property in [`LiveDataCollection`](#livedatacollection) or [`LiveDataEntry`](#livedataentry) to provide hints to assist in caching the response. This contains the following properties:

#### `CacheHint.tags`

[Section titled “CacheHint.tags”](#cachehinttags)

**Type:** `Array<string>`

**Added in:** `astro@6.0.0`

An array of string identifiers allowing fine-grained cache control. This allows you to group related content and selectively invalidate cached responses when specific content changes.

The following example defines cache hint tags for a collection of posts filtered by author:

```
return {  /* ... */  cacheHint: {    tags: ["posts", `posts-${filter.author}`],  },};
```

#### `CacheHint.lastModified`

[Section titled “CacheHint.lastModified”](#cachehintlastmodified)

**Type:** `Date`

**Added in:** `astro@6.0.0`

The date of the last modification of the content (e.g., the last update of an entry in a collection). This can be used to set HTTP cache headers like [`Last-Modified`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Last-Modified) and [`If-Modified-Since`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Modified-Since).

The following example defines a cache hint for a single product using its last update date:

```
return {  /* ... */  cacheHint: {    lastModified: new Date(product.updatedAt)  },};
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
