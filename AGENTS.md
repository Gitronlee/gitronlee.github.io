# AGENTS.md

## Project Overview

Astro 5 static site — developer toolbox (tools, games, docs). Chinese language UI. Deploys to GitHub Pages via `deploy.yml` on push to `main`.

## Commands

- `npm run dev` — local dev server
- `npm run build` — static output to `dist/`
- `npm run check` — Astro type check (no test suite exists)
- No linter or formatter configured

## Architecture

- **Data-driven routes**: `src/data/tools.json` and `src/data/games.json` define all items
- **Critical: manual registration required** — adding a tool to `tools.json` is NOT enough. You must also:
  1. Create `src/components/tools/<ToolName>.astro`
  2. Add a `toolMap` entry in `src/pages/tools/[slug].astro` (line ~15-27) mapping slug to component
- Games follow the same pattern: `games.json` + `src/components/games/` + `src/pages/games/[slug].astro`
  - Games have a `status` field: `"active"` renders the component, `"coming-soon"` shows placeholder UI
  - Only `word-tetris` is active; others show "Coming Soon" fallback automatically
- **Word Tetris structure**: 9 grades (一年级~初三) × 7 sub-levels = 63 levels, 50 words each = 3150 words
  - Files: `src/data/word-tetris/grade-{grade}-{sub}.json` (e.g., `grade-1-1.json`, `grade-9-7.json`)
  - Level format: `{grade}-{sub}` (e.g., "1-1", "3-5", "9-7")
  - Auto-advance: sub 1→7, then grade+1 sub 1
- **Tool component convention**: Tools wrap content in `<ToolLayout>` (import from `@/components/ToolLayout.astro`)
- **Docs use Astro content collections**: Schema defined in `src/content.config.ts` (title, description, category, optional order)

## Path Aliases

`@/*` maps to `src/*` (configured in `tsconfig.json`)

## Theming

- Light/dark theme via `data-theme` attribute on `<html>`, toggled in `BaseLayout.astro` inline script
- All colors use CSS custom properties defined in `src/styles/global.css` (`--bg-primary`, `--text-primary`, `--accent-blue`, etc.)
- Theme preference persisted to `localStorage`

## Adding Docs

Create `.md` files in `src/content/docs/` with required frontmatter: `title`, `description`, `category`, optional `order`. Docs are rendered via `src/pages/docs/[...slug].astro` and grouped by category on the index page.

## Key Gotchas

- Build output is `dist/` (gitignored) — do not edit it directly
- No test framework — `npm run check` is the only verification command
- CI requires Node 22 (see `.github/workflows/deploy.yml`)
- `site` and `base` in `astro.config.mjs` must match your deployment target
- Tools that need client-side interactivity use `<script>` tags inside `.astro` components (no framework runtime)
