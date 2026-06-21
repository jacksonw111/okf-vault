---
type: "Tool"
title: "Niamos（Obsidian 第二大脑模板）"
description: "pricklywiggles 开源的「开箱即用」Obsidian 第二大脑模板，基于改良版 PARA 方法，把文件夹结构、模板、查询脚本、Claude Code 自动化打包成一套可直接复用的系统。"
tags: "[obsidian, para, second-brain, claude-code, template]"
timestamp: "2026-06-20T00:00:00Z"
resource: "https://github.com/pricklywiggles/niamos"
---

# Niamos

## 它是什么

[`Niamos`](https://github.com/pricklywiggles/niamos) 是一套**完整的 Obsidian 第二大脑模板**：基于改良版 PARA 方法，把 Obsidian 知识库的**文件夹结构、模板、查询脚本、Claude Code 自动化**整理成一套可直接复用、开箱即用的系统。

> 一句话：别人要花一周配的东西，`git clone` 一下就齐了。

## 改良版 PARA 是什么

经典 PARA（Tiago Forte）= **Projects / Areas / Resources / Archive** 四类文件夹按「行动紧迫度」分。Niamos 的改良主要是：

| 改进点 | 经典 PARA | Niamos 改良 |
|--------|----------|------------|
| 文件夹结构 | 仅 4 类 | 在 PARA 之上加可挂载的「视图层」（Dashboard / Inbox 视图） |
| 模板 | 留空 | 预置多个 type 模板（daily / project / note / meeting） |
| 查询 | 用户自配 Dataview | 预置常用查询脚本（按 type、按 tag、按 project 进度） |
| 自动化 | 无 | 接 Claude Code：定期整理 inbox、补 frontmatter、跨笔记链接 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 预置 PARA 结构 | `0-Inbox / 1-Projects / 2-Areas / 3-Resources / 4-Archive` + 索引页 |
| 模板库 | 多份开箱即用模板（daily-note / project / meeting / resource） |
| Dataview 查询 | 预置脚本：本周到期 / 停滞项目 / 最近笔记 / 按 tag 聚合 |
| Claude Code 集成 | agent 跑例行整理（inbox 归类 / frontmatter 校验 / 断链修复） |
| 渐进式定制 | 结构先到位，模板可改、查询可删；不会因为「配环境」卡住 |

## 为什么这个思路重要

Obsidian 的「上手摩擦」一直存在：新人装完要建结构、配模板、装插件、写查询。Niamos 把这套**基础设施层**做成了仓库本身，绕开了「学习 Obsidian」这一关。

这与 [OKF](../index.md) 的「一个目录 = 一份知识」哲学同源——但 Niamos 是**一个能直接 fork 使用的具体实例**，对想跳过"从零搭知识库"的用户价值巨大。

## 怎么用

```bash
git clone https://github.com/pricklywiggles/niamos
# 在 Obsidian 里「Open folder as vault」指向这个目录
# 启动 Claude Code（已预置 slash commands）→ 自动跑首次整理
```

## 媒体

项目截图：

![Niamos 模板预览](https://pbs.twimg.com/media/HLLMvHiaAAE_7VH.jpg)

## 相关概念

- [Obsidian](tool-obsidian.md) — Niamos 的宿主编辑器
- [Claude Code](tool-claude-code.md) — Niamos 集成进来的 agent 客户端
- [在 Obsidian 里开始用 OKF](playbook-okf-obsidian-start.md) — 另一条从零起步的路径（更轻量、贴近本知识库的 OKF 协议）
- [OKF 是什么](term-okf.md) — Niamos 的「目录即知识库」思想同 OKF
