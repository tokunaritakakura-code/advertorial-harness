# C 競合の地図（針マット・商品理解の基盤）

作成：2026-10-07。対象：日本向けに Meta 広告で売る「針マット」（指圧マット＋枕＋袋）。
この文書は調査記録。広告・LP・配信設定には触っていない。

表記のルール
- **【事実】**：販売ページ・比較記事・第三者の広告追跡サイトで確認したこと。原文はそのまま引用。
- **【推測】**：事実からの読み取り。競合の売上・CPA・ROAS は1件も取っていない。
- 原文と値段の一覧は `C_根拠データ/広告と見出しの原文_20261007.md`。

---

## 結論（先に）

1. **日本で同じ商品を「ブランドとして」売っているのは Shakti Japan だけ【事実：見た範囲】。** 18,000〜59,000円、60日のお試し＋5年保証、レビュー39,592件。言っていることは「ストレス・リラックス・古代インドの知恵」で、腰痛の原因の話はしていない。
2. **その下に、モールの無名品（枕・袋つきで 1,790〜5,980円）がある【事実】。** 売り文句は寸法・突起の数・セットの中身で、だれに向けた話かが無い。うちの見積もりと同じ型（68×42cm・枕・袋）はこの帯にいる。
3. **まん中（6,000〜17,000円）にブランドがいない【事実：見た範囲】。** モール品の上限 5,980円と Shakti の下限 18,000円のあいだ。
4. **世界の最大手 Shakti Mat の広告は、4本とも「リラックス」の話【事実】。** 「最初の数分は痛い → そのあと深くゆるむ」「20分・家から出ない」「39K の5つ星」「60日お試し」。静止画で、着地はトップページか商品ページ。記事には着地させていない。
5. **「慢性腰痛の原因は筋肉の酸欠」「湿布は届いていない」という原因からの話をしている競合は、見た範囲では0【事実】。** 同じ商品の売り手（Shakti・Pranamat・Bed of Nails・モール品）にも、代わりの対策の販売ページ（マットレス・マッサージガン・湿布・整体）にも無かった。
6. **日本の Meta 広告は1本も見られていない。** GetHookd は実行の許可が出ず、Meta 広告ライブラリは読めなかった。5 の「0」は販売ページと海外の広告4本の範囲での話で、日本の配信中の広告の中に同じ話があるかは**まだ分からない**。

---

## 調べた範囲と限界

| 道具 | やったこと | 結果 |
|---|---|---|
| GetHookd（MCP） | `get_user_profile`、`search_ads`（acupressure mat） | **2つとも Permission denied。1本も取れていない。** クレジットの残りも見られなかった |
| Meta 広告ライブラリ | WebFetch で 国=JP「指圧マット」「シャクティマット」 | **2回とも socket hang up。読めなかった** |
| 統一 Chrome | 起動の確認 | Bash が Permission denied。使えなかった |
| brandsearch.co | Shakti Mat の3ドメイン | 取れた。広告の文面4本と集計 |
| brandsearch.co | Pranamat・Bed of Nails・Ajna・Shakti Japan | すべて 404 |
| 販売ページ | Shakti Japan・Shakti 米・Pranamat・Bed of Nails・NELL・モットン・カラダファクトリー | 取れた |
| 販売ページ | shaktimat.jp・pranamat.jp・MYTREX・ロキソニン・フェイタス | 取れなかった（接続拒否・ドメイン無し・404） |
| Amazon.co.jp・楽天の検索結果 | WebFetch | Amazon 503、楽天 403。**上位の一覧は直接取れていない。** 比較サイト（mybest・360LiFE）の一覧で代えた |
| AliExpress | 検索結果2ページ | 取れた（題と値段と売れた数） |

**見た広告の数**
- Meta 広告の文面を確認：**4本**（すべて Shakti Mat・英語・静止画。第三者サイト経由）
- 日本語の Meta 広告：**0本**
- 目標の30本に対して4本。残りは販売ページの見出しで代えた（同じ商品10社、代わりの対策6社）。**販売ページの見出しは広告ではない**ので、「広告を見た」数には入れていない。

---

## 1. 同じ商品（指圧マット）

### 1-1 日本

