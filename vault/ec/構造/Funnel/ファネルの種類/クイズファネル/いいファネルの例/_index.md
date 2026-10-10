<!-- 例 -->
# いいファネルの例 — クイズファネル12本（2026-09-11・US・score 86〜100）

読む人: クイズファネルを作る前に、勝っている本の実物を1本ずつ見たい人。
読む時: 質問の数・幕間の置き方・結果の出し方・値段を出す位置を決める時。
読まなくていい条件: 横断表と広告の絵だけ要る時は `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

1件1ノート。各ノートに GetHookd リンク・LP・広告の9ブロック分解・フック13枚（1秒刻み）・全シーンの絵・クイズ全問・結果・オファー・導線が入っている。**優劣を付けない**（クライテリアを通った時点で全部勝っている）。

集め方（`ec/wiki/quiz-teardown/criteria.json`）: GetHookd の内部API（ログイン済み Dia タブから fetch・MCP不使用）で `page_type=quiz_page`・`ad_format=video`・`performance_scores=winning,optimized`・`status=active`・`ads_per_brand_limit=2`・尺1分以上。3,320件（上限値）→ ブランド1本・英語・score 86〜100・着地が実測でクイズの12本。落選1本: The Kitchen Safety Expert（Plateful）（GetHookdは着地を quiz_page と分類しているが、実測の着地は go.plateful.co/lis-pan-v1-exp/ の記事型（「10 Shocking Reasons Families Are Switching To This Expensive Titanium Pan」）で、クイズは無い。動画（14:23・score 100・稼働120日）と絵は raw/frames に残してある。）

| # | ノート | 症状／商品 | score／日 | 広告の尺 | 問数 | 型 |
|---|---|---|---|---|---|---|
| 01 | [[01 NeuroMD（腰痛（NMES装置））]] | 腰痛（NMES装置） | 100／148 | 17分54秒 | 5問（＋入口の13択）・幕間0・失格1 | 適格審査型（Am I a candidate） |
| 02 | [[02 Zafira Organics（GLP-1の無気力（サプリ））]] | GLP-1の無気力（サプリ） | 100／148 | 6分16秒 | 24問（QUESTION n OF 24 と%を常時表示）・幕間1（18問目の後） | 診断スコア型（24問・進捗%） |
| 03 | [[03 V Shred（Taylor Wilson）（男性の減量（体型診断→講座））]] | 男性の減量（体型診断→講座） | 100／133 | 5分10秒 | 6問（広告の「six different questions」と一致）・幕間0・メール欄なし | 体型診断→VSL型（クイズの出口がVSL＋$57） |
| 04 | [[04 KilgourMD（Jean Creates）（更年期の抜け毛（頭皮美容液））]] | 更年期の抜け毛（頭皮美容液） | 100／136 | 4分33秒 | 9問（入力1）・幕間0・結果の後に説明7枚 | 教育インタースティシャル型（結果の後に説明7枚） |
| 05 | [[05 Lovy（UroControl）（尿もれ（サプリ））]] | 尿もれ（サプリ） | 100／32 | 4分58秒 | 13問（入力1）・幕間6（うち1枚は回答で文言が変わる）・レポート1 | 割引請求型＋レポート（Claim your $110 discount → Bladder Report） |
| 06 | [[06 CanineDrops（Riverside Veterinary）（犬の白濁した目（サプリ））]] | 犬の白濁した目（サプリ） | 100／83 | 4分25秒 | 8問（スライダー1）・幕間1・メールゲート1 | 結果を診断名で4分岐＋メールゲート |
| 07 | [[07 Necklo（猫背・首こり（アプリ））]] | 猫背・首こり（アプリ） | 100／87 | 3分20秒 | 13問＋メール・幕間5 | アプリ課金（BetterMe型）・プラン3段 |
| 08 | [[08 Saphire（Dr. James Harper）（子どものADHD（サフラングミ））]] | 子どものADHD（サフラングミ） | 100／108 | 3分39秒 | 8問・幕間2（見出し無し） | 心理エスカレーション型（絶望度を聞く） |
| 09 | [[09 Sculpiflex（Christy Matis）（下腹の脂肪・セルライト（3-in-1装置））]] | 下腹の脂肪・セルライト（3-in-1装置） | 90／53 | 12分59秒 | セルライト路で13問・幕間4・プロフィール1（他4路も同型。静的HTMLで36問） | 分岐型（悩み別5ルート） |
| 10 | [[10 Seranova（Stephanie Edwards）（シワ・たるみ（マイクロインフュージョン））]] | シワ・たるみ（マイクロインフュージョン） | 100／35 | 4分08秒 | 17問（入力1）・幕間2以上（27段） | 物語（復讐）→テンプレ型クイズ（Claim Your $171 Discount） |
| 11 | [[11 Aurora Skin（たるみ（7-in-1 LED sculptor））]] | たるみ（7-in-1 LED sculptor） | 100／22 | 4分06秒 | 7問・幕間5（12画面） | Seranovaと同一台本＋RevenueHunt（Shopifyアプリ）の12画面 |
| 12 | [[12 Miami MD（Dr. J）（口元のシワ（クリーム））]] | 口元のシワ（クリーム） | 86／95 | 9分53秒 | 10問・幕間4 | 医師VSL→スキップ可のクイズ（SKIP THIS QUIZ） |

## 12本で数えた結果（n=12・2026-09-11実測）

| 見る所 | 数 |
|---|---|
| 広告の尺 | 3分20秒〜17分54秒。10分超が3本（NeuroMD 17:54／Sculpiflex 12:59／Miami MD 9:53）、残り9本は3〜6分 |
| 広告の hook | 12/12 |
| 広告の UMP（原因の名指し） | 11/12（無し: KilgourMD。Aurora は「43の表情筋が弱る」の一文だけ） |
| 広告の UMS（呼び名） | 11/12（無し: KilgourMD） |
| 広告で金額を言う | 2/12（Sculpiflex「Less than $120」・Miami MD「$40 each」） |
| 広告で保証を言う | 8/12 |
| 質問数 | 5〜24問。中央値 9〜10問。入力型（年齢・身長・日付）を含むのが5本 |
| 幕間（教育カード） | 9/12 が持つ。0枚: NeuroMD（失格だけ）・V Shred・KilgourMD（結果の後に7枚） |
| メールゲート | 3/12（NeuroMD・CanineDrops・Necklo）。V Shred は「メールを聞かない」と広告で言う |
| 結果の型 | スコア／レポート 4（Zafira・Lovy・Sculpiflex・KilgourMD）／診断名で分岐 1（CanineDrops）／日付つき約束 3（Lovy・Seranova・Miami）／合格通知 3（NeuroMD・Aurora・Miami）／VSL 1（V Shred）／無し 1（Saphire） |
| 出口 | 専用オファーページ 6（NeuroMD・Miami・Sculpiflex・KilgourMD・V Shred・Necklo）／Shopify商品ページ 5（Seranova・Saphire・CanineDrops・Lovy・Aurora）／店トップ 1（Zafira） |
| 値段の型 | 装置1択 $149.95／$149.99（NeuroMD・Aurora）／講座 $57 買い切り／アプリ 6か月 $39.99／サプリ $54.90〜$69.99 の本数段／クリーム $40〜$49 の瓶数段／美容液 $330/3か月の定期 |
| 保証 | 90日 4（Lovy・Seranova・KilgourMD・CanineDrops広告）／60日 4（NeuroMD・Zafira・Saphire・Miami）／30日 3（Sculpiflex・V Shred・CanineDrops店）／無し 1（Necklo）／判定不能 1（Aurora） |
| 割引の名目 | クイズで得た権利として出す 7（NeuroMD・KilgourMD・Aurora・Lovy・Seranova・CanineDrops・Miami）／セールかタイマーだけ 3（Sculpiflex・Saphire・Necklo）／割引なし 2（Zafira・V Shred） |
| 広告の語り手がクイズか売り場に出る | 2/12（V Shred の Vince Sant・Miami MD の Dr. J） |
| 分析の範囲 | 回答は各画面で1通りだけ選んで歩いた。分岐の中身まで読んだのは NeuroMD・Aurora（定義JSON）と CanineDrops（診断名4種）。Sculpiflex の他4ルートは問いの文だけ |
| タイマー | 6/12（NeuroMD 10:00／V Shred 10:00／KilgourMD 1:24:xx／Saphire 3:00／Necklo 8:37／Miami なし・Seranova・Aurora は「LABOR DAY SALE」） |
| 同じ制作テンプレ | 4本（Lovy・Sculpiflex・Seranova・Aurora）が同じ文言（「Take This 1-Minute Quiz To Claim Your $X Discount!」「You are in the right place!💪」「Do you have an important event coming up?」「Now／Your Goal」「by 日付」）。Miami の幕間も同じ言い回し |
| 同じ台本 | Seranova と Aurora は広告の物語が逐語で同じ（別ブランド・別商品・同日稼働） |
| クイズの作り | 自前 6／heyflow 3（CanineDrops・Sculpiflex・Seranova）／RevenueHunt 2（NeuroMD・Aurora）／自前React 1（KilgourMD） |

読めていること（n=12）:

- **クイズは原因を教える場所ではない。** 原因（UMP）は広告が言い、クイズは「あなたの状態」を数字や名前で返す。幕間は反論処理（試した物が効かない理由・$1,000超の治療・忙しい）に使う
- **値段は広告で言わず、結果の後に出す。** 12本中10本が結果画面かオファーページで初めて金額を出す。出す時は「あなたは対象」「あなたの一致が解除した」と権利の形にする（7/12。NeuroMD 62%・KilgourMD 38%・Aurora 60%）
- **結果に日付を入れる型が3本。** 「by 12/10/2026」「September→December」のように、回答した日から3か月後を刻む
- **質問は5〜24問で幅がある。** 短い本（NeuroMD 5・V Shred 6）は広告が10分超か、クイズが体型計算。長い本（Zafira 24）は広告が自撮り6分で、教育をクイズ側に寄せている
- **同じテンプレが4本＋同じ台本が2本。** 制作会社の型をそのまま使っているので、作るのはクイズでなく「差し替え表」（症状語・選択肢・日付・割引額）

## LP（着地）横断表 — 広告の先で何が起きるか

| # | ブランド | クイズの作り | 問数 | 結果 | 値段の段 | 保証 | 売り場 |
|---|---|---|---|---|---|---|---|
| 01 | NeuroMD | 入口: Shopify | 5問（＋入口の13択）・幕間0・失格1 | 結果ページは無い。5問目のメール入力がそのまま「合格」画面（62% OFF・87%一致）。送信で `offer.getneuromd.com… | 1台 $149.95（定価 $399.99・62%OFF）。装置の1択。関連品は NeuroMD Restore $44.99〜（店） | 60日（結果が出なければ返金）＋1年保証 | （13択）→Check Eligibility→クイズ5問→メール→オファーページ→Shopifyカート→チェックアウト |
| 02 | Zafira Organics | 入口・質問: 自前（fbq） | 24問（QUESTION n OF 24 と%を常時表示）・幕間1（18問目の後） | 「Analyzing your responses... Over 12,000 women have taken this assessm… | 1本 $54.90（元$59.90）／2本 $92.50／3本 $119.60（店の products.json）。段は1/2/3本 | 60日・返品不要 | 広告→入口（Start）→24問→結果→教育5枚→店トップ→ADD TO CART→カート→チェックアウト |
| 03 | V Shred | 自前（Cloudflare） | 6問（広告の「six different questions」と一致）・幕間0・メール欄なし | 結果ページがそのままVSL: le.vshred.com/sp/survey/male-fl「Celebrity Trainer Vince… | $57 買い切り（講座＋ボーナス7）。1択 | 30日 | 広告→クイズ6問→VSLページ（$57）→自前チェックアウト |
| 04 | KilgourMD | Shopifyページ＋自前React | 9問（入力1）・幕間0・結果の後に説明7枚 | 「Why Your Answers Point To A Faster-Ageing Scalp」（MARKER 1 Shedding Ph… | 3か月 $330（$110/月）／1か月 $127.50。定期が既定。買い切りは別価格（2 Pack $160.20〜） | 90日・返品不要 | 広告→クイズ9問→説明7枚→結果ページ（値段）→Shopifyカート→チェックアウト |
| 05 | Lovy | 自前（heyflow風の静的HTML） | 13問（入力1）・幕間6（うち1枚は回答で文言が変わる）・レポート1 | 9問目の後に「Your Personal Bladder Report／Bladder Vulnerability Score: High」… | 定期 $40.80／買い切り $54.40（定価$79.99）。products.json では1本 $29.99（元$59.98） | 90日 | 広告→クイズ13問＋幕間6→レポート→結果→（遷移が壊れている）→店の商品ページ→カート→チェックアウト |
| 06 | CanineDrops | heyflow | 8問（スライダー1）・幕間1・メールゲート1 | 「Analysing your answers… matching your dog's eye profile…」→「Your perso… | 1本 $69.99（元$139.99）・3本で1本無料。段は本数 | 広告・クイズ 90日 → 店 30日（不一致） | 広告→入口→8問→名前・メール→診断名→CTA→店の商品ページ→カート→チェックアウト |
| 07 | Necklo | 自前（React） | 13問＋メール・幕間5 | 「Your plan is ready!／400.000+ People Have Already Chosen Necklo App／Si… | 6か月 $39.99／3か月 $24.99／1か月（アプリの定期）。段は期間 | 無し（表示なし） | 広告→クイズ13問＋幕間5→メール→プラン3段→決済 |
| 08 | Saphire | 自前（quiz.trysaphire.com） | 8問・幕間2（見出し無し） | 「Analyzing your child's behavioral patterns…」→ 100%「CLAIM MY OFFER」のボタ… | 1袋 $54.95（元$65.00）／3-Pack $95.95（元$179.85）（products.json）。B2G1 の段 | 60日 | 広告→クイズ8問＋幕間2→CLAIM→Shopify商品ページ→カート→チェックアウト |
| 09 | Sculpiflex | heyflow | セルライト路で13問・幕間4・プロフィール1（他4路も同型。静的HTMLで36問） | 8問目の後に「Summary of your Skin Profile／Skin Texture Deterioration: High／H… | 68%OFF（定期）／60%OFF（買い切り）。金額は通貨で表示（日本からはJPY表示で読めず）。広告は「Less than $120」 | 30日 | 広告→クイズ13問＋幕間4→プロフィール→（redirect）オファーページ→ADD TO CART→チェックアウト |
| 10 | Seranova | heyflow（quiz.seranova.com） | 17問（入力1）・幕間2以上（27段） | 「Based on your answers: You Are Just 3 Months Away From Younger Lookin… | 3か月 ¥19,800（元¥46,500）／2か月／1か月（JPY表示・USD未取得）。段は治療回数 | 90日 | 広告→クイズ17問＋幕間→結果→CLAIM→Shopify PDP→カート→チェックアウト |
| 11 | Aurora Skin | Shopify＋PageFly＋RevenueHunt v2（Shopifyアプリ） | 7問・幕間5（12画面） | 「Based on your answers, we know...／You'll see real, visible changes in… | 1台 $149.99（元$374.99）＋美容液を無料で付ける。1択 | 判定不能（広告の文字起こしが崩れ、店の表記を取れていない） | 広告→クイズ7問＋幕間5→結果（60%OFF）→Claim→Shopify商品→カート→チェックアウト |
| 12 | Miami MD | 自前（offer.trymiamimd.com） | 10問・幕間4 | 「Congratulations, you qualify for our biggest discount. ✅ Our Lift & F… | 3瓶 $40/瓶／2瓶 $43／1瓶 $49（定期は$36/$39/$44）。段は瓶数 | 60日 | 広告→クイズ10問＋幕間4→結果→CLAIM→オファーページ（3段）→自前チェックアウト |

