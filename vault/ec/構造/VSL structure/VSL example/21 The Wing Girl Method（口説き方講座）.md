<!-- 例 -->
# The Wing Girl Method（口説き方講座）— VSL example

読む人: この型（秘密暴露型（here's the big secret about women）＋借り物の街頭映像）の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

引き方: GetHookd で広告1本を引く（Dia のログイン済みタブから内部API `GET /api/get-ad/118025645`）。LP動画の設定は `curl -s "https://fast.vidalytics.com/embeds/kMrukacT/YDsUshTG6sj5B8J7/player.settings.json"`
出典: [118025645](https://app.gethookd.ai/share/ad/118025645?signature=410ec9d4315a3107d78e0b5ebf89dbe0a30263eba35cf01cfbb07bd955d124a1)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/118025645`）
LP: https://yourflirtmethod.com/order-form1766147252381#close-popup
形式: VSL・動画 212s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 ClickFunnels のセールスレター（動画＋長文＋ADD TO CART×7。URL名は order-form だがフォームは別ページ）
拾った日: 2026-09-12
稼働日数 / 成績: 68日 / score 86（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 597本（2026-09-12）
選定: GetHookd で「勝ち（score 81〜100）・稼働中・動画」かつブランドの稼働広告数500以上。着地が実測でVSL（長尺の売り動画が主役のページ）（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし／`W`=ローカルwhisper large-v3-turbo（この本は GetHookd の文字起こしが空なので広告も `W`）／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ）／`J`=判断

## なぜ良いのか（1行）

0〜4秒は借り物の街頭映像（男が女に声を掛ける）、5秒で女性本人が「we want you to flirt with us」と男の思い込みを裏返し、2:31で「the f formula」の名前を出して「free video」へ送る。値段・保証は広告で一度も言わない。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:13 `W`（`F` 0〜4秒は街頭の借り物映像、字幕「BIT CHEEKY.」「I'M JUST ON MY WAY TO THE PARK, I THINK.」→4秒に赤い STOP の手の標識→5秒からソファの女性本人）「here's the big secret about women we want you to flirt with us we even want you to get sexual with us desire us」 |
| lead | 0:13–0:38 `W`「the way women flirt is totally different from the way that men flirt」「will fail 99.9 of the time」「flirt the right way that makes sense to her」 |
| discovery story | 無し |
| UMP | 0:38–1:14 `W`「when she feels something about you not thinks something about you」「they logically try to trigger a woman's attraction buttons」→「logic goes totally out the window」。失敗の名指し 1:34–1:51「coming off like a sleaze or a creep」「they over sexualize things」 |
| UMS | 1:21–2:37 `W`「a simple formula that gives you the ability to flirt with any woman any time any place」→ 呼び名 2:31「the f formula that's what it's called」 |
| product reveal | 無し（名前だけ。売り物とは言わず 3:14「you're gonna watch a free video that i made for you」） |
| price drop | 無し |
| risk reversal | 無し |
| testimonials | 数だけ `W` 2:20「tested on thousands of women to make sure that it's 100 effective」 |

締め 3:08–3:32 `W`「click the button on your screen i feel like i'm pointing at it」「this video will not be available forever because if every guy on the street got this formula it would lose its value」。無かったブロックは「無し」。

## 盗む所

- 0〜4秒は商品と無関係の街頭映像＋4秒のSTOP標識、5秒から語り手1人。残り207秒はソファの1カット（16シーン中15がソファ・しきい値0.25） `F`
- 売る側の性別を武器にする。女性本人が「here's the big secret about women」と言い、LP動画でも「as a woman myself」（2:14）と繰り返す `W`
- 値段を言う前に出費の比較を置く。LP動画19:19「dinner can cost you like $50, $70, even $100」→「$150 or $200」→ 24:01「a thousand dollars」「two thousand or five thousand dollars」→ 24:25「all for only $47」 `W`

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

![[ec/wiki/vsl-teardown/絵/118025645-hook]]

## 全シーン × b-roll（`F`）

尺 212.5秒 ／ 16シーン ／ 平均 13.3秒 ／ しきい値 0.25（シーン数はしきい値に依存）。外の映像は s000（0.0–4.3秒）の1本だけで、s001〜s015 は同じソファの本人＋字幕。

![[ec/wiki/vsl-teardown/シーン/118025645]]

## LP（着地ページ）— yourflirtmethod.com/order-form1766147252381

**読む前に**: URLに order-form と付くが、このページに入力欄は無い（v=1 の input 0個 `L`）。注文フォームは ADD TO CART の先の別ページ `/order-form1779446784006`。オファーは隠さず、ボタンは動画の直下に最初からある。

| 項目 | 実測（`L`=LPページ、`W`=LP動画の文字起こし、`F`=30秒おきの絵、`J`=判断） |
|---|---|
| URL | https://yourflirtmethod.com/order-form1766147252381 （最終URLに `#close-popup` が付く） |
| 作り | ClickFunnels クラシック（`data-de-type` 要素・`cfAR` フォーム）＋VWO（A/Bテストのタグ）`L`。page json の builder 判定は clickfunnels／stripe／elementor／hubspot の4つ。測った幅はスマホ（`data-hide-on="desktop"` の画像が v=1） |
| 動画 | Vidalytics（embeds/kMrukacT/YDsUshTG6sj5B8J7）。28分46秒（1726秒）。内部名「January VSL F Formula」、作成 2022-02-03・公開 2026-01-26。自動再生あり（onlyMuted=false）、noPause=true、途中再開あり（「Continue watching?」）、シークバーあり（rapidEngage・再訪者には出さない）、再生時間表示なし、速度変更あり |
| ページの部品（上から） | ①赤帯「⚠️WARNING: The Content On This Page Is Very Sensitive And May Be Removed At Midnight On September 12, 2026」（日付は `new Date()` で今日を差し込むJS）②「Warning: If You Get Your Dating Advice From Men You're Doomed To Fail...」③見出し「Want Her to Chase You? Then Stop Doing This One Thing...」④「In this free training, Marni reveals how to spark instant desire instead.」⑤動画（y=395）⑥**ADD TO CART（動画の直下 y=851。スマホは画像ボタン、PCは黄色の文字ボタン）**⑦レビューのスクショ画像・メディア掲載の画像 ⑧長文の手紙（y=1549〜14900）「I started with a cheap Craigslist ad」「by the next morning, I had 75 responses」「I'VE WORKED WITH 272,633 MEN OVER THE LAST 20 YEARS」「it's not your fault」、Scenario #1〜#3 ⑨Option 1／Option 2（y=15320）⑩文字の証言6件（Charles 39／Jay 43／Ali 27／Eric 52／Jeff 67／Graham 35、y=15713〜17507）⑪未来の描写（y=18367）⑫商品画像「F-FORMULA」（本・PC・iPad・スマホ、「+3 HOUR AUDIOBOOK」「+15 BONUS VIDEOS」）＋ADD TO CART ⑬値段の枠（数字なし）「I'm not even asking for $100」「less than a tank of gas」「the low, low price you see below」＋ADD TO CART×4 ⑭ボーナス7個「($238 VALUE)」⑮保証「a full 7 days」⑯締め＋ADD TO CART ⑰フッター「*All Refunds are subject to a refund fee of $6.95*」、FAQ と Refund Policy は別ドメイン breakingthegirlcode.com |
| 隠れている物（v=0） | 離脱ポップアップ「Please wait! You're so close...」＋カウントダウン（data-date 07/27/2021 で 00:00:00 表示）＋「Continue Watching」ボタン（`#close-popup`）。出る条件は HTML に見つからず判定不能（modalPopup は `data-trigger="none"`、`#exitPopup` はCSSだけ）。ほかに `[[[first_name]]], Watch The Video To Learn...` の差し込み見出し、「Click the button above to get instant access...」、「Hey there! It's Marni here...💋」の3つが display:none |
| 売り場 | ADD TO CART（n=7、全部同じ href）→ `/order-form1779446784006`（同ドメインの ClickFunnels 2段注文フォーム・Stripe） |
| 値段 | LPページ本文に値段の数字なし（page json の prices 9個に $47 無し、⑫の商品画像にも無し）`L`。動画 24:25 で $47 `W`。フォームで「Regular Price $197」「Yours Today Only $47」「(Total Value is $480)」＋バンプ $29.99（The Approach Blueprint） |
| 保証 | 3か所で違う。ページ「a full 7 days」／動画 24:41「a full 60 days」→24:48「increase it to 90 days」／フォーム「60-Day Money-Back Guarantee」と「7-Day Money-Back Guarantee」の両方。返金手数料 $6.95（ページ下部） |
| 仕掛け | 隠す秒は無し。Vidalytics の settings に CTA・時刻表示の設定なし（overlay は play／redirect=show false／resume／unmute／expire=無効／multiPause だけ）。`triggers` は計測だけ3つ: 432秒「25% Watched」／864秒「50%」／**1467秒「85% Watched - FB & Google」**。ClickFunnels の `data-delay="500"` は各要素のフェードのミリ秒で、出す秒ではない。偽の期限は①の今日の日付だけ |

### 広告 → LP のつながり

| 要素 | 広告（3分32秒） | LP動画（28分46秒）・ページ | 判定 |
|---|---|---|---|
| 餌 | 街頭の声掛け映像＋「here's the big secret about women」 | 動画0:00「Want to know the most reliable way to turn a girl on」／ページ見出し「Want Her to Chase You? Then Stop Doing This One Thing...」 | **差し替え**。街頭映像はLPに無い |
| 原因の呼び名 | 「feels something about you not thinks something about you」 | 動画3:57〜「roller coaster」「that same emotional mix of danger and safety」 | 同じ「感情で選ぶ」機序を、LPはジェットコースターの喩えに置き換える |
| 解の呼び名 | 2:31「the f formula」 | 動画 8:49 初出「her F formula, flirting formula」、11:28「a potent information packed course rightfully named The F Formula」、中身は「three phases」 | 一致（LPで3段階の中身が付く） |
| 権威 | 本人がソファで「from my personal experience」 | 動画2:58「who the hell is this woman」→「the world's number one wing girl」「Forbes and Men's Health」「CNN, NBC, CBS, Fox, and MTV」＋作者の2人目 Marissa（7:32） | LPで権威と作者を足す |
| 数字 | 「99.9」「thousands of women」 | 動画「over 10,000 real women」「top 1% of men」／ページ「272,633 MEN OVER THE LAST 20 YEARS」 | 入れ替わる |
| 約束 | 3:14「a free video that i made for you」 | ページ④「In this free training」。ただし動画直下のボタンは最初から「ADD TO CART」 | 「free」は見出しまで引き継ぎ、ボタンで売り場だと分かる |
| 期限 | 3:20「this video will not be available forever」 | ページ①「May Be Removed At Midnight On」＋今日の日付 | 一致（JSで毎日「今夜」にする） |
| 商品名 | 2:31 | 動画 8:49（30.7%）「F formula」、11:28（39.9%）で講座名 | 広告が先に名前を出す |
| 値段 | 無し | 動画 24:25（84.9%）「all for only $47」／ページ本文は数字なし／フォーム $47 | 値段は動画とフォームだけ |
| 保証 | 無し | 動画 60日→90日／ページ 7日／フォーム 60日と7日 | 数字がそろっていない |

### LP動画の構成（18節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00–0:43 | hook | 「Want to know the most reliable way to turn a girl on」「you do not need to be a six-foot tall male model with a six figure income」「The secret sauce to all of this is flirting」 | 赤い服の本人・屋外のロープ椅子（全58コマ同じ構図） |
| 2 | 0:43–2:01 | 使い道の広げ | 「research done at Webster's University」「a woman who previously had no interest in you or only saw you as a friend」「your girlfriend or your wife starts acting cold and distant」 | 本人 |
| 3 | 2:01–3:57 | 約束と権威 | 「a huge almost outlandish promise」「as a woman myself」「who the hell is this woman and why should I even listen to her?」「the world's number one wing girl」「featured on… Forbes and Men's Health」 | 本人 |
| 4 | 3:57–5:47 | UMP（喩え） | 「think of the last time you were on a roller coaster」「the fear of death. But because it's safe」「that same emotional mix of danger and safety」「her logical mind steps out of the way」 | 本人 |
| 5 | 5:47–7:13 | 上位1%の約束 | 「her ape brain feels safe」「the top 1% of men who approach women the right way」「you can master it over a short weekend」 | 本人 |
| 6 | 7:13–8:49 | discovery story（作者を足す） | 「I wasn't able to see outside of myself」「then I met my amazing wing girl Marissa」「put her flirting method into a step-by-step formula」「the first time I've let anyone besides me create a wing girl product」 | 本人 |
| 7 | 8:49–10:33 | 試験 | 「college kids, grown-ups, divorced men」「only involves three phases of conversation」「over 10,000 real women」「the guys in our test group」 | 本人 |
| 8 | 10:33–11:21 | UMS | 「the three distinct phases of flirting」「most men don't even realize that these three phases of flirting exist」 | 本人 |
| 9 | 11:21–12:36 | product reveal | 「a potent information packed course rightfully named The F Formula」「written course」「an audiobook version」「over $300 worth of bonus content」 | 本人 |
| 10 | 12:36–16:05 | 中身の列挙（n=11項目） | 「physical escalation as easy as counting to four」「the two flirting roadblocks」「the boomerang technique」「women in their 20s and women over 30」「how to check all of her boxes」 | 本人＋右側に項目名の白字（13:00〜15:30のコマ） |
| 11 | 16:05–19:02 | ボーナス7個 | $27／$19／$36／$37／$40／$32／$47 →「a total of $238 that you're getting for free」 | 「BONUS #2 VIDEO ILLUSTRATIONS BREAKDOWNS AND CASE STUDIES」の白字 |
| 12 | 19:02–20:27 | 値段の枠 | 「how much is this going to cost me? An arm and a leg?」「dinner can cost you like $50, $70, even $100」「$150 or $200」 | 本人 |
| 13 | 20:27–23:40 | testimonials（メール3通の読み上げ） | Kyle「I took a girl home the first night」／Chris「I'm on my second marriage」／Graham「a 50% chance of being completely useless」「you did it in under 48 hours」 | 右側の青いカードにメール全文（20:30〜23:00のコマ） |
| 14 | 23:40–24:35 | price drop | 「most guys would easily pay thousands of dollars」「two thousand or five thousand dollars」→ 24:25「plus the seven amazing bonuses worth over $238, all for only $47」 | 本人 |
| 15 | 24:35–25:55 | risk reversal | 「a full 60 days」→「I'm going to increase it to 90 days」「Even if the only thing you don't like is the font… 100% refund」「No questions asked」 | 白字「60 DAYS TO TRY」「DRASTICALLY ADVANCING THE QUALITY OF YOUR DATING LIFE」（sheet0 の49・50枚目。`ffmpeg -ss 1481` で切った 24:41 のコマには白字なし＝白字が出る秒は判定不能） |
| 16 | 25:55–26:17 | 注文の手順 | 「click the yellow button below right now」「credit card, debit card or PayPal on the next page」 | 本人 |
| 17 | 26:17–27:01 | 要約＋3度目のCTA | 「tested on thousands of girls」「click the button below now」（27:01） | 本人 |
| 18 | 27:01–28:46 | 2択クローズ | 「Choice number one… friend zone and in the creep zone」「choose choice number two, which is just say yes」「The measly $47」「Happy flirting」 | 本人（sheet1 の4コマ） |

語り手は全58コマで本人1人・同じ椅子。b-roll 0コマ、白字かカードが乗るコマ12／58 `F`。

### 売り場までの導線

ファネル: 広告（3分32秒）→ LP（Vidalytics 28:46・オファーは隠さない、ボタンは動画直下）→ ADD TO CART → 同ドメインの2段注文フォーム `/order-form1779446784006` → 決済（ClickFunnels＋Stripe）

1. ボタンは7個とも同じ href。動画を見なくても最初のボタンで売り場へ行ける `L`
2. 動画の中のボタン誘導は n=4（25:55「click the yellow button below right now」／26:05「You click the button below」／27:01「click the button below now」／28:39「Just click the link below to get access now」）。色（yellow）を言うのは 25:55 の1回だけで、ページのボタン色（黄 rgb(254,199,0)）と一致 `L` `W`
3. 注文フォーム（読むだけ・入力なし `L`）: 見出し「Congratulations – the F Formula is Almost Yours!」、Step 1 = 氏名・メール・電話・住所 →「Go To Step #2」、Step 2 = カード番号。スクリプトは `cf_stripe_orders.js`／js.stripe.com v2・v3
4. フォームの上乗せ: バンプ「ONE TIME OFFER: For just $29.99… Approach Blueprint」「Value: $348.00」、カウントダウン「00Hour19Minutes59Seconds」と「YOUR ORDER IS RESERVED FOR 00Hour09Minutes59Seconds」、動画の証言9本（Jordan 47／Don 36／Steve 64／Tom 41 ほか）、FAQ 7問
5. フォームの綻び: ボーナスの値段の合計は $218（#7 が動画の $47 ではなく $27）なのに「$238 value」と書く。保証文に「let Jim's team know」と「LINK TO SUPPORT HUB」がそのまま残る `L`
6. LP の `cfAR` フォームの行き先 `/f-formula1779446921216` を開くと、同じ動画・同じ見出しのセールスページ（26,299文字）。サンクスページではない `L`
7. 動画の 85% 計測（1467秒）は $47 を言う区間（1464.7–1474.8秒）の中にある `L` `W`

### コピーする時の骨（比率は28分46秒の実測）

hook 2.5%→ 使い道の広げ 4.5%→ 約束と権威 6.7%→ **UMP 6.4%（ジェットコースターの喩え）**→ 上位1% 5.0%→ discovery story 5.6%（作者を2人目に足す、25.1%地点）→ 試験 6.0%→ UMS 2.8%→ **product reveal 4.3%（11:28、39.9%地点）**→ **中身の列挙 12.1%**→ **ボーナス 10.3%**→ 値段の枠 4.9%→ testimonials 11.2%→ price drop 3.2%（24:25、84.9%地点）→ 保証 4.6%→ 手順 1.3%→ 要約 2.5%→ 2択クローズ 6.1%。サプリの型（オファーを隠す・1／3／6本・FAQを動画内で読む）の部品は無く、講座の1択 $47 をボタン常設で売る。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-118025645/sheet0.jpg`（0:00〜26:30）／`sheet1.jpg`（27:00〜28:30）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-118025645.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-118025645/sheet0.jpg]]
![[ec/wiki/vsl-teardown/frames/LP-118025645/sheet1.jpg]]
