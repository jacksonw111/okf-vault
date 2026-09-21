---
type: "Tool"
title: "humanizer（blader 通用 AI 写作痕迹清洗 skill）"
description: "一个纯 Markdown 的 agent skill，任何支持 skills 的 agent 都能装，`npx skills add blader/humanizer --global` 一行安装。以 25 条 AI 写作特征为检查表，条号按辨识强度排序，前五条单次出现即可判定。"
resource: "https://github.com/blader/humanizer"
tags: "[humanizer, agent-skill, markdown, ai-writing, editing]"
timestamp: "2026-09-21T22:00:00Z"
---

# humanizer（blader）

## 它是什么

[blader/humanizer](https://github.com/blader/humanizer) 是一个**纯 Markdown 的 agent skill**，专门把**模型味儿的文字改成正常人说话的口气**，**事实一个不动**。

## 安装

```bash
npx skills add blader/humanizer --global
```

任何**支持 skills 的 agent**都能装——靠的是 npx skills 注册机制，不是具体某个 agent 的私有扩展。

## 25 条 AI 写作特征检查表

按**辨识强度 + 使用频率**排序。**前五条**单次出现即可判定为 AI 写：

| # | 特征 |
|---|------|
| 1 | Not X but Y 对比句 |
| 2 | 每节末尾的「金句」 |
| 3 | 听着深刻的格言 |
| 4 | 进正题前的铺垫 |
| 5 | 对着没人提出的反对意见辩论 |
| … | … |
| 25 | 标注 `weak alone` 的几条须一段内同时命中多条才算 |

## 为什么用它 / 适合什么场景

- 公众号 / 知乎 / Twitter 写完一段**想脱掉 AI 味**。
- 想让 agent 边写边自查，**不需要人肉 review**。
- 已经有 `npx skills` 工作流，新加一条 skill 一行命令搞定。

## 关键能力

| 能力 | 说明 |
|------|------|
| 25 条检查表 | 按强度排序，强项单次命中即判 |
| Markdown 形态 | 可直接读 / 可注入 prompt |
| 不动事实 | 只改表达层 |
| 跨 agent | 装在能跑 skills 的 agent 上都能用 |

## 项目链接

- 仓库：<https://github.com/blader/humanizer>

## 相关概念

- [humanizer-cli (0xwilliamortiz)](./tool-humanizer-cli.md) — 33 条 AI 写作痕迹的离线终端版
- [AI Humanizer Handbook](./tool-ai-humanizer-handbook.md) — 系统化 AI 去痕方法论
- [academic-humanizer](./tool-academic-humanizer.md) — 同思路但专为学术论文设计的清洗工具
