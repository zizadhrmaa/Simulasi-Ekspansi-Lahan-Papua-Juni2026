"""
runner.py
Fungsi untuk menjalankan dan menampilkan satu skenario simulasi lengkap.
"""

from algoritma import greedy_ekspansi, counter_greedy_ekspansi
from fragmentasi import analisis_fragmentasi
from visualisasi import (cetak_peta, cetak_statistik, cetak_langkah_ekspansi, cetak_perbandingan,)

def jalankan_skenario(peta_awal: list[list[int]], nilai_ekonomi: list[list[float]], target_luas: int,) -> dict:
    peta_greedy,  eks_greedy,  nilai_greedy  = greedy_ekspansi(
        peta_awal, nilai_ekonomi, target_luas)
    peta_counter, eks_counter, nilai_counter = counter_greedy_ekspansi(
        peta_awal, nilai_ekonomi, target_luas)
    return {
        "target_luas":    target_luas,
        "peta_awal":      peta_awal,
        "peta_greedy":    peta_greedy,
        "peta_counter":   peta_counter,
        "eks_greedy":     eks_greedy,
        "eks_counter":    eks_counter,
        "nilai_greedy":   nilai_greedy,
        "nilai_counter":  nilai_counter,
        "stats_awal":     analisis_fragmentasi(peta_awal,    "Kondisi Awal"),
        "stats_greedy":   analisis_fragmentasi(peta_greedy,  "Setelah Greedy"),
        "stats_counter":  analisis_fragmentasi(peta_counter, "Setelah Counter-Greedy"),
    }

def tampilkan_skenario(hasil: dict) -> None:
    """Mencetak seluruh output satu skenario ke stdout."""
    t = hasil["target_luas"]
    print(f"\n{'#' * 62}")
    print(f"  SKENARIO: TARGET KONVERSI = {t} SEL")
    print(f"{'#' * 62}")
    cetak_peta(hasil["peta_awal"], "PETA AWAL (baseline)")
    cetak_statistik(hasil["stats_awal"])
    print("\n[GREEDY] 5 langkah pertama:")
    cetak_langkah_ekspansi(hasil["eks_greedy"])
    print(f"  Total nilai ekonomi Greedy: {hasil['nilai_greedy']}")
    cetak_peta(hasil["peta_greedy"], "PETA SETELAH GREEDY")
    cetak_statistik(hasil["stats_greedy"])
    print("\n[COUNTER-GREEDY] 5 langkah pertama:")
    cetak_langkah_ekspansi(hasil["eks_counter"])
    print(f"  Total nilai ekonomi Counter-Greedy: {hasil['nilai_counter']}")
    cetak_peta(hasil["peta_counter"], "PETA SETELAH COUNTER-GREEDY")
    cetak_statistik(hasil["stats_counter"])
    cetak_perbandingan(
        hasil["stats_awal"],
        hasil["stats_greedy"],
        hasil["stats_counter"],
        hasil["nilai_greedy"],
        hasil["nilai_counter"],
    )