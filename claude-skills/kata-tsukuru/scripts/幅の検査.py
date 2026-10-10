#!/usr/bin/env python3
"""出来た飛び先を、パソコン（1280）とスマホ（390）の幅で開き、崩れを数える。

使い方: python3 幅の検査.py <index.html のパスか URL> [--押す <回数>]
  --押す N: アンケートの答えのボタン（[data-answer]）を N 回押し、押すたびに次の問いが出るか、
            最後に「ご回答」の画面が出るかを確かめる（既定 0）
見る物: 文の最後の行に1〜2文字だけ落ちた所（句読点は数えない）・横のはみ出し（ページ幅より広い）・画像の抜け（読めなかった img。小さな画像も数える）・
        細長い画像（幅40pxより大きい物で、縦÷横 0.4未満・2.5超）・押した後の画面の進み
終了コード: 0=全部0 / 1=どれかが1以上 / 2=道具が動かない・開けない（ページの見た目のせいではない）
本人のブラウザ（Dia）には繋がない。手元の Playwright の Chromium を裏で立てる。
"""
import os, sys

JS = r"""async () => {
  // 遅れて読む画像も読ませるため、一番下まで送ってから戻す
  for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
  window.scrollTo(0, 0);
  await Promise.all([...document.images].map(i => i.decode ? i.decode().catch(() => {}) : null));
  const W = document.documentElement.clientWidth;
  const over = [...document.querySelectorAll('body *')].filter(e => {
    const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.right > W + 1 && s.position !== 'fixed' && !e.closest('[data-marquee],.marquee');
  }).slice(0, 5).map(e => e.tagName + '.' + (e.className || '').toString().slice(0, 30));
  const imgs = [...document.images];
  const broken = imgs.filter(i => i.naturalWidth === 0 && getComputedStyle(i).display !== 'none').map(i => (i.currentSrc || i.src).slice(-60));
  const thin = imgs.filter(i => i.naturalWidth > 0 && i.getBoundingClientRect().width > 40)
                   .filter(i => { const q = i.naturalHeight / i.naturalWidth; return q < 0.4 || q > 2.5; })
                   .map(i => i.src.slice(-60));
  // 文の最後の行に1〜2文字だけ落ちた所（句読点と括弧は数えない）。行は「次の字が左に戻った所」で分ける
  await document.fonts.ready;
  const P = /[、。？！「」『』（）()・…\s!?]/;
  const orphans = [];
  for (const el of document.querySelectorAll('p,h1,h2,h3,h4,li,td,dd,span,div,strong,b')) {
    if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
    const r0 = el.getBoundingClientRect(); if (!r0.width || getComputedStyle(el).display === 'none') continue;
    const chars = [];
    const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let n; while ((n = walk.nextNode())) {
      for (let i = 0; i < n.textContent.length; i++) {
        const rg = document.createRange(); rg.setStart(n, i); rg.setEnd(n, i + 1);
        const b = rg.getClientRects()[0]; if (b && b.width) chars.push([n.textContent[i], b.left]);
      }
    }
    if (chars.length < 6) continue;
    let lines = [[]];
    for (let i = 0; i < chars.length; i++) {
      if (i && chars[i][1] < chars[i - 1][1] - 2) lines.push([]);
      lines[lines.length - 1].push(chars[i][0]);
    }
    if (lines.length < 2) continue;
    const last = lines[lines.length - 1].filter(c => !P.test(c));
    if (last.length > 0 && last.length <= 2) orphans.push(lines.slice(-2).map(l => l.join('')).join('｜').slice(-30));
  }
  // 必ず入れる物2: 値段の段（data-tasu=2）の中の縦長の画像は 幅÷高さ 0.67〜0.75
  const price = [...document.querySelectorAll('[data-tasu="2"] img')].filter(i => i.naturalWidth && i.naturalHeight > i.naturalWidth)
    .map(i => i.naturalWidth / i.naturalHeight).filter(q => q < 0.67 || q > 0.75).map(q => q.toFixed(3));
  return {scrollW: document.documentElement.scrollWidth, W, over, broken, thin, orphans: [...new Set(orphans)], price};
}"""

