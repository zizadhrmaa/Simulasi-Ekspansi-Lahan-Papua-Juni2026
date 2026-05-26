"""
fragmentasi.py
Analisis fragmentasi hutan menggunakan BFS (connected components).
"""

from collections import deque
from konstanta import HUTAN_PRIMER, HUTAN_SEKUNDER, PERKEBUNAN

def hitung_patch_hutan(peta: list[list[int]]) -> list[list[tuple]]:
    n = len(peta)
    dikunjungi = [[False] * n for _ in range(n)]
    patches = []
    ARAH = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for start_i in range(n):
        for start_j in range(n):
            tipe = peta[start_i][start_j]
            if tipe in (HUTAN_PRIMER, HUTAN_SEKUNDER) and not dikunjungi[start_i][start_j]:
                patch = []
                antrian = deque([(start_i, start_j)])
                dikunjungi[start_i][start_j] = True
                while antrian:
                    ci, cj = antrian.popleft()
                    patch.append((ci, cj))
                    for di, dj in ARAH:
                        ni, nj = ci + di, cj + dj
                        if (0 <= ni < n and 0 <= nj < n
                                and not dikunjungi[ni][nj]
                                and peta[ni][nj] in (HUTAN_PRIMER, HUTAN_SEKUNDER)):
                            dikunjungi[ni][nj] = True
                            antrian.append((ni, nj))
                patches.append(patch)
    return patches

def analisis_fragmentasi(peta: list[list[int]], label: str) -> dict:
    n = len(peta)
    total_sel = n * n
    hp = sum(1 for i in range(n) for j in range(n) if peta[i][j] == HUTAN_PRIMER)
    hs = sum(1 for i in range(n) for j in range(n) if peta[i][j] == HUTAN_SEKUNDER)
    pk = sum(1 for i in range(n) for j in range(n) if peta[i][j] == PERKEBUNAN)
    total_hutan = hp + hs
    patches        = hitung_patch_hutan(peta)
    jumlah_patch   = len(patches)
    ukuran_patch   = [len(p) for p in patches]
    patch_terbesar = max(ukuran_patch) if ukuran_patch else 0
    rata_patch     = round(sum(ukuran_patch) / jumlah_patch, 2) if jumlah_patch else 0
    return {
        "label":             label,
        "total_sel":         total_sel,
        "hutan_primer":      hp,
        "hutan_sekunder":    hs,
        "total_hutan":       total_hutan,
        "persentase_hutan":  round(total_hutan / total_sel * 100, 1),
        "perkebunan":        pk,
        "jumlah_patch":      jumlah_patch,
        "patch_terbesar":    patch_terbesar,
        "rata_ukuran_patch": rata_patch,}