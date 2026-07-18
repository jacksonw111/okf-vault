---
type: "Tool"
title: "netflix-cicd-pipeline（AnushaJoseph-00/netflix-cicd-pipeline）"
description: "一个端到端参考工程：在 AWS 上从零搭建 CI/CD 流水线，让 Netflix 克隆应用自动跑测试、过质量门禁、打版本、上线。"
tags: "[aws, cicd, devops, pipeline, reference-project, netflix-clone]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/AnushaJoseph-00/netflix-cicd-pipeline"
---

# netflix-cicd-pipeline（AnushaJoseph-00/netflix-cicd-pipeline）

## 它是什么

[`netflix-cicd-pipeline`](https://github.com/AnushaJoseph-00/netflix-cicd-pipeline) 是一个**端到端 CI/CD 参考实现**：

- 业务侧：Netflix 克隆应用（常见的「练习用全栈 App」）；
- 工程侧：在 AWS 上从零搭一条流水线，覆盖 **测试 → 质量门禁 → 版本 → 部署**；
- 适合作为「在 AWS 上做 CI/CD」的一份「拿来即用 / 拿来即改」的样板。

## 关键能力

| 能力 | 说明 |
|------|------|
| AWS 全套 | 用 CodePipeline / CodeBuild / CodeDeploy（或等价方案）串成一条管线 |
| 自动化测试 | 提交即触发，跑单元 / 集成测试 |
| 质量门禁 | 测试未通过阻止后续阶段 |
| 版本管理 | 构建产物打 tag、归档 |
| 一键上线 | 通过门禁后自动部署到目标环境 |

## 适合什么场景

- 第一次在 AWS 上搭 CI/CD 的工程团队 / 个人开发者；
- 想给「Netflix 克隆」这种全栈 App 加工程化能力；
- DevOps 教学 / 培训场景的参考实现。

## 参考链接

- [原始链接](https://github.com/AnushaJoseph-00/netflix-cicd-pipeline)

## 相关概念

- [Monorepo 代码质量设置 Playbook](playbook-monorepo-code-quality-setup.md) — netflix-cicd-pipeline 处理「怎么把代码推上去」，Monorepo 设置处理「代码本身怎么被门禁保护」，两者在 CI 节点处交汇