| 競合 | 値段・セット | 訴求（見出しの原文） | フック | ねらっている層 | 着地 | 保証 | 出典 |
|---|---|---|---|---|---|---|---|
| **Shakti Japan（シャクティマット）** | クラシックマット 18,000円／クラシックピロー 9,500円／究極のシャクティセット（マット＋枕）26,125円（定価 27,500円）／プレミアムマット 25,000円／プレミアムセット 38,000円（定価 40,000円）／プレミアムフルボディーセット 53,100円（定価 59,000円）。Amazon のセールで 15,675円・22,500円の時あり | 「現代のストレスに、古代の知恵を」「インド発祥、一瞬でリラックスできる指圧 ＆ ウェルネスツール」「素肌で20分以上使うのが最も効果的」 | 「★★★★★ 39,000件の認証済み5つ星レビュー」。強さ3段階（ライト・オリジナル・アドバンス）。インドの職人の手作り | 【推測】ストレス・寝つき・こりを感じている、セルフケアにお金を出す層。百貨店のポップアップ、美容誌（MAQUIA）、ギズモード・ライフハッカーの記事に出ている【事実】。腰痛の人に向けた見出しは無い | 商品ページ（自社 Shopify）。Amazon・レンタル（Rentio）もあり。日本の広告の着地は**取れなかった** | 60日間のお試し（返品の送料は客の負担）＋5年間保証 | https://www.shaktimat.co.jp/ 、https://www.shaktimat.co.jp/collections/all 、https://www.shaktimat.co.jp/pages/how-to-use |
| **BODY RAJA（MRG JAPAN）「シャクティ指圧マット」** | 値段は**取れなかった**。ロングタイプ（約129.5×40cm）＋枕＋収納袋。強さ3種類（突起 0.3／0.5／0.7cm） | 「シャクティ指圧マット ロングタイプ」「従来タイプの約2倍」 | シリーズ累計8,900枚突破（2026-02-16〜09-14）。「全身に使うには少し短い」の声から開発 | 【事実】「セルフケアを自宅で手軽に取り入れたい層」「初心者から刺激を求める経験者まで」 | Amazon・楽天・Yahoo!ショッピング | 取れなかった | https://netshop.impress.co.jp/r/prtimes/items/000000016.000153567 |
| **TKクリエイト プリマソーレ** | 3,680円。68×42×2cm、枕・収納袋 | （商品名のみ）「アキュプレッシャー マット」 | — | 【推測】値段で選ぶモールの客 | モールの商品ページ | 取れなかった | https://my-best.com/17474 |
| **WIDEN** | 4,980円。120×42×2cm（ロング）、枕・収納袋 | — | 長さ | 同上 | モールの商品ページ | 取れなかった | 同上 |
| **ErgoStep リフレッシュマット** | 5,980円（mybest）／4,980円（360LiFE）。65×42×2cm、突起7,749個、枕・収納袋 | 「全身リフレッシュマット」 | 突起の数 | 同上 | モールの商品ページ | 取れなかった | 同上、https://360life.shinyusha.co.jp/articles/-/54578 |
| **Energy Product** | 4,180円。68×42×3cm、枕・収納袋 | 「指圧マット 枕セット」 | — | 同上 | モールの商品ページ | 取れなかった | https://my-best.com/17474 |
| **Vilom** | 3,100円。66×42×2cm、枕・収納袋 | 「指圧スパイクマット」 | — | 同上 | モールの商品ページ | 取れなかった | 同上 |
| **Bindo** | 1,790円。66×42×2cm、枕・収納袋 | 「指圧マット枕セット」 | 値段 | 同上 | モールの商品ページ | 取れなかった | 同上 |
| **JON TORUDO／monotone／ハリネズミストア** | 3,980円／2,590円／1,630円。マットのみ（62×38cm、128×42cm、62×38cm） | 「指圧マット 鍼クッション」「折り畳み式マット」「針刺マッサージマット」 | 値段・折りたたみ | 同上 | モールの商品ページ | 取れなかった | https://360life.shinyusha.co.jp/articles/-/54578 |
| **PLEAVIT** | 約6,910円（フリマ・オークションの出品の値段） | 「【極上 整う体験】つぼ押しマット 指圧 マッサージシート 寝て10分 無数の指圧刺激 ストレス解放」 | 「寝て10分」「整う」 | 【推測】サウナの「整う」に反応する層 | Amazon（出品タイトルから） | 取れなかった | https://auctions.yahoo.co.jp/jp/auction/1237678161 （検索結果の表示） |
| **RelaxBax（Makuake・2020年に終了）** | 13,860円（応援購入 11,190〜12,480円）。3つに分かれるマット、綿とココナッツ繊維 | 「指圧マットで心地の良いマッサージ！毎日のリラックスタイムに「RelaxBax」」 | 「1日15分」、足裏 | 【事実】オフィスワーカー、主婦、アスリート、睡眠を良くしたい人 | Makuake のプロジェクトページ | — | https://www.makuake.com/project/relaxbax/ |
| **Pranamat ECO（プラナマット）** | 日本語の公式サイト・円の値段は**見つからなかった**（pranamat.jp はドメイン無し）。海外：Mat + Pillow $270（$360 から）〜 4点セット $620 | "UNLOCK YOUR BODY'S STRENGTH AND NATURAL VITALITY"／"Premium Massage Mats for Daily Recovery" | "93% experienced significant relief after a daily 20-minute massage"。特許の蓮の形、接着剤なし、OEKO-TEX、麻とココナッツ繊維 | 【推測】自然素材にお金を出すウェルネス層 | 商品ページ（自社サイト） | 30日のお試し＋5年保証 | https://www.pranamat.com/ |
| **Bed of Nails** | 日本での販売・円の値段は**見つからなかった**。海外：マット $79.95、枕 $49.95、ECO セット $185.00 | "The Original Premium Acupressure Brand" | 2008〜2009年創業の「元祖」 | 【推測】美容・ライフスタイル店の客（Cult Beauty・Free People・Beauty Bay で販売【事実】） | 商品ページ（自社サイト・美容の小売店） | 60日の返金保証 | https://www.bedofnails.org/ |
| **AliExpress の同型** | ¥170〜¥6,847（枕セット。売れた数 14〜2,000+） | 「指圧マットと枕セット 筋肉リラックス」「自宅での筋肉の緊張緩和に最適」 | 値段 | 最安を探す層 | AliExpress の商品ページ | — | https://www.aliexpress.com/w/wholesale-acupressure-mat-pillow-set.html |

