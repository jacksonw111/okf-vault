---
type: "Tool"
title: "CXX（微信远程接管 Codex / Claude Code 会话）"
description: "用微信当遥控器，远端接管电脑里跑的 Codex / Claude Code：看会话进度、审批命令、发新指令——不用一直守在电脑前。"
resource: "https://github.com/focuxdot/CXX"
tags: [wechat, codex, claude-code, remote-control, ai-coding-agent, mobile]
timestamp: "2026-08-30T21:50:00Z"
---

# CXX

## 它是什么
[focuxdot/CXX](https://github.com/focuxdot/CXX) 是一个把**微信**变成 **AI 编码代理遥控器**的开源工具：在电脑上跑 Codex 或 Claude Code 时，手机微信里就能**看会话进度、审批待执行的命令、再发一条新指令**——不再需要一直守在电脑前。

工作流程：

1. 电脑端启动 Codex / Claude Code；
2. CXX 把代理的输出 / 待审批动作转发到**个人微信**；
3. 手机微信回复即可审批 / 注入指令；
4. 代理继续在电脑上跑。

## 为什么用它 / 适合什么场景
- 通勤 / 出差途中想**继续推进**一次 AI 编码任务，又不想开 VPN + 远程桌面；
- **长任务监控**：让 Codex / Claude Code 在后台跑，微信收到「**需要你审批**」时才看；
- **降低注意力成本**：不用一直盯着终端流；
- 微信是**国内默认消息工具**——比再装一个 IM App 现实。

## 关键能力

| 能力 | 说明 |
|------|------|
| 微信端遥控 | 个人微信接收进度 / 审批 / 指令 |
| 多代理支持 | Codex / Claude Code 等 |
| 命令审批 | 高危命令要二次确认 |
| 指令注入 | 在跑任务中追加 prompt |
| 长任务友好 | 后台跑、被动响应 |

## 媒体
- ![](https://pbs.twimg.com/media/HQ5UEFZbkAALcAN.jpg)

## 相关概念
- [Claude Code](tool-claude-code.md) — CXX 的主要遥控目标之一
- [Pi Agent 桌面客户端](tool-pi-agent-desktop.md) — JetBrains Pi 编码代理的桌面端；CXX 是「**手机端**」对应物
- [Lody](tool-lody.md) — 通过 ACP 把任意机器上的 Claude Code / Codex / Kimi / OpenCode 接入团队共享工作空间；CXX 是「**个人微信**」对应物

## 参考链接
- 项目链接：<https://github.com/focuxdot/CXX>
