"""
algoritma.py
Implementasi Greedy dan Counter-Greedy untuk ekspansi lahan.
"""

import copy
from konstanta import HUTAN_PRIMER, HUTAN_SEKUNDER, LAHAN_TERBUKA, PERKEBUNAN, LABEL

def _konversi_kandidat(
    peta_awal: list[list[int]], 
    nilai_ekonomi: list[list[float]], 
    kandidat_terurut: list[tuple], 
    target_luas: int,) -> tuple:
    peta = copy.deepcopy(peta_awal)
    urutan_ekspansi = []
    total_nilai = 0.0
    for k in range(min(target_luas, len(kandidat_terurut))):
        i, j = kandidat_terurut[k]
        tipe_asal = peta[i][j]
        peta[i][j] = PERKEBUNAN
        nilai = nilai_ekonomi[i][j]
        total_nilai += nilai
        urutan_ekspansi.append({
            "langkah":       k + 1,
            "posisi":        (i, j),
            "tipe_asal":     LABEL[tipe_asal],
            "nilai_ekonomi": nilai,})
    return peta, urutan_ekspansi, round(total_nilai, 2)

def greedy_ekspansi(
    peta_awal: list[list[int]],
    nilai_ekonomi: list[list[float]],
    target_luas: int,) -> tuple:
    n = len(peta_awal)
    kandidat = [(i, j) for i in range(n) for j in range(n) if peta_awal[i][j] != PERKEBUNAN]
    kandidat.sort(key=lambda pos: nilai_ekonomi[pos[0]][pos[1]], reverse=True)
    return _konversi_kandidat(peta_awal, nilai_ekonomi, kandidat, target_luas)

def counter_greedy_ekspansi(
    peta_awal: list[list[int]],
    nilai_ekonomi: list[list[float]],
    target_luas: int,) -> tuple:
    n = len(peta_awal)
    urutan_tipe = {LAHAN_TERBUKA: 0, HUTAN_SEKUNDER: 1, HUTAN_PRIMER: 2}
    kandidat = [(i, j) for i in range(n) for j in range(n) if peta_awal[i][j] != PERKEBUNAN]
    kandidat.sort(key=lambda pos: (urutan_tipe[peta_awal[pos[0]][pos[1]]],-nilai_ekonomi[pos[0]][pos[1]]))
    return _konversi_kandidat(peta_awal, nilai_ekonomi, kandidat, target_luas)