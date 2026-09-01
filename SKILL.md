# daily-content-skill

日常内容创作 Skill：改写润色、中英互译、长文摘要、标题生成、语气转换。

## 触发条件

当用户需要处理日常文字创作任务时调用本 Skill：
- 改写/润色一段文字（口语化、正式、简洁、营销等风格）
- 中英文本互译
- 长文章/邮件/报告提炼要点
- 为文章生成多个备选标题
- 转换文字的语气（正式→轻松、礼貌→强硬等）

## 使用方式

本 Skill 通过 CLI 入口 `skill.py` 提供服务，需在 `.env` 配置 LLM：

```bash
# 改写润色
python skill.py rewrite "原文" [--style 口语化|正式|简洁|营销|学术]
python skill.py rewrite --file 文章.md --style 正式

# 中英互译
python skill.py translate "Hello world" --to zh
python skill.py translate "你好世界" --to en

# 长文摘要
python skill.py summarize "长文本..." [--points 3]
python skill.py summarize --file 报告.txt

# 标题生成
python skill.py title "文章主题" [--count 5] [--style 吸睛|专业|文艺]

# 语气转换
python skill.py tone "原文" [--to 礼貌|轻松|正式|强硬|鼓励]
```

## 配置

需要 LLM API，在 `.env` 中配置：

```
OPENAI_API_KEY=sk-xxx
OPENAI_BASE_URL=https://api.openai.com/v1
CHAT_MODEL=gpt-4o-mini
```

## 子功能说明

### 1. 改写润色 (rewrite)
- 支持多种风格：口语化、正式、简洁、营销、学术
- 从文件或直接文本输入
- 保持原意，优化表达

### 2. 中英互译 (translate)
- 中英双向翻译
- 保持语气和风格

### 3. 长文摘要 (summarize)
- 提取摘要和核心要点
- 可指定要点数量

### 4. 标题生成 (title)
- 一次性生成多个备选标题
- 支持不同风格（吸睛/专业/文艺）

### 5. 语气转换 (tone)
- 多种语气目标：礼貌、轻松、正式、强硬、鼓励
- 转换语气的同时保留原信息

## 设计要点

- 统一 LLM 客户端封装，所有子功能复用
- Prompt 模板独立成文件，便于调整和复用
- 支持直接文本和文件两种输入方式
- 每个子功能有独立的系统提示词设计