**この区分から読めること**
- 値段は3つの帯に分かれる【事実】：**モール品 1,630〜5,980円**／**Makuake・PLEAVIT 約6,900〜13,860円**／**Shakti 18,000〜59,000円**。
- Shakti は「ストレス・リラックス・寝つき」で売り、モール品は「寸法・個数・セット」で売る。**「腰が痛い人」に向けて、原因から話している売り手がいない**【事実：見た範囲】。
- うちの見積もり（枕＋マット＋袋 $15.40）と同じ型は、日本では 1,790〜5,980円で並んでいる【事実】。同じ見た目で値段を上げるには、モール品が言っていない話（だれの・どの悩みの・なぜ）が要る【推測】。

### 1-2 海外（US/EU）の勝ち広告・フック

「勝ち」の判定ができたのは Shakti Mat だけ（配信中の Meta 広告 966〜1,023本、EU/UK の費用 €394〜399K、S2 は「top spender」の表示）【事実】。ほかのブランドは広告の文面が取れなかったので、販売ページの売り文句をフックとして並べた。

| # | ブランド | フック（原文） | 型 | 種類 | 出典 |
|---|---|---|---|---|---|
| 1 | Shakti Mat | "The most relaxing thing I do all day"／"Yes: this is what real relaxation looks like. It hurts, but it works." | 痛いのに効く（逆説） | **Meta 広告・静止画・費用が最大** | https://brandsearch.co/brands/shaktimat.com |
| 2 | Shakti Mat | "Feel better faster"／"What's more shocking? Finally feeling relaxed, or finally feeling like you can unwind in 20 minutes without leaving the house?" | 問いかけ＋20分・家で | **Meta 広告・静止画** | 同上 |
| 3 | Shakti Mat | "Stop feeling sore"／"When your body clenches, this releases the pressure. The spikes press against tight muscles and force them to relax." | 筋肉のこわばり → 力ずくでゆるめる | **Meta 広告・静止画** | 同上 |
| 4 | Shakti Mat | "The To-Go Acupressure Footpad is like a shot of espresso for your soles..." | たとえ（エスプレッソ） | **Meta 広告・静止画** | https://brandsearch.co/brands/shaktimat.co.uk |
| 5 | Shakti Mat | "39K 5-star reviews say you're not crazy to think this can turn tired, sore and stressed into relaxed, restored and reset."／"try it risk-free for 60 days" | 数の証拠＋お試し | Meta 広告の本文の締め（1〜3に共通） | 同上 |
| 6 | Shakti Mat | "The first few minutes of lying on spikes is the hardest thing you'll do. After that, you'll wonder why you didn't get on them sooner." | 最初の数分の壁 | 販売ページ | https://www.shaktimat.eu/collections/acupressure-mats-and-pillows-1/products/premium-acupressure-mat-limited-edition-level-4 |
| 7 | Shakti Mat | "Getting a massage every day probably isn't on the cards… but lying on a Shakti Mat could be! Your back is covered in natural reset buttons…" | 毎日のマッサージの代わり／背中のリセットボタン | 販売ページ | https://shaktimat.eu/collections/all-acupressure-products/products/shakti-acupressure-mat |
| 8 | Shakti Mat | "ANCIENT SOLUTIONS TO MODERN TENSION" | 古代の知恵 × 現代の緊張 | 販売ページの見出し | https://www.shaktimat.com/ |
| 9 | Pranamat ECO | "93% experienced significant relief after a daily 20-minute massage"／"100% fall asleep faster, enjoy deeper sleep, wake refreshed" | 数字の証拠 | 販売ページ | https://www.pranamat.com/ |
| 10 | Pranamat ECO | "RELIEVE LOWER BACK PAIN Effective and totally natural treatment for lower back pain" | 腰痛を名指し | 自社サイトの広告文（2016年。英国 ASA の裁定に引用） | https://www.asa.org.uk/rulings/pranamat-sales-marketing-sia-a15-317274.html |
| 11 | Pranamat（チェコ） | "First-try acupressure mat: 5 min vs 20 min check-in"／"Night routine: mat + pillow wind-down for relaxation" | 初めての体験を5分と20分で比べる／夜の習慣 | クリエイターへの企画の依頼（広告ではない） | https://app.grin.ai/brands/pranamat.cz |
| 12 | Bed of Nails | "The Original Premium Acupressure Brand"／"invigorating at first, followed by a feeling of warmth and relaxation" | 元祖 | 販売ページ | https://www.bedofnails.org/ |

