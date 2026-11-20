"""Übernimmt den Kopf-Container 192a273 aus dem frischen Export in den Neubau und zeigt alle übrigen Unterschiede.
Aufruf: python3 -I kopf_uebernehmen.py <frisch.json> <neubau.json> <ausgabe.json>"""
import json, sys, os
frisch, neu = (json.load(open(p)) for p in sys.argv[1:3])
KOEPFE = os.environ.get('UEBERNEHMEN', '192a273').split(',')
KOPF = KOEPFE[0]
def idx(els, d=None, inkopf=False):
    d = {} if d is None else d
    for e in els:
        k = inkopf or e['id'] in KOEPFE
        d[e['id']] = (e, k); idx(e.get('elements', []), d, k)
    return d
FK = {e['id']: e for e in frisch['elements'] if e['id'] in KOEPFE}
assert set(FK) == set(KOEPFE), 'Container fehlt im frischen Export'
assert all(any(e['id'] == k for e in neu['elements']) for k in KOEPFE), 'Container fehlt im Neubau'
out = dict(neu); out['elements'] = [FK.get(e['id'], e) for e in neu['elements']]
F, N = idx(frisch['elements']), idx(out['elements'])
nurf = [i for i in F if i not in N]; nurn = [i for i in N if i not in F]
print('nur im frischen Export:', len(nurf), nurf[:30])
print('nur im Neubau:', len(nurn), nurn[:30])
TEXT = {'title', 'editor', 'text', 'description_text', 'title_text', 'eael_adv_accordion_tab', 'tabs', 'html', 'testimonial_content',
        'button_text', 'link', '_title', 'icon_list', 'inner_text', 'list', 'slides'}
andere = {}
for i, (e, k) in N.items():
    if k or i not in F: continue
    a, b = F[i][0].get('settings', {}), e.get('settings', {})
    for key in set(a) | set(b):
        if a.get(key) != b.get(key):
            andere.setdefault('text' if key in TEXT else 'SONST', []).append((i, key))
print('geänderte Text-Settings:', len(andere.get('text', [])))
print('geänderte sonstige Settings:', andere.get('SONST', []))
json.dump(out, open(sys.argv[3], 'w'), ensure_ascii=False)
