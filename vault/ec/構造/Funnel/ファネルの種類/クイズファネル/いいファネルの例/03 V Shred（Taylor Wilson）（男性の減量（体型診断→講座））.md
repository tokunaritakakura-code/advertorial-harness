<!-- 例 -->
# 03 V Shred（Taylor Wilson）（男性の減量（体型診断→講座））— クイズファネル example

読む人: この型（体型診断→VSL型（クイズの出口がVSL＋$57））の実物を、広告→質問→結果→オファー→売り場まで通しで1本見たい人。
読む時: 自分のクイズの問い・幕間・結果の出し方・値段の出す位置を決める時。
読まなくていい条件: 12本の比較だけ要る時は [[_index]] か `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

出典: [96303830](https://app.gethookd.ai/share/ad/96303830?signature=3f339110d2843a23f0c2ea09e69eab0c70dd906315a258dc34e72fa95e3edb84)（GetHookd・share_url は期限なし）
LP: https://le.vshred.com/sp/survey/survey-ga?ad_channel=facebook&utm_medium=cpc-kendago&utm_offer=ken-vs-quiz-fb
形式: 動画 310s（5分10秒）・US・Facebook／Instagram・着地 quiz_page
拾った日: 2026-09-11
稼働日数 / 成績: 133日 / score 100（GetHookd の黒箱。売上ではない）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/quiz-teardown/raw/96303830.full.txt`）／`F`=ローカルmp4から切った絵／`Q`=クイズを dia で歩いた実測（`ec/wiki/quiz-teardown/lp/`）／`L`=LP・店の実測／`J`=判断

## なぜ良いのか（1行）

5分10秒の広告は商品を売らず「6問・20秒・メール不要のクイズ」を売る。クイズの出口は26分54秒のVSL＋$57の買い切り講座で、値段は結果ページで初めて出る。 `J`

## 分解（ファネル通し・5部品）

| 位置 | 出ている物 | 何をやっているか |
|---|---|---|
| 01 入口（広告） | 動画 5分10秒・型は下の9ブロック | 0:00–0:06 `T`「Is there one exercise people should just stop doing when trying to lose weight?」（`F` ポッドキャストのマイク前の男＋コメント吹き… |
| 02 質問設計 | 6問（広告の「six different questions」と一致）・幕間0・メール欄なし | le.vshred.com/sp/survey/survey-ga（自前・curlは403でCloudflare）: 見出し「Discover Your Fat Loss Type & The Truth About Cutting Carbs & Doing Cardio」→ 1問目が最初の画面 `Q`… |
| 03 結果ページ | 結果ページがそのままVSL: le.vshred.com/sp/survey/male-fl「Celebrity Trainer Vince Sant Reveals… How thousands of men with YOUR body type are dropping weight fast WHILE enj… | 回答を「あなたの状態」に言い換えて、次の画面の値段を受け入れさせる |
| 04 オファー提示 | $57 買い切り（講座＋ボーナス7）。1択 | 同じページの動画の下: 「Get Instant Access for $57」10:00タイマー／「Get Fat Loss Extreme + 7x FREE Bonuses NOW!」「YES! I Want Instant Access for Only $57」／30 Day Money-Back Guara… |
| 05 チェックアウト | 広告→クイズ6問→VSLページ（$57）→自前チェックアウト。3段 | 保証: 30日 |

## 盗む所

- 広告の最後で商品でなく「無料・6問・20秒・メール不要」のクイズだけを売る
- 質問を入力型（年齢・身長・体重）にして「計算している」顔にする
- 出口を無料→VSL→買い切り$57の2段にして、値段は結果ページまで出さない

## 01 入口（広告）— 9ブロック分解

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:06 `T`「Is there one exercise people should just stop doing when trying to lose weight?」（`F` ポッドキャストのマイク前の男＋コメント吹き出し「Jessica @askvshred」＋トレッドミルの女性を左右2分割） |
| lead | 0:06–0:45 `T`「Back in the gladiator days, I thought intense workouts, strict diet was the only way」「we're going to teach it to you in 60 seconds」 |
| discovery story | 2:04–2:25 `T`「I decided to delve into this topic and do some research. Turns out this guy is a celebrity trainer」（司会が調べた体） |
| UMP | 0:46–1:20 `T`「This is a metabolism killer」×3「Steady state cardio can actually release cortisol」（Dr. Drew） |
| UMS | 1:29–1:59／2:28–3:00／3:50–3:59 `T`「Carbs don't make you fat」「cardio actually burns calories… replaced with the very next meal」「If you cycle your carbs properly」 | <!-- 掘った: 広告の逐語 T。`raw/96303830.segments.json` の秒で照合 -->
| product reveal | 4:36（88%地点）`T`「This is our body type quiz. That's a free quiz. It's six different questions. Legit 20 seconds.」商品でなくクイズを出す |
| price drop | 無し（`T`「We won't ask for your email or anything like that」で無料を強調） |
| risk reversal | 無し |
| testimonials | 3:11–4:17 `T`「I've lost 30 pounds」「I now went from a 6XL… I'm in a large」「53 pounds」「I went from 189 pounds to 136 pounds」（客の顔出し6人） |

無かったブロックは「無し」。欠落そのものが発見。

### フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

