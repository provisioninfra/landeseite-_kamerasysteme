"""Texte bestehender Elementor-Seiten herausziehen und geänderte Texte gezielt zurückschreiben.

  python3 -I texte_bestand.py ziehen <export.json> <texte.json>
      schreibt {"<element-id>|<pfad>": "<text>", ...} für alle Textfelder außerhalb des Kopf-Containers
  python3 -I texte_bestand.py anwenden <export.json> <alt.json> <neu.json> <ausgabe.json>
      setzt jeden Eintrag aus neu.json, dessen Wert von alt.json abweicht; bricht ab, wenn der Wert im
      Export nicht mehr dem alten entspricht (dann hat jemand anderes die Stelle inzwischen geändert)

Pfade: "title", "editor", "icon_list.2.text", "eael_adv_accordion_tab.0.eael_adv_accordion_tab_content" usw.
"""
import json, sys

KOPF = {'192a273'}
TEXT = {'title', 'editor', 'text', 'description_text', 'title_text', 'button_text', 'inner_text', 'caption',
        'tab_title', 'tab_content', 'eael_adv_accordion_tab_title', 'eael_adv_accordion_tab_content',
        'eael_content_timeline_title', 'eael_content_timeline_excerpt', 'eael_custom_content_timeline_title',
        'eael_custom_content_timeline_excerpt', 'eael_custom_content_timeline_time_text', 'testimonial_content',
        'testimonial_name', 'testimonial_job', 'prefix', 'suffix', 'before_text', 'highlighted_text', 'rotating_text',
        'after_text', 'counter_title', 'eael_custom_title', 'eael_custom_excerpt', 'alert_title', 'alert_description', 'placeholder', 'heading', 'sub_heading'}
OHNE = {'html', 'shortcode'}  # Code-Widgets nie anfassen


def felder(e):
    s = e.get('settings') or {}
    for k, v in s.items():
        if isinstance(v, str) and k in TEXT and v.strip():
            yield k, v
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    for k2, v2 in item.items():
                        if isinstance(v2, str) and k2 in TEXT and v2.strip():
                            yield f'{k}.{i}.{k2}', v2


def alle(els, kopf=False):
    for e in els:
        k = kopf or e['id'] in KOPF
        if not k and e.get('widgetType') not in OHNE:
            yield e
        yield from alle(e.get('elements', []), k)


def holen(e, pfad):
    teile = pfad.split('.')
    s = e['settings']
    if len(teile) == 1:
        return s, teile[0]
    return s[teile[0]][int(teile[1])], teile[2]


if __name__ == '__main__':
    cmd = sys.argv[1]
    exp = json.load(open(sys.argv[2]))
    if cmd == 'ziehen':
        out = {}
        for e in alle(exp['elements']):
            for p, v in felder(e):
                out[f"{e['id']}|{p}"] = v
        json.dump(out, open(sys.argv[3], 'w'), ensure_ascii=False, indent=1)
        print('felder', len(out), 'wörter', sum(len(v.split()) for v in out.values()))
    elif cmd == 'anwenden':
        alt, neu = json.load(open(sys.argv[3])), json.load(open(sys.argv[4]))
        idx = {e['id']: e for e in alle(exp['elements'])}
        n = 0
        for key, wert in neu.items():
            if alt.get(key) == wert:
                continue
            assert key in alt, f'unbekannte Stelle {key}'
            eid, pfad = key.split('|', 1)
            ziel, feld = holen(idx[eid], pfad)
            assert ziel.get(feld) == alt[key], f'Stelle {key} wurde inzwischen geändert'
            ziel[feld] = wert
            n += 1
        json.dump(exp, open(sys.argv[5], 'w'), ensure_ascii=False)
        print('geändert', n)
