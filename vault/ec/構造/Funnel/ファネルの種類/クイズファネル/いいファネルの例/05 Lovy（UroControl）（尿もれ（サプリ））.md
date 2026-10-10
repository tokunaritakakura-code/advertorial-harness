<!-- 例 -->
# 05 Lovy（UroControl）（尿もれ（サプリ））— クイズファネル example

読む人: この型（割引請求型＋レポート（Claim your $110 discount → Bladder Report））の実物を、広告→質問→結果→オファー→売り場まで通しで1本見たい人。
読む時: 自分のクイズの問い・幕間・結果の出し方・値段の出す位置を決める時。
読まなくていい条件: 12本の比較だけ要る時は [[_index]] か `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

出典: [142555234](https://app.gethookd.ai/share/ad/142555234?signature=ed76b0971cb1009aa0ee0a8f4dd863b0dc775c40411bfe9a69a239832fcab919)（GetHookd・share_url は期限なし）
LP: https://secure.trylovy.com/quiz1
形式: 動画 298s（4分58秒）・US・Facebook／Instagram・着地 quiz_page
拾った日: 2026-09-11
稼働日数 / 成績: 32日 / score 100（GetHookd の黒箱。売上ではない）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/quiz-teardown/raw/142555234.full.txt`）／`F`=ローカルmp4から切った絵／`Q`=クイズを dia で歩いた実測（`ec/wiki/quiz-teardown/lp/`）／`L`=LP・店の実測／`J`=判断

## なぜ良いのか（1行）

4分58秒の1カメ語りの後、「$110 discount を受け取るための1分クイズ」として21段を歩かせる。パッドの回答で年額が変わる1行、Bladder Vulnerability Score、3か月後の日付つきの約束で締める。 `J`

## 分解（ファネル通し・5部品）

| 位置 | 出ている物 | 何をやっているか |
|---|---|---|
| 01 入口（広告） | 動画 4分58秒・型は下の9ブロック | 0:00–0:03 `T`「Still hiding your bladder leaks with pads? Watch this.」（`F` 赤字テロップ＋カッピングマッサージの借り物クリップ→診察室の女性の1カメ。以後は2シーンしか… |
| 02 質問設計 | 13問（入力1）・幕間6（うち1枚は回答で文言が変わる）・レポート1 | secure.trylovy.com/quiz1（自前・Shopify外）: 「LABOR DAY SALE／Take This 1-Minute Quiz To Claim Your $110 Discount!」1問目が最初の画面。進捗バーは4.76%刻み（21段）`Q`… |
| 03 結果ページ | 9問目の後に「Your Personal Bladder Report／Bladder Vulnerability Score: High」（Bladder muscle integrity: Depleted／Bladder nerve signaling: Misfiring／Bladder Function: C… | 回答を「あなたの状態」に言い換えて、次の画面の値段を受け入れさせる |
| 04 オファー提示 | 定期 $40.80／買い切り $54.40（定価$79.99）。products.json では1本 $29.99（元$59.98） | 「CLAIM YOUR DISCOUNT」を押すと「100% Applying special one-time discount...」の後に「No page routing found. Please verify this button or link is set properly on an arrow.」が… | <!-- 掘った: クイズ・LPの逐語 Q/L。`ec/wiki/quiz-teardown/lp/142555234_*` で照合 -->
| 05 チェックアウト | 広告→クイズ13問＋幕間6→レポート→結果→（遷移が壊れている）→店の商品ページ→カート→チェックアウト | 保証: 90日 |

## 盗む所

- 回答で変わる1行（「save up to $329／$767／$1,205 every year on pads」）
- 結果に3か月後の日付を入れる（by 12/10/2026）
- 「Now／Your Goal」の対比表（Weakened→Restored）

## 01 入口（広告）— 9ブロック分解

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:03 `T`「Still hiding your bladder leaks with pads? Watch this.」（`F` 赤字テロップ＋カッピングマッサージの借り物クリップ→診察室の女性の1カメ。以後は2シーンしか無い） |
| lead | 0:03–0:27 `T`「Most women think bladder leaks are just part of aging. They're not.」「one overlooked marker」「Your doctor has probably never checked it」 |
| discovery story | 0:41–2:30 `T` Linda 71歳「She had done all the tests. Everything looked normal」「Week six, she called me crying」 |
| UMP | 1:09–1:36／2:32–3:13 `T`「a specific mineral deficiency that slowly shuts the bladder down」→「Magnesium」→「Most magnesium supplements don't actually reach your bladder」「the starved bladder effect」 |
| UMS | 3:24–3:43 `T`「That's when I found Eurocontrol」「the right form of magnesium your body can actually absorb」 |
| product reveal | 3:24（69%地点） |
| price drop | 4:20 `T`「available with up to 60% off」（金額なし） |
| risk reversal | 4:20 `T`「a full 90-day money-back guarantee」 |
| testimonials | Linda の物語＋`T`「nearly nine out of ten women showed the same deficiency」 |

