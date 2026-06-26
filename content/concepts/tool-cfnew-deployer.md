---
type: Tool
title: "cfnew-deployer（Cloudflare Pages / Worker 一键部署面板）"
description: "可直接部署到 Cloudflare Pages 的部署器面板：用户填邮箱和 Global API Key，自动拉取账户信息、生成随机项目名与 UUID、创建/复用 KV 并绑定，支持 Worker 和 Pages 部署、自定义域名、远程仓库实时拉取。"
resource: "https://github.com/byJoey/cfnew-deployer"
tags: [cloudflare, pages, worker, deploy, devops, paas]
timestamp: 2026-06-26T16:50:00Z
---

# cfnew-deployer

## 它是什么

cfnew-deployer 是一个**面向 Cloudflare 用户的轻量级部署面板**，目标是"任何人都能一键把代码跑在 Cloudflare 上"，无需手动开通 Pages / Workers / KV / 域名绑定。

它本身可以部署到 Cloudflare Pages（自举），用户访问后：

1. 填一个 Cloudflare 邮箱 + Global API Key
2. 面板自动调用 Cloudflare API 拉取账户信息（账号 ID、已有 KV 等）
3. 自动生成随机项目名 + UUID（避免重名冲突）
4. 复用或新建 KV，并自动绑定
5. 选 Worker / Pages 二选一部署，**代码从远程仓库实时拉取**
6. 可选绑定自定义域名

## 为什么用它

| 痛点 | cfnew-deployer 解法 |
|------|---------------------|
| 第一次用 Cloudflare 不知道从哪点 | 一个表单搞定 |
| 每次开新项目要手动建 Worker / KV / 域名 | 全自动 |
| 项目名冲突 | 随机生成 + UUID |
| 部署脚本要写 | 远程仓库直接拉取，UI 上点 |
| 部署面板自己怎么部署 | 部署面板自己也能跑在 Cloudflare Pages 上（自举） |

## 关键能力

| 能力 | 说明 |
|------|------|
| 自托管 | 面板本身部署在 Cloudflare Pages |
| 自动建项目 | 随机项目名 + UUID，避免命名冲突 |
| KV 复用 | 自动检测已存在的 KV 并绑定，避免冗余 |
| 双形态 | 支持 Worker（轻函数）和 Pages（静态 + Functions） |
| 域名绑定 | 可选自定义域名 |
| 实时同步 | 代码从远程仓库直接拉取，UI 上点一下就更新 |

## 原始链接

- [项目仓库](https://github.com/byJoey/cfnew-deployer)
- [原始推文剪藏](https://x.com/QingQ77/status/2070325170926178455)

## 相关概念

- [Single Server](./tool-single-server.md) — 类似"一站式部署"思路，但走 Cloudflare + Tailscale + Docker + Kamal 的自建链
- [OPG](./tool-opg-backend.md) — 一人公司多 app 后端控制面，比 cfnew-deployer 通用但同样强调"少写部署脚本"
- [DevSpace MCP](./tool-devspace-mcp.md) — 自托管 MCP 编程工作台，把 ChatGPT 变 Codex CLI，部署流程也常跑在 Cloudflare 上
