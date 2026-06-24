---
type: "Tool"
title: "AgentStalker（AI Agent 系统级安全审计）"
description: "把 LLM Agent 当系统而非模型来审计：从源码抽污点图 → 合成攻击链 → 沙箱重放 → 出判定报告，支持 LangChain/AutoGen/CrewAI 等主流框架。"
resource: "https://github.com/Gach0ng/AgentStalker"
tags: [security, agent, audit, llm, python, rust]
timestamp: "2026-06-24T15:30:00Z"
---

# AgentStalker（AI Agent 系统级安全审计）

## 它是什么

[`Gach0ng/AgentStalker`](https://github.com/Gach0ng/AgentStalker) 是一个**面向 AI Agent 的端到端安全评估框架**。与传统的「针对模型本身做红队」不同，它把 Agent 视作一整套系统来审计，按四步走完一轮评估：

1. **静态建模** — 把 Agent 项目的源码抽象为「污点图」（taint graph），记录数据从用户输入到工具调用 / 模型输出 / 文件系统 / 外部请求的流向；
2. **攻击链合成** — 根据污点图自动合成候选攻击链，把可能「污染面」串成可执行的攻击路径；
3. **沙箱动态验证** — 在隔离沙箱里重放攻击链，触发实际行为（命令执行、文件读取、HTTP 出站等）；
4. **判定报告** — 给出可命中 / 未命中 / 风险等级的判定报告。

## 为什么用它 / 适合什么场景

- **面向 Agent 应用的真实风险**：模型越狱只是冰山一角，更多漏洞藏在 tool/插件/agent 编排里，AgentStalker 瞄准这块；
- **不需要手写攻击脚本**：从源码自动生成攻击链，节省红队时间；
- **覆盖主流框架**：内置对 LangChain、AutoGen、CrewAI 等 Python / Rust Agent 项目的解析器；
- **沙箱安全**：所有动态验证都在隔离环境跑，本机不会被反伤。

## 关键能力

| 能力 | 说明 |
|---|---|
| 静态污点分析 | 源码 → 污点图 |
| 攻击链合成 | 13 类 payload + 10 条多轮攻击链模板 |
| 沙箱重放 | 隔离环境动态执行 |
| 报告输出 | 可命中 / 风险等级 / 修复建议 |
| 框架覆盖 | LangChain / AutoGen / CrewAI 等 |
| 双语言 | Python + Rust Agent 项目都支持 |

## 媒体 / 参考链接

![架构示意](https://pbs.twimg.com/media/HLjBpqbasAEOP4o.jpg)

- [项目链接](https://github.com/Gach0ng/AgentStalker)

## 相关概念

- [ORGII](tool-orgii.md) — Rust + Tauri 多 Agent 协作框架，作为受测对象的相关工作
- [Brigade](tool-brigade.md) — 本地多代理协作框架，同样可作为受测对象
- [Vercel Eve 框架](tool-vercel-eve-framework.md) — filesystem convention 的 Agent 框架，可作为受测对象
