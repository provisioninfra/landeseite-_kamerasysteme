#!/bin/bash
# Prüft je URL die von WP Rocket ausgelieferte Kopie der Elementor-Seiten-CSS gegen das Original (Handy- und Desktop-Cache).
UA_M='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
UA_D='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
for u in "$@"; do
  for ua in M D; do
    [ $ua = M ] && A="$UA_M" || A="$UA_D"
    html=$(curl -s -A "$A" -w '\n%{http_code}' "https://provision-infra.de$u")
    code=$(echo "$html" | tail -1)
    if [ "$code" != 200 ]; then echo "$u $ua HTML $code"; sleep 20; continue; fi
    href=$(echo "$html" | grep -o "[^\"' ]*elementor/css/post-[0-9]*\.css[^\"' ]*" | head -1)
    id=$(echo "$href" | grep -o 'post-[0-9]*' | head -1)
    c=$(curl -s -A "$A" -w '\n%{http_code}' "${href/#\//https://provision-infra.de/}")
    o=$(curl -s -A "$A" "https://provision-infra.de/wp-content/uploads/elementor/css/$id.css")
    cc=$(echo "$c" | tail -1); cn=$(echo "$c" | grep -o 'elementor-element-[0-9a-f]*' | sort -u | wc -l); on=$(echo "$o" | grep -o 'elementor-element-[0-9a-f]*' | sort -u | wc -l)
    s=OK; [ "$cc" != 200 ] || [ "$cn" -lt "$on" ] && s=DEFEKT
    echo "$s $u $ua $id code=$cc regeln_kopie=$cn original=$on $(echo "$href" | grep -o 'cache/[a-z-]*' )"
    sleep 6
  done
done
