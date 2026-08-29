---
type: Tool
title: "decionis/docker（Docker 内的 AI 代理确定性执行授权边界）"
description: "为 Docker 容器内的 AI 代理 / 自动化工作流加一层确定性执行授权边界——敏感操作在执行前必须先经过策略评估与可验证的人类审批。"
resource: "https://github.com/decionis/docker"
tags: [docker, ai-agent, authorization, policy, human-in-the-loop, sandbox]
timestamp: "2026-08-29T21:30:00Z"
---

# decionis/docker（Docker 内的 AI 代理确定性执行授权边界）

## 它是什么

[decionis/docker](https://github.com/decionis/docker) 是为**运行在容器内的 AI 代理与自动化工作流**引入的**确定性执行授权边界**：在敏感操作真正落到 host / 数据库 / 外部 API 之前，先经过策略评估，并等待**可验证的人类审批**通过。

与一般的「agent 自己决定要不要执行」不同——它把「能不能执行」的判断从 agent 内部决策变成**外部边界强制**：

- 预设策略（policy）描述什么算敏感、写操作要不要二次确认；
- 执行前必须命中策略的请求被拦截，交给人审批；
- 审批链可验证、可回溯，不只是「人点了同意」。

## 为什么用它 / 适合什么场景

- 在生产环境跑 agent / Claude Code / 自动脚本，担心误删数据 / 误发邮件 / 误操作资金；
- 想给 agent「**能跑、但不能乱跑**」的环境，但又要保留自动化的速度；
- 合规 / 审计需要「敏感操作前有人点头」的可追溯记录；
- 把多 agent 系统放进 Docker，希望统一管控而不是每个 agent 自己一套规则。

## 关键能力

| 能力 | 说明 |
|------|------|
| 策略评估 | 敏感操作在执行前走 policy 引擎 |
| 人类审批 | 必须由可验证的人确认才放行 |
| 容器边界 | 在 Docker 出口处拦截，agent 改不了 |
| 审计回溯 | 每一次授权 / 拦截都留下记录 |
| 确定性 | 不是「agent 自己判断」，是「边界强制」 |

## 相关概念

- [docker_images_sync](./tool-docker-images-sync.md) — 借 GitHub Actions 同步海外 Docker 镜像，处理的是镜像可访问性；decionis/docker 处理的是容器内执行授权
- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent，部署到 Docker 后用此工具加一层执行闸门

## 参考链接

- 项目链接：<https://github.com/decionis/docker>
- 原始推文：<https://x.com/QingQ77/status/2093538882063303043>
- 媒体：<https://pbs.twimg.com/media/HQxnPq-aUAAM6NE.jpg>