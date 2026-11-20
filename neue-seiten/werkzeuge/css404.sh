#!/bin/bash
for u in "$@"; do for ua in 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1' 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36'; do
 html=$(curl -s -A "$ua" -w '\n%{http_code}' "https://provision-infra.de$u"); code=$(echo "$html"|tail -1); n=0; bad=""
 for h in $(echo "$html" | grep -o "https\?://provision-infra.de/wp-content/cache/[^\"' )]*\.css[^\"' )]*\|/wp-content/cache/[^\"' )]*\.css[^\"' )]*" | sort -u); do n=$((n+1)); c=$(curl -s -A "$ua" -o /dev/null -w '%{http_code}' "${h/#\//https://provision-infra.de/}"); [ "$c" != 200 ] && bad="$bad $c:$(basename ${h%%\?*})"; done
 echo "$u ${ua:13:6} html=$code cache-css=$n defekt:${bad:- keine}"; sleep 3; done; done
