---
type: "Tool"
title: "Mesurer（Ibelick 出品的浏览器测距 / 录屏工具）"
description: "Ibelick 出品的浏览器测距工具集：可量元素间距 / 尺寸 / 对齐，新增 screen recording 录下整段交互，配 npm 包或 Chrome 扩展使用，适合写 PR 描述 / Slack 反馈时把视觉问题「拍下来」说清楚。"
resource: "https://github.com/Ibelick/mesurer"
tags: "[browser, design-tool, measurement, screen-recording, ux, feedback, chrome-extension]"
timestamp: "2026-10-01T23:10:00Z"
---

# Mesurer（Ibelick 出品的浏览器测距 / 录屏工具）

## 它是什么

[Mesurer](https://github.com/Ibelick/mesurer) 是 Ibelick 出品的**浏览器测距工具集**，最初用来量元素间距 / 尺寸 / 对齐，**新版本加入了 screen recording**——把整段交互（点击、滚动、hover）录成视频，方便在 PR 描述 / Slack 反馈 / Bug report 里把视觉问题「拍下来」说清楚。

## 为什么用它 / 适合什么场景

- **设计师 / 前端 review** ——「这个按钮和右边差 8px」、「这个 hover 效果中间有一帧跳动」——录下来比截图更清楚。
- **Bug 报告** ——录一段 30 秒的交互，比写三段描述更高效，对方看一眼就懂。
- **远程协作** ——把录屏直接发到 Slack / 飞书 / 邮件，团队不用再约会议。

## 关键能力

| 能力 | 说明 |
|------|------|
| 元素测距 | 点两点 / 两个元素，自动算距离、对齐、尺寸 |
| 屏幕录制 | 录下整段交互（含滚动、动画），生成 mp4 / webm |
| 测距 + 录屏二合一 | 录屏里直接叠加测距标注，无需后期 |
| 两种形态 | npm 包（嵌入自己的应用）+ Chrome 扩展（开箱即用） |
| 轻量 | 不依赖后端，全本地运行 |

## 安装

```bash
# 1) 作为依赖装到项目里
npm i mesurer

# 2) 或者装 Chrome 扩展，直接在任意网页用
# Chrome Web Store 搜 "mesurer"
```

## 参考链接

- 原始链接：<https://x.com/Ibelick/status/2105663400072159284>
- 项目链接：<https://github.com/Ibelick/mesurer>
- 视频：<https://video.twimg.com/amplify_video/2105662233686511617/vid/avc1/1916x1080/UcVn7VM1TX4IHnEi.mp4?tag=29>

## 相关概念

- [Sitecheck](./tool-sitecheck.md) — 另一类浏览器扩展（嗅探技术栈）
- [Kinetics](./tool-kinetics.md) — 动效库，可与 Mesurer 的录屏能力搭配做动效 review
