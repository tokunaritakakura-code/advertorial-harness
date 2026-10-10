<!-- 例 -->
# Ecom Accelerator（EC店舗の運営代行）— VSL example

読む人: この型（資金の名指し型（If you're sitting on $X））の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [151789982](https://app.gethookd.ai/share/ad/151789982?signature=bb303ef6eab3cc57b7399ce8b73ce277f52624301d34c4b8decc4dbaf533ee3f)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/151789982`）
LP: https://go.ecomaccelerator.io/fb/vsl
形式: VSL・動画 646s・US・Facebook／Instagram・着地 動画＋申込フォーム（Typeform）が1枚に乗ったページ。決済欄は無く、通話予約へ送る
拾った日: 2026-09-12
稼働日数 / 成績: 23日 / score 96（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 98本（2026-09-12）
選定: 補充枠。ブランドの稼働広告数500以上で着地が実測VSLの英語ブランドは2026-09-12時点で12で尽きた。GetHookd の vsl_page 分類・勝ち・稼働中から、稼働広告数が次に多いブランドを実測で確かめて入れた（98本）（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし（この本は空）／`W`=ローカルwhisper large-v3-turbo（1回目は同じ行の繰り返しになり `-mc 0 -sns` で取り直し。全文は `ec/wiki/vsl-teardown/raw/151789982.full.txt`）／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ・curl）／`J`=判断

## なぜ良いのか（1行）

0秒で資金の額「If you're sitting on 25,000 or more」を名指しして客を絞り、10分46秒の広告の中で仕組み・店5つの売上・16か月保証・証言12人・FAQ6問まで言い切る。LP動画（4分52秒）は広告の半分以下の長さで、ページの仕事は動画の下の申込フォーム（8問）で資金を聞き直すことだけ。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00〜0:11 `W`「If you're sitting on 25,000 or more and are looking for a smarter way to grow your money, you can own a cashflow generating business that you can manage on the weekends from your couch or the golf course.」（`F` スーツの年配男性とホワイトボード「Jan-Sept 29% ROI」「YOU OWN THE BUSINESS」→水色地に「PROFIT」とロケット→ソファでノートPCの男→年配男性＋ゴルフ旗の絵文字。語り手はこの人ではない） |
| lead | 0:11〜0:30 `W`「Hi, my name is Cameron Hoffman.」「Our team is 100% US-based.」「We have our own warehouse in Massachusetts.」「we manage over 300 stores for partners」「This month, we're looking for three more partners」「if you're watching this video it means there's still spots available」（`F` 「ECOM ACCELERATOR」の黒Tシャツの本人） |
| discovery story | 無し（1:48「why don't we own all these stores ourselves」は反論潰しで、発見の物語ではない） |
| UMP | 1:01〜1:18 `W` 機会の理由。「the platform we're building on is a brand new blue ocean」「top economists at the wall street journal are calling it amazon's new rival」「over 300 million users」「over 1500 buyers for every single seller」「this window will not stay open forever」。**プラットフォーム名は伏せる**（TikTok の出現 0/139区間）。痛みも原因も言わない |
| UMS | 0:30〜1:01 `W`「our team handles the entire operation for you」「your job, review the numbers and fund the products actually sold」「maybe one hour a week max」「you keep 70 of the profits we'll invoice you for 30 once a month」→2:05「You own the store, we run the operation. And if you ever let us go, you keep everything.」。呼び名は9:33「the e-com accelerator model」（ブランド名＝仕組みの名前） |
| product reveal | あり（中身は0:30「here's how it works」から。名前は9:33 `W`「that's why we built the e-com accelerator model」） |
| price drop | 無し（金額を言わない。7:32 `W`「why is there an upfront investment」は理由だけで額は0回。額は冒頭の資格条件「25,000 or more」と本文「$20-35K liquid」だけ） |
| risk reversal | あり 2:30 `W`「if you don't make your initial upfront costs back in the first 16 months after we start selling, we will work for free until you do. Or we'll open another store at no cost, and that's written into the contract.」→7:14 FAQ「16 month profit guarantee」で再掲 |
| testimonials | 個人の声12（3:13〜6:05 `F`: 動画カード7人 Jenny「SOLID 30% ROI」／Cesar「$1,384/month BY MONTH 7」／Steven「HIS STORE Outperforms Real Estate」／Blaine「PLANNING FOR RETIREMENT」／Cody「FORMER MICROSOFT EMPLOYEE」／Cory「SOLID 24% ROI」／Antonio「PASSIVE INCOME FOR A BUSY PARENT」＋レビュー画面5件 Trustpilot 2・reddit 2・Google 1）＋店の売上5つ 1:18〜1:48 `W`「$35,692 in just 31 days」「$98,734 in 3 months」ほか |

