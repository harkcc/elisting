# Real Product Component Application Analysis

## What Stayed Locked

- The source product remains the NexusTech `D6MHW43BM` EV charging cable.
- The original 13 detail images are kept in the same order.
- No original banner/detail image is replaced, cropped, recolored, or used as a noisy component background.
- No image-generation job is introduced.

## Where GIF Components Were Added

1. After the first original banner/detail image: `rank_number_strip`.
   - Purpose: define the reading order before the buyer enters detailed images.
   - Why here: first image is a broad introduction, so a small white-card guide can help without changing the banner.

2. After the early compatibility images: `corner_badge_shine`.
   - Purpose: make the plain product facts feel more like a controlled brand module.
   - Why here: brand label stays small and supports the text instead of becoming a second banner.

3. After the power/spec detail images: `proof_check_chip`.
   - Purpose: convert title facts into a scan-friendly evidence row.
   - Why here: 22kW, 32A, 5m, and IP65 are product-title facts, so the module can be deterministic.

4. After the mid-page product detail images: `motion_soft_glow_border`.
   - Purpose: add one slow, quiet motion note for usage context.
   - Why here: this is a manual/explanation moment, where slow motion feels more premium than a fast effect.

## Open Design Rules Used

- Design first, component second, motion last.
- 70/20/8/2 color balance: mostly neutral surfaces, small accent, minimal motion.
- One purpose per module: every component answers a buyer question.
- White-card micro components are preferred when the original listing already has strong image banners.
- Slow motion is used for premium/manual moments; fast looping motion is avoided.
- No fake proof: chips only use facts found in the product title or captured source.

## Scale Rule Learned

For this type of existing listing, the Agent should not rebuild the page. It should:

1. Lock the original media sequence.
2. Classify nearby buyer question: fit, power, use, package, trust, proof.
3. Select the smallest component that improves scanability.
4. Add Reference, Assist, and Guard for the chosen component.
5. Verify image order, mobile width, and claim safety.
6. Export only if the component improves hierarchy.
