from PIL import Image, ImageDraw, ImageFont
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 1500

GREEN = "#123B32"
GREEN_DARK = "#0C2A24"
CREAM = "#F7F1E6"
TERRA = "#D97757"
MUSTARD = "#E3B23C"
INK = "#1F2421"

FONT_SERIF_BOLD = r"C:\Windows\Fonts\georgiab.ttf"
FONT_SERIF = r"C:\Windows\Fonts\georgia.ttf"
FONT_SERIF_ITALIC = r"C:\Windows\Fonts\georgiai.ttf"
FONT_SANS = r"C:\Windows\Fonts\segoeui.ttf"
FONT_SANS_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_SANS_SEMI = r"C:\Windows\Fonts\seguisb.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_size(draw, text, f):
    b = draw.textbbox((0, 0), text, font=f)
    return b[2] - b[0], b[3] - b[1]


def draw_spaced(draw, xy, text, f, fill, spacing=0, anchor_left=True):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        w = draw.textlength(ch, font=f)
        x += w + spacing
    return x


def spaced_width(draw, text, f, spacing=0):
    return sum(draw.textlength(ch, font=f) for ch in text) + spacing * max(0, len(text) - 1)


def vertical_gradient(size, top, bottom):
    w, h = size
    base = Image.new("RGB", (1, h))
    px = base.load()
    for y in range(h):
        t = y / max(1, h - 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return base.resize((w, h))


def leaf(draw, cx, cy, length, width, angle_deg, fill, vein=None):
    # A pointed leaf: base at (0, 0), tip at (0, -length)
    n = 120
    left, right = [], []
    for i in range(n + 1):
        t = i / n
        hw = width * (math.sin(math.pi * t) ** 0.72)
        y = -length * t
        left.append((-hw, y))
        right.append((hw, y))
    pts = left + list(reversed(right))
    a = math.radians(angle_deg)
    def rot(x, y):
        return (cx + x * math.cos(a) - y * math.sin(a),
                cy + x * math.sin(a) + y * math.cos(a))
    out = [rot(x, y) for x, y in pts]
    draw.polygon(out, fill=fill)
    if vein:
        vx, vy = rot(0, 0)
        tx, ty = rot(0, -length * 0.94)
        draw.line([vx, vy, tx, ty], fill=vein, width=5)
        for frac in (0.28, 0.46, 0.64):
            lx, ly = rot(-width * 0.42 * (1 - frac), -length * frac)
            rx_, ry_ = rot(width * 0.42 * (1 - frac), -length * frac)
            draw.line([lx, ly, vx + (tx - vx) * frac, vy + (ty - vy) * frac], fill=vein, width=2)
            draw.line([rx_, ry_, vx + (tx - vx) * frac, vy + (ty - vy) * frac], fill=vein, width=2)


def base_canvas(top=GREEN_DARK, bottom=GREEN):
    img = vertical_gradient((W, H), ImageColor(top), ImageColor(bottom))
    return img


def ImageColor(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def make_poster(filename, palette, title_lines, subtitle, bottom1, bottom2, accent):
    bg_top, bg_bottom = palette
    img = base_canvas(bg_top, bg_bottom).convert("RGBA")
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    # subtle grain
    import random
    random.seed(42)
    for _ in range(9000):
        x = random.randint(0, W - 1)
        y = random.randint(0, H - 1)
        a = random.randint(4, 12)
        d.point((x, y), fill=(255, 255, 255, a))

    # border
    d.rectangle([36, 36, W - 37, H - 37], outline=CREAM + "66", width=3)

    # top label
    f_label = font(FONT_SANS_SEMI, 28)
    draw_spaced(d, (80, 92), "STUDIO KARYA NUSA", f_label, CREAM, spacing=6)
    d.line([80, 142, 210, 142], fill=CREAM, width=3)

    # monogram badge
    d.ellipse([W - 190, 78, W - 78, 190], outline=CREAM, width=3)
    f_badge = font(FONT_SERIF_BOLD, 42)
    tw, th = text_size(d, "SKN", f_badge)
    d.text(((W - 190 + W - 78 - tw) / 2, 78 + (112 - th) / 2 - 6), "SKN", font=f_badge, fill=CREAM)

    # big title
    y = 238
    for i, line in enumerate(title_lines):
        size = 148 if i < 2 else 108
        f_title = font(FONT_SERIF_BOLD, size)
        d.text((80, y), line, font=f_title, fill=CREAM)
        y += int(size * 1.02)

    # subtitle
    f_sub = font(FONT_SERIF_ITALIC, 46)
    d.text((82, y + 8), subtitle, font=f_sub, fill=accent)

    # abstract composition
    cx, cy = 900, 1035
    d.ellipse([cx - 245, cy - 245, cx + 245, cy + 245], fill=accent + "CC")
    d.ellipse([cx - 245, cy - 245, cx + 245, cy + 245], outline=CREAM + "55", width=3)
    leaf(d, cx - 8, cy + 168, 420, 142, 22, CREAM + "E6", vein=GREEN_DARK + "88")
    # small dots
    for (dx, dy, r, col) in [(-180, 180, 16, MUSTARD), (170, -160, 10, CREAM), (150, 205, 22, GREEN_DARK)]:
        d.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=col)

    # arc
    d.arc([700, 780, 1120, 1200], start=200, end=340, fill=MUSTARD + "CC", width=8)

    # bottom rule
    d.line([80, 1310, W - 80, 1310], fill=CREAM + "55", width=2)

    f_b1 = font(FONT_SANS_BOLD, 26)
    draw_spaced(d, (80, 1340), bottom1, f_b1, CREAM, spacing=3)
    f_b2 = font(FONT_SANS, 22)
    draw_spaced(d, (80, 1388), bottom2, f_b2, accent, spacing=3)

    # bottom-right issue mark
    f_issue = font(FONT_SANS_SEMI, 22)
    s = "VOL. 01 / 2026"
    tw, th = text_size(d, s, f_issue)
    d.text((W - 80 - tw, 1388), s, font=f_issue, fill=CREAM + "AA")

    out = Image.alpha_composite(img, overlay).convert("RGB")
    out.save(os.path.join(OUT, filename), quality=93, optimize=True)
    print("wrote", filename)


def make_logo(filename, bg=None, mark="SKN", fg=CREAM, circle=GREEN, accent=TERRA, size=512):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0) if bg is None else ImageColor(bg) + (255,))
    d = ImageDraw.Draw(img)
    pad = 26
    d.ellipse([pad, pad, size - pad, size - pad], fill=circle)
    d.ellipse([pad + 12, pad + 12, size - pad - 12, size - pad - 12], outline=CREAM + "55", width=3)
    f = font(FONT_SERIF_BOLD, 150 if len(mark) == 3 else 210)
    tw, th = text_size(d, mark, f)
    d.text(((size - tw) / 2, (size - th) / 2 - 18), mark, font=f, fill=fg)
    # small accent leaf/dot
    d.ellipse([size - 118, 82, size - 74, 126], fill=accent)
    img.save(os.path.join(OUT, filename))
    print("wrote", filename)


make_poster(
    "c_studio.jpg",
    (GREEN_DARK, "#1A4A40"),
    ["GALERI", "POSTER", "KOMUNITAS"],
    "Tema Lingkungan Sekitar",
    "KARYA KOMUNITAS  •  SAMARINDA ULU",
    "Pameran karya visual anggota komunitas",
    MUSTARD,
)

make_poster(
    "lokakarya.jpg",
    ("#8F3F2A", TERRA),
    ["LOKAKARYA", "POSTER", "DIGITAL"],
    "Untuk Peserta Pemula",
    "AGENDA KREATIF  •  SAMARINDA ULU",
    "Jumat, 14.00 WITA  •  Studio Karya Nusa",
    GREEN,
)

make_logo("logo-skn.png", bg=None, mark="SKN")
make_logo("site-icon.png", bg=CREAM, mark="S", fg=CREAM, circle=GREEN, accent=TERRA)
