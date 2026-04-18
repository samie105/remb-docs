---
title: "Build it yourself - Header"
source: "https://docs.astro.build/en/tutorial/3-components/3/"
canonical_url: "https://docs.astro.build/en/tutorial/3-components/3/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:35.651Z"
content_hash: "4832964aa69b763cd2ff9d8e9f6859560e199695ff20426dab2ba47dbb789ea3"
menu_path: ["Build it yourself - Header"]
section_path: []
nav_prev: {"path": "astro/en/tutorial/3-components/2/index.md", "title": "Create a social media footer"}
nav_next: {"path": "astro/en/tutorial/3-components/4/index.md", "title": "Send your first script to the browser"}
---

# Build it yourself - Header

Since your site will be viewed on different devices, it’s time to create a page navigation that can respond to multiple screen sizes!

Get ready to…

*   Create a Header for your site that contains the Navigation component
*   Make the Navigation component responsive

## Try it yourself - Build a new Header component

[Section titled “Try it yourself - Build a new Header component”](#try-it-yourself---build-a-new-header-component)

1.  Create a new Header component. Import and use your existing `Navigation.astro` component inside a `<nav>` element which is inside a `<header>` element.
    
    Show me the code!
    
    Create a file named `Header.astro` in `src/components/`
    
    ```
    ---import Navigation from './Navigation.astro';---<header>  <nav>    <Navigation />  </nav></header>
    ```
    

## Try it yourself - Update your pages

[Section titled “Try it yourself - Update your pages”](#try-it-yourself---update-your-pages)

1.  On each page, replace your existing `<Navigation/>` component with your new header.
    
    Show me the code!
    
    ```
    ---import Navigation from '../components/Navigation.astro';import Header from '../components/Header.astro';import Footer from '../components/Footer.astro';import '../styles/global.css';const pageTitle = "Home Page";---<html lang="en">  <head>    <meta charset="utf-8" />    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />    <meta name="viewport" content="width=device-width" />    <meta name="generator" content={Astro.generator} />    <title>{pageTitle}</title>  </head>  <body>    <Navigation />    <Header />    <h1>{pageTitle}</h1>    <Footer />  </body></html>
    ```
    
2.  Check your browser preview and verify that your header is displayed on every page. It won’t look different yet, but if you inspect your preview using dev tools, you will see that you now have elements like `<header>` and `<nav>` around your navigation links.
    

## Add responsive styles

[Section titled “Add responsive styles”](#add-responsive-styles)

1.  Update `Navigation.astro` with the CSS class to control your navigation links. Wrap the existing navigation links in a `<div>` with the class `nav-links` and the id attribute set to `main-menu`.
    
    ```
    ------<div id="main-menu" class="nav-links">  <a href="/">Home</a>  <a href="/about/">About</a>  <a href="/blog/">Blog</a></div>
    ```
    
2.  Copy the CSS styles below into `global.css`. These styles:
    
    *   Style and position the navigation links for mobile
    *   Use a `@media` query to define different styles for larger screen sizes
    
    ```
    html {  background-color: #f1f5f9;  font-family: sans-serif;}
    body {  margin: 0 auto;  width: 100%;  max-width: 80ch;  padding: 1rem;  line-height: 1.5;}
    * {  box-sizing: border-box;}
    h1 {  margin: 1rem 0;  font-size: 2.5rem;}
    /* nav styles */
    .nav-links {  width: 100%;  display: none;  margin: 0;}
    .nav-links a {  display: block;  text-align: center;  padding: 10px 0;  text-decoration: none;  font-size: 1.2rem;  font-weight: bold;  text-transform: uppercase;  color: #0d0950;}
    .nav-links a:hover,.nav-links a:focus {  background-color: #ff9776;}
    @media screen and (min-width: 636px) {  .nav-links {    margin-left: 5em;    display: block;    position: static;    width: auto;    background: none;  }
      .nav-links a {    display: inline-block;    padding: 15px 20px;  }}
    ```
    

Resize your window and look for different styles being applied at different screen widths. Your header is now **responsive** to screen size through the use of `@media` queries.

## Checklist

[Section titled “Checklist”](#checklist)

 *    I can use CSS to add responsive elements to my site.

### Resources

[Section titled “Resources”](#resources)

*   [Component-based Design](https://www.droptica.com/blog/component-based-design/) external
    
*   [Semantic HTML Tags](https://www.dofactory.com/html/semantics) external
    
*   [Mobile-first Design](https://www.mobileapps.com/blog/mobile-first-design) external
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)


