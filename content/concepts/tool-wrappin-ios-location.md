---
type: "Tool"
title: "WrapPin（iOS 27+ 位置模拟）"
description: "Roam Control 的非官方社区中文分支，给 iOS 27+ iPhone 提供本机虚拟定位，在地图上选点或规划步行路线、让系统向 App 报告模拟坐标；走 iOS 开发者位置模拟通道、不改公网 IP、不装 MITM 证书。"
resource: "https://github.com/suversal/WrapPin"
tags: "[ios, location, mock, swift, devtool, vpn-local]"
timestamp: "2026-09-16T16:04:00Z"
---

# WrapPin（iOS 27+ 位置模拟）

## 它是什么

[suversal/WrapPin](https://github.com/suversal/WrapPin) 是 Roam Control 的**非官方社区中文分支**，针对 **iOS 27+ 实体机** 提供本机虚拟定位能力。地图上选点或画一条步行路线，就能让系统向 App 报告模拟坐标，面向 LBS / 出行 / 外卖类 App 的开发与回归测试。

技术路径走的是 iOS 官方的开发者位置模拟通道：本机生成 `RPPairing` 配对记录存进钥匙串，经 `LocalDevVPN` 发现本机配对服务并建立加密隧道，再调用 `LocationSimulation` 设置坐标；**不动公网 IP、不装 MITM 根证书**。

## 为什么用它 / 适合什么场景

- 想在 iOS 27+ 设备上跑位置模拟、又不想装额外证书或改动网络。
- 测试 LBS / 出行 / 外卖 / 健身路线类 App 的位置相关逻辑。
- 中英文混排文档友好的中文项目。

## 关键能力

| 能力 | 说明 |
|------|------|
| iOS 27+ 实体机支持 | 适配最新 iOS API，实体机而非模拟器 |
| 官方位置模拟通道 | 用 `RPPairing` + `LocalDevVPN` + `LocationSimulation` 走官方路径 |
| 钥匙串存储 | 配对记录落钥匙串，免配置明文文件 |
| 选点 / 路线模拟 | 既能瞬移到指定坐标，也能按步行路线逐步移动 |
| Swift / SwiftUI | 项目本体是 SwiftUI，便于二次定制 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTYj9iagAARxZW.jpg)

## 相关概念

- [Roam-Control](./tool-roam-control.md) — WrapPin 是它的非官方社区中文分支，定位能力一致、面向的 iOS 版本更新