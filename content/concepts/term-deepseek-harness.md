---
type: "Term"
title: "DeepSeek Harness（DSH，可插拔智能体框架）"
description: "DeepSeek 官方开源的智能体框架家族统称：把推理循环每个环节（模型 / 工具 / 存储 / agent loop）做成可插拔插件，可在配置层面整体替换，不必改内核；周边已衍生出桌面端、GUI、Rust 绑定、Studio、Plugin 市场等数十个生态项目。"
resource: "https://github.com/deepseek-ai/deepseek-harness"
tags: "[deepseek, agent-framework, pluggable, dsh, harness]"
timestamp: "2026-09-28T23:40:00Z"
---

# DeepSeek Harness（DSH，可插拔智能体框架）

## 定义

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（社区常称 **DSH**）是 DeepSeek 官方开源的**可插拔智能体框架**：把推理循环（inference loop）的**每一环**——模型适配、工具调用、存储、会话记忆、甚至 agent loop 本身——都做成**可插拔插件**。

设计哲学是「**配置可替换、内核不动**」：任何想换的部分都不必改 DSH 源码，而是写一个 plugin、在配置里挂上去。

## 要点

- **全链路可插拔**：模型 / 工具 / 存储 / loop 都能替换
- **配置驱动**：不改代码，只改配置
- **模型无关**：DeepSeek / Claude / 本地 GGUF 都可挂
- **生态庞大**：官方核心仓库之外，已衍生出 Desktop、GUI、Rust 绑定、Studio、Plugin 市场等数十个周边项目（统一以 `dsh-*` / `*dsh*` 命名）
- **代表周边**：
  - 桌面端：[WorkDSH](./tool-workdsh.md) / [DSH-X](./tool-dsh-x.md) / [DSH Desktop](./tool-deepseek-harness-desktop.md)
  - 教程：[DSH 中文零基础手册](./note-deepseek-harness-handbook.md) / [DSH 橙皮书（开源 24h 非开发者视角）](./note-deepseek-harness-orange-book.md) / [Limbo101 教程站](./tool-limbo101-tutorials.md)
  - 工具集：[awesome-deepseek-harness](./tool-awesome-deepseek-harness.md) / [DSH Plugin 市集](./tool-dsh-plugin-shop.md)

## 相关概念

- [deepseek-harness-core](./tool-deepseek-harness-core.md) — 官方仓库本体（实现该框架的代码）
- [WorkDSH](./tool-workdsh.md) — 基于 DSH 的 Electron 桌面工作台
- [Limbo101 教程站](./tool-limbo101-tutorials.md) — 把 DSH 与本地 AI 代理讲透的可视化教程合集