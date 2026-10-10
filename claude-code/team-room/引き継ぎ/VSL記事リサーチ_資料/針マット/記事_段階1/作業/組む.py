# 前の記事の CSS（欄の見た目）に、この記事の本文をつなぎ、文節の切れ目に <wbr> を入れる
import re,sys
A=sys.argv[1]
prev=open(A+'/../記事_ストレッチで戻る腰/index.html',encoding='utf-8').read()
css=prev[prev.index('<style>'):prev.index('</style>')+8]
css=css.replace('h1.oh{font-size:22px;margin:8px 0 2px}','.price .oh{font-size:22px;font-weight:900;line-height:1.45;margin:8px 0 2px}')
css=css.replace('</style>','.steps{margin:18px 0;display:grid;gap:10px}\n.steps .sp{border:2px solid var(--line);border-left:6px solid var(--pink);border-radius:8px;padding:10px 14px;background:#fff}\n.steps .n{display:inline-block;background:var(--pink);color:#fff;font-weight:900;font-size:13px;border-radius:4px;padding:0 8px;margin-right:8px}\n.steps b{font-size:17.5px}\n.steps p{margin:6px 0 0;font-size:16px;line-height:1.75}\n.nw{white-space:nowrap}\n</style>')
body=open(A+'/作業/body.html',encoding='utf-8').read()
head='''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>たまに重くなるだけの腰。それは、腰の筋肉が「酸欠」で死んでいく始まりかもしれません｜からだ取材室</title>
<!-- テスト用の値: 評価の数・星・人数・割引率・保証の日数・医師・客の声は Claude が決めた値。一覧は テスト用に決めた値.md。公開の前に本物の値へ替える -->
<!-- 参考: Roosty's feather-loss（1本だけ）。段の対応は 移植表_段階1.md -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
'''
P='(?:から|まで|より|ので|けど|ても|でも|には|では|とも|へは|は|が|を|に|で|と|も|へ|や|の|、|。|・|？|！|」|）)'
def wb(t):
    t=t.replace('<wbr>','')
    # 助詞・句読点のあと、次がかなの続きでなければ切れ目
    t=re.sub('([、。？！」）])(?=[^、。・？！」）\\s<…〜％%])',r'\1<wbr>',t)
    # 助詞のあとは、次がひらがな・記号でない時だけ切れ目（「で|す」「は|い」を切らない）
    return re.sub('(?<![<])('+P+')(?=[一-龥ァ-ヶー０-９0-9A-Za-zＡ-Ｚ「（])',r'\1<wbr>',t)
out=re.sub(r'>([^<>]+)<',lambda m:'>'+wb(m.group(1))+'<',body)
# 数字の途中・「〜」の前後には入れない（念のため外す）
out=re.sub(r'(\d)<wbr>(?=\d)',r'\1',out)
# 文の終わりまでの残りが3文字以下（句読点を数えない）なら、その切れ目は外す（「酸欠」|です。 や どんより|重い？ を作らない）
INL=re.compile(r'</?(?:wbr|strong|mark|b|span|br)[^>]*>')
def keep(after):
    s=INL.sub('',after[:80])
    m=re.search('[。？！]|<',s)
    seg=s[:m.end()] if m else s
    n=len(re.sub('[、。？！」）「（・\\s<]','',seg))
    return n>3
parts=out.split('<wbr>')
res=parts[0]
for k in range(1,len(parts)):
    res+=('<wbr>' if keep(''.join(parts[k:k+6])) else '')+parts[k]
out=res
# 」のあとの短い文末（」です。 など）は、」の直後で折れないように1つにまとめる
out=re.sub(r'([^>\s<]{1,2})」([ぁ-ん]{1,3}[。？！])',r'<span class="nw">\1」\2</span>',out)
open(A+'/index.html','w',encoding='utf-8').write(head+css+'\n</head>\n'+out)
print(out.count('<wbr>'))
