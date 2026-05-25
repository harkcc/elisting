# Repo Collaboration Plan

This document defines how `elisting`, `photo_show`, and `agent-platform` should work together.

## 1. Repository Roles

### `elisting`

Purpose: clean source of truth for e-commerce listing/detail-page production assets.

Owns:

- component contracts
- stable component catalogs
- DesignMD-style design rules
- BannerPlan and prompt contracts
- review/QA/evidence policies
- validators and fixtures related to listing/detail outputs
- selected reference galleries and approved example outputs
- agent package specs before platform migration

Should not become:

- a dumping ground for every generated image
- a raw browser-capture archive without summaries
- a replacement for `agent-platform` runtime code

### `/Users/cc/Desktop/photo_show`

Purpose: current experiment and source workspace.

Owns for now:

- old research notes
- large generated output folders
- local reference captures
- exploratory scripts
- one-off visual tests
- previous conversation artifacts

Migration rule:

- Treat `photo_show` as the evidence mine and prototype lab.
- Promote only reviewed contracts, schemas, validators, prompt contracts, selected examples, and stable scripts into `elisting`.

### `/Users/cc/projects/agent-platform`

Purpose: runtime and product platform.

Owns:

- Agent profiles
- Skill/SOP loading and matching
- Task/evidence/session persistence
- Guard/Hook/validator integration boundaries
- Tool/MCP/browser execution
- desktop UI and artifact preview surfaces

Migration rule:

- Do not put e-commerce-specific business rules into generic core runtime.
- Package e-listing behavior as Agent profile, Skill, references, validators, fixtures, and tool adapters.
- Runtime should host and execute the package, not hardcode the domain.

## 2. Proposed Clean Directory Shape for `elisting`

```text
elisting/
  README.md
  docs/
    repo-collaboration-plan.md
    2026-05-25-current-retention-map.md
    designmd-notes.md
    migration-log.md
  packages/
    excitat-emag-detail-agent/
      README.md
      DESIGN.md
      DESIGN_FD.md
      SKILL.md
      agent-profile.json
      data/
        banner_patterns.jsonl
        tag_library.jsonl
        validation_cases.jsonl
      prompt_contracts/
      validators/
      fixtures/
      examples/
  components/
    html-display/
    gif-motion/
    banner/
  schemas/
  scripts/
  references/
    approved/
    source-indexes/
  examples/
    approved-detail-pages/
    approved-banners/
```

## 3. Component Library Direction

### HTML Display Components

Role: simple, stable eMAG-safe detail HTML modules.

Initial candidates:

- `first_screen_anchor_triplet`
- `buyer_question_answer_block`
- `faq_objection_closer`
- `color_band_feature_stack`
- `spec_table_clean`
- `package_and_usage`

Acceptance criteria:

- mobile-first 390px readable
- allowed/gray-zone tags documented
- one module answers one buyer question
- output can be validated without visual guessing

### GIF/Motion Components

Role: reusable motion that does not damage product accuracy or mobile readability.

Initial candidates:

- `shine_sweep`
- `step_highlight`
- `icon_pulse` only after validation

Acceptance criteria:

- static first frame works
- no product deformation
- one motion answers one proof/action need
- size and embed path documented

### Banner Components

Role: larger visual modules, usually exported as image/GIF and embedded in HTML.

Initial families:

- product-tech hero
- warm/soft category hero
- brand trust banner
- QA board
- review evidence board
- proof crop banner
- step/process banner
- brand closer

Acceptance criteria:

- has `BannerPlan`
- uses ProductTruthPack/EvidencePack for text and claims
- records route: `pure_composite`, `pure_ai_generation`, or `ai_background_plus_composite`
- has validator report and repair notes

## 4. API-Generated Banner Direction

The image API layer should be provider-adapter based.

Provider-neutral interface:

```text
ImageGenerationRequest:
  provider
  model
  mode: text_to_image | image_to_image | edit | background_only
  reference_images
  prompt
  negative_prompt
  canvas_size
  seed_or_style_ref
  output_contract
```

Important rule:

- The provider creates background/scene/mood/product context only when safe.
- Deterministic local composition adds final product cutout, logo, text, icons, claims, QA, review cards, and service cues.

First route to build:

```text
reference image + background prompt
-> generated no-text background
-> local product/text/icon composite
-> image validator
-> HTML embed validator
-> review note
```

## 5. DesignMD Relationship

DesignMD should be the human-readable design contract, not the runtime itself.

Recommended layers:

- `DESIGN.md`: current working visual system and rhythm.
- `DESIGN_FD.md`: front-end/eMAG HTML delivery contract.
- `DesignMD` / `TemplateSpec`: stricter design token, layout slot, safe-area, component, prompt, and forbidden-pattern source of truth.
- `validator`: machine checks derived from DesignMD and component contracts.
- `Skill/SOP`: judgment layer for product category, buyer-question order, and review/evidence decisions.

This fits `agent-platform` because current platform docs already separate:

- Agent profile as business role and defaults
- Skill/SOP as reusable process
- Task/evidence as execution ledger
- Hook/Guard as runtime lifecycle validation
- references as business/domain package material

## 6. Agent Platform Migration Shape

When ready, `elisting` should export a package shaped like:

```text
agent-core/
  profile.json
  skills/
    excitat-emag-detail-generation/SKILL.md
    excitat-banner-generation/SKILL.md
    excitat-listing-review/SKILL.md
  references/
    DESIGN.md
    DESIGN_FD.md
    component_catalog.json
    banner_patterns.jsonl
    validation_rules.md
  validators/
    validate_detail_html.py
    validate_banner_output.py
  fixtures/
    product_truth_pack.sample.json
    module_plan.sample.json
    expected_validation_report.sample.json
```

Platform integration principles:

- Skill triggers decide when this package is active.
- Validators produce evidence/ReviewLog artifacts.
- Guard/Hook can warn or block unsupported strong claims.
- Browser/Electron preview should verify final visual output, not just schema pass.

## 7. Next Execution Order

1. Promote the current contracts, catalogs, and agent-core docs from `photo_show`.
2. Normalize schemas and validators into a repo-level `schemas/` and `scripts/` layout.
3. Select 3-5 approved visual examples and record why they passed.
4. Build the first `packages/excitat-emag-detail-agent` skeleton.
5. Add one image-provider adapter path for reference-image + prompt background generation.
6. Add a visual review checklist and repair log format.
7. Only then expand to many category templates.
