---
type: Tool
title: "ghostty-warp-shader（Ghostty 星轨加速 GLSL shader）"
description: "Ghostty 终端自带的着色器接口一直没人做好看的动态星空背景。ghostty-warp-shader 写好 GLSL 文件直接丢进终端，就能跑出星轨加速效果。"
resource: "https://github.com/daviddodda1/ghostty-warp-shader"
tags: [ghostty, shader, glsl, terminal, cosmetic]
timestamp: "2026-07-30T00:45:00.000Z"
---

# ghostty-warp-shader

## 它是什么

**Ghostty 终端的动态星空背景着色器**——Ghostty 1.x 起开放了自定义着色器接口（custom shaders），允许用户以 GLSL 注入背景特效。

ghostty-warp-shader 是这套接口的第一个实用 demo：

- 单个 GLSL 文件
- 模拟「超空间跳跃」的星轨加速效果（warp / hyperspace）
- 丢进 Ghostty 配置目录即可生效，无需编译

![效果视频](https://video.twimg.com/tweet_video/HOXSC_xbYAAdTLK.mp4)

## 关键能力

| 能力 | 说明 |
|------|------|
| 单文件 GLSL | 复制即可用，无需构建 |
| 实时 GPU 渲染 | 走 Ghostty 着色器管线 |
| 占用低 | 终端背景层渲染，不影响主线程 |
| 可扩展模板 | 改 GLSL 即可换风格 |
| 开源 | 可 fork 二次创作 |

## 适合谁

- 想要「电影感」终端背景的玩家
- 想写自定义 GLSL 着色器的开发者（拿这个当模板）
- 经常录屏 / 直播终端界面的内容创作者

## 原始链接

- [项目仓库](https://github.com/daviddodda1/ghostty-warp-shader)
- [推文剪藏](https://x.com/QingQ77/status/2082628490747080732)

## 相关概念

- [lex-ghostty-shaders](./tool-lex-ghostty-shaders.md) — GLM-5.2 vibe-coded Ghostty 水波纹 shader
- [Vesta（macOS 终端）](./tool-vesta-terminal.md) — macOS 原生终端，Swift/AppKit + GhosttyKit Metal 渲染