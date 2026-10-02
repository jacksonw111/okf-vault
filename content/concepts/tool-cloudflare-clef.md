---
type: "Tool"
title: "Cloudflare Clef & Clef-flash（Workers AI 上的开源决策模型）"
description: "Cloudflare 在 BirthdayWeek 发布的两个开源决策模型：Clef 是主力分类 / agentic workflow 模型，Clef-flash 是它的轻量极速版——都托管在 Workers AI 上，按推理调用计费，适合边缘高吞吐分类 / 路由 / 守门场景。"
resource: "https://blog.cloudflare.com/cloudflare-clef-and-clef-flash"
tags: "[cloudflare, workers-ai, classification, decision-model, agent, edge, open-source]"
timestamp: "2026-10-01T22:55:00Z"
---

# Cloudflare Clef & Clef-flash（Workers AI 上的开源决策模型）

## 它是什么

[Clef](https://blog.cloudflare.com/cloudflare-clef-and-clef-flash) 是 Cloudflare 在 2026 BirthdayWeek 发布的**两个开源决策模型**：

- **Clef**——主力分类 / agentic workflow 决策模型
- **Clef-flash**——Clef 的轻量极速版，专为高吞吐、低延迟场景

两者都托管在 **Workers AI** 上，开发者按推理调用计费，无需自托管 GPU。

## 为什么用它 / 适合什么场景

| 场景 | 用哪个 | 为什么 |
|------|--------|--------|
| 用户意图路由（聊天机器人 / agent 入口） | Clef | 多意图分类 + 鲁棒 |
| 工单 / 邮件 / 反馈分类 | Clef | 精度优先 |
| 边缘 WAF / 垃圾 / 滥用 / 风险实时拦截 | Clef-flash | 延迟敏感，要亚十毫秒 |
| 内容守门（输入审查 / 输出审查） | Clef-flash | 极高 QPS、低延迟 |
| Agent 工具调度（上千个 tool 时挑一个） | Clef | 决策质量 > 速度 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 开源 | 模型权重开源，可自托管或走 Workers AI |
| 边缘推理 | 跑在 Cloudflare 全球边缘，无需自建 GPU |
| 双档 | 主力（Clef）+ 极速（Clef-flash），按场景挑 |
| agentic 友好 | 输出 schema 适合 agent 工具调度 |
| 治理好 | Workers AI 自带审计 / 限流 / 计费 |

## 怎么接

```ts
// Workers AI 客户端，绑定 clef 模型
import { Ai } from "@cloudflare/ai";
export default {
  async fetch(req: Request, env: Env) {
    const ai = new Ai(env.AI);
    const input = await req.text();
    const out = await ai.run("@cf/cloudflare/clef", {
      input,
      candidates: ["billing", "tech", "abuse", "other"],
    });
    return Response.json(out);
  },
};
```

## 参考链接

- 原始链接：<https://x.com/Cloudflare/status/2105747536510099540>
- 项目链接：<https://cfl.re/3Vlqb9P>

## 相关概念

- [Cloudflare Workers](./tool-cloudflare-workers.md) — 部署与运行平台
- [Workers AI](#) — Cloudflare 边缘推理服务，本仓库目前未收录
- [Cloudflare K2 Streams](./tool-cloudflare-k2-streams.md) — 同为 BirthdayWeek 发布的 serverless Kafka
- [Jev](./tool-jev-webmcp-extension.md) — 另一类决策模型，做 WebMCP 工具意图路由
