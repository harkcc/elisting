# Image Workflow

This workflow produces image assets for premium detail-page modules. It is separate from the component library.

Supported providers:

- OpenAI GPT Image / image model
- NanoBanana2

Unsupported providers:

- ComfyUI

Pipeline:

```text
ImageIntent
-> ReferencePack
-> PromptPlan
-> ProviderSelection
-> GenerateCandidates
-> VisualQA
-> RepairPrompt
-> ApprovedAsset
```

The image model creates backgrounds, mood, lighting, scenes, composition, and style transfer. Deterministic composition adds final product, exact text, brand, numbers, icons, claims, QA, and review cards.
