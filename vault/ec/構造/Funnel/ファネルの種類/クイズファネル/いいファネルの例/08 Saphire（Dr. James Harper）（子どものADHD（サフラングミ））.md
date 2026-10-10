<!-- 例 -->
# 08 Saphire（Dr. James Harper）（子どものADHD（サフラングミ））— クイズファネル example

読む人: この型（心理エスカレーション型（絶望度を聞く））の実物を、広告→質問→結果→オファー→売り場まで通しで1本見たい人。
読む時: 自分のクイズの問い・幕間・結果の出し方・値段の出す位置を決める時。
読まなくていい条件: 12本の比較だけ要る時は [[_index]] か `ec/wiki/quiz-teardown/12本-クイズファネル構造分解.md`。

出典: [102508324](https://app.gethookd.ai/share/ad/102508324?signature=86bef4bb319f29a2382093747600c99e35266cc9dc552891a54ba8006f5fa273)（GetHookd・share_url は期限なし）
LP: https://trysaphire.com/pages/gummies-kid-quiz
形式: 動画 219s（3分39秒）・US・Facebook／Instagram・着地 quiz_page
拾った日: 2026-09-11
稼働日数 / 成績: 108日 / score 100（GetHookd の黒箱。売上ではない）
出どころ記号: `T`=GetHookd文字起こし（全文は `ec/wiki/quiz-teardown/raw/102508324.full.txt`）／`F`=ローカルmp4から切った絵／`Q`=クイズを dia で歩いた実測（`ec/wiki/quiz-teardown/lp/`）／`L`=LP・店の実測／`J`=判断

## なぜ良いのか（1行）

3分39秒の教師UGCで「学校が3つの脳内物質を削る」と親を味方にし、9問で「How desperate are you feeling right now」まで登らせてから「Buy 2 Get 1 Free」の商品ページへ落とす。 `J`

## 分解（ファネル通し・5部品）

| 位置 | 出ている物 | 何をやっているか |
|---|---|---|
| 01 入口（広告） | 動画 3分39秒・型は下の9ブロック | 0:00–0:10 `T`「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't… |
| 02 質問設計 | 8問・幕間2（見出し無し） | trysaphire.com/pages/gummies-kid-quiz → quiz.trysaphire.com/og-quiz?step=1（自前・Shopify外）: 1問目が最初の画面。進捗9.09%刻み `Q`… |
| 03 結果ページ | 「Analyzing your child's behavioral patterns…」→ 100%「CLAIM MY OFFER」のボタンだけの画面（結果の文は無い）`Q`… | 回答を「あなたの状態」に言い換えて、次の画面の値段を受け入れさせる |
| 04 オファー提示 | 1袋 $54.95（元$65.00）／3-Pack $95.95（元$179.85）（products.json）。B2G1 の段 | trysaphire.com/products/saphire-saffron-gummies?utm_source=clarflow&utm_medium=referral&utm_campaign=og-quiz（Shopify PDP）: 「Back to School - Buy 2 Get 1 Free」／「… |
| 05 チェックアウト | 広告→クイズ8問＋幕間2→CLAIM→Shopify商品ページ→カート→チェックアウト。約13画面 | 保証: 60日 |

## 盗む所

- 最後の問いを「How desperate are you feeling right now」の5段階にする
- 幕間を2枚、見出し無しの短文だけで置く
- クイズは別ドメイン（quiz.trysaphire.com）でも utm_source=clarflow で来歴を店に渡す

## 01 入口（広告）— 9ブロック分解

| ブロック | 秒・出ている物・逐語 |
|---|---|
| hook | 0:00–0:10 `T`「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」（`F` 教室で叱る男性教師の芝居＋赤テロップ「The school system DESTROYS kids with ADHD 😡😡😡」＋左に「She hates us all／The principal knows／Everyone knows／No one helps…」） |
| lead | 0:10–0:23 `T`「I'm an elementary school teacher, 14 years in the classroom」「The school system was never designed for kids with ADHD」 |
| discovery story | 2:10–2:19 `T`「I found a gummy that uses the same dose of saffron extract as in the study」 |
| UMP | 0:23–1:21 `T`「three chemicals that school drains every single day, dopamine, cortisol, and serotonin」「ADHD kids get 15 times more corrections during a school day」 |
| UMS | 1:44–2:10 `T`「in 2019, a study came out where saffron extract was compared directly to Ritalin in children with ADHD」「supports dopamine, cortisol regulation and serotonin all at the same time」 |
| product reveal | 2:53（79%地点）`T`「the sapphire happy chew」（親のUGCの中で） |
| price drop | 無し |
| risk reversal | 無し |
| testimonials | 2:19–3:31 `T` 教師が見た週2・週4・週5の変化＋親3人「his teacher saying that he has been so much more focused in class」 |

無かったブロックは「無し」。欠落そのものが発見。

### フック 0〜12秒（1秒刻み・`F`）

無音: 0箇所（-45dB／0.4秒判定）。0なら音の床が全編に敷いてある。

| 秒 | 絵 | 喋っている言葉 `T` |
|---|---|---|
| 0s | ![[ec/wiki/quiz-teardown/frames/102508324/00s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 1s | ![[ec/wiki/quiz-teardown/frames/102508324/01s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 2s | ![[ec/wiki/quiz-teardown/frames/102508324/02s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 3s | ![[ec/wiki/quiz-teardown/frames/102508324/03s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 4s | ![[ec/wiki/quiz-teardown/frames/102508324/04s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 5s | ![[ec/wiki/quiz-teardown/frames/102508324/05s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 6s | ![[ec/wiki/quiz-teardown/frames/102508324/06s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 7s | ![[ec/wiki/quiz-teardown/frames/102508324/07s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 8s | ![[ec/wiki/quiz-teardown/frames/102508324/08s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 9s | ![[ec/wiki/quiz-teardown/frames/102508324/09s.jpg\|220]] | 「You just be quiet. You have no business being dramatic, thinking you're going to tell me anything. I don't appreciate it.」 |
| 10s | ![[ec/wiki/quiz-teardown/frames/102508324/10s.jpg\|220]] | 「I'm an elementary school teacher, 14 years in the classroom. It's not your fault that school is hard for your child, and it's not their fault either.」 |
| 11s | ![[ec/wiki/quiz-teardown/frames/102508324/11s.jpg\|220]] | 「I'm an elementary school teacher, 14 years in the classroom. It's not your fault that school is hard for your child, and it's not their fault either.」 |
| 12s | ![[ec/wiki/quiz-teardown/frames/102508324/12s.jpg\|220]] | 「I'm an elementary school teacher, 14 years in the classroom. It's not your fault that school is hard for your child, and it's not their fault either.」 |

### 全シーン × b-roll（`F`）

尺 218.6秒 ／ 27シーン ／ 平均 8.1秒 ／ しきい値 0.25（シーン数はしきい値に依存。0.5で約-35%、0.2で約+5%）。表と絵は `ec/wiki/quiz-teardown/シーン/102508324.md` にあり、下に埋め込む（Obsidianで展開）。

![[ec/wiki/quiz-teardown/シーン/102508324]]

## 02 質問設計 — 入口と全問（`Q`）

入口: trysaphire.com/pages/gummies-kid-quiz → quiz.trysaphire.com/og-quiz?step=1（自前・Shopify外）: 1問目が最初の画面。進捗9.09%刻み `Q`

| # | 問い | 選択肢 | 型・次に出る幕間 |
|---|---|---|---|
| 1 | 「What's your child's age range?」 | 「4-6 years old（Preschool/Kindergarten）／7-9（Early elementary）／10-12（Late elementary）／13+（Middle school & up）」 | 単一 |
| 2 | 「Which challenge with your child bothers you most?」 | 「Daily meltdowns and explosive tantrums／Can't focus or sit still in school／Hyperactivity and impulse control issues／Constant calls/notes from teachers／All of the above - I'm at my wit's end」 | 複数→Continue |
| 3 | 「When did you first notice your child's behavior becoming a serious problem?」 | 「⚠️ Within the last year／⚠️ 1-2 years ago／🚨 3-4 years ago／🚨 Since they started school」 | 単一 |
| 4 | 「How much have your child's ADHD symptoms affected their school experience?」 | 「Occasional focus issues, mostly manageable／Regular teacher complaints／Frequent calls from school／Constant problems - teachers say they…／Considering medication because school…」 | 複数→Continue → 幕間（見出し無し・Continue） |
| 5 | 「How do your child's meltdowns affect your family life?」 | 「Occasional disruptions, we manage fine／Regular tension, walking on eggshells at home／Daily chaos - siblings affected／Complete family breakdown - I cry regularly」 | 複数→Continue |
| 6 | 「What does getting your child ready for school look like?」 | 「Usually smooth with minor hiccups／Some resistance but we get there／Daily battle - yelling, crying／Complete war zone - neighbors probably…」 | 単一 |
| 7 | 「Where are you in the medication decision process?」 | 「Haven't considered it yet, hoping for natural solutions／Researching options but scared of side effects／Doctor recommended it but I want to try…／Already tried meds with limited success／Refusing medication completely」 | 単一 → 幕間（見出し無し・Continue） |
| 8 | 「How desperate are you feeling right now about your child's behavior?」 | 「Concerned but still optimistic／Worried and actively searching for help／Exhausted and running out of ideas／At my breaking point - I'll try anything／Completely defeated - feeling like a failure」 | 単一 |

問数: 8問・幕間2（見出し無し）

## 03 結果ページ（`Q`）

「Analyzing your child's behavioral patterns…」→ 100%「CLAIM MY OFFER」のボタンだけの画面（結果の文は無い）`Q`

## 04 オファー提示（`L`）

trysaphire.com/products/saphire-saffron-gummies?utm_source=clarflow&utm_medium=referral&utm_campaign=og-quiz（Shopify PDP）: 「Back to School - Buy 2 Get 1 Free」／「SELLING FAST! Offer reserved for 03:00」／Excellent 4.8・100,000+ Reviews／Trusted by 12,000+ parents／60-Day Money-Back（Less than 1% request a refund）／「Neuropsychiatrist Authority Section」「Pediatrician-Recommended Formula」／affron® Saffron Extract・Passion Flower・Magnesium・GABA・L-theanine／60 servings per pack／定期の注意書き `L`

- 値段の段: 1袋 $54.95（元$65.00）／3-Pack $95.95（元$179.85）（products.json）。B2G1 の段
- 保証: 60日
- 作り: 自前（quiz.trysaphire.com）／店: Shopify＋Klaviyo

## 05 売り場までの導線

広告→クイズ8問＋幕間2→CLAIM→Shopify商品ページ→カート→チェックアウト。約13画面

## 広告 → クイズ → 売り場 のつながり

| 要素 | 広告 | クイズ／売り場 | 判定 |
|---|---|---|---|
| 権威 | 教師14年 | Neuropsychiatrist／Pediatrician-Recommended | 人が変わる |
| 原因 | dopamine・cortisol・serotonin | 「When serotonin and dopamine levels fall out of sync」 | 一致 |
| 成分 | saffron（Ritalin比較の2019年研究） | affron® Saffron Extract・「The Science Behind Saffron」 | 一致 |
| 値段 | 無し | $54.95・B2G1 | 店で初めて出る |
| 保証 | 無し | 60日 | 店だけ |

## 補足

結果画面が無い唯一の本（Analyzing→ボタンだけ）。質問の選択肢が全部「悪化の段階」で並ぶ。
