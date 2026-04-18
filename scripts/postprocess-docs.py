#!/usr/bin/env python3
"""
postprocess-docs.py  --  post-crawl cleanup pass
Usage:
    python3 scripts/postprocess-docs.py <slug>
    python3 scripts/postprocess-docs.py --all

For each source in the flat repo structure (<slug>/):
  1. Strips sidebar/nav noise before the first H1 heading
  2. Adds nav_prev / nav_next frontmatter based on toc.json ordering
  3. Rewrites internal links from absolute URL to relative local paths

Idempotent: safe to re-run — only writes files that actually change.
"""

import json
import pathlib
import re
import sys
import textwrap

WORKSPACE = pathlib.Path(__file__).parent.parent


def load_manifest(slug_dir: pathlib.Path) -> dict[str, dict]:
    """url -> {outputPath, title}"""
    manifest_path = slug_dir / "manifest.json"
    if not manifest_path.exists():
        return {}
    entries = json.loads(manifest_path.read_text())
    if isinstance(entries, dict):
        entries = entries.get("entries", [])
    return {e["url"]: e for e in entries if e.get("status") == "visited"}


def load_toc_order(slug_dir: pathlib.Path) -> list[str]:
    """Return URLs in toc order (flattened)."""
    toc_path = slug_dir / "toc.json"
    if not toc_path.exists():
        return []
    toc = json.loads(toc_path.read_text())
    urls = []

    def walk(node):
        url = node.get("url", "")
        if url:
            urls.append(url)
        for child in node.get("children", []):
            walk(child)

    if isinstance(toc, list):
        for n in toc:
            walk(n)
    else:
        walk(toc)
    return urls


def outputpath_to_local(output_path: str, slug: str, slug_dir: pathlib.Path = None) -> str:
    """
    Convert manifest outputPath like 'output/nextjs/docs/app/index.md'
    to local repo path like 'nextjs/docs/app/index.md'.

    For nested slugs (bun/bun, deno/deno) the manifest says
    'output/bun/docs/...' but files live at 'bun/bun/docs/...'.
    We detect this by checking if the file actually exists at the
    resolved path; if not, we insert the nested segment.
    """
    p = output_path
    if p.startswith("output/"):
        p = p[len("output/"):]

    if slug_dir is None:
        return p

    # Check if the file exists at <WORKSPACE>/<p>
    candidate = WORKSPACE / p
    if candidate.exists():
        return p

    # Try the nested variant: e.g. 'bun/docs/...' -> 'bun/bun/docs/...'
    parts = pathlib.Path(p).parts  # ('bun', 'docs', ...)
    if len(parts) > 1 and parts[0] == slug:
        nested = pathlib.Path(slug) / slug / pathlib.Path(*parts[1:])
        if (WORKSPACE / nested).exists():
            return str(nested)

    return p


def strip_sidebar_noise(body: str) -> str:
    """
    Remove all content before the first H1 (# ...) heading.
    If there is no H1, return body unchanged.
    """
    m = re.search(r"^# .+", body, re.MULTILINE)
    if not m:
        return body
    return body[m.start():]


