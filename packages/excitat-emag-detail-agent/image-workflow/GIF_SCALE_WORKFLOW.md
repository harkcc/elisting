# GIF Scale Workflow

GIF is not a decoration step that the model adds freely. It is a small Scale
pipeline with its own reference, assist, guard, and delivery outputs.

## Fixed Order

```text
TextPlan
-> BaseAssembly
-> DesignState
-> ComponentMatch
-> ImageAdaptation
-> MotionEffect
-> GuardReview
-> Delivery
```

## 1. TextPlan

Generate the listing text first.

Required output:

- buyer questions
- module order
- headline and subcopy
- 3-4 key points
- proof facts and evidence ids
- FAQ / objection copy

Guard:

- no unsupported service claims
- no fake review, rating, star, date, name, or certification
- no text that depends on an unverified product fact

## 2. BaseAssembly

Insert product images and basic HTML styles before motion.

Allowed:

- `<p>`, `<img>`, `<table>`, `<tr>`, `<td>`, `<strong>`, `<br>`, `ul/li`
- inline background color, border, padding, center alignment
- 1-2 simple tables for sequence or feature grids

Guard:

- mobile 390 px cannot overflow horizontally
- image modules remain single-column
- each module has `component_id` and `data-edit-id`

## 3. DesignState

Set the overall palette and rhythm from the product image.

Required output:

- dominant dark/light mode
- accent color
- product-safe text zones
- image-to-text ratio
- module density level

Guard:

- no repeated heavy dark blocks without a visual rest
- text stays readable after scaling to mobile
- product body is not distorted by generated or motion layers

## 4. ComponentMatch

Choose components by module, not by visual taste.

Examples:

- Hero banner: `motion_shine_sweep`, `motion_background_light_streak`
- 123 sequence: `motion_icon_sequential_glow`, `motion_step_highlight`
- Product proof: `motion_magnifier_pulse`, `motion_product_edge_glow`
- Brand trust: `motion_dotted_twinkle`, `motion_parcel_micro_motion`, `brand_wordmark_shine`
- Feature grid: `rank_number_strip`, `proof_check_chip`, `e2_marker_chip`

Guard:

- every selected GIF must have a module purpose
- no more than 1-2 strong GIF modules per short listing
- do not use before/after motion unless evidence supports the comparison

## 5. ImageAdaptation

Adapt the component to the specific product image.

Assist inputs:

- source product image
- crop/focus area
- palette
- headline and labels
- icon set
- output size

Guard:

- product remains recognizable
- effect does not cover important product detail
- text overlays do not cross high-noise zones

## 6. MotionEffect

Add the GIF effect after the still design is already acceptable.

Allowed effects:

- shine sweep
- icon sequential glow
- soft border breathing
- product edge glow
- background light streak
- dotted twinkle
- step highlight
- before/after wipe with evidence
- magnifier pulse
- package / brand micro-motion

Blocked effects:

- product rotation without a motion pipeline
- fake official badge movement
- unreadable moving text
- CSS keyframes pasted into eMAG
- JS / SVG / canvas in final HTML

## 7. GuardReview

Required reports:

- `media_asset_index.json`
- `gif_scale_report.json`
- eMAG HTML validator report
- mobile overflow check

## 8. Delivery

Deliver:

- production HTML snippet
- GIF/PNG assets
- component usage notes
- static fallback rule when GIF is too large or visually unstable

