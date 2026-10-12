<!-- template: adr.md v1 -->
# 0005 The generator is sitekit, vendored into the repository

- Status: accepted
- Date: 2026-10-03
- Related: [0001](0001-no-framework-python-standard-library.md)

## Context

ydongy's product sites share their structure: head tags, header and footer, FAQ, legal pages, changelog, language handling, sitemap, and the checks for languages, links and the policy. Keeping a private copy of that code in each site drifts apart.

## Decision

The shared generator and checks are ydongy's `sitekit` repository. This repository holds a copy in `scripts/sitekit/` made by sitekit's `vendor.sh`, with the sitekit commit in `scripts/sitekit/VERSION`. It is never edited here; a change it needs is made in sitekit and re-vendored in its own pull request, and `public/` is rebuilt with it. What stays local: `scripts/build.py` (site settings, home page), `scripts/check_facts.py`, the copy, the stylesheet and the assets.

## Cost

A sitekit change that alters output touches every site, and a site cannot patch the generator for its own needs; a missing hook is added in sitekit first.

## Revisit triggers

None.
