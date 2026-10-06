---
type: "Tool"
title: "Academic-DeAI（中英学术论文去模板化编辑）"
description: "heise3 开源——为学术论文提供中英双语**去模板化**编辑：删掉空泛开头和机械段落的同时**保留数据、引文、术语和证据强度**；适合被 AI 润色过的论文回手再做一轮「人味」清理。"
resource: "https://github.com/heise3/academic-deai"
tags: "[academic, paper, editing, de-templated, ai-writing]"
timestamp: "2026-10-06T22:51:00Z"
---

# Academic-DeAI（中英学术论文去模板化编辑）

## 它是什么

**Academic-DeAI** 是 heise3 开源的工具——为学术论文提供**中英双语去模板化**编辑：删掉空泛开头（"In recent years..." / "随着……的快速发展"）和机械段落（"首先 / 其次 / 最后"硬串联）的同时，**保留数据、引文、术语和证据强度**。

## 为什么用它 / 适合什么场景

- **AI 痕迹清理**：把 LLM 润色后的论文回手再做一轮「人味」清理
- **审稿前自检**：避免审稿人一眼看出 AI 写
- **中英双语**：中文 / 英文论文同等处理
- **保留专业性**：不删数据 / 引文 / 术语，只删套话

## 关键能力

| 能力 | 说明 |
|------|------|
| 去模板开头 | 识别 "In recent years / 随着……" 类硬开头 |
| 去机械段落 | "首先 / 其次 / 最后" 改写为更有机的逻辑连接 |
| 保留数据 / 引文 | 不动正文里的数字、引用、术语 |
| 中英双语 | 同一规则同时适用中英文 |
| 可二次训练 | 输出可作为去模板化训练数据 |

## 参考链接

- 项目链接：<https://github.com/heise3/academic-deai>

## 相关概念

- [academic-research-skills 六类科研 Skill 精选清单](./note-academic-research-skills-list.md) — 同属学术写作生态
