# elisting

`elisting` is the working repository for the EXCITAT detail-page, review-checking, component-library, and banner-generation system.

This repo should become the clean source of truth for work that is currently scattered across `/Users/cc/Desktop/photo_show` experiments and later needs to connect with `/Users/cc/projects/agent-platform`.

## Current Direction

The system is split into three tracks:

1. Stable component library
   - HTML display components for ordering, separators, tables, FAQ, buyer-question blocks, and first-screen anchors.
   - GIF/motion components for simple reusable motion such as shine sweep and step highlight.
   - Banner components, including product-scene banners, proof banners, brand trust banners, QA boards, and review/evidence boards.

2. API-generated banner/image components
   - Use image-reference plus prompt generation for backgrounds, moods, people/category scenes, and product contexts.
   - Do not rely on the model for final small text, parameters, review cards, service promises, or precise product identity.
   - Default production route: AI background plus deterministic local composite.

3. Agent and validation workflow
   - Input audit -> ProductTruthPack -> buyer-question route -> module plan -> image requirements -> render -> validate -> review/repair.
   - Hard structure belongs in schemas, validators, fixtures, and evals.
   - Judgment-heavy decisions belong in Skill/SOP and DesignMD-style guidance.

## First Imported Notes

- [Current Retention Map](docs/2026-05-25-current-retention-map.md)
- [Repo Collaboration Plan](docs/repo-collaboration-plan.md)

## First Agent Package

- [EXCITAT eMAG Detail Agent](packages/excitat-emag-detail-agent/README.md)

Validate the package structure:

```bash
npm run validate:excitat-emag-detail-agent
```

## Initial Source Workspaces

- `/Users/cc/Desktop/photo_show`: current research, scripts, catalogs, references, and generated outputs.
- `/Users/cc/projects/agent-platform`: runtime/Agent/Skill/Task/Guard platform that should later host packaged agents and skills.

## Production Rule

Use AI for scene, mood, and background. Use deterministic local composition for final text, brand tags, parameters, QA, review cards, service cues, product placement, and validation artifacts.
