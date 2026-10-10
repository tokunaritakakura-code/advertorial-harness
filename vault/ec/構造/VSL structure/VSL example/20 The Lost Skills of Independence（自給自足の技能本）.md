<!-- 例 -->
# The Lost Skills of Independence（自給自足の技能本）— VSL example

読む人: この型（商品見せ問い型（Why don't they make X like this anymore））の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [150594266](https://app.gethookd.ai/share/ad/150594266?signature=a6015eda58861e9e0cdbcaadbc34fa4cf43b0dc0a36fe5601eebf9c0a559959c)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/150594266`）
LP: https://www.thelostskillsofindependence.com/book/
形式: VSL・動画 1316s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 Leadpages の長文セールスページ（動画＋スキルカード34枚＋オファー画像＋ボタン）
拾った日: 2026-09-12
稼働日数 / 成績: 23日 / score 90（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 608本（2026-09-12）
選定: GetHookd で「勝ち（score 81〜100）・稼働中・動画」かつブランドの稼働広告数500以上。着地が実測でVSL（長尺の売り動画が主役のページ）（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし／`W`=ローカルwhisper large-v3-turbo（この本は GetHookd の文字起こしが空なので広告もLP動画も `W`）／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ・curl）／`J`=判断

## なぜ良いのか（1行）

1秒目に商品（本の表紙）を机に置き、21分56秒のうち約9分をスキルの実演（31個）に使う。痛み・原因・証言のブロックを持たず、中身を見せる量で売る。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:21 `W`「Why don't they make books like this anymore?」「They should teach these in schools」→0:19「No wonder they don't want you to know this.」。`F` 0s ページをめくる手→1〜2s 机の上の表紙（書名と「Claude Davis」）→3〜9s 指でスキルカードを指す（「Stockpile a Ton of Water for 365 Days」ほか）→10〜11s 実写の蒸留器と「DISTILLED WATER」の瓶→12s パレットの菜園。字幕は13コマ全部に焼き込み |
| lead | 0:21–2:04 `W` スキルを13個「How to X＋効用1文」で列挙（「how to make water out of thin air」「This is so effective the CIA uses it」ほか）→1:50「And one hundred ninety more skills that anyone should know」→1:54「No matter if you're fifteen or ninety」 |
| discovery story | 無し |
| UMP | 無し（原因の呼び名が無い）。近い物は 0:19「they don't want you to know this」と 13:40「Little by little, we gave our power away」だけ `W` |
| UMS | 無し（解＝本そのもの。呼び名なし） |
| product reveal | **あり** 0:01 `F` 表紙が画面に出る。声で書名を言うのは 2:12 `W`「The first chapter you'll find inside the lost skills of independence」（10.1%）。続けて 2:04–4:26 章の案内8つ、4:26–13:04 スキル実演31個 |
| price drop | 無し（本の値段を言わない）。値段らしき声は 14:07「Each one is valued at $39, but today you'll get them for free」（ボーナスの値）と 21:36「for the price you see there」だけ `W` |
| risk reversal | **あり** 16:10–16:35 `W`「keep-the-book-money-back guarantee」「for the next 60 days」「you can even keep the book」 |
| testimonials | 無し（個人の声0人・人数の数字も言わない）。権威の借用は「the CIA uses it」（0:36）と「a Navy SEAL」（8:21）の2か所 `W` |

ブロックの外: ボーナス3つ 13:58–15:30／希少性 16:43「If the buy button below is not yet grayed out」／愛国クローズ 18:06–18:52「Being a true patriot isn't just about having a flag」／未来の総ざらい 18:52–21:13／最後のCTA 21:13–21:56 `W`。

## 盗む所

- 0:00 の問い「Why don't they make books like this anymore?」と、表紙を机に置く2秒（`F` 01s・02s）。商品を先に見せ、問いで「昔の良い物」の枠に入れる
- スキルは全部「How to X」＋効用1文の同じ型。広告では冒頭13個→章8つ→実演31個の順で52個並べ、「190 more」「200 skills」で数を締める
- 広告はLP動画から値段の声だけを切った版（文字起こしの一致率0.981、差分の挿入 n=5、LP動画が52秒長い）。本の値段（$166→$39）はLP動画の16:15とページの画像と決済ページでだけ出す `J`

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

