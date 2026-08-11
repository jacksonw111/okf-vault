---
type: "Tool"
title: "BlackBar（zatuomfawas/BlackBar）"
description: "Chrome 截图扩展,按 Alt+Shift+S 触发截图前会先扫描整页 DOM,把凭证 / 卡号 / 邮箱 / 地址等敏感内容遮成黑条,避免截图分享时无意泄露隐私数据。"
resource: "https://github.com/zatuomfawas/BlackBar"
tags: "[chrome-extension, screenshot, privacy, dom-scan, redaction, security]"
timestamp: "2026-08-11T16:00:00Z"
---

# BlackBar

[BlackBar](https://github.com/zatuomfawas/BlackBar) 是一个 Chrome 截图扩展,按 **Alt+Shift+S** 触发截图前会先**扫描整页 DOM**,把凭证、卡号、邮箱、地址等敏感内容遮成黑条,避免截图分享时无意泄露隐私数据。

项目链接：<https://github.com/zatuomfawas/BlackBar>

## 它是什么

一个**带隐私遮蔽的截图扩展**:在截图动作发生前对页面 DOM 做内容识别,把"看起来像敏感信息"的元素涂黑后再触发系统截图。

## 为什么用它 / 适合什么场景

- **客服 / 工单场景**:客服截图用户页面时,不必担心把用户邮箱 / 卡号截进去。
- **Bug 报告**:开发者贴截图给同事 / 公开 issue 时,自动抹掉凭据。
- **合规需求**:截图分享前自动 redaction,省去手工涂黑步骤。

## 关键能力

| 能力 | 说明 |
|------|------|
| 快捷键触发 | Alt+Shift+S 一键截图 |
| DOM 预扫描 | 截图前先扫描整页节点 |
| 多类敏感遮蔽 | 凭证 / 卡号 / 邮箱 / 地址 |
| 黑条覆盖 | 把敏感元素涂黑再截图 |
| Chrome 扩展形态 | 与 Chrome DevTools / 截图工具无缝衔接 |
| 避免事后涂改 | 截图"自带遮蔽",比事后贴黑条更省心 |

## 媒体

视频：<https://video.twimg.com/amplify_video/2086709321942151168/vid/avc1/960x540/nZjyzrYg2OTcO9zy.mp4?tag=29>

## 参考链接

- [项目仓库](https://github.com/zatuomfawas/BlackBar)

## 相关概念

- [SiteCheck](./tool-sitecheck.md) — 浏览器扩展嗅探网站技术栈,与本工具同属"浏览器扩展 + 安全/隐私增强"路线