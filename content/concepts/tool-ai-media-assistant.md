---
type: "Tool"
title: "AI Media Assistant（中文创作者本地短视频生成工具）"
description: "本地运行的 Web 短视频生成工具，专为中文创作者设计：文案编辑、字幕模板、逐句配图、TTS 配音、BGM 与视频导出全流程，支持 OmniVoice 与 Qwen3-TTS，数据全存本机。"
tags: "[video, tts, short-video, chinese, local-first, fastapi, react]"
timestamp: "2026-06-28T04:51:00Z"
resource: "https://github.com/alexchan197611/ai_caption_video"
---

# AI Media Assistant（中文创作者本地短视频生成工具）

## 它是什么

AI Media Assistant（原名 `ai_caption_video`）是**本地运行**的 Web 短视频生成工具，专为**中文创作者**设计。后端 Python FastAPI，前端 React，一站式处理：

1. **文案编辑** — 写好脚本
2. **字幕模板** — 自动套样式
3. **逐句配图** — 按句子配插图
4. **TTS 配音** — OmniVoice / Qwen3-TTS
5. **BGM** — 背景音乐轨道
6. **视频导出** — 合成最终短视频

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地优先 | 数据全存本机，仅监听本地地址 |
| 全流程 Web 工具 | 文案→字幕→配图→配音→导出 |
| 中文 TTS | OmniVoice + Qwen3-TTS 双模型可选 |
| React 前端 | 现代 Web UX |
| Python FastAPI 后端 | 一键起服务 |
| 一键导出 | 直接产出可发布的短视频 |

## 安装与运行

```bash
git clone https://github.com/alexchan197611/ai_caption_video
cd ai_caption_video
# 启动 backend + frontend，按 README 配 TTS 模型
```

## 界面预览

![AI Media Assistant 流程视图](https://pbs.twimg.com/media/HL3KNE6aIAAI9IB.jpg)

## 参考链接

- [项目仓库](https://github.com/alexchan197611/ai_caption_video)
- [原始链接](https://x.com/QingQ77/status/2071093987159556513)

## 相关概念

- [autoshorts](tool-autoshorts.md) — 长视频/音频转竖屏短视频，Tauri 2 实现，本地优先
- [Open Knowledge（Inkeep）](tool-open-knowledge.md) — WYSIWYG Markdown + LLM 知识库，AI 直接读写文档