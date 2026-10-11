# 記事（アドバトリアル）を作る工程 一式

VSL 動画が出来たあと、その飛び先の記事を作る工程を丸ごと入れた物。手順書・木の図・型の棚・参考の分解・検査の道具・実際に作った記事3本が入っている。どれも 2026-10-10 時点で使っている最新版を、1文字も変えずに写した。

## どこから読むか

1. `vault/ec/構造/ハーネス/05 記事を作る.md` が手順書。いちばん下の「VSL 動画の飛び先の記事を一回で作る道」の表 1〜10 を上から順にやる
2. 木の図は Obsidian で開く（`.canvas`）
   - `vault/ec/構造/ハーネス/VSLから記事まで_全体の木.canvas`: VSL の形式（20種）→ 記事の型（8種）のつながり。カードから各ノートへ飛べる
   - `vault/ec/構造/ハーネス/買わない理由を消す順番.canvas`: 客の気づきの段階（Unaware〜Product Aware）ごとの型
   - `vault/ec/構造/ハーネス/_参考再現フロー_工程と関門_2026-10-03.canvas`: 全工程（商品→客→アングル→広告→記事→店→配信→測る→学ぶ）の正本の図
3. 手本の完成品: `claude-code/team-room/引き継ぎ/VSL記事リサーチ_資料/針マット/記事_ストレッチで戻る腰/` ほか2本（`index.html` をブラウザで開く。移植表・審査の記録・最終確認も同じフォルダにある）

## 置き場所

手順書と道具は、決まった場所にある前提でパスを書いている。そのまま動かすなら次の場所に置く。

| このリポの中 | 置く場所 |
|---|---|
| `vault/ec/` | `~/Documents/Obsidian Vault/ec/` |
| `claude-code/` | `~/Claude Code/` |

## 中身

| 置き場 | 何か |
|---|---|
| `vault/ec/構造/ハーネス/` | 手順書・役（ファネル責任者・記事ライター・編集長）・組織図・実行の決まり・木の図 |
| `vault/ec/構造/VSL structure/VSL example/` | 木の図のカードの中身（VSL の実例20本と段階別の型） |
| `vault/ec/構造/Funnel/ファネルの種類/アドバトリアルファネル/` | 記事の型8種のブロックの詳細（入りの作り方など） |
| `vault/ec/構造/型/` | 型の棚（参考の記事を割った物） |
| `vault/ec/wiki/ads-brain/playbooks/` | 書く時の関門（advertorial.md の1〜32、native-ads.md） |
| `vault/ec/決めたこと.md` | 作る時に毎回守る決まり |
| `claude-code/team-room/引き継ぎ/VSL記事リサーチ_資料/形式別/` | VSL の形式と記事の構造の対応（`_形式と記事の構造.md`）、194本の分解、参考ページの保存 |
| `claude-code/team-room/引き継ぎ/VSL記事リサーチ_資料/針マット/` | 試しで作った記事3本・ここちドライの手本（字・値段の段・CSS）・作業の記録 |
| `claude-code/team-room/引き継ぎ/VSL記事リサーチ_資料/記事の最終確認_ひな形.md` | 出す前の最終確認の表 |
| `claude-code/ec-harness/` | 検査の道具（画像の置き方・記事の検査・仕上がり検査・割り付け検査） |
| `claude-code/adv-kata/` | 参考を数える `measure.py`、記事の殻を作る `新規.sh` |

## 動かすのに要る物

- python3
- `whisper-cli`（文字起こし。モデルは `ggml-large-v3-turbo.bin`）と ffmpeg
- 画像は ChatGPT の画像生成（MCP `chatgpt-image`）
- 新しい参考の保存（下の「新しいリンクから参考を作る」）と動きの検査に要る物:
  - Playwright の Chromium: `pip install playwright && playwright install chromium`
  - node（website-copy の焼き込み `transform.mjs`・`bake.mjs`）
  - ffmpeg・ffprobe、yt-dlp（VSL が動画のページの URL の時）: `brew install ffmpeg yt-dlp`
  - whisper-cli とモデル: `brew install whisper-cpp` のあと `mkdir -p ~/.cache/whisper && curl -L -o ~/.cache/whisper/ggml-large-v3-turbo.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin`（約1.6GB。別の場所に置いた時は `WHISPER_MODEL=<パス>`）
  - opencv-python と numpy（`動きの検査.py`）: `pip install opencv-python numpy`。Pillow（動く WebP を割る時）: `pip install pillow`
- `画像の置き方.py` は裏で動かすブラウザ `dia` を使う。無い時は、ブラウザで測った JSON を `--測った <参考.json> <うち.json>` で渡せば同じ判定になる（やり方は手順書の8）

## 入れていない物

- 動画ファイル（mp4。大きいため）
- 前の回の古い版（`_前の回_20261009`）と道具のバックアップ（`.bak`）

---

# オプション: 日本版のフォーマット（権威の暴露記事・物語の記事・長い診断）と、型を自分で増やす仕組み（2026-10-10 追加）

