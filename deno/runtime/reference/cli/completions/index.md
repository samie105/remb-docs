---
title: "deno completions"
source: "https://docs.deno.com/runtime/reference/cli/completions/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/completions/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:27:31.738Z"
content_hash: "26494c187ed23d5652f664b49a535b2a33f03eb18399282f24fd62b215e472f8"
menu_path: ["deno completions"]
section_path: []
content_language: "en"
nav_prev: {"path": "../create/index.md", "title": "deno create"}
nav_next: {"path": "../coverage/index.md", "title": "deno coverage"}
---

**On this page**

-   [Examples](#examples)
    -   [Configure Bash shell completion](#configure-bash-shell-completion)
    -   [Configure PowerShell shell completion](#configure-powershell-shell-completion)
    -   [Configure zsh shell completion](#configure-zsh-shell-completion)
    -   [Configure fish shell completion](#configure-fish-shell-completion)
-   [Options](#options)

You can use the output script to configure autocompletion for `deno` commands. For example: `deno un` -> Tab -> `deno uninstall`.

## Examples

### Configure Bash shell completion

\>\_

```sh
deno completions bash > deno.bash

if [ -d "/usr/local/etc/bash_completion.d/" ]; then
  sudo mv deno.bash /usr/local/etc/bash_completion.d/
  source /usr/local/etc/bash_completion.d/deno.bash
elif [ -d "/usr/share/bash-completion/completions/" ]; then
  sudo mv deno.bash /usr/share/bash-completion/completions/
  source /usr/share/bash-completion/completions/deno.bash
else
  echo "Please move deno.bash to the appropriate bash completions directory"
fi
```

### Configure PowerShell shell completion

\>\_

```sh
deno completions powershell | Out-String | Invoke-Expression
```

### Configure zsh shell completion

First add the following to your `.zshrc` file:

\>\_

```sh
fpath=(~/.zsh/completion $fpath)
autoload -U compinit
compinit
```

Then run the following commands:

\>\_

```sh
deno completions zsh > _deno
mv _deno ~/.zsh/completion/_deno
autoload -U compinit && compinit
```

### Configure fish shell completion

\>\_

```sh
deno completions fish > completions.fish
chmod +x ./completions.fish
```

Command line usage:

```
deno completions [OPTIONS] [shell]
```

Output shell completion script to standard output.

```
deno completions bash > /usr/local/etc/bash_completion.d/deno.bash
```

```
source /usr/local/etc/bash_completion.d/deno.bash
```

## Options

`--dynamic`

Generate dynamic completions for the given shell (unstable), currently this only provides available tasks for `deno task`.
