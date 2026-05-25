# OpenAI GPT Image Provider Profile

Provider id: `openai_gpt_image`

Use for:

- controlled image generation or editing with strong prompt structure
- reference-image driven commercial backgrounds
- iterative repair when a candidate is close but needs layout or style correction

Default route:

- `background_only`
- `image_to_image`
- `edit`

Rules:

- Treat generated text as non-production unless explicitly verified and still locally replaceable.
- Prefer no-text backgrounds with reserved product/text zones.
- Use deterministic overlay for brand, headline, parameter, icon, and service text.
- Write provider, model, prompt hash, reference refs, and candidate id into `media-asset-index.json`.
