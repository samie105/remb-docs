---
title: "Plan Redis Software deployment"
source: "https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/"
canonical_url: "https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:37.686Z"
content_hash: "0f192bf888cddb047debce0c6c2d10058a49524948224d915f58dec0e400dc24"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Software","→","Redis Software","→\n      \n        Install, set up, and upgrade Redis Software","→","Install, set up, and upgrade Redis Software","→\n      \n        Install Redis Software","→","Install Redis Software","→\n      \n        Plan Redis Software deployment","→","Plan Redis Software deployment"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Software","→","Redis Software","→\n      \n        Install, set up, and upgrade Redis Software","→","Install, set up, and upgrade Redis Software","→\n      \n        Install Redis Software","→","Install Redis Software","→\n      \n        Plan Redis Software deployment","→","Plan Redis Software deployment"]
nav_prev: {"path": "redis/docs/latest/operate/redisinsight/proxy/index.md", "title": "Subpath proxy"}
nav_next: {"path": "redis/docs/latest/operate/rs/installing-upgrading/install/prepare-install/index.md", "title": "Prepare to install Redis Software"}
---

# Plan Redis Software deployment

Plan a deployment of Redis Software.

Redis Software

Before installing Redis Software, you need to:

*   Set up your hardware. See [Hardware requirements](/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/hardware-requirements/) and [Persistent and ephemeral node storage](/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/persistent-ephemeral-storage/) for more information.
    
*   Choose your [deployment platform](/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms/).
    
    Redis Software supports a variety of platforms, including:
    
    *   Multiple Linux distributions (Ubuntu, Red Hat Enterprise Linux (RHEL), IBM CentOS, Oracle Linux)
    *   [Amazon AWS AMI](/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/configuring-aws-instances/)
    *   [Docker container](/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart/) (for development and testing only)
    *   [Kubernetes](/docs/latest/operate/kubernetes/)
    
    For more details, see [Supported platforms](/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms/).
    
*   Open appropriate [network ports](/docs/latest/operate/rs/networking/port-configurations/) in the firewall to allow connections to the nodes.
    
*   Configure [cluster DNS](/docs/latest/operate/rs/networking/cluster-dns/) so that cluster nodes can reach each other by DNS names.
    
*   By default, the installation process requires an internet connection to install dependencies and synchronize the operating system clock. To learn more, see [Offline installation](/docs/latest/operate/rs/installing-upgrading/install/offline-installation/).
    
*   [Configure different mount points for data and log directories](/docs/latest/operate/rs/installing-upgrading/install/customize-install-directories/#config-diff-data-log-dirs).
    

## Next steps

After you finish planning your deployment, you can:

*   [Download an installation package](/docs/latest/operate/rs/installing-upgrading/install/prepare-install/download-install-package/).
    
*   [Prepare to install](/docs/latest/operate/rs/installing-upgrading/install/prepare-install/) Redis Software.
    
*   [View installation questions](/docs/latest/operate/rs/installing-upgrading/install/manage-installation-questions/) and prepare answers before installation.
    

## On this page
