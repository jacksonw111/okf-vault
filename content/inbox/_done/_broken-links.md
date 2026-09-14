---
type: "Note"
title: "断链工单（自动生成）"
description: "OKF 校验器检测到的 concepts/ 断链清单；agent 修完后把本文件移到 _done/"
tags: ["okf", "maintenance"]
timestamp: "2026-09-14T22:14:20Z"
---

# ⚠️ 断链工单（自动生成，勿当知识资料）

本文件由 `scripts/okf_validate.py` 在 `concepts/` 发现断链或缺 type 时自动写入 `inbox/`。
**这不是知识资料——不要把本文件本身转成概念。**

逐条修复后，把本文件 `mv` 到 `inbox/_done/`。每条修法二选一：
1. 目标值得收录（术语/工具）→ 在 `concepts/` 新建对应 stub 概念（带 `type` frontmatter）；
2. 目标不值得单独成条 → 把那条 `[x](path.md)` 改成纯文本 `x`。

## 违例清单（16 条）

- content/concepts/tool-ampcode.md:38: 断链 -> ./tool-pi-coding-agent.md
- content/concepts/tool-artemis-google-android-automation.md:60: 断链 -> ./term-mcp.md
- content/concepts/tool-artemis-google-android-automation.md:61: 断链 -> ./term-computer-use.md
- content/concepts/tool-authentik.md:42: 断链 -> ./term-self-hosted.md
- content/concepts/tool-awesome-llm-apps.md:55: 断链 -> ./term-rag.md
- content/concepts/tool-dictionary-of-ai-coding.md:34: 断链 -> ./term-context-engineering.md
- content/concepts/tool-farcaster-multi-agent-desktop.md:43: 断链 -> ./tool-pi-coding-agent.md
- content/concepts/tool-fly-wirehead.md:44: 断链 -> ./term-comp-neuro.md
- content/concepts/tool-gvs5h-multi-agent-orchestration.md:49: 断链 -> ./term-multi-agent.md
- content/concepts/tool-mobai-dev-ios-from-linux.md:39: 断链 -> ./term-cloud-coding-agent.md
- content/concepts/tool-mobai-dev-ios-from-linux.md:40: 断链 -> ./term-sandbox.md
- content/concepts/tool-open-code-review.md:47: 断链 -> ./term-harness-engineering.md
- content/concepts/tool-pi-review.md:41: 断链 -> ./tool-pi-coding-agent.md
- content/concepts/tool-sol-pi.md:49: 断链 -> ./tool-pi-coding-agent.md
- content/concepts/tool-sol-pi.md:51: 断链 -> ./term-context-engineering.md
- content/concepts/tool-thinkingbox-ms-agent-eval.md:44: 断链 -> ./term-mcp.md