STATE = r"""() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const ans = [...document.querySelectorAll('[data-answer]')].filter(vis);
  const qs = new Set(ans.map(a => (a.closest('[data-q],[data-dan]') || a.parentElement).getAttribute('data-q') || (a.closest('[data-dan]') || {}).dataset?.dan || ''));
  return {answers: ans.length, groups: [...qs].join(','), thanks: [...document.querySelectorAll('body *')].some(e => vis(e) && e.children.length === 0 && /ご回答/.test(e.textContent + (e.alt || '')))};
}"""


def main(a):
    if not a:
        print(__doc__); return 2
    target = a[0]
    try:
        presses = int(a[a.index("--押す") + 1]) if "--押す" in a else 0
    except (IndexError, ValueError):
        print("使い方: --押す の後に回数（数字）", file=sys.stderr); return 2
    url = target if target.startswith("http") else "file://" + os.path.abspath(os.path.expanduser(target))
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("道具が無い: pip install playwright", file=sys.stderr); return 2
    bad = 0
    try:
        with sync_playwright() as pw:
            try:
                b = pw.chromium.launch(headless=True)
            except Exception as e:
                print(f"Chromium が立たない: {e}\n→ `python3 -m playwright install chromium`", file=sys.stderr); return 2
            try:
                for w, h in ((1280, 800), (390, 844)):
                    pg = b.new_page(viewport={"width": w, "height": h})
                    try:
                        pg.goto(url, wait_until="load", timeout=30000)
                    except Exception as e:
                        print(f"開けない（{w}）: {e}", file=sys.stderr); return 2
                    r = pg.evaluate(JS)
                    wide = r["scrollW"] > r["W"] + 1
                    cnt = int(wide) + len(r["broken"]) + len(r["thin"]) + len(r["orphans"]) + len(r["price"])
                    bad += cnt
                    print(f"幅{w}: はみ出し{'あり ' + str(r['over']) if wide else '0'}・画像の抜け{len(r['broken'])}・細長い画像{len(r['thin'])}・行末の1〜2文字落ち{len(r['orphans'])}・値段の縦長画像の比の外れ{len(r['price'])}")
                    for k in ("broken", "thin", "orphans", "price"):
                        for s in r[k]:
                            print(f"   {k}: {s}")
                    if presses:
                        before = pg.evaluate(STATE)
                        for n in range(presses):
                            btn = pg.query_selector("[data-answer]:visible")
                            if not btn:
                                print(f"幅{w} {n + 1}回目: 押せる答えのボタン（[data-answer]）が無い → ×"); bad += 1; break
                            try:
                                btn.click(timeout=5000)
                            except Exception as e:
                                print(f"幅{w} {n + 1}回目: 押せない（上に別の物が乗っている等）: {str(e).splitlines()[0]} → ×"); bad += 1; break
                            pg.wait_for_timeout(1500)   # ページの中で画面が切り替わる作りは load を待っても戻るので、少し待つ
                            after = pg.evaluate(STATE)
                            last = n == presses - 1
                            if not last and after["groups"] == before["groups"] and after["answers"] == before["answers"]:
                                print(f"幅{w} {n + 1}回目: 押しても次の問いに進まない → ×"); bad += 1; break
                            before = after
                        else:
                            if not pg.evaluate(STATE)["thanks"]:
                                print(f"幅{w}: {presses}回押した後に「ご回答」の画面が見えない → ×"); bad += 1
                            else:
                                print(f"幅{w}: {presses}回押して「ご回答」の画面まで出た")
                    pg.close()
            finally:
                b.close()
    except Exception as e:
        print(f"道具が途中で止まった: {type(e).__name__}: {e}", file=sys.stderr); return 2
    print("通った" if bad == 0 else f"落ちた: {bad}件")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
