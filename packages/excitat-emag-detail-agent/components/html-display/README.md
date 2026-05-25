# HTML Display Components

These components render directly into eMAG-safe HTML. They are used by both `stable_listing` and `premium_listing`.

Initial stable candidates:

- `first_screen_anchor_triplet`
- `buyer_question_answer_block`
- `faq_objection_closer`
- `color_band_feature_stack`
- `spec_table_clean`
- `package_and_usage`

Rules:

- One component answers one buyer question.
- Use simple tags and inline styles only.
- Every final root node must carry `data-edit-id` and `data-component-id` when rendered into preview HTML.
- Avoid internal SOP language in customer-facing copy.
- Keep text readable at 390px preview width.