![[ec/wiki/vsl-teardown/絵/150594266-hook]]

## 全シーン × b-roll（`F`）

尺 1315.8秒 ／ 651シーン ／ 平均 2.0秒 ／ しきい値 0.25（シーン数はしきい値に依存）。sheet0（0〜14秒）は縦の実写、sheet37・39（15:10〜16:17）は横の映像を縦枠の中央に置いて上下をぼかした画（見たシート n=4／55）。

![[ec/wiki/vsl-teardown/シーン/150594266]]

## LP（着地ページ）— thelostskillsofindependence.com/book

**読む前に**: 広告とLP動画は同じ台本（LP動画が値段とスキル3つを足した22分47秒版）。ページはオファーを隠さず、クーポン窓とタイマーで急がせてから Digistore24 の注文フォームに送る。

| 項目 | 実測（`L`=LP、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=LP動画の30秒おきの絵、`J`=判断） |
|---|---|
| URL | https://www.thelostskillsofindependence.com/book/ （広告の lp は末尾スラッシュなし。開くと付く） |
| 作り（builder） | Leadpages（`L` builder=leadpages・Leadpages の DELAY_SCRIPT は入っているが、`data-delay-display-seconds` の値を持つ要素は取得したHTML 696,531 byte の中に0個）。GTM と GA4 あり |
| 動画 | Wistia `27ha9mdwcu`、内部名「Lost Skills Of Independence VSL 500MB」、1367.55秒（22:47）。`playbar: false`（シークバー無し）・`settingsControl: false`・サムネに「Click to Play the Video With Sound」 `L` |
| ページの部品（上から） | ①見出し「Early Bird 76% Off Ends Tonight! Get Your 3 Gifts Before it's Gone!」＋Best seller バッジ ②Wistia動画 ③本の画像＋書名＋1文「the most important 200 life-skills that nobody teaches you」 ④「They Just Don't Make Books Like This Anymore:」画像5枚＋本の作り（hardcover・spiral-bound・200 illustrated skill cards） ⑤「`Here Are Some Of The Skills You Will Find Inside:`」スキルカード34枚（見出し＋説明＋「Skill no. XX of 200」） ⑥追加の書名16個（ページの文言は「just 49 of the 200 skills」、数えると34＋16＝50） ⑦「PLUS Three Life-Saving Gifts」Bonus #1〜#3 ⑧「limited edition」の文＋オファー画像（$49＋$39×3＝$166 に取り消し線・「76% OFF LIMITED TIME ONLY」「Just $39」・60 DAY バッジ）＋ボタン「GET MY COPY + BONUSES」（y=23,656）＋「60-day refund ♦ Keep the book ♦ Ships from USA」 ⑨Keep-the-Book保証 ⑩Amazon風レビュー「4.9 out of 5／363 global ratings」10件 ⑪「Why You Should Get」4項目 ⑫ボタン再掲（y=31,362） ⑬フッター（Facebook免責・Bannockburn, IL の住所） `L` |
| 売り場 | ボタン → `checkout-ds24.com/content/706867/55419/globalbro/…` → `checkout-ds24.com/product/706867/?ds24tr=TLSIPhysSPINTMB` に転送。Digistore24 の1ページ注文フォーム（Apple Pay/Google Pay・カード・PayPal） `L` |
| 値段 | 1段だけ。本「(Physical Hardcover Book)」$49→**$39**（クーポン適用後）、送料 $0、ボーナス3つ「$39 (FREE)」。ページ本文に値段の文字は無く、値段はオファー画像の中だけ（本文の「$60」はレビューの中の部品代） `L` |
| 保証 | 60日・返金しても本は返さなくてよい（「You can choose to keep the physical book」） `L` |
| 仕掛け | オファーを隠さない（遅延表示0個）。スクロール15%で上部帯「EARLY BIRD／24-hour exclusive sale／Jump to Offer」。スクロール15%か、PC幅768px以上でカーソルが上に出た時（`mouseleave` の `clientY <= 0`）にクーポン窓「Today (09/12/2026) you get 76% off」「Coupon Number LSKILLS76 can only be used today」。日付は `toLocaleDateString` で毎日その日になる。Apply Coupon を押すと下部バーに50:00のカウントダウン（`startCountdown(3000)`、0で「Offer expired」）。決済ページにも「Discounted Cart Available For 00h 04m 58s」 `L` |
| レビューの形 | 10件全部「Verified Purchase」、日付は2026-06-20〜06-24の5日間、「people found this helpful」が247→221→203→189→176→167→158→134→112→91と上から降順 `L` |
| 版 | ボタンの行き先が取得ごとに違う（ブラウザ実測の page json は `7601bookvar15`、curl のHTMLは `7601bookcontrol15`）。ページが2版で回っている `J`。var15 を dia で開いた決済ページの冒頭に「This version of the order form is not public yet.」の表示 `L` |

