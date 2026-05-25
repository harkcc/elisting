# Component Application SOP

The listing page is assembled by buyer question, not by visual decoration. Select a module first, then select compatible components.

## Module Map

| Listing module | Buyer question | Component families | Recommended components | Notes |
| --- | --- | --- | --- | --- |
| Hero banner | What is this product and why should I keep reading? | `banner-composite`, `gif-motion`, `brand-identity` | `motion_shine_sweep_gold`, `motion_shine_sweep_blue`, `brand_wordmark_shine`, `corner_badge_shine` | Use product color to choose gold, blue, green, or neutral accent. Export as image/GIF before eMAG HTML. |
| Feature intro | What are the top 3-4 benefits? | `html-display`, `micro-labels`, `gif-motion` | `rank_number_strip`, `proof_check_chip`, `motion_step_highlight_3`, `motion_step_highlight_4` | Keep each point short enough for 390 px mobile. |
| Product display | What does the product look like in use? | `banner-composite`, `gif-motion` | `motion_scan_line`, `motion_soft_glow_border`, `motion_radar_ping` | Product body must come from real product media, not generated product structure. |
| Trust builder | Why should I believe the page? | `brand-identity`, `micro-labels`, `banner-composite` | `brand_wordmark_shine`, `proof_check_chip`, `corner_badge_shine`, `motion_shine_sweep_gold` | Do not create fake certification, fake platform badges, fake reviews, or fake stars. |
| Key points 1-2-3-4 | In what order should I read the value points? | `micro-labels`, `html-display`, `gif-motion` | `rank_number_strip`, `motion_step_highlight_3`, `motion_step_highlight_4`, `motion_progress_fill` | Good for function intro, installation, package contents, or selection logic. |
| Specification board | What are the measurable facts? | `html-display`, `banner-composite` | `proof_check_chip`, `e2_marker_chip`, `motion_scan_line` | Numbers must come from evidence or product fields. |
| Package contents | What is included? | `micro-labels`, `banner-composite` | `package_count_pulse`, `proof_check_chip`, `rank_number_strip` | Avoid service promises. Package claims must match source images or supplier data. |
| Before / after | What changes after use? | `gif-motion`, `banner-composite` | `motion_before_after_wipe` | Only use with real before/after evidence or clearly illustrative non-claim scenes. |
| FAQ / objection handling | What might make me hesitate? | `html-display`, `micro-labels` | `proof_check_chip`, `e2_marker_chip`, `rank_number_strip` | If evidence is missing, downgrade testimonial/review blocks to FAQ preview. |
| Brand side label | Who is presenting this and what family is it? | `brand-identity`, `micro-labels` | `brand_wordmark_shine`, `corner_badge_shine`, `e2_marker_chip` | Safe for EXCITAT/X-City identity and internal collection markers. |

## Route Rules

### `stable_listing`

- Do not call image generation.
- Use existing product photos, deterministic HTML, and pre-rendered assets.
- Use motion only when the asset already exists as GIF/WebP/PNG and has a static fallback.
- Components can be reused across SKUs if the tags match the module and category.

### `premium_listing`

- Allow at most 1-2 image jobs.
- Use generated images only for background, atmosphere, scene, or style transfer.
- Composite final product, text, numbers, logo, and proof labels deterministically.
- Run Visual QA before exporting final detail HTML.

## Selection Order

1. Read `state-design.json` for category, route, brand tone, product color, and target output.
2. Read `evidence-index.json` and remove any component that needs unavailable proof.
3. Pick modules from the template blueprint.
4. Filter components by `tags`, `listing_modules`, route, and compatibility tier.
5. Render or export components.
6. Validate final HTML and media index.
7. If a guard fails, repair locally or downgrade to a simpler component.

