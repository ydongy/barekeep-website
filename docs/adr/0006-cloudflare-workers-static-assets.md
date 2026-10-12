<!-- template: adr.md v1 -->
# 0006 Deploy as Cloudflare Workers static assets from the committed public/

- Status: accepted
- Date: 2026-10-03
- Related: [0001](0001-no-framework-python-standard-library.md)

## Context

The site is static and the release feed already lives on Cloudflare R2. The team wants a deploy that cannot fail on a build step and a preview of exactly what is committed.

## Decision

Cloudflare's Git integration deploys `main` as Workers static assets (`wrangler.jsonc`: directory `./public`, `html_handling` auto-trailing-slash, `not_found_handling` 404-page) with the deploy command `npx wrangler deploy` and an empty build command. The generated `public/` is committed and CI checks that it matches the sources. The custom domain is bound in the dashboard; `workers_dev` and `preview_urls` are off so that the site has one origin. After a repository transfer the Git connection must be authorized again in the dashboard.

## Cost

The generated files are in the history and every copy change is a larger diff. The domain binding and the Git connection live outside the repository, so they are described in the README rather than enforced.

## Revisit triggers

Cloudflare changes how Workers static assets are deployed, or the site needs server-side behavior.
