---
type: "Tool"
title: "claude-code-recap（noluyorAbi/claude-code-recap）"
description: "敲一条命令就把本地所有 Claude Code 会话按时间线捞出来——路径、摘要、分支、模型、轮次都列好,附上能直接粘回去续聊的命令,解决 /resume 只能看当前目录的局限。"
resource: "https://github.com/noluyorAbi/claude-code-recap"
tags: "[claude-code, session-history, cli, productivity, agent-tui]"
timestamp: "2026-07-16T04:53:00Z"
---

# claude-code-recap

[claude-code-recap](https://github.com/noluyorAbi/claude-code-recap) 是一条 CLI,装上后敲一句 `recap` 就把**本机所有项目里的 Claude Code 会话**按时间序列出来——路径、摘要、分支、模型、轮次、续聊命令一并给到。Claude Code 自带的 `/resume` 只能看当前工作目录,这个工具跨目录聚合。

## 它解决了什么

用 Claude Code 跑多个项目的人,经常会忘:昨天那个改 React 的会话在哪、那次写 ETL 的跑了多少轮、能不能立刻续。`/resume` 只能在当前目录里挑,而很多对话散在七八个项目里;Claude Code 自带的 transcript 文件存在 `~/.claude/projects/...jsonl` 下,手工翻很累。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全局聚合 | 把机器上所有 Claude Code 项目会话一次性扫出来,不必 `cd` 到对应目录 |
| 元信息显示 | 路径、摘要、分支、模型、轮次全部列出 |
| 一键续聊 | 每条记录旁边附 `claude --resume <id>` 类命令,复制即用 |
| CLI 极简 | 单条命令 + TTY 选择,无需起 Web |

## 媒体

视频：

- <https://video.twimg.com/amplify_video/2076877605308133376/vid/avc1/1920x1080/q1Y1brVfZzZPcSl5.mp4?tag=28>

## 参考链接

- [项目仓库](https://github.com/noluyorAbi/claude-code-recap)

## 相关概念

- [Claude Code](./tool-claude-code.md) — 本工具专为 Claude Code 量身,二者协同使用
- [TokenScope](./tool-tokenscope.md) — 与本工具互补,后者聚焦 token 用量与成本
- [Happier](./tool-happier.md) — 跨设备接续 Claude Code 会话的另一套方案,与本工具并列参考
