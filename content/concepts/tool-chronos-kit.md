---
type: Tool
title: "chronos（chronos-kit/chronos，宿主内嵌 2D/3D 渲染包）"
description: "App 内集成高性能 2D/3D 渲染和小游戏的宿主方案，宿主与 .cron 包走消息通道做 RPC，支持预加载、包元数据、外部资源路径与沙盒目录。已在 B 站移动端弹幕与跨年晚会互动音游中落地。"
resource: "https://github.com/chronos-kit/chronos"
tags: [mobile, rendering, 2d, 3d, game-engine, embedded, sdk]
timestamp: "2026-07-24T00:00:00Z"
---

# chronos

[chronos](https://github.com/chronos-kit/chronos) 是一个**在宿主 App 里集成高性能 2D/3D 渲染和小游戏**的宿主方案——目标是把一个完整的渲染/小游戏运行时塞进任意 App，而不必从零造引擎，也不必被现成的方案绑死。

## 它解决的问题

想在 App 里跑高性能 2D/3D 内容或小游戏，常见的坑：
- **从零写引擎**：成本太高，路线还容易跑偏。
- **用现成的渲染/小游戏框架**：要么改不了，要么集成后包体爆炸，要么交互卡。

chronos 的思路是做一个**轻量宿主 + .cron 包**的体系：
- **宿主**：负责加载、调度、安全边界。
- **.cron 包**：实际的渲染 / 互动内容，以包形式下发。

## 关键能力

| 能力 | 说明 |
|------|------|
| 高性能 2D/3D 渲染 | 走宿主渲染管线，不必从零搭引擎 |
| .cron 包格式 | 把内容打包成独立单元，便于版本化与下发 |
| 消息通道 RPC | 宿主与 .cron 包之间走消息通道通信，包可调用宿主能力 |
| 预加载 | 包元数据提前读，启动时按需加载 |
| 外部资源路径 | 包可声明外部资源（如远程素材、纹理） |
| 沙盒目录 | 包有独立文件系统沙盒，不污染宿主 |
| 跨年晚会实战 | B 站跨年晚会的互动音游就用了它 |

## 适用场景

- 移动端 / 桌面 App 想加小游戏或互动特效
- 想把 2D/3D 内容做成可独立更新、可下发的「包」
- 需要在 B 站级别用户体量下保证互动内容稳定运行

## 参考链接

- 项目仓库: <https://github.com/chronos-kit/chronos>

## 媒体

视频演示：<https://video.twimg.com/amplify_video/2080472732102512640/vid/avc1/1920x864/fIxWGYjqP8m0aM3_.mp4?tag=29>

## 相关概念

- [Gorest](tool-gorest.md) — Codex 驱动的 2D 动画精灵表生成器与场景合成工作台，同样面向 2D 内容产出