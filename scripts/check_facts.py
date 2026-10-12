#!/usr/bin/env python3
"""Check that the policy facts agree everywhere, in every language.

    python3 scripts/check_facts.py

- The "Facts" table in docs/content.md (fact, value, where stated) is the expected set. Each key it lists must
  state the table's numbers, in every language, and exactly the same numbers as the English text.
- A number from the table that appears in a policy page, the FAQ or the home page at a place the table does not
  list is a problem: add the place to the table or change the copy.
- The agreement, the privacy policy and the refund policy each have one name per language (footer label = page
  title = meta title).
- Every language except English carries the translation notice (English is the reference text); English has none.
- The footer of every generated page links the Privacy Policy, the Terms of Service, the Refund Policy and the contact address.
- There is no `_redirects` file and no `/eula` page: every page has exactly one address.
Run it after editing i18n/*.json or docs/content.md. When an app fact changes, the app's legal facts document and the
Facts table in docs/content.md change together.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAG = re.compile(r"<[^>]+>")
NUMBER = re.compile(r"\d+\.\d+|(?<!\d)\d+(?!\d)")
CONTACT = "support@barekeep.com"
SCOPES = ("terms", "refund", "privacy", "faq", "home", "meta")  # where fact numbers are looked for


def strings(o, path=""):
    """Yield (key path, text) for every string in a language file."""
    if isinstance(o, dict):
        for k, v in o.items():
            yield from strings(v, f"{path}.{k}" if path else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from strings(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o


def numbers(text):
    return set(NUMBER.findall(TAG.sub(" ", text.replace("&nbsp;", " "))))


def fact_table():
    """Rows of the Facts table in docs/content.md: (fact, numbers, [keys])."""
    text = (ROOT / "docs/content.md").read_text(encoding="utf-8")
    section = re.search(r"^## Facts\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    rows = []
    for line in (section.group(1) if section else "").split("\n"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and line.startswith("|") and not set(cells[0]) <= {"-", " ", "Fact"} and cells[0] != "Fact":
            rows.append((cells[0], numbers(cells[1]), re.findall(r"`([^`]+)`", cells[2])))
    return rows


def main():
    errors = []
    rows = fact_table()
    if not rows:
        print("- docs/content.md has no Facts table")
        return 1
    langs = json.loads((ROOT / "i18n/languages.json").read_text(encoding="utf-8"))
    codes = [l["code"] for l in langs]
    data = {c: json.loads((ROOT / f"i18n/{c}.json").read_text(encoding="utf-8")) for c in codes}
    texts = {c: dict(strings(data[c])) for c in codes}
    table_numbers = set().union(*(n for _, n, _ in rows))
    listed = {}  # key -> numbers the table says it states
    for fact, nums, keys in rows:
        for key in keys:
            listed.setdefault(key, set()).update(nums)
    en = texts["en"]
    for key, expected in sorted(listed.items()):
        if key not in en:
            errors.append(f"docs/content.md: key '{key}' does not exist in i18n/en.json")
            continue
        for c in codes:
            found = numbers(texts[c].get(key, "")) & table_numbers
            if found != expected:
                errors.append(f"{c}: '{key}' states {sorted(found)}, the Facts table says {sorted(expected)}")
    for key, text in sorted(en.items()):
        if key not in listed and key.split(".")[0].split("[")[0] in SCOPES:
            extra = numbers(text) & table_numbers
            if extra:
                errors.append(f"en: '{key}' contains {sorted(extra)} but is not listed in the Facts table")
    for c in codes:
        d = data[c]
        for key in ("terms", "privacy", "refund"):
            if not (d["nav"][key] == d[key]["h1"] and d["nav"][key] in d["meta"][f"{key}_title"]):
                errors.append(f"{c}: '{key}' has more than one name (nav / h1 / meta title)")
            has_note = bool(d[key].get("note"))
            if (c == "en") == has_note:
                errors.append(f"{c}: '{key}' translation notice is {'missing' if c != 'en' else 'present on the English reference'}")
    for c in codes:
        base = ROOT / "public" / ("" if c == "en" else c)
        prefix = "" if c == "en" else f"/{c}"
        for page in ("index", "faq", "privacy", "terms", "refund", "changelog"):
            f = base / f"{page}.html"
            if not f.is_file():
                errors.append(f"{f.relative_to(ROOT)}: missing (run build.py)")
                continue
            html = f.read_text(encoding="utf-8")
            for path in ("/privacy", "/terms", "/refund"):
                if f'href="{prefix}{path}"' not in html:
                    errors.append(f"{f.relative_to(ROOT)}: footer does not link {prefix}{path}")
            if f"mailto:{CONTACT}" not in html:
                errors.append(f"{f.relative_to(ROOT)}: no contact address")
        for stale in ("eula.html",):
            if (base / stale).exists():
                errors.append(f"{(base / stale).relative_to(ROOT)}: must not exist")
    if (ROOT / "public/_redirects").exists():
        errors.append("public/_redirects must not exist: every page has one address, no aliases")
    for e in errors:
        print("-", e)
    print("facts: ok" if not errors else f"facts: {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
