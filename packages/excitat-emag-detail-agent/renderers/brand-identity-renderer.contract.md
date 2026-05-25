# Brand Identity Renderer Contract

Input:

- brand text
- brand variant id
- background mode: transparent, dark, light
- output mode: PNG, SVG, GIF, WebP, or HTML image embed

Output:

- brand asset path
- media asset record
- compatibility notes

Requirements:

- Brand text is locally rendered, never model-generated.
- Every output declares exact dimensions and background compatibility.
- Animated variants must also export a static fallback.
