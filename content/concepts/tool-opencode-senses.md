---
type: Tool
title: "opencode-senses"
description: "给纯文本 OpenCode 编码 agent 加上本地视觉层：截图 OCR、目标定位、颜色测量等图像理解在本地 GPU 完成，无需 API key"
resource: "https://github.com/itsmeadarsh2008/opencode-senses"
tags: [opencode, agent, vision, ocr, local-gpu]
timestamp: 2026-08-16T16:00:00Z
---

# opencode-senses

## 它是什么
`itsmeadarsh2008/opencode-senses` 是一个面向 **OpenCode**（终端编码 agent）的插件 / 扩展，给纯文本模型挂上一个**本地视觉层**。所有图像理解能力（OCR、目标检测 / 定位、像素级颜色测量等）都跑在用户本机 GPU 上，**不需要 OpenAI / Anthropic 之类的视觉 API key**，也不上传截图。

## 为什么用它 / 适合什么场景
- 想让 coding agent「看一眼截图就知道哪个按钮是哪个」但又不想把截图送云端。
- 离线 / 隐私敏感场景：开发机断网、本地模型当主脑、截图属机密。
- 减少 vision 模型 API 调用费：常驻 OCR / 定位类需求直接本地跑。
- 跟 OpenCode 命令行形态天然结合：终端 agent 拿到一个 UI bug 截图就能自己分析而不是请人类描述。

## 关键能力
| 能力 | 说明 |
|------|------|
| 截图 OCR | 从 UI 截图里抽文字，配合 agent 文本推理 |
| 目标定位 | 在截图里找到指定控件 / 元素并给坐标，可接 mouse / click 工具 |
| 颜色测量 | 像素级取色，方便验证视觉回归 |
| 本地 GPU 推理 | 不走云端，截图不出机器；不需要任何 vision API key |
| OpenCode 集成 | 作为 OpenCode 的扩展直接挂上去，无需改主程序 |

## 媒体
- ![](https://pbs.twimg.com/media/HPvGe92bAAAzlCs.jpg)

## 相关概念
- [项目链接](https://github.com/itsmeadarsh2008/opencode-senses)