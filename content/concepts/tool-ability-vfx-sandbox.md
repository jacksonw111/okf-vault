---
type: "Tool"
title: "ability-vfx-sandbox（Three.js + GLSL 技能 VFX 沙盒）"
description: "Three.js 技能招式 VFX 沙盒：手写 GLSL 实现 10 种线性与区域瞄准的技能特效，所有参数实时可调；晶体 / 蛇尾 / 藤蔓 / 花瓣走顶点着色器，毒雾走光线步进体积云。"
resource: "https://github.com/achrefelouafi/LinearAbiltyCastingExtendedThreeJS"
tags: "[three.js, glsl, vfx, game-dev, shader]"
timestamp: "2026-09-11T22:00:00Z"
---

# ability-vfx-sandbox

## 它是什么

[achrefelouafi/LinearAbiltyCastingExtendedThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingExtendedThreeJS) 是一个 **Three.js + 手写 GLSL** 的技能特效（VFX）沙盒：**10 种技能特效**实现线性瞄准（按住出箭头跟鼠标走）与区域瞄准（出粗边圆圈告诉你炸多大）两类，全部参数可实时调节。画面里看到的「晶体 / 石头 / 蛇尾 / 藤蔓 / 花瓣」走顶点着色器，「毒雾」走光线步进的体积云。

## 为什么用它 / 适合什么场景

- 做 MOBA / RPG / 动作类 Web 游戏，需要参考「技能特效该怎么实现」。
- 学习 WebGL / GLSL 着色器编程的实战案例（顶点 + 体积云两条路径）。
- 想做技术美术（TA）作品集 / 给团队做内部 VFX 库。

## 关键能力

| 能力 | 说明 |
|------|------|
| 10 个技能特效 | 3 个线性瞄准 + 7 个区域瞄准，覆盖常见 MOBA 技能 |
| 顶点着色器 | 晶体 / 石头 / 蛇尾 / 藤蔓 / 花瓣类硬表面 / 缠绕特效 |
| 体积云 | 毒雾类通过光线步进（ray marching）实现 |
| 参数实时调 | 鼠标拖滑块看效果，所见即所得 |
| Three.js | 与场景系统无缝组合 |

## 参考链接

- 项目仓库：<https://github.com/achrefelouafi/LinearAbiltyCastingExtendedThreeJS>

## 媒体

- ![](https://pbs.twimg.com/media/HRvkl5UagAAl6Ch.jpg)

## 相关概念

- [three.js](./term-three-js.md) — 浏览器 3D / WebGL 底层引擎
- [clay-safari](./tool-clay-safari.md) — 同为 Three.js 的儿童 3D 互动项目
- [Gorest](./tool-gorest.md) — 2D 精灵表与场景合成
</content>
</invoke>