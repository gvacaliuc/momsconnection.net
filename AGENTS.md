# Repository Guidelines

## Project Structure & Module Organization
- `content/` holds site pages, blog posts, and sections with Hugo front matter.
- `layouts/` contains site templates and partials that override theme defaults.
- `themes/terrassa/` is the Hugo theme (git submodule).
- `assets/` is for pipeline assets (e.g., `assets/css/custom.css`).
- `static/` hosts files copied directly to the site root (images, downloads).
- `public/` is the Hugo build output (generated; do not edit by hand).

## Build, Test, and Development Commands
- `git submodule update --init` initializes the theme submodule (run once or after cloning).
- `hugo serve` runs the local dev server with live reload at `http://localhost:1313`.
- `hugo` builds the production site into `public/`.

Note: this project requires Hugo `v0.119.0` or earlier.

## Coding Style & Naming Conventions
- Content files use Hugo front matter in Markdown; keep keys lower-case and consistent.
- Use descriptive slugs in `content/` paths (e.g., `content/posts/summer-events.md`).
- Prefer existing layout patterns in `layouts/` and theme structure in `themes/terrassa/`.
- No dedicated formatter or linter is configured; keep diffs minimal and readable.

## Testing Guidelines
- No automated test suite is configured for this repository.
- Validate changes by running `hugo serve` and checking the affected pages locally.

## Commit & Pull Request Guidelines
- Recent history uses short, imperative commit messages (e.g., “add designs folder”).
- Keep commits focused on one change set; avoid mixing content and layout edits.
- PRs should include a brief description of the change and any relevant screenshots
  for layout or style updates.

## Configuration & Content Tips
- Site settings live in `config.toml` (menus, params, theme config).
- New pages: `hugo new <section>/<name>.md` (example: `hugo new posts/new-post.md`).
- For home sections: `hugo new sections/<name>.md -k section`.
