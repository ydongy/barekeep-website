#!/usr/bin/env python3
"""Build the BareKeep website pages from i18n/*.json and changelog.json.

Run from the repo root after changing copy, languages or the changelog: python3 scripts/build.py

Shared structure (head, header, footer, FAQ, legal pages, changelog, 404, sitemap, lang.js) lives in
scripts/sitekit (vendored from ydongy's sitekit repository, see scripts/sitekit/VERSION).
This file holds what is specific to BareKeep: the site settings and the home page.
- i18n/languages.json lists the languages: URL path, HTML lang and the browser language prefixes that
  redirect to it. A language is built only if i18n/<code>.json exists.
- i18n/<code>.json holds the copy. Strings may contain HTML; "{{root}}" in links becomes the
  language's path prefix.
- Every page has exactly one address: there is no _redirects file. The output is committed; the site
  itself has no build step.
"""
from pathlib import Path

from sitekit import Page, Site, attr, build

ROOT = Path(__file__).resolve().parent.parent
SITE = Site(
    root=ROOT,
    url="https://barekeep.com",
    name="BareKeep",
    contact="support@barekeep.com",
    theme=(("#fbfaf7", "light"), ("#0e1220", "dark")),
    og_image=("/og.png", 1200, 630),
)

ICON = {
    "source": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><circle cx="4.5" cy="3.5" r="1.6"/><circle cx="4.5" cy="12.5" r="1.6"/><circle cx="11.5" cy="6.5" r="1.6"/><path d="M 4.5 5.1v5.8M11.5 8.1c0 2.4-2.4 2.6-7 2.9"/></svg>',
    "mac": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><rect x="3" y="3.5" width="10" height="7" rx="1.3"/><path d="M 1.5 12.5h13"/></svg>',
    "backup": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><rect x="2.5" y="2.5" width="11" height="4.5" rx="1.2"/><rect x="2.5" y="9" width="11" height="4.5" rx="1.2"/><path d="M 5 4.75h.01M5 11.25h.01"/></svg>',
}
ROUTE_ICONS = ["source", "mac", "backup"]



class BareKeepPage(Page):
    def home(self):
        t, h = self.t, self.t["home"]
        js = t["download_js"]
        card_rows = "".join(f'<div><dt>{r["label"]}</dt><dd>{r["value"]}</dd></div>' for r in h["card_rows"])
        own = "".join(f'<li><h3>{x["title"]}</h3><p>{x["text"]}</p></li>' for x in h["own"])
        route = "".join(
            f'<li class="{"held" if i == 2 else ""}"><span class="ico">{ICON[ROUTE_ICONS[i]]}</span><b>{x["name"]}</b><span>{x["detail"]}</span></li>'
            for i, x in enumerate(h["route"]))
        lamps = "".join(f'<li><h3><span class="lamp {c}"></span>{x["title"]}</h3><p>{x["text"]}</p></li>'
                        for c, x in zip(["on", "busy", "warn", "error", "off"], h["lamps"]))
        platforms = "".join(f"<li>{x}</li>" for x in h["platforms"])
        steps = "".join(f'<li><h3>{x["title"]}</h3><p>{x["text"]}</p></li>' for x in h["steps"])
        body = f'''{self.header("index")}
<main id="main">
<section class="hero wrap">
<div>
<p class="kicker">{h["kicker"]}</p>
<h1>{h["h1"]}</h1>
<p class="lead">{h["lead"]}</p>
<a class="button" href="#download">{h["cta"]}</a>
<p class="meta">{h["meta"]}</p>
</div>
<div class="card" role="img" aria-label="{attr(h["card_label_aria"])}">
<div class="card-head"><span>{h["card_label"]}</span><span class="stamp"><span class="lamp on breathe"></span>{h["synced"]}</span></div>
<p class="card-title">owner/repo</p>
<dl>{card_rows}</dl>
</div>
</section>

<section class="section wrap" id="own">
<h2>{h["own_h"]}</h2>
<ul class="ledger">{own}</ul>
</section>

<section class="section wrap diagnose" id="diverge">
<div>
<h2>{h["diverge_h"]}</h2>
<p class="lead">{h["diverge_lead"]}</p>
</div>
<div>
<ol class="route" aria-label="{attr(h["route_label"])}">{route}</ol>
<div class="message"><span class="lamp warn" aria-hidden="true"></span><p><b>{h["msg_title"]}</b><span>{h["msg"]}</span></p></div>
</div>
</section>

<section class="section wrap" id="lamps">
<h2>{h["lamps_h"]}</h2>
<p class="lead">{h["lamps_lead"]}</p>
<ul class="ledger">{lamps}</ul>
</section>

<section class="section wrap" id="platforms">
<h2>{h["platforms_h"]}</h2>
<p class="lead">{h["platforms_lead"]}</p>
<ul class="platforms">{platforms}</ul>
</section>

<section class="section wrap" id="how">
<h2>{h["steps_h"]}</h2>
<ol class="ledger">{steps}</ol>
</section>

<div class="wrap acquire">
<section class="section download" id="download" data-version="{attr(js["version"])}" data-version-no-os="{attr(js["version_no_os"])}" data-button="{attr(js["button"])}" data-error="{attr(js["error"])}">
<h2>{h["download_h"]}</h2>
<p class="lead">{h["download_lead"]}</p>
<p class="status" id="status">{h["status_default"]}</p>
<div class="actions">
<a class="button" id="download-button" href="#" hidden>{h["download_button"]}</a>
</div>
<noscript><p class="note">{h["noscript"]}</p></noscript>
<p class="checksum" id="checksum" hidden><span id="sha"></span><br>{h["checksum_hint"]}</p>
<p class="install">{self.root(h["install"])}</p>
</section>

<section class="section pricing" id="pricing">
<h2>{h["pricing_h"]}</h2>
<p class="lead">{self.root(h["pricing_lead"])}</p>
<p class="terms">{self.root(h["terms"])}</p>
</section>
</div>
</main>
'''
        return self.head("index", t["meta"]["home_title"], t["meta"]["home_desc"], '\n<script src="/download.js" defer></script>') + body + self.footer("index")



if __name__ == "__main__":
    build(SITE, BareKeepPage)
