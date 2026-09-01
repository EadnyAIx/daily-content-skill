"""标题生成：一次生成多个备选标题。"""

from llm_client import LLMClient


TITLE_STYLES = {
    "吸睛": "标题要有吸引力、抓眼球，可以适当使用悬念、数字、反差等技巧。",
    "专业": "标题要专业、严谨，准确概括主题，适合正式场合。",
    "文艺": "标题要有文艺气息，富有意境和美感，用词考究。",
    "实用": "标题要直接点明价值和用途，让读者清楚能获得什么。",
}


def generate_titles(topic: str, count: int = 5, style: str = "吸睛", llm: LLMClient = None) -> list:
    """生成多个备选标题。

    Args:
        topic: 文章主题
        count: 标题数量
        style: 风格（吸睛/专业/文艺/实用）
        llm: LLM 客户端

    Returns:
        标题列表
    """
    if style not in TITLE_STYLES:
        raise ValueError(f"不支持的风格: {style}，可选: {list(TITLE_STYLES.keys())}")
    if not topic.strip():
        raise ValueError("文章主题不能为空")
    count = max(1, min(count, 10))

    llm = llm or LLMClient()
    system = "你是一位资深新媒体编辑，擅长标题创作。"
    user = (
        f"请为以下主题生成 {count} 个【{style}】风格的标题。\n"
        f"要求：每个标题一行，直接输出标题，不要编号和解释。\n\n"
        f"主题：{topic}"
    )
    resp = llm.chat(system, user)
    titles = [line.strip().lstrip("0123456789.、)） ").strip() for line in resp.splitlines() if line.strip()]
    return titles[:count]