無かったブロックは「無し」。欠落そのものが発見。

### フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

| 秒 | 絵 | 喋っている言葉 `T` |
|---|---|---|
| 0s | ![[ec/wiki/quiz-teardown/frames/142555234/00s.jpg\|220]] | 「Still hiding your bladder leaks with pads?」 |
| 1s | ![[ec/wiki/quiz-teardown/frames/142555234/01s.jpg\|220]] | 「Still hiding your bladder leaks with pads?」 |
| 2s | ![[ec/wiki/quiz-teardown/frames/142555234/02s.jpg\|220]] | 「Watch this.」 |
| 3s | ![[ec/wiki/quiz-teardown/frames/142555234/03s.jpg\|220]] | 「Most women think bladder leaks are just part of aging.」 |
| 4s | ![[ec/wiki/quiz-teardown/frames/142555234/04s.jpg\|220]] | 「Most women think bladder leaks are just part of aging.」 |
| 5s | ![[ec/wiki/quiz-teardown/frames/142555234/05s.jpg\|220]] | 「Most women think bladder leaks are just part of aging.」 |
| 6s | ![[ec/wiki/quiz-teardown/frames/142555234/06s.jpg\|220]] | 「They're not.」 |
| 7s | ![[ec/wiki/quiz-teardown/frames/142555234/07s.jpg\|220]] | 「They're a sign your bladder is being starved of something it desperately needs.」 |
| 8s | ![[ec/wiki/quiz-teardown/frames/142555234/08s.jpg\|220]] | 「They're a sign your bladder is being starved of something it desperately needs.」 |
| 9s | ![[ec/wiki/quiz-teardown/frames/142555234/09s.jpg\|220]] | 「They're a sign your bladder is being starved of something it desperately needs.」 |
| 10s | ![[ec/wiki/quiz-teardown/frames/142555234/10s.jpg\|220]] | 「They're a sign your bladder is being starved of something it desperately needs.」 |
| 11s | ![[ec/wiki/quiz-teardown/frames/142555234/11s.jpg\|220]] | 「They're a sign your bladder is being starved of something it desperately needs.」 |
| 12s | ![[ec/wiki/quiz-teardown/frames/142555234/12s.jpg\|220]] | 「As a bladder health specialist, I see this pattern every single day.」 |

### 全シーン × b-roll（`F`）

尺 298.4秒 ／ 2シーン ／ 平均 149.2秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）。表と絵は `ec/wiki/quiz-teardown/シーン/142555234.md` にあり、下に埋め込む（Obsidianで展開）。

![[ec/wiki/quiz-teardown/シーン/142555234]]

## 02 質問設計 — 入口と全問（`Q`）

入口: secure.trylovy.com/quiz1（自前・Shopify外）: 「LABOR DAY SALE／Take This 1-Minute Quiz To Claim Your $110 Discount!」1問目が最初の画面。進捗バーは4.76%刻み（21段）`Q`

