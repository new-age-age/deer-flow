"""DeerFlow browser_automation session: for each BOOTH tag, read total count + top-N items (popularity sort), then item JSON (wish_lists_count, price, published_at)."""
import asyncio, sys, json, re
from urllib.parse import quote
from deerflow.community.browser_automation.session import get_browser_session_manager
from deerflow.community.browser_automation.tools import validate_browser_url
N=10
JS = """() => Array.from(document.querySelectorAll('li.item-card')).slice(0,40).map(c => (c.querySelector('a[href*="/items/"]')||{}).href||'')"""
async def main():
    tags=[t.strip() for t in open(sys.argv[1],encoding="utf-8") if t.strip()]
    mgr=get_browser_session_manager(); res={}
    kw=dict(headless=True,timeout_ms=45000,viewport={"width":1280,"height":2000},cdp_url=None,allow_unguarded_cdp=False,url_guard=validate_browser_url,egress_resolver=None)
    for t in tags:
        u=f"https://booth.pm/ja/items?sort=wish_lists&tags%5B%5D={quote(t)}"
        r={"listing":u}
        try:
            with mgr.acquire_session("scan",**kw) as s:
                snap=await s.navigate(u); await asyncio.sleep(1.5)
                async def _ev():
                    p=await s._ensure_page(); return await p.evaluate(JS)
                urls=[x for x in await s._loop.run(_ev()) if x]
                m=re.search(r"([\d,]+)点",snap.title); r["total"]=int(m.group(1).replace(",","")) if m else None
                items=[]
                for iu in list(dict.fromkeys(urls))[:N]:
                    iid=re.search(r"/items/(\d+)",iu).group(1)
                    await s.navigate(f"https://booth.pm/ja/items/{iid}.json")
                    txt=await s.get_text(max_chars=200000)
                    try:
                        d=json.loads(txt[txt.index("{"):])
                        items.append({"id":iid,"name":d.get("name"),"price":d.get("price"),"wish":d.get("wish_lists_count"),"published":(d.get("published_at") or "")[:10],"shop":(d.get("shop") or {}).get("name"),"category":(d.get("category") or {}).get("name"),"url":f"https://booth.pm/ja/items/{iid}"})
                    except Exception as e: items.append({"id":iid,"error":str(e)[:80]})
                r["items"]=items
        except Exception as e: r["error"]=str(e)[:200]
        res[t]=r
        print(t, r.get("total"), [i.get("wish") for i in r.get("items",[])], flush=True)
        json.dump(res,open(sys.argv[2],"w",encoding="utf-8"),ensure_ascii=False,indent=1)
asyncio.run(main())
