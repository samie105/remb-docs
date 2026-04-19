#!/usr/bin/env python3
"""
gen-skill.py  --  post-crawl SKILL.md generator
Usage: python3 scripts/gen-skill.py <source-slug>
       python3 scripts/gen-skill.py --all

Reads <slug>/toc.json + manifest.json + up to 35 pages (TOC-order sampled),
sends to gpt-4.1 via GitHub Models API, writes <slug>/SKILL.md

Links in the generated SKILL.md point to local repo paths (e.g.
nextjs/docs/app/getting-started/installation/index.md), NOT external URLs.

Page selection strategy:
  - Take the first 10 pages in TOC order (intro / getting-started)
  - Take the last 5 pages (API reference tail)
  - Sample 20 more evenly-spaced across the middle
  - Deduplicate, preserve TOC order
"""

import json, sys, os, subprocess, urllib.request, urllib.error, pathlib, textwrap, time

WORKSPACE = pathlib.Path(__file__).parent.parent
MODEL = "openai/gpt-4.1"
API_URL = "https://models.github.ai/inference/chat/completions"
SAMPLE_PAGES = 25
MAX_PAGE_CHARS = 800   # per page
MAX_TOKENS = 2000
MAX_PROMPT_CHARS = 22_000  # GitHub Models gpt-4.1: 8K token limit. ~22K chars = ~5.5K tokens, leaves room for response


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
        "max_tokens": MAX_TOKENS,
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
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.load(resp)
    return data["choices"][0]["message"]["content"].strip()


def load_manifest(slug_dir: pathlib.Path) -> dict:
    """Returns url -> entry for visited entries."""
    manifest_path = slug_dir / "manifest.json"
    if not manifest_path.exists():
        return {}
    entries = json.loads(manifest_path.read_text())
    if isinstance(entries, dict):
        entries = entries.get("entries", [])
    return {e["url"]: e for e in entries if e.get("status") == "visited"}


def outputpath_to_local(output_path: str, slug: str, slug_dir: pathlib.Path) -> str:
    """Strip 'output/' prefix; resolve nested slugs (bun/bun, deno/deno)."""
    p = output_path
    if p.startswith("output/"):
        p = p[len("output/"):]
    candidate = WORKSPACE / p
    if candidate.exists():
        return p
    parts = pathlib.Path(p).parts
    if len(parts) > 1 and parts[0] == slug:
        nested = pathlib.Path(slug) / slug / pathlib.Path(*parts[1:])
        if (WORKSPACE / nested).exists():
            return str(nested)
    return p


def load_toc_order(slug_dir: pathlib.Path) -> list[str]:
    """Return list of URLs in TOC order (flattened)."""
    toc_path = slug_dir / "toc.json"
    if not toc_path.exists():
        return []
    toc = json.loads(toc_path.read_text())
    urls = []
    def walk(node):
        url = node.get("url", "")
        if url:
            urls.append(url.rstrip("/"))
        for child in node.get("children", []):
            walk(child)
    if isinstance(toc, list):
        for n in toc:
            walk(n)
    else:
        walk(toc)
    return urls


