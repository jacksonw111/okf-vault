---
type: "Tool"
title: "xweiba/location-spoofer (iOS 定位调试代理)"
description: "iOS 定位测试工具：本地代理 / 第三方代理客户端拦截 Apple 定位服务（CLLocation）的响应，开发者和 QA 不用改目标 App 代码就能在不同坐标 / 移动轨迹下验证应用表现。"
resource: "https://github.com/xweiba/location-spoofer"
tags: [ios, location, testing, debugging, proxy, qa]
timestamp: "2026-08-10T01:38:00Z"
---

# xweiba/location-spoofer (iOS 定位调试代理)

## 它是什么

[xweiba/location-spoofer](https://github.com/xweiba/location-spoofer) 是一个面向**iOS 开发与 QA** 的定位调试工具：它把 **Apple 定位服务（CLLocation / CoreLocation）的响应**当成可代理的协议来拦截与回放，通过本地代理或第三方代理客户端给出「虚拟的 GPS 坐标 / 移动轨迹」，从而让被测 App 在不修改源码、不注入 hook、不装越狱插件的情况下，跑出「定位到任意坐标 / 按指定路径移动」的效果。

## 为什么用它 / 适合什么场景

- 测 LBS / 打车 / 外卖 / 地图 / 签到 / 地理围栏类 App：**不想改目标 App 源码**就能验证不同坐标和移动场景下的表现。
- QA 回归：把一组地理位置测试用例固化到代理的脚本里，自动回放。
- 演示 / 视频录制：录视频时希望「此刻我在某地」，但实际地理位置不是。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零侵入 | 不改目标 App 代码、不重签 IPA，靠代理拦截定位响应 |
| 本地 / 第三方代理 | 可纯本地，也可外挂第三方代理客户端 |
| 多场景模拟 | 单点定位、按路径移动、地理围栏进出 |
| QA 友好 | 测试用例可脚本化、可回放 |

## 媒体

![](https://pbs.twimg.com/media/HPPnzcBb0AAG3Gb.jpg)

## 参考链接

- [项目仓库](https://github.com/xweiba/location-spoofer)
- [原始链接](https://x.com/QingQ77/status/2086628095348633929)
