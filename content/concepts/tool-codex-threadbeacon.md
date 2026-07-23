---
type: "Tool"
title: "ThreadBeacon（Codex 任务状态原生小窗）"
description: "ExDevilLee/codex-threadbeacon-windows，Windows 上为 Codex 主任务开一个原生小窗，实时显示运行状态 / 完成度 / 异常中断；只读访问本地 SQLite 与日志，检测到 HTTP 429 / 503 / 400 后按预设规则自动续接。"
resource: "https://github.com/ExDevilLee/codex-threadbeacon-windows"
tags: "[codex, windows, monitoring, coding-agent, recovery]"
timestamp: "2026-07-23T00:48:00Z"
---

# ThreadBeacon（Codex 任务状态原生小窗）

## 它是什么

[`ExDevilLee/codex-threadbeacon-windows`](https://github.com/ExDevilLee/codex-threadbeacon-windows) 是 Windows 上的 **Codex 任务状态监测小窗**——开一个原生窗口，实时显示 Codex 主任务的运行状态、完成情况和异常中断。

- **只读**：只读访问本地 SQLite 和日志，**不改任何文件**
- **自动续接**：检测到 HTTP 429 / 503 / 400 等服务异常后，可按预设规则自动续接任务
- **可定制**：支持置顶、收藏、忽略任务、行内展开 Subagent、自定义提示音和深浅主题

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生小窗 | Windows 原生窗口，不抢浏览器标签页 |
| 实时状态 | 跑 Codex 主任务时实时看到进度 |
| 异常检测 | 检测 HTTP 429 / 503 / 400 等服务异常 |
| 自动续接 | 按预设规则自动恢复中断任务 |
| Subagent 展开 | 行内展开 Subagent 的运行 |
| 自定义提示音 | 任务结束 / 异常时可听声音 |

## 为什么用它

- **不抢屏幕**：独立小窗贴在屏幕边角，不影响 IDE / 浏览器
- **不污染 Codex 数据**：只读访问 SQLite 和日志
- **避免 429 焦虑**：自动续接减少人工值守
- **适合长任务**：训练 / 批量生成 / 跑评测

## 媒体

![](https://pbs.twimg.com/media/HNzK_8JacAASH2m.png)
![](https://pbs.twimg.com/media/HNzLFD7bAAAECp9.png)

## 相关概念

- [Claude Pulse](./tool-claude-pulse.md) — 同类「编码 Agent 仪表盘」，但面向 Claude Code
- [AI Meter](./tool-ai-meter.md) — 同类「编码 Agent 用量可视化」，但 macOS 菜单栏形态
- [Token Usage Insights](./tool-token-usage-insights.md) — 跨 Agent（Antigravity / Copilot / Codex / Claude Code）的 Token 战情室
- [codex](./tool-codex.md) — OpenAI 官方 Codex CLI / 桌面端，本工具是它的状态伴侣

## 原始链接

- [项目仓库](https://github.com/ExDevilLee/codex-threadbeacon-windows)