**海外から読めること**
- 最大手の今の広告は**静止画 × トップページ着地 × リラックス**【事実】。記事に着地させる型は、見た範囲には無い。
- 4本とも、最初に「痛い」を認めてから「そのあとゆるむ」と言う【事実】。見た目のこわさを先に言う型。
- 腰痛を名指ししたのは Pranamat の2016年の文だけ。今の Shakti の広告は "sore"（こり・張り）"tension"（緊張）で、**痛みの原因の説明は無い**【事実】。

---

## 2. 代わりの対策の売り手

日本の Meta 広告は読めなかったので、**販売ページで言っていること**の表。広告の文面・動画か静止画か・配信日数は取れていない。

| 対策 | 売り手 | 値段 | 訴求（見出しの原文） | ねらっている層 | 着地 | 保証 | 出典 |
|---|---|---|---|---|---|---|---|
| マットレス | NELL | 79,900円〜 | "Sleep for Great Tomorrow"／「寝返りを科学した」 | 【推測】寝具を買い替えて腰・睡眠を良くしたい層 | 商品ページ（自社） | 120日のフリートライアル | https://nell.life/ |
| マットレス | 雲のやすらぎプレミアム | 39,800円〜 | 「雲の上で寝ているような寝心地」。5層・体圧分散・高反発 | 【推測】朝の腰のつらさを寝具で直したい層 | 商品ページ（自社。開けていない） | 100日保証 | 検索結果の要約（https://www.atpress.ne.jp/news/0794637 ） |
| マットレス | モットン | 取れなかった | 「全国各地の整骨院で、施術用マットレスとして採用されています」 | 【推測】整骨院の権威に反応する腰痛の層 | 取れなかった | 取れなかった | https://motton-japan.com/ |
| マッサージガン | MYTREX REBIVE MINI XS2 | 14,960円（旧 XS は 10,780円） | 「どんな人にも、どんな部位にも最適な刺激を。業界初※手圧変動ハンディガン誕生!!」。「プロの整体師に施術を受けたかのような体感」 | 【推測】首・肩・腰のこりを自分でほぐしたい層 | 商品ページ・量販店・@cosme | 取れなかった | https://www.cosme.net/variations/1187149/ 、検索結果の要約 |
| 湿布 | ロキソニンSテープ（第一三共ヘルスケア） | 7枚 1,188円（希望小売価格） | 効能「腰痛、肩こりに伴う肩の痛み、関節痛、筋肉痛…」。メーカーの見出しは取れなかった | 腰痛・肩こりの全員（ドラッグストアで買う層） | ドラッグストア・通販の商品ページ | — | https://kakaku.com/item/K0001344626/ 、https://www.matsukiyococokara-online.com/store/catalog/product/view/id/4987107617859 |
| 整体 | カラダファクトリー | 取れなかった（初回体験のオンライン限定の値段あり） | 「A.P.バランス®」（骨格・骨盤の調整）。肩こり・腰痛・姿勢・産後 | 【事実】肩こり・腰痛・姿勢の悩み、産後の人 | 店の予約ページ | — | https://karada39.com/ |

