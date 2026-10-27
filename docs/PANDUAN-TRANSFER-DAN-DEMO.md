# Panduan Transfer & Demo — Studio Karya Nusa

Panduan ini untuk **kamu** (yang menyerahkan) dan **temanmu** (yang akan demo ke dosen). Bahasanya sengaja sederhana, langkah per langkah.

---

## Bagian 1 — Menyerahkan website ke laptop teman

### Yang perlu disiapkan

- File **`Studio-Karya-Nusa-Portable.zip`** (ada di `C:\Kuliah\`, ukuran ±172 MB).
- Flashdisk atau Google Drive.
- Laptop teman: **Windows 11 64-bit**.
- Browser: Edge atau Chrome.

### Langkah transfer

1. **Di laptop kamu:** matikan website dulu.
   - Double-click `MATIKAN.bat`.
   - Tunggu sampai muncul tulisan “Website sudah dimatikan.”
2. Copy file **`Studio-Karya-Nusa-Portable.zip`** ke flashdisk atau Google Drive.
3. **Di laptop teman:** copy ZIP ke folder sederhana, misalnya `C:\StudioKaryaNusa`.
4. Extract ZIP. Akan muncul folder **`AndepWordPress`**.
5. Buka folder `AndepWordPress`.
6. Double-click **`MULAI.bat`**.
7. Tunggu 5–15 detik. Browser akan otomatis membuka:
   - **<http://localhost:8080>**
8. Cek beberapa halaman:
   - Beranda
   - Profil
   - Program
   - Karya
   - Agenda
9. Untuk mematikan: double-click **`MATIKAN.bat`**.

> **Penting:** jangan copy hanya folder `public` atau `data`. Copy **seluruh folder** `AndepWordPress` karena di dalamnya ada PHP, MariaDB, database, dan WordPress.

### Kalau muncul peringatan

| Masalah | Solusi |
|---|---|
| Windows SmartScreen muncul | Klik **More info → Run anyway** |
| Antivirus menahan file | Pilih **Allow** / **Restore** untuk folder proyek |
| Browser bilang “can't reach localhost:8080” | Pastikan `MULAI.bat` sudah dijalankan dan tunggu 10–20 detik |
| Port 8080/3307 dipakai aplikasi lain | Tutup aplikasi tersebut, lalu jalankan `MULAI.bat` lagi |
| MariaDB gagal menyala | Install **Microsoft Visual C++ 2015–2022 x64**, lalu coba lagi |
| “Error establishing a database connection” | `MATIKAN.bat` → `MULAI.bat`. Jika masih, copy ulang folder dari ZIP |

### Checklist sebelum diserahkan

- [ ] Website sudah dimatikan di laptop kamu.
- [ ] ZIP sudah dicopy ke flashdisk/Drive.
- [ ] Di laptop teman, ZIP berhasil diextract.
- [ ] `MULAI.bat` berhasil membuka `http://localhost:8080`.
- [ ] Semua halaman dan postingan bisa dibuka.
- [ ] Login admin berhasil.
- [ ] `MATIKAN.bat` berhasil mematikan website.

---

## Bagian 2 — Login ke WordPress

1. Buka **<http://localhost:8080/wp-admin>**.
2. Masukkan:
   - **Username:** `admin`
   - **Password:** `StudioKaryaNusa2026!`
3. Klik **Log In**.
4. Setelah masuk, akan terlihat **Dashboard** dengan menu di sebelah kiri:
   - **Posts** — semua postingan
   - **Media** — gambar
   - **Pages** — halaman
   - **Appearance** — tema, menu, customizer
   - **Plugins** — tidak dipakai
   - **Users** — akun
   - **Settings** — pengaturan website

Di bagian atas ada tulisan **“Howdy, Muhammad Andep”**. Klik nama website di kiri atas untuk melihat front-end.

![Homepage Studio Karya Nusa](screenshots/home.png)

---

## Bagian 3 — Script demo ke dosen (5–7 menit)

Ini urutan yang bisa temanmu ikuti saat ditanya dosen. Kalimatnya boleh dipakai langsung.

### 1. Buka front-end

Buka **<http://localhost:8080>**.

> “Ini website **Studio Karya Nusa**, komunitas kreatif fiktif untuk Varian C. Di homepage ada hero, program, karya terbaru, dan agenda.”

Tunjukkan menu: **Beranda, Profil, Program, Karya, Agenda, Blog**.

### 2. Buka Page 1 — Profil

Klik menu **Profil**.

> “Ini Page pertama, **Profil Studio Karya Nusa**. Heading-nya **Tentang Studio Karya Nusa**, isinya paragraf profil, dan di bawah ada **Lokasi operasional: Samarinda Ulu**.”

### 3. Buka Page 2 — Program

Klik menu **Program**.

> “Ini Page kedua, **Program Studio Karya Nusa**. Heading-nya **Program Kami**, dan di sini ada **Kode verifikasi: UTS-C-2511102414081**.”

### 4. Buka Post 1 — Galeri Poster Komunitas

Klik menu **Karya**.

> “Ini Post pertama, **Galeri Poster Komunitas**. Ada dua paragraf, dan gambar **c_studio.jpg** diletakkan di antara paragraf pertama dan kedua. Kategori **Karya Komunitas**, tag **Poster**.”

Tunjukkan bagian bawah postingan: **Categorized as Karya Komunitas**, **Tagged Poster**.

### 5. Buka Post 2 — Lokakarya Poster Digital

Klik menu **Agenda**.

> “Ini Post kedua, **Lokakarya Poster Digital**. Ada dua paragraf dan **Jadwal khusus: Jumat, 14.00 WITA**. Kategori **Agenda Kreatif**, tag **Desain Digital**.”

### 6. Masuk admin — Settings

Buka **<http://localhost:8080/wp-admin>**.

Klik **Settings → General**.

> “Di sini **Site Title: Studio Karya Nusa** dan **Tagline: Ruang kreasi dan berbagi ide**.”

### 7. Tunjukkan Pages

Klik **Pages → All Pages**.

> “Ada dua halaman wajib yang sudah published: **Profil Studio Karya Nusa** dan **Program Studio Karya Nusa**.”

Klik **Edit** pada **Program Studio Karya Nusa**. Tunjukkan blok **Kode verifikasi: UTS-C-2511102414081** di editor.

### 8. Tunjukkan Posts + kategori/tag

Klik **Posts → All Posts**.

> “Di daftar ini terlihat kategori dan tag kedua postingan.”

Klik **Edit** pada **Galeri Poster Komunitas**.

Tunjukkan:
- Gambar `c_studio.jpg` di antara dua paragraf.
- Panel kanan **Categories → Karya Komunitas**.
- Panel kanan **Tags → Poster**.
- Panel kanan **Featured image → c_studio.jpg**.

![Editor Post 1](screenshots/editor-sidebar.png)

### 9. Tunjukkan Media Library

Klik **Media → Library**. Klik gambar **c_studio.jpg**.

> “File aslinya **c_studio.jpg**, ukuran 1200 × 1500 px. Alt text juga sudah diisi.”

![Media Library](screenshots/media-library.png)

### 10. Tutup demo

Kembali ke front-end, tunjukkan homepage dan menu.

> “Semua konten wajib sudah ada: 2 Page, 2 Post, kategori, tag, gambar, site title, tagline, lokasi, jadwal, dan kode verifikasi.”

---

## Bagian 4 — Cara membuat post baru (kalau ditanya dosen)

> **Tips:** kalau hanya latihan, gunakan **Save Draft**, jangan **Publish**. Kalau dosen minta demo publish, boleh publish satu post sederhana.

### Langkah membuat post baru

1. Login admin: **<http://localhost:8080/wp-admin>**.
2. Klik **Posts → Add New**.
3. Isi **Title**, misalnya: `Latihan Post Baru`.
4. Klik kotak besar di bawah judul, lalu ketik paragraf pertama.
5. Untuk menambah blok baru:
   - Klik tombol **+** di kiri atas, atau
   - Ketik `/` lalu pilih **Paragraph**, **Heading**, **Image**, dll.
6. Untuk menambah paragraf kedua:
   - Klik di bawah paragraf pertama, tekan **Enter**, lalu ketik paragraf kedua.
7. Untuk menambah gambar:
   - Klik **+ → Image**.
   - Pilih **Media Library** atau **Upload**.
   - Klik gambar → **Insert**.
   - Kalau ingin gambar di antara paragraf: letakkan kursor **di akhir paragraf pertama**, tambah blok Image, lalu tambah paragraf kedua di bawah gambar.
8. Atur **Category**:
   - Buka panel kanan **Post** (ikon gear).
   - Buka **Categories**.
   - Centang kategori yang ada, atau klik **Add New Category**.
9. Atur **Tag**:
   - Buka **Tags**.
   - Ketik tag, lalu tekan **Enter**.
10. Atur **Featured image** (opsional):
    - Buka **Featured image**.
    - Klik **Set featured image**.
    - Pilih gambar → **Set featured image**.
11. Cek hasil:
    - Klik **Preview → Preview in new tab**.
12. Kalau sudah yakin:
    - Klik **Publish** → **Publish** lagi.
    - Klik **View Post** untuk melihat hasilnya.
13. Kalau hanya latihan:
    - Klik **Save Draft** (bukan Publish).
    - Untuk menghapus: **Posts → All Posts** → arahkan mouse ke post → **Trash**.

### Kalau ingin menghapus post latihan

1. **Posts → All Posts**.
2. Arahkan mouse ke post latihan.
3. Klik **Trash**.
4. Post wajib **Galeri Poster Komunitas** dan **Lokakarya Poster Digital** jangan dihapus.

---

## Bagian 5 — Cara mengedit Page/Post yang sudah ada

### Edit Page

1. **Pages → All Pages**.
2. Arahkan mouse ke page → **Edit**.
3. Ubah teks di editor.
4. Klik **Update** di kanan atas.
5. Klik **View Page** untuk melihat.

### Edit Post

1. **Posts → All Posts**.
2. Arahkan mouse ke post → **Edit**.
3. Ubah judul/paragraf/gambar.
4. Klik **Update**.
5. Klik **View Post**.

### Mengganti gambar di Post 1

1. Buka **Posts → Galeri Poster Komunitas → Edit**.
2. Klik gambar `c_studio.jpg`.
3. Klik **Replace**.
4. Pilih gambar baru → **Replace**.
5. Klik **Update**.

> Jangan hapus `c_studio.jpg` dari Media Library. File itu wajib ada untuk bukti B4.

### Mengganti kode verifikasi

1. **Pages → Program Studio Karya Nusa → Edit**.
2. Cari paragraf `Kode verifikasi: UTS-C-2511102414081`.
3. Ganti angkanya jika perlu.
4. Klik **Update**.

---

## Bagian 6 — Kategori dan tag

### Bedanya

- **Category** = kelompok besar. Contoh: `Karya Komunitas`, `Agenda Kreatif`.
- **Tag** = kata kunci spesifik. Contoh: `Poster`, `Desain Digital`.

### Cara membuat kategori baru

1. **Posts → Categories**.
2. Isi **Name**, **Slug**, **Description** (opsional).
3. Klik **Add New Category**.

### Cara membuat tag baru

1. **Posts → Tags**.
2. Isi **Name**, **Slug**, **Description** (opsional).
3. Klik **Add New Tag**.

### Cara memasang ke post

1. Edit post.
2. Panel kanan **Post → Categories** → centang kategori.
3. Panel kanan **Post → Tags** → ketik tag → **Enter**.
4. Klik **Update**.

---

## Bagian 7 — Mengubah Site Title dan Tagline

1. **Settings → General**.
2. Ubah **Site Title** dan **Tagline**.
3. Klik **Save Changes**.
4. Buka front-end untuk melihat hasilnya.

![Settings General](screenshots/settings-general.png)

---

## Bagian 8 — Mengubah menu

1. **Appearance → Menus**.
2. Pilih menu **Menu Utama** (menu atas).
3. Tambahkan item:
   - **Pages** → centang halaman → **Add to Menu**.
   - **Categories** → centang kategori → **Add to Menu**.
   - **Custom Links** → isi URL dan teks → **Add to Menu**.
4. Drag item untuk mengubah urutan.
5. Klik **Save Menu**.
6. Untuk menu footer, pilih **Menu Footer**.

---

## Bagian 9 — Mengubah homepage

1. **Settings → Reading**.
2. Pada **Your homepage displays**, pilih **A static page**.
3. **Homepage:** `Beranda`.
4. **Posts page:** `Blog`.
5. Klik **Save Changes**.
6. Untuk mengedit isi homepage: **Pages → Beranda → Edit**.
   - Hero, kartu program, karya, agenda, dan CTA adalah blok-blok di editor.
   - Klik teks/gambar untuk mengubah.
   - Klik **Update**.

---

## Bagian 10 — Media Library

1. **Media → Library**.
2. Klik **Add New** untuk upload gambar baru.
3. Klik gambar untuk melihat:
   - **File name**
   - **File type**
   - **Dimensions**
   - **Alt Text**
   - **Title**
   - **File URL**
4. Klik **Copy URL** kalau perlu menempelkan URL gambar.
5. Jangan hapus `c_studio.jpg`, `lokakarya.jpg`, logo, dan site icon.

---

## Bagian 11 — Backup dan restore

### Backup

1. Pastikan website menyala (`MULAI.bat`).
2. Double-click **`BACKUP.bat`**.
3. File backup dibuat di folder `backup\`:
   - `database.sql`
   - `studio-karya-nusa-wxr.xml`
4. Copy folder `backup` ke flashdisk/Drive.

### Restore ke WordPress lain

1. Di WordPress tujuan: **Tools → Import → WordPress**.
2. Install importer jika diminta.
3. Upload `studio-karya-nusa-wxr.xml`.
4. Centang **Download and import file attachments**.
5. Assign author ke user yang ada.

> WXR tidak membawa Site Title, Tagline, menu, dan custom CSS. Atur ulang di **Settings → General**, **Appearance → Menus**, dan **Customize → Additional CSS**.

### Restore ke folder portable

- Extract ulang ZIP portable (database sudah termasuk).
- Atau jalankan `MULAI.bat`; jika database kosong, script akan mencoba import dari `backup\database.sql`.

---

## Bagian 12 — Pertanyaan yang sering ditanya dosen

### “Apa bedanya Page dan Post?”

- **Page** = halaman statis, biasanya ada di menu: Profil, Program.
- **Post** = tulisan dinamis, muncul di Blog/Karya/Agenda: Galeri Poster, Lokakarya.

### “Kenapa gambarnya ada di antara paragraf?”

> “Saya menambahkan blok Image setelah paragraf pertama, lalu paragraf kedua di bawah gambar.”

### “Bagaimana cara set featured image?”

> “Buka panel kanan Post → Featured image → Set featured image → pilih gambar → Set featured image.”

### “Di mana kode verifikasinya?”

> “Ada di konten Page 2, bukan di nama file: **Kode verifikasi: UTS-C-2511102414081**.”

### “Di mana lokasi dan jadwalnya?”

> “Lokasi ada di Page 1: **Lokasi operasional: Samarinda Ulu**. Jadwal ada di Post 2: **Jadwal khusus: Jumat, 14.00 WITA**.”

### “Kenapa website harus pakai MULAI.bat?”

> “Karena WordPress-nya berjalan di localhost dengan PHP dan MariaDB portable. `MULAI.bat` menyalakan database dan web server lokal.”

### “Kenapa alamatnya localhost:8080?”

> “Karena ini WordPress lokal untuk UTS, bukan hosting online. Port 8080 dipakai agar tidak bentrok dengan aplikasi lain.”

### “Kalau admin password lupa?”

Hubungi pemilik proyek. Password ada di README: `StudioKaryaNusa2026!`.

---

## Bagian 13 — Latihan sebelum demo

Lakukan 2–3 kali sebelum hari-H:

1. **Latihan start/stop**
   - `MULAI.bat` → buka homepage → `MATIKAN.bat`.
2. **Latihan buka semua halaman**
   - Beranda, Profil, Program, Karya, Agenda.
3. **Latihan buat draft post**
   - Posts → Add New → judul + 2 paragraf + 1 gambar + kategori + tag.
   - Klik **Save Draft** (jangan Publish).
   - Preview.
   - Hapus draft lewat **Posts → All Posts → Trash**.
4. **Latihan edit**
   - Edit Page 1, ubah satu kata, **Update**, lihat hasil, lalu kembalikan.
   - Jangan lupa klik **Update**.
5. **Latihan backup**
   - Jalankan `BACKUP.bat`, cek file di `backup\`.

> Sebelum latihan, jalankan `BACKUP.bat` dulu. Kalau ada yang salah, backup bisa dipakai untuk restore.

---

## Ringkasan satu halaman

| Kebutuhan | Langkah |
|---|---|
| Menyalakan website | Double-click `MULAI.bat` |
| Mematikan website | Double-click `MATIKAN.bat` |
| Buka front-end | <http://localhost:8080> |
| Buka admin | <http://localhost:8080/wp-admin> |
| Login | `admin` / `StudioKaryaNusa2026!` |
| Buat post baru | Posts → Add New → isi → Publish/Save Draft |
| Edit post/page | Posts/Pages → Edit → Update |
| Ganti site title/tagline | Settings → General |
| Ganti menu | Appearance → Menus |
| Ganti homepage | Settings → Reading |
| Backup | `BACKUP.bat` |
| Pindah laptop | Stop → copy/extract ZIP → `MULAI.bat` |

---

**Studio Karya Nusa — UTS Praktik Pemrograman Web Berbasis CMS, Varian C**  
Muhammad Andep — 2511102414081
