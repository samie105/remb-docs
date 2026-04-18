---
title: "Data fetching"
source: "https://docs.astro.build/en/guides/data-fetching/"
canonical_url: "https://docs.astro.build/en/guides/data-fetching/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:10.798Z"
content_hash: "8d02b8cedfb9f27f39be846a782e200988451a94f1a8999288c8da0229c98747"
menu_path: ["Data fetching"]
section_path: []
nav_prev: {"path": "astro/en/guides/images/index.md", "title": "Images"}
nav_next: {"path": "astro/en/guides/astro-db/index.md", "title": "Astro DB"}
---

# Data fetching

`.astro` files can fetch remote data to help you generate your pages.

## `fetch()` in Astro

[Section titled “fetch() in Astro”](#fetch-in-astro)

All [Astro components](/en/basics/astro-components/) have access to the [global `fetch()` function](https://developer.mozilla.org/en-US/docs/Web/API/fetch) in their component script to make HTTP requests to APIs using the full URL (e.g. `https://example.com/api`). Additionally, you can construct a URL to your project’s pages and endpoints that are rendered on demand on the server using [`new URL("/api", Astro.url)`](/en/reference/api-reference/#url).

This fetch call will be executed at build time, and the data will be available to the component template for generating dynamic HTML. If [SSR](/en/guides/on-demand-rendering/) mode is enabled, any fetch calls will be executed at runtime.

💡 Take advantage of [**top-level `await`**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top_level_await) inside of your Astro component script.

💡 Pass fetched data to both Astro and framework components, as props.

```
---import Contact from "../components/Contact.jsx";import Location from "../components/Location.astro";
const response = await fetch("https://randomuser.me/api/");const data = await response.json();const randomUser = data.results[0];---<!-- Data fetched at build can be rendered in HTML --><h1>User</h1><h2>{randomUser.name.first} {randomUser.name.last}</h2>
<!-- Data fetched at build can be passed to components as props --><Contact client:load email={randomUser.email} /><Location city={randomUser.location.city} />
```

## `fetch()` in Framework Components

[Section titled “fetch() in Framework Components”](#fetch-in-framework-components)

The `fetch()` function is also globally available to any [framework components](/en/guides/framework-components/):

```
import type { FunctionalComponent } from 'preact';
const data = await fetch('https://example.com/movies.json').then((response) => response.json());
// Components that are build-time rendered also log to the CLI.// When rendered with a `client:*` directive, they also log to the browser console.console.log(data);
const Movies: FunctionalComponent = () => {  // Output the result to the page  return <div>{JSON.stringify(data)}</div>;};
export default Movies;
```

## GraphQL queries

[Section titled “GraphQL queries”](#graphql-queries)

Astro can also use `fetch()` to query a GraphQL server with any valid GraphQL query.

```
---const response = await fetch(  "https://swapi-graphql.netlify.app/.netlify/functions/index",  {    method: "POST",    headers: { "Content-Type": "application/json" },    body: JSON.stringify({      query: `        query getFilm ($id:ID!) {          film(id: $id) {            title            releaseDate          }        }      `,      variables: {        id: "ZmlsbXM6MQ==",      },    }),  });

const json = await response.json();const { film } = json.data;---<h1>Fetching information about Star Wars: A New Hope</h1><h2>Title: {film.title}</h2><p>Year: {film.releaseDate}</p>
```

## Fetch from a Headless CMS

[Section titled “Fetch from a Headless CMS”](#fetch-from-a-headless-cms)

Astro components can fetch data from your favorite CMS and then render it as your page content. Using [dynamic routes](/en/guides/routing/#dynamic-routes), components can even generate pages based on your CMS content.

See our [CMS Guides](/en/guides/cms/) for full details on integrating Astro with headless CMSes including Storyblok, Contentful, and WordPress.

## Community resources

[Section titled “Community resources”](#community-resources)

*   [Creating a fullstack app with Astro + GraphQL](https://robkendal.co.uk/blog/how-to-build-astro-site-with-graphql/)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

