---
type: Tool
title: "pi-tbox（Pi 扩展工具开关面板）"
description: "Pi 终端 AI 助手装多了扩展后，每个扩展都带一堆工具，但 Pi 本身没统一面板去查看或开关它们。pi-tbox 在一个命令里集中展示、按声明分组整组开关、自定义分组、跨会话保持选择。"
resource: "https://github.com/coreyryanhanson/pi-tbox"
tags: [pi, ai-coding, tui, extension-manager, tool-registry]
timestamp: "2026-07-30T23:54:00.000Z"
---

# pi-tbox

## 它是什么

**Pi 扩展工具的开关面板 / 路由器**——Pi 终端 AI 助手每装一个扩展都会带来一组工具，但 Pi 没有提供统一入口去查看、开关、按需激活。

pi-tbox 填补这块缺口：

- **一次列出所有扩展声明的工具**——一眼看清现在到底能用啥
- **按扩展声明的分组整组开关**——临时禁用整个 AI 编程套件去做别的
- **自定义分组**——把零散的 extension 工具按工作流重组成「写代码组 / 调研组 / 写作组」
- **跨会话保持**——选择持久化，下次启动 Pi 直接复用

## 解决的痛点

| 痛点 | pi-tbox 解法 |
|------|-------------|
| 工具列表太长，无法看清 | 一屏列出 + 分组 |
| 想临时关一组但要逐个找 | 整组一键开关 |
| 不同任务需要不同工具子集 | 自定义工作流分组 |
| 重启会话选择丢失 | 跨会话持久化 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 全工具盘点 | 一个 TUI 页面列全 |
| 分组开关 | 按扩展声明或自定义 |
| 工作流分组 | 自定义命名 + 持久化 |
| 跨会话 | 偏好持久保存 |
| Pi 原生 | 跑在 Pi 里，不开新进程 |

## 适合谁

- Pi 重度用户，扩展装了十几个
- 不同任务想用不同工具子集（写代码时关掉浏览器工具）
- 想保持"最小可用工具集"的工程师

## 原始链接

- [项目仓库](https://github.com/coreyryanhanson/pi-tbox)
- [推文剪藏](https://x.com/QingQ77/status/2082615656030068931)

## 相关概念

- [pi-extensible-workflows](./tool-pi-extensible-workflows.md) — Pi 终端 AI 助手的多代理工作流编排，并行/审批/断点恢复
- [pi-task](./tool-pi-task-delegation.md) — Pi Agent 子任务委派扩展
- [pi-fusion](./tool-pi-fusion.md) — Pi 多模型并行扇出扩展