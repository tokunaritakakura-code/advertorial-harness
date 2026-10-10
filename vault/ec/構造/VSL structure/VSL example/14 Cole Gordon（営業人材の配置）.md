<!-- 例 -->
# Cole Gordon（営業人材の配置）— VSL example

読む人: この型（追いかけ型・見たのに予約しなかった人へ）の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [133444732](https://app.gethookd.ai/share/ad/133444732?signature=a535d2a9c15f64a16aaa9ffc5c851ab076856ece68c4c2b90b38b57477e1c43a)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/133444732`）
LP: https://g.closers.io/vsl?utm_term=aaid_d412d8f6-d083-433a-a318-d09a63fbc960
形式: VSL・動画 114s・US・Facebook／Instagram・着地 通話予約のVSLページ（見出し＋動画3分49秒＋ボタン1個。値段なし）
拾った日: 2026-09-12
稼働日数 / 成績: 39日 / score 90（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 812本（2026-09-12）
選定: GetHookd で「勝ち（score 81〜100）・稼働中・動画」かつブランドの稼働広告数500以上。着地が実測でVSL（長尺の売り動画が主役のページ）。広告の尺は114秒で、既存クライテリアの3分以上を満たさない（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `W`=ローカルwhisper large-v3-turbo（GetHookd の文字起こしが空。全文は `ec/wiki/vsl-teardown/raw/133444732.full.txt`）／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ）／`J`=判断。whisper の聞き違いは画面の名札で直した（「Hilarik Heck」→ALERICK HECK、「Rick Castillo」→BROOKE CASTILLO、「Ryan Serhan」→RYAN SERHANT、LP の「Rostrofino」→RUSS RUFFINO）

## なぜ良いのか（1行）

予約しなかった人に「So this is a little weird, huh?」で話しかけ、頼みを「Not necessarily work with us, but just at least book a call」まで下げ、114秒を「通話を予約する理由3つ」だけに使う。売り物の説明は前の広告とLPに預けている。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:22 `W`「So this is a little weird, huh? You saw one of our ads about us being able to place a setter or closer in your business or you don't pay, but you decided not to book a call, which I get it」→「in the next 60 seconds, I don't want to just give you three reasons why you should definitely book a call」（`F` 柄シャツの男の自撮り顔アップ。上に黄字の帯「DRIVE SALES WITH OUR APPOINTMENT SETTERS」、下に2行字幕） |
| lead | 0:19–0:22 `W`「Not necessarily work with us, but just at least book a call to see what we have to say」（契約ではなく通話だけを頼む） |
| discovery story | 無し |
| UMP | 無し（客の痛みの原因は語らない）。近い物は 1:08–1:15 `W`「`A lot of people pitch like a strategy call and they jump on and they just pitch a bunch of stuff`」（よその通話の問題） |
| UMS | 1:13 `W`「We call it an implementation call」→「the next six to 10 steps that you're going to take over the next 12 to 18 months」（呼び名あり＝implementation call） |
| product reveal | 無し（0:03–0:10 で前の広告の約束「place a setter or closer in your business or you don't pay」を振り返るだけ。社名も0回） |
| price drop | 無し |
| risk reversal | あり（通話の保証）1:39–1:51 `W`「If we can help you out, cool… If not, you will at the very least leave the call with an action plan」＋0:06–0:10「or you don't pay」の振り返り |
| testimonials | 数だけ `W`「4,000 other coaches, consultants, agencies」＋名札つきの顔9枚（`F` s002〜s010: DEAN GRAZIOSI／ALERICK HECK／TODD BROWN／JEFF LERNER／TANNER CHIDESTER／CLIENTS & COMMUNITY／JOEL KAPLAN／BROOKE CASTILLO／RYAN SERHANT）。本人の声は0人 |

表の外: 理由1（0:22–0:40）は顧客名10、理由2（0:41–1:05）は自社の実績 `W`「we scaled our own company from zero to $3.5 million per month in 26 months. No other company has done that, not even close」「five different eight figure sales teams」、理由3（1:05–1:35）は通話の中身、締め（1:35–1:54）はリンクを2回指す。逐語は1:35「click the link somewhere on this page」と1:51「click the link somewhere on the page」で、一致は1回、2回目は1語違う（this→the）。「in the next 60 seconds」と言って、理由3つに実測72秒（0:22–1:35）使う。

## 盗む所

- 見送った人だけに効く1行目「You saw one of our ads… but you decided not to book a call, which I get it」。2本目の広告は売り物を説明し直さず、予約の理由3つ（顧客名・自社の数字・通話の中身）だけで114秒
- 頼みを下げて、断っても持ち帰れる物を言う「Not necessarily work with us」「you will at the very least leave the call with an action plan」
- 通話に呼び名を付けて、よその通話と1文で並べる「pitch like a strategy call」対「We call it an implementation call」

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。シーン検出（しきい値0.25）では0.0–12.75秒が1シーン。13枚とも手持ちの自撮り顔アップで、コマごとに顔の向きと背景（壁・天井の照明）が動く。

![[ec/wiki/vsl-teardown/絵/133444732-hook]]

## 全シーン × b-roll（`F`）

尺 114.0秒 ／ 13シーン ／ 平均 8.8秒 ／ しきい値 0.25（シーン数はしきい値に依存）

13シーンのうち s002〜s010 の9つ（26.99–36.9秒・1つ0.63〜2.67秒）が顧客の顔＋名札。s012 は 39.21–113.96秒の74.75秒で1シーン扱いだが、ローカルmp4から切った7コマ（42／55／68／80／92／104／112秒）では、42秒=証言動画の格子に「4,000 OTHER AGENCIES」、55〜92秒=話者の顔アップ（字幕「FIVE SEPARATE」「THIS CALL IS VERY DIFFERENT」「BUT ALSO THE NEXT SIX TO TEN STEPS」）、104・112秒=下に「CLICK THE BUTTON TO LEARN MORE」＋右上に「CLICK NOW!」。同じ部屋の飛ばし切りがしきい値0.25に掛かっていない `J`。黄字の帯は見た33コマ全部に出ている。

![[ec/wiki/vsl-teardown/シーン/133444732]]

## LP（着地ページ）— g.closers.io/vsl

**読む前に**: ここは物を買わせるページではなく、通話の予約を取るページ。値段はページにも動画にも出ない（page json の prices=[]、LP動画229秒の逐語でオファーの値段は0回。$が付くのは客の単価「$2,500 or more」と実績の数字だけ）。

| 項目 | 実測（`L`=LPページ、`W`=LP動画の文字起こし・whisper、`F`=LP動画の絵） |
|---|---|
| URL | https://g.closers.io/vsl?utm_term=aaid_d412d8f6-d083-433a-a318-d09a63fbc960（title「STA Video Page」）`L` |
| 作り | ClickFunnels（classic）`L`。本文に `#cfAR`・`elHeadline`・`elButton` のクラス。ほかに HubSpot の hutk 取得スクリプト、AdRoll ピクセル、サーバー側GTM（load.ss.closers.io）。builder 検出には typeform と next/ の文字列も出たが、本文中の用途は判定不能 |
| 動画 | Vidalytics（アカウント l1U2cmHM・embed Kn5xpCfcwSKVeryO）・3分49秒（player.duration=229）・内部名「New STA Setter VSL - Cole - Short VSL High-Edits - 1.15x Speed」。`player.settings.json`: 自動再生あり（onlyMuted=false、上に「Your Video Is Playing / Click To Unmute」）／シークバーあり（mode=rapidEngage・desktopSpeed/mobileSpeed=1.25）／再生時間表示なし（playbackTimer.show=false）／速度変更あり／途中再開なし（resume=false）／CTA の設定項目なし |
| ページの部品（上から） | ①見出し「Give Us 7 Days, And We'll Place A Proven Appointment Setter Or Closer Into Your Coaching Or Agency Business.」「If They Don't Book 40 Sales Calls In The First Month - You Don't Pay!*」②動画（y=193）③赤いボタン「Schedule Demo」（y=811・読み込み時から v=1。JSで作るボタンで href なし）④フッター（y=1309〜1472: Home／Our Process／Success Stories／Blog のナビ、Privacy・Terms・DMCA・Full Disclosure・*Refund Guarantee、免責文、住所 Scottsdale AZ）⑤初回訪問だけ出るクッキー同意の枠（localStorage の first-visit）。隠れ（v=0）は同じ「Schedule Demo」2個とナビ1組。証言・値段表・FAQ・コメント欄は text に無い |
| 売り場 | 決済なし。ボタン → 同じページの上に SalesKick のポップアップ（iframe `https://app.saleskick.com/form-veVQt3WBMER83mDTDkeEW3/form-mlqxg17e`・Powered by Unthread）→ 申込フォーム。`dia read` で見えた1問目「Do You Specifically Have A Product OR Service Based Business With A Price Point Of $2500 or More?」「If not - STOP AND LEAVE THIS PAGE IMMEDIATELY.」（A Yes／B No）。2問目以降と予約画面は回答しないと出ないため未確認 |
| 値段 | 無し。比較だけ `W`「done-for-you sales agency that's going to charge 25 to 30% revenue share, our fees are much less」 |
| 保証 | 日数なし。見出し「40 Sales Calls In The First Month」＋動画「if they don't perform, you don't pay」。条件は *Refund Guarantee ページ（`L`・Last Updated October 17, 2024）: closer なら1日5件以上の新規商談と成約率20%超、setter なら月600件以上の新規リードと1日2件以上の予約。そのうえ「4 different setters or 4 different closers」が全員不発で、1on1 6回・通話レビュー2回・毎日の会議・日報をこなしたら全額返金 |
| 仕掛け | 隠す物なし（delay 断片0件・Vidalytics に CTA 設定なし・ボタンは0秒から表示）。動画は再生時間を出さない。申込の1問目で客単価$2,500未満を帰す |

### 広告 → LP のつながり

| 要素 | 広告（1分54秒） | LP動画（3分49秒）・ページ | 判定 |
|---|---|---|---|
| 餌 | 「You saw one of our ads… but you decided not to book a call」 | 0:00「Give me seven days and I'll place a proven appointment setter or closer inside of your business」 | 餌は引き継がない。LPは前の広告の約束から始める |
| 約束 | 「place a setter or closer in your business or you don't pay」 | 動画「if they don't perform, you don't pay」＋見出し「7 Days」「40 Sales Calls In The First Month」 | 一致。数字（7日・40件）はLPで足す |
| 通話の呼び名 | 「implementation call」 | 動画「book a demo」、ボタン「Schedule Demo」、ポップアップ用の見出し文「100% Free Demo Call」（隠れ） | **呼び名が変わる**（implementation call は広告だけ） |
| 権威（顧客名） | 10名（Tony Robbins／Dean Graziosi／Alerick Heck／Todd Brown／Jeff Lerner／Tanner Chidester／Clients & Community／Joel Kaplan／Brooke Castillo／Ryan Serhant） | 12名（Tony Robbins／Solar Exclusive／Frank Kern／Dean Graziosi／Jay Abraham／Ryan Serhant／Agora Financial／Russ Ruffino／Brooke Castillo／Rich Sheffern／Pete Vargas／Pedro Deo。後ろ3つは whisper の綴り） | 重なるのは4名（Tony Robbins／Dean Graziosi／Brooke Castillo／Ryan Serhant） |
| 数字（顧客数） | 「4,000 other coaches, consultants, agencies」 | 「among 2,000 plus others in the past five years」 | **食い違う**。広告本文（`raw/133444732.json` の body）は「450 more sales teams in the past 2 years」で3通り |
| 数字（自社の実績） | 「zero to $3.5 million per month in 26 months」 | 「about $5.5 million a month cash and almost $8 million rev contracted just last month」（3社合計） | **食い違う**。広告本文は「0 → 2.2M in 18 months」 |
| 商品名 | 言わない（社名0回） | 1:07「at Closer.io」（whisper。画面のロゴは CLOSERS.io） | LPで初めて社名 |
| 値段 | 無し | 無し | 両方とも言わない |
| 話し手 | 柄シャツの男の自撮り・事務所の中 | 黒シャツ（CLOSERS.io のロゴ）の男・本棚の前 | 見た目が違い、どちらも名乗らない（同一人物かは判定不能）。広告本文の署名は「-Cole」、LP動画の内部名に「Cole」 |

### LP動画の構成（9節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00–0:15 | オファーの1文＋対象の絞り | 「Give me seven days and I'll place a proven appointment setter or closer inside of your business and if they don't perform, you don't pay」「specifically for online service-based businesses… who sell at $2,500 or more」 | 本棚の前の話者＋黄字「GIVE ME SEVEN DAYS」（0秒）→黒地に「YOU DON'T PAY」（5秒） |
| 2 | 0:15–0:35 | 予告＋顧客名 | 「this video is going to cover two things. First, how the offer actually works and second, why the offer works so well」→顧客名12（Agora Financial は「$1.5 billion a year」つき）「among 2,000 plus others in the past five years」 | 黒地「TWO THINGS」（0:15）→顧客の顔に名札「RUSS RUFFINO」（0:30） |
| 3 | 0:35–1:07 | 自社の実績 | 「we practice what we preach」「three portfolio companies」「about $5.5 million a month cash and almost $8 million rev contracted just last month. Not last year, just last month」「no other recruiting company can say that not even close」 | 黒地「B2B & B2C MARKETS」（0:45） |
| 4 | 1:07–1:58 | 結果1: 7日で配置 | 「within seven days of onboarding」「about 3,500 people each month who apply」「a database of over 300,000 sales reps」「three to five candidates within three to five days」→setter と closer の使い分け | 左に文字の板「#1 - We'll Place A Proven Appointment Setter Or Closers In Your Business Within 7 Days…」右に話者（1:15）／板「This means if you need more sales calls…」（1:45） |
| 5 | 1:58–2:19 | 結果2: 立ち上げを14日に | 「30 to 45 days, really sometimes 90 days to ramp a salesperson into KPI」→「twice as fast. So 14 days」 | 板「#3 - We can help you systematize sales management and leadership.」（2:15。話より2秒先に次の板） |
| 6 | 2:19–2:44 | 結果3: 営業管理の仕組み化 | 「systematize sales management and leadership」「an automatic selling machine」「We can even place a VP of sales or a sales director」 | 同じ板の構図 |
| 7 | 2:44–3:08 | 社内に置く比較 | 「done-for-you sales agency that's going to charge 25 to 30% revenue share, our fees are much less」「they're really holding the keys to your castle」 | 板「So opposed to creating a dependency on a DFY sales agency that generally charges 25-30% revenue share…」（2:45） |
| 8 | 3:08–3:17 | 保証 | 「we guarantee those results. So if we place you with somebody that doesn't form, you don't pay」「You got to qualify for the guarantee. We'll cover more on that later」（この後の逐語に条件の説明は0回） | 板「We GUARANTEE those results…」（3:15） |
| 9 | 3:17–3:49 | CTA | 「click the schedule demo button below. You're going to fill out a five-question application」「It's not like a high-pressure sales call」「I guarantee it's going to be one of the best sales conversations you've ever had」「click the button below, schedule a call」 | 話者＋「CLICK THE BUTTON TO BOOK A DEMO」＋右上「CLICK NOW!」（3:45） |

商品名が初めて出る秒: 1:07（29%）で社名「Closer.io」。値段を初めて言う秒: 言わない（229秒の逐語でオファーの値段0回）。sheet0 のコマの秒は、1コマ目「TWO THINGS」と話（0:14）、2コマ目「B2B & B2C MARKETS」と話（0:42）が合うので 0:15 から30秒刻みの8コマ（n=8、全コマで板の文と話が一致）。0秒と5秒の絵は mp4 から切って見た。

### 売り場までの導線

ファネル: 広告（1:54・前の広告を見て予約しなかった人向けの言葉）→ LP（Vidalytics 3:49・オファー表示は隠さず0秒からボタン）→「Schedule Demo」→ 同ページのポップアップで SalesKick の申込（動画は「five-question application」、実測は1問目まで）→ 通話予約（動画「forwarded to book a demo」、予約画面は未確認）→ 通話で成約（決済の場所はページに無く判定不能）

1. 広告の言い方は1:35「click the link somewhere on this page」と1:51「click the link somewhere on the page」（2回目は this→the の1語違い）、画面は「CLICK THE BUTTON TO LEARN MORE」（104秒・112秒のコマ）
2. LPは見出し→動画→ボタンの3部品だけ。ボタンは動画を再生しなくても最初から押せる（y=811・v=1）
3. ボタンに href は無い（JSで作るボタン）。押すと SalesKick の iframe（`app.saleskick.com/form-veVQt3WBMER83mDTDkeEW3/form-mlqxg17e`）が同じページの上に開く
4. 申込の1問目で「$2500 or More」でなければ「STOP AND LEAVE THIS PAGE IMMEDIATELY」。客単価で足切りしてから通話に回す
5. 保証の条件（4人入れ替えて全員不発・1on1 6回ほか）はページ下の小さなリンク「*Refund Guarantee」の先だけにあり、動画は「We'll cover more on that later」と言ったまま3:49で終わる

### コピーする時の骨（比率は3分49秒の実測）

オファーの1文＋足切り 7%→ 予告＋顧客名 9%→ 自社の実績 14%→ **結果1 配置 22%**（応募3,500人/月・名簿30万人・3〜5日で3〜5人）→ 結果2 立ち上げ 9%（30〜90日→14日）→ 結果3 仕組み化 11%→ 社内に置く比較 10%（手数料25〜30%と並べる）→ 保証 4%→ CTA 14%（5問の申込・「not like a high-pressure sales call」）。痛み・原因・物語・値段・証言の声・FAQ の節は0。広告（114秒）が「予約しなかった理由を潰す3つ」を持ち、LP動画がオファーの中身（結果3つ）を持つ分業 `J`。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-133444732/sheet0.jpg`（8コマ・0:15〜3:45）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-133444732.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-133444732/sheet0.jpg]]
