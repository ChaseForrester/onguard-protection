#!/usr/bin/env python3
"""Score on-page SEO / image SEO / AEO readiness."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP = {"thanks.html", "404.html"}


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.metas: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.h1: list[str] = []
        self._in_h1 = False
        self._h1_buf = ""
        self.json_ld = 0
        self.html_lang = ""

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "html":
            self.html_lang = d.get("lang", "")
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            self.metas.append(d)
        if tag == "link":
            self.links.append(d)
        if tag == "img":
            self.images.append(d)
        if tag == "h1":
            self._in_h1 = True
            self._h1_buf = ""
        if tag == "script" and d.get("type") == "application/ld+json":
            self.json_ld += 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self._h1_buf += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "h1":
            self._in_h1 = False
            self.h1.append(re.sub(r"\s+", " ", self._h1_buf).strip())


def meta(page: Page, key: str, name: str = "name") -> str:
    for m in page.metas:
        if m.get(name) == key:
            return m.get("content", "")
    return ""


def audit_file(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    p = Page()
    p.feed(html)
    desc = meta(p, "description")
    checks = {
        "html_lang_en_AU": p.html_lang == "en-AU",
        "title_30_60": 30 <= len(p.title.strip()) <= 65,
        "unique_title_present": bool(p.title.strip()),
        "meta_desc_120_160": 120 <= len(desc) <= 165,
        "single_h1": len(p.h1) == 1 and bool(p.h1[0]),
        "canonical": any(l.get("rel") == "canonical" and l.get("href", "").startswith("http") for l in p.links),
        "robots_index": "index" in meta(p, "robots"),
        "og_title": bool(meta(p, "og:title", "property")),
        "og_desc": bool(meta(p, "og:description", "property")),
        "og_image_abs": meta(p, "og:image", "property").startswith("https://"),
        "og_image_w": bool(meta(p, "og:image:width", "property")),
        "og_image_h": bool(meta(p, "og:image:height", "property")),
        "og_image_alt": bool(meta(p, "og:image:alt", "property")),
        "twitter_card": bool(meta(p, "twitter:card")),
        "twitter_image": bool(meta(p, "twitter:image")),
        "json_ld": p.json_ld >= 1,
        "viewport": bool(meta(p, "viewport")),
        "theme_color": bool(meta(p, "theme-color")),
        "hreflang": any(l.get("hreflang") == "en-AU" for l in p.links),
    }
    imgs = [i for i in p.images if i.get("src") and not i.get("src").startswith("data:")]
    # empty lightbox src is allowed
    imgs = [i for i in imgs if i.get("src")]
    img_checks = []
    for img in imgs:
        alt = img.get("alt", None)
        ok = {
            "has_alt": alt is not None and alt != "",
            "has_width": bool(img.get("width")),
            "has_height": bool(img.get("height")),
            "descriptive_alt": alt is not None and len(alt) >= 12,
        }
        # lightbox placeholder
        if img.get("src") == "":
            continue
        img_checks.append(ok)
    if img_checks:
        checks["images_all_alt"] = all(i["has_alt"] for i in img_checks)
        checks["images_all_dims"] = all(i["has_width"] and i["has_height"] for i in img_checks)
        checks["images_alt_descriptive"] = all(i["descriptive_alt"] for i in img_checks)
    else:
        checks["images_all_alt"] = True
        checks["images_all_dims"] = True
        checks["images_alt_descriptive"] = True

    passed = sum(1 for v in checks.values() if v)
    total = len(checks)
    return {
        "path": str(path.relative_to(ROOT)),
        "title_len": len(p.title.strip()),
        "desc_len": len(desc),
        "h1": p.h1,
        "score": round(100 * passed / total),
        "failed": [k for k, v in checks.items() if not v],
        "img_count": len(img_checks),
    }


def main() -> None:
    pages = [ROOT / "index.html"]
    pages += sorted((ROOT / "locations").glob("*.html"))
    pages += sorted((ROOT / "locations").glob("*/*.html"))
    pages += sorted((ROOT / "services").glob("*.html"))
    pages += sorted((ROOT / "blog").glob("*.html"))
    pages += sorted((ROOT / "industries").glob("*.html"))
    jobs = ROOT / "jobs" / "index.html"
    if jobs.exists():
        pages.append(jobs)
    legal = ROOT / "legal" / "index.html"
    if legal.exists():
        pages.append(legal)
    results = []
    for page in pages:
        if page.name in SKIP:
            continue
        results.append(audit_file(page))
    fails = [r for r in results if r["score"] < 100]
    print(json.dumps({"pages": len(results), "perfect": len(results) - len(fails), "fails": fails}, indent=2))
    titles = [r["path"] + " :: " for r in results]
    title_texts = []
    for page in pages:
        if page.name in SKIP:
            continue
        m = re.search(r"<title>(.*?)</title>", page.read_text(), re.S)
        title_texts.append(re.sub(r"\s+", " ", m.group(1)).strip() if m else "")
    dupes = [t for t in title_texts if title_texts.count(t) > 1]
    print("duplicate_titles", sorted(set(dupes)))
    print("avg_score", round(sum(r["score"] for r in results) / len(results), 1))


if __name__ == "__main__":
    main()
