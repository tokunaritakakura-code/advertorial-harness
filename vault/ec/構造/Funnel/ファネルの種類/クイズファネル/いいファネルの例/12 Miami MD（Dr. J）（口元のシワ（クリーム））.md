<!-- 例 -->
# 12 Miami MD（Dr. J）（口元のシワ（クリーム））— クイズファネル example

読む人: この型（医師VSL→スキップ可のクイズ（SKIP THIS QUIZ））の実物を、広告→質問→結果→オファー→売り場まで通しで1本見たい人。
読む時: 自分のクイズの問い・幕間・結果の出し方・値段の出す位置を決める時。
読まなくていい条件: 12本の比較だけ要る時は [[_index]] か `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

出典: [106140560](https://app.gethookd.ai/share/ad/106140560?signature=6af9dfe4bff16e2388579459e01007e3ca43cdc7a5119999b0119d06a66132a7)（GetHookd・share_url は期限なし）
LP: https://offer.trymiamimd.com/quiz/v88/?affId=9977965F&c1=FB014&c2=%7B%7Bcampaign.name%7D%7D&c3=%7B%7Bad.name%7D%7D&c4=%7B%7Badset.name%7D%7D&c5=%7B%7Bcampaign.id%7D%7D&c6=%7B%7Bad.id%7D%7D&c7=%7B%7Bplacement%7D%7D
形式: 動画 593s（9分53秒）・US・Facebook／Instagram・着地 quiz_page
拾った日: 2026-09-11
稼働日数 / 成績: 95日 / score 86（GetHookd の黒箱。売上ではない）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/quiz-teardown/raw/106140560.full.txt`）／`F`=ローカルmp4から切った絵／`Q`=クイズを dia で歩いた実測（`ec/wiki/quiz-teardown/lp/`）／`L`=LP・店の実測／`J`=判断

## なぜ良いのか（1行）

9分53秒の医師VSLで「Progerin」を教え、クイズには「SKIP THIS QUIZ」を置いて温まった客を止めない。幕間で「Dr. J believes」と医師の意見を挟み、月名（September→December）で3か月を絵にしてから$40/瓶×3の段を出す。 `J`

## 分解（ファネル通し・5部品）

| 位置 | 出ている物 | 何をやっているか |
|---|---|---|
| 01 入口（広告） | 動画 9分53秒・型は下の9ブロック | 0:00–0:08 `T`「No way, the lines around the mouth are actually fading. Here's how to make the skin around your mouth look… |
| 02 質問設計 | 10問・幕間4 | offer.trymiamimd.com/quiz/v88/（自前・全画面が1ページのDOMに同居）: 「Start 1-Minute Quiz To Claim Your 41% Discount」＋「SKIP THIS QUIZ」（押すと /v29/ の商品ページへ）`Q`… |
| 03 結果ページ | 「Congratulations, you qualify for our biggest discount. ✅ Our Lift & Firm Cream Is A Match Made In Heaven For Your Particular Skin Type.」「You'll Erase All Your … | 回答を「あなたの状態」に言い換えて、次の画面の値段を受け入れさせる |
| 04 オファー提示 | 3瓶 $40/瓶／2瓶 $43／1瓶 $49（定期は$36/$39/$44）。段は瓶数 | offer.trymiamimd.com/v29/（自前・checkout）: 「Hurry! 53,084 Jars Sold Since Restock」／Single Purchase: 3 Jars $40/ea（You Save $120）／2 Jars $43/ea（Save $60）／1 Jar $49（… |
| 05 チェックアウト | 広告→クイズ10問＋幕間4→結果→CLAIM→オファーページ（3段）→自前チェックアウト。約17画面 | 保証: 60日 |

## 盗む所

- クイズの1画面目に「SKIP THIS QUIZ」を置く（VSLで温まった客を止めない）
- 「September → December」の月名で3か月の期限を絵にする
- 幕間で医師の意見を入れる（「Dr. J Believes These Treatments Aren't Necessary」）

