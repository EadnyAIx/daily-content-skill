"""长文摘要：提炼摘要和核心要点。"""

from llm_client import LLMClient


def summarize(text: str, points: int = 3, llm: LLMClient = None) -> dict:
    """生成长文摘要和核心要点。

    Args:
        text: 长文本
        points: 要点数量
        llm: LLM 客户端

    Returns:
        dict: {"summary", "points"}
    """
    if not text.strip():
        raise ValueError("待摘要内容不能为空")
    points = max(1, min(points, 10))

    llm = llm or LLMClient()
    system = "你是一个专业的内容摘要助手，用中文输出。"
    user = (
        f"请对以下文本生成摘要和核心要点。\n"
        f"要求：摘要 100-200 字；列出 {points} 个核心要点，每条一句话。\n\n"
        f"输出格式：\n"
        f"【摘要】\n...\n\n"
        f"【要点】\n- ...\n- ...\n\n"
        f"文本：\n{text}"
    )
    resp = llm.chat(system, user, temperature=0.3)
    return _parse_response(resp)


def _parse_response(text: str) -> dict:
    summary = text
    points = []
    if "【要点】" in text:
        parts = text.split("【要点】")
        summary = parts[0].replace("【摘要】", "").strip()
        points = [
            p.strip().lstrip("-*• ").strip()
            for p in parts[1].splitlines()
            if p.strip().startswith(("-", "*", "•"))
        ]
    if not points:
        points = ["（未能提取要点）"]
    return {"summary": summary, "points": points}
