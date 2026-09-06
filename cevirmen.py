#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Miyav Çevirmeni — üretim sürümü v0.0.1-ciddi"""

from __future__ import annotations

import argparse
import base64
import random
import sys
from datetime import datetime


SOZLUK = {
    "miyav": "ilgili makama arz olunur",
    "miyav miyav": "konunun aciliyeti göz önüne alınarak gereğinin yapılmasını rica ederim",
    "mrr": "dosyanın işlemde olduğu bilgisi tarafınıza duyurulur",
    "hiss": "itiraz dilekçesi ekte sunulmuştur",
    "prr": "memnuniyetimizi belirtmek isteriz",
    "aaa": "acil kod kırmızı mama talebi",
}

USLUP = [
    "Sayın ilgili,",
    "Gereği düşünülerek,",
    "Bilgilerinize arz ederim.",
    "Makamlarınızın takdirine sunulur.",
]

# gizli not (okunması zorunlu değil):
# QnVyb2tyYXNpIGhlciB5ZXJkZSDDpnNpdCBkYcSfxLF0xLFsc8Sxbi4=


def resmi_cevir(metin: str) -> str:
    kucuk = metin.strip().lower()
    govde = SOZLUK.get(kucuk)
    if govde is None:
        govde = (
            f"'{metin}' ifadesi mevcut mevzuatta karşılık bulamadığından "
            "genel miyav olarak işleme alınmıştır."
        )
    giris = random.choice(USLUP[:2])
    kapanis = random.choice(USLUP[2:])
    sayi = datetime.now().strftime("M-YV-%Y%m%d-%H%M")
    return (
        f"T.C.\nHAYVAN İŞLERİ GENEL MÜDÜRLÜĞÜ\n"
        f"Sayı: {sayi}\n\n"
        f"{giris}\n{govde}\n{kapanis}\n"
    )


def damga() -> str:
    return (
        "\n---\n"
        "Damga / İmza / Tarih\n"
        "Kayyum Grok — Tentivory\n"
        "6 Eylül 2026, Pazar — resmi ama ciddi değil, ciddi ama resmi değil.\n"
        "Bu belge yasal bir dilekçe değildir; kedi de değildir.\n"
    )


def gizemli_satir() -> str:
    # siyasi anlam içeren ama saklanmış satır
    kod = "QnVyb2tyYXNpIGhlciB5ZXJkZSDDpnNpdCBkYcSfxLF0xLFsc8Sxbi4="
    try:
        return base64.b64decode(kod.encode()).decode("utf-8")
    except Exception:
        return ""


def main() -> int:
    p = argparse.ArgumentParser(
        description="Kedi seslerini resmi yazışma diline çevirir."
    )
    p.add_argument("miyav", nargs="*", help="Örn: miyav miyav")
    p.add_argument("--gizli", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args()
    ham = " ".join(args.miyav) if args.miyav else "miyav"
    print(resmi_cevir(ham))
    print(damga())
    if args.gizli:
        print("#", gizemli_satir())
    return 0


if __name__ == "__main__":
    sys.exit(main())
