---
type: "Tool"
title: "Universal Modder（rehan-remade：游戏 Mod 的 Agent Skills 套件）"
description: "rehan-remade 出品的游戏 Mod 制作 Skill 套件：把 Mod 工作拆成 10 个 Agent Skill（侦察引擎、读代码、生成贴图模型、进游戏验证）配 12 份引擎手册（Unity/Unreal/Godot/Source/Bethesda/RE Engine 等），Claude Code / Codex / Cursor / Gemini CLI 这些读 AGENTS.md 的都能用。"
resource: "https://github.com/rehan-remade/universal-modder"
tags: "[game-mod, agent-skills, unity, unreal, godot, source-engine, claude-code, codex, cursor]"
timestamp: "2026-10-02T03:50:00Z"
---

# Universal Modder（rehan-remade：游戏 Mod 的 Agent Skills 套件）

## 它是什么

[Universal Modder](https://github.com/rehan-remade/universal-modder) 是 rehan-remade 出品的**游戏 Mod Agent Skills 套件**——把「侦察引擎 → 读代码 → 生成贴图 / 模型 → 进游戏验证」一整条 Mod 流水线拆成 **10 个 Agent Skill**，并配 **12 份引擎手册**（Unity / Unreal / Godot / Source / Bethesda / RE Engine 等），让编码 Agent（Claude Code / Codex / Cursor / Gemini CLI）按 AGENTS.md 直接开干。

## 为什么用它 / 适合什么场景

| 场景 | Universal Modder 的好处 |
|------|------------------------|
| 不会写代码也想做 Mod | 把任务交给 Agent，按 10 步走完即可 |
| 想给老游戏加新内容 | 12 份引擎手册覆盖主流老引擎（Source / Bethesda / RE Engine） |
| 想批量生成贴图 / 模型 / 音效 | Skill 中段集成 fal 等生图 API |
| 跨引擎复用 | 同一套 Skill 流程适用于多个引擎 |
| Agent 编码工具用户 | 读 AGENTS.md 即可，Claude Code / Codex / Cursor / Gemini CLI 全支持 |

## 流水线（10 个 Skill）

| # | Skill | 做什么 |
|---|-------|--------|
| 1 | recon-engine | 识别游戏引擎版本与加载器 |
| 2 | read-codebase | 逆向读现有代码 / 资源 |
| 3 | plan-mod | 输出 Mod 设计与改动清单 |
| 4 | gen-sprites | 用 fal 生成精灵图 |
| 5 | gen-textures | 生成贴图 |
| 6 | gen-3d | 生成 3D 模型（Blender 渲精灵帧） |
| 7 | gen-sfx | 生成音效 |
| 8 | integrate | 把产物打进游戏 |
| 9 | verify-in-game | 启动游戏验证 |
| 10 | package-release | 打包可发布 Mod |

## 引擎手册覆盖

| 引擎 | 引擎手册 |
|------|---------|
| Unity | ✅ |
| Unreal | ✅ |
| Godot | ✅ |
| Source | ✅ |
| Bethesda | ✅ |
| RE Engine | ✅ |
| 其他（RPG Maker / GameMaker / Ren'Py 等） | 部分覆盖 |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105866864543121674>
- 项目链接：<https://github.com/rehan-remade/universal-modder>

## 相关概念

- [Agent Skills](./term-agent-skills.md) — 大伞概念，Universal Modder 是「游戏 Mod」领域的具体实现
- [mattpocock/skills](./tool-mattpocock-skills.md) — 另一份高质量 Skill 集合
- [Codex 3D Scene Workflow](./note-codex-3d-scene-workflow.md) — 跨域 3D 工作流
