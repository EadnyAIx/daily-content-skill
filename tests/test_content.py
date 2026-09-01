"""daily-content-skill 单元测试：不依赖真实 LLM，使用 Mock。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import rewrite
import translate
import summarize
import title_gen
import tone_convert


class FakeLLM:
    """模拟 LLM 客户端。"""

    def __init__(self, response="测试响应"):
        self.response = response

    def chat(self, system, user, temperature=None):
        return self.response


def test_rewrite():
    llm = FakeLLM("改写后的文本")
    out = rewrite.rewrite("原始文本", "正式", llm)
    assert out == "改写后的文本"


def test_rewrite_invalid_style():
    llm = FakeLLM()
    try:
        rewrite.rewrite("x", "不存在风格", llm)
        assert False
    except ValueError as e:
        assert "不支持的风格" in str(e)


def test_rewrite_empty():
    try:
        rewrite.rewrite("  ")
        assert False
    except ValueError as e:
        assert "不能为空" in str(e)


def test_translate():
    llm = FakeLLM("你好世界")
    out = translate.translate("Hello world", "zh", llm)
    assert out == "你好世界"


def test_summarize_parse():
    llm = FakeLLM("【摘要】\n这是摘要\n\n【要点】\n- 要点一\n- 要点二")
    result = summarize.summarize("长文本", 2, llm)
    assert result["summary"] == "这是摘要"
    assert result["points"] == ["要点一", "要点二"]


def test_title_gen():
    llm = FakeLLM("标题一\n2. 标题二\n标题三")
    titles = title_gen.generate_titles("主题", 5, "吸睛", llm)
    assert len(titles) == 3
    assert "标题一" in titles
    # 去掉编号
    assert "2. 标题二" not in titles
    assert "标题二" in titles


def test_tone_convert():
    llm = FakeLLM("转换后的语气文本")
    out = tone_convert.convert_tone("原文", "礼貌", llm)
    assert out == "转换后的语气文本"
