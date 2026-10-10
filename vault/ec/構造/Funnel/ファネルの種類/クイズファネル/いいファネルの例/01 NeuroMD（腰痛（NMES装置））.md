<!-- 例 -->
# 01 NeuroMD（腰痛（NMES装置））— クイズファネル example

読む人: この型（適格審査型（Am I a candidate））の実物を、広告→質問→結果→オファー→売り場まで通しで1本見たい人。
読む時: 自分のクイズの問い・幕間・結果の出し方・値段の出す位置を決める時。
読まなくていい条件: 12本の比較だけ要る時は [[_index]] か `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

出典: [92750214](https://app.gethookd.ai/share/ad/92750214?signature=2eb717a16cd6e3c4466be4c23613a38639719f4d0fe3e8d98bc65b9ea8deeb2e)（GetHookd・share_url は期限なし）
LP: https://getneuromd.com/pages/quiz
形式: 動画 1074s（17分54秒）・US・Facebook／Instagram・着地 quiz_page
拾った日: 2026-09-11
稼働日数 / 成績: 148日 / score 100（GetHookd の黒箱。売上ではない）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/quiz-teardown/raw/92750214.full.txt`）／`F`=ローカルmp4から切った絵／`Q`=クイズを dia で歩いた実測（`ec/wiki/quiz-teardown/lp/`）／`L`=LP・店の実測／`J`=判断

## なぜ良いのか（1行）

17分54秒のVSLの後に「あなたは対象か」を5問で判定させ、対象なら62%OFFを権利として渡す。値段は動画で言わず、合格の後に$399.99→$149.95で出す。 `J`

## 分解（ファネル通し・5部品）

| 位置 | 出ている物 | 何をやっているか |
|---|---|---|
| 01 入口（広告） | 動画 17分54秒・型は下の9ブロック | 0:00–0:13 `T`「Physical therapists will tell you that dozens of appointments are needed to manage your back pain. This ca… |
| 02 質問設計 | 5問（＋入口の13択）・幕間0・失格1 | getneuromd.com/pages/quiz（Shopifyページ）: 「WHAT BACK CONDITION(S) DO YOU HAVE? SELECT ALL THAT APPLY」13択のチェック（Chronic Back Pain／Sciatica／Herniated Discs／…／I'm not … |
| 03 結果ページ | 結果ページは無い。5問目のメール入力がそのまま「合格」画面（62% OFF・87%一致）。送信で `offer.getneuromd.com/ctd-offer-2` へ跳ぶ `Q`… | 回答を「あなたの状態」に言い換えて、次の画面の値段を受け入れさせる |
| 04 オファー提示 | 1台 $149.95（定価 $399.99・62%OFF）。装置の1択。関連品は NeuroMD Restore $44.99〜（店） | offer.getneuromd.com/ctd-offer-2（Funnelish・Shopifyのカートへ）: 「You qualify for a 62% off discount.」「Medical Discount Reserved For 10:00」タイマー／Retail $399.99 → Your P… |
| 05 チェックアウト | 広告→入口ページ（13択）→Check Eligibility→クイズ5問→メール→オファーページ→Shopifyカート→チェックアウト。6段 | 保証: 60日（結果が出なければ返金）＋1年保証 |

## 盗む所

- 対象外を落とす問い（ペースメーカー）を入れて医療機器の顔にする
- 「Your pain type matches 87% of our 1,139,067 users」で合格感を作ってからメールを取る <!-- 掘った: クイズ・LPの逐語 Q/L。`ec/wiki/quiz-teardown/lp/92750214_*` で照合 -->
- 値段を「qualify for 62% off」の権利にして、動画では金額を言わない

