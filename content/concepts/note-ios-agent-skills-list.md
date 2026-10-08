---
type: "Note"
title: "iOS 开发 Agent Skills 五件套清单"
description: "jaimintf 整理的 5 个面向 iOS 开发的 Claude Code / Codex 技能包，覆盖 best practices / app design / animations / performance / SwiftUI，能显著拉高 Agent 写出的 iOS 代码质量。"
tags: "[agent-skills, ios, swiftui, claude-code, codex]"
timestamp: "2026-10-08T23:50:00Z"
---

# iOS 开发 Agent Skills 五件套清单

面向 **iOS / SwiftUI 开发** 的 Claude Code / Codex 技能包，5 个仓库分别覆盖一个领域。把它们装进 Agent 后，编码 Agent 写出的 iOS 代码质量明显拉高。

## 五件套

| 主题 | 仓库 | 用途 |
|------|------|------|
| best practices | <https://github.com/expo/skills> | Expo 维护的工程最佳实践合集 |
| app design | <https://github.com/Appllama/appllama-skills> | iOS 应用设计规范 |
| animations | <https://github.com/emilkowalski/skills> | 动效 / 转场规范（emilkowalski 是 Radix UI / React 动效领域知名作者） |
| performance | <https://github.com/vercel-labs/agent-skills> | Vercel Labs 维护的性能优化技能 |
| SwiftUI | <https://github.com/twostraws/SwiftUI-Agent-Skill> | twostraws（Hacking with Swift）维护的 SwiftUI 技能 |

## 适用场景

- iOS / iPadOS 项目刚启动，要给 Agent 装「行规」
- 已有 SwiftUI 项目，要让 Agent 写出的代码符合社区主流写法
- 团队想统一 Agent 写 iOS 代码的风格

## 配套使用建议

- 这五个互相**正交**：best practices + performance 偏流程层；design / animations / SwiftUI 偏写法层
- 与 `term-ios-agent-skill`（jamiemill 整理的 Expo + SwiftUI 通用 iOS Skill）一类资源互补

## 参考链接

- Expo Skills：<https://github.com/expo/skills>
- Appllama Skills：<https://github.com/Appllama/appllama-skills>
- emilkowalski Skills：<https://github.com/emilkowalski/skills>
- Vercel Labs Agent Skills：<https://github.com/vercel-labs/agent-skills>
- SwiftUI Agent Skill：<https://github.com/twostraws/SwiftUI-Agent-Skill>

## 媒体

视频：<https://video.twimg.com/amplify_video/2107830542813294592/vid/avc1/2170x1466/H5Nrw17H9lLqRowx.mp4?tag=29>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 概念总览
- [Claude Code](./term-claude-code.md) — 主流 Skills 使用场景