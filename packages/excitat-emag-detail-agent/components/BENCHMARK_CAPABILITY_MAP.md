# Benchmark Capability Map

The component library should push toward the best live reference store, not
only the conservative platform examples.

## Best Benchmark Observed

Source: `/Users/cc/Desktop/photo_show/references/user_cases/20260524_emag_shanggvu_detail_case_chrome/`

Observed capability:

| Capability | Evidence | How we implement it |
| --- | --- | --- |
| Full-width GIF banners | 42 / 45 descriptions used GIF | Use GIF as `<img>` detail media; keep static fallback. |
| Colored HTML sections | Live store uses styled blocks and table wrappers | Use inline `background`, `border`, `padding`, `text-align`; avoid `<style>`. |
| Table layout | 40 / 45 descriptions used tables | Use table grids for feature chips and icon rows; validate mobile preview. |
| Table editor residue | Live HTML often contains `tbody` and table wrapper tags | Treat as benchmark-proven gray zone, not a blocker. |
| Small icon slots | Rendered size summary includes small image slots | Use PNG/GIF icon assets or pre-rendered composite icons. |
| 1140 px source rhythm | Top rendered sizes are mostly 1140 px wide | Author source banners at 1140 px, validate 390 px readability. |
| Single-column mobile flow | Max images per row was 1 for 44 / 45 descriptions | Keep final detail as a vertical module sequence. |

## Engineering Policy

The benchmark tells us what can be attempted. Our guards decide what can ship.

- `benchmark_proven`: observed in the good store and allowed in component cards.
- `stable_candidate`: observed or locally validated, but still needs SKU-specific media QA.
- `experimental`: visually possible but not yet stable enough for batch use.
- `blocked`: technically possible somewhere, but not allowed in our route.

## Allowed Push Components

- background-color feature bands
- black/gold or blue/tech GIF hero banners
- HTML feature grids with small icon images
- brand wordmark side labels
- E2/collection marker chips
- 1-2 GIF proof or usage modules inside a long detail page

## Blocked Even If Seen In The Wild

- iframe video embeds in generated stable listings
- script or external CSS
- copied marketplace logos or platform endorsement
- fake certification badges
- review names, stars, dates, or ratings without evidence
- service claims without source evidence
