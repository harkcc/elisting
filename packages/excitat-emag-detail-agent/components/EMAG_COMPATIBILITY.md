# eMAG Component Compatibility Contract

This package separates component source patterns from eMAG production HTML.

The capability target is not the most conservative eMAG help-page example. The
target is the best live store benchmark already captured in `photo_show`, then
reduced into stable repeatable patterns.

## Compatibility Tiers

### Tier A: Benchmark-Proven Production Detail HTML

Use this tier for final eMAG product descriptions.

- Allowed output is simple HTML with image embeds and light text structure.
- Preferred tags: `p`, `h1`-`h6`, `strong`, `br`, `img`, `ul`, `ol`, `li`.
- Accepted with caution: `table`, `tr`, `td`, `tbody`, `thead`, `th`, `div`, `blockquote`, `em`, `b`, `center`, `u`, `hr`.
- Inline background color, border, padding, text alignment, and image sizing are allowed when they come from a benchmark-proven pattern.
- Small decorative or explanatory icons must be `img` assets or part of a pre-rendered composite, not inline SVG or icon-font dependencies.
- Motion must be pre-rendered as media and embedded as an image.

Example production embed:

```html
<p data-component-id="motion_shine_sweep_gold" data-edit-id="hero-banner-01" style="text-align:center;margin:0 0 18px;">
  <img src="assets/hero-banner.gif" width="800" alt="Product feature banner">
</p>
```

### Tier B: Production Composite Asset

Use this tier for deterministic banner construction before final HTML export.

- HTML/CSS/canvas/SVG may be used inside the local renderer.
- The renderer must export PNG/JPG/GIF/WebP before entering eMAG detail HTML.
- Final text, numbers, logo, proof labels, and product cutouts are overlaid deterministically.
- AI image generation is only allowed for approved `premium_listing` background or atmosphere jobs.

### Tier C: Preview-Only Source Pattern

Use this tier for local design review and motion exploration only.

- CSS keyframes, pseudo-elements, gradients, and layout grids are allowed in preview files.
- Do not paste these source blocks directly into eMAG production descriptions.
- Promote to Tier A only after exporting a static or animated image and validating the final HTML.

## Current eMAG Rule Interpretation

The local validator follows the earlier eMAG detail-page contract and live
benchmark captures:

- GIF in description HTML is accepted as an `img` detail media signal.
- Unknown tags such as `style`, `script`, `iframe`, `svg`, `canvas`, and form controls are blockers.
- Gray-zone tags and tables are warnings, not blockers.
- Price, promotion, contact, unsupported service, warranty, delivery, and platform claims are blockers unless the route has explicit evidence and the target field allows them.

The stronger live benchmark currently comes from the `shanggvu / Besplaz` Chrome
capture:

- 45 captured descriptions with HTML found.
- 42 / 45 descriptions used GIF.
- 40 / 45 descriptions used table layout.
- 347 total description images.
- Top rendered image width was 1140 px, usually in a single mobile column.
- The store uses repeated full-width banners, table-based content blocks,
  external-hosted media, GIFs, and small rendered icon slots.

This means our practical upper bound includes:

- colored background blocks through inline style
- table-based feature grids
- small image icons
- GIF banners and GIF proof/usage modules
- 1140 px source assets that collapse to the mobile description width

It does not justify:

- JavaScript interaction
- CSS keyframes pasted into the marketplace editor
- inline SVG
- external CSS
- fake platform marks, fake reviews, fake service claims, or unsupported proof

Official eMAG Marketplace guidance also distinguishes between product images and description content:

- Product image upload allows JPG/PNG/JPEG/GIF extensions, but dynamic GIF images are not accepted in image upload slots.
- Description editing supports plain text, images, video, and simple HTML-formatted text.

Therefore, this package treats animated GIFs as detail-description media candidates, not product-gallery image-upload candidates.

## Stability Rules

Every component card must declare:

- `component_name`
- `tags`
- `listing_modules`
- `source_code`
- `usage_guide`
- `emag_compatibility`
- `stability_tier`
- `failure_modes`

Any component with CSS animation remains `preview_only_css_animation` until it has a rendered media asset, a static fallback, and a passing eMAG HTML validation report.
