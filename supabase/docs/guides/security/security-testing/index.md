---
title: "Security testing of your Supabase projects"
source: "https://supabase.com/docs/guides/security/security-testing"
canonical_url: "https://supabase.com/docs/guides/security/security-testing"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:08.451Z"
content_hash: "921eaa5ebc8c5249845b1c96c9613d6f67cf1ada7a632c82d40ecf9f8d912c1a"
menu_path: ["Security","Security","Product security","Product security","Security testing","Security testing"]
section_path: ["Security","Security","Product security","Product security","Security testing","Security testing"]
nav_prev: {"path": "../product-security/index.md", "title": "Secure configuration of Supabase products"}
nav_next: {"path": "../soc-2-compliance/index.md", "title": "SOC 2 Compliance and Supabase"}
---

# 

Security testing of your Supabase projects

* * *

Supabase customer support policy for penetration testing

Customers of Supabase are permitted to carry out security assessments or penetration tests of their hosted Supabase project components. This testing may be carried out without prior approval for the customer services listed under [permitted services](#permitted-services). Supabase does not permit hosting security tooling that may be perceived as malicious or part of a campaign against Supabase customers or external services. This section is covered by the [Supabase Acceptable Use Policy](/aup) (AUP).

It is the customer’s responsibility to ensure that testing activities are aligned with this policy. Any testing performed outside of the policy will be seen as testing directly against Supabase and may be flagged as abuse behaviour. If Supabase receives an abuse report for activities related to your security testing, we will forward these to you. If you discover a security issue within any of the Supabase products, contact [Supabase Security](mailto:security@supabase.io) immediately.

Furthermore, Supabase runs a [Vulnerability Disclosure Program](https://hackerone.com/ca63b563-9661-4ac3-8d23-7581582ef451/embedded_submissions/new) (VDP) with HackerOne, and external security researchers may report any bugs found within the scope of the aforementioned program. Customer penetration testing does not form part of this VDP.

### Permitted services[#](#permitted-services)

*   Authentication
*   Database
*   Edge Functions
*   Storage
*   Realtime
*   `https://<customer_project_ref>.supabase.co/*`
*   `https://db.<customer_project_ref>.supabase.co/*`

### Prohibited testing and activities[#](#prohibited-testing-and-activities)

*   Any activity contrary to what is listed in the AUP.
*   Denial of Service (DoS) and Distributed Denial of Service (DDoS) testing.
*   Cross-tenant attacks, testing that directly targets other Supabase customers' accounts, organizations, and projects not under the customer’s control.
*   Request flooding.

## Terms and conditions[#](#terms-and-conditions)

The customer agrees to the following,

Security testing:

*   Will be limited to the services within the customer’s project.
*   Is subject to the general [Terms of Service](/terms).
*   Is within the [Acceptable Usage Policy](/aup).
*   Will be stopped if contacted by Supabase due to a breach of the above or a negative impact on Supabase and Supabase customers.
*   Any vulnerabilities discovered directly in a Supabase product will be reported to Supabase Security within 24 hours of completion of testing.
