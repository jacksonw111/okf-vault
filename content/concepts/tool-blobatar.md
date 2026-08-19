---
type: Tool
title: "Blobatar（Alain00/blobatar）"
description: "输入用户名 / 邮箱 / 用户 ID 即生成固定对应、会动的几何 SVG 小生物，约 3.7 KB 核心无依赖，支持 React / 普通 JS / 13 种表情"
resource: "https://github.com/Alain00/blobatar"
tags: "[avatar, svg, identity, generator, lightweight]"
timestamp: "2026-08-19T16:00:00Z"
---

# Blobatar（Alain00/blobatar）

## 它是什么
[`Alain00/blobatar`](https://github.com/Alain00/blobatar) 是一个用「确定性映射」生成几何风格 SVG 小生物（blob）的轻量库：输入用户名、邮箱或用户 ID，就能得到一只与输入唯一对应、能动起来的几何小生物，可作为头像 / 默认 userpic / 视觉徽章。

## 为什么用它 / 适合什么场景
- 不想给每个新用户存头像，又需要「千人千面」的视觉差异化（同一输入永远得到同一只 blob）。
- 想要纯 SVG 输出（缩放不失真、方便贴 React / 普通 JS / Tailwind / Figma）。
- 体积敏感：核心 3.7 KB、无依赖、可嵌入前端 bundle。

## 关键能力
| 能力 | 说明 |
|------|------|
| 输入确定 | 用户名 / 邮箱 / ID 经哈希后映射到 blob 形态，相同输入永远生成同一只 |
| 纯 SVG | 输出为矢量，缩放不失真、可被任意前端框架消费 |
| 体积小 | 核心约 3.7 KB、零运行时依赖 |
| 多形态接入 | 同时支持 React 组件与普通 JS 调用 |
| 13 种表情 | 默认带 13 种表情 / 状态切换 |

## 媒体
- 视频：<https://video.twimg.com/amplify_video/2089621393612869632/vid/avc1/720x1280/7MnzKV14PvckpVII.mp4?tag=14>

## 相关概念
- [项目仓库](https://github.com/Alain00/blobatar) — 仓库主页
- [bloub](./tool-bloub-mascot.md) — 同样输出 SVG 动效头像 / 吉祥物的工具