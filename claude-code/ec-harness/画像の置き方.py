#!/usr/bin/env python3
"""参考の記事とうちの記事の画像を、置き場所と大きさまで突き合わせる（工程5・6の出口）。
2026-10-06 本人「イメージが置かれてる場所を完全にコピーする。そうすれば大きさがおかしいことに気づける」。

使い方: python3 画像の置き方.py <参考のURL> <うちの記事（index.html のパスかURL）> [--移植表 <01 移植表.md>] [--測った <参考.json> <うち.json>]
  --測った: 裏用 Dia が立てられない時、内蔵ブラウザで LOAD_ALL と JS を同じ幅で当てた結果（JSON）を渡して判定だけする
裏用 Dia（9333）の同じ窓で両方を開き（同じ幅になる）、本文の画像（幅80px以上）を上から順に測る。
見る物: 枚数 / 何番目の章（h2）にあるか / 本文の中の位置（前にある段の割合） / 本文幅に対する横幅 / 縦横比。
段の並び（2026-10-07 本人「記事も同じことを」）: 章の数 / 章ごとの段・箇条・引用・小見出し・ボタンの数 / 型ごとの字の大きさ・太さ・色・後ろの箱・寄せ。言葉の中身は見ない。
ビジュアルの種類（2026-10-07 本人「ほとんどの場合は GIF」）: 1枚ずつ 動く（GIF・動くWebP）／止まり／動画 が参考と同じか。
訳（--移植表 を渡した時）: 参考の小さな言葉（actually・definitely など）を含む文が全部「## 訳の対照表」にあり、心理の効果・言葉ごとの運び方（「actually → …」）・うちの日本語が埋まっているか。参考の絵1枚ずつに「## 絵の対照表」の行（起こす感情・絵の調子・うちの絵）があるか。「## 変数の木」で参考を小さな変数まで割り、変数ごとに「→ やる事」があるか。参考が日本語なら、参考の段ごとに訳の対照表の行があるか。
終了コード: 0 一致 / 1 ずれがある（行ごとに直す所を出す） / 2 測れなかった。開いたタブは毎回閉じる。
"""
import json, os, subprocess, sys, time

ENV = {**os.environ, "DIA_CDP_PORT": "9333", "DIA_SOCK": "/tmp/dia-cdp-9333.sock"}
JS = r"""
const root = document.querySelector('article, main, .article, #content') || document.body;
const cw = root.getBoundingClientRect().width || innerWidth;
const all = [...root.querySelectorAll('h1,h2,h3,p,li,blockquote,img,video,iframe')];
const blocks = all.filter(e => !/IMG|VIDEO/.test(e.tagName) && e.innerText && e.innerText.trim().length > 1);
const out = [];
let h2 = 0, seen = 0;
for (const e of all) {
  if (e.tagName === 'H2') h2++;
  if (blocks.includes(e)) { seen++; continue; }
  const r = e.getBoundingClientRect();
  if (r.width < 80 || r.height < 40) continue;
  out.push({ 型: e.tagName, src: e.currentSrc || e.src || e.querySelector?.("source")?.src || "", 章: h2, 位置: +(seen / Math.max(blocks.length, 1)).toFixed(3), 幅: +(r.width / cw).toFixed(3), 縦横: +(r.height / r.width).toFixed(3), px: [Math.round(r.width), Math.round(r.height)] });
}
// 段の並びと見た目（2026-10-07 本人「記事も同じことをしたい」＝参考との差を0に）。言葉の中身は見ない
const css = e => getComputedStyle(e);
const bg = e => { for (let x = e; x && x !== root.parentElement; x = x.parentElement) { const c = css(x).backgroundColor; if (c && !/rgba\(0, 0, 0, 0\)|transparent/.test(c)) return x === root || x === document.body ? null : c; } return null; };
const isBtn = e => e.tagName === 'BUTTON' || (e.tagName === 'A' && (/btn|button|cta/i.test(e.className) || (bg(e) && css(e).display !== 'inline')));
const seq = []; let 章 = 0;
for (const e of root.querySelectorAll('h1,h2,h3,p,li,blockquote,a,button')) {
  const r = e.getBoundingClientRect(); if (r.width < 20 || r.height < 8) continue;
  if (e.tagName === 'H2') 章++;
  const t = e.tagName === 'A' || e.tagName === 'BUTTON' ? (isBtn(e) ? 'ボタン' : null) : e.tagName.toLowerCase();
  if (!t || (t !== 'ボタン' && !(e.innerText || '').trim())) continue;
  if (t === 'p' && e.closest('li,blockquote')) continue;
  const s = css(e);
  seq.push({ 型: t, 章, 字: +parseFloat(s.fontSize).toFixed(1), 太: +s.fontWeight >= 600, 色: s.color, 箱: bg(e), 寄せ: s.textAlign });
}
const 文 = []; { let k = 0; for (const e of root.querySelectorAll('h1,h2,h3,p,li,blockquote')) { if (e.tagName === 'H2') k++; if (e.tagName === 'P' && e.closest('li,blockquote')) continue; const t = (e.innerText || '').trim(); if (t) 文.push({ 章: k, 型: e.tagName.toLowerCase(), 文: t }); } }
return JSON.stringify({ 画像: out, 段: seq, 文 });
"""

