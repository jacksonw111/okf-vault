---
type: "Tool"
title: "xiaohongshu-ai-workbench（nihe0909/xiaohongshu-ai-workbench）"
description: "一组配套《小红书运营手册》的免费开源 Codex Skills, 把标题、主页、选题、评论和成交路径拆成可执行的 AI 工作流。"
resource: "https://github.com/nihe0909/xiaohongshu-ai-workbench"
tags: "[xiaohongshu, codex-skills, content-creation, social-media, agent-skills]"
timestamp: "2026-07-17T12:48:00Z"
---

# xiaohongshu-ai-workbench

[xiaohongshu-ai-workbench](https://github.com/nihe0909/xiaohongshu-ai-workbench) 是一组**配套《小红书运营手册》的免费开源 Codex Skills**, 把小红书创作 / 运营拆成**可执行的工作流**, 而非只给一份 prompt 模板。

## 它解决的痛点

「我要做小红书」这件事其实是由**多个子任务**组成的:

1. 标题设计
2. 主页 banner / 简介设计
3. 选题决策
4. 评论运营 / 私信引流
5. 成交路径 (转化话术 / 私域 / 链接)

每一步单做都很碎片, 但**协同时决定数据**。本仓库把每一步打包成一个 Skill, 让 Codex 可以按工作流一气调出来。

## 五个核心 Skill

| Skill | 职责 |
|------|------|
| 标题 | 套公式 + 历史数据回看 |
| 主页 | banner 文案 + 自我介绍 + 关键词矩阵 |
| 选题 | 从领域 + 热搜 + 历史数据组合出可执行选题 |
| 评论 | 评论运营话术 / 高赞话术模板 |
| 成交 | 把流量 → 转化路径拆成可调用的子动作 |

## 与同类资源的差别

| 资源 | 形态 | 差异 |
|------|------|------|
| [xiaohongshu-assistant (薄荷工坊)](./tool-xiaohongshu-assistant.md) | 桌面 Web 工作台 (React + Vite) | 偏 GUI, 单文件生成, 多模型 / RAG |
| xiaohongshu-ai-workbench | Codex Skills 合集 | 偏 Skill 化, 把整套运营拆成可复用工作流 |

两者并不重叠——一个解决「我想要一个 GUI 助手」, 一个解决「我想在自己的 Codex 里调用一批运营 skill」。

## 参考链接

- [项目仓库](https://github.com/nihe0909/xiaohongshu-ai-workbench)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 的本质定义
- [xiaohongshu-assistant（薄荷工坊）](./tool-xiaohongshu-assistant.md) — 同主题的 GUI 工作台
- [liurun-bookwriter-skills](./tool-liurun-bookwriter-skills.md) — 同样是「中文写作风格 Skill 化」的同思路项目
