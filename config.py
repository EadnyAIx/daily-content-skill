"""日常内容创作配置。"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """全局配置。"""

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    CHAT_MODEL: str = os.getenv("CHAT_MODEL", "gpt-4o-mini")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))

    @classmethod
    def validate(cls) -> None:
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "未配置 OPENAI_API_KEY，请复制 .env.example 为 .env 并填入 API Key"
            )
