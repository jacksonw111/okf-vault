---
type: Tool
title: "unbox-ai（LLM trace 摊开画图：把每轮的 system prompt 和工具定义从重复消息里拎出来）"
description: "把 LLM 调用 trace 中每轮都重复发送的 system prompt 和工具定义摊开可视化，省去逐条翻几百条重复消息；token 浪费一目了然，便于调提示词与上下文工程。"
resource: "https://github.com/tester-army/unbox-ai"
tags: [llm, observability, trace, token, prompt-engineering, debugging, ai-tooling]
timestamp: "2026-08-28T00:00:00Z"
---

# unbox-ai

## 它是什么
[tester-army/unbox-ai](https://github.com/tester-army/unbox-ai) 是**给 LLM 调用 trace 解包的可视化工具**。痛点：每轮 LLM 生成都会**重新发送** system prompt 和工具定义（tools / functions schema），一长会话里这些内容占 trace 中八成以上的 input token——但人眼看原始 trace 时，要从几百条重复消息里逐条比对才能看出哪些是「真新增」哪些是「机械重复」。

unbox-ai 把这些**重复摊开**：

- **system prompt**单独提取并高亮重复模式；
- **工具定义**按 schema 拆开，每条工具的出现频次、token 占比单独统计；
- **真新增消息**与**机械重复内容**用不同颜色 / 视图分层；
- 输出图与统计，让人**一眼看出** token 都耗在哪儿。

## 为什么用它 / 适合什么场景
- 调试 AI Agent 应用的 token 成本——发现「我以为只是几次调用，怎么账单爆了」；
- 优化 system prompt 体积或工具 schema 设计时，需要**量化证据**判断哪一块该砍；
- 排查 Agent 多轮对话中**上下文膨胀**的具体来源；
- 给团队 / 客户讲解「LLM 调用为什么这么贵」时的可视化证据。

## 关键能力
| 能力 | 说明 |
|------|------|
| Trace 解包 | 把每轮重复的 system prompt / 工具定义摊开 |
| 重复识别 | 自动标出哪些字段、哪些工具反复重发 |
| Token 占比 | 统计重复内容 vs. 真新增内容各占多少 input token |
| 可视化 | 图与表格替代「翻几百条 JSON」 |
| 提示工程 | 给出 system prompt 裁剪 / 工具收敛的量化依据 |
| Agent 调试 | 排查上下文膨胀、token 浪费来源 |

## 相关概念
- [DSH Context](tool-dsh-context.md) — DSH 上下文窗口可视化插件，把 token 用量与压缩过程拆开；unbox-ai 是**通用 Agent 场景**的同类思路
- [Codex Trajectory](tool-codex-trajectory.md) — Codex 任务日志结构化解析，unbox-ai 在 token 经济性维度上更深一层
- [Token Timer Core](tool-tokentimer-core.md) — 证书 / 密钥 / 许可证到期 + 用量监测；unbox-ai 专注 LLM 调用的 input token 维度

## 参考链接
- 项目链接：<https://github.com/tester-army/unbox-ai>
- 原始推文：<https://x.com/QingQ77/status/2093259541324652766>
