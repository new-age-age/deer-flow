#!/bin/bash
S=${SCRATCH}
cd /home/user/last30days-skill
i=0
while IFS= read -r T; do
  i=$((i+1)); [ -z "$T" ] && continue
  python3 - "$T" > $S/plans/t$i.json <<'PY'
import json,sys
t=sys.argv[1]
print(json.dumps({"intent":"product","freshness_mode":"balanced_recent","cluster_mode":"none","subqueries":[{"label":"primary","search_query":t,"ranking_query":f"{t} について日本の消費者・販売者は最近何を言っているか？売れている商品・悩み・不満は？","sources":["youtube"],"weight":1.0}]},ensure_ascii=False))
PY
  timeout 900 python3 skills/last30days/scripts/last30days.py "$T" --research-only --deep --search youtube --plan $S/plans/t$i.json --emit=compact --save-dir=$S/l30 --save-suffix=t$i > $S/l30/t$i.out 2> $S/l30/t$i.err
  echo "t$i [$T] exit=$? $(grep -o 'YouTube: [0-9]* videos' $S/l30/t$i.err)" >> $S/l30/summary.txt
done < $S/topics.txt
echo DONE >> $S/l30/summary.txt
