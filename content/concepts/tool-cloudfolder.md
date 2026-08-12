---
type: "Tool"
title: "CloudFolder"
description: "Rust 写的 Windows 工具：rclone SFTP + WinFsp 把远端 GPU 服务器目录投影成普通 Windows 路径，Claude Code / Codex / VS Code / Explorer 都能直接读写，本地 agent 不用在每台机器重新配登录、Skills、MCP。"
resource: "https://github.com/EurekaZang/CloudFolder"
tags: ["windows", "rust", "rclone", "winfsp", "ssh", "sftp", "filesystem", "agent", "remote-gpu"]
timestamp: "2026-08-12T15:44:00Z"
---

# CloudFolder

[CloudFolder](https://github.com/EurekaZang/CloudFolder) 是一个 Rust 写的 Windows 工具：**rclone SFTP + WinFsp** 把远端（GPU）服务器的目录投影成本机普通 Windows 路径，让 Claude Code、Codex、VS Code、Explorer 等所有本地应用直接读写远端代码与数据。

## 它是什么

本地 agent 想用远端 GPU 服务器的代码 / 数据时，传统做法是要么 SSH 上去操作、要么每台机器重新配登录 / Skills / MCP / 工具链。CloudFolder 把远端目录"挂"成本地路径，让本地一切工具原生就当成地路径读写。

## 为什么用它 / 适合什么场景

- **本地 agent 用远端算力**：本机跑 agent，远端跑 GPU；agent 直接读写远端目录。
- **统一配置一次**：不必在每台机器重新配 Skills / MCP / 登录。
- **VS Code / Explorer 兼容**：当作本地路径，IDE / 文件管理器都能用。
- **避免双机同步**：不必 rsync / git pull，省去中间环节。

## 关键能力

| 能力 | 说明 |
|------|------|
| 远端目录挂载 | SFTP 服务器目录映射成 Windows 本地路径 |
| rclone + WinFsp | 成熟底层：rclone 提供 SFTP、WinFsp 提供文件系统驱动 |
| 本地工具兼容 | Claude Code / Codex / VS Code / Explorer 都能直接访问 |
| Rust 实现 | 单二进制、性能好 |
| 一处配置 | 登录、Skills、MCP 只配一次，本机所有工具自动可见 |

## 参考链接

- [项目仓库](https://github.com/EurekaZang/CloudFolder)

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent，是 CloudFolder 最常见的本地消费者
- [Codex CLI](./tool-codex-cli.md) — OpenAI 的编码 agent CLI，同样可以从 CloudFolder 挂载路径读写
- [rclone](./tool-rclone.md) — CloudFolder 用 rclone 提供 SFTP 后端