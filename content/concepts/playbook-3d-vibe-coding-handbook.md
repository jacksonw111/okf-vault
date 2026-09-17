---
type: "Playbook"
title: "3D Vibe Coding 手册"
description: "alchaincyf 写给非程序员的 3D 资产生产手册：用 AI 生成 3D 模型 → 处理（拓扑 / UV / 贴图）→ 接入可运行场景。"
resource: "https://github.com/alchaincyf/3d-vibe-coding-handbook"
tags: "[3d, vibe-coding, ai-generation, glb, gltf, topology, uv-mapping, scene-integration, handbook]"
timestamp: "2026-09-17T07:55:00Z"
---

# 3D Vibe Coding 手册

## 它是什么

[alchaincyf/3d-vibe-coding-handbook](https://github.com/alchaincyf/3d-vibe-coding-handbook) 是 **alchaincyf** 写的**面向非程序员的 3D 资产生产手册**。它把「缺编程经验但想做 3D」的人带过三道关：

1. **AI 生成 3D 资产**
2. **处理模型**（拓扑 / UV / 贴图 / 减面 / 重新中心化等常见坑）
3. **接入可运行场景**（Three.js / Babylon / R3F / 游戏引擎）

## 适合谁

- 想做 3D 内容但不会写代码的创作者 / 设计师。
- 用 AI 生成 3D 模型遇到「拿到 glb 不知道怎么放进场景」问题的初学者。
- 想给团队沉淀一份「3D 资产从生到用」标准化流程的团队负责人。

## 标准流程

| 阶段 | 关键动作 | 常见坑 |
|------|----------|--------|
| 1. AI 出图 | 用 Meshy / Tripo / Rodin / Hunyuan3D 等工具出模型 | 比例 / 朝向 / 坐标中心不统一 |
| 2. 模型处理 | Blender 拓扑清理、UV 拆分、贴图减面、PBR 材质烘焙 | 拓扑烂 → 骨骼绑不动；UV 叠 → 上色脏 |
| 3. 场景接入 | glb 导入 Three.js / R3F / Babylon / Unity / UE | 坐标系 / 光照 / 阴影不匹配 |
| 4. 上线 | 静态站 / WebGL / WebGPU / 移动端 WebView | 性能 / LOD / 资产体积优化 |

## 与相关概念的关系

- [Three.js] — 手册推荐的 Web 端 3D 渲染栈之一。
- [Vibe Coding] — 该手册是 Vibe Coding 在 3D 资产领域的实践模板。

## 参考

- 项目链接：<https://github.com/alchaincyf/3d-vibe-coding-handbook>

![preview](https://pbs.twimg.com/media/HSYvW1laYAEq2Zr.jpg)
