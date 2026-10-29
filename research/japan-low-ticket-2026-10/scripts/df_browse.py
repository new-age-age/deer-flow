"""Fetch pages through DeerFlow's browser_automation session (Playwright).
Usage: df_browse.py <urls.txt> <outdir> [max_chars]"""
import asyncio, sys, os, hashlib
from deerflow.community.browser_automation.session import get_browser_session_manager
from deerflow.community.browser_automation.tools import validate_browser_url, resolve_browser_egress
mx=int(sys.argv[3]) if len(sys.argv)>3 else 30000
async def main():
    mgr=get_browser_session_manager(); os.makedirs(sys.argv[2],exist_ok=True)
    for u in open(sys.argv[1],encoding="utf-8"):
        u=u.strip()
        if not u: continue
        fn=os.path.join(sys.argv[2],hashlib.md5(u.encode()).hexdigest()[:10]+".md")
        try:
            with mgr.acquire_session("jp-research",headless=True,timeout_ms=45000,viewport={"width":1280,"height":2000},cdp_url=None,allow_unguarded_cdp=False,url_guard=validate_browser_url,egress_resolver=None) as s:
                snap=await s.navigate(u)
                await asyncio.sleep(3)
                txt=await s.get_text(max_chars=mx)
            out=f"URL: {u}\nTITLE: {snap.title}\n\n{txt}"
        except Exception as e:
            out=f"URL: {u}\nERROR: {type(e).__name__}: {e}"
        open(fn,"w",encoding="utf-8").write(out)
        print(u, len(out), fn, out.splitlines()[1][:80], flush=True)
asyncio.run(main())
