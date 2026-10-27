from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

SRC = r'C:\Kuliah\AndepWordPress\runtime\shots'
OUT = r'C:\Kuliah\AndepWordPress\bukti\report'
os.makedirs(OUT, exist_ok=True)

GREEN = '#123b32'
DEEP = '#0c2a24'
CREAM = '#f7f1e6'
TERRA = '#d97757'
MUSTARD = '#e3b23c'
MUTED = '#5e6a63'
LINE = '#d9d0c2'
WHITE = '#ffffff'

SANS = r'C:\Windows\Fonts\segoeui.ttf'
SANS_B = r'C:\Windows\Fonts\segoeuib.ttf'
SANS_SB = r'C:\Windows\Fonts\seguisb.ttf'
SERIF_B = r'C:\Windows\Fonts\georgiab.ttf'

W, H = 2100, 700

def font(path, size):
    return ImageFont.truetype(path, size)

def load(name):
    return Image.open(os.path.join(SRC, name)).convert('RGB')

def fit(img, w, h):
    im = ImageOps.contain(img, (w, h), Image.LANCZOS)
    canvas = Image.new('RGB', (w, h), WHITE)
    canvas.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
    return canvas

def fit_top(img, w, h):
    im = ImageOps.contain(img, (w, h), Image.LANCZOS)
    canvas = Image.new('RGB', (w, h), WHITE)
    canvas.paste(im, ((w - im.width) // 2, 0))
    return canvas

def panel(canvas, img, x, y, w, h, pad=6):
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=WHITE, outline=LINE, width=2)
    inner = fit(img, w - 2 * pad, h - 2 * pad)
    canvas.paste(inner, (x + pad, y + pad))

def panel_top(canvas, img, x, y, w, h, pad=6):
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=WHITE, outline=LINE, width=2)
    inner = fit_top(img, w - 2 * pad, h - 2 * pad)
    canvas.paste(inner, (x + pad, y + pad))

def base(title):
    canvas = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, 0, W, 54], fill=GREEN)
    d.text((24, 14), title, font=font(SANS_B, 24), fill=CREAM)
    return canvas, d

def text(d, xy, s, f, fill, max_width=None, line_gap=4):
    if max_width is None:
        d.text(xy, s, font=f, fill=fill)
        return
    words = s.split()
    lines, cur = [], ''
    for wd in words:
        test = (cur + ' ' + wd).strip()
        if d.textlength(test, font=f) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    x, y = xy
    for line in lines:
        d.text((x, y), line, font=f, fill=fill)
        y += f.size + line_gap
    return y

def caption(d, x, y, kicker, main, sub=None, max_width=640):
    d.text((x, y), kicker, font=font(SANS_B, 19), fill=TERRA)
    d.text((x, y + 27), main, font=font(SERIF_B, 24), fill=GREEN)
    yy = y + 62
    if sub:
        yy = text(d, (x, yy), sub, font(SANS, 17), MUTED, max_width=max_width, line_gap=3)
    return yy

# ---------------- B1 ----------------
c, d = base('B1  PAGE - DUA HALAMAN WAJIB')
panel(c, load('pages-list.png'), 20, 72, 740, 280)
d.text((34, 372), 'DAFTAR PAGE', font=font(SANS_B, 19), fill=TERRA)
d.text((34, 400), 'Page 1 - Profil Studio Karya Nusa', font=font(SERIF_B, 25), fill=GREEN)
d.text((34, 436), 'Page 2 - Program Studio Karya Nusa', font=font(SERIF_B, 25), fill=GREEN)
d.text((34, 486), 'Status: Published (2 Page)', font=font(SANS_SB, 18), fill=MUTED)
text(d, (34, 520), 'Kedua halaman wajib sudah terbit dan dapat diakses dari menu utama.', font(SANS, 16), MUTED, max_width=690)

panel_top(c, load('clean-page1.png').crop((240, 90, 1200, 700)), 780, 72, 660, 420)
caption(d, 792, 505, 'PAGE 1 - PROFIL', 'Tentang Studio Karya Nusa', 'Lokasi operasional: Samarinda Ulu', max_width=630)
panel_top(c, load('clean-page2.png').crop((240, 90, 1200, 700)), 1460, 72, 620, 420)
caption(d, 1472, 505, 'PAGE 2 - PROGRAM', 'Program Kami', 'Kode verifikasi: UTS-C-2511102414081', max_width=590)
c.save(os.path.join(OUT, 'B1.png'))

# ---------------- B2 ----------------
c, d = base('B2  POST - DUA POSTINGAN WAJIB')
panel(c, load('posts-list.png'), 20, 72, 740, 280)
d.text((34, 372), 'DAFTAR POST', font=font(SANS_B, 19), fill=TERRA)
d.text((34, 400), 'Post 1 - Galeri Poster Komunitas', font=font(SERIF_B, 25), fill=GREEN)
d.text((34, 436), 'Post 2 - Lokakarya Poster Digital', font=font(SERIF_B, 25), fill=GREEN)
d.text((34, 486), 'Status: Published (2 Post)', font=font(SANS_SB, 18), fill=MUTED)
text(d, (34, 520), 'Kedua postingan sudah terbit dan tampil di halaman Blog.', font(SANS, 16), MUTED, max_width=690)

