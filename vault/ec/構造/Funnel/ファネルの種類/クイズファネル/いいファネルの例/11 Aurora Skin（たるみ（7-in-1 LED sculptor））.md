<!-- 例 -->
# 11 Aurora Skin（たるみ（7-in-1 LED sculptor））— クイズファネル example

読む人: この型（Seranovaと同一台本＋RevenueHunt（Shopifyアプリ）の12画面）の実物を、広告→質問→結果→オファー→売り場まで通しで1本見たい人。
読む時: 自分のクイズの問い・幕間・結果の出し方・値段の出す位置を決める時。
読まなくていい条件: 12本の比較だけ要る時は [[_index]] か `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

出典: [150401876](https://app.gethookd.ai/share/ad/150401876?signature=fb893752c5e58ff231ffefc5a220b2c28d6dd67a517bff50b3cd3a24540d8647)（GetHookd・share_url は期限なし）
LP: https://auroraskin.us/pages/quiz
形式: 動画 246s（4分06秒）・US・Facebook／Instagram・着地 quiz_page
拾った日: 2026-09-11
稼働日数 / 成績: 22日 / score 100（GetHookd の黒箱。売上ではない）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/quiz-teardown/raw/150401876.full.txt`）／`F`=ローカルmp4から切った絵／`Q`=クイズを dia で歩いた実測（`ec/wiki/quiz-teardown/lp/`）／`L`=LP・店の実測／`J`=判断

## なぜ良いのか（1行）

広告はSeranova（10）と逐語で同じ物語で、原因の一文だけ「43の表情筋が弱る」に差し替えている。クイズはShopifyアプリ（RevenueHunt v2）の12画面で、結果で「60% OFF + FREE LIFTING SERUM」を出す。 `J`

## 分解（ファネル通し・5部品）

| 位置 | 出ている物 | 何をやっているか |
|---|---|---|
| 01 入口（広告） | 動画 4分06秒・型は下の9ブロック | 0:00–0:16 `T`「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer game, here… |
| 02 質問設計 | 7問・幕間5（12画面） | auroraskin.us/pages/quiz（Shopify・PageFly＋RevenueHunt v2 の inline quiz `quiz_7BaARl`・内部名「Lesgo」・shadow DOMで描画。定義は cdn.shopify.com の quiz-7BaARl.json）: 「Take This… |
| 03 結果ページ | 「Based on your answers, we know...／You'll see real, visible changes in: Sagging around jawline／Wrinkles／Skin texture & glow／Puffiness and facial definition」「✨ A… | 回答を「あなたの状態」に言い換えて、次の画面の値段を受け入れさせる |
| 04 オファー提示 | 1台 $149.99（元$374.99）＋美容液を無料で付ける。1択 | 店の商品（products.json）: AURORA 7-in-1 LED Facial Sculptor $149.99（元$374.99＝60%OFF・差額$225が見出しの「$225 Discount」）／Rewind-Age Peptide Serum $43（無料で付ける「LIFTING SERUM」に当た… |
| 05 チェックアウト | 広告→クイズ7問＋幕間5→結果（60%OFF）→Claim→Shopify商品→カート→チェックアウト | 保証: 判定不能（広告の文字起こしが崩れ、店の表記を取れていない） |

## 盗む所

- 同じ物語で機序の一文だけ差し替えて別商品を売る（Seranova→Aurora）
- クイズを自前で作らずShopifyアプリ（RevenueHunt）で12画面を組む
- 幕間4枚で反論を先に潰す（99% don't penetrate／too expensive／busy schedule／you qualify）

