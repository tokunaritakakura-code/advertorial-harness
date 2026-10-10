<!-- 例 -->
# Emma（便秘と膨満）— VSL example

読む人: この型（餌型（Watch what X）＋否定列挙）の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [143112679](https://app.gethookd.ai/share/ad/143112679?signature=6780736de8837b94d2adcf469c417d6a3f41fcbb2e0523efc2da0bd83769e5b1)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/143112679`）
LP: https://resetdigestion.com/pages/er-vslfb/
形式: VSL・動画 259s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 Wistia動画が主役の売りページ（オファーを隠す）
拾った日: 2026-09-12
稼働日数 / 成績: 32日 / score 90（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 736本（2026-09-12）
選定: GetHookd で「勝ち（score 81〜100）・稼働中・動画」かつブランドの稼働広告数500以上。着地が実測でVSL（長尺の売り動画が主役のページ）（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし／`W`=ローカルwhisper large-v3-turbo／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ）／`J`=判断
広告の文字起こしは `W`（GetHookd の文字起こしが空だったため。全文は `ec/wiki/vsl-teardown/raw/143112679.full.txt`）

## なぜ良いのか（1行）

0秒で拭く回数（`four times`）を名指しし、1:23で解に医師の名前つきの呼び名（seven second poop method）を付け、残り2:06〜4:14（49%）を証言10人に使って商品名を1回も言わずにLPへ送る。 `J`

## 分解（9ブロック）

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:26 `W`「watch what **magnesium** does to your bowels if you have to wipe more than four times after you poop」（`F` 0〜2秒 茶色い粉の山＋帯「WATCH WHAT MAGNESIUM DOES TO YOUR BOWELS」、3〜5秒 チョコ入りドーナツを紙で拭く、6〜7秒 Mayo Clinicのロゴ）→「the mayo clinic confirms that stuck poop can cause these embarrassing skid marks in your undies」（`F` 9〜10秒 汚れた黄色い布）→「liquefied stool leaks around the stuck hard poop and stains your underwear」 |
| lead | 0:26–0:59 `W`「fiber helps you poop right nope」「what about drinking lots of water nope」→「diarrhea is actually a form of constipation weird right」「your body's desperate last-ditch attempt to get things moving again」 |
| discovery story | 無し |
| UMP | 0:54–1:23 `W` 呼び名は **stuck poop**（広告内7回）。「stuck in the grooves of the colon」「that leftover poop acts like velcro and grabs onto new poop」「according to new york's top gut doctor fiber just adds bulk… like adding more cars to a traffic jam」「don't take laxatives choke down psyllium or drink lots of water」 |
| UMS | 1:23–1:45 `W`「it's called the **seven second poop method** created by dr gina sam a top new york city gut doctor」「one of the very first doctors to investigate the link between the health of our gut and excess weight」（`F` 1:30前後に女医の写真。画面で喋るのは名乗らない白髪の男性医師） |
| product reveal | 無し（動画内で商品名0回。広告本文だけ「Discover EMMA Now!」、見出し「💩Kissed 10lbs of Poop Goodbye」） |
| price drop | 無し |
| risk reversal | 無し |
| testimonials | 個人の声 `W` `F` 10人 2:06–4:14（シーン052〜062の顔で数えた。n=10）「i go maybe two times a day now」「within two days i noticed that i was becoming more regular」「i was 172 pounds… i weighted 158 pounds」「my husband says he got his wife back from 30 years ago」。全員の画面に「Click Below & Find Relief」ボタン。CTAは1:45と1:58の2回「tap the button below this video to see dr sam's seven second poop method」。最後の5秒は「Discover Dr. Sam's 7-Second Bowel Releasing Ritual」の板 |

無かったブロックは「無し」。欠落そのものが発見。

## 盗む所

- 餌（magnesium）は0〜5秒の帯と粉の絵だけに使う。広告の残りで0回、LP動画でも0回（`grep -ic magnesium` の結果）
- 不快の瞬間を回数で名指しする「wipe more than four times after you poop」＋汚れた布の実写（9〜10秒）
- 解の呼び名に秒数と医師の名前を付け（seven second poop method・dr gina sam）、動画の49%（2:06〜4:14）を証言10人に回して、全員の画面にボタンを常駐させる

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

![[ec/wiki/vsl-teardown/絵/143112679-hook]]

## 全シーン × b-roll（`F`）

尺 258.9秒 ／ 64シーン ／ 平均 4.0秒 ／ しきい値 0.25（シーン数はしきい値に依存する）

![[ec/wiki/vsl-teardown/シーン/143112679]]

## LP（着地ページ）— resetdigestion.com/pages/er-vslfb

**読む前に**: ここはLPの構造と、広告→LP→売り場のつながり。LP動画（57分02秒）は文字起こしと絵に落としてあるので、動画本体は要らない。

| 項目 | 実測（`L`=LPページ、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=30秒おきの絵） |
|---|---|
| URL | https://resetdigestion.com/pages/er-vslfb/ `L`（配信は Cloudflare。応答ヘッダに Shopify の印は0件。画像だけ emmarelief.com の Shopify CDN から読む） |
| 作り（builder） | page json の builder は空欄 `L`。HTMLは Tailwind＋Bootstrap＋jQuery の手書き。GTM-56TX85F。プライバシーのリンク先は privacy.konscious.us。テキスト版 `/pages/er-vslfb-text/` あり（HTTP 200） |
| 動画 | Wistia。PC用 `5zxlpv6osp`（内部名「CURRENT LIVE : Emma VSL [Talking Head Var 3 + Sam Full VO without Frankenstein Intro + 300kbps 1024x576] - Desktop_060826」）、スマホ用 `3m45igp0h2`（720x900・同名の Mobile_060826）。どちらも3,422秒＝57分02秒。autoPlay=false、playbar=false（URLに `#vibdeobar` を付けた時だけシークバー）、音量・全画面ボタン無し、初回再生は0秒から |
| ページの部品（上から） | オファー前: ①「TOP NYC GUT DOCTOR:」＋見出し「"Do This Once A Day To Empty Your Bowels Like Clockwork..."」②Wistia動画＋「Click for sound」③「IMPORTANT: Your video may take 10 seconds to load. Make sure your sound is on.」④医師の紹介「Top Gastroenterologist 2024 Dr. Gina Sam M.D」（PCだけ・再生すると隠れる）⑤偽コメント「20 Comments」20件（Emily〜Zack。20件中6件が動画の最後（ending／last 5 minutes）に、5件が寄生虫に触れて最後まで見させる。例「the last 5 minutes of this one were next-level」）⑥As Seen On ⑦FDA免責 ⑧フッター（Terms・Privacy は `#`）。オファー後（`afterdrop` のv=0の塊）: ⑨緑の下向き矢印 ⑩3段オファー ⑪保証枠 ⑫ボーナス「NEW! "Lean Belly Shakes"」（3本か6本で無料のレシピ本）⑬「Your Story Can Be Next」証言4件（Natasha K／Lucy C／Amberlyn F／Patricia G。Natasha K／Amberlyn F／Patricia G の3件は別商品（「this」「the greens」「Supreme Greens」）とEmmaの併用の話、Lucy C の1件はEmmaが出ず「the greens」だけの話。n=4）⑭3段オファー再掲 ⑮F.A.Qs 8問（動画のFAQと同じ順・同じ文）。オファーが出ると④⑤は `beforedrop` で消える |
| 売り場 | ボタン12本（2か所×PC用とスマホ用×3段）→ `go.emmarelief.com/products/emma-{1,3,6}-pack-er-vslfb/`。パスは /products/ だが中身は**SamCartの1ページ注文フォーム**（応答に `samcart_session` クッキー、HTMLに `samcart_checkout.js`）。連絡先・請求先・カードかPayPal・「Place Order Now」。タブ名「Emma - 1 Pack JP \| Enclave Bioactives」 |
| 値段 | 1本 $59（元$99・LPでは送料$4.95と表示、注文フォームでは Shipping Free）／3本 $147（$49/本・元$297・送料無料・DOCTOR'S CHOICE）／6本 $234（$39/本・元$594・`BIGGEST DISCOUNT`）。注文フォームに Shipping Insurance $2.49 の枠。パック名は Starter／Doctor's Choice／Gut Superhero |
| 保証 | 90日「No Questions Asked 100% Money Back」「You can even send back an empty bottle」 |
| 仕掛け | オファーの出方は3本立て `L`: (1) 動画の再生位置が1,991秒＝**33:11**（`secondchange`）(2) ページを開いてからの経過が1,986秒＝33:06（再生していなくても出る）(3) URL `#drop`／Ctrl+B で即時、`#elapsedtime=N` で経過を上書き。出たことの保存（localStorage／cookie）は0件なので、再訪すると隠れた状態に戻る。LPにある10分タイマーの関数は `.dtimer` 要素が0個で表示されない。タイマーは注文フォーム側「Your Special Price Is Reserved For 9:36」＋`Hurry! Stock is running low due to high demand` |

### 広告 → LP のつながり

| 要素 | 広告（4分19秒） | LP動画・ページ（57分02秒） | 判定 |
|---|---|---|---|
| 餌 | magnesium（0:00〜0:05） | 0回。見出しは「Do This Once A Day…」 | **餌は捨てる** |
| 原因の呼び名 | stuck poop（7回）「grooves of the colon」「velcro」 | stuck poop 9回に加えて archaea 25回・methane 12回・「gut vampires」・寄生虫（11:10〜15:20） | LPで原因が1層深くなる |
| 解の呼び名 | 「seven second poop method」3回＋1:40「her seven second morning ritual」1回 | 「poop method」は0回。1:21「my seven second bowel releasing ritual」（81.3〜86.4秒）の1回と、6:17「a seven-second morning ritual」（377.1〜384.6秒）の1回で、呼び名が1回ずつ違う。やり方は最後まで語られず、25:17で Emma に置き換わる | 広告の主な呼び名（poop method）は引き継がない。「seven second」と ritual だけ残し、中身は商品 |
| 権威 | 「dr gina sam a top new york city gut doctor」（写真だけ。画面の語り手は名乗らない白髪の男性医師） | 語り手＝Dr. Gina Sam本人（女性・一人称）・Tufts・Mount Sinai・「Dr. Poop」 | 名前は一致、画面の顔が変わる |
| 否定列挙 | fiber・water・laxatives・psyllium | fiber・laxatives・probiotics の3つ（6:35〜9:40） | water を probiotics に入れ替え |
| 数字 | 「10 15 pounds lighter」・`four times`・172→158 pounds | 「10 to 15 pounds of stuck poop」→26:57「up to 20 pounds」・17 ingredients・700,000人・99.6% | 10〜15 pounds を引き継いで20に上げる |
| 約束 | 「her seven second morning ritual」 | 6:17「In a minute, I'll show you a seven-second morning ritual」→実際は25:17で商品名 | 「In a minute」から商品まで19分 |
| 証言 | 映像10人。3:37「my wife is like we're gonna have to get you some new pants」 | 27:15〜29:15 の映像証言。28:37「we're going to have to get you some new pants」（gonna と going to の1語違い。聞き取りの差か別テイクかは判定不能：音声を突き合わせていない）。ページ⑬の4件は、3件が別商品との併用、1件は別商品だけの声 | 同じ台詞の証言が両方にあり、逐語は1語違う |
| 商品名 | 動画0回（本文「Discover EMMA Now!」） | 25:17（44%） | LPで初出 |
| 値段 | 無し | 32:15「even at $500」→32:39「$69」→33:07「$59」／$49／$39 | LPだけ |
| 保証 | 無し | 37:00「a full 90 days… ironclad」・ページ90日 | LPだけ |

### LP動画の構成（22節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00–1:15 | hook | 「Hi there, my name is Dr. Gina Sam」「the true root cause of constipation and bloating. Trust me, it's not what you think」「why you should never use fiber, laxatives, or probiotics」「a clogged colon that's backed up with impacted fecal matter」→症状の列挙 | FIBERに×印・HEARTBURN・寝込む女 |
| 2 | 1:15–2:45 | lead・未来 | 「my seven second bowel releasing ritual」「why diarrhea is also considered a form of constipation」「release the trapped 10 to 15 pounds of stuck poop」「Imagine never having to hold in gas」 | 窓辺の女・丘を歩く女 |
| 3 | 2:45–4:45 | 権威＋動機 | 「voted as top gastroenterologist in 2018, 2019, 2020, 2021」「I watched my best friend battle a devastating illness」「Tufts University」「director of Mount Sinai Gastrointestinal Motility Center」「call me "Dr. Poop"」 | 女医の語り（Talking Head）・夜のPC・DIGESTION SPEED |
| 4 | 4:45–6:35 | 症例 | 「A 73-year-old woman… over 40 years」「a foreign invader. I'll talk about that in a bit」「the Washington Post did a huge nationwide story」「In a minute, I'll show you a seven-second morning ritual」 | 病室・黒画面・自由の女神 |
| 5 | 6:35–9:40 | 否定列挙（失敗した解決策3つ） | fiber「benzidine」／laxatives「polyethylene glycol… used in jet fuel」「like a bald tire that's lost its grip」／probiotics「22-foot-long small intestine」 | 野菜・FLAVORS・トイレの札・腸CG・CLEAN AND FREE FROM ALL BACTERIA |
| 6 | 9:40–11:10 | 消化の仕組み | 「peristalsis… a little like squeezing a tube of toothpaste」「10 to 15 pounds of undigested waste fermenting in your belly」 | PROBLEMの手描き・胃のアニメ・食べる女 |
| 7 | 11:10–15:20 | UMP | 「in 2020, a study came out」「the leading cause of slow bowels is methane gas」「microscopic invaders called archaea」「I like calling them gut vampires」「a five-star luxury resort like the Ritz-Carlton」「Hookworms… up to 30,000 eggs per day」「over 100,000 blood vessels」「deadly heart disease and even death」 | 2020の論文・手描きの菌（archaea／tapeworm／amoeba／hookworm）・血管・症状イラスト |
| 8 | 15:20–16:25 | 解の予告 | 「What if there was a way to eliminate archaea, fight parasites」「rare exotic ingredients used in Southeast Asia」 | 果物と野菜・緑の菌 |
| 9 | 16:25–24:05 | UMS（成分5つ） | berberine「since around 650 BC」「75% of all television advertising is big pharma」「as effective as rifaximin」（Johns Hopkins 2014）／DGL「Like a well-lubricated slide」／Star Anise「your body's natural laxative, bile」／quercetin「acts like a repairman」／resveratrol「the French paradox」「the key to boosting bioavailability」 | USED SINCE 650 B.C.・BERBERINE・BIOAVAILABILITY・フランス国旗・RESVERATROL |
| 10 | 24:05–25:15 | 製造の相手 | 「partner with the leading nutrition company, Conscious」「more than 700,000 men and women」「Eating Well, Elle, People, Vogue」「around 99.6%」「95% of supplements」 | 研究室・雑誌ロゴ |
| 11 | 25:15–27:15 | product reveal | 「Introducing Emma. Emma includes 17 gut healing ingredients」「three-step gut restoring process」「like a pressure wash for your insides」「release up to 20 pounds of stuck poop」 | 3ステップのアイコン・成分の写真グリッド |
| 12 | 27:15–29:15 | 証言（映像） | 「I strained so much that I literally passed out on the toilet」「one side of the x-ray was all solid white gray… that's constipation」「we're going to have to get you some new pants」「Oh, hallelujah」 | 顔のグリッド・女性の証言4人 |
| 13 | 29:15–30:40 | 未来の描写 | 「Just imagine waking up each morning, completely emptying your bowels」「exotic vacation」「improved your romantic life」 | ベッドの女・跳ぶ女 |
| 14 | 30:40–32:40 | 値段の枠 | 「quality like this doesn't come cheap」「What would you be willing to spend… 200? 300? 500?」病名の列挙「colorectal cancer」「even at $500」「we cut out all middlemen」 | 女医・貯金箱・老夫婦 |
| 15 | 32:40–33:30 | **price drop** | 「we're offering Emma today for just $69. That's more than 40% off」→「a 30-day supply for just $59. That's another $10 off」「not available on Amazon」＝ページのオファー表示（33:11）は$59を言い始めた4秒後 | ボトル「THAT'S MORE THAN 40% OFF」 |
| 16 | 33:30–36:30 | まとめ買い＋希少性 | 「wipe out all of the colonies and their eggs」「Think of it like compound interest」「three-bottle… $49 per bottle… free shipping」「six bottles… $39」「just $1.30 a day」「this $59 price is not guaranteed beyond today」「if you leave the page, it may be given away to someone else」 | 菌・右肩上がりのグラフ・「$1.30 A DAY」・扉 |
| 17 | 36:30–38:30 | risk reversal | 「guarantee your order today for a full 90 days. It's a 100% ironclad money-back guarantee」「Just say maybe」「It doesn't matter if you've used up the entire bottle」 | 2人の女・便器 |
| 18 | 38:30–39:10 | 注文の手順 | 「If Emma is still in stock, then the order page will appear」「add yourself to our waiting list」「256-bit SFL encryption… Amazon.com」 | 「$」の絵 |
| 19 | 39:10–41:45 | クローズ1（2つの道） | 「a very real crossroads in life」「Forever slave to your digestion」「you may never forgive yourself」 | 分かれ道の人影・トイレの札・×の男・下向き矢印 |
| 20 | 41:45–53:30 | FAQ×8 | 「Still watching? Still making your decision?」→Marie（probiotics）／Jackie（体重・AMPK）／Jacqueline（副作用）／Amy（食物アレルギー）／Michelle（膨満）／Josie（下痢）／Veronica（効く速さ「within the first two to three days」）／最後（他で買えるか「FDA-registered, GMP-certified labs」「at least double」） | 白地に文字・AMPK・IRONCLAD・IMPROVEMENTS |
| 21 | 53:30–54:00 | 締めの希少性 | 「this one-time special offer is good today only」「click the button below now to go to our secure order checkout page」 | ボトルの山「CLICK THE LINK BELOW」 |
| 22 | 54:00–57:02 | クローズ2 | 「without compassion, it's impossible to have a 20-year career」「broken marriages」「approximately 15,000 miles of blood vessels」「Frontiers on Cardiovascular Medicine」「Choose the three or six pack」「God bless」（56:44で語り終わり） | 白地に文字・腹を押さえる男・90 DAYS GUARANTEE・黒 |

語り手: 3:00・4:30・30:30 のコマに女医の Talking Head（内部名「Talking Head Var 3」）。それ以外はストック映像・手描きアニメ・白地の文字。

### 売り場までの導線

ファネル: 広告（4:19）→ LP（Wistia 57:02・オファー表示 33:11）→ 3段のボタン → go.emmarelief.com の1ページ注文フォーム → 決済（SamCart・カードかPayPal）

1. 動画は33:11まで3段オファーを隠す。ページを開いて1,986秒たつと、動画を止めていても出る。出た瞬間に医師紹介と偽コメント20件が消え、矢印・3段・保証・ボーナス・証言4件・3段再掲・FAQ 8問に入れ替わる
2. 動画が「$59」と言い始めるのは33:07、枠が生えるのは33:11。$69（32:39）ではなく、2度目に下げた値段に合わせてある
3. ボタン → `go.emmarelief.com/products/emma-3-pack-er-vslfb/`。Shopify風のパスだが SamCart の注文フォームで、パックは1つだけ入った状態（例: EMMA Doctor's Choice PACK $147.00）
4. 注文フォームで10分の予約タイマー（読んだ時点で9:36〜9:42）＋在庫の煽り＋配送保険$2.49。PDP・カートは挟まない。3段 → 注文フォーム → 決済の3手で終わる
5. 動画38:34「If Emma is still in stock, then the order page will appear… waiting list」と言うが、注文フォームに在庫切れの分岐は実測で見えていない（読むだけで送信していない）

### コピーする時の骨（比率は57分02秒の実測）

hook 2.2%（名乗り・原因は違う・3つを使うな）→ lead・未来 2.6%（7秒の儀式・下痢も便秘・10〜15 pounds）→ 権威＋動機 3.5%→ 症例 3.2%（73歳・40年・Washington Post）→ **否定列挙 5.4%**（fiber／laxatives／probiotics、各1つずつ恐い物質名）→ 仕組み 2.6%→ **UMP 7.3%**（methane→archaea＝gut vampires→寄生虫→血管→心臓病）→ 解の予告 1.9%→ **UMS 13.4%**（成分5つ、各成分に年数・研究・喩え）→ 製造の相手 2.0%→ **product reveal 3.5%（25:17、全体の44%地点）**→ 証言 3.5%→ 未来 2.5%→ 値段の枠 3.5%→ price drop 1.5%（$69→$59＝オファー表示）→ まとめ買い＋希少性 5.3%→ 保証 3.5%→ 手順 1.2%→ クローズ1 4.5%→ **FAQ 20.6%**（8問）→ 締めの希少性 0.9%→ クローズ2 5.3%。広告の「7秒の儀式」は2回の予告で終わり、動画の中で一度も実演されない。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-143112679/sheet0.jpg`（0:00〜26:30）／`sheet1.jpg`（27:00〜53:30）／`sheet2.jpg`（54:00〜56:30）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-143112679.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-143112679/sheet0.jpg]]
![[ec/wiki/vsl-teardown/frames/LP-143112679/sheet1.jpg]]
![[ec/wiki/vsl-teardown/frames/LP-143112679/sheet2.jpg]]
