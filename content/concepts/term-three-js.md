---
type: "Term"
title: "three.js"
description: "Three.js 是 Mr.doob 主导的 JavaScript 3D 库：WebGL 之上的高层封装，把场景 / 相机 / 灯光 / 网格 / 材质 / 着色器封装成易用的面向对象 API，是浏览器端 3D / WebGL 应用的事实标准。"
resource: "https://threejs.org/"
tags: [threejs, webgl, 3d, javascript, graphics]
timestamp: "2026-08-09T19:30:00Z"
---

# three.js

## 定义

three.js 是浏览器端最主流的 JavaScript 3D 库。它在 WebGL 之上做了高层封装：场景图（Scene / Object3D）、相机（PerspectiveCamera / OrthographicCamera）、灯光、几何体、材质、纹理、加载器（glTF / FBX / OBJ）、着色器等，让「不直接写 GLSL」也能做出高质量 3D 内容。

## 要点

- **WebGL 抽象层**：不必写 GLSL 即可使用大部分功能；需要自定义效果时也能插入 ShaderMaterial。
- **场景图**：树状结构管理场景对象，遍历 / 变换 / 矩阵自动维护。
- **生态**：glTF 加载器（KHR_draco 压缩 / KHR_materials_variants / KHR_animation）、后处理（EffectComposer）、物理（Cannon-es / Rapier 集成）、AR/VR（WebXR）。
- **应用范围**：从产品营销页到数据可视化、Web 游戏、虚拟展厅、数字孪生，无处不在。
- **学习曲线**：API 友好，但性能调优（避免每帧分配、合并几何、合理 LOD）需要经验。

## 为什么需要知道

- 几乎所有「网页上看到 3D」的项目都跑在 three.js 或其衍生框架（R3F / Threlte）之上。
- 性能预算（首屏 KB 数 / 帧率 / 显存）是评估 three.js 项目的核心指标。
- 与 [Solar Wanderer](./tool-solar-wanderer.md)、[Kage (MengTo)](./tool-kage-mengto.md) 等实战项目对照看，是掌握「浏览器端 3D 套路」最快的方式。

## 相关概念

- [Solar Wanderer](./tool-solar-wanderer.md) — Three.js + WebGL2 的浏览器内太阳系模拟器
- [Kage (MengTo)](./tool-kage-mengto.md) — 滚动驱动 three.js 场景的 landing page