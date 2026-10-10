<!-- 例 -->
# Tyler Tometich（バズ動画エフェクト講座）— VSL example

読む人: この型（実演型（This is called the X Effect））の実物を1本まるごと見たい人。
読む時: 自分の本のフックとブロックの並び、LPと売り場の形を決める時。
読まなくていい条件: 30本の比較だけ要る時は [[_index]]。

出典: [102457232](https://app.gethookd.ai/share/ad/102457232?signature=f1737fd48ea45345096cf21bffa5b900e130c4280273bd967dfdc4c94ada02cd)（GetHookd・share_url は期限なし。引き直しは Dia のログイン済みタブから GetHookd 内部API `GET /api/get-ad/102457232`）
LP: https://www.viral-strategies.com/10dayviralvfxpro
形式: VSL・動画 761s・US・Facebook／Instagram／Audience Network／Messenger／Threads・着地 Kajabiの長文セールスページ（先頭にWistia動画 10:22）
拾った日: 2026-09-12
稼働日数 / 成績: 109日 / score 81（GetHookd の黒箱。売上ではない）／ブランドの稼働広告数 1050本（2026-09-12）
選定: GetHookd で「勝ち（score 81〜100）・稼働中・動画」かつブランドの稼働広告数500以上。着地が実測でVSL（長尺の売り動画が主役のページ）（取得は GetHookd 内部API `POST /api/get-ads`・2026-09-12。集め方は [[_index]] の「11〜30 の集め方」）
出どころ記号: `T`=GetHookd文字起こし／`W`=ローカルwhisper large-v3-turbo（この本は GetHookd の文字起こしが空なので広告も `W`。全文は `ec/wiki/vsl-teardown/raw/102457232.full.txt`）／`F`=ローカルmp4から切った絵／`L`=LPページの実測（ブラウザ）／`J`=判断

## なぜ良いのか（1行）

売り物（動画エフェクト）を0秒から4つ実演して24秒で名前と再生数を言い切り、「if you're thinking」3回と「if you're worried」2回で反論5つを潰し、後半369秒（48.5%）を受講者の自撮り証言だけで埋める。 `J`

## 分解（9ブロック）

| ブロック            | 秒・出ている物・逐語                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hook            | 0:00–0:24 `W`「This is called the Fake Cliff Effect, and it just bought me another 15 seconds of your attention」→「This is called the Snap Effect, and it got my student Iris over 400,000 views」→Portal Effect→「Pole Transition Effect, and it got Jaren over 1.2 million views」。`F` 崖から落ちるふり→寿司の材料が指パッチンで寿司舟に変わる→レンガ壁に炎の輪→街灯の柱で服が変わる。黄色の大字幕「FAKE CLIFF EFFECT」「SNAP EFFECT」、9〜10秒は Iris のリール画面（▶400K）を横に出す |
| lead            | 0:24–0:32＋0:53–1:08 `W`「I'm one of the guys who did visual effects for `huge` Hollywood movie campaigns, like Guardians of the Galaxy, Thor, Ant-Man」→「how to use simple scroll-stopping effects like this to blow up on social media using just your phone」「you don't need all that complicated software」　they have strong authority just bc hes from hallywood                                           |
| discovery story | あり（創業者・21秒）0:32–0:53 `W`「developing carpal tunnel on both of my wrists」→「from socially awkward Hollywood editor to getting over 200,000 followers, 30 million views」「Meta, Adobe, CapCut, and TikTok, all in just 10 weeks」                                                                                                                                                                                |
| UMP             | 無し（原因に呼び名なし。症状だけ 1:31–1:35 `W`「get out of the 200 view, why does the algorithm hate me club」）                                                                                                                                                                                                                                                                                                              |
| UMS             | 3:11–3:28 `W`「a powerful psychological effect called a pattern interrupt to stop people mid-scroll」→「Like this.」（`F` 実演）。呼び名は一般語（pattern interrupt）で自分の呼び名ではない                                                                                                                                                                                                                                             |
| product reveal  | **あり** 1:08–1:50 `W`「my full database of copy-and-paste effects」→1:25「it's called 7-Day Viral Creator, where every day I show you how to add a new viral effect」                                                                                                                                                                                                                                           |
| price drop      | 金額なし（枠だけ）4:07–4:41 `W`「This sounds awesome, so it must be expensive」→「this course pays for itself 10 times over」→「73% less than your monthly coffee budget」。`F` 証言リールの上帯「FLASH SALE 90% OFF」                                                                                                                                                                                                               |
| risk reversal   | **あり**（日数なし）5:11–5:33 `W`「I'll refund your money」＋冗談「my marketing guy says I can't actually offer massages for legal reasons」                                                                                                                                                                                                                                                                              |
| testimonials    | 個人の声 `W` 名前と再生数5人 1:59–2:27（Reto 400,000／Mauricio 3.6 million／Clint 2 million／Megan 800,000／Victor 7.8 million）＋Jaren 本人映像 2:59–3:11＋数「over 23,000 members」2:31＋自撮り証言リール 6:32–12:41（`F` 34シーン）                                                                                                                                                                                                             |

無かったブロックは「無し」。欠落そのものが発見。

## 盗む所

- 売り物を0秒で実演し、名前と効き目を1文にする（「This is called the Fake Cliff Effect, and it just bought me another 15 seconds of your attention」）。同じ文型を4回で24秒
- 反論を「if you're thinking」3回（1:50 `too good to be true`／2:55 complicated／4:07 expensive）と「if you're worried」2回（2:18 niche too small／3:28 no time）の計5つ並べ、各反論の直後に人名と再生数を置く
- 広告が「終わった後」に証言リールを繋ぐ（6:24「Oh, hey, you're still here. You know the ad is over, right?」→6:32から369秒）。シーン平均は前半4.0秒（n=98）、証言リール10.8秒（n=34）

## フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

![[ec/wiki/vsl-teardown/絵/102457232-hook]]

## 全シーン × b-roll（`F`）

尺 761.0秒 ／ 132シーン ／ 平均 5.8秒 ／ しきい値 0.25（0:00–6:32 は98シーン・平均4.0秒、6:32以降の証言リールは34シーン・平均10.8秒）

![[ec/wiki/vsl-teardown/シーン/102457232]]

## LP（着地ページ）— viral-strategies.com/10dayviralvfxpro

**読む前に**: 動画でオファーを隠すページではなく、先頭に10分22秒の動画を置いた長文セールスページ（高さ 52,988px `L`）。値段とボタンは最初から見えている。LP動画は広告の短縮版で、後半の証言リールは広告と同じ文の並び。

| 項目 | 実測（`L`=LP、`W`=LP動画の文字起こし・whisper large-v3-turbo、`F`=30秒おきの絵） |
|---|---|
| URL | https://www.viral-strategies.com/10dayviralvfxpro （最終URLも同じ `L`） |
| 作り | Kajabi（ページ名「Viral VFX Bundle」）。コメント欄なし。声の枠は testimonial.to の埋め込み1つ（y=41852） |
| 動画 | Wistia `5dka8g3rh7`・内部名「[TEST] Viral VFX Main Value Video 6 (v4 but shortened) TN 17」・622.25秒（10:22）・y=421（見出しの直下、ボタン1の上）。ページ内の動画は他に2本: Wistia `51ehb240nc`「Organic_Manychat Tease Video」13秒（y=23661）／y=41376 の動画（blob再生・ホスト判定不能） |
| ページの部品（上から・y は幅1280の実測） | ①カウントダウン「91% SALE ENDS IN」（y=30）②見出し「Hollywood VFX Artist Finally Cracked Why the Algorithm Traps 96.4% of Videos Under 500 Views」＋「Scroll-Stopper formula to GO VIRAL & GET 10k-165k VIEWS PER DAY」③動画（Wistia 10:22）④ボタン1「YES! I'm Ready to Go Viral In My Niche & Grow My Audience! (SAVE 91% TODAY)」＋「Enroll before Sunday, September 13th」＋「33,000+ Students in Over 109 Countries」⑤ロゴ帯7社（Meta／Kajabi／Marvel Studios／CapCut／TikTok／Instagram／Disney）⑥星5つ＋短い声3件（Jaren A.／Lavonne P.／Phill N.）⑦長文の物語「I HAD 28 DAYS TO BUILD AN AUDIENCE… OR I COULDN'T FEED MY KIDS」（解雇→28日→Scroll-Stoppers→「Within days, it hits 735,000 views」）⑧「Proof this works in any niche」＋結果画像7枚 ⑨反論「But I'm not techy / I don't have time」⑩「My 14-day guarantee」⑪「Your choice: Post & pray… or use this proven system」＋ボタン2 ⑫できること＋HOW IT WORKS 3段 ⑬「7.8 MILLION VIEWS」＋13秒動画 ⑭価値の積み上げ（9項目・$1825）→$97＋ボタン3 ⑮中身（DAY 1〜7＋BONUS DAY 8〜10、BONUS COURSE #2〜#4、BONUS #5 AI、#6 App）＋ボタン4 ⑯全端末・全ニッチ・フォロワー不要 ⑰BUNDLE SALE BONUSES 5つ＋ボタン5 ⑱「Over 33,000+ Happy Students」＋動画＋testimonial.to＋ボタン6 ⑲Meet Your Instructor「Gained over 400k Followers and 30+ million Views in only 10 Weeks!」⑳中身の説明＋Who This Course Is For ㉑値段の再掲「$997 $497 $97 USD」One-Time Payment＋ボタン7 ㉒FAQ 10問（「Is There A Guarantee?」と「Is there a guarantee?」が重複して11行）＋ボタン8 ㉓免責（earnings disclaimer） |
| 売り場 | ボタン8個（n=8）が全部 `/resource_redirect/offers/kBSBh9un` → `/offers/kBSBh9un/checkout`（同ドメインの Kajabi 標準チェックアウト `L`） |
| 値段 | 「TOTAL VALUE: $1825」→「JUST $997」→「$497」→「$97」（One-Time Payment・SAVE 91%）の1択。チェックアウトは $97.00 USD＋注文バンプ「SPECIAL ONE-TIME OFFER… ($197) $59」Content Creator Asset Vault |
| 保証 | 14日返金（本文⑩・FAQ・チェックアウトの3か所） |
| 仕掛け | オファーは隠さない（ボタン8個と値段の塊2つが全部 v=1）。①のカウントダウンは取得時「00 DAYS 04 HOURS 31 MINS 15 SECS」（終わる時刻と再訪時の挙動は判定不能: 終了日時の設定値がHTMLに無く、実測1回）。④の日付は `tomorrow.setDate(tomorrow.getDate() + 1)` のJSで**毎回「明日」の日付を書く**（取得日 2026-09-12 の翌日 = Sunday, September 13th） |

### 広告 → LP のつながり

| 要素 | 広告（12:41） | LP動画（10:22）・ページ | 判定 |
|---|---|---|---|
| 餌 | 0:00 エフェクト4つの実演「This is called the Fake Cliff Effect」 | 動画 0:00「I'm going to show you how to get 10,000 to 165,000 views per day on social media」（`F` 1:00 からスマホ画面で実演）／ページ見出し「Traps 96.4% of Videos Under 500 Views」 | 餌は差し替え（実演→数字の約束） |
| 原因の呼び名 | 無し（「why does the algorithm hate me club」） | 動画 0:13「you have 1.8 seconds to visually grab your viewers」／ページ「It rewards attention.」 | 原因はLPで初めて付く |
| 解の呼び名 | 「pattern interrupt」「copy-and-paste effects」 | 動画「a simple technique」／ページ「Scroll-Stoppers」 | 呼び名が面ごとに違う（3面で3通り） |
| 権威 | Guardians of the Galaxy, Thor, Ant-Man／Meta, Adobe, CapCut, TikTok | 動画 0:34 同じ3作品・0:59 同じ4社／ページのロゴ帯7社 | 一致 |
| 数字 | フォロワー 200,000（0:44）／受講者 23,000（2:31、証言リールの帯は 33,000+）／Clint 2 million／Reto 400,000 | 動画 0:07「over 500,000 followers」と 0:52「200,000 followers」、受講者 18,000（2:06）／ページ「400k Followers」、33,000+、Clint 6.2 million、Reto 415,000 | **同じ人の数字が面ごとに違う**（フォロワー3通り・受講者3通り） |
| 約束 | 6:11「let's get your next reel to hit 1 million views」 | 動画 3:07 同じ文／ページ「10k-165k VIEWS PER DAY」 | 締めの文は逐語で引き継ぐ |
| 商品名 | 1:25「7-Day Viral Creator」 | 動画では出ない（「a short online course」）／ページ「7-Day Beginner Viral Creator」、URL「10dayviralvfxpro」／チェックアウト「Viral VFX (Pro Bundle)」 | 名前が4通り |
| 値段 | 金額なし。「73% less than your monthly coffee budget」／帯「FLASH SALE 90% OFF」 | 動画も金額なし「the course is on sale right now」／ページ $97（SAVE 91%） | 金額はページだけ。％が 73（コーヒー代との比）／90／91 の3通り |
| 保証 | 「I'll refund your money」日数なし | 動画「without any risk on your shoulders」／ページ14日 | 日数はページだけ |

### LP動画の構成（8節）

| # | 秒 | 節 | 何をしている（逐語 `W`） | 絵 `F` |
|---|---|---|---|---|
| 1 | 0:00–0:34 | hook（数字の約束） | 「how to get 10,000 to 165,000 views per day on social media, even if your account's small」「from completely unknown to over 500,000 followers」「you have 1.8 seconds to visually grab your viewers」「Like you're doing with this video, right now」 | 居間で話す本人 |
| 2 | 0:34–1:07 | 権威と物語 | 「As a visual effects artist in Hollywood」「I exploded with over 200,000 followers and 30 million views in just 10 weeks」「Meta, CapCut, Adobe, TikTok」 | カメラと照明の並ぶ机で編集する本人 |
| 3 | 1:07–1:27 | 商品（名前なし） | 「I put them into a short online course」「no matter what niche you're in, even whatever this is」 | スマホ画面3枚の実演 |
| 4 | 1:27–2:06 | 受講者の結果 | Reto 400,000／Mauricio 3.6 million／Megan 800,000／Victor 7.8 million→「it's all 100% beginner-friendly」「using just your phone and a free app」→Jaren 本人 1:59 | 黒シャツの男・炎の輪の分割画面 |
| 5 | 2:06–2:26 | 数 | 「We have over 18,000 students in every niche you can think of」 | 炎の輪の分割画面 |
| 6 | 2:26–3:12 | オファー（金額なし）＋CTA | 「without any risk on your shoulders」「the course is on sale right now」→ボーナス4つ（branding blueprint／follower growth formula／VFX Creators app／AI personal assistant）→3:07「Click the link below」 | 黄色地に App Store／Google Play のバッジ |
| 7 | 3:12–9:16 | 証言リール | 「Thank you, Tyler, for your course」→「My views have quadrupled」→「I feel like you're almost robbing him」→「it's worth the investment」。広告 6:32–12:41 と同じ文の並び | 星5つの枠、左に証言者の顔・右にその人のリール画面（広告版の「FLASH SALE」帯は無い） |
| 8 | 9:16–10:22 | エンドカード | 発話なし（whisper の「We'll be right back.」×2 は無音部の誤認識と判断 `J`） | 「CLICK THE LINK BELOW TO GO VIRAL NOW!」 |

商品名が初めて出る秒: 出ない（動画内 n=0 回。ページとチェックアウトにだけある）。値段を初めて言う秒: 言わない。

### 売り場までの導線

ファネル: 広告（12:41）→ LP（Wistia 10:22・オファーは隠さない＝0秒から見える）→ ボタン8個（行き先は全部同じ）→ Kajabi チェックアウト `/offers/kBSBh9un/checkout`（$97＋注文バンプ $59）→ 決済（同ドメインの Kajabi）

1. 動画を見なくても買える。ボタン1（y=835）は動画の真下
2. ボタンの文言は8個とも「(SAVE 91% TODAY)」で終わる
3. チェックアウトは2段フォーム（Personal Information→Billing Information）。$97.00 USD、注文バンプ $59（元 $197）、ギフト送付の選択肢、「14-Day Money-Back Guarantee!」、「33,000+ Happy Members!」、声3件（Jaren A.／Lavonne P.／3件目は `dia read` の6000字打ち切りで名前が取得失敗）
4. PDP・カート・外部決済（SamCart 等）は無い。ページ→チェックアウトの2段
5. 期限の日付は④のJSで毎日「明日」に書き換わる

### コピーする時の骨（比率は広告12:41とLP動画10:22の実測）

広告: hook 3.2%（実演4つ）→ 権威＋創業者 3.8%→ lead 2.1%→ product reveal 5.5%（1:25 名前）→ 反論1〜2＋人名と再生数 8.5%→ 反論3＋Jaren 本人 2.1%→ UMS（pattern interrupt）2.2%→ 反論4（時間）＋lifetime access 5.1%→ 反論5（値段）＋セール＋ボーナス 8.0%→ 保証 3.3%→ クローズ 5.6%→ NG集＋「the ad is over」2.2%→ **証言リール 48.5%**。

LP動画: hook 5.5%→ 権威 5.4%→ 商品（名前なし）3.2%→ 結果 6.3%→ 数 3.2%→ オファー＋CTA 7.4%→ **証言リール 58.3%**→ エンドカード 10.6%。「if you're thinking／if you're worried」の言い回しは広告5回（thinking 3・worried 2）、LP動画0回。

絵の実物: `ec/wiki/vsl-teardown/frames/LP-102457232/sheet0.jpg`（0:00〜10:00）。文字起こし全文: `ec/wiki/vsl-teardown/raw/LP-102457232.full.txt`（秒つきは `.segments.json`）。

![[ec/wiki/vsl-teardown/frames/LP-102457232/sheet0.jpg]]
