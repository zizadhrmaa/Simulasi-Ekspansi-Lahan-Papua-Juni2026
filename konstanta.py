"""
konstanta.py
Definisi tipe lahan, label, dan simbol ASCII.
"""

HUTAN_PRIMER   = 0
HUTAN_SEKUNDER = 1
LAHAN_TERBUKA  = 2
PERKEBUNAN     = 3

LABEL = {
    HUTAN_PRIMER:   "Hutan Primer",
    HUTAN_SEKUNDER: "Hutan Sekunder",
    LAHAN_TERBUKA:  "Lahan Terbuka",
    PERKEBUNAN:     "Perkebunan",}

SIMBOL = {
    HUTAN_PRIMER:   "#",  
    HUTAN_SEKUNDER: "*", 
    LAHAN_TERBUKA:  ".",  
    PERKEBUNAN:     "@",}

LEGENDA = (
    "Legenda: # = Hutan Primer | * = Hutan Sekunder | "
    ". = Lahan Terbuka | @ = Perkebunan")