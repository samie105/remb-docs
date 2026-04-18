---
title: "Cron"
source: "https://bun.com/docs/runtime/cron"
canonical_url: "https://bun.com/docs/runtime/cron"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:18.347Z"
content_hash: "124a51196f745022f7f361ccb78d75e75cb4e2e5107fcc5aa8d31ce37c180b23"
menu_path: ["Cron"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/cookies/index.md", "title": "Cookies"}
nav_next: {"path": "bun/bun/docs/runtime/csrf/index.md", "title": "CSRF Protection"}
---

# systemd-based (Ubuntu, Fedora, Arch, etc.)
journalctl -u cron       # or crond on some distros
journalctl -u cron --since "1 hour ago"

# syslog-based (older systems)
grep CRON /var/log/syslog
```

To capture stdout/stderr to a file, redirect output in the crontab entry directly, or add logging inside your `scheduled()` handler. **Manually uninstalling without code:**

```
# Edit your crontab and remove the "# bun-cron: <title>" comment
# and the command line below it
crontab -e

# Or remove ALL bun cron jobs at once by filtering them out:
crontab -l | grep -v "# bun-cron:" | grep -v "\-\-cron-title=" | crontab -
```

### macOS

Bun uses [launchd](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html) to register jobs. Each job is installed as a plist file at:

```
~/Library/LaunchAgents/bun.cron.<title>.plist
```

The plist uses `StartCalendarInterval` to define the schedule. Complex patterns with ranges, lists, or steps are supported — Bun expands them into multiple `StartCalendarInterval` dicts via Cartesian product. **Viewing registered jobs:**

```
launchctl list | grep bun.cron
```

**Logs:** stdout and stderr are written to:

```
/tmp/bun.cron.<title>.stdout.log
/tmp/bun.cron.<title>.stderr.log
```

For example, a job titled `weekly-report`:

```
cat /tmp/bun.cron.weekly-report.stdout.log
tail -f /tmp/bun.cron.weekly-report.stderr.log
```

**Manually uninstalling without code:**

```
# Unload the job from launchd
launchctl bootout gui/$(id -u)/bun.cron.<title>

# Delete the plist file
rm ~/Library/LaunchAgents/bun.cron.<title>.plist

# Example for a job titled "weekly-report":
launchctl bootout gui/$(id -u)/bun.cron.weekly-report
rm ~/Library/LaunchAgents/bun.cron.weekly-report.plist
```

### Windows

Bun uses [Windows Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) with XML-based task definitions. Each job is registered as a scheduled task named `bun-cron-<title>` using [`CalendarTrigger`](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-calendartrigger-triggergroup-element) elements and [`Repetition`](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-repetition-triggerbasetype-element) patterns. Most cron expressions are fully supported, including `@daily`, `@weekly`, `@monthly`, `@yearly`, ranges (`1-5`), lists (`1,15`), named days/months, and day-of-month patterns.

#### User context

Tasks are registered using [`S4U` (Service-for-User)](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-logontype-simpletype) logon type, which runs jobs as the registering user even when not logged in — matching Linux `crontab` behavior. No password is stored. TCP/IP networking (`fetch()`, HTTP, WebSocket, database connections) works normally. The only restriction is that S4U tasks cannot access [Windows-authenticated network resources](https://learn.microsoft.com/en-us/windows/win32/taskschd/security-contexts-for-running-tasks) (SMB file shares, mapped drives, Kerberos/NTLM services). On headless servers and CI environments where the current user’s [Security Identifier (SID)](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/security-identifiers) cannot be resolved — such as service accounts created by [NSSM](https://nssm.cc/) or similar tools — `Bun.cron()` will fail with an error explaining the issue. To work around this, either run Bun as a regular user account, or create the scheduled task manually with `schtasks /create /xml <file> /tn <name> /ru SYSTEM /f`.

#### Trigger limit

**Expressions that work on all platforms:**

Pattern

Trigger strategy

Count

`*/5 * * * *`

Single trigger with [`Repetition`](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-repetition-triggerbasetype-element) (PT5M)

1

`*/15 * * * *`

Single trigger with Repetition (PT15M)

1

`0 9 * * MON-FRI`

One `CalendarTrigger` per weekday

5

`0,30 9-17 * * *`

2 minutes × 9 hours

18

`@daily`, `@weekly`, `@monthly`, `@yearly`

Single trigger

1

**Expressions that fail on Windows** (but work on Linux and macOS):

Pattern

Why

Trigger count

`*/7 * * * *`

9 minute values × 24 hours

216

`*/8 * * * *`

8 minute values × 24 hours

192

`*/9 * * * *`

7 minute values × 24 hours

168

`*/11 * * * *`

6 minute values × 24 hours

144

`*/13 * * * *`

5 minute values × 24 hours

120

`*/15 * * 6 *`

Month restriction prevents Repetition: 4 × 24

96

`0,30 * 15 * FRI`

OR-split doubles triggers: 2 × 24 × 2

96

The key factor is whether the expression can use a [`Repetition`](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-repetition-triggerbasetype-element) interval (single trigger) or must expand to individual `CalendarTrigger` elements. Minute steps that **evenly divide 60** (`*/1`, `*/2`, `*/3`, `*/4`, `*/5`, `*/6`, `*/10`, `*/12`, `*/15`, `*/20`, `*/30`) use Repetition and work regardless of other fields. Steps that don’t divide 60 (`*/7`, `*/8`, `*/9`, `*/11`, `*/13`, etc.) must be expanded, and with 24 hours active, the count quickly exceeds 48. To work around it, simplify the expression or restrict the hour range:

```
// ❌ Fails on Windows: */7 with all hours = 216 triggers
await Bun.cron("./job.ts", "*/7 * * * *", "my-job");

// ✅ Works: restrict to specific hours (9 values × 5 hours = 45 triggers)
await Bun.cron("./job.ts", "*/7 9-13 * * *", "my-job");

// ✅ Works: use a divisor of 60 instead (Repetition, 1 trigger)
await Bun.cron("./job.ts", "*/5 * * * *", "my-job");
```

#### Windows containers

**Viewing registered jobs:**

```
schtasks /query /tn "bun-cron-<title>"

# List all bun cron tasks
schtasks /query | findstr "bun-cron-"
```

**Manually uninstalling without code:**

```
schtasks /delete /tn "bun-cron-<title>" /f

# Example:
schtasks /delete /tn "bun-cron-weekly-report" /f
```

Or open **Task Scheduler** (taskschd.msc), find the task named `bun-cron-<title>`, right-click, and delete it.

* * *

## `Bun.cron.remove()`

Remove a previously registered cron job by its title. Works on all platforms.

```
await Bun.cron.remove("weekly-report");
```

This reverses what `Bun.cron()` did:

Platform

What `remove()` does

Linux

Edits crontab to remove the entry and its marker comment

macOS

Runs `launchctl bootout` and deletes the plist file

Windows

Runs `schtasks /delete` to remove the scheduled task

Removing a job that doesn’t exist resolves without error.

