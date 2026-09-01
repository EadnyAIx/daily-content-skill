"""统一 LLM 客户端封装。"""

from config import Config


class LLMError(Exception):
    """LLM 调用异常。"""


class LLMClient:
    """OpenAI 兼容客户端，所有子功能复用。"""

    def __init__(self):
        try:
            Config.validate()
        except ValueError as e:
            raise LLMError(str(e))
        try:
            from openai import OpenAI
        except ImportError:
            raise LLMError("未安装 openai，请运行 pip install openai")

        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY,
            base_url=Config.OPENAI_BASE_URL if Config.OPENAI_BASE_URL else None,
        )
        self.model = Config.CHAT_MODEL
        self.temperature = Config.TEMPERATURE

    def chat(self, system: str, user: str, temperature: float = None) -> str:
        """调用对话模型。"""
        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                temperature=temperature if temperature is not None else self.temperature,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            raise LLMError(f"LLM 调用失败: {e}")
