"""
buat_gambar.py
Menghasilkan gambar-gambar untuk makalah:
  fig_grid_awal.png       -- kondisi awal grid
  fig_grid_greedy60.png   -- setelah Greedy 60 sel
  fig_grid_counter60.png  -- setelah Counter-Greedy 60 sel
  fig_chart_patch.png     -- bar chart multi-skenario
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from inisialisasi import buat_peta, buat_nilai_ekonomi
from algoritma import greedy_ekspansi, counter_greedy_ekspansi
from konstanta import HUTAN_PRIMER, HUTAN_SEKUNDER, LAHAN_TERBUKA, PERKEBUNAN

WARNA = {
    HUTAN_PRIMER:   "#2d6a4f", 
    HUTAN_SEKUNDER: "#95d5b2",
    LAHAN_TERBUKA:  "#d9d9d9",
    PERKEBUNAN:     "#c0392b", }
NAMA = {
    HUTAN_PRIMER:   "Hutan Primer",
    HUTAN_SEKUNDER: "Hutan Sekunder",
    LAHAN_TERBUKA:  "Lahan Terbuka",
    PERKEBUNAN:     "Perkebunan",}

def peta_ke_rgb(peta):
    n = len(peta)
    img = np.zeros((n, n, 3))
    for i in range(n):
        for j in range(n):
            hex_color = WARNA[peta[i][j]].lstrip("#")
            r, g, b = (int(hex_color[k:k+2], 16) / 255 for k in (0, 2, 4))
            img[i, j] = [r, g, b]
    return img

def legenda_patches(tipe_list):
    return [mpatches.Patch(color=WARNA[t], label=NAMA[t]) for t in tipe_list]

def simpan_grid(peta, judul, nama_file, tipe_legenda):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(peta_ke_rgb(peta), interpolation="nearest", aspect="equal")
    n = len(peta)
    for x in range(n + 1):
        ax.axhline(x - 0.5, color="white", linewidth=0.4)
        ax.axvline(x - 0.5, color="white", linewidth=0.4)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(judul, fontsize=11, pad=8)
    ax.legend(
        handles=legenda_patches(tipe_legenda),
        loc="upper center",
        bbox_to_anchor=(0.5, -0.04),
        ncol=2,
        fontsize=8,
        frameon=True,)
    plt.tight_layout()
    plt.savefig(nama_file, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Tersimpan: {nama_file}")

def simpan_chart_patch(data, nama_file):
    skenarios = ["40 Sel", "60 Sel", "80 Sel"]
    g_count  = [data[s]["greedy"][0]  for s in ["40", "60", "80"]]
    cg_count = [data[s]["counter"][0] for s in ["40", "60", "80"]]
    g_max    = [data[s]["greedy"][1]  for s in ["40", "60", "80"]]
    cg_max   = [data[s]["counter"][1] for s in ["40", "60", "80"]]
    x = np.arange(len(skenarios))
    w = 0.35
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))
    bars1 = ax1.bar(x - w/2, g_count,  w, label="Greedy",         color="#c0392b", alpha=0.85)
    bars2 = ax1.bar(x + w/2, cg_count, w, label="Counter-Greedy", color="#2d6a4f", alpha=0.85)
    ax1.set_xticks(x)
    ax1.set_xticklabels(skenarios)
    ax1.set_ylabel("Jumlah Patch")
    ax1.set_title("Jumlah Patch Hutan")
    ax1.legend(fontsize=9)
    ax1.bar_label(bars1, padding=3, fontsize=9)
    ax1.bar_label(bars2, padding=3, fontsize=9)
    ax1.set_ylim(0, max(g_count) * 1.2)
    bars3 = ax2.bar(x - w/2, g_max,  w, label="Greedy",         color="#c0392b", alpha=0.85)
    bars4 = ax2.bar(x + w/2, cg_max, w, label="Counter-Greedy", color="#2d6a4f", alpha=0.85)
    ax2.set_xticks(x)
    ax2.set_xticklabels(skenarios)
    ax2.set_ylabel("Ukuran Patch Terbesar (sel)")
    ax2.set_title("Patch Terbesar")
    ax2.legend(fontsize=9)
    ax2.bar_label(bars3, padding=3, fontsize=9)
    ax2.bar_label(bars4, padding=3, fontsize=9)
    ax2.set_ylim(0, 200)
    fig.suptitle("Perbandingan Fragmentasi: Greedy vs Counter-Greedy", fontsize=12)
    plt.tight_layout()
    plt.savefig(nama_file, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Tersimpan: {nama_file}")

def main():
    print("Membangkitkan data simulasi...")
    peta_awal = buat_peta(15, seed=42)
    nilai     = buat_nilai_ekonomi(peta_awal, seed=42)
    peta_g40, _, _  = greedy_ekspansi(peta_awal, nilai, 40)
    peta_g60, _, _  = greedy_ekspansi(peta_awal, nilai, 60)
    peta_g80, _, _  = greedy_ekspansi(peta_awal, nilai, 80)
    peta_cg40, _, _ = greedy_ekspansi.__wrapped__(peta_awal, nilai, 40) if hasattr(greedy_ekspansi, '__wrapped__') else (None, None, None)
    from algoritma import counter_greedy_ekspansi
    peta_cg40, _, _ = counter_greedy_ekspansi(peta_awal, nilai, 40)
    peta_cg60, _, _ = counter_greedy_ekspansi(peta_awal, nilai, 60)
    peta_cg80, _, _ = counter_greedy_ekspansi(peta_awal, nilai, 80)
    print("Menyimpan gambar grid...")
    simpan_grid(
        peta_awal,
        "Kondisi Awal (Baseline) — 169 sel hutan, 2 patch",
        "gambar/fig_grid_awal.png",
        [HUTAN_PRIMER, HUTAN_SEKUNDER, LAHAN_TERBUKA],)
    simpan_grid(
        peta_g60,
        "Setelah Greedy (60 sel) — 30 patch, terbesar 17 sel",
        "gambar/fig_grid_greedy60.png",
        [HUTAN_PRIMER, HUTAN_SEKUNDER, LAHAN_TERBUKA, PERKEBUNAN],)
    simpan_grid(
        peta_cg60,
        "Setelah Counter-Greedy (60 sel) — 2 patch, terbesar 164 sel",
        "gambar/fig_grid_counter60.png",
        [HUTAN_PRIMER, HUTAN_SEKUNDER, LAHAN_TERBUKA, PERKEBUNAN],)
    print("Menyimpan chart multi-skenario...")
    from fragmentasi import analisis_fragmentasi
    data = {}
    for target, pg, pcg in [("40", peta_g40, peta_cg40), ("60", peta_g60, peta_cg60), ("80", peta_g80, peta_cg80),]:
        sg  = analisis_fragmentasi(pg,  "g")
        scg = analisis_fragmentasi(pcg, "cg")
        data[target] = {
            "greedy":  (sg["jumlah_patch"],  sg["patch_terbesar"]),
            "counter": (scg["jumlah_patch"], scg["patch_terbesar"]),}
    simpan_chart_patch(data, "gambar/fig_chart_patch.png")

if __name__ == "__main__":
    main()