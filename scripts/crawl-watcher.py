#!/usr/bin/env python3
"""
crawl-watcher.py — polls crawl logs every 3 mins, generates SKILL.md
and sends an email when each source finishes. CPU-friendly.
"""

import time, subprocess, pathlib, json, urllib.request, sys, os

WORKSPACE = pathlib.Path(__file__).parent.parent
OUTPUT_DIR = WORKSPACE / "output"
RUNS_DIR   = WORKSPACE / "state" / "runs"
EMAIL      = "samsonrichfield@gmail.com"
HIMALAYA   = pathlib.Path.home() / ".local/bin/himalaya"
POLL_SECS  = 180  # 3 minutes

SOURCES = [
    "react","vite","astro","svelte","tailwind","prisma",
    "drizzle","trpc","hono","fastify","bun","deno",
    "postgres","redis","supabase"
]

done_set = set()


def gh_token():
    r = subprocess.run(["gh","auth","token"], capture_output=True, text=True)
    return r.stdout.strip()


def call_model(token, prompt):
    body = json.dumps({
        "model": "openai/gpt-4.1-mini",
        "messages": [{"role":"user","content": prompt}],
        "max_tokens": 2000,
    }).encode()
    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
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


def load_toc(slug):
    toc_path = OUTPUT_DIR / slug / "toc.json"
    if not toc_path.exists():
        return "(no toc.json)"
    toc = json.loads(toc_path.read_text())
    lines = []
    def walk(node, depth=0):
        indent = "  " * depth
        lines.append(f"{indent}- {node.get('title','')}  {node.get('url','')}")
        for c in node.get("children", []):
            walk(c, depth+1)
    if isinstance(toc, list):
        [walk(n) for n in toc]
    elif isinstance(toc, dict):
        walk(toc)
    return "\n".join(lines[:200])


def load_sample_pages(slug):
    import random
    src = OUTPUT_DIR / slug
    files = [f for f in src.rglob("*.md") if f.name != "SKILL.md"]
    sample = random.sample(files, min(10, len(files)))
    parts = []
    for f in sorted(sample):
        text = f.read_text(errors="replace")[:800]
        parts.append(f"### {f.relative_to(src)}\n{text}\n")
    return "\n".join(parts)


def gen_skill(slug, token):
    toc   = load_toc(slug)
    pages = load_sample_pages(slug)
    prompt = f"""You are helping build a developer documentation skill file for an AI coding agent.
Source: {slug}

Write a SKILL.md with:
1. What this library/tool is and what problems it solves
2. Structure of the docs — key sections and what lives where
3. How an agent should navigate to answer common dev questions
4. Most important pages/concepts
5. Gotchas or non-obvious things

Be concise but genuinely useful. Start directly with markdown content.

--- TABLE OF CONTENTS ---
{toc}

--- SAMPLE PAGES ---
{pages}"""

    skill_md = call_model(token, prompt)
    out = OUTPUT_DIR / slug / "SKILL.md"
    out.write_text(skill_md)
    return str(out)


def send_email(slug, pages, skill_path):
    subject = f"[remb-docs] {slug} crawl done — {pages} pages"
    body = f"""Hey, the {slug} crawl just finished.

Pages crawled: {pages}
SKILL.md generated: {skill_path}

-- remb-docs watcher
"""
    msg = f"From: samsonrichfield@gmail.com\nTo: {EMAIL}\nSubject: {subject}\n\n{body}"
    result = subprocess.run(
        [str(HIMALAYA), "template", "send"],
        input=msg, text=True, capture_output=True
    )
    if result.returncode == 0:
        print(f"  [{slug}] email sent")
    else:
        print(f"  [{slug}] email failed: {result.stderr[:200]}")


def check_done(slug):
    log = RUNS_DIR / f"{slug}-crawl.log"
    if not log.exists():
        return None
    last = log.read_text().strip().split("\n")[-1]
    if "crawl:done" in last:
        # extract pages count
        for part in last.split():
            if part.startswith("pages="):
                return int(part.split("=")[1])
        return 0
    return None


def main():
    print(f"Watcher started. Polling every {POLL_SECS}s for {len(SOURCES)} sources.")
    token = gh_token()

    while True:
        remaining = [s for s in SOURCES if s not in done_set]
        if not remaining:
            print("All sources done. Watcher exiting.")
            break

        for slug in remaining:
            pages = check_done(slug)
            if pages is not None:
                print(f"[{slug}] DONE — {pages} pages. Generating SKILL.md...")
                try:
                    skill_path = gen_skill(slug, token)
                    print(f"[{slug}] SKILL.md written.")
                    send_email(slug, pages, skill_path)
                except Exception as e:
                    print(f"[{slug}] post-process error: {e}")
                done_set.add(slug)

        remaining = [s for s in SOURCES if s not in done_set]
        print(f"  {len(done_set)}/{len(SOURCES)} done. Still waiting: {', '.join(remaining)}")
        if remaining:
            time.sleep(POLL_SECS)

    print("All done.")


if __name__ == "__main__":
    main()
