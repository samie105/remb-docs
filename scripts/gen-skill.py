#!/usr/bin/env python3
"""
gen-skill.py  --  post-crawl SKILL.md generator
Usage: python3 scripts/gen-skill.py <source-slug>
       python3 scripts/gen-skill.py --all

Reads <slug>/toc.json + manifest.json + up to 10 sample pages, sends to
gpt-4.1-mini via GitHub Models API, writes <slug>/SKILL.md

Links in the generated SKILL.md point to local repo paths (e.g.
nextjs/docs/app/getting-started/installation/index.md), NOT external URLs.
"""

import json, sys, os, subprocess, urllib.request, urllib.error, pathlib, textwrap, random

WORKSPACE = pathlib.Path(__file__).parent.parent
MODEL = "openai/gpt-4.1-mini"
API_URL = "https://models.github.ai/inference/chat/completions"
SAMPLE_PAGES = 10
MAX_PAGE_CHARS = 800  # per page, to stay within context budget


def gh_token():
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    token = result.stdout.strip()
    if not token:
        sys.exit("ERROR: could not get gh auth token — run `gh auth login` first")
    return token


def call_model(token: str, prompt: str) -> str:
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2000,
    }).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    return data["choices"][0]["message"]["content"].strip()


def load_manifest(slug_dir: pathlib.Path) -> dict:
    """Returns url -> {outputPath, title} for visited entries."""
    manifest_path = slug_dir / "manifest.json"
    if not manifest_path.exists():
        return {}
    entries = json.loads(manifest_path.read_text())
    if isinstance(entries, dict):
        entries = entries.get("entries", [])
    return {e["url"]: e for e in entries if e.get("status") == "visited"}


def outputpath_to_local(output_path: str, slug: str) -> str:
    """Strip 'output/' prefix from manifest outputPath."""
    p = output_path
    if p.startswith("output/"):
        p = p[len("output/"):]
    return p


def load_toc(slug: str, slug_dir: pathlib.Path, manifest: dict) -> str:
    """
    Build readable TOC listing titles with LOCAL repo paths (not external URLs).
    """
    toc_path = slug_dir / "toc.json"
    if not toc_path.exists():
        return "(no toc.json found)"

    toc = json.loads(toc_path.read_text())

    # Build url -> local path lookup
    url_to_local = {
        url.rstrip("/"): outputpath_to_local(e["outputPath"], slug)
        for url, e in manifest.items()
    }

    lines = []

    def walk(node, depth=0):
        indent = "  " * depth
        title = node.get("title", "")
        url = node.get("url", "").rstrip("/")
        local = url_to_local.get(url, "")
        if local:
            lines.append(f"{indent}- [{title}]({local})")
        elif title:
            lines.append(f"{indent}- {title}")
        for child in node.get("children", []):
            walk(child, depth + 1)

    if isinstance(toc, list):
        for node in toc:
            walk(node)
    elif isinstance(toc, dict):
        walk(toc)

    return "\n".join(lines[:200])  # cap at 200 entries


def load_sample_pages(slug_dir: pathlib.Path) -> str:
    md_files = list(slug_dir.rglob("*.md"))
    # exclude SKILL.md itself
    md_files = [f for f in md_files if f.name != "SKILL.md"]
    sample = random.sample(md_files, min(SAMPLE_PAGES, len(md_files)))
    parts = []
    for f in sorted(sample):
        text = f.read_text(errors="replace")[:MAX_PAGE_CHARS]
        rel = f.relative_to(slug_dir)
        parts.append(f"### {rel}\n{text}\n")
    return "\n".join(parts)


def build_prompt(slug: str, toc: str, pages: str) -> str:
    return textwrap.dedent(f"""
    You are helping build a developer documentation skill file for an AI coding agent.
    The source is: {slug}

    Below is the table of contents for the crawled docs (with local file paths, NOT external URLs),
    followed by a sample of pages.

    Your job is to write a SKILL.md file that an AI agent can load to understand:
    1. What this library/tool/framework is and what problems it solves
    2. The structure of the docs — key sections and what lives where
    3. How an agent should navigate these docs to answer common dev questions
    4. The most important pages / concepts an agent should know about
    5. Any gotchas or non-obvious things in the docs structure

    IMPORTANT: All links in your output MUST use the local file paths from the TOC below,
    e.g. [Installation](nextjs/docs/app/getting-started/installation/index.md)
    Do NOT use external URLs like https://nextjs.org/... anywhere in the output.

    Write it in clean markdown with clear headings. Be concise but genuinely useful.
    Start directly with the markdown content — no preamble.

    --- TABLE OF CONTENTS (local paths) ---
    {toc}

    --- SAMPLE PAGES ---
    {pages}
    """).strip()


def resolve_slug_dir(slug: str) -> pathlib.Path:
    """Handle nested slugs like bun/bun and deno/deno."""
    direct = WORKSPACE / slug
    nested = direct / slug
    if nested.exists() and (nested / "manifest.json").exists():
        return nested
    return direct


def gen_skill(slug: str, token: str):
    slug_dir = resolve_slug_dir(slug)
    if not slug_dir.exists():
        print(f"  SKIP {slug} — directory not found")
        return

    print(f"  {slug}: loading manifest + toc + pages...")
    manifest = load_manifest(slug_dir)
    toc = load_toc(slug, slug_dir, manifest)
    pages = load_sample_pages(slug_dir)
    prompt = build_prompt(slug, toc, pages)

    print(f"  {slug}: calling {MODEL}...")
    try:
        skill_md = call_model(token, prompt)
    except urllib.error.HTTPError as e:
        print(f"  {slug}: ERROR {e.code} {e.reason}")
        return
    except Exception as e:
        print(f"  {slug}: ERROR {e}")
        return

    out_path = slug_dir / "SKILL.md"
    out_path.write_text(skill_md)
    print(f"  {slug}: wrote {out_path}")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 scripts/gen-skill.py <slug>  OR  --all")
        sys.exit(1)

    token = gh_token()

    if args[0] == "--all":
        slugs = []
        for d in sorted(WORKSPACE.iterdir()):
            if not d.is_dir():
                continue
            name = d.name
            if name in ("node_modules", "packages", "apps", "scripts", "state", "output"):
                continue
            if name.startswith("."):
                continue
            if ".bak-" in name:
                continue
            slugs.append(name)
        print(f"Generating SKILL.md for {len(slugs)} sources: {', '.join(slugs)}")
        for slug in sorted(slugs):
            gen_skill(slug, token)
    else:
        for slug in args:
            gen_skill(slug, token)

    print("Done.")


if __name__ == "__main__":
    main()
