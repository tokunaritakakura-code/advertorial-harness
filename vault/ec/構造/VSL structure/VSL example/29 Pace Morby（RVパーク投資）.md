<!-- 例 -->
# Pace Morby（RVパーク投資）— VSL example

読む人: この型（切り抜き・意見表明型（here's why I like X））の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [87161240](https://app.gethookd.ai/share/ad/87161240?signature=e81c3217d9e552ee3c0e27641ed1116803552968d3b3f31394f313a3b9acb8f1)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/87161240`）
LP: https://go.subto.com/rv-vsl-a
形式: VSL・動画 36s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 ClickFunnels の動画ページ（ボタンは申込フォーム行き）
拾った日: 2026-09-12
稼働日数 / 成績: 172日 / score 100（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 102本（2026-09-12）
選定: 補充枠。ブランドの稼働広告数500以上で着地が実測VSLの英語ブランドは2026-09-12時点で12で尽きた。GetHookd の vsl_page 分類・勝ち・稼働中から、稼働広告数が次に多いブランドを実測で確かめて入れた（102本）。広告の尺は36秒で、既存クライテリアの3分以上を満たさない（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/vsl-teardown/raw/87161240.full.txt`）／`W`=ローカルwhisper large-v3-turbo／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ・curl）／`J`=判断

## なぜ良いのか（1行）

36秒に数字を2つ（「$5 million RV park, no money down」「My worst RV park is $13,000 a month net」）置き、答えを言わない問い「why couldn't I just do RV parks instead of Airbnb?」で切って17分の動画へ送る。値段は広告・LP・申込ページの3か所で一度も出さず、売り物の名前はLPの免責文「DO NOT PURCHASE ANY SUBTO COURSES」にだけ出して、通話で売る。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00〜0:07 `T`「So here's why I like RV parks.」「It takes as much time for me to buy an RV park as it does for me to buy a single family house.」（`F` 黒いポッドキャスト部屋・「Subto」黒キャップ・マイク・2〜5語ずつの焼き込み字幕。13枚中9枚が4〜5語） |
| lead | 0:07〜0:22 `T`「You can go buy a $5 million RV park, no money down, seller finance.」「they're already cash flowing」「They're easier to negotiate with.」 |
| discovery story | 無し |
| UMP | 無し（痛みも原因も言わない。比べる相手だけ出す: single family house 0:02・Airbnb 0:34） |
| UMS | 0:07〜0:20 `T`「no money down, seller finance」＋「Buying them from a retiree」「Give us monthly payments. We're going to go travel.」。**呼び名は業界語の seller finance だけ**（自前の呼び名なし） |
| product reveal | 無し（本文も「Click the link below to learn more about RV Parks」で商品名なし） |
| price drop | 無し |
| risk reversal | 無し |
| testimonials | 無し（本人の数字だけ `T`「My worst RV park is $13,000 a month net」0:24、「Our average stay on all of our RV parks is four days」0:30。本文「$250 million, 2,000+ door portfolio」） |

締め: 0:34〜0:36 `T`「So why couldn't I just do RV parks instead of Airbnb?」で終わる。口頭のCTAは0回（click／link の出現 0/15区間）。CTAは本文の「STOP waiting, take action --> https://go.subto.com/rv-vsl」だけ。

## 盗む所

- 冒頭を意見表明「So here's why I like X」にして、2秒目で比べる相手（single family house）を出す
- 下限で言う数字「My worst RV park is $13,000 a month net」（0:24）。LP動画は後で平均「My average park nets about $20,000 per month」（15:12）を出す
- ボタンを動画ではなく**ページを開いてからの2分タイマー**で出す（`data-minutes="2"`）。動画17:03は一度もボタンを指さない（click／apply／button の出現 0/204区間 `W`）

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。13枚とも同じ黒い部屋の本人アップで、字幕は2〜5語（5語＝7s・8s「A $5 MILLION RV PARK」／4語＝2〜5s・10〜12s／3語＝0s・6s／2語＝1s・9s）、各コマ1語だけ色付き（黄1枚＝0s「SO」／青12枚）。9sの字幕は「SELLER FINANCED」（音声は「seller finance」）。

![[ec/wiki/vsl-teardown/絵/87161240-hook]]

## 全シーン × b-roll（`F`）

尺 35.9秒 ／ 3シーン ／ 平均 12.0秒 ／ しきい値 0.25（0.0〜6.1 アップ／6.1〜27.1 アップ／27.1〜35.9 引きの横顔。b-roll は0枚）

![[ec/wiki/vsl-teardown/シーン/87161240]]

## LP（着地ページ）— go.subto.com/rv-vsl-a

**読む前に**: 広告の `go.subto.com/rv-vsl` は302で `/rv-vsl-a` に飛ぶ（`curl -sI`）。ページは値段を出さない動画ページで、ボタンの先は通話の申込フォーム。LP動画（17分03秒）は文字起こしと絵に落としてある。

| 項目 | 実測（`L`=LP、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=30秒おきの絵） |
|---|---|
| URL | https://go.subto.com/rv-vsl-a （title「Subto \| RV Parks」） |
| 作り | ClickFunnels classic（`cf:app_domain`=app.clickfunnels.com・GTM）。builder 検出の stripe は隠しフォーム `cfAR` の `data-stripe` 属性だけで、決済欄は無し `L`。コメント欄は無し（blocks n=29） |
| 動画 | Wistia `96o5vxxzzo`（内部名「RV VSL FINAL (1702)」）1022.59秒＝17:03。16:9・コントロール表示あり（`controlsVisibleOnLoad=true`）・字幕プラグインon・`chapters=null`（media json） |
| ページの部品（上から） | ①ロゴ画像（y=13）②見出し「RV Parks: One Property Can Replace Your Job」（y=67）③副見出し「Pace breaks down how to find, acquire and expand RV parks while visiting his recently purchased park」（y=114）④[隠れ]ボタン「I'm Ready to Take Action」（CTA Top）⑤左列に動画＋「View Chapters In Progress Bar」（v=0）／右列（`col-md-4`）「What's Covered:」4行（Locate／Acquire「with no money down」／Expand Revenue／「BONUS: Top 2 lessons for new RV Park investors & an opportunity to apply for a free strategy call」）（y=205）⑥「Next steps will unlock in 👉🏻」＋カウントダウン（取得時 00:01:36）（y=660）⑦[隠れ]ボタン×3（Mobile Top／Bottom／mobile）⑧画像1枚（y=861・中身は判定不能＝blocks に alt 無し）⑨免責「results are not typical」「DO NOT PURCHASE ANY SUBTO COURSES」＋フッター4リンク（y=1015） |
| 売り場 | ボタン4個とも → https://go.subto.com/rv-vsl-schedule-a （**通話の申込フォーム**。決済ではない） |
| 値段 | 表示なし（LP・申込・完了の3ページ実測 `L`）。LP動画の「$」34区間の内訳は、本人の物件と取引の数字31（家賃・日よけの値段・売り手への支払い）／視聴者の手取りと目標額3（193.8秒「putting $40,000 per month in your pocket」・912.2秒「I want to make $50,000 a month」・918.2秒「I want to be $100,000 a month」）／売り物の値段0 `W`。値段は判定不能（通話の中で出る） |
| 保証 | 表示なし（3ページ実測）。あるのは免責文だけ |
| 仕掛け | ClickFunnels の evergreen カウントダウン `data-hours="0" data-minutes="2" data-seconds="0"`＋ボタン行4つに `data-timed-minutes="2"`。**ページを開いて2:00でタイマー行（row-109／row-143）が消え、ボタン行が出る**（`data-expire-type="showhide"`）。`data-revisit-action="reset"`＝再訪で2分からやり直し。動画の再生位置とは連動しない `L` |

### 広告 → LP のつながり

| 要素 | 広告（36秒） | LP動画・ページ（17分03秒） | 判定 |
|---|---|---|---|
| 餌（冒頭） | 「So here's why I like RV parks.」 | 0:00「People talk about single family and multifamily, but... making money by renting dirt」 | 比べる相手（single family）は引き継ぎ、言い回しは差し替え |
| 機会の理由（原因の呼び名の位置） | 「Buying them from a retiree」「ready to retire」 | 2:17「I would like to retire」→4:09「We call these people tired landlords」 | 呼び名はLPで初めて付く |
| 解の呼び名 | 「no money down, seller finance」 | 0:37「no money down, no credit, and no credentials」／3:31「seller finance deal」／7:43「PMPs, private money partners」 | 一致＋LPで2つ足す |
| 権威 | 本文「$250 million, 2,000+ door portfolio」 | 3:19「over the last five years of being in RV parks, I started as a lender first」。$250M・2,000 door は0回 | 数字は引き継がない |
| 数字 | 「$5 million」「$13,000 a month net」（最悪の物件）「four days」 | 0:09「$200,000 a year」／1:08「$18,000 per month」／3:13「$40,000 per month」／15:12「average park nets about $20,000」。four days は0回 | 下限から平均へ差し替え |
| 約束 | 見出し「1 RV Park Can Fully Replace Your Income!」 | ページ見出し「One Property Can Replace Your Job」／0:25「one park could literally allow you to quit your entire job」 | 一致 |
| 問い | 「why couldn't I just do RV parks instead of Airbnb?」 | Airbnb 0回（n=204区間） | 回収されない |
| 商品名 | 無し | 言わない。6:51「members in the Sub2 community」がブランド名の初出。売り物を名指すのは免責文「SUBTO COURSES」だけ | 売り物は通話まで伏せる |
| 値段 | 無し | 無し | 通話で出る（判定不能） |
| 絵 | 黒い部屋・黒キャップ・縦 | 青い花の壁のスタジオ・白キャップ＋現地ロケ・横16:9 | 別収録（`F`） |

### LP動画の構成（14節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00〜0:32 | hook | 「making money by renting dirt」「nets $200,000 a year in my pockets」「it's the first time I've ever been here」「how one park could literally allow you to quit your entire job」 | 建物の前に立つ本人→空撮（右下小字「OUR RV PARK IN YUMA, AZ」と読める） |
| 2 | 0:32〜1:03 | 反論潰し | 「buying an RV park is completely out of reach」→「no money down, no credit, and no credentials」「They want to give you creative finance」 | 青い花の壁のスタジオ |
| 3 | 1:03〜2:08 | 数字の階段 | 「$18,000 per month in my pocket」「revenue minus expenses minus payroll minus taxes minus my payment to the seller」→awningsで「$28,000 a month net」→拡張で「40 grand a month」 | 草地の本人・スタジオ（「The Owner, Probably...」の字） |
| 4 | 2:08〜3:02 | 機会の理由 | 「I would like to retire and not run my own park」「the rents have not been increased in five to seven years」「expand into 40 more spaces」 | スタジオ |
| 5 | 3:02〜3:48 | 権威＋比べる相手 | 「correct me if I'm wrong, would probably love to just own one of these parks」「I started as a lender first, lending to other students of mine」「way easier to get a seller finance deal on an RV park」 | 「RV PARKS ARE EASIER FOR SELLER FINANCE!」 |
| 6 | 3:48〜4:56 | 見つけ方 | 「We call these people tired landlords」「dealsauce.io... RV parks, ownership over 15 years, one park per name」「no money out of our pocket」 | 「TIRED LANDLORDS」 |
| 7 | 4:56〜6:39 | 売り手の得 | 「he is going to be my bank」「$15,000, $20,000 payment」「no management, no headaches, no taxes, no toilets, no trash」「plant trees or just harvest the fruit」 | 「STRESSORS GONE / MANAGEMENT LOCATION TENANTS」・「MOST RECENT COMMENT」 |
| 8 | 6:39〜8:24 | 頭金の作り方 | 「The seller allowed us to put $500,000 down」「members in the Sub2 community」「15% ownership」「PMPs, private money partners」「$18,000 to $20,000 every single month」 | 2人で歩く現地・「PML = PRIVATE MONEY LENDER」 |
| 9 | 8:24〜9:35 | 現場の管理人 | 「I've never been here」「we have Maddie on site」「You're in 53, right?」「a full-time mom」 | 「MADDY」・「THIS GIRL IS AWESOME」 |
| 10 | 9:35〜12:40 | 改善の計算（日よけ） | 「unlimited budget」「Awnings are $800」「$6,000 per awning」「a 30% return on my money」「pay themselves off in 36 months」「get 40 more spots」「We have a waiting list」 | 事務所の机の女性・スタジオ |
| 11 | 12:40〜13:04 | 需要 | 「none of it is seasonal」「Montana parks make all their money in five or six months」「a five-year waiting list」 | スタジオ |
| 12 | 13:04〜15:32 | 新人への教訓2つ（ページの BONUS） | 「Lesson number one... don't touch the cash flow for year one」「when my bank account hit zero」→step two「the volume game or the snowball effect」「My average park nets about $20,000 per month」「five or six parks」 | 「LESSON #1: DON'T TOUCH THE CASHFLOW」・「THE RV PARK SNOWBALL」 |
| 13 | 15:32〜16:32 | 需要の理由（車内） | 「people that don't want to commit to a lease」「It's non-committal rental」「Oil drives this entire town.」 | 運転席の本人＋YouTube の「SUBSCRIBE / COMMENT / LIKE」重ね |
| 14 | 16:32〜17:03 | 締め | 「I hope this has inspired you to show you that you can do this too」「It solves affordability」「double down, triple down, and quadruple down」 | スタジオ |

語り手: 本人が顔を出すのは34コマ中30（`F` 青い花の壁のスタジオ21／現地ロケ7／車内2）。人物のいない4コマは空撮と文字の図（0:30「OUR RV PARK IN YUMA, AZ」・3:30「RV PARKS ARE EASIER FOR SELLER FINANCE!」・5:00「STRESSORS GONE」・14:30「THE RV PARK SNOWBALL」）。15:30のコマにYouTubeの登録ボタンの重ねが残る＝YouTube用の本編をそのまま載せている。

### 売り場までの導線

ファネル: 広告（36s）→ LP（Wistia 17:03・ボタンはページを開いて2:00、動画と無関係）→ 申込フォーム（/rv-vsl-schedule-a）→ 完了ページ（/rv-parks-ty-1・通話の準備）→ 通話 → 決済（どこで払うか判定不能・通話の中）

1. 広告の `/rv-vsl` → 302 → `/rv-vsl-a`（`curl -sI`）
2. 2:00でタイマー行が消え、ボタン「I'm Ready to Take Action」が出る。動画は17:03のうちボタンを指さない（click／apply／call to action の出現 0/204区間）。申込の話はページ右列の BONUS 行「an opportunity to apply for a free strategy call」だけ
3. ボタン → https://go.subto.com/rv-vsl-schedule-a 見出し「Apply for a strategy session with my team by completing the form below」。フォームは `apps.newreacheducation.com/pub/funnel/ST?funnel=rvp_vsl` の iframe で、1段目は First Name／Last Name／Email／Phone＋「Next」（2段目以降は入力しないと出ないので取得失敗）`dia look`
4. 予備導線「Our Calendars Fill Up Fast!... click here to request a call」→ `subto.typeform.com/to/fV7eY1xp`
5. 完了（iframe の `ty=`）→ https://go.subto.com/rv-parks-ty-1 「You Are One Step Closer!」Wistia 4本・FB Group「Over 160,000 members」・「Expect to spend 30-45 minutes on the call」「Have key stakeholders (business partner or significant other)」`curl`
6. 値段・保証・決済欄は3ページのどこにも無い。売り物を名指すのは免責文「DO NOT PURCHASE ANY SUBTO COURSES」だけ

### コピーする時の骨（比率は17分03秒＝1023秒の実測）

hook 3%（地代で稼ぐ＋年$200,000＋初訪問）→ 反論潰し 3%（no money／no credit／no credentials）→ **数字の階段 6%**（$18,000→$28,000→$40,000）→ 機会の理由 5%（引退したい売り手・5〜7年上げていない家賃）→ 権威＋比べる相手 4.5% → 見つけ方 6.5%（tired landlords・15年以上1物件の絞り込み）→ 売り手の得 10% → 頭金の作り方 10%（$500,000を仲間5人で・PMPs）→ 現場の管理人 7% → **改善の計算 18%**（$6,000の日よけで月+$200・30%・36か月）→ 需要 2% → 教訓2つ 14.5% → 需要の理由 6% → 締め 3%（CTAなし）。product reveal・price drop・保証・FAQ・証言の節は0/14節。売る節を動画に置かず、2分タイマーのボタンと通話に預ける。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-87161240/sheet0.jpg`（0:00〜16:30の34コマ）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-87161240.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-87161240/sheet0.jpg]]
