---
title: "Local Debugging"
source: "https://supabase.com/docs/guides/functions/debugging-tools"
canonical_url: "https://supabase.com/docs/guides/functions/debugging-tools"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:06.890Z"
content_hash: "c2958de4ea59ce884cda48575a87aaf4c2de04f3fc8226000d7245cefe02b8d5"
menu_path: ["Edge Functions","Edge Functions","Debugging","Debugging","Local Debugging with DevTools","Local Debugging with DevTools"]
section_path: ["Edge Functions","Edge Functions","Debugging","Debugging","Local Debugging with DevTools","Local Debugging with DevTools"]
nav_prev: {"path": "supabase/docs/guides/functions/cors/index.md", "title": "CORS (Cross-Origin Resource Sharing) support for Invoking from the browser"}
nav_next: {"path": "supabase/docs/guides/functions/dart-edge/index.md", "title": "Dart Edge"}
---

# 

Local Debugging

## 

Debug your Edge Functions locally using Chrome DevTools for easy breakpoint debugging and code inspection.

* * *

Since [v1.171.0](https://github.com/supabase/cli/releases/tag/v1.171.0) the Supabase CLI supports debugging Edge Functions via the v8 inspector protocol, allowing for debugging via [Chrome DevTools](https://developer.chrome.com/docs/devtools/) and other Chromium-based browsers.

### Inspect with Chrome Developer Tools[#](#inspect-with-chrome-developer-tools)

1.  Serve your functions in inspect mode. This will set a breakpoint at the first line to pause script execution before any code runs.
    
    ```
    1supabase functions serve --inspect-mode brk
    ```
    
2.  In your Chrome browser navigate to `chrome://inspect`.
3.  Click the "Configure..." button to the right of the Discover network targets checkbox.
4.  In the Target discovery settings dialog box that opens, enter `127.0.0.1:8083` in the blank space and click the "Done" button to exit the dialog box.
5.  Click "Open dedicated DevTools for Node" to complete the preparation for debugging. The opened DevTools window will now listen to any incoming requests to edge-runtime.
6.  Send a request to your function running locally, e.g. via curl or Postman. The DevTools window will now pause script execution at first line.
7.  In the "Sources" tab navigate to `file://` > `home/deno/functions/<your-function-name>/index.ts`.
8.  Use the DevTools to set breakpoints and inspect the execution of your Edge Function.

![Debugging in Chrome DevTools.](/docs/img/guides/functions/debug-chrome-devtools.png)

Now you should have Chrome DevTools configured and ready to debug your functions.