## 01 入口（広告）— 9ブロック分解

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:16 `T`「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer game, here's what happened」（`F` Pixar風3D。3人が並ぶ→主人公のクローズアップ→元夫と歩く） |
| lead | 0:16–1:15 `T`「I'm 53 six years divorced. He didn't just leave he cheated for two years」（Seranovaと同文） |
| discovery story | 1:15–1:35 `T`「my co-worker Nina caught me crying in the office bathroom. She's a nurse」 |
| UMP | 1:35–1:51 `T`「those creams just sit on top of your skin. But sagging was never your skin's fault after 40 the 43 muscles underneath your face slowly weaken… no cream on earth can reach a muscle」 |
| UMS | 1:55–2:15 `T`「The Aurora seven in one facial sculptor uses red light therapy and EMS micro current to gently train those 43 muscles from underneath」「Over 70,000 women use it just a few minutes a day」 | <!-- 掘った: 広告の逐語 T。`raw/150401876.segments.json` の秒で照合 -->
| product reveal | 1:55（47%地点） |
| price drop | 3:32 `T`「Aurora's running your live discount」（金額なし） |
| risk reversal | 3:38 `T`「your life guaranteed」（文字起こしが崩れている。店の表記は products.json に無し） |
| testimonials | 自分の6週／12週＋`T`「Over 70,000 women」 |

無かったブロックは「無し」。欠落そのものが発見。

### フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

