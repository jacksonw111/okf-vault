---
type: "Tool"
title: "Tulip（PR 评审 HTML 生成器）"
description: "VirtusLab 出品的 TypeScript CLI，调用本机已登录的 claude CLI 分析 PR 改动并生成带 Mermaid 图 / diff 高亮 / 浮动目录的单页 HTML。"
resource: "https://github.com/VirtusLab/tulip"
tags: "[pr-review, html-report, claude-code, sonnet, opus, haiku, mermaid, typescript-cli, code-review]"
timestamp: "2026-09-17T12:39:00Z"
---

# Tulip（PR 评审 HTML 生成器）

## 它是什么

[VirtusLab/tulip](https://github.com/VirtusLab/tulip) 是 **VirtusLab** 出品的 TypeScript CLI。它把 GitHub PR 的代码改动**按关注度分组排序**，生成一份「从总览讲到代码细节」的 HTML 页面——审阅者**不必逐行翻 diff**，就能判断 PR 该不该收。

安装后在 PR 链接后面追加 `tulip` 即可触发。

## 工作流（多模型协作）

它借用**本机已登录的 claude CLI**做多轮分析（无需 API key）：

| 模型 | 角色 |
|------|------|
| Sonnet | 把改动**分组**，并按 Read closely / Read through / Skim 三档排序 |
| Haiku | 把每条改动**归到组里**，顺带丢掉 lockfile 等无关噪声 |
| Opus | 逐组**写讲解** |

最终拼成一张单页 HTML，包含：

- **Mermaid 图**（变更影响范围的可视化）
- **并排高亮 diff**（旧 / 新代码并列）
- **浮动目录**（长报告也方便跳转）

## 适合什么场景

- 收件箱里有大量 PR、需要快速判断「先看哪些 / 可以直接合 / 应该驳回」的维护者。
- 想给团队 / 社区贡献者一份「易消化的 PR 概览」的开源项目维护者。
- 已用 Claude Code 的人——直接复用本机登录状态，**无需单独申请 / 配置 API key**。

## 与相关概念的关系

- [Claude Code](./tool-claude-code.md) — Tulip 通过本机已登录的 claude CLI 调度 Sonnet / Opus / Haiku，Claude Code 是其能力底座。

## 参考

- 项目链接：<https://github.com/VirtusLab/tulip>

![preview](https://pbs.twimg.com/media/HSY5PqTbEAAlhti.jpg)
