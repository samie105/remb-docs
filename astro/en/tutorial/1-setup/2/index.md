---
title: "Create your first Astro project"
source: "https://docs.astro.build/en/tutorial/1-setup/2/"
canonical_url: "https://docs.astro.build/en/tutorial/1-setup/2/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:08.919Z"
content_hash: "461f37983ebdf5d4bee4326761dfe85499f46400782dd3b802768f75db463eb4"
menu_path: ["Create your first Astro project"]
section_path: []
nav_prev: {"path": "astro/en/tutorial/1-setup/1/index.md", "title": "Prepare your dev environment"}
nav_next: {"path": "astro/en/tutorial/1-setup/3/index.md", "title": "Write your first line of Astro"}
---

# Create your first Astro project

Get ready to…

*   Run the `create astro` setup wizard to create a new Astro project
*   Start the Astro server in development (dev) mode
*   View a live preview of your website in your browser

## Launch the Astro setup wizard

[Section titled “Launch the Astro setup wizard”](#launch-the-astro-setup-wizard)

The preferred way to create a new Astro site is through our `create astro` setup wizard.

1.  In the command line of your terminal, run the following command using your preferred package manager:
    
    *   [npm](#tab-panel-2064)
    *   [pnpm](#tab-panel-2065)
    *   [Yarn](#tab-panel-2066)
    
    ```
    # create a new project with npmnpm create astro@latest
    ```
    
2.  Enter `y` to install `create-astro`.
    
3.  When the prompt asks you where to create the project, type in the name of a folder to create a new directory for your project, e.g. `./tutorial`
    
4.  You will see a short list of starter templates to choose from. Use the arrow keys (up and down) to navigate to the minimal (empty) template, and then press return (enter) to submit your choice.
    
5.  When the prompt asks you whether or not to install dependencies, enter `y`.
    
6.  When the prompt asks you whether or not to initialize a new git repository, enter `y`.
    

When the install wizard is complete, you no longer need this terminal. You can now open VS Code to continue.

## Open your project in VS Code

[Section titled “Open your project in VS Code”](#open-your-project-in-vs-code)

7.  Open VS Code. You will be prompted to open a folder. Choose the folder that you created during the setup wizard.
    
8.  If this is your first time opening an Astro project, you should see a notification asking if you would like to install recommended extensions. Click to see the recommended extensions, and choose the [Astro language support extension](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode). This will provide syntax highlighting and autocompletions for your Astro code.
    
9.  Make sure the terminal is visible and that you can see the command prompt, such as:
    
    ```
    user@machine:~/tutorial$
    ```
    

You can now use the terminal built right into this window, instead of your computer’s Terminal app, for the rest of this tutorial.

## Run Astro in dev mode

[Section titled “Run Astro in dev mode”](#run-astro-in-dev-mode)

In order to preview your project files _as a website_ while you work, you will need Astro to be running in development (dev) mode.

### Start the dev server

[Section titled “Start the dev server”](#start-the-dev-server)

10.  Run the command to start the Astro dev server by typing into VS Code’s terminal:
     
     *   [npm](#tab-panel-2067)
     *   [pnpm](#tab-panel-2068)
     *   [Yarn](#tab-panel-2069)
     
     ```
     npm run dev
     ```
     
     Now you should see confirmation in the terminal that Astro is running in dev mode. 🚀
     

## View a preview of your website

[Section titled “View a preview of your website”](#view-a-preview-of-your-website)

Your project files contain all the code necessary to display an Astro website, but the browser is responsible for displaying your code as web pages.

11.  Click on the `localhost` link in your terminal window to see a live preview of your new Astro website!
     
     (Astro uses `http://localhost:4321` by default if port `4321` is available.)
     
     Here’s what the Astro “Empty Project” starter website should look like in the browser preview:
     
     ![A blank white page with the word Astro at the top.](/tutorial/minimal.png)
     

## Checklist

[Section titled “Checklist”](#checklist)

 *    I can create a new Astro project.
*    I can start the Astro dev server.

### Resources

[Section titled “Resources”](#resources)

*   [Getting Started with Visual Studio Code](https://code.visualstudio.com/docs/introvideos/basics) external — a video tutorial for installing, setting up and working with VS Code
    

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
