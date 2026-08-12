---
type: "Tool"
title: "Zero Password Manager"
description: "用户自己托管服务器 + 客户端加密的密码管理器：服务器在密码学上对保险库内容完全不可见，回应主流密码管理器「保险库存在别人的服务器，所谓零知识只是声称不读数据」的隐私担忧。"
resource: "https://github.com/SoulNaturalist/zero_password_manager"
tags: ["password-manager", "self-hosted", "encryption", "privacy", "zero-knowledge", "e2ee"]
timestamp: "2026-08-12T13:45:00Z"
---

# Zero Password Manager

[Zero Password Manager](https://github.com/SoulNaturalist/zero_password_manager) 让用户**自己托管服务器**，配合客户端加密，使服务器在密码学上对保险库内容**完全不可见**——回应主流密码管理器"保险库存在别人的服务器，所谓零知识只是声称不读数据"的隐私担忧。

## 它是什么

一个自托管密码管理器，特点是：服务器只存**客户端已加密的密文**，密钥永远不出客户端。即使服务器被攻破，攻击者拿到的也只是密文。

## 为什么用它 / 适合什么场景

- **隐私第一**：保险库内容对服务器不可见。
- **自托管可控**：不必信任任何第三方密码管理服务商。
- **零知识真正落地**：不是营销话术，是密码学层面的不可见。
- **规避 SaaS 风险**：商业密码管理器一旦被攻破影响极大，自托管可降低中心化风险。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自托管 | 用户自己部署服务器 |
| 客户端加密 | 加密在客户端完成，服务器只存密文 |
| 密码学不可见 | 服务器侧无法解密保险库 |
| 回应零知识信任问题 | 真正落地而非营销宣称 |
| 适合技术用户 | 部署 + 维护需自行负责 |

## 参考链接

- [项目仓库](https://github.com/SoulNaturalist/zero_password_manager)

## 相关概念

- [Simplelogin](./tool-simplelogin.md) — 邮箱别名服务，同属隐私优先的账号保护层
- [Apple Hide My Email](./term-apple-hide-my-email.md) — Apple 的隐藏邮箱方案