---
type: Tool
title: "biscuit-studio（小饼干英语视频工坊）"
description: "输入英语知识点，直接得到一条 30 秒竖屏教学视频：LLM 写脚本分镜字幕并自检 → Seedance 出固定角色无字幕原片 → 按审校字幕自动打轴 → FFmpeg 烧中文字幕并高亮英文关键词。"
resource: "https://github.com/kkkoaoa/biscuit-studio"
tags: [edtech, short-video, ai-video, seedance, ffmpeg, react, fastapi]
timestamp: "2026-09-06T00:00:00Z"
---

# biscuit-studio（小饼干英语视频工坊）

## 它是什么

[kkkoaoa/biscuit-studio](https://github.com/kkkoaoa/biscuit-studio) 是把「**英语知识点 → 30 秒竖屏教学视频**」全自动化的工坊。已经上线可用，前后端是 React + FastAPI，Docker Compose 一键启动，API Key 只放浏览器、不写进仓库。

定位：

- **教培场景的短视频流水线**：把知识点转成可发布的成品，而不是再交人工剪辑。

## 工作流

```
知识点输入
  ↓ LLM 写脚本 + 分镜 + 字幕稿（顺带自检语法 / 搭配 / 词源）
  ↓ Seedance 生成固定角色、无字幕原片
  ↓ 按审校过的字幕稿自动打轴
  ↓ FFmpeg 烧中文字幕 + 英文关键词高亮
30 秒竖屏 MP4
```

## 为什么用它 / 适合什么场景

- 英语教学 / 自媒体想量产同款风格短片，又不想每次重排流程。
- 希望 LLM 自检（语法 / 搭配 / 词源）后再生成，把错误率降到最低。
- 团队对 API Key 安全敏感——项目仓库不出现 Key，只在浏览器端持有。

## 关键能力

| 能力 | 说明 |
|------|------|
| LLM 写作 + 自检 | 脚本 / 分镜 / 字幕一次产出，并自检语法、搭配、词源 |
| Seedance 原片 | 生成「固定角色、无字幕」的原片，保证视觉一致性 |
| 自动打轴 | 按审校过的字幕稿自动对齐时间码 |
| FFmpeg 烧字幕 | 中文字幕烧入 + 英文关键词高亮 |
| 端到端 | 输入知识点 → 30 秒竖屏 MP4，无需人工 |
| Docker Compose | 一键启动前后端 |
| 密钥隔离 | API Key 只放浏览器，不进仓库 |

## 相关概念

- [video-ai-talking](./tool-video-ai-talking.md) — 同类「文本到竖屏视频」思路，video-ai-talking 走真人出镜 + AI 对口型
- [ffmpeg-skill](./tool-ffmpeg-skill.md) — biscuit-studio 最后一步「烧字幕」依赖 FFmpeg 能力
- [Kling 3 Cinematic](./note-kling-3-cinematic.md) — 视频生成模型的运镜 / 提示词参考

## 项目链接

- 项目主页：<https://github.com/kkkoaoa/biscuit-studio>
