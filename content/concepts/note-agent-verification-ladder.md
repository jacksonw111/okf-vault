---
type: "Note"
title: "Agent 自我验证阶梯（SpaceX / Dune 视角）"
description: "把「让 agent 验证自己工作」拆成五级阶梯：跑应用抓 trace → 写 feature map → 把每次失败沉淀成 skill → 把 skill 当 unit test 跑 eval → 把规则硬化（model can forget 的不是规则）。第 5 级被称为 \"Dune\"，是 SpaceX 高薪工程师真正买到的能力。"
tags: "[agent, verification, eval, skill, dune, methodology, note]"
timestamp: "2026-09-24T21:55:00Z"
---

# Agent 自我验证阶梯（SpaceX / Dune 视角）

## 它是什么

来自 SpaceX 一位工程师的 59 分钟 workshop，把「让 agent 验证自己的工作」拆成五级阶梯。最上层被称为 **Dune**——把规则写得 model 也不可能忘记。第 5 级是大多数团队没买到的能力，也是真正放权的起点。

## 五级阶梯

| 阶梯 | 内容 |
|------|------|
| Step 1 | 让 agent 自己跑应用、自己 trace、自己点；人不再当 verifier |
| Step 2 | 给 agent 写一份 feature map：每个屏幕、每个快捷方式、每个 selector，截图就够了 |
| Step 3 | 把每次被抓到的失败沉淀成 skill——「它猜是因为从没打开过代码」 |
| Step 4 | 把 skill 当 unit test 跑：换不同 model 评判，loop 到 10/10 |
| Step 5 | 把规则硬化（make the rules hard）——一条 model 可能忘掉的规则不是规则 |

## 为什么 Step 5 重要

前 4 步很多人都在做：写 skill、写 eval、写 feature map。但这些 skill model 可能在某次上下文里忘掉。**Dune** 这一层是把规则做硬，让模型「不可能」违反——这是大多数工程师还没买到的能力。

## 核心理念

- 规则：一条 model 可以忘掉的规则不是规则
- 验证：人不再是 verifier，而是设计 verifier 的人
- 信任：只有第 5 层铺好，agent 写代码 + 自动验证 + 自动合并的循环才稳

## 原始链接
- 推文原始链接：<https://x.com/distortgeekin/status/2102765685164171451>

## 相关概念
- [OpenMuse](./tool-openmuse.md) — 自托管任务跑完后能翻到每一步留下的记录
- [AegisOps](./tool-aegisops.md) — 把 Agent 在故障处置流水线里设为「只读 + 留痕」