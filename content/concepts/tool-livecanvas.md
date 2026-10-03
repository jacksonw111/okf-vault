---
type: "Tool"
title: "LiveCanvas（pengchujin/livecanvas：给 Codex / Claude Code 的「Live 图」生成 Skill）"
description: "pengchujin 出品的 Agent Skill：输入一句话 → 搜索核实 → 设计分镜 → Remotion 动画 → 预览与 Apple Live Photo 资源——一条流水线产出「带封面、有动画」的 Live 图。"
resource: "https://github.com/pengchujin/livecanvas"
tags: "[agent-skills, video, animation, remotion, live-photo, claude-code, codex]"
timestamp: "2026-10-03T00:00:00Z"
---

# LiveCanvas

## 它是什么

[LiveCanvas](https://github.com/pengchujin/livecanvas) 是 **pengchujin** 出品的 **Agent Skill**——给 Codex / Claude Code 等编码 Agent 加载后，Agent 可以**输入一句话就产出有封面、有动画的 Live 图**。

## 流水线

```
一句话
  ↓ 搜索核实（确保事实 / 来源）
  ↓ 设计分镜（关键帧 / 镜头节奏）
  ↓ Remotion 动画（React 编程式视频）
  ↓ 预览 + Apple Live Photo 资源输出
```

## 为什么用它 / 适合什么场景

- **「一张图不够，得动起来」**：科普 / 教程 / 营销类内容往往要动画图，比静态截图更有传播力。
- **不必学 Remotion**：Agent 按 Skill 流程跑完，用户只关心内容。
- **多平台产物**：可导出 Live Photo（iOS 主屏 / 锁屏动画）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | 一句话主题 |
| 步骤 | 搜索核实 → 设计分镜 → Remotion 动画 → 预览 |
| 输出 | 视频 + Apple Live Photo 资源 |
| 适用 Agent | Codex / Claude Code 等 |
| 编程模型 | Remotion（React 编程式视频） |

## 参考链接

- 项目链接：<https://github.com/pengchujin/livecanvas>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 装载机制
- [Explainroo](./tool-explainroo.md) — 同类「Agent 一条龙产出视频」方向
