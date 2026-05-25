#!/usr/bin/env python3
"""Render the first 16 stable component trials as eMAG-embeddable media."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


W, H = 1140, 360
FRAMES = 12
GOLD = (246, 182, 55)
BLUE = (38, 169, 255)
ORANGE = (255, 118, 24)
GREEN = (48, 196, 119)
PAPER = (250, 251, 253)
DARK = (10, 14, 20)
INK = (24, 30, 39)


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


FXL = font(72, True)
FLG = font(42, True)
FMD = font(28, True)
FSM = font(21, False)
FXS = font(17, False)


def clean_dark() -> Image.Image:
    im = Image.new("RGBA", (W, H), DARK + (255,))
    d = ImageDraw.Draw(im)
    for x in range(0, W, 80):
        d.line((x, 0, x - 180, H), fill=(28, 35, 46, 90), width=1)
    d.rectangle((0, H - 8, W, H), fill=GOLD + (255,))
    return im


def product_inset(source: Path | None, size=(360, 250)) -> Image.Image:
    if not source or not source.exists():
        im = Image.new("RGBA", size, (24, 30, 40, 255))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((28, 60, size[0] - 28, size[1] - 60), radius=18, outline=(120, 132, 148), width=4)
        d.text((70, 105), "PRODUCT", fill=(180, 190, 204), font=FMD)
        return im
    raw = Image.open(source).convert("RGB")
    scale = max(size[0] / raw.width, size[1] / raw.height)
    resized = raw.resize((int(raw.width * scale), int(raw.height * scale)), Image.LANCZOS)
    left = max(0, (resized.width - size[0]) // 2)
    top = max(0, (resized.height - size[1]) // 2)
    crop = resized.crop((left, top, left + size[0], top + size[1])).convert("RGBA")
    shade = Image.new("RGBA", size, (5, 8, 12, 105))
    crop = Image.alpha_composite(crop, shade)
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0], size[1]), radius=18, fill=255)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.paste(crop, (0, 0), mask)
    return out


def icon(draw: ImageDraw.ImageDraw, cx: int, cy: int, kind: str, color=ORANGE) -> None:
    draw.ellipse((cx - 34, cy - 34, cx + 34, cy + 34), fill=color)
    white = (255, 255, 255)
    if kind == "bolt":
        draw.polygon([(cx, cy - 25), (cx - 18, cy + 2), (cx - 4, cy + 2), (cx - 12, cy + 26), (cx + 20, cy - 8), (cx + 5, cy - 8)], fill=white)
    elif kind == "shield":
        pts = [(cx, cy - 24), (cx + 22, cy - 12), (cx + 16, cy + 18), (cx, cy + 30), (cx - 16, cy + 18), (cx - 22, cy - 12)]
        draw.line(pts + [pts[0]], fill=white, width=4)
        draw.line((cx - 10, cy + 2, cx - 2, cy + 12, cx + 16, cy - 12), fill=white, width=5)
    elif kind == "package":
        draw.rectangle((cx - 22, cy - 16, cx + 22, cy + 22), outline=white, width=4)
        draw.line((cx, cy - 16, cx, cy + 22), fill=white, width=3)
        draw.line((cx - 22, cy - 2, cx + 22, cy - 2), fill=white, width=3)
    else:
        draw.arc((cx - 24, cy - 8, cx + 18, cy + 28), 190, 350, fill=white, width=5)
        draw.rectangle((cx + 12, cy - 24, cx + 28, cy - 10), outline=white, width=4)


def shimmer_layer(i: int, color=GOLD) -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x = int(-260 + i * (W + 520) / (FRAMES - 1))
    d.polygon([(x, -80), (x + 90, -80), (x + 360, H + 80), (x + 270, H + 80)], fill=color + (95,))
    return layer.filter(ImageFilter.GaussianBlur(5))


def save_gif(frames: list[Image.Image], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pal = [f.convert("P", palette=Image.Palette.ADAPTIVE, colors=128) for f in frames]
    pal[0].save(path, save_all=True, append_images=pal[1:], duration=110, loop=0, optimize=True)


def save_png(frame: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.convert("RGB").save(path, optimize=True, quality=90)


def title_block(draw: ImageDraw.ImageDraw, title: str, subtitle: str, color=GOLD):
    draw.text((70, 72), title, fill=(255, 255, 255), font=FLG)
    draw.text((72, 132), subtitle, fill=(222, 229, 238), font=FSM)
    draw.rounded_rectangle((70, 188, 360, 238), radius=12, outline=color, width=3)
    draw.text((92, 200), "stable media component", fill=color, font=FXS)


def component_frames(component_id: str, source: Path | None) -> tuple[str, list[Image.Image], str, list[str]]:
    frames: list[Image.Image] = []
    if component_id in {"motion_shine_sweep_gold", "motion_shine_sweep_blue"}:
        color = GOLD if component_id.endswith("gold") else BLUE
        for i in range(FRAMES):
            im = clean_dark()
            d = ImageDraw.Draw(im)
            title_block(d, "EXCITAT", "Black-gold banner base" if color == GOLD else "Blue tech banner base", color)
            inset = product_inset(source)
            im.alpha_composite(inset, (700, 58))
            d.rounded_rectangle((690, 48, 1070, 318), radius=24, outline=color, width=3)
            im = Image.alpha_composite(im, shimmer_layer(i, color))
            frames.append(im)
        return "gif", frames, "Banner / brand trust", ["use_clean_dark_or_gold_base", "product_only_as_inset", "no_css_motion"]

    if component_id in {"motion_step_highlight_3", "motion_step_highlight_4", "rank_number_strip"}:
        count = 3 if component_id.endswith("_3") else 4
        if component_id == "rank_number_strip":
            count = 4
        for i in range(FRAMES):
            im = clean_dark()
            d = ImageDraw.Draw(im)
            d.text((58, 48), "1 2 3 4 Reading Order", fill=(255, 255, 255), font=FMD)
            gap = 22
            box_w = (W - 116 - gap * (count - 1)) // count
            active = i % count
            for idx in range(count):
                x0 = 58 + idx * (box_w + gap)
                x1 = x0 + box_w
                outline = GOLD if idx == active else (118, 130, 146)
                fill = (28, 36, 48, 255)
                d.rounded_rectangle((x0, 112, x1, 292), radius=18, fill=fill, outline=outline, width=5 if idx == active else 2)
                d.ellipse((x0 + 24, 134, x0 + 78, 188), fill=outline)
                d.text((x0 + 45, 146), str(idx + 1), fill=(15, 18, 24), font=FSM)
                d.text((x0 + 28, 218), ["Fit", "Power", "Proof", "Care"][idx], fill=(255, 255, 255), font=FMD)
            frames.append(im)
        return "gif", frames, "1234 sequence / key points", ["max_four_points", "short_labels", "mobile_readable"]

    if component_id == "motion_pulse_dot":
        for i in range(FRAMES):
            im = Image.new("RGBA", (W, H), PAPER + (255,))
            d = ImageDraw.Draw(im)
            d.text((68, 70), "Pulse Dot Marker", fill=INK, font=FLG)
            d.text((70, 130), "Use inside feature rows, not as a full hero.", fill=(86, 96, 110), font=FSM)
            r = 22 + int(24 * (0.5 + 0.5 * math.sin(i / FRAMES * math.tau)))
            d.ellipse((650 - r, 175 - r, 650 + r, 175 + r), outline=GREEN + (120,), width=4)
            d.ellipse((628, 153, 672, 197), fill=GREEN)
            frames.append(im)
        return "gif", frames, "Micro marker", ["must_have_meaning", "not_standalone_decoration", "small_motion_only"]

    if component_id == "motion_scan_line":
        for i in range(FRAMES):
            im = clean_dark()
            d = ImageDraw.Draw(im)
            d.text((70, 58), "Technical Scan", fill=(255, 255, 255), font=FLG)
            d.rounded_rectangle((70, 142, 1030, 284), radius=18, outline=BLUE, width=3)
            for x in range(90, 1020, 38):
                d.line((x, 154, x, 272), fill=(52, 90, 122), width=1)
            sx = 90 + int(i * 900 / (FRAMES - 1))
            d.rectangle((sx, 142, sx + 80, 284), fill=BLUE + (70,))
            frames.append(im)
        return "gif", frames, "Technical proof / scan", ["tie_to_real_detail", "no_fake_quality_claim", "avoid_text_zones"]

    if component_id == "motion_soft_glow_border":
        for i in range(FRAMES):
            im = clean_dark()
            d = ImageDraw.Draw(im)
            pulse = int(2 + 8 * (0.5 + 0.5 * math.sin(i / FRAMES * math.tau)))
            d.rounded_rectangle((72, 70, 1068, 290), radius=28, outline=GOLD, width=3 + pulse)
            d.text((122, 120), "Soft Trust Card", fill=(255, 255, 255), font=FLG)
            d.text((124, 184), "Low motion, high readability.", fill=(224, 232, 240), font=FSM)
            frames.append(im)
        return "gif", frames, "Trust / notice", ["one_glow_block_per_screen", "no_fake_badge", "text_first"]

    if component_id == "motion_progress_fill":
        for i in range(FRAMES):
            im = Image.new("RGBA", (W, H), PAPER + (255,))
            d = ImageDraw.Draw(im)
            d.text((68, 58), "Progress / Selection", fill=INK, font=FLG)
            for row, label in enumerate(["Choose", "Check", "Use"]):
                y = 140 + row * 58
                d.text((86, y - 8), label, fill=(38, 45, 56), font=FSM)
                d.rounded_rectangle((240, y, 960, y + 22), radius=12, fill=(225, 231, 238))
                width = int((260 + row * 140 + i * 38) % 720)
                d.rounded_rectangle((240, y, 240 + max(90, width), y + 22), radius=12, fill=GREEN if row == 2 else BLUE)
            frames.append(im)
        return "gif", frames, "Process / selection", ["not_a_performance_metric", "explain_process_only", "short_labels"]

    if component_id == "motion_before_after_wipe":
        for i in range(FRAMES):
            im = Image.new("RGBA", (W, H), (232, 236, 241, 255))
            d = ImageDraw.Draw(im)
            x = int(240 + i * 660 / (FRAMES - 1))
            d.rectangle((0, 0, x, H), fill=(38, 44, 54))
            d.rectangle((x, 0, W, H), fill=(233, 247, 239))
            d.line((x, 0, x, H), fill=(255, 255, 255), width=5)
            d.text((70, 84), "Before / After", fill=(255, 255, 255), font=FLG)
            d.text((70, 150), "Only with evidence", fill=GOLD, font=FMD)
            frames.append(im)
        return "gif", frames, "Comparison", ["requires_evidence", "no_fake_result", "block_without_before_after_source"]

    if component_id == "motion_radar_ping":
        for i in range(FRAMES):
            im = clean_dark()
            d = ImageDraw.Draw(im)
            d.text((70, 64), "Focus Area", fill=(255, 255, 255), font=FLG)
            cx, cy = 770, 180
            radius = 44 + int(78 * i / (FRAMES - 1))
            d.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=BLUE, width=4)
            d.ellipse((cx - 36, cy - 36, cx + 36, cy + 36), fill=BLUE)
            frames.append(im)
        return "gif", frames, "Focus marker", ["must_point_to_real_detail", "avoid_large_overlay", "not_for_fake_claims"]

    if component_id == "brand_wordmark_shine":
        for i in range(FRAMES):
            im = clean_dark()
            d = ImageDraw.Draw(im)
            d.text((72, 104), "EXCITAT", fill=GOLD, font=FXL)
            d.text((78, 190), "brand side label", fill=(255, 255, 255), font=FMD)
            im = Image.alpha_composite(im, shimmer_layer(i, GOLD))
            frames.append(im)
        return "gif", frames, "Brand identity", ["brand_text_local_only", "no_marketplace_logo", "spelling_guard"]

    if component_id == "corner_badge_shine":
        for i in range(FRAMES):
            im = Image.new("RGBA", (W, H), PAPER + (255,))
            d = ImageDraw.Draw(im)
            d.rounded_rectangle((64, 62, 1076, 298), radius=24, fill=(16, 23, 34), outline=(214, 221, 231), width=2)
            d.polygon([(64, 62), (280, 62), (64, 236)], fill=GOLD)
            d.text((82, 86), "X-City", fill=(12, 16, 24), font=FMD)
            d.text((350, 132), "Corner brand label", fill=(255, 255, 255), font=FLG)
            im = Image.alpha_composite(im, shimmer_layer(i, GOLD))
            frames.append(im)
        return "gif", frames, "Corner brand tag", ["not_certification", "brand_or_collection_only", "no_fake_badge"]

    if component_id == "e2_marker_chip":
        im = Image.new("RGBA", (W, H), PAPER + (255,))
        d = ImageDraw.Draw(im)
        d.text((70, 68), "E2 Marker Chip", fill=INK, font=FLG)
        d.rounded_rectangle((70, 150, 330, 230), radius=18, fill=(14, 24, 36), outline=GOLD, width=3)
        d.text((106, 168), "E2", fill=GOLD, font=FMD)
        d.text((170, 170), "module marker", fill=(255, 255, 255), font=FSM)
        return "png", [im], "Marker / component state", ["defined_meaning_only", "not_customer_claim", "not_certification"]

    if component_id == "proof_check_chip":
        im = Image.new("RGBA", (W, H), PAPER + (255,))
        d = ImageDraw.Draw(im)
        d.text((70, 54), "Proof Chips", fill=INK, font=FLG)
        for idx, label in enumerate(["Source", "Spec", "Image"]):
            x = 80 + idx * 330
            d.rounded_rectangle((x, 146, x + 260, 232), radius=16, fill=(255, 255, 255), outline=(211, 220, 230), width=2)
            d.ellipse((x + 24, 168, x + 62, 206), fill=GREEN)
            d.line((x + 34, 187, x + 43, 197, x + 56, 176), fill=(255, 255, 255), width=4)
            d.text((x + 82, 174), label, fill=INK, font=FMD)
        return "png", [im], "Evidence chip row", ["must_link_evidence", "no_reviews_without_source", "no_fake_certification"]

    if component_id == "package_count_pulse":
        for i in range(FRAMES):
            im = clean_dark()
            d = ImageDraw.Draw(im)
            d.text((70, 58), "Package Count", fill=(255, 255, 255), font=FLG)
            for idx in range(3):
                x = 540 + idx * 150
                y = 130 + int(6 * math.sin((i + idx) / FRAMES * math.tau))
                icon(d, x, y, "package", GOLD)
                d.text((x - 10, y + 54), str(idx + 1), fill=(255, 255, 255), font=FMD)
            frames.append(im)
        return "gif", frames, "Package contents", ["quantity_must_match_source", "no_shipping_claim", "short_labels"]

    raise ValueError(component_id)


COMPONENTS = [
    "motion_shine_sweep_gold",
    "motion_shine_sweep_blue",
    "motion_step_highlight_3",
    "motion_step_highlight_4",
    "motion_pulse_dot",
    "motion_scan_line",
    "motion_soft_glow_border",
    "motion_progress_fill",
    "motion_before_after_wipe",
    "motion_radar_ping",
    "brand_wordmark_shine",
    "corner_badge_shine",
    "e2_marker_chip",
    "rank_number_strip",
    "proof_check_chip",
    "package_count_pulse",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--source", type=Path, default=None)
    args = parser.parse_args()

    out = args.out
    assets = out / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    records = []
    for cid in COMPONENTS:
        typ, frames, usage, guard = component_frames(cid, args.source)
        ext = "gif" if typ == "gif" else "png"
        file = f"{cid}.{ext}"
        path = assets / file
        if typ == "gif":
            save_gif(frames, path)
        else:
            save_png(frames[0], path)
        records.append(
            {
                "component_id": cid,
                "file": f"assets/{file}",
                "output_type": typ,
                "usage": usage,
                "guard": guard,
                "html": f'<p data-component-id="{cid}" data-edit-id="trial-{cid}" style="text-align:center;margin:0 0 16px;"><img src="assets/{file}" width="1140" alt="{usage}" style="max-width:100%;height:auto;"></p>',
            }
        )

    (out / "component_trial_report.json").write_text(json.dumps({"components": records}, indent=2), encoding="utf-8")
    snippet = [
        '<h2 style="text-align:center;">Stable 16 Component Trial Gallery</h2>',
        '<p style="text-align:center;"><strong>Rule:</strong> clean black-gold or low-noise base; product image only as inset when needed.</p>',
    ]
    for record in records:
        snippet.append(record["html"])
    (out / "stable-16-component-trial.html").write_text("\n".join(snippet) + "\n", encoding="utf-8")
    print(json.dumps({"count": len(records), "out": str(out)}, indent=2))


if __name__ == "__main__":
    main()

