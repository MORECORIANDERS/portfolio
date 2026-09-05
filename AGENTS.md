# AGENTS.md — Portfolio (Astro 5)

## Commands

```bash
npm install          # install deps
npm run dev          # dev server at http://localhost:4321/portfolio/
npm run build        # production build → dist/
npm run check        # Astro typecheck (no separate lint/test)
```

No linter or test suite. The only verification is `npm run check`.

## Architecture

- **Astro 5** static site, deployed to **GitHub Pages**.
- Projects are Markdown files in `src/content/projects/`, managed as an Astro Content Collection.
- Schema defined in `src/content.config.ts` (Zod). Fields like `cover`, `coverAlt` are required.
- Dynamic route: `src/pages/projects/[slug].astro` renders each project.
- Personal info and navigation are centralized in `src/consts.ts`.
- Styles use CSS custom properties with light/dark themes in `src/styles/global.css`.

## Key Gotchas

- **`base` path**: The site is deployed under `/portfolio/` (set in `astro.config.mjs`). All internal asset paths must work with this prefix. Don't hardcode absolute paths without considering this.
- **`npm run check`** is the only type-check. Run it before committing any TypeScript or Astro component changes.
- **No `site` in astro.config**: Only `trailingSlash` and `build.format` are configured. The `base` path is not set in config (it defaults to `/`). The README references `base` but the actual config doesn't have it — the dev server auto-adds the project folder name. Be careful with path assumptions.
- **Frontmatter validation**: Wrong field types or missing required fields (`title`, `description`, `pubDate`, `cover`, `coverAlt`) will fail at build time, not dev time.
- **Deploy triggers on push to `main`**: CI runs `npm ci` then `npx astro build`. No caching beyond npm's built-in cache.

## Content Model

Each project `.md` file needs these required frontmatter fields:
`title`, `description`, `pubDate`, `cover`, `coverAlt`

Optional: `role`, `tags`, `stack`, `demoUrl`, `repoUrl`, `featured`, `order`, `updatedDate`

Cover images live in `public/projects/<slug>/` and are referenced via the `cover` field.

## File Map

| Purpose | File |
|---------|------|
| Site config | `astro.config.mjs` |
| Global info (name, nav, stack) | `src/consts.ts` |
| Content schema | `src/content.config.ts` |
| Styles / theme tokens | `src/styles/global.css` |
| Base layout (head, theme script) | `src/layouts/BaseLayout.astro` |
| Project detail page | `src/pages/projects/[slug].astro` |
| CI/CD | `.github/workflows/deploy.yml` |
