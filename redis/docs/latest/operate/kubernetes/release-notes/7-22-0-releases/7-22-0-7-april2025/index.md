---
title: "Redis Enterprise for Kubernetes 7.22.0-7 (April 2025) release notes"
source: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-7-april2025/"
canonical_url: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-7-april2025/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:01:52.551Z"
content_hash: "9271130b88bbf7aa7d4fec3cfd5b4cfde2ae7723f06b73715af7c0cf7835d2c7"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0 release notes","→","Redis Enterprise for Kubernetes 7.22.0 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0-7 (April 2025) release notes","→","Redis Enterprise for Kubernetes 7.22.0-7 (April 2025) release notes"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0 release notes","→","Redis Enterprise for Kubernetes 7.22.0 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.22.0-7 (April 2025) release notes","→","Redis Enterprise for Kubernetes 7.22.0-7 (April 2025) release notes"]
nav_prev: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-17-september2025/index.md", "title": "Redis Enterprise for Kubernetes 7.22.0-17 (September 2025) release notes"}
nav_next: {"path": "redis/docs/latest/operate/kubernetes/release-notes/7-4-2-releases/7-4-2-03-24/index.md", "title": "Redis Enterprise for Kubernetes 7.4.2-2 (March 2024) release notes"}
---

# Redis Enterprise for Kubernetes 7.22.0-7 (April 2025) release notes

Feature release with Redis Software 7.22.0-28 support, enhancements, and platform updates.

Redis Enterprise for Kubernetes

## New in the release

Redis Enterprise for Kubernetes 7.22.0-7 is a feature release that includes enhancements, platform updates, and support for Redis Software 7.22.0-28.

### Enhancements

*   Added support for Redis Software 7.22.0.
*   Enabled support for Active-Active databases (REAADB) in multi-namespace deployments.
*   Defaulted new installations and upgrades to unprivileged mode, which uses a more secure security context without additional Linux capabilities.
*   A new cronjob is created by the operator using the `redislabs/re-call-home-client:7.22.0-7` image.
*   Updated supported Kubernetes platforms.

### API changes

**CRD**

**Field**

**Change**

**Description**

REAADB

`spec.participatingClusters[].namespace`

Added

Specifies the namespace in which the REAADB object will be deployed in the corresponding participating cluster. Make sure that the Redis Enterprise operator is configured to watch this namespace and that the required RBAC configuration is in place. For more information, see [Multi-namespace deployments](/docs/latest/operate/kubernetes/re-clusters/multi-namespace/). If no namespace is specified, the REAADB object is deployed to the REC’s namespace in the corresponding cluster.

REC

`spec.usageMeter.callHomeClient`

Added

Configuration for the call home client. For details, see the [REC API reference](/docs/latest/operate/kubernetes/reference/api/redis_enterprise_cluster_api/).

REC

`spec.securityContext.resourceLimits`

Added

Configuration that allows Redis Enterprise to adjust system resource settings. For details, see the [REC API reference](/docs/latest/operate/kubernetes/reference/api/redis_enterprise_cluster_api/).

## Breaking changes

By default, the operator no longer sets additional Linux capabilities in the security context. If your deployment requires capabilities such as `SYS_RESOURCE`, see [Allow automatic resource adjustment](/docs/latest/operate/kubernetes/security/allow-resource-adjustment/).

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

**1.26**

**1.27**

**1.28**

**1.29**

**1.30**

**1.31**

**1.32**

**Community K8s**

✅

✅

✅

**Amazon EKS**

❌

✅

✅

✅

**Azure AKS**

❌

✅

✅

✅

**Google GKE**

❌

✅

✅

✅

**Rancher**

❌

✅

✅

✅

**VMware TKG 2.4**

⚠️

⚠️

**OpenShift**

**4.13**

**4.14**

**4.15**

**4.16**

**4.17**

**4.18**

❌

❌

✅

✅

✅

✅

**VMware TKGI**

**1.16**

**1.17**

**1.18**

**1.19**

**1.20**

⚠️

⚠️

✅

✅

## Downloads

*   **Redis Enterprise**: `redislabs/redis:7.22.0-28`
*   **Operator**: `redislabs/operator:7.22.0-7`
*   **Services Rigger**: `redislabs/k8s-controller:7.22.0-7`
*   **Call Home Client**: `redislabs/re-call-home-client:7.22.0-7`

### Openshift downloads

*   **OLM operator bundle** : `7.22.0-7.0`
*   **Call Home Client**: `redislabs/call-home-client:7.22.0-7`

## Known limitations

See [7.22.0 releases](/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/) for information on known limitations.

## On this page
