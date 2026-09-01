# 日常内容创作 Skill

> 改写润色、中英互译、长文摘要、标题生成、语气转换，一个技能搞定日常写作需求。

## ✨ 功能特性

### ✍️ 改写润色
- 多种风格：口语化 / 正式 / 简洁 / 营销 / 学术
- 保持原意，优化表达
- 支持直接文本或文件输入

### 🌐 中英互译
- 中英双向翻译
- 保持语气和风格

### 📝 长文摘要
- 摘要 + 核心要点
- 可指定要点数量

### 🏷️ 标题生成
- 一次生成多个备选标题
- 支持吸睛 / 专业 / 文艺风格

### 🎭 语气转换
- 礼貌 / 轻松 / 正式 / 强硬 / 鼓励
- 保留原信息，只变语气

## 🏗️ 架构

```
skill.py (CLI 入口)
 ├── llm_client.py   统一 LLM 客户端
 ├── rewrite.py      改写润色
 ├── translate.py    翻译
 ├── summarize.py    摘要
 ├── title_gen.py    标题生成
 ├── tone_convert.py 语气转换
 └── prompts/        结构化 Prompt 模板
```

## 📦 安装

```bash
git clone <repo-url>
cd daily-content-skill
pip install -r requirements.txt
cp .env.example .env   # 填入 OPENAI_API_KEY
```

## 🚀 使用方法

```bash
# 改写润色
python skill.py rewrite "这段文字有点口语化，帮我改正式一点" --style 正式
python skill.py rewrite --file 草稿.md --style 简洁

# 翻译
python skill.py translate "Hello, how are you?" --to zh
python skill.py translate "你好世界" --to en

# 摘要
python skill.py summarize "很长的文本..." --points 3
python skill.py summarize --file 报告.txt

# 标题生成
python skill.py title "人工智能的发展趋势" --count 5 --style 吸睛

# 语气转换
python skill.py tone "你赶紧把报告交上来" --to 礼貌
```

## 🧪 测试

```bash
python -m pytest tests/ -v
```

## 📁 项目结构

```
daily-content-skill/
├── SKILL.md
├── skill.py              # CLI 入口
├── llm_client.py         # 统一 LLM 客户端
├── rewrite.py            # 改写润色
├── translate.py          # 翻译
├── summarize.py          # 摘要
├── title_gen.py          # 标题生成
├── tone_convert.py       # 语气转换
├── config.py             # 配置
├── requirements.txt
├── .env.example
├── .gitignore
└── prompts/              # Prompt 模板
```

## 📄 License

MIT
