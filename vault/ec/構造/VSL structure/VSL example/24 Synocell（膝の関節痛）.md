<!-- 例 -->
# Synocell（膝の関節痛）— VSL example

読む人: この型（寸劇型＋否定列挙（2本継ぎ・AI医師））の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [160281900](https://app.gethookd.ai/share/ad/160281900?signature=ae314abe6c5d11af3953d93984b6f9781b12f7105862c7caeced2091bf9ae15a)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/160281900`）
LP: https://thepainreport.com/pages/syn-vslfb/
LPの振り分け: 上のURLは302で `/pages/syn-vslfb-dup/` か `/pages/syn-vslfb-v2/` に飛ぶ（n=3回開いて -dup 2回・-v2 1回。`curl -sIL` の Location と `dia open` で実測）
形式: VSL・動画 324s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 Wistia動画が主役の売りページ（オファーを39:38まで隠す）
拾った日: 2026-09-12
稼働日数 / 成績: 17日 / score 92（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 227本（2026-09-12）
選定: 補充枠。ブランドの稼働広告数500以上で着地が実測VSLの英語ブランドは2026-09-12時点で12で尽きた。GetHookd の vsl_page 分類・勝ち・稼働中から、稼働広告数が次に多いブランドを実測で確かめて入れた（227本）（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし／`W`=ローカルwhisper large-v3-turbo／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ）／`J`=判断
広告の文字起こしは `W`（GetHookd の文字起こしが空だったため。全文は `ec/wiki/vsl-teardown/raw/160281900.full.txt`）。LP動画の文字起こしは67:09以降に whisper の繰り返し（67:09.20〜67:29.42 に「CineCell right now」「and God bless」が16回）が混じるので、内容は67:04までを数えた

## なぜ良いのか（1行）

0秒で1人2役のバスケ寸劇「Hey, if you got bad knees, take it easy, bro」、14〜25秒で painkillers／physical therapy／knee replacement を「Nope」「No」「Of course not」で3つとも消し、33秒で「leading orthopedic surgeon in Boston」、38秒で「the team doctor for the Celtics」、5:01「Free to watch. No email required」で67分のLP動画へ送る。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00〜0:26 `W`「Hey, if you got bad knees, take it easy, bro」「Wasn't he complaining about bone-on-bone pain just, like, last week?」→「You want painkillers?」「Nope」「Uh, physical therapy?」「No」「it can't be knee replacement」「Of course not」（`F` バスケコート。灰色ヘンリー＋膝サポーターで座る男と、ヘッドバンドで玉を持つ男。同じ顔で `J` 1人2役。字幕「Nope.」だけ赤地の大文字） |
| lead | 0:26〜1:22 `W`「Dr. Kyle's joint restoration technique」「Takes about seven seconds」「No physical therapy, no creams, no meds」「My brother sent me the video that Dr. Kyle made. It's free」→1:22 で撮影素材が変わる（`F` 黒Tシャツの男の独白＋ビデオ通話風の女。画面下に「Dramatization using an AI-generated performer」）「Do your knees feel like they're grinding bone on bone?」「stop using cortisone shots and NSAIDs」「you could be pain-free in less than a week」 |
| discovery story | **短い（22秒）** 0:44〜1:06 `W`「while he was working with the players, he noticed something weird」「`Some of them would heal from injuries insanely fast`」「it wasn't genes, age, lifestyle」 |
| UMP | 2:00〜3:18 `W`「they trick your brain into feeling less pain」CBD／Biofreeze／heat／ice「none of them stop what's eating away at your joints」→cortisone「weakens your tendons, thins your cartilage」→NSAIDs「block the healing pathways your body uses to rebuild joint cartilage」→「bone grinding against bone」。**原因の呼び名なし**（LPで「joint termites」が付く） |
| UMS | 3:27〜3:54 `W`「your body can actually regenerate new cartilage」Duke University「same regenerative pathways as salamanders and zebrafish」。呼び名は **joint restoration technique**（0:26／1:06／1:36／4:32 の4回）＋「seven seconds when you wake up」（4:46） |
| product reveal | 無し（「Watch Dr. Kyle's video」「I've shared the link to the video right below」だけ。商品名なし） |
| price drop | 無し（4:15「you don't have to spend thousands on injections」は値段ではない） |
| risk reversal | 無し（5:01「Free to watch. No email required」は動画を見る側の手間を消すだけ） |
| testimonials | 個人の声1 `W` 4:07「Sandra Miller, 72 years young」「from needing knee replacement surgery to hiking the Grand Canyon」（ほかは寸劇の「my brother」だけ） |

無かったブロックは「無し」。欠落そのものが発見。

## 盗む所

- 否定列挙を寸劇の問答にする。「You want painkillers?」「Nope」→「Uh, physical therapy?」「No」→「it can't be knee replacement」「Of course not」の3往復（14〜25秒）。1人2役・屋外・スマホ撮りで撮れる
- 広告の4:07で出した証言（Sandra Miller・72歳・Grand Canyon）を、LP動画の0秒の餌にそのまま使う
- ページのオファー枠を、動画が「for just $59」と言い切った1秒後（39:37→39:38）に出す。再生しなくても開いて39:33経てば出す時計を二重に持つ

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

![[ec/wiki/vsl-teardown/絵/160281900-hook]]

## 全シーン × b-roll（`F`）

尺 324.3秒 ／ 86シーン ／ 平均 3.8秒 ／ しきい値 0.25（シーン数はしきい値に依存する）。0〜1:22 はバスケ寸劇、1:22〜5:24 は黒Tシャツの男と眼鏡の女の掛け合い＋ストックとCG

![[ec/wiki/vsl-teardown/シーン/160281900]]

## LP（着地ページ）— thepainreport.com/pages/syn-vslfb-dup

**読む前に**: 分析したLP動画は -dup 側（Wistia「SynoCell VSL V4」67:30）。もう片方の -v2 は「VSL V5」68:01 でオファー表示が40:10。見出し・3段の値段・コメント10件は両方で一致した（`curl` で取った2ページのHTMLを比較）。

| 項目 | 実測（`L`=LP、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=30秒おきの絵、`J`=判断） |
|---|---|
| URL | https://thepainreport.com/pages/syn-vslfb-dup/ （`/pages/syn-vslfb/` から302。`-v2` 側は https://thepainreport.com/pages/syn-vslfb-v2/ ） |
| 作り（builder） | 判定不能（応答ヘッダは `server: cloudflare` だけ）。`/pages/` のパスと `cdn.shopify.com/s/files/1/0615/0265/2571` の画像は Shopify の形。クラスは Tailwind の書き方（`md:mt-0`・`!hidden`）＋jQuery。偽コメント10件 `L` |
| 動画 | Wistia。PC `f59ukvojqr`／スマホ `z0vrqybhdf`（画面幅768px以下で切り替え）。内部名「CURRENT LIVE : SynoCell VSL V4 [Var 2 Intro Short + New Cred + New Blue Zone + 300kbps 1024x576] - Desktop_081326」4050.06秒＝67:30（`fast.wistia.com/embed/medias/<id>.jsonp` で確認）。シークバー無し（`playbar: false`、URLに `#vibdeobar` を付けた時だけ出る）・音量と全画面のボタン無し・「Click for sound」「Your video may take 10 seconds to load」。-v2 は `i9dbihha8d`／`gr03e2ki35`「SynoCell VSL V5 [Intro Short + New Cred + New Blue Zone + Mixed Whiteboard CT + 300kbps]」4081秒 |
| ページの部品（上から） | ①「Top Orthopedic Surgeon:」＋見出し「Are Joint Termites Causing Your Knee Pain?」＋小見出し「The real reason your knee pain spreads to your hips, back, and fingers」「the 30-second morning habit that stops it cold」②動画 ③医師の紹介（Dr. Kyle Stephenson・Harvard University Athletics・Celtics・Tufts のフェロー）④「In this Exclusive Presentation, You'll Discover...」3つ（NSAIDs が軟骨を縮める／カイロの禁じ手／3 natural ingredients）⑤偽コメント「10 Comments」10件（Liam〜Harper。10件全部が動画の位置を指す「at the 5-minute mark」「around the 6-minute mark」「at the 10-minute mark」「the ending」）⑥**ここから隠れ（v=0・`.afterdrop`）** 3段のオファー（HTML上は1本／6本 pain superhero／3本 doctor's choice の順・各段に ORDER NOW の画像ボタン）⑦保証「90-Day No Questions Asked 100% Money-Back Satisfaction Guarantee」⑧ボーナス3冊（$105相当）⑨「Your Story Can Be Next」Verified Customer 4件 ⑩3段のオファー再掲 ⑪FAQ Q1〜Q12（Read More で開閉）⑫FDA免責・© 2026 Vital Health・「Click here to view text」（`/pages/syn-vslfb-text/`＝台本の文字版、約10,857語）・Citations のURL 23本 |
| 売り場 | ORDER NOW → `https://get.synocell.com/products/syn-3-pack-syn-vslfb-dup/`（1本・6本は `syn-1-pack-`／`syn-6-pack-`、-v2 は末尾が `-syn-vslfb-v2/`）。パスは /products/ だが中身は **SamCart の1ページ注文フォーム**（HTMLに `samcart` 181〜205か所、Stripe Elements の live 鍵、ボタン「Place Order Now」）。PDP・カートは挟まない |
| 値段 | 1本 $59（元$99・送料 $4.95）／3本 $147（$49/本・元$297・doctor's choice。注文フォームで「Shipping Free」）／6本 $234（$39/本・元$594・pain superhero）。3本と6本にボーナス電子書籍3冊（$29＋$37＋$39＝$105相当）。注文フォームに「Shipping Insurance - $2.49」の追加欄 |
| 保証 | 90日返金。動画44:20「a full 90 days」45:14「even if you finish every capsule」／ページ「You can even send back an empty bottle」／注文フォーム「within the next 90 days」 |
| 仕掛け（隠す秒・タイマー） | 3段は `dropit()` で出る。条件はどれか1つ: (a) Wistia の `secondchange` が2378秒（39:38）以上 (b) 再生と関係なくページを開いて2373秒（39:33）経過（`TARGET_SECONDS = (39 * 60 + 38) - 5`。URLの `#elapsedtime=` で経過秒を上書きできる）(c) URLに `#drop` か Ctrl+B。-v2 は 40:10（`s === (40 * 60) + 10`）と 40:05。スマホは再生10秒後に `.important` の文を消す。再訪で出したままにする保存は、ページ文字列を `localStorage`／`cookie` で検索して見つからない。注文フォームに「Your Special Price Is Reserved For」10:00 のカウントダウン（`dia read` の時点で 9:26） |

### 広告 → LP のつながり

| 要素 | 広告（5:24） | LP動画（67:30）・ページ | 判定 |
|---|---|---|---|
| 餌 | 0:00 バスケ寸劇「bad knees, take it easy, bro」。4:07 に Sandra Miller 72歳・Grand Canyon | 0:00「72-year-old Sandra Miller summited the Grand Canyon's North Rim, 14 miles, 5,000 vertical feet」 | **広告4:07の証言がLPの0秒の餌になる**。寸劇は捨てる |
| 原因の呼び名 | 2:15「what's eating away at your joints」（呼び名なし） | 12:57「joint termites, or cytokines」。ページの見出しも「Joint Termites」 | 呼び名はLPで初めて付く |
| 解の呼び名 | 「joint restoration technique」「Takes about seven seconds」 | 1:02「7-second morning ritual」2:51「seven-second ritual you do each morning from your kitchen」。ページの小見出しだけ「30-second morning habit」 | 7秒は引き継ぐ。technique は ritual に変わる。ページは30秒で食い違う |
| 権威 | 0:32「leading orthopedic surgeon in Boston」Tufts／Harvard／Celtics | 0:21・3:14 同じ肩書き＋「board-certified」。`F` 白衣の実写医師（名前の帯「DR. KYLE STEPHENSON」） | 肩書きは一致。広告の医師役（黒Tシャツ・AI表記）とLPの医師は別の顔 `F` |
| 数字 | 7秒・72歳・「less than a week」・「two weeks」 | 72歳・14 miles・11 months・34%・40%・10 hours・3 inches | 共通は72歳と7秒の2つ |
| 約束 | 5:03「Just a short video」 | 0:26「By the end of this short video」→実際は67:30。3:06「I'll walk you through exactly how to do this ritual yourself」 | **7秒の儀式は予告だけで、やり方を一度も言わない**（`W` 全文で「ritual」は3回、全部3:06まで） |
| 否定 | 1:14「No physical therapy, no creams, no meds」 | 0:26「isn't a stretch, a supplement, or a surgery」→29:45 に出るのはカプセルのサプリ（`F` ボトル・カプセルの製造ライン） | 否定した物そのものを売る `J` |
| 成分 | 出ない | 0:32「it has nothing to do with glucosamine」。ページFAQ Q1 の答えは「combines ingredients like Glucosamine and MSM」 | **動画とページで食い違う**（`W`＋`L`） |
| 商品名 | 出ない | 26:48 初出（whisper は「CineCell／CenoCell」と聞き取り。ページ表記は SynoCell）、29:45「Introducing」 | LPで初出 |
| 値段 | 出ない | 37:30「$200? $300? $500?」→39:10「$69」→39:37「$59」 | LPで初出 |

### LP動画の構成（21節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00〜1:22 | hook（証言の餌＋予告4つ） | 「72-year-old Sandra Miller summited the Grand Canyon's North Rim」「My knees and hips feel stronger today than when I was 30」「former team doctor for the Boston Celtics」「isn't a stretch, a supplement, or a surgery」→予告4つ「the number one joint supplement in America」「three healthy foods」「60-second test you can do from your chair」「7-second morning ritual」 | 野原を歩く女・錠剤を持つ手「The #1 joint supplement in America」 |
| 2 | 1:22〜3:14 | lead | 「Sandra couldn't walk to her own mailbox」「A double knee replacement was already on the calendar」→「Have you ever heard of the zebrafish?」「2019 Duke University study published in Science Advances」「there's one catch」「Harvard and MIT researchers」→「daily ibuprofen, NSAIDs, cortisone shots」「It speeds it up」→「seven-second ritual」「Imagine 60 days from now」 | 膝の手術痕・医師と患者・赤い膝のCG |
| 3 | 3:14〜3:37 | 権威 | 「My name is Dr. Kyle Stevenson」「board-certified orthopedic surgeon」「Harvard University Athletics」「Boston Celtics」 | 白衣の医師＋名前の帯 |
| 4 | 3:37〜6:11 | 患者 Walter の物語（失敗の列挙） | 「Walter was 67」ibuprofen→cortisone「another and another」「For seven years」→「Both knees, bone on bone」→「double knee replacement」「saws through your femur」「Up to 34% of knee replacement patients still have chronic pain a full year later」→「Doc, I wish someone had told me this ten years ago」 | ibuprofen の瓶・手術の手袋・医師と老人 |
| 5 | 6:11〜9:49 | 発見の物語（Celtics） | 「only about 10 hours of education on pain management, out of 12 years of schooling」→「a virtually unlimited budget」→「clears out the joint termites」→Sandra と Darren（37歳の消防士）→「No addictive drugs, no side effects, no brain fog, no memory loss」 | Harvard のスタジアム・マスクで走る選手・山頂の女 |
| 6 | 9:49〜12:32 | 否定列挙（失敗3つ） | 「Mistake number one. Painkillers, NSAIDs, and CBD」「the boomerang effect」「up to 40% of products contain heavy metals」→「Mistake number two. Cortisone and steroid injections」→「The third mistake is surgery」「failed surgery syndrome」 | 自転車の夫婦・白黒のベンチの女・「NATURAL WAY TO CALM INFLAMMATION」 |
| 7 | 12:32〜17:03 | UMP | 「a natural Teflon coating」「joint termites, or cytokines」「Harvard Medical School and the National Institutes of Health」「2017 study in Frontiers in Immunology」「lose up to three inches in height」→がん・心臓病・認知症まで広げる→Duke「zebrafish and salamanders」「our ears and our noses」 | 「Cytokines:」の図・Frontiers 2017 の表紙・3 INCHES の漫画・Science Advances／DukeHealth の引用 |
| 8 | 17:03〜20:50 | Blue Zones | 「why do `some` 75-year-olds bound up a flight of stairs」→Okinawa／Sardinia／Ikaria「women in their 90s kneel on tatami mats」→「avocados, soybeans, olives, and the resin of the frankincense tree」「Not genetics, not luck, not climate, biochemistry」 | 沖縄の海の空撮・畳の女性・研究机 |
| 9 | 20:50〜29:45 | UMS（成分4つ＋製造） | 21:00 ASU「quietly ignored and suppressed in the U.S.」「three-year, randomized placebo-controlled clinical trial」→23:28 Boswellia「mentioned 22 times in the Bible」→24:41 quercetin「2022 Journal of Molecular Medicine」→26:39 hyaluronic acid→**26:48 商品名の初出**「That's when CineCell went from being a breakthrough」→29:14「triple-phase micro-encapsulation」 | 乳香を焚く手・肩のX線・カプセルの製造ライン・研究室 |
| 10 | 29:45〜31:34 | product reveal（3段の仕組み） | 「Introducing CenoCell」「Step 1. It extinguishes painful inflammation at the source」「Step 2. It reactivates your body's natural repair system」「Step 3. It restores youthful lubrication」 | 「EXTINGUISHES PAINFUL INFLAMMATION AT THE SOURCE」の文字・老夫婦 |
| 11 | 31:34〜33:26 | 証言3人 | 整備士「I even started jogging again at 62」／腰の女「My doctor said it was just old age」「walking two miles a day」／自転車の男「Within a month, I was back on my bike」 | 自撮りの女・名前の帯「MARK」の男・自転車の夫婦 |
| 12 | 33:26〜35:41 | 未来の描写 | 「finishing all 18 holes」「strolling cobblestone streets in Paris, or exploring the Grand Canyon」「dancing at weddings」 | 脚が光るCG・ストレッチの女・山を歩く女 |
| 13 | 35:41〜39:02 | 値段の枠 | 「my reputation means everything」「quality like this doesn't come cheap」→37:30「$200? $300? $500?」→heart disease／dementia／diabetes の列挙→「an incredible value even at $500 per bottle」→「only through this website」 | ボトル「CLINICAL-GRADE INGREDIENTS」 |
| 14 | 39:02〜40:09 | **price drop** | 「$500, $200, or even $100」→39:10「30-day supply of CineCell for just $69. That's more than 40% off」→39:37「for just $59. That's another $10 off」＝**ページのオファー表示（39:38）の1秒前** | 「MORE THAN 40% OFF」とボトル |
| 15 | 40:09〜42:59 | まとめ買い | 「Think of it like compound interest」→41:28「three-bottle package」「$49 per bottle」「free shipping」→41:50「six-bottle package, our `best` value option」「just $1.30 a day」→「this special $59 price is not guaranteed beyond today」「Our production costs are rising」 | ボトルを並べた医師・少量生産の瓶 |
| 16 | 42:59〜44:14 | 取り置きの脅し | 「your order has been set aside for you」「if you leave this page, your reserved bottles may be released to the next person in line」→「God's green earth」 | 白黒の男「one click away」 |
| 17 | 44:14〜46:03 | risk reversal | 「I'm personally guaranteeing your order today for a full 90 days」「Just say maybe」「this guarantee applies even if you finish every capsule」 | 机の男「To prove to you」・ボトル |
| 18 | 46:03〜47:00 | 注文の手順 | 「If CineCell is still in stock, you'll be taken directly to the secure order page」「join our waiting list」「256-bit SSL encryption」「Amazon.com」「enter your details on the next page」 | ノートPCに打ち込む女 |
| 19 | 47:00〜50:38 | クローズ1（2択） | 「a very real crossroads in life」「the devil comes straight to your door」「Unchecked inflammation is like rust spreading through metal」→「the path of healing and renewal」→「you don't pay a single penny」 | 杖の老人「The first choice is, unfortunately, to do nothing」・錆・歩く夫婦 |
| 20 | 50:44〜64:27 | FAQ×10（白地に文字） | 「Still watching?」→Linda（Scottsdale）／Robert（Dayton）／Denise（Jacksonville）／James（Spokane）／Margaret（Sarasota）／Patricia（San Diego）／Laura（Columbus）／Tom（Austin）／Sharon（Nashville）／George（Portland）。ページのFAQ Q1〜Q12 のうち Q4（nerve damage）と Q12（How do I order）を抜いた10問が同じ順 | 白地に黒字、上に質問の小見出し |
| 21 | 64:27〜67:04 | クローズ2 | 「having watched my dad struggle with pain」「your golf clubs, tennis shoes, and passport will collect dust」「$59 might cover a single meal at a decent restaurant」→partner／children／grandchildren→「Thanks for watching and God bless」 | 顔を覆う男・荷物を受け取る女・「SAY YES TO SYNOCELL TODAY!」 |

絵の床: 語り手は実写の白衣の医師（`F` 名前の帯「DR. KYLE STEPHENSON」3:15付近）。50:45付近に黒コマ1枚、51:15〜64:15 は白地に字幕だけ（`F` sheet1 の6コマ＋sheet2 の21コマ＝27コマ）。

### 売り場までの導線

ファネル: 広告（5:24）→ `/pages/syn-vslfb/` から302で2本のLPに振り分け → LP（Wistia 67:30・オファー表示 39:38。-v2 は 68:01・40:10）→ 3段の ORDER NOW → get.synocell.com の SamCart 1ページ注文フォーム → 決済（SamCart 内の Stripe 欄）

1. 広告の着地URLは振り分け用。n=3回開いて -dup 2回・-v2 1回。2本は動画の版（V4／V5）とオファーの秒（39:38／40:10）が違い、見出し・値段・コメント10件は同じ
2. 動画39:37「for just $59」の1秒後にページが3段を出す。再生しなくても開いて39:33で出る
3. ORDER NOW（3本）→ `get.synocell.com/products/syn-3-pack-syn-vslfb-dup/`。表題「Synocell 3pk JP | Synocell」、中身「SynoCell Doctor's Choice Pack」「$147.00」「Shipping Free」「Total USD $147.00」「Shipping Insurance - $2.49」、上に「Your Special Price Is Reserved For」の10分の時計、入力は Contact Information／Billing Information、隠し欄 `ad_id`、SMS の同意欄、「This order will appear as “Enclave BioActives” on your statement」、ボタン「Place Order Now」（`dia read` で読んだだけ。押していない）
4. Stripe の支払い欄の設定は `paymentMethodOrder` が card／affirm／afterpay_clearpay／klarna の順（`dia` でiframeのURLを読んだ）
5. 名前が3つに割れる: LPのドメイン thepainreport.com（表題「Pain Report」）／著作「© 2026 Vital Health」（注文フォームは「2024 VitalHealth」）／カード明細「Enclave BioActives」 `L`
6. 注文後のアップセルは判定不能（送信しないと先が見えない）。動画18節の「join our waiting list」の画面は、注文フォームを開いた時点では出ていない

### コピーする時の骨（比率は67分30秒の実測）

hook 2.0%（証言の餌＋予告4つ）→ lead 2.8%（手術の予定・zebrafish・Duke・7秒）→ 権威 0.6%→ **患者の物語 3.8%**（Walter 67歳・7年・手術の描写・34%）→ 発見の物語 5.4%（研修10時間・Celtics の予算）→ 否定列挙 4.0%（失敗3つに番号）→ **UMP 6.7%**（joint termites＝cytokines・がん／心臓／認知症まで）→ Blue Zones 5.6%→ **UMS 13.2%**（成分4つ、各成分に年号つきの研究）→ **product reveal 2.7%（29:45、全体の44%地点。名前だけなら26:48・40%）**→ 証言 2.8%→ 未来 3.3%→ 値段の枠 5.0%（$200／$300／$500）→ price drop 1.7%（$69→$59＝オファー表示）→ まとめ買い 4.2%→ 取り置き 1.9%→ 保証 2.7%→ 手順 1.4%→ クローズ1 5.4%→ **FAQ 20.3%**（10問）→ クローズ2 3.9%。冒頭の予告4つは3:06までに言うだけで中身を出さない（`W` 全文のキーワード検索: 「60-second」1回・「healthy foods」1回・「number one joint」1回・「ritual」3回、全部3:06まで）。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-160281900/sheet0.jpg`（0:00〜26:30）／`sheet1.jpg`（27:00〜53:30）／`sheet2.jpg`（54:00〜67:30）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-160281900.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-160281900/sheet0.jpg]]
![[ec/wiki/vsl-teardown/frames/LP-160281900/sheet1.jpg]]
![[ec/wiki/vsl-teardown/frames/LP-160281900/sheet2.jpg]]
