#!/usr/bin/env python3
"""
gen-rich-knowledge.py -- Generate enriched llms.txt + network-style SKILL.md per source.
Uses kimi-k2.6 via Ollama Cloud (reads OLLAMA_API_KEY from env or ~/.hermes/.env).

Model prompt produces rich SKILL.md (network of knowledge: learning paths, concept map, dependencies).
Local parsing produces structured llms.txt (flat index + concept index from headings).

Usage: python3 scripts/gen-rich-knowledge.py <slug>
"""

import json, os, re, sys, urllib.request, pathlib, time
from collections import defaultdict

WORKSPACE = pathlib.Path("/root/remb-docs")
API_URL = "https://ollama.com/v1/chat/completions"
MODEL = "kimi-k2.6"
MAX_TOKENS = 16000
TIMEOUT = 600


def get_api_key() -> str:
    key = os.environ.get("OLLAMA_API_KEY", "")
    if key:
        return key
    env_path = pathlib.Path("/root/.hermes/.env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("OLLAMA_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("ERROR: OLLAMA_API_KEY not found in env or ~/.hermes/.env")


def ollama_chat(prompt: str, retries: int = 2) -> str:
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": MAX_TOKENS,
        "temperature": 0.3,
        "stream": False,
    }).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {get_api_key()}",
            "Content-Type": "application/json"
        },
        method="POST",
    )
    last_err = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                data = json.load(resp)
            content = data["choices"][0]["message"]["content"]
            if content is None:
                content = ""
            return content.strip()
        except Exception as e:
            last_err = str(e)
            if attempt < retries:
                wait = 10 * (attempt + 1)
                print(f"  Retry {attempt + 1} after {wait}s: {last_err[:120]}")
                time.sleep(wait)
                continue
    raise RuntimeError(f"ollama_chat failed after {retries + 1} attempts: {last_err}")


def extract_page_data(slug_dir: pathlib.Path):
    pages = []
    for md_file in sorted(slug_dir.rglob("*.md")):
        if md_file.name == "SKILL.md":
            continue
        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        fm = {}
        body = text
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                for line in text[3:end].strip().splitlines():
                    if ":" in line and not line.strip().startswith("-"):
                        k, _, v = line.partition(":")
                        fm[k.strip()] = v.strip().strip('"').strip("'")
                body = text[end + 3:]

        headings = re.findall(r'^(#{1,3})\s+(.+)$', body, re.MULTILINE)
        local_links = re.findall(r'\]\(([^)]+)\)', body)
        local_links = [
            l for l in local_links
            if not l.startswith("http") and not l.startswith("#")
        ]
        code_langs = re.findall(r'```(\w+)', body)
        relative = str(md_file.relative_to(WORKSPACE))

        pages.append({
            "path": relative,
            "title": fm.get("title", headings[0][1] if headings else md_file.name),
            "source": fm.get("source", ""),
            "headings": [h[1] for h in headings[:8]],
            "local_links": local_links[:10],
            "code_langs": list(set(code_langs))[:5],
            "char_count": len(body),
            "kind": fm.get("kind", ""),
        })
    return pages


def build_graph(pages):
    concept_to_pages = defaultdict(list)
    path_set = {p["path"] for p in pages}
    link_graph = defaultdict(list)

    for p in pages:
        for h in p["headings"]:
            stripped = re.sub(r'[^\w\s/-]', '', h).strip().lower()
            concept = re.sub(r'https?\S+', '', stripped).strip()
            concept = re.sub(r'\s+', ' ', concept)
            if len(concept) > 2 and not concept.endswith((' direct link to',)):
                concept_to_pages[concept].append(p["path"])
        for link in p["local_links"]:
            link_clean = link.lstrip("/").rstrip("/")
            matched = None
            for known in path_set:
                if known.endswith(link_clean) or known.rstrip(".md").endswith(link_clean.rstrip(".md")):
                    matched = known
                    break
            if matched and matched != p["path"]:
                link_graph[p["path"]].append(matched)

    return dict(concept_to_pages), dict(link_graph)


def build_llms_local(slug: str, pages, concept_map):
    lines = [f"# {slug.title()}", ""]
    lines.append(f"\u003e Documentation corpus for {slug.title()}. {len(pages)} pages.")
    lines.append("")

    # Concept index
    lines.append("## Concept Index")
    lines.append("")
    top_concepts = sorted(concept_map.items(), key=lambda x: len(x[1]), reverse=True)[:50]
    for c, paths in top_concepts:
        best = min(paths, key=len)
        lines.append(f"- **{c}** — [`{best}`]({best})")
    lines.append("")

    # Group by first path segment
    lines.append("## Pages by Area")
    lines.append("")
    groups = defaultdict(list)
    for p in pages:
        parts = pathlib.Path(p["path"]).parts[1:]
        area = parts[0] if parts else "general"
        groups[area].append(p)
    for area, group in sorted(groups.items()):
        lines.append(f"### {area}")
        for p in group:
            lines.append(f"- [{p['title']}]({p['path']})")
        lines.append("")

    return "\n".join(lines)


