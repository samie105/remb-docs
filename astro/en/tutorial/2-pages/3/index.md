---
title: "Add dynamic content about you"
source: "https://docs.astro.build/en/tutorial/2-pages/3/"
canonical_url: "https://docs.astro.build/en/tutorial/2-pages/3/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:22.758Z"
content_hash: "6dda9670f6511f46d4f0af18edfcdebe958c37f2ac2b4c34369b6315d6a6979c"
menu_path: ["Add dynamic content about you"]
section_path: []
nav_prev: {"path": "../2/index.md", "title": "Write your first Markdown blog post"}
nav_next: {"path": "../4/index.md", "title": "Style your About page"}
---

# Add dynamic content about you

Now that you have a multi-page website with HTML content, it’s time to add some dynamic HTML!

Get ready to…

*   Define your page title in frontmatter, and use it in your HTML
*   Conditionally display HTML elements
*   Add some content about you

Any HTML file is valid Astro language. But, you can do more with Astro than just regular HTML!

## Define and use a variable

[Section titled “Define and use a variable”](#define-and-use-a-variable)

Open `about.astro`, which should look like this:

```
------<html lang="en">  <head>    <meta charset="utf-8" />    <meta name="viewport" content="width=device-width" />    <title>Astro</title>  </head>  <body>    <a href="/">Home</a>    <a href="/about/">About</a>    <a href="/blog/">Blog</a>    <h1>About Me</h1>    <h2>... and my new Astro site!</h2>
    <p>I am working through Astro's introductory tutorial. This is the second page on my website, and it's the first one I built myself!</p>
    <p>This site will update as I complete more of the tutorial, so keep checking back and see how my journey is going!</p>  </body></html>
```

1.  Add the following line of JavaScript in the frontmatter script, between the **code fences**:
    
    ```
    ---const pageTitle = "About Me";---
    ```
    
2.  Replace both the static “Astro” title and “About Me” heading in your HTML with the dynamic variable `{pageTitle}`.
    
    ```
    <html lang="en">  <head>    <meta charset="utf-8" />    <meta name="viewport" content="width=device-width" />    <title>Astro</title>    <title>{pageTitle}</title>  </head>  <body>    <a href="/">Home</a>    <a href="/about/">About</a>    <a href="/blog/">Blog</a>    <h1>About Me</h1>    <h1>{pageTitle}</h1>    <h2>... and my new Astro site!</h2>
        <p>I am working through Astro's introductory tutorial. This is the second page on my website, and it's the first one I built myself!</p>
        <p>This site will update as I complete more of the tutorial, so keep checking back and see how my journey is going!</p>  </body></html>
    ```
    
3.  Refresh the live preview of your `/about` page.
    
    Your page text should look the same, and your page title displayed in your browser tab should now read “About Me” instead of “Astro.”
    
    Instead of typing text directly into HTML tags, you just **defined and then used a variable** in the two sections of your `.astro` file, respectively.
    
4.  Use the same pattern to create a `pageTitle` value to use in `index.astro` (“Home Page”) and `blog.astro` (“My Astro Learning Blog”). Update the HTML of these pages in both places so that your page title matches the heading displayed on each page.
    

## Write JavaScript expressions in Astro

[Section titled “Write JavaScript expressions in Astro”](#write-javascript-expressions-in-astro)

1.  Add the following JavaScript to your frontmatter, between the **code fences**:
    
    (You can customize the code for yourself, but this tutorial will use the following example.)
    
    ```
    ---const pageTitle = "About Me";
    const identity = {  firstName: "Sarah",  country: "Canada",  occupation: "Technical Writer",  hobbies: ["photography", "birdwatching", "baseball"],};
    const skills = ["HTML", "CSS", "JavaScript", "React", "Astro", "Writing Docs"];---
    ```
    
2.  Then, add the following code to your HTML template, below your existing content:
    
    ```
    <p>Here are a few facts about me:</p><ul>  <li>My name is {identity.firstName}.</li>  <li>I live in {identity.country} and I work as a {identity.occupation}.</li>  {identity.hobbies.length >= 2 &&    <li>Two of my hobbies are: {identity.hobbies[0]} and {identity.hobbies[1]}</li>  }</ul><p>My skills are:</p><ul>  {skills.map((skill) => <li>{skill}</li>)}</ul>
    ```
    

### Test your knowledge

[Section titled “Test your knowledge”](#test-your-knowledge)

1.  A `.astro` file’s frontmatter is written in:
    
2.  In addition to HTML, Astro syntax allows you to include:
    
3.  When do you need to write your JavaScript inside curly braces?
    

## Conditionally render elements

[Section titled “Conditionally render elements”](#conditionally-render-elements)

You can also use your script variables to choose **whether or not** to render individual elements of your HTML `<body>` content.

1.  Add the following lines to your frontmatter script to **define variables**:
    
    ```
    ---const pageTitle = "About Me";
    const identity = {  firstName: "Sarah",  country: "Canada",  occupation: "Technical Writer",  hobbies: ["photography", "birdwatching", "baseball"],};
    const skills = ["HTML", "CSS", "JavaScript", "React", "Astro", "Writing Docs"];
    const happy = true;const finished = false;const goal = 3;---
    ```
    
2.  Add the following lines below your existing paragraphs.
    
    Then, check the live preview in your browser tab to see what is displayed on the page:
    
    ```
    {happy && <p>I am happy to be learning Astro!</p>}
    {finished && <p>I finished this tutorial!</p>}
    {goal === 3 ? <p>My goal is to finish in 3 days.</p> : <p>My goal is not 3 days.</p>}
    ```
    
3.  Commit your changes to GitHub before moving on. Do this any time you want to save your work and update your live website.
    

### Analyze the Pattern

[Section titled “Analyze the Pattern”](#analyze-the-pattern)

Given the following `.astro` script:

```
---const operatingSystem = "Linux";const quantity = 3;const footwear = "boots";const student = false;---
```

For each Astro template expression, can you predict the HTML (if any!) that will be sent to the browser? Click to reveal if you’re right!

1.  `<p>{operatingSystem}</p>`
    
     `<p>Linux</p>`
    
2.  `{student && <p>I am still in school.</p>}`
    
     Nothing will display because `student` evaluates to false.
    
3.  `<p>I have {quantity + 8} pairs of {footwear}</p>`
    
     `<p>I have 11 pairs of boots</p>`
    
4.  `{operatingSystem === "MacOS" ? <p>I am using a Mac.</p> : <p>I am not using a Mac.</p>}`
    
     `<p>I am not using a Mac.</p>`
    

## Checklist

[Section titled “Checklist”](#checklist)

 *    I can define values in and use values in `.astro` files.
*    I can conditionally render HTML elements.

### Resources

[Section titled “Resources”](#resources)

*   [Dynamic expressions in Astro](/en/reference/astro-syntax/#jsx-like-expressions)

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
