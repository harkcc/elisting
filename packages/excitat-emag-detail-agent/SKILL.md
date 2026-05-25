---
name: excitat-emag-detail-agent
description: Generate EXCITAT eMAG listing/detail-page assets through stable components or controlled premium image-generation banners.
triggers:
  - "eMAG detail page"
  - "listing detail"
  - "EXCITAT"
  - "stable_listing"
  - "premium_listing"
---

# EXCITAT eMAG Detail Agent

Use this Skill when producing or reviewing e-commerce detail-page modules, listing images, brand banners, QA boards, proof boards, or eMAG-safe HTML.

## Required Reading Order

Before planning modules, read:

1. `DESIGN.md`
2. `DESIGN_FD.md`
3. `data/stable-component-contract.md`
4. `image-workflow/IMAGE_PROMPT_CONTRACT.md`
5. `assembly/route-policies/stable-listing.md` or `assembly/route-policies/premium-listing.md`
6. `validators/VALIDATION_RULES.md`

## Workflow

1. Identify input completeness: product facts, images, specs, package contents, review/QA evidence, seller-service evidence, and output goal.
2. Run pre-verify guards: route eligibility, evidence availability, asset availability, and brand policy.
3. Select route:
   - Use `stable_listing` for batch/listing scale work.
   - Use `premium_listing` only when the user needs a refined detail page or premium banner quality.
4. Create SPEC artifacts: state design, template selection, chat plan, chart specs, evidence index, media asset index, QA report, repair plan, and execute report.
5. Select stable components before writing new modules.
6. For premium route, create one or two image jobs only for hero/banner/background/brand-trust use.
7. Render exact text, product placement, brand marks, icons, numeric claims, QA, and review cards deterministically.
8. Verify, repair, and export.

## Guard Rules

- Do not invent review names, ratings, dates, service facts, platform guarantees, warranty, return, shipping, or seller claims.
- If review evidence is missing, use FAQ/common objections or mark review modules as preview only.
- If service evidence is missing, use neutral brand-process language, not promises.
- If generated image text is readable, treat it as a failure unless explicitly marked as disposable exploration.
- If product shape drifts, switch to real product cutout plus deterministic composite.
- If the page fails 390px mobile readability, repair before final export.

## Output Contract

Every run should produce or update:

- `spec/state-design.json`
- `spec/template-selection.json`
- `spec/chat-plan.md`
- `spec/chart-specs.json`
- `spec/evidence-index.json`
- `spec/media-asset-index.json`
- `spec/qa-report.json`
- `spec/repair-plan.md`
- `spec/execute-report.json`

Final HTML modules must include stable `component_id` and `data-edit-id`.