| 秒 | 絵 | 喋っている言葉 `T` |
|---|---|---|
| 0s | ![[ec/wiki/quiz-teardown/frames/96303830/00s.jpg\|220]] | 「Is there one exercise people should just stop doing when trying to lose weight?」 |
| 1s | ![[ec/wiki/quiz-teardown/frames/96303830/01s.jpg\|220]] | 「Is there one exercise people should just stop doing when trying to lose weight?」 |
| 2s | ![[ec/wiki/quiz-teardown/frames/96303830/02s.jpg\|220]] | 「Is there one exercise people should just stop doing when trying to lose weight?」 |
| 3s | ![[ec/wiki/quiz-teardown/frames/96303830/03s.jpg\|220]] | 「Is there one exercise people should just stop doing when trying to lose weight?」 |
| 4s | ![[ec/wiki/quiz-teardown/frames/96303830/04s.jpg\|220]] | 「Is there one exercise people should just stop doing when trying to lose weight?」 |
| 5s | ![[ec/wiki/quiz-teardown/frames/96303830/05s.jpg\|220]] | 「Is there one exercise people should just stop doing when trying to lose weight?」 |
| 6s | ![[ec/wiki/quiz-teardown/frames/96303830/06s.jpg\|220]] | 「Here's the most interesting weight loss fact I learned in the last decade.」 |
| 7s | ![[ec/wiki/quiz-teardown/frames/96303830/07s.jpg\|220]] | 「Here's the most interesting weight loss fact I learned in the last decade.」 |
| 8s | ![[ec/wiki/quiz-teardown/frames/96303830/08s.jpg\|220]] | 「Here's the most interesting weight loss fact I learned in the last decade.」 |
| 9s | ![[ec/wiki/quiz-teardown/frames/96303830/09s.jpg\|220]] | 「Back in the gladiator days, I thought intense workouts, strict diet was the only way.」 |
| 10s | ![[ec/wiki/quiz-teardown/frames/96303830/10s.jpg\|220]] | 「Back in the gladiator days, I thought intense workouts, strict diet was the only way.」 |
| 11s | ![[ec/wiki/quiz-teardown/frames/96303830/11s.jpg\|220]] | 「Back in the gladiator days, I thought intense workouts, strict diet was the only way.」 |
| 12s | ![[ec/wiki/quiz-teardown/frames/96303830/12s.jpg\|220]] | 「Back in the gladiator days, I thought intense workouts, strict diet was the only way.」 |

### 全シーン × b-roll（`F`）

尺 310.5秒 ／ 114シーン ／ 平均 2.7秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）。表と絵は `ec/wiki/quiz-teardown/シーン/96303830.md` にあり、下に埋め込む（Obsidianで展開）。

![[ec/wiki/quiz-teardown/シーン/96303830]]

## 02 質問設計 — 入口と全問（`Q`）

入口: le.vshred.com/sp/survey/survey-ga（自前・curlは403でCloudflare）: 見出し「Discover Your Fat Loss Type & The Truth About Cutting Carbs & Doing Cardio」→ 1問目が最初の画面 `Q`

| # | 問い | 選択肢 | 型・次に出る幕間 |
|---|---|---|---|
| 1 | 「Select Your Gender」 | 「MALE／FEMALE」 | 画像の単一 |
| 2 | 「What's Your Age?」 | 「数字入力（years）→ Next」 | 入力 |
| 3 | 「How Tall Are You?」 | 「FT/CM切替・ft と in の入力」 | 入力 |
| 4 | 「What's Your Current Weight?」 | 「LBS/KG切替・数字入力」 | 入力 |
| 5 | 「How Often Do You Exercise?」 | 「Almost every day／Several times a week／Several times a month／Never」 | 単一 | <!-- 掘った: クイズ・LPの逐語 Q/L。`ec/wiki/quiz-teardown/lp/96303830_*` で照合 -->
| 6 | 「Which Best Describes You?」 | 「OVERWEIGHT（I have 20lbs or more of fat I really need to lose）／SOFT（I need to lose 5 to 10lbs and tone up my stomach, butt, & arms）／SLIM（I need to add some toned muscle while burning stubborn fat）」 | 単一（体型3択） |

問数: 6問（広告の「six different questions」と一致）・幕間0・メール欄なし

## 03 結果ページ（`Q`）

結果ページがそのままVSL: le.vshred.com/sp/survey/male-fl「Celebrity Trainer Vince Sant Reveals… How thousands of men with YOUR body type are dropping weight fast WHILE enjoying pizza, pasta, and beer… Click to Play」Vidalytics（尺1614秒＝26分54秒・blob配信でmp4は取れない）`Q`

## 04 オファー提示（`L`）

同じページの動画の下: 「Get Instant Access for $57」10:00タイマー／「Get Fat Loss Extreme + 7x FREE Bonuses NOW!」「YES! I Want Instant Access for Only $57」／30 Day Money-Back Guarantee／「Why Fat Loss EXtreme WORKS!」（Metabolic Confusion・Hormonal Afterburn・20分・自宅）／「THIS IS FOR YOU IF...」→ le.vshred.com/secure-checkout?funnel=vsquiz-2-2-m `L`

- 値段の段: $57 買い切り（講座＋ボーナス7）。1択
- 保証: 30日
- 作り: 自前（Cloudflare）／動画: Vidalytics／決済: 自前

## 05 売り場までの導線

広告→クイズ6問→VSLページ（$57）→自前チェックアウト。3段

## 広告 → クイズ → 売り場 のつながり

| 要素 | 広告 | クイズ／売り場 | 判定 |
|---|---|---|---|
| 約束 | six questions・20 seconds・no email | 6問・入力3問・メール欄なし | 一致 |
| 権威 | Dr. Drew／celebrity trainer（名前を言わない） | Vince Sant（Creator of V Shred） | LPで名前が出る |
| 解 | carb cycling・20分 | Fat Loss Extreme（Metabolic Confusion・Hormonal Afterburn） | 呼び名が付く |
| 値段 | 無料と言う | $57（元$790相当の記載は無し） | 結果ページで初めて出る |
| 保証 | 無し | 30日 | LPだけ |

## 補足

12本で唯一、クイズの出口が動画（VSL）。質問は体型を返すための入力3問＋選択3問で、症状を聞かない。
