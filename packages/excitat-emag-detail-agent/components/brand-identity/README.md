# Brand Identity Components

Brand identity components are reusable EXCITAT / X-City style wordmarks, badges, overlays, and motion marks.

They are not full banners. They are brand layers that can be embedded into:

- composited banner images
- static product proof boards
- GIF/WebP motion modules
- eMAG-safe HTML as image tags

Initial components:

- `brand_wordmark_xcity_static_v1`
- `brand_wordmark_excitat_static_v1`
- `brand_badge_corner_tag_v1`
- `brand_motion_shine_sweep_v1`

Rules:

- Do not ask the image model to render final brand text.
- Keep static PNG/SVG and animated GIF/WebP variants as separate asset records.
- Each variant must declare dark-background, light-background, and transparent-background compatibility.
- Brand spelling must be exact and locally rendered.
