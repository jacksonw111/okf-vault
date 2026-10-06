---
type: "Note"
title: "断链工单（自动生成）"
description: "OKF 校验器检测到的 concepts/ 断链清单；agent 修完后把本文件移到 _done/"
tags: ["okf", "maintenance"]
timestamp: "2026-10-06T22:51:58Z"
---

# ⚠️ 断链工单（自动生成，勿当知识资料）

本文件由 `scripts/okf_validate.py` 在 `concepts/` 发现断链或缺 type 时自动写入 `inbox/`。
**这不是知识资料——不要把本文件本身转成概念。**

逐条修复后，把本文件 `mv` 到 `inbox/_done/`。每条修法二选一：
1. 目标值得收录（术语/工具）→ 在 `concepts/` 新建对应 stub 概念（带 `type` frontmatter）；
2. 目标不值得单独成条 → 把那条 `[x](path.md)` 改成纯文本 `x`。

## 违例清单（27 条）

- content/concepts/note-academic-research-skills-list.md:48: 断链 -> ./tool-academic-research-skills.md
- content/concepts/note-awesome-zhuiju-free.md:41: 断链 -> ./term-awesome-list.md
- content/concepts/note-jev-cookbook.md:44: 断链 -> ./term-datawhale-china.md
- content/concepts/note-llamaindex-agentic-ocr.md:46: 断链 -> ./tool-llamaindex.md
- content/concepts/note-quant-wiki.md:37: 断链 -> ./term-quant-cn-resources.md
- content/concepts/tool-answer-me-html.md:44: 断链 -> ./term-claude-code.md
- content/concepts/tool-backburner.md:40: 断链 -> ./term-qwen3.md
- content/concepts/tool-backburner.md:41: 断链 -> ./term-apple-silicon.md
- content/concepts/tool-claude-image-view.md:45: 断链 -> ./term-claude-code.md
- content/concepts/tool-emdash.md:37: 断链 -> ./term-ai-coding-agent.md
- content/concepts/tool-hextaui.md:45: 断链 -> ./tool-shadcn-ui.md
- content/concepts/tool-hextaui.md:47: 断链 -> ./tool-hextaui-blocks.md
- content/concepts/tool-hk-traffic-intelligence.md:38: 断链 -> ./term-cloudflare-workers.md
- content/concepts/tool-hk-traffic-intelligence.md:39: 断链 -> ./term-maplibre-gl.md
- content/concepts/tool-invidious.md:45: 断链 -> ./tool-piped.md
- content/concepts/tool-jevbox.md:40: 断链 -> ./tool-spicedb.md
- content/concepts/tool-lcu.md:38: 断链 -> ./term-pi-agent.md
- content/concepts/tool-lcu.md:39: 断链 -> ./term-codex.md
- content/concepts/tool-muse-gadget-sdk.md:37: 断链 -> ./term-esp32.md
- content/concepts/tool-muse-gadget-sdk.md:38: 断链 -> ./term-home-assistant.md
- content/concepts/tool-mygo.md:40: 断链 -> ./tool-wails.md
- content/concepts/tool-neonplan3d.md:38: 断链 -> ./term-home-assistant.md
- content/concepts/tool-neonplan3d.md:39: 断链 -> ./term-3d-floor-plan.md
- content/concepts/tool-opengym.md:41: 断链 -> ./term-docker-compose.md
- content/concepts/tool-serverbox.md:38: 断链 -> ./tool-termux.md
- content/concepts/tool-tsuzuri.md:41: 断链 -> ./tool-logseq.md
- content/concepts/tool-warp-lite.md:37: 断链 -> ./tool-warp.md
