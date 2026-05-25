# Motion Renderer Contract

Input:

- source static image or canvas definition
- motion component id
- frame count and duration
- output format: GIF or WebP

Output:

- animated asset path
- static first-frame preview path
- media asset record
- QA notes

Requirements:

- Product geometry must not change.
- First frame must be acceptable as a static fallback.
- Motion must be subtle enough for mobile detail-page reading.
