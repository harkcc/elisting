# Banner Composite Components

Banner components are image or GIF modules embedded into the detail page. They may use existing assets, deterministic composition, or generated backgrounds depending on route policy.

Initial families:

- product-tech hero
- warm/soft category hero
- brand trust banner
- QA board
- review evidence board
- proof crop banner
- step/process banner
- brand closer

Rules:

- Stable route uses existing assets and deterministic composition only.
- Premium route may consume approved image jobs, but final text and brand marks remain deterministic.
- Every banner must write a media asset record with source, dimensions, usage, evidence refs, and QA status.
- Review/testimonial banners require sourced review evidence or must be marked preview.
