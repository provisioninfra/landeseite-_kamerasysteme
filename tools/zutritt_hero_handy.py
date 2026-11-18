#!/usr/bin/env python3
"""Zutrittssystem-Seite (ID 3316), 18.11.2026: Auf Handys im Hochformat liefen zwei Hero-Videos gleichzeitig – der
Desktop-Hero 74da297c (zutritt-hero-desktop-2560.mp4, 1,3 MB) und der darin verschachtelte Handy-Hero 601d5d0
(zutritt-hero-handy-1080-q17.mp4). Anders als auf der Startseite ist der Handy-Container hier ein Kind des Desktop-
Heros, deshalb greift die Querformat-Steuerung nicht. Lösung ohne Strukturänderung: beim Desktop-Hero „Auf Mobilgeräten
abspielen“ ausschalten (`background_play_on_mobile` entfernen) – unter 768 px lädt Elementor das Desktop-Video dann
nicht mehr, Überschrift und Handy-Video bleiben; ab 768 px (auch Handy quer) unverändert.
Aufruf: python3 -I tools/zutritt_hero_handy.py export.json ziel.json   (Ausgabe: Zahl der Änderungen)
"""
import json, pathlib, sys


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data):
    for e in walk(data["elements"]):
        if e.get("id") == "74da297c" and e.get("settings", {}).get("background_play_on_mobile"):
            del e["settings"]["background_play_on_mobile"]
            return data, 1
    return data, 0


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
