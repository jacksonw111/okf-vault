---
type: Tool
title: "Rescript（改字幕 = 剪视频）"
description: "剪视频不用开 Premiere / Final Cut 了。Rescript 把剪辑变成改字幕：删文字等于删画面，浏览器里跑完整套流程，文件全程不出本机。"
resource: "https://github.com/wassgha/rescript"
tags: [video, editor, browser, subtitle, local-first, privacy]
timestamp: "2026-07-30T03:35:00.000Z"
---

# Rescript

## 它是什么

**「改字幕 = 剪视频」的浏览器视频编辑器**——把传统的非线性时间轴剪辑抽象成「字幕文本编辑」：

- 删除字幕行 → 对应片段从视频里删除
- 编辑字幕文字 → 同时改写视频对应段
- 调整字幕顺序 → 视频片段顺序跟着变

整个工作流跑在浏览器里，**视频文件全程不出本机**（本地处理）。

![截图](https://pbs.twimg.com/media/HOXY1smaYAAV5Px.jpg)

## 解决的痛点

| 痛点 | Rescript 解法 |
|------|--------------|
| Premiere / Final Cut 太重 | 浏览器跑 |
| 时间轴剪辑门槛高 | 改字幕就行 |
| 云端剪辑要上传（隐私 / 带宽） | 全本地 |
| 文字与画面同步靠手工 | 字幕驱动自动同步 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 字幕驱动剪辑 | 文本即时间轴 |
| 浏览器原生 | 不装客户端 |
| 全本地处理 | 文件不出本机 |
| 隐私优先 | 适合敏感素材 |
| 轻量 | 比 NLE 软件低得多 |

## 适合谁

- 短视频 / 字幕驱动内容创作者
- 处理敏感素材（隐私 / 法律 / 商业机密）
- 想快速剪辑但学不会 Premiere 的非专业用户
- 想把视频剪成纯文本工作流一部分的人

## 原始链接

- [项目仓库](https://github.com/wassgha/rescript)
- [推文剪藏](https://x.com/QingQ77/status/2082671272790736900)

## 相关概念

- [OpenMontage](./tool-openmontage.md) — 首个开源 agentic 视频制作系统，自然语言到成片
- [autoshorts](./tool-autoshorts.md) — Tauri 2 长视频 / 音频转竖屏短视频
- [Timecode-Agent](./tool-timecode-agent.md) — 长视频带时间戳证据账本，转录优先