無かったブロックは「無し」。欠落そのものが発見。

締めの形: CTAは3回（click の出現 4/139区間 `W`）。3:02「Click the link below to watch the full breakdown」（動画へ）→6:05「click the link below you can book a call」→6:09「still here still watching」で後半に入り、白地カードの FAQ 6問（6:34〜9:50 `F`）→10:36「click the button below to book your call」。

## 盗む所

- 資金の額で0秒に客を絞る「If you're sitting on 25,000 or more」。同じ額を申込フォームの2問目「minimum $20,000 investment」で聞き直し、「No, I have less than $20,000 available」だけ点数 -10 で通話予約から外す
- 自分で減点してから保証を置く。2:10 `W`「This is not a get-rich-quick scheme. Those revenue numbers I showed you are gross, not net profit.」（`F` レポート画面に「GROSS REVENUE」の判子）→2:30 16か月保証→2:42「If you're looking for overnight riches with no risk, keep scrolling.」
- 10分46秒の広告に CTA を3回置き、1回目は「full video breakdown」へ、2回目以降は「book a call」へ行き先を変える。後半の FAQ は6:09「still here still watching」から始める

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

![[ec/wiki/vsl-teardown/絵/151789982-hook]]

## 全シーン × b-roll（`F`）

尺 645.6秒 ／ 116シーン ／ 平均 5.6秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）

![[ec/wiki/vsl-teardown/シーン/151789982]]

## LP（着地ページ）— go.ecomaccelerator.io/fb/vsl

**読む前に**: 値段も決済欄も無い、動画1本＋申込フォーム1つのページ。フォームは開いた時から動画の下に出ていて、隠す仕掛けは無い。LP動画（4分52秒）は文字起こしと絵に落としてある。

| 項目 | 実測（`L`=LP、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=LP動画の絵） |
|---|---|
| URL | https://go.ecomaccelerator.io/fb/vsl （title「Unlock a NEW Stream of Income with Ecommerce!」） |
| 作り | DropFunnels（WordPress マルチサイト＋Beaver Builder。本文に `dropfunnels-multisite-plugin`・`fl-builder`・`bb-theme`）。builder 検出の `next/` は Typeform の `embed.typeform.com/next/embed.js` のことで Next.js ではない `L`。コメント欄は無し（要素 n=14、LPページの実測（2026-09-12・ブラウザ）） |
| 動画 | Vidalytics `fumbuU7I/sStNB5mtvec5gkXV`（内部名「Prince TT VSL Sped Up」）292秒＝4:52。自動再生はミュートのみ（`autoplay.onlyMuted=true`）・シークバーあり・再生時間表示なし・途中再開なし（`resume=false`）・チャプター9本（`ui.chapters.enabled=true`）。設定に CTA の項目は0件（`player.settings.json`） |
| ページの部品（上から） | ①ロゴ画像（y=40）②見出し「We Build & Manage Your Ecommerce Business - Live In As Little As 31 Days」（y=126）③「Watch The Video Below To See The Full Details 👇」（y=249）④動画（y=327・「Your Video Is Playing / Click To Unmute」）⑤「Apply Below To See How You Can Get A Income Generating Ecom Store」（y=1033）⑥「If You Qualify You Will Be Covered By Our 'No Profit No Payment' Guarantee」（y=1089）⑦Typeform の iframe `gLuwxRey`（y=1164・表示中。隠し項目 `funnel=FB,h_ad_id=,fbclid=`）⑧同意文「By submitting, you agree to our Privacy Policy」（y=1786）⑨画像（y=1932）⑩フッター Privacy Policy／Terms of Service＋「*Our spots are limited based on the amount of clients we can help onboard and fulfill on every month.」 |
| 売り場 | ページ内の Typeform（8問）→ 点数で2つに分かれる。Qualified → https://go.ecomaccelerator.io/fb/schedule （「Please Use The Calendar Below To Book A Demo With Our Team」・OnceHub のカレンダー `oncehub.com/mergedjs/so.js`）／Not Qualified → https://go.ecomaccelerator.io/fb/dq （「Thank You, Our Team Will Be In Touch Shortly」「within 24 hours」＋Vidalytics 埋め込み15本） |
| 値段 | ページ・LP動画とも金額0回（LP動画の「$」0/81区間 `W`）。出るのはフォーム2問目「Our proven e-commerce system requires a minimum $20,000 investment for set up, initial onboarding and inventory.」だけ `L`。利益の分け方（70／30）は広告だけ |
| 保証 | ページ「'No Profit No Payment' Guarantee」／LP動画3:22「make back your initial upfront costs back in the first 16 months」。日数でなく16か月 |
| 仕掛け | 隠す秒は無し（iframe は開いた時から表示中＝LPページの実測（2026-09-12・ブラウザ）、ページの `data-animation-delay` 0件、Vidalytics 設定に CTA 0件）。タイマー無し。フォームは `typeform-welcome=0` で最初の画面を飛ばし、1問目から出る |

