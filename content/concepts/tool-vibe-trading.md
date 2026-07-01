---
type: Tool
title: "Vibe-Trading"
description: "港大 HKUDS 实验室开源的 AI 交易研究平台，底层 29 个 AI Agent 自动分工拉数据 / 写因子 / 编策略 / 跑回测 / 出报告，自然语言一句话即可启动整套量化研究流水线。"
tags: "[trading, quant, ai-agent, hkuds]"
timestamp: "2026-07-01T15:30:00Z"
resource: "https://github.com/HKUDS/Vibe-Trading"
---

# Vibe-Trading

## 它是什么
港大 HKUDS Data Intelligence Lab 开源的 AI 驱动量化交易研究平台，自然语言写策略，全程不碰代码；底层把投委会、量化台、风控委员会、加密交易台等机构职能映射为 29 个互相协作的 AI Agent。

## 为什么用它 / 适合什么场景
- 一句话「回测港股高股息低 PE 策略」就能让 AI 拆解→编码→回测→归因→出报告
- 想把 AI Agent 接进自有投研工作流
- 想在没有团队的情况下快速验证策略想法
- 适合单兵 / 小团队量化研究，不想维护一套机构级投研 IT

## 关键能力
| 能力 | 说明 |
|------|------|
| 自然语言策略 | 说人话，AI 自动拆解→编码→回测→归因→报告 |
| 29 个预设 AI 团队 | 投委会辩论 / 量化台 / 风控委员会 / 加密交易台等机构级分工 |
| Alpha Zoo | 452 个预置因子（qlib158 + alpha101 + gtja191 + Fama-French），alpha compare 一键排 IC/IR |
| 7 大回测引擎 | 蒙特卡洛 / Walk-Forward / Bootstrap 置信区间 |
| 影子账户 | 上传券商交割单，AI 逆向提取交易模式，用自己的数据验证 |
| 多平台导出 | TradingView Pine Script v6 / 通达信 / MT5 MQL5 |
| 刚性风控 | 仓位上限 / 单日最大亏损 / 极端行情熔断 — AI 强制执行 |

## 安装
```bash
pip install vibe-trading-ai
```

## 相关概念
- [a-stock-data](tool-a-stock-data.md) — A 股全栈数据 Skill，是 Vibe-Trading 在 A 股端的底层数据来源
- [global-stock-data](tool-global-stock-data.md) — 美港股全栈数据 Skill，可补 Vibe-Trading 在美港股端的因子与财务数据
- [liangmai-sdk](tool-liangmai-sdk.md) — 良买金融数据 Python SDK，105 个 API，与 Vibe-Trading 共享数据底座
- [AI 托管个人资产的方向](tool-personal-asset-via-claude.md) — AI 全面接管个人财务的讨论，Vibe-Trading 是机构端的最强解

## 原始链接
- [项目仓库](https://github.com/HKUDS/Vibe-Trading)
- [演示视频](https://video.twimg.com/amplify_video/2072189099281453057/vid/avc1/3164x2160/yZQGbbHEepMimRxw.mp4?tag=28)