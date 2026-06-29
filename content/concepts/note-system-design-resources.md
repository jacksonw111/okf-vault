---
type: Note
title: "Top 10 系统设计资源清单"
description: "开发者社区广为流传的系统设计十本经典与十种资源汇总：DDIA、SRE、Kleppmann、Alex Xu、Jepsen 等。"
resource: "https://x.com/0xlelouch_/status/2071095706845143222"
tags: "[system-design, reading-list, architecture, distributed-systems]"
timestamp: "2026-06-29T16:00:00Z"
---

# Top 10 系统设计资源清单

## 它是什么
开发者社区长期流传的一份「Top 10 系统设计资源」清单，覆盖书 / 官方文档 / 实战博客 / 复盘平台四类：Designing Data-Intensive Applications、Software Architecture: The Hard Parts、Google SRE、System Design Interview、Designing Distributed Systems、AWS Well-Architected Framework、Martin Fowler's blog、High Scalability、Jepsen analyses，以及「搭个 mini SaaS 自己跑通」这个动手练习。

## 为什么读这份清单
- **想在系统设计上从「会用框架」跨到「懂权衡」**：DDIA 讲 logs vs DBs / 一致性 / 流处理；Hard Parts 讲怎么选而不是只讲 pattern；SRE 把 SLI/SLO / 错误预算 / 事故响应 / 容量规划整成体系。
- **面试压力下要快速练习**：Alex Xu 的《System Design Interview》提供速成套路：API、存储、缓存、分片在时间压力下怎么画。
- **在 Kubernetes 之外理解分布式系统**：Brendan Burns 把 K8s 模式抽象成通用分布式系统构件。
- **不绑定云厂商**：AWS Well-Architected 的可靠性 / 安全 / 成本清单在 on-prem 同样适用。
- **学习真实事故**：High Scalability 的拆解帖、Jepsen 的 3 AM 失败模式（脑裂、脏读、错误重试）。
- **架构演进视角**：Martin Fowler 关于 bounded context、evolutionary architecture、integration patterns 的文章。
- **最后是动手**：搭一个 mini SaaS，REST + DB → 加 Redis 缓存 → 异步任务 → 指标 / 链路 → 压测 → chaos / 故障注入「打碎它」。

## 清单速览
| # | 资源 | 强项 |
|---|------|------|
| 1 | Designing Data-Intensive Applications (Kleppmann) | 真实权衡：logs vs DBs、一致性、流处理 |
| 2 | Software Architecture: The Hard Parts (Ford/Richards) | 怎么选，不只讲 pattern；模块化 / 耦合 |
| 3 | Site Reliability Engineering (Google) | SLI/SLO / 错误预算 / 事故响应 / 容量规划 |
| 4 | System Design Interview (Alex Xu) | 速成套路：API / 存储 / 缓存 / 分片 |
| 5 | Designing Distributed Systems (Brendan Burns) | K8s 模式抽象成通用分布式构件 |
| 6 | AWS Well-Architected Framework | 可靠性 / 安全 / 成本清单（on-prem 也适用） |
| 7 | Martin Fowler 架构文章 | bounded context / 演进式架构 / 集成模式 |
| 8 | High Scalability blog | 拆解帖：生产里为何选队列 / 缓存 / DB |
| 9 | Jepsen analyses | 3 AM 失败模式：脑裂、脏读、错误重试 |
| 10 | 动手练习：搭 mini SaaS | REST+DB → Redis → 异步任务 → 指标 → chaos |

## 参考链接
- [原始链接](https://x.com/Wen_Zw/status/2071351477579252062)
- [来源原帖](https://x.com/0xlelouch_/status/2071095706845143222)

## 相关概念
- [后端面试开放式问题清单](./tool-backend-interview-questions.md) — 另一份无标准答案的开放清单，适合与技术对话引子配套
- [Jepsen 在 OKF 中的间接对应：DataBuff](./tool-databuff.md) — 国产 AI Native OpenTelemetry APM，可作为清单第 10 项「指标 / 链路 / 故障注入」的中文实现参考