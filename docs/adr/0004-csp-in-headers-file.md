<!-- template: adr.md v1 -->
# 0004 The Content-Security-Policy is set in public/_headers

- Status: accepted
- Date: 2026-10-03
- Related: [0002](0002-no-analytics-no-cookies.md)

## Context

The site must keep its promise of no tracking and no external resources, and it should not depend on reviewers noticing a stray script tag.

## Decision

`public/_headers` sets `Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self'; img-src 'self'; connect-src https://dl.barekeep.com`, `X-Content-Type-Options: nosniff` and `Referrer-Policy: no-referrer`. Styles are never inline and nothing external is loaded; the one `connect-src` host is the release feed. `scripts/sitekit/check_site.py` reads the policy and fails the build on a page that violates it.

## Cost

Inline scripts are allowed because the generated pages carry small ones; every new inline script widens the policy's reach. Moving the feed to another host means changing this file too.

## Revisit triggers

The feed moves to another host, or the pages stop needing inline scripts (then drop `'unsafe-inline'`).