## 01 入口（広告）— 9ブロック分解

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:08 `T`「No way, the lines around the mouth are actually fading. Here's how to make the skin around your mouth look up to 10 years younger. Just do this before bed every night.」（`F` 白髪女性の顔にスクラブのUGC＋青いスクラブ服の医師のワイプ＋テロップ「Here's how to make the skin around your mouth… look up to TEN YEARS YOUNGER!」） |
| lead | 0:10–0:36 `T`「Most women may waste hundreds of dollars buying collagen, then buying retinol, then buying the latest wrinkle creams」「Less is more」 |
| discovery story | 3:04–3:17 `T`「I partnered with the incredible team of chemists and formulators at MiamiMD」 |
| UMP | 0:38–1:41 `T`「a toxic protein called produrin」（LPの綴りは Progerin）「increasing about 3% a year」ボウルの比喩 |
| UMS | 1:46–3:04 `T`「a powerful anti-aging peptide that immediately reduces… by an astonishing 22%」「rolling back the biological clock… 7 or 8 years」「23 women aged 34 to 78 used produrin for 30 days」＋5:10–5:59 Matrixyl 3000／Argireline／Ceramide |
| product reveal | 3:32（36%地点）`T`「MiamiMD's Age Defying Lift and Firm Cream」 |
| price drop | 8:02–8:20 `T`「when you order a 6 month supply through this video right now, you'll save $29 per bottle and pay just $40 each」 |
| risk reversal | 6:30 `T`「if you try Lift and Firm and you're not thoroughly impressed after the first 60 days, we will issue a full prompt refund」 |
| testimonials | 3:46–4:29 `T` 3人「My friend asked me if I had Botox」 |

無かったブロックは「無し」。欠落そのものが発見。

### フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

| 秒 | 絵 | 喋っている言葉 `T` |
|---|---|---|
| 0s | ![[ec/wiki/quiz-teardown/frames/106140560/00s.jpg\|220]] | 「No way, the lines around the mouth are actually fading.」 |
| 1s | ![[ec/wiki/quiz-teardown/frames/106140560/01s.jpg\|220]] | 「No way, the lines around the mouth are actually fading.」 |
| 2s | ![[ec/wiki/quiz-teardown/frames/106140560/02s.jpg\|220]] | 「No way, the lines around the mouth are actually fading.」 |
| 3s | ![[ec/wiki/quiz-teardown/frames/106140560/03s.jpg\|220]] | 「No way, the lines around the mouth are actually fading.」 |
| 4s | ![[ec/wiki/quiz-teardown/frames/106140560/04s.jpg\|220]] | 「Here's how to make the skin around your mouth look up to 10 years younger.」 |
| 5s | ![[ec/wiki/quiz-teardown/frames/106140560/05s.jpg\|220]] | 「Here's how to make the skin around your mouth look up to 10 years younger.」 |
| 6s | ![[ec/wiki/quiz-teardown/frames/106140560/06s.jpg\|220]] | 「Here's how to make the skin around your mouth look up to 10 years younger.」 |
| 7s | ![[ec/wiki/quiz-teardown/frames/106140560/07s.jpg\|220]] | 「Here's how to make the skin around your mouth look up to 10 years younger.」 |
| 8s | ![[ec/wiki/quiz-teardown/frames/106140560/08s.jpg\|220]] | 「Just do this before bed every night.」 |
| 9s | ![[ec/wiki/quiz-teardown/frames/106140560/09s.jpg\|220]] | 「Just do this before bed every night.」 |
| 10s | ![[ec/wiki/quiz-teardown/frames/106140560/10s.jpg\|220]] | 「This is my best secret for mouth wrinkles, neck wrinkles or loose sagging skin around」 |
| 11s | ![[ec/wiki/quiz-teardown/frames/106140560/11s.jpg\|220]] | 「This is my best secret for mouth wrinkles, neck wrinkles or loose sagging skin around」 |
| 12s | ![[ec/wiki/quiz-teardown/frames/106140560/12s.jpg\|220]] | 「This is my best secret for mouth wrinkles, neck wrinkles or loose sagging skin around」 |

### 全シーン × b-roll（`F`）

尺 592.9秒 ／ 204シーン ／ 平均 2.9秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）。表と絵は `ec/wiki/quiz-teardown/シーン/106140560.md` にあり、下に埋め込む（Obsidianで展開）。

![[ec/wiki/quiz-teardown/シーン/106140560]]

## 02 質問設計 — 入口と全問（`Q`）

入口: offer.trymiamimd.com/quiz/v88/（自前・全画面が1ページのDOMに同居）: 「Start 1-Minute Quiz To Claim Your 41% Discount」＋「SKIP THIS QUIZ」（押すと /v29/ の商品ページへ）`Q`