### 広告 → LP のつながり

| 要素 | 広告（21:56） | LP動画（22:47）・ページ | 判定 |
|---|---|---|---|
| 餌 | 0:00「Why don't they make books like this anymore?」 | 0:00 同じ文。ページ④の見出し「They Just Don't Make Books Like This Anymore」 | 逐語で引き継ぐ（動画とページの両方） |
| 原因の呼び名 | 無し（0:19「they don't want you to know this」） | 無し（0:17 同じ文） | どちらも無し |
| 解の呼び名 | 本そのもの（書名） | 本そのもの。ページ最上部③に書名 | 一致 |
| 権威 | 語り手は名乗らない。「the CIA uses it」「a Navy SEAL」 | 同じ2か所（8:45 Navy SEAL）。著者名「Claude Davis」は表紙の絵とレビュー1件の「Thank You to Claude Davis」だけ | 一致（人の権威を立てない） |
| 数字 | 13個＋「190 more」・「200 skills」・「3,500 calories」・「99%」・ボーナス「$39」 | 同じ数字＋「$117」「$166」「$39」。ページは「Skill no. XX of 200」×34 | 値段の数字だけLPで足す |
| 約束 | 0:16「self-reliant and to not depend on anyone for anything」 | 0:17 同じ文 | 一致 |
| 商品名 | 0:01 表紙（`F`）・2:12 声（10.1%） | 2:12 声（9.7%）・ページ①③ | 一致 |
| 値段 | 本の値段なし。21:36「for the price you see there」 | 16:15「not for $166 but only $39」・16:36「just $39」（`F` 16:15 のコマに $49＋$39×3＝$166 の板）→ページのオファー画像「Just $39」→決済 $39 | 広告から値段の声だけ切る（挿入 n=5 のうち2つが値段） |
| 足した中身 | 無し | 5:15 樹液の草の使い方・7:43「Stop Bleeding Power」・13:37「flu bomb drops」 | 広告で切ったスキル3つ（挿入 n=5 のうち3つ） |
| 保証 | 16:17「for the next 60 days」 | 17:09 同じ・ページ⑨ | 一致 |

