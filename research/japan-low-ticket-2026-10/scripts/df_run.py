"""Driver: executes DeerFlow harness tools (web_search / web_fetch) on a batch file.
Usage: df_run.py search <queries.txt> <out.jsonl> [time_range]
       df_run.py fetch <urls.txt> <outdir>"""
import json, sys, asyncio, hashlib, os, time
from deerflow.community.ddg_search.tools import web_search_tool
from deerflow.community.jina_ai.tools import web_fetch_tool
mode=sys.argv[1]
if mode=="search":
    tr = sys.argv[4] if len(sys.argv)>4 else None
    with open(sys.argv[3],"a",encoding="utf-8") as out:
        for q in open(sys.argv[2],encoding="utf-8"):
            q=q.strip()
            if not q: continue
            args={"query":q,"max_results":10}
            if tr: args["time_range"]=tr
            r=web_search_tool.invoke(args)
            try: d=json.loads(r)
            except Exception: d={"raw":r}
            d["query"]=q; d["time_range"]=tr
            out.write(json.dumps(d,ensure_ascii=False)+"\n"); out.flush()
            print(q, d.get("total_results", d.get("error")), flush=True)
            time.sleep(1)
else:
    od=sys.argv[3]; os.makedirs(od,exist_ok=True)
    async def go():
        for u in open(sys.argv[2],encoding="utf-8"):
            u=u.strip()
            if not u: continue
            try: r=await web_fetch_tool.ainvoke({"url":u})
            except Exception as e: r=f"ERROR {e}"
            fn=os.path.join(od,hashlib.md5(u.encode()).hexdigest()[:10]+".md")
            open(fn,"w",encoding="utf-8").write(f"URL: {u}\n\n{r}")
            print(u, len(str(r)), fn, flush=True); await asyncio.sleep(4)
    asyncio.run(go())
