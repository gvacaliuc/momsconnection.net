# Website Redesign Plan (Step-by-step)

## 0) Baseline Snapshot (Current State)
**Goal:** establish a reference build for HTML parity checks.
- Commands:
  - `git submodule update --init`
  - `hugo version` (confirm `<= v0.119.0`)
  - `hugo --minify` (or `hugo` if minify not used)
  - `cp -R public public.baseline`
- Success criteria:
  - `public.baseline/` exists and contains the current site output.
  - No errors in build output.

## 1) Theme Removal (Keep HTML the Same)
**Goal:** remove `themes/terrassa` while preserving generated HTML.
- Steps:
  - Copy theme templates into repo-local layouts:
    - `cp -R themes/terrassa/layouts/* layouts/`
  - Copy theme assets if needed:
    - `cp -R themes/terrassa/assets/* assets/` (only if Hugo pipes are used)
    - `cp -R themes/terrassa/static/* static/` (for static files)
  - Update `config.toml` to remove `theme = "terrassa"`.
  - Remove submodule from git index and filesystem:
    - `git rm -r themes/terrassa`
    - remove `.gitmodules` entry if present.
  - Rebuild: `hugo` and compare to baseline.
- Success criteria:
  - `themes/terrassa` no longer exists and no submodule remains.
  - `hugo` builds without theme references.
  - HTML output matches baseline (diff acceptable only for non-semantic ordering):
    - `diff -ru public.baseline public` is empty or only trivial differences.

## 2) Hugo Upgrade (Keep HTML as Close as Possible)
**Goal:** run on latest Hugo with minimal output changes.
- Install latest Hugo (macOS/Homebrew):
  - `brew install hugo` or `brew upgrade hugo`
  - Verify: `hugo version` (record version in notes).
- Rebuild: `hugo` and compare to baseline.
- If output differs:
  - Identify changes via `diff -ru public.baseline public`.
  - Adjust templates or config until diffs are minimized.
- Success criteria:
  - Latest Hugo builds the site without warnings or errors.
  - Output is identical or diffs are limited to known, documented changes.

## 3) Design Translation Plan (Desktop Only)
**Goal:** map comps to reusable components and templates.
- Create a component inventory:
  - Header/nav, hero, section titles, text blocks, icon clusters, cards, forms.
- Define design tokens:
  - Colors, type scale, spacing scale, border radius, shadow, button styles.
- Success criteria:
  - A written mapping between each comp and templates/partials.
  - Tokens documented and referenced by CSS variables.

## 4) Template Refactor (New Layouts, Same Content)
**Goal:** wire pages to new layouts using existing content where possible.
- Implement base layout:
  - `layouts/_default/baseof.html`
  - `layouts/partials/header.html`, `footer.html`
- Create page templates:
  - Home: `layouts/index.html`
  - My Story: `layouts/page/my-story.html` (or `layouts/_default/single.html`)
  - Services: `layouts/page/services.html`
  - Resources: `layouts/page/resources.html`
- Success criteria:
  - Each page renders with the new layout files.
  - No missing template errors.

## 5) Content Modeling & Data Sources
**Goal:** support repeatable blocks cleanly.
- Decide what goes in front matter vs `data/`:
  - Services packages, resource cards, poem cards, link lists.
- Implement shortcodes or partials for repeated blocks.
- Success criteria:
  - Content is editable without touching templates for routine updates.
  - Clear examples exist in `content/` or `data/`.

## 6) Visual Build-out (Desktop Fidelity)
**Goal:** match the comps with practical improvements.
- Implement CSS in `assets/css/custom.css` (or SCSS if enabled).
- Include only necessary images in `static/` and optimize sizing.
- Acceptable simplifications:
  - If a design element is unclear or inconsistent, use a clean, consistent pattern.
- Success criteria:
  - Each desktop page visually matches the comp at a glance.
  - Approved deviations are documented in a short list.

## 7) QA & Accessibility
**Goal:** ensure a clean, accessible, working site.
- Check:
  - Headings in order, alt text on images, color contrast.
  - Links on Resources page, form action/behavior.
- Success criteria:
  - No broken links.
  - Reasonable contrast and semantic structure.

## 8) Deployment & Post-launch
**Goal:** ship and verify.
- Build: `hugo` and verify `public/`.
- Deploy (confirm current method).
- Follow-up:
  - Review mobile layouts using `designs/mobile/`.
- Success criteria:
  - Live site matches desktop comps.
  - Deployment is reproducible.
