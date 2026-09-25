---
type: "Tool"
title: "threejs-architecture-effects（三维古建生成的 Agent Skill）"
description: "让 Codex / Claude Code / Cursor 按统一方法生成可旋转查看、能逐层或逐块搭建的三维古建网站——基于 Three.js + React + Vite，砖 / 木 / 石 / 瓦 / 铜等材质全部代码生成，不用付费模型或 API。"
resource: "https://github.com/lhlGitHub/threejs-architecture-effects"
tags: "[threejs, react, vite, agent-skill, architecture, 3d, ancient-buildings, claude-code, codex, cursor, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# threejs-architecture-effects（三维古建生成的 Agent Skill）

## 它是什么

[threejs-architecture-effects](https://github.com/lhlGitHub/threejs-architecture-effects) 是一个生成**交互式三维古建**的 **Agent Skill**——给 Codex / Claude Code / Cursor 等编码 Agent 一套统一方法，输出**可旋转查看、能逐层或逐块搭建**的三维古建网站。

技术栈：

- **Three.js** —— 3D 渲染
- **React** —— UI 层
- **Vite** —— 构建

建筑由**砖块 / 木架 / 斗拱 / 屋檐 / 瓦片**等实体组成，搭建过程可**暂停 / 回放**。

材质（砖 / 木 / 石 / 瓦 / 铜）全部由**代码生成**，**不依赖付费模型或付费 API**。

## 为什么用它 / 适合什么场景

- 想让 AI 编码 Agent **一键搭一个可交互的中国古建 demo**——做文博站、教学课件、个人作品集都不错。
- 不愿意每次都让 Agent 重新设计建筑结构，需要一份**可复用的 Skill**作为脚手架。
- 想**完全本地化**：没有外部 3D 模型下载、没有付费纹理 API、没有第三方服务依赖。
- 适合作为「**3D + Agent Skill**」的模板——照着这个 Skill 的写法，把建筑换成机甲 / 园林 / 城市 / 飞船都很顺。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Agent Skill（Codex / Claude Code / Cursor 通用） |
| 技术栈 | Three.js + React + Vite |
| 建筑构成 | 砖块 / 木架 / 斗拱 / 屋檐 / 瓦片等实体 |
| 交互 | 可旋转查看 |
| 搭建动画 | 逐层 / 逐块搭建，可暂停 / 回放 |
| 材质 | 砖 / 木 / 石 / 瓦 / 铜，全部代码生成 |
| 外部依赖 | 无付费模型 / 无付费 API |

## 媒体

视频演示：

<https://video.twimg.com/amplify_video/2103297138377805824/vid/avc1/1280x740/W4WVDz0vlNjAog2j.mp4?tag=29>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — threejs-architecture-effects 所属的技能生态
- [Codex 3D 场景工作流](./note-codex-3d-scene-workflow.md) — Codex 生成 3D 场景的另一类流程
