---
type: "Note"
title: "断链工单（自动生成）"
description: "OKF 校验器检测到的 concepts/ 断链清单；agent 修完后把本文件移到 _done/"
tags: ["okf", "maintenance"]
timestamp: "2026-09-26T21:46:22Z"
---

# ⚠️ 断链工单（自动生成，勿当知识资料）

本文件由 `scripts/okf_validate.py` 在 `concepts/` 发现断链或缺 type 时自动写入 `inbox/`。
**这不是知识资料——不要把本文件本身转成概念。**

逐条修复后，把本文件 `mv` 到 `inbox/_done/`。每条修法二选一：
1. 目标值得收录（术语/工具）→ 在 `concepts/` 新建对应 stub 概念（带 `type` frontmatter）；
2. 目标不值得单独成条 → 把那条 `[x](path.md)` 改成纯文本 `x`。

## 违例清单（14 条）

- content/concepts/term-clm.md:44: 断链 -> ./term-jev.md
- content/concepts/term-clm.md:45: 断链 -> ./term-laya.md
- content/concepts/term-clm.md:46: 断链 -> ./term-clm-8b.md
- content/concepts/tool-djev-run.md:44: 断链 -> ./tool-cloud-run.md
- content/concepts/tool-jev-chat-jarvis-mac.md:49: 断链 -> ./term-decider-2b.md
- content/concepts/tool-jev-seo.md:49: 断链 -> ./term-jev.md
- content/concepts/tool-jevrev.md:14: 断链 -> ./term-jev.md
- content/concepts/tool-jevrev.md:44: 断链 -> ./term-jev.md
- content/concepts/tool-laya-server.md:14: 断链 -> ./term-laya.md
- content/concepts/tool-laya-server.md:46: 断链 -> ./term-laya.md
- content/concepts/tool-laya-server.md:47: 断链 -> ./term-jev.md
- content/concepts/tool-tincan-cli.md:25: 断链 -> ./term-iroh.md
- content/concepts/tool-tincan-cli.md:45: 断链 -> ./term-iroh.md
- content/concepts/tool-tincan-cli.md:46: 断链 -> ./term-ratatui.md