**代わりの対策が言っている「原因」**【事実：見た販売ページの範囲】
- マットレス：寝返り・体圧・寝姿勢（＝寝具が合っていない）
- マッサージガン：筋肉の奥のこり（＝ほぐす力が足りない）
- 整体：骨格・骨盤のゆがみ
- 湿布：原因は言わない（効能だけ）
- **「筋肉が酸欠になっている」「血が届いていない」を原因として言っている売り手は無かった。**

---

## 3. 広告の一覧（だれ向け・何を言っているか・動画か静止画か・着地）

目標30本に対して、確認できたのは4本。

| # | 広告主 | だれ向け | 何を言っているか | 形式 | 着地 | 出典 |
|---|---|---|---|---|---|---|
| S1 | Shakti Mat | 疲れ・こり・ストレスのある人（"tired, sore and stressed"）。年代は表示なし | 20分・家から出ずにゆるむ。最初の数分は強いが、そのあと深くゆるむ。39K の5つ星。60日お試し | 静止画 | トップページ | https://brandsearch.co/brands/shaktimat.com |
| S2 | Shakti Mat | 本当に休めていない人 | 痛いが効く。指圧は数千年の歴史。20分でいい。60日お試し | 静止画 | トップページ | 同上 |
| S3 | Shakti Mat | 体がこわばっている人（"sore" "tight muscles"） | 突起が固い筋肉を押して、力ずくでゆるめる。20分と深呼吸。家でできる | 静止画 | トップページ | 同上 |
| S4 | Shakti Mat | 足の疲れ | 足裏用の小さいパッド。「足裏のエスプレッソ」 | 静止画 | 商品ページ | https://brandsearch.co/brands/shaktimat.co.uk |

**取れなかったもの**：日本語の指圧マット・腰痛・肩こりの広告（0本）、動画広告（0本）、配信日数の長い広告の順位、記事に着地している広告。

---

## 4. 型ごとの本数（見た範囲）

販売ページ・広告を合わせて、同じ商品の売り手13（Shakti Japan／Shakti 海外／BODY RAJA／モール品7／PLEAVIT／RelaxBax／Pranamat／Bed of Nails を、言っていることで分けた）。

| 訴求の型 | 言っていること | 売り手・広告 | 本数 |
|---|---|---|---|
| リラックス・ストレス・整う | 寝るだけでゆるむ、古代の知恵 | Shakti Japan、Shakti の広告 S1・S2、PLEAVIT、RelaxBax、Bed of Nails | 広告2本＋販売ページ4社 |
| こり・筋肉の張りをゆるめる | 突起が筋肉を押してゆるめる | Shakti の広告 S3、AliExpress の出品、MYTREX（代わりの対策） | 広告1本＋販売ページ2社 |
| 寸法・個数・セット・値段 | 大きさ、突起の数、枕と袋つき、安い | モール品7社（TKクリエイト・WIDEN・ErgoStep・Energy Product・Vilom・Bindo・ほか）、BODY RAJA（長さ） | 販売ページ8社 |
| 寝つき・睡眠 | 寝る前に使うと眠れる | ギズモードの記事、Pranamat（"fall asleep faster"）、RelaxBax | 販売ページ・記事3 |
| 数の証拠＋お試し | 39K レビュー、93%、60日 | Shakti（広告3本の締め）、Pranamat | 広告3本＋販売ページ2社 |
| 腰痛を名指し | 腰痛に、と言う | Pranamat（2016年の文）だけ | 1（今の配信は未確認） |
| **原因から話す（腰痛は筋肉の酸欠／湿布は届いていない）** | — | **なし** | **0** |

