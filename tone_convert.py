"""语气转换：调整文字语气但保留原信息。"""

from llm_client import LLMClient


TONES = {
    "礼貌": "把语气改得礼貌客气，多用敬语和委婉表达，让人感觉被尊重。",
    "轻松": "把语气改得轻松随意，像朋友聊天，减少压迫感。",
    "正式": "把语气改得正式严谨，符合正式书面沟通规范。",
    "强硬": "把语气改得坚定强硬，立场明确，不容置疑，但仍保持基本礼貌。",
    "鼓励": "把语气改得积极鼓励，传递支持和信心。",
}


def convert_tone(text: str, to: str = "礼貌", llm: LLMClient = None) -> str:
    """转换文字语气。

    Args:
        text: 原文
        to: 目标语气（礼貌/轻松/正式/强硬/鼓励）
        llm: LLM 客户端

    Returns:
        转换后的文字
    """
    if to not in TONES:
        raise ValueError(f"不支持的语气: {to}，可选: {list(TONES.keys())}")
    if not text.strip():
        raise ValueError("待转换内容不能为空")

    llm = llm or LLMClient()
    system = "你是一位沟通技巧专家，擅长调整表达语气。"
    user = (
        f"请将下面的文字转换成【{to}】语气。\n"
        f"要求：保留全部原始信息，只调整语气和措辞。\n\n"
        f"原文：\n{text}"
    )
    return llm.chat(system, user)
