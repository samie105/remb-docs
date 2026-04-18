---
title: "Install Redis Open Source on Linux"
source: "https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/rpm/"
canonical_url: "https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/rpm/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:51.890Z"
content_hash: "34a42e2b69a62b283e061e23e12fdde214a3fd348fca538cd58688d9da1b0825"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source on Linux","→","Install Redis Open Source on Linux"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Redis products","→","Redis products","→\n      \n        Redis Open Source","→","Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source","→","Install Redis Open Source","→\n      \n        Install Redis Open Source on Linux","→","Install Redis Open Source on Linux"]
nav_prev: {"path": "redis/docs/latest/operate/oss_and_stack/install/install-stack/homebrew/index.md", "title": "Install Redis Open Source on macOS"}
nav_next: {"path": "redis/docs/latest/operate/oss_and_stack/install/install-stack/snap/index.md", "title": "Install Redis Open Source on Linux"}
---

# Install Redis Open Source on Linux

How to install Redis Open Source using RPM

Redis Open Source

## Install Redis Open Source on Rocky Linux 8 and 9, or AlmaLinux 8 and 9 using RPM

Follow these steps to install Redis Open Source.

1.  Create the file `/etc/yum.repos.d/redis.repo` with the following contents.
    
    *   For Rocky Linux 9 and AlmaLinux 9
        
        ```ini
        [Redis]
        name=Redis
        baseurl=http://packages.redis.io/rpm/rockylinux9
        enabled=1
        gpgcheck=1
        ```
        
    *   For Rocky Linux 8 and AlmaLinux 8
        
        ```ini
        [Redis]
        name=Redis
        baseurl=http://packages.redis.io/rpm/rockylinux8
        enabled=1
        gpgcheck=1
        ```
        
2.  Run the following commands:
    
    ```bash
    curl -fsSL https://packages.redis.io/gpg > /tmp/redis.key
    sudo rpm --import /tmp/redis.key
    sudo yum install redis
    ```
    

Redis will not start automatically, nor will it start at boot time. To do this, run the following commands.

```bash
sudo systemctl enable redis
sudo systemctl start redis
```

## On this page