## 日本の実物（13〜18・2026-10-10・JP）

一覧と共通の骨組みは [[_日本の実物_2026-10-10]]。日本は「記事＋アンケート3問＋回答のお礼で割引」が6本中5本。

| # | ノート | 型 |
|---|---|---|
| 13 | [[13 BODY-VO（ファーマフーズ）（デリケートゾーンのかゆみ（塗り薬））]] | 記事＋アンケート3問 |
| 14 | [[14 てんらい黄望皇（ファーマフーズ×明治薬品）（尿もれ・頻尿（漢方））]] | 記事＋チェック6項目＋アンケート3問 |
| 15 | [[15 YURiiRO（E-seeds）（デリケートゾーンのニオイ（香水オイル））]] | 漫画の記事＋3問／7問の香り診断 |
| 16 | [[16 生漢煎 防風通聖散（ジェイフロンティア）（お腹の脂肪・肥満症（漢方））]] | 記事＋3問（画像）／2択4問のタイプ診断 |
| 17 | [[17 からだかがみ（クラシエ 漢方セラピー）（体質の不調（漢方））]] | 9問の多問診断・8タイプ・値段なし |
| 18 | [[18 らでぃっしゅぼーや（お試しセット）（野菜の宅配・農家応援）]] | 記事＋3問／記事なし・問いの間に動画 |
