"""日常内容创作 - CLI 入口。

用法:
    python skill.py rewrite <文本> [--style 口语化|正式|简洁|营销|学术] [--file 路径]
    python skill.py translate <文本> --to zh|en
    python skill.py summarize <文本> [--points N] [--file 路径]
    python skill.py title <主题> [--count N] [--style 吸睛|专业|文艺|实用]
    python skill.py tone <文本> --to 礼貌|轻松|正式|强硬|鼓励
"""

import argparse
import sys
from pathlib import Path

from llm_client import LLMClient, LLMError
from rewrite import rewrite
from translate import translate
from summarize import summarize
from title_gen import generate_titles
from tone_convert import convert_tone


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="skill", description="日常内容创作 Skill")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # rewrite
    r = sub.add_parser("rewrite", help="改写润色")
    r.add_argument("text", nargs="?", default=None, help="待改写文本")
    r.add_argument("--file", default=None, help="从文件读取")
    r.add_argument("--style", default="口语化", help="风格: 口语化/正式/简洁/营销/学术")

    # translate
    t = sub.add_parser("translate", help="中英互译")
    t.add_argument("text", help="待翻译文本")
    t.add_argument("--to", required=True, help="目标语言: zh/en")

    # summarize
    s = sub.add_parser("summarize", help="长文摘要")
    s.add_argument("text", nargs="?", default=None, help="待摘要文本")
    s.add_argument("--file", default=None, help="从文件读取")
    s.add_argument("--points", type=int, default=3, help="要点数量")

    # title
    ti = sub.add_parser("title", help="标题生成")
    ti.add_argument("topic", help="文章主题")
    ti.add_argument("--count", type=int, default=5, help="标题数量")
    ti.add_argument("--style", default="吸睛", help="风格: 吸睛/专业/文艺/实用")

    # tone
    to = sub.add_parser("tone", help="语气转换")
    to.add_argument("text", help="待转换文本")
    to.add_argument("--to", required=True, help="语气: 礼貌/轻松/正式/强硬/鼓励")

    return parser


def _read_input(text: str, file: str) -> str:
    """读取输入：优先文件，否则用文本。"""
    if file:
        path = Path(file)
        if not path.exists():
            raise ValueError(f"文件不存在: {file}")
        return path.read_text(encoding="utf-8-sig", errors="ignore").strip()
    if not text or not text.strip():
        raise ValueError("请提供文本或 --file 文件路径")
    return text.strip()


def main():
    args = build_parser().parse_args()

    try:
        llm = LLMClient()

        if args.cmd == "rewrite":
            content = _read_input(args.text, args.file)
            print(rewrite(content, args.style, llm))

        elif args.cmd == "translate":
            print(translate(args.text, args.to, llm))

        elif args.cmd == "summarize":
            content = _read_input(args.text, args.file)
            result = summarize(content, args.points, llm)
            print(f"【摘要】\n{result['summary']}\n")
            print("【要点】")
            for i, p in enumerate(result["points"], 1):
                print(f"  {i}. {p}")

        elif args.cmd == "title":
            titles = generate_titles(args.topic, args.count, args.style, llm)
            print(f"🎯 生成的标题（{len(titles)}个）:")
            for i, t in enumerate(titles, 1):
                print(f"  {i}. {t}")

        elif args.cmd == "tone":
            print(convert_tone(args.text, args.to, llm))

    except (LLMError, ValueError) as e:
        print(f"❌ {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 未知错误: {type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