panel_top(c, load('clean-post1.png').crop((240, 90, 1200, 600)), 780, 72, 660, 430)
caption(d, 792, 515, 'POST 1', 'Galeri Poster Komunitas', 'Judul, paragraf 1, dan gambar c_studio.jpg.', max_width=630)
panel_top(c, load('clean-post2.png').crop((240, 90, 1200, 760)), 1460, 72, 620, 430)
caption(d, 1472, 515, 'POST 2', 'Lokakarya Poster Digital', 'Dua paragraf + jadwal khusus.', max_width=590)
c.save(os.path.join(OUT, 'B2.png'))

# ---------------- B3 ----------------
c, d = base('B3  CATEGORY & TAG - PENERAPAN PADA KEDUA POST')
posts = load('posts-list.png').crop((0, 88, 1225, 369))
panel(c, posts, 20, 72, 2060, 460, pad=8)
d.text((34, 548), 'Post 1: Karya Komunitas  |  Poster', font=font(SANS_B, 26), fill=GREEN)
d.text((34, 586), 'Post 2: Agenda Kreatif  |  Desain Digital', font=font(SANS_B, 26), fill=GREEN)
text(d, (900, 552), 'Kategori dan tag masing-masing post terlihat pada kolom Categories dan Tags di daftar Posts.', font(SANS, 18), MUTED, max_width=1140)
c.save(os.path.join(OUT, 'B3.png'))

# ---------------- B4 ----------------
c, d = base('B4  GAMBAR - MEDIA LIBRARY + GAMBAR DI POST 1')
poster = load('media-details.png').crop((155, 90, 800, 900))
panel(c, poster, 20, 72, 330, 530, pad=5)
details = load('media-details.png').crop((900, 90, 1400, 230))
panel(c, details, 366, 72, 640, 220, pad=8)
d.text((382, 310), 'MEDIA LIBRARY', font=font(SANS_B, 19), fill=TERRA)
d.text((382, 338), 'c_studio.jpg', font=font(SERIF_B, 28), fill=GREEN)
d.text((382, 378), '1200 x 1500 px  |  image/jpeg  |  179 KB', font=font(SANS_SB, 17), fill=MUTED)
text(d, (382, 410), 'Alt text: Poster Galeri Poster Komunitas Studio Karya Nusa bertema lingkungan sekitar.', font(SANS, 15), MUTED, max_width=600)

strip = load('clean-post1.png').crop((240, 90, 1200, 1450))
panel_top(c, strip, 1030, 72, 430, 600, pad=5)
d.line([1478, 300, 1520, 300], fill=TERRA, width=8)
d.polygon([(1520, 286), (1540, 300), (1520, 314)], fill=TERRA)
d.text((1552, 270), 'GAMBAR c_studio.jpg', font=font(SANS_B, 26), fill=GREEN)
text(d, (1552, 308), 'disisipkan setelah paragraf pertama dan sebelum paragraf kedua Post 1.', font(SANS, 20), MUTED, max_width=520)
d.text((1552, 410), 'Post 1 - Galeri Poster Komunitas', font=font(SERIF_B, 22), fill=GREEN)
text(d, (1552, 448), 'Gambar juga dipakai sebagai featured image. File asli tetap tersimpan di Media Library.', font(SANS, 16), MUTED, max_width=500)
c.save(os.path.join(OUT, 'B4.png'))

# ---------------- B5 ----------------
c, d = base('B5  IDENTITAS WEBSITE - SETTINGS -> GENERAL')
settings = load('settings-general.png').crop((0, 0, 1230, 330))
panel(c, settings, 20, 72, 2060, 500, pad=8)
d.text((38, 590), 'Site Title:', font=font(SANS_B, 22), fill=TERRA)
d.text((190, 586), 'Studio Karya Nusa', font=font(SERIF_B, 27), fill=GREEN)
d.text((760, 590), 'Tagline:', font=font(SANS_B, 22), fill=TERRA)
d.text((880, 586), 'Ruang kreasi dan berbagi ide', font=font(SERIF_B, 27), fill=GREEN)
c.save(os.path.join(OUT, 'B5.png'))

# ---------------- B6 ----------------
c, d = base('B6  KETENTUAN KHUSUS - LOKASI, JADWAL, KODE VERIFIKASI')
panel_top(c, load('clean-page1.png').crop((240, 120, 1200, 700)), 20, 72, 660, 400)
d.text((34, 486), 'PAGE 1 - LOKASI', font=font(SANS_B, 19), fill=TERRA)
d.text((34, 514), 'Lokasi operasional: Samarinda Ulu', font=font(SERIF_B, 23), fill=GREEN)
text(d, (34, 550), 'Baris tambahan pada konten Page 1.', font(SANS, 16), MUTED, max_width=620)

panel_top(c, load('clean-post2.png').crop((240, 120, 1200, 760)), 720, 72, 660, 400)
d.text((734, 486), 'POST 2 - JADWAL', font=font(SANS_B, 19), fill=TERRA)
d.text((734, 514), 'Jadwal khusus: Jumat, 14.00 WITA', font=font(SERIF_B, 23), fill=GREEN)
text(d, (734, 550), 'Baris tambahan pada konten Post 2.', font(SANS, 16), MUTED, max_width=620)

panel_top(c, load('clean-page2.png').crop((240, 120, 1200, 700)), 1420, 72, 660, 400)
d.text((1434, 486), 'PAGE 2 - KODE VERIFIKASI', font=font(SANS_B, 19), fill=TERRA)
d.text((1434, 514), 'UTS-C-2511102414081', font=font(SERIF_B, 26), fill=GREEN)
text(d, (1434, 552), 'Kode tampil di dalam konten Page 2, bukan hanya nama file.', font(SANS, 16), MUTED, max_width=620)
c.save(os.path.join(OUT, 'B6.png'))

print('done')
