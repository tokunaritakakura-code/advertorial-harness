<!-- 例 -->
# Codie Sanchez（ビジネス買収講座）— VSL example

読む人: この型（推薦者の切り抜き型・ポッドキャスト）の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形（通話予約・点数で振り分け）を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [149860657](https://app.gethookd.ai/share/ad/149860657?signature=97b709f9a76f5445427cfe3933e3da3f3f11a9865ae8d86039e9988da4c4b780)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/149860657`）
LP: https://info.contrarianthinking.co/buy-a-cash-flowing-business-vsl4
形式: VSL・動画 74s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 HubSpot の申込VSLページ（金額なし・通話予約へ）
拾った日: 2026-09-12
稼働日数 / 成績: 23日 / score 90（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 168本（2026-09-12）
選定: 補充枠。ブランドの稼働広告数500以上で着地が実測VSLの英語ブランドは2026-09-12時点で12で尽きた。GetHookd の vsl_page 分類・勝ち・稼働中から、稼働広告数が次に多いブランドを実測で確かめて入れた（168本）。広告の尺は74秒で、既存クライテリアの3分以上を満たさない（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし／`W`=ローカルwhisper large-v3-turbo／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ）／`J`=判断

広告の文字起こしは GetHookd 側が空だったので全部 `W`（全文は `ec/wiki/vsl-teardown/raw/149860657.full.txt`、出どころの1行は `.src`）。広告の見出し「Buy a Business, Don't Start One」、本文の締め「Book a call with Codie Sanchez's team to see what it actually takes.」（`raw/149860657.json`）。

## なぜ良いのか（1行）

他人の口で「anybody has access to small business」と約束させ、広告は商品を語らず（音声に商品名 n=0）、選別はLP動画の「it's not for everybody」（0:53–0:58 の区間・1回）と「this is not for everyone」（2:05–2:09 の区間・1回）とフォームの点数3分岐に任せる。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:16 `W`「Forget that side of it, the trillionaires, billionaires.」→「What I've always admired about you, even when you were first starting out」→「anybody has access to small business.」「Anybody.」。`F` 0秒は聞き手の女性（BigDeal のマイク）、1秒で男性ゲスト（名前は音声にも字幕にも出ない）に切り替わり、以後12秒まで男性の顔アップ |
| lead | 0:16–0:25 `W`「There is no magic.」「There's no God-given talent you need.」「You just need a little help.」「You're showing them how to get there.」（才能・魔法という言い訳を消す） |
| discovery story | 無し |
| UMP | 0:44–0:51 `W`「Too many people have lost sight of the fact that, oh, I can't become a trillionaire, so I should just give up.」「You know, like what's wrong?」。**呼び名なし**（原因は「億万長者になれないなら諦める」という思い込み） |
| UMS | 0:25–0:35 `W`「you don't have to love Elon Musk or hate Elon Musk, but you can buy a car wash.」「that car wash can provide a living for you and your family.」→0:51–0:58「A donut shop, a bakery, a dry cleaning business」→1:06「Anybody can buy a business and be successful.」。**呼び名なし**（動詞 buy だけ。見出しの「Buy a Business, Don't Start One」と対） |
| product reveal | **絵だけ** 1:09–1:14 `F` 終わりの赤いカード「CONTRARIAN ACADEMY」「Want to learn how to buy a business? Click Below.」（発話なし）。音声で商品名は出ない |
| price drop | 無し |
| risk reversal | 無し |
| testimonials | 推薦者1人 `W`（顧客の声ではなく、男性ゲストが語り手を褒める形。「I think your message for America is the right message at this time.」を1:02で2回目） |

無かったブロックは「無し」。欠落そのものが発見。

## 盗む所

- 本人に売り込ませず、第三者が本人を褒める74秒の切り抜きで出す。広告の音声に商品名・値段・数字は n=0。商品名は終わりの5.1秒の赤カードに文字だけ `F`
- 字幕を2書体で切り替える。白箱のゴシックで語ごとに出す字幕（13枚中6枚）と、明朝の大字で強調語だけ置く字幕（「admired」「message」「America」、13枚中5枚が大字）`F`
- 広告は「Anybody can buy a business」、LP動画は「it's not for everybody」（0:53–0:58 の区間・1回）と「this is not for everyone」（2:05–2:09 の区間・1回）。広く呼んで、LPとフォームで削る

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。語りは男性ゲスト1人で、12秒までの画の切替は0→1秒の1回（n=13枚）。

![[ec/wiki/vsl-teardown/絵/149860657-hook]]

## 全シーン × b-roll（`F`）

尺 73.7秒 ／ 5シーン ／ 平均 14.7秒 ／ しきい値 0.25（0秒の女性→1秒の男性の切替はこのしきい値で拾えていない。同じ構図の対談カットは数が小さく出る）。b-roll は n=0。対談の2カメ（男性アップ・女性の引き）と終わりの赤カードだけ。

![[ec/wiki/vsl-teardown/シーン/149860657]]

## LP（着地ページ）— info.contrarianthinking.co/buy-a-cash-flowing-business-vsl4

**読む前に**: 金額を1つも出さない申込型のVSLページ。動画は2分15秒と短く、ボタンは読み込んだ時から見えていて、押すと点数付きのフォームで3つの行き先に振り分けられる。

| 項目 | 実測（`L`=LP、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=30秒おきの絵、`J`=判断） |
|---|---|
| URL | https://info.contrarianthinking.co/buy-a-cash-flowing-business-vsl4 （title「Learn How to Buy a Cashflowing Business」）`L` |
| 作り | HubSpot のランディングページ（HTML に `templates/partials/lp-header.hubl.html`・`lp-footer.hubl.html`、テーマのパスに elevate）＋Wistia＋Typeform。偽コメント欄は blocks n=43 の中に無い `L` |
| 動画 | Wistia `s4x4qnjn9z`、内部名「01_CTA_Apply」、134.7秒（2:15）、横16:9、2025-04-17作成。seoDescription「a VSL(3) GHL by Joe @ResponsivAgency video」。設定は autoPlay=true・playbar=true（シークバーあり）・字幕が既定でオン・CTAやフォームの plugin は無し。Wistia の累計は再生 203,184回／平均視聴率 0.17（このページ以外の埋め込みも含む数字） `L` |
| ページの部品（上から） | ①ロゴ Contrarian Thinking（y=24）②見出し「Build a LEGACY of Financial Independence by ACQUIRING PROFITABLE SMALL BUSINESSES.」＋「Without starting from scratch. Without investing millions. Without taking out huge loans.」（y=163）③動画（y=431）＋「Discover the fourth path to wealth」の段落 ④ボタン「BOOK A CALL」（y=1154）⑤見出し「I can't guarantee results. Big Brother won't allow that. But…」＋「Over 5,000 people have joined the Contrarian Academy」（y=1323）⑥Trustpilot 5つ星の画像（y=1578）⑦声のカード画像 n=15（3列×5段・y=1726〜3948。名前は William B. から Trina J. まで15人、Manuel だけイニシャル無しで他14人は名＋姓の頭文字、写真なし）⑧ボタン「BOOK MY CALL WITH THE TEAM」（y=4086）⑨免責「This is not an offer to buy a business or a franchise」＋earnings-disclaimer へのリンク ⑩フッターのロゴ `L` |
| 隠れた要素 | v=0 は n=4（h1 と video の複製・音量アイコンの button・GTM の iframe）。h1 は font-size 17px の同じ見出しで、スマホ用の複製と見る `J` |
| 売り場 | ボタン2つとも同じ Typeform `contrarianthinking.typeform.com/to/axCJB6mU`（フォーム名「Paid VSL 5」）→ 点数で OnceHub の通話予約2種か、$2,000 の講座ページへ（下の導線） `L` |
| 値段 | ページ・LP動画・フォームのどこにも金額なし（prices 抽出 n=0、本文を全部読んで確認）。フォームが聞くのは**買収に使う予算**（$0-24K／$25K-49K／$50K-99K／$100K+）で、商品の値段ではない。0〜7点の人の行き先の講座ページは FAQ に「Is the course worth $2,000?」 `L` |
| 保証 | 返金保証の文言はページ本文に出ない。出るのは「I can't guarantee results.」の否定。自動抽出の「90 days」は声の中の「close my first small laundromat deal in the next 90 days」 `L` |
| 仕掛け | 隠すオファーは無い（delay 断片 n=0、ボタン2つとも v=1 で最初から表示、Wistia に時刻付きCTAの設定なし）。代わりにフォームの点数で客を3つに割る `L` |

### 広告 → LP のつながり

| 要素 | 広告（74秒） | LP動画（2:15）・ページ | 判定 |
|---|---|---|---|
| 餌 | 「Forget that side of it, the trillionaires, billionaires.」 | 0:00「hey there cody sanchez here」で本人の自己紹介から入る | 餌は捨てる |
| 語り手 | 男性ゲストが聞き手を褒める（対談の切り抜き） | 本人1人が椅子に座って1カメで話す（`F` 4コマ全部同じ画） | 第三者から本人へ替わる |
| 原因の呼び名 | 「I can't become a trillionaire, so I should just give up」（諦め） | 「`avoid a lot of the mistakes that i made`」「doing a bad deal」（失敗の怖さ） | **原因が替わる**。どちらも呼び名なし |
| 解の呼び名 | 「you can buy a car wash」「Anybody can buy a business」 | 「buy a cash flowing business」→1:37–1:43 の区間の末尾「i call this collapsing time」。見出しは「ACQUIRING PROFITABLE SMALL BUSINESSES」 | 動詞 buy は一致。呼び名（collapsing time）はLPで初めて付く |
| 権威 | 推薦者の褒め言葉だけ（名前なし） | 「15 years in finance」「my team's knowledge who have done billions in transactions」・ページ「Over 5,000 people」 | LPで数字の権威に替わる |
| 数字 | n=0 | 15年・billions・thousands・3.5年（動画）／5,000人（ページ） | LPで初出 |
| 約束 | 「Anybody can buy a business and be successful.」 | 「it's not for everybody」（0:53–0:58 の区間・1回）、「this is not for everyone」（2:05–2:09 の区間・1回）・ページ「I can't guarantee results」 | **逆になる**（誰でも→選ぶ） |
| 商品名 | 音声 n=0。終わりの赤カードに「CONTRARIAN ACADEMY」 `F` | 動画は「community」「this program」だけで商品名 n=0。ページ⑤の本文に「Contrarian Academy」 | 名前は文字でだけ出す |
| 値段 | 無し | 無し（動画・ページ・フォーム） | 値段は通話で出す `J` |
| 行動 | 本文「Book a call with Codie Sanchez's team」 | ボタン「BOOK A CALL」・動画1:57–2:01 の区間の末尾「fill out the form below」 | 一致 |

### LP動画の構成（6節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00–0:17 | 自己紹介＋対象の名指し | 「hey there cody sanchez here」「you want to buy a cash flowing business or at least you're thinking about it」→すでに買っている人・株や債券やFXの人の3通りを名指し | 0:00 暗い木の壁の前、緑の椅子に座った女性・卓上マイク・横に本が1冊（表紙の文字は判読不能） |
| 2 | 0:17–0:38 | 機会 | 「`there are so many businesses available to buy right now`」「transition from one baby boomer generation to our generation」「i've built an entire community and a support system」 | 0:30 同じ画（手を上げる） |
| 3 | 0:38–0:48 | 時代の枠 | 「we are sitting at a generational wealth creation event」「one generation owning businesses that needs the next generation to step up」 | 同じ画 |
| 4 | 0:48–1:23 | 選別＋失敗の怖さ | 「it's not for everybody」「`avoid a lot of the mistakes that i made the headaches`」「what makes a good deal」「the worst thing possible which is doing a bad deal」→「you get personal support」 | 1:00 同じ画 |
| 5 | 1:23–1:43 | 権威＋解の呼び名 | 「borrow my knowledge for 15 years in finance」「billions in transactions」「three and a half years」「steal the mistakes that we've made」「i call this collapsing time」 | 1:30 同じ画 |
| 6 | 1:43–2:15 | CTA＋2度目の選別 | 「if you're ready to buy a business but the right way and do the work」「fill out the form below」（1:57–2:01 の区間の末尾）「if there's not it's all good」「this is not for everyone」「if it's not business buying we'll see you on the internet」 | 画は変わらない（sheet0 は n=4コマ） |

商品名が出る秒: **出ない**（「community」は0:34–0:38 の区間と0:58–1:03 の区間、「this program」は「this」が1:13–1:18 の区間の末尾・「program」が1:18–1:24 の区間の頭で区間をまたぐ。この2語だけ）。値段を言う秒: **言わない**。CTA「fill out the form below」を初めて言うのは1:57–2:01 の区間の末尾（区間の始まり1:57.5は87%地点）。

### 売り場までの導線

ファネル: 広告（74秒）→ LP（Wistia 2:15・ボタンは最初から表示で隠す秒なし）→ Typeform（4問・点数で3分岐）→ 14点以上は OnceHub 30分Zoom／8〜13点は OnceHub 15分電話／7点以下は $2,000 の講座ページ → 決済（通話の後。ページ上に決済なし `J`）

1. ページのボタン2つ（y=1154・4086）は同じ Typeform。開くと「Let's get you on your way to buying your first business.」「Takes 30 sec」`L`
2. 質問は4問: ①名前・姓・電話・メール ②買収の予算（$0-24K=1点／$25K-49K=2点／$50K-99K=7点／$100K+=10点）③時期（Sometime later=4点／Within 1 year=6点／I'm already looking=8点）④どこで知ったか（自由記入）`L`
3. 点数の行き先（フォームの logic を読んだ）: 0〜7点「Dreamers」→ `contrarianthinking.co/acquisition-foundations/`（講座ページ）／8〜13点「Explorers」→ `oncehub.com/CTintroductionvsl`（Contrarian Academy Introduction・15分・Phone、Host will call you）／14〜18点「Action Takers」→ `oncehub.com/CTconsultationvsl`（Contrarian Academy Consultation・30分・Zoom）`L`
4. 予算×時期の組み合わせ n=12 で数えると、Dreamers 3／Explorers 5／Action Takers 4。予算 $100K+ は時期に関係なく全部 Action Takers、$0-24K は「already looking」の時だけ Explorers に上がる `J`
5. Dreamers の行き先の講座ページ（Acquisition Foundations・10ユニット）は「START NOW」→ `/acquisition-foundations-checkout`。この決済ページを読んだ時点で金額の文字も決済フォームも出ていない（iframe・form を列挙して Trustpilot の iframe n=1 だけ）ので、決済の場所は判定不能。講座ページの FAQ に「$2,000」と「credit you $2,000 towards the Contrarian Academy」`L`
6. 本命の Contrarian Academy の値段と決済場所は、ページ・動画・フォーム・予約ページのどこにも出ないので取得失敗（通話の中で出す物と見る `J`）

### コピーする時の骨（比率は2:15の実測）

自己紹介＋対象の名指し 12.5%→ 機会 15.9%→ 時代の枠 7.5%→ **選別＋失敗の怖さ 26.1%**→ 権威＋解の呼び名 14.9%→ **CTA＋2度目の選別 23.0%**。商品名・値段・保証・証言の節は動画に無く、証言はページの声カード15枚、選別はフォームの点数が持つ。広告は第三者の推薦だけで作り、商品の説明を1秒も入れない。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-149860657/sheet0.jpg`（0:00〜1:30・4コマ）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-149860657.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-149860657/sheet0.jpg]]
