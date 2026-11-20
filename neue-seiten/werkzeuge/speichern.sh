#!/bin/bash
# Je Seite: frischer Export, nur geänderte Textfelder setzen (Abbruch, wenn eine Stelle inzwischen anders ist), speichern, 30 s Pause.
W=/tmp/claude-0/-home-user/8101c591-dd55-5971-91e8-f9b3f727dc4d/scratchpad/wp
T=/home/user/landeseite-_kamerasysteme/neue-seiten/werkzeuge/texte_bestand.py
mkdir -p $W/bestand/frisch
cd $W
for id in "$@"; do
  echo "== $id $(date -u +%H:%M:%S)"
  STATE=$W/state.json PAGE_ID=$id MODE=export OUT=$W/bestand/frisch node edit_page.mjs 2>&1 | tail -1 | cut -c1-120
  if ! python3 -I $T anwenden bestand/frisch/page-$id-vorher.json bestand/$id-ALT.json bestand/$id-NEU.json bestand/$id-FINAL.json; then
    echo "   ABBRUCH $id: Abgleich fehlgeschlagen, nicht gespeichert"; sleep 20; continue
  fi
  STATE=$W/state.json PAGE_ID=$id DATA=$W/bestand/$id-FINAL.json POST_STATUS=publish node save.mjs 2>&1 | tail -1 | cut -c1-110
  sleep 30
done
echo FERTIG
