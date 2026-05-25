# Open Source Component Reference Scan

Date: 2026-05-25

This scan records open or source-available references for the first EXCITAT component-library expansion. The goal is not to copy UI code directly, but to extract durable component patterns that can survive eMAG/detail-page HTML constraints.

## References

### Shopify Dawn

- URL: https://github.com/Shopify/dawn
- Useful because: product-page structure, product media, collapsible product information, performance-first theme discipline.
- Borrowable patterns: product media stack, product information sections, low-JS progressive enhancement, theme QA discipline.
- Use boundary: source-available reference theme, not a direct visual source for EXCITAT.

### Preline Ecommerce Blocks

- URL: https://preline.co/blocks/ecommerce/
- Useful because: ecommerce headers, product listing cards, product grids, discovery cards, and filter/listing structures.
- Borrowable patterns: product-card rhythm, category card spacing, ecommerce list hierarchy.
- Use boundary: reference component grammar only; rewrite into our own eMAG-safe HTML or deterministic image boards.

### HyperUI

- URL: https://hyperui.dev/
- Useful because: free open-source Tailwind components for marketing, app, and ecommerce surfaces.
- Borrowable patterns: badges, dividers, cards, banners, detail lists, carts, CTAs.
- Use boundary: use for simple HTML display ideas, not as direct Tailwind dependency for eMAG snippets.

### shadcn/ui

- URL: https://ui.shadcn.com/
- Useful because: copy-owned component philosophy and design-system orientation.
- Borrowable patterns: component ownership model, registry thinking, cards/badges/separators/tabs as controlled building blocks.
- Use boundary: do not import React components into eMAG output; adapt the component-card discipline.

### Animate.css

- URL: https://github.com/animate-css/animate.css
- Useful because: mature catalog of CSS animation primitives.
- Borrowable patterns: pulse, flash, fade, slide, attention effects.
- Use boundary: only subtle motion is allowed for detail-page modules; avoid attention-seeking effects that distract from product proof.

### Motion

- URL: https://motion.dev/
- Useful because: modern animation vocabulary and composable motion patterns.
- Borrowable patterns: transition naming, easing, restrained motion primitives.
- Use boundary: Agent output should use self-contained CSS/SVG/GIF/WebP artifacts, not depend on a runtime animation library inside eMAG HTML.

## First Pattern Takeaways

- Use ecommerce references for structure: media stack, proof rows, product facts, FAQ, package, and trust blocks.
- Use animation references only for tiny primitives: shine, pulse, wipe, progress, step highlight, scan line.
- Avoid importing framework code into production snippets.
- Every borrowed pattern becomes an EXCITAT component card with its own inputs, failure modes, and QA rules.

## Candidate Families To Build First

- `gif-motion`: GIF-like HTML/CSS effects that can later be exported to GIF/WebP.
- `brand-identity`: X-City / EXCITAT wordmark, corner badge, brand strip, animated shine.
- `micro-labels`: E2 marker, rank strip, proof chips, parameter markers, sequence numbers.
- `html-display`: first-screen anchors, FAQ, package table, separators, short proof bands.
