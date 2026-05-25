#!/usr/bin/env python3
"""Deterministic image-adapted GIF component renderer.

This renderer is intentionally simple: it adapts motion components to a source
product image, then exports GIF/PNG assets that can be embedded with eMAG-safe
HTML. It does not generate product structure or marketplace claims.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


W, H = 1140, 456
FRAME_COUNT = 10


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        if path and Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


FONT_XL = font(64, True)
FONT_LG = font(36, True)
FONT_MD = font(26, True)
FONT_SM = font(20, False)
FONT_XS = font(16, False)


def cover_image(path: Path, size: tuple[int, int] = (W, H)) -> Image.Image:
    img = Image.open(path).convert("RGB")
    iw, ih = img.size
    scale = max(size[0] / iw, size[1] / ih)
    resized = img.resize((int(iw * scale), int(ih * scale)), Image.LANCZOS)
    left = max(0, (resized.width - size[0]) // 2)
    top = max(0, (resized.height - size[1]) // 2)
    return resized.crop((left, top, left + size[0], top + size[1]))


def average_color(img: Image.Image) -> tuple[int, int, int]:
    small = img.resize((1, 1), Image.Resampling.BILINEAR)
    return small.getpixel((0, 0))


def accent_from_image(img: Image.Image) -> tuple[int, int, int]:
    r, g, b = average_color(img)
    if b >= max(r, g):
        return (36, 169, 255)
    if r > g:
        return (255, 139, 34)
    return (46, 198, 126)


def dark_base(src: Image.Image) -> Image.Image:
    base = ImageEnhance.Contrast(src).enhance(1.1)
    overlay = Image.new("RGBA", (W, H), (5, 12, 20, 150))
    return Image.alpha_composite(base.convert("RGBA"), overlay)


def draw_text_block(draw: ImageDraw.ImageDraw, title: str, subtitle: str, accent: tuple[int, int, int]) -> None:
    draw.rounded_rectangle((56, 58, 520, 282), radius=18, fill=(7, 12, 18, 208), outline=accent, width=4)
    draw.text((86, 88), title, fill=(255, 255, 255), font=FONT_LG)
    draw.text((88, 146), subtitle, fill=(220, 230, 239), font=FONT_SM)
    chips = ["FIT", "POWER", "CARE"]
    values = ["Type 2", "22kW", "Daily"]
    x = 86
    for chip, value in zip(chips, values):
        draw.rounded_rectangle((x, 210, x + 118, 260), radius=8, fill=(255, 255, 255, 235), outline=accent, width=2)
        draw.text((x + 12, 216), chip, fill=accent, font=FONT_XS)
        draw.text((x + 12, 236), value, fill=(20, 27, 36), font=FONT_XS)
        x += 138


def icon(draw: ImageDraw.ImageDraw, cx: int, cy: int, kind: str, fill: tuple[int, int, int]) -> None:
    draw.ellipse((cx - 34, cy - 34, cx + 34, cy + 34), fill=fill)
    white = (255, 255, 255)
    if kind == "bolt":
        pts = [(cx + 2, cy - 26), (cx - 18, cy + 4), (cx - 2, cy + 4), (cx - 10, cy + 28), (cx + 20, cy - 8), (cx + 4, cy - 8)]
        draw.polygon(pts, fill=white)
    elif kind == "shield":
        pts = [(cx, cy - 24), (cx + 22, cy - 12), (cx + 16, cy + 18), (cx, cy + 30), (cx - 16, cy + 18), (cx - 22, cy - 12)]
        draw.line(pts + [pts[0]], fill=white, width=4)
        draw.line((cx - 10, cy + 2, cx - 2, cy + 12, cx + 16, cy - 12), fill=white, width=5)
    else:
        draw.arc((cx - 24, cy - 12, cx + 18, cy + 28), 190, 350, fill=white, width=5)
        draw.rectangle((cx + 12, cy - 24, cx + 28, cy - 10), outline=white, width=4)
        draw.line((cx + 12, cy - 10, cx - 2, cy + 2), fill=white, width=4)


def save_gif(frames: list[Image.Image], path: Path, duration: int = 120) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    paletted = [frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=128) for frame in frames]
    paletted[0].save(path, save_all=True, append_images=paletted[1:], duration=duration, loop=0, optimize=True)


def save_png(frame: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.convert("RGB").save(path, optimize=True, quality=88)


def shine_sweep(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    for i in range(FRAME_COUNT):
        frame = dark_base(src)
        draw = ImageDraw.Draw(frame)
        draw_text_block(draw, "Image-fit hero", "Text first. Motion last.", accent)
        sweep = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(sweep)
        x = int(-280 + i * (W + 560) / (FRAME_COUNT - 1))
        sd.polygon([(x, -80), (x + 120, -80), (x + 400, H + 80), (x + 280, H + 80)], fill=(*accent, 84))
        frame = Image.alpha_composite(frame, sweep.filter(ImageFilter.GaussianBlur(8)))
        frames.append(frame)
    return frames


def icon_sequence(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    labels = [("Fit", "cable"), ("Power", "bolt"), ("Care", "shield")]
    frames = []
    for i in range(FRAME_COUNT):
        frame = Image.new("RGBA", (W, H), (12, 28, 43, 255))
        draw = ImageDraw.Draw(frame)
        for idx, (label, kind) in enumerate(labels):
            x0 = idx * W // 3
            x1 = (idx + 1) * W // 3
            active = idx == (i // 3) % 3
            bg = (18, 43, 63, 255) if active else (14, 31, 48, 255)
            draw.rectangle((x0, 0, x1, H), fill=bg, outline=(55, 82, 104), width=2)
            color = accent if active else (255, 118, 24)
            icon(draw, (x0 + x1) // 2, 126, kind, color)
            draw.text(((x0 + x1) // 2 - 10, 190), str(idx + 1), fill=(255, 255, 255), font=FONT_MD)
            draw.text(((x0 + x1) // 2 - 70, 246), label, fill=(255, 255, 255), font=FONT_LG)
        frames.append(frame)
    return frames


def border_breathing(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    for i in range(FRAME_COUNT):
        pulse = int(70 + 110 * (0.5 + 0.5 * math.sin(i / FRAME_COUNT * math.tau)))
        frame = dark_base(src)
        draw = ImageDraw.Draw(frame)
        draw.rounded_rectangle((44, 38, W - 44, H - 38), radius=22, outline=(*accent, pulse), width=8)
        draw.text((80, 84), "Stable proof board", fill=(255, 255, 255), font=FONT_LG)
        draw.text((82, 138), "Use background color, icons and GIF only after text is locked.", fill=(224, 232, 240), font=FONT_SM)
        frames.append(frame)
    return frames


def edge_glow(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    for i in range(FRAME_COUNT):
        frame = dark_base(src)
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        alpha = int(55 + 95 * (0.5 + 0.5 * math.sin(i / FRAME_COUNT * math.tau)))
        gd.rounded_rectangle((610, 72, 1050, 380), radius=22, outline=(*accent, alpha), width=12)
        frame = Image.alpha_composite(frame, glow.filter(ImageFilter.GaussianBlur(8)))
        ImageDraw.Draw(frame).rounded_rectangle((610, 72, 1050, 380), radius=22, outline=(*accent, 230), width=3)
        frames.append(frame)
    return frames


def light_streak(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    for i in range(FRAME_COUNT):
        frame = dark_base(src)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        x = int(-180 + i * (W + 360) / (FRAME_COUNT - 1))
        ld.line((x, H + 20, x + 380, -30), fill=(*accent, 120), width=24)
        ld.line((x + 44, H + 20, x + 424, -30), fill=(255, 255, 255, 55), width=8)
        frame = Image.alpha_composite(frame, layer.filter(ImageFilter.GaussianBlur(5)))
        ImageDraw.Draw(frame).text((70, 78), "Color-adapted banner", fill=(255, 255, 255), font=FONT_LG)
        frames.append(frame)
    return frames


def dotted_twinkle(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    dots = [(80 + (j * 73) % 460, 44 + (j * 41) % 340, 2 + (j % 4)) for j in range(42)]
    for i in range(FRAME_COUNT):
        frame = dark_base(src)
        draw = ImageDraw.Draw(frame)
        for j, (x, y, r) in enumerate(dots):
            alpha = 45 + ((i * 27 + j * 17) % 140)
            draw.ellipse((x - r, y - r, x + r, y + r), fill=(*accent, alpha))
        draw_text_block(draw, "Brand texture", "Small motion. Stable media.", accent)
        frames.append(frame)
    return frames


def step_highlight(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    boxes = [(54, 54, 350, 184), (422, 54, 718, 184), (790, 54, 1086, 184), (54, 238, 1086, 398)]
    for i in range(FRAME_COUNT):
        frame = dark_base(src)
        draw = ImageDraw.Draw(frame)
        active = i % 4
        for idx, box in enumerate(boxes):
            color = accent if idx == active else (226, 232, 240)
            width = 8 if idx == active else 3
            draw.rounded_rectangle(box, radius=14, outline=color, width=width)
            draw.ellipse((box[0] + 16, box[1] + 16, box[0] + 62, box[1] + 62), fill=color)
            draw.text((box[0] + 33, box[1] + 24), str(idx + 1), fill=(255, 255, 255) if idx == active else accent, font=FONT_SM)
        frames.append(frame)
    return frames


def before_after(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    gray = ImageEnhance.Color(src).enhance(0.0).convert("RGBA")
    color = ImageEnhance.Color(src).enhance(1.25).convert("RGBA")
    frames = []
    for i in range(FRAME_COUNT):
        x = int(W * (0.18 + 0.64 * i / (FRAME_COUNT - 1)))
        frame = gray.copy()
        frame.paste(color.crop((0, 0, x, H)), (0, 0))
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 65))
        frame = Image.alpha_composite(frame, overlay)
        draw = ImageDraw.Draw(frame)
        draw.line((x, 0, x, H), fill=(255, 255, 255), width=5)
        draw.text((70, 70), "Comparison needs evidence", fill=(255, 255, 255), font=FONT_LG)
        draw.text((72, 124), "Use only when the source supports the claim.", fill=(230, 236, 242), font=FONT_SM)
        frames.append(frame)
    return frames


def magnifier(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    focus = src.crop((670, 120, 930, 380)).resize((320, 320), Image.LANCZOS)
    mask = Image.new("L", (320, 320), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 320, 320), fill=255)
    for i in range(FRAME_COUNT):
        frame = dark_base(src)
        pulse = int(3 + 8 * (0.5 + 0.5 * math.sin(i / FRAME_COUNT * math.tau)))
        frame.paste(focus, (720, 70), mask)
        draw = ImageDraw.Draw(frame)
        draw.ellipse((720, 70, 1040, 390), outline=accent, width=6 + pulse)
        draw.line((972, 322, 1080, 430), fill=accent, width=14)
        draw.text((70, 82), "Detail focus", fill=(255, 255, 255), font=FONT_LG)
        frames.append(frame)
    return frames


def parcel_motion(src: Image.Image, accent: tuple[int, int, int]) -> list[Image.Image]:
    frames = []
    for i in range(FRAME_COUNT):
        frame = Image.new("RGBA", (W, H), (12, 12, 14, 255))
        draw = ImageDraw.Draw(frame)
        draw_text_block(draw, "Brand closer", "Package and care module.", accent)
        x = 760 + int(8 * math.sin(i / FRAME_COUNT * math.tau))
        y = 118
        draw.rounded_rectangle((x, y, x + 220, y + 170), radius=10, fill=(178, 124, 74), outline=(226, 175, 112), width=3)
        draw.line((x + 110, y, x + 110, y + 170), fill=(128, 86, 48), width=3)
        draw.line((x, y + 58, x + 220, y + 58), fill=(128, 86, 48), width=3)
        draw.arc((x - 160, y - 50, x + 330, y + 236), 200, 320, fill=(*accent, 190), width=5)
        frames.append(frame)
    return frames


def brand_side_tag(src: Image.Image, accent: tuple[int, int, int]) -> Image.Image:
    frame = dark_base(src)
    draw = ImageDraw.Draw(frame)
    draw.rounded_rectangle((42, 68, 340, 388), radius=22, fill=(5, 9, 14, 226), outline=accent, width=4)
    draw.text((78, 114), "EXCITAT", fill=(255, 184, 49), font=FONT_XL)
    draw.text((80, 198), "Image-adapted", fill=(255, 255, 255), font=FONT_MD)
    draw.text((82, 242), "brand label", fill=(225, 233, 241), font=FONT_SM)
    return frame


def e2_marker(src: Image.Image, accent: tuple[int, int, int]) -> Image.Image:
    frame = Image.new("RGBA", (W, H), (247, 249, 252, 255))
    draw = ImageDraw.Draw(frame)
    for idx, label in enumerate(["Module", "Evidence", "Guard"]):
        x0 = 72 + idx * 344
        draw.rounded_rectangle((x0, 82, x0 + 278, 326), radius=20, fill=(255, 255, 255), outline=(214, 222, 232), width=2)
        draw.rounded_rectangle((x0 + 24, 112, x0 + 112, 178), radius=12, fill=accent)
        draw.text((x0 + 48, 128), "E2", fill=(255, 255, 255), font=FONT_MD)
        draw.text((x0 + 24, 210), label, fill=(22, 32, 44), font=FONT_MD)
        draw.text((x0 + 24, 250), "stable tag", fill=(86, 99, 116), font=FONT_SM)
    return frame


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    src = cover_image(args.source)
    accent = accent_from_image(src)
    out = args.out
    out.mkdir(parents=True, exist_ok=True)

    recipes = [
        ("motion_shine_sweep", "gif", shine_sweep(src, accent), "Hero banner / premium attention"),
        ("motion_icon_sequential_glow", "gif", icon_sequence(src, accent), "123 sequence / proof chips"),
        ("motion_border_breathing", "gif", border_breathing(src, accent), "Important note / trust closer"),
        ("motion_product_edge_glow", "gif", edge_glow(src, accent), "Product detail focus"),
        ("motion_background_light_streak", "gif", light_streak(src, accent), "Technical energy banner"),
        ("motion_dotted_twinkle", "gif", dotted_twinkle(src, accent), "Brand texture"),
        ("motion_step_highlight", "gif", step_highlight(src, accent), "How-to / steps"),
        ("motion_before_after_wipe", "gif", before_after(src, accent), "Evidence-based comparison"),
        ("motion_magnifier_pulse", "gif", magnifier(src, accent), "Detail inspection"),
        ("motion_parcel_micro_motion", "gif", parcel_motion(src, accent), "Brand/package trust"),
    ]

    assets = []
    for effect_id, kind, frames, usage in recipes:
        filename = f"{effect_id}.gif"
        save_gif(frames, out / filename)
        assets.append(
            {
                "component_id": effect_id,
                "file": filename,
                "output_type": kind,
                "usage": usage,
                "production_embed": f'<p data-component-id="{effect_id}" data-edit-id="{effect_id}-01" style="text-align:center;margin:0 0 14px;"><img src="assets/generated/{filename}" width="1140" alt="{usage}" style="max-width:100%;height:auto;"></p>',
                "guard": [
                    "GIF is embedded as image media only",
                    "Text and proof are deterministic overlays",
                    "Do not use if mobile text is unreadable",
                ],
            }
        )

    pngs = [
        ("brand_wordmark_side_tag", brand_side_tag(src, accent), "Brand side tag"),
        ("e2_marker_chip_board", e2_marker(src, accent), "E2 marker board"),
    ]
    for component_id, frame, usage in pngs:
        filename = f"{component_id}.png"
        save_png(frame, out / filename)
        assets.append(
            {
                "component_id": component_id,
                "file": filename,
                "output_type": "png",
                "usage": usage,
                "production_embed": f'<p data-component-id="{component_id}" data-edit-id="{component_id}-01" style="text-align:center;margin:0 0 14px;"><img src="assets/generated/{filename}" width="1140" alt="{usage}" style="max-width:100%;height:auto;"></p>',
                "guard": [
                    "Static fallback candidate",
                    "Brand text is rendered locally",
                    "Do not imitate platform or certification badges",
                ],
            }
        )

    report = {
        "source": str(args.source),
        "size": [W, H],
        "accent": accent,
        "asset_count": len(assets),
        "assets": assets,
    }
    (out / "gif_scale_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

