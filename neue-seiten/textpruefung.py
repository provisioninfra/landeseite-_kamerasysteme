"""Prüft die Texte einer gebauten Seite auf Stilregeln des Kunden.
Regeln: keine Gedankenstriche, keine vorhersehbaren Muster („nicht nur … sondern auch“, „X, nicht Y“, „statt … zu“ gehäuft),
keine auffälligen Dreiergruppen („A, B und C“ als Aufzählungsmuster), keine vagen Autoritäten („Experten sagen“, „Studien zeigen“)."""
import json, re, sys, html
SKIP = {'custom_css', 'html', '_title', 'uich_custom_css_field'}
def texte(els):
    out = []
    def w(e):
        s = e['settings']
        for k, v in s.items():
            if k in SKIP: continue
            if isinstance(v, str) and re.search(r'[a-zäöü]{4,} [a-zäöü]{3,}', v): out.append((e['id'], k, v))
            elif isinstance(v, list):
                for it in v:
                    if isinstance(it, dict):
                        for kk, vv in it.items():
                            if isinstance(vv, str) and re.search(r'[a-zäöü]{4,} [a-zäöü]{3,}', vv): out.append((e['id'], k + '.' + kk, vv))
        for c in e.get('elements', []): w(c)
    for e in els: w(e)
    return out
REGELN = [
 ('Gedankenstrich', re.compile(r'\s[–—-]\s|[–—]')),
 ('nicht nur/sondern', re.compile(r'nicht nur\b.*\bsondern', re.I)),
 ('X, nicht Y', re.compile(r',\s+nicht\s+(?:nach|bei|aus|in|für|mit|erst|der|die|das|dem|den|ein|eine|einer)\b', re.I)),
 ('statt-Konstruktion', re.compile(r'\bstatt\b', re.I)),
 ('vage Autorität', re.compile(r'(Experten|Fachleute|Studien|Untersuchungen|Kenner)\s+(sagen|zeigen|empfehlen|raten|wissen)|laut Experten|wie viele wissen', re.I)),
 ('Dreiergruppe', re.compile(r'\b[\wäöüÄÖÜß-]+(?:\s[\wäöüÄÖÜß-]+)?,\s[\wäöüÄÖÜß-]+(?:\s[\wäöüÄÖÜß-]+)?\s(?:und|oder)\s[\wäöüÄÖÜß-]+')),
 ('ohne-Reihe', re.compile(r'ohne [^,.]+, ohne [^,.]+', re.I)),
]
def pruefe(path, ignoriere_ids=()):
    d = json.load(open(path, encoding='utf-8'))
    funde = []
    for eid, k, v in texte(d['elements']):
        if eid in ignoriere_ids: continue
        t = html.unescape(re.sub('<[^>]+>', ' ', v))
        for name, rx in REGELN:
            for m in rx.finditer(t):
                funde.append((name, eid, k, t[max(0, m.start()-50):m.end()+50].replace('\n', ' ')))
    return funde
if __name__ == '__main__':
    ign = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else set()
    f = pruefe(sys.argv[1], ign)
    from collections import Counter
    print(Counter(x[0] for x in f))
    for x in f: print(f'  {x[0]:18} {x[1]} {x[2][:22]:22} …{x[3]}…')
