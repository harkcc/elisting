# D6MHW43BM Component Application Demo

This demo promotes the earlier D6MHW43BM stable component run into the `elisting` package as a reviewable example.

It demonstrates the production-safe route:

- pre-rendered GIF/PNG assets
- simple HTML image embeds
- `data-component-id` and `data-edit-id` on every module wrapper
- no image generation
- eMAG detail validator report stored beside the demo

Open:

```text
examples/d6mhw43bm-component-application/demo.html
```

Benchmark-push variant:

```text
examples/d6mhw43bm-component-application/benchmark-push-demo.html
```

This variant intentionally uses the stronger live-store pattern: colored
background bands, table layout, small image icons, and embedded GIF media.

Validation:

```bash
python3 packages/excitat-emag-detail-agent/validators/validate-emag-detail-html.py \
  packages/excitat-emag-detail-agent/examples/d6mhw43bm-component-application/demo.html \
  --out packages/excitat-emag-detail-agent/examples/d6mhw43bm-component-application/validation_report.json
```

```bash
python3 packages/excitat-emag-detail-agent/validators/validate-emag-detail-html.py \
  packages/excitat-emag-detail-agent/examples/d6mhw43bm-component-application/benchmark-push-demo.html \
  --out packages/excitat-emag-detail-agent/examples/d6mhw43bm-component-application/benchmark_push_validation_report.json
```