申込フォームの中身（`dia read` と Typeform の公開定義 `form.typeform.com/to/gLuwxRey` を読んだだけ。入力・送信はしていない。項目 n=11、分岐ルール n=4）:

| # | 質問（逐語） | 選択肢 | 点数 |
|---|---|---|---|
| 1 | 「What's your monthly income goal with a mostly hands-off Ecom Store?」 | $2,500 - $4,000／$4,000 - $6,000／$6,000 - $8,000／「I'm open to realistic returns for an investment of this size.」 | 0（ルールに無し） |
| 2 | 「...requires a minimum $20,000 investment... Do you have access to at least $20,000 in liquid capital for this opportunity?」 | $20,000 - $30,000／$30,000+／less than $20,000 | less than $20,000 だけ -10、3問目を飛ばして4問目へ |
| 3 | 「How quickly could you access your investment capital if this is the right fit?」 | Immediately／1-2 weeks／1 month／2+ months | +3／+2（変数 qualify を NOT QUALIFIED にする）／+1／0 |
| 4 | 「When are you looking to start generating this additional income?」 | next 2 weeks／30 days／2-3 months／Just exploring | +3／+2（変数 qualify を NOT QUALIFIED にする）／+1／0 |
| 5 | 「What assets have you invested in before?」 | Real Estate／Stocks, Bonds, Commodities／Crypto／Businesses／Other／No previous investing experience | 0（ルールに無し） |
| 6〜8 | 「What's your best email?」「What name should I use when we chat?」「What's the best number to contact you at?」 | 自由入力 | 最後の項目（電話）で行き先を決める。行き先は点数 score だけで決まる: -10〜-1 → Not Qualified（/fb/dq）、0〜10 → Qualified（/fb/schedule）。取りうる点数は less than $20,000 の人が -10〜-7、それ以外が 0〜6。変数 qualify は行き先のルール（4ルール中）に出てこない |

### 広告 → LP のつながり

