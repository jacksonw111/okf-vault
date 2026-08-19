---
type: Tool
title: "sloptrim（seyedehsanhadi/sloptrim）"
description: "本地检测 AI 写作套路的 Python 工具，对代理保存的散文文件按 0-100 打分，71 个文档化写作模式 / 62 个检测器，超阈值列出位置要求重写"
resource: "https://github.com/seyedehsanhadi/sloptrim"
tags: "[ai-writing, detection, prose, python, local]"
timestamp: "2026-08-19T16:00:00Z"
---

# sloptrim（seyedehsanhadi/sloptrim）

## 它是什么
[`seyedehsanhadi/sloptrim`](https://github.com/seyedehsanhadi/sloptrim) 盯住 AI 代理**保存的散文文件**（不是代码），按 **0-100 打分**判断「AI 味」严重程度。它覆盖 **71 个已文档化的写作模式**，其中 **62 个**配有检测器；分数落入 5 档，超过 40（strict 模式 20）会列出**具体位置**让代理重写。纯 Python 标准库实现，**无网络、无模型**，纯本地。

## 为什么用它 / 适合什么场景
- AI 写作 pipeline 跑出来的散文味道太重，需要在保存前「人话化」。
- 想要**本地、可审计**的检测工具，不愿把内容上传到第三方检测服务。
- 调试 AI 写作风格时想知道「到底是哪个模式让它显出 AI 味」。

## 关键能力
| 能力 | 说明 |
|------|------|
| 71 个写作模式 | 已文档化的「AI 味」写作模式清单 |
| 62 个检测器 | 大部分模式有可执行的检测器 |
| 0-100 打分 + 5 档 | 量化 AI 味严重程度 |
| 列出具体位置 | 超阈值指出问题位置，让代理针对性重写 |
| 零网络 / 零模型 | 纯 Python 标准库实现 |

## 相关概念
- [项目仓库](https://github.com/seyedehsanhadi/sloptrim) — 仓库主页
- [human-writing](./playbook-human-writing.md) — Playbook 形式的「去 AI 味」skill
- [ai-humanizer-handbook](./tool-ai-humanizer-handbook.md) — AI 文本人性化实操指南