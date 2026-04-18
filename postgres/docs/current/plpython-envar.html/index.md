---
title: "PostgreSQL: Documentation: 18: 44.11. Environment Variables"
source: "https://www.postgresql.org/docs/current/plpython-envar.html"
canonical_url: "https://www.postgresql.org/docs/current/plpython-envar.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:29.950Z"
content_hash: "b5a48a5d55e1fa04fe06569287b4559537ff8cdb95e7b212b6d53b957e29e62c"
menu_path: ["PostgreSQL: Documentation: 18: 44.11. Environment Variables"]
section_path: []
---
Some of the environment variables that are accepted by the Python interpreter can also be used to affect PL/Python behavior. They would need to be set in the environment of the main PostgreSQL server process, for example in a start script. The available environment variables depend on the version of Python; see the Python documentation for details. At the time of this writing, the following environment variables have an affect on PL/Python, assuming an adequate Python version:

*   `PYTHONHOME`
    
*   `PYTHONPATH`
    
*   `PYTHONY2K`
    
*   `PYTHONOPTIMIZE`
    
*   `PYTHONDEBUG`
    
*   `PYTHONVERBOSE`
    
*   `PYTHONCASEOK`
    
*   `PYTHONDONTWRITEBYTECODE`
    
*   `PYTHONIOENCODING`
    
*   `PYTHONUSERBASE`
    
*   `PYTHONHASHSEED`
    

(It appears to be a Python implementation detail beyond the control of PL/Python that some of the environment variables listed on the `python` man page are only effective in a command-line interpreter and not an embedded Python interpreter.)
