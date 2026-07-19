---
type: Tool
title: "FORGE Framework（lava-security-research）"
description: "面向 AI 数据中心与基础设施的安全风险框架，列出最关键的 10 类基础设施层安全失效模式，帮助供给方与用户识别、排序并整改底层算力环境的安全风险。"
resource: "https://github.com/lava-security-research/forge-framework"
tags: "[security, ai-infrastructure, risk-framework, datacenter, threat-modeling]"
timestamp: "2026-07-19T12:46:00Z"
---

# FORGE Framework（lava-security-research）

## 它是什么

lava-security-research/forge-framework 是一个**面向 AI 数据中心与基础设施**的安全风险评估框架，聚焦于**基础设施层**（而非模型 / 应用层）的失效模式。它把 AI 算力环境的风险按**五个评估域**分门别类，再据此排出十大风险，每条都给出严重度、可能性、影响、检测难度等评估维度。

## 五个评估域

| 评估域 | 范围 |
|--------|------|
| 机队完整性 | 硬件固件 / 启动链路 / 物理防篡改 |
| 运维管理平面 | 带外管理 / 远程运维通道 / 控制面访问 |
| 资源隔离 | 多租户边界 / 显存 / 网络命名空间 |
| 网格网络设施 | 训练 / 推理集群网络互联 / RDMA / 拓扑泄露 |
| 证据与暴露管理 | 日志 / 审计 / 外部暴露面 / 补丁节奏 |

## 十大风险覆盖范围

从硬件固件、网络互联、多租户隔离、带外管理面，到供应链、补丁节奏——**每条都给出风险描述 + 影响评估 + 检测建议**，帮供给方（算力提供方）与用户（模型部署方）建立共同的「基础设施层红队清单」。

## 适合谁

- AI 算力 / 智算中心的安全负责人，需要标准化风险评估表
- 模型部署方在选型时评估供应商基础设施安全水位
- 安全研究 / 蓝队为 AI 算力环境做 Threat Modeling

## 与已有安全工具的差别

- [Strix](./tool-strix.md) — 自主 AI 渗透测试 agent（针对应用层）
- [bot-signal](./tool-bot-signal.md) — 全套机器人检测（针对访问层）
- [Synapse CE](./tool-synapse-ce.md) — SCA + 侦察 + 证据 + 报告的治理控制平面（针对软件供应链）
- FORGE 的差异点：**唯一聚焦「AI 基础设施层」安全失效**，是 Strix / bot-signal 都不覆盖的层

## 媒体预览

![](https://pbs.twimg.com/media/HNbj9UCbgAA2ARp.jpg)

## 相关概念

- [Strix](./tool-strix.md) — 自主 AI 渗透测试 agent
- [Synapse CE](./tool-synapse-ce.md) — 安全治理控制平面

## 参考链接

- 项目链接: <https://github.com/lava-security-research/forge-framework>