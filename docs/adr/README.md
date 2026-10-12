# Architecture Decision Records

Each record covers one decision: context, decision, cost. A reversed decision keeps its file: write a new
record and mark the old one "superseded by NNNN".

## Index

| No. | Decision | Status |
|---|---|---|
| [0001](0001-no-framework-python-standard-library.md) | No framework: pages are generated with the Python standard library only | accepted |
| [0002](0002-no-analytics-no-cookies.md) | No analytics, no cookies, no third-party scripts | accepted |
| [0003](0003-one-address-per-page.md) | One address per page: no redirects, no aliases | accepted |
| [0004](0004-csp-in-headers-file.md) | The Content-Security-Policy is set in public/_headers | accepted |
| [0005](0005-sitekit-vendored.md) | The generator is sitekit, vendored into the repository | accepted |
| [0006](0006-cloudflare-workers-static-assets.md) | Deploy as Cloudflare Workers static assets from the committed public/ | accepted |

## Record format

Title, then Status, Date and Related, then Context, Decision and Cost. Copy the newest record as a starting point.
