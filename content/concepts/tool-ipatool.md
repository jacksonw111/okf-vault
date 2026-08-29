---
type: Tool
title: "ipatool（命令行下载与管理 iOS App Store IPA）"
description: "majd/ipatool：从 App Store 下载 IPA（应用包）的命令行工具，支持登录、获取 / 列出应用元数据与版本，并发起签名 SAP 请求；最新 v2.4.0 修复了 Apple 服务端变更带来的鉴权问题。"
resource: "https://github.com/majd/ipatool"
tags: [ios, app-store, ipa, cli, download, signing, automation]
timestamp: "2026-08-29T21:30:00Z"
---

# ipatool（命令行下载与管理 iOS App Store IPA）

## 它是什么

[majd/ipatool](https://github.com/majd/ipatool) 是从 App Store **下载 IPA（iOS 应用包）**的命令行工具——正常用户从 App Store 装 App，开发者 / CI / 备份场景需要**直接拿到 IPA**（用于归档、签名、重打包、企业分发、灰盒测试）。

能力：

- App Store 账号**登录 / 登出**；
- 按 bundle ID **获取 / 列出** App 元数据与版本；
- 下载指定版本 IPA；
- v2.4.0 起支持**签名 SAP 请求**（应对 Apple 服务端变更带来的鉴权问题）。

## 为什么用它 / 适合什么场景

- **企业内部分发 / 灰盒测试**：把 IPA 装到登记设备，无需走 TestFlight；
- **CI / 自动化**：从 App Store 拉一个稳定版本 IPA 跑兼容性测试 / 安全扫描；
- **备份 / 归档**：把发布过的 App 版本留在本地仓库；
- **逆向 / 安全研究**：拿到 App 后做静态分析 / 漏洞扫描；
- 开发者想**不依赖 Xcode** 直接跟 App Store 交互。

## 关键能力

| 能力 | 说明 |
|------|------|
| 命令行 | 非 GUI，适合 CI / 脚本 |
| 账号登录 | App Store 账号鉴权 |
| 元数据查询 | 按 bundle ID 列出 App / 版本信息 |
| IPA 下载 | 指定版本号拉取应用包 |
| SAP 签名 | v2.4.0 起发起签名请求 |
| 鉴权修复 | 应对 Apple 服务端变更带来的鉴权失败 |

## 相关概念

- [darwin-vm](./tool-darwin-vm.md) — 在 QEMU 上跑 iOS 做安全研究；ipatool 是研究 / 测试前的**包获取**阶段
- [Plugin DeepSeek Vision](./tool-plugin-deepseek-vision.md) — 不直接相关；列举为示例非 Apple 平台工具

## 参考链接

- 项目链接：<https://github.com/majd/ipatool>
- 原始推文：<https://x.com/Wen_Zw/status/2093561866257871252>