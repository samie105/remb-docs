---
title: "Redis Enterprise for Kubernetes 7.4.2-2 (Feb 2024) release notes"
source: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-4-2-releases/7-4-2-2/"
canonical_url: "https://redis.io/docs/latest/operate/kubernetes/release-notes/7-4-2-releases/7-4-2-2/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:11:53.493Z"
content_hash: "da78af0d8e00fc1df841465c5bc627770aef80365dc1e609c2152ff7d420b570"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.4.2 release notes","→","Redis Enterprise for Kubernetes 7.4.2 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.4.2-2 (Feb 2024) release notes","→","Redis Enterprise for Kubernetes 7.4.2-2 (Feb 2024) release notes"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Enterprise for Kubernetes","→","Redis Enterprise for Kubernetes","→\n      \n        Redis Enterprise Software for Kubernetes release notes","→","Redis Enterprise Software for Kubernetes release notes","→\n      \n        Redis Enterprise for Kubernetes 7.4.2 release notes","→","Redis Enterprise for Kubernetes 7.4.2 release notes","→\n      \n        Redis Enterprise for Kubernetes 7.4.2-2 (Feb 2024) release notes","→","Redis Enterprise for Kubernetes 7.4.2-2 (Feb 2024) release notes"]
nav_prev: {"path": "redis/docs/latest/develop/tools/insight/release-notes/v.2.6.0/index.md", "title": "RedisInsight v2.6.0, July 2022"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/concepts/binary_data/index.md", "title": "Binary data"}
---

# Redis Enterprise for Kubernetes 7.4.2-2 (Feb 2024) release notes

The primary purpose of this release is to support Redis Enterprise 7.4.2

Redis Enterprise for Kubernetes

## Highlights

The primary purpose of this release is to support [Redis Enterprise 7.4.2](/docs/latest/operate/rs/release-notes/rs-7-4-2-releases/rs-7-4-2-54/), which is a major update to Redis Enterprise Software. As such, we have limited the scope of changes to focus on supporting RS 7.4 changes, in addition to implementing a few enhancements and major fixes.

## New in this release

### Enhancements

*   Added RESP3 support in K8s APIs (RED-94601)
*   Added to [supported distributions](#supported-distributions)
*   Added support for Redis Enterprise Software 7.4.2
*   Enhanced resilience of operators to misconfigured REDB namespaces (RED-113908)
*   Both the operator and services rigger are now based on UBI9 (RED-116083)

### Resolved issues

*   Fixed the operator to prevent reconciliation of non-REDB custom resources in observed namespaces. This eliminates the need for unnecessary permission rules. (RED-87790)
*   Fixed excessive updates to ingresses and services. (RED-109289)
*   Fixed update issues in rigger after the upgrade in multi-namespace environments. (RED-111732)
*   Fixed Active-Active sharding configuration by adding a new field. (RED-112909)
*   Fixed operator CVE. (RED-115157)
*   Fixed a race condition that could have rarely caused the cluster upgrade to break. (RED-118940)

### API changes

**CRD**

**Field**

**Change**

**Description**

REC

resp3Default

Add

Boolean controlling whether Resp3 should be enabled by default

REDB

resp3

Add

Controls resp3 for specific REDBs

## Version changes

For a list of fixes related to CVEs, see the [Redis Enterprise 7.4.2-54 release notes](/docs/latest/operate/rs/release-notes/rs-7-4-2-releases/rs-7-4-2-54/#security).

### Breaking changes

The following changes included in this release affect the upgrade process. Please read carefully before upgrading.

#### Upgrade operating system

Warning:

If your databases use modules, you need to update all nodes in the cluster to Redis Enterprise 7.2.4 or later before upgrading your operating system. See [Upgrade a cluster's operating system](/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-os/)in the Redis Enterprise Software documentation for more details.

#### terminationGracePeriodSeconds

The configurable `terminationGracePeriodSeconds` REC field was added in version 7.2.4-12 to replace the hard-coded timeout of 15 minutes for a node to be stopped or drained (RED-111471).

#### ValidatingWebhookConfiguration

Versions 6.4.2-4 and later include a new `ValidatingWebhookConfiguration` resource to replace the `redb-admission` webhook resource. To use releases 6.4.2-4 or later, delete the old webhook resource and apply the new file. See [upgrade Redis cluster](/docs/latest/operate/kubernetes/upgrade/upgrade-redis-cluster/#reapply-webhook) for instructions.

#### OpenShift SCC

Versions 6.4.2-6 and later include a new SCC (`redis-enterprise-scc-v2`) that you need to bind to your service account before upgrading. OpenShift clusters running version 6.2.12 or earlier upgrading to version 6.2.18 or later might get stuck if you skip this step. See [upgrade a Redis Enterprise cluster (REC)](/docs/latest/operate/kubernetes/upgrade/upgrade-redis-cluster/#before-upgrading) for instructions.

### Deprecations

*   Redis Software for Kubernetes no longer supports the RHEL7 operating system. Migrate to RHEL8 to use this version.

### Supported distributions

See the [7.4.2 releases](/docs/latest/operate/kubernetes/release-notes/7-4-2-releases/) page for the list of supported distributions.

## Downloads

*   **Redis Enterprise**: `redislabs/redis:7.4.2-54`
*   **Operator**: `redislabs/operator:7.4.2-2`
*   **Services Rigger**: `redislabs/k8s-controller:7.4.2-2`

#### OpenShift images

*   **Redis Enterprise**: `registry.connect.redhat.com/redislabs/redis-enterprise:7.4.2-54.rhel8-openshift`
*   **Operator**: `registry.connect.redhat.com/redislabs/redis-enterprise-operator:7.4.2-2`
*   **Services Rigger**: `registry.connect.redhat.com/redislabs/services-manager:7.4.2-2`

#### OLM bundle

**Redis Enterprise operator bundle** : `v7.4.2-2`

## Known limitations

See the [7.4.2 releases](/docs/latest/operate/kubernetes/release-notes/7-4-2-releases/) page for the list of known limitations.

## On this page

