"""
visualisasi.py
Fungsi-fungsi pencetakan peta ASCII dan tabel statistik ke stdout.
"""

from konstanta import SIMBOL, LEGENDA

def cetak_peta(peta: list[list[int]], judul: str) -> None:
    lebar = 50
    print(f"\n{'=' * lebar}")
    print(f"  {judul}")
    print(f"  {LEGENDA}")
    print(f"{'=' * lebar}")
    for baris in peta:
        print("  " + " ".join(SIMBOL[sel] for sel in baris))
    print()

def cetak_statistik(stats: dict) -> None:
    print(f"\n[STATISTIK] {stats['label']}")
    print(f"{'─' * 40}")
    print(f"  Hutan Primer    : {stats['hutan_primer']:>4} sel")
    print(f"  Hutan Sekunder  : {stats['hutan_sekunder']:>4} sel")
    print(f"  Perkebunan      : {stats['perkebunan']:>4} sel")
    print(f"  Total Hutan     : {stats['total_hutan']:>4} sel ({stats['persentase_hutan']}%)")
    print(f"  Jumlah Patch    : {stats['jumlah_patch']:>4}")
    print(f"  Patch Terbesar  : {stats['patch_terbesar']:>4} sel")
    print(f"  Rata Patch      : {stats['rata_ukuran_patch']:>6} sel")

def cetak_langkah_ekspansi(urutan: list[dict], n_tampil: int = 5) -> None:
    tampil = urutan[:n_tampil]
    l_langkah = max(len(str(s["langkah"])) for s in tampil)
    l_posisi  = max(len(str(s["posisi"]))  for s in tampil)
    l_tipe    = max(len(s["tipe_asal"])    for s in tampil)
    for step in tampil:
        langkah = str(step["langkah"]).rjust(l_langkah)
        posisi  = str(step["posisi"]).ljust(l_posisi)
        tipe    = step["tipe_asal"].ljust(l_tipe)
        nilai   = f"{step['nilai_ekonomi']:.2f}"
        print(f"  Langkah {langkah}: sel {posisi} | {tipe} | nilai={nilai}")
    if len(urutan) > n_tampil:
        print(f"  ... (total {len(urutan)} langkah)")

def cetak_perbandingan(
    stats_awal: dict,
    stats_greedy: dict,
    stats_counter: dict,
    nilai_greedy: float,
    nilai_counter: float,) -> None:
    lebar = 62
    print(f"\n{'=' * lebar}")
    print("  PERBANDINGAN HASIL EKSPANSI")
    print(f"{'=' * lebar}")
    print(f"  {'Metrik':<28} {'Awal':>8} {'Greedy':>10} {'Counter-G':>10}")
    print(f"  {'─' * 58}")
    metrik = [
        ("Hutan Primer (sel)",   "hutan_primer"),
        ("Hutan Sekunder (sel)", "hutan_sekunder"),
        ("Total Hutan (sel)",    "total_hutan"),
        ("Hutan Tersisa (%)",    "persentase_hutan"),
        ("Perkebunan (sel)",     "perkebunan"),
        ("Jumlah Patch",         "jumlah_patch"),
        ("Patch Terbesar (sel)", "patch_terbesar"),
        ("Rata Ukuran Patch",    "rata_ukuran_patch"),]
    for nama, key in metrik:
        a = stats_awal[key]
        g = stats_greedy[key]
        c = stats_counter[key]
        print(f"  {nama:<28} {str(a):>8} {str(g):>10} {str(c):>10}")
    print(f"  {'─' * 58}")
    print(f"  {'Total Nilai Ekonomi':<28} {'':>8} "
          f"{str(nilai_greedy):>10} {str(nilai_counter):>10}")
    selisih_patch = stats_greedy["jumlah_patch"] - stats_counter["jumlah_patch"]
    selisih_hutan = stats_counter["total_hutan"] - stats_greedy["total_hutan"]
    selisih_nilai = round(nilai_greedy - nilai_counter, 2)
    print(f"\n  [KESIMPULAN]")
    print(f"  - Greedy menghasilkan {selisih_patch} patch lebih banyak (fragmentasi lebih parah)")
    print(f"  - Counter-Greedy menyisakan {selisih_hutan} sel hutan lebih banyak")
    print(f"  - Greedy unggul secara ekonomi sebesar +{selisih_nilai} poin")
    print(f"  - Trade-off: keuntungan ekonomi jangka pendek vs.")
    print(f"    kelestarian ekologi & lahan adat jangka panjang")
    print(f"{'=' * lebar}\n")