# EXCITAT eMAG Detail Agent

This package is the first clean source package for the EXCITAT listing/detail-page production system.

It supports two production routes:

- `stable_listing`: low-cost batch route. It uses stable components, existing assets, and deterministic rendering only.
- `premium_listing`: refined route. It allows one or two image-generation jobs for distinctive banners, then uses deterministic composition for product, text, numbers, icons, and evidence-backed claims.

The package is designed to migrate later into `agent-platform` as an Agent/Profile/Skill/reference/validator bundle. It does not modify `agent-platform` runtime code.

## Package Map

```text
DESIGN.md                 Visual design system.
DESIGN_FD.md              eMAG-safe HTML and front-end delivery contract.
SKILL.md                  Agent SOP and route policy.
agent-profile.json        Agent Platform adapter draft.
data/                     Component catalogs, route rules, validation cases.
components/               Component-family definitions.
image-workflow/           Prompt and image-generation workflow.
spec/                     Auditable output SPEC templates.
assembly/                 Stable and premium route policies and blueprints.
renderers/                Deterministic renderer contracts.
validators/               Guard rules and package validation.
examples/                 Approved examples only.
```

## First Component Candidates

- `components/gif-motion/component-candidates.md` lists the first 16 small motion / brand / micro-label candidates.
- `examples/component-gallery/gif-motion-html-preview.html` is the current HTML/CSS preview page for review.
- `components/micro-labels/README.md` defines E2 marker, rank strip, proof chip, and related ordering labels.

## Component Stability Position

The HTML/CSS motion gallery is a local preview and source-pattern library. Do
not paste its CSS keyframes into eMAG descriptions.

For production eMAG detail HTML, motion components must be exported as
GIF/WebP/PNG and embedded through simple image HTML. See:

- `components/EMAG_COMPATIBILITY.md`
- `components/BENCHMARK_CAPABILITY_MAP.md`
- `components/COMPONENT_APPLICATION_SOP.md`
- `components/STABLE_GIF_DESIGN_MD.md`
- `data/component-cards.json`
- `data/gif-component-usage-cards.json`
- `data/stable-16-gif-library.json`
- `data/stable-16-application-table.json`
- `image-workflow/GIF_SCALE_WORKFLOW.md`
- `renderers/gif-motion-renderer.py`
- `renderers/stable-16-component-renderer.py`
- `examples/d6mhw43bm-component-application/demo.html`
- `examples/d6mhw43bm-component-application/benchmark-push-demo.html`
- `examples/d6mhw43bm-component-application/adapted-gif-component-gallery.html`
- `examples/d6mhw43bm-component-application/adapted-listing-flow-demo.html`
- `examples/stable-16-component-trial/stable-16-component-trial.html`

## Production Loop

```text
Input recognition
-> Pre-verify guards
-> Route selection
-> Lock design and template
-> Build evidence and media indexes
-> Generate modules or image jobs
-> Deterministic render
-> Verify
-> Repair
-> Execute/export
```

## Non-Negotiable Rules

- Stable listings must not call image generation.
- Premium listings may use at most two image-generation jobs.
- Image models must not generate final small text, brand names, parameter numbers, review identities, service promises, marketplace marks, or precise product facts.
- Review, rating, warranty, return, shipping, and seller-service claims require evidence.
- Every final module needs `component_id` and `data-edit-id` for preview annotation and local repair.
