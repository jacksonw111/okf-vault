---
type: "Tool"
title: "authentik（开源身份认证平台）"
description: "开源身份认证平台，OAuth2/OIDC、SAML、LDAP、RADIUS 都支持，MFA 和权限策略也能直接在 Web 界面配置。部署后自带统一门户，Docker Compose 几分钟跑起来。"
resource: "https://github.com/goauthentik/authentik"
tags: "[sso, oauth, oidc, saml, ldap, radius, identity-provider, self-hosted]"
timestamp: "2026-09-13T08:57:00Z"
---

# authentik（开源身份认证平台）

## 它是什么

[goauthentik/authentik](https://github.com/goauthentik/authentik) 是一个**开源身份认证平台**：把企业 SSO 要的协议（OAuth2 / OIDC / SAML / LDAP / RADIUS）一次性打包，MFA 与权限策略直接在 Web 界面配置。**自托管 + Docker Compose 几分钟跑起来**，自带统一门户（一个入口聚合所有内部服务）。

## 为什么用它 / 适合什么场景

- 公司要 SSO，不想交几万刀授权费。
- 内部服务越来越杂，需要**一个统一门户**收口。
- 想用统一标准（OAuth2 / OIDC / SAML）而不是每个产品自建。
- 部署周期以天计 / 以小时计，**不想为上线做重活**。

## 关键能力

| 能力 | 说明 |
|------|------|
| OAuth2 / OIDC | 标准授权 + 现代身份 |
| SAML | 兼容老旧企业 IdP |
| LDAP / RADIUS | 给遗留基础设施用 |
| MFA | Web 界面配置策略 |
| 权限策略 | 直接在 Web UI 写规则 |
| 统一门户 | 部署后自带一个入口聚合服务 |
| Docker Compose 一键部署 | 几分钟起步 |

## 项目链接

- 仓库：<https://github.com/goauthentik/authentik>

## 相关概念

- [OAuth2](https://oauth.net/2/) / [OIDC](https://openid.net/connect/) / [SAML](https://en.wikipedia.org/wiki/SAML) — authentik 实现的标准协议（项目未在 concepts 收录，留官方链接）
- [Self-Hosted（自托管）](./term-self-hosted.md) — authentik 是这一类的典型项目