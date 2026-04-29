---
title: "deno task"
source: "https://docs.deno.com/runtime/reference/cli/task/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/task/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:33:22.063Z"
content_hash: "3c9c0e553479f3dac2476591e748c837d1c71980341011ea3e38c582d287ca70"
menu_path: ["deno task"]
section_path: []
content_language: "en"
nav_prev: {"path": "../serve/index.md", "title": "deno serve"}
nav_next: {"path": "../test/index.md", "title": "deno test"}
---

# outputs 10
deno eval 'Deno.exit(10)' || echo $?
```

### Pipelines

Pipelines provide a way to pipe the output of one command to another.

The following command pipes the stdout output "Hello" to the stdin of the spawned Deno process:

\>\_

```sh
echo Hello | deno run main.ts
```

To pipe stdout and stderr, use `|&` instead:

\>\_

```sh
deno eval 'console.log(1); console.error(2);' |& deno run main.ts
```

### Command substitution

The `$(command)` syntax provides a way to use the output of a command in other commands that get executed.

For example, to provide the output of getting the latest git revision to another command you could do the following:

\>\_

```sh
deno run main.ts $(git rev-parse HEAD)
```

Another example using a shell variable:

\>\_

```sh
REV=$(git rev-parse HEAD) && deno run main.ts $REV && echo $REV
```

### Negate exit code

To negate the exit code, add an exclamation point and space before a command:

\>\_

```sh
# change the exit code from 1 to 0
! deno eval 'Deno.exit(1);'
```

### Redirects

Redirects provide a way to pipe stdout and/or stderr to a file.

For example, the following redirects _stdout_ of `deno run main.ts` to a file called `file.txt` on the file system:

\>\_

```sh
deno run main.ts > file.txt
```

To instead redirect _stderr_, use `2>`:

\>\_

```sh
deno run main.ts 2> file.txt
```

To redirect both stdout _and_ stderr, use `&>`:

\>\_

```sh
deno run main.ts &> file.txt
```

To append to a file, instead of overwriting an existing one, use two right angle brackets instead of one:

\>\_

```sh
deno run main.ts >> file.txt
```

Suppressing either stdout, stderr, or both of a command is possible by redirecting to `/dev/null`. This works in a cross-platform way including on Windows.

\>\_

```sh
# suppress stdout
deno run main.ts > /dev/null
# suppress stderr
deno run main.ts 2> /dev/null
# suppress both stdout and stderr
deno run main.ts &> /dev/null
```

Or redirecting stdout to stderr and vice-versa:

\>\_

```sh
# redirect stdout to stderr
deno run main.ts >&2
# redirect stderr to stdout
deno run main.ts 2>&1
```

Input redirects are also supported:

\>\_

```sh
# redirect file.txt to the stdin of gzip
gzip < file.txt
```

Note that redirecting multiple redirects is currently not supported.

### Cross-platform shebang

Starting in Deno 1.42, `deno task` will execute scripts that start with `#!/usr/bin/env -S` the same way on all platforms.

For example:

script.ts

```ts
#!/usr/bin/env -S deno run
console.log("Hello there!");
```

deno.json

```json
{
  "tasks": {
    "hi": "./script.ts"
  }
}
```

Then on a Windows machine:

\>\_

```sh
> pwd
C:\Users\david\dev\my_project
> deno task hi
Hello there!
```

### Glob expansion

Glob expansion is supported in Deno 1.34 and above. This allows for specifying globs to match files in a cross-platform way.

\>\_

```sh
# match .ts files in the current and descendant directories
echo **/*.ts
# match .ts files in the current directory
echo *.ts
# match files that start with "data", have a single number, then end with .csv
echo data[0-9].csv
```

The supported glob characters are `*`, `?`, and `[`/`]`.

### Shell options

`deno task` supports shell options in Deno 2.6.6 and above to control glob expansion and pipeline behavior. By default, `failglob` and `globstar` are enabled.

-   **failglob** - When enabled, globs that don't match any files will cause an error. Disable with `shopt -u failglob`.
-   **globstar** - When enabled, `**` matches zero or more directories. Disable with `shopt -u globstar`.
-   **nullglob** - When enabled, globs that don't match any files expand to nothing instead of the literal glob pattern. Enable with `shopt -s nullglob`.
-   **pipefail** - When enabled, the exit code of a pipeline is the exit code of the last command to exit with a non-zero status, or zero if all commands exit successfully. Enable with `set -o pipefail`.

