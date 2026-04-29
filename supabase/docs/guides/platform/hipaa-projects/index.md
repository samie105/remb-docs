---
title: "HIPAA Projects"
source: "https://supabase.com/docs/guides/platform/hipaa-projects"
canonical_url: "https://supabase.com/docs/guides/platform/hipaa-projects"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:35.189Z"
content_hash: "60ae868222d1a2c58219b52241bc50ce543dcc9210e0765e0241350fd3bdbfb8"
menu_path: ["Platform","Platform","Platform Configuration","Platform Configuration","HIPAA Projects","HIPAA Projects"]
section_path: ["Platform","Platform","Platform Configuration","Platform Configuration","HIPAA Projects","HIPAA Projects"]
nav_prev: {"path": "supabase/docs/guides/platform/get-set-up-for-billing/index.md", "title": "Get set up for billing"}
nav_next: {"path": "supabase/docs/guides/platform/ipv4-address/index.md", "title": "Dedicated IPv4 Address for Ingress"}
---

# 

HIPAA Projects

* * *

You can use Supabase to store and process Protected Health Information (PHI). If you want to start developing healthcare apps on Supabase, reach out to the Supabase team [here](https://forms.supabase.com/hipaa2) to sign the Business Associate Agreement (BAA).

Organizations must have a signed BAA with Supabase and have the Health Insurance Portability and Accountability Act (HIPAA) add-on enabled when dealing with PHI.

## Configuring a HIPAA project[#](#configuring-a-hipaa-project)

When the HIPAA add-on is enabled on an organization, projects within the organization can be configured as _High Compliance_. This configuration can be found in the [General Project Settings page](/dashboard/project/_/settings) of the dashboard. Once enabled, additional security checks will be run against the project to ensure the deployed configuration is compliant. These checks are performed on a continual basis and security warnings will appear in the [Security Advisor](/dashboard/project/_/advisors/security) if a non-compliant setting is detected.

The required project configuration is outlined in the [shared responsibility model](../../deployment/shared-responsibility-model/index.md#managing-healthcare-data) for managing healthcare data.

These include:

*   Enabling [Point in Time Recovery](../backups/index.md#point-in-time-recovery) which requires at least a [small compute add-on](/docs/guides/platform/compute-add-ons).
*   Turning on [SSL Enforcement](../ssl-enforcement/index.md).
*   Enabling [Network Restrictions](../network-restrictions/index.md).

Additional security checks and controls will be added as the security advisor is extended and additional security controls are made available.
