---
title: "Feedback"
source: "https://bun.com/docs/feedback"
canonical_url: "https://bun.com/docs/feedback"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:32.131Z"
content_hash: "5731032b61d6544ca154af1e6f23db4819d0d5e5525405f41b9bbd3c0e5af686"
menu_path: ["Feedback"]
section_path: []
nav_prev: {"path": "bun/docs/bundler/standalone-html/index.md", "title": "Standalone HTML"}
nav_next: {"path": "bun/docs/guides/index.md", "title": "Guides"}
---

# To revert back to the stable
bun upgrade --stable
```

If the issue still persists after upgrading, continue to the next step.

2

[

](#)

Review Existing Issues

First take a minute to check if the issue has already been reported. Don’t open a new issue if it has already been reported, it saves time for everyone and helps us focus on fixing things faster.

*   🔍 [**Search existing issues**](https://github.com/oven-sh/bun/issues)
*   💬 [**Check discussions**](https://github.com/oven-sh/bun/discussions)

If you find a related issue, add a 👍 reaction or comment with extra details instead of opening a new one.

3

[

](#)

Report the Issue

If no one has reported the issue, please open a new issue or suggest an improvement.

*   🐞 [**Report a Bug**](https://github.com/oven-sh/bun/issues/new?template=2-bug-report.yml)
*   ⚡ [**Suggest an Improvement**](https://github.com/oven-sh/bun/issues/new?template=4-feature-request.yml)

Please provide as much detail as possible, including:

*   A clear and concise title
*   A code example or steps to reproduce the issue
*   The version of Bun you are using (run `bun --version`)
*   A detailed description of the issue (what happened, what you expected to happen, and what actually happened)
*   The operating system and version you are using
    
    *   For MacOS and Linux: copy the output of `uname -mprs`
    *   For Windows: copy the output of this command in the powershell console: `"$([Environment]::OSVersion | ForEach-Object VersionString) $(if ([Environment]::Is64BitOperatingSystem) { "x64" } else { "x86" })"`
    

The Bun team will review the issue and get back to you as soon as possible!

* * *

## 

[​

](#use-bun-feedback)

Use `bun feedback`

Alternatively, you can use `bun feedback` to share feedback, bug reports, and feature requests directly with the Bun team.

terminal

```
bun feedback "Love the new release!"
bun feedback report.txt details.log
echo "please document X" | bun feedback --email you@example.com
```

You can provide feedback as text arguments, file paths, or piped input.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/feedback.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /feedback>)
