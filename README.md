# Simulasi-Ekspansi-Lahan-Papua-Juni2026

Dibuat sebagai bagian dari makalah **"Simulasi Ekspansi Lahan Perkebunan Menggunakan Algoritma Greedy dan Analisis Dampaknya terhadap Fragmentasi Hutan Adat Papua"** untuk mata kuliah IF2211 Strategi Algoritma, Institut Teknologi Bandung, Tahun Ajaran 2025/2026.

---
## Deskripsi

Program ini memodelkan pola pembukaan lahan perkebunan pada *grid* 15×15 yang merepresentasikan peta lahan Papua. Dua algoritma dibandingkan:

- **Greedy** — selalu memilih sel dengan nilai ekonomi tertinggi, merepresentasikan ekspansi yang berorientasi keuntungan jangka pendek.
- **Counter-Greedy** — mendahulukan lahan terbuka sebelum mengonversi hutan sekunder dan hutan primer, merepresentasikan pendekatan yang lebih konservatif terhadap hutan.

Setelah ekspansi, fragmentasi hutan dianalisis menggunakan algoritma BFS (*Breadth-First Search*) untuk menghitung jumlah dan ukuran *patch* hutan yang tersisa.

---

## Struktur Direktori

```
.
├── main.py              # Entry point — jalankan ini
├── konstanta.py         # Tipe lahan, label, simbol ASCII
├── inisialisasi.py      # Pembuatan grid dan nilai ekonomi
├── algoritma.py         # Greedy dan Counter-Greedy
├── fragmentasi.py       # BFS dan analisis patch
├── visualisasi.py       # Fungsi cetak dan tabel output
├── runner.py            # Menjalankan dan menampilkan satu skenario
└── buat_gambar.py       # Menghasilkan gambar untuk makalah (butuh matplotlib)
```

---

## Cara Menjalankan

Pastikan Python 3.9 atau lebih baru sudah terinstal.

```bash
# Jalankan simulasi teks
python main.py

# Hasilkan gambar untuk makalah
python buat_gambar.py
```

Tidak ada dependensi eksternal untuk `main.py`. Untuk `buat_gambar.py` dibutuhkan `matplotlib`:

```bash
pip install matplotlib
```

---

## Contoh Output

```
Grid  : 15 x 15 = 225 sel total
Seed  : 42 (deterministik, reproducible)

SKENARIO: TARGET KONVERSI = 60 SEL
...
  Metrik                           Awal     Greedy  Counter-G
  Total Hutan (sel)                 169        109        165
  Jumlah Patch                        2         30          2
  Patch Terbesar (sel)              168         17        164
  Total Nilai Ekonomi                       555.12     161.75
```

---

## Hasil Utama

| Skenario | Greedy — Patch | Counter-Greedy — Patch | Greedy — Nilai | Counter-Greedy — Nilai |
|---|---|---|---|---|
| 40 sel | 15 | 2 | 380,38 | 111,57 |
| 60 sel | 30 | 2 | 555,12 | 161,75 |
| 80 sel | 35 | 6 | 719,91 | 291,24 |

*Greedy* menghasilkan nilai ekonomi lebih tinggi di semua skenario, tetapi menyebabkan fragmentasi hutan yang jauh lebih parah. *Counter-Greedy* menjaga konektivitas hutan selama masih tersedia lahan terbuka.

---

## Tautan

- 📄 **Makalah**: tersedia di repositori ini
- 🎥 **Video penjelasan**: [bit.ly/SimulasiGreedyLahanPapua2026Ziza](https://bit.ly/SimulasiGreedyLahanPapua2026Ziza)

---

## Penulis

**Aziza Dharma Putri** — 13524017  
Program Studi Teknik Informatika, STEI ITB  
13524017@std.stei.itb.ac.id | zizadhrmaa@gmail.com