def rewrite_internal_links(body: str, url_to_local: dict[str, str], base_url: str) -> str:
    """
    Replace absolute doc links like (https://nextjs.org/docs/app/getting-started)
    with relative local paths like (../../getting-started/index.md).
    Only rewrites links whose URL is in the manifest (i.e. we actually crawled it).
    """
    # We'll rewrite markdown links [text](url) and [text](url#anchor)
    def replacer(match):
        text = match.group(1)
        url = match.group(2)
        anchor = match.group(3) or ""
        # Normalise: strip trailing slash
        clean_url = url.rstrip("/")
        if clean_url in url_to_local:
            local = url_to_local[clean_url]
            return f"[{text}]({local}{anchor})"
        return match.group(0)

    # Match [text](https://...) optionally with #anchor
    pattern = re.compile(r"\[([^\]]*)\]\((https?://[^)#\s]+)(#[^)\s]*)?\)")
    return pattern.sub(replacer, body)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown. Returns (fm_dict, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.index("---", 3)
    fm_raw = text[3:end].strip()
    body = text[end + 3:].lstrip("\n")
    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, body


def build_frontmatter(fm: dict, extra: dict) -> str:
    """Rebuild frontmatter, merging in extra keys."""
    merged = {**fm, **extra}
    lines = ["---"]
    for k, v in merged.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def process_slug(slug: str):
    # Determine the slug dir — could be at root or nested (e.g. bun/bun)
    slug_dir = WORKSPACE / slug
    if not slug_dir.exists():
        print(f"  SKIP {slug} — directory not found")
        return

    # Some sources nest manifest under a subdirectory (bun/bun, deno/deno)
    manifest_candidates = [slug_dir, slug_dir / slug]
    manifest_dir = next((d for d in manifest_candidates if (d / "manifest.json").exists()), slug_dir)

    manifest = load_manifest(manifest_dir)
    if not manifest:
        print(f"  SKIP {slug} — no manifest.json or no visited entries")
        return

    toc_urls = load_toc_order(manifest_dir)

    # Build ordered list of visited pages following toc order
    visited_urls_in_toc = [u for u in toc_urls if u in manifest]
    # Add any visited URLs not in toc (appended at end)
    in_toc_set = set(visited_urls_in_toc)
    extras = [u for u in manifest if u not in in_toc_set]
    ordered_urls = visited_urls_in_toc + extras

    # Build url -> local path mapping for link rewriting
    # Local path is relative to repo root: slug/docs/...
    url_to_local: dict[str, str] = {}
    for url, entry in manifest.items():
        local = outputpath_to_local(entry["outputPath"], slug, manifest_dir)
        url_to_local[url.rstrip("/")] = local

    changed = skipped = 0

    for i, url in enumerate(ordered_urls):
        entry = manifest[url]
        local_path = outputpath_to_local(entry["outputPath"], slug, manifest_dir)
        file_path = WORKSPACE / local_path

        if not file_path.exists():
            continue

        original = file_path.read_text(errors="replace")

        # Parse frontmatter
        fm, body = parse_frontmatter(original)

        # 1. Strip sidebar noise
        cleaned_body = strip_sidebar_noise(body)

        # 2. Compute prev/next
        nav_extra = {}
        if i > 0:
            prev_url = ordered_urls[i - 1]
            prev_local = url_to_local.get(prev_url.rstrip("/"), "")
            prev_title = manifest[prev_url].get("title", "")
            if prev_local:
                nav_extra["nav_prev"] = json.dumps({"path": prev_local, "title": prev_title})
        if i < len(ordered_urls) - 1:
            next_url = ordered_urls[i + 1]
            next_local = url_to_local.get(next_url.rstrip("/"), "")
            next_title = manifest[next_url].get("title", "")
            if next_local:
                nav_extra["nav_next"] = json.dumps({"path": next_local, "title": next_title})

        # 3. Rewrite internal links in body
        cleaned_body = rewrite_internal_links(cleaned_body, url_to_local, url)

        # Rebuild the file
        new_fm = build_frontmatter(fm, nav_extra)
        new_text = f"{new_fm}\n\n{cleaned_body}\n"

        if new_text == original:
            skipped += 1
            continue

        file_path.write_text(new_text)
        changed += 1

    print(f"  {slug}: {changed} files updated, {skipped} unchanged out of {len(ordered_urls)} total")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 scripts/postprocess-docs.py <slug>  OR  --all")
        sys.exit(1)

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
        print(f"Post-processing {len(slugs)} sources: {', '.join(slugs)}")
        for slug in slugs:
            process_slug(slug)
    else:
        for slug in args:
            process_slug(slug)

    print("Done.")


if __name__ == "__main__":
    main()
