#!/usr/bin/env python3
"""値段の段（ここちドライ型）を組む。1枚の JSON から、記事にそのまま貼る HTML の断片を出す。

使い方: python3 値段の段を組む.py <入力.json> [-o <出力.html>] [--見本 <見本.html>] [--出す 全部|札だけ]
  --出す  全部（既定）か 札だけ。札だけ＝縦長の値段画像（と画像の後の文）を出さない。アンケート型・漫画で値段が
          「問いの前の札」と「答えた後の段」に分かれる時、前は 札だけ・後は 全部（同じ入力で2回組む。外枠の印は両方に付く）
  -o      断片の書き出し先（無ければ標準出力）
  --見本  断片だけを入れた確かめ用のページも書く（幅の検査・見比べ用。記事には使わない）
終了コード: 0 書けた / 2 入力の誤り（何が足りないかを出す）

見せ方と効果は ここちドライ advertorial-08 の値段の段（2026-10-11 本番を幅390・1280で実測）のまま。色・字の形・値段・文は全部入力から。
並び: (お知らせ帯) → 見出し → 前振り → 比べる物 → 価格の箱 → 1日あたりの文 → 縦長の値段画像 → (画像の後の文) → セットのカード → (セットの後の文) → ボタン → ボタンの下の一文 → (下の固定帯)
道具が必ずやる事（入力で外せない。_必ず入れる物.md の 2・決めたこと 2026-10-11）:
  - いちばん大きいセット（「数」が最大）に「一番人気」の札を付け、最初から選ばれた状態（濃い枠・淡い地）にする。
    そのセットの値段が並べた中で最大でなければ止める（いちばん大きいセットを、いちばん高い値段で見せる決まり）
  - 価格の箱は、いちばん大きいセットの値段で出す
  - 外枠に data-tasu="2" と data-nedan="ここちドライ型"
  - 縦長の値段画像（800×1200）。入力に画像が無ければ、1日あたりの値段を大きく見せる画像を SVG で作って埋め込む

入力（JSON。* は必須。例は 値段の段/例_*.json）:
  "色": {"主"*: "#rrggbb", "濃い": 影と字, "淡い": 選ばれたカードの地, "枠": 価格の箱の枠, "値段": 今の値段の字（無ければ赤 #d93025）}
  "字": {"形": "font-family の値", "見出しの太さ": 900}
  "単位": "枚"（1つあたりの数え方）
  "セット"*: [{"名前": "15枚", "数"*: 15, "値段"*: 29890, "通常"*: 49890, "登録後": 27890, "おまけ": "ネット3個", "行き先": URL}]
  "送料無料": true
  "割引": "40%OFF"（無ければ いちばん大きいセットの 通常と値段 から出す）  "札": 価格の箱の札（無ければ 割引）
  "登録": "メール登録"（登録後の値段がある時の言い方）
  "1日あたり": {"元": "登録後" か "値段", "日数": 365, "言い方": "1年使うと"}
  "見出し"・"前振り": [文]・"比べる前の一文"・"比べる物"*: [{"名": "紙パンツ", "文": "1枚87〜173円。…"}]
  "保証の日数"*: 30
  "ボタン"*: {"文": "…", "行き先": URL}   "ボタンの下": 文
  "値段画像": {"ファイル": 画像のパスかURL（あれば作らない）, "上の一言", "見出し", "前提", "比べ", "締め"}
  "画像の後": [文]（無ければ1つあたりの値段の比べを出す）  "セットの後": [文]
  "お知らせ帯": {"頭": "● お知らせ：", "文": "…", "リンク": "▶ 在庫を見る", "行き先": URL}
  "固定帯": {"文": "…", "出す所": "CSSの選び方"} か false（無ければボタンの文で出す）
  "段の印": "9"（data-dan に入れる）   "外枠の属性": {"id": "thanks", "hidden": true}（記事の側の出し入れの印を外枠に残す）
文の中の <b> と <wbr> はそのまま通す。それ以外の字は HTML として逃がす。
"""
import base64, html, json, os, re, sys

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "値段の段")
外せない = ("一番人気", "選ぶ", "選ばれた", "札を外す")


def err(m):
    print(f"入力の誤り: {m}", file=sys.stderr); sys.exit(2)


try:
    import budoux
    _BX = budoux.load_default_japanese_parser()
