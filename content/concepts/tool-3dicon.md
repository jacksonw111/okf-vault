---
type: "Tool"
title: "3dicon（描述 / 静态图 → 3D 动画 WebP 图标的 Claude Code 技能）"
description: "用 Claude Code 技能把一句描述或一张静态图变成可无缝循环、带真实透明通道的 3D 动画 WebP 图标。"
resource: "https://github.com/samyost1/3dicon"
tags: "[3d, webp, animated-icon, transparent, claude-code-skill, agent-skill, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# 3dicon（描述 / 静态图 → 3D 动画 WebP 图标的 Claude Code 技能）

## 它是什么

[3dicon](https://github.com/samyost1/3dicon) 是一个 **Claude Code 技能**——把一句自然语言描述、或一张静态图，**自动转成 3D 动画 WebP 图标**：

- **无缝循环**（loop seam 看不见）
- **真实透明通道**（Alpha 通道干净，可用做 favicon / app icon / 加载占位）
- 一次生成，多端复用

## 为什么用它 / 适合什么场景

- 想给应用 / 网站 / 文档站做一组**动效图标**，但又没有 3D 设计师、又不想用 After Effects / Blender 折腾。
- 想要**透明背景的动效图标**——很多 AI 视频 / 动效工具默认黑底或白底，抠图又是体力活。
- 想从「一句话」或「一张静图」就能**反复迭代**出想要的图标，迭代成本接近零。
- 产物**WebP 体积小**，适合直接放进 web、移动端、Electron、Raycast 扩展等场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Claude Code Skill |
| 输入 | 一句描述 / 一张静态图 |
| 输出 | 3D 动画 WebP 图标 |
| 透明通道 | 真实 Alpha（可用做 favicon / app icon） |
| 循环 | 无缝 loop |
| 复用 | 一次生成，多端使用 |

## 媒体

视频演示（3D 动画 WebP 预览）：

<https://video.twimg.com/amplify_video/2103289790854799360/vid/avc1/1800x600/VPwcsUjcqKnP7ZNM.mp4?tag=29>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 3dicon 所属的技能生态
- [Regen Icons](./tool-regen-icons.md) — Shopify 出品的 AI Agent 图标系统（JSON 绘图语言 + 多 Agent 指令），3dicon 偏向「动效」一侧
