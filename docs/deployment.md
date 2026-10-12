# Deployment

Cloudflare's Git integration (Workers & Pages, project `barekeep`) deploys `main` with the deploy command
`npx wrangler deploy` and an empty build command; there is no deploy-time build, so the generated `public/` is
committed. `wrangler.jsonc` points at `public/`. The custom domain `barekeep.com` is bound in the dashboard
(project > Domains), not in the config. `workers_dev` and `preview_urls` are off on purpose. Response headers,
including the Content-Security-Policy, are in `public/_headers`.

