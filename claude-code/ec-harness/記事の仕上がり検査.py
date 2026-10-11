#!/usr/bin/env python3
"""記事のページ（index.html）だけを見て、本人に出す前に機械で落とす（2026-10-09 本人「構造的に直して」）。

使い方: python3 記事の仕上がり検査.py <記事のフォルダか index.html>
終了コード: 0 全部通った / 1 落ちた所がある（行ごとに出す） / 2 読めなかった

見る物（最終確認の表のうち、機械で決められる物だけ。目で見る物は表に残す）:
  1. 「未定」の字が画面に出ていない（HTML のコメントは数えない）
  2. 細長い画像が無い（縦÷横 が 0.4 未満か 2.5 より大きい。80px 未満の飾りと svg は数えない）
  3. 同じ物を指す数字がページの中で食い違っていない（声・評価の数・使っている人の数・保証の日数）
  4. 文の書き方がここちドライの記事の幅に入っている（1文の平均 18〜30字・数字の無い60字超えの文が3本以下・強調は 100〜260字に1回）
     基準の元: 針マット/ここちドライの手本/共通点.md（平均22〜27字・約165字に1回）
  5. テスト用の印がある（noindex と「テスト用の値」のコメント）。公開前に本物の値へ替えるため
  6. 最悪の結末の箱（data-tasu="1"）が読み手への警告の言い方になっていない（「こうなります」「放っておくと」「放置すると」「読まずに」「⚠」が0）。
     「最後まで読」がページに1回だけある（2026-10-11 本人「押しつけにせず、書き手が寄り添う。最後まで読んでほしいは自然に1回」。正本は Vault ec/構造/型/_必ず入れる物.md の「1 の言い方」）
"""
import html, os, re, sys

def 読む(p):
    f = os.path.join(p, "index.html") if os.path.isdir(p) else p
    return f, open(f, encoding="utf-8", errors="ignore").read()

def 画面の字(s):
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", "", s, flags=re.S | re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</(p|h[1-6]|li|div|blockquote)>", "\n", s, flags=re.I)
    return html.unescape(re.sub(r"<[^>]+>", "", s))

def 画像の縦横(f, s):
    bad = []
    try:
        from PIL import Image
    except ImportError:
        return ["Pillow が無いので画像を測れない（pip install pillow）"]
    base = os.path.dirname(f)
    srcs = set(re.findall(r'<img[^>]+src="([^"]+)"', s)) | set(re.findall(r'srcSet="([^" ,]+)', s))
    for src in sorted(srcs):
        if src.startswith(("http", "data:", "//")) or src.lower().endswith(".svg"):
            continue
        p = os.path.join(base, src.split("?")[0])
        if not os.path.exists(p):
            bad.append(f"画像が無い: {src}"); continue
        w, h = Image.open(p).size
        if min(w, h) < 80:
            continue
        r = h / w
        if r < 0.4 or r > 2.5:
            bad.append(f"細長い画像: {src}（{w}×{h}・縦÷横 {r:.2f}）")
    return bad

def 数字の食い違い(t):
    """同じ物を指す数字だけを比べる（医者の人数と客の人数のような別の数は比べない）"""
    bad = []
    n = r"(\d{1,3}(?:,\d{3})+|\d{3,})"
    声 = set(re.findall(n + r"\s*(?:件|人)(?:以上)?(?:の|が|を)?\s*(?:声|レビュー|評価|口コミ)", t))
    声 |= set(re.findall(r"(?:声|レビュー|評価|口コミ)[^。\n]{0,8}?" + n + r"\s*(?:件|人)", t))
    使う人 = set(re.findall(n + r"\s*人(?:以上)?(?:が|の方が)(?:使|愛用|選|購入|試)", t))
    保証 = set(re.findall(r"(\d+)\s*日間?(?:の)?(?:返金|全額返金|お試し|保証)", t))
    for 名, v in (("声・評価の数", 声), ("使っている人の数", 使う人), ("保証の日数", 保証)):
        if len(v) > 1:
            bad.append(f"{名}が食い違う: {'・'.join(sorted(v))}（同じ物を指すなら1つにそろえる）")
    return bad

def 文の書き方(s, t):
    bad = []
    文 = [x.strip() for x in re.split(r"(?<=[。！？])|\n", t) if len(x.strip()) >= 6]
    if not 文:
        return ["本文の文が取れない"]
    平均 = sum(len(x) for x in 文) / len(文)
    if not 18 <= 平均 <= 30:
        bad.append(f"1文の平均が {平均:.1f}字（手本は22〜27字。18〜30字に入れる）")
    長い = [x for x in 文 if len(x) > 60 and not re.search(r"\d", x)]
    if len(長い) > 3:
        bad.append(f"数字の無い60字超えの文が {len(長い)}本（3本以下）: 「{長い[0][:30]}…」")
    強調 = len(re.findall(r"<(strong|b|mark)\b", s, flags=re.I))
    字数 = len(re.sub(r"\s", "", t))
    if 強調 == 0:
        bad.append("強調（太字・色）が0回")
    else:
        間 = 字数 / 強調
        if not 100 <= 間 <= 260:
            bad.append(f"強調が {間:.0f}字に1回（手本は約165字に1回。100〜260字に入れる）")
    return bad

def テストの印(s):
    bad = []
    if not re.search(r'name="robots"\s+content="noindex"', s):
        bad.append('noindex が無い（<meta name="robots" content="noindex">）')
    if "テスト用の値" not in s:
        bad.append("「テスト用の値」のコメントが無い（決めた値の一覧の場所を書く）")
    return bad

def 寄り添い(s, t):
    bad = []
    m = re.search(r'data-tasu="1"', s)
    if m:
        seg = s[m.start():m.start() + 2500]
        nxt = re.search(r'data-tasu="[02-9]', seg)
        box = 画面の字(seg[:nxt.start()] if nxt else seg)
        hit = [w for w in ("こうなります", "放っておくと", "放置すると", "読まずに", "⚠") if w in box]
        if hit:
            bad.append(f"最悪の結末の箱が読み手への警告の言い方: {'・'.join(hit)}（書き手の立場で、知っている理由と気持ちで言う。_必ず入れる物.md の「1 の言い方」）")
    n = len(re.findall(r"最後まで読", t))
    漫画 = re.search(r'data-format="漫画"|class="[^"]*manga', s)  # 漫画は物語で読ませるので入れない（2026-10-11 本人）
    if n != 1 and not (漫画 and n == 0):
        bad.append(f"「最後まで読んでほしい」がページに {n}回（書き手の気持ちとして自然に1回）")
    return bad

def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    try:
        f, s = 読む(argv[1])
    except Exception as e:
        print(f"読めなかった: {e}"); return 2
    t = 画面の字(s)
    bad = []
    n = t.count("未定")
    if n:
        bad.append(f"画面に「未定」が {n}か所")
    bad += 画像の縦横(f, s) + 数字の食い違い(t) + 文の書き方(s, t) + テストの印(s) + 寄り添い(s, t)
    if bad:
        print("\n".join("- " + x for x in bad)); return 1
    print("通った"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