### LP動画の構成（14節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F`（コマは0:15から30秒おき） |
|---|---|---|---|---|
| 1 | 0:00–0:21 | hook | 「Why don't they make books like this anymore?」「No wonder they don't want you to know this」 | 0:15 屋根の上で銀色の板を持つ男 |
| 2 | 0:21–2:03 | スキル列挙13個 | 「like how to make water out of thin air」…「And 190 more skills that anyone should know」「No matter if you're 15 or 90」 | 0:45 油を瓶に注ぐ手／1:15 スーパーの棚／1:45 瓶詰めのパン |
| 3 | 2:03–4:28 | 章の案内8つ（product reveal） | 「The book is organized in a very practical way, by type of skill」→2:12 書名→Self-Sufficient Home Projects…Forbidden Psychology Skills | 2:15「Self-Sufficient Home Projects」の挿絵／3:15 レシピの挿絵ページ／4:15 スキルカード |
| 4 | 4:28–13:28 | スキル実演32個 | 「take this book with you」→ペミカン「3,500 calories」→「kill disrespect」→「Stop Bleeding Power」→「a Navy SEAL」→「99% of people make that ruins cast iron」→ダニ「like a harpoon」 | 4:45 リュックに本／6:15 怒鳴る男／7:45「Stop-Bleeding Powder」カードを指す／11:15「Make a Faraday Cage at Home」／13:15 ダニのCG |
| 5 | 13:28–13:50 | 残りの書名 | `「many, many more skills like this」`→「There are 200 practical life skills in this beautiful book」 | 13:45 本のページ一覧を指す |
| 6 | 13:50–14:21 | 遺産・失われる物 | 「no better gift you can give them」「Each year that passes, more and more skills are lost forever」「you'll always be a slave to the fisherman」 | 14:15 本を持って歩く男 |
| 7 | 14:21–15:57 | ボーナス3つ | 「three bonus gifts, which won't be available much longer」「Each one is valued at $39」→Wild Edibles／Quarter Acre／Patriot's Bug-In Guide | 14:45 野草を摘む手／15:15 温室／15:45 家の設計図 |
| 8 | 15:57–16:41 | **price drop** | 「all these guides worth $117 for free」「not for $166 but only $39」→「complete package for just $39」 | 16:15 値段の板（$49・$39・$39・$39・$166に取り消し線） |
| 9 | 16:41–17:02 | 唯一性 | 「There's never been a book like this one」「this book is the only place it's been preserved」 | 16:45 雨水タンク |
| 10 | 17:02–17:31 | risk reversal | 「keep-the-book-money-back guarantee」「for the next 60 days」「you can even keep the book」 | 17:15 本のページ |
| 11 | 17:31–18:07 | 希少性・配送 | 「If the buy button below is not yet grayed out, then I suggest you hurry up」「tracking link」「available 24/7」 | 17:45 黒地に白文字「If you order it today」 |
| 12 | 18:07–19:46 | 愛国クローズ | 「Or you can equip yourself」「We are not the descendants of fearful men」「Being a true patriot」 | 18:15 ランタン／19:15 麦畑の家族／19:45 群衆 |
| 13 | 19:46–22:04 | 未来の総ざらい | 「You'll be among the most prepared for the next disaster」「slash your utility bills」「for your kids, your grandkids」 | 20:15「Analysts Warn of Imminent Economic Collapse」の記事の画／21:45 温室で本を持つ男 |
| 14 | 22:04–22:47 | 最後のCTA | 「If the button below is not yet grayed out, you can still secure everything」「for the price you see there」「God bless you」 | 22:15 本＋ボーナス3冊の画／22:45 机の上の本 |

商品名が初めて出る秒: 2:12（9.7%）`W`。値段を初めて言う秒: 14:34 ボーナスの「$39」、本の値段は 16:15「$166→$39」（71.4%）`W`。

### 売り場までの導線

ファネル: 広告（21:56・縦）→ LP（Wistia 22:47・オファーは隠さない、ボタンはページの y=23,656 と 31,362 の2か所）→ Digistore24 の1ページ注文フォーム（$39・クーポン LSKILLS76 適用済み・5分のカート保持タイマー）→ 決済 Digistore24

1. ページはスクロールだけでボタンに届く（遅延表示0個）。動画の17:35と22:26「not yet grayed out」に対応するボタンの灰色化の処理はHTMLに無い（`grayed` 系の文字列0件）`L`
2. スクロール15%で「Jump to Offer」帯とクーポン窓が同時に出る。Apply Coupon で50:00タイマー。クーポン名と「76% off」はページ①の見出しとオファー画像と決済ページで同じ `L`
3. ボタン→Digistore24。決済ページは「Coupon LSKILLS76 Applied!」「Discounted cart reserved for 04:57」、配送予定「09/15–09/17」、日本の住所だと「Unfortunately we cannot ship this product to Japan」`L`
4. PDP・カート・まとめ買いの段は無い。本1冊 $39 の1択
5. 購入後のアップセル: 判定不能（購入しないと見えないため、押していない）

### コピーする時の骨（比率は22:47の実測）

hook 1.5%（問い＋表紙）→ スキル列挙13個 7.5% → 章の案内8つ 10.6%（書名は2:12）→ **スキル実演32個 39.5%** → 残りの書名 1.6% → 遺産・失われる物 2.3% → ボーナス3つ 7.0% → **price drop 3.2%（15:57、70%地点）** → 唯一性 1.5% → 保証 2.1% → 希少性・配送 2.6% → 愛国クローズ 7.2% → 未来の総ざらい 10.1% → 最後のCTA 3.1%。痛み・原因・発見の物語・証言の部品が無く、中身の実演が全体の59.2%（節2〜5、809秒÷1367.55秒）。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-150594266/sheet0.jpg`（46コマ・0:15〜22:45）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-150594266.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-150594266/sheet0.jpg]]
