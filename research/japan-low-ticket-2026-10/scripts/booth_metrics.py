import json,re,statistics,sys,glob
S="${SCRATCH}/df/"
data={}
for f in ["booth_scan.json","booth_scan2.json","booth_scan4.json","booth_scan3.json"]:  # scan3 (top30) last so it overrides
    try: data.update(json.load(open(S+f)))
    except Exception: pass
def p(x):
    m=re.search(r"([\d,]+)",x or ""); return int(m.group(1).replace(",","")) if m else 0
rows=[]
for t,v in data.items():
    it=[i for i in v.get("items",[]) if i.get("wish") is not None]
    paid=[i for i in it if p(i.get("price"))>0]
    recent=[i for i in it if (i.get("published") or "")>="2025-01-01"]
    recent_paid=[i for i in paid if (i.get("published") or "")>="2025-01-01"]
    best=max(paid,key=lambda i:i["wish"]) if paid else None
    bestr=max(recent_paid,key=lambda i:i["wish"]) if recent_paid else None
    rows.append(dict(tag=t,total=v.get("total"),n=len(it),paid_med_wish=int(statistics.median([i["wish"] for i in paid])) if paid else 0,
        price_med=int(statistics.median([p(i["price"]) for i in paid])) if paid else 0,
        recent_share=round(len(recent)/len(it),2) if it else 0,
        best=(best["wish"],best["price"],best["name"][:40],best["url"]) if best else None,
        best_recent=(bestr["wish"],bestr["price"],bestr["published"],bestr["name"][:40],bestr["url"]) if bestr else None))
json.dump(rows,open(S+"booth_metrics.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in sorted(rows,key=lambda r:-r["paid_med_wish"]):
    print(f'{r["tag"]:<14} total={r["total"]} n={r["n"]} paidMedWish={r["paid_med_wish"]} priceMed=¥{r["price_med"]} recent={r["recent_share"]}\n   best={r["best"]}\n   bestRecent={r["best_recent"]}')