日本で配信中の勝っている飛び先を割ると、6本中5本が「縦長の記事 → 後ろ3分の1で3問のアンケート → 答えてくれたお礼の割引 → 申込」の形だった。これを写して作るスキルと、新しい型を見つけて子スキルまで作るスキルを足した。

## まず開く物

| 物 | 場所 |
|---|---|
| どの型で作るかを VSL から決める表 | `vault/ec/構造/型/_VSLから型を選ぶ.md`（図は `記事の型の木.canvas` の左「VSL から始める」） |
| 日本のアンケート型を写して1本作るスキル | `claude-skills/quiz-jp-copy/SKILL.md`（検査の道具は `scripts/`） |
| 型を見つけて子スキルまで作るスキル（リンク1本から） | `claude-skills/kata-tsukuru/SKILL.md`（ゴールの判定 `scripts/goal.py`） |
| 日本のアンケート型の型（固定16段・分かれ道・決められない所） | `claude-code/kata-tsukuru/runs/quiz-jp/型.md`・参考6本 `refs/`・変数の木 `木.canvas` |
| どの型にも足す物（最初の画面の最悪の結末・値段の見せ方） | `vault/ec/構造/型/_必ず入れる物.md` |
| 作った見本 | `examples/` の3つ: ここちドライのアンケート型（https://kokochi-quiz-padteki.vercel.app ）・ハリネルのアンケート型（https://harinel-quiz-koshi.vercel.app ）・ここちドライの7問の診断（https://kokochi-shindan-anshin.vercel.app ）。どれも申込のページ（`申込/`）まで |
| 調べた物 | 日本の実物23本 `vault/ec/構造/Funnel/ファネルの種類/クイズファネル/_日本の実物_2026-10-10.md`、X の調べ2本（`vault/ec/構造/Funnel/_Xリサーチ_VSLの飛び先_2026-10-10.md`・`vault/ec/構造/ハーネス/_Xリサーチ_指示とループの作り方_2026-10-10.md`） |

## 置き場所（追加分）

| このリポの中 | 置く場所 |
|---|---|
| `claude-skills/<名前>/` | `~/.claude/skills/<名前>/` |
| `claude-hooks/kiji-guard.py` | `~/.claude/hooks/`（settings.json の PreToolUse Bash と PostToolUse Write|Edit に登録） |

## 流れ（全自動）

1. VSL を割り、`_VSLから型を選ぶ.md` で型を決める
2. その型の手順（日本のアンケート型なら quiz-jp-copy）で作る
3. 機械の検査3本 → 審査役（質と効き目を見る）と読み手の目（参考を見せずに浮いた所を探す）の2人の審査 → 最終確認の箱
4. 全部通ったら `quiz-jp-copy/scripts/公開する.py` が Vercel に上げる（人の承認なし）
5. 新しい型のリンクを渡されたら kata-tsukuru の手順0: 記事を先に割る → 今ある型と照らす → 同じなら VSL の枝を足す・違えば新しい型を作る

## 要る物（追加分）

- Playwright と Chromium（`python3 -m playwright install chromium`）: 幅の検査・画面を撮る
- `dia`（本人のログイン済みのブラウザを裏で動かす道具）: 広告ライブラリをたどる `リンクから辿る.py`
- Vercel の CLI（ログイン済み）: 公開する.py

---

# 新しいリンクから参考を作る（2026-10-11 追加）

保存済みの参考（`形式別/lp/`）に無い記事のリンク1本から、誰の手元でも同じ形で参考を作る。本人の Dia は使わず、Playwright の Chromium（headless）で動く。

```bash
# 1 その記事へ飛ばしている広告を Meta の広告ライブラリでたどる（Dia が無ければ headless に切り替わる）
python3 claude-skills/kata-tsukuru/scripts/リンクから辿る.py <記事のURL> <作業>/辿る/ --国 US
# 2 記事を保存し、段に割り、同じ飛び先の一番長く出ている VSL を文字起こしする
python3 claude-skills/kata-tsukuru/scripts/参考を保存する.py <記事のURL> <作業>/参考/ --辿る <作業>/辿る/
#   VSL の動画が手元にある時は --辿る の代わりに --vsl <mp4かURL>
```

出る物: `生.html`・`焼き込み.html`・`画面_390.png`・`画面_1280.png`・`段.md`（段ごとに画像と文を切らずに全部。動く物はカットの時刻・カットごとのコマの一覧・画面の割り）・`画像/`・`文字起こし.txt`（時刻つき）・`記録.json`。

| 部品 | このリポの中 | 置く場所 |
|---|---|---|
| 焼き込み | `claude-skills/website-copy/scripts/`（transform・bake・lib-clone・fetch） | `~/.claude/skills/website-copy/scripts/` |
| 文字起こし | `claude-skills/fukikae/scripts/01_transcribe.sh` | `~/.claude/skills/fukikae/scripts/` |

部品は `claude-skills/` の並びのまま置けば見つかる（別の場所なら `WEBSITE_COPY_SCRIPTS`・`TRANSCRIBE_SH` で指定）。

取れない物: ログインやボット除けがあるページ（Alibaba・1688 は headless だと CAPTCHA で止まる。道具は「ボット除けで止まった」と言って終了コード2で止まり、空の参考は作らない）。
