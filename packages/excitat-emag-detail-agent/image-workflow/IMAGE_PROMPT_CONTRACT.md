# Image Prompt Contract

## Purpose

Make image generation stable enough to become a reusable production step.

## Model May Generate

- background
- atmosphere
- lighting
- scene
- composition variation
- reference-banner style rhythm
- empty text zones

## Model Must Not Generate

- final readable text
- EXCITAT / X-City brand text
- parameter numbers
- review names, ratings, dates, or stars
- warranty, return, shipping, or service promises
- marketplace logos, platform badges, or fake endorsements
- precise product facts
- distorted product structure

## Required Prompt Slots

Each prompt pattern must declare:

- `image_type`
- `generation_route`
- `reference_roles`
- `scene_goal`
- `composition_goal`
- `reserved_text_zone`
- `brand_policy`
- `product_policy`
- `negative_constraints`
- `post_process`

## Default Negative Constraints

Use these unless a provider profile overrides wording:

```text
no readable text, no fake badge, no marketplace logo, no warranty claim,
no shipping or return promise, no distorted product, no crowded layout,
no tiny labels, no copied official marketplace asset
```

## Approval Rule

Generated images are candidates only. They become approved assets after Visual QA and deterministic post-processing.
