"""
main.py — Entry point simulasi.
Jalankan: python main.py
"""

from inisialisasi import buat_peta, buat_nilai_ekonomi
from runner import jalankan_skenario, tampilkan_skenario

def main() -> None:
    print("\n" + "=" * 62)
    print("  SIMULASI GREEDY EKSPANSI LAHAN PAPUA")
    print("  IF2211 Strategi Algoritma | Institut Teknologi Bandung")
    print("=" * 62)
    N    = 15
    SEED = 42
    peta_awal     = buat_peta(N, seed=SEED)
    nilai_ekonomi = buat_nilai_ekonomi(peta_awal, seed=SEED)
    print(f"\nGrid  : {N} x {N} = {N * N} sel total")
    print(f"Seed  : {SEED} (deterministik, reproducible)")
    for target in [40, 60, 80]:
        hasil = jalankan_skenario(peta_awal, nilai_ekonomi, target)
        tampilkan_skenario(hasil)

if __name__ == "__main__":
    main()