| # | 問い | 選択肢 | 型・次に出る幕間 |
|---|---|---|---|
| 1 | 「How old are you?」 | 「Under 50／50-59／60-69／70-79／Over 80」 | 単一 |
| 2 | 「Which of these are you dealing with? Choose all that apply」 | 「Sudden urges to go／Leaks when you laugh, cough, or sneeze／Going to the bathroom more than 8 times a day／Waking up 2 or more times a night／Never feeling like your bladder is fully empty／Worrying about accidents in public」 | 複数 |
| 3 | 「How often do you experience leaks or urgency in a typical day?」 | 「Rarely — 1 to 2 times／Sometimes — 3 to 5 times／Often — 6 to 8 times／Constantly — more than 8 times」 | 単一 |
| 4 | 「How many pads do you usually go through in a day?」 | 「I don't use pads／1–2 per day／3–4 per day／5–6 per day／7+ per day」 | 単一 → 幕間の文言が回答で変わる（3–4→「save up to $767 every year on pads」） |
| 5 | 「Which of these have you done because of your bladder? Choose all that apply」 | 「I plan every outing around bathroom locations／I avoid long car trips or flights／I've pulled back from exercise／I wear dark clothing or extra layers／…」 | 複数 → 幕間「You are not alone. More than half of women over 65…」 |
| 6 | 「What have you already tried?」 | 「Pads or protective underwear／Kegel exercises／Cutting back on fluids／Prescription medication／Doctor visits — and been told to "just live with it"／Nothing yet」 | 複数 → 幕間「Here's why nothing has worked.」（Pads catch the evidence／Kegels only work the muscle／Medications mute the signal） |
| 7 | 「How many times do you wake up at night to use the bathroom?」 | 「0 to 1 times／2 to 3 times／4 or more times／It varies」 | 単一 |
| 8 | 「How long have you been dealing with bladder control issues?」 | 「Less than a year／1 to 3 years／3 to 5 years／More than 5 years」 | 単一 |
| 9 | 「When did you go through menopause?」 | 「More than 10 years ago／5 to 10 years ago／Within the last 5 years／I'm not sure」 | 単一 → 幕間「Congratulations — you may be a great fit.」→「Generating your Bladder Profile」→ レポート |
| 10 | 「Have you ever avoided something you love because of your bladder?」 | 「Yes — more than I like to admit／Sometimes／Rarely／Not yet」 | 単一 → 幕間「A leaky bladder doesn't have to run your life.」 |
| 11 | 「What would you do first, if your bladder stopped holding you back?」 | 「Take a long trip without planning around bathrooms／Go back to church, events, and gatherings freely／Exercise again without fear／Sleep through the whole night／All」 | 単一 |
| 12 | 「Is there something coming up you want to feel confident for?」 | 「A family gathering or reunion／A trip or vacation／A wedding／Nothing specific／I'd simply love to feel like myself again」 | 単一 |
| 13 | 「When is your event?（We'll keep this in mind when building your plan.）」 | 「日付入力／Skip this step」 | 入力 |

問数: 13問（入力1）・幕間6（うち1枚は回答で文言が変わる）・レポート1

## 03 結果ページ（`Q`）

9問目の後に「Your Personal Bladder Report／Bladder Vulnerability Score: High」（Bladder muscle integrity: Depleted／Bladder nerve signaling: Misfiring／Bladder Function: Compromised／Symptom Progression Risk: High）。最後に「BASED ON YOUR ANSWERS／You Are 90 Days Away From Reclaiming Bladder Confidence」「First noticeable improvement within 2 to 3 weeks／Significant reduction… by 12/10/2026」「NOW: Weakened・Poor・Frequent」→「YOUR GOAL: Restored・Improved・Reduced」→「CLAIM YOUR DISCOUNT」`Q`

## 04 オファー提示（`L`）

「CLAIM YOUR DISCOUNT」を押すと「100% Applying special one-time discount...」の後に「No page routing found. Please verify this button or link is set properly on an arrow.」が出て遷移しない（このA/B版の設定漏れ・2026-09-11実測）。店の商品ページ trylovy.com/products/urocontrol-s: 「LABOR DAY SALE Shop Now and Get Up To 62% Off」／Subscribe & Save $79.99→$40.80（Save $29.99・Refill Every 30 Days）／One Time $54.40（Save $19.99・No Free Shipping）／90-Day Money-Back／HSA/FSA／6成分（Red Clover・Pumpkin Seed・Hyaluronic Acid・Cranberry・Magnesium Citrate・Sea Buckthorn）／vturb動画 `L` <!-- 掘った: クイズ・LPの逐語 Q/L。`ec/wiki/quiz-teardown/lp/142555234_*` で照合 -->

- 値段の段: 定期 $40.80／買い切り $54.40（定価$79.99）。products.json では1本 $29.99（元$59.98）
- 保証: 90日
- 作り: 自前（heyflow風の静的HTML）／店: Shopify＋vturb

## 05 売り場までの導線

広告→クイズ13問＋幕間6→レポート→結果→（遷移が壊れている）→店の商品ページ→カート→チェックアウト

## 広告 → クイズ → 売り場 のつながり

| 要素 | 広告 | クイズ／売り場 | 判定 |
|---|---|---|---|
| 原因 | magnesium・starved bladder | Magnesium Citrate（6成分の1つ） | 主役から6分の1に薄まる |
| 値段 | up to 60% off | Up To 62% Off・$110 discount | ほぼ一致 |
| 保証 | 90日 | 90日 | 一致 |
| 症状語 | pads | 4問目・幕間（年額） | 一致 |
| 権威 | Lauren（urodynamic specialist） | 無し | 店に人は出ない |

## 補足

Seranova・Sculpiflex・Aurora と同じ文言のテンプレ（「Take This 1-Minute Quiz To Claim Your $X Discount!」「Do you have an important event」「When is your event?」「Now／Your Goal」「by 日付」）。
