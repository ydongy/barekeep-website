# 0003 One address per page: no redirects, no aliases

- Status: accepted
- Date: 2026-10-03
- Related: [0004](0004-csp-in-headers-file.md)

## Context

The app, the release script and the legal text link to the site by path. Aliases and redirects (a `/buy` that forwards to the pricing section, an `/eula` for the license) double the number of addresses to keep valid and make it unclear which one the app should use.

## Decision

Every page has exactly one address per language: `/`, `/faq`, `/changelog`, `/privacy`, `/terms`, `/refund`, with the language prefix for the other eight languages. Download and pricing are sections of the home page (`/#download`, `/#pricing`). There is no `_redirects` file and no alias page; `scripts/check_facts.py` fails if one appears. The first visit may switch language in the browser (`lang.js`), which is not a server redirect.

## Cost

A path that was published and later changes breaks old links, so the paths the app uses are treated as a contract. A page that moves needs a new decision.

## Revisit triggers

None.
