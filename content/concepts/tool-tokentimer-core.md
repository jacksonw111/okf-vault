---
type: Tool
title: "TokenTimer"
description: "把证书、密钥、许可证等会过期的东西收进一个自托管面板统一看管，到期前多渠道报警，证书自动续期。"
resource: "https://github.com/tokentimerch/tokentimer-core"
tags: [certificate, expiration, monitoring, self-hosted, acme, alert]
timestamp: "2026-08-25T19:30:00Z"
---

# TokenTimer

## 它是什么

[tokentimerch/tokentimer-core](https://github.com/tokentimerch/tokentimer-core) 是给**所有「会过期的东西」**做集中看护的自托管面板。它盯的对象不止 HTTPS 证书，还包括 API key、SSH key、license、订阅、token、密码轮换周期等。

- **到期前多渠道报警**：邮件 / IM / webhook 等。
- **证书自动续期**：对接 ACME（Let's Encrypt / 自建 CA）自动跑续签。

![](https://pbs.twimg.com/media/HQfDWcWaUAARurf.png)

## 为什么用它 / 适合什么场景

- **证书 / 密钥 / 许可证过期导致的故障是常见事**：没人盯、责任不清、续期全靠手动。
- **多渠道报警**：到期前 N 天推送，避免单一通道漏掉。
- **证书自动续好**：HTTPS 证书到点自动续，省掉运维半夜被叫醒。
- **想给团队做集中治理**：自托管面板，所有人看同一份到期表。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多对象监控 | HTTPS 证书 / API key / SSH key / license / 订阅等 |
| 到期预警 | 到期前多渠道报警（邮件 / IM / webhook） |
| 证书自动续期 | 对接 ACME 自动续 HTTPS 证书 |
| 自托管面板 | 数据留在自己服务器 |
| 责任清单 | 给每个对象分配 owner / 团队，避免「没人盯」 |
| 历史审计 | 续期 / 报警 / 替换记录可追溯 |

## 相关概念

- [Lucky](./tool-lucky.md) — 自托管 Swiss Army knife：DDNS + ACME + 反代，可与 TokenTimer 联动
- [Self-hosted Backup](./note-self-hosted-backup.md) — 自托管生态基础

## 参考链接

- 项目链接: <https://github.com/tokentimerch/tokentimer-core>
- 原始链接: <https://x.com/QingQ77/status/2092232776107880473>