LOAD_ALL = r"""
document.querySelectorAll('img').forEach(i => { i.loading = 'eager'; for (const k of ['data-src','data-lazy-src','data-original']) { const v = i.getAttribute(k); if (v && !i.getAttribute('src')?.startsWith('http')) i.src = v; } const ss = i.getAttribute('data-srcset'); if (ss) i.srcset = ss; });
for (let y = 0; y < document.body.scrollHeight; y += Math.max(innerHeight / 2, 300)) { scrollTo(0, y); await new Promise(r => setTimeout(r, 250)); }
scrollTo(0, document.body.scrollHeight); await new Promise(r => setTimeout(r, 1500));
await Promise.all([...document.images].filter(i => !i.complete).map(i => new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 8000); })));
scrollTo(0, 0); return 1;
"""

def dia(*args, timeout=90):
    r = subprocess.run(["dia", *args], env=ENV, capture_output=True, text=True, timeout=timeout)
    return r.stdout.strip()

def measure(target):
    url = target if target.startswith("http") or target.startswith("file:") else "file://" + os.path.abspath(target)
    tab = dia("open", url).splitlines()[0].strip()
    try:
        time.sleep(6)
        # 遅延読み込みの画像を出す。一番下へ飛ぶだけだと途中の絵が読み込まれない（2026-10-07 Everdries の理由5・6の絵が数えられず終了コード1）
        dia("do", LOAD_ALL, "--tab", tab, timeout=120)
        time.sleep(3)
        raw = dia("do", JS, "--tab", tab)
        return json.loads(raw[raw.index("{"): raw.rindex("}") + 1])
    finally:
        dia("close", "--tab", tab)

def 色(c):
    import re
    v = [int(x) for x in re.findall(r"\d+", c or "")[:3]]
    return v if len(v) == 3 else None

