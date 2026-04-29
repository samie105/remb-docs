---
title: "JavaScript in JSX with Curly Braces"
source: "https://react.dev/learn/javascript-in-jsx-with-curly-braces"
canonical_url: "https://react.dev/learn/javascript-in-jsx-with-curly-braces"
docset: "react"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:34.133Z"
content_hash: "79e2654050720cc5e2e245d338ff9f75fe005a753bbec8803916f142f87b2907"
menu_path: ["JavaScript in JSX with Curly Braces"]
section_path: []
nav_prev: {"path": "react/learn/writing-markup-with-jsx/index.md", "title": "Writing Markup with JSX"}
nav_next: {"path": "react/learn/passing-props-to-a-component/index.md", "title": "Passing Props to a Component"}
---

JSX lets you write HTML-like markup inside a JavaScript file, keeping rendering logic and content in the same place. Sometimes you will want to add a little JavaScript logic or reference a dynamic property inside that markup. In this situation, you can use curly braces in your JSX to open a window to JavaScript.

### You will learn

*   How to pass strings with quotes
*   How to reference a JavaScript variable inside JSX with curly braces
*   How to call a JavaScript function inside JSX with curly braces
*   How to use a JavaScript object inside JSX with curly braces

## Passing strings with quotes[](#passing-strings-with-quotes "Link for Passing strings with quotes ")

When you want to pass a string attribute to JSX, you put it in single or double quotes:

Here, `"https://react.dev/images/docs/scientists/7vQD0fPs.jpg"` and `"Gregorio Y. Zara"` are being passed as strings.

But what if you want to dynamically specify the `src` or `alt` text? You could **use a value from JavaScript by replacing `"` and `"` with `{` and `}`**:

Notice the difference between `className="avatar"`, which specifies an `"avatar"` CSS class name that makes the image round, and `src={avatar}` that reads the value of the JavaScript variable called `avatar`. That’s because curly braces let you work with JavaScript right there in your markup!

## Using curly braces: A window into the JavaScript world[](#using-curly-braces-a-window-into-the-javascript-world "Link for Using curly braces: A window into the JavaScript world ")

JSX is a special way of writing JavaScript. That means it’s possible to use JavaScript inside it—with curly braces `{ }`. The example below first declares a name for the scientist, `name`, then embeds it with curly braces inside the `<h1>`:

Try changing the `name`’s value from `'Gregorio Y. Zara'` to `'Hedy Lamarr'`. See how the list title changes?

Any JavaScript expression will work between curly braces, including function calls like `formatDate()`:

### Where to use curly braces[](#where-to-use-curly-braces "Link for Where to use curly braces ")

You can only use curly braces in two ways inside JSX:

1.  **As text** directly inside a JSX tag: `<h1>{name}'s To Do List</h1>` works, but `<{tag}>Gregorio Y. Zara's To Do List</{tag}>` will not.
2.  **As attributes** immediately following the `=` sign: `src={avatar}` will read the `avatar` variable, but `src="{avatar}"` will pass the string `"{avatar}"`.

## Using “double curlies”: CSS and other objects in JSX[](#using-double-curlies-css-and-other-objects-in-jsx "Link for Using “double curlies”: CSS and other objects in JSX ")

In addition to strings, numbers, and other JavaScript expressions, you can even pass objects in JSX. Objects are also denoted with curly braces, like `{ name: "Hedy Lamarr", inventions: 5 }`. Therefore, to pass a JS object in JSX, you must wrap the object in another pair of curly braces: `person={{ name: "Hedy Lamarr", inventions: 5 }}`.

You may see this with inline CSS styles in JSX. React does not require you to use inline styles (CSS classes work great for most cases). But when you need an inline style, you pass an object to the `style` attribute:

Try changing the values of `backgroundColor` and `color`.

You can really see the JavaScript object inside the curly braces when you write it like this:

```
<ul style={{backgroundColor: 'black',color: 'pink'}}>
```

The next time you see `{{` and `}}` in JSX, know that it’s nothing more than an object inside the JSX curlies!

### Pitfall

Inline `style` properties are written in camelCase. For example, HTML `<ul style="background-color: black">` would be written as `<ul style={{ backgroundColor: 'black' }}>` in your component.

## More fun with JavaScript objects and curly braces[](#more-fun-with-javascript-objects-and-curly-braces "Link for More fun with JavaScript objects and curly braces ")

You can move several expressions into one object, and reference them in your JSX inside curly braces:

In this example, the `person` JavaScript object contains a `name` string and a `theme` object:

```
const person = {name: 'Gregorio Y. Zara',theme: {backgroundColor: 'black',color: 'pink'}};
```

The component can use these values from `person` like so:

```
<div style={person.theme}><h1>{person.name}'s Todos</h1>
```

JSX is very minimal as a templating language because it lets you organize data and logic using JavaScript.

## Recap[](#recap "Link for Recap")

Now you know almost everything about JSX:

*   JSX attributes inside quotes are passed as strings.
*   Curly braces let you bring JavaScript logic and variables into your markup.
*   They work inside the JSX tag content or immediately after `=` in attributes.
*   `{{` and `}}` is not special syntax: it’s a JavaScript object tucked inside JSX curly braces.

#### 

Challenge

1

of

3:

Fix the mistake[](#fix-the-mistake "Link for this heading")

This code crashes with an error saying `Objects are not valid as a React child`:

Can you find the problem?
