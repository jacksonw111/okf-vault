---
type: Tool
title: "agent-lock"
description: "通过 eBPF LSM 程序把 AI 代理（Claude Code / Codex / Gemini CLI / omp 等）及其派生的所有进程限制在指定目录内，实时显示它打开的每个文件，给 AI 编码代理套一个文件级沙箱。"
resource: "https://github.com/yeet-src/agent-lock"
tags: "[ai-agent, sandbox, ebpf, lsm, security, claude-code, codex, gemini-cli]"
timestamp: "2026-07-03T06:07:00Z"
---

# agent-lock

## 它是什么
**给 AI 编码代理套文件级沙箱**：通过 **eBPF LSM（Linux Security Module）**程序，把 Claude Code / Codex / Gemini CLI / omp 等 AI 代理及其所有派生的子进程限制在指定目录内。**实时显示**代理打开的每个文件（路径 + 操作），让用户看清「AI 现在到底在读什么、改什么」。

由 yeet-src 开发。

## 为什么用它 / 适合什么场景
- 让 AI 代理在自己项目目录干活时，怕它「越界」——读 / 写 / 删到无关目录（比如 `.ssh/`、其他项目、配置文件）。
- 调试时想知道 AI 每一步具体在动哪些文件，而不是等它「完成」再看 diff。
- 想用 Linux 内核级 eBPF LSM 做强制沙箱，而不是基于文件系统权限的脆弱隔离。
- 在共享服务器 / CI 机器上跑 AI 代理，必须限定工作边界。

## 关键能力
| 能力 | 说明 |
|------|------|
| 沙箱机制 | eBPF LSM 程序，内核级强制 |
| 沙箱边界 | 指定目录 |
| 兼容代理 | Claude Code / Codex / Gemini CLI / omp 等 |
| 进程范围 | 代理主进程 + 所有派生子进程（含 Shell） |
| 文件可见性 | 实时显示每个被打开的文件 |
| 操作可见性 | 显示打开模式（读 / 写等） |
| 形态 | Linux 系统级工具 |

## 相关概念
- [Flounder](tool-flounder.md) — 把编码 Agent 包装为白帽安全审计系统，每步沙箱隔离；agent-lock 是「给 Agent 加沙箱」的安全防护侧工具
- [forkd](tool-forkd.md) — microVM fork 化沙箱；agent-lock 是 eBPF LSM 文件级沙箱，更轻量但仅限 Linux
- [Obscura](tool-obscura-headless-browser.md) — 反检测无头浏览器；agent-lock 不涉及浏览器，纯文件级隔离

## 项目链接
- 项目主页：<https://github.com/yeet-src/agent-lock>

## 媒体
- 演示视频：<https://video.twimg.com/tweet_video/HMRLck_bYAALERP.mp4>