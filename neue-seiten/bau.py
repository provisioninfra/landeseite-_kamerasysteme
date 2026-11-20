"""Baukasten für neue Seiten auf Basis eines frischen Elementor-Exports (Vorlage: Uelzen, 4605).

Eine Seiten-Spezifikation (Python-Modul mit SPEC-Dict) legt fest:
  set      {element_id: {setting: wert}}       Texte/Einstellungen je Element
  remove   [element_id, ...]                   ganze Abschnitte/Elemente entfernen
  clone    [(quelle_id, ziel_parent_id, nach_id, {alt_id: {setting: wert}}), ...]
  ablauf   {schritt_titel: html}               Ablauf (Computer-Widgets und Handy-Timeline)
  faq      [(frage, antwort_html), ...]        Akkordeon ed852c3 (erzeugt FAQPage-Schema)
  schema   dict                                JSON-LD im Widget f058554
  menu     Menü-Slug für Kopf- und Fußnavigation
  title    WordPress-Seitentitel
  seo      Yoast-Werte
  erlaubt  Wörter aus der Vorlage, die auf der neuen Seite vorkommen dürfen
"""
import json, copy, random, re, sys, importlib.util

def walk(els, f, parent=None):
    for e in els:
        f(e, parent)
        walk(e.get('elements', []), f, e)

def find(els, eid):
    hit = []
    walk(els, lambda e, p: hit.append((e, p)) if e['id'] == eid else None)
    if not hit: raise KeyError(eid)
    return hit[0]

def all_ids(els):
    s = set(); walk(els, lambda e, p: s.add(e['id'])); return s

def new_id(ids):
    while True:
        i = '%07x' % random.randrange(16**7)
        if i not in ids and not i.isdigit(): ids.add(i); return i

def reid(e, ids, mapping):
    nid = new_id(ids); mapping[e['id']] = nid; e['id'] = nid
    for c in e.get('elements', []): reid(c, ids, mapping)

