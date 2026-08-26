---
type: "Tool"
title: "Apodex 1.1 + FrontierAgent（科研向推理核查多 Agent 框架）"
description: "ApodexAI 出品的科研场景专业 Agent 1.1 版本：先核查用户输入事实 → 启动子 Agent 并行收集数据 → 交叉验证 → 撰写报告 → 终审验证；同步开源 35B 本地模型 Apodex 1.1 mini 与 Agent 框架 FrontierAgent。"
tags: "[agent, scientific-research, fact-check, multi-agent, open-source, huggingface]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://www.apodex.ai/"
---

# Apodex 1.1 + FrontierAgent

## 它是什么

[Apodex 1.1](https://www.apodex.ai/) 是 **ApodexAI** 出品的「面向复杂科研任务」的专业 Agent——区别于「传统 Deep Research 只搜资料出报告」，它把 **推理与核查** 应用在**整个任务过程**：

1. **核查用户输入事实**——例如先校验「Moderna 与默沙东联合研发的癌症疫苗临床取得成功」这条用户断言是否真实；
2. **启动子 Agent 并行收集数据 + 写子报告**——例如同时预测生物医药 × AI 机会、突破点、相关股票；
3. **交叉验证子报告**——互相检查，避免子 Agent 之间结论相互打架；
4. **撰写最终报告**——汇总成单一文档；
5. **终审验证**——最后一道独立评审通过才交付。

整个质疑 / 核查环节始终贯穿，降低幻觉，专门为科研场景优化。

## 同时开源的两块

- **[FrontierAgent](https://github.com/ApodexAI/FrontierAgent)**（Agent 框架）——GitHub 上 star 即可用；
- **[Apodex 1.1 mini](https://huggingface.co/collections/apodex/apodex-11)**（35B 本地模型）——可搭配 FrontierAgent 跑本地部署。

## 为什么用它 / 适合什么场景

- **需要可核查链路**的科研 / 投研 / 政策研究——交付物必须附证据链；
- **想用本地模型跑科研辅助**——避免把研究数据传到闭源服务；
- **多子任务并行 + 交叉验证**——比单 Agent 串联更适合「同一主题下多个互相关联的子问题」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 用户输入事实核查 | 起始必走 |
| 子 Agent 并行 | 多子任务同时启动 |
| 交叉验证 | 子 Agent 输出互相校验 |
| 终审 | 最终报告独立再过一遍 |
| 35B 本地模型 | 可与 FrontierAgent 搭配本地部署 |
| 全流程质疑 / 核查 | 降低幻觉贯穿全链 |
| Demo | 单个完整任务执行约 25 分钟 |

## 演示 / 媒体

- [完整任务全流程视频](https://video.twimg.com/amplify_video/2092395095723294721/vid/avc1/1380x720/E7Typw-pO03hGMAV.mp4?tag=29) — 25 分钟实跑示例

## 参考链接

- [在线体验](https://www.apodex.ai/)
- [FrontierAgent 仓库](https://github.com/ApodexAI/FrontierAgent)
- [Apodex 1.1 mini 模型集合](https://huggingface.co/collections/apodex/apodex-11)
