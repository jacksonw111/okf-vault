---
type: Tool
title: "CodexPetdexSkins（Codex 桌面端一站式换装工具）"
description: "Electron 写的 Windows 工具，给 Codex 桌面版管理主题、皮肤、壁纸、宠物和搭配。导入预览一键应用，通过本机 CDP 注入装饰层，不碰 ASAR/MSIX 原始文件。"
resource: "https://github.com/IceSaury/CodexPetdexSkins"
tags: [codex, theme, skin, wallpaper, customization, cdp, electron]
timestamp: "2026-07-24T00:00:00Z"
---

# CodexPetdexSkins

[CodexPetdexSkins](https://github.com/IceSaury/CodexPetdexSkins) 是给 ChatGPT Codex 桌面端的**一站式外观定制工具**——把主题、皮肤、壁纸、宠物搭配这些原本需要手动操作的环节，全部包到同一款 Electron Windows 工具里。

## 它解决的问题

Codex 桌面端是封闭的 Electron 应用，原生主题单调。
- 想换主题 → 翻 ASAR 改文件，易被升级覆盖
- 想换壁纸 → 没有内置入口
- 想加宠物 → 单独装一个 Petdex
- 多个东西搭配保存 → 完全没有

本工具用**本机 CDP（Chrome DevTools Protocol）注入装饰层**的方式做这一切，**完全不碰 Codex 安装文件**——升级也不会被覆盖。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一站式 | 主题 / 皮肤 / 壁纸 / 宠物 / 搭配 全部一个工具管 |
| 零侵入 | 通过本机 CDP 注入装饰层，不改 ASAR / MSIX |
| 导入预览 | 主题 / 皮肤能导入预览再一键应用 |
| 壁纸 / 皮肤互斥 | 自动避免冲突 |
| 宠物从 Petdex 装 | 复用 Petdex 的宠物源，不必另起生态 |
| 托盘常驻 | 后台常驻方便快速切换 |
| 启动预连接 | 启动 Codex 时自动预连 CDP |
| 一键搭配保存 | 整套主题 / 皮肤 / 壁纸 / 宠物一键打包保存 |

## 与同类工具的关系

| 工具 | 范围 | 方式 |
|------|------|------|
| Codex Dream Skin | 仅壁纸 | CDP 注入 16:9 壁纸 |
| **CodexPetdexSkins** | 主题 / 皮肤 / 壁纸 / 宠物 | CDP 注入全套装饰层 |
| Codex-X | 提示词注入 / Provider 切换 / 配置可视化 | Tauri 2 跨平台 |

## 适用场景

- 已经用 Codex 桌面端，想让它更像「自己写的编辑器」
- 怕改 ASAR 被升级覆盖，又想持续折腾外观
- 想把整套主题打包分享给同事

## 参考链接

- 项目仓库: <https://github.com/IceSaury/CodexPetdexSkins>

## 媒体

![](https://pbs.twimg.com/media/HN9QGrob0AAq27k.jpg)

## 相关概念

- [Codex Dream Skin](tool-codex-dream-skin.md) — 仅做壁纸的轻量 CDP 注入方案，本工具是其「全套装饰层」扩展
- [Codex-X](tool-codex-x.md) — Tauri 2 跨平台 Codex 桌面端管理器，覆盖 Provider 切换 / 提示词注入等更广场景
- [joi-codex-pet](tool-joi-codex-pet.md) — Codex 桌面端宠物装饰，本工具与之互补（搭配保存）