except Exception:  # BudouX が無いパソコンでも動く（<wbr> が入らないだけ。pip install budoux で入る）
    _BX = None
_PUNCT = re.compile(r"[、。，．・「」『』（）()!?！？…\s]")


def 区切る(h):
    """文節の切れ目に <wbr> を入れる（記事を作る 05 の手順6 と同じ決まり: 文の終わりまで3文字以下の所には入れない）"""
    if not _BX:
        return h
    parts = re.split(r"(<[^>]+>)", h)
    plain = "".join(x for x in parts if not x.startswith("<"))
    plain_u = html.unescape(plain)
    if plain_u != plain:  # 逃がした字（&amp; など）が混ざる時は位置がずれるので入れない
        return h
    chunks = _BX.parse(plain)
    i = len(chunks) - 1
    while i > 0:  # 文の終わりの短い節は前とつなぐ
        c = chunks[i]
        if len(_PUNCT.sub("", c)) <= 3 and (c.endswith("。") or i == len(chunks) - 1 or not _PUNCT.sub("", c)):
            chunks[i - 1] += c; del chunks[i]
        i -= 1
    cuts, n = set(), 0
    for c in chunks[:-1]:
        n += len(c); cuts.add(n)
    out, n = [], 0
    for x in parts:
        if x.startswith("<"):
            out.append(x); continue
        for ch in x:
            if n in cuts and n:
                out.append("<wbr>")
            out.append(ch); n += 1
    return "".join(out)


def 文(s):
    """<b> <wbr> だけ通して、他は逃がす。文節の切れ目に <wbr>"""
    s = re.sub(r"&lt;(/?b|wbr)&gt;", r"<\1>", html.escape(str(s), quote=False))
    return s if "<wbr>" in s else 区切る(s)  # 自分で <wbr> を入れた文はそのまま


def E(x):
    return html.escape(str(x), quote=False)


def 行き先(u, 画像=False):
    """href・src に入れる URL を確かめて逃がす（javascript: などは止める）"""
    u = str(u).strip()
    if re.match(r"(?i)\s*(javascript|vbscript|data):", u) and not (画像 and u.lower().startswith("data:image/")):
        err(f"行き先に使えない URL: {u[:40]}")
    return html.escape(u, quote=True)


def 円(n):
    return f"¥{int(round(n)):,}"


