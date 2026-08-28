---
type: Tool
title: "uni-baidu-map-harmony（百度地图 HarmonyOS NEXT 原生 SDK 的 uni-app 插件）"
description: "carlChina88/uni-baidu-map-harmony：通过 UTS + defineNativeEmbed 注册 <embed tag=\"baidu-map\" />，把百度 HarmonyOS NEXT 原生地图 SDK 以插件形式补进 uni-app + APP-HARMONY 路径。"
resource: "https://github.com/carlChina88/uni-baidu-map-harmony"
tags: [uni-app, harmonyos, baidu-map, uts, native-embed, plugin]
timestamp: "2026-08-27T13:45:00Z"
---

# uni-baidu-map-harmony

## 它是什么
[carlChina88/uni-baidu-map-harmony](https://github.com/carlChina88/uni-baidu-map-harmony) 解决一个具体的缺口：

- **uni-app 官方文档**给 HarmonyOS 内置 `map` 组件列出的地图商只有**腾讯**；
- 传统 **uni-app + APP-HARMONY** 路径**没有百度地图选项**。

这个仓库通过 **UTS + `defineNativeEmbed`**，注册 `<embed tag="baidu-map" />`，把**百度 HarmonyOS NEXT 原生地图 SDK**以插件形式补进这条路径。

## 为什么用它 / 适合什么场景
- 用 uni-app 跨端开发、目标包含 HarmonyOS NEXT 应用；
- 想用百度地图（自有账号体系 / 行业方案 / 国内合规）而不是腾讯地图；
- 不想 fork uni-app 主干去改 map 组件。

## 关键能力
| 能力 | 说明 |
|------|------|
| 形态 | uni-app 插件 |
| 实现 | UTS + defineNativeEmbed |
| 原生 SDK | 百度地图 HarmonyOS NEXT 原生 SDK |
| 嵌入标签 | `<embed tag="baidu-map" />` |
| 补缺 | 填补 uni-app × HarmonyOS 的百度地图空白 |
| 开源 | 仓库开源 |

## 相关概念
- [Toolcraft](tool-toolcraft.md) — pixel-point 出的创意类应用 starter kit；uni-baidu-map-harmony 是「跨端框架 × 平台原生能力」桥接的另一个样本

## 参考链接
- 项目链接：<https://github.com/carlChina88/uni-baidu-map-harmony>
