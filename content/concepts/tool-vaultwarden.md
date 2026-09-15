---
type: "Tool"
title: "vaultwarden（Rust 重写的 Bitwarden 自托管服务端）"
description: "dani-garcia/vaultwarden：用 Rust 重写 Bitwarden 服务端，1 核 1G 小机器甚至 512M 内存也能跑；完整实现官方客户端 API，支持 Send 加密分享、附件、网站图标、TOTP 双因子；内置管理后台支持用户 / 组织 / 策略 / 事件日志，官方 App 与浏览器插件可直连。"
resource: "https://github.com/dani-garcia/vaultwarden"
tags: "[self-hosted, password-manager, bitwarden, rust, password-vault]"
timestamp: "2026-09-15T00:10:00Z"
---

# vaultwarden（Rust 重写的 Bitwarden 自托管服务端）

## 它是什么

[vaultwarden](https://github.com/dani-garcia/vaultwarden) 是社区用 **Rust** 重写的 Bitwarden 服务端实现，与官方 Bitwarden 客户端 API 完全兼容。目标场景：**用最低的机器配置（1 核 1G 甚至 512MB 内存）跑一个完整的密码库服务**。

## 关键能力

| 能力 | 说明 |
|------|------|
| Rust 重写 | 内存占用远低于官方镜像（官方动辄几个 GB） |
| 客户端 API 兼容 | 官方 Bitwarden App / 浏览器插件 / 手机端均可直连 |
| Send 加密分享 | 单次 / 限时分享链接 |
| 附件支持 | 密码条目的文件附件 |
| 网站图标 | 自动拉取并缓存 |
| TOTP 双因子 | 内置 TOTP 验证 |
| 管理后台 | 用户 / 组织 / 策略 / 事件日志网页管理 |
| 极低资源 | 树莓派级别就能稳定跑 |

## 与官方 Bitwarden 自托管对比

| 维度 | 官方 Bitwarden | vaultwarden |
|------|---------------|-------------|
| 内存 | 几个 GB 起 | 512MB ~ 1GB 足够 |
| 适用机器 | 至少中端 VPS | 1 核 1G VPS / 树莓派 |
| 客户端 | 官方全兼容 | 官方全兼容 |
| Web Vault | 需 HTTPS 安全上下文（反代） | 需 HTTPS 安全上下文（反代） |
| SLA | 官方背书 | 社区版本，无 SLA |

## 为什么用它

- **省钱**：官方自托管版在 1G VPS 上很可能跑不动；vaultwarden 把门槛打到 512MB / 树莓派级，**月省下服务器钱够买两杯咖啡**。
- **数据可控**：密码库是核心隐私资产，自托管 + 兼容官方 App = **安全的可控 + 客户端习惯不被打乱**。
- **零迁移成本**：现有 Bitwarden 用户可以**直接换服务端**——客户端不变。

## 适用与不适用

- ✅ 个人 / 家庭 / 小团队自建密码库
- ✅ 树莓派 / 小主机 / NAS 玩家
- ❌ 追求官方 SLA 的企业——它不是 Bitwarden 官方出品

## 媒体

![](https://pbs.twimg.com/media/HSJ_fHXbMAAJmJQ.jpg)

## 项目链接

- 仓库：<https://github.com/dani-garcia/vaultwarden>

## 相关概念

- [Self-Hosted（自托管）](term-self-hosted.md) — vaultwarden 是自托管密码管理的代表案例