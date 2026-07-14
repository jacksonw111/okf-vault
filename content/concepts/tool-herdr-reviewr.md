---
type: "Tool"
title: "herdr-reviewr（persiyanov/herdr-reviewr）"
description: "终端 AI agent herdr 的代码审查侧栏:agent 改了什么就在聊天旁边开面板摊开 diff,可逐行批注,按发送即把意见灌回 agent 输入框;顺带只读浏览 PR 与工作树。"
resource: "https://github.com/persiyanov/herdr-reviewr"
tags: "[code-review, diff, ai-agent, terminal, herdr, pr]"
timestamp: "2026-07-14T01:26:00Z"
---

# herdr-reviewr

[herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) 是给 **herdr**(终端里的 AI agent)配的**代码审查侧栏**:agent 一动文件,你就能在它聊天旁边开个面板摊 diff、批注,把多行意见一股脑灌回 agent 的输入框。顺带只读浏览 PR 与整棵工作树。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时 diff | agent 的改动自动以面板形式摊开 |
| 逐行批注 | 选中行即可写批注 |
| 一键回灌 | 按下发送,所有批注批量灌回 agent 输入 |
| PR 浏览 | 只读模式浏览当前 PR 详情 |
| 工作树浏览 | 在侧栏浏览整个工作树,不改文件 |
| 终端原生 | 嵌入 herdr 终端 TUI,不跳到 GUI |

## 适合什么场景

- 长期用 herdr / 类似终端 AI agent 的开发者,**想要审稿环节不那么碎片**。
- Code review 流程从「打开 GitHub 网页」简化到「就在终端批一句」的场景。
- 想让 agent 的每一步改动都过一道「人审」,而不是跑完一锤定音。

## 与同类资源的差别

| 资源 | 特征 | herdr-reviewr |
|------|------|---------------|
| fuzzier | 在线代码 review 工具 | 在线;herdr-reviewr 在终端 |
| Codex Pro | ChatGPT Web ↔ 本地仓库 MCP 桥 | 模型连接;herdr-reviewr 是审稿 UI |
| Aura-IDE | diff 审批 | GUI;herdr-reviewr 终端原生 |

## 参考链接

- [项目仓库](https://github.com/persiyanov/herdr-reviewr)

## 相关概念

- [Aura-IDE](./tool-aura-ide.md) — 同样支持 diff 审批,但走 GUI(双智能体本地编码工作台)
- [CodexPro](./tool-codexpro.md) — ChatGPT Web ↔ 本地仓库 MCP 桥,模型层桥接
