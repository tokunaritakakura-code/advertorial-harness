<!-- 例 -->
# 06 CanineDrops（Riverside Veterinary）（犬の白濁した目（サプリ））— クイズファネル example

読む人: この型（結果を診断名で4分岐＋メールゲート）の実物を、広告→質問→結果→オファー→売り場まで通しで1本見たい人。
読む時: 自分のクイズの問い・幕間・結果の出し方・値段の出す位置を決める時。
読まなくていい条件: 12本の比較だけ要る時は [[_index]] か `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

出典: [111977735](https://app.gethookd.ai/share/ad/111977735?signature=46623d89ec6feef3eacd1e50f9e11fa8098befac9db13041a92923d9b1c0ee70)（GetHookd・share_url は期限なし）
LP: https://quiz.caninedrops.com/
形式: 動画 265s（4分25秒）・US・Facebook／Instagram・着地 quiz_page
拾った日: 2026-09-11
稼働日数 / 成績: 83日 / score 100（GetHookd の黒箱。売上ではない）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/quiz-teardown/raw/111977735.full.txt`）／`F`=ローカルmp4から切った絵／`Q`=クイズを dia で歩いた実測（`ec/wiki/quiz-teardown/lp/`）／`L`=LP・店の実測／`J`=判断

## なぜ良いのか（1行）

4分25秒の演台語り（1シーン）の後、30秒クイズの1問目で結果を4つの診断名に分ける。名前とメールを取ってから診断名を返し、「Quiz reward: Buy 2 get 1 FREE」で店へ落とす。 `J`

## 分解（ファネル通し・5部品）

| 位置 | 出ている物 | 何をやっているか |
|---|---|---|
| 01 入口（広告） | 動画 4分25秒・型は下の9ブロック | 0:00–0:12 `T`「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye is… |
| 02 質問設計 | 8問（スライダー1）・幕間1・メールゲート1 | quiz.caninedrops.com（heyflow）: 「Is your dog's eyesight getting worse?／Discover what's happening inside your dog's eyes in 30 seconds.」→「Take Our 30-second quiz」… |
| 03 結果ページ | 「Analysing your answers… matching your dog's eye profile…」→「Your personalized eye health plan is ready ✓／Trusted by 9,000+ dog parents」First name＋Email →「Unlock… | 回答を「あなたの状態」に言い換えて、次の画面の値段を受け入れさせる |
| 04 オファー提示 | 1本 $69.99（元$139.99）・3本で1本無料。段は本数 | caninedrops.com/products/clearvision-drops（Shopify・GemPages）: 「LIMITED TIME OFFER: BUY 2 GET 1 FREE」／Regular $69.99（元$139.99・SAVE 50%）／Rated 4.8/5 by 9,249／Vet-… |
| 05 チェックアウト | 広告→入口→8問→名前・メール→診断名→CTA→店の商品ページ→カート→チェックアウト。約14画面 | 保証: 広告・クイズ 90日 → 店 30日（不一致） |

## 盗む所

- 1問目の回答で結果を4つの診断名（Nuclear Sclerosis／PRA／Corneal Opacity／Sudden Vision Loss）に分ける
- メールゲートの前に「Your personalized eye health plan is ready ✓」と先に言う
- クイズ限定の「Buy 2 bottles, get 1 FREE」を『quiz reward』と呼ぶ

## 01 入口（広告）— 9ブロック分解

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:12 `T`「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging. What your dog has is oxidative damage」（`F` 演台のマイクの男・テロップ「The hidden reason your dog's eyes keep getting worse 😱／Listen carefully」・黄色強調の単語字幕。全編1シーン） | <!-- 掘った: 広告の逐語 T。`raw/111977735.segments.json` の秒で照合 -->
| lead | 0:12–0:29 `T`「Cloudy eyes are the obvious sign of constant compounding damage. And the longer you wait, the less you can do about it.」 |
| discovery story | 1:05–1:54 `T`「I had a senior dog patient… early stage cataracts」「In my 11 years working at Riverside County Animal Shelter, I have never seen a response like this」 |
| UMP | 0:29–1:05 `T`「free radicals constantly attacking the proteins inside the lens」「It accelerates. And every week you wait, more proteins are damaged.」 |
| UMS | 1:58–2:43 `T`「antioxidants… neutralize free radicals instantly」「the blood-eye barrier」→ 2:43「Clear Vision by K9 Drops」astaxanthin・lutein・vitamin C/E・zeaxanthin・omega-3 |
| product reveal | 2:43（61%地点） |
| price drop | 3:49 `T`「a rare 60% off sale」（金額なし） |
| risk reversal | 3:49 `T`「90-day money-back guarantee」 |
| testimonials | `T`「thousands of people swear by it」（数だけ） |

無かったブロックは「無し」。欠落そのものが発見。

### フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