| # | 問い | 選択肢 | 型・次に出る幕間 |
|---|---|---|---|
| 1 | 「What Age Are You & Your Skin? 🤔」 | 「Under 30／30-40／41-50／51-60／Over 60」 | 単一 |
| 2 | 「What's Bothering You Today? 🤷‍♀️ (Choose whatever skin issues you have)」 | 「Mouth wrinkles／Forehead lines／Crows feet／Saggy jowls／Necklace lines／Turkey neck」 | 複数 |
| 3 | 「How Noticeable Are Your Wrinkles?」 | 「Almost invisible／Clearly visible／Deeply visible」 | 単一 |
| 4 | 「What Do You Wish Would Go Away? (Choose all that apply)」 | 「Mouth wrinkles／Fine lines／Saggy jowls／Turkey neck」 | 複数 → 幕間「You Are Exactly Where You Need To Be! 🥰 Over 100,000 women have seen their mouth wrinkles… disappear with the help of MiamiMD's Lift & Firm Cream」 |
| 5 | 「Which Skincare Products Have You Tried?」 | 「Wrinkle Creams／Collagen／Retinol／Hyaluronic Acid／LED Masks／Beauty Supplements」 | 複数 → 幕間「Don't Worry If Nothing Has Worked For You Yet… 99% of skincare products… don't do anything to block the wrinkle-accelerating effects of Progerin.」 |
| 6 | 「Have You Ever Gone For A Pricey Treatment?」 | 「Botox／Fillers／Lasers／Microneedling／Hydrafacial／Other」 | 複数 → 幕間「Dr. J Believes These Treatments Aren't Necessary… $1,000+ a time is far too expensive in the long run.」 |
| 7 | 「What Does Dreamy Skin Mean For You? 🎯」 | 「Looking years younger／Being wrinkle-free／Tight neck and jawline／Look great without makeup／Never feeling self-conscious／All of the above」 | 複数 |
| 8 | 「How Much Time Do You Have For Skincare Each Day? ⏰」 | 「I'm not sure／5 Minutes／10 Minutes／20 Minutes／30+ Minutes／I don't have time every day」 | 単一 → 幕間「Being Busy Shouldn't Affect Your Results. With our famous Lift & Firm Cream, just 2 minutes a day」 |
| 9 | 「What Skin Tone Do You Have?」 | 「Fair／Light／Medium／Dark／Very Dark／I'm Not Sure」 | 単一 |
| 10 | 「Do You Have Sensitive Skin? 🤔」 | 「Yes／No／Sometimes」 | 単一 |

問数: 10問・幕間4

## 03 結果ページ（`Q`）

「Congratulations, you qualify for our biggest discount. ✅ Our Lift & Firm Cream Is A Match Made In Heaven For Your Particular Skin Type.」「You'll Erase All Your Wrinkles & Notice How Much Tighter Your Skin Is In Just 3 Months」「we guarantee you'll achieve remarkable results with a 3-month supply… If not, you'll receive all your money back」September（Goal）→December →「CLAIM YOUR DISCOUNT」`Q`

## 04 オファー提示（`L`）

offer.trymiamimd.com/v29/（自前・checkout）: 「Hurry! 53,084 Jars Sold Since Restock」／Single Purchase: 3 Jars $40/ea（You Save $120）／2 Jars $43/ea（Save $60）／1 Jar $49（Save $20・+Shipping $4.95）／Subscribe & Save 10%: $36／$39／$44 Monthly／The MiamiMD Promise（Paraben・Fragrance・Cruelty・BHA free）／Dr. Jegasothy（Univ. of Miami）／Progeline・Matrixyl 3000・Argireline／60-day `L`

- 値段の段: 3瓶 $40/瓶／2瓶 $43／1瓶 $49（定期は$36/$39/$44）。段は瓶数
- 保証: 60日
- 作り: 自前（offer.trymiamimd.com）／決済: 自前（affId付きのアフィリエイト計測）

## 05 売り場までの導線

広告→クイズ10問＋幕間4→結果→CLAIM→オファーページ（3段）→自前チェックアウト。約17画面

## 広告 → クイズ → 売り場 のつながり

| 要素 | 広告 | クイズ／売り場 | 判定 |
|---|---|---|---|
| 原因 | produrin（音） | Progerin（幕間）→ Progeline（成分） | 綴りが3つ |
| 値段 | $40 each（6か月） | 3 Jars $40/ea・41% Discount | $40は一致。41%の分母は判定不能 |
| 保証 | 60日 | 60日・3か月分で結果保証 | 一致 |
| 権威 | Dr. J（一人称） | Dr. Jegasothy, Associated Professor of Dermatology, University of Miami | 一致（実名がLPで出る） |
| 入口 | 無し | SKIP THIS QUIZ | VSL客を通す穴 |

## 補足

12本で唯一クイズを飛ばせる。幕間の文言（「Don't worry…」「Being busy shouldn't…」「Congratulations, you qualify」）は Aurora（RevenueHunt）とほぼ同じで、テンプレの出どころが同じと見える。
