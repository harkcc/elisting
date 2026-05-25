# Route Policy: stable_listing

Use for batch listings, low-cost SKU tests, and pages where clear product communication matters more than premium visual differentiation.

Rules:

- Do not call image generation.
- Use stable components, existing product assets, brand identity components, and deterministic renderers.
- Review/testimonial modules require real review evidence; otherwise use FAQ/common-objection framing.
- Service claims require evidence; otherwise use neutral process language.
- Every module must render with `component_id` and `data-edit-id`.
- Final output must include SPEC files, QA report, and execute report.

Default component order:

```text
existing_or_composite_banner
-> first_screen_anchor_triplet
-> product_proof_or_feature_band
-> spec_table_or_spec_icon_board
-> package_and_usage
-> faq_objection_closer
-> brand_identity_or_trust_close
```