Examples:

deno.jsonc

```jsonc
{
  "tasks": {
    // disable failglob
    "task1": "shopt -u failglob && rm -rf *.ts",
    // disable failglob and enable nullglob
    "task2": "shopt -u failglob && shopt -s nullglob && rm -rf *.ts",
    // disable globstar
    "task3": "shopt -u globstar && echo **/*.ts",
    // enable pipefail
    "task4": "set -o pipefail && cat missing.txt | echo 'hello'"
  }
}
```

Note

Shell options do not propagate to `deno task` subprocesses. Each `deno task` invocation starts with the default options.

## Built-in commands

`deno task` ships with several built-in commands that work the same out of the box on Windows, Mac, and Linux.

-   [`cp`](https://man7.org/linux/man-pages/man1/cp.1.html) - Copies files.
-   [`mv`](https://man7.org/linux/man-pages/man1/mv.1.html) - Moves files.
-   [`rm`](https://man7.org/linux/man-pages/man1/rm.1.html) - Remove files or directories.
    -   Ex: `rm -rf [FILE]...` - Commonly used to recursively delete files or directories.
-   [`mkdir`](https://man7.org/linux/man-pages/man1/mkdir.1.html) - Makes directories.
    -   Ex. `mkdir -p DIRECTORY...` - Commonly used to make a directory and all its parents with no error if it exists.
-   [`pwd`](https://man7.org/linux/man-pages/man1/pwd.1.html) - Prints the name of the current/working directory.
-   [`sleep`](https://man7.org/linux/man-pages/man1/sleep.1.html) - Delays for a specified amount of time.
    -   Ex. `sleep 1` to sleep for 1 second, `sleep 0.5` to sleep for half a second, or `sleep 1m` to sleep a minute
-   [`echo`](https://man7.org/linux/man-pages/man1/echo.1.html) - Displays a line of text.
-   [`cat`](https://man7.org/linux/man-pages/man1/cat.1.html) - Concatenates files and outputs them on stdout. When no arguments are provided it reads and outputs stdin.
-   [`exit`](https://man7.org/linux/man-pages/man1/exit.1p.html) - Causes the shell to exit.
-   [`head`](https://man7.org/linux/man-pages/man1/head.1.html) - Output the first part of a file.
-   [`unset`](https://man7.org/linux/man-pages/man1/unset.1p.html) - Unsets environment variables.
-   [`xargs`](https://man7.org/linux/man-pages/man1/xargs.1p.html) - Builds arguments from stdin and executes a command.

If you find a useful flag missing on a command or have any suggestions for additional commands that should be supported out of the box, then please [open an issue](https://github.com/denoland/deno_task_shell/issues) on the [deno\_task\_shell](https://github.com/denoland/deno_task_shell/) repo.

Note that if you wish to execute any of these commands in a non-cross-platform way on Mac or Linux, then you may do so by running it through `sh`: `sh -c <command>` (ex. `sh -c cp source destination`).

## package.json support

`deno task` falls back to reading from the `"scripts"` entries in a package.json file if it is discovered. Note that Deno does not respect or support any npm life cycle events like `preinstall` or `postinstall`—you must explicitly run the script entries you want to run (ex. `deno install --entrypoint main.ts && deno task postinstall`).

Command line usage:

```
deno task [OPTIONS] [TASK]
```

Run a task defined in the configuration file:

```
deno task build
```

List all available tasks (from config files in the current and ancestor directories):

```
deno task
```

Evaluate a task from string:

```
deno task --eval "echo $(pwd)"
```

## Options

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--cwd`<DIR>

Specify the directory to run the task in.

`--eval`

Evaluate the passed value as if it was a task in a configuration file.

`--filter, -f`<filter>

Filter members of the workspace by name, implies `--recursive` flag.

`--recursive, -r`

Run the task in all projects in the workspace.

`--tunnel, -t`<tunnel>optional

Execute tasks with a tunnel to Deno Deploy.

Create a secure connection between your local machine and Deno Deploy, providing access to centralised environment variables, logging, and serving from your local environment to the public internet.

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.

`--node-modules-dir`<MODE>optional

Sets the node modules management mode for npm packages.
