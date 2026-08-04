---
type: "Tool"
title: "humanizer-cli (0xwilliamortiz)"
description: "把 Wikipedia《Signs of AI writing》整理的 33 种 AI 写作痕迹做成终端里的离线参考与草稿检查工具——每条都带前后对比例子，支持 patterns、show、search、check、prompt 等命令，数据固化到 SKILL.md，号称「无网络、无 Key、零依赖」编译产物。"
resource: "https://github.com/0xwilliamortiz/humanizer-cli"
tags: "[ai-writing, humanizer, cli, offline, no-network, skill, writing-quality]"
timestamp: "2026-08-04T20:30:00Z"
---

# humanizer-cli (0xwilliamortiz)

## 它是什么

[humanizer-cli](https://github.com/0xwilliamortiz/humanizer-cli) 把 Wikipedia《**Signs of AI writing**》整理的 **33 种 AI 写作痕迹**做成终端里的**离线参考与草稿检查工具**。

- **数据源**：blader 的 humanizer skill + Wikipedia 的 AI 清理记录
- **存储**：数据固化到同目录的 `SKILL.md`
- **零依赖**：无网络、无 Key、零依赖的编译产物
- **额外入口**：`npx` 交互界面

![humanizer-cli 截图](https://pbs.twimg.com/media/HOw1MzPaEAAOq-e.png)

## 为什么用它 / 适合什么场景

- **去 AI 味**：检查自己 / 别人写的文字里有没有 AI 套路。
- **离线可用**：内嵌 33 条痕迹数据，不联网也能跑。
- **可挂技能**：直接喂给 LLM，让模型边写边自查。
- **教学价值**：每条痕迹都带前后对比例子。

## 命令

| 命令 | 干什么 |
|------|--------|
| `patterns` | 列出全部 33 种 AI 写作痕迹 |
| `show` | 展示指定痕迹的详情 + 前后对比 |
| `search` | 按关键词搜痕迹 |
| `check` | 检查一份草稿里出现的痕迹 |
| `prompt` | 把痕迹清单导出成可喂给 LLM 的 prompt |

## 关键能力

| 能力 | 说明 |
|------|------|
| 33 条 AI 写作痕迹 | 来自 Wikipedia《Signs of AI writing》 |
| 前后对比 | 每条都带改前 / 改后例子 |
| 草稿检查 | 直接对一篇文章做痕迹扫描 |
| SKILL.md 固化 | 数据和工具同目录打包，可整目录喂给 agent |
| 零依赖 | 无网络、无 Key、不需要 Node 运行时之外的依赖 |

## 参考链接

- [项目仓库](https://github.com/0xwilliamortiz/humanizer-cli)

## 相关概念

- [Stop Slop](./tool-stop-slop.md) — 同样为 LLM 去 AI 腔的技能包，结构上更细化到评分维度
- [No Slop 中文版](./tool-no-slop-zh.md) — 中文场景的「去 AI 腔」规则
- [AI Humanizer Handbook](./tool-ai-humanizer-handbook.md) — 系统化的 AI 去痕方法论
