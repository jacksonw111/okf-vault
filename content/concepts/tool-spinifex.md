---
type: Tool
title: "Spinifex (mulgadc/spinifex)"
description: "AWS API 兼容的开源私有云平台，在裸机/边缘站点复刻 EC2 / EBS / S3 / VPC / IAM 等 AWS 服务面，让现有 AWS 应用零代码改动部署到自有硬件"
resource: "https://github.com/mulgadc/spinifex"
tags: [aws, cloud, open-source, bare-metal, s3, ec2, sigv4, nats, agpl]
timestamp: 2026-08-20T04:31:00Z
---

# Spinifex (mulgadc/spinifex)

## 它是什么
[`mulgadc/spinifex`](https://github.com/mulgadc/spinifex) 是 Mulga 公司开源（AGPL-3.0）的 **AWS API 兼容私有云**：在裸机、边缘站点或私有数据中心复刻 AWS 的 **EC2 / EBS / S3 / VPC / IAM** 等核心服务面。**已有的 AWS CLI、SDK、Terraform 代码无需任何改动**，只要把 endpoint 指向 Spinifex 就能直接跑起来——内置 **ALB / NLB、EKS、ECR、ECS、RDS** 等一整套配套。

## 为什么用它 / 适合什么场景
- 想把工作负载从 AWS 迁到自有机房 / 边缘节点，但不希望重写 Terraform / boto3 代码。
- 边缘 / 离线场景需要"还能跑 AWS 风格 API"的替代品。
- 想替换掉 OpenStack / Kubernetes 这种重控制面，希望网关 → NATS → 无状态守护进程的极简架构。
- 需要全部组件能脱离 etcd / Kubernetes 在断网环境下正常工作。

## 关键能力
| 能力 | 说明 |
|------|------|
| AWS API 兼容 | EC2 / EBS / S3 / VPC / IAM / ALB / NLB / EKS / ECR / ECS / RDS 等 |
| 零代码迁移 | 现有 CLI / SDK / Terraform 直连即用 |
| 极简架构 | API 网关（SigV4 认证） → NATS 总线 → 无状态守护进程 |
| 无外部控制面 | 不依赖 etcd / Kubernetes，断网也能跑 |
| AGPL-3.0 开源 | 商业可用性强、修改需公开 |

## 架构示意（文字版）
```
[AWS SDK / CLI / Terraform]
            │ SigV4
            ▼
┌──────────────────────────┐
│      API Gateway          │
└──────────┬───────────────┘
           │
           ▼
      ┌─────────┐
      │  NATS   │ ◀── 消息总线
      └────┬────┘
           │
   ┌───────┼───────┬────────┐
   ▼       ▼       ▼        ▼
EC2守护  S3守护  EBS守护  IAM守护 …（均无状态）
```

## 媒体
- ![Spinifex 控制台](https://pbs.twimg.com/media/HP_cOpFbsAAJh-b.jpg)
- ![Spinifex 拓扑](https://pbs.twimg.com/media/HP_caXYasAA0VXU.jpg)

## 相关概念
- [项目仓库](https://github.com/mulgadc/spinifex) — 仓库主页
- [note-cloud-agent-infrastructure](./note-cloud-agent-infrastructure.md) — 关于 AI 时代云基础设施的笔记，可对照阅读
