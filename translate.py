"""中英互译。"""

from llm_client import LLMClient


def translate(text: str, to: str, llm: LLMClient = None) -> str:
    """中英互译。

    Args:
        text: 待翻译文本
        to: 目标语言 (zh 中文 / en 英文)
        llm: LLM 客户端

    Returns:
        翻译结果
    """
    if not text.strip():
        raise ValueError("待翻译内容不能为空")

    target_lang = "中文" if to.lower() in ("zh", "cn", "中文", "中") else "英文"
    llm = llm or LLMClient()
    system = "你是一位专业翻译，翻译准确、自然、忠实原意。"
    user = f"请将以下文本翻译成{target_lang}，只输出译文，不要解释。\n\n文本：\n{text}"
    return llm.chat(system, user, temperature=0.3)
