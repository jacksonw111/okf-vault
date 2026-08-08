---
type: "Note"
title: "断链工单（自动生成）"
description: "OKF 校验器检测到的 concepts/ 断链清单；agent 修完后把本文件移到 _done/"
tags: ["okf", "maintenance"]
timestamp: "2026-08-08T19:25:18Z"
---

# ⚠️ 断链工单（自动生成，勿当知识资料）

本文件由 `scripts/okf_validate.py` 在 `concepts/` 发现断链或缺 type 时自动写入 `inbox/`。
**这不是知识资料——不要把本文件本身转成概念。**

逐条修复后，把本文件 `mv` 到 `inbox/_done/`。每条修法二选一：
1. 目标值得收录（术语/工具）→ 在 `concepts/` 新建对应 stub 概念（带 `type` frontmatter）；
2. 目标不值得单独成条 → 把那条 `[x](path.md)` 改成纯文本 `x`。

## 违例清单（22 条）

- content/concepts/tool-deepclonewebsite.md:42: 断链 -> ./tool-httrack.md
- content/concepts/tool-deepclonewebsite.md:43: 断链 -> ./tool-firecrawl.md
- content/concepts/tool-ghostlink.md:41: 断链 -> ./tool-llama-cpp.md
- content/concepts/tool-ghostty-studio.md:36: 断链 -> ./tool-ghostty.md
- content/concepts/tool-icloud-create-workbench.md:36: 断链 -> ./term-apple-hide-my-email.md
- content/concepts/tool-icloud-create-workbench.md:37: 断链 -> ./tool-simplelogin.md
- content/concepts/tool-liyuan.md:42: 断链 -> ./term-story-engine.md
- content/concepts/tool-macos-web.md:41: 断链 -> ./tool-win11-web.md
- content/concepts/tool-macos-web.md:42: 断链 -> ./note-single-file-web.md
- content/concepts/tool-macos-web.md:43: 断链 -> ./tool-win98-browser.md
- content/concepts/tool-mailworker.md:41: 断链 -> ./tool-resend.md
- content/concepts/tool-mailworker.md:43: 断链 -> ./tool-cloudflare-workers.md
- content/concepts/tool-oh-my-cli.md:38: 断链 -> ./tool-codex-cli.md
- content/concepts/tool-postcat.md:43: 断链 -> ./tool-httpie.md
- content/concepts/tool-postcat.md:44: 断链 -> ./tool-bruno.md
- content/concepts/tool-repopilot.md:42: 断链 -> ./tool-langgraph.md
- content/concepts/tool-salience-macos.md:40: 断链 -> ./tool-gitbutler.md
- content/concepts/tool-sparkfetch.md:40: 断链 -> ./tool-jina-reader.md
- content/concepts/tool-sparkfetch.md:41: 断链 -> ./tool-firecrawl.md
- content/concepts/tool-sparkfetch.md:42: 断链 -> ./note-markdown-fetch-protocol.md
- content/concepts/tool-webchat.md:38: 断链 -> ./term-webrtc.md
- content/concepts/tool-webchat.md:39: 断链 -> ./tool-briar.md
