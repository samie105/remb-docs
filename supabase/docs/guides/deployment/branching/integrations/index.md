---
title: "Integrations"
source: "https://supabase.com/docs/guides/deployment/branching/integrations"
canonical_url: "https://supabase.com/docs/guides/deployment/branching/integrations"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:09.580Z"
content_hash: "24f098d5d68ecf2f2cf89966f66c6f06b553f8d4d7545ef62a624e719975f012"
menu_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Integrations","Integrations"]
section_path: ["Deployment & Branching","Deployment & Branching","Branching","Branching","Integrations","Integrations"]
---
# 

Integrations

## 

Use Supabase branching with hosting providers and other tools

* * *

Branching works with hosting providers that support preview deployments. Learn how to integrate Supabase branching with various platforms and tools.

## Hosting providers[#](#hosting-providers)

With the Supabase branching integration, you can sync the Git branch used by the hosting provider with the corresponding Supabase preview branch. This means that the preview deployment built by your hosting provider is matched to the correct database schema, edge functions, and other Supabase configurations.

### Vercel[#](#vercel)

Install the Vercel integration:

*   From the [Vercel marketplace](https://vercel.com/integrations/supabase) or
*   By clicking the blue `Deploy` button in a Supabase example app's `README` file

##### Vercel GitHub integration also required.

For branching to work with Vercel, you also need the [Vercel GitHub integration](https://vercel.com/docs/deployments/git/vercel-for-github).

And make sure you have [connected](/dashboard/org/_/integrations) your Supabase project to your Vercel project.

Supabase automatically updates your Vercel project with the correct environment variables for the corresponding preview branches. The synchronization happens at the time of Pull Request being opened, not at the time of branch creation.

As branching integration is tied to the Preview Deployments feature in Vercel, there are possible race conditions between Supabase setting correct variables, and Vercel running a deployment process. Because of that, Supabase is always automatically re-deploying the most recent deployment of the given pull request.
