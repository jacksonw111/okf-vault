---
type: Tool
title: "Open GENAI（日本数字厅 GENAI 的本地化开源版）"
description: "把日本数字厅的政府 AI「源内（GENAI）」从 AWS 搬到本地跑的开源项目——Keycloak 替 Cognito、FastAPI 替 Lambda/Bedrock、SQLite 替 DynamoDB、Qdrant 替 OpenSearch，全栈离线可用。"
resource: "https://github.com/hirokawaguchi/open-genai"
tags: "[genai, japan, government-ai, local-first, rag, docker]"
timestamp: "2026-06-30T15:30:00Z"
---

# Open GENAI（日本数字厅 GENAI 的本地化开源版）

## 它是什么

Open GENAI 是非官方开源项目，把日本数字厅的政府 AI「源内（GENAI）」从 AWS 整套搬到本地跑，完全脱离云依赖，可在内网 / 隔离网络 / 离线环境部署。

## 关键能力

| 能力 | 原 AWS 组件 | 本地替代 |
|------|-------------|----------|
| 认证 | Cognito | Keycloak |
| API / LLM 编排 | Lambda / Bedrock | 本地 FastAPI |
| 数据库 | DynamoDB | SQLite |
| 向量检索 | OpenSearch | Qdrant |
| 语音转文字 | Transcribe | faster-whisper |
| 图像生成 | Bedrock | Stable Diffusion |
| 部署 | — | Docker Compose 一键启动 |
| LLM 后端 | — | 任意 OpenAI 兼容接口（Ollama / vLLM / LM Studio） |

## 内置功能

- RAG（基于 Qdrant 向量检索）
- 语音转文字
- 图像生成
- 团队管理
- AI 应用注册
- Dify 工作流集成

## 平台支持

- macOS Apple Silicon
- Linux + NVIDIA GPU

## 适用场景

- 政府 / 公共部门想复刻日本数字厅 GENAI 模式，又必须内网 / 离线部署。
- 学习「把 AWS 上的 AI 系统完整拆出来到本地」的实操样例。
- 需要一个开箱即用、本地能跑、含 RAG + TTS + 图像生成的 AI 中台。

## 相关概念

- [Floci](./tool-floci.md) — LocalStack 的免费开源替代，本地 AWS 模拟器
- [OPG](./tool-opg-backend.md) — 一人公司多 app 后端控制面
- [CasaOS](./tool-casaos.md) — 个人云 OS，10 万+ Docker 镜像一键装
- [llmaker](./tool-llmaker.md) — Go 写的私有 LLM 应用栈编排器

## 参考链接

- 项目链接：<https://github.com/hirokawaguchi/open-genai>