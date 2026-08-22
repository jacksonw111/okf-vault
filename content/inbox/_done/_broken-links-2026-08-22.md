---
type: "Note"
title: "断链工单（自动生成）"
description: "OKF 校验器检测到的 concepts/ 断链清单；agent 修完后把本文件移到 _done/"
tags: ["okf", "maintenance"]
timestamp: "2026-08-22T19:19:12Z"
---

# ⚠️ 断链工单（自动生成，勿当知识资料）

本文件由 `scripts/okf_validate.py` 在 `concepts/` 发现断链或缺 type 时自动写入 `inbox/`。
**这不是知识资料——不要把本文件本身转成概念。**

逐条修复后，把本文件 `mv` 到 `inbox/_done/`。每条修法二选一：
1. 目标值得收录（术语/工具）→ 在 `concepts/` 新建对应 stub 概念（带 `type` frontmatter）；
2. 目标不值得单独成条 → 把那条 `[x](path.md)` 改成纯文本 `x`。

## 违例清单（34 条）

- content/concepts/note-earendil-agent-harness.md:33: 断链 -> ./concepts/tool-deepseek-harness-rs.md
- content/concepts/note-earendil-agent-harness.md:34: 断链 -> ./concepts/tool-longhorizon-harness.md
- content/concepts/note-earendil-agent-harness.md:35: 断链 -> ./concepts/tool-fable-harness.md
- content/concepts/tool-autoprompt-skill.md:44: 断链 -> ./concepts/playbook-orca-ticket-orchestration.md
- content/concepts/tool-autoprompt-skill.md:45: 断链 -> ./concepts/tool-loop-js.md
- content/concepts/tool-boujoy-harness.md:36: 断链 -> ./concepts/tool-deepseek-harness-desktop.md
- content/concepts/tool-boujoy-harness.md:37: 断链 -> ./concepts/note-deepseek-harness-handbook.md
- content/concepts/tool-cordis-mini.md:36: 断链 -> ./concepts/note-deepseek-harness-handbook.md
- content/concepts/tool-cordis-mini.md:37: 断链 -> ./concepts/note-deepseek-harness-orange-book.md
- content/concepts/tool-crocs-visualizer.md:39: 断链 -> ./concepts/tool-toolcraft.md
- content/concepts/tool-crocs-visualizer.md:40: 断链 -> ./concepts/term-three-js.md
- content/concepts/tool-desktop-fly.md:40: 断链 -> ./concepts/tool-heartmorrow.md
- content/concepts/tool-dreeve.md:38: 断链 -> ./concepts/tool-garmin-tracker-rs.md
- content/concepts/tool-dreeve.md:39: 断链 -> ./concepts/tool-yamtrack.md
- content/concepts/tool-dsh-plugin-dir-tree.md:38: 断链 -> ./concepts/tool-dsh-market.md
- content/concepts/tool-dsh-plugin-dir-tree.md:39: 断链 -> ./concepts/tool-dsh-visualize.md
- content/concepts/tool-flare-ide.md:40: 断链 -> ./concepts/tool-codebase-memory-mcp.md
- content/concepts/tool-flare-ide.md:41: 断链 -> ./concepts/tool-aigx.md
- content/concepts/tool-helius-finance-tracker.md:38: 断链 -> ./concepts/tool-pushcv-cli.md
- content/concepts/tool-helius-finance-tracker.md:39: 断链 -> ./concepts/tool-fintech-advisor.md
- content/concepts/tool-jakubkrehel-skills.md:35: 断链 -> ./concepts/note-jakub-design-skills.md
- content/concepts/tool-jakubkrehel-skills.md:36: 断链 -> ./concepts/term-agent-skills.md
- content/concepts/tool-openbot.md:36: 断链 -> ./concepts/tool-copilotkit.md
- content/concepts/tool-openbot.md:37: 断链 -> ./concepts/tool-agent-stalker.md
- content/concepts/tool-plannotator-guides.md:39: 断链 -> ./concepts/tool-kcap-cli.md
- content/concepts/tool-plannotator-guides.md:40: 断链 -> ./concepts/tool-codex-dream-skin.md
- content/concepts/tool-simplecard.md:40: 断链 -> ./concepts/tool-xianyu-super-butler.md
- content/concepts/tool-simplecard.md:41: 断链 -> ./concepts/tool-gancook.md
- content/concepts/tool-sprix-sage-router.md:37: 断链 -> ./concepts/tool-cotal.md
- content/concepts/tool-sprix-sage-router.md:38: 断链 -> ./concepts/tool-pi-hive.md
- content/concepts/tool-terminal-code-tode.md:35: 断链 -> ./concepts/tool-codex-cli.md
- content/concepts/tool-terminal-code-tode.md:36: 断链 -> ./concepts/tool-pi-fabric.md
- content/concepts/tool-vediohub-dovideoai.md:39: 断链 -> ./concepts/tool-claude-real-video.md
- content/concepts/tool-vediohub-dovideoai.md:40: 断链 -> ./concepts/tool-ai-media-assistant.md
