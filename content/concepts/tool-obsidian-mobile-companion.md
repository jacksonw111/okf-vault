---
type: Tool
title: "Obsidian Mobile Companion"
description: "让 Obsidian 知识库存进 GitHub 仓库：Android 手机上离线读笔记 + 安全编辑，PC 端再自动同步回同一个仓库。"
resource: "https://github.com/zhdmm35/obsidian-mobile-companion"
tags: [obsidian, android, mobile, github-sync, offline, knowledge-base]
timestamp: 2026-09-18T06:34:00Z"
---

# Obsidian Mobile Companion

## 它是什么

[zhdmm35/obsidian-mobile-companion](https://github.com/zhdmm35/obsidian-mobile-companion) 是一款 **Obsidian 的 Android 移动伴侣**。它把 Obsidian 知识库存进一个 GitHub 仓库（Vault = GitHub Repo），让用户在 Android 手机上能：

- **离线**读笔记
- **安全**编辑
- 等回到 PC 端，**自动同步**回同一个仓库

它解决的问题：Obsidian 官方移动端体验较弱，且许多人的 Vault 是普通本地文件夹，多设备同步要靠 iCloud / OneDrive / git 自己折腾。这套工具直接以 **GitHub 为单一事实源**。

## 关键能力

| 能力 | 说明 |
|------|------|
| GitHub 即 Vault | 仓库本身是知识库 |
| Android 离线 | 没网时也能读已有笔记 |
| 安全编辑 | 移动端提供受控的编辑界面，避免误改 |
| PC 自动回写 | 回到电脑端同步回同一仓库 |
| 跨设备一致 | 用 Git 做版本控制，conflict 可追溯 |

## 适合什么场景

- 长期用 Obsidian 整理笔记、想要「**手机能看 / 能改 / PC 端自动收**」的用户。
- 把 Vault 放在 GitHub 上、希望移动端不必依赖 iCloud / Dropbox 的开源用户。
- 需要一个明确「单一事实源」的 Obsidian 跨设备方案的人。

## 与相关概念的关系

- [Obsidian](./tool-obsidian.md) — Obsidian 是 PC 端核心，移动伴侣补全跨设备体验。
- [Self-Hosted（自托管）](./term-self-hosted.md) — Vault 落在自己的 GitHub 仓库里，符合自托管 / 自有备份的精神。

## 参考

- 项目链接：<https://github.com/zhdmm35/obsidian-mobile-companion>

![移动端截图](https://pbs.twimg.com/media/HSdmQIKbwAAGqDD.jpg)
