---
type: Tool
title: "dsh-auto-mode（NanmiCoder/dsh-auto-mode）"
description: "DeepSeek Harness 权限分级插件：常规项目操作在 workspace-write 沙箱里直接跑，越界高风险动作交模型分类审查，真正会毁数据的才拦"
resource: "https://github.com/NanmiCoder/dsh-auto-mode"
tags: "[deepseek-harness, dsh, sandbox, permission, security]"
timestamp: "2026-08-19T16:00:00Z"
---

# dsh-auto-mode（NanmiCoder/dsh-auto-mode）

## 它是什么
[`NanmiCoder/dsh-auto-mode`](https://github.com/NanmiCoder/dsh-auto-mode) 填补 DeepSeek Harness 在「**权限分级**」上的空档：把 dsh 的工作流划分成「workspace-write 沙箱内可直接跑」与「越界高风险动作需模型分类审查」两类，真正会**毁数据**的动作才拦截；其它常见项目操作默认放行，减少人工一次次确认的疲劳。

## 为什么用它 / 适合什么场景
- dsh 默认每一步都问「要不要继续」，长任务被打断太多。
- 又怕直接「yes & run everything」会出 rm -rf / 强制 push / 删数据库这类事故。
- 想在「自动化效率」与「关键动作安全」之间找一个平衡点。

## 关键能力
| 能力 | 说明 |
|------|------|
| 工作区分级 | 沙箱内常规操作免确认，越界高风险需审查 |
| 模型分类审查 | 高风险动作由模型二次判断「是否真正危险」 |
| 真正兜底 | 只拦会毁数据的动作，其余都放行 |
| dsh 原生 | 作为 dsh 插件挂载，无外部依赖 |

## 相关概念
- [项目仓库](https://github.com/NanmiCoder/dsh-auto-mode) — 仓库主页
- [dsh-agent-teams](./tool-dsh-agent-teams.md) — 同作者（NanmiCoder）的 dsh 多代理插件
- [agent-lock](./tool-agent-lock.md) — eBPF LSM 把 AI 代理限制在指定目录（更底层的硬隔离思路）