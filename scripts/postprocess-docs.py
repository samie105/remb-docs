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

Idempotent: safe to re-run -- only writes files that actually change.
"""

import json
import os
import pathlib
import re
import sys

WORKSPACE = pathlib.Path(__file__).parent.parent


def load_manifest(slug_dir: pathlib.Path) -> dict:
    """url -> {outputPath, title}"""
    manifest_path = slug_dir / "manifest.json"
    if not manifest_path.exists():
        return {}
    entries = json.loads(manifest_path.read_text())
    if isinstance(entries, dict):
        entries = entries.get("entries", [])
    return {e["url"]: e for e in entries if e.get("status") == "visited"}


def load_toc_order(slug_dir: pathlib.Path) -> list:
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
    We detect this by checking if the file actually exists; if not, insert nested segment.
    """
    p = output_path
    if p.startswith("output/"):
        p = p[len("output/"):]

    if slug_dir is None:
        return p

    candidate = WORKSPACE / p
    if candidate.exists():
        return p

    # Try nested variant: 'bun/docs/...' -> 'bun/bun/docs/...'
    parts = pathlib.Path(p).parts
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



def local_to_relpath(current_repo_path: str, target_repo_path: str) -> str:
    """
    Compute a relative path from current_repo_path to target_repo_path.
    Both paths are relative to the repo root.
    """
    cur_dir = os.path.dirname(current_repo_path) or "."
    target = target_repo_path
    rel = os.path.relpath(target, cur_dir)
    return rel if rel.startswith("./") else rel


def rewrite_internal_links(body: str, url_to_local: dict, base_url: str, current_repo_path: str) -> str:
    """
    Replace absolute doc links like (https://nextjs.org/docs/app/getting-started)
    with relative local paths like (installation/index.md).
    Only rewrites links whose URL is in the manifest (i.e. we actually crawled it).
    """
    def replacer(match):
        text = match.group(1)
        url = match.group(2)
        anchor = match.group(3) or ""
        clean_url = url.rstrip("/")
        if clean_url in url_to_local:
            target_repo = url_to_local[clean_url]
            rel = local_to_relpath(current_repo_path, target_repo)
            return f"[{text}]({rel}{anchor})"
        return match.group(0)

    pattern = re.compile(r"\[([^\]]*)\]\((https?://[^)#\s]+)(#[^)\s]*)?\)")
    return pattern.sub(replacer, body)


def split_frontmatter(text: str):
    """
    Split markdown into (fm_block, body) where fm_block includes both --- delimiters.
    Returns ("", text) if no frontmatter found.
    """
    if not text.startswith("---"):
        return "", text
    # find the closing ---
    end = text.index("---", 3)
    fm_block = text[:end + 3]  # includes closing ---
    body = text[end + 3:]
    return fm_block, body


def upsert_nav_in_frontmatter(fm_block: str, nav_extra: dict) -> str:
    """
    Add or replace nav_prev / nav_next lines in a raw frontmatter block.
    Works on the raw string -- avoids full YAML parse/serialize that breaks
    values containing colons (e.g. JSON with URLs).
    nav_extra: dict of key -> value string (already serialized for the line)
    Pass empty dict to remove all nav keys.
    """
    nav_keys = set(nav_extra.keys())
    # All nav keys we ever write -- so stale ones get removed too
    all_nav_keys = {"nav_prev", "nav_next"}
    lines = fm_block.splitlines()
    result = []
    inserted = set()

    for line in lines:
        if ":" in line:
            key = line.split(":", 1)[0].strip()
        else:
            key = ""

        if key in all_nav_keys:
            if key in nav_extra:
                # Replace with new value
                result.append(f"{key}: {nav_extra[key]}")
                inserted.add(key)
            # else: drop stale nav key (page moved to first/last position)
        else:
            result.append(line)

    # Insert any new nav keys before the closing ---
    for k, v in nav_extra.items():
        if k not in inserted:
            result.insert(-1, f"{k}: {v}")

    return "\n".join(result)


def process_slug(slug: str):
    # Determine the slug dir -- could be at root or nested (e.g. bun/bun)
    slug_dir = WORKSPACE / slug
    if not slug_dir.exists():
        print(f"  SKIP {slug} -- directory not found")
        return

    # Some sources nest manifest under a subdirectory (bun/bun, deno/deno)
    manifest_candidates = [slug_dir, slug_dir / slug]
    manifest_dir = next((d for d in manifest_candidates if (d / "manifest.json").exists()), slug_dir)

    manifest = load_manifest(manifest_dir)
    if not manifest:
        print(f"  SKIP {slug} -- no manifest.json or no visited entries")
        return

    toc_urls = load_toc_order(manifest_dir)

    # Build ordered list following toc, then any extras not in toc
    # Deduplicate by output path so files with multiple URLs only appear once
    visited_urls_in_toc = [u for u in toc_urls if u in manifest]
    in_toc_set = set(visited_urls_in_toc)
    # Track which output paths are already in the ordered list
    seen_paths = set()
    deduped_toc = []
    for u in visited_urls_in_toc:
        op = outputpath_to_local(manifest[u]["outputPath"], slug, manifest_dir)
        if op not in seen_paths:
            seen_paths.add(op)
            deduped_toc.append(u)
    # Add extras (sorted for determinism), skipping already-seen paths
    extras = sorted(u for u in manifest if u not in in_toc_set)
    deduped_extras = []
    for u in extras:
        op = outputpath_to_local(manifest[u]["outputPath"], slug, manifest_dir)
        if op not in seen_paths:
            seen_paths.add(op)
            deduped_extras.append(u)
    ordered_urls = deduped_toc + deduped_extras

    # Build url -> local path mapping for link rewriting
    url_to_local = {}
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

        # Split frontmatter (raw) and body
        fm_block, body = split_frontmatter(original)

        # 1. Strip sidebar noise from body
        cleaned_body = strip_sidebar_noise(body.lstrip("\n"))

        # 2. Compute prev/next nav
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
        cleaned_body = rewrite_internal_links(cleaned_body, url_to_local, url, local_path)

        # Upsert nav into raw frontmatter (no full re-serialize)
        if fm_block:
            new_fm = upsert_nav_in_frontmatter(fm_block, nav_extra)
        else:
            # No frontmatter yet -- create one
            lines = ["---"]
            for k, v in nav_extra.items():
                lines.append(f"{k}: {v}")
            lines.append("---")
            new_fm = "\n".join(lines)

        new_text = f"{new_fm}\n\n{cleaned_body.strip()}\n"

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
