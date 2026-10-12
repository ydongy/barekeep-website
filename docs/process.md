<!-- template: process.md v1 -->
# BareKeep website development process

The process is the ydongy handbook (`https://github.com/ydongy/.github/tree/6b48552c969c28a954498123bb502a556f8eed79/handbook`).
This file lists only what is specific to the BareKeep website.

## Commit scopes and labels

`i18n` (copy and translations) · `build` (generator settings, vendored sitekit) · `style` (`public/style.css`) ·
`facts` (`scripts/check_facts.py`) · `changelog` · `adr`. Shared type and status labels come from the
ydongy/.github repository (`labels.yml`).

## Contracts

### Changelog entries

`changelog.json` is a list of releases, newest first. Each release has `version`, `date`, `title` and `items` (a list of
strings) per language code, and optionally `summary`; a language without an entry shows the English text. The
app's release flow writes the file; do not edit it by hand.

### Download feed

`public/download.js` reads `https://dl.barekeep.com/latest.json` (`version`, `url`, `sha256`, `minimumOS`) and
the button wording comes from `download_js` in the i18n files. The feed is written by the app's release script.

## CI

The docs workflow and handbook link pin the same ydongy/.github revision. Upgrade both explicitly;
changes to the shared handbook on main do not alter this repository's checks.

`.github/workflows/ci.yml` calls the shared `site-ci.yml` (i18n check, build, `git diff --exit-code public/`,
site check, facts check). `.github/workflows/docs.yml` calls the shared `docs-check.yml`, which runs
`scripts/check-docs.py` from the ydongy/.github repository; `.docs-check.json` holds the per-repository options.

## History

The site was first built with its own page and check scripts and moved to ydongy's sitekit
([0005](adr/0005-sitekit-vendored.md)). Its documentation was rewritten from the ydongy templates on
2026-10-03; earlier design notes were folded into [design.md](design.md) and
[milestones/v1.0.md](milestones/v1.0.md).
