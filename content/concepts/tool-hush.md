---
type: Tool
title: "hush"
description: "面向 AI 代理的密钥管理 Bash 工具：密钥永不离开系统钥匙串，只在被调用的那一刻按名注入到子进程环境里。"
resource: "https://github.com/royashbrook/hush"
tags: "[secrets, keychain, ai-agent, bash, cli]"
timestamp: "2026-06-29T16:00:00Z"
---

# hush

## 它是什么
hush 是一个 Bash 脚本实现的小工具，专门解决「AI 代理跑带密钥命令时密钥被打印或粘进聊天记录」的问题：设计上根本没有「读出明文」这一步。密钥存进各平台原生钥匙串（macOS Keychain / Linux Secret Service / Windows Credential Manager），使用时按名注入到目标命令的环境变量里，命令执行完即销毁。

## 为什么用它 / 适合什么场景
- **代理跑了 `curl -H "Authorization: Bearer sk-..."`，结果把整行响应回显出来**：用 hush 调起 `hush run my-key -- curl ...`，sk-xxx 永远不出现在命令字符串里，也永远不会被回显。
- **代理会话日志被截图 / 复制粘贴出去**：密钥根本没在代理上下文里出现过。
- **想给代理长期配一批「按名取用」的密钥**：代理读 `SKILL.md` 即可自行 `hush set` / `hush get` / `hush run`。

## 关键能力
| 能力 | 说明 |
|------|------|
| 按名存密钥 | `hush set NAME` 把读自 stdin 的值存进钥匙串 |
| 按名取密钥 | `hush get NAME` 输出明文（仅供调试） |
| 按名注入执行 | `hush run NAME -- cmd args...` 把密钥作为环境变量注入 cmd |
| 随机生成密钥 | `hush gen NAME` 直接在钥匙串里建随机值 |
| 跨平台后端 | macOS Keychain / Linux Secret Service / Windows Credential Manager |
| 代理友好 | 一条 `SKILL.md` 说明即可让代理自助安装 / 使用 |

## 安全模型
- 「不读出明文」是核心承诺：`run` 模式只通过文件描述符 / 环境变量注入，目标进程读完后这些值随进程销毁
- `get` 子命令仍会输出明文，仅供调试与人工查看，**不应在代理自动化里调用**
- 代理读 SKILL.md 即可自助 `set` / `run`，不需要人工介入

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071480785605943752)
- [项目链接](https://github.com/royashbrook/hush)

## 相关概念
- [Vaultty](./tool-vaultty.md) — macOS 块式终端 + Keychain 自动注入 .env，与 hush 思路一致但面向日常终端场景
- [Verenu](./tool-verenu.md) — 同样要把外部 API Key 注入到本地进程，可与 hush 共用密钥存储