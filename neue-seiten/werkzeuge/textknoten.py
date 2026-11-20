"""Sichtbare Textknoten eines HTML-Widgets ziehen / zurückschreiben.
ziehen <export.json> <widget-id> <knoten.json>   |   anwenden <export.json> <widget-id> <alt.json> <neu.json> <ausgabe.json>"""
import json, re, sys
TOK = re.compile(r'(<!--.*?-->|<script\b.*?</script\s*>|<style\b.*?</style\s*>|<[^>]+>)', re.S | re.I)
def knoten(html):
    out = []; pos = 0
    for m in TOK.finditer(html):
        if m.start() > pos: out.append((pos, m.start()))
        pos = m.end()
    if pos < len(html): out.append((pos, len(html)))
    return [(a, b) for a, b in out if html[a:b].strip()]
def widget(exp, wid):
    def w(els):
        for e in els:
            if e['id'] == wid: return e
            r = w(e.get('elements', []))
            if r: return r
    return w(exp['elements'])
cmd, exp = sys.argv[1], json.load(open(sys.argv[2])); e = widget(exp, sys.argv[3]); h = e['settings']['html']
if cmd == 'ziehen':
    k = {str(i): h[a:b] for i, (a, b) in enumerate(knoten(h))}
    json.dump(k, open(sys.argv[4], 'w'), ensure_ascii=False, indent=1)
    print('knoten', len(k), 'wörter', sum(len(v.split()) for v in k.values()))
else:
    alt, neu = json.load(open(sys.argv[4])), json.load(open(sys.argv[5]))
    kn = knoten(h); assert len(kn) == len(alt), 'Knotenzahl anders'
    n = 0
    for i in sorted((int(x) for x in alt), reverse=True):
        a, b = kn[i]; assert h[a:b] == alt[str(i)], f'Knoten {i} geändert'
        if neu[str(i)] != alt[str(i)]: h = h[:a] + neu[str(i)] + h[b:]; n += 1
    e['settings']['html'] = h
    json.dump(exp, open(sys.argv[6], 'w'), ensure_ascii=False); print('geändert', n)
