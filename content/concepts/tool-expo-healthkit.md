---
type: "Tool"
title: "expo-healthkit（RN/Expo 健康双端统一桥）"
description: "把 Apple Health（iOS）和 Health Connect（Android）封装成同一套 TypeScript 接口，React Native / Expo 应用只需写一次就能在两端读取健康数据。"
resource: "https://github.com/appeeky/expo-healthkit"
tags: "[react-native, expo, healthkit, health-connect, typescript]"
timestamp: "2026-09-11T22:00:00Z"
---

# expo-healthkit

## 它是什么

[appeeky/expo-healthkit](https://github.com/appeeky/expo-healthkit) 是一个 **React Native / Expo** 库，把 iOS 的 Apple HealthKit 与 Android 的 Health Connect **封装成同一套 TypeScript API**，开发者写一次调用就能在两端读取步数、心率、睡眠、锻炼等健康数据，不用再各写一套原生桥接。

## 为什么用它 / 适合什么场景

- 想做跨端健康 / 健身 / 冥想 App，不想为 iOS / Android 各写一套原生模块。
- 已有 Expo 项目，需要快速接入健康数据但不想 eject 到原生工程。
- 想统一抽象双端健康数据模型（权限、查询、单位、聚合）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 双端统一 API | iOS HealthKit + Android Health Connect 同名方法 |
| TypeScript 友好 | 完整类型定义，IDE 自动补全 |
| Expo 兼容 | Expo Go / dev client 都能跑 |
| 权限封装 | 双端健康数据权限申请一次搞定 |
| 查询抽象 | 时间范围 / 聚合 / 实时订阅统一接口 |

## 参考链接

- 项目仓库：<https://github.com/appeeky/expo-healthkit>

## 媒体

- ![](https://pbs.twimg.com/media/HRvfeEbbcAAidlB.jpg)

## 相关概念

- [mobilecode](./tool-mobilecode.md) — 移动端 AI 编码会话内嵌 iOS 模拟器 + Android emulator
- [mobile-harness](./tool-mobile-harness.md) — 安卓端原生 AI 编码套件
- [PanelUI](./tool-panelui.md) — React Native / Expo 上的 128 组件 UI 库
</content>
</invoke>