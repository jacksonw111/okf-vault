---
type: "Tool"
title: "VibeSDK（SLOWRAINMDML/vibesdk）"
description: "「说句话就生成可用应用」的 AI 编程平台整套开源,部署到自己的 Cloudflare 账户即可跑;内置模型路由 / 沙箱 / 存储 / 预览,免去自建 vibe-coding 平台时从零搭基础设施的成本。"
resource: "https://github.com/SLOWRAINMDML/vibesdk"
tags: "[vibe-coding, cloudflare, ai-app-generator, open-source, self-hosted]"
timestamp: "2026-08-11T16:00:00Z"
---

# VibeSDK

[VibeSDK](https://github.com/SLOWRAINMDML/vibesdk) 是把"**说句话就生成可用应用**"的 AI 编程平台整套开源——从模型接入、沙箱执行、文件存储到预览,部署到自己的 Cloudflare 账户即可跑,改起来没有限制。

项目链接：<https://github.com/SLOWRAINMDML/vibesdk>

## 它是什么

一个**自托管 vibe-coding 平台引擎**:把通常闭源的 Bolt / v0 / Lovable 类产品背后的关键组件(LLM 路由 / 代码生成 / 安全沙箱 / 实时预览 / 持久化)全做出来,部署即用,改起来没有 license 限制。

## 为什么用它 / 适合什么场景

- **自建 vibe-coding 服务**:想自己控制模型、用户数据、计费时直接 fork。
- **Cloudflare 部署**:Workers + D1 + R2 等基础设施天然契合。
- **改起来无限制**:可商用、可重塑。

## 关键能力

| 能力 | 说明 |
|------|------|
| LLM 路由层 | 多模型切换 / 故障转移 |
| 安全沙箱 | 用户生成的代码在隔离环境执行 |
| 实时预览 | 边生成边预览 |
| 持久化 | 文件 / 项目状态保存 |
| Cloudflare 原生 | Workers + D1 + R2 等基础架构 |
| 开源可商用 | 部署到自己的账户即可上线 |
| 可塑性强 | 无 license 限制,可改可二次开发 |

## 媒体

![](https://pbs.twimg.com/media/HPUz9crbcAACieQ.jpg)

## 参考链接

- [项目仓库](https://github.com/SLOWRAINMDML/vibesdk)

## 相关概念

- [Vibe Coding Design System](./playbook-vibe-coding-design-system.md) — Vibe Coding 摆脱「UI 调试地狱」八步法,与本工具互补(设计约束 vs 平台基建)
- [Cloudflare Workers](./tool-cloudflare-workers.md) — 本工具的部署载体
- [Codex Work Starter](./tool-codex-work-starter.md) — 给不会写代码的人一条稳妥 Codex 路线,与 vibe-coding 路线形成对照