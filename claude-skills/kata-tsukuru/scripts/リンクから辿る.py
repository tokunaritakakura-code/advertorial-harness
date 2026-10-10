#!/usr/bin/env python3
"""飛び先のリンク1本から、そこへ飛ばしている広告（動画・画像）を Meta の広告ライブラリでたどる。

使い方: python3 リンクから辿る.py <飛び先のURL> <出力フォルダ> [--国 JP] [--最大 30]
  1 URL のドメインで広告ライブラリを検索（配信中・全部の形式）。本人の Dia（ポート9222）の裏タブで開く
  2 出てきた広告を1本ずつ開き、飛び先・配信開始日・動画か画像か・広告主・本文を取る
  3 飛び先が同じドメインの物だけ残し、<出力>/広告.json と 広告.tsv に書く。動画は src、画像は1枚目の URL も残す
  当たっているかの目安: 同じ飛び先に30日以上の広告があり、広告が5本以上（kata-tsukuru の SKILL.md と同じ線）
終了コード: 0=1本以上取れた / 1=広告が0本（検索は通った） / 2=開けない・道具が無い・取れなかった
本人の Dia のタブは閉じない。開いた1枚だけを使う。
"""
import json, os, re, subprocess, sys, time, urllib.parse
from datetime import date, datetime

LIB = "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country={c}&q={q}&search_type=keyword_unordered"
CARDS = r"""JSON.stringify([...document.body.innerText.matchAll(/Library ID: (\d+)\s+Started running on ([A-Za-z]+ \d+, \d+)/g)].map(m=>[m[1],m[2]]))"""
DETAIL = r"""JSON.stringify((()=>{const h=document.documentElement.innerHTML;
 const dec=s=>{try{return JSON.parse('"'+s+'"')}catch(e){return s}};
 const vids=[...new Set([...h.matchAll(/"video_(?:hd|sd)_url":"([^"]+)"/g)].map(m=>dec(m[1])))];
 const imgs=[...new Set([...h.matchAll(/"original_image_url":"([^"]+)"/g)].map(m=>dec(m[1])))];
 const links=[...new Set([...h.matchAll(/"link_url":"([^"]+)"/g)].map(m=>dec(m[1])))];
 const page=(h.match(/"page_name":"([^"]+)"/)||[])[1]||'';
 const body=(h.match(/"body":\{"text":"([^"]*)"/)||[])[1]||'';
 return {video:document.querySelectorAll('video').length, vids:vids.slice(0,2), imgs:imgs.slice(0,2), links, page:dec(page), body:dec(body).slice(0,400)}})())"""


def dia(*args, timeout=60):
    r = subprocess.run(["dia", *args], capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stdout + r.stderr).strip()[:200])
    return r.stdout


def do(js, tab, tries=3):
    last = None
    for k in range(tries):
        try:
            out = dia("do", js, "--tab", tab).splitlines()
            return json.loads(out[0]) if out and out[0].strip() else None
        except Exception as e:   # 読み込み途中で落ちたら少し待って取り直す
            last = e
            time.sleep(2 + 2 * k)
    raise RuntimeError(f"ページを読めない: {last}")


def days_since(s):
    try:
        return (date.today() - datetime.strptime(s, "%b %d, %Y").date()).days
    except ValueError:
        return None


def main(a):
    if len(a) < 2:
        print(__doc__); return 2
    url, out = a[0], os.path.expanduser(a[1])
    country = a[a.index("--国") + 1] if "--国" in a else "JP"
    most = int(a[a.index("--最大") + 1]) if "--最大" in a else 30
    host = urllib.parse.urlparse(url).netloc.lower()
    if not host:
        print("URL が読めない", file=sys.stderr); return 2
    key = host.removeprefix("www.")
    os.makedirs(out, exist_ok=True)
    try:
        doc = subprocess.run(["dia", "doctor"], capture_output=True, text=True, timeout=30).stdout
    except FileNotFoundError:
        print("道具が無い: dia", file=sys.stderr); return 2
    if "全部OK" not in doc:
        print("本人の Dia に繋がらない（ポート9222）。`dia doctor` の → を上から", file=sys.stderr); return 2
    tab = dia("open", LIB.format(c=country, q=urllib.parse.quote(key))).splitlines()[0].strip()
    time.sleep(6)
    for _ in range(4):    # 下まで送って続きを読み込ませる（固定の回数。0件と取れなかったを分けるため回数を記録）
        dia("do", "window.scrollTo(0,document.body.scrollHeight)", "--tab", tab)
        time.sleep(2)
    cards = do(CARDS, tab) or []
    text = do("JSON.stringify(document.body.innerText.slice(0,3000))", tab) or ""
    if not cards:
        if re.search(r"No ads match|該当する広告はありません|0 results", text):
            print(f"広告が0本（検索語 {key}・国 {country}）"); return 1
        print(f"検索結果が読めない（ログイン切れ・ブロックの疑い）。先頭: {text[:120]}", file=sys.stderr); return 2
    seen, ads = set(), []
    for lid, start in cards:
        if lid in seen or len(ads) >= most:
            continue
        seen.add(lid)
        dia("nav", f"https://www.facebook.com/ads/library/?id={lid}", "--tab", tab)
        time.sleep(5)
        d = do(DETAIL, tab) or {}
        land = [l for l in d.get("links", []) if key in l.lower()]
        ads.append({"id": lid, "開始": start, "日数": days_since(start), "形": "動画" if (d.get("video") or d.get("vids")) else "画像",
                    "広告主": d.get("page", ""), "飛び先": land[0] if land else (d.get("links") or [""])[0],
                    "同じドメイン": bool(land), "動画": d.get("vids", []), "画像": d.get("imgs", []), "本文": d.get("body", ""),
                    "広告ライブラリ": f"https://www.facebook.com/ads/library/?id={lid}"})
    mine = [x for x in ads if x["同じドメイン"]]
    long_ = [x for x in mine if (x["日数"] or 0) >= 30]
    res = {"入力": url, "検索語": key, "国": country, "取った日": date.today().isoformat(), "広告": ads,
           "同じドメインの本数": len(mine), "30日以上": len(long_),
           "当たっている": len(mine) >= 5 and len(long_) >= 1}
    with open(os.path.join(out, "広告.json"), "w") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out, "広告.tsv"), "w") as f:
        f.write("id\t日数\t形\t広告主\t飛び先\t本文\n")
        for x in mine:
            f.write(f"{x['id']}\t{x['日数']}\t{x['形']}\t{x['広告主']}\t{x['飛び先']}\t{x['本文'][:80]}\n")
    print(f"広告 {len(ads)}本（同じドメイン {len(mine)}本・30日以上 {len(long_)}本・{'当たっている' if res['当たっている'] else '当たりの線に届かない'}） → {out}")
    return 0 if mine else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
