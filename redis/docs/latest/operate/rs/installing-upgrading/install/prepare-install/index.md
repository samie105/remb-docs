---
title: "Prepare to install Redis Software"
source: "https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install/"
canonical_url: "https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:22.344Z"
content_hash: "350b99cfb07ec234c77391278538e628e264b5258354cc8ccdb050e14509ea31"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Software","→","Redis Software","→\n      \n        Install, set up, and upgrade Redis Software","→","Install, set up, and upgrade Redis Software","→\n      \n        Install Redis Software","→","Install Redis Software","→\n      \n        Prepare to install Redis Software","→","Prepare to install Redis Software"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Software","→","Redis Software","→\n      \n        Install, set up, and upgrade Redis Software","→","Install, set up, and upgrade Redis Software","→\n      \n        Install Redis Software","→","Install Redis Software","→\n      \n        Prepare to install Redis Software","→","Prepare to install Redis Software"]
nav_prev: {"path": "../plan-deployment/index.md", "title": "Plan Redis Software deployment"}
nav_next: {"path": "../../quickstarts/docker-quickstart/index.md", "title": "Docker quickstart for Redis Software"}
---

# Prepare to install Redis Software

Prepare to install Redis Software.

Redis Software

Before you install Redis Software:

*   [Download an installation package](/docs/latest/operate/rs/installing-upgrading/install/prepare-install/download-install-package/).
    
*   [View installation questions](/docs/latest/operate/rs/installing-upgrading/install/manage-installation-questions/) and optionally prepare answers before installation.
    
*   Review the [security considerations](/docs/latest/operate/rs/security/) for your deployment.
    
*   Check that you have root-level access to each node, either directly or with `sudo`.
    
*   Check that all [required ports are available](/docs/latest/operate/rs/installing-upgrading/install/prepare-install/port-availability/).
    
*   [Turn off Linux swap](/docs/latest/operate/rs/installing-upgrading/configuring/linux-swap/) on all cluster nodes.
    
*   If you require the `redislabs` UID (user ID) and GID (group ID) numbers to be the same on all the nodes, create the `redislabs` user and group with the required numbers on each node.
    
*   If you want to use Auto Tiering for your databases, see [Auto Tiering installation](/docs/latest/operate/rs/installing-upgrading/install/install-on-linux/#auto-tiering-installation).
    

## Next steps

*   View [installation script options](/docs/latest/operate/rs/installing-upgrading/install/install-script/) before starting the installation.
    
*   [Install Redis Software](/docs/latest/operate/rs/installing-upgrading/install/).
    

## On this page
