---
title: "PostgreSQL: Documentation: 18: I.1. Getting the Source via Git"
source: "https://www.postgresql.org/docs/current/git.html"
canonical_url: "https://www.postgresql.org/docs/current/git.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:51.170Z"
content_hash: "89d718cd245303d25244e21149615d563264de367689b3029cdeb472fe9c1726"
menu_path: ["PostgreSQL: Documentation: 18: I.1. Getting the Source via Git"]
section_path: []
nav_prev: {"path": "postgres/docs/current/gist.html/index.md", "title": "PostgreSQL: Documentation: 18: 65.2.\u00a0GiST Indexes"}
nav_next: {"path": "postgres/docs/current/gssapi-auth.html/index.md", "title": "PostgreSQL: Documentation: 18: 20.6.\u00a0GSSAPI Authentication"}
---

With Git you will make a copy of the entire code repository on your local machine, so you will have access to all history and branches offline. This is the fastest and most flexible way to develop or test patches.

**Git**

1.  You will need an installed version of Git, which you can get from [https://git-scm.com](https://git-scm.com/). Many systems already have a recent version of Git installed by default, or available in their package distribution system.
    
2.  To begin using the Git repository, make a clone of the official mirror:
    
    git clone https://git.postgresql.org/git/postgresql.git
    
    This will copy the full repository to your local machine, so it may take a while to complete, especially if you have a slow Internet connection. The files will be placed in a new subdirectory `postgresql` of your current directory.
    
3.  Whenever you want to get the latest updates in the system, `cd` into the repository, and run:
    
    git fetch
    

Git can do a lot more things than just fetch the source. For more information, consult the Git man pages, or see the website at [https://git-scm.com](https://git-scm.com/).
