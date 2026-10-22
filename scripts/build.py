#!/usr/bin/env python3
"""Build the distributable forms of every skill.

  python3 scripts/build.py

Writes:
  .claude-plugin/marketplace.json                 Claude Code marketplace (one plugin per category)
  plugins/<cat>/.claude-plugin/plugin.json        plugin manifest per category
  dist/zips/<name>.zip                            upload to Claude.ai (folder <name>/ at the zip root)
  dist/prompts/<name>.md                          paste into ChatGPT or any AI (references inlined)
  dist/catalog.json                               data for the ruzora.com/skills pages
"""
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = "ruzora-hiring"
REPO = "Ruzora/hiring-skills"
CATEGORIES = {
    "plan": ("hire-plan", "Decide what to hire, when, and what it really costs."),
    "attract": ("hire-attract", "Job posts and outreach that senior engineers answer."),
    "screen": ("hire-screen", "Screen CVs, profiles and candidates fast, and catch fake ones."),
    "interview": ("hire-interview", "Interview kits, take-homes, rubrics and debriefs that predict performance."),
    "close": ("hire-close", "References, offers and contracts, including international hires."),
    "onboard": ("hire-onboard", "Onboarding and the first 90 days, so the hire works out."),
}


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise SystemExit("missing frontmatter")
    data, key = {}, None
    for line in m.group(1).split("\n"):
        km = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", line)
        if km and not line.startswith(" "):
            key = km.group(1)
            data[key] = km.group(2).strip().strip("\"'")
        elif key and line.startswith(" "):
            sub = re.match(r"^\s+([\w-]+):\s?(.*)$", line)
            if sub and data[key] == "":
                data.setdefault(key + "." + sub.group(1), sub.group(2).strip().strip("\"'"))
            else:
                data[key] = (data[key] + " " + line.strip()).strip()
    return data, m.group(2)


def title_of(body, fallback):
    m = re.search(r"^# (.+)$", body, re.M)
    return m.group(1).strip() if m else fallback


STAGE_TITLES = {"plan": "Plan the hire", "attract": "Attract candidates", "screen": "Screen and verify",
                "interview": "Interview and assess", "close": "Close the hire", "onboard": "Onboard and review"}


def write_readme_catalog(catalog):
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    lines = []
    for cat, (plugin, desc) in CATEGORIES.items():
        rows = [c for c in catalog if c["category"] == cat]
        if not rows:
            continue
        lines.append(f"### {STAGE_TITLES[cat]} (`{plugin}`)\n\n{desc}\n")
        lines.append("| Skill | What you get | Guide |\n|---|---|---|")
        for c in rows:
            what = re.sub(r"\s*Use when.*$", "", c["description"]).strip()
            lines.append(f"| [{c['title']}](plugins/{cat}/skills/{c['name']}/SKILL.md) | {what} | [guide](site/{c['name']}/page.md) |")
        lines.append("")
    text = readme.read_text()
    block = "<!-- catalog:start -->\n" + "\n".join(lines) + "<!-- catalog:end -->"
    readme.write_text(re.sub(r"<!-- catalog:start -->.*?<!-- catalog:end -->", lambda m: block, text, flags=re.S))


def main():
    dist = ROOT / "dist"
    (dist / "zips").mkdir(parents=True, exist_ok=True)
    (dist / "prompts").mkdir(parents=True, exist_ok=True)
    catalog, plugins = [], []
    for cat, (plugin, desc) in CATEGORIES.items():
        skills_dir = ROOT / "plugins" / cat / "skills"
        if not skills_dir.exists():
            continue
        names = []
        for sk in sorted(skills_dir.glob("*/SKILL.md")):
            d = sk.parent
            fm, body = frontmatter(sk.read_text())
            name = fm["name"]
            assert name == d.name, f"{d}: name mismatch"
            names.append(name)
            title = title_of(body, name)
            # zip for Claude.ai
            with zipfile.ZipFile(dist / "zips" / f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
                for f in sorted(d.rglob("*")):
                    if f.is_file() and not f.name.startswith("."):
                        z.write(f, f"{name}/{f.relative_to(d).as_posix()}")
            # prompt for any AI
            parts = [
                f"# {title}\n",
                "Follow the instructions below for the rest of this conversation. "
                "Start by asking me for the inputs listed under Inputs (or use what I already gave you).\n",
                body.strip().replace(f"# {title}\n", "", 1),
            ]
            for ref in sorted((d / "references").glob("*.md")) if (d / "references").exists() else []:
                parts.append(f"\n\n## Reference: {ref.relative_to(d).as_posix()}\n\n" + ref.read_text().strip())
            (dist / "prompts" / f"{name}.md").write_text("\n".join(parts) + "\n")
            page = ROOT / "site" / name / "page.md"
            pfm = frontmatter(page.read_text())[0] if page.exists() else {}
            catalog.append({
                "name": name, "title": title, "category": cat, "plugin": plugin,
                "description": fm["description"],
                "page": {k: pfm.get(k) for k in ("title", "description", "target_query", "related_blog", "cta")},
                "install": {
                    "claude_code": f"/plugin marketplace add {REPO}\n/plugin install {plugin}@{MARKETPLACE}",
                    "zip": f"dist/zips/{name}.zip", "prompt": f"dist/prompts/{name}.md",
                },
            })
        if not names:
            continue
        man = {"name": plugin, "description": desc, "version": "1.0.0",
               "author": {"name": "Ruzora", "url": "https://www.ruzora.com"},
               "homepage": "https://www.ruzora.com/skills",
               "repository": f"https://github.com/{REPO}", "license": "CC-BY-4.0",
               "keywords": ["hiring", "recruiting", "engineering", cat]}
        p = ROOT / "plugins" / cat / ".claude-plugin"
        p.mkdir(parents=True, exist_ok=True)
        (p / "plugin.json").write_text(json.dumps(man, indent=2) + "\n")
        plugins.append({"name": plugin, "source": f"./plugins/{cat}", "description": desc,
                        "version": "1.0.0", "category": "productivity",
                        "author": {"name": "Ruzora", "url": "https://www.ruzora.com"},
                        "homepage": "https://www.ruzora.com/skills", "repository": f"https://github.com/{REPO}",
                        "tags": ["hiring", "recruiting", cat], "skills": names})
    mk = {"name": MARKETPLACE,
          "owner": {"name": "Ruzora", "url": "https://www.ruzora.com"},
          "description": "Free skills for hiring software engineers: plan, attract, screen, interview, close, onboard.",
          "plugins": [{k: v for k, v in pl.items() if k != "skills"} for pl in plugins]}
    (ROOT / ".claude-plugin").mkdir(exist_ok=True)
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(json.dumps(mk, indent=2) + "\n")
    (dist / "catalog.json").write_text(json.dumps(catalog, indent=2) + "\n")
    write_readme_catalog(catalog)
    print(f"built {len(catalog)} skills in {len(plugins)} plugins")
    for pl in plugins:
        print(f"  {pl['name']}: {', '.join(pl['skills'])}")


if __name__ == "__main__":
    main()
