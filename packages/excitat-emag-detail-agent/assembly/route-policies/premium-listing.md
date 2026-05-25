# Route Policy: premium_listing

Use for refined SKU detail pages where one or two distinctive banners can improve perceived quality.

Rules:

- Maximum two image-generation jobs.
- Image jobs may only produce hero/banner/background/brand-trust/proof-scene assets.
- Final product placement, brand text, headings, numbers, service cues, icons, QA, and review cards must be deterministic.
- Generated images are candidates until Visual QA passes.
- If product shape drifts, use a real product cutout and deterministic composite.
- If generated text appears, reject or repair unless it is fully replaced during deterministic post-processing.
- PublishGuard must pass before final export.

Default component order:

```text
premium_generated_or_composite_hero
-> first_screen_anchor_triplet
-> product_scene_or_proof_banner
-> stable_feature_modules
-> spec_icon_board
-> package_and_usage
-> faq_or_review_if_real
-> brand_trust_close
```
