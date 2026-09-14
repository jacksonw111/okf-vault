---
type: "Term"
title: "Context Engineering（上下文工程）"
description: "围绕「给 LLM 的上下文怎么选、怎么排、怎么省」展开的工程实践：检索、压缩、句柄化、摘要、计划压缩等都属于这个范畴。"
tags: "[context-engineering, llm, prompt, rag, token-saving, agent]"
timestamp: "2026-09-14T22:30:00Z"
---

# Context Engineering（上下文工程）

## 它是什么

**Context Engineering（上下文工程）** 是围绕 **「LLM 上下文窗口里到底放什么、怎么放、什么时候刷新」** 展开的工程实践。它比 prompt engineering 更广——不仅写好 prompt，还包括**检索 / 压缩 / 摘要 / 句柄化 / 计划压缩**等整套让上下文「既够用又不爆」的招数。

Andrej Karpathy 在 2025 年明确提出：「Context Engineering is the delicate art and science of filling the context window with just the right information for the next step.」

## 与 Prompt Engineering 的关系

| 维度 | Prompt Engineering | Context Engineering |
|------|--------------------|--------------------|
| 关心什么 | 单条 prompt 怎么写 | 整段上下文窗口怎么管理 |
| 关注点 | 措辞 / 示例 / 角色 | 检索 / 压缩 / 摘要 / 状态 |
| 时代 | 早期 LLM | LLM 走向长任务 / agent 时代 |

## 常见技法

| 技法 | 解决什么 | 代表项目 |
|------|----------|----------|
| 检索（RAG） | 上下文不够新 / 私有时补知识 | LangChain / pgvector |
| 句柄化 | 重复用大块结果时按页取 | SoL-Pi |
| 日志摘要 + 原文可查 | 长日志占满上下文 | SoL-Pi |
| 计划压缩 | 计划越写越长 | SoL-Pi |
| 多轮摘要 | 跨多轮对话保留关键信息 | LangGraph Memory |
| Playbook / Skills 注入 | 临时切换角色 / 规则 | Skills 系统 |
| 工具结果精简 | 工具返回原始 JSON 太大 | LangChain trim_messages |

## 实战法则

1. **少即是多** —— 没用的旧消息、工具结果、system 指令都该清掉
2. **可回查** —— 摘要时把原文留在可回查接口
3. **结构化** —— 计划 / 任务清单 / 当前状态写成结构化块而非自然语言
4. **分页 / 句柄** —— 大文档按页访问，避免整段重传
5. **缓存前缀** —— 静态 system / 工具说明放前缀，享 prompt cache 折扣

## 相关概念

- [SoL-Pi（NVIDIA 给 Pi 的省 token 扩展）](./tool-sol-pi.md) — 四招上下文工程技法具体实现
- [RAG（检索增强生成）](./term-rag.md) — 上下文工程的检索分支
- [Pi Coding Agent](./tool-pi-coding-agent.md) — 上下文工程落地的典型宿主

## 参考链接

- Anthropic 上下文工程指南：<https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-context-windows>
