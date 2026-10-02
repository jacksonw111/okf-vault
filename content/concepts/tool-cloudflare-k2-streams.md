---
type: "Tool"
title: "Cloudflare K2 Streams（边缘 serverless Kafka 替代）"
description: "Cloudflare 发布的 serverless 流式数据产品，对标 Kafka：免运维、自动伸缩、与 Workers / R2 / Workers AI 同生态，按使用计费。在 BirthdayWeek 2026 上线。"
resource: "https://blog.cloudflare.com/cloudflare-k2-streams"
tags: "[cloudflare, kafka, streaming, serverless, edge, event-stream, workers]"
timestamp: "2026-10-02T04:00:00Z"
---

# Cloudflare K2 Streams（边缘 serverless Kafka 替代）

## 它是什么

[Cloudflare K2 Streams](https://blog.cloudflare.com/cloudflare-k2-streams) 是 Cloudflare 在 2026 BirthdayWeek 上线的**无服务器流式数据产品**，定位「Kafka 的 serverless 替代」——

- 免运维（没有 broker 要管）
- 自动伸缩（流量来即扩容）
- 与 Workers / R2 / Workers AI 同生态（同账号、同计费、同权限模型）
- 按使用计费（按消息字节 / 留存时长）

## 为什么用它 / 适合什么场景

| 场景 | 用 K2 的理由 |
|------|--------------|
| Event-driven 后端 | 传统 Kafka 自建运维成本高，K2 零运维 |
| Workers 间解耦通信 | 多个 Worker 之间用 K2 做事件总线，无需自管 broker |
| 实时数据管道 | 上游 Workers 写、下游 Worker 消费，无须外部依赖 |
| 日志 / 指标 / 审计流 | 边缘节点 → K2 → 聚合分析 |
| RAG 数据更新通知 | 文档变更事件推到 K2，触发 embedding 重算 |

## 与 Kafka 的对比

| 维度 | Kafka | K2 |
|------|-------|-----|
| 运维 | 要管 broker / ZK / 副本 | 零运维 |
| 弹性 | 提前规划分区 | 自动伸缩 |
| 计费 | 节点 + 存储 | 按消息字节 / 留存 |
| 延迟 | 毫秒级 | 同 |
| 生态 | 庞杂（Schema Registry / Connect） | Workers 原生集成 |
| 规模 | 单集群可到 PB | 单 stream 自动伸缩 |

## 典型用法（伪代码）

```ts
// producer: 一个 Worker 把事件推进 K2
export default {
  async fetch(req: Request, env: Env) {
    await env.K2.send("user-events", { payload: await req.text() });
    return new Response("ok");
  },
};

// consumer: 另一个 Worker 拉 / 订阅
export default {
  async queue(batch: MessageBatch, env: Env) {
    for (const msg of batch.messages) {
      await handle(msg.body);
      msg.ack();
    }
  },
};
```

## 参考链接

- 原始链接：<https://x.com/akazwz_/status/2105656306912883031>
- 项目链接：<https://blog.cloudflare.com/cloudflare-k2-streams>

## 相关概念

- [Cloudflare Workers](./tool-cloudflare-workers.md) — Producer / Consumer 都跑在 Workers 上
- [Cloudflare Clef & Clef-flash](./tool-cloudflare-clef.md) — 同为 BirthdayWeek 发布，可消费 K2 事件做实时决策
- [Cloudflare Durable Objects](./tool-cloudflare-durable-objects-agent.md) — 另一种「带状态」边缘运行时，与 K2 互补