| 要素 | 広告（10分46秒） | LP動画・ページ（4分52秒） | 判定 |
|---|---|---|---|
| 餌（冒頭） | 「If you're sitting on 25,000 or more」 | 0:00「What if I told you there's a way you could generate a new stream of monthly cash flow」。資金の額は動画で0回 | 差し替え。額はフォーム2問目「minimum $20,000」で戻る |
| 原因の呼び名（機会の理由） | 1:06「brand new blue ocean」「amazon's new rival」。名前は伏せる | 0:06「Amazon's new rival」→0:38「This is the opportunity that you have available today with TikTok Shop」（TikTok 14/81区間） | 呼び名は一致。名前はLPで明かす |
| 解の呼び名 | 「You own the store, we run the operation」2:05／「the e-com accelerator model」9:33 | 2:51「My team will handle it for you」／3:08「we will operate off of a profit share model with you」 | 仕組みは一致。70／30 の数字はLPで0回 |
| 権威 | 「Hi, my name is Cameron Hoffman」「100% US-based」「own warehouse in Massachusetts」「over 300 stores」 | 0:52「My team and I have been in the e-commerce space since 2018」「hundreds of clients」。名乗り0回（Cameron 0/81区間）・倉庫0回 | 数字を差し替え。語り手は同じ顔に見える（`F` 紺のポロ）が名乗らない `J` |
| 数字 | 「over 300 million users」「1500 buyers for every single seller」「46 roi」（FTC earnings claims statement・2026年1〜6月）・店の売上5つ | 「a billion users」「over 5,000 users for every single seller」「20% to 30% return per cycle」、0:41「TikTok Shop is the fastest-growing e-commerce platform in 2024」 | **食い違う**（1,500と5,000、3億と10億）。LP動画は2024年ごろの収録と読める `J`（根拠は0:41の発話1区間だけ）。広告は2026年1〜6月の数字 |
| 約束 | 2:56「Which platform this is, how the profit split actually works, how $1 moves from a buyer's wallet to yours, the guarantee」 | platform ○（0:38）／guarantee ○（3:19）／profit split の数字 ×／$1 の流れ × | 4つ中2つ回収 |
| 商品名 | 9:33「e-com accelerator model」 | 動画で0回。ページはロゴとフッター「Ecom Accelerator © 2026」だけ | 名前は広告のほうが先に出す |
| 値段 | 金額0回（7:32 upfront investment は額なし） | 動画0回・ページ0回・フォーム「minimum $20,000 investment」 | 額はフォームで初めて出る |
| 保証 | 16 months・「written into the contract」 | 動画「first 16 months」／ページ「'No Profit No Payment' Guarantee」 | 中身は一致。ページだけ呼び名が違う |
| 絵 | 縦・焼き込み字幕・ストック映像・証言カード（`F`） | 横16:9・会議室の本人＋図5枚（黒地4＋青地1「63%」）（`F` sheet0 10コマ） | 別収録 |

### LP動画の構成（9節）

節の区切りは Vidalytics のチャプター（`ui.chapters.data` の秒と名前）。`W` の発話の切れ目と9本とも1秒以内で一致。絵は sheet0 の左から n枚目で書く（sheet の字幕と `W` の秒が約13秒ずれる。「63%」の絵は4枚目、発話は1:43）。

| # | 秒 | 節（チャプター名） | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00〜0:14 | The Hidden Cash Flow Opportunity | 「What if I told you there's a way you could generate a new stream of monthly cash flow on one of the most under-the-radar e-commerce platforms out there?」「Amazon's new rival」 | 1枚目 本人（会議室・紺のポロ） |
| 2 | 0:14〜0:53 | Why TikTok Shop Is Different | 「This platform already has a billion users」「50 times larger than Amazon's user base in 2000」「90 minutes per day」→0:38「with TikTok Shop」「a small handful of elite e-commerce store owners are making a killing on it」 | 2枚目 黒地に「TIKTOK SHOP」と amazon の比較図 |
| 3 | 0:53〜1:27 | Proof From the Trenches | 「in the e-commerce space since 2018」「sold on every platform from Amazon to Shopify to Walmart」「20% to 30% return per cycle on their inventory spend」「practically like a dating app for TikTok users and TikTok sellers」 | 3枚目 本人 |
| 4 | 1:27〜2:00 | Why This Isn't a Short-Term Fad | 「This isn't just some quick cash grab」「reap rewards for the next 10 years」「widely used by 63% of Gen Z in America」「user base will triple by 2030」 | 4枚目 青地「63%」の折れ線 |
| 5 | 2:00〜2:41 | The Harsh Truth: Why Most Will Fail | 「I'm not going to lie to you and tell you that selling on TikTok is easy」「You wouldn't know what products are going to sell」「the big institutional money will have moved into the space」 | 5枚目 黒地のイラスト「YOU'D PROBABLY JUST WASTE A TON OF TIME」 |
| 6 | 2:41〜3:19 | The Smarter Path: Partnering With Experts | 「Luckily for you, there's a better way」「My team will handle it for you」「viral, trending, impulse purchase products」「profit share model with you. So when you win, we win」 | 6枚目「NO NEED FOR A WAREHOUSE」・7枚目「HIGH LEVEL FINANCIAL DECISIONS」 |
| 7 | 3:19〜3:48 | Risk Removed: The 16-Month Guarantee | 「we guarantee you will make back your initial upfront costs back in the first 16 months」「we'll work with you for free until you do」→3:32 CTA1「click the link below and schedule a call with my team now」→3:42「fill out a brief application, and schedule a call with our team in the next 48 hours」 | 8枚目 本人 |
| 8 | 3:48〜4:35 | The Exact Process We Run For You | 5つの仕事: product research／sourcing and logistics／listing「over 5,000 users for every single seller」／marketing「we're going to cover ad spend」／customer service | 9枚目 本人 |
| 9 | 4:35〜4:52 | Your Next Step | CTA2 4:35「click the link below to book a call now」→「this won't be some hard sell of a call」「We're only looking for serious long-term partners」→CTA3 4:46「click the link below to schedule your call now」 | 10枚目 本人 |