def build(template_path, spec):
    d = json.load(open(template_path, encoding='utf-8'))
    els, settings = d['elements'], d['settings']
    ids = all_ids(els)
    TOP0 = set(e['id'] for e in els)
    # Bausteine der Startseite einsetzen (IDs bleiben, außer reid=True)
    if spec.get('graft'):
        import os
        B = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'startseite-bausteine.json'), encoding='utf-8'))
        for g in spec['graft']:
            bid, after, sets = g[0], g[1], g[2]; neu_ids = len(g) > 3 and g[3]
            c = copy.deepcopy(B[bid]); m = {}
            if neu_ids: reid(c, ids, m)
            else:
                walk([c], lambda e, p: ids.add(e['id'])); m = None; TOP0.add(c['id'])
            pos = [k['id'] for k in els].index(after) + 1
            els.insert(pos, c)
            for old, vals in sets.items():
                x, _ = find([c], m[old] if m else old); x['settings'].update(vals)
        if spec.get('handy_css'):
            e, _ = find(els, 'b1ab0ce'); e['settings']['html'] = e['settings']['html'] + '\n' + B['__handy_css']
    # Klone (Quellen sind Original-IDs), danach Texte setzen
    for src, parent_id, after_id, sets in spec.get('clone', []):
        e, _ = find(els, src)
        c = copy.deepcopy(e); m = {}; reid(c, ids, m)
        parent, _ = find(els, parent_id) if parent_id else ({'elements': els}, None)
        kids = parent['elements']
        pos = [k['id'] for k in kids].index(after_id) + 1
        kids.insert(pos, c)
        for old, vals in sets.items():
            if old == '__remove__':
                for r in vals:
                    x, p = find([c], m[r]); p['elements'].remove(x)
                continue
            x, _ = find([c], m[old]); x['settings'].update(vals)
    # Artikel-Karten: Karte 94cb6e5 (Überschrift 8cc96a4, Text 71be80d, Kurzfassung 59a04cb) als Vorlage, übrige Karten entfernen
    if spec.get('karten'):
        cont, _ = find(els, 'c5f5120')
        vorlage = next(k for k in cont['elements'] if k['id'] == '94cb6e5')
        neu = []
        for i, (titel, text, kurz) in enumerate(spec['karten']):
            c = copy.deepcopy(vorlage); m = {}
            if i: reid(c, ids, m)
            else: m = {x: x for x in ('94cb6e5', '8cc96a4', '71be80d', '59a04cb')}
            c['settings']['_title'] = titel[:40]
            find([c], m['8cc96a4'])[0]['settings']['title'] = titel
            find([c], m['71be80d'])[0]['settings']['editor'] = text
            if kurz: find([c], m['59a04cb'])[0]['settings']['editor'] = kurz
            else:
                fb, fp = find([c], m['59a04cb']); box, bp = find([c], fp['id']); bp['elements'].remove(box)
            neu.append(c)
        cont['elements'] = neu
    for eid in spec.get('remove', []):
        e, p = find(els, eid)
        (p['elements'] if p else els).remove(e)
    for eid, vals in spec.get('set', {}).items():
        e, _ = find(els, eid); e['settings'].update(vals)
    # Ablauf: Computer-Variante (Überschrift + folgender Text) und Handy-Timeline
    if spec.get('ablauf'):
        ab = spec['ablauf']
        def f(e, p):
            if e.get('widgetType') == 'heading' and p is not None:
                t = re.sub('<[^>]+>', '', e['settings'].get('title', '')).strip()
                if t in ab:
                    sib = p['elements']; i = sib.index(e)
                    for nxt in sib[i+1:]:
                        if nxt.get('widgetType') == 'text-editor': nxt['settings']['editor'] = ab[t]; break
            if e.get('widgetType') == 'eael-content-timeline':
                for post in e['settings'].get('eael_coustom_content_posts', []):
                    t = re.sub('<[^>]+>', '', post.get('eael_custom_title', '')).strip()
                    if t in ab: post['eael_custom_excerpt'] = ab[t]
        walk(els, f)
    if spec.get('faq'):
        acc, _ = find(els, 'ed852c3')
        tmpl = acc['settings']['eael_adv_accordion_tab'][0]
        tabs = []
        for q, a in spec['faq']:
            t = copy.deepcopy(tmpl); t['_id'] = new_id(ids)[:7]
            t['eael_adv_accordion_tab_title'] = q; t['eael_adv_accordion_tab_content'] = a
            tabs.append(t)
        acc['settings']['eael_adv_accordion_tab'] = tabs
    if spec.get('schema'):
        e, _ = find(els, 'f058554')
        e['settings']['html'] = '<script type="application/ld+json">' + json.dumps(spec['schema'], ensure_ascii=False) + '</script>'
    if spec.get('menu'):
        def setmenu(e, p):
            if e.get('widgetType') == 'nav-menu':
                e['settings']['menu'] = spec['menu'] if e['id'] == '2a487ab' else spec.get('menu_footer', spec['menu'])
        walk(els, setmenu)
    # Reihenfolge der Hauptabschnitte wie auf der Startseite; Klone mit neuen IDs bleiben hinter ihrem Vorgänger
    if spec.get('order'):
        order = spec['order']; groups = []
        for e in els:
            if e['id'] in TOP0 or not groups: groups.append([e])
            else: groups[-1].append(e)
        groups.sort(key=lambda g: (0, order.index(g[0]['id'])) if g[0]['id'] in order else (1, 0))
        els[:] = [e for g in groups for e in g]
    settings['post_title'] = spec['title']
    # Prüfungen
    texte = []
    def coll(v):
        if isinstance(v, str): texte.append(v)
        elif isinstance(v, list): [coll(x) for x in v]
        elif isinstance(v, dict): [coll(x) for k, x in v.items() if k not in ('custom_css',)]
    walk(els, lambda e, p: coll(e['settings']))
    blob = '\n'.join(texte)
    rest = []
    for w in spec.get('verboten', []):
        for m in re.finditer(re.escape(w), blob):
            ctx = blob[max(0, m.start()-60):m.end()+60].replace('\n', ' ')
            if not any(ok in ctx for ok in spec.get('erlaubt', [])): rest.append((w, ctx))
    ids2 = []; walk(els, lambda e, p: ids2.append(e['id']))
    anker = []; walk(els, lambda e, p: anker.append(e['settings']['_element_id']) if e['settings'].get('_element_id') else None)
    assert len(anker) == len(set(anker)), ('doppelte Anker', anker)
    assert len(ids2) == len(set(ids2)), 'doppelte IDs'
    assert len(spec['seo']['title']) <= 60, ('Titel zu lang', len(spec['seo']['title']))
    assert len(spec['seo']['description']) <= 158, ('Description zu lang', len(spec['seo']['description']))
    return {'elements': els, 'settings': settings, 'seo': spec['seo'], 'slug': spec['slug']}, rest

def text_export(data):
    out = []
    def strip(s): return re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', s.replace('<br>', ' '))).strip()
    def f(e, p):
        s = e['settings']; w = e.get('widgetType')
        if w == 'heading': out.append(('## ' if s.get('header_size') in ('h1', 'h2') else '') + strip(s.get('title', '')))
        elif w == 'text-editor': out.append(strip(s.get('editor', '')))
        elif w == 'button': out.append('[Button] ' + strip(s.get('text', '')) + ' → ' + str((s.get('link') or {}).get('url')))
        elif w == 'eael-adv-accordion':
            for t in s['eael_adv_accordion_tab']: out.append('**FAQ:** ' + strip(t['eael_adv_accordion_tab_title']) + '\n' + strip(t['eael_adv_accordion_tab_content']))
        elif w == 'icon-box': out.append(strip(s.get('description_text', '')))
        elif w == 'image-box': out.append(strip(s.get('title_text', '')) + ' – ' + strip(s.get('description_text', '')))
        if w in ('heading', 'text-editor', 'eael-adv-accordion', 'button', 'icon-box', 'image-box'): out.append('')
    walk(data['elements'], f)
    return '\n'.join(out)

if __name__ == '__main__':
    tpl, spec_path, out = sys.argv[1:4]
    sp = importlib.util.spec_from_file_location('spec', spec_path); mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    data, rest = build(tpl, mod.SPEC)
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    open(out.replace('.json', '-texte.md'), 'w', encoding='utf-8').write(text_export(data))
    n = len(all_ids(data['elements']))
    print('gebaut:', out, 'elemente', n, '| Reste aus der Vorlage:', len(rest))
    for w, ctx in rest: print('  REST', w, '::', ctx)
