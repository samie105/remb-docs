---
title: "Create and pass data to a custom blog layout"
source: "https://docs.astro.build/en/tutorial/4-layouts/2/"
canonical_url: "https://docs.astro.build/en/tutorial/4-layouts/2/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:44.304Z"
content_hash: "cb1c57aa51f28d4270e3cce6c4048f80d1835e2eebd2d90c1a2caac803f191c0"
menu_path: ["Create and pass data to a custom blog layout"]
section_path: []
nav_prev: {"path": "astro/en/tutorial/4-layouts/1/index.md", "title": "Build your first layout"}
nav_next: {"path": "astro/en/tutorial/4-layouts/3/index.md", "title": "Combine layouts to get the best of both worlds"}
---

# Create and pass data to a custom blog layout

Now that you have a layout for your pages, it’s time to add a layout for blog posts!

Get ready to…

*   Create a new blog post layout for your Markdown files
*   Pass YAML frontmatter values as props to layout component

## Add a layout to your blog posts

[Section titled “Add a layout to your blog posts”](#add-a-layout-to-your-blog-posts)

When you include the `layout` frontmatter property in an `.md` file, all of your frontmatter YAML values are available to the layout file.

1.  Create a new file at `src/layouts/MarkdownPostLayout.astro`
    
2.  Copy the following code into `MarkdownPostLayout.astro`
    
    ```
    ---const { frontmatter } = Astro.props;---<meta charset="utf-8" /><h1>{frontmatter.title}</h1><p>Written by {frontmatter.author}</p><slot />
    ```
    
3.  Add the following frontmatter property in `post-1.md`
    
    ```
    ---layout: ../../layouts/MarkdownPostLayout.astrotitle: 'My First Blog Post'pubDate: 2022-07-01description: 'This is the first post of my new Astro blog.'author: 'Astro Learner'image:    url: 'https://docs.astro.build/assets/rose.webp'    alt: 'The Astro logo on a dark background with a pink glow.'tags: ["astro", "blogging", "learning in public"]---
    ```
    
4.  Check your browser preview again at `http://localhost:4321/posts/post-1` and notice what the layout has added to your page.
    
5.  Add the same layout property to your two other blog posts `post-2.md` and `post-3.md`. Verify in your browser that your layout is also applied to these posts.
    

## Try it yourself - Customize your blog post layout

[Section titled “Try it yourself - Customize your blog post layout”](#try-it-yourself---customize-your-blog-post-layout)

**Challenge**: Identify items common to every blog post, and use `MarkdownPostLayout.astro` to render them, instead of writing them in your Markdown in `post-1.md` and in every future blog post.

Here’s an example of refactoring your code to include the `pubDate` in the layout component instead of writing it in the body of your Markdown:

```
Published on: 2022-07-01
Welcome to my _new blog_ about learning Astro! Here, I will share my learning journey as I build a new website.
```

```
---const { frontmatter } = Astro.props;---<meta charset="utf-8" /><h1>{frontmatter.title}</h1><p>Published on: {frontmatter.pubDate.toString().slice(0,10)}</p><p>Written by {frontmatter.author}</p><slot />
```

Refactor as much as you think is useful to you, and add as much to your layout as you want, remembering that everything that you add to your layout is one less thing you will write in each and every blog post!

Here is an example of a refactored layout that leaves only individual blog post content rendered by the slot. Feel free to use this, or create your own!

```
---const { frontmatter } = Astro.props;---<meta charset="utf-8" /><h1>{frontmatter.title}</h1><p>{frontmatter.pubDate.toString().slice(0,10)}</p><p><em>{frontmatter.description}</em></p><p>Written by: {frontmatter.author}</p><img src={frontmatter.image.url} width="300" alt={frontmatter.image.alt} /><slot />
```

### Test your knowledge

[Section titled “Test your knowledge”](#test-your-knowledge)

Can you figure out what should go in the blanks so that the following two components together produce working Astro code?

1.  ```
    ---layout: ../../__________/MyMarkdownLayout.astrotitle: "Learning About Markdown in Astro"author: Astro Learner____: 2022-08-08---I learned so much today! Astro allows me to write in Markdown, but also use variables from the frontmatter. I can even access those values in an Astro layout component.
    ```
    
2.  ```
    ---import ____________ from '../components/Footer.astro'const { ___________ } = Astro.props---<h1>{frontmatter.title}</h1><p>Written by: {frontmatter.______} on {frontmatter.pubDate}</p>< _______ /><Footer />
    ```
    
    Show the blanks filled in!
    
    1.  ```
        ---layout: ../../layouts/MyMarkdownLayout.astrotitle: "Learning About Markdown in Astro"author: Astro LearnerpubDate: 2022-08-08---I learned so much today! Astro allows me to write in Markdown, but also use variables from the frontmatter. I can even access those values in an Astro layout component.
        ```
        
    2.  ```
        ---import Footer from '../components/Footer.astro'const { frontmatter } = Astro.props---<h1>{frontmatter.title}</h1><p>Written by: {frontmatter.author} on {frontmatter.pubDate}</p><slot /><Footer />
        ```
        
    

## Checklist

[Section titled “Checklist”](#checklist)

 *    I can add a layout property to a Markdown blog post in its YAML frontmatter.
*    I can create a separate layout for Markdown posts.
*    I can use values from a blog post’s frontmatter in a layout component.

### Resources

[Section titled “Resources”](#resources)

*   [Markdown Layouts in Astro](../../../guides/markdown-content/index.md#frontmatter-layout-property)
    
*   [Markdown Layout Props](../../../basics/layouts/index.md#markdown-layout-props)
    
*   [Introduction to YAML](https://dev.to/paulasantamaria/introduction-to-yaml-125f) external
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
