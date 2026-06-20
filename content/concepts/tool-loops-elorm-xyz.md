---
type: "Tool"
title: "loops.elorm.xyz"
description: "elorm.xyz 维护的「loop engineering」思路集合，收录了几十位大神写代码 / 跑 agent 时常用的「循环套路」（如「写 → 跑 → 看 → 改」、「prompt → 评估 → 改 prompt」），是构建 agent 自迭代工作流时的灵感来源。"
tags: "[ai, agent, loops, automation, prompt-engineering]"
timestamp: "2026-06-20T00:00:00Z"
resource: "https://loops.elorm.xyz/"
---

# loops.elorm.xyz

## 它是什么

[`loops.elorm.xyz`](https://loops.elorm.xyz/) 是 **elorm.xyz** 维护的「**loop engineering**」思路集合——收录了几十位大神在**写代码 / 跑 agent** 时常用的「**循环套路**」。

「Loop」在这里有两层意思：

- **狭义**：写程序时常用的循环结构（while / for / recursion）。
- **广义**：**agent / 自动化工作流里的反馈闭环**——`prompt → 执行 → 评估 → 修正 prompt → 再执行`，直到结果达标。

[li9292 @x 2026-06-20 推文](https://x.com/li9292/status/2067991077211251010) 的原话：「收录了几十个大神的 loop engineering 的思路」。

## 为什么这个资源值得收录

| 痛点 | loops.elorm.xyz 给的视角 |
|------|--------------------------|
| agent 一次跑不到位 | 看大神们怎么设计「评估-修正」闭环 |
| 写自动化脚本卡在「判断何时停下」 | 各种终止条件 / 收敛指标的参考 |
| 调 prompt 凭感觉 | 「prompt 工程」循环化、可观测化 |
| 想了解「Eval-driven development」 | 大神们怎么把循环拆成可复用模块 |

视频演示（li9292 推文附带）：

- <https://video.twimg.com/amplify_video/2067991012178526208/vid/avc1/1336x818/Rn9OM39CK1t8RxL4.mp4?tag=28>

## 与本知识库现有工具的呼应

- 配合 [OKF 生产者协议](./../PRODUCER.md)：「读资料 → 切概念 → 写文件 → 更新索引 → 归档」本身就是一个 **loop**。
- 与 [Claude Code](tool-claude-code.md) 的「skill」理念呼应：每个 skill 就是一个**可复用的 loop 片段**（如 `/improve` = 「审计 → 给改进意见」循环）。
- 与 [mattpocock/skills](tool-mattpocock-skills.md) 的 `/zoom-out` 等 skill 同源——都是「循环型 prompt」的实例化。

## 社区验证 / 二次来源

- [li9292 原推](https://x.com/li9292/status/2067991077211251010) → [Wen_Zw 转载](https://x.com/Wen_Zw/status/2068229318816526823)。

## 相关概念

- [Claude Code](tool-claude-code.md) — 跑这些 loops 的载体
- [mattpocock/skills](tool-mattpocock-skills.md) — 每个 skill 本质上是一个可复用的 loop
- [Agent Skills 是什么](term-agent-skills.md) — loop 思路在 skill 层的体现
- [OKF 生产者协议](./../PRODUCER.md) — 「读资料→切概念→写文件→更新索引→归档」本身就是一个 loop