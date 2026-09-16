---
type: "Tool"
title: "bg0"
description: "开源浏览器本地背景移除工具，WebGPU 可用时推理、不行则回退 WASM，最终输出透明 PNG；原图全程不上传，没有账号 / 计费 / 用量限制。"
resource: "https://github.com/opencoredev/bg0"
tags: "[browser, image-processing, background-removal, webgpu, wasm, privacy]"
timestamp: "2026-09-16T16:07:00Z"
---

# bg0

## 它是什么

[opencoredev/bg0](https://github.com/opencoredev/bg0) 是一个**完全跑在浏览器里的开源背景移除工具**：本机有 WebGPU 就走 WebGPU 推理、不可用就回退 WASM，输出透明 PNG。**原图全程不上传**，没有账号、没有计费、没有用量限制。

## 为什么用它 / 适合什么场景

- 需要去背景但又不想把图片传第三方服务（隐私 / 合规场景）。
- 想给 LLM / 文档流里的图片快速抠图，无需装桌面软件。
- 离线场景下也能继续工作（WebGPU / WASM 都在本机）。

## 关键能力

| 能力 | 说明 |
|------|------|
| WebGPU 推理 | 优先利用 GPU 加速 |
| WASM 回退 | 旧浏览器 / 无 GPU 也能用 |
| 透明 PNG 输出 | 标准抠图格式 |
| 零上传 | 原图留在本地，隐私友好 |
| 无账号 / 计费 / 用量限制 | 开箱即用 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTZ8tHakAAeyr_.png)

## 相关概念

- [PaperOtter](./tool-paperotter.md) — 19 个本机离线 PDF / 图片工具，bg0 是其「去背景」场景的浏览器版