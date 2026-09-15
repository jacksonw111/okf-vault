---
type: "Tool"
title: "WeKnora（腾讯开源企业级 LLM 知识平台）"
description: "Tencent/WeKnora：把散落原始文档变成可检索的 RAG 问答、能自主执行多步任务的 ReAct Agent 和自动维护的 Wiki；支持 PDF/Word/图片/Excel/XMind 等 10 余种格式，从飞书/GitLab/Notion/语雀等平台自动同步，兼容 OpenAI/DeepSeek/Qwen 等主流模型。"
resource: "https://github.com/Tencent/WeKnora"
tags: "[rag, llm, knowledge-base, agent, react, wiki, tencent]"
timestamp: "2026-09-15T14:30:00Z"
---

# WeKnora（腾讯开源企业级 LLM 知识平台）

## 它是什么

[WeKnora](https://github.com/Tencent/WeKnora) 是腾讯开源的 LLM 知识库框架。它把企业里散落的原始文档**沉淀为三种知识资产**：

1. **可问答的 RAG 知识库**
2. **可自主推理的 ReAct Agent**
3. **可持续演进的自动 Wiki**

背后是腾讯微信对话开放平台的核心技术框架，有真实生产背书。

## 三大核心能力

### 1. RAG 快速问答

| 项 | 说明 |
|----|----|
| 检索策略 | BM25 稀疏检索 + 稠密向量 + GraphRAG + 父子分块，可组合 |
| 向量层 | 默认 pgvector（HNSW，1024 维），可切到 8 种向量库做多库扇出检索 |
| 问答体验 | 引用溯源 + 引用气泡 + 建议问题 |
| 效果评测 | 内置召回命中率 + BLEU/ROUGE 的 E2E 评测工具（同类少见） |

### 2. ReAct Agent 智能推理

- 自主编排知识检索、MCP 工具、网络搜索（11 家搜索源）、租户技能目录
- v0.8 起**会话级持久沙箱**（Docker / E2B / Cube 三种后端）；v0.8 移除了本地宿主进程后端，安全更收紧
- **跨会话长期记忆**（画像 / 偏好 / 事实 / 任务 / 兴趣 五类，自动抽取 + 用户确认）

### 3. Wiki 模式（差异化）

- Agent 自动把文档蒸馏成**相互链接的 Markdown 知识库**
- 配可视化知识图谱、手动编辑、版本历史、一键回滚
- 官方称可支撑 **4 万文档级**知识库
- 大多数 RAG 项目止步于「问答」，WeKnora 额外给出「**知识再生产**」的输出形态——知识库不只是被查，而是被持续整理成结构化资产

## 企业级能力

| 能力 | 说明 |
|------|------|
| 多租户 + RBAC | 四级（Owner / Admin / Contributor / Viewer），按 KB ownership 隔离 |
| 审计日志 | 租户级审计 |
| API Key | 一等主体，可限定作用域的密钥 + principal 模型，适合 headless / CI |
| 安全 | AES-256-GCM 凭据、gRPC/Redis TLS、SSRF 加固 HTTP 客户端、OIDC JWKS 校验、沙箱隔离 |
| 知识库工程化 | 分块可编辑、逐版本 diff + 回滚、自动重索引、自动打标、批量重解析 |

## 文档来源与多模态

- 文档格式：PDF / Word / 图片 / Excel / XMind 等 **10 余种**
- 自动同步平台：飞书 / GitLab / Notion / 语雀 / 钉钉 / 企微 / RSS
- 模型兼容：OpenAI / DeepSeek / Qwen 等主流模型

## 为什么用它

- 想找**带「自动 Wiki」产物**的 RAG，而不是「只会回答」的检索增强。
- 多租户 + RBAC + 审计 + 沙箱：**对企业内网部署足够严肃**。
- 检索策略、向量库、评测工具**没有藏着掖着**——可视化、可切换、可度量。

## 媒体

![](https://pbs.twimg.com/media/HSOKj7EaoAAq_cQ.jpg)

## 项目链接

- 仓库：<https://github.com/Tencent/WeKnora>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — 多源同步的「技能目录」是 ReAct Agent 的执行层
- [RAG（检索增强生成）](term-rag.md) — WeKnora 的核心范式之一
- [Sandbox（沙箱）](term-sandbox.md) — WeKnora v0.8 收紧为 Docker/E2B/Cube 三种沙箱后端
- [Multi-Agent（多智能体协作）](term-multi-agent.md) — Agent 可调度 MCP 工具 / 搜索 / 沙箱 / 记忆等多组件