---

## 5. 空いている場所

| 空いている場所 | 根拠（見た範囲で、だれも言っていない） | 種類 |
|---|---|---|
| **① 原因からの話：「慢性腰痛の原因は筋肉の酸欠」「湿布は届いていない」** | 同じ商品の売り手13・代わりの対策6社の販売ページと、Shakti の広告4本に、この話は**0**。Shakti は「緊張をゆるめる」、マットレスは「寝返り・体圧」、整体は「骨格」、湿布は原因を言わない。血の流れ・酸素を原因に置いている売り手はいなかった | 【事実：見た範囲】。日本の配信中の Meta 広告は未確認 |
| **② 「腰が痛い人」に向けた指圧マット** | Shakti Japan はストレス・リラックス、モール品はだれ向けかを言わない。腰痛を名指ししたのは Pranamat の2016年の文だけ | 【事実：見た範囲】 |
| **③ 湿布を責める入口** | 代わりの対策を名指しして「それでは届かない」と言う売り手は、同じ商品の中に0。Shakti の比べる相手は「毎日のマッサージ」だけ（"Getting a massage every day probably isn't on the cards…"） | 【事実：見た範囲】 |
| **④ 記事への着地** | Shakti の広告4本はトップページか商品ページ。日本の Shakti も商品ページ。記事（原因の説明 → 商品）で売っている指圧マットは見つからなかった | 【事実：見た範囲】 |
| **⑤ 動画（VSL）** | 確認できた広告4本はすべて静止画。指圧マットの長い動画広告は見つかっていない（GetHookd が使えず、動画は探せていない） | 【事実：見た範囲】。未確認が大きい |
| **⑥ まん中の値段（6,000〜17,000円）** | モール品の上限 5,980円、Shakti の下限 18,000円。あいだにいるのは PLEAVIT（約6,910円）と終了した RelaxBax（13,860円）だけ | 【事実】 |
| **⑦ 保証で Shakti に並ぶ・上回る** | Shakti 60日＋5年、Pranamat 30日＋5年、Bed of Nails 60日。モール品は保証の表示が取れていない | 【事実】 |
| **⑧ 「最初の数分は痛い」を日本語で正面から言う** | 海外の Shakti は4本とも最初に言う。Shakti Japan の見出しは「一瞬でリラックス」で、痛さを前に出していない | 【事実】 |

**① への答え（頼まれた問い）**：「慢性腰痛の原因は筋肉の酸欠／湿布は届いていない」という原因からの話をしている競合は、**見た範囲ではいない**。見た範囲は、同じ商品の売り手13・代わりの対策6社の販売ページと、Shakti Mat の Meta 広告4本（英語）。日本の Meta 広告は読めていないので、日本の配信中の広告にいるか・いないかは、GetHookd か広告ライブラリが使えるようになってから確かめる所。
なお、広告ではない読み物（週刊女性PRIME https://www.jprime.jp/articles/-/4432 、東洋経済 https://toyokeizai.net/articles/-/197851 ）には「腰痛と血流」「湿布では治らない」という話が出ている【事実：検索結果の要約】。お客さんがこの話を初めて聞くとは限らない。

---

## 6. 次に取る物（道具が使えるようになったら）

- GetHookd：`acupressure mat`・`shakti mat`・`pranamat`・`back pain`・`指圧マット`・`腰痛`・`肩こり`・`湿布`・`マッサージガン`・`整体`・`マットレス 腰痛` で、動画・配信日数・着地・文字起こし
- Meta 広告ライブラリ（国=日本）：同じ語で、Shakti Japan・BODY RAJA・PLEAVIT と、腰痛の記事 LP を回している広告主
- Amazon.co.jp・楽天の「指圧マット」上位の実際の一覧（題・値段・レビュー数）