## 01 入口（広告）— 9ブロック分解

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:13 `T`「Physical therapists will tell you that dozens of appointments are needed to manage your back pain. This can cost hundreds of dollars monthly.」（`F` 赤帯テロップ「SIMPLE THINGS YOU CAN DO TO ELIMINATE YOUR BACK PAIN」＋医師が女性の腰を診る実写→3Dの脊椎断面で神経が赤く光る） |
| lead | 0:13–0:41 `T`「there's a secret they may not have told you」「three simple things you can do to eliminate the pain for good」 |
| discovery story | 6:49–8:55 `T`「we've studied over 1,300 patients」「After several prototypes and months of testing, we were facing financial difficulties」「working 12 to 14 hours over a span of 4 months」 | <!-- 掘った: 広告の逐語 T。`raw/92750214.segments.json` の秒で照合 -->
| UMP | 0:41–2:09 `T`「spinal nerve impingement」「This is the root cause of all back pain」「It's a vicious cycle」 |
| UMS | 2:28–4:00 `T`「activating the deep muscles around your spine」「Think of your spine as a bridge and the muscles around it as the cables」→ 7:50「Neuromuscular Electrical Stimulation, or NMES for short」 |
| product reveal | 8:57（50%地点）`T`「The NeuroMD Corrective Therapy Device」「a mini-defibrillator for your back」 |
| price drop | 14:24–15:26 `T`「I've reserved 500 NeuroMD Corrective Therapy devices at a substantially discounted rate」「I recommend purchasing two devices」（金額は言わない） |
| risk reversal | 15:47 `T`「60-day results or refund guarantee」「no questions asked」 |
| testimonials | 11:18–13:30 `T` Barbara「I had lower back pain for years」／男性「herniated discs since 2011」／医師「My patients with chronic back pain have seen remarkable relief」 |
| 権威 | 4:21–6:44 `T`「I'm Elena Hartley, the Director of Research at NeuroMD」「I'm what you might call a super specialist」 |

無かったブロックは「無し」。欠落そのものが発見。

### フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

| 秒 | 絵 | 喋っている言葉 `T` |
|---|---|---|
| 0s | ![[ec/wiki/quiz-teardown/frames/92750214/00s.jpg\|220]] | 「Physical therapists will tell you that dozens of appointments are needed to manage your」 |
| 1s | ![[ec/wiki/quiz-teardown/frames/92750214/01s.jpg\|220]] | 「Physical therapists will tell you that dozens of appointments are needed to manage your」 |
| 2s | ![[ec/wiki/quiz-teardown/frames/92750214/02s.jpg\|220]] | 「Physical therapists will tell you that dozens of appointments are needed to manage your」 |
| 3s | ![[ec/wiki/quiz-teardown/frames/92750214/03s.jpg\|220]] | 「Physical therapists will tell you that dozens of appointments are needed to manage your」 |
| 4s | ![[ec/wiki/quiz-teardown/frames/92750214/04s.jpg\|220]] | 「back pain.」 |
| 5s | ![[ec/wiki/quiz-teardown/frames/92750214/05s.jpg\|220]] | 「This can cost hundreds of dollars monthly.」 |
| 6s | ![[ec/wiki/quiz-teardown/frames/92750214/06s.jpg\|220]] | 「This can cost hundreds of dollars monthly.」 |
| 7s | ![[ec/wiki/quiz-teardown/frames/92750214/07s.jpg\|220]] | 「Typically, a specialist visit can cost around $100, and even then, the relief is often temporary.」 |
| 8s | ![[ec/wiki/quiz-teardown/frames/92750214/08s.jpg\|220]] | 「Typically, a specialist visit can cost around $100, and even then, the relief is often temporary.」 |
| 9s | ![[ec/wiki/quiz-teardown/frames/92750214/09s.jpg\|220]] | 「Typically, a specialist visit can cost around $100, and even then, the relief is often temporary.」 |
| 10s | ![[ec/wiki/quiz-teardown/frames/92750214/10s.jpg\|220]] | 「Typically, a specialist visit can cost around $100, and even then, the relief is often temporary.」 |
| 11s | ![[ec/wiki/quiz-teardown/frames/92750214/11s.jpg\|220]] | 「Typically, a specialist visit can cost around $100, and even then, the relief is often temporary.」 |
| 12s | ![[ec/wiki/quiz-teardown/frames/92750214/12s.jpg\|220]] | 「Typically, a specialist visit can cost around $100, and even then, the relief is often temporary.」 |

### 全シーン × b-roll（`F`）

尺 1073.7秒 ／ 409シーン ／ 平均 2.6秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）。表と絵は `ec/wiki/quiz-teardown/シーン/92750214.md` にあり、下に埋め込む（Obsidianで展開）。

![[ec/wiki/quiz-teardown/シーン/92750214]]

## 02 質問設計 — 入口と全問（`Q`）

