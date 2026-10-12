# 0002 No analytics, no cookies, no third-party scripts

- Status: accepted
- Date: 2026-10-03
- Related: [0004](0004-csp-in-headers-file.md)

## Context

BareKeep's promise is that it collects nothing about its users: no telemetry, no crash reports, no accounts. The Privacy Policy states it, and a website that tracks visitors would contradict it.

## Decision

The site sets no cookies, runs no analytics and loads no third-party script, font or image. The only script that talks to the network is `public/download.js`, which reads the release feed at `dl.barekeep.com`. The only thing remembered in the browser is the chosen language, in `localStorage`. The Content-Security-Policy enforces this.

## Cost

There are no visitor statistics, no campaign attribution and no embedded widgets (video, chat, payment forms); the purchase happens on the payment provider's own page.

## Revisit triggers

The privacy promise changes, or a purchase flow needs an embedded component; either needs a new decision and a Privacy Policy change first.
