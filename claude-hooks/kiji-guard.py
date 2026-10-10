#!/usr/bin/env python3
"""記事・飛び先（アドバトリアル・アンケートLP）の2つの決まりを、その場で効かせるフック（2026-10-10 本人）。

1. PreToolUse Bash: 記事の置き場を Shopify の店に上げるコマンドを止める（Vercel への公開は 公開する.py が検査を通して自動で行う）。
   本人が承認した時は、コマンドの頭に `HONBAN_OK=1 ` を付けると通る。
2. PostToolUse Write|Edit: kata-tsukuru の作業場の結果_<k>.json が「出力」に挙げている物の
   フォルダの中を直した時、審査と読み手の目をやり直すよう知らせる（審査の後に直した物は審査が効かない）。
どちらも、関係ない呼び出しでは何もしない（終了コード0・出力なし）。
"""
import glob, json, os, re, sys

RUNS = os.path.expanduser("~/Claude Code/kata-tsukuru/runs")
KIJI = re.compile(r"08 記事|08\\ 記事|kata-tsukuru|VSL記事リサーチ|advertorial|アンケート型|記事_")
# 止めるのは Shopify の店（実際のお客さんが見る店）に上げる物だけ。Vercel などリンクで見せる所へは、
# 公開する.py が検査を通してから自動で上げる（2026-10-10 本人「OKだったら vercel に勝手にあげていい。全自動」）
DEPLOY = re.compile(r"shopify\s+theme\s+(push|publish)")


def pre(data):
    cmd = (data.get("tool_input") or {}).get("command", "")
    if not DEPLOY.search(cmd) or not KIJI.search(cmd):
        return 0
    if re.match(r"\s*HONBAN_OK=1\s", cmd):
        return 0
    print("止めた: 記事・飛び先を Shopify の店に直接上げるコマンドです。リンクで見せる公開は `python3 ~/.claude/skills/quiz-jp-copy/scripts/公開する.py <フォルダ>` が検査を通して自動で行う。店に載せるのは別の決め。"
          "本人が上げてよいと言った時だけ、コマンドの頭に `HONBAN_OK=1 ` を付けて打ち直す。", file=sys.stderr)
    return 2


def outputs():
    res = []
    for p in glob.glob(os.path.join(RUNS, "*", "e2e", "結果_*.json")):
        try:
            out = json.load(open(p)).get("出力")
        except Exception:
            continue
        if out:
            res.append((p, os.path.dirname(os.path.realpath(os.path.expanduser(out)))))
    return res


def post(data):
    f = (data.get("tool_input") or {}).get("file_path") or (data.get("tool_response") or {}).get("filePath") or ""
    if not f:
        return 0
    f = os.path.realpath(os.path.expanduser(f))
    for res, folder in outputs():
        if f.startswith(folder + os.sep):
            k = re.findall(r"結果_(\d+)", res)[0]
            msg = (f"審査の後の直し: {os.path.basename(f)} は {k}本目の出来た物です。直した後の版で、子スキルの手順8の審査（審査_{k}_<回>.md）と"
                   f"読み手の目（読み手の目_{k}_<回>.md）をもう一度通す。通すまで goal.py の G6 は×になる。")
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}, ensure_ascii=False))
            return 0
    return 0


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    ev = data.get("hook_event_name") or ("PreToolUse" if "tool_response" not in data else "PostToolUse")
    if ev == "PreToolUse" and data.get("tool_name") == "Bash":
        return pre(data)
    if ev == "PostToolUse" and data.get("tool_name") in ("Write", "Edit", "MultiEdit"):
        return post(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
