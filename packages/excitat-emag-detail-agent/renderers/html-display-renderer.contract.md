# HTML Display Renderer Contract

Input:

- `component_id`
- `data_edit_id`
- `ProductTruthPack`
- selected buyer-question copy
- style tokens from `DESIGN.md`

Output:

- eMAG-safe HTML snippet
- validation notes
- optional media asset refs

Requirements:

- Root element includes `data-component-id` and `data-edit-id`.
- Text must be short enough for 390px preview.
- Unsupported tags, scripts, iframe, forms, and external CSS are blocked.