| 秒 | 絵 | 喋っている言葉 `T` |
|---|---|---|
| 0s | ![[ec/wiki/quiz-teardown/frames/111977735/00s.jpg\|220]] | 「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging.」 |
| 1s | ![[ec/wiki/quiz-teardown/frames/111977735/01s.jpg\|220]] | 「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging.」 |
| 2s | ![[ec/wiki/quiz-teardown/frames/111977735/02s.jpg\|220]] | 「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging.」 |
| 3s | ![[ec/wiki/quiz-teardown/frames/111977735/03s.jpg\|220]] | 「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging.」 |
| 4s | ![[ec/wiki/quiz-teardown/frames/111977735/04s.jpg\|220]] | 「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging.」 |
| 5s | ![[ec/wiki/quiz-teardown/frames/111977735/05s.jpg\|220]] | 「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging.」 |
| 6s | ![[ec/wiki/quiz-teardown/frames/111977735/06s.jpg\|220]] | 「Your dog doesn't have cloudy eyes, your dog doesn't have cataracts, your dog doesn't have all these eye issues due to aging.」 |
| 7s | ![[ec/wiki/quiz-teardown/frames/111977735/07s.jpg\|220]] | 「What your dog has is oxidative damage and it's happening inside their lens right now.」 |
| 8s | ![[ec/wiki/quiz-teardown/frames/111977735/08s.jpg\|220]] | 「What your dog has is oxidative damage and it's happening inside their lens right now.」 |
| 9s | ![[ec/wiki/quiz-teardown/frames/111977735/09s.jpg\|220]] | 「What your dog has is oxidative damage and it's happening inside their lens right now.」 |
| 10s | ![[ec/wiki/quiz-teardown/frames/111977735/10s.jpg\|220]] | 「What your dog has is oxidative damage and it's happening inside their lens right now.」 |
| 11s | ![[ec/wiki/quiz-teardown/frames/111977735/11s.jpg\|220]] | 「What your dog has is oxidative damage and it's happening inside their lens right now.」 |
| 12s | ![[ec/wiki/quiz-teardown/frames/111977735/12s.jpg\|220]] | 「Most people still think cloudy eyes in a dog means aging.」 |

### 全シーン × b-roll（`F`）

尺 265.3秒 ／ 1シーン ／ 平均 265.3秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）。表と絵は `ec/wiki/quiz-teardown/シーン/111977735.md` にあり、下に埋め込む（Obsidianで展開）。

![[ec/wiki/quiz-teardown/シーン/111977735]]

## 02 質問設計 — 入口と全問（`Q`）

入口: quiz.caninedrops.com（heyflow）: 「Is your dog's eyesight getting worse?／Discover what's happening inside your dog's eyes in 30 seconds.」→「Take Our 30-second quiz」。全画面が最初からDOMに載っている `Q`

| # | 問い | 選択肢 | 型・次に出る幕間 |
|---|---|---|---|
| 1 | 「What was the main thing you noticed?」 | 「A haze or film over the eyes／Bumping into things or hesitating／Eyes look dull or lifeless／Sudden vision loss or disorientation」 | 単一（結果の分岐キー） |
| 2 | 「How long ago did you first notice this?」 | 「Less than a month ago／1–3 months ago／3–6 months ago／More than 6 months ago」 | 単一 |
| 3 | 「How much does it impact his daily life?」 | 「0〜10のスライダー」 | 入力 |
| 4 | 「Can he still see shadows and movement?」 | 「Yes, reacts to light and movement／Sometimes, in good light／Rarely Now／Not Sure」 | 単一 |
| 5 | 「What has your vet said about this?」 | 「It's just old age, monitor it／Surgery was the only option／Surgery isn't possible for my dog／Haven't asked」 | 単一 |
| 6 | 「Have you already tried anything to help?」 | 「Supplements/chews/vision foods／Other eye drops／Changed their diet／Nothing yet」 | 単一 → 幕間「Just 2 more questions your personalized result is almost ready.」 |
| 7 | 「When something new shows real results, how soon would you expect to notice?」 | 「Couple of weeks／1–2 months／However long it takes／Not sure」 | 単一 |
| 8 | 「If your dog's vision improved… what would that mean to you?」 | 「Fewer bumps, safe at home／They'd recognise me again／Confidence at night & stairs／Just feeling I did something」 | 単一 |

問数: 8問（スライダー1）・幕間1・メールゲート1

## 03 結果ページ（`Q`）

「Analysing your answers… matching your dog's eye profile…」→「Your personalized eye health plan is ready ✓／Trusted by 9,000+ dog parents」First name＋Email →「Unlock Plan →」→ 1問目で分岐した診断名: Nuclear Sclerosis（ClearVision penetrate the lens）／Progressive Retinal Atrophy（While not reversible…）／Corneal Opacity／Sudden Vision Loss（Consult with your vet first）→「Learn more about CanineDrops」→「Ready to help your dog see clearly again? 🎁 Quiz reward: Buy 2 bottles, get 1 FREE… Add 3 bottles to your cart the discount is applied automatically」→「Check Availability →」`Q`

## 04 オファー提示（`L`）

caninedrops.com/products/clearvision-drops（Shopify・GemPages）: 「LIMITED TIME OFFER: BUY 2 GET 1 FREE」／Regular $69.99（元$139.99・SAVE 50%）／Rated 4.8/5 by 9,249／Vet-formulated／800,000+ units sold／30-day money-back guarantee（広告・クイズは90日）／「Most eye drops fail for one reason: They stay on the surface」7成分 `L`

- 値段の段: 1本 $69.99（元$139.99）・3本で1本無料。段は本数
- 保証: 広告・クイズ 90日 → 店 30日（不一致）
- 作り: heyflow／店: Shopify＋GemPages

## 05 売り場までの導線

広告→入口→8問→名前・メール→診断名→CTA→店の商品ページ→カート→チェックアウト。約14画面

## 広告 → クイズ → 売り場 のつながり

| 要素 | 広告 | クイズ／売り場 | 判定 |
|---|---|---|---|
| 原因 | oxidative damage・blood-eye barrier | 「They stay on the surface / inside the lens」 | 一致 |
| 値段 | 60% off | $139.99→$69.99（50%）＋B2G1 | 割引率が違う |
| 保証 | 90日 | 30日（店）・90日（クイズCTA） | 店だけ短い |
| 権威 | Riverside County Animal Shelter 11年 | Vet-formulated | 人は出ない |
| 結果 | 無し | 診断名4種 | クイズだけの部品 |

## 補足

12本で唯一、結果を症状名で分岐させる。動画は1シーンでカット0。
