---
title: "Make a reusable Navigation component"
source: "https://docs.astro.build/en/tutorial/3-components/1/"
canonical_url: "https://docs.astro.build/en/tutorial/3-components/1/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:30.966Z"
content_hash: "3568e81fd8fc481a2aa417f6ffa084f9a3cd1ee769d31af7810bff761df48e6c"
menu_path: ["Make a reusable Navigation component"]
section_path: []
nav_prev: {"path": "astro/en/tutorial/2-pages/5/index.md", "title": "Add site-wide styling"}
nav_next: {"path": "astro/en/tutorial/3-components/2/index.md", "title": "Create a social media footer"}
---

# Make a reusable Navigation component

Now that you have the same HTML written in multiple pages of your Astro site, it’s time to replace that duplicated content with a reusable Astro component!

Get ready to…

*   Create a new folder for components
*   Build an Astro component to display your navigation links
*   Replace existing HTML with a new, reusable navigation component

## Create a new `src/components/` folder

[Section titled “Create a new src/components/ folder”](#create-a-new-srccomponents-folder)

To hold `.astro` files that will generate HTML but that will not become new pages on your website, you will need a new folder in your project: `src/components/`.

[Section titled “Create a Navigation component”](#create-a-navigation-component)

1.  Create a new file: `src/components/Navigation.astro`.
    
2.  Copy your links to navigate between pages from the top of any page and paste them into your new file, `Navigation.astro`:
    
    ```
    ------<a href="/">Home</a><a href="/about/">About</a><a href="/blog/">Blog</a>
    ```
    

[Section titled “Import and use Navigation.astro”](#import-and-use-navigationastro)

1.  Go back to `index.astro` and import your new component inside the code fence:
    
    ```
    ---import Navigation from '../components/Navigation.astro';import "../styles/global.css";
    const pageTitle = "Home Page";---
    ```
    
2.  Then below, replace the existing navigation HTML link elements with the new navigation component you just imported:
    
    ```
    <a href="/">Home</a><a href="/about/">About</a><a href="/blog/">Blog</a><Navigation />
    ```
    
3.  Check the preview in your browser and notice that it should look exactly the same… and that’s what you want!
    

Your site contains the same HTML as it did before. But now, those three lines of code are provided by your `<Navigation />` component.

[Section titled “Try it yourself - Add navigation to the rest of your site”](#try-it-yourself---add-navigation-to-the-rest-of-your-site)

Import and use the `<Navigation />` component in the other two pages on your site (`about.astro` and `blog.astro`) using the same method.

Don’t forget to

*   Add an import statement at the top of the component script, inside the code fence.
*   Replace the existing code with the navigation component.

### Test your knowledge

[Section titled “Test your knowledge”](#test-your-knowledge)

1.  You can do this when you have elements repeated on multiple pages:
    
2.  Astro components are:
    
3.  Astro components will automatically create a new page on your site when you…
    

## Checklist

[Section titled “Checklist”](#checklist)

 *    I can refactor content into reusable components.
*    I can add a new component to an `.astro` page.

### Resources

[Section titled “Resources”](#resources)

*   [Astro Component Overview](/en/basics/astro-components/)
    
*   [Refactoring](https://refactoring.com/) external
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)