def hex2rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        err(f"色が #rrggbb でない: {h}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(h, to, t):
    a, b = hex2rgb(h), hex2rgb(to)
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


def 明るさ(h):
    r, g, b = (c / 255 for c in hex2rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


# ---------- 縦長の値段画像（SVG） ----------
SERIF = "'Hiragino Mincho ProN','Yu Mincho','Noto Serif JP','Noto Serif CJK JP',serif"
COIN = {  # 硬貨の地の色は物の色（ブランドの色ではない）
    500: ("#e3cf8e", "#a8904a", "500", False), 100: ("#eeeef0", "#a9a9b0", "100", False),
    50: ("#efeff1", "#acacb3", "50", True), 10: ("#e09a68", "#9a5328", "10", False),
    5: ("#eccd6a", "#b08a22", "", True), 1: ("#f6f6f6", "#c3c3c3", "1", False),
}


def 字幅(s, size):
    """明朝の幅の見積もり: 全角1em・半角0.55em（textLength で実際の幅をこれに合わせる）"""
    return sum(size * (0.55 if ord(c) < 0x2E80 else 1.0) for c in s)


def 一行(x, y, s, size, fill, weight=400, anchor="middle"):
    s = str(s)
    w = 字幅(s, size)
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{SERIF}" font-size="{size:.0f}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" textLength="{w:.0f}" lengthAdjust="spacingAndGlyphs">{html.escape(s)}</text>'), w


def 収める(s, size, maxw):
    w = 字幅(s, size)
    return size if w <= maxw else size * maxw / w


def 硬貨(n):
    out, rest = [], int(n)
    for c in (500, 100, 50, 10, 5, 1):
        while rest >= c:
            out.append(c); rest -= c
    return out


def 値段画像(o, 色):
    W, H = 816, 1200  # 幅÷高さ 0.68（_必ず入れる物.md の 0.67〜0.75 に入れる。手本 800×1200 は 0.667 で外れるため）
    dark, soft, ink = 色["濃い"], 色["淡い"], "#2f2226"
    p = []
    p.append(f'<rect width="{W}" height="{H}" fill="#fff"/><rect width="{W}" height="{H}" fill="{soft}" opacity=".35"/>')
    # 上の一言
    if o.get("上の一言"):
        t, _ = 一行(W / 2, 92, o["上の一言"], 収める(o["上の一言"], 30, 640), dark)
        p.append(t)
    # 見出し: 「は、」の後ろに下線
    hd = o["見出し"]; size = 収める(hd, 68, 730)
    i = hd.find("は、")
    if 0 < i < len(hd) - 3:
        a, b = hd[:i + 2], hd[i + 2:]
        wa, wb = 字幅(a, size), 字幅(b, size)
        x0 = W / 2 - (wa + wb) / 2
        ub = b.rstrip("。")
        p.append(f'<rect x="{x0 + wa:.0f}" y="{222:.0f}" width="{字幅(ub, size):.0f}" height="7" rx="3" fill="{dark}" opacity=".85"/>')
        p.append(一行(x0, 205, a, size, ink, 800, "start")[0])
        p.append(一行(x0 + wa, 205, b, size, ink, 800, "start")[0])
    else:
        p.append(一行(W / 2, 205, hd, size, ink, 700)[0])
    # 淡い地の箱
    p.append(f'<rect x="64" y="285" width="688" height="870" rx="36" fill="{soft}"/>')
    dy = {0: 110, 1: 55}.get(bool(o.get("比べ")) + bool(o.get("締め")), 0)  # 下の2行が無い分だけ中身を下げて、箱の中の空きを上下に分ける
    p.append(一行(W / 2, 378 + dy * .6, o["前提"], 収める(o["前提"], 34, 600), ink)[0])
    # 硬貨の並び（1日あたりを硬貨で数えられる時だけ）
    cs = 硬貨(o["日"]) if o["日"] <= 2000 else []
    if 0 < len(cs) <= 10:
        r = min(62, 300 / len(cs)); gap = r * 0.12
        tot = len(cs) * 2 * r + (len(cs) - 1) * gap; x = W / 2 - tot / 2 + r
        for k, c in enumerate(cs):
            hi, lo, label, hole = COIN[c]
            gid = f"c{k}"
            p.append(f'<defs><radialGradient id="{gid}" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="{hi}"/><stop offset="1" stop-color="{lo}"/></radialGradient></defs>')
            p.append(f'<circle cx="{x:.0f}" cy="{530 + dy:.0f}" r="{r:.0f}" fill="url(#{gid})" stroke="{lo}" stroke-width="2"/>')
            p.append(f'<circle cx="{x:.0f}" cy="{530 + dy:.0f}" r="{r * .82:.0f}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/>')
            if hole:
                p.append(f'<circle cx="{x:.0f}" cy="{530 + dy:.0f}" r="{r * .22:.0f}" fill="{soft}" stroke="{lo}" stroke-width="2"/>')
            if label:
                ly = 530 + dy - r * .38 if hole else 530 + dy + r * .2
                p.append(f'<text x="{x:.0f}" y="{ly:.0f}" font-family="Arial,sans-serif" font-size="{r * (.5 if len(label) < 3 else .4):.0f}" font-weight="700" fill="#fff" fill-opacity=".9" text-anchor="middle">{label}</text>')
            x += 2 * r + gap
    # 大きい数字
    num = f"{o['日']:,}"; ns = 収める(num, 230, 470)
    wn, wy = 字幅(num, ns), 字幅("円", ns * .42)
    x0 = W / 2 - (wn + wy + 10) / 2
    p.append(一行(x0, 815 + dy, num, ns, dark, 800, "start")[0])
    p.append(一行(x0 + wn + 10, 815 + dy, "円", ns * .42, dark, 800, "start")[0])
    if o.get("比べ"):
        p.append(一行(W / 2, 945, o["比べ"], 収める(o["比べ"], 32, 600), ink)[0])
    if o.get("締め"):
        p.append(一行(W / 2, 1065, o["締め"], 収める(o["締め"], 36, 600), ink)[0])
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(p)}</svg>'
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


# ---------- 組む ----------
def 組む(d, 出す="全部"):
    for k in ("色", "セット", "比べる物", "保証の日数", "ボタン"):
        if not d.get(k):
            err(f"「{k}」が無い")
    for k in 外せない:
        if k in d:
            print(f"注意: 「{k}」は入力では変えられない（いちばん大きいセットに一番人気・選ばれた状態は道具が必ず付ける）。読み捨てた", file=sys.stderr)
    c = d["色"]
    if not c.get("主"):
        err("「色」の「主」が無い")
    主 = c["主"]
    色 = {
        "主": 主,
        "濃い": c.get("濃い") or mix(主, "#000000", .18),
        "淡い": c.get("淡い") or mix(主, "#ffffff", .88),
        "枠": c.get("枠") or mix(主, "#ffffff", .12),
        "値段": c.get("値段") or "#d93025",
    }
    for k in ("主", "濃い", "淡い", "枠", "値段"):
        hex2rgb(色[k])  # #rrggbb 以外は止める（属性に入れるため）
    色["線"] = mix(色["淡い"], 色["主"], .12)
    on = "#fff" if 明るさ(主) < .72 else "#2f2226"
    字 = d.get("字") or {}
    style = (f"--nd-main:{色['主']};--nd-dark:{色['濃い']};--nd-soft:{色['淡い']};--nd-frame:{色['枠']};"
             f"--nd-price:{色['値段']};--nd-line:{色['線']};--nd-on-main:{on};")
    if 字.get("形"):
        if re.search(r"[;{}<>\\]", 字["形"]):
            err("「字」の「形」に ; { } < > \\ は使えない")
        style += f"--nd-font:{字['形']};"
    if 字.get("見出しの太さ"):
        style += f"--nd-h-weight:{int(字['見出しの太さ'])};"

    sets = d["セット"]
    for s in sets:
        for k in ("数", "値段", "通常"):
            if k not in s:
                err(f"セット {s.get('名前', '?')} に「{k}」が無い")
        if not (s["数"] > 0 and s["値段"] > 0 and s["通常"] >= s["値段"]) or (s.get("登録後") is not None and not 0 < s["登録後"] <= s["値段"]):
            err(f"セット {s.get('名前', '?')} の数・値段が合わない（数>0・値段>0・通常>=値段・0<登録後<=値段）")
    大 = max(sets, key=lambda s: s["数"])
    if 大["値段"] < max(s["値段"] for s in sets):
        err(f"いちばん大きいセット（{大.get('名前')}）の値段が、並べた中でいちばん高くない。いちばん大きいセットを、いちばん高い値段で見せる決まり（_必ず入れる物.md の 2）")
    単位 = d.get("単位", "個")
    名 = lambda s: s.get("名前") or f"{s['数']}{単位}"
    セット名 = lambda s: 名(s) if 名(s).endswith(("セット", "組")) else 名(s) + "セット"
    登録 = d.get("登録", "メール登録")
    one = d.get("1日あたり") or {}
    元 = one.get("元") or ("登録後" if 大.get("登録後") else "値段")
    base = 大.get(元) or 大["値段"]
    日数 = int(one.get("日数", 365))
    if 日数 <= 0:
        err("「1日あたり」の「日数」は1以上")
    日 = int(round(base / 日数))
    一つ = lambda s: (s.get(元) or s["値段"]) / s["数"]
    割引 = d.get("割引") or f"{round((1 - 大['値段'] / 大['通常']) * 100)}%OFF"
    保証 = int(d["保証の日数"])
    送料 = d.get("送料無料", True)

    # 前振り・比べる物
    見出し = d.get("見出し") or f"いまは{割引}。1日あたり約{日}円です"
    前振り = "\n".join(f"<p>{文(x)}</p>" for x in d.get("前振り", []))
    比べ = "\n".join(f'  <li><b>{文(x["名"])}：</b>{文(x["文"])}</li>' for x in d["比べる物"])
    # 価格の箱の注
    注 = []
    if 大.get("登録後"):
        注.append(f"{登録}でさらに{大['値段'] - 大['登録後']:,}円OFF（{円(大['登録後'])}）")
    if 大.get("おまけ"):
        注.append(大["おまけ"] if re.search(r"(つき|付き|無料|プレゼント)$", 大["おまけ"]) else f"{大['おまけ']}つき")
    if 送料:
        注.append("送料無料")
    注.append(f"{保証}日間の返金保証")
    # 1日あたりの文（本文で言う）
    一日文 = ""
    if 大.get("登録後") and 元 == "登録後":
        一日文 += f"{E(セット名(大))}は、{E(登録)}をすると {円(大['登録後'])}\u00a0です。</p>\n<p>"
    言い方 = one.get("言い方") or (f"1年使うと" if 日数 == 365 else f"{日数}日で見ると")
    一日文 += f"1{E(単位)}あたり {円(一つ(大))}。{E(言い方)}、<b>1日あたり約{日}円</b>です。"
    # 値段画像
    gi = dict(d.get("値段画像") or {})
    if gi.get("ファイル"):
        src = 行き先(gi["ファイル"], 画像=True)
    else:
        gi.setdefault("見出し", f"{円(base)}は、高いでしょうか。")
        gi.setdefault("前提", f"{名(大)}を{('1年' if 日数 == 365 else f'{日数}日')}で見ると、1日あたり")
        gi["日"] = 日
        src = 値段画像(gi, 色)
    # 画像の後: 1つあたりの比べ（嘘にならない時だけ「いちばん安い」）
    if "画像の後" in d:
        後 = "\n".join(f"<p>{文(x)}</p>" for x in d["画像の後"])
    else:
        並 = sorted(sets, key=lambda s: s["数"])
        安い = min(sets, key=一つ) is 大
        一覧 = "、".join((f"<b>{E(セット名(s))}は\u00a0{円(一つ(s))}</b>" if s is 大 else f"{E(セット名(s))}は\u00a0{円(一つ(s))}") for s in 並)
        後 = ("<p>" + 区切る(f"1{E(単位)}あたりで比べると、いちばん安いのは{E(セット名(大))}です。") + "</p>\n" if 安い and len(sets) > 1 else "") + ("<p>" + 区切る(一覧 + "\u00a0です。") + "</p>" if len(sets) > 1 else "")
    # セットのカード
    cards = []
    href0 = d["ボタン"].get("行き先") or "#"
    for s in sorted(sets, key=lambda s: s["数"]):
        is大 = s is 大
        u = []
        if s.get("登録後"):
            u.append(f"登録後 {円(s['登録後'])}")
        u.append(f"1{単位}あたり {円(一つ(s))}")
        last = [x for x in ((f"1日約{日}円" if is大 else ""), s.get("おまけ", ""), ("送料無料" if 送料 and not is大 else "")) if x]
        if last:
            u.append("・".join(文(x) for x in last))
        sel = ' is-sel' if is大 else ''
        cur = ' aria-current="true"' if is大 else ''
        badge = '<span class="nd-badge">一番人気</span>' if is大 else ''
        link = 行き先(s.get("行き先") or href0)
        cards.append(
            f'  <a class="nd-set{sel}" data-cta href="{link}"{cur}>{badge}'
            f'<div class="nd-n">{文(名(s))}</div><div class="nd-y">{円(s["値段"])}</div>'
            f'<div class="nd-u">{"<br>".join(u)}</div><div class="nd-go">選ぶ ›</div></a>')
    セット後 = "\n".join(f"<p>{文(x)}</p>" for x in d.get("セットの後", []))
    # 帯
    帯 = ""
    if d.get("お知らせ帯"):
        f = d["お知らせ帯"]
        帯 = (f'<div class="nd-flash"><b>{文(f.get("頭", "● お知らせ："))}</b>{文(f["文"])}'
             + (f' <a data-cta href="{行き先(f.get("行き先") or href0)}">{文(f["リンク"])}</a>' if f.get("リンク") else "") + "</div>")
    固定 = ""
    fx = d.get("固定帯", {})
    if fx is not False:
        fx = fx or {}
        frm = f' data-nedan-from="{html.escape(fx["出す所"])}"' if fx.get("出す所") else ""
        固定 = f'<div class="nd-stick off"{frm}><a data-cta href="{行き先(fx.get("行き先") or href0)}">{文(fx.get("文") or d["ボタン"]["文"])}</a></div>'
    ボタン下 = d.get("ボタンの下") or f"{セット名(大)}が一番人気・{割引}・{保証}日間の返金保証つき"

    外枠 = ""
    for k, v in (d.get("外枠の属性") or {}).items():  # 例 {"id": "thanks", "hidden": true}。記事の側で段を出し入れする印をそのまま残す
        if not re.fullmatch(r"[a-z][a-z0-9-]*", k) or k.startswith("on") or k in ("class", "style", "data-tasu", "data-nedan", "data-dan"):
            err(f"外枠の属性に使えない名前: {k}")
        外枠 += f" {k}" if v is True else f' {k}="{html.escape(str(v), quote=True)}"'
    t = open(os.path.join(HERE, "値段の段.html"), encoding="utf-8").read()
    if 出す == "札だけ":  # 問いの前の札: 縦長の値段画像と画像の後の文を出さない（後の段で「全部」を出す）
        t = re.sub(r"<figure class=\"nd-fig\">.*?</figure>\n\{\{画像の後\}\}\n", "", t, flags=re.S)
    t = re.sub(r"^<!--.*?-->\n", "", t, flags=re.S)
    css = re.sub(r"/\*.*?\*/", "", open(os.path.join(HERE, "値段の段.css"), encoding="utf-8").read(), flags=re.S)
    js = re.sub(r"/\*.*?\*/", "", open(os.path.join(HERE, "値段の段.js"), encoding="utf-8").read(), flags=re.S)
    sub = {
        "段の印": (f' data-dan="{html.escape(str(d["段の印"]))}"' if d.get("段の印") else "") + 外枠 + (' data-nedan-part="札だけ"' if 出す == "札だけ" else ""),
        "色": html.escape(style, quote=True), "CSS": re.sub(r"\n\s*", "", css), "JS": js.strip(),
        "お知らせ帯": 帯, "見出し": 文(見出し), "前振り": 前振り,
        "比べる前の一文": 文(d.get("比べる前の一文") or "まず、今使っている物の値段と比べてみてください。"),
        "比べる物": 比べ, "札": 文(d.get("札") or 割引), "箱のセット名": 文(セット名(大)),
        "通常の値段": 円(大["通常"]), "今の値段": 円(大["値段"]), "箱の注": "・".join(文(x) for x in 注),
        "1日あたりの文": "</p>\n<p>".join(区切る(x) for x in 一日文.split("</p>\n<p>")), "値段画像": src, "値段画像の説明": f"1日あたり約{日}円",
        "画像の後": 後, "セットの数": str(len(sets)), "セット": "\n".join(cards), "セットの後": セット後,
        "行き先": 行き先(href0), "ボタンの文": 文(d["ボタン"]["文"]), "ボタンの下": 文(ボタン下), "固定帯": 固定,
    }
    for k, v in sub.items():
        t = t.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{[^}]+\}\}", t)
    if left:
        err(f"ひな形に埋まらない所: {left}")
    return re.sub(r"\n{2,}", "\n", t)


