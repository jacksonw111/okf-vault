---
type: Tool
title: "SLYE / speak-like-you-eat (wtfzambo/speak-like-you-eat)"
description: "Pi 的扩展：在模型回答后自动追加一段大白话重写，把 AI 套话翻译成人话；用 /slye on/off 控制开关"
resource: "https://github.com/wtfzambo/speak-like-you-eat"
tags: [pi, extension, plain-language, ai-writing, llm]
timestamp: 2026-08-20T00:58:00Z
---

# SLYE / speak-like-you-eat (wtfzambo/speak-like-you-eat)

## 它是什么
[`wtfzambo/speak-like-you-eat`](https://github.com/wtfzambo/speak-like-you-eat)（缩写 **SLYE**）是一个 **Pi** 扩展。它在模型回答**结束之后**自动追加一段"**大白话重写**"，把 AI 套话翻译成人话，**原文一字不动**。名字取自意大利俗语 *parla come mangi*：说话要跟吃饭一样直接，不堆空词。

## 为什么用它 / 适合什么场景
- 喜欢模型的推理能力，但嫌它正式 / 套话 / 啰嗦。
- 想有一个**最低成本**的"说人话层"挂在 Pi 外面，而不是替换模型。
- 写作 / 教学 / 内部沟通时希望 AI 输出能"第一眼就读懂"。

## 关键能力
| 能力 | 说明 |
|------|------|
| 原回答保留 | AI 原答案不被修改，只在末尾追加 |
| 大白话卡片 | 末尾添加「🤌 Speak like you eat:」卡片 |
| 模型选择 | `/slye model` 切到一个已登录的便宜模型（推荐 Terra / DeepSeek V4 Flash / GPT-OSS 120B） |
| 自动跳过 | 回答正文不足 200 字 → 不重写 |
| 超时兜底 | 重写 45 秒还没出 → 保留原文 |
| 一键开关 | `/slye on` / `/slye off` |

## 配置示例
```
/slye model     # 选一个便宜的二级模型跑重写
/slye on        # 启动
/slye off       # 关闭
```

## 关键参数（默认值）
| 参数 | 默认 | 含义 |
|------|------|------|
| min_answer_length | 200 字 | 短于此跳过重写 |
| rewrite_timeout | 45 s | 超时即放弃 |
| 二次模型建议 | Terra / DeepSeek V4 Flash / GPT-OSS 120B | 作者实测便宜、推理少 |

## 相关概念
- [项目仓库](https://github.com/wtfzambo/speak-like-you-eat) — 仓库主页
- [pi-agent-core-book](./note-pi-agent-core-book.md) — 关于 Pi 代理体系的总览，本工具就是一个扩展
