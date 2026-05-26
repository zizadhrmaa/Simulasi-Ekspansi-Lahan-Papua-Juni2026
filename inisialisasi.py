"""
inisialisasi.py
Pembuatan grid peta lahan dan nilai ekonomi tiap sel.
"""

import random
from konstanta import HUTAN_PRIMER, HUTAN_SEKUNDER, LAHAN_TERBUKA

def buat_peta(n: int, seed: int = 42) -> list[list[int]]:
    random.seed(seed)
    peta = []
    for _ in range(n):
        baris = []
        for _ in range(n):
            r = random.random()
            if r < 0.50:
                baris.append(HUTAN_PRIMER)
            elif r < 0.75:
                baris.append(HUTAN_SEKUNDER)
            else:
                baris.append(LAHAN_TERBUKA)
        peta.append(baris)
    return peta

def buat_nilai_ekonomi(peta: list[list[int]], seed: int = 42) -> list[list[float]]:
    random.seed(seed + 1)
    n = len(peta)
    nilai = []
    for i in range(n):
        baris = []
        for j in range(n):
            tipe = peta[i][j]
            if tipe == HUTAN_PRIMER:
                baris.append(round(random.uniform(7.0, 10.0), 2))
            elif tipe == HUTAN_SEKUNDER:
                baris.append(round(random.uniform(4.0, 7.0), 2))
            else:
                baris.append(round(random.uniform(1.0, 4.0), 2))
        nilai.append(baris)
    return nilai