def main(a):
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); return 0 if a else 2
    d = json.load(open(a[0], encoding="utf-8"))
    出す = a[a.index("--出す") + 1] if "--出す" in a else "全部"
    if 出す not in ("全部", "札だけ"):
        err("--出す は 全部 か 札だけ")
    out = 組む(d, 出す)
    o = a[a.index("-o") + 1] if "-o" in a else None
    if o:
        open(o, "w", encoding="utf-8").write(out)
    else:
        sys.stdout.write(out)
    if "--見本" in a:
        p = a[a.index("--見本") + 1]
        font = (d.get("字") or {}).get("形", "'Noto Sans JP','Hiragino Sans',sans-serif")
        fam = re.match(r"""\s*["']?([^"',]+)""", font).group(1).strip()
        gf = (f"<link rel=stylesheet href='https://fonts.googleapis.com/css2?family={fam.replace(' ', '+')}:wght@400;500;700;900&display=swap'>"
              if not fam.startswith(("Hiragino", "Yu ", "-apple")) else "")
        page = ("<!doctype html><html lang=ja><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
                "<meta name=robots content=noindex><title>値段の段 見本</title>" + gf + "<style>*{box-sizing:border-box}body{margin:0;color:#2f2226;"
                f"font-family:{font};font-size:17px;line-height:1.85}}.wrap{{max-width:720px;margin:0 auto;padding:0 16px 40px}}"
                "p{margin:0 0 1.1em}h2{font-size:23px;line-height:1.5;margin:44px 0 16px}img{max-width:100%}"
                "@media (max-width:480px){body{font-size:16.5px}h2{font-size:21px}}</style></head><body><div class=wrap>"
                + out + "<div style='height:900px'></div></div></body></html>")
        open(p, "w", encoding="utf-8").write(page)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
