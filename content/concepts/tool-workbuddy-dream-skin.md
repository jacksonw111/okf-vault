---
type: "Tool"
title: "WorkBuddy-Dream-Skin（zhouwei713/WorkBuddy-Dream-Skin）"
description: "通过本机回环 CDP 连上 WorkBuddy 桌面端的 Electron 渲染进程,往里注入可随时还原的 CSS 与主题变量,不碰 WorkBuddy.exe / app.asar / 安装目录,即可给整个界面套上随图片气质变化的明暗主题与动态挂件。"
resource: "https://github.com/zhouwei713/WorkBuddy-Dream-Skin"
tags: "[workbuddy, electron, cdp, theming, skin, customization]"
timestamp: "2026-08-11T16:00:00Z"
---

# WorkBuddy-Dream-Skin

[WorkBuddy-Dream-Skin](https://github.com/zhouwei713/WorkBuddy-Dream-Skin) 是给 WorkBuddy 桌面端用的**无损换肤方案**——WorkBuddy 本身不允许换皮肤、界面只能用官方样式,本项目通过本机回环 CDP 连上它的 Electron 渲染进程,往里注入可随时还原的 CSS 与主题变量,从而给整个界面套上随图片气质变化的明暗主题与动态挂件。

项目链接：<https://github.com/zhouwei713/WorkBuddy-Dream-Skin>

## 它是什么

利用 Electron 自带的**Chrome DevTools Protocol**远程调试能力,在不修改目标程序的前提下,通过本机回环连接把 CSS / 主题变量动态注入到 WorkBuddy 的渲染进程。

## 为什么用它 / 适合什么场景

- **不破不修**:不碰 WorkBuddy.exe / app.asar / 安装目录,后续官方升级不会因为替换文件炸掉。
- **可随时还原**:注入的 CSS 与变量集中管理,出问题一键回退官方外观。
- **图片气质联动**:能根据当前壁纸 / 选图配色动态切明暗主题与动态挂件。

## 关键能力

| 能力 | 说明 |
|------|------|
| CDP 本机回环 | 不开外部端口,通过 localhost 直连 Electron 渲染进程 |
| CSS / 变量注入 | 全部以主题变量形式注入,不修改源文件 |
| 不碰安装目录 | 不动 WorkBuddy.exe / app.asar,升级安全 |
| 一键还原 | 出问题可恢复官方原貌 |
| 图片气质联动 | 按当前壁纸 / 主图配色自动套主题 |
| 动态挂件 | 可叠加动画与装饰组件,不破坏布局 |

## 媒体

![](https://pbs.twimg.com/media/HPU0fftbUAAZWah.jpg)
![](https://pbs.twimg.com/media/HPU0gxQaoAEtH5U.jpg)
![](https://pbs.twimg.com/media/HPU0iO0a8AAhVG2.jpg)
![](https://pbs.twimg.com/media/HPU0km-aMAAx8Nf.jpg)

## 参考链接

- [项目仓库](https://github.com/zhouwei713/WorkBuddy-Dream-Skin)

## 相关概念

- [WorkBuddyGuide](./tool-workbuddy-guide.md) — WorkBuddy 官方蓝皮书教程,本项目是其上层的视觉个性化方案