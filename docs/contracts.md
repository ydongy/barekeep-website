# BareKeep website contracts

What other systems rely on in this site: the shape of `changelog.json`, the addresses the app links to, and the
download feed. Commit scopes used in Conventional Commits are listed first.

## Commit scopes

`i18n` (copy and translations) · `build` (generator settings, vendored sitekit) · `style` (`public/style.css`) ·
`facts` (`scripts/check_facts.py`) · `changelog` · `adr`.

## Contracts

### Changelog entries

`changelog.json` is a list of releases, newest first. Each release has `version`, `date`, `title` and `items` (a list of
strings) per language code, and optionally `summary`; a language without an entry shows the English text. The
app's release flow writes the file; do not edit it by hand.

### Download feed

`public/download.js` reads `https://dl.barekeep.com/latest.json` (`version`, `url`, `sha256`, `minimumOS`) and
the button wording comes from `download_js` in the i18n files. The feed is written by the app's release script.
