---
type: Tool
title: "SimulTeX（acb3688/simultex）"
description: "把 Codex CLI / Claude Code 的终端会话镜像到本地 localhost 浏览器页面，终端键盘输入不动、浏览器只读跟看，长对话回看 / 搜索 / 复制排版问题"
resource: "https://github.com/acb3688/simultex"
tags: "[codex, claude-code, terminal, viewer, readability]"
timestamp: "2026-08-19T16:00:00Z"
---

# SimulTeX（acb3688/simultex）

## 它是什么
[`acb3688/simultex`](https://github.com/acb3688/simultex) 把 Codex CLI 与 Claude Code 在终端里跑的会话**镜像**到本地 localhost 的浏览器页面：终端保持原样运行（键盘输入与命令交互不受影响），浏览器只读地跟随显示。它在本地起一层 loopback 反向代理，把模型 API 的往返归一化成 turn、调用、用户消息这几类事件，让 Markdown 与 LaTeX 在浏览器侧呈现更精确；启动信息、状态条、权限面板这些 API 拿不到的内容由 PTY 重构补齐。

## 为什么用它 / 适合什么场景
- 长会话（几千轮 token 回看）在终端里翻找 / 搜索 / 复制排版乱得没法用。
- 想在副屏 / 平板 / 浏览器侧以「可滚动 + 可搜索 + 可复制带格式」的形式跟看。
- 在不打断终端交互的前提下，把对话内容结构化展示。

## 关键能力
| 能力 | 说明 |
|------|------|
| 终端 ↔ 浏览器镜像 | 终端跑、浏览器看，键盘流走原终端不走浏览器 |
| loopback 反向代理 | 把模型 API 往返归一化为 turn / 调用 / 用户消息等事件 |
| 精确 Markdown / LaTeX | 浏览器侧渲染优于终端 ANSI / 等宽字体回放 |
| PTY 重构补全 | 启动信息、状态条、权限面板等 API 拿不到的 UI 由 PTY 端补充 |
| 只读 | 浏览器侧不能改会话，保留会话原始权威 |

## 媒体
- 视频：<https://video.twimg.com/amplify_video/2089206864223539200/vid/avc1/1280x720/iGLKNaNZQU2RYFkY.mp4?tag=29>

## 相关概念
- [项目仓库](https://github.com/acb3688/simultex) — 仓库主页
- [codex-trajectory](./tool-codex-trajectory.md) — 把 Codex 本地任务日志解析为结构化事件账本