def 段の突き合わせ(R, O):
    """章ごとの段の数と、型ごとの見た目（字の大きさ・太さ・色・後ろの箱・寄せ）を比べる"""
    bad = []
    rn, on = max([x["章"] for x in R] + [0]), max([x["章"] for x in O] + [0])
    if rn != on: bad.append(f"章（h2）の数: 参考 {rn} / うち {on}")
    for k in range(min(rn, on) + 1):
        for t in ("p", "li", "blockquote", "h3", "ボタン"):
            a = sum(1 for x in R if x["章"] == k and x["型"] == t); b = sum(1 for x in O if x["章"] == k and x["型"] == t)
            if abs(a - b) > (max(1, round(a * 0.25)) if t == "p" else 0): bad.append(f"{k}番目の章: {t} の数 参考 {a} / うち {b}")
    for t in ("h1", "h2", "h3", "p", "li", "blockquote", "ボタン"):
        a = [x for x in R if x["型"] == t]; b = [x for x in O if x["型"] == t]
        if not a or not b: continue
        ma, mb = sorted(x["字"] for x in a)[len(a) // 2], sorted(x["字"] for x in b)[len(b) // 2]
        if abs(ma - mb) > 0.15 * ma: bad.append(f"{t}: 字の大きさ 参考 {ma}px / うち {mb}px")
        if (sum(x["太"] for x in a) * 2 > len(a)) != (sum(x["太"] for x in b) * 2 > len(b)): bad.append(f"{t}: 太字 参考 {'太い' if sum(x['太'] for x in a) * 2 > len(a) else '細い'} / うち {'太い' if sum(x['太'] for x in b) * 2 > len(b) else '細い'}")
        多 = lambda xs, k: max(set(x[k] for x in xs), key=[x[k] for x in xs].count)  # 1つ目ではなく一番多い見た目で比べる（飾りの1個に引きずられない）
        ca, cb = 色(多(a, "色")), 色(多(b, "色"))
        if ca and cb and sum((x - y) ** 2 for x, y in zip(ca, cb)) ** 0.5 > 90: bad.append(f"{t}: 字の色 参考 {多(a, '色')} / うち {多(b, '色')}")
        if (sum(1 for x in a if x["箱"]) * 2 > len(a)) != (sum(1 for x in b if x["箱"]) * 2 > len(b)): bad.append(f"{t}: 後ろの箱 参考 {'あり' if sum(1 for x in a if x['箱']) * 2 > len(a) else 'なし'} / うち {'あり' if sum(1 for x in b if x['箱']) * 2 > len(b) else 'なし'}")
        if 多(a, "寄せ") != 多(b, "寄せ") and t in ("h1", "h2", "ボタン"): bad.append(f"{t}: 寄せ 参考 {多(a, '寄せ')} / うち {多(b, '寄せ')}")
    return bad


小さな言葉 = ["actually", "definitely", "just", "even", "only", "still", "really", "finally", "simply", "exactly", "quietly", "secretly", "literally", "already", "never", "ever", "almost", "truly", "honestly", "instantly", "suddenly", "completely", "totally", "absolutely", "seriously", "surprisingly", "basically", "practically", "barely", "hardly", "right now", "today", "anymore", "at last", "no longer", "in fact", "of course", "here's", "here is", "why", "what", "imagine", "but"]

def 動きの種類(img):
    """動く（GIF・動くWebP）／止まり／動画 を見分ける"""
    if img.get("型") in ("VIDEO", "IFRAME"): return "動画"
    src = img.get("src") or ""
    try:
        import io, urllib.request
        from PIL import Image
        if src.startswith("file://"):
            import urllib.parse; data = open(urllib.parse.unquote(src[7:]), "rb").read()
        elif src.startswith("data:"):
            import base64; data = base64.b64decode(src.split(",", 1)[1])
        else:
            data = urllib.request.urlopen(urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"}), timeout=20).read()
        im = Image.open(io.BytesIO(data))
        return "動く" if getattr(im, "is_animated", False) and getattr(im, "n_frames", 1) > 1 else "止まり"
    except Exception:
        return "測れない"

def 訳の照らし(参考の文, 移植表):
    """参考の小さな言葉を含む文が、移植表の「訳の対照表」に全部あり、その言葉の運び方が書いてあるか（2026-10-07 本人「小さい英語を訳すところが弱い」）"""
    import re
    md = open(移植表, encoding="utf-8").read()
    m = re.search(r"\n## 訳の対照表[^\n]*\n(.*?)(?=\n## |\Z)", md, re.S)
    if not m: return ["移植表に「## 訳の対照表」が無い（| # | 参考の英語 | 心理の効果 | 小さな言葉 → 日本語での運び方 | うちの日本語 |）"]
    行 = [[c.strip() for c in l.strip().strip("|").split("|")] for l in m.group(1).splitlines() if l.strip().startswith("|") and not re.match(r"^\|\s*-", l.strip())][1:]
    norm = lambda t: re.sub(r"\s+", " ", t.lower()).strip()
    bad = []
    全文 = "".join(x["文"] for x in 参考の文)
    if 全文 and sum(1 for c in 全文 if "\u3040" <= c <= "\u9fff") / len(全文) > 0.3:
        # 参考が日本語（たいていは違う商品）: 段ごとに、同じ心理の効果を起こす行が要る（2026-10-07 本人）
        for x in 参考の文:
            if x["型"] not in ("p", "li", "blockquote", "h1", "h2") or len(x["文"]) < 8: continue
            hit = next((r for r in 行 if len(r) >= 5 and norm(x["文"])[:20] in norm(r[1])), None)
            if not hit: bad.append(f"訳の対照表に無い段（日本語の参考）: 「{x['文'][:40]}」")
            elif not hit[2] or not hit[4]: bad.append(f"心理の効果かうちの文が空: 「{x['文'][:30]}」")
        return bad
    for x in 参考の文:
        for s_ in re.split(r"(?<=[.!?])\s+", x["文"]):
            ns = norm(s_)
            if len(ns) < 8: continue
            words = [w for w in 小さな言葉 if re.search(r"(?<![a-z'])" + re.escape(w) + r"(?![a-z])", ns)]
            if not words: continue
            hit = next((r for r in 行 if len(r) >= 5 and (ns[:40] in norm(r[1]) or norm(r[1])[:40] in ns)), None)
            if not hit: bad.append(f"訳の対照表に無い文（小さな言葉 {', '.join(words)}）: 「{s_[:60]}」"); continue
            if not hit[2]: bad.append(f"心理の効果が空: 「{s_[:40]}」")
            for w in words:
                if not re.search(re.escape(w) + r"[^|]*→", hit[3].lower()): bad.append(f"小さな言葉「{w}」の運び方が無い（「{w} → …」と書く）: 「{s_[:40]}」")
            if not hit[4]: bad.append(f"うちの日本語が空: 「{s_[:40]}」")
    return bad

def 木の照らし(移植表):
    """参考を小さな変数の木に割ってから作っているか（2026-10-07 本人「どの小さな variable で集まってるかを tree diagram で考える」）"""
    import re
    md = open(移植表, encoding="utf-8").read()
    m = re.search(r"\n## 変数の木[^\n]*\n(.*?)(?=\n## |\Z)", md, re.S)
    if not m: return ["移植表に「## 変数の木」が無い（参考を 構造（シンプルさ・コピー）とビジュアル から小さな変数まで割り、変数ごとに差を0にするやる事を書く）"]
    枝 = [l for l in m.group(1).splitlines() if re.match(r"^\s*[-*]\s+\S", l)]
    深い = [l for l in 枝 if len(l) - len(l.lstrip()) >= 4]
    bad = []
    if len(枝) < 6 or not 深い: bad.append(f"変数の木が浅い（枝 {len(枝)} 本・2段目より下 {len(深い)} 本）。構造とビジュアルの下に、差を測れる小さな変数まで割る")
    if 枝 and not any("→" in l for l in 枝): bad.append("変数の木に「→ 差を0にするやる事」が無い")
    return bad

def 絵の照らし(参考の画像, 移植表):
    """参考の絵1枚ずつに、読み手に起こす感情と絵の調子を読み取ってから、うちの絵を作っているか（2026-10-07 本人「その画像がどんな心理的な感情を与えてるのかを読み取って、同じ感情を与える画像を作る」）"""
    import re
    md = open(移植表, encoding="utf-8").read()
    m = re.search(r"\n## 絵の対照表[^\n]*\n(.*?)(?=\n## |\Z)", md, re.S)
    if not m: return ["移植表に「## 絵の対照表」が無い（| 枚 | 参考の絵が起こす感情 | 絵の調子（例: 日本風の優しい感じ） | うちの絵（ファイルとプロンプト） |）"]
    行 = [[c.strip() for c in l.strip().strip("|").split("|")] for l in m.group(1).splitlines() if l.strip().startswith("|") and not re.match(r"^\|\s*-", l.strip())][1:]
    bad = []
    if len(行) != len(参考の画像): bad.append(f"絵の対照表の行 {len(行)} / 参考の絵 {len(参考の画像)} 枚。1枚1行にする")
    for i, r in enumerate(行, 1):
        if len(r) < 4 or not all(r[:4]): bad.append(f"絵の対照表の{i}行目: 空の欄がある（感情・調子・うちの絵を全部書く）")
    return bad

def main(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    try:
        if "--測った" in argv:
            # 裏用 Dia が立てられない時（本人の Dia が 9222 無しで開いている時）は、内蔵ブラウザで同じ JS（下の JS_FOR_EXPORT）を当てた結果を渡す（2026-10-09）
            k = argv.index("--測った")
            ref, ours = json.load(open(argv[k + 1], encoding="utf-8")), json.load(open(argv[k + 2], encoding="utf-8"))
        else:
            ref, ours = measure(argv[1]), measure(argv[2])
    except Exception as e:
        print(f"測れなかった: {e}"); return 2
    移植表 = argv[argv.index("--移植表") + 1] if "--移植表" in argv else None
    bad = 段の突き合わせ(ref["段"], ours["段"])  # 分かりやすさは字数・漢字では測れない（2026-10-07 本人）。編集長が客の目で読んで決める
    if 移植表: bad += 木の照らし(移植表) + 訳の照らし(ref["文"], 移植表) + 絵の照らし(ref["画像"], 移植表)
    参考の文 = ref["文"]
    ref, ours = ref["画像"], ours["画像"]
    for i, (a, b) in enumerate(zip(ref, ours), 1):
        ka, kb = 動きの種類(a), 動きの種類(b)
        if "測れない" not in (ka, kb) and ka != kb: bad.append(f"{i}枚目: 参考は「{ka}」/ うちは「{kb}」（GIF・動画は同じ種類で作る）")
    if len(ref) != len(ours):
        bad.append(f"画像の枚数: 参考 {len(ref)} 枚 / うち {len(ours)} 枚。参考と同じ枚数にする")
    for i, (a, b) in enumerate(zip(ref, ours), 1):
        if a["章"] != b["章"]: bad.append(f"{i}枚目: 参考は {a['章']} 番目の章 / うちは {b['章']} 番目の章")
        if abs(a["位置"] - b["位置"]) > 0.08: bad.append(f"{i}枚目: 本文の中の位置 参考 {a['位置']:.0%} / うち {b['位置']:.0%}")
        if abs(a["幅"] - b["幅"]) > 0.10: bad.append(f"{i}枚目: 横幅（本文幅に対して）参考 {a['幅']:.0%} / うち {b['幅']:.0%}（{a['px']} / {b['px']}px）")
        if abs(a["縦横"] - b["縦横"]) > 0.10 * max(a["縦横"], 0.1): bad.append(f"{i}枚目: 縦横比 参考 {a['縦横']} / うち {b['縦横']}（{a['px']} / {b['px']}px）")
    bad = list(dict.fromkeys(bad))  # 同じ文が入れ子の段で2回数えられても1回だけ出す
    print(f"参考 {len(ref)} 枚・うち {len(ours)} 枚を突き合わせた")
    if bad:
        print("\n".join("- " + x for x in bad)); return 1
    print("通った"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
