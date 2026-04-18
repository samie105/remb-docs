---
title: "Build your first layout"
source: "https://docs.astro.build/en/tutorial/4-layouts/1/"
canonical_url: "https://docs.astro.build/en/tutorial/4-layouts/1/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:43.041Z"
content_hash: "e7298cc74bd037c9265403190dabc4c7256024b09a8d03ccc80b4901f40b4b7e"
menu_path: ["Build your first layout"]
section_path: []
---
# Build your first layout

Get ready to…

*   Refactor common elements into a page layout
*   Use an Astro `<slot />` element to place page contents within a layout
*   Pass page-specific values as props to its layout

You still have some Astro components repeatedly rendered on every page. It’s time to refactor again to create a shared page layout!

## Create your first layout component

[Section titled “Create your first layout component”](#create-your-first-layout-component)

1.  Create a new file at the location `src/layouts/BaseLayout.astro`. (You will need to create a new `layouts` folder first.)
    
2.  Copy the **entire contents** of `index.astro` into your new file, `BaseLayout.astro`.
    
    ```
    ---import Header from '../components/Header.astro';import Footer from '../components/Footer.astro';import '../styles/global.css';const pageTitle = "Home Page";---<html lang="en">  <head>    <meta charset="utf-8" />    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />    <meta name="viewport" content="width=device-width" />    <meta name="generator" content={Astro.generator} />    <title>{pageTitle}</title>  </head>  <body>    <Header />    <h1>{pageTitle}</h1>    <Footer />    <script>      import "../scripts/menu.js";    </script>  </body></html>
    ```
    

## Use your layout on a page

[Section titled “Use your layout on a page”](#use-your-layout-on-a-page)

3.  Replace the code at `src/pages/index.astro` with the following:
    
    ```
    ---import BaseLayout from '../layouts/BaseLayout.astro';const pageTitle = "Home Page";---<BaseLayout>  <h2>My awesome blog subtitle</h2></BaseLayout>
    ```
    
4.  Check the browser preview again to notice what did (or, spoiler alert: did _not_!) change.
    
5.  Add a `<slot />` element to `src/layouts/BaseLayout.astro` just above the footer component, then check the browser preview of your Home page and notice what really _did_ change this time!
    
    ```
    ---import Header from '../components/Header.astro';import Footer from '../components/Footer.astro';import '../styles/global.css';const pageTitle = "Home Page";---<html lang="en">  <head>    <meta charset="utf-8" />    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />    <meta name="viewport" content="width=device-width" />    <meta name="generator" content={Astro.generator} />    <title>{pageTitle}</title>  </head>  <body>    <Header />    <h1>{pageTitle}</h1>    <slot />    <Footer />    <script>      import "../scripts/menu.js";    </script>  </body></html>
    ```
    

The `<slot />` allows you to inject (or “slot in”) **child content** written between opening and closing `<Component></Component>` tags to any `Component.astro` file.

## Pass page-specific values as props

[Section titled “Pass page-specific values as props”](#pass-page-specific-values-as-props)

6.  Pass the page title to your layout component from `index.astro` using a component attribute:
    
    ```
    ---import BaseLayout from '../layouts/BaseLayout.astro';const pageTitle = "Home Page";---<BaseLayout pageTitle={pageTitle}>  <h2>My awesome blog subtitle</h2></BaseLayout>
    ```
    
7.  Change the script of your `BaseLayout.astro` layout component to receive a page title via `Astro.props` instead of defining it as a constant.
    
    ```
    ---import Header from '../components/Header.astro';import Footer from '../components/Footer.astro';import '../styles/global.css';const pageTitle = "Home Page";const { pageTitle } = Astro.props;---
    ```
    
8.  Check your browser preview to verify that your page title has not changed. It has the same value, but is now being rendered dynamically. And now, each individual page can specify its own title to the layout.
    

## Try it yourself - Use your layout everywhere

[Section titled “Try it yourself - Use your layout everywhere”](#try-it-yourself---use-your-layout-everywhere)

**Refactor** your other pages (`blog.astro` and `about.astro`) so that they use your new `<BaseLayout>` component to render the common page elements.

Don’t forget to:

*   Pass a page title as props via a component attribute.
    
*   Let the layout be responsible for the HTML rendering of any common elements.
    
*   Move any existing `<style>` tags in the page `<head>` with styles you wish to keep to the page HTML template.
    
*   Delete anything from each individual page that is now being handled by the layout, including:
    
    *   HTML elements
    *   Components and their imports
    *   CSS rules in a `<style>` tag (e.g. `<h1>` in your About page)
    *   `<script>` tags

### Test your knowledge

[Section titled “Test your knowledge”](#test-your-knowledge)

1.  An Astro component (`.astro` file) can function as a:
    
2.  To display a page title on the page, you can:
    
3.  Information can be passed from one component to another by:
    

## Checklist

[Section titled “Checklist”](#checklist)

 *    I can create an Astro layout component with a `<slot />`.
*    I can send page-specific properties to a layout.

### Resources

[Section titled “Resources”](#resources)

*   [Astro layout components](/en/basics/layouts/)
    
*   [Astro `<slot />`](/en/basics/astro-components/#slots)
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
