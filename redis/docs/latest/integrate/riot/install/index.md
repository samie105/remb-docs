---
title: "Install"
source: "https://redis.io/docs/latest/integrate/riot/install/"
canonical_url: "https://redis.io/docs/latest/integrate/riot/install/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:45.352Z"
content_hash: "3daeeea8bf1280e2cd4447ddc33cd1c63ade761d3282fc68f944b6e91934f20b"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        RIOT-X","→","RIOT-X","→\n      \n        Install","→","Install"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Libraries and tools","→","Libraries and tools","→\n      \n        RIOT-X","→","RIOT-X","→\n      \n        Install","→","Install"]
---
# Install

Install RIOT-X on macOS, Linux, Windows, and Docker

RIOT-X can be installed in different ways depending on your environment and preference.

## macOS and Linux via Homebrew

```
brew install redis/tap/riotx
```

## Windows via Scoop

```
scoop bucket add redis https://github.com/redis/scoop.git
scoop install riotx
```

## Docker

```
docker run riotx/riotx [OPTIONS] [COMMAND]
```

## Manual installation on all supported platforms

Download the pre-compiled binary from [RIOT-X Releases](https://github.com/redis/riotx-dist/releases), uncompress, and copy to the desired location.

Full installation documentation is available [here](https://redis.github.io/riotx/quick-start/install.html).

## On this page
