---
type: "Tool"
title: "Vaultty（macOS 块式终端 + 钥匙串自动注入 .env）"
description: "automic-vault/vaultty —— macOS 上搭配 Automic Vault 用的块式终端：命令和输出按块排好，加密的 .env 变量从钥匙串（Keychain）自动加载，告别每次手动 source .env / 输入密钥。"
tags: "[macos, terminal, keychain, dotenv, secret-management, block-ui]"
timestamp: "2026-06-22T07:40:00Z"
---

# Vaultty（macOS 块式终端 + 钥匙串自动注入 .env）

## 它是什么

[`automic-vault/vaultty`](https://github.com/automic-vault/vaultty) 是 macOS 上一款**搭配 Automic Vault 用的块式终端**。它解决两个长期困扰开发者的小问题：

1. **块式排版**：命令和对应输出以「块」形式整齐排列，而不是像传统 terminal 那样所有内容混在一个无限滚动的流里。
2. **钥匙串自动注入 .env**：所有用 Automic Vault 加密存储在 macOS Keychain 里的环境变量，会在命令执行前**自动注入到环境**，不再需要手动 `source .env` / 复制粘贴密钥 / 每次 git pull 后重设。

> 截图：
> ![](https://pbs.twimg.com/media/HLTaiWua0AA-Zih.jpg)
> ![](https://pbs.twimg.com/media/HLTanB3aEAA0Wn3.jpg)

## 为什么用它 / 适合什么场景

- **开发者每天 `source .env` 数十次**：每个项目都有自己的 API key / DB URL / 签名密钥，跨项目切换时手动维护 .env 既繁琐又不安全（容易误提交）。
- **macOS Keychain 已是系统级秘密管理**：与其自己搞加密文件，不如直接用系统 Keychain。
- **传统 terminal 的"流式"输出难回顾**：跑完一长串命令，回头想看「第三步的输出是什么」要往上翻半天。块式 UI 把每条命令及其输出圈成一个块，扫一眼就明白。

适合：

- 跨多个 SaaS / 云项目、需要管理大量 API key 的开发者。
- 对"环境变量管理"有安全要求（不能写在 `.env` 里 commit 出去）的团队 / 个人。
- 喜欢 IDE-like 终端体验（VSCode 那种 block 排版）的人。

## 关键能力

| 能力 | 说明 |
|---|---|
| 块式终端 UI | 每条命令 + 输出为一个块，便于回顾 |
| Automic Vault 集成 | macOS Keychain 加密存储密钥 |
| 自动注入 .env | 命令执行前把 Keychain 里的变量注入环境 |
| 不再手动 source | 跨项目切换不用手动维护 .env |
| macOS 原生 | 与系统 Keychain 深度集成（推测走 Security framework） |

## 工作流

```
Automic Vault（写入）                Vaultty（使用）
  ↓                                       ↑
macOS Keychain  ←── 自动同步 ──→  读取 + 注入环境变量
  ↓
加密存储 API key / DB URL / 签名密钥
```

用户在 Vaultty 里直接跑命令（如 `npm run dev`），背后已经把 `DATABASE_URL` / `STRIPE_SECRET_KEY` 等全部注入好。

## 与"传统 .env 方案"的对比

| 维度 | .env 文件 | Vaultty + Automic Vault |
|---|---|---|
| 存储 | 明文文件（容易误提交） | 加密 + Keychain |
| 跨项目 | 每个项目一个 .env，手动切换 | Keychain 统一管理 |
| 同步 | 不会同步 | macOS Keychain iCloud 同步（可选） |
| 注入 | `source .env` / direnv | 终端启动时自动注入 |
| 适合场景 | 简单项目、临时测试 | 多项目、安全敏感 |

## 适用人群

- macOS 开发者。
- 维护 5+ 项目 / 同时跑多个 SaaS 集成的全栈 / 后端工程师。
- 对 secret 管理有合规要求（金融 / 医疗 / 政企）的个人或团队。

## 参考链接

- [项目链接](https://github.com/automic-vault/vaultty)
- [原始链接](https://t.co/tNDSvgFiR0)

## 相关概念

- [OmniWM（macOS 水平滚动平铺 WM）](tool-omniwm-macos.md) — macOS 桌面工具
- [Forel（macOS 文件夹自动化）](tool-forel-macos.md) — macOS 文件夹自动化工具
- [Cloud Mail](tool-cloud-mail.md) — 单域名「无限收发」自托管邮件