def build_skill_prompt(slug, pages, concept_map, link_graph):
    centrality = defaultdict(int)
    for src, targets in link_graph.items():
        centrality[src] += len(targets)
        for t in targets:
            centrality[t] += 1

    sorted_pages = sorted(pages, key=lambda p: centrality.get(p["path"], 0), reverse=True)
    selected = []
    seen = set()
    for p in sorted_pages[:15]:
        selected.append(p)
        seen.add(p["path"])
    for p in pages[:5]:
        if p["path"] not in seen:
            selected.append(p)
            seen.add(p["path"])
    selected.sort(key=lambda p: pages.index(p))

    page_blocks = []
    for p in selected:
        links = ", ".join(p["local_links"][:5]) if p["local_links"] else "none"
        block = (
            f"Title: {p['title']}\n"
            f"Path: {p['path']}\n"
            f"Headings: {', '.join(p['headings'][:5])}\n"
            f"Links: {links}\n"
            f"Code: {', '.join(p['code_langs']) or 'none'}"
        )
        page_blocks.append(block)

    top_concepts = sorted(concept_map.items(), key=lambda x: len(x[1]), reverse=True)[:20]
    concept_block = "\n".join(
        f"- {c} ({len(paths)} pages)"
        for c, paths in top_concepts
    )

    page_blocks_text = "\n\n".join(page_blocks)

    prompt = f"""You are a documentation architect building a knowledge network for `{slug}`.
Below is extracted metadata from {len(pages)} local documentation pages.

TOP CONCEPTS:
{concept_block}

KEY PAGES:
{page_blocks_text}

TASK: Write a single markdown document (SKILL.md style) with ONLY these sections. No commentary, no reasoning outside the output:

1. **Overview** — 2-3 sentences on what {slug} is and why an agent needs to know it.
2. **Mental Model** — A short paragraph describing the architecture or core philosophy, with links to canonical pages.
3. **Learning Paths** — 3 ordered paths for different scenarios (e.g., "Getting Started", "Production Ready", "Reference Deep-Dive"). Each step names a page path.
4. **Concept Map** — Bulleted tree: top-level concepts → sub-concepts → page paths. Group related ideas together.
5. **If You Need To...** — A quick-reference table: "If you need to X → read `page.md`"
6. **Top Must-Know Pages** — Numbered list of 10 pages. 1 sentence each. Include page path.

RULES:
- Use ONLY local paths like `{slug}/docs/page.md`. NEVER use https:// links.
- Do not include a reasoning block or any text outside the markdown sections.
- Be concise. Each section should be scannable in under 30 seconds.
"""
    return prompt


def clean_md(text: str) -> str:
    text = re.sub(r'^```markdown\s*\n?', '', text)
    text = re.sub(r'```\s*$', '', text)
    return text.strip()


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 scripts/gen-rich-knowledge.py <slug>")
    slug = sys.argv[1]
    slug_dir = WORKSPACE / slug
    if not slug_dir.exists():
        sys.exit(f"ERROR: directory not found: {slug_dir}")

    print(f"[{slug}] Scanning pages...")
    pages = extract_page_data(slug_dir)
    if not pages:
        sys.exit("ERROR: no .md pages found")
    print(f"[{slug}] Found {len(pages)} pages")

    print(f"[{slug}] Building graph...")
    concept_map, link_graph = build_graph(pages)
    print(f"[{slug}] Concepts: {len(concept_map)}, Internal links: {sum(len(v) for v in link_graph.values())}")

    # Generate llms.txt locally
    llms_txt = build_llms_local(slug, pages, concept_map)
    llms_path = WORKSPACE / slug / "llms.txt"
    llms_path.write_text(llms_txt, encoding="utf-8")
    print(f"[{slug}] Wrote {llms_path} ({len(llms_txt.splitlines())} lines)")

    # Generate SKILL.md via model
    prompt = build_skill_prompt(slug, pages, concept_map, link_graph)
    print(f"[{slug}] Prompt: {len(prompt)} chars (~{len(prompt)//4} tok)")
    print(f"[{slug}] Calling {MODEL}...")

    skill_md = clean_md(ollama_chat(prompt))
    skill_path = WORKSPACE / slug / "SKILL.md"
    skill_path.write_text(skill_md, encoding="utf-8")
    print(f"[{slug}] Wrote {skill_path} ({len(skill_md.splitlines())} lines)")


if __name__ == "__main__":
    main()
