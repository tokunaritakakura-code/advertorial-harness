<!-- 例 -->
# Alex Hormozi（マーケティングワークショップ）— VSL example

読む人: この型（創業者・通話予約型）の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [144479583](https://app.gethookd.ai/share/ad/144479583?signature=948293aa23e5f50d11f754eb5796630fb985f4d99dc9cef7860c1fb055ae1da0)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/144479583`）
LP: https://www.acquisition.com/workshop-marketing
形式: VSL・動画 85s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 通話予約つきのVSLページ（動画4:16＋iclosed予約枠）
拾った日: 2026-09-12
稼働日数 / 成績: 32日 / score 86（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 789本（2026-09-12）
選定: GetHookd で「勝ち（score 81〜100）・稼働中・動画」かつブランドの稼働広告数500以上。着地が実測でVSL（長尺の売り動画が主役のページ）。広告の尺は85秒で、既存クライテリアの3分以上を満たさない（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし（この本は空で未使用）／`W`=ローカルwhisper large-v3-turbo（全文は `ec/wiki/vsl-teardown/raw/144479583.full.txt`）／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ）／`J`=判断

## なぜ良いのか（1行）

85秒の中で商品名も値段も言わず、「No one knows you exist.」の断言と3択の列挙だけで「Book, click, call」に送る。値段$5k はLPのFAQの文字だけに預ける。資格と残席は広告本文「doing $1m+ a year」とLP動画3:06「this is for million-dollar-plus business owners」でも言う。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00〜0:20 `W`「No one knows you exist.」「And so the answer is you have to advertise more.」→「100 reach outs a day」「100 minutes of making content」「100 minutes a day of making paid ads」→「pick one」（`F` 紫背景のスタジオ・机に開いた本・画面に「100 reach outs/day」＋絵文字4つ。0:00〜0:20.7 の7シーン） |
| lead | 0:20〜0:47 `W`「If your ads and your content are not performing the way you want them to, I don't know what the problem is, but I can tell you what we're doing that is working.」（`F` 0:20.7 から屋外の自撮りに切り替わる。鼻にテープ・後ろ向きの帽子・紫の箱の字幕。2本継ぎ） |
| discovery story | 無し |
| UMP | 0:27〜0:47 `W`「it's not just branding, it's not just content, and it's not just ads. You have to do all three.」→「how do you do all three in a way that is operationally efficient?」「a 20-person marketing department for a 40-person company? It doesn't work, right?」。原因に自分の呼び名なし |
| UMS | 0:27／0:48 `W`「layered strategy」＋「leverage AI right now in 2026 in our marketing」「I just finished the stuff and it's fire.」 |
| product reveal | 無し（音声は「`I can't think of a better thing than this to come to`」(1:04)「I'll see you here in Vegas」(1:16) だけ。名前は広告本文「We finally launched a marketing workshop. A whole new 2-day experience here in Vegas.」） |
| price drop | 無し（本文は資格「If you're a business owner doing $1m+ a year」だけ） |
| risk reversal | 無し（1:20「And if not, keep rocking and rolling. I'm rooting for you either way.」は保証でなく押しを外す一言） |
| testimonials | 無し（音声0人。本文に「The last marketing workshop sold out in 12 hours」の数だけ） |

無かったブロックは「無し」。欠落そのものが発見。

## 盗む所

- 0秒を状況の断言1文（「No one knows you exist.」5語）で取り、次の20秒で選択肢を同じ数字「100」で3つ並べる。画面は数字だけ大きく、横に絵文字を3〜4個
- LP動画で権威を人数でなく1人あたりの数字で出す「one editor is managing and it does 140 longs per week. That's 20 a day. One guy.」「one editor who made 369 paid ads last week. Video ads, not statics.」
- 値段は動画で言わず、ページのFAQで資格と一緒に出す「Tickets are $5k per seat.」「If you haven't made at least $5k from the free content, don't do it.」＋日程4つ中3つを「SOLD OUT／0 SEATS LEFT」で見せる

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。字幕は0s だけ無く、1s〜12s は1〜4語ずつ出る（n=13コマ中12）。

![[ec/wiki/vsl-teardown/絵/144479583-hook]]

## 全シーン × b-roll（`F`）

尺 84.5秒 ／ 11シーン ／ 平均 7.7秒 ／ しきい値 0.25（スタジオ7シーン 0〜20.7秒、屋外の自撮り4シーン 20.7〜84.5秒。最長は s007 の32.4秒）

![[ec/wiki/vsl-teardown/シーン/144479583]]

## LP（着地ページ）— acquisition.com/workshop-marketing

**読む前に**: 動画4:16は隠す物が無く、ボタンは0秒から動画の直下にある。4本のボタン（y0／y622／y3710／y5893）は全部同じページの予約枠（iclosed）へ飛び、決済の入口はページに無い。

| 項目 | 実測（`L`=LP、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=30秒おきの絵） |
|---|---|
| URL | https://www.acquisition.com/workshop-marketing （最終URLも同じ。`L`） |
| 作り | Next.js にHubSpotのページ部品を流し込み（`hs-content-id`・テンプレ「Acquisition_September2022」）＋予約はiclosed埋め込み。Shopifyではない。偽コメント欄は無い `L` |
| 動画 | Vidalytics（アカウント 8Okpkhqb・embed fJ7wBRNTmIufpm1N・内部名「vsl_v6」）。4分16秒（player.duration=256）。自動再生あり（画面は「Click To Unmute」）・**シークバーあり**・再生時間表示あり・速度変更あり・resume=false・redirect.show=false・chapters=false（`curl player.settings.json`） |
| ページの部品（上から・blocks n=75） | ①帯「LIVE NEW MARKETING WORKSHOP \| LAS VEGAS \|SEP 30 - OCT 1」（→#booking-widget）②h1「IS YOUR MARKETING THE THING LIMITING YOUR BUSINESS?」③h2「Join our first ever Marketing Workshop - Build a Consistent Marketing Engine with the help of AI.」④動画（y244）⑤「BOOK MY CALL」（y622）⑥h2「What people are saying about our past workshops」＋証言動画6本（Vidalytics・y854／1156）⑦Googleレビュー体裁5件（屋根屋・メドスパ・法律事務所「`I learned more in these two days than I did during my entire MBA program`」・$2M建設・Local Guide。本物か検証していない）⑧iclosed予約枠（y2365・540×620）⑨h2「UPCOMING MARKETING WORKSHOPS IN LAS VEGAS」「cap at 100 founders. Seats tend to fill around 60 days out」＋日程4つ（AUG 14／SEPT 18／SEP 30 が SOLD OUT・OCT 28 が OPEN）⑩「BOOK MY CALL →」（y3710）⑪FAQ4問（2日で何をするか／何を持ち帰るか「3-5 tactical next steps」「which of the 5 links is actually leaking」／規模と業種「under $1M/yr this is not a fit (yet.)」業種17個／値段「$5k per seat」）⑫「I'M READY TO GROW」（y5893）⑬免責「results are not typical」 |
| 売り場 | 同じページの iclosed 予約枠 → 電話番号・First name・Last name の3欄（メール欄なし）→ 通話枠のカレンダー。**決済の入口はページにも予約枠にも無い** `L` |
| 値段 | **$5k/席の1択**（FAQの文字だけ。動画は値段を言わない）。資格 年商$1M〜$100M。講師側の年俸「$350k, $600k, $900k+ per year」を値段の理由に置く |
| 保証 | 返金保証の記載なし（見えている本文 text で refund／money back は0語。guarantee は2回あるが、どちらもフッターの免責文「are not a guarantee of your success」「We cannot guarantee that you will make money」で返金保証ではない） |
| 仕掛け | 隠す秒なし（delay 断片 n=0・Vidalytics の redirect なし・ボタン⑤は読み込み時点で v=1）。タイマーなし。残席は「0 SEATS LEFT」×3 と上の帯の SEP 30 が同じページで食い違う（帯は告知、日程欄は SOLD OUT） |

### 広告 → LP のつながり

| 要素 | 広告（85秒） | LP動画・ページ | 判定 |
|---|---|---|---|
| 餌（冒頭） | 0:00「No one knows you exist.」 | 動画0:00「If you're not getting as many leads as you want and your business is demand-constraining」 | 冒頭は引き継がない。広告0:57の行「If you are not getting the amount of leads that you want」がLPの0秒に来る |
| 原因の呼び名 | 「You have to do all three」「20-person marketing department for a 40-person company」 | 動画3:52「Social media became interest media. Andromeda became personalized… AI has given more leverage」／ページ「which of the 5 links is actually leaking」 | **呼び名が変わる**（3本柱→3つの変化／5 links）。広告の見出し「Learn Where Your Marketing Is Leaking」はページの「leaking」と一致 |
| 解の呼び名 | 「layered strategy」「leverage AI」 | 動画0:58「how we scale our marketing using AI」3:46「this is the flywheel」／h2「Consistent Marketing Engine」 | AIは一致。呼び名はLPで2つ足される |
| 権威 | 1:08「`we spend a lot of money across our company and obviously our portfolio companies`」 | 動画0:11「we also build custom software」＋director 3人（140 longs/週・369 paid ads/週）／ページ 年俸$350k〜$900k | LPで数字が付く |
| 数字 | 100×3・20人／40人 | 140・20 a day・369（動画）／$5k・100 founders・$1M〜$100M（ページ） | 広告の数字はLPに1つも出ない |
| 約束 | 1:14「Just get the answers.」 | 動画1:39「You're probably not going to adopt my entire system overnight」／ページ「3-5 tactical next steps」 | LPで約束を小さくする |
| 商品名 | 音声で0回。本文「marketing workshop」「2-day」「Vegas」 | 動画0:22「marketing workshop」0:50「our first ever marketing workshop in Vegas」 | 本文とLP動画で一致 |
| 値段 | 無し | 動画で0回／ページFAQ「$5k per seat」 | 値段はページ下部の文字だけ |
| 希少性 | 本文「The last marketing workshop sold out in 12 hours」 | 動画3:13「it's the first time we've done it」／h2「first ever」 | **食い違う**（本文は前回があった、LPは初回） |
| 時期 | 本文「marketing has changed so much in the last 18 months」 | 動画0:35「in the last 12 months」 | 月数が18→12にずれる |

### LP動画の構成（13節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00〜0:08 | 呼びかけ（誰向け） | 「If you're not getting as many leads as you want and your business is demand-constraining, meaning you could service more customers than you currently have, then this is for you.」 | 屋外の自撮り（以下全節同じ） |
| 2 | 0:08〜0:23 | 権威とコスト | 「ACQ tends to be on the bleeding edge」「we also build custom software and we pay amazing vendors and very expensive people」「open kimono style」 | 字幕「BUILD CUSTOM SOFTWARE AND WE」 |
| 3 | 0:23〜0:55 | 今やる理由2つ＋招待（商品名） | 「I didn't want the brand of a marketer」「marketing has changed so much in the last 12 months」「you will like us more」→「two days to our first ever marketing workshop in Vegas」 | 字幕「I THOUGHT IF I WERE TO SHOW」 |
| 4 | 0:55〜1:39 | 1日目の中身 | 「how we scale our marketing using AI」「how we measure ROI and attribute sales across platforms」「how we pick content topics」「how we structure our teams」「if you don't have a personal brand…」「leverage it with paid ads」 | 字幕「WE MAKE STUFF THAT GETS」 |
| 5 | 1:39〜1:54 | 期待を下げる | 「You're probably not going to adopt my entire system overnight」「The most important thing is that you actually get something out that you can apply」 | 字幕「BECAUSE YOU DON'T HAVE THE」 |
| 6 | 1:54〜2:42 | 2日目の中身＋director の数字 | 「breaking up into small groups」「director of longs… 140 longs per week. That's 20 a day. One guy.」「director of paid… 369 paid ads last week」「director of content… local… national… international」 | 字幕「DIRECTOR OF PAID WHO WILL」 |
| 7 | 2:42〜3:06 | 小グループの理由 | 「grouped by revenue, ends up being more valuable. At least that's what our surveys tell us」「almost like getting a one-on-one all day」 | 字幕「ON ONE AND IT KIND」 |
| 8 | 3:06〜3:20 | 資格と希少性 | 「this is for million-dollar-plus business owners」「always sold out a few months in advance」「it'll probably sell out a little faster since it's the first time」 | 字幕「PROBABLY SELL OUT A LITTLE」 | <!-- 掘った: LP動画の逐語 W。`raw/LP-144479583.segments.json` の186.0〜200.5秒で照合 -->
| 9 | 3:20〜3:29 | 払ったコストを渡す | 「`we'll just give it to you without the trial and error and the millions of dollars spent`」「fill up your bucket under the spigot of leads」 | 自撮り |
| 10 | 3:29〜3:34 | CTA1 | 「if you want in, you can book a call below. It's going to be sick.」 | 自撮り |
| 11 | 3:34〜3:52 | 業種の広さ | 「which don't have personal risk」「software, brick and mortar, professional services, healthcare services, home services」 | 字幕「SERVICES HOME SERVICES IF」 |
| 12 | 3:52〜4:11 | 今が時期の理由（3つの変化） | 「Social media became interest media. Andromeda became personalized and required more volume at scale on the ad side. And AI has given more leverage to creating media」「this is a magical moment for marketing」 | 自撮り |
| 13 | 4:11〜4:16 | CTA2 | 「boy, do I have the thing for you. Click below, book call, and hopefully I'll see you in Vegas.」 | 字幕「YOU IN VEGAS」 |

商品名が初めて出る秒: 0:22.8（「marketing workshop」・256秒の9%）。値段を言う秒: 動画内で0回（`W` で「$」「price」「ticket」「5k」を検索して0件）。絵: sheet0 のコマ9枚は全部同じ自撮りの屋外歩き（スライド・b-roll・商品の絵は0枚）。字幕との照合で、コマは0:15から30秒おき（0:15, 0:45…4:15）。広告の屋外部分は鼻にテープ・曇り空（4シーン中4）、LP動画は鼻テープなし・晴れ（9コマ中9）で、別の日の撮影 `F`。

### 売り場までの導線

ファネル: 広告（85秒）→ LP（動画4:16・オファーは隠さない、ボタンは0秒から y622）→ 同じページの iclosed 予約枠（電話番号＋姓名）→ 通話枠の予約 → 決済（ページと予約枠に入口なし。通話の先で取得不能）

1. ボタンは4本（上の帯・BOOK MY CALL×2・I'M READY TO GROW）で、href は4本とも `#booking-widget`。別ページに出ない `L`
2. 予約枠 `app.iclosed.io/e/Acquisition/acq-marketing-workshop-meeting` の文言は「ACQ Marketing Workshop Meeting」「Excited to speak with you for our in-person scaling workshop. Book a call below to see if you are a fit.」。マーケの枠なのに「scaling workshop」のまま `L`
3. 入力は電話番号・First name・Last name の3欄＋reCAPTCHA。カレンダーは「Please fill out the form before choosing your time slot.」で入力前は押せない。9月の30日のうち disabled でない日は12〜15日の4日 `L`（クリック・入力はしていない）
4. 動画のCTAは2回（3:29「book a call below」／4:11「Click below, book call」）で、どちらも直下のボタン⑤を指す
5. 値段$5k はFAQ4問目の文字だけ。動画→ボタン→予約枠のどこでも金額は出ない

### コピーする時の骨（比率は4分16秒の実測）

呼びかけ 3%（リード不足の人だけ呼ぶ）→ 権威とコスト 6% → 今やる理由2つ＋招待 13%（商品名は9%地点）→ **1日目の中身 17%**（how we scale／measure／pick／make／structure の5本＋how to then scale の1本）→ 期待を下げる 6% → **2日目＋director の数字 19%**（1人あたり140本・369本）→ 小グループの理由 9% → 資格と希少性 6% → 払ったコスト 3% → CTA1 2% → 業種 7% → 3つの変化 7% → CTA2 2%。サプリのVSLにある物語・UMPの喩え・値段の段・保証・FAQの読み上げは0節で、値段（$5k）はページの文字だけが担い、資格と残席は動画の3:06〜3:20（6%）でも言う。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-144479583/sheet0.jpg`（9コマ・0:15〜4:15）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-144479583.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-144479583/sheet0.jpg]]
