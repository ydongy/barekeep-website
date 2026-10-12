# BareKeep website

[![CI](https://github.com/ydongy/barekeep-website/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/barekeep-website/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Static website of BareKeep (`https://barekeep.com`), nine languages, deployed as Cloudflare Workers static assets
from `public/`.

## Quick start

Python 3 only (standard library); no install step.

```
git clone https://github.com/ydongy/barekeep-website.git
cd barekeep-website
python3 scripts/sitekit/preview.py      # preview at http://localhost:8765/
```

## Deploy

Cloudflare's Git integration (Workers & Pages, project `barekeep`) deploys `main` with the deploy command
`npx wrangler deploy` and an empty build command; there is no deploy-time build, so the generated `public/` is
committed. `wrangler.jsonc` points at `public/`. The custom domain `barekeep.com` is bound in the dashboard
(project > Domains), not in the config. `workers_dev` and `preview_urls` are off on purpose. Response headers,
including the Content-Security-Policy, are in `public/_headers`.

## Development

Edit `i18n/*.json`, `changelog.json`, `public/style.css` or `scripts/build.py`; never the generated HTML or
`public/lang.js`. Then run, in this order (CI runs the same):

```
python3 scripts/sitekit/check_i18n.py   # every language matches English: structure, tags, links, placeholders
python3 scripts/build.py                # regenerate public/
git diff --exit-code public/            # after committing: the committed output matches the sources
python3 scripts/sitekit/check_site.py   # pages, links, anchors, Content-Security-Policy
python3 scripts/check_facts.py          # the Facts table in docs/content.md against every language
```

Commit the generated files together with the source change that produces them. Preview:
`python3 scripts/sitekit/preview.py` serves `public/` the way Cloudflare does (extensionless URLs open); a browser
that prefers another supported language is redirected on its first visit, and picking a language in the menu is
remembered. `npx wrangler dev` also works. The generator is ydongy's sitekit, vendored in
`scripts/sitekit/` (commit in `scripts/sitekit/VERSION`); update it with sitekit's `vendor.sh`, never by editing
the copy ([0005](docs/adr/0005-sitekit-vendored.md)). Page layout and design: [docs/design.md](docs/design.md);
contracts with the app: [docs/contracts.md](docs/contracts.md); agent guide: [AGENTS.md](AGENTS.md).

## Pages

| Page | Address | Copy source |
|---|---|---|
| Home (with the download and pricing sections) | `/`, `/#download`, `/#pricing` | `home` in `i18n/<code>.json`; built by `scripts/build.py` |
| FAQ | `/faq` | `faq` |
| Changelog | `/changelog` | `changelog.json` |
| Privacy Policy | `/privacy` | `privacy` |
| Terms of Service | `/terms` | `terms` |
| Refund Policy | `/refund` | `refund` |
| Not found | `/404` (served for unknown paths) | built by sitekit |

Other languages add their prefix (`/zh/faq`, `/zh-hant/terms`, and so on). Every page has exactly one address:
no redirects, no aliases ([0003](docs/adr/0003-one-address-per-page.md)). Details in [docs/content.md](docs/content.md).

## Languages

English, Chinese (simplified, traditional), Japanese, Korean, French, German, Spanish, Portuguese; English is the
reference. To add a language (open an issue first): add it to `i18n/languages.json`, translate `i18n/en.json` into
`i18n/<code>.json` with the same JSON formatting, rebuild and run the five commands.

## Content sources

- Legal and product facts: the product's own facts list (not published). The Facts table in
  [docs/content.md](docs/content.md) mirrors the numbers and `scripts/check_facts.py` checks them.
- Terms of Service: the text of the app's license, translated. Privacy Policy and Refund Policy are
  written here and checked against the app's facts.
- `changelog.json`: written by BareKeep's release tooling, not by hand; keep its path and format
  ([docs/contracts.md](docs/contracts.md)).
- Home and FAQ copy: written here, using the app's own names for menus and buttons.
- Icon and share image: composed from the app's icon layers.

## App dependencies

The app links to `/`, `/privacy`, `/terms`, `/refund`, `/changelog` and `/#pricing`, and the release script writes
`https://dl.barekeep.com/latest.json`, which `public/download.js` reads for the download button (version, SHA-256,
minimum system). These paths and the feed format are stable. If the feed address
changes, change `connect-src` in `public/_headers` too.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md): copy lives in `i18n/*.json`; after editing run `python3 scripts/build.py` and
commit the regenerated `public/` with the change.

## License

The source code in this repository is released under the [MIT License](LICENSE).

The BareKeep name, logo and icon, and the website copy (text and translations), are copyright (c) 2026 ydongy and are not covered by the MIT License. BareKeep is a closed-source product (only this website is open); the name and icon may not be used to suggest endorsement or to name a derived work. 品牌名称、Logo、图标与网站文案版权归 ydongy 所有，不在 MIT 授权范围内。
