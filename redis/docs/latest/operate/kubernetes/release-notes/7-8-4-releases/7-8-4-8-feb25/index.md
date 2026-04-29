---
title: "Redis Enterprise for Kubernetes 7.8.4-8 (Feb 2025) release notes"
source: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-4-releases/7-8-4-8-feb25/"
canonical_url: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-8-4-releases/7-8-4-8-feb25/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:16.048Z"
content_hash: "cc78908cd7dd3019581c5635a71fae1cab152e0a49186f978778ab6dbb9703c3"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.8.4 release notes","→","Redis Enterprise for Kubernetes 7.8.4 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.8.4-8 (Feb 2025) release notes","→","Redis Enterprise for Kubernetes 7.8.4-8 (Feb 2025) release notes"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.8.4 release notes","→","Redis Enterprise for Kubernetes 7.8.4 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.8.4-8 (Feb 2025) release notes","→","Redis Enterprise for Kubernetes 7.8.4-8 (Feb 2025) release notes"]
nav_prev: {"path": "../../7-8-2-releases/7-8-2-6-nov24/index.md", "title": "Redis Enterprise for Kubernetes 7.8.2-6 (Nov 2024) release notes"}
nav_next: {"path": "../7-8-4-9-mar25/index.md", "title": "Redis Enterprise for Kubernetes 7.8.4-9 (March 2025) release notes"}
---

# Redis Enterprise for Kubernetes 7.8.4-8 (Feb 2025) release notes

Maintenance release to support Redis Enterprise Software version 7.8.4-66.

Redis Enterprise for Kubernetes

This release includes bug fixes, enhancements, and support for [Redis Enterprise Software version 7.8.4-66](/docs/latest/operate/rs/release-notes/rs-7-8-releases/rs-7-8-4-66/).

## New in this release

### Enhancements

*   Support for a read-only file system on Redis Enterprise containers (RED-75139).
*   Support for [Redis Enterprise Software version 7.8.4-66](/docs/latest/operate/rs/release-notes/rs-7-8-releases/rs-7-8-4-66/).

### Resolved issues

*   Fixed log collector handling of STDERR warnings (RED-148292).

### API changes

**CRD**

**Field**

**Change**

**Description**

REC

spec.SecurityContext.readOnlyRootFilesystemPolicy.enabled

Add

Enables the read-only filesystem

## Supported distributions

The following table shows supported distributions at the time of this release. You can also find this list in [Supported Kubernetes distributions](/docs/latest/operate/kubernetes/reference/supported_k8s_distributions/).

✅ Supported – This distribution is supported for this version of Redis Enterprise Software for Kubernetes.

⚠️ Deprecated – This distribution is still supported for this version of Redis Enterprise Software for Kubernetes, but support will be removed in a future release.

❌ End of life – Support for this distribution ended.

Any distribution not listed below is not supported for production workloads.

**Kubernetes version**

**1.25**

**1.26**

**1.27**

**1.28**

**1.29**

**1.30**

**1.31**

**Community Kubernetes**

❌

✅

✅

✅

✅

**Amazon EKS**

❌

⚠️

✅

✅

✅

**Azure AKS**

⚠️

✅

✅

✅

**Google GKE**

❌

✅

✅

✅

**Rancher RKE2**

⚠️

✅

✅

**VMware TKG 2.3**

⚠️

**VMware TKG 2.4**

✅

✅

**OpenShift**

**4.12**

**4.13**

**4.14**

**4.15**

**4.16**

\*\*\*\*

✅

✅

✅

✅

✅

**VMWare TKGI**

**1.16**

**1.17**

**1.18**

**1.19**

\*\*\*\*

❌

✅

✅

✅

## Downloads

*   **Redis Enterprise**: `redislabs/redis:7.8.4-66`
*   **Operator**: `redislabs/operator:7.8.4-8`
*   **Services Rigger**: `redislabs/k8s-controller:7.8.4-8`
*   **OLM operator bundle** : `v7.8.4-8.0`

## On this page
