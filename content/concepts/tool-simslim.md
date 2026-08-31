---
type: "Tool"
title: "Simslim（低内存 iOS 模拟器瘦身）"
description: "针对 16 GB 内存机器跑 iOS 模拟器的瘦身工具——移动开发时常见的「内存不够」问题的开源缓解方案。"
resource: "https://github.com/MobAI-App/simslim"
tags: [ios, simulator, mobile-dev, memory, optimization]
timestamp: "2026-08-31T16:00:00Z"
---

# Simslim

## 它是什么

[Simslim](https://github.com/MobAI-App/simslim) 是 **MobAI-App** 团队开源的 **iOS 模拟器瘦身工具**，专门解决「**16 GB 内存机器跑 Xcode + iOS 模拟器卡到爆**」的痛点。

核心思路：把模拟器运行时里那些移动开发**用不到的子系统**关掉 / 卸载，腾出内存留给编译与调试。

## 为什么用它 / 适合什么场景

- **低内存 MacBook / MacBook Air**：默认 Xcode 模拟器一开就吞 8 GB+，编译只能等待；
- **CI / 自动化**：流水线里跑模拟器测试时希望最小化资源占用；
- **本地多模拟器调试**：想并行跑多个 iOS 版本时尤为关键。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模拟器瘦身 | 关闭用不到的子系统，腾出内存 |
| 兼容性 | 标准 Xcode 工作流无需变 |
| 开源 | GitHub 公开 |

## 相关概念

（暂无关联项目可链。）

## 参考链接

- 项目链接：<https://github.com/MobAI-App/simslim>