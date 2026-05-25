# 2026-05-25 Current Retention Map

This note preserves the useful output from the previous EXCITAT/eMAG detail-page and review-checking discussions before the work is reorganized into a clean repo.

## 1. What Must Be Preserved

### 1.1 Raw Detail HTML Is First-Class Evidence

The earlier research corrected the target: the detail-page workflow must preserve expanded product-detail HTML/DOM, not only screenshots, product images, or extracted metadata.

Reusable selector baseline from `photo_show`:

- `#description-section`
- `#description-body`
- `.product-page-description`
- expand control: `Vezi mai mult`

Useful local files:

- `/Users/cc/Desktop/photo_show/scripts/scrape_emag_detail_html.mjs`
- `/Users/cc/Desktop/photo_show/scripts/summarize_emag_detail_html.mjs`
- `/Users/cc/Desktop/photo_show/scripts/scrape_emag_vendor_detail_case.mjs`
- `/Users/cc/Desktop/photo_show/research/2026-05-23_emag_detail_html_constraints_and_template_inputs.md`
- `/Users/cc/Desktop/photo_show/research/2026-05-23_emag_detail_capability_matrix.md`

Operational rule:

- When headless scraping hits WAF/HTTP 511, use the verified Chrome-session collection path, then batch/resume collection instead of one monolithic sweep.

### 1.2 Detail Generation Stack

The current generation stack is layered and should not collapse into one prompt:

```text
input audit
-> ProductTruthPack
-> buyer_question_map
-> DetailSectionPlan / module_plan
-> image_requirements
-> render detail HTML
-> validate HTML/artifacts/claims
-> human review and repair log
```

Useful local files:

- `/Users/cc/Desktop/photo_show/workflow/EMAG_DETAIL_SCALE_CONTRACT.md`
- `/Users/cc/Desktop/photo_show/workflow/schemas/emag_detail_product_input.schema.json`
- `/Users/cc/Desktop/photo_show/workflow/schemas/emag_detail_section_plan.schema.json`
- `/Users/cc/Desktop/photo_show/scripts/render_emag_detail_from_plan.py`
- `/Users/cc/Desktop/photo_show/scripts/validate_emag_detail_html.py`
- `/Users/cc/Desktop/photo_show/scripts/validate_emag_detail_artifacts.py`
- `/Users/cc/Desktop/photo_show/research/2026-05-24_emag_detail_sop_synthesis_v1.md`

Validator-worthy rules:

- required product/spec/package fields
- allowed and gray-zone HTML tags
- GIF/table/external-host/1140px image warnings
- service/review/rating evidence requirements
- mobile safety and structure checks

Skill/SOP-worthy rules:

- which buyer questions go first
- which module family fits the product category
- how to vary visual rhythm
- when to use FAQ instead of review/testimonial
- when a product needs scene, parameter, package, compatibility, or safety boards

### 1.3 Stable HTML Display Components

The first stable HTML component family is the mobile-first decision structure after the banner.

Key component:

- `first_screen_anchor_triplet`

Purpose:

- three stacked first-screen decision anchors
- answers the top buyer questions before the page enters proof/spec/FAQ modules
- must read as buyer-facing proof, not internal SOP language

Useful local files:

- `/Users/cc/Desktop/photo_show/workflow/emag_detail_module_catalog.v2.json`
- `/Users/cc/Desktop/photo_show/workflow/template_cards/FirstScreenAnchorTriplet.json`
- `/Users/cc/Desktop/photo_show/research/2026-05-24_emag_detail_sop_synthesis_v1.md`

Other reusable micro-components:

- `buyer_question_answer_block`
- `faq_objection_closer`
- `color_band_feature_stack`
- `spec_table_clean`
- `package_and_usage`
- `brand_platform_trust_banner`
- `testimonial_evidence_board`

### 1.4 Stable GIF/Motion Components

Accepted stable motion should be subtle and based on static image overlays.

Current stable effects:

- `shine_sweep`: suitable for brand banner, trust closer, review/feedback board.
- `step_highlight`: suitable for installation, operation, and process proof.

Experimental effects, not default production:

- people micro-motion
- product rotation
- product edge glow
- particle fields
- breathing borders

Useful local files:

- `/Users/cc/Desktop/photo_show/scripts/build_emag_motion_effect_demo_gifs.py`
- `/Users/cc/Desktop/photo_show/output/emag_motion_effect_demos/motion_effect_recipes.json`
- `/Users/cc/Desktop/photo_show/output/emag_motion_effect_demos/index.html`

### 1.5 Stable Banner Component Route

The banner direction is not one fixed visual template. It is a route system:

```text
BannerPlan -> provider/background generation or local composite -> deterministic overlay -> validator -> repair log -> final asset index
```

Three production routes:

- `pure_composite`: precise QA, review, spec, manual, package, and parameter boards.
- `pure_ai_generation`: moodboard/exploration only; not final production.
- `ai_background_plus_composite`: default production route for premium hero, product scene, and brand atmosphere.

Useful local files:

- `/Users/cc/Desktop/photo_show/workflow/emag_stable_component_contract.v1.md`
- `/Users/cc/Desktop/photo_show/workflow/emag_stable_component_catalog.v1.json`
- `/Users/cc/Desktop/photo_show/workflow/agent_flows/emag_detail_banner_agent_v1.md`
- `/Users/cc/Desktop/photo_show/workflow/agent_core/emag_banner_html_agent_v1_1/README.md`
- `/Users/cc/Desktop/photo_show/workflow/agent_core/emag_banner_html_agent_v1_1/DESIGN.md`
- `/Users/cc/Desktop/photo_show/workflow/agent_core/emag_banner_html_agent_v1_1/DESIGN_FD.md`
- `/Users/cc/Desktop/photo_show/workflow/agent_core/emag_banner_html_agent_v1_1/data/banner_patterns.jsonl`
- `/Users/cc/Desktop/photo_show/workflow/agent_core/emag_banner_html_agent_v1_1/data/validation_cases.jsonl`
- `/Users/cc/Desktop/photo_show/workflow/agent_core/emag_banner_html_agent_v1_1/validators/VALIDATION_RULES.md`

Current banner families:

- `premium_dark_brand_trust`
- `product_tech_context`
- `official_blue_people_category` as style reference only
- QA board
- review/feedback board
- product proof banner
- brand closer
- step highlight GIF

### 1.6 Stable Component Contract

Every reusable component should have these fields:

- `component_id`
- `required_inputs`
- `buyer_question`
- `output_type`
- `invariants`
- `allowed_variations`
- `failure_modes`
- `asset_paths`
- `media_asset_index` records
- `validation_notes`

Core input packs:

- `ProductTruthPack`
- `BrandKit`
- `AssetInventory`
- `IconLibrary`
- `EvidencePack`

Component output contract:

- `detail.html`
- `preview_mobile.html`
- `DESIGN_SPEC.json`
- `validation_report.json`
- `media_asset_index.json`
- optional `repair_log.md`

### 1.7 Evidence and Review Rules

Important non-negotiable rules:

- QA and Review are separate component families.
- Review/testimonial/star rating/name/date require real sourced review evidence.
- Service claims such as delivery, return, warranty, seller rating, and support require source evidence.
- If evidence is missing, use FAQ, buyer-question framing, or preview labeling instead of fake social proof.
- Official eMAG assets can be references, not commercial assets unless rights are confirmed.

### 1.8 Visual Quality Rules

Known failures to avoid:

- long flat `image + text` repetition
- internal SOP copy appearing in the customer-facing page
- a compliance-cleaned single board instead of named modules
- too many dark modules in sequence
- too many small framed cards
- repeated product hero images without new proof
- model-generated small text
- product shape drift in AI output

Useful rhythm:

```text
wide scene/banner
-> short white/light text
-> cropped proof image
-> spec/QA/module board
-> package/use/review-if-real
-> trust closer
```

## 2. What Is Not Yet Done

- No mature component-library UI.
- No complete component search/retrieval layer.
- No real provider comparison for OpenAI/FAL/Google image generation in this cleaned repo.
- No 10-20 approved fixed Banner/Manner templates yet.
- No complete category palette system for baby, tech, home, cleaning, beauty, kitchen, and brand trust.
- No packaged `agent-platform` built-in Agent yet.
- No stable DesignMD source-of-truth file yet.

## 3. Immediate Migration Priority

1. Copy contracts and catalogs first.
2. Copy schemas and validators second.
3. Copy agent-core docs and prompt contracts third.
4. Copy only the best example outputs, not every experiment.
5. Create a visual QA checklist and sample gallery before expanding template count.
