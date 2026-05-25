# Stable GIF Design MD

This Design MD controls how small GIF components are allowed to enter eMAG
listing pages. It follows the Open Design idea: design first, component second,
motion last.

## Visual Theme & Atmosphere

The listing should feel like a calm premium product manual, not a motion demo.
Use motion as a small signal that guides the buyer's eye.

Default atmosphere:

- clean white cards for micro components
- one black-gold hero or trust banner when premium tone is needed
- restrained technical blue only for EV, tools, electronics, and spec modules
- no noisy product image as full background unless the image is already a clean banner

## Color Palette & Roles

Use a 70 / 20 / 8 / 2 balance:

- 70% neutral: white, off-white, dark navy, gray text
- 20% structural surface: cards, table bands, quiet dividers
- 8% accent: gold, blue, green, or orange
- 2% motion/effect: shine, pulse, glow, sweep

Color rules:

- Black-gold is the primary premium route.
- Blue is a category variant for technical modules, not a second independent component.
- Green is for proof/check state only.
- Orange is for package or warm attention markers.
- Do not use more than one accent family in one module.

## Typography Rules

- Banner headline: 36-56 px in source image.
- Small component label: 18-28 px in source image.
- Micro chip text: 14-18 px in source image.
- Do not put paragraph text inside a GIF.
- Mobile 390 px must still identify the label purpose.

## Component Stylings

### Hero / Trust Banner

Use one `shine_sweep` design with color variants.

- `black_gold`: default premium hero.
- `blue_tech`: technical variant only.

Do not maintain two separate design concepts just because the color changes.

### 123 / 1234 Sequence

Use for ordered buyer education.

- Good for: feature intro, usage steps, package sequence, selection logic.
- Keep labels short: one or two words.
- The active state should be slow enough to read.

### Brand Small Label

Use `brand_wordmark_shine` and `corner_badge_shine` as small tags, not large
sections.

- Good for: side label, corner marker, brand closer.
- White / off-white card context usually looks better than heavy black blocks.
- Brand text must be deterministic and locally rendered.

### Pulse / Glow / Scan

These are assistive effects.

- `motion_pulse_dot`: tiny attention marker for one verified point.
- `motion_soft_glow_border`: one focused trust/notice card.
- `motion_scan_line`: technical/spec context only.

## Motion Rules

Motion speed is part of the design language.

| Motion tier | Duration | Use |
| --- | --- | --- |
| Luxury slow | 4.2-5.6s | shine sweep, soft glow, brand wordmark |
| Reading slow | 3.6-4.8s | 123 / 1234 highlights |
| Utility medium | 2.8-3.6s | scan line, progress |
| Micro attention | 2.0-2.8s | pulse dot, badge dot |

Do not use fast looping motion for premium modules. Fast loops feel cheap.

## Layout Principles

- Start with text plan and module purpose.
- Choose the module container before choosing the GIF.
- Keep black-gold hero as the first or last major visual, not repeated through the page.
- Put small brand tags beside or inside modules, not as a full-width black banner every time.
- Do not stack more than two dark modules without a white or light rest module.
- When in doubt, use a white card with one small moving element.

## Depth & Elevation

Prefer flat surfaces and hairline borders.

- White cards: 1 px border, no heavy shadow.
- Dark premium banners: one gold rule, one product inset, one motion effect.
- Small chips: pill or square tag with one status dot.
- Avoid decorative gradients unless they carry hierarchy.

## Do's and Don'ts

Do:

- Use one strong visual move per module.
- Keep motion tied to a buyer question.
- Use real product images as inset or proof media only.
- Export final motion as GIF/WebP/PNG before eMAG HTML.
- Keep GIFs small enough for detail-page loading.

Do not:

- Use a noisy full product image as the background for every component.
- Use CSS animation directly in final eMAG HTML.
- Make every component black-gold.
- Use moving text that becomes unreadable.
- Use badges that look like certification, platform approval, award, or guarantee.

## Responsive Behavior

- Source asset width can be 1140 px, but must pass 390 px visual review.
- Micro labels need to stay recognizable at 375-390 px viewport.
- Sequence components can remain one row if labels are short; otherwise split into two modules.
- Full-width GIF modules should be separated by visual rest.

## Agent Prompt Guide

When applying a GIF component:

1. Identify the listing module.
2. Pick the Design MD component.
3. Decide whether this is Design MD only or Adapted MD.
4. Load reference and guard.
5. Apply color and speed parameters.
6. Render final GIF/PNG.
7. Validate eMAG HTML and 390 px preview.

If the component does not improve hierarchy, remove it.

