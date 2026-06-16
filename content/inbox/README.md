---
type: Note
title: inbox 投递区说明
description: 把要喂给 agent 的资料丢进本文件夹。agent 会按 PRODUCER.md 协议把它们转成 OKF 概念文件，处理完移到 _done/。
tags: [okf, inbox]
timestamp: 2026-06-16T12:30:00Z
---

# inbox/ —— 资料投递区

## 怎么用

1. **把资料扔进来**：任意格式都行——`.md`、`.pdf`、`.txt`、截图、一段话、一个 URL（可以存成 `.md` 写上链接）。
2. **（可选）附一句话意图**：在资料文件名或同目录新建 `_.note`，写上你希望 agent 怎么处理，例如：
   ```
   把这份 PDF 转成 1 个 Tool 概念 + 1 个 Playbook 概念，拆开。
   ```
   不写也行，agent 会自己推断。
3. **告诉 agent**：对 agent 说"处理 inbox" / "把 inbox 里的资料转成 OKF"。
4. agent 按 [`../PRODUCER.md`](../PRODUCER.md) 处理，产出到 `concepts/`，并把本文件夹里的资料移到 `_done/`。

## 约定

- `_done/`：已处理资料的归档，不要重复投喂。
- 同一份资料想产出多个概念，在意图里说清楚即可。

## 当前状态

（这里由 agent 维护：待处理 / 处理中的资料清单。）