売り物（運営代行）を初めて言う秒: 2:51「My team will handle it for you」（171秒／292秒＝59%）。ブランド名は0回。値段を言う秒: 無し（「$」0/81区間）。

### 売り場までの導線

ファネル: 広告（646s）→ LP（Vidalytics 4:52・申込フォームは開いた時から動画の下、隠さない）→ Typeform 申込（8問・点数で振り分け）→ Qualified: 通話予約 /fb/schedule（OnceHub）→ 通話 → 決済（どこで払うか判定不能・通話の中）／Not Qualified: /fb/dq（24時間以内に連絡・動画15本）

1. 広告の URL と最終 URL は同じ `https://go.ecomaccelerator.io/fb/vsl`（広告の着地URLとブラウザで開いた最終URLが一致）
2. ページを開くと動画がミュートで自動再生。スクロールすれば動画を見ずにフォームへ行ける（iframe は y=1164・表示中。LPページの実測（2026-09-12・ブラウザ））
3. 動画の CTA は3:32（CTA1）・4:35（CTA2）・4:46（CTA3）の3か所（click the link below 3/81区間）で「schedule a call」「book a call」「schedule your call」と言い、3:42 で「fill out a brief application」とフォームの存在を先に言う `W`
4. Typeform `gLuwxRey`: 1問目は収入の目標、2問目で初めて「minimum $20,000 investment」を出し、残り3問で資金の時期と開始時期を点数化、最後に email・名前・電話 `dia read`
5. 点数 0以上 → https://go.ecomaccelerator.io/fb/schedule 見出し「Please Use The Calendar Below To Book A Demo With Our Team」（title「Book Your FREE Call」・OnceHub）。URL に name・email・phone を差し込んで渡す（Typeform の `redirect_url`）
6. 2問目で less than $20,000 → 点数 -10 → https://go.ecomaccelerator.io/fb/dq 「a member of our team will be in touch within 24 hours」＋「`Check Out What Some Of Our Clients Are Saying`」と Vidalytics 15本 `curl`
7. 値段・決済欄はここまでの4ページ（LP・フォーム・schedule・dq）のどこにも無い。金額はフォームの「minimum $20,000」だけ

### コピーする時の骨（比率は4分52秒＝292秒の実測）

機会の予告 5%（Amazon's new rival）→ **プラットフォームの大きさ 13%**（10億人・1日90分・名前を明かす）→ 実績 12%（2018年から・20〜30%）→ 長く続く理由 11%（10年・Gen Z 63%・2030年に3倍）→ 自分でやると失敗する 14%（3年・大資本が来る）→ **代わりにやる 13%**（運営代行・利益の分け合い）→ 保証 10%（16か月・ここでCTA1と申込の予告）→ 5つの仕事 16% → 次の一手 6%（CTA2・3・「not a hard sell」）。値段・証言・FAQ の節は0/9節。証言12人と FAQ 6問は広告側（10分46秒）に置き、LP動画は短い要約とフォームの前座にする。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-151789982/sheet0.jpg`（10コマ）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-151789982.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-151789982/sheet0.jpg]]
