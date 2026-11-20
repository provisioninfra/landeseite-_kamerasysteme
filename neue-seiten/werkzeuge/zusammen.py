"""Baut je Bestandsseite bestand/<ID>-ALT.json und -NEU.json (vollständige Feldsets) für texte_bestand.py anwenden.
Aufruf: python3 -I zusammen.py <ID> [...]"""
import json, re, sys, subprocess, os
W = os.path.dirname(os.path.abspath(__file__))
T = '/home/user/landeseite-_kamerasysteme/neue-seiten/werkzeuge/texte_bestand.py'
ORTE = {'4496', '4605', '4735', '4739', '4743', '4747', '4751', '4755', '4759', '4763', '4767', '4771', '4775', '4779', '4783'}
ABLAUF = ['20734e0', '8595654', '2f2676e', '933e53d', 'd11be39']
def plain(h): return re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', h)).strip()
for pid in sys.argv[1:]:
    exp = f'{W}/../footer/page-{pid}-vorher.json'
    subprocess.run(['python3', '-I', T, 'ziehen', exp, f'{W}/{pid}-ALT.json'], check=True, capture_output=True)
    alt = json.load(open(f'{W}/{pid}-ALT.json'))
    neu = dict(alt)
    teile = [f'{W}/{pid}-eigen-neu.json', f'{W}/ort-gemeinsam-neu.json'] if pid in ORTE else [f'{W}/{pid}-neu.json']
    for t in teile:
        for k, v in json.load(open(t)).items():
            assert k in alt, (pid, t, k)
            neu[k] = v
    for i, did in enumerate(ABLAUF):
        k = f'756a14f|eael_coustom_content_posts.{i}.eael_custom_excerpt'
        if k in alt and f'{did}|editor' in neu:
            v = neu[f'{did}|editor']
            neu[k] = v if alt[k].lstrip().startswith('<') else plain(v)
    json.dump(neu, open(f'{W}/{pid}-NEU.json', 'w'), ensure_ascii=False, indent=1)
    print(pid, 'Felder', len(alt), 'geändert', sum(1 for k in alt if alt[k] != neu[k]))
