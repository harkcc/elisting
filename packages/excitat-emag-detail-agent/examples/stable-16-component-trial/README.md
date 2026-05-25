# Stable 16 Component Trial

This folder renders the first 16 motion / label components as independent
library candidates.

The purpose is confirmation, not final SKU delivery:

- each component is visible as a separate GIF/PNG asset
- each component has an eMAG-safe `<p><img></p>` embed
- the visual base is intentionally clean black-gold / dark / low-noise
- product imagery is only used as a small inset when useful

Open:

```text
examples/stable-16-component-trial/stable-16-component-trial.html
```

Library definitions:

```text
data/stable-16-gif-library.json
```

Renderer:

```bash
/Users/cc/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  packages/excitat-emag-detail-agent/renderers/stable-16-component-renderer.py \
  --source /Users/cc/Desktop/photo_show/output/emag_exit_two_product_stable_components_v4/assets/D6MHW43BM/03.jpg \
  --out packages/excitat-emag-detail-agent/examples/stable-16-component-trial
```

Validation:

```bash
python3 packages/excitat-emag-detail-agent/validators/validate-emag-detail-html.py \
  packages/excitat-emag-detail-agent/examples/stable-16-component-trial/stable-16-component-trial.html \
  --out packages/excitat-emag-detail-agent/examples/stable-16-component-trial/validation_report.json
```

