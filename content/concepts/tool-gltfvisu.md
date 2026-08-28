---
type: Tool
title: "GLTFVisu（glTF 着色器在线实验台）"
description: "把 glTF 模型 + 自定义着色器的调试装进同一个网页：左选模型 / 着色器，右改 GLSL，中间即时看效果，改好的预设可保存。"
resource: "https://github.com/MaxMFonseca/GLTFVisu"
tags: [gltf, shader, glsl, webgl, three-js, design-tool]
timestamp: "2026-08-27T08:29:00Z"
---

# GLTFVisu

## 它是什么
[MaxMFonseca/GLTFVisu](https://github.com/MaxMFonseca/GLTFVisu) 是一个**在线 glTF 着色器实验台**。调 glTF 模型的自定义着色器通常要在代码和预览窗口之间反复切——这个工具把它们装进同一个网页：

- **左边**：选模型和着色器；
- **右边**：改 GLSL 代码；
- **中间**：即时看效果；
- **保存预设**：调好的着色器可存为预设。

## 为什么用它 / 适合什么场景
- 在做 glTF / WebGL 项目，需要快速迭代自定义着色器；
- 想给团队 / 学生演示"模型 + 着色器"实时互动效果；
- 不想起本地 three.js 工程就能试一套 GLSL。

## 关键能力
| 能力 | 说明 |
|------|------|
| 单页三栏 | 模型 / 代码 / 预览同屏 |
| 即时预览 | GLSL 改了立刻看效果 |
| 预设保存 | 调好的着色器存为预设复用 |
| glTF 模型选择 | 多模型可挑 |
| 着色器选择 | 多个内置着色器可选 |
| 在线工具 | 浏览器即可用 |

## 相关概念
- [three.js](term-three-js.md) — 主流 WebGL 库；GLTFVisu 是 three.js 生态下的「glTF + GLSL 实验台」专化工具
- [Threeui](tool-threeui.md) — three.js 的高质量 UI 组件库；与 GLTFVisu 都是 three.js 生态的延展

## 参考链接
- 项目链接：<https://github.com/MaxMFonseca/GLTFVisu>
