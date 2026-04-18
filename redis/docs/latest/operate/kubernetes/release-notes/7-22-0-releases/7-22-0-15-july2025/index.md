---
title: "Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes"
source: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-15-july2025/"
canonical_url: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-15-july2025/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:51.226Z"
content_hash: "cff837e7ae44c7815e523c69d07434db49062a58a26eb505d0dd4a2e22214033"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0 release notes","→","Redis Enterprise for Kubernetes 7.22.0 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes","→","Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0 release notes","→","Redis Enterprise for Kubernetes 7.22.0 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes","→","Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.14.0/index.md", "title": "RedisInsight v2.14.0, November 2022"}
nav_next: {"path": "redis/docs/latest/integrate/amazon-bedrock/index.md", "title": "Amazon Bedrock"}
---

# Redis Enterprise for Kubernetes 7.22.0-15 (July 2025) release notes

Feature release with Helm chart general availability, Kubernetes 1.33 and OpenShift 4.19 support, Redis Software 7.22.0-216 support, and enhancements.

Redis Enterprise for Kubernetes

## Highlights

*   Helm chart support is now generally available.

## New in this release

Redis Enterprise for Kubernetes 7.22.0-15 is a feature release that includes enhancements, platform updates, and support for Redis Software 7.22.0-216.

### Enhancements

*   Call home - support HTTP proxy configuration (RED-156935)
*   Helm - optimize installation time (RED-153889)
*   Add support for migrating to a Helm-based installation from a non-Helm installation (RED-113099)
*   Support upgrade using Helm (RED-153890)
*   Support any custom port for database service (different from cluster database port) (RED-156946)
*   Hardened the securityContext of init containers created when readOnlyRootFilesystem is enabled
*   Kubernetes platform updates, support for Kubernetes 1.33
*   Support for Redis Software 7.22.0-216 (RED-163025)

### Resolved Issues

*   Adding `servicesAnnotations` in the REC spec keeps updating the services in a loop (RED-154777, RED-158816)
*   New call home job is not created if the old one is stuck due to pod in `imagePullBackoff` (RED-157526)
*   REAADB ACL roles do not get properly assigned according to `rolesPermissions` in spec (RED-158955)
*   CVE fixes
*   `allowPrivilegeEscalation` is unset in the init container for `readOnlyRootFilesystem` (RED-163637)

### API changes

CRD

Field

Change

Description

REAADB

`spec.databaseServicePort`

Add

A custom port to be exposed by the database services. Can be modified/added/removed after REDB creation. If set, it replaces the default service port (namely, `databasePort` or `defaultRedisPort`).

REC

`spec.usageMeterSpec.CallHomeClient.proxySecretName`

Add

If needed, add proxy details in secret. The name of the proxy secret in the secret, can send the following keys: `proxy-url`, `proxy-username`, `proxy-password` (the URL includes the proxy port).

REDB

`spec.databaseServicePort`

Add

A custom port to be exposed by the database services. Can be modified/added/removed after REDB creation. If set, it replaces the default service port (namely, `databasePort` or `defaultRedisPort`).

## RHEL9-based image

As of version 7.8.2-6, Redis Enterprise images are based on Red Hat Enterprise Linux 9 (RHEL9). This means upgrades require:

*   [Cluster version of 7.4.2-2 or later](https://redis.io/docs/latest/operate/kubernetes/7.4.6/upgrade/).
*   Database version 7.2 or later.
*   RHEL9 compatible binaries for any modules you need.

For detailed steps, see the relevant upgrade page:

*   [OpenShift CLI](/docs/latest/operate/kubernetes/upgrade/openshift-cli/)
*   [OpenShift OperatorHub](/docs/latest/operate/kubernetes/upgrade/upgrade-olm/)
*   [Kubernetes](/docs/latest/operate/kubernetes/upgrade/upgrade-redis-cluster/)

## Supported distributions

The following table shows supported distributions at the time of this release. You can also find this list in [Supported Kubernetes distributions](/docs/latest/operate/kubernetes/reference/supported_k8s_distributions/).

✅ Supported – This distribution is supported for this version of Redis Enterprise Kubernetes.

⚠️ Deprecated – This distribution is still supported for this version of Redis Enterprise Kubernetes, but support will be removed in a future release.

❌ End of life – Support for this distribution ended.

Any distribution not listed below is not supported for production workloads.

Kubernetes version

**1.28**

**1.29**

**1.30**

**1.31**

**1.32**

**1.33**

**Community K8s**

⚠️

✅

✅

✅

**Amazon EKS**

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

⚠️

✅

✅

✅

**Rancher**

⚠️

✅

✅

**OpenShift**

**4.15**

**4.16**

**4.17**

**4.18**

**4.19**

⚠️

✅

✅

✅

✅

**VMware TKGI**

**1.19**

**1.20**

**1.21**

⚠️

✅

✅

## Downloads

*   **Redis Enterprise**: `redislabs/redis:7.22.0-216`
*   **Operator**: `redislabs/operator:7.22.0-15`
*   **Services Rigger**: `redislabs/k8s-controller:7.22.0-15`
*   **Call Home Client**: `redislabs/re-call-home-client:7.22.0-15`

### Openshift downloads

*   **OLM operator bundle**: `7.22.0-15.0`
*   **Call Home Client**: `redislabs/call-home-client:7.22.0-15`

## Known limitations

See [7.22.0 releases](/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/) for information on known limitations.

## On this page

