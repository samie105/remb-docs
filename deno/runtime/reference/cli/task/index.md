---
title: "deno task"
source: "https://docs.deno.com/runtime/reference/cli/task/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/task/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:08.226Z"
content_hash: "1fb8906412849bbc74e793a8e4add6116eceb2106c34a2cad980d27465a3e21c"
menu_path: ["deno task"]
section_path: []
---
On this page

*   [Description](#description)
*   [Specifying the current working directory](#specifying-the-current-working-directory)
*   [Getting directory deno task was run from](#getting-directory-deno-task-was-run-from)
*   [Wildcard matching of tasks](#wildcard-matching-of-tasks)
*   [Task dependencies](#task-dependencies)
*   [Node and npx binary support](#node-and-npx-binary-support)
*   [Workspace support](#workspace-support)
*   [Syntax](#syntax)
    *   [Boolean lists](#boolean-lists)
    *   [Sequential lists](#sequential-lists)
    *   [Async commands](#async-commands)
    *   [Environment variables](#environment-variables)
        *   [Setting environment variables for a command](#setting-environment-variables-for-a-command)
    *   [Shell variables](#shell-variables)
    *   [Exit status variable](#exit-status-variable)
    *   [Pipelines](#pipelines)
    *   [Command substitution](#command-substitution)
    *   [Negate exit code](#negate-exit-code)
    *   [Redirects](#redirects)
    *   [Cross-platform shebang](#cross-platform-shebang)
    *   [Glob expansion](#glob-expansion)
    *   [Shell options](#shell-options)
*   [Built-in commands](#built-in-commands)
*   [package.json support](#package.json-support)
*   [Options](#options)
*   [Dependency management options](#dependency-management-options)

## Description

`deno task` provides a cross-platform way to define and execute custom commands specific to a codebase.

To get started, define your commands in your codebase's [Deno configuration file](/runtime/fundamentals/configuration/) under a `"tasks"` key.

For example:

deno.json

```jsonc
{
  "tasks": {
    "data": "deno task collect && deno task analyze",
    "collect": "deno run --allow-read=. --allow-write=. scripts/collect.js",
    "analyze": {
      "description": "Run analysis script",
      "command": "deno run --allow-read=. scripts/analyze.js"
    }
  }
}
```

## Specifying the current working directory

By default, `deno task` executes commands with the directory of the Deno configuration file (ex. _deno.json_) as the current working directory. This allows tasks to use relative paths and continue to work regardless of where in the directory tree you happen to execute the deno task from. In some scenarios, this may not be desired and this behavior can be overridden with the `INIT_CWD` environment variable.

`INIT_CWD` will be set with the full path to the directory the task was run in, if not already set. This aligns with the same behavior as `npm run`.

For example, the following task will change the current working directory of the task to be in the same directory the user ran the task from and then output the current working directory which is now that directory (remember, this works on Windows too because `deno task` is cross-platform).

deno.json

```json
{
  "tasks": {
    "my_task": "cd $INIT_CWD && pwd"
  }
}
```

## Getting directory `deno task` was run from

Since tasks are run using the directory of the Deno configuration file as the current working directory, it may be useful to know the directory the `deno task` was executed from instead. This is possible by using the `INIT_CWD` environment variable in a task or script launched from `deno task` (works the same way as in `npm run`, but in a cross-platform way).

For example, to provide this directory to a script in a task, do the following (note the directory is surrounded in double quotes to keep it as a single argument in case it contains spaces):

deno.json

```json
{
  "tasks": {
    "start": "deno run main.ts \"$INIT_CWD\""
  }
}
```

## Wildcard matching of tasks

The `deno task` command can run multiple tasks in parallel by passing a wildcard pattern. A wildcard pattern is specified with the `*` character.

deno.json

```json
{
  "tasks": {
    "build-client": "deno run -RW client/build.ts",
    "build-server": "deno run -RW server/build.ts"
  }
}
```

Running `deno task "build-*"` will run both `build-client` and `build-server` tasks.

Note

**When using a wildcard** make sure to quote the task name (eg. `"build-*"`), otherwise your shell might try to expand the wildcard character, leading to surprising errors.

## Task dependencies

You can specify dependencies for a task:

deno.json

```json
{
  "tasks": {
    "build": "deno run -RW build.ts",
    "generate": "deno run -RW generate.ts",
    "serve": {
      "command": "deno run -RN server.ts",
      "dependencies": ["build", "generate"]
    }
  }
}
```

In the above example, running `deno task serve` will first execute `build` and `generate` tasks in parallel, and once both of them finish successfully the `serve` task will be executed:

\>\_

```sh
deno task serve
Task build deno run -RW build.ts
Task generate deno run -RW generate.ts
Generating data...
Starting the build...
Build finished
Data generated
Task serve deno run -RN server.ts
Listening on http://localhost:8000/
```

Dependency tasks are executed in parallel, with the default parallel limit being equal to number of cores on your machine. To change this limit, use the `DENO_JOBS` environmental variable.

Dependencies are tracked and if multiple tasks depend on the same task, that task will only be run once:

deno.json

```jsonc
{
  //   a
  //  / \
  // b   c
  //  \ /
  //   d
  "tasks": {
    "a": {
      "command": "deno run a.js",
      "dependencies": ["b", "c"]
    },
    "b": {
      "command": "deno run b.js",
      "dependencies": ["d"]
    },
    "c": {
      "command": "deno run c.js",
      "dependencies": ["d"]
    },
    "d": "deno run d.js"
  }
}
```

\>\_

```sh
deno task a
Task d deno run d.js
Running d
Task c deno run c.js
Running c
Task b deno run b.js
Running b
Task a deno run a.js
Running a
```

If a cycle between dependencies is discovered, an error will be returned:

deno.json

```jsonc
{
  "tasks": {
    "a": {
      "command": "deno run a.js",
      "dependencies": ["b"]
    },
    "b": {
      "command": "deno run b.js",
      "dependencies": ["a"]
    }
  }
}
```

\>\_

```sh
deno task a
Task cycle detected: a -> b -> a
```

You can also specify a task that has `dependencies` but no `command`. This is useful to logically group several tasks together:

deno.json

```json
{
  "tasks": {
    "dev-client": "deno run --watch client/mod.ts",
    "dev-server": "deno run --watch sever/mod.ts",
    "dev": {
      "dependencies": ["dev-client", "dev-server"]
    }
  }
}
```

Running `deno task dev` will run both `dev-client` and `dev-server` in parallel.

## Node and npx binary support

By default, `deno task` will execute commands with the `deno` binary. If you need to ensure that a command is run with the `npm` or `npx` binary, you can do so by invoking the `npm` or `npx` `run` command respectively. For example:

deno.json

```json
{
  "tasks": {
    "test:node": "npm run test"
  }
}
```

## Workspace support

`deno task` can be used in workspaces, to run tasks from multiple member directories in parallel. To execute `dev` tasks from all workspace members use `--recursive` flag:

deno.json

```jsonc
{
  "workspace": [
    "client",
    "server"
  ]
}
```

client/deno.json

```jsonc
{
  "name": "@scope/client",
  "tasks": {
    "dev": "deno run -RN build.ts"
  }
}
```

server/deno.json

```jsonc
{
  "name": "@scope/server",
  "tasks": {
    "dev": "deno run -RN server.ts"
  }
}
```

\>\_

```sh
deno task --recursive dev
Task dev deno run -RN build.ts
Task dev deno run -RN server.ts
Bundling project...
Listening on http://localhost:8000/
Project bundled
```

Tasks to run can be filtered based on the workspace members:

\>\_

```sh
deno task --filter "client" dev
Task dev deno run -RN build.ts
Bundling project...
Project bundled
```

Note that the filter matches against the workspace member names as specified in the `name` field of each member's [`deno.json`](/runtime/fundamentals/configuration/) file.

## Syntax

`deno task` uses a cross-platform shell that's a subset of sh/bash to execute defined tasks.

### Boolean lists

Boolean lists provide a way to execute additional commands based on the exit code of the initial command. They separate commands using the `&&` and `||` operators.

The `&&` operator provides a way to execute a command and if it _succeeds_ (has an exit code of `0`) it will execute the next command:

\>\_

```sh
deno run --allow-read=. --allow-write=. collect.ts && deno run --allow-read=. analyze.ts
```

The `||` operator is the opposite. It provides a way to execute a command and only if it _fails_ (has a non-zero exit code) it will execute the next command:

\>\_

```sh
deno run --allow-read=. --allow-write=. collect.ts || deno run play_sad_music.ts
```

### Sequential lists

Sequential lists are similar to boolean lists, but execute regardless of whether the previous command in the list passed or failed. Commands are separated with a semi-colon (`;`).

\>\_

```sh
deno run output_data.ts ; deno run --allow-net server.ts
```

### Async commands

Async commands provide a way to make a command execute asynchronously. This can be useful when starting multiple processes. To make a command asynchronous, add an `&` to the end of it. For example the following would execute `sleep 1 && deno run --allow-net server.ts` and `deno run --allow-net client.ts` at the same time:

\>\_

```sh
sleep 1 && deno run --allow-net server.ts & deno run --allow-net client.ts
```

Unlike in most shells, the first async command to fail will cause all the other commands to fail immediately. In the example above, this would mean that if the server command fails then the client command will also fail and exit. You can opt out of this behavior by adding `|| true` to the end of a command, which will force a `0` exit code. For example:

\>\_

```sh
deno run --allow-net server.ts || true & deno run --allow-net client.ts || true
```

### Environment variables

Environment variables are defined like the following:

\>\_

```sh
export VAR_NAME=value
```

Here's an example of using one in a task with shell variable substitution and then with it being exported as part of the environment of the spawned Deno process (note that in the JSON configuration file the double quotes would need to be escaped with backslashes):

\>\_

```sh
export VAR=hello && echo $VAR && deno eval "console.log('Deno: ' + Deno.env.get('VAR'))"
```

Would output:

\>\_

```sh
hello
Deno: hello
```

#### Setting environment variables for a command

To specify environment variable(s) before a command, list them like so:

\>\_

```sh
VAR=hello VAR2=bye deno run main.ts
```

This will use those environment variables specifically for the following command.

### Shell variables

Shell variables are similar to environment variables, but won't be exported to spawned commands. They are defined with the following syntax:

\>\_

```sh
VAR_NAME=value
```

If we use a shell variable instead of an environment variable in a similar example to what's shown in the previous "Environment variables" section:

\>\_

```sh
VAR=hello && echo $VAR && deno eval "console.log('Deno: ' + Deno.env.get('VAR'))"
```

We will get the following output:

\>\_

```sh
hello
Deno: undefined
```

Shell variables can be useful when we want to reuse a value, but don't want it available in any spawned processes.

### Exit status variable

The exit code of the previously run command is available in the `$?` variable.

\>\_

```sh
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

*   **failglob** - When enabled, globs that don't match any files will cause an error. Disable with `shopt -u failglob`.
*   **globstar** - When enabled, `**` matches zero or more directories. Disable with `shopt -u globstar`.
*   **nullglob** - When enabled, globs that don't match any files expand to nothing instead of the literal glob pattern. Enable with `shopt -s nullglob`.
*   **pipefail** - When enabled, the exit code of a pipeline is the exit code of the last command to exit with a non-zero status, or zero if all commands exit successfully. Enable with `set -o pipefail`.

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

*   [`cp`](https://man7.org/linux/man-pages/man1/cp.1.html) - Copies files.
*   [`mv`](https://man7.org/linux/man-pages/man1/mv.1.html) - Moves files.
*   [`rm`](https://man7.org/linux/man-pages/man1/rm.1.html) - Remove files or directories.
    *   Ex: `rm -rf [FILE]...` - Commonly used to recursively delete files or directories.
*   [`mkdir`](https://man7.org/linux/man-pages/man1/mkdir.1.html) - Makes directories.
    *   Ex. `mkdir -p DIRECTORY...` - Commonly used to make a directory and all its parents with no error if it exists.
*   [`pwd`](https://man7.org/linux/man-pages/man1/pwd.1.html) - Prints the name of the current/working directory.
*   [`sleep`](https://man7.org/linux/man-pages/man1/sleep.1.html) - Delays for a specified amount of time.
    *   Ex. `sleep 1` to sleep for 1 second, `sleep 0.5` to sleep for half a second, or `sleep 1m` to sleep a minute
*   [`echo`](https://man7.org/linux/man-pages/man1/echo.1.html) - Displays a line of text.
*   [`cat`](https://man7.org/linux/man-pages/man1/cat.1.html) - Concatenates files and outputs them on stdout. When no arguments are provided it reads and outputs stdin.
*   [`exit`](https://man7.org/linux/man-pages/man1/exit.1p.html) - Causes the shell to exit.
*   [`head`](https://man7.org/linux/man-pages/man1/head.1.html) - Output the first part of a file.
*   [`unset`](https://man7.org/linux/man-pages/man1/unset.1p.html) - Unsets environment variables.
*   [`xargs`](https://man7.org/linux/man-pages/man1/xargs.1p.html) - Builds arguments from stdin and executes a command.

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
