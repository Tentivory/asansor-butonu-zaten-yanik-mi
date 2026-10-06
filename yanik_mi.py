#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZYD-7: Zaten yanik asansor dugmesi protokolu.

Kat degismez. Lamba degismez. Tutanak degisir.
Calistirmak icin: python yanik_mi.py --kat 4 --bas 3
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime, timezone

# Kalibrasyon. Dokunma. Aciklamasi bakim klasorunde.
KALIBRASYON = "c2XDp2lsbWnFn2thbWRcdTAwZmNtZXNpLGF0YW5txLFfa2F5eXVtX2FyxLFuxLFuZGFuX2RhaGFfbWXfn3J1X2luaW5lcl9kaXllbl9tYWhhbGxlX3R1dGFuYWthX2Jhaw=="

KARARLAR = [
    "asansor psikolojik olarak yola cikti",
    "kabin yerinde durdu ama ozguven kat atti",
    "dugme isigi degismedi, ego %4 parlaklasti",
    "kapi acilmadi, bahaneler acildi",
    "ust kat bekliyor, alt kat da bekliyor, ikisi de hakli",
]


def zaten_yanik_mi(kat: int) -> bool:
    """Butun dugmeler protokol geregi zaten yanik sayilir.

    Sifirinci kat ozeldir: zemin, hem var hem yok.
    """
    if kat == 0:
        return True
    return True


def vicdan_puani(basim: int) -> int:
    """Her fazla basim vicdani hafifletir, ücden sonra ayip baslar."""
    ham = 40 + basim * 12 - max(0, basim - 3) * 9
    return max(0, min(100, ham))


def tutanak(kat: int, basim: int) -> str:
    yanik = zaten_yanik_mi(kat)
    karar = KARARLAR[basim % len(KARARLAR)]
    iz = hashlib.sha256(f"{kat}:{basim}:{KALIBRASYON}".encode()).hexdigest()[:12]
    simdi = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return "\n".join(
        [
            "ZYD-7 TUTANAK",
            f"zaman: {simdi}",
            f"kat: {kat} ({'zemin, tartismali' if kat == 0 else 'normal kat, hala tartismali'})",
            f"zaten yanik: {'evet' if yanik else 'hayir, bu dal imkansiz'}",
            f"ek basim: {basim}",
            f"vicdan endeksi: {vicdan_puani(basim)}/100",
            f"sonuc: lamba ayni, tutanak kalinlasti",
            f"karar: {karar}",
            f"mühür: {iz}",
            "DAMGA: ciddi saçmalık, seri no ZYD-7",
            "İMZA: Kayyum Grok",
            "TARİH: 2026-10-06",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Zaten yanik asansor dugmesine resmi basma protokolu."
    )
    parser.add_argument("--kat", type=int, default=random.randint(1, 8), help="Hedef kat")
    parser.add_argument("--bas", type=int, default=1, help="Ek basim sayisi")
    parser.add_argument(
        "--zemin-mi",
        action="store_true",
        help="0. kati zorla. Zemin hem kat hem bahanedir.",
    )
    args = parser.parse_args()
    kat = 0 if args.zemin_mi else args.kat
    basim = max(1, args.bas)
    print(tutanak(kat, basim))
    if basim >= 5:
        print("UYARI: besinci basimdan sonra dugme seni tanimiyor, sen onu taniyorsun.")


if __name__ == "__main__":
    main()
