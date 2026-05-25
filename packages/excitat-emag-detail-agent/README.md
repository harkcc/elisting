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