| 秒 | 絵 | 喋っている言葉 `T` |
|---|---|---|
| 0s | ![[ec/wiki/quiz-teardown/frames/150401876/00s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer」 |
| 1s | ![[ec/wiki/quiz-teardown/frames/150401876/01s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer」 |
| 2s | ![[ec/wiki/quiz-teardown/frames/150401876/02s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer」 |
| 3s | ![[ec/wiki/quiz-teardown/frames/150401876/03s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer」 |
| 4s | ![[ec/wiki/quiz-teardown/frames/150401876/04s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer」 |
| 5s | ![[ec/wiki/quiz-teardown/frames/150401876/05s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer」 |
| 6s | ![[ec/wiki/quiz-teardown/frames/150401876/06s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer」 |
| 7s | ![[ec/wiki/quiz-teardown/frames/150401876/07s.jpg\|220]] | 「Had to stand next to my ex-husband and the woman he left me for through our son's entire soccer …(続き)」 |
| 8s | ![[ec/wiki/quiz-teardown/frames/150401876/08s.jpg\|220]] | 「Game, here's what happened」 |
| 9s | ![[ec/wiki/quiz-teardown/frames/150401876/09s.jpg\|220]] | 「Game, here's what happened」 |
| 10s | ![[ec/wiki/quiz-teardown/frames/150401876/10s.jpg\|220]] | 「Last Saturday at our son's soccer game. He walked up and said what happened to you?」 |
| 11s | ![[ec/wiki/quiz-teardown/frames/150401876/11s.jpg\|220]] | 「Last Saturday at our son's soccer game. He walked up and said what happened to you?」 |
| 12s | ![[ec/wiki/quiz-teardown/frames/150401876/12s.jpg\|220]] | 「Last Saturday at our son's soccer game. He walked up and said what happened to you?」 |

### 全シーン × b-roll（`F`）

尺 245.9秒 ／ 58シーン ／ 平均 4.2秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）。表と絵は `ec/wiki/quiz-teardown/シーン/150401876.md` にあり、下に埋め込む（Obsidianで展開）。

![[ec/wiki/quiz-teardown/シーン/150401876]]

## 02 質問設計 — 入口と全問（`Q`）

入口: auroraskin.us/pages/quiz（Shopify・PageFly＋RevenueHunt v2 の inline quiz `quiz_7BaARl`・内部名「Lesgo」・shadow DOMで描画。定義は cdn.shopify.com の quiz-7BaARl.json）: 「Take This 1-Minute Quiz To Claim Your $225 Discount!」1問目が最初の画面 `Q`

| # | 問い | 選択肢 | 型・次に出る幕間 |
|---|---|---|---|
| 1 | 「How old are you? 🤔」 | 「Over 85／75-84／65-74／55-64／45-54／35-44／Under 35」 | 単一 |
| 2 | 「What is your biggest skin-related concern?🤷 (Choose as many as you like)」 | 「Wrinkles／Fine Lines／Saggy Skin／Crepe Skin／Dark Spots／Patchy Skin」 | 複数 |
| 3 | 「Which of the following do you want to visibly erase?🤷」 | 「Sagging Jowl's／Forehead Lines／Turkey Neck／Crow's Feet／Hollow Cheeks／Dark Spots／Double Chin」 | 複数 → 幕間「You're in the right spot 💪 Thousands are already using the Aurora 7-in-1 Sculptor to lift their jawline…」 |
| 4 | 「Which skincare products have you tried before? (Select all that apply)」 | 「Anti-aging creams／Retinol／Hyaluronic acid／Collagen boosters／Vitamin C serums／Face oils／Daily moisturizer／Other」 | 複数 → 幕間「Don't worry if other solutions haven't worked for you... 99% of topical anti-aging Solutions don't penetrate the skin deeply enough」 |
| 5 | 「Have you ever done any of these treatments? 💉」 | 「Botox／Fillers／Hydrafacials／Chemical peels／Microneedling／Laser resurfacing／Other」 | 複数 → 幕間「These treatments are just way too expensive right? Yes, they deliver results, but the results only last a few months」 | <!-- 掘った: クイズ・LPの逐語 Q/L。`ec/wiki/quiz-teardown/lp/150401876_*` で照合 -->
| 6 | 「What results are you most excited about?」 | 「Look more youthful／Smooth fine lines／Lift & firm skin／Brighten/even skin tone／Reduce puffiness／Define jawline／Boost skincare absorption／All of the above」 | 複数 → 幕間「A busy schedule doesn't have to stop you from looking years younger... even while watching TV」 |
| 7 | 「Do you have sensitive skin? 🤔」 | 「Yes／No／I am not sure」 | 単一 → 幕間「Congratulations, you qualify! The Aurora LED Facial Sculptor is 100% safe, gentle, and effective for your skin type.」 |

問数: 7問・幕間5（12画面）

## 03 結果ページ（`Q`）

「Based on your answers, we know...／You'll see real, visible changes in: Sagging around jawline／Wrinkles／Skin texture & glow／Puffiness and facial definition」「✨ And because you're part of today's LABOR DAY SALE 🇺🇸… You just unlocked our Best Deal of 2026: 🔥 60% OFF + FREE LIFTING SERUM」→「Claim My One Time Offer」（定義JSONから `Q`。クリックは shadow DOM で dia が効かず結果画面は目視していない）

## 04 オファー提示（`L`）

店の商品（products.json）: AURORA 7-in-1 LED Facial Sculptor $149.99（元$374.99＝60%OFF・差額$225が見出しの「$225 Discount」）／Rewind-Age Peptide Serum $43（無料で付ける「LIFTING SERUM」に当たる）`L`

- 値段の段: 1台 $149.99（元$374.99）＋美容液を無料で付ける。1択
- 保証: 判定不能（広告の文字起こしが崩れ、店の表記を取れていない）
- 作り: Shopify＋PageFly＋RevenueHunt v2（Shopifyアプリ）

## 05 売り場までの導線

広告→クイズ7問＋幕間5→結果（60%OFF）→Claim→Shopify商品→カート→チェックアウト

## 広告 → クイズ → 売り場 のつながり

| 要素 | 広告 | クイズ／売り場 | 判定 |
|---|---|---|---|
| 物語 | Seranovaと同文 | 無し | PDPに物語は無い |
| 原因 | 43 muscles underneath your face | 無し（結果は効果の列挙） | クイズ側に原因は出ない |
| 値段 | live discount | $225 Discount・60% OFF・$149.99 | クイズの見出しで金額が出る |
| 数 | Over 70,000 women | Thousands are already using | 一致（桁は下がる） |
| 保証 | 不明 | 不明 | 判定不能 |

## 補足

クイズの中身がCDNのJSON（quiz-7BaARl.json）で丸ごと取れる。NeuroMD（RevenueHunt v1）も同じで、公開URLかJSONで全問が読める。
