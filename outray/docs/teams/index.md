---
title: "Teams & Organizations"
source: "https://outray.dev/docs/teams"
canonical_url: "https://outray.dev/docs/teams"
docset: "outray"
kind: "tool"
adapter: "generic"
last_crawled_at: "2026-04-29T23:25:36.840Z"
content_hash: "801d988b7b456cf08ee674efb65290ab3c3b09f0b74205d94a861acc3622357b"
menu_path: ["Teams & Organizations"]
section_path: []
nav_prev: {"path": "outray/docs/custom-domains/index.md", "title": "Custom Domains"}
nav_next: {"path": "outray/docs/ci-cd/index.md", "title": "CI/CD Integration"}
---

## Teams & Organizations

Collaborate with your team on OutRay

OutRay is built for collaboration. You can create organizations and invite team members to share resources.

-   **Shared Domains**: Any domain added to an organization is available to all members.
-   **Centralized Billing**: Manage subscriptions for your entire team in one place.
-   **Role-Based Access**: Control who can manage domains and billing.

If you belong to multiple organizations, you can switch between them using the CLI.

### [Interactive Switch](#interactive-switch)

Run the following command to see a list of your organizations and select one:

```
outray switch
```

### [Direct Switch](#direct-switch)

If you know the slug of the organization you want to switch to, you can pass it directly:

```
outray switch my-org-slug
```

### [Per-Command Override](#per-command-override)

You can also override the active organization for a single command using the `--org` flag:

```
outray 3000 --org my-other-org
```
