"""改写润色：按风格改写文字。"""

from llm_client import LLMClient


STYLES = {
    "口语化": "把文字改写成口语化的表达，自然流畅，像日常对话，避免书面语。",
    "正式": "把文字改写成正式、严谨的书面表达，用词准确，结构规范，适合商务场合。",
    "简洁": "把文字压缩得简洁凝练，删去冗余，保留核心信息，一句话能说清就不用两句。",
    "营销": "把文字改写成有吸引力的营销文案，突出卖点和价值，用词有感染力，可适当使用短句和感叹。",
    "学术": "把文字改写成学术化的表达，用词专业、逻辑严谨、客观中立，适合论文或报告。",
}


def rewrite(text: str, style: str = "口语化", llm: LLMClient = None) -> str:
    """改写润色文字。

    Args:
        text: 原文
        style: 目标风格（口语化/正式/简洁/营销/学术）
        llm: LLM 客户端

    Returns:
        改写后的文字
    """
    if style not in STYLES:
        raise ValueError(f"不支持的风格: {style}，可选: {list(STYLES.keys())}")
    if not text.strip():
        raise ValueError("待改写内容不能为空")

    llm = llm or LLMClient()
    system = "你是一位专业的中文文字编辑，擅长按不同风格改写文字，始终保持原意。"
    user = (
        f"请将下面的文字改写成【{style}】风格。\n"
        f"要求：保持原意不变，只调整表达方式。\n\n"
        f"原文：\n{text}"
    )
    return llm.chat(system, user)
