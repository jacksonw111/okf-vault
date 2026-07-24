---
type: Tool
title: "expo-glass-tabs（Expo Router 毛玻璃底部标签栏组件）"
description: "Expo Router 没有原生的毛玻璃底部标签栏,这个组件用 Revolut 那种「滚动缩小但不隐藏图标」的方案补上了。"
resource: "https://github.com/davidmokos/expo-glass-tabs"
tags: [expo, react-native, tab-bar, glass, ui-component]
timestamp: "2026-07-24T00:00:00Z"
---

# expo-glass-tabs

[expo-glass-tabs](https://github.com/davidmokos/expo-glass-tabs) 是给 **Expo Router** 项目补上的**毛玻璃底部标签栏组件**——Expo Router 官方并没有原生支持这种样式，本组件参考 Revolut 的交互方案：**滚动时缩小但不隐藏**图标。

## 它解决的问题

Expo Router 的底部 Tabs 想要：
- 毛玻璃背景（frosted glass）
- 滚动内容时图标**缩小变淡但不消失**

这两件事官方组件都没给现成方案。开发者通常要自己包两层 + 监听滚动位置 + 手动算缩放曲线，做出来还不一定顺滑。

expo-glass-tabs 把这个交互直接打成可复用组件：

## 关键能力

| 能力 | 说明 |
|------|------|
| 毛玻璃背景 | 走 expo-blur，玻璃效果 |
| 滚动缩小 | 滚动时图标缩小但不消失 |
| Revolut 风格交互 | 借鉴主流移动端交互范式 |
| Expo Router 原生 | 直接作为 `Tabs` 替代组件使用 |

## 适用场景

- 用 Expo Router 做移动端 App，想要「高级感」底部栏
- 需要兼顾内容阅读和导航可达性
- 想直接复用 Revolut / Apple Music 风格的标签栏

## 参考链接

- 项目仓库: <https://github.com/davidmokos/expo-glass-tabs>

## 媒体

视频演示：<https://video.twimg.com/tweet_video/HN9PzVsaMAEEmpK.mp4>

## 相关概念

- [liquid-glass](tool-liquid-glass.md) — React 零依赖液态玻璃折射组件，本工具是其在 React Native / Expo 的对应物