def load_toc_text(slug: str, slug_dir: pathlib.Path, manifest: dict) -> str:
    """Build readable TOC with local file paths."""
    toc_path = slug_dir / "toc.json"
    if not toc_path.exists():
        return "(no toc.json found)"
    toc = json.loads(toc_path.read_text())
    url_to_local = {
        url.rstrip("/"): outputpath_to_local(e["outputPath"], slug, slug_dir)
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
    return "\n".join(lines[:150])  # cap at 150 entries to keep prompt size sane


def select_pages(toc_urls: list[str], manifest: dict, slug: str, slug_dir: pathlib.Path) -> list[pathlib.Path]:
    """
    Smart page selection: first 10 (intro), last 5 (API ref tail),
    20 evenly-spaced from the middle. Dedup, preserve TOC order.
    """
    # Build ordered list of (url, local_path) from TOC
    ordered = []
    seen = set()
    for url in toc_urls:
        entry = manifest.get(url) or manifest.get(url + "/")
        if not entry:
            continue
        local = outputpath_to_local(entry["outputPath"], slug, slug_dir)
        fp = WORKSPACE / local
        if not fp.exists() or local in seen:
            continue
        seen.add(local)
        ordered.append(fp)

    # Fallback: if toc didn't give us enough, scan directory
    if len(ordered) < 5:
        ordered = [f for f in sorted(slug_dir.rglob("*.md")) if f.name != "SKILL.md"]

    n = len(ordered)
    if n <= SAMPLE_PAGES:
        return ordered

    head = ordered[:10]
    tail = ordered[max(10, n - 5):]
    middle = ordered[10:max(10, n - 5)]

    # Evenly sample up to 20 from the middle
    budget = SAMPLE_PAGES - len(head) - len(tail)
    if middle and budget > 0:
        step = max(1, len(middle) // budget)
        sampled_middle = middle[::step][:budget]
    else:
        sampled_middle = []

    combined = []
    seen2 = set()
    for f in head + sampled_middle + tail:
        if f not in seen2:
            combined.append(f)
            seen2.add(f)
    return combined


def load_sample_pages(pages: list[pathlib.Path], slug_dir: pathlib.Path) -> str:
    parts = []
    for f in pages:
        text = f.read_text(errors="replace")[:MAX_PAGE_CHARS]
        rel = f.relative_to(WORKSPACE)
        parts.append(f"### {rel}\n{text}\n")
    return "\n".join(parts)


def build_prompt(slug: str, toc: str, pages: str) -> str:
    return textwrap.dedent(f"""
    You are helping build a developer documentation skill file for an AI coding agent.
    The documentation source is: {slug}

    Below is the full table of contents (with local repo file paths, NOT external URLs),
    followed by a curated sample of pages (intro pages, key concept pages, API reference tail).

    Write a SKILL.md that an AI agent can load to:
    1. Understand what this library/tool/framework does and the problems it solves
    2. Know the doc structure — key sections, what lives where
    3. Navigate the docs efficiently to answer common developer questions
    4. Know the most important concepts, patterns, and gotchas
    5. Find the right page for any task (with local file path links)

    Quality bar: production-grade, genuinely useful to a developer agent. Include:
    - A concise overview (2-3 sentences)
    - Key concepts section with brief explanations
    - Navigation guide: which sections to look in for common task types
    - Top 10-15 most important pages with local links and one-line descriptions
    - Any notable gotchas or non-obvious doc structure quirks

    CRITICAL: Every link MUST use the local repo path format from the TOC below.
    Example: [Installation](nextjs/docs/app/getting-started/installation/index.md)
    Do NOT use any external URLs (no https://...) anywhere in your output.

    Start directly with the markdown — no preamble or meta-commentary.

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

    print(f"  {slug}: loading manifest + toc...")
    manifest = load_manifest(slug_dir)
    if not manifest:
        print(f"  SKIP {slug} — no manifest.json")
        return

    toc_urls = load_toc_order(slug_dir)
    toc_text = load_toc_text(slug, slug_dir, manifest)
    pages = select_pages(toc_urls, manifest, slug, slug_dir)
    pages_text = load_sample_pages(pages, slug_dir)

    print(f"  {slug}: {len(pages)} pages selected, calling {MODEL}...")
    prompt = build_prompt(slug, toc_text, pages_text)
    # Trim prompt if over hard cap (truncate pages section)
    if len(prompt) > MAX_PROMPT_CHARS:
        overage = len(prompt) - MAX_PROMPT_CHARS
        pages_text = pages_text[:-overage]
        prompt = build_prompt(slug, toc_text, pages_text)

    try:
        skill_md = call_model(token, prompt)
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print(f"  {slug}: rate limited, waiting 60s...")
            time.sleep(60)
            try:
                skill_md = call_model(token, prompt)
            except Exception as e2:
                print(f"  {slug}: ERROR after retry: {e2}")
                return
        else:
            print(f"  {slug}: ERROR {e.code} {e.reason}")
            return
    except Exception as e:
        print(f"  {slug}: ERROR {e}")
        return

    out_path = slug_dir / "SKILL.md"
    # Strip wrapping ```markdown ... ``` if the model added it
    if skill_md.startswith("```"):
        lines = skill_md.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        skill_md = "\n".join(lines).strip()
    out_path.write_text(skill_md)
    print(f"  {slug}: wrote {out_path} ({len(skill_md)} chars)")


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
        for i, slug in enumerate(sorted(slugs)):
            if i > 0:
                time.sleep(8)  # throttle to avoid 429
            gen_skill(slug, token)
    else:
        for slug in args:
            gen_skill(slug, token)

    print("Done.")


if __name__ == "__main__":
    main()