入口: getneuromd.com/pages/quiz（Shopifyページ）: 「WHAT BACK CONDITION(S) DO YOU HAVE? SELECT ALL THAT APPLY」13択のチェック（Chronic Back Pain／Sciatica／Herniated Discs／…／I'm not sure）→「Check Eligibility」→ /pages/full-page-questionnaire-4（Zipify Pages）に RevenueHunt のクイズ `AoHpB6`（内部名 Insurance Quiz V2 (No Rebate)）を600pxで埋め込み。日本からは埋め込みが描画されず、`admin.revenuehunt.com/public/quiz/AoHpB6` の公開URLを curl して同じ定義JSON（quiz_json_raw）を取った `Q`

| # | 問い | 選択肢 | 型・次に出る幕間 |
|---|---|---|---|
| 1 | 「How long have you been suffering from back pain?」 | 「Less than 6 months／6-12 months／12 months or longer」 | 単一 |
| 2 | 「Where is your pain located?」 | 「Lower/Mid back／Upper back/Neck／Buttock/Leg／Multiple areas」 | 画像つき単一 |
| 3 | 「Do you have any electronic implants? (i.e. pacemakers, implantable cardioverter defibrillators, pain pump, etc.)」 | 「Yes／No」 | Yes→「Unfortunately, NeuroMD IS NOT Advisable for Use With Electronic Implants」（Retake Question）に飛ぶ | <!-- 掘った: クイズ・LPの逐語 Q/L。`ec/wiki/quiz-teardown/lp/92750214_*` で照合 -->
| 4 | 「We want to make sure we are a good match for you. Please select what may be causing your pain: （NeuroMD does not help with pain caused by tumors.）」 | 「Joint Pain／Spinal Disc Pain／Nerve Pain／Muscle Pain／I'm not too sure」 | 複数 |
| 5 | 「Congratulations! As an ideal candidate, you're eligible for a 62% OFF discount. Your pain type matches 87% of our 1,139,067 users. Save 62% on NeuroMD by entering your email」 | 「メール入力→「Redeem Offer」」 | メールゲート |

問数: 5問（＋入口の13択）・幕間0・失格1

## 03 結果ページ（`Q`）

結果ページは無い。5問目のメール入力がそのまま「合格」画面（62% OFF・87%一致）。送信で `offer.getneuromd.com/ctd-offer-2` へ跳ぶ `Q`

## 04 オファー提示（`L`）

offer.getneuromd.com/ctd-offer-2（Funnelish・Shopifyのカートへ）: 「You qualify for a 62% off discount.」「Medical Discount Reserved For 10:00」タイマー／Retail $399.99 → Your Price $149.95／ShopPayで「From $18 with payment plan」／FSA・HSA対応／60-Day Money Back／1 Year Warranty／Dr. Mark Rosenberg, M.D. の推薦文／12週プロトコル表（Week 1 Mode 1・Week 2-12 Mode 2・Week 13+ Maintenance）／NMES vs Heating Pad vs TENS の比較表／FAQ（保険は効かない・Affirm）／臨床の引用／YouTube埋め込み3本 `L`

- 値段の段: 1台 $149.95（定価 $399.99・62%OFF）。装置の1択。関連品は NeuroMD Restore $44.99〜（店）
- 保証: 60日（結果が出なければ返金）＋1年保証
- 作り: 入口: Shopify／質問: RevenueHunt（Shopifyアプリ）を Zipify Pages に埋め込み／オファー: Funnelish／決済: Shopify

## 05 売り場までの導線

広告→入口ページ（13択）→Check Eligibility→クイズ5問→メール→オファーページ→Shopifyカート→チェックアウト。6段

## 広告 → クイズ → 売り場 のつながり

| 要素 | 広告 | クイズ／売り場 | 判定 |
|---|---|---|---|
| 権威 | Elena Hartley（研究責任者） | Dr. Mark Rosenberg, M.D.（推薦文） | 人が変わる。動画の語り手はLPに出ない |
| 原因 | spinal nerve impingement・深層筋 | 「treat the root problem, not just mask the pain」 | 一致 |
| 解の呼び名 | NMES | 「patented NMES」「FDA-cleared」 | 一致（FDA-clearedはLPだけ） |
| 値段 | 言わない（500台・2台推奨） | $399.99→$149.95・10分タイマー | LPで初めて出る |
| 保証 | 60日 | 60日＋1年保証 | 一致 |

## 補足

`page_type=quiz_page` の12本で唯一、クイズの前に別の入口ページ（13択）がある。
